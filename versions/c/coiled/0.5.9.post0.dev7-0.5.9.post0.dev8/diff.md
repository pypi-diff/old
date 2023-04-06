# Comparing `tmp/coiled-0.5.9.post0.dev7.tar.gz` & `tmp/coiled-0.5.9.post0.dev8.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "coiled-0.5.9.post0.dev7.tar", last modified: Thu Mar 30 16:24:51 2023, max compression
+gzip compressed data, was "coiled-0.5.9.post0.dev8.tar", last modified: Thu Mar 30 19:46:07 2023, max compression
```

## Comparing `coiled-0.5.9.post0.dev7.tar` & `coiled-0.5.9.post0.dev8.tar`

### file list

```diff
@@ -1,270 +1,270 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 16:24:51.660891 coiled-0.5.9.post0.dev7/
--rw-r--r--   0 runner    (1001) docker     (123)     1524 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)      327 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     1076 2023-03-30 16:24:51.660891 coiled-0.5.9.post0.dev7/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      848 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 16:24:51.660891 coiled-0.5.9.post0.dev7/coiled/
--rw-r--r--   0 runner    (1001) docker     (123)     2158 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/coiled/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 16:24:51.612890 coiled-0.5.9.post0.dev7/coiled/_beta/
--rw-r--r--   0 runner    (1001) docker     (123)      501 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/coiled/_beta/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    80134 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/coiled/_beta/cluster.py
--rw-r--r--   0 runner    (1001) docker     (123)    60251 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/coiled/_beta/core.py
--rw-r--r--   0 runner    (1001) docker     (123)     1895 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/coiled/_beta/cwi_log_link.py
--rw-r--r--   0 runner    (1001) docker     (123)     7937 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/coiled/_beta/states.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 16:24:51.612890 coiled-0.5.9.post0.dev7/coiled/_beta/widgets/
--rw-r--r--   0 runner    (1001) docker     (123)     1011 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/coiled/_beta/widgets/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    15129 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/coiled/_beta/widgets/rich.py
--rw-r--r--   0 runner    (1001) docker     (123)     2608 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/coiled/_beta/widgets/util.py
--rw-r--r--   0 runner    (1001) docker     (123)      508 2023-03-30 16:24:51.660891 coiled-0.5.9.post0.dev7/coiled/_version.py
--rw-r--r--   0 runner    (1001) docker     (123)     7188 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/coiled/analytics.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 16:24:51.612890 coiled-0.5.9.post0.dev7/coiled/cli/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/coiled/cli/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 16:24:51.612890 coiled-0.5.9.post0.dev7/coiled/cli/cluster/
--rw-r--r--   0 runner    (1001) docker     (123)      526 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/coiled/cli/cluster/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    11190 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/coiled/cli/cluster/better_logs.py
--rw-r--r--   0 runner    (1001) docker     (123)     6474 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/coiled/cli/cluster/logs.py
--rw-r--r--   0 runner    (1001) docker     (123)     4693 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/coiled/cli/cluster/ssh.py
--rw-r--r--   0 runner    (1001) docker     (123)      714 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/coiled/cli/core.py
--rw-r--r--   0 runner    (1001) docker     (123)      992 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/coiled/cli/curl.py
--rw-r--r--   0 runner    (1001) docker     (123)      394 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/coiled/cli/diagnostics.py
--rw-r--r--   0 runner    (1001) docker     (123)     5942 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/coiled/cli/env.py
--rw-r--r--   0 runner    (1001) docker     (123)      716 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/coiled/cli/login.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 16:24:51.616890 coiled-0.5.9.post0.dev7/coiled/cli/notebook/
--rw-r--r--   0 runner    (1001) docker     (123)      916 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/coiled/cli/notebook/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    11211 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/coiled/cli/notebook/notebook.py
--rw-r--r--   0 runner    (1001) docker     (123)     2675 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/coiled/cli/package_sync.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 16:24:51.616890 coiled-0.5.9.post0.dev7/coiled/cli/setup/
--rw-r--r--   0 runner    (1001) docker     (123)      766 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/coiled/cli/setup/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4321 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/coiled/cli/setup/amp.py
--rw-r--r--   0 runner    (1001) docker     (123)    43611 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/coiled/cli/setup/aws.py
--rw-r--r--   0 runner    (1001) docker     (123)     2643 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/coiled/cli/setup/entry.py
--rw-r--r--   0 runner    (1001) docker     (123)    25966 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/coiled/cli/setup/gcp.py
--rw-r--r--   0 runner    (1001) docker     (123)     2076 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/coiled/cli/setup/prometheus.py
--rw-r--r--   0 runner    (1001) docker     (123)      160 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/coiled/cli/setup/util.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 16:24:51.616890 coiled-0.5.9.post0.dev7/coiled/cli/tests/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/coiled/cli/tests/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      261 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/coiled/cli/tests/test_core.py
--rw-r--r--   0 runner    (1001) docker     (123)      482 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/coiled/cli/tests/test_diagnostics.py
--rw-r--r--   0 runner    (1001) docker     (123)     3241 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/coiled/cli/tests/test_env.py
--rw-r--r--   0 runner    (1001) docker     (123)     4386 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/coiled/cli/tests/test_login.py
--rw-r--r--   0 runner    (1001) docker     (123)     1752 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/coiled/cli/utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     1170 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/coiled/cluster.py
--rw-r--r--   0 runner    (1001) docker     (123)      842 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/coiled/coiled.yaml
--rw-r--r--   0 runner    (1001) docker     (123)      284 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/coiled/compatibility.py
--rw-r--r--   0 runner    (1001) docker     (123)      189 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/coiled/config.py
--rw-r--r--   0 runner    (1001) docker     (123)     3427 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/coiled/context.py
--rw-r--r--   0 runner    (1001) docker     (123)   110704 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/coiled/core.py
--rw-r--r--   0 runner    (1001) docker     (123)      305 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/coiled/errors.py
--rw-r--r--   0 runner    (1001) docker     (123)     2926 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/coiled/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)    17261 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/coiled/magic.py
--rw-r--r--   0 runner    (1001) docker     (123)    12271 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/coiled/scan.py
--rw-r--r--   0 runner    (1001) docker     (123)     3984 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/coiled/software.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 16:24:51.616890 coiled-0.5.9.post0.dev7/coiled/tests/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/coiled/tests/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    29802 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/coiled/tests/test_core.py
--rw-r--r--   0 runner    (1001) docker     (123)     2354 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/coiled/tests/test_exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)     3249 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/coiled/tests/test_manage_api_tokens.py
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/coiled/tests/test_package_sync.py
--rw-r--r--   0 runner    (1001) docker     (123)     3601 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/coiled/tests/test_public_configs.py
--rw-r--r--   0 runner    (1001) docker     (123)     4696 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/coiled/tests/test_scan.py
--rw-r--r--   0 runner    (1001) docker     (123)    17096 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/coiled/tests/test_software_environments.py
--rw-r--r--   0 runner    (1001) docker     (123)     2887 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/coiled/tests/test_type_validator.py
--rw-r--r--   0 runner    (1001) docker     (123)    20225 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/coiled/tests/test_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     4307 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/coiled/types.py
--rw-r--r--   0 runner    (1001) docker     (123)    47332 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/coiled/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 16:24:51.616890 coiled-0.5.9.post0.dev7/coiled/v2/
--rw-r--r--   0 runner    (1001) docker     (123)      649 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/coiled/v2/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     7973 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/coiled/websockets.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 16:24:51.612890 coiled-0.5.9.post0.dev7/coiled.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     1076 2023-03-30 16:24:51.000000 coiled-0.5.9.post0.dev7/coiled.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)    10146 2023-03-30 16:24:51.000000 coiled-0.5.9.post0.dev7/coiled.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-30 16:24:51.000000 coiled-0.5.9.post0.dev7/coiled.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       47 2023-03-30 16:24:51.000000 coiled-0.5.9.post0.dev7/coiled.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-30 16:24:42.000000 coiled-0.5.9.post0.dev7/coiled.egg-info/not-zip-safe
--rw-r--r--   0 runner    (1001) docker     (123)      203 2023-03-30 16:24:51.000000 coiled-0.5.9.post0.dev7/coiled.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        7 2023-03-30 16:24:51.000000 coiled-0.5.9.post0.dev7/coiled.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)    20889 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/conftest.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 16:24:51.616890 coiled-0.5.9.post0.dev7/docs/
--rw-r--r--   0 runner    (1001) docker     (123)      654 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/Makefile
--rw-r--r--   0 runner    (1001) docker     (123)      764 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/make.bat
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 16:24:51.616890 coiled-0.5.9.post0.dev7/docs/source/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 16:24:51.620890 coiled-0.5.9.post0.dev7/docs/source/_static/
--rw-r--r--   0 runner    (1001) docker     (123)     1877 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/_static/Coiled-Logo.svg
--rw-r--r--   0 runner    (1001) docker     (123)   293786 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/_static/coiledsnake.png
--rw-r--r--   0 runner    (1001) docker     (123)     9307 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/_static/custom.css
--rw-r--r--   0 runner    (1001) docker     (123)   338221 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/_static/favicon.ico
--rw-r--r--   0 runner    (1001) docker     (123)      593 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/_static/left-arrow.svg
--rw-r--r--   0 runner    (1001) docker     (123)     7053 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/_static/logo-horizontal.svg
--rw-r--r--   0 runner    (1001) docker     (123)     1544 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/_static/logo-solo.svg
--rw-r--r--   0 runner    (1001) docker     (123)     6740 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/_static/logo-vertical.svg
--rw-r--r--   0 runner    (1001) docker     (123)      456 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/_static/note-icon.svg
--rw-r--r--   0 runner    (1001) docker     (123)      585 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/_static/right-arrow.svg
--rw-r--r--   0 runner    (1001) docker     (123)      456 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/_static/tip-icon.svg
--rw-r--r--   0 runner    (1001) docker     (123)      456 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/_static/warning-icon.svg
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 16:24:51.620890 coiled-0.5.9.post0.dev7/docs/source/_templates/
--rw-r--r--   0 runner    (1001) docker     (123)     3657 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/_templates/layout.html
--rw-r--r--   0 runner    (1001) docker     (123)     5772 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/conf.py
--rw-r--r--   0 runner    (1001) docker     (123)      252 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/index.rst
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 16:24:51.628890 coiled-0.5.9.post0.dev7/docs/source/user_guide/
--rw-r--r--   0 runner    (1001) docker     (123)     3009 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/accessing_secure_data.rst
--rw-r--r--   0 runner    (1001) docker     (123)      394 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/analytics-api.rst
--rw-r--r--   0 runner    (1001) docker     (123)     3292 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/analytics-install.rst
--rw-r--r--   0 runner    (1001) docker     (123)     8185 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/analytics-privacy.rst
--rw-r--r--   0 runner    (1001) docker     (123)     2958 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/analytics.rst
--rw-r--r--   0 runner    (1001) docker     (123)     3348 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/api.rst
--rw-r--r--   0 runner    (1001) docker     (123)     1475 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/aws-cli.rst
--rw-r--r--   0 runner    (1001) docker     (123)     8875 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/aws_configure.rst
--rw-r--r--   0 runner    (1001) docker     (123)     9109 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/aws_reference.rst
--rw-r--r--   0 runner    (1001) docker     (123)      501 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/azure_reference.rst
--rw-r--r--   0 runner    (1001) docker     (123)     1517 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/backends.rst
--rw-r--r--   0 runner    (1001) docker     (123)      609 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/best_practices.rst
--rw-r--r--   0 runner    (1001) docker     (123)    34583 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/changelog.rst
--rw-r--r--   0 runner    (1001) docker     (123)     3034 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/choose_cloud_provider.rst
--rw-r--r--   0 runner    (1001) docker     (123)     1477 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/cli_setup.rst
--rw-r--r--   0 runner    (1001) docker     (123)      849 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/cloud-provider-reference.rst
--rw-r--r--   0 runner    (1001) docker     (123)    18340 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/cloud_changelog.rst
--rw-r--r--   0 runner    (1001) docker     (123)    13076 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/cluster_creation.rst
--rw-r--r--   0 runner    (1001) docker     (123)     1558 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/cluster_management.rst
--rw-r--r--   0 runner    (1001) docker     (123)     1134 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/cluster_reuse.rst
--rw-r--r--   0 runner    (1001) docker     (123)     1928 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/cluster_scaling.rst
--rw-r--r--   0 runner    (1001) docker     (123)     4703 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/configuration.rst
--rw-r--r--   0 runner    (1001) docker     (123)     3619 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/docker.rst
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 16:24:51.628890 coiled-0.5.9.post0.dev7/docs/source/user_guide/examples/
--rw-r--r--   0 runner    (1001) docker     (123)    61035 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/examples/dask-optuna-hpo.ipynb
--rw-r--r--   0 runner    (1001) docker     (123)    12606 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/examples/dask-xgboost.ipynb
--rw-r--r--   0 runner    (1001) docker     (123)     5148 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/examples/jupyterlab.ipynb
--rw-r--r--   0 runner    (1001) docker     (123)    15596 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/examples/mongodb.ipynb
--rw-r--r--   0 runner    (1001) docker     (123)    87895 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/examples/parallel-hpo-multi-cluster.ipynb
--rw-r--r--   0 runner    (1001) docker     (123)      677 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/examples/prefect-dask-client.py
--rw-r--r--   0 runner    (1001) docker     (123)      664 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/examples/prefect-dask-task-runner.py
--rw-r--r--   0 runner    (1001) docker     (123)     1078 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/examples/prefect-executor.py
--rw-r--r--   0 runner    (1001) docker     (123)      763 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/examples/prefect-no-runner.py
--rw-r--r--   0 runner    (1001) docker     (123)     1104 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/examples/prefect-task.py
--rw-r--r--   0 runner    (1001) docker     (123)     6703 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/examples/prefect-v2.rst
--rw-r--r--   0 runner    (1001) docker     (123)     7375 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/examples/prefect.rst
--rw-r--r--   0 runner    (1001) docker     (123)    31848 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/examples/study_many_threads.pickle
--rw-r--r--   0 runner    (1001) docker     (123)     2451 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/examples.rst
--rw-r--r--   0 runner    (1001) docker     (123)    10893 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/faq.rst
--rw-r--r--   0 runner    (1001) docker     (123)     2263 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/gcp-cli.rst
--rw-r--r--   0 runner    (1001) docker     (123)    10392 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/gcp_configure.rst
--rw-r--r--   0 runner    (1001) docker     (123)     6243 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/gcp_reference.rst
--rw-r--r--   0 runner    (1001) docker     (123)     5133 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/getting_started.rst
--rw-r--r--   0 runner    (1001) docker     (123)     8100 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/gpu.rst
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 16:24:51.656891 coiled-0.5.9.post0.dev7/docs/source/user_guide/images/
--rw-r--r--   0 runner    (1001) docker     (123)    29164 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/images/account-statistics.png
--rw-r--r--   0 runner    (1001) docker     (123)   246771 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/images/aws-cloudwatch.png
--rw-r--r--   0 runner    (1001) docker     (123)   195084 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/images/aws-tag-editor.png
--rw-r--r--   0 runner    (1001) docker     (123)    48308 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/images/backend-coiled-aws-architecture.png
--rw-r--r--   0 runner    (1001) docker     (123)    36833 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/images/backend-coiled-aws-architecture.svg
--rw-r--r--   0 runner    (1001) docker     (123)   222087 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/images/backend-coiled-aws-vm.png
--rw-r--r--   0 runner    (1001) docker     (123)    79203 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/images/backend-coiled-aws-vm.svg
--rw-r--r--   0 runner    (1001) docker     (123)   232656 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/images/backend-coiled-gcp-vm.png
--rw-r--r--   0 runner    (1001) docker     (123)    80022 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/images/backend-coiled-gcp-vm.svg
--rw-r--r--   0 runner    (1001) docker     (123)   229777 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/images/backend-external-aws-vm.png
--rw-r--r--   0 runner    (1001) docker     (123)    81443 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/images/backend-external-aws-vm.svg
--rw-r--r--   0 runner    (1001) docker     (123)   229181 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/images/backend-external-gcp-vm.png
--rw-r--r--   0 runner    (1001) docker     (123)   277717 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/images/cloud-analytics-clusters.png
--rw-r--r--   0 runner    (1001) docker     (123)   478779 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/images/cloud-analytics-usage.png
--rw-r--r--   0 runner    (1001) docker     (123)    23441 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/images/cloud-backend-browser-aws.png
--rw-r--r--   0 runner    (1001) docker     (123)   129143 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/images/cloud-backend-complete-gcp.gif
--rw-r--r--   0 runner    (1001) docker     (123)   224680 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/images/cloud-backend-complete-slow.gif
--rw-r--r--   0 runner    (1001) docker     (123)   120800 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/images/cloud-backend-flow-gcp.png
--rw-r--r--   0 runner    (1001) docker     (123)    38843 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/images/cloud-backend-keys-aws.png
--rw-r--r--   0 runner    (1001) docker     (123)    47316 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/images/cloud-backend-keys-gcp.png
--rw-r--r--   0 runner    (1001) docker     (123)    34087 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/images/cloud-backend-network.png
--rw-r--r--   0 runner    (1001) docker     (123)    86339 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/images/cloud-backend-provider-aws.png
--rw-r--r--   0 runner    (1001) docker     (123)    93757 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/images/cloud-backend-provider-gcp.png
--rw-r--r--   0 runner    (1001) docker     (123)    31315 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/images/cloud-backend-registry-aws.png
--rw-r--r--   0 runner    (1001) docker     (123)    31740 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/images/cloud-backend-registry-gcp.png
--rw-r--r--   0 runner    (1001) docker     (123)   221648 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/images/cloud-backend-reset.png
--rw-r--r--   0 runner    (1001) docker     (123)    42173 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/images/cloud-backend-review-aws.png
--rw-r--r--   0 runner    (1001) docker     (123)    44403 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/images/cloud-backend-review-gcp.png
--rw-r--r--   0 runner    (1001) docker     (123)    82685 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/images/cloud-backend-start.png
--rw-r--r--   0 runner    (1001) docker     (123)    62482 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/images/cloud-billing-free.png
--rw-r--r--   0 runner    (1001) docker     (123)    74351 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/images/cloud-billing-payg.png
--rw-r--r--   0 runner    (1001) docker     (123)    34848 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/images/cloud-billing-spend-limit.png
--rw-r--r--   0 runner    (1001) docker     (123)    78140 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/images/cloud-cluster-alerts.png
--rw-r--r--   0 runner    (1001) docker     (123)   121085 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/images/cloud-cluster-dashboard.png
--rw-r--r--   0 runner    (1001) docker     (123)   312535 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/images/cloud-cluster-lifecycle.png
--rw-r--r--   0 runner    (1001) docker     (123)   350352 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/images/cloud-cluster-logs.png
--rw-r--r--   0 runner    (1001) docker     (123)    71503 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/images/cloud-cluster-usage.png
--rw-r--r--   0 runner    (1001) docker     (123)    99727 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/images/cluster-profile.png
--rw-r--r--   0 runner    (1001) docker     (123)   428284 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/images/cluster-repr.png
--rw-r--r--   0 runner    (1001) docker     (123)    42601 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/images/cluster-statistics.png
--rw-r--r--   0 runner    (1001) docker     (123)    57582 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/images/cluster-widget-notebook.png
--rw-r--r--   0 runner    (1001) docker     (123)   422843 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/images/clusters-table.png
--rw-r--r--   0 runner    (1001) docker     (123)   410552 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/images/coiled-architecture.png
--rw-r--r--   0 runner    (1001) docker     (123)   110851 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/images/coiled-architecture.svg
--rw-r--r--   0 runner    (1001) docker     (123)   171959 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/images/coiled-prefect-executor.png
--rw-r--r--   0 runner    (1001) docker     (123)   128633 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/images/coiled-prefect-executor.svg
--rw-r--r--   0 runner    (1001) docker     (123)   168887 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/images/coiled-prefect-task.png
--rw-r--r--   0 runner    (1001) docker     (123)   130821 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/images/coiled-prefect-task.svg
--rw-r--r--   0 runner    (1001) docker     (123)   300959 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/images/coiled-profile.png
--rw-r--r--   0 runner    (1001) docker     (123)    36341 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/images/coiled-setup.png
--rw-r--r--   0 runner    (1001) docker     (123)   467848 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/images/coiled-streamlit-example.png
--rw-r--r--   0 runner    (1001) docker     (123)    76347 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/images/coiled-upload-install.svg
--rw-r--r--   0 runner    (1001) docker     (123)   352442 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/images/github-add-token.png
--rw-r--r--   0 runner    (1001) docker     (123)    47899 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/images/jupyterlab-extension.png
--rw-r--r--   0 runner    (1001) docker     (123)     3139 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/images/logo-aws.png
--rw-r--r--   0 runner    (1001) docker     (123)    65865 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/images/logo-gcp.png
--rw-r--r--   0 runner    (1001) docker     (123)   419116 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/images/nb_conda_kernels.png
--rw-r--r--   0 runner    (1001) docker     (123)   120276 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/images/networking-coiled.svg
--rw-r--r--   0 runner    (1001) docker     (123)   121792 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/images/networking-dask.svg
--rw-r--r--   0 runner    (1001) docker     (123)   327594 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/images/notebook-shutdown.png
--rw-r--r--   0 runner    (1001) docker     (123)   358094 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/images/notebooks.png
--rw-r--r--   0 runner    (1001) docker     (123)   140733 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/images/performance-report-profile.png
--rw-r--r--   0 runner    (1001) docker     (123)   468366 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/images/performance-report-tasks.png
--rw-r--r--   0 runner    (1001) docker     (123)    47420 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/images/task-prefixes.png
--rw-r--r--   0 runner    (1001) docker     (123)    15926 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/images/team-account.png
--rw-r--r--   0 runner    (1001) docker     (123)    26332 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/images/team-add-member.png
--rw-r--r--   0 runner    (1001) docker     (123)   111562 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/images/team-invite.png
--rw-r--r--   0 runner    (1001) docker     (123)    85136 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/images/teams.png
--rw-r--r--   0 runner    (1001) docker     (123)   214434 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/images/view-senv-dependencies.png
--rw-r--r--   0 runner    (1001) docker     (123)   366443 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/images/widget-gif.gif
--rw-r--r--   0 runner    (1001) docker     (123)   118161 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/images/widget.png
--rw-r--r--   0 runner    (1001) docker     (123)     4622 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/index.rst
--rw-r--r--   0 runner    (1001) docker     (123)     4814 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/logging.rst
--rw-r--r--   0 runner    (1001) docker     (123)      894 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/manual_configure.rst
--rw-r--r--   0 runner    (1001) docker     (123)     6443 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/network_architecture.rst
--rw-r--r--   0 runner    (1001) docker     (123)     5218 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/oss-foundations.rst
--rw-r--r--   0 runner    (1001) docker     (123)     7515 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/package_sync.rst
--rw-r--r--   0 runner    (1001) docker     (123)     1262 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/package_sync_compatibility.rst
--rw-r--r--   0 runner    (1001) docker     (123)     4075 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/package_sync_limitations.rst
--rw-r--r--   0 runner    (1001) docker     (123)     4123 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/package_sync_production.rst
--rw-r--r--   0 runner    (1001) docker     (123)     4396 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/performance_reports.rst
--rw-r--r--   0 runner    (1001) docker     (123)     3687 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/quick_reference.rst
--rw-r--r--   0 runner    (1001) docker     (123)      809 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/release_notes.rst
--rw-r--r--   0 runner    (1001) docker     (123)     5145 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/software_environment.rst
--rw-r--r--   0 runner    (1001) docker     (123)     1050 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/software_environment_cli.rst
--rw-r--r--   0 runner    (1001) docker     (123)     3153 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/software_environment_local.rst
--rw-r--r--   0 runner    (1001) docker     (123)     1729 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/software_environment_management.rst
--rw-r--r--   0 runner    (1001) docker     (123)     1513 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/support.rst
--rw-r--r--   0 runner    (1001) docker     (123)     5690 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/teams.rst
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 16:24:51.656891 coiled-0.5.9.post0.dev7/docs/source/user_guide/troubleshooting/
--rw-r--r--   0 runner    (1001) docker     (123)      775 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/troubleshooting/expired_token_error.rst
--rw-r--r--   0 runner    (1001) docker     (123)      593 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/troubleshooting/index.rst
--rw-r--r--   0 runner    (1001) docker     (123)     4640 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/troubleshooting/killedworker_exception.rst
--rw-r--r--   0 runner    (1001) docker     (123)     5059 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/troubleshooting/repeated_timeout_errors.rst
--rw-r--r--   0 runner    (1001) docker     (123)     1338 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/troubleshooting/setup_access_token_error.rst
--rw-r--r--   0 runner    (1001) docker     (123)     1258 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/troubleshooting/timeout_error.rst
--rw-r--r--   0 runner    (1001) docker     (123)     2743 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/troubleshooting/tls_ssl_context_error.rst
--rw-r--r--   0 runner    (1001) docker     (123)      861 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/troubleshooting/visibility_resource_creation.rst
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 16:24:51.660891 coiled-0.5.9.post0.dev7/docs/source/user_guide/tutorials/
--rw-r--r--   0 runner    (1001) docker     (123)     4491 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/tutorials/arm.rst
--rw-r--r--   0 runner    (1001) docker     (123)     2732 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/tutorials/aws_permissions.rst
--rw-r--r--   0 runner    (1001) docker     (123)    10757 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/tutorials/bring_your_own_network.rst
--rw-r--r--   0 runner    (1001) docker     (123)     2668 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/tutorials/changing_backends.rst
--rw-r--r--   0 runner    (1001) docker     (123)     3893 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/tutorials/configuring_firewalls.rst
--rw-r--r--   0 runner    (1001) docker     (123)      671 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/tutorials/github_tokens.rst
--rw-r--r--   0 runner    (1001) docker     (123)      545 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/tutorials/index.rst
--rw-r--r--   0 runner    (1001) docker     (123)     1782 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/tutorials/resources_created_by_coiled.rst
--rw-r--r--   0 runner    (1001) docker     (123)     3117 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/tutorials/select_instance_types.rst
--rw-r--r--   0 runner    (1001) docker     (123)     4525 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/tutorials/set_backend_options.rst
--rw-r--r--   0 runner    (1001) docker     (123)     1745 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/tutorials/ssh.rst
--rw-r--r--   0 runner    (1001) docker     (123)     4713 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/tutorials/upload_file_to_coiled.rst
--rw-r--r--   0 runner    (1001) docker     (123)     3812 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/docs/source/user_guide/v2.rst
--rw-r--r--   0 runner    (1001) docker     (123)      147 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)      333 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/requirements.txt
--rw-r--r--   0 runner    (1001) docker     (123)      201 2023-03-30 16:24:51.660891 coiled-0.5.9.post0.dev7/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)      833 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/setup.py
--rw-r--r--   0 runner    (1001) docker     (123)    70028 2023-03-30 16:24:15.000000 coiled-0.5.9.post0.dev7/versioneer.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 19:46:07.013184 coiled-0.5.9.post0.dev8/
+-rw-r--r--   0 runner    (1001) docker     (123)     1524 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)      327 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     1076 2023-03-30 19:46:07.013184 coiled-0.5.9.post0.dev8/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      848 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 19:46:07.013184 coiled-0.5.9.post0.dev8/coiled/
+-rw-r--r--   0 runner    (1001) docker     (123)     2158 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/coiled/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 19:46:06.965183 coiled-0.5.9.post0.dev8/coiled/_beta/
+-rw-r--r--   0 runner    (1001) docker     (123)      501 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/coiled/_beta/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    80134 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/coiled/_beta/cluster.py
+-rw-r--r--   0 runner    (1001) docker     (123)    60251 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/coiled/_beta/core.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1895 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/coiled/_beta/cwi_log_link.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7937 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/coiled/_beta/states.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 19:46:06.965183 coiled-0.5.9.post0.dev8/coiled/_beta/widgets/
+-rw-r--r--   0 runner    (1001) docker     (123)     1011 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/coiled/_beta/widgets/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15129 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/coiled/_beta/widgets/rich.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2608 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/coiled/_beta/widgets/util.py
+-rw-r--r--   0 runner    (1001) docker     (123)      508 2023-03-30 19:46:07.013184 coiled-0.5.9.post0.dev8/coiled/_version.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7188 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/coiled/analytics.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 19:46:06.969183 coiled-0.5.9.post0.dev8/coiled/cli/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/coiled/cli/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 19:46:06.969183 coiled-0.5.9.post0.dev8/coiled/cli/cluster/
+-rw-r--r--   0 runner    (1001) docker     (123)      526 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/coiled/cli/cluster/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11190 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/coiled/cli/cluster/better_logs.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6474 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/coiled/cli/cluster/logs.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4693 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/coiled/cli/cluster/ssh.py
+-rw-r--r--   0 runner    (1001) docker     (123)      714 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/coiled/cli/core.py
+-rw-r--r--   0 runner    (1001) docker     (123)      992 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/coiled/cli/curl.py
+-rw-r--r--   0 runner    (1001) docker     (123)      394 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/coiled/cli/diagnostics.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5942 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/coiled/cli/env.py
+-rw-r--r--   0 runner    (1001) docker     (123)      716 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/coiled/cli/login.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 19:46:06.969183 coiled-0.5.9.post0.dev8/coiled/cli/notebook/
+-rw-r--r--   0 runner    (1001) docker     (123)      916 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/coiled/cli/notebook/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11249 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/coiled/cli/notebook/notebook.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2675 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/coiled/cli/package_sync.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 19:46:06.969183 coiled-0.5.9.post0.dev8/coiled/cli/setup/
+-rw-r--r--   0 runner    (1001) docker     (123)      766 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/coiled/cli/setup/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4321 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/coiled/cli/setup/amp.py
+-rw-r--r--   0 runner    (1001) docker     (123)    43611 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/coiled/cli/setup/aws.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2643 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/coiled/cli/setup/entry.py
+-rw-r--r--   0 runner    (1001) docker     (123)    25966 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/coiled/cli/setup/gcp.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2076 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/coiled/cli/setup/prometheus.py
+-rw-r--r--   0 runner    (1001) docker     (123)      160 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/coiled/cli/setup/util.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 19:46:06.969183 coiled-0.5.9.post0.dev8/coiled/cli/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/coiled/cli/tests/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      261 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/coiled/cli/tests/test_core.py
+-rw-r--r--   0 runner    (1001) docker     (123)      482 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/coiled/cli/tests/test_diagnostics.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3241 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/coiled/cli/tests/test_env.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4386 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/coiled/cli/tests/test_login.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1752 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/coiled/cli/utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1170 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/coiled/cluster.py
+-rw-r--r--   0 runner    (1001) docker     (123)      842 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/coiled/coiled.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)      284 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/coiled/compatibility.py
+-rw-r--r--   0 runner    (1001) docker     (123)      189 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/coiled/config.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3427 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/coiled/context.py
+-rw-r--r--   0 runner    (1001) docker     (123)   110704 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/coiled/core.py
+-rw-r--r--   0 runner    (1001) docker     (123)      305 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/coiled/errors.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2926 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/coiled/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17261 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/coiled/magic.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12271 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/coiled/scan.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3984 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/coiled/software.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 19:46:06.973183 coiled-0.5.9.post0.dev8/coiled/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/coiled/tests/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    29802 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/coiled/tests/test_core.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2354 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/coiled/tests/test_exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3249 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/coiled/tests/test_manage_api_tokens.py
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/coiled/tests/test_package_sync.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3601 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/coiled/tests/test_public_configs.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4696 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/coiled/tests/test_scan.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17096 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/coiled/tests/test_software_environments.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2887 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/coiled/tests/test_type_validator.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20225 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/coiled/tests/test_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4307 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/coiled/types.py
+-rw-r--r--   0 runner    (1001) docker     (123)    47332 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/coiled/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 19:46:06.973183 coiled-0.5.9.post0.dev8/coiled/v2/
+-rw-r--r--   0 runner    (1001) docker     (123)      649 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/coiled/v2/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7973 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/coiled/websockets.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 19:46:06.965183 coiled-0.5.9.post0.dev8/coiled.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     1076 2023-03-30 19:46:06.000000 coiled-0.5.9.post0.dev8/coiled.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)    10146 2023-03-30 19:46:06.000000 coiled-0.5.9.post0.dev8/coiled.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-30 19:46:06.000000 coiled-0.5.9.post0.dev8/coiled.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       47 2023-03-30 19:46:06.000000 coiled-0.5.9.post0.dev8/coiled.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-30 19:45:56.000000 coiled-0.5.9.post0.dev8/coiled.egg-info/not-zip-safe
+-rw-r--r--   0 runner    (1001) docker     (123)      203 2023-03-30 19:46:06.000000 coiled-0.5.9.post0.dev8/coiled.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        7 2023-03-30 19:46:06.000000 coiled-0.5.9.post0.dev8/coiled.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)    20889 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/conftest.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 19:46:06.973183 coiled-0.5.9.post0.dev8/docs/
+-rw-r--r--   0 runner    (1001) docker     (123)      654 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/Makefile
+-rw-r--r--   0 runner    (1001) docker     (123)      764 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/make.bat
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 19:46:06.973183 coiled-0.5.9.post0.dev8/docs/source/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 19:46:06.973183 coiled-0.5.9.post0.dev8/docs/source/_static/
+-rw-r--r--   0 runner    (1001) docker     (123)     1877 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/_static/Coiled-Logo.svg
+-rw-r--r--   0 runner    (1001) docker     (123)   293786 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/_static/coiledsnake.png
+-rw-r--r--   0 runner    (1001) docker     (123)     9307 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/_static/custom.css
+-rw-r--r--   0 runner    (1001) docker     (123)   338221 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/_static/favicon.ico
+-rw-r--r--   0 runner    (1001) docker     (123)      593 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/_static/left-arrow.svg
+-rw-r--r--   0 runner    (1001) docker     (123)     7053 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/_static/logo-horizontal.svg
+-rw-r--r--   0 runner    (1001) docker     (123)     1544 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/_static/logo-solo.svg
+-rw-r--r--   0 runner    (1001) docker     (123)     6740 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/_static/logo-vertical.svg
+-rw-r--r--   0 runner    (1001) docker     (123)      456 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/_static/note-icon.svg
+-rw-r--r--   0 runner    (1001) docker     (123)      585 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/_static/right-arrow.svg
+-rw-r--r--   0 runner    (1001) docker     (123)      456 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/_static/tip-icon.svg
+-rw-r--r--   0 runner    (1001) docker     (123)      456 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/_static/warning-icon.svg
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 19:46:06.973183 coiled-0.5.9.post0.dev8/docs/source/_templates/
+-rw-r--r--   0 runner    (1001) docker     (123)     3657 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/_templates/layout.html
+-rw-r--r--   0 runner    (1001) docker     (123)     5772 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/conf.py
+-rw-r--r--   0 runner    (1001) docker     (123)      252 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/index.rst
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 19:46:06.981183 coiled-0.5.9.post0.dev8/docs/source/user_guide/
+-rw-r--r--   0 runner    (1001) docker     (123)     3009 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/accessing_secure_data.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      394 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/analytics-api.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     3292 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/analytics-install.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     8185 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/analytics-privacy.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     2958 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/analytics.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     3348 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/api.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     1475 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/aws-cli.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     8875 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/aws_configure.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     9109 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/aws_reference.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      501 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/azure_reference.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     1517 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/backends.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      609 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/best_practices.rst
+-rw-r--r--   0 runner    (1001) docker     (123)    34583 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/changelog.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     3034 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/choose_cloud_provider.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     1477 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/cli_setup.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      849 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/cloud-provider-reference.rst
+-rw-r--r--   0 runner    (1001) docker     (123)    18340 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/cloud_changelog.rst
+-rw-r--r--   0 runner    (1001) docker     (123)    13076 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/cluster_creation.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     1558 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/cluster_management.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     1134 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/cluster_reuse.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     1928 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/cluster_scaling.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     4703 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/configuration.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     3619 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/docker.rst
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 19:46:06.985183 coiled-0.5.9.post0.dev8/docs/source/user_guide/examples/
+-rw-r--r--   0 runner    (1001) docker     (123)    61035 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/examples/dask-optuna-hpo.ipynb
+-rw-r--r--   0 runner    (1001) docker     (123)    12606 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/examples/dask-xgboost.ipynb
+-rw-r--r--   0 runner    (1001) docker     (123)     5148 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/examples/jupyterlab.ipynb
+-rw-r--r--   0 runner    (1001) docker     (123)    15596 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/examples/mongodb.ipynb
+-rw-r--r--   0 runner    (1001) docker     (123)    87895 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/examples/parallel-hpo-multi-cluster.ipynb
+-rw-r--r--   0 runner    (1001) docker     (123)      677 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/examples/prefect-dask-client.py
+-rw-r--r--   0 runner    (1001) docker     (123)      664 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/examples/prefect-dask-task-runner.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1078 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/examples/prefect-executor.py
+-rw-r--r--   0 runner    (1001) docker     (123)      763 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/examples/prefect-no-runner.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1104 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/examples/prefect-task.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6703 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/examples/prefect-v2.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     7375 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/examples/prefect.rst
+-rw-r--r--   0 runner    (1001) docker     (123)    31848 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/examples/study_many_threads.pickle
+-rw-r--r--   0 runner    (1001) docker     (123)     2451 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/examples.rst
+-rw-r--r--   0 runner    (1001) docker     (123)    10893 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/faq.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     2263 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/gcp-cli.rst
+-rw-r--r--   0 runner    (1001) docker     (123)    10392 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/gcp_configure.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     6243 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/gcp_reference.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     5133 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/getting_started.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     8100 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/gpu.rst
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 19:46:07.009184 coiled-0.5.9.post0.dev8/docs/source/user_guide/images/
+-rw-r--r--   0 runner    (1001) docker     (123)    29164 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/images/account-statistics.png
+-rw-r--r--   0 runner    (1001) docker     (123)   246771 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/images/aws-cloudwatch.png
+-rw-r--r--   0 runner    (1001) docker     (123)   195084 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/images/aws-tag-editor.png
+-rw-r--r--   0 runner    (1001) docker     (123)    48308 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/images/backend-coiled-aws-architecture.png
+-rw-r--r--   0 runner    (1001) docker     (123)    36833 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/images/backend-coiled-aws-architecture.svg
+-rw-r--r--   0 runner    (1001) docker     (123)   222087 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/images/backend-coiled-aws-vm.png
+-rw-r--r--   0 runner    (1001) docker     (123)    79203 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/images/backend-coiled-aws-vm.svg
+-rw-r--r--   0 runner    (1001) docker     (123)   232656 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/images/backend-coiled-gcp-vm.png
+-rw-r--r--   0 runner    (1001) docker     (123)    80022 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/images/backend-coiled-gcp-vm.svg
+-rw-r--r--   0 runner    (1001) docker     (123)   229777 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/images/backend-external-aws-vm.png
+-rw-r--r--   0 runner    (1001) docker     (123)    81443 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/images/backend-external-aws-vm.svg
+-rw-r--r--   0 runner    (1001) docker     (123)   229181 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/images/backend-external-gcp-vm.png
+-rw-r--r--   0 runner    (1001) docker     (123)   277717 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/images/cloud-analytics-clusters.png
+-rw-r--r--   0 runner    (1001) docker     (123)   478779 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/images/cloud-analytics-usage.png
+-rw-r--r--   0 runner    (1001) docker     (123)    23441 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/images/cloud-backend-browser-aws.png
+-rw-r--r--   0 runner    (1001) docker     (123)   129143 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/images/cloud-backend-complete-gcp.gif
+-rw-r--r--   0 runner    (1001) docker     (123)   224680 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/images/cloud-backend-complete-slow.gif
+-rw-r--r--   0 runner    (1001) docker     (123)   120800 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/images/cloud-backend-flow-gcp.png
+-rw-r--r--   0 runner    (1001) docker     (123)    38843 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/images/cloud-backend-keys-aws.png
+-rw-r--r--   0 runner    (1001) docker     (123)    47316 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/images/cloud-backend-keys-gcp.png
+-rw-r--r--   0 runner    (1001) docker     (123)    34087 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/images/cloud-backend-network.png
+-rw-r--r--   0 runner    (1001) docker     (123)    86339 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/images/cloud-backend-provider-aws.png
+-rw-r--r--   0 runner    (1001) docker     (123)    93757 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/images/cloud-backend-provider-gcp.png
+-rw-r--r--   0 runner    (1001) docker     (123)    31315 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/images/cloud-backend-registry-aws.png
+-rw-r--r--   0 runner    (1001) docker     (123)    31740 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/images/cloud-backend-registry-gcp.png
+-rw-r--r--   0 runner    (1001) docker     (123)   221648 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/images/cloud-backend-reset.png
+-rw-r--r--   0 runner    (1001) docker     (123)    42173 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/images/cloud-backend-review-aws.png
+-rw-r--r--   0 runner    (1001) docker     (123)    44403 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/images/cloud-backend-review-gcp.png
+-rw-r--r--   0 runner    (1001) docker     (123)    82685 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/images/cloud-backend-start.png
+-rw-r--r--   0 runner    (1001) docker     (123)    62482 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/images/cloud-billing-free.png
+-rw-r--r--   0 runner    (1001) docker     (123)    74351 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/images/cloud-billing-payg.png
+-rw-r--r--   0 runner    (1001) docker     (123)    34848 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/images/cloud-billing-spend-limit.png
+-rw-r--r--   0 runner    (1001) docker     (123)    78140 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/images/cloud-cluster-alerts.png
+-rw-r--r--   0 runner    (1001) docker     (123)   121085 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/images/cloud-cluster-dashboard.png
+-rw-r--r--   0 runner    (1001) docker     (123)   312535 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/images/cloud-cluster-lifecycle.png
+-rw-r--r--   0 runner    (1001) docker     (123)   350352 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/images/cloud-cluster-logs.png
+-rw-r--r--   0 runner    (1001) docker     (123)    71503 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/images/cloud-cluster-usage.png
+-rw-r--r--   0 runner    (1001) docker     (123)    99727 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/images/cluster-profile.png
+-rw-r--r--   0 runner    (1001) docker     (123)   428284 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/images/cluster-repr.png
+-rw-r--r--   0 runner    (1001) docker     (123)    42601 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/images/cluster-statistics.png
+-rw-r--r--   0 runner    (1001) docker     (123)    57582 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/images/cluster-widget-notebook.png
+-rw-r--r--   0 runner    (1001) docker     (123)   422843 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/images/clusters-table.png
+-rw-r--r--   0 runner    (1001) docker     (123)   410552 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/images/coiled-architecture.png
+-rw-r--r--   0 runner    (1001) docker     (123)   110851 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/images/coiled-architecture.svg
+-rw-r--r--   0 runner    (1001) docker     (123)   171959 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/images/coiled-prefect-executor.png
+-rw-r--r--   0 runner    (1001) docker     (123)   128633 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/images/coiled-prefect-executor.svg
+-rw-r--r--   0 runner    (1001) docker     (123)   168887 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/images/coiled-prefect-task.png
+-rw-r--r--   0 runner    (1001) docker     (123)   130821 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/images/coiled-prefect-task.svg
+-rw-r--r--   0 runner    (1001) docker     (123)   300959 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/images/coiled-profile.png
+-rw-r--r--   0 runner    (1001) docker     (123)    36341 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/images/coiled-setup.png
+-rw-r--r--   0 runner    (1001) docker     (123)   467848 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/images/coiled-streamlit-example.png
+-rw-r--r--   0 runner    (1001) docker     (123)    76347 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/images/coiled-upload-install.svg
+-rw-r--r--   0 runner    (1001) docker     (123)   352442 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/images/github-add-token.png
+-rw-r--r--   0 runner    (1001) docker     (123)    47899 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/images/jupyterlab-extension.png
+-rw-r--r--   0 runner    (1001) docker     (123)     3139 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/images/logo-aws.png
+-rw-r--r--   0 runner    (1001) docker     (123)    65865 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/images/logo-gcp.png
+-rw-r--r--   0 runner    (1001) docker     (123)   419116 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/images/nb_conda_kernels.png
+-rw-r--r--   0 runner    (1001) docker     (123)   120276 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/images/networking-coiled.svg
+-rw-r--r--   0 runner    (1001) docker     (123)   121792 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/images/networking-dask.svg
+-rw-r--r--   0 runner    (1001) docker     (123)   327594 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/images/notebook-shutdown.png
+-rw-r--r--   0 runner    (1001) docker     (123)   358094 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/images/notebooks.png
+-rw-r--r--   0 runner    (1001) docker     (123)   140733 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/images/performance-report-profile.png
+-rw-r--r--   0 runner    (1001) docker     (123)   468366 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/images/performance-report-tasks.png
+-rw-r--r--   0 runner    (1001) docker     (123)    47420 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/images/task-prefixes.png
+-rw-r--r--   0 runner    (1001) docker     (123)    15926 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/images/team-account.png
+-rw-r--r--   0 runner    (1001) docker     (123)    26332 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/images/team-add-member.png
+-rw-r--r--   0 runner    (1001) docker     (123)   111562 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/images/team-invite.png
+-rw-r--r--   0 runner    (1001) docker     (123)    85136 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/images/teams.png
+-rw-r--r--   0 runner    (1001) docker     (123)   214434 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/images/view-senv-dependencies.png
+-rw-r--r--   0 runner    (1001) docker     (123)   366443 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/images/widget-gif.gif
+-rw-r--r--   0 runner    (1001) docker     (123)   118161 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/images/widget.png
+-rw-r--r--   0 runner    (1001) docker     (123)     4622 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/index.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     4814 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/logging.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      894 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/manual_configure.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     6443 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/network_architecture.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     5218 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/oss-foundations.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     7515 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/package_sync.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     1262 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/package_sync_compatibility.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     4075 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/package_sync_limitations.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     4123 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/package_sync_production.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     4396 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/performance_reports.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     3687 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/quick_reference.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      809 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/release_notes.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     5145 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/software_environment.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     1050 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/software_environment_cli.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     3153 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/software_environment_local.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     1729 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/software_environment_management.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     1513 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/support.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     5690 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/teams.rst
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 19:46:07.013184 coiled-0.5.9.post0.dev8/docs/source/user_guide/troubleshooting/
+-rw-r--r--   0 runner    (1001) docker     (123)      775 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/troubleshooting/expired_token_error.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      593 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/troubleshooting/index.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     4640 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/troubleshooting/killedworker_exception.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     5059 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/troubleshooting/repeated_timeout_errors.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     1338 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/troubleshooting/setup_access_token_error.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     1258 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/troubleshooting/timeout_error.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     2743 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/troubleshooting/tls_ssl_context_error.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      861 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/troubleshooting/visibility_resource_creation.rst
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 19:46:07.013184 coiled-0.5.9.post0.dev8/docs/source/user_guide/tutorials/
+-rw-r--r--   0 runner    (1001) docker     (123)     4491 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/tutorials/arm.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     2732 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/tutorials/aws_permissions.rst
+-rw-r--r--   0 runner    (1001) docker     (123)    10757 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/tutorials/bring_your_own_network.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     2668 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/tutorials/changing_backends.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     3893 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/tutorials/configuring_firewalls.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      671 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/tutorials/github_tokens.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      545 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/tutorials/index.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     1782 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/tutorials/resources_created_by_coiled.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     3117 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/tutorials/select_instance_types.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     4525 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/tutorials/set_backend_options.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     1745 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/tutorials/ssh.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     4713 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/tutorials/upload_file_to_coiled.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     3812 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/docs/source/user_guide/v2.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      147 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)      333 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/requirements.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      201 2023-03-30 19:46:07.013184 coiled-0.5.9.post0.dev8/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)      833 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/setup.py
+-rw-r--r--   0 runner    (1001) docker     (123)    70028 2023-03-30 19:45:30.000000 coiled-0.5.9.post0.dev8/versioneer.py
```

### Comparing `coiled-0.5.9.post0.dev7/LICENSE` & `coiled-0.5.9.post0.dev8/LICENSE`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/PKG-INFO` & `coiled-0.5.9.post0.dev8/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: coiled
-Version: 0.5.9.post0.dev7
+Version: 0.5.9.post0.dev8
 Home-page: https://coiled.io
 Maintainer: Coiled
 Maintainer-email: info@coiled.io
 Requires-Python: >=3.7
 Description-Content-Type: text/markdown
 License-File: LICENSE
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: coiled Version: 0.5.9.post0.dev7 Home-page: https:/
+Metadata-Version: 2.1 Name: coiled Version: 0.5.9.post0.dev8 Home-page: https:/
 /coiled.io Maintainer: Coiled Maintainer-email: info@coiled.io Requires-Python:
 >=3.7 Description-Content-Type: text/markdown License-File: LICENSE
                                    [Coiled]
              Coiled.io â¢ Documentation â¢ Community â¢ Support
 Coiled is a deployment-as-a-service library for scaling Python with Dask, a
 popular open source library for parallel analytics. Coiled manages cloud
 resources, networking, software environments, and everything you need to scale
```

### Comparing `coiled-0.5.9.post0.dev7/README.md` & `coiled-0.5.9.post0.dev8/README.md`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/coiled/__init__.py` & `coiled-0.5.9.post0.dev8/coiled/__init__.py`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/coiled/_beta/cluster.py` & `coiled-0.5.9.post0.dev8/coiled/_beta/cluster.py`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/coiled/_beta/core.py` & `coiled-0.5.9.post0.dev8/coiled/_beta/core.py`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/coiled/_beta/cwi_log_link.py` & `coiled-0.5.9.post0.dev8/coiled/_beta/cwi_log_link.py`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/coiled/_beta/states.py` & `coiled-0.5.9.post0.dev8/coiled/_beta/states.py`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/coiled/_beta/widgets/__init__.py` & `coiled-0.5.9.post0.dev8/coiled/_beta/widgets/__init__.py`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/coiled/_beta/widgets/rich.py` & `coiled-0.5.9.post0.dev8/coiled/_beta/widgets/rich.py`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/coiled/_beta/widgets/util.py` & `coiled-0.5.9.post0.dev8/coiled/_beta/widgets/util.py`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/coiled/analytics.py` & `coiled-0.5.9.post0.dev8/coiled/analytics.py`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/coiled/cli/cluster/__init__.py` & `coiled-0.5.9.post0.dev8/coiled/cli/cluster/__init__.py`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/coiled/cli/cluster/better_logs.py` & `coiled-0.5.9.post0.dev8/coiled/cli/cluster/better_logs.py`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/coiled/cli/cluster/logs.py` & `coiled-0.5.9.post0.dev8/coiled/cli/cluster/logs.py`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/coiled/cli/cluster/ssh.py` & `coiled-0.5.9.post0.dev8/coiled/cli/cluster/ssh.py`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/coiled/cli/core.py` & `coiled-0.5.9.post0.dev8/coiled/cli/core.py`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/coiled/cli/curl.py` & `coiled-0.5.9.post0.dev8/coiled/cli/curl.py`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/coiled/cli/env.py` & `coiled-0.5.9.post0.dev8/coiled/cli/env.py`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/coiled/cli/login.py` & `coiled-0.5.9.post0.dev8/coiled/cli/login.py`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/coiled/cli/notebook/__init__.py` & `coiled-0.5.9.post0.dev8/coiled/cli/notebook/__init__.py`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/coiled/cli/notebook/notebook.py` & `coiled-0.5.9.post0.dev8/coiled/cli/notebook/notebook.py`

 * *Files 2% similar despite different names*

```diff
@@ -3,14 +3,15 @@
 import base64
 import hashlib
 import os
 import re
 import shutil
 import subprocess
 import webbrowser
+from typing import Sequence
 
 import click
 import importlib_metadata
 from rich import print
 from urllib3.util import parse_url
 
 import coiled
@@ -134,25 +135,25 @@
     help=(
         "Software environment name to use. If not given, all the currently-installed "
         "Python packages are replicated on the VM using package sync."
     ),
 )
 @click.option(
     "--vm-type",
-    default=[],
+    default=(),
     multiple=True,
     help=("VM type to use. Specify multiple times to provide multiple options."),
 )
 @click.option(
     "--open",
     default=True,
     is_flag=True,
     help="Whether to open the notebook in the default browser once it's launched",
 )
-def start_notebook(name: str, sync: bool, software: str | None, vm_type: list[str], open: bool):
+def start_notebook(name: str, sync: bool, software: str | None, vm_type: Sequence[str], open: bool):
     """
     Launch or re-open a notebook session, with optional file syncing.
 
     If a notebook session with the same ``name`` already exists, it's not re-created.
     If file sync was initially not enabled, running ``coiled notebook-beta up --sync``
     will begin file sync without re-launching the notebook.
     """
@@ -167,15 +168,15 @@
         cluster = coiled.Cluster(
             name=name,
             cloud=cloud,
             n_workers=0,
             software=software,
             jupyter=True,
             scheduler_options={"idle_timeout": None},
-            scheduler_vm_types=vm_type if vm_type else None,
+            scheduler_vm_types=list(vm_type) if vm_type else None,
             allow_ssh=True,
         )
 
         url = cluster.jupyter_link
         cluster_id = cluster.cluster_id
         assert cluster_id is not None
         if sync:
```

### Comparing `coiled-0.5.9.post0.dev7/coiled/cli/package_sync.py` & `coiled-0.5.9.post0.dev8/coiled/cli/package_sync.py`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/coiled/cli/setup/__init__.py` & `coiled-0.5.9.post0.dev8/coiled/cli/setup/__init__.py`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/coiled/cli/setup/amp.py` & `coiled-0.5.9.post0.dev8/coiled/cli/setup/amp.py`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/coiled/cli/setup/aws.py` & `coiled-0.5.9.post0.dev8/coiled/cli/setup/aws.py`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/coiled/cli/setup/entry.py` & `coiled-0.5.9.post0.dev8/coiled/cli/setup/entry.py`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/coiled/cli/setup/gcp.py` & `coiled-0.5.9.post0.dev8/coiled/cli/setup/gcp.py`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/coiled/cli/setup/prometheus.py` & `coiled-0.5.9.post0.dev8/coiled/cli/setup/prometheus.py`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/coiled/cli/tests/test_env.py` & `coiled-0.5.9.post0.dev8/coiled/cli/tests/test_env.py`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/coiled/cli/tests/test_login.py` & `coiled-0.5.9.post0.dev8/coiled/cli/tests/test_login.py`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/coiled/cli/utils.py` & `coiled-0.5.9.post0.dev8/coiled/cli/utils.py`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/coiled/cluster.py` & `coiled-0.5.9.post0.dev8/coiled/cluster.py`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/coiled/coiled.yaml` & `coiled-0.5.9.post0.dev8/coiled/coiled.yaml`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/coiled/context.py` & `coiled-0.5.9.post0.dev8/coiled/context.py`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/coiled/core.py` & `coiled-0.5.9.post0.dev8/coiled/core.py`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/coiled/exceptions.py` & `coiled-0.5.9.post0.dev8/coiled/exceptions.py`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/coiled/magic.py` & `coiled-0.5.9.post0.dev8/coiled/magic.py`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/coiled/scan.py` & `coiled-0.5.9.post0.dev8/coiled/scan.py`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/coiled/software.py` & `coiled-0.5.9.post0.dev8/coiled/software.py`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/coiled/tests/test_core.py` & `coiled-0.5.9.post0.dev8/coiled/tests/test_core.py`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/coiled/tests/test_exceptions.py` & `coiled-0.5.9.post0.dev8/coiled/tests/test_exceptions.py`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/coiled/tests/test_manage_api_tokens.py` & `coiled-0.5.9.post0.dev8/coiled/tests/test_manage_api_tokens.py`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/coiled/tests/test_public_configs.py` & `coiled-0.5.9.post0.dev8/coiled/tests/test_public_configs.py`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/coiled/tests/test_scan.py` & `coiled-0.5.9.post0.dev8/coiled/tests/test_scan.py`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/coiled/tests/test_software_environments.py` & `coiled-0.5.9.post0.dev8/coiled/tests/test_software_environments.py`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/coiled/tests/test_type_validator.py` & `coiled-0.5.9.post0.dev8/coiled/tests/test_type_validator.py`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/coiled/tests/test_utils.py` & `coiled-0.5.9.post0.dev8/coiled/tests/test_utils.py`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/coiled/types.py` & `coiled-0.5.9.post0.dev8/coiled/types.py`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/coiled/utils.py` & `coiled-0.5.9.post0.dev8/coiled/utils.py`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/coiled/v2/__init__.py` & `coiled-0.5.9.post0.dev8/coiled/v2/__init__.py`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/coiled/websockets.py` & `coiled-0.5.9.post0.dev8/coiled/websockets.py`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/coiled.egg-info/PKG-INFO` & `coiled-0.5.9.post0.dev8/coiled.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: coiled
-Version: 0.5.9.post0.dev7
+Version: 0.5.9.post0.dev8
 Home-page: https://coiled.io
 Maintainer: Coiled
 Maintainer-email: info@coiled.io
 Requires-Python: >=3.7
 Description-Content-Type: text/markdown
 License-File: LICENSE
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: coiled Version: 0.5.9.post0.dev7 Home-page: https:/
+Metadata-Version: 2.1 Name: coiled Version: 0.5.9.post0.dev8 Home-page: https:/
 /coiled.io Maintainer: Coiled Maintainer-email: info@coiled.io Requires-Python:
 >=3.7 Description-Content-Type: text/markdown License-File: LICENSE
                                    [Coiled]
              Coiled.io â¢ Documentation â¢ Community â¢ Support
 Coiled is a deployment-as-a-service library for scaling Python with Dask, a
 popular open source library for parallel analytics. Coiled manages cloud
 resources, networking, software environments, and everything you need to scale
```

### Comparing `coiled-0.5.9.post0.dev7/coiled.egg-info/SOURCES.txt` & `coiled-0.5.9.post0.dev8/coiled.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/conftest.py` & `coiled-0.5.9.post0.dev8/conftest.py`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/Makefile` & `coiled-0.5.9.post0.dev8/docs/Makefile`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/make.bat` & `coiled-0.5.9.post0.dev8/docs/make.bat`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/_static/Coiled-Logo.svg` & `coiled-0.5.9.post0.dev8/docs/source/_static/Coiled-Logo.svg`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/_static/coiledsnake.png` & `coiled-0.5.9.post0.dev8/docs/source/_static/coiledsnake.png`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/_static/custom.css` & `coiled-0.5.9.post0.dev8/docs/source/_static/custom.css`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/_static/favicon.ico` & `coiled-0.5.9.post0.dev8/docs/source/_static/favicon.ico`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/_static/left-arrow.svg` & `coiled-0.5.9.post0.dev8/docs/source/_static/left-arrow.svg`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/_static/logo-horizontal.svg` & `coiled-0.5.9.post0.dev8/docs/source/_static/logo-horizontal.svg`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/_static/logo-solo.svg` & `coiled-0.5.9.post0.dev8/docs/source/_static/logo-solo.svg`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/_static/logo-vertical.svg` & `coiled-0.5.9.post0.dev8/docs/source/_static/logo-vertical.svg`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/_static/right-arrow.svg` & `coiled-0.5.9.post0.dev8/docs/source/_static/right-arrow.svg`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/_templates/layout.html` & `coiled-0.5.9.post0.dev8/docs/source/_templates/layout.html`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/conf.py` & `coiled-0.5.9.post0.dev8/docs/source/conf.py`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/accessing_secure_data.rst` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/accessing_secure_data.rst`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/analytics-install.rst` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/analytics-install.rst`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/analytics-privacy.rst` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/analytics-privacy.rst`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/analytics.rst` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/analytics.rst`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/api.rst` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/api.rst`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/aws-cli.rst` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/aws-cli.rst`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/aws_configure.rst` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/aws_configure.rst`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/aws_reference.rst` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/aws_reference.rst`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/backends.rst` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/backends.rst`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/best_practices.rst` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/best_practices.rst`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/changelog.rst` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/changelog.rst`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/choose_cloud_provider.rst` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/choose_cloud_provider.rst`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/cli_setup.rst` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/cli_setup.rst`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/cloud-provider-reference.rst` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/cloud-provider-reference.rst`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/cloud_changelog.rst` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/cloud_changelog.rst`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/cluster_creation.rst` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/cluster_creation.rst`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/cluster_management.rst` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/cluster_management.rst`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/cluster_reuse.rst` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/cluster_reuse.rst`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/cluster_scaling.rst` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/cluster_scaling.rst`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/configuration.rst` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/configuration.rst`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/docker.rst` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/docker.rst`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/examples/dask-optuna-hpo.ipynb` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/examples/dask-optuna-hpo.ipynb`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/examples/dask-xgboost.ipynb` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/examples/dask-xgboost.ipynb`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/examples/jupyterlab.ipynb` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/examples/jupyterlab.ipynb`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/examples/mongodb.ipynb` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/examples/mongodb.ipynb`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/examples/parallel-hpo-multi-cluster.ipynb` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/examples/parallel-hpo-multi-cluster.ipynb`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/examples/prefect-dask-client.py` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/examples/prefect-dask-client.py`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/examples/prefect-dask-task-runner.py` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/examples/prefect-dask-task-runner.py`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/examples/prefect-executor.py` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/examples/prefect-executor.py`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/examples/prefect-no-runner.py` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/examples/prefect-no-runner.py`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/examples/prefect-task.py` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/examples/prefect-task.py`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/examples/prefect-v2.rst` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/examples/prefect-v2.rst`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/examples/prefect.rst` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/examples/prefect.rst`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/examples/study_many_threads.pickle` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/examples/study_many_threads.pickle`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/examples.rst` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/examples.rst`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/faq.rst` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/faq.rst`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/gcp-cli.rst` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/gcp-cli.rst`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/gcp_configure.rst` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/gcp_configure.rst`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/gcp_reference.rst` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/gcp_reference.rst`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/getting_started.rst` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/getting_started.rst`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/gpu.rst` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/gpu.rst`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/images/account-statistics.png` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/images/account-statistics.png`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/images/aws-cloudwatch.png` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/images/aws-cloudwatch.png`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/images/aws-tag-editor.png` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/images/aws-tag-editor.png`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/images/backend-coiled-aws-architecture.png` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/images/backend-coiled-aws-architecture.png`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/images/backend-coiled-aws-architecture.svg` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/images/backend-coiled-aws-architecture.svg`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/images/backend-coiled-aws-vm.png` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/images/backend-coiled-aws-vm.png`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/images/backend-coiled-aws-vm.svg` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/images/backend-coiled-aws-vm.svg`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/images/backend-coiled-gcp-vm.png` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/images/backend-coiled-gcp-vm.png`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/images/backend-coiled-gcp-vm.svg` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/images/backend-coiled-gcp-vm.svg`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/images/backend-external-aws-vm.png` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/images/backend-external-aws-vm.png`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/images/backend-external-aws-vm.svg` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/images/backend-external-aws-vm.svg`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/images/backend-external-gcp-vm.png` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/images/backend-external-gcp-vm.png`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/images/cloud-analytics-clusters.png` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/images/cloud-analytics-clusters.png`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/images/cloud-analytics-usage.png` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/images/cloud-analytics-usage.png`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/images/cloud-backend-browser-aws.png` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/images/cloud-backend-browser-aws.png`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/images/cloud-backend-complete-gcp.gif` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/images/cloud-backend-complete-gcp.gif`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/images/cloud-backend-complete-slow.gif` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/images/cloud-backend-complete-slow.gif`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/images/cloud-backend-flow-gcp.png` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/images/cloud-backend-flow-gcp.png`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/images/cloud-backend-keys-aws.png` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/images/cloud-backend-keys-aws.png`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/images/cloud-backend-keys-gcp.png` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/images/cloud-backend-keys-gcp.png`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/images/cloud-backend-network.png` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/images/cloud-backend-network.png`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/images/cloud-backend-provider-aws.png` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/images/cloud-backend-provider-aws.png`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/images/cloud-backend-provider-gcp.png` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/images/cloud-backend-provider-gcp.png`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/images/cloud-backend-registry-aws.png` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/images/cloud-backend-registry-aws.png`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/images/cloud-backend-registry-gcp.png` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/images/cloud-backend-registry-gcp.png`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/images/cloud-backend-reset.png` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/images/cloud-backend-reset.png`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/images/cloud-backend-review-aws.png` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/images/cloud-backend-review-aws.png`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/images/cloud-backend-review-gcp.png` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/images/cloud-backend-review-gcp.png`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/images/cloud-backend-start.png` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/images/cloud-backend-start.png`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/images/cloud-billing-free.png` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/images/cloud-billing-free.png`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/images/cloud-billing-payg.png` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/images/cloud-billing-payg.png`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/images/cloud-billing-spend-limit.png` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/images/cloud-billing-spend-limit.png`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/images/cloud-cluster-alerts.png` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/images/cloud-cluster-alerts.png`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/images/cloud-cluster-dashboard.png` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/images/cloud-cluster-dashboard.png`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/images/cloud-cluster-lifecycle.png` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/images/cloud-cluster-lifecycle.png`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/images/cloud-cluster-logs.png` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/images/cloud-cluster-logs.png`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/images/cloud-cluster-usage.png` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/images/cloud-cluster-usage.png`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/images/cluster-profile.png` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/images/cluster-profile.png`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/images/cluster-repr.png` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/images/cluster-repr.png`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/images/cluster-statistics.png` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/images/cluster-statistics.png`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/images/cluster-widget-notebook.png` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/images/cluster-widget-notebook.png`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/images/clusters-table.png` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/images/clusters-table.png`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/images/coiled-architecture.png` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/images/coiled-architecture.png`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/images/coiled-architecture.svg` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/images/coiled-architecture.svg`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/images/coiled-prefect-executor.png` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/images/coiled-prefect-executor.png`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/images/coiled-prefect-executor.svg` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/images/coiled-prefect-executor.svg`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/images/coiled-prefect-task.png` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/images/coiled-prefect-task.png`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/images/coiled-prefect-task.svg` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/images/coiled-prefect-task.svg`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/images/coiled-profile.png` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/images/coiled-profile.png`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/images/coiled-setup.png` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/images/coiled-setup.png`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/images/coiled-streamlit-example.png` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/images/coiled-streamlit-example.png`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/images/coiled-upload-install.svg` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/images/coiled-upload-install.svg`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/images/github-add-token.png` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/images/github-add-token.png`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/images/jupyterlab-extension.png` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/images/jupyterlab-extension.png`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/images/logo-aws.png` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/images/logo-aws.png`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/images/logo-gcp.png` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/images/logo-gcp.png`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/images/nb_conda_kernels.png` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/images/nb_conda_kernels.png`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/images/networking-coiled.svg` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/images/networking-coiled.svg`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/images/networking-dask.svg` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/images/networking-dask.svg`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/images/notebook-shutdown.png` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/images/notebook-shutdown.png`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/images/notebooks.png` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/images/notebooks.png`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/images/performance-report-profile.png` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/images/performance-report-profile.png`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/images/performance-report-tasks.png` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/images/performance-report-tasks.png`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/images/task-prefixes.png` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/images/task-prefixes.png`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/images/team-account.png` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/images/team-account.png`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/images/team-add-member.png` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/images/team-add-member.png`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/images/team-invite.png` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/images/team-invite.png`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/images/teams.png` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/images/teams.png`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/images/view-senv-dependencies.png` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/images/view-senv-dependencies.png`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/images/widget-gif.gif` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/images/widget-gif.gif`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/images/widget.png` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/images/widget.png`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/index.rst` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/index.rst`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/logging.rst` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/logging.rst`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/manual_configure.rst` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/manual_configure.rst`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/network_architecture.rst` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/network_architecture.rst`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/oss-foundations.rst` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/oss-foundations.rst`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/package_sync.rst` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/package_sync.rst`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/package_sync_compatibility.rst` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/package_sync_compatibility.rst`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/package_sync_limitations.rst` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/package_sync_limitations.rst`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/package_sync_production.rst` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/package_sync_production.rst`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/performance_reports.rst` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/performance_reports.rst`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/quick_reference.rst` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/quick_reference.rst`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/release_notes.rst` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/release_notes.rst`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/software_environment.rst` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/software_environment.rst`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/software_environment_cli.rst` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/software_environment_cli.rst`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/software_environment_local.rst` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/software_environment_local.rst`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/software_environment_management.rst` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/software_environment_management.rst`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/support.rst` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/support.rst`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/teams.rst` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/teams.rst`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/troubleshooting/expired_token_error.rst` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/troubleshooting/expired_token_error.rst`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/troubleshooting/index.rst` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/troubleshooting/index.rst`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/troubleshooting/killedworker_exception.rst` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/troubleshooting/killedworker_exception.rst`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/troubleshooting/repeated_timeout_errors.rst` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/troubleshooting/repeated_timeout_errors.rst`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/troubleshooting/setup_access_token_error.rst` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/troubleshooting/setup_access_token_error.rst`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/troubleshooting/timeout_error.rst` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/troubleshooting/timeout_error.rst`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/troubleshooting/tls_ssl_context_error.rst` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/troubleshooting/tls_ssl_context_error.rst`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/troubleshooting/visibility_resource_creation.rst` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/troubleshooting/visibility_resource_creation.rst`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/tutorials/arm.rst` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/tutorials/arm.rst`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/tutorials/aws_permissions.rst` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/tutorials/aws_permissions.rst`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/tutorials/bring_your_own_network.rst` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/tutorials/bring_your_own_network.rst`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/tutorials/changing_backends.rst` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/tutorials/changing_backends.rst`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/tutorials/configuring_firewalls.rst` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/tutorials/configuring_firewalls.rst`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/tutorials/github_tokens.rst` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/tutorials/github_tokens.rst`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/tutorials/index.rst` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/tutorials/index.rst`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/tutorials/resources_created_by_coiled.rst` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/tutorials/resources_created_by_coiled.rst`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/tutorials/select_instance_types.rst` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/tutorials/select_instance_types.rst`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/tutorials/set_backend_options.rst` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/tutorials/set_backend_options.rst`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/tutorials/ssh.rst` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/tutorials/ssh.rst`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/tutorials/upload_file_to_coiled.rst` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/tutorials/upload_file_to_coiled.rst`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/docs/source/user_guide/v2.rst` & `coiled-0.5.9.post0.dev8/docs/source/user_guide/v2.rst`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/setup.py` & `coiled-0.5.9.post0.dev8/setup.py`

 * *Files identical despite different names*

### Comparing `coiled-0.5.9.post0.dev7/versioneer.py` & `coiled-0.5.9.post0.dev8/versioneer.py`

 * *Files identical despite different names*

