# Comparing `tmp/aws-cdk.aws-iot-actions-alpha-2.8.0a0.tar.gz` & `tmp/aws-cdk.aws-iot-actions-alpha-2.9.0a0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "/codebuild/output/src248253565/src/packages/individual-packages/aws-iot-actions/dist/python/aws-cdk.aws-iot-actions-alpha-2.8.0", last modified: Thu Jan 13 18:06:07 2022, max compression
+gzip compressed data, was "/codebuild/output/src277428142/src/packages/individual-packages/aws-iot-actions/dist/python/aws-cdk.aws-iot-actions-alpha-2.9.0", last modified: Wed Jan 26 11:22:21 2022, max compression
```

## Comparing `aws-cdk.aws-iot-actions-alpha-2.8.0a0.tar` & `aws-cdk.aws-iot-actions-alpha-2.9.0a0.tar`

### file list

```diff
@@ -1,23 +1,23 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-13 18:06:06.000000 aws-cdk.aws-iot-actions-alpha-2.8.0a0/
--rw-r--r--   0 root         (0) root         (0)    11391 2022-01-13 18:06:03.000000 aws-cdk.aws-iot-actions-alpha-2.8.0a0/LICENSE
--rw-r--r--   0 root         (0) root         (0)       23 2022-01-13 18:06:03.000000 aws-cdk.aws-iot-actions-alpha-2.8.0a0/MANIFEST.in
--rw-r--r--   0 root         (0) root         (0)     1382 2022-01-13 18:06:03.000000 aws-cdk.aws-iot-actions-alpha-2.8.0a0/NOTICE
--rw-r--r--   0 root         (0) root         (0)     7705 2022-01-13 18:06:06.000000 aws-cdk.aws-iot-actions-alpha-2.8.0a0/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)     6743 2022-01-13 18:06:03.000000 aws-cdk.aws-iot-actions-alpha-2.8.0a0/README.md
--rw-r--r--   0 root         (0) root         (0)      106 2022-01-13 18:06:03.000000 aws-cdk.aws-iot-actions-alpha-2.8.0a0/pyproject.toml
--rw-r--r--   0 root         (0) root         (0)       38 2022-01-13 18:06:06.000000 aws-cdk.aws-iot-actions-alpha-2.8.0a0/setup.cfg
--rw-r--r--   0 root         (0) root         (0)     1907 2022-01-13 18:06:03.000000 aws-cdk.aws-iot-actions-alpha-2.8.0a0/setup.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-13 18:06:06.000000 aws-cdk.aws-iot-actions-alpha-2.8.0a0/src/
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-13 18:06:06.000000 aws-cdk.aws-iot-actions-alpha-2.8.0a0/src/aws_cdk/
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-13 18:06:06.000000 aws-cdk.aws-iot-actions-alpha-2.8.0a0/src/aws_cdk/aws_iot_actions_alpha/
--rw-r--r--   0 root         (0) root         (0)    49006 2022-01-13 18:06:03.000000 aws-cdk.aws-iot-actions-alpha-2.8.0a0/src/aws_cdk/aws_iot_actions_alpha/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-13 18:06:06.000000 aws-cdk.aws-iot-actions-alpha-2.8.0a0/src/aws_cdk/aws_iot_actions_alpha/_jsii/
--rw-r--r--   0 root         (0) root         (0)      495 2022-01-13 18:06:03.000000 aws-cdk.aws-iot-actions-alpha-2.8.0a0/src/aws_cdk/aws_iot_actions_alpha/_jsii/__init__.py
--rw-r--r--   0 root         (0) root         (0)    49248 2022-01-13 18:06:03.000000 aws-cdk.aws-iot-actions-alpha-2.8.0a0/src/aws_cdk/aws_iot_actions_alpha/_jsii/aws-iot-actions-alpha@2.8.0-alpha.0.jsii.tgz
--rw-r--r--   0 root         (0) root         (0)        1 2022-01-13 18:06:03.000000 aws-cdk.aws-iot-actions-alpha-2.8.0a0/src/aws_cdk/aws_iot_actions_alpha/py.typed
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-13 18:06:06.000000 aws-cdk.aws-iot-actions-alpha-2.8.0a0/src/aws_cdk.aws_iot_actions_alpha.egg-info/
--rw-r--r--   0 root         (0) root         (0)     7705 2022-01-13 18:06:06.000000 aws-cdk.aws-iot-actions-alpha-2.8.0a0/src/aws_cdk.aws_iot_actions_alpha.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)      570 2022-01-13 18:06:06.000000 aws-cdk.aws-iot-actions-alpha-2.8.0a0/src/aws_cdk.aws_iot_actions_alpha.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2022-01-13 18:06:06.000000 aws-cdk.aws-iot-actions-alpha-2.8.0a0/src/aws_cdk.aws_iot_actions_alpha.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)      168 2022-01-13 18:06:06.000000 aws-cdk.aws-iot-actions-alpha-2.8.0a0/src/aws_cdk.aws_iot_actions_alpha.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)        8 2022-01-13 18:06:06.000000 aws-cdk.aws-iot-actions-alpha-2.8.0a0/src/aws_cdk.aws_iot_actions_alpha.egg-info/top_level.txt
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-26 11:22:21.000000 aws-cdk.aws-iot-actions-alpha-2.9.0a0/
+-rw-r--r--   0 root         (0) root         (0)    11391 2022-01-26 11:22:18.000000 aws-cdk.aws-iot-actions-alpha-2.9.0a0/LICENSE
+-rw-r--r--   0 root         (0) root         (0)       23 2022-01-26 11:22:18.000000 aws-cdk.aws-iot-actions-alpha-2.9.0a0/MANIFEST.in
+-rw-r--r--   0 root         (0) root         (0)     1382 2022-01-26 11:22:18.000000 aws-cdk.aws-iot-actions-alpha-2.9.0a0/NOTICE
+-rw-r--r--   0 root         (0) root         (0)     8235 2022-01-26 11:22:21.000000 aws-cdk.aws-iot-actions-alpha-2.9.0a0/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)     7273 2022-01-26 11:22:18.000000 aws-cdk.aws-iot-actions-alpha-2.9.0a0/README.md
+-rw-r--r--   0 root         (0) root         (0)      106 2022-01-26 11:22:18.000000 aws-cdk.aws-iot-actions-alpha-2.9.0a0/pyproject.toml
+-rw-r--r--   0 root         (0) root         (0)       38 2022-01-26 11:22:21.000000 aws-cdk.aws-iot-actions-alpha-2.9.0a0/setup.cfg
+-rw-r--r--   0 root         (0) root         (0)     1907 2022-01-26 11:22:18.000000 aws-cdk.aws-iot-actions-alpha-2.9.0a0/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-26 11:22:21.000000 aws-cdk.aws-iot-actions-alpha-2.9.0a0/src/
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-26 11:22:21.000000 aws-cdk.aws-iot-actions-alpha-2.9.0a0/src/aws_cdk/
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-26 11:22:21.000000 aws-cdk.aws-iot-actions-alpha-2.9.0a0/src/aws_cdk/aws_iot_actions_alpha/
+-rw-r--r--   0 root         (0) root         (0)    54651 2022-01-26 11:22:18.000000 aws-cdk.aws-iot-actions-alpha-2.9.0a0/src/aws_cdk/aws_iot_actions_alpha/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-26 11:22:21.000000 aws-cdk.aws-iot-actions-alpha-2.9.0a0/src/aws_cdk/aws_iot_actions_alpha/_jsii/
+-rw-r--r--   0 root         (0) root         (0)      495 2022-01-26 11:22:18.000000 aws-cdk.aws-iot-actions-alpha-2.9.0a0/src/aws_cdk/aws_iot_actions_alpha/_jsii/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    51843 2022-01-26 11:22:18.000000 aws-cdk.aws-iot-actions-alpha-2.9.0a0/src/aws_cdk/aws_iot_actions_alpha/_jsii/aws-iot-actions-alpha@2.9.0-alpha.0.jsii.tgz
+-rw-r--r--   0 root         (0) root         (0)        1 2022-01-26 11:22:18.000000 aws-cdk.aws-iot-actions-alpha-2.9.0a0/src/aws_cdk/aws_iot_actions_alpha/py.typed
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-26 11:22:21.000000 aws-cdk.aws-iot-actions-alpha-2.9.0a0/src/aws_cdk.aws_iot_actions_alpha.egg-info/
+-rw-r--r--   0 root         (0) root         (0)     8235 2022-01-26 11:22:21.000000 aws-cdk.aws-iot-actions-alpha-2.9.0a0/src/aws_cdk.aws_iot_actions_alpha.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)      570 2022-01-26 11:22:21.000000 aws-cdk.aws-iot-actions-alpha-2.9.0a0/src/aws_cdk.aws_iot_actions_alpha.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2022-01-26 11:22:21.000000 aws-cdk.aws-iot-actions-alpha-2.9.0a0/src/aws_cdk.aws_iot_actions_alpha.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)      168 2022-01-26 11:22:21.000000 aws-cdk.aws-iot-actions-alpha-2.9.0a0/src/aws_cdk.aws_iot_actions_alpha.egg-info/requires.txt
+-rw-r--r--   0 root         (0) root         (0)        8 2022-01-26 11:22:21.000000 aws-cdk.aws-iot-actions-alpha-2.9.0a0/src/aws_cdk.aws_iot_actions_alpha.egg-info/top_level.txt
```

### Comparing `aws-cdk.aws-iot-actions-alpha-2.8.0a0/LICENSE` & `aws-cdk.aws-iot-actions-alpha-2.9.0a0/LICENSE`

 * *Files identical despite different names*

### Comparing `aws-cdk.aws-iot-actions-alpha-2.8.0a0/NOTICE` & `aws-cdk.aws-iot-actions-alpha-2.9.0a0/NOTICE`

 * *Files identical despite different names*

### Comparing `aws-cdk.aws-iot-actions-alpha-2.8.0a0/PKG-INFO` & `aws-cdk.aws-iot-actions-alpha-2.9.0a0/PKG-INFO`

 * *Files 3% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: aws-cdk.aws-iot-actions-alpha
-Version: 2.8.0a0
+Version: 2.9.0a0
 Summary: Receipt rule actions for AWS IoT
 Home-page: https://github.com/aws/aws-cdk
 Author: Amazon Web Services
 License: Apache-2.0
 Project-URL: Source, https://github.com/aws/aws-cdk.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
@@ -48,14 +48,15 @@
 Currently supported are:
 
 * Invoke a Lambda function
 * Put objects to a S3 bucket
 * Put logs to CloudWatch Logs
 * Capture CloudWatch metrics
 * Change state for a CloudWatch alarm
+* Put records to Kinesis Data stream
 * Put records to Kinesis Data Firehose stream
 * Send messages to SQS queues
 
 ## Invoke a Lambda function
 
 The code snippet below creates an AWS IoT Rule that invoke a Lambda function
 when it is triggered.
@@ -191,14 +192,35 @@
             reason="AWS Iot Rule action is triggered",
             alarm_state_to_set=cloudwatch.AlarmState.ALARM
         )
     ]
 )
 ```
 
+## Put records to Kinesis Data stream
+
+The code snippet below creates an AWS IoT Rule that put records to Kinesis Data
+stream when it is triggered.
+
+```python
+import aws_cdk.aws_kinesis as kinesis
+
+
+stream = kinesis.Stream(self, "MyStream")
+
+topic_rule = iot.TopicRule(self, "TopicRule",
+    sql=iot.IotSql.from_string_as_ver20160323("SELECT * FROM 'device/+/data'"),
+    actions=[
+        actions.KinesisPutRecordAction(stream,
+            partition_key="${newuuid()}"
+        )
+    ]
+)
+```
+
 ## Put records to Kinesis Data Firehose stream
 
 The code snippet below creates an AWS IoT Rule that put records to Put records
 to Kinesis Data Firehose stream when it is triggered.
 
 ```python
 import aws_cdk.aws_kinesisfirehose_alpha as firehose
```

### Comparing `aws-cdk.aws-iot-actions-alpha-2.8.0a0/README.md` & `aws-cdk.aws-iot-actions-alpha-2.9.0a0/README.md`

 * *Files 5% similar despite different names*

```diff
@@ -21,14 +21,15 @@
 Currently supported are:
 
 * Invoke a Lambda function
 * Put objects to a S3 bucket
 * Put logs to CloudWatch Logs
 * Capture CloudWatch metrics
 * Change state for a CloudWatch alarm
+* Put records to Kinesis Data stream
 * Put records to Kinesis Data Firehose stream
 * Send messages to SQS queues
 
 ## Invoke a Lambda function
 
 The code snippet below creates an AWS IoT Rule that invoke a Lambda function
 when it is triggered.
@@ -164,14 +165,35 @@
             reason="AWS Iot Rule action is triggered",
             alarm_state_to_set=cloudwatch.AlarmState.ALARM
         )
     ]
 )
 ```
 
+## Put records to Kinesis Data stream
+
+The code snippet below creates an AWS IoT Rule that put records to Kinesis Data
+stream when it is triggered.
+
+```python
+import aws_cdk.aws_kinesis as kinesis
+
+
+stream = kinesis.Stream(self, "MyStream")
+
+topic_rule = iot.TopicRule(self, "TopicRule",
+    sql=iot.IotSql.from_string_as_ver20160323("SELECT * FROM 'device/+/data'"),
+    actions=[
+        actions.KinesisPutRecordAction(stream,
+            partition_key="${newuuid()}"
+        )
+    ]
+)
+```
+
 ## Put records to Kinesis Data Firehose stream
 
 The code snippet below creates an AWS IoT Rule that put records to Put records
 to Kinesis Data Firehose stream when it is triggered.
 
 ```python
 import aws_cdk.aws_kinesisfirehose_alpha as firehose
```

### Comparing `aws-cdk.aws-iot-actions-alpha-2.8.0a0/setup.py` & `aws-cdk.aws-iot-actions-alpha-2.9.0a0/setup.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import json
 import setuptools
 
 kwargs = json.loads(
     """
 {
     "name": "aws-cdk.aws-iot-actions-alpha",
-    "version": "2.8.0.a0",
+    "version": "2.9.0.a0",
     "description": "Receipt rule actions for AWS IoT",
     "license": "Apache-2.0",
     "url": "https://github.com/aws/aws-cdk",
     "long_description_content_type": "text/markdown",
     "author": "Amazon Web Services",
     "bdist_wheel": {
         "universal": true
@@ -22,25 +22,25 @@
     },
     "packages": [
         "aws_cdk.aws_iot_actions_alpha",
         "aws_cdk.aws_iot_actions_alpha._jsii"
     ],
     "package_data": {
         "aws_cdk.aws_iot_actions_alpha._jsii": [
-            "aws-iot-actions-alpha@2.8.0-alpha.0.jsii.tgz"
+            "aws-iot-actions-alpha@2.9.0-alpha.0.jsii.tgz"
         ],
         "aws_cdk.aws_iot_actions_alpha": [
             "py.typed"
         ]
     },
     "python_requires": ">=3.6",
     "install_requires": [
-        "aws-cdk-lib>=2.8.0, <3.0.0",
-        "aws-cdk.aws-iot-alpha==2.8.0.a0",
-        "aws-cdk.aws-kinesisfirehose-alpha==2.8.0.a0",
+        "aws-cdk-lib>=2.9.0, <3.0.0",
+        "aws-cdk.aws-iot-alpha==2.9.0.a0",
+        "aws-cdk.aws-kinesisfirehose-alpha==2.9.0.a0",
         "constructs>=10.0.0, <11.0.0",
         "jsii>=1.52.1, <2.0.0",
         "publication>=0.0.3"
     ],
     "classifiers": [
         "Intended Audience :: Developers",
         "Operating System :: OS Independent",
```

### Comparing `aws-cdk.aws-iot-actions-alpha-2.8.0a0/src/aws_cdk/aws_iot_actions_alpha/__init__.py` & `aws-cdk.aws-iot-actions-alpha-2.9.0a0/src/aws_cdk/aws_iot_actions_alpha/__init__.py`

 * *Files 4% similar despite different names*

```diff
@@ -22,14 +22,15 @@
 Currently supported are:
 
 * Invoke a Lambda function
 * Put objects to a S3 bucket
 * Put logs to CloudWatch Logs
 * Capture CloudWatch metrics
 * Change state for a CloudWatch alarm
+* Put records to Kinesis Data stream
 * Put records to Kinesis Data Firehose stream
 * Send messages to SQS queues
 
 ## Invoke a Lambda function
 
 The code snippet below creates an AWS IoT Rule that invoke a Lambda function
 when it is triggered.
@@ -165,14 +166,35 @@
             reason="AWS Iot Rule action is triggered",
             alarm_state_to_set=cloudwatch.AlarmState.ALARM
         )
     ]
 )
 ```
 
+## Put records to Kinesis Data stream
+
+The code snippet below creates an AWS IoT Rule that put records to Kinesis Data
+stream when it is triggered.
+
+```python
+import aws_cdk.aws_kinesis as kinesis
+
+
+stream = kinesis.Stream(self, "MyStream")
+
+topic_rule = iot.TopicRule(self, "TopicRule",
+    sql=iot.IotSql.from_string_as_ver20160323("SELECT * FROM 'device/+/data'"),
+    actions=[
+        actions.KinesisPutRecordAction(stream,
+            partition_key="${newuuid()}"
+        )
+    ]
+)
+```
+
 ## Put records to Kinesis Data Firehose stream
 
 The code snippet below creates an AWS IoT Rule that put records to Put records
 to Kinesis Data Firehose stream when it is triggered.
 
 ```python
 import aws_cdk.aws_kinesisfirehose_alpha as firehose
@@ -227,14 +249,15 @@
 import typing_extensions
 
 from ._jsii import *
 
 import aws_cdk.aws_cloudwatch
 import aws_cdk.aws_iam
 import aws_cdk.aws_iot_alpha
+import aws_cdk.aws_kinesis
 import aws_cdk.aws_kinesisfirehose_alpha
 import aws_cdk.aws_lambda
 import aws_cdk.aws_logs
 import aws_cdk.aws_s3
 import aws_cdk.aws_sqs
 
 
@@ -710,14 +733,151 @@
     '''(experimental) Separate by a commma.
 
     :stability: experimental
     '''
 
 
 @jsii.implements(aws_cdk.aws_iot_alpha.IAction)
+class KinesisPutRecordAction(
+    metaclass=jsii.JSIIMeta,
+    jsii_type="@aws-cdk/aws-iot-actions-alpha.KinesisPutRecordAction",
+):
+    '''(experimental) The action to put the record from an MQTT message to the Kinesis Data stream.
+
+    :stability: experimental
+    :exampleMetadata: infused
+
+    Example::
+
+        import aws_cdk.aws_kinesis as kinesis
+        
+        
+        stream = kinesis.Stream(self, "MyStream")
+        
+        topic_rule = iot.TopicRule(self, "TopicRule",
+            sql=iot.IotSql.from_string_as_ver20160323("SELECT * FROM 'device/+/data'"),
+            actions=[
+                actions.KinesisPutRecordAction(stream,
+                    partition_key="${newuuid()}"
+                )
+            ]
+        )
+    '''
+
+    def __init__(
+        self,
+        stream: aws_cdk.aws_kinesis.IStream,
+        *,
+        partition_key: builtins.str,
+        role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
+    ) -> None:
+        '''
+        :param stream: The Kinesis Data stream to which to put records.
+        :param partition_key: (experimental) The partition key used to determine to which shard the data is written. The partition key is usually composed of an expression (for example, ${topic()} or ${timestamp()}).
+        :param role: (experimental) The IAM role that allows access to AWS service. Default: a new role will be created
+
+        :stability: experimental
+        '''
+        props = KinesisPutRecordActionProps(partition_key=partition_key, role=role)
+
+        jsii.create(self.__class__, self, [stream, props])
+
+    @jsii.member(jsii_name="bind")
+    def bind(
+        self,
+        rule: aws_cdk.aws_iot_alpha.ITopicRule,
+    ) -> aws_cdk.aws_iot_alpha.ActionConfig:
+        '''(experimental) (experimental) Returns the topic rule action specification.
+
+        :param rule: -
+
+        :stability: experimental
+        '''
+        return typing.cast(aws_cdk.aws_iot_alpha.ActionConfig, jsii.invoke(self, "bind", [rule]))
+
+
+@jsii.data_type(
+    jsii_type="@aws-cdk/aws-iot-actions-alpha.KinesisPutRecordActionProps",
+    jsii_struct_bases=[CommonActionProps],
+    name_mapping={"role": "role", "partition_key": "partitionKey"},
+)
+class KinesisPutRecordActionProps(CommonActionProps):
+    def __init__(
+        self,
+        *,
+        role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
+        partition_key: builtins.str,
+    ) -> None:
+        '''(experimental) Configuration properties of an action for the Kinesis Data stream.
+
+        :param role: (experimental) The IAM role that allows access to AWS service. Default: a new role will be created
+        :param partition_key: (experimental) The partition key used to determine to which shard the data is written. The partition key is usually composed of an expression (for example, ${topic()} or ${timestamp()}).
+
+        :stability: experimental
+        :exampleMetadata: infused
+
+        Example::
+
+            import aws_cdk.aws_kinesis as kinesis
+            
+            
+            stream = kinesis.Stream(self, "MyStream")
+            
+            topic_rule = iot.TopicRule(self, "TopicRule",
+                sql=iot.IotSql.from_string_as_ver20160323("SELECT * FROM 'device/+/data'"),
+                actions=[
+                    actions.KinesisPutRecordAction(stream,
+                        partition_key="${newuuid()}"
+                    )
+                ]
+            )
+        '''
+        self._values: typing.Dict[str, typing.Any] = {
+            "partition_key": partition_key,
+        }
+        if role is not None:
+            self._values["role"] = role
+
+    @builtins.property
+    def role(self) -> typing.Optional[aws_cdk.aws_iam.IRole]:
+        '''(experimental) The IAM role that allows access to AWS service.
+
+        :default: a new role will be created
+
+        :stability: experimental
+        '''
+        result = self._values.get("role")
+        return typing.cast(typing.Optional[aws_cdk.aws_iam.IRole], result)
+
+    @builtins.property
+    def partition_key(self) -> builtins.str:
+        '''(experimental) The partition key used to determine to which shard the data is written.
+
+        The partition key is usually composed of an expression (for example, ${topic()} or ${timestamp()}).
+
+        :see: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_PutRecord.html#API_PutRecord_RequestParameters
+        :stability: experimental
+        '''
+        result = self._values.get("partition_key")
+        assert result is not None, "Required property 'partition_key' is missing"
+        return typing.cast(builtins.str, result)
+
+    def __eq__(self, rhs: typing.Any) -> builtins.bool:
+        return isinstance(rhs, self.__class__) and rhs._values == self._values
+
+    def __ne__(self, rhs: typing.Any) -> builtins.bool:
+        return not (rhs == self)
+
+    def __repr__(self) -> str:
+        return "KinesisPutRecordActionProps(%s)" % ", ".join(
+            k + "=" + repr(v) for k, v in self._values.items()
+        )
+
+
+@jsii.implements(aws_cdk.aws_iot_alpha.IAction)
 class LambdaFunctionAction(
     metaclass=jsii.JSIIMeta,
     jsii_type="@aws-cdk/aws-iot-actions-alpha.LambdaFunctionAction",
 ):
     '''(experimental) The action to invoke an AWS Lambda function, passing in an MQTT message.
 
     :stability: experimental
@@ -1365,14 +1525,16 @@
     "CloudWatchPutMetricActionProps",
     "CloudWatchSetAlarmStateAction",
     "CloudWatchSetAlarmStateActionProps",
     "CommonActionProps",
     "FirehosePutRecordAction",
     "FirehosePutRecordActionProps",
     "FirehoseRecordSeparator",
+    "KinesisPutRecordAction",
+    "KinesisPutRecordActionProps",
     "LambdaFunctionAction",
     "S3PutObjectAction",
     "S3PutObjectActionProps",
     "SqsQueueAction",
     "SqsQueueActionProps",
 ]
```

### Comparing `aws-cdk.aws-iot-actions-alpha-2.8.0a0/src/aws_cdk.aws_iot_actions_alpha.egg-info/PKG-INFO` & `aws-cdk.aws-iot-actions-alpha-2.9.0a0/src/aws_cdk.aws_iot_actions_alpha.egg-info/PKG-INFO`

 * *Files 3% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: aws-cdk.aws-iot-actions-alpha
-Version: 2.8.0a0
+Version: 2.9.0a0
 Summary: Receipt rule actions for AWS IoT
 Home-page: https://github.com/aws/aws-cdk
 Author: Amazon Web Services
 License: Apache-2.0
 Project-URL: Source, https://github.com/aws/aws-cdk.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
@@ -48,14 +48,15 @@
 Currently supported are:
 
 * Invoke a Lambda function
 * Put objects to a S3 bucket
 * Put logs to CloudWatch Logs
 * Capture CloudWatch metrics
 * Change state for a CloudWatch alarm
+* Put records to Kinesis Data stream
 * Put records to Kinesis Data Firehose stream
 * Send messages to SQS queues
 
 ## Invoke a Lambda function
 
 The code snippet below creates an AWS IoT Rule that invoke a Lambda function
 when it is triggered.
@@ -191,14 +192,35 @@
             reason="AWS Iot Rule action is triggered",
             alarm_state_to_set=cloudwatch.AlarmState.ALARM
         )
     ]
 )
 ```
 
+## Put records to Kinesis Data stream
+
+The code snippet below creates an AWS IoT Rule that put records to Kinesis Data
+stream when it is triggered.
+
+```python
+import aws_cdk.aws_kinesis as kinesis
+
+
+stream = kinesis.Stream(self, "MyStream")
+
+topic_rule = iot.TopicRule(self, "TopicRule",
+    sql=iot.IotSql.from_string_as_ver20160323("SELECT * FROM 'device/+/data'"),
+    actions=[
+        actions.KinesisPutRecordAction(stream,
+            partition_key="${newuuid()}"
+        )
+    ]
+)
+```
+
 ## Put records to Kinesis Data Firehose stream
 
 The code snippet below creates an AWS IoT Rule that put records to Put records
 to Kinesis Data Firehose stream when it is triggered.
 
 ```python
 import aws_cdk.aws_kinesisfirehose_alpha as firehose
```

### Comparing `aws-cdk.aws-iot-actions-alpha-2.8.0a0/src/aws_cdk.aws_iot_actions_alpha.egg-info/SOURCES.txt` & `aws-cdk.aws-iot-actions-alpha-2.9.0a0/src/aws_cdk.aws_iot_actions_alpha.egg-info/SOURCES.txt`

 * *Files 0% similar despite different names*

```diff
@@ -8,8 +8,8 @@
 src/aws_cdk.aws_iot_actions_alpha.egg-info/SOURCES.txt
 src/aws_cdk.aws_iot_actions_alpha.egg-info/dependency_links.txt
 src/aws_cdk.aws_iot_actions_alpha.egg-info/requires.txt
 src/aws_cdk.aws_iot_actions_alpha.egg-info/top_level.txt
 src/aws_cdk/aws_iot_actions_alpha/__init__.py
 src/aws_cdk/aws_iot_actions_alpha/py.typed
 src/aws_cdk/aws_iot_actions_alpha/_jsii/__init__.py
-src/aws_cdk/aws_iot_actions_alpha/_jsii/aws-iot-actions-alpha@2.8.0-alpha.0.jsii.tgz
+src/aws_cdk/aws_iot_actions_alpha/_jsii/aws-iot-actions-alpha@2.9.0-alpha.0.jsii.tgz
```

