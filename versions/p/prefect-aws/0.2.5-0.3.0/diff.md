# Comparing `tmp/prefect-aws-0.2.5.tar.gz` & `tmp/prefect-aws-0.3.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "/home/runner/work/prefect-aws/prefect-aws/dist/.tmp-op0gdrry/prefect-aws-0.2.5.tar", last modified: Mon Mar 13 15:23:22 2023, max compression
+gzip compressed data, was "/home/runner/work/prefect-aws/prefect-aws/dist/.tmp-4uymi3en/prefect-aws-0.3.0.tar", last modified: Thu Apr  6 13:35:12 2023, max compression
```

## Comparing `prefect-aws-0.2.5.tar` & `prefect-aws-0.3.0.tar`

### file list

```diff
@@ -1,36 +1,39 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-13 15:23:22.000000 prefect-aws-0.2.5/
--rw-r--r--   0 runner    (1001) docker     (123)    11356 2023-03-13 15:21:21.000000 prefect-aws-0.2.5/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)      318 2023-03-13 15:21:21.000000 prefect-aws-0.2.5/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     6860 2023-03-13 15:23:22.000000 prefect-aws-0.2.5/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     5950 2023-03-13 15:21:21.000000 prefect-aws-0.2.5/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-13 15:23:22.000000 prefect-aws-0.2.5/prefect_aws/
--rw-r--r--   0 runner    (1001) docker     (123)      351 2023-03-13 15:21:21.000000 prefect-aws-0.2.5/prefect_aws/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      497 2023-03-13 15:23:22.000000 prefect-aws-0.2.5/prefect_aws/_version.py
--rw-r--r--   0 runner    (1001) docker     (123)     2181 2023-03-13 15:21:21.000000 prefect-aws-0.2.5/prefect_aws/batch.py
--rw-r--r--   0 runner    (1001) docker     (123)     5542 2023-03-13 15:21:21.000000 prefect-aws-0.2.5/prefect_aws/client_parameters.py
--rw-r--r--   0 runner    (1001) docker     (123)     2710 2023-03-13 15:21:21.000000 prefect-aws-0.2.5/prefect_aws/client_waiter.py
--rw-r--r--   0 runner    (1001) docker     (123)     8200 2023-03-13 15:21:21.000000 prefect-aws-0.2.5/prefect_aws/credentials.py
--rw-r--r--   0 runner    (1001) docker     (123)    56791 2023-03-13 15:21:21.000000 prefect-aws-0.2.5/prefect_aws/ecs.py
--rw-r--r--   0 runner    (1001) docker     (123)    39001 2023-03-13 15:21:21.000000 prefect-aws-0.2.5/prefect_aws/s3.py
--rw-r--r--   0 runner    (1001) docker     (123)    17074 2023-03-13 15:21:21.000000 prefect-aws-0.2.5/prefect_aws/secrets_manager.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-13 15:23:22.000000 prefect-aws-0.2.5/prefect_aws.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     6860 2023-03-13 15:23:22.000000 prefect-aws-0.2.5/prefect_aws.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      739 2023-03-13 15:23:22.000000 prefect-aws-0.2.5/prefect_aws.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-13 15:23:22.000000 prefect-aws-0.2.5/prefect_aws.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       48 2023-03-13 15:23:22.000000 prefect-aws-0.2.5/prefect_aws.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (123)      379 2023-03-13 15:23:22.000000 prefect-aws-0.2.5/prefect_aws.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       12 2023-03-13 15:23:22.000000 prefect-aws-0.2.5/prefect_aws.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)      325 2023-03-13 15:21:21.000000 prefect-aws-0.2.5/requirements-dev.txt
--rw-r--r--   0 runner    (1001) docker     (123)      103 2023-03-13 15:21:21.000000 prefect-aws-0.2.5/requirements.txt
--rw-r--r--   0 runner    (1001) docker     (123)      755 2023-03-13 15:23:22.000000 prefect-aws-0.2.5/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1650 2023-03-13 15:21:21.000000 prefect-aws-0.2.5/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-13 15:23:22.000000 prefect-aws-0.2.5/tests/
--rw-r--r--   0 runner    (1001) docker     (123)     2182 2023-03-13 15:21:21.000000 prefect-aws-0.2.5/tests/test_batch.py
--rw-r--r--   0 runner    (1001) docker     (123)      670 2023-03-13 15:21:21.000000 prefect-aws-0.2.5/tests/test_block_standards.py
--rw-r--r--   0 runner    (1001) docker     (123)     4610 2023-03-13 15:21:21.000000 prefect-aws-0.2.5/tests/test_client_parameters.py
--rw-r--r--   0 runner    (1001) docker     (123)     1805 2023-03-13 15:21:21.000000 prefect-aws-0.2.5/tests/test_client_waiter.py
--rw-r--r--   0 runner    (1001) docker     (123)     1361 2023-03-13 15:21:21.000000 prefect-aws-0.2.5/tests/test_credentials.py
--rw-r--r--   0 runner    (1001) docker     (123)    66199 2023-03-13 15:21:21.000000 prefect-aws-0.2.5/tests/test_ecs.py
--rw-r--r--   0 runner    (1001) docker     (123)    25061 2023-03-13 15:21:21.000000 prefect-aws-0.2.5/tests/test_s3.py
--rw-r--r--   0 runner    (1001) docker     (123)     6704 2023-03-13 15:21:21.000000 prefect-aws-0.2.5/tests/test_secrets_manager.py
--rw-r--r--   0 runner    (1001) docker     (123)    80049 2023-03-13 15:21:21.000000 prefect-aws-0.2.5/versioneer.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:35:12.000000 prefect-aws-0.3.0/
+-rw-r--r--   0 runner    (1001) docker     (123)    11356 2023-04-06 13:33:33.000000 prefect-aws-0.3.0/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)      318 2023-04-06 13:33:33.000000 prefect-aws-0.3.0/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     2776 2023-04-06 13:35:12.000000 prefect-aws-0.3.0/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     1865 2023-04-06 13:33:33.000000 prefect-aws-0.3.0/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:35:12.000000 prefect-aws-0.3.0/prefect_aws/
+-rw-r--r--   0 runner    (1001) docker     (123)      407 2023-04-06 13:33:33.000000 prefect-aws-0.3.0/prefect_aws/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      497 2023-04-06 13:35:12.000000 prefect-aws-0.3.0/prefect_aws/_version.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2181 2023-04-06 13:33:33.000000 prefect-aws-0.3.0/prefect_aws/batch.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5831 2023-04-06 13:33:33.000000 prefect-aws-0.3.0/prefect_aws/client_parameters.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2710 2023-04-06 13:33:33.000000 prefect-aws-0.3.0/prefect_aws/client_waiter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8200 2023-04-06 13:33:33.000000 prefect-aws-0.3.0/prefect_aws/credentials.py
+-rw-r--r--   0 runner    (1001) docker     (123)    57054 2023-04-06 13:33:33.000000 prefect-aws-0.3.0/prefect_aws/ecs.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:35:12.000000 prefect-aws-0.3.0/prefect_aws/projects/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 13:33:33.000000 prefect-aws-0.3.0/prefect_aws/projects/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5765 2023-04-06 13:33:33.000000 prefect-aws-0.3.0/prefect_aws/projects/steps.py
+-rw-r--r--   0 runner    (1001) docker     (123)    32792 2023-04-06 13:33:33.000000 prefect-aws-0.3.0/prefect_aws/s3.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17379 2023-04-06 13:33:33.000000 prefect-aws-0.3.0/prefect_aws/secrets_manager.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:35:12.000000 prefect-aws-0.3.0/prefect_aws.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     2776 2023-04-06 13:35:12.000000 prefect-aws-0.3.0/prefect_aws.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      802 2023-04-06 13:35:12.000000 prefect-aws-0.3.0/prefect_aws.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 13:35:12.000000 prefect-aws-0.3.0/prefect_aws.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       48 2023-04-06 13:35:12.000000 prefect-aws-0.3.0/prefect_aws.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      392 2023-04-06 13:35:12.000000 prefect-aws-0.3.0/prefect_aws.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       12 2023-04-06 13:35:12.000000 prefect-aws-0.3.0/prefect_aws.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      338 2023-04-06 13:33:33.000000 prefect-aws-0.3.0/requirements-dev.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      103 2023-04-06 13:33:33.000000 prefect-aws-0.3.0/requirements.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      755 2023-04-06 13:35:12.000000 prefect-aws-0.3.0/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1650 2023-04-06 13:33:33.000000 prefect-aws-0.3.0/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:35:12.000000 prefect-aws-0.3.0/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)     2182 2023-04-06 13:33:33.000000 prefect-aws-0.3.0/tests/test_batch.py
+-rw-r--r--   0 runner    (1001) docker     (123)      670 2023-04-06 13:33:33.000000 prefect-aws-0.3.0/tests/test_block_standards.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4747 2023-04-06 13:33:33.000000 prefect-aws-0.3.0/tests/test_client_parameters.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1805 2023-04-06 13:33:33.000000 prefect-aws-0.3.0/tests/test_client_waiter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1361 2023-04-06 13:33:33.000000 prefect-aws-0.3.0/tests/test_credentials.py
+-rw-r--r--   0 runner    (1001) docker     (123)    66908 2023-04-06 13:33:33.000000 prefect-aws-0.3.0/tests/test_ecs.py
+-rw-r--r--   0 runner    (1001) docker     (123)    23872 2023-04-06 13:33:33.000000 prefect-aws-0.3.0/tests/test_s3.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6704 2023-04-06 13:33:33.000000 prefect-aws-0.3.0/tests/test_secrets_manager.py
+-rw-r--r--   0 runner    (1001) docker     (123)    80049 2023-04-06 13:33:33.000000 prefect-aws-0.3.0/versioneer.py
```

### Comparing `prefect-aws-0.2.5/LICENSE` & `prefect-aws-0.3.0/LICENSE`

 * *Files identical despite different names*

### Comparing `prefect-aws-0.2.5/prefect_aws/batch.py` & `prefect-aws-0.3.0/prefect_aws/batch.py`

 * *Files identical despite different names*

### Comparing `prefect-aws-0.2.5/prefect_aws/client_parameters.py` & `prefect-aws-0.3.0/prefect_aws/client_parameters.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,12 +1,13 @@
 """Module handling Client parameters"""
 
 import warnings
 from typing import Any, Dict, Optional, Union
 
+from botocore import UNSIGNED
 from botocore.client import Config
 from pydantic import BaseModel, Field, FilePath, root_validator, validator
 
 
 class AwsClientParameters(BaseModel):
     """
     Model used to manage extra parameters that you can pass when you initialize
@@ -124,12 +125,16 @@
 
         params_override = {}
         for key, value in params.items():
             if value is None:
                 continue
             elif key == "config":
                 params_override[key] = Config(**value)
+                # botocore UNSIGNED is an instance while actual signers can
+                # be fetched as strings
+                if params_override[key].signature_version == "unsigned":
+                    params_override[key].signature_version = UNSIGNED
             elif key == "verify_cert_path":
                 params_override["verify"] = value
             else:
                 params_override[key] = value
         return params_override
```

### Comparing `prefect-aws-0.2.5/prefect_aws/client_waiter.py` & `prefect-aws-0.3.0/prefect_aws/client_waiter.py`

 * *Files identical despite different names*

### Comparing `prefect-aws-0.2.5/prefect_aws/credentials.py` & `prefect-aws-0.3.0/prefect_aws/credentials.py`

 * *Files identical despite different names*

### Comparing `prefect-aws-0.2.5/prefect_aws/ecs.py` & `prefect-aws-0.3.0/prefect_aws/ecs.py`

 * *Files 0% similar despite different names*

```diff
@@ -101,14 +101,15 @@
             },
         ],
     )
     ```
 """
 import copy
 import difflib
+import json
 import logging
 import pprint
 import sys
 import time
 import warnings
 from typing import TYPE_CHECKING, Any, Dict, Generator, List, Optional, Tuple, Union
 
@@ -253,15 +254,15 @@
             the default cluster will be used.
         env: A dictionary of environment variables to provide to
             the task run. These variables are set on the
             Prefect container at task runtime.
         task_role_arn: An optional role to attach to the task run.
             This controls the permissions of the task while it is running.
         task_customizations: A list of JSON 6902 patches to apply to the task
-            run request.
+            run request. If a string is given, it will parsed as a JSON expression.
         task_start_timeout_seconds: The amount of time to watch for the
             start of the ECS task before marking it as failed. The task must
             enter a RUNNING state to be considered started.
         task_watch_poll_interval: The amount of time to wait between AWS API
             calls while monitoring the state of an ECS task.
     """
 
@@ -432,15 +433,18 @@
         description=(
             "A role to attach to the task run. This controls the permissions of the "
             "task while it is running."
         ),
     )
     task_customizations: JsonPatch = Field(
         default_factory=lambda: JsonPatch([]),
-        description="A list of JSON 6902 patches to apply to the task run request.",
+        description=(
+            "A list of JSON 6902 patches to apply to the task run request. "
+            "If a string is given, it will parsed as a JSON expression."
+        ),
     )
 
     # Execution settings
     task_start_timeout_seconds: int = Field(
         default=120,
         description=(
             "The amount of time to watch for the start of the ECS task "
@@ -534,22 +538,24 @@
         # Otherwise, it should default to the Prefect base image
         else:
             values["image"] = get_prefect_image_name()
         return values
 
     @validator("task_customizations", pre=True)
     def cast_customizations_to_a_json_patch(
-        cls, value: Union[List[Dict], JsonPatch]
+        cls, value: Union[List[Dict], JsonPatch, str]
     ) -> JsonPatch:
         """
         Casts lists to JsonPatch instances.
         """
+        if isinstance(value, str):
+            value = json.loads(value)
         if isinstance(value, list):
             return JsonPatch(value)
-        return value
+        return value  # type: ignore
 
     class Config:
         """Configuration of pydantic."""
 
         # Support serialization of the 'JsonPatch' type
         arbitrary_types_allowed = True
         json_encoders = {JsonPatch: lambda p: p.patch}
```

### Comparing `prefect-aws-0.2.5/prefect_aws/s3.py` & `prefect-aws-0.3.0/prefect_aws/s3.py`

 * *Files 13% similar despite different names*

```diff
@@ -1,24 +1,23 @@
 """Tasks for interacting with AWS S3"""
 import asyncio
 import io
 import os
 import uuid
-import warnings
-from pathlib import Path, PurePath
+from pathlib import Path
 from typing import Any, BinaryIO, Dict, List, Optional, Union
 
 import boto3
 from botocore.paginate import PageIterator
 from prefect import get_run_logger, task
 from prefect.blocks.abstract import ObjectStorageBlock
 from prefect.filesystems import WritableDeploymentStorage, WritableFileSystem
 from prefect.utilities.asyncutils import run_sync_in_worker_thread, sync_compatible
 from prefect.utilities.filesystem import filter_files
-from pydantic import Field, root_validator, validator
+from pydantic import Field
 
 from prefect_aws import AwsCredentials, MinIOCredentials
 from prefect_aws.client_parameters import AwsClientParameters
 
 
 @task
 async def s3_download(
@@ -236,246 +235,95 @@
 class S3Bucket(WritableFileSystem, WritableDeploymentStorage, ObjectStorageBlock):
 
     """
     Block used to store data using AWS S3 or S3-compatible object storage like MinIO.
 
     Attributes:
         bucket_name: Name of your bucket.
-        minio_credentials: [DEPRECATED; use the credentials field instead]
-            A block containing your credentials (choose this or AWS Credentials)
-        aws_credentials: [DEPRECATED; use the credentials field instead]
-            A block containing your credentials (choose this or MinIO Credentials)
-        basepath: [DEPRECATED; use the bucket_folder field instead]
-            The base path to use when storing data in this bucket.
-        endpoint_url: [DEPRECATED; pass AwsClientParameters in AwsCredentials instead]
-            The URL of the S3-compatible object storage service.
         credentials: A block containing your credentials to AWS or MinIO.
         bucket_folder: A default path to a folder within the S3 bucket to use
             for reading and writing objects.
     """
 
     _logo_url = "https://images.ctfassets.net/gm98wzqotmnx/1jbV4lceHOjGgunX15lUwT/db88e184d727f721575aeb054a37e277/aws.png?h=250"  # noqa
     _block_type_name = "S3 Bucket"
     _documentation_url = (
         "https://prefecthq.github.io/prefect-aws/s3/#prefect_aws.s3.S3Bucket"  # noqa
     )
 
     bucket_name: str = Field(default=..., description="Name of your bucket.")
 
-    # TODO: remove deprecated minio_credentials after March 27, 2023
-    minio_credentials: Optional[MinIOCredentials] = Field(
-        default=None,
-        description=(
-            "[DEPRECATED; use the credentials field instead] "
-            "A block containing your credentials (choose this or "
-            "AWS Credentials)"
-        ),
-    )
-
-    # TODO: remove deprecated aws_credentials after March 27, 2023
-    aws_credentials: Optional[AwsCredentials] = Field(
-        default=None,
-        description=(
-            "[DEPRECATED; use the credentials field instead] "
-            "A block containing your credentials (choose this or "
-            "MinIO Credentials)."
-        ),
-    )
-
-    # TODO: remove deprecated basepath after March 27, 2023
-    basepath: Optional[Union[str, Path]] = Field(
-        default="",
-        description=(
-            "[DEPRECATED; use the bucket_folder field instead] "
-            "A default location to write to and read from in the S3 bucket. Defaults "
-            "to the root of the bucket."
-        ),
-    )
-
-    # TODO: remove deprecated endpoint_url after March 27, 2023
-    endpoint_url: Optional[str] = Field(
-        default=None,
-        description=(
-            "[DEPRECATED; pass AwsClientParameters in AwsCredentials instead] "
-            "URL endpoint to use for S3 compatible storage. Defaults to "
-            "standard AWS S3 endpoint."
-        ),
-    )
-
-    credentials: Optional[Union[AwsCredentials, MinIOCredentials]] = Field(
-        default=None, description="A block containing your credentials to AWS or MinIO."
+    credentials: Union[AwsCredentials, MinIOCredentials] = Field(
+        default_factory=AwsCredentials,
+        description="A block containing your credentials to AWS or MinIO.",
     )
 
     bucket_folder: str = Field(
         default="",
         description=(
             "A default path to a folder within the S3 bucket to use "
             "for reading and writing objects."
         ),
     )
 
-    @validator("basepath", pre=True)
-    def cast_pathlib(cls, value):
+    # Property to maintain compatibility with storage block based deployments
+    @property
+    def basepath(self) -> str:
         """
-        If basepath provided, it means we aren't writing to the root directory
-        of the bucket. We need to ensure that it is a valid path. This is called
-        when the S3Bucket block is instantiated.
-        """
-
-        if issubclass(value.__class__, PurePath):
-            return value.as_posix()
-        return value
+        The base path of the S3 bucket.
 
-    @validator("basepath", pre=True)
-    def deprecate_basepath(cls, value):
-        """
-        Raises deprecation warning.
+        Returns:
+            str: The base path of the S3 bucket.
         """
-        if value:
-            warnings.warn(
-                "The basepath field is deprecated and will be removed March 2023. "
-                "Please use bucket_folder instead.",
-                DeprecationWarning,
-            )
-        return value
+        return self.bucket_folder
 
-    @validator("endpoint_url", pre=True)
-    def deprecate_endpoint_url(cls, value):
-        """
-        Raises deprecation warning.
-        """
-        if value:
-            warnings.warn(
-                "The endpoint_url field is deprecated and will be removed March 2023. "
-                "Please pass it in AwsClientParameters and pass it into "
-                "the credentials block instead.",
-                DeprecationWarning,
-            )
-        return value
-
-    @root_validator(pre=True)
-    def check_credentials(cls, values):
-        """
-        Ensure exactly 1 of 2 optional credentials fields has been provided by
-        user.
-        """
-        creds_exist = bool(values.get("credentials"))
-        minio_creds_exist = bool(values.get("minio_credentials"))
-        aws_creds_exist = bool(values.get("aws_credentials"))
-
-        # if both credentials fields provided
-        if minio_creds_exist and aws_creds_exist:
-            raise ValueError("Only one set of credentials should be provided.")
-
-        if minio_creds_exist:
-            # raise deprecationwarning
-            warnings.warn(
-                "The minio_credentials field is deprecated and "
-                "will be removed March 2023. Please use credentials instead.",
-                DeprecationWarning,
-            )
-            values["credentials"] = values.get("minio_credentials")
-        elif aws_creds_exist:
-            # raise deprecationwarning
-            warnings.warn(
-                "The aws_credentials field is deprecated and "
-                "will be removed March 2023. Please use credentials instead.",
-                DeprecationWarning,
-            )
-            values["credentials"] = values.get("aws_credentials")
-
-        # if neither credentials fields provided
-        if not creds_exist and not minio_creds_exist and not aws_creds_exist:
-            raise ValueError(
-                "S3Bucket requires at least one credentials block to be provided."
-            )
-        return values
+    @basepath.setter
+    def basepath(self, value: str) -> None:
+        self.bucket_folder = value
 
     def _resolve_path(self, path: str) -> str:
 
         """
         A helper function used in write_path to join `self.basepath` and `path`.
 
         Args:
 
             path: Name of the key, e.g. "file1". Each object in your
                 bucket has a unique key (or key name).
 
         """
-        bucket_folder = self.bucket_folder or self.basepath
-        # If basepath provided, it means we won't write to the root dir of
+        # If bucket_folder provided, it means we won't write to the root dir of
         # the bucket. So we need to add it on the front of the path.
         #
         # AWS object key naming guidelines require '/' for bucket folders.
         # Get POSIX path to prevent `pathlib` from inferring '\' on Windows OS
-        path = (Path(bucket_folder) / path).as_posix() if bucket_folder else path
+        path = (
+            (Path(self.bucket_folder) / path).as_posix() if self.bucket_folder else path
+        )
 
         return path
 
     def _get_s3_client(self) -> boto3.client:
 
         """
         Authenticate MinIO credentials or AWS credentials and return an S3 client.
         This is a helper function called by read_path() or write_path().
         """
-        if self.credentials:
-            s3_client = self.credentials.get_s3_client()
-        elif self.minio_credentials:
-            s3_client = self.minio_credentials.get_s3_client()
-
-        elif self.aws_credentials:
-            s3_client = self.aws_credentials.get_s3_client()
-        else:
-            raise ValueError(
-                "S3 Bucket requires either a minio_credentials"
-                "field or an aws_credentials field."
-            )
-        return s3_client
+        return self.credentials.get_s3_client()
 
     def _get_bucket_resource(self) -> boto3.resource:
         """
         Retrieves boto3 resource object for the configured bucket
         """
-        if self.credentials:
-            params_override = (
-                self.credentials.aws_client_parameters.get_params_override()
-            )
-            if "endpoint_url" not in params_override and self.endpoint_url:
-                params_override["endpoint_url"] = self.endpoint_url
-            bucket = (
-                self.credentials.get_boto3_session()
-                .resource("s3", **params_override)
-                .Bucket(self.bucket_name)
-            )
-        elif self.minio_credentials:
-            params_override = (
-                self.minio_credentials.aws_client_parameters.get_params_override()
-            )
-            if "endpoint_url" not in params_override and self.endpoint_url:
-                params_override["endpoint_url"] = self.endpoint_url
-            bucket = (
-                self.minio_credentials.get_boto3_session()
-                .resource("s3", **params_override)
-                .Bucket(self.bucket_name)
-            )
-
-        elif self.aws_credentials:
-            params_override = (
-                self.aws_credentials.aws_client_parameters.get_params_override()
-            )
-            bucket = (
-                self.aws_credentials.get_boto3_session()
-                .resource("s3", **params_override)
-                .Bucket(self.bucket_name)
-            )
-        else:
-            raise ValueError(
-                "S3 Bucket requires either a minio_credentials"
-                "field or an aws_credentials field."
-            )
+        params_override = self.credentials.aws_client_parameters.get_params_override()
+        bucket = (
+            self.credentials.get_boto3_session()
+            .resource("s3", **params_override)
+            .Bucket(self.bucket_name)
+        )
         return bucket
 
     @sync_compatible
     async def get_directory(
         self, from_path: Optional[str] = None, local_path: Optional[str] = None
     ) -> None:
         """
@@ -486,15 +334,15 @@
 
         Args:
             from_path: Path in S3 bucket to download from. Defaults to the block's
                 configured basepath.
             local_path: Local path to download S3 contents to. Defaults to the current
                 working directory.
         """
-        bucket_folder = self.bucket_folder or self.basepath
+        bucket_folder = self.bucket_folder
         if from_path is None:
             from_path = str(bucket_folder) if bucket_folder else ""
 
         if local_path is None:
             local_path = str(Path(".").absolute())
         else:
             local_path = str(Path(local_path).expanduser())
```

### Comparing `prefect-aws-0.2.5/prefect_aws/secrets_manager.py` & `prefect-aws-0.3.0/prefect_aws/secrets_manager.py`

 * *Files 2% similar despite different names*

```diff
@@ -359,14 +359,18 @@
     Manages a secret in AWS's Secrets Manager.
 
     Attributes:
         aws_credentials: The credentials to use for authentication with AWS.
         secret_name: The name of the secret.
     """
 
+    _logo_url = "https://images.ctfassets.net/gm98wzqotmnx/1jbV4lceHOjGgunX15lUwT/db88e184d727f721575aeb054a37e277/aws.png?h=250"  # noqa
+    _block_type_name = "AWS Secret"
+    _documentation_url = "https://prefecthq.github.io/prefect-aws/secrets_manager/#prefect_aws.secrets_manager.AwsSecret"  # noqa
+
     aws_credentials: AwsCredentials
     secret_name: str = Field(default=..., description="The name of the secret.")
 
     @sync_compatible
     async def read_secret(
         self,
         version_id: str = None,
```

### Comparing `prefect-aws-0.2.5/prefect_aws.egg-info/SOURCES.txt` & `prefect-aws-0.3.0/prefect_aws.egg-info/SOURCES.txt`

 * *Files 23% similar despite different names*

```diff
@@ -17,14 +17,16 @@
 prefect_aws/secrets_manager.py
 prefect_aws.egg-info/PKG-INFO
 prefect_aws.egg-info/SOURCES.txt
 prefect_aws.egg-info/dependency_links.txt
 prefect_aws.egg-info/entry_points.txt
 prefect_aws.egg-info/requires.txt
 prefect_aws.egg-info/top_level.txt
+prefect_aws/projects/__init__.py
+prefect_aws/projects/steps.py
 tests/test_batch.py
 tests/test_block_standards.py
 tests/test_client_parameters.py
 tests/test_client_waiter.py
 tests/test_credentials.py
 tests/test_ecs.py
 tests/test_s3.py
```

### Comparing `prefect-aws-0.2.5/setup.cfg` & `prefect-aws-0.3.0/setup.cfg`

 * *Files identical despite different names*

### Comparing `prefect-aws-0.2.5/setup.py` & `prefect-aws-0.3.0/setup.py`

 * *Files identical despite different names*

### Comparing `prefect-aws-0.2.5/tests/test_batch.py` & `prefect-aws-0.3.0/tests/test_batch.py`

 * *Files identical despite different names*

### Comparing `prefect-aws-0.2.5/tests/test_block_standards.py` & `prefect-aws-0.3.0/tests/test_block_standards.py`

 * *Files identical despite different names*

### Comparing `prefect-aws-0.2.5/tests/test_client_parameters.py` & `prefect-aws-0.3.0/tests/test_client_parameters.py`

 * *Files 3% similar despite different names*

```diff
@@ -1,10 +1,11 @@
 from typing import Any, Dict
 
 import pytest
+from botocore import UNSIGNED
 from botocore.client import Config
 
 from prefect_aws.client_parameters import AwsClientParameters
 
 
 class TestAwsClientParameters:
     @pytest.mark.parametrize(
@@ -41,23 +42,25 @@
         assert result == params.get_params_override()
 
     @pytest.mark.parametrize(
         "params,result",
         [
             (
                 AwsClientParameters(
-                    config=Config(
+                    config=dict(
                         region_name="eu_west_1",
                         retries={"max_attempts": 10, "mode": "standard"},
+                        signature_version="unsigned",
                     )
                 ),
                 {
                     "config": {
                         "region_name": "eu_west_1",
                         "retries": {"max_attempts": 10, "mode": "standard"},
+                        "signature_version": UNSIGNED,
                     },
                 },
             ),
         ],
     )
     def test_with_custom_config(
         self, params: AwsClientParameters, result: Dict[str, Any]
```

### Comparing `prefect-aws-0.2.5/tests/test_client_waiter.py` & `prefect-aws-0.3.0/tests/test_client_waiter.py`

 * *Files identical despite different names*

### Comparing `prefect-aws-0.2.5/tests/test_credentials.py` & `prefect-aws-0.3.0/tests/test_credentials.py`

 * *Files identical despite different names*

### Comparing `prefect-aws-0.2.5/tests/test_ecs.py` & `prefect-aws-0.3.0/tests/test_ecs.py`

 * *Files 1% similar despite different names*

```diff
@@ -858,15 +858,14 @@
         else "override"
     )
 
 
 @pytest.mark.usefixtures("ecs_mocks")
 @pytest.mark.parametrize("default_cluster", [True, False])
 async def test_cluster(aws_credentials, default_cluster: bool):
-
     session = aws_credentials.get_boto3_session()
     ecs_client = session.client("ecs")
 
     # Construct a non-default cluster. We build this in either case since otherwise
     # there is only one cluster and there's no choice but to use the default.
     second_cluster_arn = create_test_ecs_cluster(ecs_client, "second-cluster")
     add_ec2_instance_to_ecs_cluster(session, "second-cluster")
@@ -1705,14 +1704,37 @@
             "subnets": [subnet.id],
             "assignPublicIp": "DISABLED",
         }
     }
 
 
 @pytest.mark.usefixtures("ecs_mocks")
+async def test_task_customizations_as_string(aws_credentials):
+    tc = (
+        '[{"op": "replace", "path": "/overrides/cpu", "value": "512"}, '
+        '{"op": "replace", "path": "/overrides/memory", "value": "1024"}]'
+    )
+
+    task = ECSTask(
+        aws_credentials=aws_credentials, memory=512, cpu=256, task_customizations=tc
+    )  # type: ignore
+
+    original_run_task = task._run_task
+    mock_run_task = MagicMock(side_effect=original_run_task)
+    task._run_task = mock_run_task
+
+    await run_then_stop_task(task)
+
+    overrides = mock_run_task.call_args[0][1].get("overrides")
+
+    assert overrides["memory"] == "1024"
+    assert overrides["cpu"] == "512"
+
+
+@pytest.mark.usefixtures("ecs_mocks")
 @pytest.mark.parametrize(
     "fields,prepare_inputs,expected_family",
     [
         # Default
         ({}, {}, "prefect"),
         # Only flow
         ({}, {"flow": Flow(name="foo")}, "prefect__foo"),
@@ -1840,15 +1862,14 @@
 
 
 @pytest.mark.usefixtures("ecs_mocks")
 @pytest.mark.parametrize(
     "cluster", [None, "default", "second-cluster", "second-cluster-arn"]
 )
 async def test_kill(aws_credentials, cluster: str):
-
     session = aws_credentials.get_boto3_session()
     ecs_client = session.client("ecs")
 
     # Kill requires cluster-specificity so we test with variable clusters
     second_cluster_arn = create_test_ecs_cluster(ecs_client, "second-cluster")
     add_ec2_instance_to_ecs_cluster(session, "second-cluster")
```

### Comparing `prefect-aws-0.2.5/tests/test_s3.py` & `prefect-aws-0.3.0/tests/test_s3.py`

 * *Files 1% similar despite different names*

```diff
@@ -361,57 +361,49 @@
 
     with pytest.raises(ClientError):
         await s3_bucket.read_path("test_bucket/foo/bar")
 
 
 @pytest.mark.parametrize("type_", [PureWindowsPath, PurePosixPath, str])
 @pytest.mark.parametrize("delimiter", ["\\", "/"])
-async def test_aws_basepath(s3_bucket, aws_creds_block, delimiter, type_):
-    """Test the basepath functionality."""
+async def test_aws_bucket_folder(s3_bucket, aws_creds_block, delimiter, type_):
+    """Test the bucket folder functionality."""
 
     # create a new block with a subfolder
     s3_bucket_block = S3Bucket(
         bucket_name=BUCKET_NAME,
-        aws_credentials=aws_creds_block,
-        basepath=type_(f"subfolder{delimiter}subsubfolder"),
+        credentials=aws_creds_block,
+        bucket_folder="subfolder/subsubfolder",
     )
 
     key = await s3_bucket_block.write_path("test.txt", content=b"hello")
     assert await s3_bucket_block.read_path("test.txt") == b"hello"
 
     expected: str = "subfolder/subsubfolder/test.txt"
-    if (
-        delimiter == "\\"
-        and type_ != PureWindowsPath
-        and (os.sep != "\\" and os.altsep != "\\")
-    ):
-        # In this case, \\ will not be recognized as a delimiter
-        # This case is triggered on POSIX systems
-        expected = "subfolder\\subsubfolder/test.txt"
     assert key == expected
 
 
 async def test_get_directory(
     nested_s3_bucket_structure, s3_bucket: S3Bucket, tmp_path: Path
 ):
     await s3_bucket.get_directory(local_path=str(tmp_path))
 
     assert (tmp_path / "object.txt").exists()
     assert (tmp_path / "level1" / "object_level1.txt").exists()
     assert (tmp_path / "level1" / "level2" / "object_level2.txt").exists()
     assert (tmp_path / "level1" / "level2" / "object2_level2.txt").exists()
 
 
-async def test_get_directory_respects_basepath(
+async def test_get_directory_respects_bucket_folder(
     nested_s3_bucket_structure, s3_bucket: S3Bucket, tmp_path: Path, aws_creds_block
 ):
     s3_bucket_block = S3Bucket(
         bucket_name=BUCKET_NAME,
-        aws_credentials=aws_creds_block,
-        basepath="level1/level2",
+        credentials=aws_creds_block,
+        bucket_folder="level1/level2",
     )
 
     await s3_bucket_block.get_directory(local_path=str(tmp_path))
 
     assert (len(list(tmp_path.glob("*")))) == 2
     assert (tmp_path / "object_level2.txt").exists()
     assert (tmp_path / "object2_level2.txt").exists()
@@ -534,40 +526,14 @@
     await s3_bucket.get_directory(local_path=str(tmp_path / "downloaded_files"))
 
     assert (tmp_path / "downloaded_files" / "file3.txt").exists()
     assert (tmp_path / "downloaded_files" / "file4.txt").exists()
     assert (tmp_path / "downloaded_files" / "folder2" / "file5.txt").exists()
 
 
-async def test_too_many_credentials_arguments(
-    s3_bucket, aws_creds_block, minio_creds_block
-):
-
-    """Test providing too many credentials as input."""
-    with pytest.raises(ValueError, match="Only one set of credentials should be"):
-        # create a new block with a subfolder
-        S3Bucket(
-            bucket_name=BUCKET_NAME,
-            aws_credentials=aws_creds_block,
-            minio_credentials=minio_creds_block,
-            basepath="subfolder",
-        )
-
-
-async def test_too_few_credentials_arguments(s3_bucket, aws_creds_block):
-
-    """Test providing no credentials as input."""
-    with pytest.raises(ValueError, match="S3Bucket requires at least one"):
-        # create a new block with a subfolder
-        S3Bucket(
-            bucket_name=BUCKET_NAME,
-            basepath="subfolder",
-        )
-
-
 def test_read_path_in_sync_context(s3_bucket_with_file):
     """Test that read path works in a sync context."""
     s3_bucket, key = s3_bucket_with_file
     content = s3_bucket.read_path(key)
     assert content == b"hello"
 
 
@@ -579,20 +545,19 @@
 
 
 def test_deployment_default_basepath(s3_bucket):
     deployment = Deployment(name="testing", storage=s3_bucket)
     assert deployment.location == "/"
 
 
-@pytest.mark.parametrize("type_", [str, Path])
-def test_deployment_set_basepath(aws_creds_block, type_):
+def test_deployment_set_basepath(aws_creds_block):
     s3_bucket_block = S3Bucket(
         bucket_name=BUCKET_NAME,
-        aws_credentials=aws_creds_block,
-        basepath=type_("home"),
+        credentials=aws_creds_block,
+        bucket_folder="home",
     )
     deployment = Deployment(name="testing", storage=s3_bucket_block)
     assert deployment.location == "home/"
 
 
 def test_resolve_path(s3_bucket):
     assert s3_bucket._resolve_path("") == ""
```

### Comparing `prefect-aws-0.2.5/tests/test_secrets_manager.py` & `prefect-aws-0.3.0/tests/test_secrets_manager.py`

 * *Files identical despite different names*

### Comparing `prefect-aws-0.2.5/versioneer.py` & `prefect-aws-0.3.0/versioneer.py`

 * *Files identical despite different names*

