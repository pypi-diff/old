# Comparing `tmp/montecarlodata-0.9.1.tar.gz` & `tmp/montecarlodata-0.9.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/montecarlodata-0.9.1.tar", last modified: Wed Sep  1 18:22:12 2021, max compression
+gzip compressed data, was "dist/montecarlodata-0.9.2.tar", last modified: Tue Sep  7 18:37:01 2021, max compression
```

## Comparing `montecarlodata-0.9.1.tar` & `montecarlodata-0.9.2.tar`

### file list

```diff
@@ -1,77 +1,77 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-09-01 18:22:12.120195 montecarlodata-0.9.1/
--rw-r--r--   0 root         (0) root         (0)    11357 2021-09-01 18:21:59.000000 montecarlodata-0.9.1/LICENSE
--rw-r--r--   0 root         (0) root         (0)     7041 2021-09-01 18:22:12.120195 montecarlodata-0.9.1/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)     6345 2021-09-01 18:21:59.000000 montecarlodata-0.9.1/README.md
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-09-01 18:22:12.116195 montecarlodata-0.9.1/montecarlodata/
--rw-r--r--   0 root         (0) root         (0)        0 2021-09-01 18:21:59.000000 montecarlodata-0.9.1/montecarlodata/__init__.py
--rw-r--r--   0 root         (0) root         (0)     3331 2021-09-01 18:21:59.000000 montecarlodata-0.9.1/montecarlodata/cli.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-09-01 18:22:12.116195 montecarlodata-0.9.1/montecarlodata/collector/
--rw-r--r--   0 root         (0) root         (0)        0 2021-09-01 18:21:59.000000 montecarlodata-0.9.1/montecarlodata/collector/__init__.py
--rw-r--r--   0 root         (0) root         (0)     6268 2021-09-01 18:21:59.000000 montecarlodata-0.9.1/montecarlodata/collector/commands.py
--rw-r--r--   0 root         (0) root         (0)      523 2021-09-01 18:21:59.000000 montecarlodata-0.9.1/montecarlodata/collector/fields.py
--rw-r--r--   0 root         (0) root         (0)     9844 2021-09-01 18:21:59.000000 montecarlodata-0.9.1/montecarlodata/collector/management.py
--rw-r--r--   0 root         (0) root         (0)     1541 2021-09-01 18:21:59.000000 montecarlodata-0.9.1/montecarlodata/collector/network_tests.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-09-01 18:22:12.116195 montecarlodata-0.9.1/montecarlodata/common/
--rw-r--r--   0 root         (0) root         (0)        0 2021-09-01 18:21:59.000000 montecarlodata-0.9.1/montecarlodata/common/__init__.py
--rw-r--r--   0 root         (0) root         (0)      337 2021-09-01 18:21:59.000000 montecarlodata-0.9.1/montecarlodata/common/commands.py
--rw-r--r--   0 root         (0) root         (0)      271 2021-09-01 18:21:59.000000 montecarlodata-0.9.1/montecarlodata/common/common.py
--rw-r--r--   0 root         (0) root         (0)     1963 2021-09-01 18:21:59.000000 montecarlodata-0.9.1/montecarlodata/common/data.py
--rw-r--r--   0 root         (0) root         (0)     6460 2021-09-01 18:21:59.000000 montecarlodata-0.9.1/montecarlodata/common/resources.py
--rw-r--r--   0 root         (0) root         (0)     2729 2021-09-01 18:21:59.000000 montecarlodata-0.9.1/montecarlodata/common/user.py
--rw-r--r--   0 root         (0) root         (0)     2162 2021-09-01 18:21:59.000000 montecarlodata-0.9.1/montecarlodata/config.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-09-01 18:22:12.120195 montecarlodata-0.9.1/montecarlodata/discovery/
--rw-r--r--   0 root         (0) root         (0)        0 2021-09-01 18:21:59.000000 montecarlodata-0.9.1/montecarlodata/discovery/__init__.py
--rw-r--r--   0 root         (0) root         (0)     1909 2021-09-01 18:21:59.000000 montecarlodata-0.9.1/montecarlodata/discovery/commands.py
--rw-r--r--   0 root         (0) root         (0)     1768 2021-09-01 18:21:59.000000 montecarlodata-0.9.1/montecarlodata/errors.py
--rw-r--r--   0 root         (0) root         (0)      100 2021-09-01 18:21:59.000000 montecarlodata-0.9.1/montecarlodata/fs_utils.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-09-01 18:22:12.120195 montecarlodata-0.9.1/montecarlodata/iac/
--rw-r--r--   0 root         (0) root         (0)        0 2021-09-01 18:21:59.000000 montecarlodata-0.9.1/montecarlodata/iac/__init__.py
--rw-r--r--   0 root         (0) root         (0)     1760 2021-09-01 18:21:59.000000 montecarlodata-0.9.1/montecarlodata/iac/client.py
--rw-r--r--   0 root         (0) root         (0)     2101 2021-09-01 18:21:59.000000 montecarlodata-0.9.1/montecarlodata/iac/commands.py
--rw-r--r--   0 root         (0) root         (0)     9102 2021-09-01 18:21:59.000000 montecarlodata-0.9.1/montecarlodata/iac/mc_config_service.py
--rw-r--r--   0 root         (0) root         (0)     1769 2021-09-01 18:21:59.000000 montecarlodata-0.9.1/montecarlodata/iac/schemas.py
--rw-r--r--   0 root         (0) root         (0)     1175 2021-09-01 18:21:59.000000 montecarlodata-0.9.1/montecarlodata/iac/utils.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-09-01 18:22:12.120195 montecarlodata-0.9.1/montecarlodata/integrations/
--rw-r--r--   0 root         (0) root         (0)        0 2021-09-01 18:21:59.000000 montecarlodata-0.9.1/montecarlodata/integrations/__init__.py
--rw-r--r--   0 root         (0) root         (0)    22765 2021-09-01 18:21:59.000000 montecarlodata-0.9.1/montecarlodata/integrations/commands.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-09-01 18:22:12.120195 montecarlodata-0.9.1/montecarlodata/integrations/info/
--rw-r--r--   0 root         (0) root         (0)        0 2021-09-01 18:21:59.000000 montecarlodata-0.9.1/montecarlodata/integrations/info/__init__.py
--rw-r--r--   0 root         (0) root         (0)     2850 2021-09-01 18:21:59.000000 montecarlodata-0.9.1/montecarlodata/integrations/info/status.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-09-01 18:22:12.120195 montecarlodata-0.9.1/montecarlodata/integrations/onboarding/
--rw-r--r--   0 root         (0) root         (0)        0 2021-09-01 18:21:59.000000 montecarlodata-0.9.1/montecarlodata/integrations/onboarding/__init__.py
--rw-r--r--   0 root         (0) root         (0)     9378 2021-09-01 18:21:59.000000 montecarlodata-0.9.1/montecarlodata/integrations/onboarding/base.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-09-01 18:22:12.120195 montecarlodata-0.9.1/montecarlodata/integrations/onboarding/bi/
--rw-r--r--   0 root         (0) root         (0)        0 2021-09-01 18:21:59.000000 montecarlodata-0.9.1/montecarlodata/integrations/onboarding/bi/__init__.py
--rw-r--r--   0 root         (0) root         (0)     3700 2021-09-01 18:21:59.000000 montecarlodata-0.9.1/montecarlodata/integrations/onboarding/bi/reports.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-09-01 18:22:12.120195 montecarlodata-0.9.1/montecarlodata/integrations/onboarding/data_lake/
--rw-r--r--   0 root         (0) root         (0)        0 2021-09-01 18:21:59.000000 montecarlodata-0.9.1/montecarlodata/integrations/onboarding/data_lake/__init__.py
--rw-r--r--   0 root         (0) root         (0)     1486 2021-09-01 18:21:59.000000 montecarlodata-0.9.1/montecarlodata/integrations/onboarding/data_lake/events.py
--rw-r--r--   0 root         (0) root         (0)     1346 2021-09-01 18:21:59.000000 montecarlodata-0.9.1/montecarlodata/integrations/onboarding/data_lake/glue_athena.py
--rw-r--r--   0 root         (0) root         (0)     2514 2021-09-01 18:21:59.000000 montecarlodata-0.9.1/montecarlodata/integrations/onboarding/data_lake/hive.py
--rw-r--r--   0 root         (0) root         (0)     1653 2021-09-01 18:21:59.000000 montecarlodata-0.9.1/montecarlodata/integrations/onboarding/data_lake/presto.py
--rw-r--r--   0 root         (0) root         (0)     1464 2021-09-01 18:21:59.000000 montecarlodata-0.9.1/montecarlodata/integrations/onboarding/data_lake/spark.py
--rw-r--r--   0 root         (0) root         (0)     3941 2021-09-01 18:21:59.000000 montecarlodata-0.9.1/montecarlodata/integrations/onboarding/fields.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-09-01 18:22:12.120195 montecarlodata-0.9.1/montecarlodata/integrations/onboarding/operations/
--rw-r--r--   0 root         (0) root         (0)        0 2021-09-01 18:21:59.000000 montecarlodata-0.9.1/montecarlodata/integrations/onboarding/operations/__init__.py
--rw-r--r--   0 root         (0) root         (0)     3277 2021-09-01 18:21:59.000000 montecarlodata-0.9.1/montecarlodata/integrations/onboarding/operations/connection_ops.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-09-01 18:22:12.120195 montecarlodata-0.9.1/montecarlodata/integrations/onboarding/warehouse/
--rw-r--r--   0 root         (0) root         (0)        0 2021-09-01 18:21:59.000000 montecarlodata-0.9.1/montecarlodata/integrations/onboarding/warehouse/__init__.py
--rw-r--r--   0 root         (0) root         (0)     2355 2021-09-01 18:21:59.000000 montecarlodata-0.9.1/montecarlodata/integrations/onboarding/warehouse/warehouses.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-09-01 18:22:12.120195 montecarlodata-0.9.1/montecarlodata/queries/
--rw-r--r--   0 root         (0) root         (0)        0 2021-09-01 18:21:59.000000 montecarlodata-0.9.1/montecarlodata/queries/__init__.py
--rw-r--r--   0 root         (0) root         (0)      972 2021-09-01 18:21:59.000000 montecarlodata-0.9.1/montecarlodata/queries/collector.py
--rw-r--r--   0 root         (0) root         (0)      810 2021-09-01 18:21:59.000000 montecarlodata-0.9.1/montecarlodata/queries/iac.py
--rw-r--r--   0 root         (0) root         (0)     7963 2021-09-01 18:21:59.000000 montecarlodata-0.9.1/montecarlodata/queries/onboarding.py
--rw-r--r--   0 root         (0) root         (0)      912 2021-09-01 18:21:59.000000 montecarlodata-0.9.1/montecarlodata/queries/user.py
--rw-r--r--   0 root         (0) root         (0)     1546 2021-09-01 18:21:59.000000 montecarlodata-0.9.1/montecarlodata/settings.py
--rw-r--r--   0 root         (0) root         (0)     4415 2021-09-01 18:21:59.000000 montecarlodata-0.9.1/montecarlodata/tools.py
--rw-r--r--   0 root         (0) root         (0)     9268 2021-09-01 18:21:59.000000 montecarlodata-0.9.1/montecarlodata/utils.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-09-01 18:22:12.116195 montecarlodata-0.9.1/montecarlodata.egg-info/
--rw-r--r--   0 root         (0) root         (0)     7041 2021-09-01 18:22:12.000000 montecarlodata-0.9.1/montecarlodata.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)     2318 2021-09-01 18:22:12.000000 montecarlodata-0.9.1/montecarlodata.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2021-09-01 18:22:12.000000 montecarlodata-0.9.1/montecarlodata.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)       81 2021-09-01 18:22:12.000000 montecarlodata-0.9.1/montecarlodata.egg-info/entry_points.txt
--rw-r--r--   0 root         (0) root         (0)      494 2021-09-01 18:22:12.000000 montecarlodata-0.9.1/montecarlodata.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)       15 2021-09-01 18:22:12.000000 montecarlodata-0.9.1/montecarlodata.egg-info/top_level.txt
--rw-r--r--   0 root         (0) root         (0)       79 2021-09-01 18:22:12.120195 montecarlodata-0.9.1/setup.cfg
--rw-r--r--   0 root         (0) root         (0)     1430 2021-09-01 18:21:59.000000 montecarlodata-0.9.1/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-09-07 18:37:01.450244 montecarlodata-0.9.2/
+-rw-r--r--   0 root         (0) root         (0)    11357 2021-09-07 18:36:48.000000 montecarlodata-0.9.2/LICENSE
+-rw-r--r--   0 root         (0) root         (0)     7041 2021-09-07 18:37:01.450244 montecarlodata-0.9.2/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)     6345 2021-09-07 18:36:48.000000 montecarlodata-0.9.2/README.md
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-09-07 18:37:01.446244 montecarlodata-0.9.2/montecarlodata/
+-rw-r--r--   0 root         (0) root         (0)        0 2021-09-07 18:36:48.000000 montecarlodata-0.9.2/montecarlodata/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     3331 2021-09-07 18:36:48.000000 montecarlodata-0.9.2/montecarlodata/cli.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-09-07 18:37:01.446244 montecarlodata-0.9.2/montecarlodata/collector/
+-rw-r--r--   0 root         (0) root         (0)        0 2021-09-07 18:36:48.000000 montecarlodata-0.9.2/montecarlodata/collector/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     6268 2021-09-07 18:36:48.000000 montecarlodata-0.9.2/montecarlodata/collector/commands.py
+-rw-r--r--   0 root         (0) root         (0)      523 2021-09-07 18:36:48.000000 montecarlodata-0.9.2/montecarlodata/collector/fields.py
+-rw-r--r--   0 root         (0) root         (0)     9844 2021-09-07 18:36:48.000000 montecarlodata-0.9.2/montecarlodata/collector/management.py
+-rw-r--r--   0 root         (0) root         (0)     1541 2021-09-07 18:36:48.000000 montecarlodata-0.9.2/montecarlodata/collector/network_tests.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-09-07 18:37:01.446244 montecarlodata-0.9.2/montecarlodata/common/
+-rw-r--r--   0 root         (0) root         (0)        0 2021-09-07 18:36:48.000000 montecarlodata-0.9.2/montecarlodata/common/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      337 2021-09-07 18:36:48.000000 montecarlodata-0.9.2/montecarlodata/common/commands.py
+-rw-r--r--   0 root         (0) root         (0)      271 2021-09-07 18:36:48.000000 montecarlodata-0.9.2/montecarlodata/common/common.py
+-rw-r--r--   0 root         (0) root         (0)     1963 2021-09-07 18:36:48.000000 montecarlodata-0.9.2/montecarlodata/common/data.py
+-rw-r--r--   0 root         (0) root         (0)     6460 2021-09-07 18:36:48.000000 montecarlodata-0.9.2/montecarlodata/common/resources.py
+-rw-r--r--   0 root         (0) root         (0)     2729 2021-09-07 18:36:48.000000 montecarlodata-0.9.2/montecarlodata/common/user.py
+-rw-r--r--   0 root         (0) root         (0)     2162 2021-09-07 18:36:48.000000 montecarlodata-0.9.2/montecarlodata/config.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-09-07 18:37:01.446244 montecarlodata-0.9.2/montecarlodata/discovery/
+-rw-r--r--   0 root         (0) root         (0)        0 2021-09-07 18:36:48.000000 montecarlodata-0.9.2/montecarlodata/discovery/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     1909 2021-09-07 18:36:48.000000 montecarlodata-0.9.2/montecarlodata/discovery/commands.py
+-rw-r--r--   0 root         (0) root         (0)     1768 2021-09-07 18:36:48.000000 montecarlodata-0.9.2/montecarlodata/errors.py
+-rw-r--r--   0 root         (0) root         (0)      100 2021-09-07 18:36:48.000000 montecarlodata-0.9.2/montecarlodata/fs_utils.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-09-07 18:37:01.446244 montecarlodata-0.9.2/montecarlodata/iac/
+-rw-r--r--   0 root         (0) root         (0)        0 2021-09-07 18:36:48.000000 montecarlodata-0.9.2/montecarlodata/iac/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     1760 2021-09-07 18:36:48.000000 montecarlodata-0.9.2/montecarlodata/iac/client.py
+-rw-r--r--   0 root         (0) root         (0)     2101 2021-09-07 18:36:48.000000 montecarlodata-0.9.2/montecarlodata/iac/commands.py
+-rw-r--r--   0 root         (0) root         (0)     9102 2021-09-07 18:36:48.000000 montecarlodata-0.9.2/montecarlodata/iac/mc_config_service.py
+-rw-r--r--   0 root         (0) root         (0)     1769 2021-09-07 18:36:48.000000 montecarlodata-0.9.2/montecarlodata/iac/schemas.py
+-rw-r--r--   0 root         (0) root         (0)     1175 2021-09-07 18:36:48.000000 montecarlodata-0.9.2/montecarlodata/iac/utils.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-09-07 18:37:01.446244 montecarlodata-0.9.2/montecarlodata/integrations/
+-rw-r--r--   0 root         (0) root         (0)        0 2021-09-07 18:36:48.000000 montecarlodata-0.9.2/montecarlodata/integrations/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    22781 2021-09-07 18:36:48.000000 montecarlodata-0.9.2/montecarlodata/integrations/commands.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-09-07 18:37:01.446244 montecarlodata-0.9.2/montecarlodata/integrations/info/
+-rw-r--r--   0 root         (0) root         (0)        0 2021-09-07 18:36:48.000000 montecarlodata-0.9.2/montecarlodata/integrations/info/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     2850 2021-09-07 18:36:48.000000 montecarlodata-0.9.2/montecarlodata/integrations/info/status.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-09-07 18:37:01.450244 montecarlodata-0.9.2/montecarlodata/integrations/onboarding/
+-rw-r--r--   0 root         (0) root         (0)        0 2021-09-07 18:36:48.000000 montecarlodata-0.9.2/montecarlodata/integrations/onboarding/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     9378 2021-09-07 18:36:48.000000 montecarlodata-0.9.2/montecarlodata/integrations/onboarding/base.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-09-07 18:37:01.450244 montecarlodata-0.9.2/montecarlodata/integrations/onboarding/bi/
+-rw-r--r--   0 root         (0) root         (0)        0 2021-09-07 18:36:48.000000 montecarlodata-0.9.2/montecarlodata/integrations/onboarding/bi/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     3700 2021-09-07 18:36:48.000000 montecarlodata-0.9.2/montecarlodata/integrations/onboarding/bi/reports.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-09-07 18:37:01.450244 montecarlodata-0.9.2/montecarlodata/integrations/onboarding/data_lake/
+-rw-r--r--   0 root         (0) root         (0)        0 2021-09-07 18:36:48.000000 montecarlodata-0.9.2/montecarlodata/integrations/onboarding/data_lake/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     1486 2021-09-07 18:36:48.000000 montecarlodata-0.9.2/montecarlodata/integrations/onboarding/data_lake/events.py
+-rw-r--r--   0 root         (0) root         (0)     1346 2021-09-07 18:36:48.000000 montecarlodata-0.9.2/montecarlodata/integrations/onboarding/data_lake/glue_athena.py
+-rw-r--r--   0 root         (0) root         (0)     2514 2021-09-07 18:36:48.000000 montecarlodata-0.9.2/montecarlodata/integrations/onboarding/data_lake/hive.py
+-rw-r--r--   0 root         (0) root         (0)     1653 2021-09-07 18:36:48.000000 montecarlodata-0.9.2/montecarlodata/integrations/onboarding/data_lake/presto.py
+-rw-r--r--   0 root         (0) root         (0)     1464 2021-09-07 18:36:48.000000 montecarlodata-0.9.2/montecarlodata/integrations/onboarding/data_lake/spark.py
+-rw-r--r--   0 root         (0) root         (0)     3941 2021-09-07 18:36:48.000000 montecarlodata-0.9.2/montecarlodata/integrations/onboarding/fields.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-09-07 18:37:01.450244 montecarlodata-0.9.2/montecarlodata/integrations/onboarding/operations/
+-rw-r--r--   0 root         (0) root         (0)        0 2021-09-07 18:36:48.000000 montecarlodata-0.9.2/montecarlodata/integrations/onboarding/operations/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     3277 2021-09-07 18:36:48.000000 montecarlodata-0.9.2/montecarlodata/integrations/onboarding/operations/connection_ops.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-09-07 18:37:01.450244 montecarlodata-0.9.2/montecarlodata/integrations/onboarding/warehouse/
+-rw-r--r--   0 root         (0) root         (0)        0 2021-09-07 18:36:48.000000 montecarlodata-0.9.2/montecarlodata/integrations/onboarding/warehouse/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     2355 2021-09-07 18:36:48.000000 montecarlodata-0.9.2/montecarlodata/integrations/onboarding/warehouse/warehouses.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-09-07 18:37:01.450244 montecarlodata-0.9.2/montecarlodata/queries/
+-rw-r--r--   0 root         (0) root         (0)        0 2021-09-07 18:36:48.000000 montecarlodata-0.9.2/montecarlodata/queries/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      972 2021-09-07 18:36:48.000000 montecarlodata-0.9.2/montecarlodata/queries/collector.py
+-rw-r--r--   0 root         (0) root         (0)      810 2021-09-07 18:36:48.000000 montecarlodata-0.9.2/montecarlodata/queries/iac.py
+-rw-r--r--   0 root         (0) root         (0)     7963 2021-09-07 18:36:48.000000 montecarlodata-0.9.2/montecarlodata/queries/onboarding.py
+-rw-r--r--   0 root         (0) root         (0)      912 2021-09-07 18:36:48.000000 montecarlodata-0.9.2/montecarlodata/queries/user.py
+-rw-r--r--   0 root         (0) root         (0)     1546 2021-09-07 18:36:48.000000 montecarlodata-0.9.2/montecarlodata/settings.py
+-rw-r--r--   0 root         (0) root         (0)     4415 2021-09-07 18:36:48.000000 montecarlodata-0.9.2/montecarlodata/tools.py
+-rw-r--r--   0 root         (0) root         (0)     9268 2021-09-07 18:36:48.000000 montecarlodata-0.9.2/montecarlodata/utils.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2021-09-07 18:37:01.446244 montecarlodata-0.9.2/montecarlodata.egg-info/
+-rw-r--r--   0 root         (0) root         (0)     7041 2021-09-07 18:37:01.000000 montecarlodata-0.9.2/montecarlodata.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)     2318 2021-09-07 18:37:01.000000 montecarlodata-0.9.2/montecarlodata.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2021-09-07 18:37:01.000000 montecarlodata-0.9.2/montecarlodata.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)       81 2021-09-07 18:37:01.000000 montecarlodata-0.9.2/montecarlodata.egg-info/entry_points.txt
+-rw-r--r--   0 root         (0) root         (0)      494 2021-09-07 18:37:01.000000 montecarlodata-0.9.2/montecarlodata.egg-info/requires.txt
+-rw-r--r--   0 root         (0) root         (0)       15 2021-09-07 18:37:01.000000 montecarlodata-0.9.2/montecarlodata.egg-info/top_level.txt
+-rw-r--r--   0 root         (0) root         (0)       79 2021-09-07 18:37:01.450244 montecarlodata-0.9.2/setup.cfg
+-rw-r--r--   0 root         (0) root         (0)     1430 2021-09-07 18:36:48.000000 montecarlodata-0.9.2/setup.py
```

### Comparing `montecarlodata-0.9.1/LICENSE` & `montecarlodata-0.9.2/LICENSE`

 * *Files identical despite different names*

### Comparing `montecarlodata-0.9.1/PKG-INFO` & `montecarlodata-0.9.2/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: montecarlodata
-Version: 0.9.1
+Version: 0.9.2
 Summary: Monte Carlo's CLI
 Home-page: https://www.montecarlodata.com/
 Author: Monte Carlo Data, Inc
 Author-email: info@montecarlodata.com
 License: Apache Software License (Apache 2.0)
 Platform: UNKNOWN
 Classifier: Development Status :: 3 - Alpha
```

### Comparing `montecarlodata-0.9.1/README.md` & `montecarlodata-0.9.2/README.md`

 * *Files identical despite different names*

### Comparing `montecarlodata-0.9.1/montecarlodata/cli.py` & `montecarlodata-0.9.2/montecarlodata/cli.py`

 * *Files identical despite different names*

### Comparing `montecarlodata-0.9.1/montecarlodata/collector/commands.py` & `montecarlodata-0.9.2/montecarlodata/collector/commands.py`

 * *Files identical despite different names*

### Comparing `montecarlodata-0.9.1/montecarlodata/collector/fields.py` & `montecarlodata-0.9.2/montecarlodata/collector/fields.py`

 * *Files identical despite different names*

### Comparing `montecarlodata-0.9.1/montecarlodata/collector/management.py` & `montecarlodata-0.9.2/montecarlodata/collector/management.py`

 * *Files identical despite different names*

### Comparing `montecarlodata-0.9.1/montecarlodata/collector/network_tests.py` & `montecarlodata-0.9.2/montecarlodata/collector/network_tests.py`

 * *Files identical despite different names*

### Comparing `montecarlodata-0.9.1/montecarlodata/common/data.py` & `montecarlodata-0.9.2/montecarlodata/common/data.py`

 * *Files identical despite different names*

### Comparing `montecarlodata-0.9.1/montecarlodata/common/resources.py` & `montecarlodata-0.9.2/montecarlodata/common/resources.py`

 * *Files identical despite different names*

### Comparing `montecarlodata-0.9.1/montecarlodata/common/user.py` & `montecarlodata-0.9.2/montecarlodata/common/user.py`

 * *Files identical despite different names*

### Comparing `montecarlodata-0.9.1/montecarlodata/config.py` & `montecarlodata-0.9.2/montecarlodata/config.py`

 * *Files identical despite different names*

### Comparing `montecarlodata-0.9.1/montecarlodata/discovery/commands.py` & `montecarlodata-0.9.2/montecarlodata/discovery/commands.py`

 * *Files identical despite different names*

### Comparing `montecarlodata-0.9.1/montecarlodata/errors.py` & `montecarlodata-0.9.2/montecarlodata/errors.py`

 * *Files identical despite different names*

### Comparing `montecarlodata-0.9.1/montecarlodata/iac/client.py` & `montecarlodata-0.9.2/montecarlodata/iac/client.py`

 * *Files identical despite different names*

### Comparing `montecarlodata-0.9.1/montecarlodata/iac/commands.py` & `montecarlodata-0.9.2/montecarlodata/iac/commands.py`

 * *Files identical despite different names*

### Comparing `montecarlodata-0.9.1/montecarlodata/iac/mc_config_service.py` & `montecarlodata-0.9.2/montecarlodata/iac/mc_config_service.py`

 * *Files identical despite different names*

### Comparing `montecarlodata-0.9.1/montecarlodata/iac/schemas.py` & `montecarlodata-0.9.2/montecarlodata/iac/schemas.py`

 * *Files identical despite different names*

### Comparing `montecarlodata-0.9.1/montecarlodata/iac/utils.py` & `montecarlodata-0.9.2/montecarlodata/iac/utils.py`

 * *Files identical despite different names*

### Comparing `montecarlodata-0.9.1/montecarlodata/integrations/commands.py` & `montecarlodata-0.9.2/montecarlodata/integrations/commands.py`

 * *Files 1% similar despite different names*

```diff
@@ -66,16 +66,16 @@
 NETWORK_OPTIONS = [
     click.option('--test-network-only', 'skip_permission_tests', is_flag=True, default=False, show_default=True,
                  cls=AdvancedOptions, mutually_exclusive_options=['skip_validation'],
                  help='Skip any permission tests. Only validates network connection between the collector and resource can be established.')
 ]
 
 BI_OPTIONS = [
-    click.option('--verify-ssl', help='Whether to verify the SSL connection (uncheck for self-signed certs).',
-                 required=False, is_flag=True, default=True, show_default=True)
+    click.option('--verify-ssl/--no-verify-ssl', 'verify_ssl', required=False, default=True, show_default=True,
+                 help='Whether to verify the SSL connection (uncheck for self-signed certs).')
 ]
 
 
 @click.group(help='Manage or integrate an asset with Monte Carlo.')
 def integrations():
     """
     Group for any integration related subcommands
```

### Comparing `montecarlodata-0.9.1/montecarlodata/integrations/info/status.py` & `montecarlodata-0.9.2/montecarlodata/integrations/info/status.py`

 * *Files identical despite different names*

### Comparing `montecarlodata-0.9.1/montecarlodata/integrations/onboarding/base.py` & `montecarlodata-0.9.2/montecarlodata/integrations/onboarding/base.py`

 * *Files identical despite different names*

### Comparing `montecarlodata-0.9.1/montecarlodata/integrations/onboarding/bi/reports.py` & `montecarlodata-0.9.2/montecarlodata/integrations/onboarding/bi/reports.py`

 * *Files identical despite different names*

### Comparing `montecarlodata-0.9.1/montecarlodata/integrations/onboarding/data_lake/events.py` & `montecarlodata-0.9.2/montecarlodata/integrations/onboarding/data_lake/events.py`

 * *Files identical despite different names*

### Comparing `montecarlodata-0.9.1/montecarlodata/integrations/onboarding/data_lake/glue_athena.py` & `montecarlodata-0.9.2/montecarlodata/integrations/onboarding/data_lake/glue_athena.py`

 * *Files identical despite different names*

### Comparing `montecarlodata-0.9.1/montecarlodata/integrations/onboarding/data_lake/hive.py` & `montecarlodata-0.9.2/montecarlodata/integrations/onboarding/data_lake/hive.py`

 * *Files identical despite different names*

### Comparing `montecarlodata-0.9.1/montecarlodata/integrations/onboarding/data_lake/presto.py` & `montecarlodata-0.9.2/montecarlodata/integrations/onboarding/data_lake/presto.py`

 * *Files identical despite different names*

### Comparing `montecarlodata-0.9.1/montecarlodata/integrations/onboarding/data_lake/spark.py` & `montecarlodata-0.9.2/montecarlodata/integrations/onboarding/data_lake/spark.py`

 * *Files identical despite different names*

### Comparing `montecarlodata-0.9.1/montecarlodata/integrations/onboarding/fields.py` & `montecarlodata-0.9.2/montecarlodata/integrations/onboarding/fields.py`

 * *Files identical despite different names*

### Comparing `montecarlodata-0.9.1/montecarlodata/integrations/onboarding/operations/connection_ops.py` & `montecarlodata-0.9.2/montecarlodata/integrations/onboarding/operations/connection_ops.py`

 * *Files identical despite different names*

### Comparing `montecarlodata-0.9.1/montecarlodata/integrations/onboarding/warehouse/warehouses.py` & `montecarlodata-0.9.2/montecarlodata/integrations/onboarding/warehouse/warehouses.py`

 * *Files identical despite different names*

### Comparing `montecarlodata-0.9.1/montecarlodata/queries/collector.py` & `montecarlodata-0.9.2/montecarlodata/queries/collector.py`

 * *Files identical despite different names*

### Comparing `montecarlodata-0.9.1/montecarlodata/queries/iac.py` & `montecarlodata-0.9.2/montecarlodata/queries/iac.py`

 * *Files identical despite different names*

### Comparing `montecarlodata-0.9.1/montecarlodata/queries/onboarding.py` & `montecarlodata-0.9.2/montecarlodata/queries/onboarding.py`

 * *Files identical despite different names*

### Comparing `montecarlodata-0.9.1/montecarlodata/queries/user.py` & `montecarlodata-0.9.2/montecarlodata/queries/user.py`

 * *Files identical despite different names*

### Comparing `montecarlodata-0.9.1/montecarlodata/settings.py` & `montecarlodata-0.9.2/montecarlodata/settings.py`

 * *Files identical despite different names*

### Comparing `montecarlodata-0.9.1/montecarlodata/tools.py` & `montecarlodata-0.9.2/montecarlodata/tools.py`

 * *Files identical despite different names*

### Comparing `montecarlodata-0.9.1/montecarlodata/utils.py` & `montecarlodata-0.9.2/montecarlodata/utils.py`

 * *Files identical despite different names*

### Comparing `montecarlodata-0.9.1/montecarlodata.egg-info/PKG-INFO` & `montecarlodata-0.9.2/montecarlodata.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: montecarlodata
-Version: 0.9.1
+Version: 0.9.2
 Summary: Monte Carlo's CLI
 Home-page: https://www.montecarlodata.com/
 Author: Monte Carlo Data, Inc
 Author-email: info@montecarlodata.com
 License: Apache Software License (Apache 2.0)
 Platform: UNKNOWN
 Classifier: Development Status :: 3 - Alpha
```

### Comparing `montecarlodata-0.9.1/montecarlodata.egg-info/SOURCES.txt` & `montecarlodata-0.9.2/montecarlodata.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `montecarlodata-0.9.1/setup.py` & `montecarlodata-0.9.2/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 import distutils.text_file
 from pathlib import Path
 from typing import List, Optional
 
 from setuptools import setup, find_packages
 
-__VERSION__ = '0.9.1'
+__VERSION__ = '0.9.2'
 
 
 def parse_requirements(file_name: Optional[str] = 'requirements.txt') -> List[str]:
     return distutils.text_file.TextFile(filename=str(Path(__file__).with_name(file_name))).readlines()
 
 
 def get_long_description():
```

