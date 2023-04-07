# Comparing `tmp/cdk-ecs-service-extensions-2.0.0a98.tar.gz` & `tmp/cdk-ecs-service-extensions-2.0.0a99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "cdk-ecs-service-extensions-2.0.0a98.tar", last modified: Tue Jul 26 00:31:45 2022, max compression
+gzip compressed data, was "cdk-ecs-service-extensions-2.0.0a99.tar", last modified: Wed Jul 27 00:33:56 2022, max compression
```

## Comparing `cdk-ecs-service-extensions-2.0.0a98.tar` & `cdk-ecs-service-extensions-2.0.0a99.tar`

### file list

```diff
@@ -1,22 +1,22 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-26 00:31:45.867015 cdk-ecs-service-extensions-2.0.0a98/
--rw-r--r--   0 runner    (1001) docker     (121)    11358 2022-07-26 00:31:30.000000 cdk-ecs-service-extensions-2.0.0a98/LICENSE
--rw-r--r--   0 runner    (1001) docker     (121)       23 2022-07-26 00:31:30.000000 cdk-ecs-service-extensions-2.0.0a98/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (121)       67 2022-07-26 00:31:30.000000 cdk-ecs-service-extensions-2.0.0a98/NOTICE
--rw-r--r--   0 runner    (1001) docker     (121)    24826 2022-07-26 00:31:45.867015 cdk-ecs-service-extensions-2.0.0a98/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)    23876 2022-07-26 00:31:30.000000 cdk-ecs-service-extensions-2.0.0a98/README.md
--rw-r--r--   0 runner    (1001) docker     (121)      106 2022-07-26 00:31:30.000000 cdk-ecs-service-extensions-2.0.0a98/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (121)       38 2022-07-26 00:31:45.867015 cdk-ecs-service-extensions-2.0.0a98/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)     1789 2022-07-26 00:31:30.000000 cdk-ecs-service-extensions-2.0.0a98/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-26 00:31:45.863015 cdk-ecs-service-extensions-2.0.0a98/src/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-26 00:31:45.867015 cdk-ecs-service-extensions-2.0.0a98/src/cdk_ecs_service_extensions/
--rw-r--r--   0 runner    (1001) docker     (121)   209023 2022-07-26 00:31:30.000000 cdk-ecs-service-extensions-2.0.0a98/src/cdk_ecs_service_extensions/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-26 00:31:45.867015 cdk-ecs-service-extensions-2.0.0a98/src/cdk_ecs_service_extensions/_jsii/
--rw-r--r--   0 runner    (1001) docker     (121)      428 2022-07-26 00:31:30.000000 cdk-ecs-service-extensions-2.0.0a98/src/cdk_ecs_service_extensions/_jsii/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)   163512 2022-07-26 00:31:30.000000 cdk-ecs-service-extensions-2.0.0a98/src/cdk_ecs_service_extensions/_jsii/ecs-service-extensions@2.0.0-alpha.98.jsii.tgz
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-07-26 00:31:30.000000 cdk-ecs-service-extensions-2.0.0a98/src/cdk_ecs_service_extensions/py.typed
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-26 00:31:45.867015 cdk-ecs-service-extensions-2.0.0a98/src/cdk_ecs_service_extensions.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)    24826 2022-07-26 00:31:45.000000 cdk-ecs-service-extensions-2.0.0a98/src/cdk_ecs_service_extensions.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)      545 2022-07-26 00:31:45.000000 cdk-ecs-service-extensions-2.0.0a98/src/cdk_ecs_service_extensions.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-07-26 00:31:45.000000 cdk-ecs-service-extensions-2.0.0a98/src/cdk_ecs_service_extensions.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)       92 2022-07-26 00:31:45.000000 cdk-ecs-service-extensions-2.0.0a98/src/cdk_ecs_service_extensions.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)       27 2022-07-26 00:31:45.000000 cdk-ecs-service-extensions-2.0.0a98/src/cdk_ecs_service_extensions.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-27 00:33:56.124487 cdk-ecs-service-extensions-2.0.0a99/
+-rw-r--r--   0 runner    (1001) docker     (121)    11358 2022-07-27 00:33:42.000000 cdk-ecs-service-extensions-2.0.0a99/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (121)       23 2022-07-27 00:33:42.000000 cdk-ecs-service-extensions-2.0.0a99/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (121)       67 2022-07-27 00:33:42.000000 cdk-ecs-service-extensions-2.0.0a99/NOTICE
+-rw-r--r--   0 runner    (1001) docker     (121)    24826 2022-07-27 00:33:56.124487 cdk-ecs-service-extensions-2.0.0a99/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)    23876 2022-07-27 00:33:42.000000 cdk-ecs-service-extensions-2.0.0a99/README.md
+-rw-r--r--   0 runner    (1001) docker     (121)      106 2022-07-27 00:33:42.000000 cdk-ecs-service-extensions-2.0.0a99/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (121)       38 2022-07-27 00:33:56.124487 cdk-ecs-service-extensions-2.0.0a99/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (121)     1818 2022-07-27 00:33:42.000000 cdk-ecs-service-extensions-2.0.0a99/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-27 00:33:56.124487 cdk-ecs-service-extensions-2.0.0a99/src/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-27 00:33:56.124487 cdk-ecs-service-extensions-2.0.0a99/src/cdk_ecs_service_extensions/
+-rw-r--r--   0 runner    (1001) docker     (121)   230694 2022-07-27 00:33:42.000000 cdk-ecs-service-extensions-2.0.0a99/src/cdk_ecs_service_extensions/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-27 00:33:56.124487 cdk-ecs-service-extensions-2.0.0a99/src/cdk_ecs_service_extensions/_jsii/
+-rw-r--r--   0 runner    (1001) docker     (121)      462 2022-07-27 00:33:42.000000 cdk-ecs-service-extensions-2.0.0a99/src/cdk_ecs_service_extensions/_jsii/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)   163510 2022-07-27 00:33:42.000000 cdk-ecs-service-extensions-2.0.0a99/src/cdk_ecs_service_extensions/_jsii/ecs-service-extensions@2.0.0-alpha.99.jsii.tgz
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-07-27 00:33:42.000000 cdk-ecs-service-extensions-2.0.0a99/src/cdk_ecs_service_extensions/py.typed
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-27 00:33:56.124487 cdk-ecs-service-extensions-2.0.0a99/src/cdk_ecs_service_extensions.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (121)    24826 2022-07-27 00:33:55.000000 cdk-ecs-service-extensions-2.0.0a99/src/cdk_ecs_service_extensions.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)      545 2022-07-27 00:33:56.000000 cdk-ecs-service-extensions-2.0.0a99/src/cdk_ecs_service_extensions.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-07-27 00:33:55.000000 cdk-ecs-service-extensions-2.0.0a99/src/cdk_ecs_service_extensions.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (121)      110 2022-07-27 00:33:55.000000 cdk-ecs-service-extensions-2.0.0a99/src/cdk_ecs_service_extensions.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       27 2022-07-27 00:33:56.000000 cdk-ecs-service-extensions-2.0.0a99/src/cdk_ecs_service_extensions.egg-info/top_level.txt
```

### Comparing `cdk-ecs-service-extensions-2.0.0a98/LICENSE` & `cdk-ecs-service-extensions-2.0.0a99/LICENSE`

 * *Files identical despite different names*

### Comparing `cdk-ecs-service-extensions-2.0.0a98/PKG-INFO` & `cdk-ecs-service-extensions-2.0.0a99/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: cdk-ecs-service-extensions
-Version: 2.0.0a98
+Version: 2.0.0a99
 Summary: @aws-cdk-containers/ecs-service-extensions
 Home-page: https://github.com/cdklabs/cdk-ecs-service-extensions.git
 Author: Amazon Web Services
 License: Apache-2.0
 Project-URL: Source, https://github.com/cdklabs/cdk-ecs-service-extensions.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

### Comparing `cdk-ecs-service-extensions-2.0.0a98/README.md` & `cdk-ecs-service-extensions-2.0.0a99/README.md`

 * *Files identical despite different names*

### Comparing `cdk-ecs-service-extensions-2.0.0a98/setup.py` & `cdk-ecs-service-extensions-2.0.0a99/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import json
 import setuptools
 
 kwargs = json.loads(
     """
 {
     "name": "cdk-ecs-service-extensions",
-    "version": "2.0.0.a98",
+    "version": "2.0.0.a99",
     "description": "@aws-cdk-containers/ecs-service-extensions",
     "license": "Apache-2.0",
     "url": "https://github.com/cdklabs/cdk-ecs-service-extensions.git",
     "long_description_content_type": "text/markdown",
     "author": "Amazon Web Services",
     "bdist_wheel": {
         "universal": true
@@ -22,26 +22,27 @@
     },
     "packages": [
         "cdk_ecs_service_extensions",
         "cdk_ecs_service_extensions._jsii"
     ],
     "package_data": {
         "cdk_ecs_service_extensions._jsii": [
-            "ecs-service-extensions@2.0.0-alpha.98.jsii.tgz"
+            "ecs-service-extensions@2.0.0-alpha.99.jsii.tgz"
         ],
         "cdk_ecs_service_extensions": [
             "py.typed"
         ]
     },
     "python_requires": "~=3.7",
     "install_requires": [
         "aws-cdk-lib>=2.8.0, <3.0.0",
         "constructs>=10.0.5, <11.0.0",
-        "jsii>=1.62.0, <2.0.0",
-        "publication>=0.0.3"
+        "jsii>=1.63.0, <2.0.0",
+        "publication>=0.0.3",
+        "typeguard~=2.13.3"
     ],
     "classifiers": [
         "Intended Audience :: Developers",
         "Operating System :: OS Independent",
         "Programming Language :: JavaScript",
         "Programming Language :: Python :: 3 :: Only",
         "Programming Language :: Python :: 3.7",
```

### Comparing `cdk-ecs-service-extensions-2.0.0a98/src/cdk_ecs_service_extensions/__init__.py` & `cdk-ecs-service-extensions-2.0.0a99/src/cdk_ecs_service_extensions/__init__.py`

 * *Files 13% similar despite different names*

```diff
@@ -578,14 +578,16 @@
 import enum
 import typing
 
 import jsii
 import publication
 import typing_extensions
 
+from typeguard import check_type
+
 from ._jsii import *
 
 import aws_cdk
 import aws_cdk.aws_appmesh
 import aws_cdk.aws_ec2
 import aws_cdk.aws_ecs
 import aws_cdk.aws_iam
@@ -611,14 +613,18 @@
     ) -> None:
         '''
         :param record_name: (experimental) Name of the record to add to the zone and in which to add the task IP addresses to.
         :param zone: (experimental) A DNS Zone to expose task IPs in.
 
         :stability: experimental
         '''
+        if __debug__:
+            type_hints = typing.get_type_hints(AssignPublicIpDnsOptions.__init__)
+            check_type(argname="argument record_name", value=record_name, expected_type=type_hints["record_name"])
+            check_type(argname="argument zone", value=zone, expected_type=type_hints["zone"])
         self._values: typing.Dict[str, typing.Any] = {
             "record_name": record_name,
             "zone": zone,
         }
 
     @builtins.property
     def record_name(self) -> builtins.str:
@@ -670,14 +676,17 @@
         '''
         :param dns: (experimental) Enable publishing task public IPs to a recordset in a Route 53 hosted zone. Note: If you want to change the DNS zone or record name, you will need to remove this extension completely and then re-add it.
 
         :stability: experimental
         '''
         if isinstance(dns, dict):
             dns = AssignPublicIpDnsOptions(**dns)
+        if __debug__:
+            type_hints = typing.get_type_hints(AssignPublicIpExtensionOptions.__init__)
+            check_type(argname="argument dns", value=dns, expected_type=type_hints["dns"])
         self._values: typing.Dict[str, typing.Any] = {}
         if dns is not None:
             self._values["dns"] = dns
 
     @builtins.property
     def dns(self) -> typing.Optional[AssignPublicIpDnsOptions]:
         '''(experimental) Enable publishing task public IPs to a recordset in a Route 53 hosted zone.
@@ -725,14 +734,20 @@
         :param max_task_count: (experimental) The maximum number of tasks when scaling out.
         :param min_task_count: (experimental) The minimum number of tasks when scaling in. Default: - 1
         :param target_cpu_utilization: (experimental) The target value for CPU utilization across all tasks in the service.
         :param target_memory_utilization: (experimental) The target value for memory utilization across all tasks in the service.
 
         :stability: experimental
         '''
+        if __debug__:
+            type_hints = typing.get_type_hints(AutoScalingOptions.__init__)
+            check_type(argname="argument max_task_count", value=max_task_count, expected_type=type_hints["max_task_count"])
+            check_type(argname="argument min_task_count", value=min_task_count, expected_type=type_hints["min_task_count"])
+            check_type(argname="argument target_cpu_utilization", value=target_cpu_utilization, expected_type=type_hints["target_cpu_utilization"])
+            check_type(argname="argument target_memory_utilization", value=target_memory_utilization, expected_type=type_hints["target_memory_utilization"])
         self._values: typing.Dict[str, typing.Any] = {
             "max_task_count": max_task_count,
         }
         if min_task_count is not None:
             self._values["min_task_count"] = min_task_count
         if target_cpu_utilization is not None:
             self._values["target_cpu_utilization"] = target_cpu_utilization
@@ -799,14 +814,17 @@
     def __init__(self, *, local_bind_port: typing.Optional[jsii.Number] = None) -> None:
         '''(experimental) connectToProps will have all the extra parameters which are required for connecting services.
 
         :param local_bind_port: (experimental) localBindPort is the local port that this application should use when calling the upstream service in ECS Consul Mesh Extension Currently, this parameter will only be used in the ECSConsulMeshExtension https://github.com/aws-ia/ecs-consul-mesh-extension.
 
         :stability: experimental
         '''
+        if __debug__:
+            type_hints = typing.get_type_hints(ConnectToProps.__init__)
+            check_type(argname="argument local_bind_port", value=local_bind_port, expected_type=type_hints["local_bind_port"])
         self._values: typing.Dict[str, typing.Any] = {}
         if local_bind_port is not None:
             self._values["local_bind_port"] = local_bind_port
 
     @builtins.property
     def local_bind_port(self) -> typing.Optional[jsii.Number]:
         '''(experimental) localBindPort is the local port that this application should use when calling the upstream service in ECS Consul Mesh Extension Currently, this parameter will only be used in the ECSConsulMeshExtension https://github.com/aws-ia/ecs-consul-mesh-extension.
@@ -858,14 +876,22 @@
         :param memory_mib: (experimental) How much memory in megabytes the container requires.
         :param traffic_port: (experimental) What port the image listen for traffic on.
         :param environment: (experimental) Environment variables to pass into the container. Default: - No environment variables.
         :param log_group: (experimental) The log group into which application container logs should be routed. Default: - A log group is automatically created for you if the ``ECS_SERVICE_EXTENSIONS_ENABLE_DEFAULT_LOG_DRIVER`` feature flag is set.
 
         :stability: experimental
         '''
+        if __debug__:
+            type_hints = typing.get_type_hints(ContainerExtensionProps.__init__)
+            check_type(argname="argument cpu", value=cpu, expected_type=type_hints["cpu"])
+            check_type(argname="argument image", value=image, expected_type=type_hints["image"])
+            check_type(argname="argument memory_mib", value=memory_mib, expected_type=type_hints["memory_mib"])
+            check_type(argname="argument traffic_port", value=traffic_port, expected_type=type_hints["traffic_port"])
+            check_type(argname="argument environment", value=environment, expected_type=type_hints["environment"])
+            check_type(argname="argument log_group", value=log_group, expected_type=type_hints["log_group"])
         self._values: typing.Dict[str, typing.Any] = {
             "cpu": cpu,
             "image": image,
             "memory_mib": memory_mib,
             "traffic_port": traffic_port,
         }
         if environment is not None:
@@ -1123,14 +1149,22 @@
 
         use the ``minTaskCount`` and ``maxTaskCount`` properties of ``autoScaleTaskCount`` in the ``Service`` construct
         to configure the auto scaling target for the service. For more information, please refer
         https://github.com/aws/aws-cdk/blob/master/packages/%40aws-cdk-containers/ecs-service-extensions/README.md#task-auto-scaling .
 
         :stability: deprecated
         '''
+        if __debug__:
+            type_hints = typing.get_type_hints(CpuScalingProps.__init__)
+            check_type(argname="argument initial_task_count", value=initial_task_count, expected_type=type_hints["initial_task_count"])
+            check_type(argname="argument max_task_count", value=max_task_count, expected_type=type_hints["max_task_count"])
+            check_type(argname="argument min_task_count", value=min_task_count, expected_type=type_hints["min_task_count"])
+            check_type(argname="argument scale_in_cooldown", value=scale_in_cooldown, expected_type=type_hints["scale_in_cooldown"])
+            check_type(argname="argument scale_out_cooldown", value=scale_out_cooldown, expected_type=type_hints["scale_out_cooldown"])
+            check_type(argname="argument target_cpu_utilization", value=target_cpu_utilization, expected_type=type_hints["target_cpu_utilization"])
         self._values: typing.Dict[str, typing.Any] = {}
         if initial_task_count is not None:
             self._values["initial_task_count"] = initial_task_count
         if max_task_count is not None:
             self._values["max_task_count"] = max_task_count
         if min_task_count is not None:
             self._values["min_task_count"] = min_task_count
@@ -1233,14 +1267,18 @@
     ) -> None:
         '''
         :param capacity_type: (experimental) The capacity type used by the service's cluster.
         :param cluster: (experimental) The cluster that is providing capacity for this service.
 
         :stability: experimental
         '''
+        if __debug__:
+            type_hints = typing.get_type_hints(EnvironmentAttributes.__init__)
+            check_type(argname="argument capacity_type", value=capacity_type, expected_type=type_hints["capacity_type"])
+            check_type(argname="argument cluster", value=cluster, expected_type=type_hints["cluster"])
         self._values: typing.Dict[str, typing.Any] = {
             "capacity_type": capacity_type,
             "cluster": cluster,
         }
 
     @builtins.property
     def capacity_type(self) -> "EnvironmentCapacityType":
@@ -1315,14 +1353,19 @@
 
         :param capacity_type: (experimental) The type of capacity to use for this environment. Default: - EnvironmentCapacityType.FARGATE
         :param cluster: (experimental) The ECS cluster which provides compute capacity to this service. [disable-awslint:ref-via-interface] Default: - Create a new cluster
         :param vpc: (experimental) The VPC used by the service for networking. Default: - Create a new VPC
 
         :stability: experimental
         '''
+        if __debug__:
+            type_hints = typing.get_type_hints(EnvironmentProps.__init__)
+            check_type(argname="argument capacity_type", value=capacity_type, expected_type=type_hints["capacity_type"])
+            check_type(argname="argument cluster", value=cluster, expected_type=type_hints["cluster"])
+            check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
         self._values: typing.Dict[str, typing.Any] = {}
         if capacity_type is not None:
             self._values["capacity_type"] = capacity_type
         if cluster is not None:
             self._values["cluster"] = cluster
         if vpc is not None:
             self._values["vpc"] = vpc
@@ -1528,14 +1571,18 @@
         '''(experimental) Settings for the hook which mutates the application container to route logs through FireLens.
 
         :param log_group: (experimental) The log group into which logs should be routed.
         :param parent_service: (experimental) The parent service that is being mutated.
 
         :stability: experimental
         '''
+        if __debug__:
+            type_hints = typing.get_type_hints(FirelensProps.__init__)
+            check_type(argname="argument log_group", value=log_group, expected_type=type_hints["log_group"])
+            check_type(argname="argument parent_service", value=parent_service, expected_type=type_hints["parent_service"])
         self._values: typing.Dict[str, typing.Any] = {
             "log_group": log_group,
             "parent_service": parent_service,
         }
 
     @builtins.property
     def log_group(self) -> aws_cdk.aws_logs.LogGroup:
@@ -1581,14 +1628,17 @@
         requests_per_target: typing.Optional[jsii.Number] = None,
     ) -> None:
         '''
         :param requests_per_target: (experimental) The number of ALB requests per target.
 
         :stability: experimental
         '''
+        if __debug__:
+            type_hints = typing.get_type_hints(HttpLoadBalancerProps.__init__)
+            check_type(argname="argument requests_per_target", value=requests_per_target, expected_type=type_hints["requests_per_target"])
         self._values: typing.Dict[str, typing.Any] = {}
         if requests_per_target is not None:
             self._values["requests_per_target"] = requests_per_target
 
     @builtins.property
     def requests_per_target(self) -> typing.Optional[jsii.Number]:
         '''(experimental) The number of ALB requests per target.
@@ -1828,14 +1878,17 @@
     def subscribe(self, extension: "QueueExtension") -> aws_cdk.aws_sqs.IQueue:
         '''(experimental) All classes implementing this interface must also implement the ``subscribe()`` method.
 
         :param extension: -
 
         :stability: experimental
         '''
+        if __debug__:
+            type_hints = typing.get_type_hints(ISubscribable.subscribe)
+            check_type(argname="argument extension", value=extension, expected_type=type_hints["extension"])
         return typing.cast(aws_cdk.aws_sqs.IQueue, jsii.invoke(self, "subscribe", [extension]))
 
 # Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
 typing.cast(typing.Any, ISubscribable).__jsii_proxy_class__ = lambda : _ISubscribableProxy
 
 
 @jsii.implements(IEnvironment)
@@ -1860,14 +1913,18 @@
         :param scope: -
         :param id: -
         :param capacity_type: (experimental) The capacity type used by the service's cluster.
         :param cluster: (experimental) The cluster that is providing capacity for this service.
 
         :stability: experimental
         '''
+        if __debug__:
+            type_hints = typing.get_type_hints(ImportedEnvironment.__init__)
+            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
+            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
         props = EnvironmentAttributes(capacity_type=capacity_type, cluster=cluster)
 
         jsii.create(self.__class__, self, [scope, id, props])
 
     @jsii.member(jsii_name="addDefaultCloudMapNamespace")
     def add_default_cloud_map_namespace(
         self,
@@ -1936,14 +1993,17 @@
     def __init__(self, *, topic: aws_cdk.aws_sns.ITopic) -> None:
         '''(experimental) The settings for the ``InjectableTopic`` class.
 
         :param topic: (experimental) The SNS Topic to publish events to.
 
         :stability: experimental
         '''
+        if __debug__:
+            type_hints = typing.get_type_hints(InjectableTopicProps.__init__)
+            check_type(argname="argument topic", value=topic, expected_type=type_hints["topic"])
         self._values: typing.Dict[str, typing.Any] = {
             "topic": topic,
         }
 
     @builtins.property
     def topic(self) -> aws_cdk.aws_sns.ITopic:
         '''(experimental) The SNS Topic to publish events to.
@@ -1975,14 +2035,17 @@
     def __init__(self, *, injectables: typing.Sequence[IInjectable]) -> None:
         '''(experimental) The settings for the Injecter extension.
 
         :param injectables: (experimental) The list of injectable resources for this service.
 
         :stability: experimental
         '''
+        if __debug__:
+            type_hints = typing.get_type_hints(InjecterExtensionProps.__init__)
+            check_type(argname="argument injectables", value=injectables, expected_type=type_hints["injectables"])
         self._values: typing.Dict[str, typing.Any] = {
             "injectables": injectables,
         }
 
     @builtins.property
     def injectables(self) -> typing.List[IInjectable]:
         '''(experimental) The list of injectable resources for this service.
@@ -2020,14 +2083,18 @@
         '''(experimental) The settings for the App Mesh extension.
 
         :param mesh: (experimental) The service mesh into which to register the service.
         :param protocol: (experimental) The protocol of the service. Valid values are Protocol.HTTP, Protocol.HTTP2, Protocol.TCP, Protocol.GRPC Default: - Protocol.HTTP
 
         :stability: experimental
         '''
+        if __debug__:
+            type_hints = typing.get_type_hints(MeshProps.__init__)
+            check_type(argname="argument mesh", value=mesh, expected_type=type_hints["mesh"])
+            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
         self._values: typing.Dict[str, typing.Any] = {
             "mesh": mesh,
         }
         if protocol is not None:
             self._values["protocol"] = protocol
 
     @builtins.property
@@ -2108,14 +2175,18 @@
         '''(experimental) Options for configuring SQS Queue auto scaling.
 
         :param acceptable_latency: (experimental) Acceptable amount of time a message can sit in the queue (including the time required to process it).
         :param message_processing_time: (experimental) Average amount of time for processing a single message in the queue.
 
         :stability: experimental
         '''
+        if __debug__:
+            type_hints = typing.get_type_hints(QueueAutoScalingOptions.__init__)
+            check_type(argname="argument acceptable_latency", value=acceptable_latency, expected_type=type_hints["acceptable_latency"])
+            check_type(argname="argument message_processing_time", value=message_processing_time, expected_type=type_hints["message_processing_time"])
         self._values: typing.Dict[str, typing.Any] = {
             "acceptable_latency": acceptable_latency,
             "message_processing_time": message_processing_time,
         }
 
     @builtins.property
     def acceptable_latency(self) -> aws_cdk.Duration:
@@ -2172,14 +2243,19 @@
         :param scale_on_latency: (experimental) The user-provided queue delay fields to configure auto scaling for the default queue. Default: none
         :param subscriptions: (experimental) The list of subscriptions for this service. Default: none
 
         :stability: experimental
         '''
         if isinstance(scale_on_latency, dict):
             scale_on_latency = QueueAutoScalingOptions(**scale_on_latency)
+        if __debug__:
+            type_hints = typing.get_type_hints(QueueExtensionProps.__init__)
+            check_type(argname="argument events_queue", value=events_queue, expected_type=type_hints["events_queue"])
+            check_type(argname="argument scale_on_latency", value=scale_on_latency, expected_type=type_hints["scale_on_latency"])
+            check_type(argname="argument subscriptions", value=subscriptions, expected_type=type_hints["subscriptions"])
         self._values: typing.Dict[str, typing.Any] = {}
         if events_queue is not None:
             self._values["events_queue"] = events_queue
         if scale_on_latency is not None:
             self._values["scale_on_latency"] = scale_on_latency
         if subscriptions is not None:
             self._values["subscriptions"] = subscriptions
@@ -2263,14 +2339,18 @@
         :param service_description: (experimental) The ServiceDescription used to build the service.
         :param auto_scale_task_count: (experimental) The options for configuring the auto scaling target. Default: none
         :param desired_count: (experimental) The desired number of instantiations of the task definition to keep running on the service. Default: - When creating the service, default is 1; when updating the service, default uses the current task number.
         :param task_role: (experimental) The name of the IAM role that grants containers in the task permission to call AWS APIs on your behalf. Default: - A task role is automatically created for you.
 
         :stability: experimental
         '''
+        if __debug__:
+            type_hints = typing.get_type_hints(Service.__init__)
+            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
+            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
         props = ServiceProps(
             environment=environment,
             service_description=service_description,
             auto_scale_task_count=auto_scale_task_count,
             desired_count=desired_count,
             task_role=task_role,
         )
@@ -2286,14 +2366,18 @@
         URL, or App Mesh can add its DNS name for the service.
 
         :param url_name: - The identifier name for this URL.
         :param url: - The URL itself.
 
         :stability: experimental
         '''
+        if __debug__:
+            type_hints = typing.get_type_hints(Service.add_url)
+            check_type(argname="argument url_name", value=url_name, expected_type=type_hints["url_name"])
+            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
         return typing.cast(None, jsii.invoke(self, "addURL", [url_name, url]))
 
     @jsii.member(jsii_name="connectTo")
     def connect_to(
         self,
         service: "Service",
         *,
@@ -2302,14 +2386,17 @@
         '''(experimental) Tell extensions from one service to connect to extensions from another sevice if they have implemented a hook for it.
 
         :param service: -
         :param local_bind_port: (experimental) localBindPort is the local port that this application should use when calling the upstream service in ECS Consul Mesh Extension Currently, this parameter will only be used in the ECSConsulMeshExtension https://github.com/aws-ia/ecs-consul-mesh-extension.
 
         :stability: experimental
         '''
+        if __debug__:
+            type_hints = typing.get_type_hints(Service.connect_to)
+            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
         connect_to_props = ConnectToProps(local_bind_port=local_bind_port)
 
         return typing.cast(None, jsii.invoke(self, "connectTo", [service, connect_to_props]))
 
     @jsii.member(jsii_name="enableAutoScalingPolicy")
     def enable_auto_scaling_policy(self) -> None:
         '''(experimental) This helper method is used to set the ``autoScalingPoliciesEnabled`` attribute whenever an auto scaling policy is configured for the service.
@@ -2325,14 +2412,17 @@
         The URL must have previously been
         stored by one of the URL providing extensions.
 
         :param url_name: - The URL to look up.
 
         :stability: experimental
         '''
+        if __debug__:
+            type_hints = typing.get_type_hints(Service.get_url)
+            check_type(argname="argument url_name", value=url_name, expected_type=type_hints["url_name"])
         return typing.cast(builtins.str, jsii.invoke(self, "getURL", [url_name]))
 
     @builtins.property # type: ignore[misc]
     @jsii.member(jsii_name="capacityType")
     def capacity_type(self) -> EnvironmentCapacityType:
         '''(experimental) The capacity type that this service will use.
 
@@ -2410,14 +2500,17 @@
         return typing.cast(typing.Union[aws_cdk.aws_ecs.Ec2Service, aws_cdk.aws_ecs.FargateService], jsii.get(self, "ecsService"))
 
     @ecs_service.setter
     def ecs_service(
         self,
         value: typing.Union[aws_cdk.aws_ecs.Ec2Service, aws_cdk.aws_ecs.FargateService],
     ) -> None:
+        if __debug__:
+            type_hints = typing.get_type_hints(getattr(Service, "ecs_service").fset)
+            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
         jsii.set(self, "ecsService", value)
 
     @builtins.property # type: ignore[misc]
     @jsii.member(jsii_name="taskDefinition")
     def _task_definition(self) -> aws_cdk.aws_ecs.TaskDefinition:
         '''(experimental) The generated task definition for this service.
 
@@ -2426,14 +2519,17 @@
 
         :stability: experimental
         '''
         return typing.cast(aws_cdk.aws_ecs.TaskDefinition, jsii.get(self, "taskDefinition"))
 
     @_task_definition.setter
     def _task_definition(self, value: aws_cdk.aws_ecs.TaskDefinition) -> None:
+        if __debug__:
+            type_hints = typing.get_type_hints(getattr(Service, "_task_definition").fset)
+            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
         jsii.set(self, "taskDefinition", value)
 
 
 @jsii.data_type(
     jsii_type="@aws-cdk-containers/ecs-service-extensions.ServiceBuild",
     jsii_struct_bases=[],
     name_mapping={
@@ -2475,14 +2571,24 @@
         :param max_healthy_percent: (experimental) Maximum percentage of tasks that can be launched. Default: - 200
         :param min_healthy_percent: (experimental) Minimum healthy task percentage. Default: - 100
 
         :stability: experimental
         '''
         if isinstance(cloud_map_options, dict):
             cloud_map_options = aws_cdk.aws_ecs.CloudMapOptions(**cloud_map_options)
+        if __debug__:
+            type_hints = typing.get_type_hints(ServiceBuild.__init__)
+            check_type(argname="argument cluster", value=cluster, expected_type=type_hints["cluster"])
+            check_type(argname="argument task_definition", value=task_definition, expected_type=type_hints["task_definition"])
+            check_type(argname="argument assign_public_ip", value=assign_public_ip, expected_type=type_hints["assign_public_ip"])
+            check_type(argname="argument cloud_map_options", value=cloud_map_options, expected_type=type_hints["cloud_map_options"])
+            check_type(argname="argument desired_count", value=desired_count, expected_type=type_hints["desired_count"])
+            check_type(argname="argument health_check_grace_period", value=health_check_grace_period, expected_type=type_hints["health_check_grace_period"])
+            check_type(argname="argument max_healthy_percent", value=max_healthy_percent, expected_type=type_hints["max_healthy_percent"])
+            check_type(argname="argument min_healthy_percent", value=min_healthy_percent, expected_type=type_hints["min_healthy_percent"])
         self._values: typing.Dict[str, typing.Any] = {
             "cluster": cluster,
             "task_definition": task_definition,
         }
         if assign_public_ip is not None:
             self._values["assign_public_ip"] = assign_public_ip
         if cloud_map_options is not None:
@@ -2625,27 +2731,33 @@
         The extensions mutate a service
         to add resources to or configure properties for the service.
 
         :param extension: - The extension that you wish to add.
 
         :stability: experimental
         '''
+        if __debug__:
+            type_hints = typing.get_type_hints(ServiceDescription.add)
+            check_type(argname="argument extension", value=extension, expected_type=type_hints["extension"])
         return typing.cast("ServiceDescription", jsii.invoke(self, "add", [extension]))
 
     @jsii.member(jsii_name="get")
     def get(self, name: builtins.str) -> "ServiceExtension":
         '''(experimental) Get the extension with a specific name.
 
         This is generally used by
         extensions in order to discover each other.
 
         :param name: -
 
         :stability: experimental
         '''
+        if __debug__:
+            type_hints = typing.get_type_hints(ServiceDescription.get)
+            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
         return typing.cast("ServiceExtension", jsii.invoke(self, "get", [name]))
 
     @builtins.property # type: ignore[misc]
     @jsii.member(jsii_name="extensions")
     def extensions(self) -> typing.Mapping[builtins.str, "ServiceExtension"]:
         '''(experimental) The list of extensions that have been registered to run when preparing this service.
 
@@ -2654,14 +2766,17 @@
         return typing.cast(typing.Mapping[builtins.str, "ServiceExtension"], jsii.get(self, "extensions"))
 
     @extensions.setter
     def extensions(
         self,
         value: typing.Mapping[builtins.str, "ServiceExtension"],
     ) -> None:
+        if __debug__:
+            type_hints = typing.get_type_hints(getattr(ServiceDescription, "extensions").fset)
+            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
         jsii.set(self, "extensions", value)
 
 
 class ServiceExtension(
     metaclass=jsii.JSIIAbstractClass,
     jsii_type="@aws-cdk-containers/ecs-service-extensions.ServiceExtension",
 ):
@@ -2676,14 +2791,17 @@
 
     def __init__(self, name: builtins.str) -> None:
         '''
         :param name: -
 
         :stability: experimental
         '''
+        if __debug__:
+            type_hints = typing.get_type_hints(ServiceExtension.__init__)
+            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
         jsii.create(self.__class__, self, [name])
 
     @jsii.member(jsii_name="addContainerMutatingHook")
     def add_container_mutating_hook(self, hook: ContainerMutatingHook) -> None:
         '''(experimental) This hook allows another service extension to register a mutating hook for changing the primary container of this extension.
 
         This is primarily used
@@ -2691,14 +2809,17 @@
         be able to modify the settings of the application container to
         route logs through Firelens.
 
         :param hook: -
 
         :stability: experimental
         '''
+        if __debug__:
+            type_hints = typing.get_type_hints(ServiceExtension.add_container_mutating_hook)
+            check_type(argname="argument hook", value=hook, expected_type=type_hints["hook"])
         return typing.cast(None, jsii.invoke(self, "addContainerMutatingHook", [hook]))
 
     @jsii.member(jsii_name="addHooks")
     def add_hooks(self) -> None:
         '''(experimental) A hook that allows the extension to add hooks to other extensions that are registered.
 
         :stability: experimental
@@ -2719,14 +2840,17 @@
         proxy for another service.
 
         :param service: - The other service to connect to.
         :param local_bind_port: (experimental) localBindPort is the local port that this application should use when calling the upstream service in ECS Consul Mesh Extension Currently, this parameter will only be used in the ECSConsulMeshExtension https://github.com/aws-ia/ecs-consul-mesh-extension.
 
         :stability: experimental
         '''
+        if __debug__:
+            type_hints = typing.get_type_hints(ServiceExtension.connect_to_service)
+            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
         connect_to_props = ConnectToProps(local_bind_port=local_bind_port)
 
         return typing.cast(None, jsii.invoke(self, "connectToService", [service, connect_to_props]))
 
     @jsii.member(jsii_name="modifyServiceProps")
     def modify_service_props(
         self,
@@ -2836,14 +2960,18 @@
         '''(experimental) A hook that is called for each extension ahead of time to allow for any initial setup, such as creating resources in advance.
 
         :param parent: - The parent service which this extension has been added to.
         :param scope: - The scope that this extension should create resources in.
 
         :stability: experimental
         '''
+        if __debug__:
+            type_hints = typing.get_type_hints(ServiceExtension.prehook)
+            check_type(argname="argument parent", value=parent, expected_type=type_hints["parent"])
+            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
         return typing.cast(None, jsii.invoke(self, "prehook", [parent, scope]))
 
     @jsii.member(jsii_name="resolveContainerDependencies")
     def resolve_container_dependencies(self) -> None:
         '''(experimental) Once all containers are added to the task definition, this hook is called for each extension to give it a chance to resolve its dependency graph so that its container starts in the right order based on the other extensions that were enabled.
 
         :stability: experimental
@@ -2860,27 +2988,33 @@
         It is generally used to
         create any final resources which might depend on the service itself.
 
         :param service: - The generated service.
 
         :stability: experimental
         '''
+        if __debug__:
+            type_hints = typing.get_type_hints(ServiceExtension.use_service)
+            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
         return typing.cast(None, jsii.invoke(self, "useService", [service]))
 
     @jsii.member(jsii_name="useTaskDefinition")
     def use_task_definition(
         self,
         task_definition: aws_cdk.aws_ecs.TaskDefinition,
     ) -> None:
         '''(experimental) Once the task definition is created, this hook is called for each extension to give it a chance to add containers to the task definition, change the task definition's role to add permissions, etc.
 
         :param task_definition: - The created task definition to add containers to.
 
         :stability: experimental
         '''
+        if __debug__:
+            type_hints = typing.get_type_hints(ServiceExtension.use_task_definition)
+            check_type(argname="argument task_definition", value=task_definition, expected_type=type_hints["task_definition"])
         return typing.cast(None, jsii.invoke(self, "useTaskDefinition", [task_definition]))
 
     @builtins.property # type: ignore[misc]
     @jsii.member(jsii_name="containerMutatingHooks")
     def _container_mutating_hooks(self) -> typing.List[ContainerMutatingHook]:
         '''
         :stability: experimental
@@ -2888,27 +3022,33 @@
         return typing.cast(typing.List[ContainerMutatingHook], jsii.get(self, "containerMutatingHooks"))
 
     @_container_mutating_hooks.setter
     def _container_mutating_hooks(
         self,
         value: typing.List[ContainerMutatingHook],
     ) -> None:
+        if __debug__:
+            type_hints = typing.get_type_hints(getattr(ServiceExtension, "_container_mutating_hooks").fset)
+            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
         jsii.set(self, "containerMutatingHooks", value)
 
     @builtins.property # type: ignore[misc]
     @jsii.member(jsii_name="name")
     def name(self) -> builtins.str:
         '''(experimental) The name of the extension.
 
         :stability: experimental
         '''
         return typing.cast(builtins.str, jsii.get(self, "name"))
 
     @name.setter
     def name(self, value: builtins.str) -> None:
+        if __debug__:
+            type_hints = typing.get_type_hints(getattr(ServiceExtension, "name").fset)
+            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
         jsii.set(self, "name", value)
 
     @builtins.property # type: ignore[misc]
     @jsii.member(jsii_name="parentService")
     def _parent_service(self) -> Service:
         '''(experimental) The service which this extension is being added to.
 
@@ -2918,26 +3058,32 @@
 
         :stability: experimental
         '''
         return typing.cast(Service, jsii.get(self, "parentService"))
 
     @_parent_service.setter
     def _parent_service(self, value: Service) -> None:
+        if __debug__:
+            type_hints = typing.get_type_hints(getattr(ServiceExtension, "_parent_service").fset)
+            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
         jsii.set(self, "parentService", value)
 
     @builtins.property # type: ignore[misc]
     @jsii.member(jsii_name="scope")
     def _scope(self) -> constructs.Construct:
         '''
         :stability: experimental
         '''
         return typing.cast(constructs.Construct, jsii.get(self, "scope"))
 
     @_scope.setter
     def _scope(self, value: constructs.Construct) -> None:
+        if __debug__:
+            type_hints = typing.get_type_hints(getattr(ServiceExtension, "_scope").fset)
+            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
         jsii.set(self, "scope", value)
 
     @builtins.property # type: ignore[misc]
     @jsii.member(jsii_name="container")
     def container(self) -> typing.Optional[aws_cdk.aws_ecs.ContainerDefinition]:
         '''(experimental) The container for this extension.
 
@@ -2951,14 +3097,17 @@
         return typing.cast(typing.Optional[aws_cdk.aws_ecs.ContainerDefinition], jsii.get(self, "container"))
 
     @container.setter
     def container(
         self,
         value: typing.Optional[aws_cdk.aws_ecs.ContainerDefinition],
     ) -> None:
+        if __debug__:
+            type_hints = typing.get_type_hints(getattr(ServiceExtension, "container").fset)
+            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
         jsii.set(self, "container", value)
 
 
 class _ServiceExtensionProxy(ServiceExtension):
     pass
 
 # Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
@@ -2994,14 +3143,21 @@
         :param desired_count: (experimental) The desired number of instantiations of the task definition to keep running on the service. Default: - When creating the service, default is 1; when updating the service, default uses the current task number.
         :param task_role: (experimental) The name of the IAM role that grants containers in the task permission to call AWS APIs on your behalf. Default: - A task role is automatically created for you.
 
         :stability: experimental
         '''
         if isinstance(auto_scale_task_count, dict):
             auto_scale_task_count = AutoScalingOptions(**auto_scale_task_count)
+        if __debug__:
+            type_hints = typing.get_type_hints(ServiceProps.__init__)
+            check_type(argname="argument environment", value=environment, expected_type=type_hints["environment"])
+            check_type(argname="argument service_description", value=service_description, expected_type=type_hints["service_description"])
+            check_type(argname="argument auto_scale_task_count", value=auto_scale_task_count, expected_type=type_hints["auto_scale_task_count"])
+            check_type(argname="argument desired_count", value=desired_count, expected_type=type_hints["desired_count"])
+            check_type(argname="argument task_role", value=task_role, expected_type=type_hints["task_role"])
         self._values: typing.Dict[str, typing.Any] = {
             "environment": environment,
             "service_description": service_description,
         }
         if auto_scale_task_count is not None:
             self._values["auto_scale_task_count"] = auto_scale_task_count
         if desired_count is not None:
@@ -3094,14 +3250,18 @@
         :param queue: (experimental) The user-provided queue to subscribe to the given topic.
         :param scale_on_latency: (experimental) The user-provided queue delay fields to configure auto scaling for the topic-specific queue. Default: none
 
         :stability: experimental
         '''
         if isinstance(scale_on_latency, dict):
             scale_on_latency = QueueAutoScalingOptions(**scale_on_latency)
+        if __debug__:
+            type_hints = typing.get_type_hints(SubscriptionQueue.__init__)
+            check_type(argname="argument queue", value=queue, expected_type=type_hints["queue"])
+            check_type(argname="argument scale_on_latency", value=scale_on_latency, expected_type=type_hints["scale_on_latency"])
         self._values: typing.Dict[str, typing.Any] = {
             "queue": queue,
         }
         if scale_on_latency is not None:
             self._values["scale_on_latency"] = scale_on_latency
 
     @builtins.property
@@ -3176,14 +3336,17 @@
 
         :param extension: ``QueueExtension`` added to the service.
 
         :return: the queue subscribed to the given topic
 
         :stability: experimental
         '''
+        if __debug__:
+            type_hints = typing.get_type_hints(TopicSubscription.subscribe)
+            check_type(argname="argument extension", value=extension, expected_type=type_hints["extension"])
         return typing.cast(aws_cdk.aws_sqs.IQueue, jsii.invoke(self, "subscribe", [extension]))
 
     @builtins.property # type: ignore[misc]
     @jsii.member(jsii_name="topic")
     def topic(self) -> aws_cdk.aws_sns.ITopic:
         '''
         :stability: experimental
@@ -3238,14 +3401,19 @@
         :param queue: (deprecated) The user-provided queue to subscribe to the given topic. Default: none
         :param topic_subscription_queue: (experimental) The object representing topic-specific queue and corresponding queue delay fields to configure auto scaling. If not provided, the default ``eventsQueue`` will subscribe to the given topic. Default: none
 
         :stability: experimental
         '''
         if isinstance(topic_subscription_queue, dict):
             topic_subscription_queue = SubscriptionQueue(**topic_subscription_queue)
+        if __debug__:
+            type_hints = typing.get_type_hints(TopicSubscriptionProps.__init__)
+            check_type(argname="argument topic", value=topic, expected_type=type_hints["topic"])
+            check_type(argname="argument queue", value=queue, expected_type=type_hints["queue"])
+            check_type(argname="argument topic_subscription_queue", value=topic_subscription_queue, expected_type=type_hints["topic_subscription_queue"])
         self._values: typing.Dict[str, typing.Any] = {
             "topic": topic,
         }
         if queue is not None:
             self._values["queue"] = queue
         if topic_subscription_queue is not None:
             self._values["topic_subscription_queue"] = topic_subscription_queue
@@ -3319,14 +3487,18 @@
         '''(experimental) A hook that is called for each extension ahead of time to allow for any initial setup, such as creating resources in advance.
 
         :param service: -
         :param scope: -
 
         :stability: experimental
         '''
+        if __debug__:
+            type_hints = typing.get_type_hints(XRayExtension.prehook)
+            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
+            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
         return typing.cast(None, jsii.invoke(self, "prehook", [service, scope]))
 
     @jsii.member(jsii_name="resolveContainerDependencies")
     def resolve_container_dependencies(self) -> None:
         '''(experimental) Once all containers are added to the task definition, this hook is called for each extension to give it a chance to resolve its dependency graph so that its container starts in the right order based on the other extensions that were enabled.
 
         :stability: experimental
@@ -3340,14 +3512,17 @@
     ) -> None:
         '''(experimental) Once the task definition is created, this hook is called for each extension to give it a chance to add containers to the task definition, change the task definition's role to add permissions, etc.
 
         :param task_definition: -
 
         :stability: experimental
         '''
+        if __debug__:
+            type_hints = typing.get_type_hints(XRayExtension.use_task_definition)
+            check_type(argname="argument task_definition", value=task_definition, expected_type=type_hints["task_definition"])
         return typing.cast(None, jsii.invoke(self, "useTaskDefinition", [task_definition]))
 
 
 class AppMeshExtension(
     ServiceExtension,
     metaclass=jsii.JSIIMeta,
     jsii_type="@aws-cdk-containers/ecs-service-extensions.AppMeshExtension",
@@ -3392,14 +3567,17 @@
         proxy for another service.
 
         :param other_service: -
         :param local_bind_port: (experimental) localBindPort is the local port that this application should use when calling the upstream service in ECS Consul Mesh Extension Currently, this parameter will only be used in the ECSConsulMeshExtension https://github.com/aws-ia/ecs-consul-mesh-extension.
 
         :stability: experimental
         '''
+        if __debug__:
+            type_hints = typing.get_type_hints(AppMeshExtension.connect_to_service)
+            check_type(argname="argument other_service", value=other_service, expected_type=type_hints["other_service"])
         _connect_to_props = ConnectToProps(local_bind_port=local_bind_port)
 
         return typing.cast(None, jsii.invoke(self, "connectToService", [other_service, _connect_to_props]))
 
     @jsii.member(jsii_name="modifyServiceProps")
     def modify_service_props(
         self,
@@ -3509,14 +3687,18 @@
         '''(experimental) A hook that is called for each extension ahead of time to allow for any initial setup, such as creating resources in advance.
 
         :param service: -
         :param scope: -
 
         :stability: experimental
         '''
+        if __debug__:
+            type_hints = typing.get_type_hints(AppMeshExtension.prehook)
+            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
+            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
         return typing.cast(None, jsii.invoke(self, "prehook", [service, scope]))
 
     @jsii.member(jsii_name="useService")
     def use_service(
         self,
         service: typing.Union[aws_cdk.aws_ecs.Ec2Service, aws_cdk.aws_ecs.FargateService],
     ) -> None:
@@ -3525,27 +3707,33 @@
         It is generally used to
         create any final resources which might depend on the service itself.
 
         :param service: -
 
         :stability: experimental
         '''
+        if __debug__:
+            type_hints = typing.get_type_hints(AppMeshExtension.use_service)
+            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
         return typing.cast(None, jsii.invoke(self, "useService", [service]))
 
     @jsii.member(jsii_name="useTaskDefinition")
     def use_task_definition(
         self,
         task_definition: aws_cdk.aws_ecs.TaskDefinition,
     ) -> None:
         '''(experimental) Once the task definition is created, this hook is called for each extension to give it a chance to add containers to the task definition, change the task definition's role to add permissions, etc.
 
         :param task_definition: -
 
         :stability: experimental
         '''
+        if __debug__:
+            type_hints = typing.get_type_hints(AppMeshExtension.use_task_definition)
+            check_type(argname="argument task_definition", value=task_definition, expected_type=type_hints["task_definition"])
         return typing.cast(None, jsii.invoke(self, "useTaskDefinition", [task_definition]))
 
     @builtins.property # type: ignore[misc]
     @jsii.member(jsii_name="protocol")
     def protocol(self) -> Protocol:
         '''(experimental) The protocol used for AppMesh routing.
 
@@ -3561,50 +3749,62 @@
         '''
         :stability: experimental
         '''
         return typing.cast(aws_cdk.aws_appmesh.Route, jsii.get(self, "route"))
 
     @_route.setter
     def _route(self, value: aws_cdk.aws_appmesh.Route) -> None:
+        if __debug__:
+            type_hints = typing.get_type_hints(getattr(AppMeshExtension, "_route").fset)
+            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
         jsii.set(self, "route", value)
 
     @builtins.property # type: ignore[misc]
     @jsii.member(jsii_name="virtualNode")
     def _virtual_node(self) -> aws_cdk.aws_appmesh.VirtualNode:
         '''
         :stability: experimental
         '''
         return typing.cast(aws_cdk.aws_appmesh.VirtualNode, jsii.get(self, "virtualNode"))
 
     @_virtual_node.setter
     def _virtual_node(self, value: aws_cdk.aws_appmesh.VirtualNode) -> None:
+        if __debug__:
+            type_hints = typing.get_type_hints(getattr(AppMeshExtension, "_virtual_node").fset)
+            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
         jsii.set(self, "virtualNode", value)
 
     @builtins.property # type: ignore[misc]
     @jsii.member(jsii_name="virtualRouter")
     def _virtual_router(self) -> aws_cdk.aws_appmesh.VirtualRouter:
         '''
         :stability: experimental
         '''
         return typing.cast(aws_cdk.aws_appmesh.VirtualRouter, jsii.get(self, "virtualRouter"))
 
     @_virtual_router.setter
     def _virtual_router(self, value: aws_cdk.aws_appmesh.VirtualRouter) -> None:
+        if __debug__:
+            type_hints = typing.get_type_hints(getattr(AppMeshExtension, "_virtual_router").fset)
+            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
         jsii.set(self, "virtualRouter", value)
 
     @builtins.property # type: ignore[misc]
     @jsii.member(jsii_name="virtualService")
     def _virtual_service(self) -> aws_cdk.aws_appmesh.VirtualService:
         '''
         :stability: experimental
         '''
         return typing.cast(aws_cdk.aws_appmesh.VirtualService, jsii.get(self, "virtualService"))
 
     @_virtual_service.setter
     def _virtual_service(self, value: aws_cdk.aws_appmesh.VirtualService) -> None:
+        if __debug__:
+            type_hints = typing.get_type_hints(getattr(AppMeshExtension, "_virtual_service").fset)
+            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
         jsii.set(self, "virtualService", value)
 
 
 class AssignPublicIpExtension(
     ServiceExtension,
     metaclass=jsii.JSIIMeta,
     jsii_type="@aws-cdk-containers/ecs-service-extensions.AssignPublicIpExtension",
@@ -3675,14 +3875,18 @@
         '''(experimental) A hook that is called for each extension ahead of time to allow for any initial setup, such as creating resources in advance.
 
         :param service: -
         :param _scope: -
 
         :stability: experimental
         '''
+        if __debug__:
+            type_hints = typing.get_type_hints(AssignPublicIpExtension.prehook)
+            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
+            check_type(argname="argument _scope", value=_scope, expected_type=type_hints["_scope"])
         return typing.cast(None, jsii.invoke(self, "prehook", [service, _scope]))
 
     @jsii.member(jsii_name="useService")
     def use_service(
         self,
         service: typing.Union[aws_cdk.aws_ecs.Ec2Service, aws_cdk.aws_ecs.FargateService],
     ) -> None:
@@ -3691,26 +3895,32 @@
         It is generally used to
         create any final resources which might depend on the service itself.
 
         :param service: -
 
         :stability: experimental
         '''
+        if __debug__:
+            type_hints = typing.get_type_hints(AssignPublicIpExtension.use_service)
+            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
         return typing.cast(None, jsii.invoke(self, "useService", [service]))
 
     @builtins.property # type: ignore[misc]
     @jsii.member(jsii_name="dns")
     def dns(self) -> typing.Optional[AssignPublicIpDnsOptions]:
         '''
         :stability: experimental
         '''
         return typing.cast(typing.Optional[AssignPublicIpDnsOptions], jsii.get(self, "dns"))
 
     @dns.setter
     def dns(self, value: typing.Optional[AssignPublicIpDnsOptions]) -> None:
+        if __debug__:
+            type_hints = typing.get_type_hints(getattr(AssignPublicIpExtension, "dns").fset)
+            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
         jsii.set(self, "dns", value)
 
 
 class CloudwatchAgentExtension(
     ServiceExtension,
     metaclass=jsii.JSIIMeta,
     jsii_type="@aws-cdk-containers/ecs-service-extensions.CloudwatchAgentExtension",
@@ -3731,14 +3941,18 @@
         '''(experimental) A hook that is called for each extension ahead of time to allow for any initial setup, such as creating resources in advance.
 
         :param service: -
         :param scope: -
 
         :stability: experimental
         '''
+        if __debug__:
+            type_hints = typing.get_type_hints(CloudwatchAgentExtension.prehook)
+            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
+            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
         return typing.cast(None, jsii.invoke(self, "prehook", [service, scope]))
 
     @jsii.member(jsii_name="resolveContainerDependencies")
     def resolve_container_dependencies(self) -> None:
         '''(experimental) Once all containers are added to the task definition, this hook is called for each extension to give it a chance to resolve its dependency graph so that its container starts in the right order based on the other extensions that were enabled.
 
         :stability: experimental
@@ -3752,14 +3966,17 @@
     ) -> None:
         '''(experimental) Once the task definition is created, this hook is called for each extension to give it a chance to add containers to the task definition, change the task definition's role to add permissions, etc.
 
         :param task_definition: -
 
         :stability: experimental
         '''
+        if __debug__:
+            type_hints = typing.get_type_hints(CloudwatchAgentExtension.use_task_definition)
+            check_type(argname="argument task_definition", value=task_definition, expected_type=type_hints["task_definition"])
         return typing.cast(None, jsii.invoke(self, "useTaskDefinition", [task_definition]))
 
 
 class Container(
     ServiceExtension,
     metaclass=jsii.JSIIMeta,
     jsii_type="@aws-cdk-containers/ecs-service-extensions.Container",
@@ -3874,14 +4091,18 @@
         '''(experimental) A hook that is called for each extension ahead of time to allow for any initial setup, such as creating resources in advance.
 
         :param service: -
         :param scope: -
 
         :stability: experimental
         '''
+        if __debug__:
+            type_hints = typing.get_type_hints(Container.prehook)
+            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
+            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
         return typing.cast(None, jsii.invoke(self, "prehook", [service, scope]))
 
     @jsii.member(jsii_name="resolveContainerDependencies")
     def resolve_container_dependencies(self) -> None:
         '''(experimental) Once all containers are added to the task definition, this hook is called for each extension to give it a chance to resolve its dependency graph so that its container starts in the right order based on the other extensions that were enabled.
 
         :stability: experimental
@@ -3895,14 +4116,17 @@
     ) -> None:
         '''(experimental) Once the task definition is created, this hook is called for each extension to give it a chance to add containers to the task definition, change the task definition's role to add permissions, etc.
 
         :param task_definition: -
 
         :stability: experimental
         '''
+        if __debug__:
+            type_hints = typing.get_type_hints(Container.use_task_definition)
+            check_type(argname="argument task_definition", value=task_definition, expected_type=type_hints["task_definition"])
         return typing.cast(None, jsii.invoke(self, "useTaskDefinition", [task_definition]))
 
     @builtins.property # type: ignore[misc]
     @jsii.member(jsii_name="trafficPort")
     def traffic_port(self) -> jsii.Number:
         '''(experimental) The port on which the container expects to receive network traffic.
 
@@ -3917,14 +4141,17 @@
 
         :stability: experimental
         '''
         return typing.cast(typing.Optional[aws_cdk.aws_logs.ILogGroup], jsii.get(self, "logGroup"))
 
     @log_group.setter
     def log_group(self, value: typing.Optional[aws_cdk.aws_logs.ILogGroup]) -> None:
+        if __debug__:
+            type_hints = typing.get_type_hints(getattr(Container, "log_group").fset)
+            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
         jsii.set(self, "logGroup", value)
 
 
 @jsii.implements(IEnvironment)
 class Environment(
     constructs.Construct,
     metaclass=jsii.JSIIMeta,
@@ -3954,14 +4181,18 @@
         :param id: -
         :param capacity_type: (experimental) The type of capacity to use for this environment. Default: - EnvironmentCapacityType.FARGATE
         :param cluster: (experimental) The ECS cluster which provides compute capacity to this service. [disable-awslint:ref-via-interface] Default: - Create a new cluster
         :param vpc: (experimental) The VPC used by the service for networking. Default: - Create a new VPC
 
         :stability: experimental
         '''
+        if __debug__:
+            type_hints = typing.get_type_hints(Environment.__init__)
+            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
+            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
         props = EnvironmentProps(capacity_type=capacity_type, cluster=cluster, vpc=vpc)
 
         jsii.create(self.__class__, self, [scope, id, props])
 
     @jsii.member(jsii_name="fromEnvironmentAttributes") # type: ignore[misc]
     @builtins.classmethod
     def from_environment_attributes(
@@ -3977,14 +4208,18 @@
         :param scope: -
         :param id: -
         :param capacity_type: (experimental) The capacity type used by the service's cluster.
         :param cluster: (experimental) The cluster that is providing capacity for this service.
 
         :stability: experimental
         '''
+        if __debug__:
+            type_hints = typing.get_type_hints(Environment.from_environment_attributes)
+            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
+            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
         attrs = EnvironmentAttributes(capacity_type=capacity_type, cluster=cluster)
 
         return typing.cast(IEnvironment, jsii.sinvoke(cls, "fromEnvironmentAttributes", [scope, id, attrs]))
 
     @jsii.member(jsii_name="addDefaultCloudMapNamespace")
     def add_default_cloud_map_namespace(
         self,
@@ -4075,14 +4310,18 @@
         '''(experimental) A hook that is called for each extension ahead of time to allow for any initial setup, such as creating resources in advance.
 
         :param service: -
         :param scope: -
 
         :stability: experimental
         '''
+        if __debug__:
+            type_hints = typing.get_type_hints(FireLensExtension.prehook)
+            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
+            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
         return typing.cast(None, jsii.invoke(self, "prehook", [service, scope]))
 
     @jsii.member(jsii_name="resolveContainerDependencies")
     def resolve_container_dependencies(self) -> None:
         '''(experimental) Once all containers are added to the task definition, this hook is called for each extension to give it a chance to resolve its dependency graph so that its container starts in the right order based on the other extensions that were enabled.
 
         :stability: experimental
@@ -4096,14 +4335,17 @@
     ) -> None:
         '''(experimental) Once the task definition is created, this hook is called for each extension to give it a chance to add containers to the task definition, change the task definition's role to add permissions, etc.
 
         :param task_definition: -
 
         :stability: experimental
         '''
+        if __debug__:
+            type_hints = typing.get_type_hints(FireLensExtension.use_task_definition)
+            check_type(argname="argument task_definition", value=task_definition, expected_type=type_hints["task_definition"])
         return typing.cast(None, jsii.invoke(self, "useTaskDefinition", [task_definition]))
 
 
 class HttpLoadBalancerExtension(
     ServiceExtension,
     metaclass=jsii.JSIIMeta,
     jsii_type="@aws-cdk-containers/ecs-service-extensions.HttpLoadBalancerExtension",
@@ -4171,14 +4413,18 @@
         '''(experimental) A hook that is called for each extension ahead of time to allow for any initial setup, such as creating resources in advance.
 
         :param service: -
         :param scope: -
 
         :stability: experimental
         '''
+        if __debug__:
+            type_hints = typing.get_type_hints(HttpLoadBalancerExtension.prehook)
+            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
+            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
         return typing.cast(None, jsii.invoke(self, "prehook", [service, scope]))
 
     @jsii.member(jsii_name="useService")
     def use_service(
         self,
         service: typing.Union[aws_cdk.aws_ecs.Ec2Service, aws_cdk.aws_ecs.FargateService],
     ) -> None:
@@ -4187,14 +4433,17 @@
         It is generally used to
         create any final resources which might depend on the service itself.
 
         :param service: -
 
         :stability: experimental
         '''
+        if __debug__:
+            type_hints = typing.get_type_hints(HttpLoadBalancerExtension.use_service)
+            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
         return typing.cast(None, jsii.invoke(self, "useService", [service]))
 
 
 @jsii.interface(
     jsii_type="@aws-cdk-containers/ecs-service-extensions.IGrantInjectable"
 )
 class IGrantInjectable(IInjectable, typing_extensions.Protocol):
@@ -4226,14 +4475,17 @@
     @jsii.member(jsii_name="grant")
     def grant(self, task_definition: aws_cdk.aws_ecs.TaskDefinition) -> None:
         '''
         :param task_definition: -
 
         :stability: experimental
         '''
+        if __debug__:
+            type_hints = typing.get_type_hints(IGrantInjectable.grant)
+            check_type(argname="argument task_definition", value=task_definition, expected_type=type_hints["task_definition"])
         return typing.cast(None, jsii.invoke(self, "grant", [task_definition]))
 
 # Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
 typing.cast(typing.Any, IGrantInjectable).__jsii_proxy_class__ = lambda : _IGrantInjectableProxy
 
 
 @jsii.implements(IGrantInjectable)
@@ -4266,14 +4518,17 @@
     @jsii.member(jsii_name="grant")
     def grant(self, task_definition: aws_cdk.aws_ecs.TaskDefinition) -> None:
         '''
         :param task_definition: -
 
         :stability: experimental
         '''
+        if __debug__:
+            type_hints = typing.get_type_hints(InjectableTopic.grant)
+            check_type(argname="argument task_definition", value=task_definition, expected_type=type_hints["task_definition"])
         return typing.cast(None, jsii.invoke(self, "grant", [task_definition]))
 
     @builtins.property # type: ignore[misc]
     @jsii.member(jsii_name="topic")
     def topic(self) -> aws_cdk.aws_sns.ITopic:
         '''
         :stability: experimental
@@ -4316,27 +4571,34 @@
         '''(experimental) A hook that is called for each extension ahead of time to allow for any initial setup, such as creating resources in advance.
 
         :param service: -
         :param scope: -
 
         :stability: experimental
         '''
+        if __debug__:
+            type_hints = typing.get_type_hints(InjecterExtension.prehook)
+            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
+            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
         return typing.cast(None, jsii.invoke(self, "prehook", [service, scope]))
 
     @jsii.member(jsii_name="useTaskDefinition")
     def use_task_definition(
         self,
         task_definition: aws_cdk.aws_ecs.TaskDefinition,
     ) -> None:
         '''(experimental) After the task definition has been created, this hook grants the required permissions to the task role for the parent service.
 
         :param task_definition: The created task definition.
 
         :stability: experimental
         '''
+        if __debug__:
+            type_hints = typing.get_type_hints(InjecterExtension.use_task_definition)
+            check_type(argname="argument task_definition", value=task_definition, expected_type=type_hints["task_definition"])
         return typing.cast(None, jsii.invoke(self, "useTaskDefinition", [task_definition]))
 
 
 class QueueExtension(
     ServiceExtension,
     metaclass=jsii.JSIIMeta,
     jsii_type="@aws-cdk-containers/ecs-service-extensions.QueueExtension",
@@ -4392,14 +4654,18 @@
         the provided ``ISubscribable`` objects.
 
         :param service: The parent service which this extension has been added to.
         :param scope: The scope that this extension should create resources in.
 
         :stability: experimental
         '''
+        if __debug__:
+            type_hints = typing.get_type_hints(QueueExtension.prehook)
+            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
+            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
         return typing.cast(None, jsii.invoke(self, "prehook", [service, scope]))
 
     @jsii.member(jsii_name="useService")
     def use_service(
         self,
         service: typing.Union[aws_cdk.aws_ecs.Ec2Service, aws_cdk.aws_ecs.FargateService],
     ) -> None:
@@ -4409,27 +4675,33 @@
         scaling policies for the SQS Queues of the service. It also creates an AWS Lambda
         Function for calculating the backlog per task metric.
 
         :param service: - The generated service.
 
         :stability: experimental
         '''
+        if __debug__:
+            type_hints = typing.get_type_hints(QueueExtension.use_service)
+            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
         return typing.cast(None, jsii.invoke(self, "useService", [service]))
 
     @jsii.member(jsii_name="useTaskDefinition")
     def use_task_definition(
         self,
         task_definition: aws_cdk.aws_ecs.TaskDefinition,
     ) -> None:
         '''(experimental) After the task definition has been created, this hook grants SQS permissions to the task role.
 
         :param task_definition: The created task definition.
 
         :stability: experimental
         '''
+        if __debug__:
+            type_hints = typing.get_type_hints(QueueExtension.use_task_definition)
+            check_type(argname="argument task_definition", value=task_definition, expected_type=type_hints["task_definition"])
         return typing.cast(None, jsii.invoke(self, "useTaskDefinition", [task_definition]))
 
     @builtins.property # type: ignore[misc]
     @jsii.member(jsii_name="eventsQueue")
     def events_queue(self) -> aws_cdk.aws_sqs.IQueue:
         '''
         :stability: experimental
@@ -4451,14 +4723,17 @@
 
         :stability: experimental
         '''
         return typing.cast(typing.Optional[aws_cdk.aws_logs.ILogGroup], jsii.get(self, "logGroup"))
 
     @log_group.setter
     def log_group(self, value: typing.Optional[aws_cdk.aws_logs.ILogGroup]) -> None:
+        if __debug__:
+            type_hints = typing.get_type_hints(getattr(QueueExtension, "log_group").fset)
+            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
         jsii.set(self, "logGroup", value)
 
 
 class ScaleOnCpuUtilization(
     ServiceExtension,
     metaclass=jsii.JSIIMeta,
     jsii_type="@aws-cdk-containers/ecs-service-extensions.ScaleOnCpuUtilization",
@@ -4553,14 +4828,17 @@
         It is generally used to
         create any final resources which might depend on the service itself.
 
         :param service: -
 
         :stability: deprecated
         '''
+        if __debug__:
+            type_hints = typing.get_type_hints(ScaleOnCpuUtilization.use_service)
+            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
         return typing.cast(None, jsii.invoke(self, "useService", [service]))
 
     @builtins.property # type: ignore[misc]
     @jsii.member(jsii_name="initialTaskCount")
     def initial_task_count(self) -> jsii.Number:
         '''(deprecated) How many tasks to launch initially.
```

### Comparing `cdk-ecs-service-extensions-2.0.0a98/src/cdk_ecs_service_extensions.egg-info/PKG-INFO` & `cdk-ecs-service-extensions-2.0.0a99/src/cdk_ecs_service_extensions.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: cdk-ecs-service-extensions
-Version: 2.0.0a98
+Version: 2.0.0a99
 Summary: @aws-cdk-containers/ecs-service-extensions
 Home-page: https://github.com/cdklabs/cdk-ecs-service-extensions.git
 Author: Amazon Web Services
 License: Apache-2.0
 Project-URL: Source, https://github.com/cdklabs/cdk-ecs-service-extensions.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

### Comparing `cdk-ecs-service-extensions-2.0.0a98/src/cdk_ecs_service_extensions.egg-info/SOURCES.txt` & `cdk-ecs-service-extensions-2.0.0a99/src/cdk_ecs_service_extensions.egg-info/SOURCES.txt`

 * *Files 0% similar despite different names*

```diff
@@ -8,8 +8,8 @@
 src/cdk_ecs_service_extensions/py.typed
 src/cdk_ecs_service_extensions.egg-info/PKG-INFO
 src/cdk_ecs_service_extensions.egg-info/SOURCES.txt
 src/cdk_ecs_service_extensions.egg-info/dependency_links.txt
 src/cdk_ecs_service_extensions.egg-info/requires.txt
 src/cdk_ecs_service_extensions.egg-info/top_level.txt
 src/cdk_ecs_service_extensions/_jsii/__init__.py
-src/cdk_ecs_service_extensions/_jsii/ecs-service-extensions@2.0.0-alpha.98.jsii.tgz
+src/cdk_ecs_service_extensions/_jsii/ecs-service-extensions@2.0.0-alpha.99.jsii.tgz
```

