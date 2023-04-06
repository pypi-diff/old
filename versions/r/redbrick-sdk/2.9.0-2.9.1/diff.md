# Comparing `tmp/redbrick-sdk-2.9.0.tar.gz` & `tmp/redbrick-sdk-2.9.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "redbrick-sdk-2.9.0.tar", last modified: Fri Jan  6 05:45:13 2023, max compression
+gzip compressed data, was "redbrick-sdk-2.9.1.tar", last modified: Mon Feb 13 11:49:02 2023, max compression
```

## Comparing `redbrick-sdk-2.9.0.tar` & `redbrick-sdk-2.9.1.tar`

### file list

```diff
@@ -1,87 +1,87 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 05:45:13.281209 redbrick-sdk-2.9.0/
--rw-r--r--   0 runner    (1001) docker     (123)     1084 2023-01-06 05:45:05.000000 redbrick-sdk-2.9.0/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)       82 2023-01-06 05:45:05.000000 redbrick-sdk-2.9.0/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)      984 2023-01-06 05:45:13.281209 redbrick-sdk-2.9.0/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      638 2023-01-06 05:45:05.000000 redbrick-sdk-2.9.0/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 05:45:13.277209 redbrick-sdk-2.9.0/redbrick/
--rw-r--r--   0 runner    (1001) docker     (123)     4243 2023-01-06 05:45:05.000000 redbrick-sdk-2.9.0/redbrick/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 05:45:13.277209 redbrick-sdk-2.9.0/redbrick/cli/
--rw-r--r--   0 runner    (1001) docker     (123)      126 2023-01-06 05:45:05.000000 redbrick-sdk-2.9.0/redbrick/cli/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4805 2023-01-06 05:45:05.000000 redbrick-sdk-2.9.0/redbrick/cli/cli_base.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 05:45:13.277209 redbrick-sdk-2.9.0/redbrick/cli/command/
--rw-r--r--   0 runner    (1001) docker     (123)      443 2023-01-06 05:45:05.000000 redbrick-sdk-2.9.0/redbrick/cli/command/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3387 2023-01-06 05:45:05.000000 redbrick-sdk-2.9.0/redbrick/cli/command/clone.py
--rw-r--r--   0 runner    (1001) docker     (123)     7965 2023-01-06 05:45:05.000000 redbrick-sdk-2.9.0/redbrick/cli/command/config.py
--rw-r--r--   0 runner    (1001) docker     (123)    16088 2023-01-06 05:45:05.000000 redbrick-sdk-2.9.0/redbrick/cli/command/export.py
--rw-r--r--   0 runner    (1001) docker     (123)     3970 2023-01-06 05:45:05.000000 redbrick-sdk-2.9.0/redbrick/cli/command/info.py
--rw-r--r--   0 runner    (1001) docker     (123)     2912 2023-01-06 05:45:05.000000 redbrick-sdk-2.9.0/redbrick/cli/command/init.py
--rw-r--r--   0 runner    (1001) docker     (123)     1725 2023-01-06 05:45:05.000000 redbrick-sdk-2.9.0/redbrick/cli/command/report.py
--rw-r--r--   0 runner    (1001) docker     (123)    13918 2023-01-06 05:45:05.000000 redbrick-sdk-2.9.0/redbrick/cli/command/upload.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 05:45:13.277209 redbrick-sdk-2.9.0/redbrick/cli/entity/
--rw-r--r--   0 runner    (1001) docker     (123)      182 2023-01-06 05:45:05.000000 redbrick-sdk-2.9.0/redbrick/cli/entity/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4728 2023-01-06 05:45:05.000000 redbrick-sdk-2.9.0/redbrick/cli/entity/cache.py
--rw-r--r--   0 runner    (1001) docker     (123)     2038 2023-01-06 05:45:05.000000 redbrick-sdk-2.9.0/redbrick/cli/entity/conf.py
--rw-r--r--   0 runner    (1001) docker     (123)     4432 2023-01-06 05:45:05.000000 redbrick-sdk-2.9.0/redbrick/cli/entity/creds.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 05:45:13.277209 redbrick-sdk-2.9.0/redbrick/cli/input/
--rw-r--r--   0 runner    (1001) docker     (123)      385 2023-01-06 05:45:05.000000 redbrick-sdk-2.9.0/redbrick/cli/input/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1173 2023-01-06 05:45:05.000000 redbrick-sdk-2.9.0/redbrick/cli/input/api_key.py
--rw-r--r--   0 runner    (1001) docker     (123)     1207 2023-01-06 05:45:05.000000 redbrick-sdk-2.9.0/redbrick/cli/input/number.py
--rw-r--r--   0 runner    (1001) docker     (123)     2254 2023-01-06 05:45:05.000000 redbrick-sdk-2.9.0/redbrick/cli/input/profile.py
--rw-r--r--   0 runner    (1001) docker     (123)     1379 2023-01-06 05:45:05.000000 redbrick-sdk-2.9.0/redbrick/cli/input/select.py
--rw-r--r--   0 runner    (1001) docker     (123)     1419 2023-01-06 05:45:05.000000 redbrick-sdk-2.9.0/redbrick/cli/input/text.py
--rw-r--r--   0 runner    (1001) docker     (123)     1261 2023-01-06 05:45:05.000000 redbrick-sdk-2.9.0/redbrick/cli/input/url.py
--rw-r--r--   0 runner    (1001) docker     (123)     1271 2023-01-06 05:45:05.000000 redbrick-sdk-2.9.0/redbrick/cli/input/uuid.py
--rw-r--r--   0 runner    (1001) docker     (123)     5729 2023-01-06 05:45:05.000000 redbrick-sdk-2.9.0/redbrick/cli/project.py
--rw-r--r--   0 runner    (1001) docker     (123)     4314 2023-01-06 05:45:05.000000 redbrick-sdk-2.9.0/redbrick/cli/public.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 05:45:13.277209 redbrick-sdk-2.9.0/redbrick/common/
--rw-r--r--   0 runner    (1001) docker     (123)       51 2023-01-06 05:45:05.000000 redbrick-sdk-2.9.0/redbrick/common/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4874 2023-01-06 05:45:05.000000 redbrick-sdk-2.9.0/redbrick/common/client.py
--rw-r--r--   0 runner    (1001) docker     (123)      642 2023-01-06 05:45:05.000000 redbrick-sdk-2.9.0/redbrick/common/constants.py
--rw-r--r--   0 runner    (1001) docker     (123)     1292 2023-01-06 05:45:05.000000 redbrick-sdk-2.9.0/redbrick/common/context.py
--rw-r--r--   0 runner    (1001) docker     (123)     1601 2023-01-06 05:45:05.000000 redbrick-sdk-2.9.0/redbrick/common/enums.py
--rw-r--r--   0 runner    (1001) docker     (123)     2004 2023-01-06 05:45:05.000000 redbrick-sdk-2.9.0/redbrick/common/export.py
--rw-r--r--   0 runner    (1001) docker     (123)     1873 2023-01-06 05:45:05.000000 redbrick-sdk-2.9.0/redbrick/common/labeling.py
--rw-r--r--   0 runner    (1001) docker     (123)     3243 2023-01-06 05:45:05.000000 redbrick-sdk-2.9.0/redbrick/common/project.py
--rw-r--r--   0 runner    (1001) docker     (123)     1818 2023-01-06 05:45:05.000000 redbrick-sdk-2.9.0/redbrick/common/upload.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 05:45:13.281209 redbrick-sdk-2.9.0/redbrick/export/
--rw-r--r--   0 runner    (1001) docker     (123)       60 2023-01-06 05:45:05.000000 redbrick-sdk-2.9.0/redbrick/export/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    24027 2023-01-06 05:45:05.000000 redbrick-sdk-2.9.0/redbrick/export/public.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 05:45:13.281209 redbrick-sdk-2.9.0/redbrick/labeling/
--rw-r--r--   0 runner    (1001) docker     (123)       81 2023-01-06 05:45:05.000000 redbrick-sdk-2.9.0/redbrick/labeling/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    20987 2023-01-06 05:45:05.000000 redbrick-sdk-2.9.0/redbrick/labeling/public.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 05:45:13.281209 redbrick-sdk-2.9.0/redbrick/organization/
--rw-r--r--   0 runner    (1001) docker     (123)     9169 2023-01-06 05:45:05.000000 redbrick-sdk-2.9.0/redbrick/organization/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2016 2023-01-06 05:45:05.000000 redbrick-sdk-2.9.0/redbrick/organization/basic_project.py
--rw-r--r--   0 runner    (1001) docker     (123)     8181 2023-01-06 05:45:05.000000 redbrick-sdk-2.9.0/redbrick/project.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 05:45:13.281209 redbrick-sdk-2.9.0/redbrick/repo/
--rw-r--r--   0 runner    (1001) docker     (123)      161 2023-01-06 05:45:05.000000 redbrick-sdk-2.9.0/redbrick/repo/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    11404 2023-01-06 05:45:05.000000 redbrick-sdk-2.9.0/redbrick/repo/export.py
--rw-r--r--   0 runner    (1001) docker     (123)     7970 2023-01-06 05:45:05.000000 redbrick-sdk-2.9.0/redbrick/repo/labeling.py
--rw-r--r--   0 runner    (1001) docker     (123)    14839 2023-01-06 05:45:05.000000 redbrick-sdk-2.9.0/redbrick/repo/project.py
--rw-r--r--   0 runner    (1001) docker     (123)     3889 2023-01-06 05:45:05.000000 redbrick-sdk-2.9.0/redbrick/repo/shards.py
--rw-r--r--   0 runner    (1001) docker     (123)     6975 2023-01-06 05:45:05.000000 redbrick-sdk-2.9.0/redbrick/repo/upload.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 05:45:13.281209 redbrick-sdk-2.9.0/redbrick/upload/
--rw-r--r--   0 runner    (1001) docker     (123)       63 2023-01-06 05:45:05.000000 redbrick-sdk-2.9.0/redbrick/upload/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    24659 2023-01-06 05:45:05.000000 redbrick-sdk-2.9.0/redbrick/upload/public.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 05:45:13.281209 redbrick-sdk-2.9.0/redbrick/utils/
--rw-r--r--   0 runner    (1001) docker     (123)       41 2023-01-06 05:45:05.000000 redbrick-sdk-2.9.0/redbrick/utils/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1493 2023-01-06 05:45:05.000000 redbrick-sdk-2.9.0/redbrick/utils/async_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)      311 2023-01-06 05:45:05.000000 redbrick-sdk-2.9.0/redbrick/utils/common_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     9419 2023-01-06 05:45:05.000000 redbrick-sdk-2.9.0/redbrick/utils/dicom.py
--rw-r--r--   0 runner    (1001) docker     (123)     7658 2023-01-06 05:45:05.000000 redbrick-sdk-2.9.0/redbrick/utils/files.py
--rw-r--r--   0 runner    (1001) docker     (123)      981 2023-01-06 05:45:05.000000 redbrick-sdk-2.9.0/redbrick/utils/logging.py
--rw-r--r--   0 runner    (1001) docker     (123)     2139 2023-01-06 05:45:05.000000 redbrick-sdk-2.9.0/redbrick/utils/pagination.py
--rw-r--r--   0 runner    (1001) docker     (123)     7574 2023-01-06 05:45:05.000000 redbrick-sdk-2.9.0/redbrick/utils/rb_event_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)    18915 2023-01-06 05:45:05.000000 redbrick-sdk-2.9.0/redbrick/utils/rb_label_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)      738 2023-01-06 05:45:05.000000 redbrick-sdk-2.9.0/redbrick/utils/rb_tax_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     9115 2023-01-06 05:45:05.000000 redbrick-sdk-2.9.0/redbrick/utils/upload.py
--rw-r--r--   0 runner    (1001) docker     (123)     2533 2023-01-06 05:45:05.000000 redbrick-sdk-2.9.0/redbrick/version_check.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 05:45:13.281209 redbrick-sdk-2.9.0/redbrick_sdk.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)      984 2023-01-06 05:45:13.000000 redbrick-sdk-2.9.0/redbrick_sdk.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     1965 2023-01-06 05:45:13.000000 redbrick-sdk-2.9.0/redbrick_sdk.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-06 05:45:13.000000 redbrick-sdk-2.9.0/redbrick_sdk.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       52 2023-01-06 05:45:13.000000 redbrick-sdk-2.9.0/redbrick_sdk.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (123)      789 2023-01-06 05:45:13.000000 redbrick-sdk-2.9.0/redbrick_sdk.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        9 2023-01-06 05:45:13.000000 redbrick-sdk-2.9.0/redbrick_sdk.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)     1061 2023-01-06 05:45:13.281209 redbrick-sdk-2.9.0/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1980 2023-01-06 05:45:05.000000 redbrick-sdk-2.9.0/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-13 11:49:02.227869 redbrick-sdk-2.9.1/
+-rw-r--r--   0 runner    (1001) docker     (123)     1084 2023-02-13 11:48:53.000000 redbrick-sdk-2.9.1/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)       82 2023-02-13 11:48:53.000000 redbrick-sdk-2.9.1/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)      984 2023-02-13 11:49:02.227869 redbrick-sdk-2.9.1/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      638 2023-02-13 11:48:53.000000 redbrick-sdk-2.9.1/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-13 11:49:02.219869 redbrick-sdk-2.9.1/redbrick/
+-rw-r--r--   0 runner    (1001) docker     (123)     4243 2023-02-13 11:48:53.000000 redbrick-sdk-2.9.1/redbrick/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-13 11:49:02.219869 redbrick-sdk-2.9.1/redbrick/cli/
+-rw-r--r--   0 runner    (1001) docker     (123)      126 2023-02-13 11:48:53.000000 redbrick-sdk-2.9.1/redbrick/cli/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4805 2023-02-13 11:48:53.000000 redbrick-sdk-2.9.1/redbrick/cli/cli_base.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-13 11:49:02.219869 redbrick-sdk-2.9.1/redbrick/cli/command/
+-rw-r--r--   0 runner    (1001) docker     (123)      443 2023-02-13 11:48:53.000000 redbrick-sdk-2.9.1/redbrick/cli/command/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3387 2023-02-13 11:48:53.000000 redbrick-sdk-2.9.1/redbrick/cli/command/clone.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7965 2023-02-13 11:48:53.000000 redbrick-sdk-2.9.1/redbrick/cli/command/config.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16088 2023-02-13 11:48:53.000000 redbrick-sdk-2.9.1/redbrick/cli/command/export.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3970 2023-02-13 11:48:53.000000 redbrick-sdk-2.9.1/redbrick/cli/command/info.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2912 2023-02-13 11:48:53.000000 redbrick-sdk-2.9.1/redbrick/cli/command/init.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1725 2023-02-13 11:48:53.000000 redbrick-sdk-2.9.1/redbrick/cli/command/report.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13918 2023-02-13 11:48:53.000000 redbrick-sdk-2.9.1/redbrick/cli/command/upload.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-13 11:49:02.219869 redbrick-sdk-2.9.1/redbrick/cli/entity/
+-rw-r--r--   0 runner    (1001) docker     (123)      182 2023-02-13 11:48:53.000000 redbrick-sdk-2.9.1/redbrick/cli/entity/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4728 2023-02-13 11:48:53.000000 redbrick-sdk-2.9.1/redbrick/cli/entity/cache.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2038 2023-02-13 11:48:53.000000 redbrick-sdk-2.9.1/redbrick/cli/entity/conf.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4432 2023-02-13 11:48:53.000000 redbrick-sdk-2.9.1/redbrick/cli/entity/creds.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-13 11:49:02.223868 redbrick-sdk-2.9.1/redbrick/cli/input/
+-rw-r--r--   0 runner    (1001) docker     (123)      385 2023-02-13 11:48:53.000000 redbrick-sdk-2.9.1/redbrick/cli/input/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1173 2023-02-13 11:48:53.000000 redbrick-sdk-2.9.1/redbrick/cli/input/api_key.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1207 2023-02-13 11:48:53.000000 redbrick-sdk-2.9.1/redbrick/cli/input/number.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2254 2023-02-13 11:48:53.000000 redbrick-sdk-2.9.1/redbrick/cli/input/profile.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1379 2023-02-13 11:48:53.000000 redbrick-sdk-2.9.1/redbrick/cli/input/select.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1419 2023-02-13 11:48:53.000000 redbrick-sdk-2.9.1/redbrick/cli/input/text.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1261 2023-02-13 11:48:53.000000 redbrick-sdk-2.9.1/redbrick/cli/input/url.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1271 2023-02-13 11:48:53.000000 redbrick-sdk-2.9.1/redbrick/cli/input/uuid.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5729 2023-02-13 11:48:53.000000 redbrick-sdk-2.9.1/redbrick/cli/project.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4314 2023-02-13 11:48:53.000000 redbrick-sdk-2.9.1/redbrick/cli/public.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-13 11:49:02.223868 redbrick-sdk-2.9.1/redbrick/common/
+-rw-r--r--   0 runner    (1001) docker     (123)       51 2023-02-13 11:48:53.000000 redbrick-sdk-2.9.1/redbrick/common/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4874 2023-02-13 11:48:53.000000 redbrick-sdk-2.9.1/redbrick/common/client.py
+-rw-r--r--   0 runner    (1001) docker     (123)      642 2023-02-13 11:48:53.000000 redbrick-sdk-2.9.1/redbrick/common/constants.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1292 2023-02-13 11:48:53.000000 redbrick-sdk-2.9.1/redbrick/common/context.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1601 2023-02-13 11:48:53.000000 redbrick-sdk-2.9.1/redbrick/common/enums.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2004 2023-02-13 11:48:53.000000 redbrick-sdk-2.9.1/redbrick/common/export.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1873 2023-02-13 11:48:53.000000 redbrick-sdk-2.9.1/redbrick/common/labeling.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3243 2023-02-13 11:48:53.000000 redbrick-sdk-2.9.1/redbrick/common/project.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1818 2023-02-13 11:48:53.000000 redbrick-sdk-2.9.1/redbrick/common/upload.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-13 11:49:02.223868 redbrick-sdk-2.9.1/redbrick/export/
+-rw-r--r--   0 runner    (1001) docker     (123)       60 2023-02-13 11:48:53.000000 redbrick-sdk-2.9.1/redbrick/export/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    24027 2023-02-13 11:48:53.000000 redbrick-sdk-2.9.1/redbrick/export/public.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-13 11:49:02.223868 redbrick-sdk-2.9.1/redbrick/labeling/
+-rw-r--r--   0 runner    (1001) docker     (123)       81 2023-02-13 11:48:53.000000 redbrick-sdk-2.9.1/redbrick/labeling/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20987 2023-02-13 11:48:53.000000 redbrick-sdk-2.9.1/redbrick/labeling/public.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-13 11:49:02.223868 redbrick-sdk-2.9.1/redbrick/organization/
+-rw-r--r--   0 runner    (1001) docker     (123)     9169 2023-02-13 11:48:53.000000 redbrick-sdk-2.9.1/redbrick/organization/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2016 2023-02-13 11:48:53.000000 redbrick-sdk-2.9.1/redbrick/organization/basic_project.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8181 2023-02-13 11:48:53.000000 redbrick-sdk-2.9.1/redbrick/project.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-13 11:49:02.223868 redbrick-sdk-2.9.1/redbrick/repo/
+-rw-r--r--   0 runner    (1001) docker     (123)      161 2023-02-13 11:48:53.000000 redbrick-sdk-2.9.1/redbrick/repo/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11404 2023-02-13 11:48:53.000000 redbrick-sdk-2.9.1/redbrick/repo/export.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7970 2023-02-13 11:48:53.000000 redbrick-sdk-2.9.1/redbrick/repo/labeling.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14839 2023-02-13 11:48:53.000000 redbrick-sdk-2.9.1/redbrick/repo/project.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3889 2023-02-13 11:48:53.000000 redbrick-sdk-2.9.1/redbrick/repo/shards.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6975 2023-02-13 11:48:53.000000 redbrick-sdk-2.9.1/redbrick/repo/upload.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-13 11:49:02.223868 redbrick-sdk-2.9.1/redbrick/upload/
+-rw-r--r--   0 runner    (1001) docker     (123)       63 2023-02-13 11:48:53.000000 redbrick-sdk-2.9.1/redbrick/upload/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    24659 2023-02-13 11:48:53.000000 redbrick-sdk-2.9.1/redbrick/upload/public.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-13 11:49:02.227869 redbrick-sdk-2.9.1/redbrick/utils/
+-rw-r--r--   0 runner    (1001) docker     (123)       41 2023-02-13 11:48:53.000000 redbrick-sdk-2.9.1/redbrick/utils/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1493 2023-02-13 11:48:53.000000 redbrick-sdk-2.9.1/redbrick/utils/async_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)      311 2023-02-13 11:48:53.000000 redbrick-sdk-2.9.1/redbrick/utils/common_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9419 2023-02-13 11:48:53.000000 redbrick-sdk-2.9.1/redbrick/utils/dicom.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7658 2023-02-13 11:48:53.000000 redbrick-sdk-2.9.1/redbrick/utils/files.py
+-rw-r--r--   0 runner    (1001) docker     (123)      981 2023-02-13 11:48:53.000000 redbrick-sdk-2.9.1/redbrick/utils/logging.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2139 2023-02-13 11:48:53.000000 redbrick-sdk-2.9.1/redbrick/utils/pagination.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7574 2023-02-13 11:48:53.000000 redbrick-sdk-2.9.1/redbrick/utils/rb_event_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19525 2023-02-13 11:48:53.000000 redbrick-sdk-2.9.1/redbrick/utils/rb_label_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)      738 2023-02-13 11:48:53.000000 redbrick-sdk-2.9.1/redbrick/utils/rb_tax_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9115 2023-02-13 11:48:53.000000 redbrick-sdk-2.9.1/redbrick/utils/upload.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2533 2023-02-13 11:48:53.000000 redbrick-sdk-2.9.1/redbrick/version_check.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-13 11:49:02.227869 redbrick-sdk-2.9.1/redbrick_sdk.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)      984 2023-02-13 11:49:02.000000 redbrick-sdk-2.9.1/redbrick_sdk.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     1965 2023-02-13 11:49:02.000000 redbrick-sdk-2.9.1/redbrick_sdk.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-02-13 11:49:02.000000 redbrick-sdk-2.9.1/redbrick_sdk.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       52 2023-02-13 11:49:02.000000 redbrick-sdk-2.9.1/redbrick_sdk.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      789 2023-02-13 11:49:02.000000 redbrick-sdk-2.9.1/redbrick_sdk.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        9 2023-02-13 11:49:02.000000 redbrick-sdk-2.9.1/redbrick_sdk.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     1061 2023-02-13 11:49:02.227869 redbrick-sdk-2.9.1/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1980 2023-02-13 11:48:53.000000 redbrick-sdk-2.9.1/setup.py
```

### Comparing `redbrick-sdk-2.9.0/LICENSE` & `redbrick-sdk-2.9.1/LICENSE`

 * *Files identical despite different names*

### Comparing `redbrick-sdk-2.9.0/PKG-INFO` & `redbrick-sdk-2.9.1/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: redbrick-sdk
-Version: 2.9.0
+Version: 2.9.1
 Summary: RedBrick platform Python SDK!
 Home-page: https://github.com/redbrick-ai/redbrick-sdk
 License: UNKNOWN
 Description: This is an SDK to make integration with the RedBrick AI platform as easy as possible. This includes uploading and downloading data
         as well as making your datasets easily available for training. Use this SDK to access your data and labels anywhere you run your code, whether that is on the cloud or locally with a Jupyter Notebook.
         
         Please feel free to submit issues on github or at [support@redbrickai.com](mailto:support@redbrickai.com) if you run into any problems or have suggestions.
```

### Comparing `redbrick-sdk-2.9.0/README.md` & `redbrick-sdk-2.9.1/README.md`

 * *Files identical despite different names*

### Comparing `redbrick-sdk-2.9.0/redbrick/__init__.py` & `redbrick-sdk-2.9.1/redbrick/__init__.py`

 * *Files 1% similar despite different names*

```diff
@@ -21,15 +21,15 @@
 from redbrick.project import RBProject
 from redbrick.organization import RBOrganization
 
 from redbrick.utils.logging import logger
 
 from .version_check import version_check
 
-__version__ = "2.9.0"
+__version__ = "2.9.1"
 
 # windows event loop close bug https://github.com/encode/httpx/issues/914#issuecomment-622586610
 try:
     if (
         sys.version_info[0] == 3
         and sys.version_info[1] >= 8
         and sys.platform.startswith("win")
```

### Comparing `redbrick-sdk-2.9.0/redbrick/cli/cli_base.py` & `redbrick-sdk-2.9.1/redbrick/cli/cli_base.py`

 * *Files identical despite different names*

### Comparing `redbrick-sdk-2.9.0/redbrick/cli/command/clone.py` & `redbrick-sdk-2.9.1/redbrick/cli/command/clone.py`

 * *Files identical despite different names*

### Comparing `redbrick-sdk-2.9.0/redbrick/cli/command/config.py` & `redbrick-sdk-2.9.1/redbrick/cli/command/config.py`

 * *Files identical despite different names*

### Comparing `redbrick-sdk-2.9.0/redbrick/cli/command/export.py` & `redbrick-sdk-2.9.1/redbrick/cli/command/export.py`

 * *Files identical despite different names*

### Comparing `redbrick-sdk-2.9.0/redbrick/cli/command/info.py` & `redbrick-sdk-2.9.1/redbrick/cli/command/info.py`

 * *Files identical despite different names*

### Comparing `redbrick-sdk-2.9.0/redbrick/cli/command/init.py` & `redbrick-sdk-2.9.1/redbrick/cli/command/init.py`

 * *Files identical despite different names*

### Comparing `redbrick-sdk-2.9.0/redbrick/cli/command/report.py` & `redbrick-sdk-2.9.1/redbrick/cli/command/report.py`

 * *Files identical despite different names*

### Comparing `redbrick-sdk-2.9.0/redbrick/cli/command/upload.py` & `redbrick-sdk-2.9.1/redbrick/cli/command/upload.py`

 * *Files identical despite different names*

### Comparing `redbrick-sdk-2.9.0/redbrick/cli/entity/cache.py` & `redbrick-sdk-2.9.1/redbrick/cli/entity/cache.py`

 * *Files identical despite different names*

### Comparing `redbrick-sdk-2.9.0/redbrick/cli/entity/conf.py` & `redbrick-sdk-2.9.1/redbrick/cli/entity/conf.py`

 * *Files identical despite different names*

### Comparing `redbrick-sdk-2.9.0/redbrick/cli/entity/creds.py` & `redbrick-sdk-2.9.1/redbrick/cli/entity/creds.py`

 * *Files identical despite different names*

### Comparing `redbrick-sdk-2.9.0/redbrick/cli/input/api_key.py` & `redbrick-sdk-2.9.1/redbrick/cli/input/api_key.py`

 * *Files identical despite different names*

### Comparing `redbrick-sdk-2.9.0/redbrick/cli/input/number.py` & `redbrick-sdk-2.9.1/redbrick/cli/input/number.py`

 * *Files identical despite different names*

### Comparing `redbrick-sdk-2.9.0/redbrick/cli/input/profile.py` & `redbrick-sdk-2.9.1/redbrick/cli/input/profile.py`

 * *Files identical despite different names*

### Comparing `redbrick-sdk-2.9.0/redbrick/cli/input/select.py` & `redbrick-sdk-2.9.1/redbrick/cli/input/select.py`

 * *Files identical despite different names*

### Comparing `redbrick-sdk-2.9.0/redbrick/cli/input/text.py` & `redbrick-sdk-2.9.1/redbrick/cli/input/text.py`

 * *Files identical despite different names*

### Comparing `redbrick-sdk-2.9.0/redbrick/cli/input/url.py` & `redbrick-sdk-2.9.1/redbrick/cli/input/url.py`

 * *Files identical despite different names*

### Comparing `redbrick-sdk-2.9.0/redbrick/cli/input/uuid.py` & `redbrick-sdk-2.9.1/redbrick/cli/input/uuid.py`

 * *Files identical despite different names*

### Comparing `redbrick-sdk-2.9.0/redbrick/cli/project.py` & `redbrick-sdk-2.9.1/redbrick/cli/project.py`

 * *Files identical despite different names*

### Comparing `redbrick-sdk-2.9.0/redbrick/cli/public.py` & `redbrick-sdk-2.9.1/redbrick/cli/public.py`

 * *Files identical despite different names*

### Comparing `redbrick-sdk-2.9.0/redbrick/common/client.py` & `redbrick-sdk-2.9.1/redbrick/common/client.py`

 * *Files identical despite different names*

### Comparing `redbrick-sdk-2.9.0/redbrick/common/constants.py` & `redbrick-sdk-2.9.1/redbrick/common/constants.py`

 * *Files identical despite different names*

### Comparing `redbrick-sdk-2.9.0/redbrick/common/context.py` & `redbrick-sdk-2.9.1/redbrick/common/context.py`

 * *Files identical despite different names*

### Comparing `redbrick-sdk-2.9.0/redbrick/common/enums.py` & `redbrick-sdk-2.9.1/redbrick/common/enums.py`

 * *Files identical despite different names*

### Comparing `redbrick-sdk-2.9.0/redbrick/common/export.py` & `redbrick-sdk-2.9.1/redbrick/common/export.py`

 * *Files identical despite different names*

### Comparing `redbrick-sdk-2.9.0/redbrick/common/labeling.py` & `redbrick-sdk-2.9.1/redbrick/common/labeling.py`

 * *Files identical despite different names*

### Comparing `redbrick-sdk-2.9.0/redbrick/common/project.py` & `redbrick-sdk-2.9.1/redbrick/common/project.py`

 * *Files identical despite different names*

### Comparing `redbrick-sdk-2.9.0/redbrick/common/upload.py` & `redbrick-sdk-2.9.1/redbrick/common/upload.py`

 * *Files identical despite different names*

### Comparing `redbrick-sdk-2.9.0/redbrick/export/public.py` & `redbrick-sdk-2.9.1/redbrick/export/public.py`

 * *Files identical despite different names*

### Comparing `redbrick-sdk-2.9.0/redbrick/labeling/public.py` & `redbrick-sdk-2.9.1/redbrick/labeling/public.py`

 * *Files identical despite different names*

### Comparing `redbrick-sdk-2.9.0/redbrick/organization/__init__.py` & `redbrick-sdk-2.9.1/redbrick/organization/__init__.py`

 * *Files identical despite different names*

### Comparing `redbrick-sdk-2.9.0/redbrick/organization/basic_project.py` & `redbrick-sdk-2.9.1/redbrick/organization/basic_project.py`

 * *Files identical despite different names*

### Comparing `redbrick-sdk-2.9.0/redbrick/project.py` & `redbrick-sdk-2.9.1/redbrick/project.py`

 * *Files identical despite different names*

### Comparing `redbrick-sdk-2.9.0/redbrick/repo/export.py` & `redbrick-sdk-2.9.1/redbrick/repo/export.py`

 * *Files identical despite different names*

### Comparing `redbrick-sdk-2.9.0/redbrick/repo/labeling.py` & `redbrick-sdk-2.9.1/redbrick/repo/labeling.py`

 * *Files identical despite different names*

### Comparing `redbrick-sdk-2.9.0/redbrick/repo/project.py` & `redbrick-sdk-2.9.1/redbrick/repo/project.py`

 * *Files identical despite different names*

### Comparing `redbrick-sdk-2.9.0/redbrick/repo/shards.py` & `redbrick-sdk-2.9.1/redbrick/repo/shards.py`

 * *Files identical despite different names*

### Comparing `redbrick-sdk-2.9.0/redbrick/repo/upload.py` & `redbrick-sdk-2.9.1/redbrick/repo/upload.py`

 * *Files identical despite different names*

### Comparing `redbrick-sdk-2.9.0/redbrick/upload/public.py` & `redbrick-sdk-2.9.1/redbrick/upload/public.py`

 * *Files identical despite different names*

### Comparing `redbrick-sdk-2.9.0/redbrick/utils/async_utils.py` & `redbrick-sdk-2.9.1/redbrick/utils/async_utils.py`

 * *Files identical despite different names*

### Comparing `redbrick-sdk-2.9.0/redbrick/utils/dicom.py` & `redbrick-sdk-2.9.1/redbrick/utils/dicom.py`

 * *Files identical despite different names*

### Comparing `redbrick-sdk-2.9.0/redbrick/utils/files.py` & `redbrick-sdk-2.9.1/redbrick/utils/files.py`

 * *Files identical despite different names*

### Comparing `redbrick-sdk-2.9.0/redbrick/utils/logging.py` & `redbrick-sdk-2.9.1/redbrick/utils/logging.py`

 * *Files identical despite different names*

### Comparing `redbrick-sdk-2.9.0/redbrick/utils/pagination.py` & `redbrick-sdk-2.9.1/redbrick/utils/pagination.py`

 * *Files identical despite different names*

### Comparing `redbrick-sdk-2.9.0/redbrick/utils/rb_event_utils.py` & `redbrick-sdk-2.9.1/redbrick/utils/rb_event_utils.py`

 * *Files identical despite different names*

### Comparing `redbrick-sdk-2.9.0/redbrick/utils/rb_label_utils.py` & `redbrick-sdk-2.9.1/redbrick/utils/rb_label_utils.py`

 * *Files 2% similar despite different names*

```diff
@@ -153,15 +153,15 @@
         )
     except (AttributeError, KeyError, TypeError, json.decoder.JSONDecodeError):
         return {}
 
 
 def dicom_rb_series(input_task: Dict, output_task: Dict) -> None:
     """Get standard rb flat format, same as import format."""
-    # pylint: disable=too-many-branches, too-many-statements
+    # pylint: disable=too-many-branches, too-many-statements, too-many-locals
     labels = input_task.get("labels", []) or []
     labels_map = input_task.get("labelsMap", []) or []
     series = output_task["series"]
     for volume_index, label_map in enumerate(labels_map):
         if volume_index >= len(series):
             series.extend([{} for _ in range(volume_index - len(series) + 1)])
         if label_map and label_map.get("labelName"):
@@ -214,28 +214,43 @@
                     "frameIndex": label["frameindex"],
                     "trackId": label.get("trackid", ""),
                     "keyFrame": label.get("keyframe", True),
                     "endTrack": label.get("end", True),
                 }
             }
 
+        items: List[str] = volume.get("items", []) or []
+
         measurement_stats = {}
         if label.get("stats"):
             measurement_stats = {"stats": label["stats"]}
 
         if label.get("tasklevelclassify") or label.get("studyclassify"):
             output_task["classification"] = {**label_obj}
         elif label.get("multiclassify") or label.get("seriesclassify"):
             volume["classifications"] = volume.get("classifications", []) or []
             volume["classifications"].append(
                 {
                     **label_obj,
                     **video_metadata,
                 }
             )
+        elif label.get("instanceclassify"):
+            volume["instanceClassifications"] = (
+                volume.get("instanceClassifications", []) or []
+            )
+            volume["instanceClassifications"].append(
+                {
+                    "fileIndex": label["frameindex"],
+                    "fileName": items[label["frameindex"]]
+                    if label["frameindex"] < len(items)
+                    else "",
+                    "values": label_obj["attributes"] or {},
+                }
+            )
         elif label.get("dicom", {}).get("instanceid"):
             volume_indices = (
                 [label["volumeindex"]]
                 if isinstance(label.get("volumeindex"), int)
                 and 0 <= label["volumeindex"] < len(series)
                 else list(range(len(series)))
             )
```

### Comparing `redbrick-sdk-2.9.0/redbrick/utils/rb_tax_utils.py` & `redbrick-sdk-2.9.1/redbrick/utils/rb_tax_utils.py`

 * *Files identical despite different names*

### Comparing `redbrick-sdk-2.9.0/redbrick/utils/upload.py` & `redbrick-sdk-2.9.1/redbrick/utils/upload.py`

 * *Files identical despite different names*

### Comparing `redbrick-sdk-2.9.0/redbrick/version_check.py` & `redbrick-sdk-2.9.1/redbrick/version_check.py`

 * *Files identical despite different names*

### Comparing `redbrick-sdk-2.9.0/redbrick_sdk.egg-info/PKG-INFO` & `redbrick-sdk-2.9.1/redbrick_sdk.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: redbrick-sdk
-Version: 2.9.0
+Version: 2.9.1
 Summary: RedBrick platform Python SDK!
 Home-page: https://github.com/redbrick-ai/redbrick-sdk
 License: UNKNOWN
 Description: This is an SDK to make integration with the RedBrick AI platform as easy as possible. This includes uploading and downloading data
         as well as making your datasets easily available for training. Use this SDK to access your data and labels anywhere you run your code, whether that is on the cloud or locally with a Jupyter Notebook.
         
         Please feel free to submit issues on github or at [support@redbrickai.com](mailto:support@redbrickai.com) if you run into any problems or have suggestions.
```

### Comparing `redbrick-sdk-2.9.0/redbrick_sdk.egg-info/SOURCES.txt` & `redbrick-sdk-2.9.1/redbrick_sdk.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `redbrick-sdk-2.9.0/redbrick_sdk.egg-info/requires.txt` & `redbrick-sdk-2.9.1/redbrick_sdk.egg-info/requires.txt`

 * *Files identical despite different names*

### Comparing `redbrick-sdk-2.9.0/setup.cfg` & `redbrick-sdk-2.9.1/setup.cfg`

 * *Files identical despite different names*

### Comparing `redbrick-sdk-2.9.0/setup.py` & `redbrick-sdk-2.9.1/setup.py`

 * *Files identical despite different names*

