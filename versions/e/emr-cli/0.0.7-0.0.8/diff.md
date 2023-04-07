# Comparing `tmp/emr_cli-0.0.7.tar.gz` & `tmp/emr_cli-0.0.8.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "emr_cli-0.0.7.tar", max compression
+gzip compressed data, was "emr_cli-0.0.8.tar", max compression
```

## Comparing `emr_cli-0.0.7.tar` & `emr_cli-0.0.8.tar`

### file list

```diff
@@ -1,23 +1,23 @@
--rw-r--r--   0        0        0    10173 2023-03-31 22:59:51.144074 emr_cli-0.0.7/LICENSE
--rw-r--r--   0        0        0     4755 2023-03-31 22:59:51.144074 emr_cli-0.0.7/README.md
--rw-r--r--   0        0        0      593 2023-03-31 23:00:11.475900 emr_cli-0.0.7/pyproject.toml
--rw-r--r--   0        0        0      976 2023-03-31 22:59:51.144074 emr_cli-0.0.7/src/emr_cli/config.py
--rw-r--r--   0        0        0     1286 2023-03-31 22:59:51.144074 emr_cli-0.0.7/src/emr_cli/deployments/__init__.py
--rw-r--r--   0        0        0     2474 2023-03-31 22:59:51.144074 emr_cli-0.0.7/src/emr_cli/deployments/emr_ec2.py
--rw-r--r--   0        0        0    10637 2023-03-31 22:59:51.144074 emr_cli-0.0.7/src/emr_cli/deployments/emr_serverless.py
--rw-r--r--   0        0        0     6732 2023-03-31 22:59:51.144074 emr_cli-0.0.7/src/emr_cli/emr_cli.py
--rw-r--r--   0        0        0     1564 2023-03-31 22:59:51.144074 emr_cli-0.0.7/src/emr_cli/packaging/detector.py
--rw-r--r--   0        0        0     1905 2023-03-31 22:59:51.144074 emr_cli-0.0.7/src/emr_cli/packaging/python_files_project.py
--rw-r--r--   0        0        0     3877 2023-03-31 22:59:51.144074 emr_cli-0.0.7/src/emr_cli/packaging/python_poetry_project.py
--rw-r--r--   0        0        0     3704 2023-03-31 22:59:51.144074 emr_cli-0.0.7/src/emr_cli/packaging/python_project.py
--rw-r--r--   0        0        0      856 2023-03-31 22:59:51.144074 emr_cli-0.0.7/src/emr_cli/packaging/simple_project.py
--rw-r--r--   0        0        0     1101 2023-03-31 22:59:51.144074 emr_cli-0.0.7/src/emr_cli/templates/poetry/README.md
--rw-r--r--   0        0        0      413 2023-03-31 22:59:51.144074 emr_cli-0.0.7/src/emr_cli/templates/poetry/pyproject.toml
--rw-r--r--   0        0        0        6 2023-03-31 22:59:51.144074 emr_cli-0.0.7/src/emr_cli/templates/pyspark/.dockerignore
--rw-r--r--   0        0        0       12 2023-03-31 22:59:51.144074 emr_cli-0.0.7/src/emr_cli/templates/pyspark/.gitignore
--rw-r--r--   0        0        0     2680 2023-03-31 22:59:51.144074 emr_cli-0.0.7/src/emr_cli/templates/pyspark/Dockerfile
--rw-r--r--   0        0        0      458 2023-03-31 22:59:51.144074 emr_cli-0.0.7/src/emr_cli/templates/pyspark/entrypoint.py
--rw-r--r--   0        0        0     3369 2023-03-31 22:59:51.144074 emr_cli-0.0.7/src/emr_cli/templates/pyspark/jobs/extreme_weather.py
--rw-r--r--   0        0        0      175 2023-03-31 22:59:51.144074 emr_cli-0.0.7/src/emr_cli/templates/pyspark/pyproject.toml
--rw-r--r--   0        0        0     2619 2023-03-31 22:59:51.144074 emr_cli-0.0.7/src/emr_cli/utils/__init__.py
--rw-r--r--   0        0        0     5543 1970-01-01 00:00:00.000000 emr_cli-0.0.7/PKG-INFO
+-rw-r--r--   0        0        0    10173 2023-04-06 23:53:41.013939 emr_cli-0.0.8/LICENSE
+-rw-r--r--   0        0        0     4755 2023-04-06 23:53:41.013939 emr_cli-0.0.8/README.md
+-rw-r--r--   0        0        0      593 2023-04-06 23:53:59.558425 emr_cli-0.0.8/pyproject.toml
+-rw-r--r--   0        0        0      976 2023-04-06 23:53:41.013939 emr_cli-0.0.8/src/emr_cli/config.py
+-rw-r--r--   0        0        0     1286 2023-04-06 23:53:41.013939 emr_cli-0.0.8/src/emr_cli/deployments/__init__.py
+-rw-r--r--   0        0        0     5650 2023-04-06 23:53:41.017939 emr_cli-0.0.8/src/emr_cli/deployments/emr_ec2.py
+-rw-r--r--   0        0        0    10964 2023-04-06 23:53:41.017939 emr_cli-0.0.8/src/emr_cli/deployments/emr_serverless.py
+-rw-r--r--   0        0        0     6940 2023-04-06 23:53:41.017939 emr_cli-0.0.8/src/emr_cli/emr_cli.py
+-rw-r--r--   0        0        0     1564 2023-04-06 23:53:41.017939 emr_cli-0.0.8/src/emr_cli/packaging/detector.py
+-rw-r--r--   0        0        0     1905 2023-04-06 23:53:41.017939 emr_cli-0.0.8/src/emr_cli/packaging/python_files_project.py
+-rw-r--r--   0        0        0     3877 2023-04-06 23:53:41.017939 emr_cli-0.0.8/src/emr_cli/packaging/python_poetry_project.py
+-rw-r--r--   0        0        0     3704 2023-04-06 23:53:41.017939 emr_cli-0.0.8/src/emr_cli/packaging/python_project.py
+-rw-r--r--   0        0        0      856 2023-04-06 23:53:41.017939 emr_cli-0.0.8/src/emr_cli/packaging/simple_project.py
+-rw-r--r--   0        0        0     1101 2023-04-06 23:53:41.017939 emr_cli-0.0.8/src/emr_cli/templates/poetry/README.md
+-rw-r--r--   0        0        0      413 2023-04-06 23:53:41.017939 emr_cli-0.0.8/src/emr_cli/templates/poetry/pyproject.toml
+-rw-r--r--   0        0        0        6 2023-04-06 23:53:41.017939 emr_cli-0.0.8/src/emr_cli/templates/pyspark/.dockerignore
+-rw-r--r--   0        0        0       12 2023-04-06 23:53:41.017939 emr_cli-0.0.8/src/emr_cli/templates/pyspark/.gitignore
+-rw-r--r--   0        0        0     2680 2023-04-06 23:53:41.017939 emr_cli-0.0.8/src/emr_cli/templates/pyspark/Dockerfile
+-rw-r--r--   0        0        0      458 2023-04-06 23:53:41.017939 emr_cli-0.0.8/src/emr_cli/templates/pyspark/entrypoint.py
+-rw-r--r--   0        0        0     3369 2023-04-06 23:53:41.017939 emr_cli-0.0.8/src/emr_cli/templates/pyspark/jobs/extreme_weather.py
+-rw-r--r--   0        0        0      175 2023-04-06 23:53:41.017939 emr_cli-0.0.8/src/emr_cli/templates/pyspark/pyproject.toml
+-rw-r--r--   0        0        0     2619 2023-04-06 23:53:41.017939 emr_cli-0.0.8/src/emr_cli/utils/__init__.py
+-rw-r--r--   0        0        0     5543 1970-01-01 00:00:00.000000 emr_cli-0.0.8/PKG-INFO
```

### Comparing `emr_cli-0.0.7/LICENSE` & `emr_cli-0.0.8/LICENSE`

 * *Files identical despite different names*

### Comparing `emr_cli-0.0.7/README.md` & `emr_cli-0.0.8/README.md`

 * *Files identical despite different names*

### Comparing `emr_cli-0.0.7/pyproject.toml` & `emr_cli-0.0.8/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "emr-cli"
-version = "v0.0.7"
+version = "v0.0.8"
 description = "A command-line interface for packaging, deploying, and running your EMR Serverless Spark jobs."
 authors = ["Amazon EMR <emr-developer-advocates@amazon.com>"]
 license = "Apache-2.0"
 readme = "README.md"
 
 [tool.poetry.dependencies]
 python = "^3.7"
```

### Comparing `emr_cli-0.0.7/src/emr_cli/config.py` & `emr_cli-0.0.8/src/emr_cli/config.py`

 * *Files identical despite different names*

### Comparing `emr_cli-0.0.7/src/emr_cli/deployments/__init__.py` & `emr_cli-0.0.8/src/emr_cli/deployments/__init__.py`

 * *Files identical despite different names*

### Comparing `emr_cli-0.0.7/src/emr_cli/deployments/emr_serverless.py` & `emr_cli-0.0.8/src/emr_cli/deployments/emr_serverless.py`

 * *Files 3% similar despite different names*

```diff
@@ -219,15 +219,23 @@
 
     def run_job(
         self,
         job_name: str,
         job_args: Optional[List[str]] = None,
         spark_submit_opts: Optional[str] = None,
         wait: bool = True,
+        show_logs: bool = False,
     ):
+        if show_logs:
+            raise RuntimeError(
+                "--show-stdout is not compatible with EMR Serverless (yet).\n"
+                + "Please 👍 this GitHub issue to voice your support: "
+                + "https://github.com/awslabs/amazon-emr-cli/issues/11"
+            )
+
         jobDriver = {
             "sparkSubmit": {
                 "entryPoint": self.dp.entrypoint_uri(),
             }
         }
         spark_submit_parameters = self.dp.spark_submit_parameters().params_for(
             "emr_serverless"
```

#### encoding

```diff
@@ -1 +1 @@
-us-ascii
+utf-8
```

### Comparing `emr_cli-0.0.7/src/emr_cli/emr_cli.py` & `emr_cli-0.0.8/src/emr_cli/emr_cli.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,7 +1,8 @@
+from sys import is_finalizing
 import click
 from emr_cli.config import ConfigReader, ConfigWriter
 from emr_cli.deployments.emr_ec2 import EMREC2
 from emr_cli.packaging.detector import ProjectDetector
 from emr_cli.utils import console_log
 
 from .deployments.emr_serverless import Bootstrap, EMRServerless
@@ -149,29 +150,35 @@
 @click.option(
     "--entry-point",
     type=click.Path(exists=True, dir_okay=False, allow_dash=False),
     help="Python or Jar file for the main entrypoint",
 )
 @click.option("--job-role", help="IAM Role ARN to use for the job execution")
 @click.option("--wait", default=False, is_flag=True, help="Wait for job to finish")
-@click.option("--s3-code-uri", help="Where to copy code artifacts to")
+@click.option("--s3-code-uri", help="Where to copy/run code artifacts to/from")
 @click.option("--job-name", help="The name of the job", default="emr-cli job")
 @click.option(
     "--job-args",
     help="Comma-delimited string of arguments to be passed to Spark job",
     default=None,
 )
 @click.option(
     "--spark-submit-opts",
     help="String of spark-submit options",
     default=None,
 )
 @click.option(
     "--build",
-    help="Do not package and deploy the job assets",
+    help="Package and deploy job artifacts",
+    default=False,
+    is_flag=True,
+)
+@click.option(
+    "--show-stdout",
+    help="Show the stdout of the job after it's finished",
     default=False,
     is_flag=True,
 )
 @click.pass_obj
 def run(
     project,
     application_id,
@@ -180,14 +187,15 @@
     job_role,
     wait,
     s3_code_uri,
     job_name,
     job_args,
     spark_submit_opts,
     build,
+    show_stdout,
 ):
     """
     Run a project on EMR, optionally build and deploy
     """
     # Either a cluster or applciation ID must be specified
     if cluster_id is None and application_id is None:
         raise click.BadArgumentUsage(
@@ -212,22 +220,22 @@
             raise click.BadArgumentUsage(
                 "--entry-point and --job-role are required if --application-id is used."
             )
 
         if job_args:
             job_args = job_args.split(",")
         emrs = EMRServerless(application_id, job_role, p)
-        emrs.run_job(job_name, job_args, spark_submit_opts, wait)
+        emrs.run_job(job_name, job_args, spark_submit_opts, wait, show_stdout)
 
     # cluster_id indicates EMR on EC2 job
     if cluster_id is not None:
         if job_args:
             job_args = job_args.split(",")
         emr = EMREC2(cluster_id, p)
-        emr.run_job(job_name, job_args, wait)
+        emr.run_job(job_name, job_args, wait, show_stdout)
 
 
 cli.add_command(package)
 cli.add_command(deploy)
 cli.add_command(run)
 cli.add_command(init)
 cli.add_command(bootstrap)
```

### Comparing `emr_cli-0.0.7/src/emr_cli/packaging/detector.py` & `emr_cli-0.0.8/src/emr_cli/packaging/detector.py`

 * *Files identical despite different names*

### Comparing `emr_cli-0.0.7/src/emr_cli/packaging/python_files_project.py` & `emr_cli-0.0.8/src/emr_cli/packaging/python_files_project.py`

 * *Files identical despite different names*

### Comparing `emr_cli-0.0.7/src/emr_cli/packaging/python_poetry_project.py` & `emr_cli-0.0.8/src/emr_cli/packaging/python_poetry_project.py`

 * *Files identical despite different names*

### Comparing `emr_cli-0.0.7/src/emr_cli/packaging/python_project.py` & `emr_cli-0.0.8/src/emr_cli/packaging/python_project.py`

 * *Files identical despite different names*

### Comparing `emr_cli-0.0.7/src/emr_cli/packaging/simple_project.py` & `emr_cli-0.0.8/src/emr_cli/packaging/simple_project.py`

 * *Files identical despite different names*

### Comparing `emr_cli-0.0.7/src/emr_cli/templates/poetry/README.md` & `emr_cli-0.0.8/src/emr_cli/templates/poetry/README.md`

 * *Files identical despite different names*

### Comparing `emr_cli-0.0.7/src/emr_cli/templates/pyspark/Dockerfile` & `emr_cli-0.0.8/src/emr_cli/templates/pyspark/Dockerfile`

 * *Files identical despite different names*

### Comparing `emr_cli-0.0.7/src/emr_cli/templates/pyspark/jobs/extreme_weather.py` & `emr_cli-0.0.8/src/emr_cli/templates/pyspark/jobs/extreme_weather.py`

 * *Files identical despite different names*

### Comparing `emr_cli-0.0.7/src/emr_cli/utils/__init__.py` & `emr_cli-0.0.8/src/emr_cli/utils/__init__.py`

 * *Files identical despite different names*

### Comparing `emr_cli-0.0.7/PKG-INFO` & `emr_cli-0.0.8/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: emr-cli
-Version: 0.0.7
+Version: 0.0.8
 Summary: A command-line interface for packaging, deploying, and running your EMR Serverless Spark jobs.
 License: Apache-2.0
 Author: Amazon EMR
 Author-email: emr-developer-advocates@amazon.com
 Requires-Python: >=3.7,<4.0
 Classifier: License :: OSI Approved :: Apache Software License
 Classifier: Programming Language :: Python :: 3
```

