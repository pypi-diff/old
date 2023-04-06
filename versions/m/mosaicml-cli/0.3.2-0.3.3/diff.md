# Comparing `tmp/mosaicml-cli-0.3.2.tar.gz` & `tmp/mosaicml-cli-0.3.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "mosaicml-cli-0.3.2.tar", last modified: Wed Apr  5 00:12:43 2023, max compression
+gzip compressed data, was "mosaicml-cli-0.3.3.tar", last modified: Thu Apr  6 21:21:43 2023, max compression
```

## Comparing `mosaicml-cli-0.3.2.tar` & `mosaicml-cli-0.3.3.tar`

### file list

```diff
@@ -1,268 +1,268 @@
-drwxr-xr-x   0 jeffchen   (501) staff       (20)        0 2023-04-05 00:12:43.358471 mosaicml-cli-0.3.2/
--rw-r--r--   0 jeffchen   (501) staff       (20)      696 2023-04-05 00:12:43.358106 mosaicml-cli-0.3.2/PKG-INFO
--rw-r--r--   0 jeffchen   (501) staff       (20)     7799 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/README.md
-drwxr-xr-x   0 jeffchen   (501) staff       (20)        0 2023-04-05 00:12:43.228220 mosaicml-cli-0.3.2/mcli/
--rw-r--r--   0 jeffchen   (501) staff       (20)       54 2022-09-07 04:52:30.000000 mosaicml-cli-0.3.2/mcli/__init__.py
-drwxr-xr-x   0 jeffchen   (501) staff       (20)        0 2023-04-05 00:12:43.229562 mosaicml-cli-0.3.2/mcli/api/
--rw-r--r--   0 jeffchen   (501) staff       (20)        0 2022-09-07 04:52:30.000000 mosaicml-cli-0.3.2/mcli/api/__init__.py
-drwxr-xr-x   0 jeffchen   (501) staff       (20)        0 2023-04-05 00:12:43.231258 mosaicml-cli-0.3.2/mcli/api/cluster/
--rw-r--r--   0 jeffchen   (501) staff       (20)      134 2022-10-27 20:22:32.000000 mosaicml-cli-0.3.2/mcli/api/cluster/__init__.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     4058 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/api/cluster/api_get_clusters.py
-drwxr-xr-x   0 jeffchen   (501) staff       (20)        0 2023-04-05 00:12:43.233965 mosaicml-cli-0.3.2/mcli/api/engine/
--rw-r--r--   0 jeffchen   (501) staff       (20)        0 2022-09-07 04:52:30.000000 mosaicml-cli-0.3.2/mcli/api/engine/__init__.py
--rw-r--r--   0 jeffchen   (501) staff       (20)    22935 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/api/engine/engine.py
--rw-r--r--   0 jeffchen   (501) staff       (20)      787 2022-09-07 04:52:30.000000 mosaicml-cli-0.3.2/mcli/api/engine/utils.py
--rw-r--r--   0 jeffchen   (501) staff       (20)    11677 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/api/exceptions.py
-drwxr-xr-x   0 jeffchen   (501) staff       (20)        0 2023-04-05 00:12:43.240414 mosaicml-cli-0.3.2/mcli/api/inference_deployments/
--rw-r--r--   0 jeffchen   (501) staff       (20)      858 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/api/inference_deployments/__init__.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     3388 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/api/inference_deployments/api_create_inference_deployment.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     3278 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/api/inference_deployments/api_delete_inference_deployments.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     6091 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/api/inference_deployments/api_get_inference_deployments.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     1156 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/api/inference_deployments/api_ping_inference_deployment.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     1276 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/api/inference_deployments/api_predict_inference_deployment.py
-drwxr-xr-x   0 jeffchen   (501) staff       (20)        0 2023-04-05 00:12:43.241103 mosaicml-cli-0.3.2/mcli/api/kube/
--rw-r--r--   0 jeffchen   (501) staff       (20)        0 2022-09-07 04:52:30.000000 mosaicml-cli-0.3.2/mcli/api/kube/__init__.py
-drwxr-xr-x   0 jeffchen   (501) staff       (20)        0 2023-04-05 00:12:43.246875 mosaicml-cli-0.3.2/mcli/api/kube/runs/
--rw-r--r--   0 jeffchen   (501) staff       (20)      856 2022-09-07 04:52:30.000000 mosaicml-cli-0.3.2/mcli/api/kube/runs/__init__.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     4816 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/api/kube/runs/api_create_run.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     5042 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/api/kube/runs/api_delete_runs.py
--rw-r--r--   0 jeffchen   (501) staff       (20)    14458 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/api/kube/runs/api_get_run_logs.py
--rw-r--r--   0 jeffchen   (501) staff       (20)    15782 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/api/kube/runs/api_get_runs.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     6007 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/api/kube/runs/api_stop_runs.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     6210 2022-10-27 20:22:32.000000 mosaicml-cli-0.3.2/mcli/api/kube/runs/api_watch_run.py
-drwxr-xr-x   0 jeffchen   (501) staff       (20)        0 2023-04-05 00:12:43.250618 mosaicml-cli-0.3.2/mcli/api/mint/
--rw-r--r--   0 jeffchen   (501) staff       (20)        0 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/api/mint/__init__.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     4987 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/api/mint/shell.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     1530 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/api/mint/tty.py
-drwxr-xr-x   0 jeffchen   (501) staff       (20)        0 2023-04-05 00:12:43.255527 mosaicml-cli-0.3.2/mcli/api/model/
--rw-r--r--   0 jeffchen   (501) staff       (20)      209 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/api/model/__init__.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     5655 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/api/model/cluster_details.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     3015 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/api/model/inference_deployment.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     3946 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/api/model/run.py
-drwxr-xr-x   0 jeffchen   (501) staff       (20)        0 2023-04-05 00:12:43.258123 mosaicml-cli-0.3.2/mcli/api/runs/
--rw-r--r--   0 jeffchen   (501) staff       (20)      828 2023-01-26 01:45:43.000000 mosaicml-cli-0.3.2/mcli/api/runs/__init__.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     2664 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/api/runs/api_create_run.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     3928 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/api/runs/api_delete_runs.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     9281 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/api/runs/api_get_run_logs.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     6205 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/api/runs/api_get_runs.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     6018 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/api/runs/api_stop_runs.py
--rw-r--r--   0 jeffchen   (501) staff       (20)    10619 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/api/runs/api_watch_run.py
-drwxr-xr-x   0 jeffchen   (501) staff       (20)        0 2023-04-05 00:12:43.258536 mosaicml-cli-0.3.2/mcli/api/schema/
--rw-r--r--   0 jeffchen   (501) staff       (20)        0 2022-09-07 04:52:30.000000 mosaicml-cli-0.3.2/mcli/api/schema/__init__.py
--rw-r--r--   0 jeffchen   (501) staff       (20)      636 2022-11-11 00:18:38.000000 mosaicml-cli-0.3.2/mcli/api/schema/generic_model.py
-drwxr-xr-x   0 jeffchen   (501) staff       (20)        0 2023-04-05 00:12:43.260143 mosaicml-cli-0.3.2/mcli/api/secrets/
--rw-r--r--   0 jeffchen   (501) staff       (20)      309 2022-09-19 22:17:10.000000 mosaicml-cli-0.3.2/mcli/api/secrets/__init__.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     2365 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/api/secrets/api_create_secret.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     2998 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/api/secrets/api_delete_secrets.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     3697 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/api/secrets/api_get_secrets.py
--rw-r--r--   0 jeffchen   (501) staff       (20)      508 2023-01-10 00:19:00.000000 mosaicml-cli-0.3.2/mcli/api/types.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     2354 2022-09-07 04:52:30.000000 mosaicml-cli-0.3.2/mcli/api/typing_future.py
-drwxr-xr-x   0 jeffchen   (501) staff       (20)        0 2023-04-05 00:12:43.260707 mosaicml-cli-0.3.2/mcli/api/users/
--rw-r--r--   0 jeffchen   (501) staff       (20)      139 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/api/users/__init__.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     2694 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/api/users/api_get_users.py
-drwxr-xr-x   0 jeffchen   (501) staff       (20)        0 2023-04-05 00:12:43.261092 mosaicml-cli-0.3.2/mcli/cli/
--rw-r--r--   0 jeffchen   (501) staff       (20)        0 2022-09-07 04:52:30.000000 mosaicml-cli-0.3.2/mcli/cli/__init__.py
--rwxr-xr-x   0 jeffchen   (501) staff       (20)     7182 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/cli/cli.py
-drwxr-xr-x   0 jeffchen   (501) staff       (20)        0 2023-04-05 00:12:43.261808 mosaicml-cli-0.3.2/mcli/cli/common/
--rw-r--r--   0 jeffchen   (501) staff       (20)        0 2023-02-01 21:37:29.000000 mosaicml-cli-0.3.2/mcli/cli/common/__init__.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     2670 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/cli/common/deployment_filters.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     7077 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/cli/common/run_filters.py
-drwxr-xr-x   0 jeffchen   (501) staff       (20)        0 2023-04-05 00:12:43.262203 mosaicml-cli-0.3.2/mcli/cli/m_clean/
--rw-r--r--   0 jeffchen   (501) staff       (20)        0 2022-09-07 04:52:30.000000 mosaicml-cli-0.3.2/mcli/cli/m_clean/__init__.py
--rw-r--r--   0 jeffchen   (501) staff       (20)      950 2022-10-27 20:22:32.000000 mosaicml-cli-0.3.2/mcli/cli/m_clean/m_clean.py
-drwxr-xr-x   0 jeffchen   (501) staff       (20)        0 2023-04-05 00:12:43.263191 mosaicml-cli-0.3.2/mcli/cli/m_connect/
--rw-r--r--   0 jeffchen   (501) staff       (20)        0 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/cli/m_connect/__init__.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     1541 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/cli/m_connect/m_connect.py
-drwxr-xr-x   0 jeffchen   (501) staff       (20)        0 2023-04-05 00:12:43.266116 mosaicml-cli-0.3.2/mcli/cli/m_create/
--rw-r--r--   0 jeffchen   (501) staff       (20)        0 2022-09-07 04:52:30.000000 mosaicml-cli-0.3.2/mcli/cli/m_create/__init__.py
--rw-r--r--   0 jeffchen   (501) staff       (20)    11513 2022-10-27 20:22:32.000000 mosaicml-cli-0.3.2/mcli/cli/m_create/cluster.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     7167 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/cli/m_create/env_var.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     4217 2023-02-01 21:37:29.000000 mosaicml-cli-0.3.2/mcli/cli/m_create/m_create.py
--rw-r--r--   0 jeffchen   (501) staff       (20)    24927 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/cli/m_create/secret.py
-drwxr-xr-x   0 jeffchen   (501) staff       (20)        0 2023-04-05 00:12:43.266960 mosaicml-cli-0.3.2/mcli/cli/m_delete/
--rw-r--r--   0 jeffchen   (501) staff       (20)        0 2022-09-07 04:52:30.000000 mosaicml-cli-0.3.2/mcli/cli/m_delete/__init__.py
--rw-r--r--   0 jeffchen   (501) staff       (20)    14072 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/cli/m_delete/delete.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     8417 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/cli/m_delete/m_delete.py
-drwxr-xr-x   0 jeffchen   (501) staff       (20)        0 2023-04-05 00:12:43.267577 mosaicml-cli-0.3.2/mcli/cli/m_deploy/
--rw-r--r--   0 jeffchen   (501) staff       (20)        0 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/cli/m_deploy/__init__.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     3896 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/cli/m_deploy/m_deploy.py
-drwxr-xr-x   0 jeffchen   (501) staff       (20)        0 2023-04-05 00:12:43.268773 mosaicml-cli-0.3.2/mcli/cli/m_describe/
--rw-r--r--   0 jeffchen   (501) staff       (20)        0 2023-01-26 01:45:43.000000 mosaicml-cli-0.3.2/mcli/cli/m_describe/__init__.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     4409 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/cli/m_describe/describe_inference_deployments.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     7391 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/cli/m_describe/describe_runs.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     1860 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/cli/m_describe/m_describe.py
-drwxr-xr-x   0 jeffchen   (501) staff       (20)        0 2023-04-05 00:12:43.275770 mosaicml-cli-0.3.2/mcli/cli/m_get/
--rw-r--r--   0 jeffchen   (501) staff       (20)      549 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/cli/m_get/__init__.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     3909 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/cli/m_get/clusters.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     6452 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/cli/m_get/display.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     1315 2022-09-14 20:53:21.000000 mosaicml-cli-0.3.2/mcli/cli/m_get/envvars.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     5361 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/cli/m_get/inference_deployments.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     4866 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/cli/m_get/m_get.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     5050 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/cli/m_get/runs.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     3567 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/cli/m_get/secrets.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     1580 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/cli/m_get/users.py
-drwxr-xr-x   0 jeffchen   (501) staff       (20)        0 2023-04-05 00:12:43.276415 mosaicml-cli-0.3.2/mcli/cli/m_init/
--rw-r--r--   0 jeffchen   (501) staff       (20)        0 2022-09-07 04:52:30.000000 mosaicml-cli-0.3.2/mcli/cli/m_init/__init__.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     4113 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/cli/m_init/m_init.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     9374 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/cli/m_init/m_init_kube.py
-drwxr-xr-x   0 jeffchen   (501) staff       (20)        0 2023-04-05 00:12:43.277639 mosaicml-cli-0.3.2/mcli/cli/m_interactive/
--rw-r--r--   0 jeffchen   (501) staff       (20)        0 2022-09-07 04:52:30.000000 mosaicml-cli-0.3.2/mcli/cli/m_interactive/__init__.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     9005 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/cli/m_interactive/interactive.py
--rw-r--r--   0 jeffchen   (501) staff       (20)    16203 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/cli/m_interactive/m_interactive.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     4571 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/cli/m_interactive/temp_mcloud_interactive.py
-drwxr-xr-x   0 jeffchen   (501) staff       (20)        0 2023-04-05 00:12:43.278124 mosaicml-cli-0.3.2/mcli/cli/m_log/
--rw-r--r--   0 jeffchen   (501) staff       (20)        0 2022-09-07 04:52:30.000000 mosaicml-cli-0.3.2/mcli/cli/m_log/__init__.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     8628 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/cli/m_log/m_log.py
-drwxr-xr-x   0 jeffchen   (501) staff       (20)        0 2023-04-05 00:12:43.278581 mosaicml-cli-0.3.2/mcli/cli/m_ping/
--rw-r--r--   0 jeffchen   (501) staff       (20)        0 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/cli/m_ping/__init__.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     1742 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/cli/m_ping/m_ping.py
-drwxr-xr-x   0 jeffchen   (501) staff       (20)        0 2023-04-05 00:12:43.279115 mosaicml-cli-0.3.2/mcli/cli/m_predict/
--rw-r--r--   0 jeffchen   (501) staff       (20)        0 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/cli/m_predict/__init__.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     2160 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/cli/m_predict/m_predict.py
-drwxr-xr-x   0 jeffchen   (501) staff       (20)        0 2023-04-05 00:12:43.279535 mosaicml-cli-0.3.2/mcli/cli/m_root/
--rw-r--r--   0 jeffchen   (501) staff       (20)        0 2022-09-07 04:52:30.000000 mosaicml-cli-0.3.2/mcli/cli/m_root/__init__.py
--rw-r--r--   0 jeffchen   (501) staff       (20)      947 2022-10-31 17:33:03.000000 mosaicml-cli-0.3.2/mcli/cli/m_root/m_config.py
-drwxr-xr-x   0 jeffchen   (501) staff       (20)        0 2023-04-05 00:12:43.280660 mosaicml-cli-0.3.2/mcli/cli/m_run/
--rw-r--r--   0 jeffchen   (501) staff       (20)        0 2022-09-07 04:52:30.000000 mosaicml-cli-0.3.2/mcli/cli/m_run/__init__.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     9494 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/cli/m_run/m_run.py
-drwxr-xr-x   0 jeffchen   (501) staff       (20)        0 2023-04-05 00:12:43.282015 mosaicml-cli-0.3.2/mcli/cli/m_set_unset/
--rw-r--r--   0 jeffchen   (501) staff       (20)        0 2022-10-06 23:40:35.000000 mosaicml-cli-0.3.2/mcli/cli/m_set_unset/__init__.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     2973 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/cli/m_set_unset/api_key.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     1927 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/cli/m_set_unset/m_set.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     1408 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/cli/m_set_unset/m_unset.py
--rw-r--r--   0 jeffchen   (501) staff       (20)      881 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/cli/m_set_unset/user.py
-drwxr-xr-x   0 jeffchen   (501) staff       (20)        0 2023-04-05 00:12:43.282426 mosaicml-cli-0.3.2/mcli/cli/m_stop/
--rw-r--r--   0 jeffchen   (501) staff       (20)        0 2022-09-27 01:04:20.000000 mosaicml-cli-0.3.2/mcli/cli/m_stop/__init__.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     3847 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/cli/m_stop/m_stop.py
-drwxr-xr-x   0 jeffchen   (501) staff       (20)        0 2023-04-05 00:12:43.282762 mosaicml-cli-0.3.2/mcli/cli/m_use/
--rw-r--r--   0 jeffchen   (501) staff       (20)        0 2022-09-07 04:52:30.000000 mosaicml-cli-0.3.2/mcli/cli/m_use/__init__.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     3234 2022-12-09 18:28:49.000000 mosaicml-cli-0.3.2/mcli/cli/m_use/m_use.py
-drwxr-xr-x   0 jeffchen   (501) staff       (20)        0 2023-04-05 00:12:43.284185 mosaicml-cli-0.3.2/mcli/cli/m_util/
--rw-r--r--   0 jeffchen   (501) staff       (20)        0 2022-09-07 04:52:30.000000 mosaicml-cli-0.3.2/mcli/cli/m_util/__init__.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     9853 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/cli/m_util/kube_util.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     1147 2022-10-27 20:22:32.000000 mosaicml-cli-0.3.2/mcli/cli/m_util/m_util.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     6515 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/cli/m_util/util.py
--rw-r--r--   0 jeffchen   (501) staff       (20)    16462 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/config.py
-drwxr-xr-x   0 jeffchen   (501) staff       (20)        0 2023-04-05 00:12:43.288385 mosaicml-cli-0.3.2/mcli/models/
--rw-r--r--   0 jeffchen   (501) staff       (20)     1061 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/models/__init__.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     7179 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/models/inference_deployment_config.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     3693 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/models/mcli_cluster.py
--rw-r--r--   0 jeffchen   (501) staff       (20)      563 2022-09-14 20:53:21.000000 mosaicml-cli-0.3.2/mcli/models/mcli_envvar.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     3386 2022-09-14 20:53:21.000000 mosaicml-cli-0.3.2/mcli/models/mcli_integration.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     9400 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/models/mcli_secret.py
--rw-r--r--   0 jeffchen   (501) staff       (20)    21114 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/models/run_config.py
-drwxr-xr-x   0 jeffchen   (501) staff       (20)        0 2023-04-05 00:12:43.288699 mosaicml-cli-0.3.2/mcli/objects/
--rw-r--r--   0 jeffchen   (501) staff       (20)        0 2022-09-07 04:52:30.000000 mosaicml-cli-0.3.2/mcli/objects/__init__.py
-drwxr-xr-x   0 jeffchen   (501) staff       (20)        0 2023-04-05 00:12:43.295297 mosaicml-cli-0.3.2/mcli/objects/integrations/
--rw-r--r--   0 jeffchen   (501) staff       (20)      660 2022-09-14 20:53:21.000000 mosaicml-cli-0.3.2/mcli/objects/integrations/__init__.py
--rw-r--r--   0 jeffchen   (501) staff       (20)      671 2022-09-07 04:52:30.000000 mosaicml-cli-0.3.2/mcli/objects/integrations/apt_packages.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     1287 2022-09-14 20:53:21.000000 mosaicml-cli-0.3.2/mcli/objects/integrations/comet.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     2597 2023-01-26 01:45:43.000000 mosaicml-cli-0.3.2/mcli/objects/integrations/git_repo.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     3491 2022-09-23 00:37:17.000000 mosaicml-cli-0.3.2/mcli/objects/integrations/local.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     2126 2022-12-01 00:52:00.000000 mosaicml-cli-0.3.2/mcli/objects/integrations/mosaicml_agent.py
--rw-r--r--   0 jeffchen   (501) staff       (20)      810 2022-09-07 04:52:30.000000 mosaicml-cli-0.3.2/mcli/objects/integrations/pip_packages.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     2742 2022-09-07 04:52:30.000000 mosaicml-cli-0.3.2/mcli/objects/integrations/wandb.py
-drwxr-xr-x   0 jeffchen   (501) staff       (20)        0 2023-04-05 00:12:43.302028 mosaicml-cli-0.3.2/mcli/objects/secrets/
--rw-r--r--   0 jeffchen   (501) staff       (20)     1090 2022-12-09 18:28:49.000000 mosaicml-cli-0.3.2/mcli/objects/secrets/__init__.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     4913 2022-10-27 20:22:32.000000 mosaicml-cli-0.3.2/mcli/objects/secrets/cluster_secret.py
-drwxr-xr-x   0 jeffchen   (501) staff       (20)        0 2023-04-05 00:12:43.309163 mosaicml-cli-0.3.2/mcli/objects/secrets/create/
--rw-r--r--   0 jeffchen   (501) staff       (20)        0 2022-09-07 04:52:30.000000 mosaicml-cli-0.3.2/mcli/objects/secrets/create/__init__.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     3953 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/objects/secrets/create/base.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     3461 2022-12-09 18:28:49.000000 mosaicml-cli-0.3.2/mcli/objects/secrets/create/docker_registry.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     2406 2022-11-30 21:02:34.000000 mosaicml-cli-0.3.2/mcli/objects/secrets/create/gcp.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     7554 2022-11-04 23:17:49.000000 mosaicml-cli-0.3.2/mcli/objects/secrets/create/generic.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     3855 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/objects/secrets/create/oci.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     2998 2022-09-19 22:17:10.000000 mosaicml-cli-0.3.2/mcli/objects/secrets/create/s3.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     6701 2022-09-07 04:52:30.000000 mosaicml-cli-0.3.2/mcli/objects/secrets/create/ssh.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     3782 2022-09-19 22:17:10.000000 mosaicml-cli-0.3.2/mcli/objects/secrets/docker_registry.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     1634 2022-09-19 22:17:10.000000 mosaicml-cli-0.3.2/mcli/objects/secrets/env_var.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     1122 2022-12-13 00:59:45.000000 mosaicml-cli-0.3.2/mcli/objects/secrets/gcp.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     2893 2022-10-03 22:11:44.000000 mosaicml-cli-0.3.2/mcli/objects/secrets/mounted.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     2855 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/objects/secrets/oci.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     2577 2022-09-19 22:17:10.000000 mosaicml-cli-0.3.2/mcli/objects/secrets/s3.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     3952 2022-11-30 21:02:34.000000 mosaicml-cli-0.3.2/mcli/objects/secrets/ssh.py
-drwxr-xr-x   0 jeffchen   (501) staff       (20)        0 2023-04-05 00:12:43.310792 mosaicml-cli-0.3.2/mcli/sdk/
--rw-r--r--   0 jeffchen   (501) staff       (20)      586 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/sdk/__init__.py
-drwxr-xr-x   0 jeffchen   (501) staff       (20)        0 2023-04-05 00:12:43.311090 mosaicml-cli-0.3.2/mcli/serverside/
--rw-r--r--   0 jeffchen   (501) staff       (20)        0 2022-09-07 04:52:30.000000 mosaicml-cli-0.3.2/mcli/serverside/__init__.py
-drwxr-xr-x   0 jeffchen   (501) staff       (20)        0 2023-04-05 00:12:43.314132 mosaicml-cli-0.3.2/mcli/serverside/clusters/
--rw-r--r--   0 jeffchen   (501) staff       (20)      381 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/serverside/clusters/__init__.py
--rw-r--r--   0 jeffchen   (501) staff       (20)    11245 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/serverside/clusters/cluster.py
--rw-r--r--   0 jeffchen   (501) staff       (20)    23072 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/serverside/clusters/cluster_instances.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     4005 2022-10-27 20:22:32.000000 mosaicml-cli-0.3.2/mcli/serverside/clusters/cluster_pv_setup.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     2793 2022-09-27 00:07:54.000000 mosaicml-cli-0.3.2/mcli/serverside/clusters/gpu_type.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     2824 2023-01-26 01:45:43.000000 mosaicml-cli-0.3.2/mcli/serverside/clusters/instance_type.py
-drwxr-xr-x   0 jeffchen   (501) staff       (20)        0 2023-04-05 00:12:43.323297 mosaicml-cli-0.3.2/mcli/serverside/clusters/overrides/
--rw-r--r--   0 jeffchen   (501) staff       (20)     1603 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/serverside/clusters/overrides/__init__.py
--rw-r--r--   0 jeffchen   (501) staff       (20)      548 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/serverside/clusters/overrides/microk8s.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     2219 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/serverside/clusters/overrides/r10z1.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     2822 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/serverside/clusters/overrides/r1z1.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     2495 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/serverside/clusters/overrides/r1z4.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     2759 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/serverside/clusters/overrides/r3z1.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     5355 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/serverside/clusters/overrides/r4z1.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     1049 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/serverside/clusters/overrides/r7z1.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     1161 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/serverside/clusters/overrides/r7z10.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     2497 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/serverside/clusters/overrides/r7z2.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     1062 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/serverside/clusters/overrides/r7z3.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     1034 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/serverside/clusters/overrides/r7z4.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     1047 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/serverside/clusters/overrides/r7z5.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     1047 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/serverside/clusters/overrides/r7z6.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     1214 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/serverside/clusters/overrides/r7z7.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     1242 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/serverside/clusters/overrides/r7z9.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     1034 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/serverside/clusters/overrides/r8z1.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     1071 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/serverside/clusters/overrides/r8z2.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     1054 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/serverside/clusters/overrides/r8z3.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     1061 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/serverside/clusters/overrides/r99z1.py
--rw-r--r--   0 jeffchen   (501) staff       (20)      310 2022-09-20 00:08:28.000000 mosaicml-cli-0.3.2/mcli/serverside/clusters/volumekind.py
-drwxr-xr-x   0 jeffchen   (501) staff       (20)        0 2023-04-05 00:12:43.330185 mosaicml-cli-0.3.2/mcli/serverside/job/
--rw-r--r--   0 jeffchen   (501) staff       (20)        0 2022-09-07 04:52:30.000000 mosaicml-cli-0.3.2/mcli/serverside/job/__init__.py
--rw-r--r--   0 jeffchen   (501) staff       (20)    15555 2023-02-01 21:37:29.000000 mosaicml-cli-0.3.2/mcli/serverside/job/mcli_job.py
--rw-r--r--   0 jeffchen   (501) staff       (20)      465 2022-09-07 04:52:30.000000 mosaicml-cli-0.3.2/mcli/serverside/job/mcli_k8s_config_map_typing.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     6471 2023-02-01 21:37:29.000000 mosaicml-cli-0.3.2/mcli/serverside/job/mcli_k8s_job.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     8090 2022-09-07 04:52:30.000000 mosaicml-cli-0.3.2/mcli/serverside/job/mcli_k8s_job_typing.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     7524 2022-10-06 23:40:35.000000 mosaicml-cli-0.3.2/mcli/serverside/job/mcli_k8s_resource_requirements_typing.py
--rw-r--r--   0 jeffchen   (501) staff       (20)      459 2022-09-07 04:52:30.000000 mosaicml-cli-0.3.2/mcli/serverside/job/mcli_k8s_service_typing.py
-drwxr-xr-x   0 jeffchen   (501) staff       (20)        0 2023-04-05 00:12:43.330730 mosaicml-cli-0.3.2/mcli/serverside/runners/
--rw-r--r--   0 jeffchen   (501) staff       (20)        0 2022-09-07 04:52:30.000000 mosaicml-cli-0.3.2/mcli/serverside/runners/__init__.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     5770 2022-12-13 00:59:45.000000 mosaicml-cli-0.3.2/mcli/serverside/runners/runner.py
-drwxr-xr-x   0 jeffchen   (501) staff       (20)        0 2023-04-05 00:12:43.338861 mosaicml-cli-0.3.2/mcli/utils/
--rw-r--r--   0 jeffchen   (501) staff       (20)        0 2022-09-07 04:52:30.000000 mosaicml-cli-0.3.2/mcli/utils/__init__.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     5306 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/utils/utils_cli.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     2555 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/utils/utils_config.py
--rw-r--r--   0 jeffchen   (501) staff       (20)      740 2022-09-23 00:37:17.000000 mosaicml-cli-0.3.2/mcli/utils/utils_date.py
--rw-r--r--   0 jeffchen   (501) staff       (20)    10453 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/utils/utils_docker.py
--rw-r--r--   0 jeffchen   (501) staff       (20)    12947 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/utils/utils_epilog.py
--rw-r--r--   0 jeffchen   (501) staff       (20)      751 2022-09-07 04:52:30.000000 mosaicml-cli-0.3.2/mcli/utils/utils_file.py
--rw-r--r--   0 jeffchen   (501) staff       (20)    11769 2022-12-09 18:28:49.000000 mosaicml-cli-0.3.2/mcli/utils/utils_interactive.py
--rw-r--r--   0 jeffchen   (501) staff       (20)    49322 2022-11-14 21:21:56.000000 mosaicml-cli-0.3.2/mcli/utils/utils_kube.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     6980 2023-02-01 21:37:29.000000 mosaicml-cli-0.3.2/mcli/utils/utils_kube_labels.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     4741 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/utils/utils_logging.py
--rw-r--r--   0 jeffchen   (501) staff       (20)      359 2022-09-07 04:52:30.000000 mosaicml-cli-0.3.2/mcli/utils/utils_modules.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     6614 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/utils/utils_pypi.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     6513 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/utils/utils_rancher.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     3115 2022-09-08 17:54:07.000000 mosaicml-cli-0.3.2/mcli/utils/utils_rich.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     8533 2022-12-01 00:52:00.000000 mosaicml-cli-0.3.2/mcli/utils/utils_run_status.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     4350 2022-09-09 21:35:49.000000 mosaicml-cli-0.3.2/mcli/utils/utils_serializable_dataclass.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     1103 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/utils/utils_spinner.py
--rw-r--r--   0 jeffchen   (501) staff       (20)    11437 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/utils/utils_string_functions.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     3954 2022-11-30 21:02:34.000000 mosaicml-cli-0.3.2/mcli/utils/utils_types.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     1001 2022-09-07 04:52:30.000000 mosaicml-cli-0.3.2/mcli/utils/utils_yaml.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     3884 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/mcli/version.py
-drwxr-xr-x   0 jeffchen   (501) staff       (20)        0 2023-04-05 00:12:43.341799 mosaicml-cli-0.3.2/mosaicml_cli.egg-info/
--rw-r--r--   0 jeffchen   (501) staff       (20)      696 2023-04-05 00:12:43.000000 mosaicml-cli-0.3.2/mosaicml_cli.egg-info/PKG-INFO
--rw-r--r--   0 jeffchen   (501) staff       (20)     7139 2023-04-05 00:12:43.000000 mosaicml-cli-0.3.2/mosaicml_cli.egg-info/SOURCES.txt
--rw-r--r--   0 jeffchen   (501) staff       (20)        1 2023-04-05 00:12:43.000000 mosaicml-cli-0.3.2/mosaicml_cli.egg-info/dependency_links.txt
--rw-r--r--   0 jeffchen   (501) staff       (20)       75 2023-04-05 00:12:43.000000 mosaicml-cli-0.3.2/mosaicml_cli.egg-info/entry_points.txt
--rw-r--r--   0 jeffchen   (501) staff       (20)     1630 2023-04-05 00:12:43.000000 mosaicml-cli-0.3.2/mosaicml_cli.egg-info/requires.txt
--rw-r--r--   0 jeffchen   (501) staff       (20)       11 2023-04-05 00:12:43.000000 mosaicml-cli-0.3.2/mosaicml_cli.egg-info/top_level.txt
--rw-r--r--   0 jeffchen   (501) staff       (20)    30933 2022-12-14 22:12:45.000000 mosaicml-cli-0.3.2/pyproject.toml
--rw-r--r--   0 jeffchen   (501) staff       (20)       38 2023-04-05 00:12:43.359339 mosaicml-cli-0.3.2/setup.cfg
--rw-r--r--   0 jeffchen   (501) staff       (20)     3111 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/setup.py
-drwxr-xr-x   0 jeffchen   (501) staff       (20)        0 2023-04-05 00:12:43.350087 mosaicml-cli-0.3.2/tests/
-drwxr-xr-x   0 jeffchen   (501) staff       (20)        0 2023-04-05 00:12:43.355835 mosaicml-cli-0.3.2/tests/submit/
--rw-r--r--   0 jeffchen   (501) staff       (20)        0 2022-09-07 04:52:30.000000 mosaicml-cli-0.3.2/tests/submit/__init__.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     6393 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/tests/submit/test_cluster.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     9266 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/tests/submit/test_cluster_secrets.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     7973 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/tests/test_config.py
--rw-r--r--   0 jeffchen   (501) staff       (20)       62 2022-09-07 04:52:30.000000 mosaicml-cli-0.3.2/tests/test_simple.py
--rw-r--r--   0 jeffchen   (501) staff       (20)     6116 2023-04-05 00:11:39.000000 mosaicml-cli-0.3.2/tests/test_upgrade.py
+drwxr-xr-x   0 anna       (501) staff       (20)        0 2023-04-06 21:21:43.508520 mosaicml-cli-0.3.3/
+-rw-r--r--   0 anna       (501) staff       (20)      696 2023-04-06 21:21:43.508200 mosaicml-cli-0.3.3/PKG-INFO
+-rw-r--r--   0 anna       (501) staff       (20)     7799 2023-03-27 21:07:48.000000 mosaicml-cli-0.3.3/README.md
+drwxr-xr-x   0 anna       (501) staff       (20)        0 2023-04-06 21:21:43.428429 mosaicml-cli-0.3.3/mcli/
+-rw-r--r--   0 anna       (501) staff       (20)       54 2022-12-14 17:51:04.000000 mosaicml-cli-0.3.3/mcli/__init__.py
+drwxr-xr-x   0 anna       (501) staff       (20)        0 2023-04-06 21:21:43.429519 mosaicml-cli-0.3.3/mcli/api/
+-rw-r--r--   0 anna       (501) staff       (20)        0 2022-07-01 20:27:34.000000 mosaicml-cli-0.3.3/mcli/api/__init__.py
+drwxr-xr-x   0 anna       (501) staff       (20)        0 2023-04-06 21:21:43.430281 mosaicml-cli-0.3.3/mcli/api/cluster/
+-rw-r--r--   0 anna       (501) staff       (20)      134 2022-10-27 22:42:42.000000 mosaicml-cli-0.3.3/mcli/api/cluster/__init__.py
+-rw-r--r--   0 anna       (501) staff       (20)     4058 2023-03-30 22:21:56.000000 mosaicml-cli-0.3.3/mcli/api/cluster/api_get_clusters.py
+drwxr-xr-x   0 anna       (501) staff       (20)        0 2023-04-06 21:21:43.431671 mosaicml-cli-0.3.3/mcli/api/engine/
+-rw-r--r--   0 anna       (501) staff       (20)        0 2022-07-01 20:27:34.000000 mosaicml-cli-0.3.3/mcli/api/engine/__init__.py
+-rw-r--r--   0 anna       (501) staff       (20)    22935 2023-04-05 22:41:30.000000 mosaicml-cli-0.3.3/mcli/api/engine/engine.py
+-rw-r--r--   0 anna       (501) staff       (20)      787 2022-09-12 18:09:44.000000 mosaicml-cli-0.3.3/mcli/api/engine/utils.py
+-rw-r--r--   0 anna       (501) staff       (20)    11677 2023-04-05 22:17:10.000000 mosaicml-cli-0.3.3/mcli/api/exceptions.py
+drwxr-xr-x   0 anna       (501) staff       (20)        0 2023-04-06 21:21:43.433550 mosaicml-cli-0.3.3/mcli/api/inference_deployments/
+-rw-r--r--   0 anna       (501) staff       (20)      858 2023-03-30 22:21:56.000000 mosaicml-cli-0.3.3/mcli/api/inference_deployments/__init__.py
+-rw-r--r--   0 anna       (501) staff       (20)     3388 2023-03-30 22:24:52.000000 mosaicml-cli-0.3.3/mcli/api/inference_deployments/api_create_inference_deployment.py
+-rw-r--r--   0 anna       (501) staff       (20)     3278 2023-03-30 22:24:52.000000 mosaicml-cli-0.3.3/mcli/api/inference_deployments/api_delete_inference_deployments.py
+-rw-r--r--   0 anna       (501) staff       (20)     6091 2023-03-30 22:24:52.000000 mosaicml-cli-0.3.3/mcli/api/inference_deployments/api_get_inference_deployments.py
+-rw-r--r--   0 anna       (501) staff       (20)     1156 2023-03-30 22:24:52.000000 mosaicml-cli-0.3.3/mcli/api/inference_deployments/api_ping_inference_deployment.py
+-rw-r--r--   0 anna       (501) staff       (20)     1276 2023-03-30 22:24:52.000000 mosaicml-cli-0.3.3/mcli/api/inference_deployments/api_predict_inference_deployment.py
+drwxr-xr-x   0 anna       (501) staff       (20)        0 2023-04-06 21:21:43.433818 mosaicml-cli-0.3.3/mcli/api/kube/
+-rw-r--r--   0 anna       (501) staff       (20)        0 2022-09-01 16:10:03.000000 mosaicml-cli-0.3.3/mcli/api/kube/__init__.py
+drwxr-xr-x   0 anna       (501) staff       (20)        0 2023-04-06 21:21:43.435990 mosaicml-cli-0.3.3/mcli/api/kube/runs/
+-rw-r--r--   0 anna       (501) staff       (20)      856 2022-09-01 16:10:03.000000 mosaicml-cli-0.3.3/mcli/api/kube/runs/__init__.py
+-rw-r--r--   0 anna       (501) staff       (20)     4900 2023-04-06 21:21:07.000000 mosaicml-cli-0.3.3/mcli/api/kube/runs/api_create_run.py
+-rw-r--r--   0 anna       (501) staff       (20)     5042 2023-03-27 21:07:48.000000 mosaicml-cli-0.3.3/mcli/api/kube/runs/api_delete_runs.py
+-rw-r--r--   0 anna       (501) staff       (20)    14458 2023-03-27 21:07:48.000000 mosaicml-cli-0.3.3/mcli/api/kube/runs/api_get_run_logs.py
+-rw-r--r--   0 anna       (501) staff       (20)    16142 2023-04-06 21:21:07.000000 mosaicml-cli-0.3.3/mcli/api/kube/runs/api_get_runs.py
+-rw-r--r--   0 anna       (501) staff       (20)     6007 2023-03-27 21:07:48.000000 mosaicml-cli-0.3.3/mcli/api/kube/runs/api_stop_runs.py
+-rw-r--r--   0 anna       (501) staff       (20)     6210 2022-12-16 00:52:51.000000 mosaicml-cli-0.3.3/mcli/api/kube/runs/api_watch_run.py
+drwxr-xr-x   0 anna       (501) staff       (20)        0 2023-04-06 21:21:43.436596 mosaicml-cli-0.3.3/mcli/api/mint/
+-rw-r--r--   0 anna       (501) staff       (20)        0 2023-03-27 21:07:48.000000 mosaicml-cli-0.3.3/mcli/api/mint/__init__.py
+-rw-r--r--   0 anna       (501) staff       (20)     4987 2023-03-27 21:07:48.000000 mosaicml-cli-0.3.3/mcli/api/mint/shell.py
+-rw-r--r--   0 anna       (501) staff       (20)     1530 2023-03-27 21:07:48.000000 mosaicml-cli-0.3.3/mcli/api/mint/tty.py
+drwxr-xr-x   0 anna       (501) staff       (20)        0 2023-04-06 21:21:43.437555 mosaicml-cli-0.3.3/mcli/api/model/
+-rw-r--r--   0 anna       (501) staff       (20)      209 2023-03-27 21:07:48.000000 mosaicml-cli-0.3.3/mcli/api/model/__init__.py
+-rw-r--r--   0 anna       (501) staff       (20)     5655 2023-03-30 20:02:22.000000 mosaicml-cli-0.3.3/mcli/api/model/cluster_details.py
+-rw-r--r--   0 anna       (501) staff       (20)     3015 2023-03-30 22:24:52.000000 mosaicml-cli-0.3.3/mcli/api/model/inference_deployment.py
+-rw-r--r--   0 anna       (501) staff       (20)     4050 2023-04-06 21:21:07.000000 mosaicml-cli-0.3.3/mcli/api/model/run.py
+drwxr-xr-x   0 anna       (501) staff       (20)        0 2023-04-06 21:21:43.439335 mosaicml-cli-0.3.3/mcli/api/runs/
+-rw-r--r--   0 anna       (501) staff       (20)      828 2023-04-06 21:20:57.000000 mosaicml-cli-0.3.3/mcli/api/runs/__init__.py
+-rw-r--r--   0 anna       (501) staff       (20)     2683 2023-04-06 21:21:07.000000 mosaicml-cli-0.3.3/mcli/api/runs/api_create_run.py
+-rw-r--r--   0 anna       (501) staff       (20)     3947 2023-04-06 21:21:07.000000 mosaicml-cli-0.3.3/mcli/api/runs/api_delete_runs.py
+-rw-r--r--   0 anna       (501) staff       (20)     9281 2023-03-30 22:21:56.000000 mosaicml-cli-0.3.3/mcli/api/runs/api_get_run_logs.py
+-rw-r--r--   0 anna       (501) staff       (20)     6563 2023-04-06 21:21:07.000000 mosaicml-cli-0.3.3/mcli/api/runs/api_get_runs.py
+-rw-r--r--   0 anna       (501) staff       (20)     6037 2023-04-06 21:21:07.000000 mosaicml-cli-0.3.3/mcli/api/runs/api_stop_runs.py
+-rw-r--r--   0 anna       (501) staff       (20)    10619 2023-03-27 21:07:48.000000 mosaicml-cli-0.3.3/mcli/api/runs/api_watch_run.py
+drwxr-xr-x   0 anna       (501) staff       (20)        0 2023-04-06 21:21:43.439738 mosaicml-cli-0.3.3/mcli/api/schema/
+-rw-r--r--   0 anna       (501) staff       (20)        0 2022-07-01 20:27:34.000000 mosaicml-cli-0.3.3/mcli/api/schema/__init__.py
+-rw-r--r--   0 anna       (501) staff       (20)      636 2022-09-01 16:10:03.000000 mosaicml-cli-0.3.3/mcli/api/schema/generic_model.py
+drwxr-xr-x   0 anna       (501) staff       (20)        0 2023-04-06 21:21:43.441241 mosaicml-cli-0.3.3/mcli/api/secrets/
+-rw-r--r--   0 anna       (501) staff       (20)      309 2022-10-06 23:19:14.000000 mosaicml-cli-0.3.3/mcli/api/secrets/__init__.py
+-rw-r--r--   0 anna       (501) staff       (20)     2365 2023-03-30 23:10:34.000000 mosaicml-cli-0.3.3/mcli/api/secrets/api_create_secret.py
+-rw-r--r--   0 anna       (501) staff       (20)     2998 2023-03-30 22:21:56.000000 mosaicml-cli-0.3.3/mcli/api/secrets/api_delete_secrets.py
+-rw-r--r--   0 anna       (501) staff       (20)     3697 2023-03-30 22:21:56.000000 mosaicml-cli-0.3.3/mcli/api/secrets/api_get_secrets.py
+-rw-r--r--   0 anna       (501) staff       (20)      508 2023-01-12 23:53:10.000000 mosaicml-cli-0.3.3/mcli/api/types.py
+-rw-r--r--   0 anna       (501) staff       (20)     2354 2022-08-15 20:43:31.000000 mosaicml-cli-0.3.3/mcli/api/typing_future.py
+drwxr-xr-x   0 anna       (501) staff       (20)        0 2023-04-06 21:21:43.441995 mosaicml-cli-0.3.3/mcli/api/users/
+-rw-r--r--   0 anna       (501) staff       (20)      139 2023-02-22 17:58:38.000000 mosaicml-cli-0.3.3/mcli/api/users/__init__.py
+-rw-r--r--   0 anna       (501) staff       (20)     2694 2023-03-27 21:07:48.000000 mosaicml-cli-0.3.3/mcli/api/users/api_get_users.py
+drwxr-xr-x   0 anna       (501) staff       (20)        0 2023-04-06 21:21:43.442308 mosaicml-cli-0.3.3/mcli/cli/
+-rw-r--r--   0 anna       (501) staff       (20)        0 2022-07-01 20:27:34.000000 mosaicml-cli-0.3.3/mcli/cli/__init__.py
+-rwxr-xr-x   0 anna       (501) staff       (20)     7182 2023-03-30 22:21:56.000000 mosaicml-cli-0.3.3/mcli/cli/cli.py
+drwxr-xr-x   0 anna       (501) staff       (20)        0 2023-04-06 21:21:43.442893 mosaicml-cli-0.3.3/mcli/cli/common/
+-rw-r--r--   0 anna       (501) staff       (20)        0 2023-02-02 22:26:54.000000 mosaicml-cli-0.3.3/mcli/cli/common/__init__.py
+-rw-r--r--   0 anna       (501) staff       (20)     2670 2023-03-27 21:07:48.000000 mosaicml-cli-0.3.3/mcli/cli/common/deployment_filters.py
+-rw-r--r--   0 anna       (501) staff       (20)     7180 2023-04-06 21:21:07.000000 mosaicml-cli-0.3.3/mcli/cli/common/run_filters.py
+drwxr-xr-x   0 anna       (501) staff       (20)        0 2023-04-06 21:21:43.443349 mosaicml-cli-0.3.3/mcli/cli/m_clean/
+-rw-r--r--   0 anna       (501) staff       (20)        0 2022-07-01 20:27:34.000000 mosaicml-cli-0.3.3/mcli/cli/m_clean/__init__.py
+-rw-r--r--   0 anna       (501) staff       (20)      950 2022-10-27 22:42:42.000000 mosaicml-cli-0.3.3/mcli/cli/m_clean/m_clean.py
+drwxr-xr-x   0 anna       (501) staff       (20)        0 2023-04-06 21:21:43.443899 mosaicml-cli-0.3.3/mcli/cli/m_connect/
+-rw-r--r--   0 anna       (501) staff       (20)        0 2023-03-27 21:07:48.000000 mosaicml-cli-0.3.3/mcli/cli/m_connect/__init__.py
+-rw-r--r--   0 anna       (501) staff       (20)     1541 2023-03-27 21:07:48.000000 mosaicml-cli-0.3.3/mcli/cli/m_connect/m_connect.py
+drwxr-xr-x   0 anna       (501) staff       (20)        0 2023-04-06 21:21:43.445209 mosaicml-cli-0.3.3/mcli/cli/m_create/
+-rw-r--r--   0 anna       (501) staff       (20)        0 2022-07-01 20:27:34.000000 mosaicml-cli-0.3.3/mcli/cli/m_create/__init__.py
+-rw-r--r--   0 anna       (501) staff       (20)    11513 2023-03-31 04:06:45.000000 mosaicml-cli-0.3.3/mcli/cli/m_create/cluster.py
+-rw-r--r--   0 anna       (501) staff       (20)     7167 2023-03-31 04:06:45.000000 mosaicml-cli-0.3.3/mcli/cli/m_create/env_var.py
+-rw-r--r--   0 anna       (501) staff       (20)     4217 2023-03-31 04:06:45.000000 mosaicml-cli-0.3.3/mcli/cli/m_create/m_create.py
+-rw-r--r--   0 anna       (501) staff       (20)    24927 2023-03-31 04:06:45.000000 mosaicml-cli-0.3.3/mcli/cli/m_create/secret.py
+drwxr-xr-x   0 anna       (501) staff       (20)        0 2023-04-06 21:21:43.446005 mosaicml-cli-0.3.3/mcli/cli/m_delete/
+-rw-r--r--   0 anna       (501) staff       (20)        0 2022-07-01 20:27:34.000000 mosaicml-cli-0.3.3/mcli/cli/m_delete/__init__.py
+-rw-r--r--   0 anna       (501) staff       (20)    14072 2023-03-31 04:06:45.000000 mosaicml-cli-0.3.3/mcli/cli/m_delete/delete.py
+-rw-r--r--   0 anna       (501) staff       (20)     8417 2023-03-31 04:06:45.000000 mosaicml-cli-0.3.3/mcli/cli/m_delete/m_delete.py
+drwxr-xr-x   0 anna       (501) staff       (20)        0 2023-04-06 21:21:43.446453 mosaicml-cli-0.3.3/mcli/cli/m_deploy/
+-rw-r--r--   0 anna       (501) staff       (20)        0 2023-03-27 21:07:48.000000 mosaicml-cli-0.3.3/mcli/cli/m_deploy/__init__.py
+-rw-r--r--   0 anna       (501) staff       (20)     3896 2023-03-27 21:07:48.000000 mosaicml-cli-0.3.3/mcli/cli/m_deploy/m_deploy.py
+drwxr-xr-x   0 anna       (501) staff       (20)        0 2023-04-06 21:21:43.447292 mosaicml-cli-0.3.3/mcli/cli/m_describe/
+-rw-r--r--   0 anna       (501) staff       (20)        0 2023-02-02 22:26:54.000000 mosaicml-cli-0.3.3/mcli/cli/m_describe/__init__.py
+-rw-r--r--   0 anna       (501) staff       (20)     4409 2023-03-30 22:24:52.000000 mosaicml-cli-0.3.3/mcli/cli/m_describe/describe_inference_deployments.py
+-rw-r--r--   0 anna       (501) staff       (20)     7391 2023-04-06 21:20:57.000000 mosaicml-cli-0.3.3/mcli/cli/m_describe/describe_runs.py
+-rw-r--r--   0 anna       (501) staff       (20)     1860 2023-03-30 22:24:52.000000 mosaicml-cli-0.3.3/mcli/cli/m_describe/m_describe.py
+drwxr-xr-x   0 anna       (501) staff       (20)        0 2023-04-06 21:21:43.449472 mosaicml-cli-0.3.3/mcli/cli/m_get/
+-rw-r--r--   0 anna       (501) staff       (20)      549 2023-03-31 04:06:45.000000 mosaicml-cli-0.3.3/mcli/cli/m_get/__init__.py
+-rw-r--r--   0 anna       (501) staff       (20)     3909 2023-03-31 01:05:42.000000 mosaicml-cli-0.3.3/mcli/cli/m_get/clusters.py
+-rw-r--r--   0 anna       (501) staff       (20)     6452 2023-04-05 17:48:41.000000 mosaicml-cli-0.3.3/mcli/cli/m_get/display.py
+-rw-r--r--   0 anna       (501) staff       (20)     1315 2023-03-31 04:06:45.000000 mosaicml-cli-0.3.3/mcli/cli/m_get/envvars.py
+-rw-r--r--   0 anna       (501) staff       (20)     5361 2023-03-27 21:07:48.000000 mosaicml-cli-0.3.3/mcli/cli/m_get/inference_deployments.py
+-rw-r--r--   0 anna       (501) staff       (20)     4866 2023-03-31 04:06:45.000000 mosaicml-cli-0.3.3/mcli/cli/m_get/m_get.py
+-rw-r--r--   0 anna       (501) staff       (20)     6289 2023-04-06 21:21:07.000000 mosaicml-cli-0.3.3/mcli/cli/m_get/runs.py
+-rw-r--r--   0 anna       (501) staff       (20)     3567 2023-03-31 04:06:45.000000 mosaicml-cli-0.3.3/mcli/cli/m_get/secrets.py
+-rw-r--r--   0 anna       (501) staff       (20)     1580 2023-02-22 17:58:38.000000 mosaicml-cli-0.3.3/mcli/cli/m_get/users.py
+drwxr-xr-x   0 anna       (501) staff       (20)        0 2023-04-06 21:21:43.450008 mosaicml-cli-0.3.3/mcli/cli/m_init/
+-rw-r--r--   0 anna       (501) staff       (20)        0 2022-07-01 20:27:34.000000 mosaicml-cli-0.3.3/mcli/cli/m_init/__init__.py
+-rw-r--r--   0 anna       (501) staff       (20)     4113 2023-03-30 22:21:56.000000 mosaicml-cli-0.3.3/mcli/cli/m_init/m_init.py
+-rw-r--r--   0 anna       (501) staff       (20)     9374 2023-03-31 01:05:42.000000 mosaicml-cli-0.3.3/mcli/cli/m_init/m_init_kube.py
+drwxr-xr-x   0 anna       (501) staff       (20)        0 2023-04-06 21:21:43.450916 mosaicml-cli-0.3.3/mcli/cli/m_interactive/
+-rw-r--r--   0 anna       (501) staff       (20)        0 2022-07-01 20:27:34.000000 mosaicml-cli-0.3.3/mcli/cli/m_interactive/__init__.py
+-rw-r--r--   0 anna       (501) staff       (20)     9005 2023-03-31 20:52:34.000000 mosaicml-cli-0.3.3/mcli/cli/m_interactive/interactive.py
+-rw-r--r--   0 anna       (501) staff       (20)    16203 2023-04-06 21:21:07.000000 mosaicml-cli-0.3.3/mcli/cli/m_interactive/m_interactive.py
+-rw-r--r--   0 anna       (501) staff       (20)     4571 2023-04-06 21:21:07.000000 mosaicml-cli-0.3.3/mcli/cli/m_interactive/temp_mcloud_interactive.py
+drwxr-xr-x   0 anna       (501) staff       (20)        0 2023-04-06 21:21:43.451187 mosaicml-cli-0.3.3/mcli/cli/m_log/
+-rw-r--r--   0 anna       (501) staff       (20)        0 2022-07-01 20:27:34.000000 mosaicml-cli-0.3.3/mcli/cli/m_log/__init__.py
+-rw-r--r--   0 anna       (501) staff       (20)     8633 2023-04-06 21:21:07.000000 mosaicml-cli-0.3.3/mcli/cli/m_log/m_log.py
+drwxr-xr-x   0 anna       (501) staff       (20)        0 2023-04-06 21:21:43.451457 mosaicml-cli-0.3.3/mcli/cli/m_ping/
+-rw-r--r--   0 anna       (501) staff       (20)        0 2023-03-27 21:07:48.000000 mosaicml-cli-0.3.3/mcli/cli/m_ping/__init__.py
+-rw-r--r--   0 anna       (501) staff       (20)     1742 2023-03-30 22:21:56.000000 mosaicml-cli-0.3.3/mcli/cli/m_ping/m_ping.py
+drwxr-xr-x   0 anna       (501) staff       (20)        0 2023-04-06 21:21:43.451719 mosaicml-cli-0.3.3/mcli/cli/m_predict/
+-rw-r--r--   0 anna       (501) staff       (20)        0 2023-03-30 22:21:56.000000 mosaicml-cli-0.3.3/mcli/cli/m_predict/__init__.py
+-rw-r--r--   0 anna       (501) staff       (20)     2160 2023-03-30 22:21:56.000000 mosaicml-cli-0.3.3/mcli/cli/m_predict/m_predict.py
+drwxr-xr-x   0 anna       (501) staff       (20)        0 2023-04-06 21:21:43.451974 mosaicml-cli-0.3.3/mcli/cli/m_root/
+-rw-r--r--   0 anna       (501) staff       (20)        0 2022-07-01 20:27:34.000000 mosaicml-cli-0.3.3/mcli/cli/m_root/__init__.py
+-rw-r--r--   0 anna       (501) staff       (20)      947 2023-03-31 04:06:45.000000 mosaicml-cli-0.3.3/mcli/cli/m_root/m_config.py
+drwxr-xr-x   0 anna       (501) staff       (20)        0 2023-04-06 21:21:43.452371 mosaicml-cli-0.3.3/mcli/cli/m_run/
+-rw-r--r--   0 anna       (501) staff       (20)        0 2022-07-01 20:27:34.000000 mosaicml-cli-0.3.3/mcli/cli/m_run/__init__.py
+-rw-r--r--   0 anna       (501) staff       (20)     9494 2023-03-27 21:07:48.000000 mosaicml-cli-0.3.3/mcli/cli/m_run/m_run.py
+drwxr-xr-x   0 anna       (501) staff       (20)        0 2023-04-06 21:21:43.453256 mosaicml-cli-0.3.3/mcli/cli/m_set_unset/
+-rw-r--r--   0 anna       (501) staff       (20)        0 2022-10-06 23:19:14.000000 mosaicml-cli-0.3.3/mcli/cli/m_set_unset/__init__.py
+-rw-r--r--   0 anna       (501) staff       (20)     2973 2023-04-06 21:21:07.000000 mosaicml-cli-0.3.3/mcli/cli/m_set_unset/api_key.py
+-rw-r--r--   0 anna       (501) staff       (20)     1927 2023-04-06 21:21:07.000000 mosaicml-cli-0.3.3/mcli/cli/m_set_unset/m_set.py
+-rw-r--r--   0 anna       (501) staff       (20)     1408 2023-02-22 17:58:38.000000 mosaicml-cli-0.3.3/mcli/cli/m_set_unset/m_unset.py
+-rw-r--r--   0 anna       (501) staff       (20)      881 2023-02-22 17:58:38.000000 mosaicml-cli-0.3.3/mcli/cli/m_set_unset/user.py
+drwxr-xr-x   0 anna       (501) staff       (20)        0 2023-04-06 21:21:43.453576 mosaicml-cli-0.3.3/mcli/cli/m_stop/
+-rw-r--r--   0 anna       (501) staff       (20)        0 2022-10-06 23:19:14.000000 mosaicml-cli-0.3.3/mcli/cli/m_stop/__init__.py
+-rw-r--r--   0 anna       (501) staff       (20)     3847 2023-03-27 21:07:48.000000 mosaicml-cli-0.3.3/mcli/cli/m_stop/m_stop.py
+drwxr-xr-x   0 anna       (501) staff       (20)        0 2023-04-06 21:21:43.454050 mosaicml-cli-0.3.3/mcli/cli/m_use/
+-rw-r--r--   0 anna       (501) staff       (20)        0 2022-07-01 20:27:34.000000 mosaicml-cli-0.3.3/mcli/cli/m_use/__init__.py
+-rw-r--r--   0 anna       (501) staff       (20)     3234 2022-12-21 22:27:10.000000 mosaicml-cli-0.3.3/mcli/cli/m_use/m_use.py
+drwxr-xr-x   0 anna       (501) staff       (20)        0 2023-04-06 21:21:43.455137 mosaicml-cli-0.3.3/mcli/cli/m_util/
+-rw-r--r--   0 anna       (501) staff       (20)        0 2022-09-01 16:10:03.000000 mosaicml-cli-0.3.3/mcli/cli/m_util/__init__.py
+-rw-r--r--   0 anna       (501) staff       (20)     9853 2023-03-27 21:07:48.000000 mosaicml-cli-0.3.3/mcli/cli/m_util/kube_util.py
+-rw-r--r--   0 anna       (501) staff       (20)     1147 2022-10-27 22:42:42.000000 mosaicml-cli-0.3.3/mcli/cli/m_util/m_util.py
+-rw-r--r--   0 anna       (501) staff       (20)     6515 2023-03-30 22:24:52.000000 mosaicml-cli-0.3.3/mcli/cli/m_util/util.py
+-rw-r--r--   0 anna       (501) staff       (20)    16462 2023-04-06 21:21:07.000000 mosaicml-cli-0.3.3/mcli/config.py
+drwxr-xr-x   0 anna       (501) staff       (20)        0 2023-04-06 21:21:43.457062 mosaicml-cli-0.3.3/mcli/models/
+-rw-r--r--   0 anna       (501) staff       (20)     1061 2023-03-27 21:07:48.000000 mosaicml-cli-0.3.3/mcli/models/__init__.py
+-rw-r--r--   0 anna       (501) staff       (20)     7179 2023-03-30 22:24:52.000000 mosaicml-cli-0.3.3/mcli/models/inference_deployment_config.py
+-rw-r--r--   0 anna       (501) staff       (20)     3693 2023-03-30 20:02:22.000000 mosaicml-cli-0.3.3/mcli/models/mcli_cluster.py
+-rw-r--r--   0 anna       (501) staff       (20)      563 2022-09-12 19:04:53.000000 mosaicml-cli-0.3.3/mcli/models/mcli_envvar.py
+-rw-r--r--   0 anna       (501) staff       (20)     3386 2022-10-06 23:19:14.000000 mosaicml-cli-0.3.3/mcli/models/mcli_integration.py
+-rw-r--r--   0 anna       (501) staff       (20)     9400 2023-03-31 04:06:45.000000 mosaicml-cli-0.3.3/mcli/models/mcli_secret.py
+-rw-r--r--   0 anna       (501) staff       (20)    21114 2023-04-06 21:20:57.000000 mosaicml-cli-0.3.3/mcli/models/run_config.py
+drwxr-xr-x   0 anna       (501) staff       (20)        0 2023-04-06 21:21:43.457474 mosaicml-cli-0.3.3/mcli/objects/
+-rw-r--r--   0 anna       (501) staff       (20)        0 2022-07-01 20:27:34.000000 mosaicml-cli-0.3.3/mcli/objects/__init__.py
+drwxr-xr-x   0 anna       (501) staff       (20)        0 2023-04-06 21:21:43.459561 mosaicml-cli-0.3.3/mcli/objects/integrations/
+-rw-r--r--   0 anna       (501) staff       (20)      660 2022-10-06 23:19:14.000000 mosaicml-cli-0.3.3/mcli/objects/integrations/__init__.py
+-rw-r--r--   0 anna       (501) staff       (20)      671 2022-07-14 18:08:16.000000 mosaicml-cli-0.3.3/mcli/objects/integrations/apt_packages.py
+-rw-r--r--   0 anna       (501) staff       (20)     1287 2022-10-06 23:19:14.000000 mosaicml-cli-0.3.3/mcli/objects/integrations/comet.py
+-rw-r--r--   0 anna       (501) staff       (20)     2597 2023-02-02 22:26:54.000000 mosaicml-cli-0.3.3/mcli/objects/integrations/git_repo.py
+-rw-r--r--   0 anna       (501) staff       (20)     3491 2022-10-06 23:19:14.000000 mosaicml-cli-0.3.3/mcli/objects/integrations/local.py
+-rw-r--r--   0 anna       (501) staff       (20)     2126 2022-12-21 22:27:10.000000 mosaicml-cli-0.3.3/mcli/objects/integrations/mosaicml_agent.py
+-rw-r--r--   0 anna       (501) staff       (20)      810 2022-07-14 18:08:20.000000 mosaicml-cli-0.3.3/mcli/objects/integrations/pip_packages.py
+-rw-r--r--   0 anna       (501) staff       (20)     2742 2022-09-01 16:42:18.000000 mosaicml-cli-0.3.3/mcli/objects/integrations/wandb.py
+drwxr-xr-x   0 anna       (501) staff       (20)        0 2023-04-06 21:21:43.461402 mosaicml-cli-0.3.3/mcli/objects/secrets/
+-rw-r--r--   0 anna       (501) staff       (20)     1090 2022-12-21 22:27:10.000000 mosaicml-cli-0.3.3/mcli/objects/secrets/__init__.py
+-rw-r--r--   0 anna       (501) staff       (20)     4913 2023-03-31 04:06:45.000000 mosaicml-cli-0.3.3/mcli/objects/secrets/cluster_secret.py
+drwxr-xr-x   0 anna       (501) staff       (20)        0 2023-04-06 21:21:43.462897 mosaicml-cli-0.3.3/mcli/objects/secrets/create/
+-rw-r--r--   0 anna       (501) staff       (20)        0 2022-07-01 20:27:34.000000 mosaicml-cli-0.3.3/mcli/objects/secrets/create/__init__.py
+-rw-r--r--   0 anna       (501) staff       (20)     3953 2023-03-31 04:06:45.000000 mosaicml-cli-0.3.3/mcli/objects/secrets/create/base.py
+-rw-r--r--   0 anna       (501) staff       (20)     3461 2023-03-31 04:06:45.000000 mosaicml-cli-0.3.3/mcli/objects/secrets/create/docker_registry.py
+-rw-r--r--   0 anna       (501) staff       (20)     2406 2023-03-31 04:06:45.000000 mosaicml-cli-0.3.3/mcli/objects/secrets/create/gcp.py
+-rw-r--r--   0 anna       (501) staff       (20)     7554 2023-03-31 04:06:45.000000 mosaicml-cli-0.3.3/mcli/objects/secrets/create/generic.py
+-rw-r--r--   0 anna       (501) staff       (20)     3855 2023-03-31 04:06:45.000000 mosaicml-cli-0.3.3/mcli/objects/secrets/create/oci.py
+-rw-r--r--   0 anna       (501) staff       (20)     2998 2023-03-31 04:06:45.000000 mosaicml-cli-0.3.3/mcli/objects/secrets/create/s3.py
+-rw-r--r--   0 anna       (501) staff       (20)     6701 2023-03-31 04:06:45.000000 mosaicml-cli-0.3.3/mcli/objects/secrets/create/ssh.py
+-rw-r--r--   0 anna       (501) staff       (20)     3782 2023-03-31 04:06:45.000000 mosaicml-cli-0.3.3/mcli/objects/secrets/docker_registry.py
+-rw-r--r--   0 anna       (501) staff       (20)     1634 2023-03-31 04:06:45.000000 mosaicml-cli-0.3.3/mcli/objects/secrets/env_var.py
+-rw-r--r--   0 anna       (501) staff       (20)     1122 2023-03-31 04:06:45.000000 mosaicml-cli-0.3.3/mcli/objects/secrets/gcp.py
+-rw-r--r--   0 anna       (501) staff       (20)     2893 2023-03-31 04:06:45.000000 mosaicml-cli-0.3.3/mcli/objects/secrets/mounted.py
+-rw-r--r--   0 anna       (501) staff       (20)     2855 2023-03-31 04:06:45.000000 mosaicml-cli-0.3.3/mcli/objects/secrets/oci.py
+-rw-r--r--   0 anna       (501) staff       (20)     2577 2023-03-31 04:06:45.000000 mosaicml-cli-0.3.3/mcli/objects/secrets/s3.py
+-rw-r--r--   0 anna       (501) staff       (20)     3952 2023-03-31 04:06:45.000000 mosaicml-cli-0.3.3/mcli/objects/secrets/ssh.py
+drwxr-xr-x   0 anna       (501) staff       (20)        0 2023-04-06 21:21:43.463087 mosaicml-cli-0.3.3/mcli/sdk/
+-rw-r--r--   0 anna       (501) staff       (20)      586 2023-04-06 21:20:57.000000 mosaicml-cli-0.3.3/mcli/sdk/__init__.py
+drwxr-xr-x   0 anna       (501) staff       (20)        0 2023-04-06 21:21:43.463247 mosaicml-cli-0.3.3/mcli/serverside/
+-rw-r--r--   0 anna       (501) staff       (20)        0 2022-07-01 20:27:34.000000 mosaicml-cli-0.3.3/mcli/serverside/__init__.py
+drwxr-xr-x   0 anna       (501) staff       (20)        0 2023-04-06 21:21:43.465114 mosaicml-cli-0.3.3/mcli/serverside/clusters/
+-rw-r--r--   0 anna       (501) staff       (20)      381 2023-03-30 20:02:22.000000 mosaicml-cli-0.3.3/mcli/serverside/clusters/__init__.py
+-rw-r--r--   0 anna       (501) staff       (20)    11245 2023-03-31 04:06:45.000000 mosaicml-cli-0.3.3/mcli/serverside/clusters/cluster.py
+-rw-r--r--   0 anna       (501) staff       (20)    23072 2023-03-30 20:02:22.000000 mosaicml-cli-0.3.3/mcli/serverside/clusters/cluster_instances.py
+-rw-r--r--   0 anna       (501) staff       (20)     4005 2022-10-27 22:42:42.000000 mosaicml-cli-0.3.3/mcli/serverside/clusters/cluster_pv_setup.py
+-rw-r--r--   0 anna       (501) staff       (20)     2793 2023-03-15 21:04:58.000000 mosaicml-cli-0.3.3/mcli/serverside/clusters/gpu_type.py
+-rw-r--r--   0 anna       (501) staff       (20)     2824 2023-02-02 22:26:54.000000 mosaicml-cli-0.3.3/mcli/serverside/clusters/instance_type.py
+drwxr-xr-x   0 anna       (501) staff       (20)        0 2023-04-06 21:21:43.476653 mosaicml-cli-0.3.3/mcli/serverside/clusters/overrides/
+-rw-r--r--   0 anna       (501) staff       (20)     1603 2023-03-31 00:39:43.000000 mosaicml-cli-0.3.3/mcli/serverside/clusters/overrides/__init__.py
+-rw-r--r--   0 anna       (501) staff       (20)      548 2023-03-31 00:39:43.000000 mosaicml-cli-0.3.3/mcli/serverside/clusters/overrides/microk8s.py
+-rw-r--r--   0 anna       (501) staff       (20)     2219 2023-03-31 00:39:43.000000 mosaicml-cli-0.3.3/mcli/serverside/clusters/overrides/r10z1.py
+-rw-r--r--   0 anna       (501) staff       (20)     2822 2023-03-31 00:39:43.000000 mosaicml-cli-0.3.3/mcli/serverside/clusters/overrides/r1z1.py
+-rw-r--r--   0 anna       (501) staff       (20)     2495 2023-03-31 00:39:43.000000 mosaicml-cli-0.3.3/mcli/serverside/clusters/overrides/r1z4.py
+-rw-r--r--   0 anna       (501) staff       (20)     2759 2023-03-31 00:39:43.000000 mosaicml-cli-0.3.3/mcli/serverside/clusters/overrides/r3z1.py
+-rw-r--r--   0 anna       (501) staff       (20)     5355 2023-03-31 00:39:43.000000 mosaicml-cli-0.3.3/mcli/serverside/clusters/overrides/r4z1.py
+-rw-r--r--   0 anna       (501) staff       (20)     1049 2023-03-31 00:39:43.000000 mosaicml-cli-0.3.3/mcli/serverside/clusters/overrides/r7z1.py
+-rw-r--r--   0 anna       (501) staff       (20)     1161 2023-03-31 00:39:43.000000 mosaicml-cli-0.3.3/mcli/serverside/clusters/overrides/r7z10.py
+-rw-r--r--   0 anna       (501) staff       (20)     2497 2023-03-31 00:39:43.000000 mosaicml-cli-0.3.3/mcli/serverside/clusters/overrides/r7z2.py
+-rw-r--r--   0 anna       (501) staff       (20)     1062 2023-03-31 00:39:43.000000 mosaicml-cli-0.3.3/mcli/serverside/clusters/overrides/r7z3.py
+-rw-r--r--   0 anna       (501) staff       (20)     1034 2023-03-31 00:39:43.000000 mosaicml-cli-0.3.3/mcli/serverside/clusters/overrides/r7z4.py
+-rw-r--r--   0 anna       (501) staff       (20)     1047 2023-03-31 00:39:43.000000 mosaicml-cli-0.3.3/mcli/serverside/clusters/overrides/r7z5.py
+-rw-r--r--   0 anna       (501) staff       (20)     1047 2023-03-31 00:39:43.000000 mosaicml-cli-0.3.3/mcli/serverside/clusters/overrides/r7z6.py
+-rw-r--r--   0 anna       (501) staff       (20)     1214 2023-03-31 00:39:43.000000 mosaicml-cli-0.3.3/mcli/serverside/clusters/overrides/r7z7.py
+-rw-r--r--   0 anna       (501) staff       (20)     1242 2023-03-31 00:39:43.000000 mosaicml-cli-0.3.3/mcli/serverside/clusters/overrides/r7z9.py
+-rw-r--r--   0 anna       (501) staff       (20)     1034 2023-03-31 00:39:43.000000 mosaicml-cli-0.3.3/mcli/serverside/clusters/overrides/r8z1.py
+-rw-r--r--   0 anna       (501) staff       (20)     1071 2023-03-31 00:39:43.000000 mosaicml-cli-0.3.3/mcli/serverside/clusters/overrides/r8z2.py
+-rw-r--r--   0 anna       (501) staff       (20)     1054 2023-03-31 00:39:43.000000 mosaicml-cli-0.3.3/mcli/serverside/clusters/overrides/r8z3.py
+-rw-r--r--   0 anna       (501) staff       (20)     1061 2023-03-31 00:39:43.000000 mosaicml-cli-0.3.3/mcli/serverside/clusters/overrides/r99z1.py
+-rw-r--r--   0 anna       (501) staff       (20)      310 2022-10-06 23:19:14.000000 mosaicml-cli-0.3.3/mcli/serverside/clusters/volumekind.py
+drwxr-xr-x   0 anna       (501) staff       (20)        0 2023-04-06 21:21:43.481828 mosaicml-cli-0.3.3/mcli/serverside/job/
+-rw-r--r--   0 anna       (501) staff       (20)        0 2022-07-01 20:27:34.000000 mosaicml-cli-0.3.3/mcli/serverside/job/__init__.py
+-rw-r--r--   0 anna       (501) staff       (20)    15555 2023-02-02 22:26:54.000000 mosaicml-cli-0.3.3/mcli/serverside/job/mcli_job.py
+-rw-r--r--   0 anna       (501) staff       (20)      465 2022-07-14 19:44:13.000000 mosaicml-cli-0.3.3/mcli/serverside/job/mcli_k8s_config_map_typing.py
+-rw-r--r--   0 anna       (501) staff       (20)     6471 2023-03-31 04:06:45.000000 mosaicml-cli-0.3.3/mcli/serverside/job/mcli_k8s_job.py
+-rw-r--r--   0 anna       (501) staff       (20)     8090 2022-08-08 20:33:01.000000 mosaicml-cli-0.3.3/mcli/serverside/job/mcli_k8s_job_typing.py
+-rw-r--r--   0 anna       (501) staff       (20)     7524 2022-10-06 23:19:14.000000 mosaicml-cli-0.3.3/mcli/serverside/job/mcli_k8s_resource_requirements_typing.py
+-rw-r--r--   0 anna       (501) staff       (20)      459 2022-07-01 20:27:34.000000 mosaicml-cli-0.3.3/mcli/serverside/job/mcli_k8s_service_typing.py
+drwxr-xr-x   0 anna       (501) staff       (20)        0 2023-04-06 21:21:43.483232 mosaicml-cli-0.3.3/mcli/serverside/runners/
+-rw-r--r--   0 anna       (501) staff       (20)        0 2022-07-01 20:27:34.000000 mosaicml-cli-0.3.3/mcli/serverside/runners/__init__.py
+-rw-r--r--   0 anna       (501) staff       (20)     5770 2022-12-21 22:27:10.000000 mosaicml-cli-0.3.3/mcli/serverside/runners/runner.py
+drwxr-xr-x   0 anna       (501) staff       (20)        0 2023-04-06 21:21:43.499369 mosaicml-cli-0.3.3/mcli/utils/
+-rw-r--r--   0 anna       (501) staff       (20)        0 2022-07-01 20:27:34.000000 mosaicml-cli-0.3.3/mcli/utils/__init__.py
+-rw-r--r--   0 anna       (501) staff       (20)     5306 2023-03-27 21:07:48.000000 mosaicml-cli-0.3.3/mcli/utils/utils_cli.py
+-rw-r--r--   0 anna       (501) staff       (20)     2555 2023-04-05 17:17:35.000000 mosaicml-cli-0.3.3/mcli/utils/utils_config.py
+-rw-r--r--   0 anna       (501) staff       (20)      740 2022-10-06 23:19:14.000000 mosaicml-cli-0.3.3/mcli/utils/utils_date.py
+-rw-r--r--   0 anna       (501) staff       (20)    10453 2023-03-27 21:07:48.000000 mosaicml-cli-0.3.3/mcli/utils/utils_docker.py
+-rw-r--r--   0 anna       (501) staff       (20)    12947 2023-03-27 21:07:48.000000 mosaicml-cli-0.3.3/mcli/utils/utils_epilog.py
+-rw-r--r--   0 anna       (501) staff       (20)      751 2022-07-01 20:27:34.000000 mosaicml-cli-0.3.3/mcli/utils/utils_file.py
+-rw-r--r--   0 anna       (501) staff       (20)    11769 2022-12-21 22:27:10.000000 mosaicml-cli-0.3.3/mcli/utils/utils_interactive.py
+-rw-r--r--   0 anna       (501) staff       (20)    49322 2022-11-16 17:00:39.000000 mosaicml-cli-0.3.3/mcli/utils/utils_kube.py
+-rw-r--r--   0 anna       (501) staff       (20)     6980 2023-02-02 22:26:54.000000 mosaicml-cli-0.3.3/mcli/utils/utils_kube_labels.py
+-rw-r--r--   0 anna       (501) staff       (20)     4741 2023-03-27 21:07:48.000000 mosaicml-cli-0.3.3/mcli/utils/utils_logging.py
+-rw-r--r--   0 anna       (501) staff       (20)      359 2022-07-01 20:27:34.000000 mosaicml-cli-0.3.3/mcli/utils/utils_modules.py
+-rw-r--r--   0 anna       (501) staff       (20)     6614 2023-03-27 21:07:48.000000 mosaicml-cli-0.3.3/mcli/utils/utils_pypi.py
+-rw-r--r--   0 anna       (501) staff       (20)     6513 2023-03-27 21:07:48.000000 mosaicml-cli-0.3.3/mcli/utils/utils_rancher.py
+-rw-r--r--   0 anna       (501) staff       (20)     3115 2022-09-12 17:46:33.000000 mosaicml-cli-0.3.3/mcli/utils/utils_rich.py
+-rw-r--r--   0 anna       (501) staff       (20)     8533 2023-01-06 22:51:41.000000 mosaicml-cli-0.3.3/mcli/utils/utils_run_status.py
+-rw-r--r--   0 anna       (501) staff       (20)     4350 2022-09-12 17:46:33.000000 mosaicml-cli-0.3.3/mcli/utils/utils_serializable_dataclass.py
+-rw-r--r--   0 anna       (501) staff       (20)     1103 2023-03-27 21:07:48.000000 mosaicml-cli-0.3.3/mcli/utils/utils_spinner.py
+-rw-r--r--   0 anna       (501) staff       (20)    11437 2023-03-27 21:07:48.000000 mosaicml-cli-0.3.3/mcli/utils/utils_string_functions.py
+-rw-r--r--   0 anna       (501) staff       (20)     3954 2022-11-15 18:47:24.000000 mosaicml-cli-0.3.3/mcli/utils/utils_types.py
+-rw-r--r--   0 anna       (501) staff       (20)     1001 2022-07-01 20:27:34.000000 mosaicml-cli-0.3.3/mcli/utils/utils_yaml.py
+-rw-r--r--   0 anna       (501) staff       (20)     3884 2023-04-06 21:21:07.000000 mosaicml-cli-0.3.3/mcli/version.py
+drwxr-xr-x   0 anna       (501) staff       (20)        0 2023-04-06 21:21:43.503145 mosaicml-cli-0.3.3/mosaicml_cli.egg-info/
+-rw-r--r--   0 anna       (501) staff       (20)      696 2023-04-06 21:21:43.000000 mosaicml-cli-0.3.3/mosaicml_cli.egg-info/PKG-INFO
+-rw-r--r--   0 anna       (501) staff       (20)     7139 2023-04-06 21:21:43.000000 mosaicml-cli-0.3.3/mosaicml_cli.egg-info/SOURCES.txt
+-rw-r--r--   0 anna       (501) staff       (20)        1 2023-04-06 21:21:43.000000 mosaicml-cli-0.3.3/mosaicml_cli.egg-info/dependency_links.txt
+-rw-r--r--   0 anna       (501) staff       (20)       75 2023-04-06 21:21:43.000000 mosaicml-cli-0.3.3/mosaicml_cli.egg-info/entry_points.txt
+-rw-r--r--   0 anna       (501) staff       (20)     1630 2023-04-06 21:21:43.000000 mosaicml-cli-0.3.3/mosaicml_cli.egg-info/requires.txt
+-rw-r--r--   0 anna       (501) staff       (20)       11 2023-04-06 21:21:43.000000 mosaicml-cli-0.3.3/mosaicml_cli.egg-info/top_level.txt
+-rw-r--r--   0 anna       (501) staff       (20)    30933 2022-12-15 00:57:04.000000 mosaicml-cli-0.3.3/pyproject.toml
+-rw-r--r--   0 anna       (501) staff       (20)       38 2023-04-06 21:21:43.508717 mosaicml-cli-0.3.3/setup.cfg
+-rw-r--r--   0 anna       (501) staff       (20)     3111 2023-03-27 21:07:48.000000 mosaicml-cli-0.3.3/setup.py
+drwxr-xr-x   0 anna       (501) staff       (20)        0 2023-04-06 21:21:43.505313 mosaicml-cli-0.3.3/tests/
+drwxr-xr-x   0 anna       (501) staff       (20)        0 2023-04-06 21:21:43.507257 mosaicml-cli-0.3.3/tests/submit/
+-rw-r--r--   0 anna       (501) staff       (20)        0 2023-03-17 15:59:14.000000 mosaicml-cli-0.3.3/tests/submit/__init__.py
+-rw-r--r--   0 anna       (501) staff       (20)     6393 2023-03-31 04:06:45.000000 mosaicml-cli-0.3.3/tests/submit/test_cluster.py
+-rw-r--r--   0 anna       (501) staff       (20)     9266 2023-03-31 04:06:45.000000 mosaicml-cli-0.3.3/tests/submit/test_cluster_secrets.py
+-rw-r--r--   0 anna       (501) staff       (20)     7973 2023-04-06 21:21:07.000000 mosaicml-cli-0.3.3/tests/test_config.py
+-rw-r--r--   0 anna       (501) staff       (20)       62 2023-03-17 15:59:14.000000 mosaicml-cli-0.3.3/tests/test_simple.py
+-rw-r--r--   0 anna       (501) staff       (20)     6116 2023-03-27 21:07:48.000000 mosaicml-cli-0.3.3/tests/test_upgrade.py
```

### Comparing `mosaicml-cli-0.3.2/PKG-INFO` & `mosaicml-cli-0.3.3/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: mosaicml-cli
-Version: 0.3.2
+Version: 0.3.3
 Summary: Interact with the MosaicML platform from python or a command line interface
 Home-page: https://github.com/mosaicml/mosaicml-cli
 Author: MosaicML
 Author-email: team@mosaicml.com
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
```

### Comparing `mosaicml-cli-0.3.2/README.md` & `mosaicml-cli-0.3.3/README.md`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/api/cluster/api_get_clusters.py` & `mosaicml-cli-0.3.3/mcli/api/cluster/api_get_clusters.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/api/engine/engine.py` & `mosaicml-cli-0.3.3/mcli/api/engine/engine.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/api/engine/utils.py` & `mosaicml-cli-0.3.3/mcli/api/engine/utils.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/api/exceptions.py` & `mosaicml-cli-0.3.3/mcli/api/exceptions.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/api/inference_deployments/__init__.py` & `mosaicml-cli-0.3.3/mcli/api/inference_deployments/__init__.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/api/inference_deployments/api_create_inference_deployment.py` & `mosaicml-cli-0.3.3/mcli/api/inference_deployments/api_create_inference_deployment.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/api/inference_deployments/api_delete_inference_deployments.py` & `mosaicml-cli-0.3.3/mcli/api/inference_deployments/api_delete_inference_deployments.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/api/inference_deployments/api_get_inference_deployments.py` & `mosaicml-cli-0.3.3/mcli/api/inference_deployments/api_get_inference_deployments.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/api/inference_deployments/api_ping_inference_deployment.py` & `mosaicml-cli-0.3.3/mcli/api/inference_deployments/api_ping_inference_deployment.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/api/inference_deployments/api_predict_inference_deployment.py` & `mosaicml-cli-0.3.3/mcli/api/inference_deployments/api_predict_inference_deployment.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/api/kube/runs/__init__.py` & `mosaicml-cli-0.3.3/mcli/api/kube/runs/__init__.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/api/kube/runs/api_create_run.py` & `mosaicml-cli-0.3.3/mcli/api/kube/runs/api_create_run.py`

 * *Files 2% similar despite different names*

```diff
@@ -113,22 +113,21 @@
 
     if isinstance(_priority, PriorityLabel):
         _priority = _priority.value
         assert not isinstance(_priority, PriorityLabel)
 
     mcli_job = MCLIJob.from_final_run_config(run)
     mock_uuid = str(uuid.uuid4())
-    model = Run(
-        run_uid=mock_uuid,
-        name=mcli_job.unique_name,
-        status=RunStatus.PENDING,
-        created_at=dt.datetime.now(),
-        updated_at=dt.datetime.now(),
-        config=run,
-    )
+    model = Run(run_uid=mock_uuid,
+                name=mcli_job.unique_name,
+                status=RunStatus.PENDING,
+                created_at=dt.datetime.now(),
+                updated_at=dt.datetime.now(),
+                config=run,
+                created_by='should-not-be-here@gmail.com')
 
     res = run_kube_in_threadpool(_submit_run, model, mcli_job, _priority, _job_type)
 
     if not future:
         return res.result(timeout=timeout)
     else:
         return res
```

### Comparing `mosaicml-cli-0.3.2/mcli/api/kube/runs/api_delete_runs.py` & `mosaicml-cli-0.3.3/mcli/api/kube/runs/api_delete_runs.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/api/kube/runs/api_get_run_logs.py` & `mosaicml-cli-0.3.3/mcli/api/kube/runs/api_get_run_logs.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/api/kube/runs/api_get_runs.py` & `mosaicml-cli-0.3.3/mcli/api/kube/runs/api_get_runs.py`

 * *Files 3% similar despite different names*

```diff
@@ -182,14 +182,17 @@
         # Add updated time
         run_data['updated_at'] = _get_update_time(pod)
 
         # Get job type
         run_data['_type'] = _get_job_type(pod)
 
         run_data['config'] = config
+
+        # Add createdByEmail - enabled in MCloud
+        run_data['created_by'] = 'user@gmail.com'
         runs.append(Run(**run_data))
 
     return runs
 
 
 def _extract_run_config(pod: Dict[str, Any]) -> FinalRunConfig:
     """Extract the :type FinalRunConfig: as best we can from one of a run's pods
@@ -300,14 +303,15 @@
     after: Optional[Union[str, dt.datetime]] = None,
     gpu_types: Optional[Union[List[str], List[GPUType]]] = None,
     gpu_nums: Optional[List[int]] = None,
     statuses: Optional[Union[List[str], List[RunStatus]]] = None,
     timeout: Optional[float] = 10,
     future: Literal[False] = False,
     clusters: Optional[Union[List[str], List[Cluster]]] = None,
+    user_emails: Optional[List[str]] = None,
 ) -> List[Run]:
     ...
 
 
 @overload
 def get_runs(
     runs: Optional[Union[List[str], List[Run]]] = None,
@@ -316,14 +320,15 @@
     after: Optional[Union[str, dt.datetime]] = None,
     gpu_types: Optional[Union[List[str], List[GPUType]]] = None,
     gpu_nums: Optional[List[int]] = None,
     statuses: Optional[Union[List[str], List[RunStatus]]] = None,
     timeout: Optional[float] = None,
     future: Literal[True] = True,
     clusters: Optional[Union[List[str], List[Cluster]]] = None,
+    user_emails: Optional[List[str]] = None,
 ) -> Future[List[Run]]:
     ...
 
 
 def get_runs(
     runs: Optional[Union[List[str], List[Run]]] = None,
     cluster_names: Optional[Union[List[str], List[Cluster]]] = None,
@@ -331,14 +336,15 @@
     after: Optional[Union[str, dt.datetime]] = None,
     gpu_types: Optional[Union[List[str], List[GPUType]]] = None,
     gpu_nums: Optional[List[int]] = None,
     statuses: Optional[Union[List[str], List[RunStatus]]] = None,
     timeout: Optional[float] = 10,
     future: bool = False,
     clusters: Optional[Union[List[str], List[Cluster]]] = None,
+    user_emails: Optional[List[str]] = None,
 ):
     """Get a filtered list of runs
 
     List runs that have been launched in the MosaicML platform. The returned list will
     contain all of the details stored about the requested runs.
 
     Arguments:
@@ -398,13 +404,16 @@
 
     if gpu_types is not None:
         gpu_types = [gt.name if isinstance(gt, GPUType) else gt for gt in gpu_types]
 
     if statuses is not None:
         statuses = [st.name if isinstance(st, RunStatus) else st for st in statuses]
 
+    if user_emails is not None:
+        raise NotImplementedError("Getting runs of another user is only supported in mapi")
+
     runs_future = _get_runs_kube(run_names, cluster_names, gpu_types, gpu_nums, statuses)
 
     if not future:
         return runs_future.result(timeout=timeout)
     else:
         return runs_future
```

### Comparing `mosaicml-cli-0.3.2/mcli/api/kube/runs/api_stop_runs.py` & `mosaicml-cli-0.3.3/mcli/api/kube/runs/api_stop_runs.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/api/kube/runs/api_watch_run.py` & `mosaicml-cli-0.3.3/mcli/api/kube/runs/api_watch_run.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/api/mint/shell.py` & `mosaicml-cli-0.3.3/mcli/api/mint/shell.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/api/mint/tty.py` & `mosaicml-cli-0.3.3/mcli/api/mint/tty.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/api/model/cluster_details.py` & `mosaicml-cli-0.3.3/mcli/api/model/cluster_details.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/api/model/inference_deployment.py` & `mosaicml-cli-0.3.3/mcli/api/model/inference_deployment.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/api/model/run.py` & `mosaicml-cli-0.3.3/mcli/api/model/run.py`

 * *Files 8% similar despite different names*

```diff
@@ -50,14 +50,15 @@
 
     run_uid: str
     name: str
     status: RunStatus
     created_at: datetime
     updated_at: datetime
     config: FinalRunConfig
+    created_by: str
 
     started_at: Optional[datetime] = None
     completed_at: Optional[datetime] = None
     reason: Optional[str] = None
     submitted_config: Optional[RunConfig] = None
     nodes: List[Node] = field(default_factory=list)
 
@@ -65,14 +66,15 @@
         'id',
         'name',
         'status',
         'createdAt',
         'updatedAt',
         'runInput',
         'originalRunInput',
+        'createdByEmail',
     ])
 
     # This "job type" field is used only by interactive sessions in kube mcli
     # Let's add it as an optional only to be used by api.kube.get_runs
     _type: Optional[MCLIJobType] = None
 
     @classmethod
@@ -95,11 +97,12 @@
         return cls(run_uid=response['id'],
                    name=response['name'],
                    created_at=convert_datetime(response['createdAt']),
                    started_at=started_at,
                    completed_at=completed_at,
                    updated_at=convert_datetime(response['updatedAt']),
                    status=RunStatus.from_string(response['status']),
+                   created_by=response['createdByEmail'],
                    config=FinalRunConfig.from_mapi_response(response['runInput']),
                    submitted_config=RunConfig.from_mapi_response(response['originalRunInput']),
                    nodes=[Node.from_mapi_response(n) for n in response.get('nodes', [])],
                    reason=response['reason'])
```

### Comparing `mosaicml-cli-0.3.2/mcli/api/runs/__init__.py` & `mosaicml-cli-0.3.3/mcli/api/runs/__init__.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/api/runs/api_create_run.py` & `mosaicml-cli-0.3.3/mcli/api/runs/api_create_run.py`

 * *Files 5% similar despite different names*

```diff
@@ -17,14 +17,15 @@
 QUERY = f"""
 mutation CreateRun(${VARIABLE_DATA_NAME}: CreateRunInput!) {{
   {QUERY_FUNCTION}({VARIABLE_DATA_NAME}: ${VARIABLE_DATA_NAME}) {{
     id
     name
     runInput
     originalRunInput
+    createdByEmail
     status
     createdAt
     startedAt
     completedAt
     updatedAt
     reason
   }}
```

### Comparing `mosaicml-cli-0.3.2/mcli/api/runs/api_delete_runs.py` & `mosaicml-cli-0.3.3/mcli/api/runs/api_delete_runs.py`

 * *Files 1% similar despite different names*

```diff
@@ -17,14 +17,15 @@
 QUERY = f"""
 mutation DeleteRuns(${VARIABLE_DATA_NAME}: GetRunsInput!) {{
   {QUERY_FUNCTION}({VARIABLE_DATA_NAME}: ${VARIABLE_DATA_NAME}) {{
     id
     name
     runInput
     originalRunInput
+    createdByEmail
     status
     createdAt
     startedAt
     completedAt
     updatedAt
     reason
   }}
```

### Comparing `mosaicml-cli-0.3.2/mcli/api/runs/api_get_run_logs.py` & `mosaicml-cli-0.3.3/mcli/api/runs/api_get_run_logs.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/api/runs/api_get_runs.py` & `mosaicml-cli-0.3.3/mcli/api/runs/api_get_runs.py`

 * *Files 6% similar despite different names*

```diff
@@ -31,14 +31,15 @@
     completedAt
     updatedAt
     reason
     nodes {{
         rank
         name
     }}
+    createdByEmail
   }}
 }}"""
 
 
 @overload
 def get_runs(
     runs: Optional[Union[List[str], List[Run]]] = None,
@@ -47,14 +48,15 @@
     after: Optional[Union[str, datetime]] = None,
     gpu_types: Optional[Union[List[str], List[GPUType]]] = None,
     gpu_nums: Optional[List[int]] = None,
     statuses: Optional[Union[List[str], List[RunStatus]]] = None,
     timeout: Optional[float] = 10,
     future: Literal[False] = False,
     clusters: Optional[Union[List[str], List[Cluster]]] = None,
+    user_emails: Optional[List[str]] = None,
 ) -> List[Run]:
     ...
 
 
 @overload
 def get_runs(
     runs: Optional[Union[List[str], List[Run]]] = None,
@@ -63,29 +65,31 @@
     after: Optional[Union[str, datetime]] = None,
     gpu_types: Optional[Union[List[str], List[GPUType]]] = None,
     gpu_nums: Optional[List[int]] = None,
     statuses: Optional[Union[List[str], List[RunStatus]]] = None,
     timeout: Optional[float] = None,
     future: Literal[True] = True,
     clusters: Optional[Union[List[str], List[Cluster]]] = None,
+    user_emails: Optional[List[str]] = None,
 ) -> Future[List[Run]]:
     ...
 
 
 def get_runs(
-        runs: Optional[Union[List[str], List[Run]]] = None,
-        cluster_names: Optional[Union[List[str], List[Cluster]]] = None,
-        before: Optional[Union[str, datetime]] = None,
-        after: Optional[Union[str, datetime]] = None,
-        gpu_types: Optional[Union[List[str], List[GPUType]]] = None,
-        gpu_nums: Optional[List[int]] = None,
-        statuses: Optional[Union[List[str], List[RunStatus]]] = None,
-        timeout: Optional[float] = 10,
-        future: bool = False,
-        clusters: Optional[Union[List[str], List[Cluster]]] = None,  # TODO: deprecate
+    runs: Optional[Union[List[str], List[Run]]] = None,
+    cluster_names: Optional[Union[List[str], List[Cluster]]] = None,
+    before: Optional[Union[str, datetime]] = None,
+    after: Optional[Union[str, datetime]] = None,
+    gpu_types: Optional[Union[List[str], List[GPUType]]] = None,
+    gpu_nums: Optional[List[int]] = None,
+    statuses: Optional[Union[List[str], List[RunStatus]]] = None,
+    timeout: Optional[float] = 10,
+    future: bool = False,
+    clusters: Optional[Union[List[str], List[Cluster]]] = None,  # TODO: deprecate
+    user_emails: Optional[List[str]] = None,
 ):
     """List runs that have been launched in the MosaicML platform
 
     The returned list will contain all of the details stored about the requested runs.
 
     Arguments:
         runs: List of runs on which to get information
@@ -143,14 +147,19 @@
             'includeDeleted': False,
         },
     }
 
     cfg = MCLIConfig.load_config(safe=True)
     if cfg.user_id:
         variables[VARIABLE_DATA_NAME]['entity'] = {'userIds': [cfg.user_id]}
+    if user_emails:
+        if variables[VARIABLE_DATA_NAME].get('entity'):
+            variables[VARIABLE_DATA_NAME]['entity']['emails'] = user_emails
+        else:
+            variables[VARIABLE_DATA_NAME]['entity'] = {'emails': user_emails}
 
     response = run_plural_mapi_request(
         query=QUERY,
         query_function=QUERY_FUNCTION,
         return_model_type=Run,
         variables=variables,
     )
```

### Comparing `mosaicml-cli-0.3.2/mcli/api/runs/api_stop_runs.py` & `mosaicml-cli-0.3.3/mcli/api/runs/api_stop_runs.py`

 * *Files 2% similar despite different names*

```diff
@@ -17,14 +17,15 @@
 QUERY = f"""
 mutation StopRuns(${VARIABLE_DATA_NAME}: GetRunsInput!) {{
   {QUERY_FUNCTION}({VARIABLE_DATA_NAME}: ${VARIABLE_DATA_NAME}) {{
     id
     name
     runInput
     originalRunInput
+    createdByEmail
     status
     createdAt
     startedAt
     completedAt
     updatedAt
     reason
   }}
```

### Comparing `mosaicml-cli-0.3.2/mcli/api/runs/api_watch_run.py` & `mosaicml-cli-0.3.3/mcli/api/runs/api_watch_run.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/api/schema/generic_model.py` & `mosaicml-cli-0.3.3/mcli/api/schema/generic_model.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/api/secrets/api_create_secret.py` & `mosaicml-cli-0.3.3/mcli/api/secrets/api_create_secret.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/api/secrets/api_delete_secrets.py` & `mosaicml-cli-0.3.3/mcli/api/secrets/api_delete_secrets.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/api/secrets/api_get_secrets.py` & `mosaicml-cli-0.3.3/mcli/api/secrets/api_get_secrets.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/api/typing_future.py` & `mosaicml-cli-0.3.3/mcli/api/typing_future.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/api/users/api_get_users.py` & `mosaicml-cli-0.3.3/mcli/api/users/api_get_users.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/cli/cli.py` & `mosaicml-cli-0.3.3/mcli/cli/cli.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/cli/common/deployment_filters.py` & `mosaicml-cli-0.3.3/mcli/cli/common/deployment_filters.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/cli/common/run_filters.py` & `mosaicml-cli-0.3.3/mcli/cli/common/run_filters.py`

 * *Files 2% similar despite different names*

```diff
@@ -143,25 +143,27 @@
     before_filter: Optional[str] = None,
     after_filter: Optional[str] = None,
     gpu_type_filter: Optional[List[str]] = None,
     gpu_num_filter: Optional[List[int]] = None,
     status_filter: Optional[List[RunStatus]] = None,
     latest: bool = False,
     action_all: Optional[bool] = None,
+    user_filter: Optional[List[str]] = None,
 ) -> List[Run]:
 
     filter_used = any([
         name_filter,
         before_filter,
         after_filter,
         cluster_filter,
         gpu_type_filter,
         gpu_num_filter,
         status_filter,
         latest,
+        user_filter,
     ])
     if not filter_used:
         if action_all is False:
             raise MCLIException('Must specify at least one filter or --all')
 
     if not name_filter:
         # Accept all that pass other filters
@@ -174,14 +176,15 @@
     if not conf.feature_enabled(FeatureFlag.USE_MCLOUD) and not conf.clusters:
         raise MCLIException('No clusters found. You must have at least 1 cluster added before working with runs.')
 
     with console_status('Retrieving requested runs...'):
         runs = get_runs(
             runs=(run_names or None) if not glob_filters else None,
             cluster_names=cluster_filter,
+            user_emails=user_filter,
             before=before_filter,
             after=after_filter,
             gpu_types=gpu_type_filter,
             gpu_nums=gpu_num_filter,
             statuses=status_filter,
             timeout=None,
         )
```

### Comparing `mosaicml-cli-0.3.2/mcli/cli/m_clean/m_clean.py` & `mosaicml-cli-0.3.3/mcli/cli/m_clean/m_clean.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/cli/m_connect/m_connect.py` & `mosaicml-cli-0.3.3/mcli/cli/m_connect/m_connect.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/cli/m_create/cluster.py` & `mosaicml-cli-0.3.3/mcli/cli/m_create/cluster.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/cli/m_create/env_var.py` & `mosaicml-cli-0.3.3/mcli/cli/m_create/env_var.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/cli/m_create/m_create.py` & `mosaicml-cli-0.3.3/mcli/cli/m_create/m_create.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/cli/m_create/secret.py` & `mosaicml-cli-0.3.3/mcli/cli/m_create/secret.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/cli/m_delete/delete.py` & `mosaicml-cli-0.3.3/mcli/cli/m_delete/delete.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/cli/m_delete/m_delete.py` & `mosaicml-cli-0.3.3/mcli/cli/m_delete/m_delete.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/cli/m_deploy/m_deploy.py` & `mosaicml-cli-0.3.3/mcli/cli/m_deploy/m_deploy.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/cli/m_describe/describe_inference_deployments.py` & `mosaicml-cli-0.3.3/mcli/cli/m_describe/describe_inference_deployments.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/cli/m_describe/describe_runs.py` & `mosaicml-cli-0.3.3/mcli/cli/m_describe/describe_runs.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/cli/m_describe/m_describe.py` & `mosaicml-cli-0.3.3/mcli/cli/m_describe/m_describe.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/cli/m_get/__init__.py` & `mosaicml-cli-0.3.3/mcli/cli/m_get/__init__.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/cli/m_get/clusters.py` & `mosaicml-cli-0.3.3/mcli/cli/m_get/clusters.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/cli/m_get/display.py` & `mosaicml-cli-0.3.3/mcli/cli/m_get/display.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/cli/m_get/envvars.py` & `mosaicml-cli-0.3.3/mcli/cli/m_get/envvars.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/cli/m_get/inference_deployments.py` & `mosaicml-cli-0.3.3/mcli/cli/m_get/inference_deployments.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/cli/m_get/m_get.py` & `mosaicml-cli-0.3.3/mcli/cli/m_get/m_get.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/cli/m_get/runs.py` & `mosaicml-cli-0.3.3/mcli/cli/m_get/runs.py`

 * *Files 20% similar despite different names*

```diff
@@ -8,41 +8,44 @@
 from typing import Dict, Generator, List, Optional
 
 from mcli import config
 from mcli.api.exceptions import cli_error_handler
 from mcli.cli.common.run_filters import configure_submission_filter_argparser, get_runs_with_filters
 from mcli.cli.m_get.display import MCLIDisplayItem, MCLIGetDisplay, OutputDisplay, format_timestamp
 from mcli.sdk import Run
+from mcli.utils.utils_cli import comma_separated
 from mcli.utils.utils_run_status import RunStatus
 
 logger = logging.getLogger(__name__)
 
 
 class RunColumns(Enum):
     ID = 'id'
     NAME = 'name'
     CLUSTER = 'cluster'
     GPU_TYPE = 'gpu_type'
     GPU_NUM = 'gpu_num'
     CREATED_TIME = 'created_time'
     START_TIME = 'start_time'
     END_TIME = 'end_time'
+    USER = 'user'
     STATUS = 'status'
 
 
 @dataclass
 class RunDisplayItem(MCLIDisplayItem):
     """Tuple that extracts run data for display purposes.
     """
     name: str
     gpu_num: str
     created_time: str
     start_time: str
     end_time: str
     status: str
+    user: str
     cluster: Optional[str] = None
     gpu_type: Optional[str] = None
     id: Optional[str] = None
 
     @classmethod
     def from_run(cls, run: Run, include_ids: bool = False) -> RunDisplayItem:
         display_status = run.status.display_name
@@ -52,22 +55,24 @@
             RunColumns.NAME.value: run.name,
             RunColumns.CLUSTER.value: run.config.cluster,
             RunColumns.GPU_TYPE.value: run.config.gpu_type,
             RunColumns.GPU_NUM.value: str(run.config.gpu_num),
             RunColumns.CREATED_TIME.value: format_timestamp(run.created_at),
             RunColumns.START_TIME.value: format_timestamp(run.started_at),
             RunColumns.END_TIME.value: format_timestamp(run.completed_at),
+            RunColumns.USER.value: run.created_by,
             RunColumns.STATUS.value: display_status
         }
         if include_ids:
             extracted[RunColumns.ID.value] = run.run_uid
 
         return RunDisplayItem(**extracted)
 
 
+# TODO: add column for USER
 class MCLIRunDisplay(MCLIGetDisplay):
     """Display manager for runs
     """
 
     def __init__(self, models: List[Run], include_ids: bool = False):
         self.models = sorted(models, key=lambda x: x.created_at, reverse=True)
         self.include_ids = include_ids
@@ -97,29 +102,31 @@
     after_filter: Optional[str] = None,
     gpu_type_filter: Optional[List[str]] = None,
     gpu_num_filter: Optional[List[int]] = None,
     status_filter: Optional[List[RunStatus]] = None,
     output: OutputDisplay = OutputDisplay.TABLE,
     include_ids: bool = False,
     latest: bool = False,
+    user_filter: Optional[List[str]] = None,
     **kwargs,
 ) -> int:
     """Get a table of ongoing and completed runs
     """
     del kwargs
 
     runs = get_runs_with_filters(
-        name_filter,
-        cluster_filter,
-        before_filter,
-        after_filter,
-        gpu_type_filter,
-        gpu_num_filter,
-        status_filter,
-        latest,
+        name_filter=name_filter,
+        cluster_filter=cluster_filter,
+        before_filter=before_filter,
+        after_filter=after_filter,
+        gpu_type_filter=gpu_type_filter,
+        gpu_num_filter=gpu_num_filter,
+        status_filter=status_filter,
+        latest=latest,
+        user_filter=user_filter,
     )
 
     display = MCLIRunDisplay(runs, include_ids=include_ids)
     display.print(output)
 
     return 0
 
@@ -127,17 +134,22 @@
 def get_runs_argparser(subparsers: argparse._SubParsersAction):
     """Configures the ``mcli get runs`` argparser
     """
 
     run_examples: str = """Examples:
     $ mcli get runs
 
-    NAME                         CLUSTER   GPU_TYPE      GPU_NUM      CREATED_TIME     STATUS
-    run-foo                      c-1        g0-type       8            05/06/22 1:58pm  Completed
-    run-bar                      c-2        g0-type       1            05/06/22 1:57pm  Completed
+    NAME                         CLUSTER    GPU_TYPE      GPU_NUM      CREATED_TIME     USER               STATUS
+    run-foo                      c-1        g0-type       8            05/06/22 1:58pm  abc@gmail.com      Completed
+    run-bar                      c-2        g0-type       1            05/06/22 1:57pm  abc@gmail.com      Completed
+
+    $ mcli get runs --user xyz@gmail.com
+    NAME                         CLUSTER    GPU_TYPE      GPU_NUM      CREATED_TIME     USER               STATUS
+    run-xyz-1                    c-1        g0-type       8            05/06/22 1:58pm  xyz@gmail.com      Completed
+    run-xyz-2                    c-2        g0-type       1            05/06/22 1:57pm  xyz@gmail.com      Completed
     """
     runs_parser = subparsers.add_parser('runs',
                                         aliases=['run'],
                                         help='Get information on all of your existing runs across all clusters.',
                                         epilog=run_examples,
                                         formatter_class=argparse.RawDescriptionHelpFormatter)
 
@@ -145,8 +157,23 @@
     runs_parser.set_defaults(func=cli_get_runs)
 
     runs_parser.add_argument('--ids',
                              action='store_true',
                              dest='include_ids',
                              default=config.ADMIN_MODE,
                              help='Include the run ids in the output')
+
+    def user(value: str):
+        return comma_separated(value)
+
+    runs_parser.add_argument(
+        '-u',
+        '--user',
+        dest='user_filter',
+        default=None,
+        metavar='User',
+        type=user,
+        help='Fetch the runs created by a user in your organization with their email address. '
+        'Multiple users should be specified using a comma-separated list, '
+        'e.g. "alice@gmail.com,bob@gmail.com"',
+    )
     return runs_parser
```

### Comparing `mosaicml-cli-0.3.2/mcli/cli/m_get/secrets.py` & `mosaicml-cli-0.3.3/mcli/cli/m_get/secrets.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/cli/m_get/users.py` & `mosaicml-cli-0.3.3/mcli/cli/m_get/users.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/cli/m_init/m_init.py` & `mosaicml-cli-0.3.3/mcli/cli/m_init/m_init.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/cli/m_init/m_init_kube.py` & `mosaicml-cli-0.3.3/mcli/cli/m_init/m_init_kube.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/cli/m_interactive/interactive.py` & `mosaicml-cli-0.3.3/mcli/cli/m_interactive/interactive.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/cli/m_interactive/m_interactive.py` & `mosaicml-cli-0.3.3/mcli/cli/m_interactive/m_interactive.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/cli/m_interactive/temp_mcloud_interactive.py` & `mosaicml-cli-0.3.3/mcli/cli/m_interactive/temp_mcloud_interactive.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/cli/m_log/m_log.py` & `mosaicml-cli-0.3.3/mcli/cli/m_log/m_log.py`

 * *Files 0% similar despite different names*

```diff
@@ -48,15 +48,15 @@
         run: Optional[Run] = None
         with err_console.status('Getting run details...') as spinner:
             if run_name is None:
                 spinner.update('No run name provided. Finding latest run...')
                 run = get_latest_run()
                 logger.info(f'{INFO} No run name provided. Displaying log of latest run: [cyan]{run.name}[/]')
             else:
-                runs = get_runs([run_name])
+                runs = get_runs(runs=[run_name])
                 if not runs:
                     raise KubernetesException(status=HTTPStatus.NOT_FOUND,
                                               message=f'Could not find run: [red]{run_name}[/]')
                 run = runs[0]
 
         if follow and run.status.before(RunStatus.RUNNING):
             timeout = 300
```

### Comparing `mosaicml-cli-0.3.2/mcli/cli/m_ping/m_ping.py` & `mosaicml-cli-0.3.3/mcli/cli/m_ping/m_ping.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/cli/m_predict/m_predict.py` & `mosaicml-cli-0.3.3/mcli/cli/m_predict/m_predict.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/cli/m_root/m_config.py` & `mosaicml-cli-0.3.3/mcli/cli/m_root/m_config.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/cli/m_run/m_run.py` & `mosaicml-cli-0.3.3/mcli/cli/m_run/m_run.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/cli/m_set_unset/api_key.py` & `mosaicml-cli-0.3.3/mcli/cli/m_set_unset/api_key.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/cli/m_set_unset/m_set.py` & `mosaicml-cli-0.3.3/mcli/cli/m_set_unset/m_set.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/cli/m_set_unset/m_unset.py` & `mosaicml-cli-0.3.3/mcli/cli/m_set_unset/m_unset.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/cli/m_set_unset/user.py` & `mosaicml-cli-0.3.3/mcli/cli/m_set_unset/user.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/cli/m_stop/m_stop.py` & `mosaicml-cli-0.3.3/mcli/cli/m_stop/m_stop.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/cli/m_use/m_use.py` & `mosaicml-cli-0.3.3/mcli/cli/m_use/m_use.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/cli/m_util/kube_util.py` & `mosaicml-cli-0.3.3/mcli/cli/m_util/kube_util.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/cli/m_util/m_util.py` & `mosaicml-cli-0.3.3/mcli/cli/m_util/m_util.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/cli/m_util/util.py` & `mosaicml-cli-0.3.3/mcli/cli/m_util/util.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/config.py` & `mosaicml-cli-0.3.3/mcli/config.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/models/__init__.py` & `mosaicml-cli-0.3.3/mcli/models/__init__.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/models/inference_deployment_config.py` & `mosaicml-cli-0.3.3/mcli/models/inference_deployment_config.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/models/mcli_cluster.py` & `mosaicml-cli-0.3.3/mcli/models/mcli_cluster.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/models/mcli_envvar.py` & `mosaicml-cli-0.3.3/mcli/models/mcli_envvar.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/models/mcli_integration.py` & `mosaicml-cli-0.3.3/mcli/models/mcli_integration.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/models/mcli_secret.py` & `mosaicml-cli-0.3.3/mcli/models/mcli_secret.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/models/run_config.py` & `mosaicml-cli-0.3.3/mcli/models/run_config.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/objects/integrations/__init__.py` & `mosaicml-cli-0.3.3/mcli/objects/integrations/__init__.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/objects/integrations/apt_packages.py` & `mosaicml-cli-0.3.3/mcli/objects/integrations/apt_packages.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/objects/integrations/comet.py` & `mosaicml-cli-0.3.3/mcli/objects/integrations/comet.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/objects/integrations/git_repo.py` & `mosaicml-cli-0.3.3/mcli/objects/integrations/git_repo.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/objects/integrations/local.py` & `mosaicml-cli-0.3.3/mcli/objects/integrations/local.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/objects/integrations/mosaicml_agent.py` & `mosaicml-cli-0.3.3/mcli/objects/integrations/mosaicml_agent.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/objects/integrations/pip_packages.py` & `mosaicml-cli-0.3.3/mcli/objects/integrations/pip_packages.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/objects/integrations/wandb.py` & `mosaicml-cli-0.3.3/mcli/objects/integrations/wandb.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/objects/secrets/__init__.py` & `mosaicml-cli-0.3.3/mcli/objects/secrets/__init__.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/objects/secrets/cluster_secret.py` & `mosaicml-cli-0.3.3/mcli/objects/secrets/cluster_secret.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/objects/secrets/create/base.py` & `mosaicml-cli-0.3.3/mcli/objects/secrets/create/base.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/objects/secrets/create/docker_registry.py` & `mosaicml-cli-0.3.3/mcli/objects/secrets/create/docker_registry.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/objects/secrets/create/gcp.py` & `mosaicml-cli-0.3.3/mcli/objects/secrets/create/gcp.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/objects/secrets/create/generic.py` & `mosaicml-cli-0.3.3/mcli/objects/secrets/create/generic.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/objects/secrets/create/oci.py` & `mosaicml-cli-0.3.3/mcli/objects/secrets/create/oci.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/objects/secrets/create/s3.py` & `mosaicml-cli-0.3.3/mcli/objects/secrets/create/s3.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/objects/secrets/create/ssh.py` & `mosaicml-cli-0.3.3/mcli/objects/secrets/create/ssh.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/objects/secrets/docker_registry.py` & `mosaicml-cli-0.3.3/mcli/objects/secrets/docker_registry.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/objects/secrets/env_var.py` & `mosaicml-cli-0.3.3/mcli/objects/secrets/env_var.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/objects/secrets/gcp.py` & `mosaicml-cli-0.3.3/mcli/objects/secrets/gcp.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/objects/secrets/mounted.py` & `mosaicml-cli-0.3.3/mcli/objects/secrets/mounted.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/objects/secrets/oci.py` & `mosaicml-cli-0.3.3/mcli/objects/secrets/oci.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/objects/secrets/s3.py` & `mosaicml-cli-0.3.3/mcli/objects/secrets/s3.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/objects/secrets/ssh.py` & `mosaicml-cli-0.3.3/mcli/objects/secrets/ssh.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/sdk/__init__.py` & `mosaicml-cli-0.3.3/mcli/sdk/__init__.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/serverside/clusters/cluster.py` & `mosaicml-cli-0.3.3/mcli/serverside/clusters/cluster.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/serverside/clusters/cluster_instances.py` & `mosaicml-cli-0.3.3/mcli/serverside/clusters/cluster_instances.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/serverside/clusters/cluster_pv_setup.py` & `mosaicml-cli-0.3.3/mcli/serverside/clusters/cluster_pv_setup.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/serverside/clusters/gpu_type.py` & `mosaicml-cli-0.3.3/mcli/serverside/clusters/gpu_type.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/serverside/clusters/instance_type.py` & `mosaicml-cli-0.3.3/mcli/serverside/clusters/instance_type.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/serverside/clusters/overrides/__init__.py` & `mosaicml-cli-0.3.3/mcli/serverside/clusters/overrides/__init__.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/serverside/clusters/overrides/microk8s.py` & `mosaicml-cli-0.3.3/mcli/serverside/clusters/overrides/microk8s.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/serverside/clusters/overrides/r10z1.py` & `mosaicml-cli-0.3.3/mcli/serverside/clusters/overrides/r10z1.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/serverside/clusters/overrides/r1z1.py` & `mosaicml-cli-0.3.3/mcli/serverside/clusters/overrides/r1z1.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/serverside/clusters/overrides/r1z4.py` & `mosaicml-cli-0.3.3/mcli/serverside/clusters/overrides/r1z4.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/serverside/clusters/overrides/r3z1.py` & `mosaicml-cli-0.3.3/mcli/serverside/clusters/overrides/r3z1.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/serverside/clusters/overrides/r4z1.py` & `mosaicml-cli-0.3.3/mcli/serverside/clusters/overrides/r4z1.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/serverside/clusters/overrides/r7z1.py` & `mosaicml-cli-0.3.3/mcli/serverside/clusters/overrides/r7z1.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/serverside/clusters/overrides/r7z10.py` & `mosaicml-cli-0.3.3/mcli/serverside/clusters/overrides/r7z10.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/serverside/clusters/overrides/r7z2.py` & `mosaicml-cli-0.3.3/mcli/serverside/clusters/overrides/r7z2.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/serverside/clusters/overrides/r7z3.py` & `mosaicml-cli-0.3.3/mcli/serverside/clusters/overrides/r7z3.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/serverside/clusters/overrides/r7z4.py` & `mosaicml-cli-0.3.3/mcli/serverside/clusters/overrides/r7z4.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/serverside/clusters/overrides/r7z5.py` & `mosaicml-cli-0.3.3/mcli/serverside/clusters/overrides/r7z5.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/serverside/clusters/overrides/r7z6.py` & `mosaicml-cli-0.3.3/mcli/serverside/clusters/overrides/r7z6.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/serverside/clusters/overrides/r7z7.py` & `mosaicml-cli-0.3.3/mcli/serverside/clusters/overrides/r7z7.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/serverside/clusters/overrides/r7z9.py` & `mosaicml-cli-0.3.3/mcli/serverside/clusters/overrides/r7z9.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/serverside/clusters/overrides/r8z1.py` & `mosaicml-cli-0.3.3/mcli/serverside/clusters/overrides/r8z1.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/serverside/clusters/overrides/r8z2.py` & `mosaicml-cli-0.3.3/mcli/serverside/clusters/overrides/r8z2.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/serverside/clusters/overrides/r8z3.py` & `mosaicml-cli-0.3.3/mcli/serverside/clusters/overrides/r8z3.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/serverside/clusters/overrides/r99z1.py` & `mosaicml-cli-0.3.3/mcli/serverside/clusters/overrides/r99z1.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/serverside/job/mcli_job.py` & `mosaicml-cli-0.3.3/mcli/serverside/job/mcli_job.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/serverside/job/mcli_k8s_job.py` & `mosaicml-cli-0.3.3/mcli/serverside/job/mcli_k8s_job.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/serverside/job/mcli_k8s_job_typing.py` & `mosaicml-cli-0.3.3/mcli/serverside/job/mcli_k8s_job_typing.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/serverside/job/mcli_k8s_resource_requirements_typing.py` & `mosaicml-cli-0.3.3/mcli/serverside/job/mcli_k8s_resource_requirements_typing.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/serverside/runners/runner.py` & `mosaicml-cli-0.3.3/mcli/serverside/runners/runner.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/utils/utils_cli.py` & `mosaicml-cli-0.3.3/mcli/utils/utils_cli.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/utils/utils_config.py` & `mosaicml-cli-0.3.3/mcli/utils/utils_config.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/utils/utils_date.py` & `mosaicml-cli-0.3.3/mcli/utils/utils_date.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/utils/utils_docker.py` & `mosaicml-cli-0.3.3/mcli/utils/utils_docker.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/utils/utils_epilog.py` & `mosaicml-cli-0.3.3/mcli/utils/utils_epilog.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/utils/utils_file.py` & `mosaicml-cli-0.3.3/mcli/utils/utils_file.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/utils/utils_interactive.py` & `mosaicml-cli-0.3.3/mcli/utils/utils_interactive.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/utils/utils_kube.py` & `mosaicml-cli-0.3.3/mcli/utils/utils_kube.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/utils/utils_kube_labels.py` & `mosaicml-cli-0.3.3/mcli/utils/utils_kube_labels.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/utils/utils_logging.py` & `mosaicml-cli-0.3.3/mcli/utils/utils_logging.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/utils/utils_pypi.py` & `mosaicml-cli-0.3.3/mcli/utils/utils_pypi.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/utils/utils_rancher.py` & `mosaicml-cli-0.3.3/mcli/utils/utils_rancher.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/utils/utils_rich.py` & `mosaicml-cli-0.3.3/mcli/utils/utils_rich.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/utils/utils_run_status.py` & `mosaicml-cli-0.3.3/mcli/utils/utils_run_status.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/utils/utils_serializable_dataclass.py` & `mosaicml-cli-0.3.3/mcli/utils/utils_serializable_dataclass.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/utils/utils_spinner.py` & `mosaicml-cli-0.3.3/mcli/utils/utils_spinner.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/utils/utils_string_functions.py` & `mosaicml-cli-0.3.3/mcli/utils/utils_string_functions.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/utils/utils_types.py` & `mosaicml-cli-0.3.3/mcli/utils/utils_types.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/utils/utils_yaml.py` & `mosaicml-cli-0.3.3/mcli/utils/utils_yaml.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mcli/version.py` & `mosaicml-cli-0.3.3/mcli/version.py`

 * *Files 2% similar despite different names*

```diff
@@ -111,13 +111,13 @@
 
 def print_version(**kwargs) -> None:
     """ Prints version """
     del kwargs
     print(get_formatted_version())
 
 
-__version__ = "0.3.2"
+__version__ = "0.3.3"
 v = Version.from_string(__version__)
 __version_major__ = v.major
 __version_minor__ = v.minor
 __version_patch__ = v.patch
 __version_extras__ = v.extras
```

### Comparing `mosaicml-cli-0.3.2/mosaicml_cli.egg-info/PKG-INFO` & `mosaicml-cli-0.3.3/mosaicml_cli.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: mosaicml-cli
-Version: 0.3.2
+Version: 0.3.3
 Summary: Interact with the MosaicML platform from python or a command line interface
 Home-page: https://github.com/mosaicml/mosaicml-cli
 Author: MosaicML
 Author-email: team@mosaicml.com
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
```

### Comparing `mosaicml-cli-0.3.2/mosaicml_cli.egg-info/SOURCES.txt` & `mosaicml-cli-0.3.3/mosaicml_cli.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/mosaicml_cli.egg-info/requires.txt` & `mosaicml-cli-0.3.3/mosaicml_cli.egg-info/requires.txt`

 * *Ordering differences only*

 * *Files 4% similar despite different names*

```diff
@@ -16,43 +16,43 @@
 jinja2
 arrow>=1.2.2
 slack-sdk>=3.17.1
 docker>=5.0.3
 gql[websockets]>=3.4.0
 
 [all]
-sphinx-markdown-tables>=0.0.15
-sphinxcontrib-devhelp>=1.0.2
-yapf>=0.32.0
+pytest-mock>=3.7.0
 sphinx-copybutton>=0.5.0
+pylint>=2.12.2
+pre-commit>=2.17.0
+myst-parser>=0.16.1
 sphinxcontrib-htmlhelp>=2.0.0
-sphinxcontrib-serializinghtml>=1.1.5
-pytest-cov>=4.0.0
-sphinx>=4.4.0
-sphinx_external_toc>=0.3.0
-sphinxcontrib-applehelp>=1.0.2
+sphinxcontrib-katex>=0.8.6
 pyright>=1.1.256
+sphinx_external_toc>=0.3.0
+sphinx-design
+pytest>=6.2.5
 sphinx-argparse>=0.3.1
-sphinxcontrib-katex>=0.8.6
+pytest-cov>=4.0.0
 sphinx-rtd-theme>=1.0.0
-myst-parser>=0.16.1
-furo>=2022.3.4
-sphinxcontrib-jsmath>=1.0.1
+isort>=5.9.3
 sphinxemoji>=0.2.0
-radon>=5.1.0
-sphinxcontrib-images>=0.9.4
-sphinx-design
+sphinxcontrib-applehelp>=1.0.2
+sphinxcontrib-serializinghtml>=1.1.5
 sphinx-panels>=0.6.0
-pytest>=6.2.5
-sphinxcontrib-qthelp>=1.0.3
-pylint>=2.12.2
+yapf>=0.32.0
+sphinx-markdown-tables>=0.0.15
 sphinxext-opengraph>=0.6.1
-pre-commit>=2.17.0
-isort>=5.9.3
-pytest-mock>=3.7.0
+sphinxcontrib-images>=0.9.4
+sphinxcontrib-jsmath>=1.0.1
+sphinxcontrib-qthelp>=1.0.3
+radon>=5.1.0
+sphinxcontrib-devhelp>=1.0.2
+furo>=2022.3.4
+sphinx>=4.4.0
 
 [dev]
 isort>=5.9.3
 pre-commit>=2.17.0
 pylint>=2.12.2
 pyright>=1.1.256
 pytest>=6.2.5
```

### Comparing `mosaicml-cli-0.3.2/pyproject.toml` & `mosaicml-cli-0.3.3/pyproject.toml`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/setup.py` & `mosaicml-cli-0.3.3/setup.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/tests/submit/test_cluster.py` & `mosaicml-cli-0.3.3/tests/submit/test_cluster.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/tests/submit/test_cluster_secrets.py` & `mosaicml-cli-0.3.3/tests/submit/test_cluster_secrets.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/tests/test_config.py` & `mosaicml-cli-0.3.3/tests/test_config.py`

 * *Files identical despite different names*

### Comparing `mosaicml-cli-0.3.2/tests/test_upgrade.py` & `mosaicml-cli-0.3.3/tests/test_upgrade.py`

 * *Files identical despite different names*

