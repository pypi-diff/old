# Comparing `tmp/redis-benchmarks-specification-0.1.8.tar.gz` & `tmp/redis-benchmarks-specification-0.1.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "redis-benchmarks-specification-0.1.8.tar", max compression
+gzip compressed data, was "redis-benchmarks-specification-0.1.9.tar", max compression
```

## Comparing `redis-benchmarks-specification-0.1.8.tar` & `redis-benchmarks-specification-0.1.9.tar`

### file list

```diff
@@ -1,31 +1,34 @@
--rw-r--r--   0        0        0    11357 2021-08-20 15:15:36.063910 redis-benchmarks-specification-0.1.8/LICENSE
--rw-r--r--   0        0        0    12229 2021-08-20 15:15:36.063910 redis-benchmarks-specification-0.1.8/Readme.md
--rw-r--r--   0        0        0     1422 2021-08-20 15:15:36.063910 redis-benchmarks-specification-0.1.8/pyproject.toml
--rw-r--r--   0        0        0      368 2021-08-20 15:15:36.063910 redis-benchmarks-specification-0.1.8/redis_benchmarks_specification/__api__/Readme.md
--rw-r--r--   0        0        0        0 2021-08-20 15:15:36.063910 redis-benchmarks-specification-0.1.8/redis_benchmarks_specification/__api__/__init__.py
--rw-r--r--   0        0        0     2542 2021-08-20 15:15:36.063910 redis-benchmarks-specification-0.1.8/redis_benchmarks_specification/__api__/api.py
--rw-r--r--   0        0        0     1955 2021-08-20 15:15:36.063910 redis-benchmarks-specification-0.1.8/redis_benchmarks_specification/__api__/app.py
--rw-r--r--   0        0        0     1618 2021-08-20 15:15:36.063910 redis-benchmarks-specification-0.1.8/redis_benchmarks_specification/__api__/schema.py
--rw-r--r--   0        0        0      111 2021-08-20 15:15:36.063910 redis-benchmarks-specification-0.1.8/redis_benchmarks_specification/__builder__/Readme.md
--rw-r--r--   0        0        0       83 2021-08-20 15:15:36.063910 redis-benchmarks-specification-0.1.8/redis_benchmarks_specification/__builder__/__init__.py
--rw-r--r--   0        0        0    12859 2021-08-20 15:15:36.063910 redis-benchmarks-specification-0.1.8/redis_benchmarks_specification/__builder__/builder.py
--rw-r--r--   0        0        0      584 2021-08-20 15:15:36.063910 redis-benchmarks-specification-0.1.8/redis_benchmarks_specification/__builder__/schema.py
--rw-r--r--   0        0        0        0 2021-08-20 15:15:36.063910 redis-benchmarks-specification-0.1.8/redis_benchmarks_specification/__common__/__init__.py
--rw-r--r--   0        0        0     2275 2021-08-20 15:15:36.063910 redis-benchmarks-specification-0.1.8/redis_benchmarks_specification/__common__/env.py
--rw-r--r--   0        0        0      834 2021-08-20 15:15:36.063910 redis-benchmarks-specification-0.1.8/redis_benchmarks_specification/__common__/package.py
--rw-r--r--   0        0        0      541 2021-08-20 15:15:36.063910 redis-benchmarks-specification-0.1.8/redis_benchmarks_specification/__common__/spec.py
--rw-r--r--   0        0        0      491 2021-08-20 15:15:36.063910 redis-benchmarks-specification-0.1.8/redis_benchmarks_specification/__init__.py
--rw-r--r--   0        0        0       83 2021-08-20 15:15:36.063910 redis-benchmarks-specification-0.1.8/redis_benchmarks_specification/__self_contained_coordinator__/__init__.py
--rw-r--r--   0        0        0     2231 2021-08-20 15:15:36.063910 redis-benchmarks-specification-0.1.8/redis_benchmarks_specification/__self_contained_coordinator__/args.py
--rw-r--r--   0        0        0    23945 2021-08-20 15:15:36.063910 redis-benchmarks-specification-0.1.8/redis_benchmarks_specification/__self_contained_coordinator__/self_contained_coordinator.py
--rw-r--r--   0        0        0        0 2021-08-20 15:15:36.063910 redis-benchmarks-specification-0.1.8/redis_benchmarks_specification/__setups__/__init__.py
--rw-r--r--   0        0        0      481 2021-08-20 15:15:36.063910 redis-benchmarks-specification-0.1.8/redis_benchmarks_specification/__setups__/topologies.py
--rw-r--r--   0        0        0      441 2021-08-20 15:15:36.063910 redis-benchmarks-specification-0.1.8/redis_benchmarks_specification/setups/builders/gcc:8.5.0-amd64-debian-buster-default.yml
--rw-r--r--   0        0        0      584 2021-08-20 15:15:36.063910 redis-benchmarks-specification-0.1.8/redis_benchmarks_specification/setups/builders/icc-2021.3.0-amd64-ubuntu18.04-default.yml
--rw-r--r--   0        0        0      597 2021-08-20 15:15:36.063910 redis-benchmarks-specification-0.1.8/redis_benchmarks_specification/setups/builders/icc-2021.3.0-amd64-ubuntu18.04-libc.yml
--rw-r--r--   0        0        0      625 2021-08-20 15:15:36.063910 redis-benchmarks-specification-0.1.8/redis_benchmarks_specification/setups/builders/icc-2021.3.0-amd64-ubuntu18.04-monotonic-clock.yml
--rw-r--r--   0        0        0      622 2021-08-20 15:15:36.063910 redis-benchmarks-specification-0.1.8/redis_benchmarks_specification/setups/platforms/aws-ec2-1node-c5.4xlarge.yml
--rw-r--r--   0        0        0     1472 2021-08-20 15:15:36.067910 redis-benchmarks-specification-0.1.8/redis_benchmarks_specification/setups/topologies/topologies.yml
--rw-r--r--   0        0        0     1149 2021-08-20 15:15:36.067910 redis-benchmarks-specification-0.1.8/redis_benchmarks_specification/test-suites/redis-benchmark-full-suite-1Mkeys-100B.yml
--rw-r--r--   0        0        0    14583 2021-08-20 15:16:53.603821 redis-benchmarks-specification-0.1.8/setup.py
--rw-r--r--   0        0        0    13445 2021-08-20 15:16:53.605612 redis-benchmarks-specification-0.1.8/PKG-INFO
+-rw-r--r--   0        0        0    11357 2021-08-21 00:42:59.313300 redis-benchmarks-specification-0.1.9/LICENSE
+-rw-r--r--   0        0        0    12229 2021-08-21 00:42:59.313300 redis-benchmarks-specification-0.1.9/Readme.md
+-rw-r--r--   0        0        0     1541 2021-08-21 00:42:59.313300 redis-benchmarks-specification-0.1.9/pyproject.toml
+-rw-r--r--   0        0        0      368 2021-08-21 00:42:59.313300 redis-benchmarks-specification-0.1.9/redis_benchmarks_specification/__api__/Readme.md
+-rw-r--r--   0        0        0        0 2021-08-21 00:42:59.313300 redis-benchmarks-specification-0.1.9/redis_benchmarks_specification/__api__/__init__.py
+-rw-r--r--   0        0        0     2542 2021-08-21 00:42:59.313300 redis-benchmarks-specification-0.1.9/redis_benchmarks_specification/__api__/api.py
+-rw-r--r--   0        0        0     2079 2021-08-21 00:42:59.313300 redis-benchmarks-specification-0.1.9/redis_benchmarks_specification/__api__/app.py
+-rw-r--r--   0        0        0      204 2021-08-21 00:42:59.317300 redis-benchmarks-specification-0.1.9/redis_benchmarks_specification/__api__/schema.py
+-rw-r--r--   0        0        0      111 2021-08-21 00:42:59.317300 redis-benchmarks-specification-0.1.9/redis_benchmarks_specification/__builder__/Readme.md
+-rw-r--r--   0        0        0       83 2021-08-21 00:42:59.317300 redis-benchmarks-specification-0.1.9/redis_benchmarks_specification/__builder__/__init__.py
+-rw-r--r--   0        0        0    13387 2021-08-21 00:42:59.317300 redis-benchmarks-specification-0.1.9/redis_benchmarks_specification/__builder__/builder.py
+-rw-r--r--   0        0        0      584 2021-08-21 00:42:59.317300 redis-benchmarks-specification-0.1.9/redis_benchmarks_specification/__builder__/schema.py
+-rw-r--r--   0        0        0       83 2021-08-21 00:42:59.317300 redis-benchmarks-specification-0.1.9/redis_benchmarks_specification/__cli__/__init__.py
+-rw-r--r--   0        0        0     4975 2021-08-21 00:42:59.317300 redis-benchmarks-specification-0.1.9/redis_benchmarks_specification/__cli__/cli.py
+-rw-r--r--   0        0        0        0 2021-08-21 00:42:59.317300 redis-benchmarks-specification-0.1.9/redis_benchmarks_specification/__common__/__init__.py
+-rw-r--r--   0        0        0     3920 2021-08-21 00:42:59.317300 redis-benchmarks-specification-0.1.9/redis_benchmarks_specification/__common__/builder_schema.py
+-rw-r--r--   0        0        0     2314 2021-08-21 00:42:59.317300 redis-benchmarks-specification-0.1.9/redis_benchmarks_specification/__common__/env.py
+-rw-r--r--   0        0        0      834 2021-08-21 00:42:59.317300 redis-benchmarks-specification-0.1.9/redis_benchmarks_specification/__common__/package.py
+-rw-r--r--   0        0        0      541 2021-08-21 00:42:59.317300 redis-benchmarks-specification-0.1.9/redis_benchmarks_specification/__common__/spec.py
+-rw-r--r--   0        0        0      491 2021-08-21 00:42:59.317300 redis-benchmarks-specification-0.1.9/redis_benchmarks_specification/__init__.py
+-rw-r--r--   0        0        0       83 2021-08-21 00:42:59.317300 redis-benchmarks-specification-0.1.9/redis_benchmarks_specification/__self_contained_coordinator__/__init__.py
+-rw-r--r--   0        0        0     2231 2021-08-21 00:42:59.317300 redis-benchmarks-specification-0.1.9/redis_benchmarks_specification/__self_contained_coordinator__/args.py
+-rw-r--r--   0        0        0    24574 2021-08-21 00:42:59.317300 redis-benchmarks-specification-0.1.9/redis_benchmarks_specification/__self_contained_coordinator__/self_contained_coordinator.py
+-rw-r--r--   0        0        0        0 2021-08-21 00:42:59.317300 redis-benchmarks-specification-0.1.9/redis_benchmarks_specification/__setups__/__init__.py
+-rw-r--r--   0        0        0      481 2021-08-21 00:42:59.317300 redis-benchmarks-specification-0.1.9/redis_benchmarks_specification/__setups__/topologies.py
+-rw-r--r--   0        0        0      441 2021-08-21 00:42:59.317300 redis-benchmarks-specification-0.1.9/redis_benchmarks_specification/setups/builders/gcc:8.5.0-amd64-debian-buster-default.yml
+-rw-r--r--   0        0        0      584 2021-08-21 00:42:59.317300 redis-benchmarks-specification-0.1.9/redis_benchmarks_specification/setups/builders/icc-2021.3.0-amd64-ubuntu18.04-default.yml
+-rw-r--r--   0        0        0      597 2021-08-21 00:42:59.317300 redis-benchmarks-specification-0.1.9/redis_benchmarks_specification/setups/builders/icc-2021.3.0-amd64-ubuntu18.04-libc.yml
+-rw-r--r--   0        0        0      625 2021-08-21 00:42:59.317300 redis-benchmarks-specification-0.1.9/redis_benchmarks_specification/setups/builders/icc-2021.3.0-amd64-ubuntu18.04-monotonic-clock.yml
+-rw-r--r--   0        0        0      622 2021-08-21 00:42:59.317300 redis-benchmarks-specification-0.1.9/redis_benchmarks_specification/setups/platforms/aws-ec2-1node-c5.4xlarge.yml
+-rw-r--r--   0        0        0     1472 2021-08-21 00:42:59.317300 redis-benchmarks-specification-0.1.9/redis_benchmarks_specification/setups/topologies/topologies.yml
+-rw-r--r--   0        0        0     1175 2021-08-21 00:42:59.317300 redis-benchmarks-specification-0.1.9/redis_benchmarks_specification/test-suites/redis-benchmark-full-suite-1Mkeys-100B.yml
+-rw-r--r--   0        0        0    14803 2021-08-21 00:44:19.814397 redis-benchmarks-specification-0.1.9/setup.py
+-rw-r--r--   0        0        0    13526 2021-08-21 00:44:19.815764 redis-benchmarks-specification-0.1.9/PKG-INFO
```

### Comparing `redis-benchmarks-specification-0.1.8/LICENSE` & `redis-benchmarks-specification-0.1.9/LICENSE`

 * *Files identical despite different names*

### Comparing `redis-benchmarks-specification-0.1.8/Readme.md` & `redis-benchmarks-specification-0.1.9/Readme.md`

 * *Files identical despite different names*

### Comparing `redis-benchmarks-specification-0.1.8/pyproject.toml` & `redis-benchmarks-specification-0.1.9/pyproject.toml`

 * *Files 13% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "redis-benchmarks-specification"
-version = "0.1.8"
+version = "0.1.9"
 description = "The Redis benchmarks specification describes the cross-language/tools requirements and expectations to foster performance and observability standards around redis related technologies. Members from both industry and academia, including organizations and individuals are encouraged to contribute."
 authors = ["filipecosta90 <filipecosta.90@gmail.com>"]
 readme = "Readme.md"
 
 [tool.poetry.dependencies]
 python = "^3.6.1"
 Flask = "^2.0.1"
@@ -15,14 +15,16 @@
 argparse = "^1.4.0"
 Flask-HTTPAuth = "^4.4.0"
 PyYAML = "^5.4.1"
 docker = "^4.4.4"
 redisbench-admin = "^0.4.16"
 psutil = "^5.8.0"
 tox-docker = "^3.0.0"
+PyGithub = "^1.55"
+GitPython = "^3.1.20"
 
 [tool.poetry.dev-dependencies]
 black = "20.8b1"
 pytest = "^5.2"
 flake8 = "^3.9.2"
 pytest-cov = "^2.12.1"
 codecov = "^2.1.12"
@@ -33,7 +35,8 @@
 requires = ["poetry-core>=1.0.0"]
 build-backend = "poetry.core.masonry.api"
 
 [tool.poetry.scripts]
 redis-benchmarks-spec-api = "redis_benchmarks_specification.__api__.api:main"
 redis-benchmarks-spec-builder = "redis_benchmarks_specification.__builder__.builder:main"
 redis-benchmarks-spec-sc-coordinator = "redis_benchmarks_specification.__self_contained_coordinator__.self_contained_coordinator:main"
+redis-benchmarks-spec-cli = "redis_benchmarks_specification.__cli__.cli:main"
```

### Comparing `redis-benchmarks-specification-0.1.8/redis_benchmarks_specification/__api__/api.py` & `redis-benchmarks-specification-0.1.9/redis_benchmarks_specification/__api__/api.py`

 * *Files identical despite different names*

### Comparing `redis-benchmarks-specification-0.1.8/redis_benchmarks_specification/__api__/app.py` & `redis-benchmarks-specification-0.1.9/redis_benchmarks_specification/__api__/app.py`

 * *Files 18% similar despite different names*

```diff
@@ -1,17 +1,19 @@
 from flask import Flask, jsonify, request
 from marshmallow import ValidationError
 from json import dumps
 import redis
 from flask_httpauth import HTTPBasicAuth
 
 from redis_benchmarks_specification.__api__.schema import (
-    commit_schema_to_stream,
     CommitSchema,
 )
+from redis_benchmarks_specification.__common__.builder_schema import (
+    commit_schema_to_stream,
+)
 from redis_benchmarks_specification.__common__.env import (
     REDIS_AUTH_SERVER_HOST,
     REDIS_AUTH_SERVER_PORT,
 )
 
 
 def create_app(conn, test_config=None):
@@ -39,28 +41,29 @@
         return result
 
     @app.route("/api/gh/redis/redis/commits", methods=["POST"])
     @auth.login_required
     def base():
         # Get Request body from JSON
         request_data = request.json
+        gh_org = "redis"
+        gh_repo = "redis"
         schema = CommitSchema()
         try:
             # Validate request body against schema data types
             result = schema.load(request_data)
         except ValidationError as err:
-            # Return a nice message if validation fails
-            return jsonify(err.messages), 400
+            err_message = err.messages
+        if result is True:
+            # Convert request body back to JSON str
+            data_now_json_str = dumps(result)
 
-        # Convert request body back to JSON str
-        data_now_json_str = dumps(result)
-
-        result, response_data, err_message = commit_schema_to_stream(
-            data_now_json_str, conn
-        )
+            result, response_data, err_message = commit_schema_to_stream(
+                data_now_json_str, conn, gh_org, gh_repo
+            )
         if result is False:
             return jsonify(err_message), 400
 
         # Send data back as JSON
         return jsonify(response_data), 200
 
     return app
```

### Comparing `redis-benchmarks-specification-0.1.8/redis_benchmarks_specification/__builder__/builder.py` & `redis-benchmarks-specification-0.1.9/redis_benchmarks_specification/__builder__/builder.py`

 * *Files 6% similar despite different names*

```diff
@@ -173,14 +173,20 @@
         if b"git_hash" in testDetails:
             git_hash = testDetails[b"git_hash"]
             logging.info("Received commit hash specifier {}.".format(git_hash))
             buffer = testDetails[b"zip_archive"]
             git_branch = None
             if b"git_branch" in testDetails:
                 git_branch = testDetails[b"git_branch"]
+            git_timestamp_ms = None
+            use_git_timestamp = False
+            if b"use_git_timestamp" in testDetails:
+                use_git_timestamp = bool(testDetails[b"use_git_timestamp"])
+            if b"git_timestamp_ms" in testDetails:
+                git_timestamp_ms = int(testDetails[b"git_timestamp_ms"].decode())
 
             for build_spec in different_build_specs:
                 build_config, id = get_build_config(builders_folder + "/" + build_spec)
                 build_config_metadata = get_build_config_metadata(build_config)
 
                 build_image = build_config["build_image"]
                 run_image = build_image
@@ -242,27 +248,30 @@
                     privileged=True,
                     working_dir="/mnt/redis/",
                     command=build_command,
                 )
                 build_stream_fields = {
                     "id": id,
                     "git_hash": git_hash,
+                    "use_git_timestamp": str(use_git_timestamp),
                     "build_image": build_image,
                     "run_image": run_image,
                     "compiler": compiler,
                     "cpp_compiler": cpp_compiler,
                     "os": build_os,
                     "arch": build_arch,
                     "build_vars": build_vars_str,
                     "build_command": build_command,
                     "metadata": json.dumps(build_config_metadata),
                     "build_artifacts": ",".join(build_artifacts),
                 }
                 if git_branch is not None:
                     build_stream_fields["git_branch"] = git_branch
+                if git_timestamp_ms is not None:
+                    build_stream_fields["git_timestamp_ms"] = git_timestamp_ms
                 for artifact in build_artifacts:
                     bin_artifact = open(
                         "{}src/{}".format(redis_temporary_dir, artifact), "rb"
                     ).read()
                     build_stream_fields[artifact] = bytes(bin_artifact)
                     build_stream_fields["{}_len_bytes".format(artifact)] = len(
                         bytes(bin_artifact)
```

### Comparing `redis-benchmarks-specification-0.1.8/redis_benchmarks_specification/__builder__/schema.py` & `redis-benchmarks-specification-0.1.9/redis_benchmarks_specification/__builder__/schema.py`

 * *Files identical despite different names*

### Comparing `redis-benchmarks-specification-0.1.8/redis_benchmarks_specification/__common__/env.py` & `redis-benchmarks-specification-0.1.9/redis_benchmarks_specification/__common__/env.py`

 * *Files 5% similar despite different names*

```diff
@@ -33,14 +33,15 @@
 )
 
 STREAM_GH_NEW_BUILD_RUNNERS_CG = os.getenv(
     "STREAM_GH_NEW_BUILD_RUNNERS_CG", "runners-cg:redis/redis/commits"
 )
 
 # host used to store the streams of events
+GH_TOKEN = os.getenv("GH_TOKEN", None)
 GH_REDIS_SERVER_HOST = os.getenv("GH_REDIS_SERVER_HOST", "localhost")
 GH_REDIS_SERVER_PORT = int(os.getenv("GH_REDIS_SERVER_PORT", "6379"))
 GH_REDIS_SERVER_AUTH = os.getenv("GH_REDIS_SERVER_AUTH", None)
 GH_REDIS_SERVER_USER = os.getenv("GH_REDIS_SERVER_USER", None)
 
 # DB used to authenticate ( read-only/non-dangerous access only )
 REDIS_AUTH_SERVER_HOST = os.getenv("REDIS_AUTH_SERVER_HOST", "localhost")
```

### Comparing `redis-benchmarks-specification-0.1.8/redis_benchmarks_specification/__common__/package.py` & `redis-benchmarks-specification-0.1.9/redis_benchmarks_specification/__common__/package.py`

 * *Files identical despite different names*

### Comparing `redis-benchmarks-specification-0.1.8/redis_benchmarks_specification/__common__/spec.py` & `redis-benchmarks-specification-0.1.9/redis_benchmarks_specification/__common__/spec.py`

 * *Files identical despite different names*

### Comparing `redis-benchmarks-specification-0.1.8/redis_benchmarks_specification/__self_contained_coordinator__/args.py` & `redis-benchmarks-specification-0.1.9/redis_benchmarks_specification/__self_contained_coordinator__/args.py`

 * *Files identical despite different names*

### Comparing `redis-benchmarks-specification-0.1.8/redis_benchmarks_specification/__self_contained_coordinator__/self_contained_coordinator.py` & `redis-benchmarks-specification-0.1.9/redis_benchmarks_specification/__self_contained_coordinator__/self_contained_coordinator.py`

 * *Files 6% similar despite different names*

```diff
@@ -278,14 +278,16 @@
             build_variant_name,
             metadata,
             build_artifacts,
             git_hash,
             git_branch,
             git_version,
             run_image,
+            use_git_timestamp,
+            git_timestamp_ms,
         ) = extract_build_info_from_streamdata(testDetails)
 
         overall_result = True
         for test_file in testsuite_spec_files:
             redis_containers = []
             client_containers = []
 
@@ -446,39 +448,43 @@
                         benchmark_duration_seconds = (
                             calculate_benchmark_duration_and_check(
                                 benchmark_end_time, benchmark_start_time
                             )
                         )
                         logging.info("output {}".format(client_container_stdout))
                         r.shutdown(save=False)
+                        datapoint_time_ms = start_time_ms
+                        if use_git_timestamp is True and git_timestamp_ms is not None:
+                            datapoint_time_ms = git_timestamp_ms
                         post_process_benchmark_results(
                             benchmark_tool,
                             local_benchmark_output_filename,
-                            start_time_ms,
+                            datapoint_time_ms,
                             start_time_str,
                             client_container_stdout,
                             None,
                         )
 
                         with open(local_benchmark_output_filename, "r") as json_file:
                             results_dict = json.load(json_file)
                             logging.info("Final JSON result {}".format(results_dict))
                         dataset_load_duration_seconds = 0
+
                         timeseries_test_sucess_flow(
                             datasink_push_results_redistimeseries,
                             git_version,
                             benchmark_config,
                             benchmark_duration_seconds,
                             dataset_load_duration_seconds,
                             None,
                             topology_spec_name,
                             None,
                             results_dict,
                             rts,
-                            start_time_ms,
+                            datapoint_time_ms,
                             test_name,
                             git_branch,
                             tf_github_org,
                             tf_github_repo,
                             tf_triggering_env,
                             metadata,
                             build_variant_name,
@@ -535,19 +541,25 @@
     logging.info(
         "Running all specified benchmarks: {}".format(" ".join([str(x) for x in files]))
     )
     return files
 
 
 def extract_build_info_from_streamdata(testDetails):
+    use_git_timestamp = False
+    git_timestamp_ms = None
     git_version = None
     git_branch = None
     metadata = None
     build_variant_name = None
     git_hash = testDetails[b"git_hash"]
+    if b"use_git_timestamp" in testDetails:
+        use_git_timestamp = bool(testDetails[b"use_git_timestamp"].decode())
+    if b"git_timestamp_ms" in testDetails:
+        git_timestamp_ms = int(testDetails[b"git_timestamp_ms"].decode())
     if b"id" in testDetails:
         build_variant_name = testDetails[b"id"]
         if type(build_variant_name) == bytes:
             build_variant_name = build_variant_name.decode()
     if b"git_branch" in testDetails:
         git_branch = testDetails[b"git_branch"]
         if type(git_branch) == bytes:
@@ -573,14 +585,16 @@
         build_variant_name,
         metadata,
         build_artifacts,
         git_hash,
         git_branch,
         git_version,
         run_image,
+        use_git_timestamp,
+        git_timestamp_ms,
     )
 
 
 def generate_cpuset_cpus(ceil_db_cpu_limit, current_cpu_pos):
     previous_cpu_pos = current_cpu_pos
     current_cpu_pos = current_cpu_pos + int(ceil_db_cpu_limit)
     db_cpuset_cpus = ",".join(
```

### Comparing `redis-benchmarks-specification-0.1.8/redis_benchmarks_specification/setups/builders/icc-2021.3.0-amd64-ubuntu18.04-default.yml` & `redis-benchmarks-specification-0.1.9/redis_benchmarks_specification/setups/builders/icc-2021.3.0-amd64-ubuntu18.04-default.yml`

 * *Files identical despite different names*

### Comparing `redis-benchmarks-specification-0.1.8/redis_benchmarks_specification/setups/builders/icc-2021.3.0-amd64-ubuntu18.04-libc.yml` & `redis-benchmarks-specification-0.1.9/redis_benchmarks_specification/setups/builders/icc-2021.3.0-amd64-ubuntu18.04-libc.yml`

 * *Files identical despite different names*

### Comparing `redis-benchmarks-specification-0.1.8/redis_benchmarks_specification/setups/builders/icc-2021.3.0-amd64-ubuntu18.04-monotonic-clock.yml` & `redis-benchmarks-specification-0.1.9/redis_benchmarks_specification/setups/builders/icc-2021.3.0-amd64-ubuntu18.04-monotonic-clock.yml`

 * *Files identical despite different names*

### Comparing `redis-benchmarks-specification-0.1.8/redis_benchmarks_specification/setups/platforms/aws-ec2-1node-c5.4xlarge.yml` & `redis-benchmarks-specification-0.1.9/redis_benchmarks_specification/setups/platforms/aws-ec2-1node-c5.4xlarge.yml`

 * *Files identical despite different names*

### Comparing `redis-benchmarks-specification-0.1.8/redis_benchmarks_specification/setups/topologies/topologies.yml` & `redis-benchmarks-specification-0.1.9/redis_benchmarks_specification/setups/topologies/topologies.yml`

 * *Files identical despite different names*

### Comparing `redis-benchmarks-specification-0.1.8/redis_benchmarks_specification/test-suites/redis-benchmark-full-suite-1Mkeys-100B.yml` & `redis-benchmarks-specification-0.1.9/redis_benchmarks_specification/test-suites/redis-benchmark-full-suite-1Mkeys-100B.yml`

 * *Files 13% similar despite different names*

```diff
@@ -28,15 +28,16 @@
   tool: redis-benchmark
   min-tool-version: "6.2.0"
   parameters:
     - clients: 50
     - requests: 1000000
     - threads: 3
     - pipeline: 1
-    - r: 1000000
+    - keyspacelen: 1000000
+    - size: 100
   resources:
     requests:
       cpus: "3"
       memory: "2g"
 exporter:
   redistimeseries:
     break_by:
```

### Comparing `redis-benchmarks-specification-0.1.8/setup.py` & `redis-benchmarks-specification-0.1.9/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,28 +1,31 @@
 # -*- coding: utf-8 -*-
 from setuptools import setup
 
 packages = \
 ['redis_benchmarks_specification',
  'redis_benchmarks_specification.__api__',
  'redis_benchmarks_specification.__builder__',
+ 'redis_benchmarks_specification.__cli__',
  'redis_benchmarks_specification.__common__',
  'redis_benchmarks_specification.__self_contained_coordinator__',
  'redis_benchmarks_specification.__setups__']
 
 package_data = \
 {'': ['*'],
  'redis_benchmarks_specification': ['setups/builders/*',
                                     'setups/platforms/*',
                                     'setups/topologies/*',
                                     'test-suites/*']}
 
 install_requires = \
 ['Flask-HTTPAuth>=4.4.0,<5.0.0',
  'Flask>=2.0.1,<3.0.0',
+ 'GitPython>=3.1.20,<4.0.0',
+ 'PyGithub>=1.55,<2.0',
  'PyYAML>=5.4.1,<6.0.0',
  'Werkzeug>=2.0.1,<3.0.0',
  'argparse>=1.4.0,<2.0.0',
  'docker>=4.4.4,<5.0.0',
  'flask-restx>=0.5.0,<0.6.0',
  'marshmallow>=3.12.2,<4.0.0',
  'psutil>=5.8.0,<6.0.0',
@@ -31,20 +34,22 @@
  'tox-docker>=3.0.0,<4.0.0']
 
 entry_points = \
 {'console_scripts': ['redis-benchmarks-spec-api = '
                      'redis_benchmarks_specification.__api__.api:main',
                      'redis-benchmarks-spec-builder = '
                      'redis_benchmarks_specification.__builder__.builder:main',
+                     'redis-benchmarks-spec-cli = '
+                     'redis_benchmarks_specification.__cli__.cli:main',
                      'redis-benchmarks-spec-sc-coordinator = '
                      'redis_benchmarks_specification.__self_contained_coordinator__.self_contained_coordinator:main']}
 
 setup_kwargs = {
     'name': 'redis-benchmarks-specification',
-    'version': '0.1.8',
+    'version': '0.1.9',
     'description': 'The Redis benchmarks specification describes the cross-language/tools requirements and expectations to foster performance and observability standards around redis related technologies. Members from both industry and academia, including organizations and individuals are encouraged to contribute.',
     'long_description': "\n[![codecov](https://codecov.io/gh/filipecosta90/redis-benchmarks-specification/branch/main/graph/badge.svg?token=GS64MV1H4W)](https://codecov.io/gh/filipecosta90/redis-benchmarks-specification)\n[![CI tests](https://github.com/filipecosta90/redis-benchmarks-specification/actions/workflows/tox.yml/badge.svg)](https://github.com/filipecosta90/redis-benchmarks-specification/actions/workflows/tox.yml)\n[![PyPI version](https://badge.fury.io/py/redis-benchmarks-specification.svg)](https://badge.fury.io/py/redis-benchmarks-specification)\n## Benchmark specifications goal\n\nThe Redis benchmarks specification describes the cross-language/tools requirements and expectations to foster performance and observability standards around redis related technologies. \n\nMembers from both industry and academia, including organizations and individuals are encouraged to contribute. \n\nCurrently, the following members actively support this project:\n\n- [Redis Ltd.](https://redis.com/): providing steady-stable infrastructure platform to run the benchmark suite. Supporting the active development of this project within the company.\n\n\n## Scope \n\nThis repo aims to provide Redis related benchmark standards and methodologies for:\n\n- Management of benchmark data and specifications across different setups\n\n- Running benchmarks and recording results\n\n- Exporting performance results in several formats (CSV, RedisTimeSeries, JSON)\n\n- **[SOON]** Finding on-cpu, off-cpu, io, and threading performance problems by attaching profiling tools/probers ( perf (a.k.a. perf_events), bpf tooling, vtune )\n\n- **[SOON]** Finding performance problems by attaching telemetry probes\n\nCurrent supported benchmark tools:\n\n- [redis-benchmark](https://github.com/redis/redis)\n- [SOON][memtier_benchmark](https://github.com/RedisLabs/memtier_benchmark)\n- [SOON][redis-benchmark-go](https://github.com/filipecosta90/redis-benchmark-go)\n\n## Architecture diagram\n\n```                                                                                    \n                                                                                      \n                                                                                      \n┌──────────────────────────────────────┐                                              \n│1) gh.com/redis/redis update          │                                              \n│   - git_repo: github.com/redis/redis │                                              \n│   - git_hash: 459c3a                 │                                              \n│   - git_branch: unstable             │                                              \n└─────────────────┬────────────────────┘                                              \n                  │                                                                   \n                  │      ┌───────────────────────────────────┐                        \n                  │      │HTTP POST                          │                        \n                  └──────┤<domain>/api/gh/redis/redis/commit │──┐                     \n                         └───────────────────────────────────┘  │                     \n                                                                │                     \n                                                                ▼                     \n                                          ┌──────────────────────────────────────────┐\n                                          │2) api                                    │\n                                          │  - Converts the HTTP info into an stream │\n                                          │entry                                     │\n                                          │  - XADD stream:redis:redis:commit <...>  │\n                                          │                                          │\n                                          └─────────────────────┬────────────────────┘\n                                                                │                     \n                                                                │                     \n                                                                │                     \n                                                                │ ┌────┐              \n                    .─────────────────────────────────────.     │ │push│              \n        ┌─────┐ ┌ ▶(  2.1 ) stream of build events         )◀───┘ └────┘              \n        │pull │     `─────────────────────────────────────'                           \n        └─────┘ │                                                                     \n                                                                                      \n                │                       ┌────────────────────────────────────────────┐\n                 ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─│2.2) build_agent                            │\n                                        │   - based on setup platforms               │\n                                        │   - build different required redis         │\n                                        │artifacts                                   │\n                                        └───────────────────────┬────────────────────┘\n                                                                │                     \n                                                                │                     \n                                                                │ ┌────┐              \n                   .─────────────────────────────────────.      │ │push│              \n        ┌─────┐ ─▶(   2.3 ) stream of artifact benchmarks )◀────┘ └────┘              \n        │pull ││   `─────────────────────────────────────'                            \n        └─────┘                                                                       \n               │                                                                      \n                                        ┌────────────────────────────────────────────┐\n               │                        │                                            │\n                                        │3) benchmark_coordinator                    │\n               │                        │   - based on test-suites and setups:       │\n                                        │      - Trigger env setup                   │\n               └ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─│      - 3.1 ) Trigger topology setup        │\n                                        │      - 3.2 ) Run benchmarks                │\n                                        │      - Record results into datasinks       │\n                                        │                                            │\n                                        └────────────────────────────────────────────┘\n```                                              \n\nIn a very brief description, github.com/redis/redis upstream changes trigger an HTTP API call containing the\nrelevant git information. \n\nThe HTTP request is then converted into an event ( tracked within redis ) that will trigger multiple build variants requests based upon the distinct platforms described in [`platforms`](redis_benchmarks_specification/setups/platforms/). \n\nAs soon as a new build variant request is received, the build agent ([`redis-benchmarks-spec-builder`](https://github.com/filipecosta90/redis-benchmarks-specification/tree/main/redis_benchmarks_specification/__builder__/)) prepares the artifact(s) and proceeds into adding an artifact benchmark event so that the benchmark coordinator ([`redis-benchmarks-spec-sc-coordinator`](https://github.com/filipecosta90/redis-benchmarks-specification/tree/main/redis_benchmarks_specification/__self_contained_coordinator__/))  can deploy/manage the required infrastructure and DB topologies, run the benchmark, and export the performance results.\n## Directory layout\n\n### Specifications \n\n  The following is a high level status report for currently available specs.\n\n* `redis_benchmarks_specification`\n  * [`test-suites`](https://github.com/filipecosta90/redis-benchmarks-specification/tree/main/redis_benchmarks_specification/test-suites/): contains the benchmark suites definitions, specifying the target redis topology, the tested commands, the benchmark utility to use (the client), and if required the preloading dataset steps.\n  \n* `redis_benchmarks_specification/setups`\n  * [`platforms`](https://github.com/filipecosta90/redis-benchmarks-specification/tree/main/redis_benchmarks_specification/setups/platforms/): contains the standard platforms considered to provide steady stable results, and to represent common deployment targets.\n  * [`topologies`](https://github.com/filipecosta90/redis-benchmarks-specification/tree/main/redis_benchmarks_specification/setups/topologies/): contains the standard deployment topologies definition with the associated minimum specs to enable the topology definition.\n  * [`builders`](https://github.com/filipecosta90/redis-benchmarks-specification/tree/main/redis_benchmarks_specification/setups/builders/): contains the build environment variations, that enable to build Redis with different compilers, compiler flags, libraries, etc...\n\n### Spec tool implementations\n\n  The following is a high level status report for currently available spec implementations.\n\n* **STATUS: Experimental** [`redis-benchmarks-spec-api`](https://github.com/filipecosta90/redis-benchmarks-specification/tree/main/redis_benchmarks_specification/__api__/) : contains the API that translates the POST HTTP request that was triggered by github.com/redis/redis upstream changes, and fetches the relevant git/source info and coverts it into an event ( tracked within redis ).\n\n* **STATUS: Experimental** [`redis-benchmarks-spec-builder`](https://github.com/filipecosta90/redis-benchmarks-specification/tree/main/redis_benchmarks_specification/__builder__/): contains the benchmark build agent utility that receives an event indicating a new build variant, generates the required redis binaries to test, and triggers the benchmark run on the listening agents.\n* **STATUS: Experimental** [`redis-benchmarks-spec-sc-coordinator`](https://github.com/filipecosta90/redis-benchmarks-specification/tree/main/redis_benchmarks_specification/__self_contained_coordinator__/): contains the coordinator utility that listens for benchmark suite run requests and setups the required steps to spin the actual benchmark topologies and to trigger the actual benchmarks.\n\n\n## Contributing guidelines\n\n### Adding new test suites\n\nTBD\n\n### Adding new topologies\n\nTBD\n\n### Adding new test platforms\n\nTBD\n\n## License\n\nredis-benchmark-specifications is distributed under the Apache 2 license - see [LICENSE](LICENSE)",
     'author': 'filipecosta90',
     'author_email': 'filipecosta.90@gmail.com',
     'maintainer': None,
     'maintainer_email': None,
     'url': None,
```

### Comparing `redis-benchmarks-specification-0.1.8/PKG-INFO` & `redis-benchmarks-specification-0.1.9/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,20 +1,22 @@
 Metadata-Version: 2.1
 Name: redis-benchmarks-specification
-Version: 0.1.8
+Version: 0.1.9
 Summary: The Redis benchmarks specification describes the cross-language/tools requirements and expectations to foster performance and observability standards around redis related technologies. Members from both industry and academia, including organizations and individuals are encouraged to contribute.
 Author: filipecosta90
 Author-email: filipecosta.90@gmail.com
 Requires-Python: >=3.6.1,<4.0.0
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Requires-Dist: Flask (>=2.0.1,<3.0.0)
 Requires-Dist: Flask-HTTPAuth (>=4.4.0,<5.0.0)
+Requires-Dist: GitPython (>=3.1.20,<4.0.0)
+Requires-Dist: PyGithub (>=1.55,<2.0)
 Requires-Dist: PyYAML (>=5.4.1,<6.0.0)
 Requires-Dist: Werkzeug (>=2.0.1,<3.0.0)
 Requires-Dist: argparse (>=1.4.0,<2.0.0)
 Requires-Dist: docker (>=4.4.4,<5.0.0)
 Requires-Dist: flask-restx (>=0.5.0,<0.6.0)
 Requires-Dist: marshmallow (>=3.12.2,<4.0.0)
 Requires-Dist: psutil (>=5.8.0,<6.0.0)
```

