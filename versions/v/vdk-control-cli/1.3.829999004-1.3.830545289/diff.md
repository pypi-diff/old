# Comparing `tmp/vdk-control-cli-1.3.829999004.tar.gz` & `tmp/vdk-control-cli-1.3.830545289.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/vdk-control-cli-1.3.829999004.tar", last modified: Thu Apr  6 11:02:22 2023, max compression
+gzip compressed data, was "dist/vdk-control-cli-1.3.830545289.tar", last modified: Thu Apr  6 19:53:26 2023, max compression
```

## Comparing `vdk-control-cli-1.3.829999004.tar` & `vdk-control-cli-1.3.830545289.tar`

### file list

```diff
@@ -1,72 +1,72 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 11:02:22.000000 vdk-control-cli-1.3.829999004/
--rw-rw-rw-   0 root         (0) root         (0)      270 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/MANIFEST.in
--rw-r--r--   0 root         (0) root         (0)     5153 2023-04-06 11:02:22.000000 vdk-control-cli-1.3.829999004/PKG-INFO
--rw-rw-rw-   0 root         (0) root         (0)     4192 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/README.md
--rw-rw-rw-   0 root         (0) root         (0)     1746 2023-04-06 11:02:22.000000 vdk-control-cli-1.3.829999004/setup.cfg
--rw-rw-rw-   0 root         (0) root         (0)      460 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/setup.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 11:02:22.000000 vdk-control-cli-1.3.829999004/src/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 11:02:22.000000 vdk-control-cli-1.3.829999004/src/vdk/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 11:02:22.000000 vdk-control-cli-1.3.829999004/src/vdk/api/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 11:02:22.000000 vdk-control-cli-1.3.829999004/src/vdk/api/control/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 11:02:22.000000 vdk-control-cli-1.3.829999004/src/vdk/api/control/plugin/
--rw-rw-rw-   0 root         (0) root         (0)      717 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/src/vdk/api/control/plugin/markers.py
--rw-rw-rw-   0 root         (0) root         (0)     1423 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/src/vdk/api/control/plugin/specs.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 11:02:22.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 11:02:22.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 11:02:22.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/command_groups/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 11:02:22.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/command_groups/common_group/
--rw-rw-rw-   0 root         (0) root         (0)     2284 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/command_groups/common_group/default.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 11:02:22.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/command_groups/job/
--rw-rw-rw-   0 root         (0) root         (0)    11236 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/command_groups/job/create.py
--rw-rw-rw-   0 root         (0) root         (0)     2121 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/command_groups/job/delete.py
--rw-rw-rw-   0 root         (0) root         (0)     7183 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/command_groups/job/deploy_cli.py
--rw-rw-rw-   0 root         (0) root         (0)    13882 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/command_groups/job/deploy_cli_impl.py
--rw-rw-rw-   0 root         (0) root         (0)     5115 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/command_groups/job/download_job.py
--rw-rw-rw-   0 root         (0) root         (0)     2673 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/command_groups/job/download_key.py
--rw-rw-rw-   0 root         (0) root         (0)    12146 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/command_groups/job/execute.py
--rw-rw-rw-   0 root         (0) root         (0)     8970 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/command_groups/job/list.py
--rw-rw-rw-   0 root         (0) root         (0)    12264 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/command_groups/job/properties.py
--rw-rw-rw-   0 root         (0) root         (0)     3375 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/command_groups/job/show.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 11:02:22.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/command_groups/login_group/
--rw-rw-rw-   0 root         (0) root         (0)     6510 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/command_groups/login_group/login.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 11:02:22.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/command_groups/logout_group/
--rw-rw-rw-   0 root         (0) root         (0)      410 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/command_groups/logout_group/logout.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 11:02:22.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/command_groups/version_group/
--rw-rw-rw-   0 root         (0) root         (0)      371 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/command_groups/version_group/version.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 11:02:22.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/configuration/
--rw-rw-rw-   0 root         (0) root         (0)      424 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/configuration/default_options.py
--rw-rw-rw-   0 root         (0) root         (0)     1221 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/configuration/defaults_config.py
--rw-rw-rw-   0 root         (0) root         (0)     2272 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/configuration/log_config.py
--rw-rw-rw-   0 root         (0) root         (0)     9834 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/configuration/vdk_config.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 11:02:22.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/exception/
--rw-rw-rw-   0 root         (0) root         (0)      649 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/exception/vdk_exception.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 11:02:22.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/job/
--rw-rw-rw-   0 root         (0) root         (0)     1930 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/job/job_archive.py
--rw-rw-rw-   0 root         (0) root         (0)     4768 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/job/job_config.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 11:02:22.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/job/sample_job/
--rw-rw-rw-   0 root         (0) root         (0)      579 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/job/sample_job/10_sql_step.sql
--rw-rw-rw-   0 root         (0) root         (0)      816 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/job/sample_job/20_python_step.py
--rw-rw-rw-   0 root         (0) root         (0)     1446 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/job/sample_job/README.md
--rw-rw-rw-   0 root         (0) root         (0)     2902 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/job/sample_job/config.ini
--rw-rw-rw-   0 root         (0) root         (0)      243 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/job/sample_job/requirements.txt
--rw-rw-rw-   0 root         (0) root         (0)     3458 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/main.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 11:02:22.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/plugin/
--rw-rw-rw-   0 root         (0) root         (0)     3715 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/plugin/control_plugin_manager.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 11:02:22.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/rest_lib/
--rw-rw-rw-   0 root         (0) root         (0)     2915 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/rest_lib/factory.py
--rw-rw-rw-   0 root         (0) root         (0)     3845 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/rest_lib/rest_client_errors.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 11:02:22.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/utils/
--rw-rw-rw-   0 root         (0) root         (0)     7297 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/utils/cli_utils.py
--rw-rw-rw-   0 root         (0) root         (0)     1413 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/utils/control_utils.py
--rw-rw-rw-   0 root         (0) root         (0)     3690 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/utils/output_printer.py
--rw-rw-rw-   0 root         (0) root         (0)      819 2023-04-06 11:02:06.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/utils/version_utils.py
--rw-rw-rw-   0 root         (0) root         (0)      181 2023-04-06 11:02:10.000000 vdk-control-cli-1.3.829999004/src/vdk/internal/control/vdk_control_build_info.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 11:02:22.000000 vdk-control-cli-1.3.829999004/src/vdk_control_cli.egg-info/
--rw-r--r--   0 root         (0) root         (0)     5153 2023-04-06 11:02:22.000000 vdk-control-cli-1.3.829999004/src/vdk_control_cli.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)     2312 2023-04-06 11:02:22.000000 vdk-control-cli-1.3.829999004/src/vdk_control_cli.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2023-04-06 11:02:22.000000 vdk-control-cli-1.3.829999004/src/vdk_control_cli.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)       57 2023-04-06 11:02:22.000000 vdk-control-cli-1.3.829999004/src/vdk_control_cli.egg-info/entry_points.txt
--rw-r--r--   0 root         (0) root         (0)        1 2023-04-06 11:02:22.000000 vdk-control-cli-1.3.829999004/src/vdk_control_cli.egg-info/not-zip-safe
--rw-r--r--   0 root         (0) root         (0)      184 2023-04-06 11:02:22.000000 vdk-control-cli-1.3.829999004/src/vdk_control_cli.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)        4 2023-04-06 11:02:22.000000 vdk-control-cli-1.3.829999004/src/vdk_control_cli.egg-info/top_level.txt
--rw-rw-rw-   0 root         (0) root         (0)       14 2023-04-06 11:02:10.000000 vdk-control-cli-1.3.829999004/version.txt
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 19:53:26.000000 vdk-control-cli-1.3.830545289/
+-rw-rw-rw-   0 root         (0) root         (0)      270 2023-04-06 19:53:07.000000 vdk-control-cli-1.3.830545289/MANIFEST.in
+-rw-r--r--   0 root         (0) root         (0)     5153 2023-04-06 19:53:26.000000 vdk-control-cli-1.3.830545289/PKG-INFO
+-rw-rw-rw-   0 root         (0) root         (0)     4192 2023-04-06 19:53:07.000000 vdk-control-cli-1.3.830545289/README.md
+-rw-rw-rw-   0 root         (0) root         (0)     1746 2023-04-06 19:53:26.000000 vdk-control-cli-1.3.830545289/setup.cfg
+-rw-rw-rw-   0 root         (0) root         (0)      460 2023-04-06 19:53:07.000000 vdk-control-cli-1.3.830545289/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 19:53:26.000000 vdk-control-cli-1.3.830545289/src/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 19:53:26.000000 vdk-control-cli-1.3.830545289/src/vdk/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 19:53:26.000000 vdk-control-cli-1.3.830545289/src/vdk/api/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 19:53:26.000000 vdk-control-cli-1.3.830545289/src/vdk/api/control/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 19:53:26.000000 vdk-control-cli-1.3.830545289/src/vdk/api/control/plugin/
+-rw-rw-rw-   0 root         (0) root         (0)      717 2023-04-06 19:53:07.000000 vdk-control-cli-1.3.830545289/src/vdk/api/control/plugin/markers.py
+-rw-rw-rw-   0 root         (0) root         (0)     1423 2023-04-06 19:53:07.000000 vdk-control-cli-1.3.830545289/src/vdk/api/control/plugin/specs.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 19:53:26.000000 vdk-control-cli-1.3.830545289/src/vdk/internal/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 19:53:26.000000 vdk-control-cli-1.3.830545289/src/vdk/internal/control/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 19:53:26.000000 vdk-control-cli-1.3.830545289/src/vdk/internal/control/command_groups/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 19:53:26.000000 vdk-control-cli-1.3.830545289/src/vdk/internal/control/command_groups/common_group/
+-rw-rw-rw-   0 root         (0) root         (0)     2284 2023-04-06 19:53:07.000000 vdk-control-cli-1.3.830545289/src/vdk/internal/control/command_groups/common_group/default.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 19:53:26.000000 vdk-control-cli-1.3.830545289/src/vdk/internal/control/command_groups/job/
+-rw-rw-rw-   0 root         (0) root         (0)    11236 2023-04-06 19:53:07.000000 vdk-control-cli-1.3.830545289/src/vdk/internal/control/command_groups/job/create.py
+-rw-rw-rw-   0 root         (0) root         (0)     2121 2023-04-06 19:53:07.000000 vdk-control-cli-1.3.830545289/src/vdk/internal/control/command_groups/job/delete.py
+-rw-rw-rw-   0 root         (0) root         (0)     7121 2023-04-06 19:53:07.000000 vdk-control-cli-1.3.830545289/src/vdk/internal/control/command_groups/job/deploy_cli.py
+-rw-rw-rw-   0 root         (0) root         (0)    13891 2023-04-06 19:53:07.000000 vdk-control-cli-1.3.830545289/src/vdk/internal/control/command_groups/job/deploy_cli_impl.py
+-rw-rw-rw-   0 root         (0) root         (0)     5115 2023-04-06 19:53:07.000000 vdk-control-cli-1.3.830545289/src/vdk/internal/control/command_groups/job/download_job.py
+-rw-rw-rw-   0 root         (0) root         (0)     2673 2023-04-06 19:53:07.000000 vdk-control-cli-1.3.830545289/src/vdk/internal/control/command_groups/job/download_key.py
+-rw-rw-rw-   0 root         (0) root         (0)    12088 2023-04-06 19:53:07.000000 vdk-control-cli-1.3.830545289/src/vdk/internal/control/command_groups/job/execute.py
+-rw-rw-rw-   0 root         (0) root         (0)     8735 2023-04-06 19:53:07.000000 vdk-control-cli-1.3.830545289/src/vdk/internal/control/command_groups/job/list.py
+-rw-rw-rw-   0 root         (0) root         (0)    12040 2023-04-06 19:53:07.000000 vdk-control-cli-1.3.830545289/src/vdk/internal/control/command_groups/job/properties.py
+-rw-rw-rw-   0 root         (0) root         (0)     3403 2023-04-06 19:53:07.000000 vdk-control-cli-1.3.830545289/src/vdk/internal/control/command_groups/job/show.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 19:53:26.000000 vdk-control-cli-1.3.830545289/src/vdk/internal/control/command_groups/login_group/
+-rw-rw-rw-   0 root         (0) root         (0)     6510 2023-04-06 19:53:07.000000 vdk-control-cli-1.3.830545289/src/vdk/internal/control/command_groups/login_group/login.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 19:53:26.000000 vdk-control-cli-1.3.830545289/src/vdk/internal/control/command_groups/logout_group/
+-rw-rw-rw-   0 root         (0) root         (0)      410 2023-04-06 19:53:07.000000 vdk-control-cli-1.3.830545289/src/vdk/internal/control/command_groups/logout_group/logout.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 19:53:26.000000 vdk-control-cli-1.3.830545289/src/vdk/internal/control/command_groups/version_group/
+-rw-rw-rw-   0 root         (0) root         (0)      772 2023-04-06 19:53:07.000000 vdk-control-cli-1.3.830545289/src/vdk/internal/control/command_groups/version_group/version.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 19:53:26.000000 vdk-control-cli-1.3.830545289/src/vdk/internal/control/configuration/
+-rw-rw-rw-   0 root         (0) root         (0)      424 2023-04-06 19:53:07.000000 vdk-control-cli-1.3.830545289/src/vdk/internal/control/configuration/default_options.py
+-rw-rw-rw-   0 root         (0) root         (0)     1221 2023-04-06 19:53:07.000000 vdk-control-cli-1.3.830545289/src/vdk/internal/control/configuration/defaults_config.py
+-rw-rw-rw-   0 root         (0) root         (0)     2272 2023-04-06 19:53:07.000000 vdk-control-cli-1.3.830545289/src/vdk/internal/control/configuration/log_config.py
+-rw-rw-rw-   0 root         (0) root         (0)     9834 2023-04-06 19:53:07.000000 vdk-control-cli-1.3.830545289/src/vdk/internal/control/configuration/vdk_config.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 19:53:26.000000 vdk-control-cli-1.3.830545289/src/vdk/internal/control/exception/
+-rw-rw-rw-   0 root         (0) root         (0)      649 2023-04-06 19:53:07.000000 vdk-control-cli-1.3.830545289/src/vdk/internal/control/exception/vdk_exception.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 19:53:26.000000 vdk-control-cli-1.3.830545289/src/vdk/internal/control/job/
+-rw-rw-rw-   0 root         (0) root         (0)     1930 2023-04-06 19:53:07.000000 vdk-control-cli-1.3.830545289/src/vdk/internal/control/job/job_archive.py
+-rw-rw-rw-   0 root         (0) root         (0)     4768 2023-04-06 19:53:07.000000 vdk-control-cli-1.3.830545289/src/vdk/internal/control/job/job_config.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 19:53:26.000000 vdk-control-cli-1.3.830545289/src/vdk/internal/control/job/sample_job/
+-rw-rw-rw-   0 root         (0) root         (0)      579 2023-04-06 19:53:07.000000 vdk-control-cli-1.3.830545289/src/vdk/internal/control/job/sample_job/10_sql_step.sql
+-rw-rw-rw-   0 root         (0) root         (0)      816 2023-04-06 19:53:07.000000 vdk-control-cli-1.3.830545289/src/vdk/internal/control/job/sample_job/20_python_step.py
+-rw-rw-rw-   0 root         (0) root         (0)     1446 2023-04-06 19:53:07.000000 vdk-control-cli-1.3.830545289/src/vdk/internal/control/job/sample_job/README.md
+-rw-rw-rw-   0 root         (0) root         (0)     2902 2023-04-06 19:53:07.000000 vdk-control-cli-1.3.830545289/src/vdk/internal/control/job/sample_job/config.ini
+-rw-rw-rw-   0 root         (0) root         (0)      243 2023-04-06 19:53:07.000000 vdk-control-cli-1.3.830545289/src/vdk/internal/control/job/sample_job/requirements.txt
+-rw-rw-rw-   0 root         (0) root         (0)     3458 2023-04-06 19:53:07.000000 vdk-control-cli-1.3.830545289/src/vdk/internal/control/main.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 19:53:26.000000 vdk-control-cli-1.3.830545289/src/vdk/internal/control/plugin/
+-rw-rw-rw-   0 root         (0) root         (0)     3715 2023-04-06 19:53:07.000000 vdk-control-cli-1.3.830545289/src/vdk/internal/control/plugin/control_plugin_manager.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 19:53:26.000000 vdk-control-cli-1.3.830545289/src/vdk/internal/control/rest_lib/
+-rw-rw-rw-   0 root         (0) root         (0)     2915 2023-04-06 19:53:07.000000 vdk-control-cli-1.3.830545289/src/vdk/internal/control/rest_lib/factory.py
+-rw-rw-rw-   0 root         (0) root         (0)     3845 2023-04-06 19:53:07.000000 vdk-control-cli-1.3.830545289/src/vdk/internal/control/rest_lib/rest_client_errors.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 19:53:26.000000 vdk-control-cli-1.3.830545289/src/vdk/internal/control/utils/
+-rw-rw-rw-   0 root         (0) root         (0)     7297 2023-04-06 19:53:07.000000 vdk-control-cli-1.3.830545289/src/vdk/internal/control/utils/cli_utils.py
+-rw-rw-rw-   0 root         (0) root         (0)     1413 2023-04-06 19:53:07.000000 vdk-control-cli-1.3.830545289/src/vdk/internal/control/utils/control_utils.py
+-rw-rw-rw-   0 root         (0) root         (0)     3690 2023-04-06 19:53:07.000000 vdk-control-cli-1.3.830545289/src/vdk/internal/control/utils/output_printer.py
+-rw-rw-rw-   0 root         (0) root         (0)      819 2023-04-06 19:53:07.000000 vdk-control-cli-1.3.830545289/src/vdk/internal/control/utils/version_utils.py
+-rw-rw-rw-   0 root         (0) root         (0)      181 2023-04-06 19:53:11.000000 vdk-control-cli-1.3.830545289/src/vdk/internal/control/vdk_control_build_info.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 19:53:26.000000 vdk-control-cli-1.3.830545289/src/vdk_control_cli.egg-info/
+-rw-r--r--   0 root         (0) root         (0)     5153 2023-04-06 19:53:25.000000 vdk-control-cli-1.3.830545289/src/vdk_control_cli.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)     2312 2023-04-06 19:53:26.000000 vdk-control-cli-1.3.830545289/src/vdk_control_cli.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2023-04-06 19:53:25.000000 vdk-control-cli-1.3.830545289/src/vdk_control_cli.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)       57 2023-04-06 19:53:25.000000 vdk-control-cli-1.3.830545289/src/vdk_control_cli.egg-info/entry_points.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2023-04-06 19:53:25.000000 vdk-control-cli-1.3.830545289/src/vdk_control_cli.egg-info/not-zip-safe
+-rw-r--r--   0 root         (0) root         (0)      184 2023-04-06 19:53:25.000000 vdk-control-cli-1.3.830545289/src/vdk_control_cli.egg-info/requires.txt
+-rw-r--r--   0 root         (0) root         (0)        4 2023-04-06 19:53:25.000000 vdk-control-cli-1.3.830545289/src/vdk_control_cli.egg-info/top_level.txt
+-rw-rw-rw-   0 root         (0) root         (0)       14 2023-04-06 19:53:11.000000 vdk-control-cli-1.3.830545289/version.txt
```

### Comparing `vdk-control-cli-1.3.829999004/PKG-INFO` & `vdk-control-cli-1.3.830545289/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: vdk-control-cli
-Version: 1.3.829999004
+Version: 1.3.830545289
 Summary: VDK Control CLI allows user to create, delete, manage and their Data Jobs in Kubernetes runtime.
 Home-page: https://github.com/vmware/versatile-data-kit
 Author: VMware Inc.
 Author-email: aivanov@vmware.com
 Project-URL: Documentation, https://github.com/vmware/versatile-data-kit/wiki
 Project-URL: Source, https://github.com/vmware/versatile-data-kit/projects/vdk-control-cli
 Platform: any
```

### Comparing `vdk-control-cli-1.3.829999004/README.md` & `vdk-control-cli-1.3.830545289/README.md`

 * *Files identical despite different names*

### Comparing `vdk-control-cli-1.3.829999004/setup.cfg` & `vdk-control-cli-1.3.830545289/setup.cfg`

 * *Files identical despite different names*

### Comparing `vdk-control-cli-1.3.829999004/src/vdk/api/control/plugin/markers.py` & `vdk-control-cli-1.3.830545289/src/vdk/api/control/plugin/markers.py`

 * *Files identical despite different names*

### Comparing `vdk-control-cli-1.3.829999004/src/vdk/api/control/plugin/specs.py` & `vdk-control-cli-1.3.830545289/src/vdk/api/control/plugin/specs.py`

 * *Files identical despite different names*

### Comparing `vdk-control-cli-1.3.829999004/src/vdk/internal/control/command_groups/common_group/default.py` & `vdk-control-cli-1.3.830545289/src/vdk/internal/control/command_groups/common_group/default.py`

 * *Files identical despite different names*

### Comparing `vdk-control-cli-1.3.829999004/src/vdk/internal/control/command_groups/job/create.py` & `vdk-control-cli-1.3.830545289/src/vdk/internal/control/command_groups/job/create.py`

 * *Files identical despite different names*

### Comparing `vdk-control-cli-1.3.829999004/src/vdk/internal/control/command_groups/job/delete.py` & `vdk-control-cli-1.3.830545289/src/vdk/internal/control/command_groups/job/delete.py`

 * *Files identical despite different names*

### Comparing `vdk-control-cli-1.3.829999004/src/vdk/internal/control/command_groups/job/deploy_cli.py` & `vdk-control-cli-1.3.830545289/src/vdk/internal/control/command_groups/job/deploy_cli.py`

 * *Files 1% similar despite different names*

```diff
@@ -174,26 +174,24 @@
         name = get_or_prompt("Job Name", name)
         team = get_or_prompt("Job Team", team)
         # default to ask for job version to update
         if not vdk_version and not job_version and enabled is None:
             job_version = get_or_prompt("Job Version", job_version)
         if job_path:
             reason = get_or_prompt("Reason", reason)
-            return cmd.create(
-                name, team, job_path, reason, output, vdk_version, enabled
-            )
+            return cmd.create(name, team, job_path, reason, vdk_version, enabled)
         else:
-            return cmd.update(name, team, enabled, job_version, vdk_version, output)
+            return cmd.update(name, team, enabled, job_version, vdk_version)
     if operation == DeployOperation.REMOVE.value:
         name = get_or_prompt("Job Name", name)
         team = get_or_prompt("Job Team", team)
         return cmd.remove(name, team)
     if operation == DeployOperation.SHOW.value:
         name = get_or_prompt("Job Name", name)
         team = get_or_prompt("Job Team", team)
-        return cmd.show(name, team, output)
+        return cmd.show(name, team)
     if operation == DeployOperation.CREATE.value:
         job_path = get_or_prompt("Job Path", job_path)
         default_name = os.path.basename(job_path)
         name = get_or_prompt("Job Name", name, default_name)
         reason = get_or_prompt("Reason", reason)
-        return cmd.create(name, team, job_path, reason, output, vdk_version, enabled)
+        return cmd.create(name, team, job_path, reason, vdk_version, enabled)
```

### Comparing `vdk-control-cli-1.3.829999004/src/vdk/internal/control/command_groups/job/deploy_cli_impl.py` & `vdk-control-cli-1.3.830545289/src/vdk/internal/control/command_groups/job/deploy_cli_impl.py`

 * *Files 7% similar despite different names*

```diff
@@ -1,48 +1,49 @@
 # Copyright 2021-2023 VMware, Inc.
 # SPDX-License-Identifier: Apache-2.0
 import glob
-import json
 import logging
 import os
 from typing import Optional
 
 import click
 import click_spinner
-from tabulate import tabulate
 from taurus_datajob_api import ApiException
 from taurus_datajob_api import DataJob
 from taurus_datajob_api import DataJobConfig
 from taurus_datajob_api import DataJobContacts
 from taurus_datajob_api import DataJobDeployment
 from taurus_datajob_api import DataJobSchedule
 from vdk.internal.control.configuration.defaults_config import load_default_team_name
 from vdk.internal.control.exception.vdk_exception import VDKException
 from vdk.internal.control.job.job_archive import JobArchive
 from vdk.internal.control.job.job_config import JobConfig
 from vdk.internal.control.rest_lib.factory import ApiClientFactory
 from vdk.internal.control.rest_lib.rest_client_errors import ApiClientErrorDecorator
+from vdk.internal.control.utils import output_printer
 from vdk.internal.control.utils.cli_utils import get_or_prompt
 from vdk.internal.control.utils.output_printer import OutputFormat
 
 log = logging.getLogger(__name__)
 
 
 class JobDeploy:
     ZIP_ARCHIVE_TYPE = "zip"
     ARCHIVE_SUFFIX = "-archive"
 
-    def __init__(self, rest_api_url: str, output):
+    def __init__(self, rest_api_url: str, output_format: str):
         self.deploy_api = ApiClientFactory(rest_api_url).get_deploy_api()
         self.jobs_api = ApiClientFactory(rest_api_url).get_jobs_api()
         self.job_sources_api = ApiClientFactory(rest_api_url).get_jobs_sources_api()
         # support for multiple deployments is not implemented yet so we can put anything here.
         # Ultimately this will be user facing parameter (possibly fetched from config.ini)
         self.__deployment_id = "production"
         self.__job_archive = JobArchive()
+        self.__output_format = output_format
+        self.__printer = output_printer.create_printer(self.__output_format)
 
     @staticmethod
     def __detect_keytab_files_in_job_directory(job_path: str) -> None:
         keytab_glob = os.path.join(job_path, "**/*.keytab")
         keytab_files = glob.glob(keytab_glob, recursive=True)
         if keytab_files:
             raise VDKException(
@@ -149,25 +150,24 @@
     def update(
         self,
         name: str,
         team: str,
         enabled: Optional[bool],  # true, false or None
         job_version: Optional[str],
         vdk_version: Optional[str],
-        output: str,
     ) -> None:
         deployment = DataJobDeployment(enabled=None)
         if job_version:
             deployment.job_version = job_version
         if vdk_version:
             deployment.vdk_version = vdk_version
         deployment.enabled = enabled
 
         if job_version:
-            self.__update_job_version(name, team, deployment, output)
+            self.__update_job_version(name, team, deployment)
         elif vdk_version or enabled is not None:
             self.__update_deployment(name, team, deployment)
             msg = f"Deployment of Data Job {name} updated; "
             if vdk_version:
                 msg = msg + f"vdk version: {vdk_version}; "
             if enabled is not None:
                 msg = msg + "status: " + ("enabled" if enabled else "disabled") + "; "
@@ -182,50 +182,48 @@
         self.deploy_api.deployment_patch(
             team_name=team,
             job_name=name,
             deployment_id=self.__deployment_id,
             data_job_deployment=deployment,
         )
 
-    def __update_job_version(
-        self, name: str, team: str, deployment: DataJobDeployment, output: str
-    ):
+    def __update_job_version(self, name: str, team: str, deployment: DataJobDeployment):
         log.debug(
             f"Update Deployment version of a job {name} of team {team} : {deployment}"
         )
         self.deploy_api.deployment_update(
             team_name=team, job_name=name, data_job_deployment=deployment
         )
-        if output == OutputFormat.TEXT.value:
+        if self.__output_format == OutputFormat.TEXT.value:
             log.info(
                 f"Request to deploy Data Job {name} using version {deployment.job_version} finished successfully.\n"
                 f"It would take a few minutes for the Data Job to be deployed in the server.\n"
                 f"If notified_on_job_deploy option in config.ini is configured then "
                 f"notification will be sent on successful deploy or in case of an error.\n\n"
                 f"You can also execute `vdk deploy --show -t '{team}' -n '{name}'` and compare the printed version "
                 f"to the one of the newly deployed job - {deployment.job_version} - to verify that the deployment "
                 f"was successful."
             )
         else:
             result = {
                 "job_name": name,
                 "job_version": deployment.job_version,
             }
-            click.echo(json.dumps(result))
+            self.__printer.print_dict(result)
 
     @ApiClientErrorDecorator()
     def remove(self, name: str, team: str) -> None:
         log.debug(f"Remove Deployment of a job {name} of team {team}")
         self.deploy_api.deployment_delete(
             team_name=team, job_name=name, deployment_id=self.__deployment_id
         )
         log.info(f"Deployment of Data Job {name} removed.")
 
     @ApiClientErrorDecorator()
-    def show(self, name: str, team: str, output: str) -> None:
+    def show(self, name: str, team: str) -> None:
         log.debug(f"Get list of deployments for job {name} of team {team} ")
         deployments = self.deploy_api.deployment_list(team_name=team, job_name=name)
         log.debug(
             f"Found following deployments for job {name} of team {team} : {deployments}"
         )
         if deployments:
             # d.to_dict() brings unnecessary parts of data
@@ -235,37 +233,33 @@
                     job_version=d.job_version,
                     last_deployed_by=d.last_deployed_by,
                     last_deployed_date=d.last_deployed_date,
                     enabled=d.enabled,
                 ),
                 deployments,
             )
-            if output == OutputFormat.TEXT.value:
+            if self.__output_format == OutputFormat.TEXT.value:
                 click.echo(
                     "You can compare the version seen here to the one seen when "
                     "deploying to verify your deployment was successful."
                 )
                 click.echo("")
-                click.echo(tabulate(deployments, headers="keys"))
+                self.__printer.print_table(list(deployments))
             else:
-                click.echo(json.dumps(list(deployments)))
+                self.__printer.print_table(list(deployments))
         else:
-            if output == OutputFormat.TEXT.value:
-                click.echo("No deployments.")
-            else:
-                click.echo(json.dumps([]))
+            self.__printer.print_table(None)
 
     @ApiClientErrorDecorator()
     def create(
         self,
         name: str,
         team: str,
         job_path: str,
         reason: str,
-        output: str,
         vdk_version: Optional[str],
         enabled: Optional[bool],
     ) -> None:
         log.debug(
             f"Create Deployment of a job {name} of team {team} with local path {job_path} and reason {reason}"
         )
         job_path = os.path.abspath(job_path)
@@ -283,34 +277,34 @@
         job_config = JobConfig(job_path)
 
         self.__validate_datajob(job_path=job_path, job_config=job_config, team=team)
         team = get_or_prompt(
             "Team Name", team or job_config.get_team() or load_default_team_name()
         )
 
-        if output == OutputFormat.TEXT.value:
+        if self.__output_format == OutputFormat.TEXT.value:
             log.info(
                 f"Deploy Data Job with name {name} from directory {job_path} ... \n"
             )
 
         archive_path = self.__job_archive.archive_data_job(
             job_name=name, job_archive_path=job_path
         )
         try:
             job_archive_binary = self.__archive_binary(archive_path)
 
-            if output == OutputFormat.TEXT.value:
+            if self.__output_format == OutputFormat.TEXT.value:
                 log.info("Uploading the data job might take some time ...")
-            with click_spinner.spinner(disable=(output == OutputFormat.JSON.value)):
+            with click_spinner.spinner(
+                disable=(self.__output_format == OutputFormat.JSON.value)
+            ):
                 data_job_version = self.job_sources_api.sources_upload(
                     team_name=team,
                     job_name=name,
                     body=job_archive_binary,
                     reason=reason,
                 )
 
             self.__update_data_job_deploy_configuration(job_path, name, team)
-            self.update(
-                name, team, enabled, data_job_version.version_sha, vdk_version, output
-            )
+            self.update(name, team, enabled, data_job_version.version_sha, vdk_version)
         finally:
             self.__cleanup_archive(archive_path=archive_path)
```

### Comparing `vdk-control-cli-1.3.829999004/src/vdk/internal/control/command_groups/job/download_job.py` & `vdk-control-cli-1.3.830545289/src/vdk/internal/control/command_groups/job/download_job.py`

 * *Files identical despite different names*

### Comparing `vdk-control-cli-1.3.829999004/src/vdk/internal/control/command_groups/job/download_key.py` & `vdk-control-cli-1.3.830545289/src/vdk/internal/control/command_groups/job/download_key.py`

 * *Files identical despite different names*

### Comparing `vdk-control-cli-1.3.829999004/src/vdk/internal/control/command_groups/job/execute.py` & `vdk-control-cli-1.3.830545289/src/vdk/internal/control/command_groups/job/execute.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,30 +1,30 @@
 # Copyright 2021-2023 VMware, Inc.
 # SPDX-License-Identifier: Apache-2.0
 import json
 import logging
 import operator
 import os
-import sys
 import webbrowser
 from enum import Enum
 from enum import unique
+from typing import List
 from typing import Optional
 
 import click
 import click_spinner
-from tabulate import tabulate
 from taurus_datajob_api import DataJobExecution
 from taurus_datajob_api import DataJobExecutionLogs
 from taurus_datajob_api import DataJobExecutionRequest
 from vdk.internal.control.configuration.defaults_config import load_default_team_name
 from vdk.internal.control.exception.vdk_exception import VDKException
 from vdk.internal.control.rest_lib.factory import ApiClientFactory
 from vdk.internal.control.rest_lib.rest_client_errors import ApiClientErrorDecorator
 from vdk.internal.control.utils import cli_utils
+from vdk.internal.control.utils import output_printer
 from vdk.internal.control.utils.cli_utils import get_or_prompt
 from vdk.internal.control.utils.output_printer import OutputFormat
 
 log = logging.getLogger(__name__)
 
 
 @unique
@@ -42,27 +42,23 @@
 
 
 class JobExecute:
     def __init__(self, rest_api_url: str):
         self.__execution_api = ApiClientFactory(rest_api_url).get_execution_api()
 
     @staticmethod
-    def __model_executions(executions, output: OutputFormat) -> str:
+    def __model_executions(executions, output_format: OutputFormat) -> str:
         def transform_execution(e: DataJobExecution):
             d = e.to_dict()
             d["job_version"] = e.deployment.job_version
             del d["deployment"]
             return d
 
         executions = list(map(lambda e: transform_execution(e), executions))
-
-        if output == OutputFormat.TEXT.value:
-            return tabulate(executions, headers="keys")
-        elif output == OutputFormat.JSON.value:
-            return cli_utils.json_format(list(executions))
+        output_printer.create_printer(output_format).print_table(executions)
 
     @staticmethod
     def __validate_and_parse_args(arguments: str) -> str:
         try:
             if arguments:
                 return json.loads(arguments)
             else:
@@ -73,15 +69,17 @@
                 why=str(e),
                 consequence="I will not make the API call.",
                 countermeasure="Make sure provided --arguments is a valid JSON string.",
             )
             raise vdk_ex
 
     @ApiClientErrorDecorator()
-    def start(self, name: str, team: str, output: OutputFormat, arguments: str) -> None:
+    def start(
+        self, name: str, team: str, output_format: OutputFormat, arguments: str
+    ) -> None:
         execution_request = DataJobExecutionRequest(
             started_by=f"vdk-control-cli",
             args=self.__validate_and_parse_args(arguments),
         )
         log.debug(f"Starting job with request {execution_request}")
         _, _, headers = self.__execution_api.data_job_execution_start_with_http_info(
             team_name=team,
@@ -89,55 +87,55 @@
             deployment_id="production",  # TODO
             data_job_execution_request=execution_request,
         )
         log.debug(f"Received headers: {headers}")
 
         location = headers["Location"]
         execution_id = os.path.basename(location)
-        if output == OutputFormat.TEXT.value:
+        if output_format == OutputFormat.TEXT.value:
             click.echo(
                 f"Execution of Data Job {name} started. "
                 f"See execution status using: \n\n"
                 f"vdk execute --show --execution-id {execution_id} -n {name} -t {team}\n\n"
                 f"See execution logs using: \n\n"
                 f"vdk execute --logs --execution-id {execution_id} -n {name} -t {team}"
             )
-        elif output == OutputFormat.JSON.value:
+        else:
             result = {
                 "job_name": name,
                 "team": team,
                 "execution_id": execution_id,
             }
-            click.echo(json.dumps(result))
+            output_printer.create_printer(output_format).print_dict(result)
 
     @ApiClientErrorDecorator()
     def cancel(self, name: str, team: str, execution_id: str) -> None:
         click.echo("Cancelling data job execution. Might take some time...")
         with click_spinner.spinner():
             response = self.__execution_api.data_job_execution_cancel(
                 team_name=team, job_name=name, execution_id=execution_id
             )
             log.debug(f"Response: {response}")
         click.echo("Job cancelled successfully.")
 
     @ApiClientErrorDecorator()
     def show(
-        self, name: str, team: str, execution_id: str, output: OutputFormat
+        self, name: str, team: str, execution_id: str, output_format: OutputFormat
     ) -> None:
         execution: DataJobExecution = self.__execution_api.data_job_execution_read(
             team_name=team, job_name=name, execution_id=execution_id
         )
-        click.echo(self.__model_executions([execution], output))
+        self.__model_executions([execution], output_format)
 
     @ApiClientErrorDecorator()
-    def list(self, name: str, team: str, output: OutputFormat) -> None:
-        executions: list[
+    def list(self, name: str, team: str, output_format: OutputFormat) -> None:
+        executions: List[
             DataJobExecution
         ] = self.__execution_api.data_job_execution_list(team_name=team, job_name=name)
-        click.echo(self.__model_executions(executions, output))
+        self.__model_executions(executions, output_format)
 
     def __get_execution_to_log(
         self, name: str, team: str, execution_id: str
     ) -> Optional[DataJobExecution]:
         if not execution_id:
             executions: list[
                 DataJobExecution
```

### Comparing `vdk-control-cli-1.3.829999004/src/vdk/internal/control/command_groups/job/list.py` & `vdk-control-cli-1.3.830545289/src/vdk/internal/control/command_groups/job/list.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,37 +1,35 @@
 # Copyright 2021-2023 VMware, Inc.
 # SPDX-License-Identifier: Apache-2.0
 import datetime
-import json
 import logging
 from enum import Enum
 from enum import unique
 from typing import Dict
 from typing import List
 
 import click
-from tabulate import tabulate
 from taurus_datajob_api import DataJobQueryResponse
 from vdk.internal.control.configuration.defaults_config import load_default_team_name
 from vdk.internal.control.rest_lib.factory import ApiClientFactory
 from vdk.internal.control.rest_lib.rest_client_errors import ApiClientErrorDecorator
 from vdk.internal.control.utils import cli_utils
+from vdk.internal.control.utils import output_printer
 from vdk.internal.control.utils.cli_utils import GqlQueryBuilder
-from vdk.internal.control.utils.output_printer import OutputFormat
 
 log = logging.getLogger(__name__)
 
 
 class JobList:
     def __init__(self, rest_api_url: str):
         self.jobs_api = ApiClientFactory(rest_api_url).get_jobs_api()
 
     @ApiClientErrorDecorator()
     def list_jobs(
-        self, team: str, jobs_for_all_teams: bool, more_details: int, output: str
+        self, team: str, jobs_for_all_teams: bool, more_details: int, output_format: str
     ):
         has_more_jobs = True
         page_number = 1
         page_size = 100
 
         jobs = []
 
@@ -51,21 +49,15 @@
             if next_page and len(next_page) > 0:
                 jobs.extend(next_page)
             if len(next_page) < page_size:
                 has_more_jobs = False
             page_number += 1
 
         jobs = list(map(self.job_to_dict, jobs))
-        if output == OutputFormat.TEXT.value:
-            if len(jobs) > 0:
-                click.echo(tabulate(jobs, headers="keys"))
-            else:
-                click.echo("No Data Jobs.")
-        else:
-            click.echo(json.dumps(list(jobs)))
+        output_printer.create_printer(output_format).print_table(jobs)
 
     @staticmethod
     def job_to_dict(job: Dict):
         # TODO: response model should come from open api client
         res = dict(
             job_name=job["jobName"],
             job_team=job["config"]["team"],
```

### Comparing `vdk-control-cli-1.3.829999004/src/vdk/internal/control/command_groups/job/properties.py` & `vdk-control-cli-1.3.830545289/src/vdk/internal/control/command_groups/job/properties.py`

 * *Files 4% similar despite different names*

```diff
@@ -7,20 +7,20 @@
 from enum import unique
 from typing import Any
 from typing import Dict
 from typing import Tuple
 from typing import Type
 
 import click
-from tabulate import tabulate
 from vdk.internal.control.configuration.defaults_config import load_default_team_name
 from vdk.internal.control.exception.vdk_exception import VDKException
 from vdk.internal.control.rest_lib.factory import ApiClientFactory
 from vdk.internal.control.rest_lib.rest_client_errors import ApiClientErrorDecorator
 from vdk.internal.control.utils import cli_utils
+from vdk.internal.control.utils import output_printer
 from vdk.internal.control.utils.output_printer import OutputFormat
 
 log = logging.getLogger(__name__)
 
 
 @unique
 class PropertyOperation(Enum):
@@ -35,42 +35,32 @@
 
 class JobProperties:
     def __init__(
         self,
         rest_api_url: str,
         job_name: str,
         team: str,
-        output: OutputFormat,
+        output_format: OutputFormat,
     ):
-        self.properties_api = ApiClientFactory(rest_api_url).get_properties_api()
-        self.output = output
-        self.job_name = job_name
-        self.team = team
-        self.deployment_id = "TODO"
+        self.__properties_api = ApiClientFactory(rest_api_url).get_properties_api()
+        self.__output = output_format
+        self.__printer = output_printer.create_printer(output_format)
+        self.__job_name = job_name
+        self.__team = team
+        self.__deployment_id = "TODO"
 
     def __get_all_remote_properties(self) -> Dict[str, Any]:
-        return self.properties_api.data_job_properties_read(
-            team_name=self.team,
-            job_name=self.job_name,
-            deployment_id=self.deployment_id,
+        return self.__properties_api.data_job_properties_read(
+            team_name=self.__team,
+            job_name=self.__job_name,
+            deployment_id=self.__deployment_id,
         )
 
     def __list_properties(self, remote_props: Dict[str, Any]) -> None:
-        if self.output == OutputFormat.TEXT.value:
-            if len(remote_props) > 0:
-                click.echo(
-                    tabulate(
-                        [[k, v] for k, v in remote_props.items()],
-                        headers=("key", "value"),
-                    )
-                )
-            else:
-                click.echo("No properties.")
-        else:
-            click.echo(json.dumps(remote_props))
+        self.__printer.print_dict(remote_props)
 
     @staticmethod
     def _to_bool(value: str) -> bool:
         if value == "true" or value == "True":
             return True
         if value == "false" or value == "False":
             return False
@@ -134,48 +124,48 @@
         remote_props = self.__get_all_remote_properties()
         self.__list_properties(remote_props)
 
     @ApiClientErrorDecorator()
     def update_properties(self, new_properties: Dict[str, str]) -> None:
         remote_props = self.__get_all_remote_properties()
         merged_props = self.__merge_props(new_properties, remote_props)
-        self.properties_api.data_job_properties_update(
-            team_name=self.team,
-            job_name=self.job_name,
-            deployment_id=self.deployment_id,
+        self.__properties_api.data_job_properties_update(
+            team_name=self.__team,
+            job_name=self.__job_name,
+            deployment_id=self.__deployment_id,
             request_body=merged_props,
         )
 
     @ApiClientErrorDecorator()
     def overwrite_properties(self, new_properties: Dict[str, str]) -> None:
-        self.properties_api.data_job_properties_update(
-            team_name=self.team,
-            job_name=self.job_name,
-            deployment_id=self.deployment_id,
+        self.__properties_api.data_job_properties_update(
+            team_name=self.__team,
+            job_name=self.__job_name,
+            deployment_id=self.__deployment_id,
             request_body=new_properties,
         )
 
     @ApiClientErrorDecorator()
     def delete_keys(self, delete_keys: Tuple[str]) -> None:
         props = self.__get_all_remote_properties()
         for key in delete_keys:
             props.pop(key)
-        self.properties_api.data_job_properties_update(
-            team_name=self.team,
-            job_name=self.job_name,
-            deployment_id=self.deployment_id,
+        self.__properties_api.data_job_properties_update(
+            team_name=self.__team,
+            job_name=self.__job_name,
+            deployment_id=self.__deployment_id,
             request_body=props,
         )
 
     @ApiClientErrorDecorator()
     def delete_all_job_properties(self) -> None:
-        self.properties_api.data_job_properties_update(
-            team_name=self.team,
-            job_name=self.job_name,
-            deployment_id=self.deployment_id,
+        self.__properties_api.data_job_properties_update(
+            team_name=self.__team,
+            job_name=self.__job_name,
+            deployment_id=self.__deployment_id,
             request_body={},
         )
 
 
 # Below is the definition of the CLI API/UX users will be interacting
 # Above is the actual implementation of the operations
```

### Comparing `vdk-control-cli-1.3.829999004/src/vdk/internal/control/command_groups/job/show.py` & `vdk-control-cli-1.3.830545289/src/vdk/internal/control/command_groups/job/show.py`

 * *Files 7% similar despite different names*

```diff
@@ -1,67 +1,66 @@
 # Copyright 2021-2023 VMware, Inc.
 # SPDX-License-Identifier: Apache-2.0
-import json
 import logging
 from typing import List
 
 import click
 from taurus_datajob_api import ApiException
 from taurus_datajob_api import DataJob
 from taurus_datajob_api import DataJobDeploymentStatus
 from taurus_datajob_api import DataJobExecution
 from vdk.internal.control.configuration.defaults_config import load_default_team_name
 from vdk.internal.control.exception.vdk_exception import VDKException
 from vdk.internal.control.rest_lib.factory import ApiClientFactory
 from vdk.internal.control.rest_lib.rest_client_errors import ApiClientErrorDecorator
 from vdk.internal.control.utils import cli_utils
-from vdk.internal.control.utils.output_printer import json_format
+from vdk.internal.control.utils import output_printer
 
 log = logging.getLogger(__name__)
 
 
 class JobShow:
-    def __init__(self, rest_api_url: str, output: str):
-        self.jobs_api = ApiClientFactory(rest_api_url).get_jobs_api()
-        self.deploy_api = ApiClientFactory(rest_api_url).get_deploy_api()
-        self.execution_api = ApiClientFactory(rest_api_url).get_execution_api()
-        self.output = output
+    def __init__(self, rest_api_url: str, output_format: str):
+        self.__jobs_api = ApiClientFactory(rest_api_url).get_jobs_api()
+        self.__deploy_api = ApiClientFactory(rest_api_url).get_deploy_api()
+        self.__execution_api = ApiClientFactory(rest_api_url).get_execution_api()
+        self.__printer = output_printer.create_printer(output_format)
 
     def __read_data_job(self, name: str, team: str) -> DataJob:
         try:
-            return self.jobs_api.data_job_read(team_name=team, job_name=name)
+            return self.__jobs_api.data_job_read(team_name=team, job_name=name)
         except ApiException as e:
             raise VDKException(
                 what=f"Cannot find data job {name}",
                 why="Data job does not exist on CLOUD.",
                 consequence="Cannot show job details.",
                 countermeasure="Use VDK CLI create command to create the job first.",
             ) from e
 
     def __read_deployments(
         self, job_name: str, team: str
     ) -> List[DataJobDeploymentStatus]:
-        return self.deploy_api.deployment_list(team_name=team, job_name=job_name)
+        return self.__deploy_api.deployment_list(team_name=team, job_name=job_name)
 
     def __read_executions(self, job_name: str, team: str) -> List[DataJobExecution]:
-        return self.execution_api.data_job_execution_list(
+        return self.__execution_api.data_job_execution_list(
             team_name=team, job_name=job_name
         )
 
     @ApiClientErrorDecorator()
     def show_job(self, job_name: str, team: str) -> None:
         job = self.__read_data_job(job_name, team)
         deployments = self.__read_deployments(job_name, team)
         executions = self.__read_executions(job_name, team)
 
         job_as_dict = job.to_dict()
         job_as_dict["deployments"] = list(map(lambda d: d.to_dict(), deployments))
         job_as_dict["executions"] = list(map(lambda e: e.to_dict(), executions))[:2]
 
-        click.echo(json_format(job_as_dict, indent=2))
+        self.__printer.print_dict(job_as_dict)
 
 
 @click.command(
     name="show",
     help="Show data job definition deployments if any and recent (2) executions. "
     "The format of the data is same one as returned by backend API."
     """
```

### Comparing `vdk-control-cli-1.3.829999004/src/vdk/internal/control/command_groups/login_group/login.py` & `vdk-control-cli-1.3.830545289/src/vdk/internal/control/command_groups/login_group/login.py`

 * *Files identical despite different names*

### Comparing `vdk-control-cli-1.3.829999004/src/vdk/internal/control/configuration/defaults_config.py` & `vdk-control-cli-1.3.830545289/src/vdk/internal/control/configuration/defaults_config.py`

 * *Files identical despite different names*

### Comparing `vdk-control-cli-1.3.829999004/src/vdk/internal/control/configuration/log_config.py` & `vdk-control-cli-1.3.830545289/src/vdk/internal/control/configuration/log_config.py`

 * *Files identical despite different names*

### Comparing `vdk-control-cli-1.3.829999004/src/vdk/internal/control/configuration/vdk_config.py` & `vdk-control-cli-1.3.830545289/src/vdk/internal/control/configuration/vdk_config.py`

 * *Files identical despite different names*

### Comparing `vdk-control-cli-1.3.829999004/src/vdk/internal/control/exception/vdk_exception.py` & `vdk-control-cli-1.3.830545289/src/vdk/internal/control/exception/vdk_exception.py`

 * *Files identical despite different names*

### Comparing `vdk-control-cli-1.3.829999004/src/vdk/internal/control/job/job_archive.py` & `vdk-control-cli-1.3.830545289/src/vdk/internal/control/job/job_archive.py`

 * *Files identical despite different names*

### Comparing `vdk-control-cli-1.3.829999004/src/vdk/internal/control/job/job_config.py` & `vdk-control-cli-1.3.830545289/src/vdk/internal/control/job/job_config.py`

 * *Files identical despite different names*

### Comparing `vdk-control-cli-1.3.829999004/src/vdk/internal/control/job/sample_job/10_sql_step.sql` & `vdk-control-cli-1.3.830545289/src/vdk/internal/control/job/sample_job/10_sql_step.sql`

 * *Files identical despite different names*

### Comparing `vdk-control-cli-1.3.829999004/src/vdk/internal/control/job/sample_job/20_python_step.py` & `vdk-control-cli-1.3.830545289/src/vdk/internal/control/job/sample_job/20_python_step.py`

 * *Files identical despite different names*

### Comparing `vdk-control-cli-1.3.829999004/src/vdk/internal/control/job/sample_job/README.md` & `vdk-control-cli-1.3.830545289/src/vdk/internal/control/job/sample_job/README.md`

 * *Files identical despite different names*

### Comparing `vdk-control-cli-1.3.829999004/src/vdk/internal/control/job/sample_job/config.ini` & `vdk-control-cli-1.3.830545289/src/vdk/internal/control/job/sample_job/config.ini`

 * *Files identical despite different names*

### Comparing `vdk-control-cli-1.3.829999004/src/vdk/internal/control/main.py` & `vdk-control-cli-1.3.830545289/src/vdk/internal/control/main.py`

 * *Files identical despite different names*

### Comparing `vdk-control-cli-1.3.829999004/src/vdk/internal/control/plugin/control_plugin_manager.py` & `vdk-control-cli-1.3.830545289/src/vdk/internal/control/plugin/control_plugin_manager.py`

 * *Files identical despite different names*

### Comparing `vdk-control-cli-1.3.829999004/src/vdk/internal/control/rest_lib/factory.py` & `vdk-control-cli-1.3.830545289/src/vdk/internal/control/rest_lib/factory.py`

 * *Files identical despite different names*

### Comparing `vdk-control-cli-1.3.829999004/src/vdk/internal/control/rest_lib/rest_client_errors.py` & `vdk-control-cli-1.3.830545289/src/vdk/internal/control/rest_lib/rest_client_errors.py`

 * *Files identical despite different names*

### Comparing `vdk-control-cli-1.3.829999004/src/vdk/internal/control/utils/cli_utils.py` & `vdk-control-cli-1.3.830545289/src/vdk/internal/control/utils/cli_utils.py`

 * *Files identical despite different names*

### Comparing `vdk-control-cli-1.3.829999004/src/vdk/internal/control/utils/control_utils.py` & `vdk-control-cli-1.3.830545289/src/vdk/internal/control/utils/control_utils.py`

 * *Files identical despite different names*

### Comparing `vdk-control-cli-1.3.829999004/src/vdk/internal/control/utils/output_printer.py` & `vdk-control-cli-1.3.830545289/src/vdk/internal/control/utils/output_printer.py`

 * *Files identical despite different names*

### Comparing `vdk-control-cli-1.3.829999004/src/vdk/internal/control/utils/version_utils.py` & `vdk-control-cli-1.3.830545289/src/vdk/internal/control/utils/version_utils.py`

 * *Files identical despite different names*

### Comparing `vdk-control-cli-1.3.829999004/src/vdk_control_cli.egg-info/PKG-INFO` & `vdk-control-cli-1.3.830545289/src/vdk_control_cli.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: vdk-control-cli
-Version: 1.3.829999004
+Version: 1.3.830545289
 Summary: VDK Control CLI allows user to create, delete, manage and their Data Jobs in Kubernetes runtime.
 Home-page: https://github.com/vmware/versatile-data-kit
 Author: VMware Inc.
 Author-email: aivanov@vmware.com
 Project-URL: Documentation, https://github.com/vmware/versatile-data-kit/wiki
 Project-URL: Source, https://github.com/vmware/versatile-data-kit/projects/vdk-control-cli
 Platform: any
```

### Comparing `vdk-control-cli-1.3.829999004/src/vdk_control_cli.egg-info/SOURCES.txt` & `vdk-control-cli-1.3.830545289/src/vdk_control_cli.egg-info/SOURCES.txt`

 * *Files identical despite different names*

