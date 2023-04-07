# Comparing `tmp/sentential-0.9.0.tar.gz` & `tmp/sentential-0.9.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "sentential-0.9.0.tar", max compression
+gzip compressed data, was "sentential-0.9.1.tar", max compression
```

## Comparing `sentential-0.9.0.tar` & `sentential-0.9.1.tar`

### file list

```diff
@@ -1,35 +1,35 @@
--rw-r--r--   0        0        0     1087 2023-03-12 04:14:00.831424 sentential-0.9.0/LICENSE
--rw-r--r--   0        0        0     1428 2023-03-12 04:14:11.895556 sentential-0.9.0/pyproject.toml
--rw-r--r--   0        0        0       22 2023-03-12 04:14:11.895556 sentential-0.9.0/sentential/__init__.py
--rw-r--r--   0        0        0     1438 2023-03-12 04:14:00.831424 sentential-0.9.0/sentential/cli/deploy.py
--rw-r--r--   0        0        0      571 2023-03-12 04:14:00.831424 sentential-0.9.0/sentential/cli/destroy.py
--rw-r--r--   0        0        0      489 2023-03-12 04:14:00.831424 sentential-0.9.0/sentential/cli/invoke.py
--rw-r--r--   0        0        0      504 2023-03-12 04:14:00.831424 sentential-0.9.0/sentential/cli/logs.py
--rw-r--r--   0        0        0      520 2023-03-12 04:14:00.831424 sentential-0.9.0/sentential/cli/mount.py
--rw-r--r--   0        0        0     1930 2023-03-12 04:14:00.831424 sentential-0.9.0/sentential/cli/root.py
--rw-r--r--   0        0        0      690 2023-03-12 04:14:00.831424 sentential-0.9.0/sentential/cli/store.py
--rw-r--r--   0        0        0      308 2023-03-12 04:14:00.831424 sentential-0.9.0/sentential/cli/umount.py
--rw-r--r--   0        0        0     1014 2023-03-12 04:14:00.831424 sentential-0.9.0/sentential/lib/clients.py
--rw-r--r--   0        0        0     3098 2023-03-12 04:14:00.831424 sentential-0.9.0/sentential/lib/context.py
--rw-r--r--   0        0        0     5355 2023-03-12 04:14:00.831424 sentential-0.9.0/sentential/lib/drivers/aws_ecr.py
--rw-r--r--   0        0        0     9239 2023-03-12 04:14:00.831424 sentential-0.9.0/sentential/lib/drivers/aws_lambda.py
--rw-r--r--   0        0        0      882 2023-03-12 04:14:00.831424 sentential-0.9.0/sentential/lib/drivers/local_bridge.py
--rw-r--r--   0        0        0     3818 2023-03-12 04:14:00.831424 sentential-0.9.0/sentential/lib/drivers/local_images.py
--rw-r--r--   0        0        0     4709 2023-03-12 04:14:00.831424 sentential-0.9.0/sentential/lib/drivers/local_lambda.py
--rw-r--r--   0        0        0      447 2023-03-12 04:14:00.831424 sentential-0.9.0/sentential/lib/drivers/spec.py
--rw-r--r--   0        0        0      829 2023-03-12 04:14:00.831424 sentential-0.9.0/sentential/lib/exceptions.py
--rw-r--r--   0        0        0     8036 2023-03-12 04:14:00.831424 sentential-0.9.0/sentential/lib/joinery.py
--rw-r--r--   0        0        0     3174 2023-03-12 04:14:00.831424 sentential-0.9.0/sentential/lib/mounts/aws_event_schedule.py
--rw-r--r--   0        0        0     2778 2023-03-12 04:14:00.831424 sentential-0.9.0/sentential/lib/mounts/aws_lambda_public_url.py
--rw-r--r--   0        0        0     1705 2023-03-12 04:14:00.831424 sentential-0.9.0/sentential/lib/mounts/local_lambda_public_url.py
--rw-r--r--   0        0        0      251 2023-03-12 04:14:00.831424 sentential-0.9.0/sentential/lib/mounts/spec.py
--rw-r--r--   0        0        0     1573 2023-03-12 04:14:00.831424 sentential-0.9.0/sentential/lib/ontology.py
--rw-r--r--   0        0        0    10609 2023-03-12 04:14:00.831424 sentential-0.9.0/sentential/lib/shapes.py
--rw-r--r--   0        0        0     4958 2023-03-12 04:14:00.831424 sentential-0.9.0/sentential/lib/store.py
--rw-r--r--   0        0        0     1831 2023-03-12 04:14:00.835424 sentential-0.9.0/sentential/lib/template.py
--rw-r--r--   0        0        0     1295 2023-03-12 04:14:00.835424 sentential-0.9.0/sentential/sntl.py
--rw-r--r--   0        0        0     4327 2023-03-12 04:14:00.835424 sentential-0.9.0/sentential/support/shaper.py
--rw-r--r--   0        0        0      295 2023-03-12 04:14:00.835424 sentential-0.9.0/sentential/templates/Dockerfile
--rw-r--r--   0        0        0     1085 2023-03-12 04:14:00.835424 sentential-0.9.0/sentential/templates/policy.json
--rw-r--r--   0        0        0      613 2023-03-12 04:14:00.835424 sentential-0.9.0/sentential/templates/shapes.py
--rw-r--r--   0        0        0      866 1970-01-01 00:00:00.000000 sentential-0.9.0/PKG-INFO
+-rw-r--r--   0        0        0     1087 2023-03-23 02:36:35.241137 sentential-0.9.1/LICENSE
+-rw-r--r--   0        0        0     1428 2023-03-23 02:36:45.685377 sentential-0.9.1/pyproject.toml
+-rw-r--r--   0        0        0       22 2023-03-23 02:36:45.685377 sentential-0.9.1/sentential/__init__.py
+-rw-r--r--   0        0        0     1438 2023-03-23 02:36:35.241137 sentential-0.9.1/sentential/cli/deploy.py
+-rw-r--r--   0        0        0      571 2023-03-23 02:36:35.241137 sentential-0.9.1/sentential/cli/destroy.py
+-rw-r--r--   0        0        0      489 2023-03-23 02:36:35.241137 sentential-0.9.1/sentential/cli/invoke.py
+-rw-r--r--   0        0        0      504 2023-03-23 02:36:35.241137 sentential-0.9.1/sentential/cli/logs.py
+-rw-r--r--   0        0        0      520 2023-03-23 02:36:35.241137 sentential-0.9.1/sentential/cli/mount.py
+-rw-r--r--   0        0        0     2192 2023-03-23 02:36:35.241137 sentential-0.9.1/sentential/cli/root.py
+-rw-r--r--   0        0        0      690 2023-03-23 02:36:35.241137 sentential-0.9.1/sentential/cli/store.py
+-rw-r--r--   0        0        0      308 2023-03-23 02:36:35.241137 sentential-0.9.1/sentential/cli/umount.py
+-rw-r--r--   0        0        0     1008 2023-03-23 02:36:35.241137 sentential-0.9.1/sentential/lib/clients.py
+-rw-r--r--   0        0        0     3098 2023-03-23 02:36:35.241137 sentential-0.9.1/sentential/lib/context.py
+-rw-r--r--   0        0        0     5355 2023-03-23 02:36:35.241137 sentential-0.9.1/sentential/lib/drivers/aws_ecr.py
+-rw-r--r--   0        0        0     9926 2023-03-23 02:36:35.241137 sentential-0.9.1/sentential/lib/drivers/aws_lambda.py
+-rw-r--r--   0        0        0      882 2023-03-23 02:36:35.241137 sentential-0.9.1/sentential/lib/drivers/local_bridge.py
+-rw-r--r--   0        0        0     3818 2023-03-23 02:36:35.241137 sentential-0.9.1/sentential/lib/drivers/local_images.py
+-rw-r--r--   0        0        0     4709 2023-03-23 02:36:35.241137 sentential-0.9.1/sentential/lib/drivers/local_lambda.py
+-rw-r--r--   0        0        0      447 2023-03-23 02:36:35.241137 sentential-0.9.1/sentential/lib/drivers/spec.py
+-rw-r--r--   0        0        0      829 2023-03-23 02:36:35.241137 sentential-0.9.1/sentential/lib/exceptions.py
+-rw-r--r--   0        0        0     8036 2023-03-23 02:36:35.241137 sentential-0.9.1/sentential/lib/joinery.py
+-rw-r--r--   0        0        0     3174 2023-03-23 02:36:35.241137 sentential-0.9.1/sentential/lib/mounts/aws_event_schedule.py
+-rw-r--r--   0        0        0     2778 2023-03-23 02:36:35.245138 sentential-0.9.1/sentential/lib/mounts/aws_lambda_public_url.py
+-rw-r--r--   0        0        0     1705 2023-03-23 02:36:35.245138 sentential-0.9.1/sentential/lib/mounts/local_lambda_public_url.py
+-rw-r--r--   0        0        0      251 2023-03-23 02:36:35.245138 sentential-0.9.1/sentential/lib/mounts/spec.py
+-rw-r--r--   0        0        0     1573 2023-03-23 02:36:35.245138 sentential-0.9.1/sentential/lib/ontology.py
+-rw-r--r--   0        0        0    10687 2023-03-23 02:36:35.245138 sentential-0.9.1/sentential/lib/shapes.py
+-rw-r--r--   0        0        0     4958 2023-03-23 02:36:35.245138 sentential-0.9.1/sentential/lib/store.py
+-rw-r--r--   0        0        0     1831 2023-03-23 02:36:35.245138 sentential-0.9.1/sentential/lib/template.py
+-rw-r--r--   0        0        0     1295 2023-03-23 02:36:35.245138 sentential-0.9.1/sentential/sntl.py
+-rw-r--r--   0        0        0     4327 2023-03-23 02:36:35.245138 sentential-0.9.1/sentential/support/shaper.py
+-rw-r--r--   0        0        0      295 2023-03-23 02:36:35.245138 sentential-0.9.1/sentential/templates/Dockerfile
+-rw-r--r--   0        0        0     1085 2023-03-23 02:36:35.245138 sentential-0.9.1/sentential/templates/policy.json
+-rw-r--r--   0        0        0      613 2023-03-23 02:36:35.245138 sentential-0.9.1/sentential/templates/shapes.py
+-rw-r--r--   0        0        0      866 1970-01-01 00:00:00.000000 sentential-0.9.1/PKG-INFO
```

### Comparing `sentential-0.9.0/LICENSE` & `sentential-0.9.1/LICENSE`

 * *Files identical despite different names*

### Comparing `sentential-0.9.0/pyproject.toml` & `sentential-0.9.1/pyproject.toml`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "sentential"
-version = "0.9.0"
+version = "0.9.1"
 description = "because lambdas are good"
 authors = [
   "Brendan Keane <btkeane@gmail.com>",
   "Raymond Douglas <r@rymnd.org>"
 ]
 license = "MIT"
```

### Comparing `sentential-0.9.0/sentential/cli/deploy.py` & `sentential-0.9.1/sentential/cli/deploy.py`

 * *Files identical despite different names*

### Comparing `sentential-0.9.0/sentential/cli/destroy.py` & `sentential-0.9.1/sentential/cli/destroy.py`

 * *Files identical despite different names*

### Comparing `sentential-0.9.0/sentential/cli/mount.py` & `sentential-0.9.1/sentential/cli/mount.py`

 * *Files identical despite different names*

### Comparing `sentential-0.9.0/sentential/cli/root.py` & `sentential-0.9.1/sentential/cli/root.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,13 +1,14 @@
 from typing import List, Optional
 import typer
 from sentential.lib.clients import clients
 from sentential.lib.drivers.local_images import LocalImagesDriver
 from sentential.lib.drivers.local_lambda import LocalLambdaDriver
 from sentential.lib.drivers.aws_ecr import AwsEcrDriver
+from sentential.lib.drivers.aws_lambda import AwsLambdaDriver
 from sentential.lib.template import Init
 from sentential.lib.shapes import Architecture, Runtimes
 from sentential.lib.ontology import Ontology
 from sentential.lib.joinery import Joinery
 from rich import print
 
 root = typer.Typer()
@@ -55,13 +56,17 @@
 @root.command()
 def ls(verbose: bool = typer.Option(False)):
     """list image information"""
     print(Joinery(Ontology()).list(verbose))
 
 
 @root.command()
-def clean(remote: bool = typer.Option(False)):
-    """clean images"""
+def clean(remote: bool = typer.Option(False), remote_logs: bool = typer.Option(False)):
+    """clean images (and logs)"""
     ontology = Ontology()
     LocalImagesDriver(ontology).clean()
     if remote:
         AwsEcrDriver(ontology).clean()
+    if (
+        remote_logs
+    ):  # MAYBE: is it time to graduate to `clean local` and `clean remote`?
+        AwsLambdaDriver(ontology).clean()
```

### Comparing `sentential-0.9.0/sentential/cli/store.py` & `sentential-0.9.1/sentential/cli/store.py`

 * *Files identical despite different names*

### Comparing `sentential-0.9.0/sentential/lib/clients.py` & `sentential-0.9.1/sentential/lib/clients.py`

 * *Files 8% similar despite different names*

```diff
@@ -13,15 +13,15 @@
         self.iam = boto3.client("iam", **boto3_config[env])
         self.sts = boto3.client("sts", **boto3_config[env])
         self.ecr = boto3.client("ecr", **boto3_config[env])
         self.ssm = boto3.client("ssm", **boto3_config[env])
         self.kms = boto3.client("kms", **boto3_config[env])
         self.ebr = boto3.client("events", **boto3_config[env])
         self.api_gw = boto3.client("apigatewayv2", **boto3_config[env])
-        self.cloudwatch = boto3.client("logs", **boto3_config[env])
+        self.logs = boto3.client("logs", **boto3_config[env])
         self.docker = docker
 
 
 try:
     clients = Clients()
 except AWS_EXCEPTIONS as e:
     print(f"AWS: {e}")
```

### Comparing `sentential-0.9.0/sentential/lib/context.py` & `sentential-0.9.1/sentential/lib/context.py`

 * *Files identical despite different names*

### Comparing `sentential-0.9.0/sentential/lib/drivers/aws_ecr.py` & `sentential-0.9.1/sentential/lib/drivers/aws_ecr.py`

 * *Files identical despite different names*

### Comparing `sentential-0.9.0/sentential/lib/drivers/aws_lambda.py` & `sentential-0.9.1/sentential/lib/drivers/aws_lambda.py`

 * *Files 7% similar despite different names*

```diff
@@ -18,14 +18,15 @@
 
 
 class AwsLambdaDriver(LambdaDriver):
     def __init__(self, ontology: Ontology) -> None:
         self.ontology = ontology
         self.function_name = ontology.context.resource_name
         self.policy_arn = f"arn:aws:iam::{self.ontology.context.account_id}:policy/{self.ontology.context.resource_name}"
+        self.log_group = f"/aws/lambda/{self.function_name}"
 
     @property
     def provision(self) -> Provision:
         # there must be a better way to do polymorphic type stuff...
         return cast(Provision, self.ontology.configs.parameters)
 
     def deploy(self, image: AwsImageDetail, arch: Union[Architecture, None]) -> str:
@@ -37,14 +38,15 @@
         tags = self.ontology.tags.as_dict()
 
         clients.iam.attach_role_policy(
             RoleName=self._put_role(tags)["Role"]["RoleName"],
             PolicyArn=self._put_policy(tags)["Policy"]["Arn"],
         )
         self._put_lambda(chosen_dist, tags)
+        self._put_log_policy()
 
         return f"deployed {self.ontology.context.resource_name} to aws"
 
     def _choose_dist(
         self, image: AwsImageDetail, arch: Union[Architecture, None]
     ) -> AwsManifestListDistribution:
         if not isinstance(image.imageManifest, AwsManifestList):
@@ -118,14 +120,17 @@
         response = clients.lmb.invoke(
             FunctionName=self.function_name, Payload=payload, LogType="Tail"
         )
         response["Payload"] = response["Payload"].read()
         response["Payload"] = response["Payload"].decode("utf-8")
         return LambdaInvokeResponse(**response).json()
 
+    def clean(self) -> None:
+        self._clean_logs()
+
     def _put_role(self, tags: Optional[Dict[str, str]] = None) -> Dict:
         role_name = self.function_name
         try:
             clients.iam.create_role(
                 RoleName=role_name,
                 AssumeRolePolicyDocument=LAMBDA_ROLE_POLICY_JSON,
             )
@@ -245,7 +250,24 @@
                 Publish=True,
             )
 
         if tags:
             clients.lmb.tag_resource(Resource=function["FunctionArn"], Tags=tags)
 
         return function
+
+    def _put_log_policy(self) -> None:
+        try:
+            clients.logs.put_retention_policy(
+                logGroupName=self.log_group,
+                retentionInDays=self.provision.log_retention,
+            )
+        except clients.logs.exceptions.ResourceNotFoundException:
+            pass
+
+    def _clean_logs(self) -> None:
+        try:
+            clients.logs.delete_log_group(
+                logGroupName=self.log_group,
+            )
+        except clients.logs.exceptions.ResourceNotFoundException:
+            pass
```

### Comparing `sentential-0.9.0/sentential/lib/drivers/local_bridge.py` & `sentential-0.9.1/sentential/lib/drivers/local_bridge.py`

 * *Files identical despite different names*

### Comparing `sentential-0.9.0/sentential/lib/drivers/local_images.py` & `sentential-0.9.1/sentential/lib/drivers/local_images.py`

 * *Files identical despite different names*

### Comparing `sentential-0.9.0/sentential/lib/drivers/local_lambda.py` & `sentential-0.9.1/sentential/lib/drivers/local_lambda.py`

 * *Files identical despite different names*

### Comparing `sentential-0.9.0/sentential/lib/exceptions.py` & `sentential-0.9.1/sentential/lib/exceptions.py`

 * *Files identical despite different names*

### Comparing `sentential-0.9.0/sentential/lib/joinery.py` & `sentential-0.9.1/sentential/lib/joinery.py`

 * *Files identical despite different names*

### Comparing `sentential-0.9.0/sentential/lib/mounts/aws_event_schedule.py` & `sentential-0.9.1/sentential/lib/mounts/aws_event_schedule.py`

 * *Files identical despite different names*

### Comparing `sentential-0.9.0/sentential/lib/mounts/aws_lambda_public_url.py` & `sentential-0.9.1/sentential/lib/mounts/aws_lambda_public_url.py`

 * *Files identical despite different names*

### Comparing `sentential-0.9.0/sentential/lib/mounts/local_lambda_public_url.py` & `sentential-0.9.1/sentential/lib/mounts/local_lambda_public_url.py`

 * *Files identical despite different names*

### Comparing `sentential-0.9.0/sentential/lib/ontology.py` & `sentential-0.9.1/sentential/lib/ontology.py`

 * *Files identical despite different names*

### Comparing `sentential-0.9.0/sentential/lib/shapes.py` & `sentential-0.9.1/sentential/lib/shapes.py`

 * *Files 1% similar despite different names*

```diff
@@ -26,14 +26,15 @@
     subnet_ids: List[str] = Field(default=[], description="subnet ids")
     security_group_ids: List[str] = Field(default=[], description="security group ids")
     auth_type: str = Field(default="NONE", description="auth type")
     allow_headers: List[str] = Field(default=["*"], description="CORS AllowHeaders")
     allow_methods: List[str] = Field(default=["*"], description="CORS AllowMethods")
     allow_origins: List[str] = Field(default=["*"], description="CORS AllowOrigins")
     expose_headers: List[str] = Field(default=["*"], description="CORS ExposeHeaders")
+    log_retention: int = Field(default=7, description="log retention (days)")
 
     @validator("auth_type")
     def is_valid_auth_type(cls, v):
         valid_auth_types = ["NONE", "AWS_IAM"]
         if v not in valid_auth_types:
             raise ValueError(f"auth_type must be one of {', '.join(valid_auth_types)}")
         return v
```

### Comparing `sentential-0.9.0/sentential/lib/store.py` & `sentential-0.9.1/sentential/lib/store.py`

 * *Files identical despite different names*

### Comparing `sentential-0.9.0/sentential/lib/template.py` & `sentential-0.9.1/sentential/lib/template.py`

 * *Files identical despite different names*

### Comparing `sentential-0.9.0/sentential/sntl.py` & `sentential-0.9.1/sentential/sntl.py`

 * *Files identical despite different names*

### Comparing `sentential-0.9.0/sentential/support/shaper.py` & `sentential-0.9.1/sentential/support/shaper.py`

 * *Files identical despite different names*

### Comparing `sentential-0.9.0/sentential/templates/policy.json` & `sentential-0.9.1/sentential/templates/policy.json`

 * *Files identical despite different names*

### Comparing `sentential-0.9.0/sentential/templates/shapes.py` & `sentential-0.9.1/sentential/templates/shapes.py`

 * *Files identical despite different names*

### Comparing `sentential-0.9.0/PKG-INFO` & `sentential-0.9.1/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: sentential
-Version: 0.9.0
+Version: 0.9.1
 Summary: because lambdas are good
 License: MIT
 Author: Brendan Keane
 Author-email: btkeane@gmail.com
 Requires-Python: >=3.8,<4.0
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Programming Language :: Python :: 3
```

