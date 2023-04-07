# Comparing `tmp/pybiolib-1.1.91.tar.gz` & `tmp/pybiolib-1.1.94.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pybiolib-1.1.91.tar", max compression
+gzip compressed data, was "pybiolib-1.1.94.tar", max compression
```

## Comparing `pybiolib-1.1.91.tar` & `pybiolib-1.1.94.tar`

### file list

```diff
@@ -1,96 +1,96 @@
--rw-r--r--   0        0        0     1067 2022-07-12 10:55:26.377398 pybiolib-1.1.91/LICENSE
--rw-r--r--   0        0        0      369 2022-07-12 10:55:26.377398 pybiolib-1.1.91/README.md
--rw-r--r--   0        0        0     1923 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/__init__.py
--rw-r--r--   0        0        0       78 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/api/__init__.py
--rw-r--r--   0        0        0     1643 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/api/client.py
--rw-r--r--   0        0        0       37 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/app/__init__.py
--rw-r--r--   0        0        0     4264 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/app/app.py
--rw-r--r--   0        0        0     3162 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/app/app_result.py
--rw-r--r--   0        0        0     4099 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/app/utils.py
--rw-r--r--   0        0        0      182 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/biolib_api_client/__init__.py
--rw-r--r--   0        0        0     5574 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/biolib_api_client/api_client.py
--rw-r--r--   0        0        0     2355 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/biolib_api_client/app_types.py
--rw-r--r--   0        0        0     1668 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/biolib_api_client/auth.py
--rw-r--r--   0        0        0      580 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/biolib_api_client/biolib_account_api.py
--rw-r--r--   0        0        0     2859 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/biolib_api_client/biolib_app_api.py
--rw-r--r--   0        0        0     9165 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/biolib_api_client/biolib_job_api.py
--rw-r--r--   0        0        0     2646 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/biolib_api_client/biolib_large_file_system_api.py
--rw-r--r--   0        0        0      123 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/biolib_api_client/common_types.py
--rw-r--r--   0        0        0     1205 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/biolib_api_client/job_types.py
--rw-r--r--   0        0        0      493 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/biolib_api_client/lfs_types.py
--rw-r--r--   0        0        0      635 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/biolib_api_client/user_state.py
--rw-r--r--   0        0        0      303 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/biolib_binary_format/__init__.py
--rw-r--r--   0        0        0      959 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/biolib_binary_format/base_bbf_package.py
--rw-r--r--   0        0        0      154 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/biolib_binary_format/common_types.py
--rw-r--r--   0        0        0     6450 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/biolib_binary_format/encrypted_module_output.py
--rw-r--r--   0        0        0     2594 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/biolib_binary_format/module_input.py
--rw-r--r--   0        0        0     2452 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/biolib_binary_format/module_output.py
--rw-r--r--   0        0        0     2269 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/biolib_binary_format/rsa_encrypted_aes_package.py
--rw-r--r--   0        0        0     1125 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/biolib_binary_format/saved_job.py
--rw-r--r--   0        0        0     1023 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/biolib_binary_format/stdout_and_stderr.py
--rw-r--r--   0        0        0      853 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/biolib_binary_format/system_exception.py
--rw-r--r--   0        0        0     1191 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/biolib_binary_format/system_status_update.py
--rw-r--r--   0        0        0     6887 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/biolib_binary_format/unencrypted_module_output.py
--rw-r--r--   0        0        0     3595 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/biolib_binary_format/utils.py
--rw-r--r--   0        0        0     1121 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/biolib_docker_client/__init__.py
--rw-r--r--   0        0        0      381 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/biolib_errors.py
--rw-r--r--   0        0        0     2854 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/biolib_logging.py
--rw-r--r--   0        0        0    10219 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/biolib_push.py
--rw-r--r--   0        0        0     1029 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/biolib_singularity_client/__init__.py
--rw-r--r--   0        0        0    11204 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/cli.py
--rw-r--r--   0        0        0     8859 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/cli_utils.py
--rw-r--r--   0        0        0       45 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/compute_node/.gitignore
--rw-r--r--   0        0        0        0 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/compute_node/__init__.py
--rw-r--r--   0        0        0       67 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/compute_node/cloud_utils/__init__.py
--rw-r--r--   0        0        0     6976 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/compute_node/cloud_utils/cloud_utils.py
--rw-r--r--   0        0        0       71 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/compute_node/job_worker/__init__.py
--rw-r--r--   0        0        0     3531 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/compute_node/job_worker/cache_state.py
--rw-r--r--   0        0        0      922 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/compute_node/job_worker/cache_types.py
--rw-r--r--   0        0        0     6517 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/compute_node/job_worker/docker_image_cache.py
--rw-r--r--   0        0        0      315 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/compute_node/job_worker/executors/__init__.py
--rw-r--r--   0        0        0      448 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/compute_node/job_worker/executors/base_executor.py
--rw-r--r--   0        0        0    21198 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/compute_node/job_worker/executors/docker_executor.py
--rw-r--r--   0        0        0      122 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/compute_node/job_worker/executors/docker_types.py
--rw-r--r--   0        0        0       91 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/compute_node/job_worker/executors/remote/__init__.py
--rw-r--r--   0        0        0     1842 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/compute_node/job_worker/executors/remote/remote_executor.py
--rw-r--r--   0        0        0    13537 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/compute_node/job_worker/executors/singularity_executor.py
--rw-r--r--   0        0        0        0 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/compute_node/job_worker/executors/tars/__init__.py
--rw-r--r--   0        0        0     1493 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/compute_node/job_worker/executors/types.py
--rw-r--r--   0        0        0      394 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/compute_node/job_worker/job_key_cache.py
--rw-r--r--   0        0        0     1174 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/compute_node/job_worker/job_max_runtime_timer_thread.py
--rw-r--r--   0        0        0     5332 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/compute_node/job_worker/job_storage.py
--rw-r--r--   0        0        0    27753 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/compute_node/job_worker/job_worker.py
--rw-r--r--   0        0        0    10277 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/compute_node/job_worker/large_file_system.py
--rw-r--r--   0        0        0     2499 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/compute_node/job_worker/mappings.py
--rw-r--r--   0        0        0     1282 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/compute_node/job_worker/utils.py
--rw-r--r--   0        0        0    10090 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/compute_node/remote_host_proxy.py
--rw-r--r--   0        0        0     1601 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/compute_node/socker_listener_thread.py
--rw-r--r--   0        0        0      971 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/compute_node/socket_sender_thread.py
--rw-r--r--   0        0        0     4366 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/compute_node/utils.py
--rw-r--r--   0        0        0        0 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/compute_node/webserver/__init__.py
--rw-r--r--   0        0        0      914 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/compute_node/webserver/gunicorn_flask_application.py
--rw-r--r--   0        0        0     6570 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/compute_node/webserver/webserver.py
--rw-r--r--   0        0        0      490 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/compute_node/webserver/webserver_types.py
--rw-r--r--   0        0        0     4122 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/compute_node/webserver/webserver_utils.py
--rw-r--r--   0        0        0    10799 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/compute_node/webserver/worker_thread.py
--rw-r--r--   0        0        0       32 2022-07-12 10:55:26.377398 pybiolib-1.1.91/biolib/jobs/__init__.py
--rw-r--r--   0        0        0      453 2022-07-12 10:55:26.381398 pybiolib-1.1.91/biolib/jobs/job.py
--rw-r--r--   0        0        0     3754 2022-07-12 10:55:26.381398 pybiolib-1.1.91/biolib/jobs/job_result.py
--rw-r--r--   0        0        0     7412 2022-07-12 10:55:26.381398 pybiolib-1.1.91/biolib/lfs.py
--rw-r--r--   0        0        0      210 2022-07-12 10:55:26.381398 pybiolib-1.1.91/biolib/start_cli.py
--rw-r--r--   0        0        0       36 2022-07-12 10:55:26.381398 pybiolib-1.1.91/biolib/templates/__init__.py
--rw-r--r--   0        0        0      715 2022-07-12 10:55:26.381398 pybiolib-1.1.91/biolib/templates/example_app.py
--rw-r--r--   0        0        0      263 2022-07-12 10:55:26.381398 pybiolib-1.1.91/biolib/typing_utils.py
--rw-r--r--   0        0        0       39 2022-07-12 10:55:26.381398 pybiolib-1.1.91/biolib/user/__init__.py
--rw-r--r--   0        0        0     2061 2022-07-12 10:55:26.381398 pybiolib-1.1.91/biolib/user/sign_in.py
--rw-r--r--   0        0        0     7554 2022-07-12 10:55:26.381398 pybiolib-1.1.91/biolib/utils/__init__.py
--rw-r--r--   0        0        0     2635 2022-07-12 10:55:26.381398 pybiolib-1.1.91/biolib/utils/cache_state.py
--rw-r--r--   0        0        0     7743 2022-07-12 10:55:26.381398 pybiolib-1.1.91/biolib/utils/multipart_uploader.py
--rw-r--r--   0        0        0     6916 2022-07-12 10:55:26.381398 pybiolib-1.1.91/biolib/validators/validate_app_version.py
--rw-r--r--   0        0        0     4300 2022-07-12 10:55:26.381398 pybiolib-1.1.91/biolib/validators/validate_argument.py
--rw-r--r--   0        0        0    13298 2022-07-12 10:55:26.381398 pybiolib-1.1.91/biolib/validators/validate_module.py
--rw-r--r--   0        0        0     1655 2022-07-12 10:55:26.381398 pybiolib-1.1.91/biolib/validators/validate_zip_file.py
--rw-r--r--   0        0        0     2135 2022-07-12 10:55:26.381398 pybiolib-1.1.91/biolib/validators/validator_utils.py
--rw-r--r--   0        0        0     1169 2022-07-12 10:56:37.339233 pybiolib-1.1.91/pyproject.toml
--rw-r--r--   0        0        0     2043 2022-07-12 10:56:37.976688 pybiolib-1.1.91/setup.py
--rw-r--r--   0        0        0     1546 2022-07-12 10:56:37.977135 pybiolib-1.1.91/PKG-INFO
+-rw-r--r--   0        0        0     1067 2022-07-12 11:16:01.133705 pybiolib-1.1.94/LICENSE
+-rw-r--r--   0        0        0      369 2022-07-12 11:16:01.133705 pybiolib-1.1.94/README.md
+-rw-r--r--   0        0        0     1923 2022-07-12 11:16:01.133705 pybiolib-1.1.94/biolib/__init__.py
+-rw-r--r--   0        0        0       78 2022-07-12 11:16:01.133705 pybiolib-1.1.94/biolib/api/__init__.py
+-rw-r--r--   0        0        0     1643 2022-07-12 11:16:01.133705 pybiolib-1.1.94/biolib/api/client.py
+-rw-r--r--   0        0        0       37 2022-07-12 11:16:01.133705 pybiolib-1.1.94/biolib/app/__init__.py
+-rw-r--r--   0        0        0     4264 2022-07-12 11:16:01.133705 pybiolib-1.1.94/biolib/app/app.py
+-rw-r--r--   0        0        0     3162 2022-07-12 11:16:01.133705 pybiolib-1.1.94/biolib/app/app_result.py
+-rw-r--r--   0        0        0     4138 2022-07-12 11:16:01.133705 pybiolib-1.1.94/biolib/app/utils.py
+-rw-r--r--   0        0        0      182 2022-07-12 11:16:01.133705 pybiolib-1.1.94/biolib/biolib_api_client/__init__.py
+-rw-r--r--   0        0        0     5574 2022-07-12 11:16:01.133705 pybiolib-1.1.94/biolib/biolib_api_client/api_client.py
+-rw-r--r--   0        0        0     2355 2022-07-12 11:16:01.133705 pybiolib-1.1.94/biolib/biolib_api_client/app_types.py
+-rw-r--r--   0        0        0     1668 2022-07-12 11:16:01.133705 pybiolib-1.1.94/biolib/biolib_api_client/auth.py
+-rw-r--r--   0        0        0      580 2022-07-12 11:16:01.133705 pybiolib-1.1.94/biolib/biolib_api_client/biolib_account_api.py
+-rw-r--r--   0        0        0     2859 2022-07-12 11:16:01.133705 pybiolib-1.1.94/biolib/biolib_api_client/biolib_app_api.py
+-rw-r--r--   0        0        0     9165 2022-07-12 11:16:01.133705 pybiolib-1.1.94/biolib/biolib_api_client/biolib_job_api.py
+-rw-r--r--   0        0        0     2646 2022-07-12 11:16:01.133705 pybiolib-1.1.94/biolib/biolib_api_client/biolib_large_file_system_api.py
+-rw-r--r--   0        0        0      123 2022-07-12 11:16:01.133705 pybiolib-1.1.94/biolib/biolib_api_client/common_types.py
+-rw-r--r--   0        0        0     1205 2022-07-12 11:16:01.133705 pybiolib-1.1.94/biolib/biolib_api_client/job_types.py
+-rw-r--r--   0        0        0      493 2022-07-12 11:16:01.133705 pybiolib-1.1.94/biolib/biolib_api_client/lfs_types.py
+-rw-r--r--   0        0        0      635 2022-07-12 11:16:01.133705 pybiolib-1.1.94/biolib/biolib_api_client/user_state.py
+-rw-r--r--   0        0        0      303 2022-07-12 11:16:01.133705 pybiolib-1.1.94/biolib/biolib_binary_format/__init__.py
+-rw-r--r--   0        0        0      959 2022-07-12 11:16:01.133705 pybiolib-1.1.94/biolib/biolib_binary_format/base_bbf_package.py
+-rw-r--r--   0        0        0      154 2022-07-12 11:16:01.133705 pybiolib-1.1.94/biolib/biolib_binary_format/common_types.py
+-rw-r--r--   0        0        0     6450 2022-07-12 11:16:01.133705 pybiolib-1.1.94/biolib/biolib_binary_format/encrypted_module_output.py
+-rw-r--r--   0        0        0     2594 2022-07-12 11:16:01.133705 pybiolib-1.1.94/biolib/biolib_binary_format/module_input.py
+-rw-r--r--   0        0        0     2452 2022-07-12 11:16:01.133705 pybiolib-1.1.94/biolib/biolib_binary_format/module_output.py
+-rw-r--r--   0        0        0     2269 2022-07-12 11:16:01.133705 pybiolib-1.1.94/biolib/biolib_binary_format/rsa_encrypted_aes_package.py
+-rw-r--r--   0        0        0     1125 2022-07-12 11:16:01.133705 pybiolib-1.1.94/biolib/biolib_binary_format/saved_job.py
+-rw-r--r--   0        0        0     1023 2022-07-12 11:16:01.133705 pybiolib-1.1.94/biolib/biolib_binary_format/stdout_and_stderr.py
+-rw-r--r--   0        0        0      853 2022-07-12 11:16:01.133705 pybiolib-1.1.94/biolib/biolib_binary_format/system_exception.py
+-rw-r--r--   0        0        0     1191 2022-07-12 11:16:01.133705 pybiolib-1.1.94/biolib/biolib_binary_format/system_status_update.py
+-rw-r--r--   0        0        0     6887 2022-07-12 11:16:01.133705 pybiolib-1.1.94/biolib/biolib_binary_format/unencrypted_module_output.py
+-rw-r--r--   0        0        0     3595 2022-07-12 11:16:01.133705 pybiolib-1.1.94/biolib/biolib_binary_format/utils.py
+-rw-r--r--   0        0        0     1121 2022-07-12 11:16:01.133705 pybiolib-1.1.94/biolib/biolib_docker_client/__init__.py
+-rw-r--r--   0        0        0      381 2022-07-12 11:16:01.133705 pybiolib-1.1.94/biolib/biolib_errors.py
+-rw-r--r--   0        0        0     2854 2022-07-12 11:16:01.133705 pybiolib-1.1.94/biolib/biolib_logging.py
+-rw-r--r--   0        0        0    10219 2022-07-12 11:16:01.133705 pybiolib-1.1.94/biolib/biolib_push.py
+-rw-r--r--   0        0        0     1029 2022-07-12 11:16:01.133705 pybiolib-1.1.94/biolib/biolib_singularity_client/__init__.py
+-rw-r--r--   0        0        0    11204 2022-07-12 11:16:01.133705 pybiolib-1.1.94/biolib/cli.py
+-rw-r--r--   0        0        0     8859 2022-07-12 11:16:01.133705 pybiolib-1.1.94/biolib/cli_utils.py
+-rw-r--r--   0        0        0       45 2022-07-12 11:16:01.133705 pybiolib-1.1.94/biolib/compute_node/.gitignore
+-rw-r--r--   0        0        0        0 2022-07-12 11:16:01.133705 pybiolib-1.1.94/biolib/compute_node/__init__.py
+-rw-r--r--   0        0        0       67 2022-07-12 11:16:01.133705 pybiolib-1.1.94/biolib/compute_node/cloud_utils/__init__.py
+-rw-r--r--   0        0        0     6976 2022-07-12 11:16:01.133705 pybiolib-1.1.94/biolib/compute_node/cloud_utils/cloud_utils.py
+-rw-r--r--   0        0        0       71 2022-07-12 11:16:01.133705 pybiolib-1.1.94/biolib/compute_node/job_worker/__init__.py
+-rw-r--r--   0        0        0     3531 2022-07-12 11:16:01.133705 pybiolib-1.1.94/biolib/compute_node/job_worker/cache_state.py
+-rw-r--r--   0        0        0      922 2022-07-12 11:16:01.133705 pybiolib-1.1.94/biolib/compute_node/job_worker/cache_types.py
+-rw-r--r--   0        0        0     6517 2022-07-12 11:16:01.133705 pybiolib-1.1.94/biolib/compute_node/job_worker/docker_image_cache.py
+-rw-r--r--   0        0        0      315 2022-07-12 11:16:01.133705 pybiolib-1.1.94/biolib/compute_node/job_worker/executors/__init__.py
+-rw-r--r--   0        0        0      448 2022-07-12 11:16:01.133705 pybiolib-1.1.94/biolib/compute_node/job_worker/executors/base_executor.py
+-rw-r--r--   0        0        0    21198 2022-07-12 11:16:01.133705 pybiolib-1.1.94/biolib/compute_node/job_worker/executors/docker_executor.py
+-rw-r--r--   0        0        0      122 2022-07-12 11:16:01.133705 pybiolib-1.1.94/biolib/compute_node/job_worker/executors/docker_types.py
+-rw-r--r--   0        0        0       91 2022-07-12 11:16:01.133705 pybiolib-1.1.94/biolib/compute_node/job_worker/executors/remote/__init__.py
+-rw-r--r--   0        0        0     1842 2022-07-12 11:16:01.133705 pybiolib-1.1.94/biolib/compute_node/job_worker/executors/remote/remote_executor.py
+-rw-r--r--   0        0        0    13537 2022-07-12 11:16:01.133705 pybiolib-1.1.94/biolib/compute_node/job_worker/executors/singularity_executor.py
+-rw-r--r--   0        0        0        0 2022-07-12 11:16:01.133705 pybiolib-1.1.94/biolib/compute_node/job_worker/executors/tars/__init__.py
+-rw-r--r--   0        0        0     1493 2022-07-12 11:16:01.133705 pybiolib-1.1.94/biolib/compute_node/job_worker/executors/types.py
+-rw-r--r--   0        0        0      394 2022-07-12 11:16:01.133705 pybiolib-1.1.94/biolib/compute_node/job_worker/job_key_cache.py
+-rw-r--r--   0        0        0     1174 2022-07-12 11:16:01.133705 pybiolib-1.1.94/biolib/compute_node/job_worker/job_max_runtime_timer_thread.py
+-rw-r--r--   0        0        0     5332 2022-07-12 11:16:01.133705 pybiolib-1.1.94/biolib/compute_node/job_worker/job_storage.py
+-rw-r--r--   0        0        0    27753 2022-07-12 11:16:01.133705 pybiolib-1.1.94/biolib/compute_node/job_worker/job_worker.py
+-rw-r--r--   0        0        0    10277 2022-07-12 11:16:01.133705 pybiolib-1.1.94/biolib/compute_node/job_worker/large_file_system.py
+-rw-r--r--   0        0        0     2499 2022-07-12 11:16:01.133705 pybiolib-1.1.94/biolib/compute_node/job_worker/mappings.py
+-rw-r--r--   0        0        0     1282 2022-07-12 11:16:01.133705 pybiolib-1.1.94/biolib/compute_node/job_worker/utils.py
+-rw-r--r--   0        0        0    10090 2022-07-12 11:16:01.133705 pybiolib-1.1.94/biolib/compute_node/remote_host_proxy.py
+-rw-r--r--   0        0        0     1601 2022-07-12 11:16:01.137705 pybiolib-1.1.94/biolib/compute_node/socker_listener_thread.py
+-rw-r--r--   0        0        0      971 2022-07-12 11:16:01.137705 pybiolib-1.1.94/biolib/compute_node/socket_sender_thread.py
+-rw-r--r--   0        0        0     4366 2022-07-12 11:16:01.137705 pybiolib-1.1.94/biolib/compute_node/utils.py
+-rw-r--r--   0        0        0        0 2022-07-12 11:16:01.137705 pybiolib-1.1.94/biolib/compute_node/webserver/__init__.py
+-rw-r--r--   0        0        0      914 2022-07-12 11:16:01.137705 pybiolib-1.1.94/biolib/compute_node/webserver/gunicorn_flask_application.py
+-rw-r--r--   0        0        0     6570 2022-07-12 11:16:01.137705 pybiolib-1.1.94/biolib/compute_node/webserver/webserver.py
+-rw-r--r--   0        0        0      490 2022-07-12 11:16:01.137705 pybiolib-1.1.94/biolib/compute_node/webserver/webserver_types.py
+-rw-r--r--   0        0        0     4122 2022-07-12 11:16:01.137705 pybiolib-1.1.94/biolib/compute_node/webserver/webserver_utils.py
+-rw-r--r--   0        0        0    10799 2022-07-12 11:16:01.137705 pybiolib-1.1.94/biolib/compute_node/webserver/worker_thread.py
+-rw-r--r--   0        0        0       32 2022-07-12 11:16:01.137705 pybiolib-1.1.94/biolib/jobs/__init__.py
+-rw-r--r--   0        0        0      453 2022-07-12 11:16:01.137705 pybiolib-1.1.94/biolib/jobs/job.py
+-rw-r--r--   0        0        0     3754 2022-07-12 11:16:01.137705 pybiolib-1.1.94/biolib/jobs/job_result.py
+-rw-r--r--   0        0        0     7412 2022-07-12 11:16:01.137705 pybiolib-1.1.94/biolib/lfs.py
+-rw-r--r--   0        0        0      210 2022-07-12 11:16:01.137705 pybiolib-1.1.94/biolib/start_cli.py
+-rw-r--r--   0        0        0       36 2022-07-12 11:16:01.137705 pybiolib-1.1.94/biolib/templates/__init__.py
+-rw-r--r--   0        0        0      715 2022-07-12 11:16:01.137705 pybiolib-1.1.94/biolib/templates/example_app.py
+-rw-r--r--   0        0        0      263 2022-07-12 11:16:01.137705 pybiolib-1.1.94/biolib/typing_utils.py
+-rw-r--r--   0        0        0       39 2022-07-12 11:16:01.137705 pybiolib-1.1.94/biolib/user/__init__.py
+-rw-r--r--   0        0        0     2061 2022-07-12 11:16:01.137705 pybiolib-1.1.94/biolib/user/sign_in.py
+-rw-r--r--   0        0        0     7554 2022-07-12 11:16:01.137705 pybiolib-1.1.94/biolib/utils/__init__.py
+-rw-r--r--   0        0        0     2635 2022-07-12 11:16:01.137705 pybiolib-1.1.94/biolib/utils/cache_state.py
+-rw-r--r--   0        0        0     7743 2022-07-12 11:16:01.137705 pybiolib-1.1.94/biolib/utils/multipart_uploader.py
+-rw-r--r--   0        0        0     6916 2022-07-12 11:16:01.137705 pybiolib-1.1.94/biolib/validators/validate_app_version.py
+-rw-r--r--   0        0        0     4300 2022-07-12 11:16:01.137705 pybiolib-1.1.94/biolib/validators/validate_argument.py
+-rw-r--r--   0        0        0    13298 2022-07-12 11:16:01.137705 pybiolib-1.1.94/biolib/validators/validate_module.py
+-rw-r--r--   0        0        0     1655 2022-07-12 11:16:01.137705 pybiolib-1.1.94/biolib/validators/validate_zip_file.py
+-rw-r--r--   0        0        0     2135 2022-07-12 11:16:01.137705 pybiolib-1.1.94/biolib/validators/validator_utils.py
+-rw-r--r--   0        0        0     1169 2022-07-12 11:17:14.966690 pybiolib-1.1.94/pyproject.toml
+-rw-r--r--   0        0        0     2043 2022-07-12 11:17:15.586946 pybiolib-1.1.94/setup.py
+-rw-r--r--   0        0        0     1546 2022-07-12 11:17:15.587411 pybiolib-1.1.94/PKG-INFO
```

### Comparing `pybiolib-1.1.91/LICENSE` & `pybiolib-1.1.94/LICENSE`

 * *Files identical despite different names*

### Comparing `pybiolib-1.1.91/biolib/__init__.py` & `pybiolib-1.1.94/biolib/__init__.py`

 * *Files identical despite different names*

### Comparing `pybiolib-1.1.91/biolib/api/client.py` & `pybiolib-1.1.94/biolib/api/client.py`

 * *Files identical despite different names*

### Comparing `pybiolib-1.1.91/biolib/app/app.py` & `pybiolib-1.1.94/biolib/app/app.py`

 * *Files identical despite different names*

### Comparing `pybiolib-1.1.91/biolib/app/app_result.py` & `pybiolib-1.1.94/biolib/app/app_result.py`

 * *Files identical despite different names*

### Comparing `pybiolib-1.1.91/biolib/app/utils.py` & `pybiolib-1.1.94/biolib/app/utils.py`

 * *Files 2% similar despite different names*

```diff
@@ -25,15 +25,15 @@
 # TODO: type return value as ModuleOutput class
 def run_job(job, module_input_serialized: bytes):
     job_id = job['public_id']
     modules = job['app_version'].get('modules')
     logger.info(f'Job "{job_id}" is starting...')
 
     # Run in remote (in cloud)
-    if modules is None or utils.BIOLIB_FORCE_REMOTE_COMPUTE or (
+    if modules is None or utils.BIOLIB_FORCE_REMOTE_COMPUTE or not utils.BASE_URL_IS_PUBLIC_BIOLIB or (
             not BiolibDockerClient.is_docker_running() and not BiolibSingularityClient.is_singularity_running()
     ):
         result = RemoteExecutor.execute_job(
             RemoteExecuteOptions(
                 biolib_base_url=utils.BIOLIB_BASE_URL,
                 job=job,
                 root_job_id=job_id,
```

### Comparing `pybiolib-1.1.91/biolib/biolib_api_client/api_client.py` & `pybiolib-1.1.94/biolib/biolib_api_client/api_client.py`

 * *Files identical despite different names*

### Comparing `pybiolib-1.1.91/biolib/biolib_api_client/app_types.py` & `pybiolib-1.1.94/biolib/biolib_api_client/app_types.py`

 * *Files identical despite different names*

### Comparing `pybiolib-1.1.91/biolib/biolib_api_client/auth.py` & `pybiolib-1.1.94/biolib/biolib_api_client/auth.py`

 * *Files identical despite different names*

### Comparing `pybiolib-1.1.91/biolib/biolib_api_client/biolib_account_api.py` & `pybiolib-1.1.94/biolib/biolib_api_client/biolib_account_api.py`

 * *Files identical despite different names*

### Comparing `pybiolib-1.1.91/biolib/biolib_api_client/biolib_app_api.py` & `pybiolib-1.1.94/biolib/biolib_api_client/biolib_app_api.py`

 * *Files identical despite different names*

### Comparing `pybiolib-1.1.91/biolib/biolib_api_client/biolib_job_api.py` & `pybiolib-1.1.94/biolib/biolib_api_client/biolib_job_api.py`

 * *Files identical despite different names*

### Comparing `pybiolib-1.1.91/biolib/biolib_api_client/biolib_large_file_system_api.py` & `pybiolib-1.1.94/biolib/biolib_api_client/biolib_large_file_system_api.py`

 * *Files identical despite different names*

### Comparing `pybiolib-1.1.91/biolib/biolib_api_client/job_types.py` & `pybiolib-1.1.94/biolib/biolib_api_client/job_types.py`

 * *Files identical despite different names*

### Comparing `pybiolib-1.1.91/biolib/biolib_api_client/user_state.py` & `pybiolib-1.1.94/biolib/biolib_api_client/user_state.py`

 * *Files identical despite different names*

### Comparing `pybiolib-1.1.91/biolib/biolib_binary_format/base_bbf_package.py` & `pybiolib-1.1.94/biolib/biolib_binary_format/base_bbf_package.py`

 * *Files identical despite different names*

### Comparing `pybiolib-1.1.91/biolib/biolib_binary_format/encrypted_module_output.py` & `pybiolib-1.1.94/biolib/biolib_binary_format/encrypted_module_output.py`

 * *Files identical despite different names*

### Comparing `pybiolib-1.1.91/biolib/biolib_binary_format/module_input.py` & `pybiolib-1.1.94/biolib/biolib_binary_format/module_input.py`

 * *Files identical despite different names*

### Comparing `pybiolib-1.1.91/biolib/biolib_binary_format/module_output.py` & `pybiolib-1.1.94/biolib/biolib_binary_format/module_output.py`

 * *Files identical despite different names*

### Comparing `pybiolib-1.1.91/biolib/biolib_binary_format/rsa_encrypted_aes_package.py` & `pybiolib-1.1.94/biolib/biolib_binary_format/rsa_encrypted_aes_package.py`

 * *Files identical despite different names*

### Comparing `pybiolib-1.1.91/biolib/biolib_binary_format/saved_job.py` & `pybiolib-1.1.94/biolib/biolib_binary_format/saved_job.py`

 * *Files identical despite different names*

### Comparing `pybiolib-1.1.91/biolib/biolib_binary_format/stdout_and_stderr.py` & `pybiolib-1.1.94/biolib/biolib_binary_format/stdout_and_stderr.py`

 * *Files identical despite different names*

### Comparing `pybiolib-1.1.91/biolib/biolib_binary_format/system_exception.py` & `pybiolib-1.1.94/biolib/biolib_binary_format/system_exception.py`

 * *Files identical despite different names*

### Comparing `pybiolib-1.1.91/biolib/biolib_binary_format/system_status_update.py` & `pybiolib-1.1.94/biolib/biolib_binary_format/system_status_update.py`

 * *Files identical despite different names*

### Comparing `pybiolib-1.1.91/biolib/biolib_binary_format/unencrypted_module_output.py` & `pybiolib-1.1.94/biolib/biolib_binary_format/unencrypted_module_output.py`

 * *Files identical despite different names*

### Comparing `pybiolib-1.1.91/biolib/biolib_binary_format/utils.py` & `pybiolib-1.1.94/biolib/biolib_binary_format/utils.py`

 * *Files identical despite different names*

### Comparing `pybiolib-1.1.91/biolib/biolib_docker_client/__init__.py` & `pybiolib-1.1.94/biolib/biolib_docker_client/__init__.py`

 * *Files identical despite different names*

### Comparing `pybiolib-1.1.91/biolib/biolib_logging.py` & `pybiolib-1.1.94/biolib/biolib_logging.py`

 * *Files identical despite different names*

### Comparing `pybiolib-1.1.91/biolib/biolib_push.py` & `pybiolib-1.1.94/biolib/biolib_push.py`

 * *Files identical despite different names*

### Comparing `pybiolib-1.1.91/biolib/biolib_singularity_client/__init__.py` & `pybiolib-1.1.94/biolib/biolib_singularity_client/__init__.py`

 * *Files identical despite different names*

### Comparing `pybiolib-1.1.91/biolib/cli.py` & `pybiolib-1.1.94/biolib/cli.py`

 * *Files identical despite different names*

### Comparing `pybiolib-1.1.91/biolib/cli_utils.py` & `pybiolib-1.1.94/biolib/cli_utils.py`

 * *Files identical despite different names*

### Comparing `pybiolib-1.1.91/biolib/compute_node/cloud_utils/cloud_utils.py` & `pybiolib-1.1.94/biolib/compute_node/cloud_utils/cloud_utils.py`

 * *Files identical despite different names*

### Comparing `pybiolib-1.1.91/biolib/compute_node/job_worker/cache_state.py` & `pybiolib-1.1.94/biolib/compute_node/job_worker/cache_state.py`

 * *Files identical despite different names*

### Comparing `pybiolib-1.1.91/biolib/compute_node/job_worker/cache_types.py` & `pybiolib-1.1.94/biolib/compute_node/job_worker/cache_types.py`

 * *Files identical despite different names*

### Comparing `pybiolib-1.1.91/biolib/compute_node/job_worker/docker_image_cache.py` & `pybiolib-1.1.94/biolib/compute_node/job_worker/docker_image_cache.py`

 * *Files identical despite different names*

### Comparing `pybiolib-1.1.91/biolib/compute_node/job_worker/executors/docker_executor.py` & `pybiolib-1.1.94/biolib/compute_node/job_worker/executors/docker_executor.py`

 * *Files identical despite different names*

### Comparing `pybiolib-1.1.91/biolib/compute_node/job_worker/executors/remote/remote_executor.py` & `pybiolib-1.1.94/biolib/compute_node/job_worker/executors/remote/remote_executor.py`

 * *Files identical despite different names*

### Comparing `pybiolib-1.1.91/biolib/compute_node/job_worker/executors/singularity_executor.py` & `pybiolib-1.1.94/biolib/compute_node/job_worker/executors/singularity_executor.py`

 * *Files identical despite different names*

### Comparing `pybiolib-1.1.91/biolib/compute_node/job_worker/executors/types.py` & `pybiolib-1.1.94/biolib/compute_node/job_worker/executors/types.py`

 * *Files identical despite different names*

### Comparing `pybiolib-1.1.91/biolib/compute_node/job_worker/job_max_runtime_timer_thread.py` & `pybiolib-1.1.94/biolib/compute_node/job_worker/job_max_runtime_timer_thread.py`

 * *Files identical despite different names*

### Comparing `pybiolib-1.1.91/biolib/compute_node/job_worker/job_storage.py` & `pybiolib-1.1.94/biolib/compute_node/job_worker/job_storage.py`

 * *Files identical despite different names*

### Comparing `pybiolib-1.1.91/biolib/compute_node/job_worker/job_worker.py` & `pybiolib-1.1.94/biolib/compute_node/job_worker/job_worker.py`

 * *Files identical despite different names*

### Comparing `pybiolib-1.1.91/biolib/compute_node/job_worker/large_file_system.py` & `pybiolib-1.1.94/biolib/compute_node/job_worker/large_file_system.py`

 * *Files identical despite different names*

### Comparing `pybiolib-1.1.91/biolib/compute_node/job_worker/mappings.py` & `pybiolib-1.1.94/biolib/compute_node/job_worker/mappings.py`

 * *Files identical despite different names*

### Comparing `pybiolib-1.1.91/biolib/compute_node/job_worker/utils.py` & `pybiolib-1.1.94/biolib/compute_node/job_worker/utils.py`

 * *Files identical despite different names*

### Comparing `pybiolib-1.1.91/biolib/compute_node/remote_host_proxy.py` & `pybiolib-1.1.94/biolib/compute_node/remote_host_proxy.py`

 * *Files identical despite different names*

### Comparing `pybiolib-1.1.91/biolib/compute_node/socker_listener_thread.py` & `pybiolib-1.1.94/biolib/compute_node/socker_listener_thread.py`

 * *Files identical despite different names*

### Comparing `pybiolib-1.1.91/biolib/compute_node/socket_sender_thread.py` & `pybiolib-1.1.94/biolib/compute_node/socket_sender_thread.py`

 * *Files identical despite different names*

### Comparing `pybiolib-1.1.91/biolib/compute_node/utils.py` & `pybiolib-1.1.94/biolib/compute_node/utils.py`

 * *Files identical despite different names*

### Comparing `pybiolib-1.1.91/biolib/compute_node/webserver/gunicorn_flask_application.py` & `pybiolib-1.1.94/biolib/compute_node/webserver/gunicorn_flask_application.py`

 * *Files identical despite different names*

### Comparing `pybiolib-1.1.91/biolib/compute_node/webserver/webserver.py` & `pybiolib-1.1.94/biolib/compute_node/webserver/webserver.py`

 * *Files identical despite different names*

### Comparing `pybiolib-1.1.91/biolib/compute_node/webserver/webserver_utils.py` & `pybiolib-1.1.94/biolib/compute_node/webserver/webserver_utils.py`

 * *Files identical despite different names*

### Comparing `pybiolib-1.1.91/biolib/compute_node/webserver/worker_thread.py` & `pybiolib-1.1.94/biolib/compute_node/webserver/worker_thread.py`

 * *Files identical despite different names*

### Comparing `pybiolib-1.1.91/biolib/jobs/job_result.py` & `pybiolib-1.1.94/biolib/jobs/job_result.py`

 * *Files identical despite different names*

### Comparing `pybiolib-1.1.91/biolib/lfs.py` & `pybiolib-1.1.94/biolib/lfs.py`

 * *Files identical despite different names*

### Comparing `pybiolib-1.1.91/biolib/templates/example_app.py` & `pybiolib-1.1.94/biolib/templates/example_app.py`

 * *Files identical despite different names*

### Comparing `pybiolib-1.1.91/biolib/user/sign_in.py` & `pybiolib-1.1.94/biolib/user/sign_in.py`

 * *Files identical despite different names*

### Comparing `pybiolib-1.1.91/biolib/utils/__init__.py` & `pybiolib-1.1.94/biolib/utils/__init__.py`

 * *Files identical despite different names*

### Comparing `pybiolib-1.1.91/biolib/utils/cache_state.py` & `pybiolib-1.1.94/biolib/utils/cache_state.py`

 * *Files identical despite different names*

### Comparing `pybiolib-1.1.91/biolib/utils/multipart_uploader.py` & `pybiolib-1.1.94/biolib/utils/multipart_uploader.py`

 * *Files identical despite different names*

### Comparing `pybiolib-1.1.91/biolib/validators/validate_app_version.py` & `pybiolib-1.1.94/biolib/validators/validate_app_version.py`

 * *Files identical despite different names*

### Comparing `pybiolib-1.1.91/biolib/validators/validate_argument.py` & `pybiolib-1.1.94/biolib/validators/validate_argument.py`

 * *Files identical despite different names*

### Comparing `pybiolib-1.1.91/biolib/validators/validate_module.py` & `pybiolib-1.1.94/biolib/validators/validate_module.py`

 * *Files identical despite different names*

### Comparing `pybiolib-1.1.91/biolib/validators/validate_zip_file.py` & `pybiolib-1.1.94/biolib/validators/validate_zip_file.py`

 * *Files identical despite different names*

### Comparing `pybiolib-1.1.91/biolib/validators/validator_utils.py` & `pybiolib-1.1.94/biolib/validators/validator_utils.py`

 * *Files identical despite different names*

### Comparing `pybiolib-1.1.91/pyproject.toml` & `pybiolib-1.1.94/pyproject.toml`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "pybiolib"
-version = "1.1.91"
+version = "1.1.94"
 description = "BioLib Python Client"
 readme = "README.md"
 license = "MIT"
 homepage = "https://github.com/biolib"
 keywords = ["biolib"]
 authors = [
     "biolib <hello@biolib.com>",
```

### Comparing `pybiolib-1.1.91/setup.py` & `pybiolib-1.1.94/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -44,15 +44,15 @@
                              'typing_inspect>=0.5.0,<0.6.0']}
 
 entry_points = \
 {'console_scripts': ['biolib = biolib:call_cli']}
 
 setup_kwargs = {
     'name': 'pybiolib',
-    'version': '1.1.91',
+    'version': '1.1.94',
     'description': 'BioLib Python Client',
     'long_description': "# PyBioLib\n\nPyBioLib is a Python package for running BioLib applications from Python scripts and the command line.\n\n### Python Example\n```python\n# pip3 install -U pybiolib\nimport biolib\nsamtools = biolib.load('samtools/samtools')\nprint(samtools.cli(args='--help'))\n```\n\n### Command Line Example\n```bash\npip3 install -U pybiolib\nbiolib run samtools/samtools --help\n```\n\n",
     'author': 'biolib',
     'author_email': 'hello@biolib.com',
     'maintainer': None,
     'maintainer_email': None,
     'url': 'https://github.com/biolib',
```

### Comparing `pybiolib-1.1.91/PKG-INFO` & `pybiolib-1.1.94/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pybiolib
-Version: 1.1.91
+Version: 1.1.94
 Summary: BioLib Python Client
 Home-page: https://github.com/biolib
 License: MIT
 Keywords: biolib
 Author: biolib
 Author-email: hello@biolib.com
 Requires-Python: >=3.6.3,<4.0.0
```

