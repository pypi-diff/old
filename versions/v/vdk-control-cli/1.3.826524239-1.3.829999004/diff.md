# Comparing `tmp/vdk-control-cli-1.3.826524239.tar.gz` & `tmp/vdk-control-cli-1.3.829999004.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/vdk-control-cli-1.3.826524239.tar", last modified: Mon Apr  3 15:41:22 2023, max compression
+gzip compressed data, was "dist/vdk-control-cli-1.3.829999004.tar", last modified: Thu Apr  6 11:02:22 2023, max compression
```

## Comparing `vdk-control-cli-1.3.826524239.tar` & `vdk-control-cli-1.3.829999004.tar`

### file list

```diff
@@ -1,71 +1,72 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-03 15:41:22.000000 vdk-control-cli-1.3.826524239/
--rw-rw-rw-   0 root         (0) root         (0)      270 2023-04-03 15:41:08.000000 vdk-control-cli-1.3.826524239/MANIFEST.in
--rw-r--r--   0 root         (0) root         (0)     5153 2023-04-03 15:41:22.000000 vdk-control-cli-1.3.826524239/PKG-INFO
--rw-rw-rw-   0 root         (0) root         (0)     4192 2023-04-03 15:41:08.000000 vdk-control-cli-1.3.826524239/README.md
--rw-rw-rw-   0 root         (0) root         (0)     1746 2023-04-03 15:41:22.000000 vdk-control-cli-1.3.826524239/setup.cfg
--rw-rw-rw-   0 root         (0) root         (0)      460 2023-04-03 15:41:08.000000 vdk-control-cli-1.3.826524239/setup.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-03 15:41:22.000000 vdk-control-cli-1.3.826524239/src/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-03 15:41:22.000000 vdk-control-cli-1.3.826524239/src/vdk/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-03 15:41:22.000000 vdk-control-cli-1.3.826524239/src/vdk/api/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-03 15:41:22.000000 vdk-control-cli-1.3.826524239/src/vdk/api/control/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-03 15:41:22.000000 vdk-control-cli-1.3.826524239/src/vdk/api/control/plugin/
--rw-rw-rw-   0 root         (0) root         (0)      717 2023-04-03 15:41:08.000000 vdk-control-cli-1.3.826524239/src/vdk/api/control/plugin/markers.py
--rw-rw-rw-   0 root         (0) root         (0)     1423 2023-04-03 15:41:08.000000 vdk-control-cli-1.3.826524239/src/vdk/api/control/plugin/specs.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-03 15:41:22.000000 vdk-control-cli-1.3.826524239/src/vdk/internal/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-03 15:41:22.000000 vdk-control-cli-1.3.826524239/src/vdk/internal/control/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-03 15:41:22.000000 vdk-control-cli-1.3.826524239/src/vdk/internal/control/command_groups/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-03 15:41:22.000000 vdk-control-cli-1.3.826524239/src/vdk/internal/control/command_groups/common_group/
--rw-rw-rw-   0 root         (0) root         (0)     2284 2023-04-03 15:41:08.000000 vdk-control-cli-1.3.826524239/src/vdk/internal/control/command_groups/common_group/default.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-03 15:41:22.000000 vdk-control-cli-1.3.826524239/src/vdk/internal/control/command_groups/job/
--rw-rw-rw-   0 root         (0) root         (0)    11236 2023-04-03 15:41:08.000000 vdk-control-cli-1.3.826524239/src/vdk/internal/control/command_groups/job/create.py
--rw-rw-rw-   0 root         (0) root         (0)     2121 2023-04-03 15:41:08.000000 vdk-control-cli-1.3.826524239/src/vdk/internal/control/command_groups/job/delete.py
--rw-rw-rw-   0 root         (0) root         (0)     7183 2023-04-03 15:41:08.000000 vdk-control-cli-1.3.826524239/src/vdk/internal/control/command_groups/job/deploy_cli.py
--rw-rw-rw-   0 root         (0) root         (0)    13877 2023-04-03 15:41:08.000000 vdk-control-cli-1.3.826524239/src/vdk/internal/control/command_groups/job/deploy_cli_impl.py
--rw-rw-rw-   0 root         (0) root         (0)     5115 2023-04-03 15:41:08.000000 vdk-control-cli-1.3.826524239/src/vdk/internal/control/command_groups/job/download_job.py
--rw-rw-rw-   0 root         (0) root         (0)     2673 2023-04-03 15:41:08.000000 vdk-control-cli-1.3.826524239/src/vdk/internal/control/command_groups/job/download_key.py
--rw-rw-rw-   0 root         (0) root         (0)    12141 2023-04-03 15:41:08.000000 vdk-control-cli-1.3.826524239/src/vdk/internal/control/command_groups/job/execute.py
--rw-rw-rw-   0 root         (0) root         (0)     8252 2023-04-03 15:41:08.000000 vdk-control-cli-1.3.826524239/src/vdk/internal/control/command_groups/job/list.py
--rw-rw-rw-   0 root         (0) root         (0)    12259 2023-04-03 15:41:08.000000 vdk-control-cli-1.3.826524239/src/vdk/internal/control/command_groups/job/properties.py
--rw-rw-rw-   0 root         (0) root         (0)     3381 2023-04-03 15:41:08.000000 vdk-control-cli-1.3.826524239/src/vdk/internal/control/command_groups/job/show.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-03 15:41:22.000000 vdk-control-cli-1.3.826524239/src/vdk/internal/control/command_groups/login_group/
--rw-rw-rw-   0 root         (0) root         (0)     6510 2023-04-03 15:41:08.000000 vdk-control-cli-1.3.826524239/src/vdk/internal/control/command_groups/login_group/login.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-03 15:41:22.000000 vdk-control-cli-1.3.826524239/src/vdk/internal/control/command_groups/logout_group/
--rw-rw-rw-   0 root         (0) root         (0)      410 2023-04-03 15:41:08.000000 vdk-control-cli-1.3.826524239/src/vdk/internal/control/command_groups/logout_group/logout.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-03 15:41:22.000000 vdk-control-cli-1.3.826524239/src/vdk/internal/control/command_groups/version_group/
--rw-rw-rw-   0 root         (0) root         (0)      371 2023-04-03 15:41:08.000000 vdk-control-cli-1.3.826524239/src/vdk/internal/control/command_groups/version_group/version.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-03 15:41:22.000000 vdk-control-cli-1.3.826524239/src/vdk/internal/control/configuration/
--rw-rw-rw-   0 root         (0) root         (0)      424 2023-04-03 15:41:08.000000 vdk-control-cli-1.3.826524239/src/vdk/internal/control/configuration/default_options.py
--rw-rw-rw-   0 root         (0) root         (0)     1221 2023-04-03 15:41:08.000000 vdk-control-cli-1.3.826524239/src/vdk/internal/control/configuration/defaults_config.py
--rw-rw-rw-   0 root         (0) root         (0)     2272 2023-04-03 15:41:08.000000 vdk-control-cli-1.3.826524239/src/vdk/internal/control/configuration/log_config.py
--rw-rw-rw-   0 root         (0) root         (0)     9834 2023-04-03 15:41:08.000000 vdk-control-cli-1.3.826524239/src/vdk/internal/control/configuration/vdk_config.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-03 15:41:22.000000 vdk-control-cli-1.3.826524239/src/vdk/internal/control/exception/
--rw-rw-rw-   0 root         (0) root         (0)      649 2023-04-03 15:41:08.000000 vdk-control-cli-1.3.826524239/src/vdk/internal/control/exception/vdk_exception.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-03 15:41:22.000000 vdk-control-cli-1.3.826524239/src/vdk/internal/control/job/
--rw-rw-rw-   0 root         (0) root         (0)     1930 2023-04-03 15:41:08.000000 vdk-control-cli-1.3.826524239/src/vdk/internal/control/job/job_archive.py
--rw-rw-rw-   0 root         (0) root         (0)     4768 2023-04-03 15:41:08.000000 vdk-control-cli-1.3.826524239/src/vdk/internal/control/job/job_config.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-03 15:41:22.000000 vdk-control-cli-1.3.826524239/src/vdk/internal/control/job/sample_job/
--rw-rw-rw-   0 root         (0) root         (0)      579 2023-04-03 15:41:08.000000 vdk-control-cli-1.3.826524239/src/vdk/internal/control/job/sample_job/10_sql_step.sql
--rw-rw-rw-   0 root         (0) root         (0)      816 2023-04-03 15:41:08.000000 vdk-control-cli-1.3.826524239/src/vdk/internal/control/job/sample_job/20_python_step.py
--rw-rw-rw-   0 root         (0) root         (0)     1446 2023-04-03 15:41:08.000000 vdk-control-cli-1.3.826524239/src/vdk/internal/control/job/sample_job/README.md
--rw-rw-rw-   0 root         (0) root         (0)     2902 2023-04-03 15:41:08.000000 vdk-control-cli-1.3.826524239/src/vdk/internal/control/job/sample_job/config.ini
--rw-rw-rw-   0 root         (0) root         (0)      243 2023-04-03 15:41:08.000000 vdk-control-cli-1.3.826524239/src/vdk/internal/control/job/sample_job/requirements.txt
--rw-rw-rw-   0 root         (0) root         (0)     3458 2023-04-03 15:41:08.000000 vdk-control-cli-1.3.826524239/src/vdk/internal/control/main.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-03 15:41:22.000000 vdk-control-cli-1.3.826524239/src/vdk/internal/control/plugin/
--rw-rw-rw-   0 root         (0) root         (0)     3715 2023-04-03 15:41:08.000000 vdk-control-cli-1.3.826524239/src/vdk/internal/control/plugin/control_plugin_manager.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-03 15:41:22.000000 vdk-control-cli-1.3.826524239/src/vdk/internal/control/rest_lib/
--rw-rw-rw-   0 root         (0) root         (0)     2915 2023-04-03 15:41:08.000000 vdk-control-cli-1.3.826524239/src/vdk/internal/control/rest_lib/factory.py
--rw-rw-rw-   0 root         (0) root         (0)     3845 2023-04-03 15:41:08.000000 vdk-control-cli-1.3.826524239/src/vdk/internal/control/rest_lib/rest_client_errors.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-03 15:41:22.000000 vdk-control-cli-1.3.826524239/src/vdk/internal/control/utils/
--rw-rw-rw-   0 root         (0) root         (0)     7794 2023-04-03 15:41:08.000000 vdk-control-cli-1.3.826524239/src/vdk/internal/control/utils/cli_utils.py
--rw-rw-rw-   0 root         (0) root         (0)     1413 2023-04-03 15:41:08.000000 vdk-control-cli-1.3.826524239/src/vdk/internal/control/utils/control_utils.py
--rw-rw-rw-   0 root         (0) root         (0)      819 2023-04-03 15:41:08.000000 vdk-control-cli-1.3.826524239/src/vdk/internal/control/utils/version_utils.py
--rw-rw-rw-   0 root         (0) root         (0)      181 2023-04-03 15:41:12.000000 vdk-control-cli-1.3.826524239/src/vdk/internal/control/vdk_control_build_info.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-03 15:41:22.000000 vdk-control-cli-1.3.826524239/src/vdk_control_cli.egg-info/
--rw-r--r--   0 root         (0) root         (0)     5153 2023-04-03 15:41:22.000000 vdk-control-cli-1.3.826524239/src/vdk_control_cli.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)     2263 2023-04-03 15:41:22.000000 vdk-control-cli-1.3.826524239/src/vdk_control_cli.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2023-04-03 15:41:22.000000 vdk-control-cli-1.3.826524239/src/vdk_control_cli.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)       57 2023-04-03 15:41:22.000000 vdk-control-cli-1.3.826524239/src/vdk_control_cli.egg-info/entry_points.txt
--rw-r--r--   0 root         (0) root         (0)        1 2023-04-03 15:41:22.000000 vdk-control-cli-1.3.826524239/src/vdk_control_cli.egg-info/not-zip-safe
--rw-r--r--   0 root         (0) root         (0)      184 2023-04-03 15:41:22.000000 vdk-control-cli-1.3.826524239/src/vdk_control_cli.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)        4 2023-04-03 15:41:22.000000 vdk-control-cli-1.3.826524239/src/vdk_control_cli.egg-info/top_level.txt
--rw-rw-rw-   0 root         (0) root         (0)       14 2023-04-03 15:41:12.000000 vdk-control-cli-1.3.826524239/version.txt
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 11:02:22.000000 vdk-control-cli-1.3.829999004/
+-rw-rw-rw-   0 root         (0) root         (0)      270 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/MANIFEST.in
+-rw-r--r--   0 root         (0) root         (0)     5153 2023-04-06 11:02:22.000000 vdk-control-cli-1.3.829999004/PKG-INFO
+-rw-rw-rw-   0 root         (0) root         (0)     4192 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/README.md
+-rw-rw-rw-   0 root         (0) root         (0)     1746 2023-04-06 11:02:22.000000 vdk-control-cli-1.3.829999004/setup.cfg
+-rw-rw-rw-   0 root         (0) root         (0)      460 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 11:02:22.000000 vdk-control-cli-1.3.829999004/src/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 11:02:22.000000 vdk-control-cli-1.3.829999004/src/vdk/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 11:02:22.000000 vdk-control-cli-1.3.829999004/src/vdk/api/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 11:02:22.000000 vdk-control-cli-1.3.829999004/src/vdk/api/control/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 11:02:22.000000 vdk-control-cli-1.3.829999004/src/vdk/api/control/plugin/
+-rw-rw-rw-   0 root         (0) root         (0)      717 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/src/vdk/api/control/plugin/markers.py
+-rw-rw-rw-   0 root         (0) root         (0)     1423 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/src/vdk/api/control/plugin/specs.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 11:02:22.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 11:02:22.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 11:02:22.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/command_groups/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 11:02:22.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/command_groups/common_group/
+-rw-rw-rw-   0 root         (0) root         (0)     2284 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/command_groups/common_group/default.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 11:02:22.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/command_groups/job/
+-rw-rw-rw-   0 root         (0) root         (0)    11236 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/command_groups/job/create.py
+-rw-rw-rw-   0 root         (0) root         (0)     2121 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/command_groups/job/delete.py
+-rw-rw-rw-   0 root         (0) root         (0)     7183 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/command_groups/job/deploy_cli.py
+-rw-rw-rw-   0 root         (0) root         (0)    13882 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/command_groups/job/deploy_cli_impl.py
+-rw-rw-rw-   0 root         (0) root         (0)     5115 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/command_groups/job/download_job.py
+-rw-rw-rw-   0 root         (0) root         (0)     2673 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/command_groups/job/download_key.py
+-rw-rw-rw-   0 root         (0) root         (0)    12146 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/command_groups/job/execute.py
+-rw-rw-rw-   0 root         (0) root         (0)     8970 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/command_groups/job/list.py
+-rw-rw-rw-   0 root         (0) root         (0)    12264 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/command_groups/job/properties.py
+-rw-rw-rw-   0 root         (0) root         (0)     3375 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/command_groups/job/show.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 11:02:22.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/command_groups/login_group/
+-rw-rw-rw-   0 root         (0) root         (0)     6510 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/command_groups/login_group/login.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 11:02:22.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/command_groups/logout_group/
+-rw-rw-rw-   0 root         (0) root         (0)      410 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/command_groups/logout_group/logout.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 11:02:22.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/command_groups/version_group/
+-rw-rw-rw-   0 root         (0) root         (0)      371 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/command_groups/version_group/version.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 11:02:22.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/configuration/
+-rw-rw-rw-   0 root         (0) root         (0)      424 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/configuration/default_options.py
+-rw-rw-rw-   0 root         (0) root         (0)     1221 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/configuration/defaults_config.py
+-rw-rw-rw-   0 root         (0) root         (0)     2272 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/configuration/log_config.py
+-rw-rw-rw-   0 root         (0) root         (0)     9834 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/configuration/vdk_config.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 11:02:22.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/exception/
+-rw-rw-rw-   0 root         (0) root         (0)      649 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/exception/vdk_exception.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 11:02:22.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/job/
+-rw-rw-rw-   0 root         (0) root         (0)     1930 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/job/job_archive.py
+-rw-rw-rw-   0 root         (0) root         (0)     4768 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/job/job_config.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 11:02:22.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/job/sample_job/
+-rw-rw-rw-   0 root         (0) root         (0)      579 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/job/sample_job/10_sql_step.sql
+-rw-rw-rw-   0 root         (0) root         (0)      816 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/job/sample_job/20_python_step.py
+-rw-rw-rw-   0 root         (0) root         (0)     1446 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/job/sample_job/README.md
+-rw-rw-rw-   0 root         (0) root         (0)     2902 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/job/sample_job/config.ini
+-rw-rw-rw-   0 root         (0) root         (0)      243 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/job/sample_job/requirements.txt
+-rw-rw-rw-   0 root         (0) root         (0)     3458 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/main.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 11:02:22.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/plugin/
+-rw-rw-rw-   0 root         (0) root         (0)     3715 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/plugin/control_plugin_manager.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 11:02:22.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/rest_lib/
+-rw-rw-rw-   0 root         (0) root         (0)     2915 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/rest_lib/factory.py
+-rw-rw-rw-   0 root         (0) root         (0)     3845 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/rest_lib/rest_client_errors.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 11:02:22.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/utils/
+-rw-rw-rw-   0 root         (0) root         (0)     7297 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/utils/cli_utils.py
+-rw-rw-rw-   0 root         (0) root         (0)     1413 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/utils/control_utils.py
+-rw-rw-rw-   0 root         (0) root         (0)     3690 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/utils/output_printer.py
+-rw-rw-rw-   0 root         (0) root         (0)      819 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/utils/version_utils.py
+-rw-rw-rw-   0 root         (0) root         (0)      181 2023-04-06 11:02:10.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/vdk_control_build_info.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 11:02:22.000000 vdk-control-cli-1.3.829999004/src/vdk_control_cli.egg-info/
+-rw-r--r--   0 root         (0) root         (0)     5153 2023-04-06 11:02:22.000000 vdk-control-cli-1.3.829999004/src/vdk_control_cli.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)     2312 2023-04-06 11:02:22.000000 vdk-control-cli-1.3.829999004/src/vdk_control_cli.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2023-04-06 11:02:22.000000 vdk-control-cli-1.3.829999004/src/vdk_control_cli.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)       57 2023-04-06 11:02:22.000000 vdk-control-cli-1.3.829999004/src/vdk_control_cli.egg-info/entry_points.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2023-04-06 11:02:22.000000 vdk-control-cli-1.3.829999004/src/vdk_control_cli.egg-info/not-zip-safe
+-rw-r--r--   0 root         (0) root         (0)      184 2023-04-06 11:02:22.000000 vdk-control-cli-1.3.829999004/src/vdk_control_cli.egg-info/requires.txt
+-rw-r--r--   0 root         (0) root         (0)        4 2023-04-06 11:02:22.000000 vdk-control-cli-1.3.829999004/src/vdk_control_cli.egg-info/top_level.txt
+-rw-rw-rw-   0 root         (0) root         (0)       14 2023-04-06 11:02:10.000000 vdk-control-cli-1.3.829999004/version.txt
```

### Comparing `vdk-control-cli-1.3.826524239/PKG-INFO` & `vdk-control-cli-1.3.829999004/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: vdk-control-cli
-Version: 1.3.826524239
+Version: 1.3.829999004
 Summary: VDK Control CLI allows user to create, delete, manage and their Data Jobs in Kubernetes runtime.
 Home-page: https://github.com/vmware/versatile-data-kit
 Author: VMware Inc.
 Author-email: aivanov@vmware.com
 Project-URL: Documentation, https://github.com/vmware/versatile-data-kit/wiki
 Project-URL: Source, https://github.com/vmware/versatile-data-kit/projects/vdk-control-cli
 Platform: any
```

### Comparing `vdk-control-cli-1.3.826524239/README.md` & `vdk-control-cli-1.3.829999004/README.md`

 * *Files identical despite different names*

### Comparing `vdk-control-cli-1.3.826524239/setup.cfg` & `vdk-control-cli-1.3.829999004/setup.cfg`

 * *Files identical despite different names*

### Comparing `vdk-control-cli-1.3.826524239/src/vdk/api/control/plugin/markers.py` & `vdk-control-cli-1.3.829999004/src/vdk/api/control/plugin/markers.py`

 * *Files identical despite different names*

### Comparing `vdk-control-cli-1.3.826524239/src/vdk/api/control/plugin/specs.py` & `vdk-control-cli-1.3.829999004/src/vdk/api/control/plugin/specs.py`

 * *Files identical despite different names*

### Comparing `vdk-control-cli-1.3.826524239/src/vdk/internal/control/command_groups/common_group/default.py` & `vdk-control-cli-1.3.829999004/src/vdk/internal/control/command_groups/common_group/default.py`

 * *Files identical despite different names*

### Comparing `vdk-control-cli-1.3.826524239/src/vdk/internal/control/command_groups/job/create.py` & `vdk-control-cli-1.3.829999004/src/vdk/internal/control/command_groups/job/create.py`

 * *Files identical despite different names*

### Comparing `vdk-control-cli-1.3.826524239/src/vdk/internal/control/command_groups/job/delete.py` & `vdk-control-cli-1.3.829999004/src/vdk/internal/control/command_groups/job/delete.py`

 * *Files identical despite different names*

### Comparing `vdk-control-cli-1.3.826524239/src/vdk/internal/control/command_groups/job/deploy_cli.py` & `vdk-control-cli-1.3.829999004/src/vdk/internal/control/command_groups/job/deploy_cli.py`

 * *Files identical despite different names*

### Comparing `vdk-control-cli-1.3.826524239/src/vdk/internal/control/command_groups/job/deploy_cli_impl.py` & `vdk-control-cli-1.3.829999004/src/vdk/internal/control/command_groups/job/deploy_cli_impl.py`

 * *Files 0% similar despite different names*

```diff
@@ -18,15 +18,15 @@
 from vdk.internal.control.configuration.defaults_config import load_default_team_name
 from vdk.internal.control.exception.vdk_exception import VDKException
 from vdk.internal.control.job.job_archive import JobArchive
 from vdk.internal.control.job.job_config import JobConfig
 from vdk.internal.control.rest_lib.factory import ApiClientFactory
 from vdk.internal.control.rest_lib.rest_client_errors import ApiClientErrorDecorator
 from vdk.internal.control.utils.cli_utils import get_or_prompt
-from vdk.internal.control.utils.cli_utils import OutputFormat
+from vdk.internal.control.utils.output_printer import OutputFormat
 
 log = logging.getLogger(__name__)
 
 
 class JobDeploy:
     ZIP_ARCHIVE_TYPE = "zip"
     ARCHIVE_SUFFIX = "-archive"
```

### Comparing `vdk-control-cli-1.3.826524239/src/vdk/internal/control/command_groups/job/download_job.py` & `vdk-control-cli-1.3.829999004/src/vdk/internal/control/command_groups/job/download_job.py`

 * *Files identical despite different names*

### Comparing `vdk-control-cli-1.3.826524239/src/vdk/internal/control/command_groups/job/download_key.py` & `vdk-control-cli-1.3.829999004/src/vdk/internal/control/command_groups/job/download_key.py`

 * *Files identical despite different names*

### Comparing `vdk-control-cli-1.3.826524239/src/vdk/internal/control/command_groups/job/execute.py` & `vdk-control-cli-1.3.829999004/src/vdk/internal/control/command_groups/job/execute.py`

 * *Files 1% similar despite different names*

```diff
@@ -18,15 +18,15 @@
 from taurus_datajob_api import DataJobExecutionRequest
 from vdk.internal.control.configuration.defaults_config import load_default_team_name
 from vdk.internal.control.exception.vdk_exception import VDKException
 from vdk.internal.control.rest_lib.factory import ApiClientFactory
 from vdk.internal.control.rest_lib.rest_client_errors import ApiClientErrorDecorator
 from vdk.internal.control.utils import cli_utils
 from vdk.internal.control.utils.cli_utils import get_or_prompt
-from vdk.internal.control.utils.cli_utils import OutputFormat
+from vdk.internal.control.utils.output_printer import OutputFormat
 
 log = logging.getLogger(__name__)
 
 
 @unique
 class ExecuteOperation(Enum):
     """
```

### Comparing `vdk-control-cli-1.3.826524239/src/vdk/internal/control/command_groups/job/list.py` & `vdk-control-cli-1.3.829999004/src/vdk/internal/control/command_groups/job/list.py`

 * *Files 6% similar despite different names*

```diff
@@ -12,15 +12,15 @@
 from tabulate import tabulate
 from taurus_datajob_api import DataJobQueryResponse
 from vdk.internal.control.configuration.defaults_config import load_default_team_name
 from vdk.internal.control.rest_lib.factory import ApiClientFactory
 from vdk.internal.control.rest_lib.rest_client_errors import ApiClientErrorDecorator
 from vdk.internal.control.utils import cli_utils
 from vdk.internal.control.utils.cli_utils import GqlQueryBuilder
-from vdk.internal.control.utils.cli_utils import OutputFormat
+from vdk.internal.control.utils.output_printer import OutputFormat
 
 log = logging.getLogger(__name__)
 
 
 class JobList:
     def __init__(self, rest_api_url: str):
         self.jobs_api = ApiClientFactory(rest_api_url).get_jobs_api()
@@ -88,14 +88,20 @@
                 res["last_deployment_status"] = deployments[0]["status"]
             if "jobVersion" in deployments[0]:
                 res["job_version"] = deployments[0]["jobVersion"]
             if "lastDeployedBy" in deployments[0]:
                 res["deployed_by"] = deployments[0]["lastDeployedBy"]
             if "lastDeployedDate" in deployments[0]:
                 res["deployed_date"] = deployments[0]["lastDeployedDate"]
+            if "executions" in deployments[0] and len(deployments[0]["executions"]) > 0:
+                last_execution = deployments[0]["executions"][0]
+                res["last_execution_status"] = last_execution.get("status")
+                res["last_execution_date"] = last_execution.get("startTime")
+                res["last_execution_type"] = last_execution.get("type")
+                res["last_execution_started_by"] = last_execution.get("startedBy")
         else:
             res["status"] = "NOT_DEPLOYED"
         if "contacts" in job["config"]:
             contacts = job["config"]["contacts"]
             if "notifiedOnJobSuccess" in contacts:
                 res["notified_on_success"] = contacts["notifiedOnJobSuccess"]
             if "notifiedOnJobFailureUserError" in contacts:
@@ -153,14 +159,19 @@
             )
 
         if more_details >= 2:
             job_contacts = jobs_config.add_return_new("contacts")
             job_contacts.add("notifiedOnJobDeploy").add("notifiedOnJobSuccess").add(
                 "notifiedOnJobFailurePlatformError"
             ).add("notifiedOnJobFailureUserError")
+        if more_details >= 3:
+            executions = jobs_deployments.add_return_new("executions")
+            executions.add("id").add("type").add("status").add("startTime").add(
+                "endTime"
+            ).add("opId").add("startedBy")
 
         query = jobs_builder.build()
         log.debug("Jobs list (graphql) query: " + query)
         return query
 
 
 # Below is the definition of the CLI API/UX users will be interacting
```

### Comparing `vdk-control-cli-1.3.826524239/src/vdk/internal/control/command_groups/job/properties.py` & `vdk-control-cli-1.3.829999004/src/vdk/internal/control/command_groups/job/properties.py`

 * *Files 0% similar despite different names*

```diff
@@ -13,15 +13,15 @@
 import click
 from tabulate import tabulate
 from vdk.internal.control.configuration.defaults_config import load_default_team_name
 from vdk.internal.control.exception.vdk_exception import VDKException
 from vdk.internal.control.rest_lib.factory import ApiClientFactory
 from vdk.internal.control.rest_lib.rest_client_errors import ApiClientErrorDecorator
 from vdk.internal.control.utils import cli_utils
-from vdk.internal.control.utils.cli_utils import OutputFormat
+from vdk.internal.control.utils.output_printer import OutputFormat
 
 log = logging.getLogger(__name__)
 
 
 @unique
 class PropertyOperation(Enum):
     """
```

### Comparing `vdk-control-cli-1.3.826524239/src/vdk/internal/control/command_groups/job/show.py` & `vdk-control-cli-1.3.829999004/src/vdk/internal/control/command_groups/job/show.py`

 * *Files 12% similar despite different names*

```diff
@@ -10,15 +10,15 @@
 from taurus_datajob_api import DataJobDeploymentStatus
 from taurus_datajob_api import DataJobExecution
 from vdk.internal.control.configuration.defaults_config import load_default_team_name
 from vdk.internal.control.exception.vdk_exception import VDKException
 from vdk.internal.control.rest_lib.factory import ApiClientFactory
 from vdk.internal.control.rest_lib.rest_client_errors import ApiClientErrorDecorator
 from vdk.internal.control.utils import cli_utils
-from vdk.internal.control.utils.cli_utils import OutputFormat
+from vdk.internal.control.utils.output_printer import json_format
 
 log = logging.getLogger(__name__)
 
 
 class JobShow:
     def __init__(self, rest_api_url: str, output: str):
         self.jobs_api = ApiClientFactory(rest_api_url).get_jobs_api()
@@ -53,15 +53,15 @@
         deployments = self.__read_deployments(job_name, team)
         executions = self.__read_executions(job_name, team)
 
         job_as_dict = job.to_dict()
         job_as_dict["deployments"] = list(map(lambda d: d.to_dict(), deployments))
         job_as_dict["executions"] = list(map(lambda e: e.to_dict(), executions))[:2]
 
-        click.echo(cli_utils.json_format(job_as_dict, indent=2))
+        click.echo(json_format(job_as_dict, indent=2))
 
 
 @click.command(
     name="show",
     help="Show data job definition deployments if any and recent (2) executions. "
     "The format of the data is same one as returned by backend API."
     """
```

### Comparing `vdk-control-cli-1.3.826524239/src/vdk/internal/control/command_groups/login_group/login.py` & `vdk-control-cli-1.3.829999004/src/vdk/internal/control/command_groups/login_group/login.py`

 * *Files identical despite different names*

### Comparing `vdk-control-cli-1.3.826524239/src/vdk/internal/control/configuration/defaults_config.py` & `vdk-control-cli-1.3.829999004/src/vdk/internal/control/configuration/defaults_config.py`

 * *Files identical despite different names*

### Comparing `vdk-control-cli-1.3.826524239/src/vdk/internal/control/configuration/log_config.py` & `vdk-control-cli-1.3.829999004/src/vdk/internal/control/configuration/log_config.py`

 * *Files identical despite different names*

### Comparing `vdk-control-cli-1.3.826524239/src/vdk/internal/control/configuration/vdk_config.py` & `vdk-control-cli-1.3.829999004/src/vdk/internal/control/configuration/vdk_config.py`

 * *Files identical despite different names*

### Comparing `vdk-control-cli-1.3.826524239/src/vdk/internal/control/exception/vdk_exception.py` & `vdk-control-cli-1.3.829999004/src/vdk/internal/control/exception/vdk_exception.py`

 * *Files identical despite different names*

### Comparing `vdk-control-cli-1.3.826524239/src/vdk/internal/control/job/job_archive.py` & `vdk-control-cli-1.3.829999004/src/vdk/internal/control/job/job_archive.py`

 * *Files identical despite different names*

### Comparing `vdk-control-cli-1.3.826524239/src/vdk/internal/control/job/job_config.py` & `vdk-control-cli-1.3.829999004/src/vdk/internal/control/job/job_config.py`

 * *Files identical despite different names*

### Comparing `vdk-control-cli-1.3.826524239/src/vdk/internal/control/job/sample_job/10_sql_step.sql` & `vdk-control-cli-1.3.829999004/src/vdk/internal/control/job/sample_job/10_sql_step.sql`

 * *Files identical despite different names*

### Comparing `vdk-control-cli-1.3.826524239/src/vdk/internal/control/job/sample_job/20_python_step.py` & `vdk-control-cli-1.3.829999004/src/vdk/internal/control/job/sample_job/20_python_step.py`

 * *Files identical despite different names*

### Comparing `vdk-control-cli-1.3.826524239/src/vdk/internal/control/job/sample_job/README.md` & `vdk-control-cli-1.3.829999004/src/vdk/internal/control/job/sample_job/README.md`

 * *Files identical despite different names*

### Comparing `vdk-control-cli-1.3.826524239/src/vdk/internal/control/job/sample_job/config.ini` & `vdk-control-cli-1.3.829999004/src/vdk/internal/control/job/sample_job/config.ini`

 * *Files identical despite different names*

### Comparing `vdk-control-cli-1.3.826524239/src/vdk/internal/control/main.py` & `vdk-control-cli-1.3.829999004/src/vdk/internal/control/main.py`

 * *Files identical despite different names*

### Comparing `vdk-control-cli-1.3.826524239/src/vdk/internal/control/plugin/control_plugin_manager.py` & `vdk-control-cli-1.3.829999004/src/vdk/internal/control/plugin/control_plugin_manager.py`

 * *Files identical despite different names*

### Comparing `vdk-control-cli-1.3.826524239/src/vdk/internal/control/rest_lib/factory.py` & `vdk-control-cli-1.3.829999004/src/vdk/internal/control/rest_lib/factory.py`

 * *Files identical despite different names*

### Comparing `vdk-control-cli-1.3.826524239/src/vdk/internal/control/rest_lib/rest_client_errors.py` & `vdk-control-cli-1.3.829999004/src/vdk/internal/control/rest_lib/rest_client_errors.py`

 * *Files identical despite different names*

### Comparing `vdk-control-cli-1.3.826524239/src/vdk/internal/control/utils/cli_utils.py` & `vdk-control-cli-1.3.829999004/src/vdk/internal/control/utils/cli_utils.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,25 +1,22 @@
 # Copyright 2021-2023 VMware, Inc.
 # SPDX-License-Identifier: Apache-2.0
 from __future__ import annotations
 
 import functools
-import json
 import logging
 import os
 import shutil
 from dataclasses import dataclass
-from enum import Enum
-from enum import unique
 
 import click
 from vdk.internal.control.configuration.defaults_config import load_default_rest_api_url
 from vdk.internal.control.configuration.vdk_config import VDKConfig
 from vdk.internal.control.exception.vdk_exception import VDKException
-
+from vdk.internal.control.utils import output_printer
 
 log = logging.getLogger(__name__)
 
 
 def get_or_prompt(option_description, option_value, default_value=None):
     if not option_value:
         option_value = click.prompt(option_description, default=default_value)
@@ -92,59 +89,39 @@
         check_rest_api_url(rest_api_url)
 
         return f(*args, **kwargs)
 
     return check
 
 
-@unique
-class OutputFormat(str, Enum):
-    """
-    An enum used to specify the output formatting of a command.
-    """
-
-    TEXT = "TEXT"
-    JSON = "JSON"
-
-
 def output_option(*names, **kwargs):
     """
     A decorator that adds an `--output, -o` option to the decorated command.
     Name can be configured through ``*names``. Keyword arguments are passed to
     the underlying ``click.option`` decorator.
     """
     if not names:
         names = ["--output", "-o"]
 
     def decorator(f):
         return click.option(
             *names,
-            type=click.Choice([e.value for e in OutputFormat], case_sensitive=False),
-            default=OutputFormat.TEXT.value,
+            type=click.Choice(
+                [e.upper() for e in output_printer._registered_printers.keys()],
+                case_sensitive=False,
+            ),
+            default="text",
             cls=extended_option(hide_if_default=True),
             help="The desirable format of the result. Supported formats include text and json.",
             **kwargs,
         )(f)
 
     return decorator
 
 
-def json_format(data, indent=None):
-    from datetime import date, datetime
-
-    def json_serial(obj):
-        """JSON serializer for objects not serializable by default json code"""
-
-        if isinstance(obj, (datetime, date)):
-            return obj.isoformat()
-        raise TypeError("Type %s not serializable" % type(obj))
-
-    return json.dumps(data, default=json_serial, indent=indent)
-
-
 def copy_directory(src, dst):
     if not os.path.exists(dst):
         os.makedirs(dst)
     for item in os.listdir(src):
         source_file = os.path.join(src, item)
         dest_file = os.path.join(dst, item)
         if os.path.isfile(source_file):
```

### Comparing `vdk-control-cli-1.3.826524239/src/vdk/internal/control/utils/control_utils.py` & `vdk-control-cli-1.3.829999004/src/vdk/internal/control/utils/control_utils.py`

 * *Files identical despite different names*

### Comparing `vdk-control-cli-1.3.826524239/src/vdk/internal/control/utils/version_utils.py` & `vdk-control-cli-1.3.829999004/src/vdk/internal/control/utils/version_utils.py`

 * *Files identical despite different names*

### Comparing `vdk-control-cli-1.3.826524239/src/vdk_control_cli.egg-info/PKG-INFO` & `vdk-control-cli-1.3.829999004/src/vdk_control_cli.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: vdk-control-cli
-Version: 1.3.826524239
+Version: 1.3.829999004
 Summary: VDK Control CLI allows user to create, delete, manage and their Data Jobs in Kubernetes runtime.
 Home-page: https://github.com/vmware/versatile-data-kit
 Author: VMware Inc.
 Author-email: aivanov@vmware.com
 Project-URL: Documentation, https://github.com/vmware/versatile-data-kit/wiki
 Project-URL: Source, https://github.com/vmware/versatile-data-kit/projects/vdk-control-cli
 Platform: any
```

### Comparing `vdk-control-cli-1.3.826524239/src/vdk_control_cli.egg-info/SOURCES.txt` & `vdk-control-cli-1.3.829999004/src/vdk_control_cli.egg-info/SOURCES.txt`

 * *Files 4% similar despite different names*

```diff
@@ -34,14 +34,15 @@
 src/vdk/internal/control/job/sample_job/config.ini
 src/vdk/internal/control/job/sample_job/requirements.txt
 src/vdk/internal/control/plugin/control_plugin_manager.py
 src/vdk/internal/control/rest_lib/factory.py
 src/vdk/internal/control/rest_lib/rest_client_errors.py
 src/vdk/internal/control/utils/cli_utils.py
 src/vdk/internal/control/utils/control_utils.py
+src/vdk/internal/control/utils/output_printer.py
 src/vdk/internal/control/utils/version_utils.py
 src/vdk_control_cli.egg-info/PKG-INFO
 src/vdk_control_cli.egg-info/SOURCES.txt
 src/vdk_control_cli.egg-info/dependency_links.txt
 src/vdk_control_cli.egg-info/entry_points.txt
 src/vdk_control_cli.egg-info/not-zip-safe
 src/vdk_control_cli.egg-info/requires.txt
```

