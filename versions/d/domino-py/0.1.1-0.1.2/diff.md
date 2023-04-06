# Comparing `tmp/domino-py-0.1.1.tar.gz` & `tmp/domino-py-0.1.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "domino-py-0.1.1.tar", last modified: Thu Apr  6 13:01:27 2023, max compression
+gzip compressed data, was "domino-py-0.1.2.tar", last modified: Thu Apr  6 13:16:22 2023, max compression
```

## Comparing `domino-py-0.1.1.tar` & `domino-py-0.1.2.tar`

### file list

```diff
@@ -1,90 +1,104 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:01:27.836632 domino-py-0.1.1/
--rw-r--r--   0 runner    (1001) docker     (123)     1075 2023-04-06 13:01:18.000000 domino-py-0.1.1/LICENSE.md
--rw-r--r--   0 runner    (1001) docker     (123)      408 2023-04-06 13:01:18.000000 domino-py-0.1.1/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     3557 2023-04-06 13:01:27.836632 domino-py-0.1.1/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     2657 2023-04-06 13:01:18.000000 domino-py-0.1.1/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:01:27.832632 domino-py-0.1.1/domino/
--rw-r--r--   0 runner    (1001) docker     (123)       32 2023-04-06 13:01:18.000000 domino-py-0.1.1/domino/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    13861 2023-04-06 13:01:18.000000 domino-py-0.1.1/domino/base_piece.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:01:27.832632 domino-py-0.1.1/domino/cli/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 13:01:18.000000 domino-py-0.1.1/domino/cli/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    10056 2023-04-06 13:01:18.000000 domino-py-0.1.1/domino/cli/cli.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:01:27.832632 domino-py-0.1.1/domino/cli/utils/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 13:01:18.000000 domino-py-0.1.1/domino/cli/utils/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      647 2023-04-06 13:01:18.000000 domino-py-0.1.1/domino/cli/utils/config-domino-local.toml
--rw-r--r--   0 runner    (1001) docker     (123)      248 2023-04-06 13:01:18.000000 domino-py-0.1.1/domino/cli/utils/constants.py
--rw-r--r--   0 runner    (1001) docker     (123)      599 2023-04-06 13:01:18.000000 domino-py-0.1.1/domino/cli/utils/create_cluster.sh
--rw-r--r--   0 runner    (1001) docker     (123)    18301 2023-04-06 13:01:18.000000 domino-py-0.1.1/domino/cli/utils/pieces_repository.py
--rw-r--r--   0 runner    (1001) docker     (123)    22663 2023-04-06 13:01:18.000000 domino-py-0.1.1/domino/cli/utils/platform.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:01:27.832632 domino-py-0.1.1/domino/client/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 13:01:18.000000 domino-py-0.1.1/domino/client/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2581 2023-04-06 13:01:18.000000 domino-py-0.1.1/domino/client/airflow_client.py
--rw-r--r--   0 runner    (1001) docker     (123)     1862 2023-04-06 13:01:18.000000 domino-py-0.1.1/domino/client/domino_backend_client.py
--rw-r--r--   0 runner    (1001) docker     (123)     2176 2023-04-06 13:01:18.000000 domino-py-0.1.1/domino/client/fs_client.py
--rw-r--r--   0 runner    (1001) docker     (123)     2970 2023-04-06 13:01:18.000000 domino-py-0.1.1/domino/client/github_rest_client.py
--rw-r--r--   0 runner    (1001) docker     (123)      844 2023-04-06 13:01:18.000000 domino-py-0.1.1/domino/client/local_files_client.py
--rw-r--r--   0 runner    (1001) docker     (123)     2739 2023-04-06 13:01:18.000000 domino-py-0.1.1/domino/client/s3_client.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:01:27.832632 domino-py-0.1.1/domino/custom_operators/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 13:01:18.000000 domino-py-0.1.1/domino/custom_operators/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2298 2023-04-06 13:01:18.000000 domino-py-0.1.1/domino/custom_operators/bash_operator.py
--rw-r--r--   0 runner    (1001) docker     (123)    16991 2023-04-06 13:01:18.000000 domino-py-0.1.1/domino/custom_operators/k8s_operator.py
--rw-r--r--   0 runner    (1001) docker     (123)     3484 2023-04-06 13:01:18.000000 domino-py-0.1.1/domino/custom_operators/python_operator.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:01:27.832632 domino-py-0.1.1/domino/custom_operators/sidecar/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 13:01:18.000000 domino-py-0.1.1/domino/custom_operators/sidecar/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      279 2023-04-06 13:01:18.000000 domino-py-0.1.1/domino/custom_operators/sidecar/fuse.conf
--rw-r--r--   0 runner    (1001) docker     (123)      911 2023-04-06 13:01:18.000000 domino-py-0.1.1/domino/custom_operators/sidecar/logger.py
--rw-r--r--   0 runner    (1001) docker     (123)    11284 2023-04-06 13:01:18.000000 domino-py-0.1.1/domino/custom_operators/sidecar/mount.py
--rw-r--r--   0 runner    (1001) docker     (123)      437 2023-04-06 13:01:18.000000 domino-py-0.1.1/domino/custom_operators/sidecar/rclone.conf
--rw-r--r--   0 runner    (1001) docker     (123)      144 2023-04-06 13:01:18.000000 domino-py-0.1.1/domino/custom_operators/sidecar/sidecar_lifecycle.sh
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:01:27.832632 domino-py-0.1.1/domino/exceptions/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 13:01:18.000000 domino-py-0.1.1/domino/exceptions/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1423 2023-04-06 13:01:18.000000 domino-py-0.1.1/domino/exceptions/exceptions.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:01:27.832632 domino-py-0.1.1/domino/helm/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 13:01:18.000000 domino-py-0.1.1/domino/helm/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:01:27.832632 domino-py-0.1.1/domino/helm/domino-airflow/
--rw-r--r--   0 runner    (1001) docker     (123)      142 2023-04-06 13:01:18.000000 domino-py-0.1.1/domino/helm/domino-airflow/Chart.yaml
--rw-r--r--   0 runner    (1001) docker     (123)      763 2023-04-06 13:01:18.000000 domino-py-0.1.1/domino/helm/domino-airflow/values.yaml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:01:27.832632 domino-py-0.1.1/domino/helm/domino-base/
--rw-r--r--   0 runner    (1001) docker     (123)      349 2023-04-06 13:01:18.000000 domino-py-0.1.1/domino/helm/domino-base/.helmignore
--rw-r--r--   0 runner    (1001) docker     (123)      303 2023-04-06 13:01:18.000000 domino-py-0.1.1/domino/helm/domino-base/Chart.lock
--rw-r--r--   0 runner    (1001) docker     (123)      246 2023-04-06 13:01:18.000000 domino-py-0.1.1/domino/helm/domino-base/Chart.yaml
--rw-r--r--   0 runner    (1001) docker     (123)      484 2023-04-06 13:01:18.000000 domino-py-0.1.1/domino/helm/domino-base/values.yaml
--rw-r--r--   0 runner    (1001) docker     (123)      896 2023-04-06 13:01:18.000000 domino-py-0.1.1/domino/logger.py
--rw-r--r--   0 runner    (1001) docker     (123)      508 2023-04-06 13:01:18.000000 domino-py-0.1.1/domino/piece_generator.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:01:27.836632 domino-py-0.1.1/domino/schemas/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 13:01:18.000000 domino-py-0.1.1/domino/schemas/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      427 2023-04-06 13:01:18.000000 domino-py-0.1.1/domino/schemas/container_resources.py
--rw-r--r--   0 runner    (1001) docker     (123)      246 2023-04-06 13:01:18.000000 domino-py-0.1.1/domino/schemas/from_upstream.py
--rw-r--r--   0 runner    (1001) docker     (123)     1559 2023-04-06 13:01:18.000000 domino-py-0.1.1/domino/schemas/piece_metadata.py
--rw-r--r--   0 runner    (1001) docker     (123)     1527 2023-04-06 13:01:18.000000 domino-py-0.1.1/domino/schemas/shared_storage.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:01:27.836632 domino-py-0.1.1/domino/scripts/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 13:01:18.000000 domino-py-0.1.1/domino/scripts/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5412 2023-04-06 13:01:18.000000 domino-py-0.1.1/domino/scripts/build_docker_images_pieces.py
--rw-r--r--   0 runner    (1001) docker     (123)     6744 2023-04-06 13:01:18.000000 domino-py-0.1.1/domino/scripts/create_docker_compose_file.py
--rw-r--r--   0 runner    (1001) docker     (123)    11538 2023-04-06 13:01:18.000000 domino-py-0.1.1/domino/scripts/docker_compose_constants.py
--rw-r--r--   0 runner    (1001) docker     (123)     2560 2023-04-06 13:01:18.000000 domino-py-0.1.1/domino/scripts/docker_compose_scripts.py
--rw-r--r--   0 runner    (1001) docker     (123)     2666 2023-04-06 13:01:18.000000 domino-py-0.1.1/domino/scripts/generate_infrasctructure.py
--rw-r--r--   0 runner    (1001) docker     (123)     1368 2023-04-06 13:01:18.000000 domino-py-0.1.1/domino/scripts/load_piece.py
--rw-r--r--   0 runner    (1001) docker     (123)     2219 2023-04-06 13:01:18.000000 domino-py-0.1.1/domino/scripts/run_piece_bash.py
--rw-r--r--   0 runner    (1001) docker     (123)     1965 2023-04-06 13:01:18.000000 domino-py-0.1.1/domino/scripts/run_piece_dry.py
--rw-r--r--   0 runner    (1001) docker     (123)     1821 2023-04-06 13:01:18.000000 domino-py-0.1.1/domino/scripts/run_piece_k8s.py
--rw-r--r--   0 runner    (1001) docker     (123)    11841 2023-04-06 13:01:18.000000 domino-py-0.1.1/domino/task.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:01:27.836632 domino-py-0.1.1/domino/utils/
--rw-r--r--   0 runner    (1001) docker     (123)      231 2023-04-06 13:01:18.000000 domino-py-0.1.1/domino/utils/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)       57 2023-04-06 13:01:18.000000 domino-py-0.1.1/domino/utils/custom_types.py
--rw-r--r--   0 runner    (1001) docker     (123)      145 2023-04-06 13:01:18.000000 domino-py-0.1.1/domino/utils/enum_types.py
--rw-r--r--   0 runner    (1001) docker     (123)      455 2023-04-06 13:01:18.000000 domino-py-0.1.1/domino/utils/metadata_default.py
--rw-r--r--   0 runner    (1001) docker     (123)      271 2023-04-06 13:01:18.000000 domino-py-0.1.1/domino/utils/types_map.py
--rw-r--r--   0 runner    (1001) docker     (123)     2093 2023-04-06 13:01:18.000000 domino-py-0.1.1/domino/utils/validators.py
--rw-r--r--   0 runner    (1001) docker     (123)      272 2023-04-06 13:01:18.000000 domino-py-0.1.1/domino/utils/workflow_shared_storage.py
--rw-r--r--   0 runner    (1001) docker     (123)       22 2023-04-06 13:01:18.000000 domino-py-0.1.1/domino/version.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:01:27.836632 domino-py-0.1.1/domino_py.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     3557 2023-04-06 13:01:27.000000 domino-py-0.1.1/domino_py.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     2312 2023-04-06 13:01:27.000000 domino-py-0.1.1/domino_py.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 13:01:27.000000 domino-py-0.1.1/domino_py.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       47 2023-04-06 13:01:27.000000 domino-py-0.1.1/domino_py.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (123)      420 2023-04-06 13:01:27.000000 domino-py-0.1.1/domino_py.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        7 2023-04-06 13:01:27.000000 domino-py-0.1.1/domino_py.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)      221 2023-04-06 13:01:18.000000 domino-py-0.1.1/requirements.txt
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 13:01:27.836632 domino-py-0.1.1/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1856 2023-04-06 13:01:18.000000 domino-py-0.1.1/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:16:22.349886 domino-py-0.1.2/
+-rw-r--r--   0 runner    (1001) docker     (123)     1075 2023-04-06 13:16:12.000000 domino-py-0.1.2/LICENSE.md
+-rw-r--r--   0 runner    (1001) docker     (123)      602 2023-04-06 13:16:12.000000 domino-py-0.1.2/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     3557 2023-04-06 13:16:22.349886 domino-py-0.1.2/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     2657 2023-04-06 13:16:12.000000 domino-py-0.1.2/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:16:22.341886 domino-py-0.1.2/domino/
+-rw-r--r--   0 runner    (1001) docker     (123)       32 2023-04-06 13:16:12.000000 domino-py-0.1.2/domino/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13861 2023-04-06 13:16:12.000000 domino-py-0.1.2/domino/base_piece.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:16:22.341886 domino-py-0.1.2/domino/cli/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 13:16:12.000000 domino-py-0.1.2/domino/cli/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10056 2023-04-06 13:16:12.000000 domino-py-0.1.2/domino/cli/cli.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:16:22.341886 domino-py-0.1.2/domino/cli/utils/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 13:16:12.000000 domino-py-0.1.2/domino/cli/utils/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      647 2023-04-06 13:16:12.000000 domino-py-0.1.2/domino/cli/utils/config-domino-local.toml
+-rw-r--r--   0 runner    (1001) docker     (123)      248 2023-04-06 13:16:12.000000 domino-py-0.1.2/domino/cli/utils/constants.py
+-rw-r--r--   0 runner    (1001) docker     (123)      599 2023-04-06 13:16:12.000000 domino-py-0.1.2/domino/cli/utils/create_cluster.sh
+-rw-r--r--   0 runner    (1001) docker     (123)    18301 2023-04-06 13:16:12.000000 domino-py-0.1.2/domino/cli/utils/pieces_repository.py
+-rw-r--r--   0 runner    (1001) docker     (123)    22663 2023-04-06 13:16:12.000000 domino-py-0.1.2/domino/cli/utils/platform.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:16:22.345886 domino-py-0.1.2/domino/client/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 13:16:12.000000 domino-py-0.1.2/domino/client/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2581 2023-04-06 13:16:12.000000 domino-py-0.1.2/domino/client/airflow_client.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1862 2023-04-06 13:16:12.000000 domino-py-0.1.2/domino/client/domino_backend_client.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2176 2023-04-06 13:16:12.000000 domino-py-0.1.2/domino/client/fs_client.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2970 2023-04-06 13:16:12.000000 domino-py-0.1.2/domino/client/github_rest_client.py
+-rw-r--r--   0 runner    (1001) docker     (123)      844 2023-04-06 13:16:12.000000 domino-py-0.1.2/domino/client/local_files_client.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2739 2023-04-06 13:16:12.000000 domino-py-0.1.2/domino/client/s3_client.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:16:22.345886 domino-py-0.1.2/domino/custom_operators/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 13:16:12.000000 domino-py-0.1.2/domino/custom_operators/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2298 2023-04-06 13:16:12.000000 domino-py-0.1.2/domino/custom_operators/bash_operator.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16991 2023-04-06 13:16:12.000000 domino-py-0.1.2/domino/custom_operators/k8s_operator.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3484 2023-04-06 13:16:12.000000 domino-py-0.1.2/domino/custom_operators/python_operator.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:16:22.345886 domino-py-0.1.2/domino/custom_operators/sidecar/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 13:16:12.000000 domino-py-0.1.2/domino/custom_operators/sidecar/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      279 2023-04-06 13:16:12.000000 domino-py-0.1.2/domino/custom_operators/sidecar/fuse.conf
+-rw-r--r--   0 runner    (1001) docker     (123)      911 2023-04-06 13:16:12.000000 domino-py-0.1.2/domino/custom_operators/sidecar/logger.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11284 2023-04-06 13:16:12.000000 domino-py-0.1.2/domino/custom_operators/sidecar/mount.py
+-rw-r--r--   0 runner    (1001) docker     (123)      437 2023-04-06 13:16:12.000000 domino-py-0.1.2/domino/custom_operators/sidecar/rclone.conf
+-rw-r--r--   0 runner    (1001) docker     (123)      144 2023-04-06 13:16:12.000000 domino-py-0.1.2/domino/custom_operators/sidecar/sidecar_lifecycle.sh
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:16:22.345886 domino-py-0.1.2/domino/exceptions/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 13:16:12.000000 domino-py-0.1.2/domino/exceptions/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1423 2023-04-06 13:16:12.000000 domino-py-0.1.2/domino/exceptions/exceptions.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:16:22.345886 domino-py-0.1.2/domino/helm/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 13:16:12.000000 domino-py-0.1.2/domino/helm/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:16:22.345886 domino-py-0.1.2/domino/helm/domino-airflow/
+-rw-r--r--   0 runner    (1001) docker     (123)      142 2023-04-06 13:16:12.000000 domino-py-0.1.2/domino/helm/domino-airflow/Chart.yaml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:16:22.345886 domino-py-0.1.2/domino/helm/domino-airflow/charts/
+-rw-r--r--   0 runner    (1001) docker     (123)   157053 2023-04-06 13:16:12.000000 domino-py-0.1.2/domino/helm/domino-airflow/charts/airflow-1.7.0.tgz
+-rw-r--r--   0 runner    (1001) docker     (123)      763 2023-04-06 13:16:12.000000 domino-py-0.1.2/domino/helm/domino-airflow/values.yaml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:16:22.345886 domino-py-0.1.2/domino/helm/domino-base/
+-rw-r--r--   0 runner    (1001) docker     (123)      349 2023-04-06 13:16:12.000000 domino-py-0.1.2/domino/helm/domino-base/.helmignore
+-rw-r--r--   0 runner    (1001) docker     (123)      303 2023-04-06 13:16:12.000000 domino-py-0.1.2/domino/helm/domino-base/Chart.lock
+-rw-r--r--   0 runner    (1001) docker     (123)      246 2023-04-06 13:16:12.000000 domino-py-0.1.2/domino/helm/domino-base/Chart.yaml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:16:22.345886 domino-py-0.1.2/domino/helm/domino-base/templates/
+-rw-r--r--   0 runner    (1001) docker     (123)     2966 2023-04-06 13:16:12.000000 domino-py-0.1.2/domino/helm/domino-base/templates/domino-backend-deployment.yml
+-rw-r--r--   0 runner    (1001) docker     (123)     1430 2023-04-06 13:16:12.000000 domino-py-0.1.2/domino/helm/domino-base/templates/domino-frontend-deployment.yml
+-rw-r--r--   0 runner    (1001) docker     (123)     1317 2023-04-06 13:16:12.000000 domino-py-0.1.2/domino/helm/domino-base/templates/domino-postgres-deployment.yml
+-rw-r--r--   0 runner    (1001) docker     (123)      379 2023-04-06 13:16:12.000000 domino-py-0.1.2/domino/helm/domino-base/templates/ingress-api.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)      425 2023-04-06 13:16:12.000000 domino-py-0.1.2/domino/helm/domino-base/templates/ingress-frontend.yaml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:16:22.345886 domino-py-0.1.2/domino/helm/domino-base/templates/jobs/
+-rw-r--r--   0 runner    (1001) docker     (123)      804 2023-04-06 13:16:12.000000 domino-py-0.1.2/domino/helm/domino-base/templates/jobs/domino-migrations.yml
+-rw-r--r--   0 runner    (1001) docker     (123)      245 2023-04-06 13:16:12.000000 domino-py-0.1.2/domino/helm/domino-base/templates/secrets.yaml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:16:22.345886 domino-py-0.1.2/domino/helm/domino-base/templates/volumes/
+-rw-r--r--   0 runner    (1001) docker     (123)      220 2023-04-06 13:16:12.000000 domino-py-0.1.2/domino/helm/domino-base/templates/volumes/domino-backend-volume-claim-dev.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)      479 2023-04-06 13:16:12.000000 domino-py-0.1.2/domino/helm/domino-base/templates/volumes/domino-backend-volume-dev.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)      484 2023-04-06 13:16:12.000000 domino-py-0.1.2/domino/helm/domino-base/values.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)      896 2023-04-06 13:16:12.000000 domino-py-0.1.2/domino/logger.py
+-rw-r--r--   0 runner    (1001) docker     (123)      508 2023-04-06 13:16:12.000000 domino-py-0.1.2/domino/piece_generator.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:16:22.345886 domino-py-0.1.2/domino/schemas/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 13:16:12.000000 domino-py-0.1.2/domino/schemas/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      427 2023-04-06 13:16:12.000000 domino-py-0.1.2/domino/schemas/container_resources.py
+-rw-r--r--   0 runner    (1001) docker     (123)      246 2023-04-06 13:16:12.000000 domino-py-0.1.2/domino/schemas/from_upstream.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1559 2023-04-06 13:16:12.000000 domino-py-0.1.2/domino/schemas/piece_metadata.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1527 2023-04-06 13:16:12.000000 domino-py-0.1.2/domino/schemas/shared_storage.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:16:22.349886 domino-py-0.1.2/domino/scripts/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 13:16:12.000000 domino-py-0.1.2/domino/scripts/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5412 2023-04-06 13:16:12.000000 domino-py-0.1.2/domino/scripts/build_docker_images_pieces.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6744 2023-04-06 13:16:12.000000 domino-py-0.1.2/domino/scripts/create_docker_compose_file.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11538 2023-04-06 13:16:12.000000 domino-py-0.1.2/domino/scripts/docker_compose_constants.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2560 2023-04-06 13:16:12.000000 domino-py-0.1.2/domino/scripts/docker_compose_scripts.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2666 2023-04-06 13:16:12.000000 domino-py-0.1.2/domino/scripts/generate_infrasctructure.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1368 2023-04-06 13:16:12.000000 domino-py-0.1.2/domino/scripts/load_piece.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2219 2023-04-06 13:16:12.000000 domino-py-0.1.2/domino/scripts/run_piece_bash.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1965 2023-04-06 13:16:12.000000 domino-py-0.1.2/domino/scripts/run_piece_dry.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1821 2023-04-06 13:16:12.000000 domino-py-0.1.2/domino/scripts/run_piece_k8s.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11841 2023-04-06 13:16:12.000000 domino-py-0.1.2/domino/task.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:16:22.349886 domino-py-0.1.2/domino/utils/
+-rw-r--r--   0 runner    (1001) docker     (123)      231 2023-04-06 13:16:12.000000 domino-py-0.1.2/domino/utils/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)       57 2023-04-06 13:16:12.000000 domino-py-0.1.2/domino/utils/custom_types.py
+-rw-r--r--   0 runner    (1001) docker     (123)      145 2023-04-06 13:16:12.000000 domino-py-0.1.2/domino/utils/enum_types.py
+-rw-r--r--   0 runner    (1001) docker     (123)      455 2023-04-06 13:16:12.000000 domino-py-0.1.2/domino/utils/metadata_default.py
+-rw-r--r--   0 runner    (1001) docker     (123)      271 2023-04-06 13:16:12.000000 domino-py-0.1.2/domino/utils/types_map.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2093 2023-04-06 13:16:12.000000 domino-py-0.1.2/domino/utils/validators.py
+-rw-r--r--   0 runner    (1001) docker     (123)      272 2023-04-06 13:16:12.000000 domino-py-0.1.2/domino/utils/workflow_shared_storage.py
+-rw-r--r--   0 runner    (1001) docker     (123)       22 2023-04-06 13:16:12.000000 domino-py-0.1.2/domino/version.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:16:22.349886 domino-py-0.1.2/domino_py.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     3557 2023-04-06 13:16:22.000000 domino-py-0.1.2/domino_py.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     2925 2023-04-06 13:16:22.000000 domino-py-0.1.2/domino_py.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 13:16:22.000000 domino-py-0.1.2/domino_py.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       47 2023-04-06 13:16:22.000000 domino-py-0.1.2/domino_py.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      420 2023-04-06 13:16:22.000000 domino-py-0.1.2/domino_py.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        7 2023-04-06 13:16:22.000000 domino-py-0.1.2/domino_py.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      221 2023-04-06 13:16:12.000000 domino-py-0.1.2/requirements.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 13:16:22.349886 domino-py-0.1.2/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     2116 2023-04-06 13:16:12.000000 domino-py-0.1.2/setup.py
```

### Comparing `domino-py-0.1.1/LICENSE.md` & `domino-py-0.1.2/LICENSE.md`

 * *Files identical despite different names*

### Comparing `domino-py-0.1.1/PKG-INFO` & `domino-py-0.1.2/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: domino-py
-Version: 0.1.1
+Version: 0.1.2
 Summary: Domino project
 Home-page: UNKNOWN
 Author: Luiz Tauffer and Vinicius Vaz
 Author-email: luiz@taufferconsulting.com
 License: UNKNOWN
 Description: [<img src="https://img.shields.io/pypi/v/flowui-project?color=%231BA331&label=PyPI&logo=python&logoColor=%23F7F991%20">](https://pypi.org/project/flowui-project/)
         [<img src="https://img.shields.io/docker/v/taufferconsulting/flowui-backend?label=Backend&logo=docker&style=flat">](https://hub.docker.com/r/taufferconsulting/flowui-backend)
```

### Comparing `domino-py-0.1.1/README.md` & `domino-py-0.1.2/README.md`

 * *Files identical despite different names*

### Comparing `domino-py-0.1.1/domino/base_piece.py` & `domino-py-0.1.2/domino/base_piece.py`

 * *Files identical despite different names*

### Comparing `domino-py-0.1.1/domino/cli/cli.py` & `domino-py-0.1.2/domino/cli/cli.py`

 * *Files identical despite different names*

### Comparing `domino-py-0.1.1/domino/cli/utils/config-domino-local.toml` & `domino-py-0.1.2/domino/cli/utils/config-domino-local.toml`

 * *Files identical despite different names*

### Comparing `domino-py-0.1.1/domino/cli/utils/create_cluster.sh` & `domino-py-0.1.2/domino/cli/utils/create_cluster.sh`

 * *Files identical despite different names*

### Comparing `domino-py-0.1.1/domino/cli/utils/pieces_repository.py` & `domino-py-0.1.2/domino/cli/utils/pieces_repository.py`

 * *Files identical despite different names*

### Comparing `domino-py-0.1.1/domino/cli/utils/platform.py` & `domino-py-0.1.2/domino/cli/utils/platform.py`

 * *Files identical despite different names*

### Comparing `domino-py-0.1.1/domino/client/airflow_client.py` & `domino-py-0.1.2/domino/client/airflow_client.py`

 * *Files identical despite different names*

### Comparing `domino-py-0.1.1/domino/client/domino_backend_client.py` & `domino-py-0.1.2/domino/client/domino_backend_client.py`

 * *Files identical despite different names*

### Comparing `domino-py-0.1.1/domino/client/fs_client.py` & `domino-py-0.1.2/domino/client/fs_client.py`

 * *Files identical despite different names*

### Comparing `domino-py-0.1.1/domino/client/github_rest_client.py` & `domino-py-0.1.2/domino/client/github_rest_client.py`

 * *Files identical despite different names*

### Comparing `domino-py-0.1.1/domino/client/local_files_client.py` & `domino-py-0.1.2/domino/client/local_files_client.py`

 * *Files identical despite different names*

### Comparing `domino-py-0.1.1/domino/client/s3_client.py` & `domino-py-0.1.2/domino/client/s3_client.py`

 * *Files identical despite different names*

### Comparing `domino-py-0.1.1/domino/custom_operators/bash_operator.py` & `domino-py-0.1.2/domino/custom_operators/bash_operator.py`

 * *Files identical despite different names*

### Comparing `domino-py-0.1.1/domino/custom_operators/k8s_operator.py` & `domino-py-0.1.2/domino/custom_operators/k8s_operator.py`

 * *Files identical despite different names*

### Comparing `domino-py-0.1.1/domino/custom_operators/python_operator.py` & `domino-py-0.1.2/domino/custom_operators/python_operator.py`

 * *Files identical despite different names*

### Comparing `domino-py-0.1.1/domino/custom_operators/sidecar/logger.py` & `domino-py-0.1.2/domino/custom_operators/sidecar/logger.py`

 * *Files identical despite different names*

### Comparing `domino-py-0.1.1/domino/custom_operators/sidecar/mount.py` & `domino-py-0.1.2/domino/custom_operators/sidecar/mount.py`

 * *Files identical despite different names*

### Comparing `domino-py-0.1.1/domino/exceptions/exceptions.py` & `domino-py-0.1.2/domino/exceptions/exceptions.py`

 * *Files identical despite different names*

### Comparing `domino-py-0.1.1/domino/helm/domino-airflow/values.yaml` & `domino-py-0.1.2/domino/helm/domino-airflow/values.yaml`

 * *Files identical despite different names*

### Comparing `domino-py-0.1.1/domino/logger.py` & `domino-py-0.1.2/domino/logger.py`

 * *Files identical despite different names*

### Comparing `domino-py-0.1.1/domino/schemas/piece_metadata.py` & `domino-py-0.1.2/domino/schemas/piece_metadata.py`

 * *Files identical despite different names*

### Comparing `domino-py-0.1.1/domino/schemas/shared_storage.py` & `domino-py-0.1.2/domino/schemas/shared_storage.py`

 * *Files identical despite different names*

### Comparing `domino-py-0.1.1/domino/scripts/build_docker_images_pieces.py` & `domino-py-0.1.2/domino/scripts/build_docker_images_pieces.py`

 * *Files identical despite different names*

### Comparing `domino-py-0.1.1/domino/scripts/create_docker_compose_file.py` & `domino-py-0.1.2/domino/scripts/create_docker_compose_file.py`

 * *Files identical despite different names*

### Comparing `domino-py-0.1.1/domino/scripts/docker_compose_constants.py` & `domino-py-0.1.2/domino/scripts/docker_compose_constants.py`

 * *Files identical despite different names*

### Comparing `domino-py-0.1.1/domino/scripts/docker_compose_scripts.py` & `domino-py-0.1.2/domino/scripts/docker_compose_scripts.py`

 * *Files identical despite different names*

### Comparing `domino-py-0.1.1/domino/scripts/generate_infrasctructure.py` & `domino-py-0.1.2/domino/scripts/generate_infrasctructure.py`

 * *Files identical despite different names*

### Comparing `domino-py-0.1.1/domino/scripts/load_piece.py` & `domino-py-0.1.2/domino/scripts/load_piece.py`

 * *Files identical despite different names*

### Comparing `domino-py-0.1.1/domino/scripts/run_piece_bash.py` & `domino-py-0.1.2/domino/scripts/run_piece_bash.py`

 * *Files identical despite different names*

### Comparing `domino-py-0.1.1/domino/scripts/run_piece_dry.py` & `domino-py-0.1.2/domino/scripts/run_piece_dry.py`

 * *Files identical despite different names*

### Comparing `domino-py-0.1.1/domino/scripts/run_piece_k8s.py` & `domino-py-0.1.2/domino/scripts/run_piece_k8s.py`

 * *Files identical despite different names*

### Comparing `domino-py-0.1.1/domino/task.py` & `domino-py-0.1.2/domino/task.py`

 * *Files identical despite different names*

### Comparing `domino-py-0.1.1/domino/utils/validators.py` & `domino-py-0.1.2/domino/utils/validators.py`

 * *Files identical despite different names*

### Comparing `domino-py-0.1.1/domino_py.egg-info/PKG-INFO` & `domino-py-0.1.2/domino_py.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: domino-py
-Version: 0.1.1
+Version: 0.1.2
 Summary: Domino project
 Home-page: UNKNOWN
 Author: Luiz Tauffer and Vinicius Vaz
 Author-email: luiz@taufferconsulting.com
 License: UNKNOWN
 Description: [<img src="https://img.shields.io/pypi/v/flowui-project?color=%231BA331&label=PyPI&logo=python&logoColor=%23F7F991%20">](https://pypi.org/project/flowui-project/)
         [<img src="https://img.shields.io/docker/v/taufferconsulting/flowui-backend?label=Backend&logo=docker&style=flat">](https://hub.docker.com/r/taufferconsulting/flowui-backend)
```

### Comparing `domino-py-0.1.1/domino_py.egg-info/SOURCES.txt` & `domino-py-0.1.2/domino_py.egg-info/SOURCES.txt`

 * *Files 8% similar despite different names*

```diff
@@ -35,18 +35,28 @@
 domino/custom_operators/sidecar/rclone.conf
 domino/custom_operators/sidecar/sidecar_lifecycle.sh
 domino/exceptions/__init__.py
 domino/exceptions/exceptions.py
 domino/helm/__init__.py
 domino/helm/domino-airflow/Chart.yaml
 domino/helm/domino-airflow/values.yaml
+domino/helm/domino-airflow/charts/airflow-1.7.0.tgz
 domino/helm/domino-base/.helmignore
 domino/helm/domino-base/Chart.lock
 domino/helm/domino-base/Chart.yaml
 domino/helm/domino-base/values.yaml
+domino/helm/domino-base/templates/domino-backend-deployment.yml
+domino/helm/domino-base/templates/domino-frontend-deployment.yml
+domino/helm/domino-base/templates/domino-postgres-deployment.yml
+domino/helm/domino-base/templates/ingress-api.yaml
+domino/helm/domino-base/templates/ingress-frontend.yaml
+domino/helm/domino-base/templates/secrets.yaml
+domino/helm/domino-base/templates/jobs/domino-migrations.yml
+domino/helm/domino-base/templates/volumes/domino-backend-volume-claim-dev.yaml
+domino/helm/domino-base/templates/volumes/domino-backend-volume-dev.yaml
 domino/schemas/__init__.py
 domino/schemas/container_resources.py
 domino/schemas/from_upstream.py
 domino/schemas/piece_metadata.py
 domino/schemas/shared_storage.py
 domino/scripts/__init__.py
 domino/scripts/build_docker_images_pieces.py
```

### Comparing `domino-py-0.1.1/setup.py` & `domino-py-0.1.2/setup.py`

 * *Files 10% similar despite different names*

```diff
@@ -37,16 +37,21 @@
     keywords=["airflow", "UI"],
     packages=find_packages(),
     package_data={
         'domino': [
             'cli/utils/config-domino-local.toml',
             'cli/utils/create_cluster.sh',
             'helm/domino-airflow/kind-cluster-config',
-            'helm/domino-airflow/**',
-            'helm/domino-base/**',
+            'helm/domino-airflow/**/*',
+            'helm/domino-base/**/*',
+            'helm/domino-airflow/charts/**',
+            'domino/helm/domino-base/**',
+            'domino/helm/domino-base/templates/**',
+            'domino/helm/domino-base/templates/jobs/**',
+            'domino/helm/domino-base/templates/volumes/**',
             'custom_operators/sidecar/sidecar_lifecycle.sh',
             'custom_operators/sidecar/rclone.conf',
             'custom_operators/sidecar/fuse.conf',
         ]
     },
     include_package_data=True,
     python_requires=">=3.7",
```

