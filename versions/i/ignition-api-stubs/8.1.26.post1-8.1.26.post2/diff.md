# Comparing `tmp/ignition_api_stubs-8.1.26.post1.tar.gz` & `tmp/ignition_api_stubs-8.1.26.post2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "ignition_api_stubs-8.1.26.post1.tar", last modified: Wed Apr  5 06:44:37 2023, max compression
+gzip compressed data, was "ignition_api_stubs-8.1.26.post2.tar", last modified: Thu Apr  6 23:22:20 2023, max compression
```

## Comparing `ignition_api_stubs-8.1.26.post1.tar` & `ignition_api_stubs-8.1.26.post2.tar`

### file list

```diff
@@ -1,405 +1,405 @@
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.511338 ignition_api_stubs-8.1.26.post1/
--rw-r--r--   0 runner    (1001) docker     (122)     6555 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/CHANGELOG.md
--rw-r--r--   0 runner    (1001) docker     (122)     1070 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/LICENSE
--rw-r--r--   0 runner    (1001) docker     (122)       21 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (122)     4636 2023-04-05 06:44:37.511338 ignition_api_stubs-8.1.26.post1/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (122)     2031 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/README.md
--rw-r--r--   0 runner    (1001) docker     (122)     1593 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (122)       38 2023-04-05 06:44:37.511338 ignition_api_stubs-8.1.26.post1/setup.cfg
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.475336 ignition_api_stubs-8.1.26.post1/stubs/
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.479336 ignition_api_stubs-8.1.26.post1/stubs/ch/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/ch/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.479336 ignition_api_stubs-8.1.26.post1/stubs/ch/qos/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/ch/qos/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.479336 ignition_api_stubs-8.1.26.post1/stubs/ch/qos/logback/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/ch/qos/logback/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.479336 ignition_api_stubs-8.1.26.post1/stubs/ch/qos/logback/classic/
--rw-r--r--   0 runner    (1001) docker     (122)      650 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/ch/qos/logback/classic/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.479336 ignition_api_stubs-8.1.26.post1/stubs/com/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.479336 ignition_api_stubs-8.1.26.post1/stubs/com/codahale/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/codahale/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.479336 ignition_api_stubs-8.1.26.post1/stubs/com/codahale/metrics/
--rw-r--r--   0 runner    (1001) docker     (122)     1271 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/codahale/metrics/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.479336 ignition_api_stubs-8.1.26.post1/stubs/com/google/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/google/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.479336 ignition_api_stubs-8.1.26.post1/stubs/com/google/common/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/google/common/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.479336 ignition_api_stubs-8.1.26.post1/stubs/com/google/common/collect/
--rw-r--r--   0 runner    (1001) docker     (122)     2204 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/google/common/collect/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.479336 ignition_api_stubs-8.1.26.post1/stubs/com/google/common/eventbus/
--rw-r--r--   0 runner    (1001) docker     (122)      359 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/google/common/eventbus/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.479336 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.479336 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/factorypmi/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/factorypmi/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.479336 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/factorypmi/application/
--rw-r--r--   0 runner    (1001) docker     (122)     1780 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/factorypmi/application/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.479336 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/factorypmi/application/binding/
--rw-r--r--   0 runner    (1001) docker     (122)      875 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/factorypmi/application/binding/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.479336 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/factorypmi/application/components/
--rw-r--r--   0 runner    (1001) docker     (122)      285 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/factorypmi/application/components/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.479336 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/factorypmi/application/model/
--rw-r--r--   0 runner    (1001) docker     (122)      193 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/factorypmi/application/model/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.479336 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/factorypmi/application/script/
--rw-r--r--   0 runner    (1001) docker     (122)      260 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/factorypmi/application/script/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.479336 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/factorypmi/application/script/builtin/
--rw-r--r--   0 runner    (1001) docker     (122)     7676 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/factorypmi/application/script/builtin/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.479336 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/factorypmi/application/sqltags/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/factorypmi/application/sqltags/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.479336 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/factorypmi/application/sqltags/project/
--rw-r--r--   0 runner    (1001) docker     (122)      136 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/factorypmi/application/sqltags/project/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.479336 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.483336 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/alarming/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/alarming/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.483336 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/alarming/common/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/alarming/common/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.483336 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/alarming/common/rosters/
--rw-r--r--   0 runner    (1001) docker     (122)      509 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/alarming/common/rosters/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.483336 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/client/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/client/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.483336 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/client/launch/
--rw-r--r--   0 runner    (1001) docker     (122)     6082 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/client/launch/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.483336 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/client/model/
--rw-r--r--   0 runner    (1001) docker     (122)     4075 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/client/model/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.483336 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/client/util/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/client/util/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.483336 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/client/util/gui/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/client/util/gui/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.483336 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/client/util/gui/progress/
--rw-r--r--   0 runner    (1001) docker     (122)     1602 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/client/util/gui/progress/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.483336 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/client/util/gui/scheduling/
--rw-r--r--   0 runner    (1001) docker     (122)     1402 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/client/util/gui/scheduling/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.483336 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/
--rw-r--r--   0 runner    (1001) docker     (122)    10487 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.483336 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/alarming/
--rw-r--r--   0 runner    (1001) docker     (122)     3228 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/alarming/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.483336 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/alarming/evaluation/
--rw-r--r--   0 runner    (1001) docker     (122)     1228 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/alarming/evaluation/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.483336 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/alarming/query/
--rw-r--r--   0 runner    (1001) docker     (122)      818 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/alarming/query/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.483336 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/binding/
--rw-r--r--   0 runner    (1001) docker     (122)       78 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/binding/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.483336 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/browsing/
--rw-r--r--   0 runner    (1001) docker     (122)     3590 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/browsing/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.483336 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/config/
--rw-r--r--   0 runner    (1001) docker     (122)     3188 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/config/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.483336 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/db/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/db/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.483336 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/db/namedquery/
--rw-r--r--   0 runner    (1001) docker     (122)      777 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/db/namedquery/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.483336 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/document/
--rw-r--r--   0 runner    (1001) docker     (122)      215 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/document/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.483336 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/execution/
--rw-r--r--   0 runner    (1001) docker     (122)     1169 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/execution/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.483336 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/expressions/
--rw-r--r--   0 runner    (1001) docker     (122)     1024 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/expressions/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.483336 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/expressions/functions/
--rw-r--r--   0 runner    (1001) docker     (122)      672 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/expressions/functions/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.483336 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/functional/
--rw-r--r--   0 runner    (1001) docker     (122)       54 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/functional/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.483336 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/gson/
--rw-r--r--   0 runner    (1001) docker     (122)     8733 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/gson/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.483336 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/gson/reflect/
--rw-r--r--   0 runner    (1001) docker     (122)      284 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/gson/reflect/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.483336 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/gson/stream/
--rw-r--r--   0 runner    (1001) docker     (122)     2056 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/gson/stream/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.487336 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/gui/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/gui/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.487336 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/gui/progress/
--rw-r--r--   0 runner    (1001) docker     (122)     1374 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/gui/progress/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.487336 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/i18n/
--rw-r--r--   0 runner    (1001) docker     (122)      925 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/i18n/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.487336 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/i18n/translation/
--rw-r--r--   0 runner    (1001) docker     (122)      242 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/i18n/translation/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.487336 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/jsonschema/
--rw-r--r--   0 runner    (1001) docker     (122)     4057 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/jsonschema/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.487336 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/licensing/
--rw-r--r--   0 runner    (1001) docker     (122)     1355 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/licensing/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.487336 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/logging/
--rw-r--r--   0 runner    (1001) docker     (122)      887 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/logging/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.487336 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/messages/
--rw-r--r--   0 runner    (1001) docker     (122)     1266 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/messages/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.487336 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/model/
--rw-r--r--   0 runner    (1001) docker     (122)     3275 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/model/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.487336 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/model/values/
--rw-r--r--   0 runner    (1001) docker     (122)     4721 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/model/values/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.487336 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/modules/
--rw-r--r--   0 runner    (1001) docker     (122)     4709 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/modules/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.487336 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/opc/
--rw-r--r--   0 runner    (1001) docker     (122)     3834 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/opc/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.487336 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/project/
--rw-r--r--   0 runner    (1001) docker     (122)     3515 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/project/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.487336 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/project/resource/
--rw-r--r--   0 runner    (1001) docker     (122)     5714 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/project/resource/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.487336 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/script/
--rw-r--r--   0 runner    (1001) docker     (122)     2556 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/script/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.487336 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/script/abc/
--rw-r--r--   0 runner    (1001) docker     (122)     4504 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/script/abc/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.487336 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/script/adapters/
--rw-r--r--   0 runner    (1001) docker     (122)     1297 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/script/adapters/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.487336 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/script/builtin/
--rw-r--r--   0 runner    (1001) docker     (122)     8422 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/script/builtin/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.487336 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/script/builtin/http/
--rw-r--r--   0 runner    (1001) docker     (122)     2702 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/script/builtin/http/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.487336 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/script/builtin/ialabs/
--rw-r--r--   0 runner    (1001) docker     (122)     1802 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/script/builtin/ialabs/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.487336 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/script/hints/
--rw-r--r--   0 runner    (1001) docker     (122)      374 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/script/hints/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.487336 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/script/message/
--rw-r--r--   0 runner    (1001) docker     (122)      594 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/script/message/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.487336 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/sqltags/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/sqltags/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.487336 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/sqltags/history/
--rw-r--r--   0 runner    (1001) docker     (122)      418 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/sqltags/history/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.487336 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/sqltags/history/annotations/
--rw-r--r--   0 runner    (1001) docker     (122)     1931 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/sqltags/history/annotations/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.487336 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/sqltags/model/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/sqltags/model/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.487336 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/sqltags/model/types/
--rw-r--r--   0 runner    (1001) docker     (122)     1950 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/sqltags/model/types/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.491337 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/tags/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/tags/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.491337 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/tags/config/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/tags/config/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.491337 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/tags/config/types/
--rw-r--r--   0 runner    (1001) docker     (122)      311 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/tags/config/types/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.491337 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/tags/model/
--rw-r--r--   0 runner    (1001) docker     (122)     2030 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/tags/model/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.491337 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/tags/paths/
--rw-r--r--   0 runner    (1001) docker     (122)     1156 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/tags/paths/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.491337 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/tags/paths/parser/
--rw-r--r--   0 runner    (1001) docker     (122)      799 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/tags/paths/parser/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.491337 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/tags/tagpaths/
--rw-r--r--   0 runner    (1001) docker     (122)      248 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/tags/tagpaths/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.491337 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/user/
--rw-r--r--   0 runner    (1001) docker     (122)     4590 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/user/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.491337 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/user/schedule/
--rw-r--r--   0 runner    (1001) docker     (122)     4957 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/user/schedule/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.491337 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/util/
--rw-r--r--   0 runner    (1001) docker     (122)     6007 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/util/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.491337 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/xmlserialization/
--rw-r--r--   0 runner    (1001) docker     (122)      614 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/xmlserialization/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.491337 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/xmlserialization/deserialization/
--rw-r--r--   0 runner    (1001) docker     (122)     2818 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/xmlserialization/deserialization/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.491337 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/xmlserialization/encoding/
--rw-r--r--   0 runner    (1001) docker     (122)       63 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/xmlserialization/encoding/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.491337 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/xmlserialization/serialization/
--rw-r--r--   0 runner    (1001) docker     (122)     2253 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/xmlserialization/serialization/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.491337 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/xmlserialization/serialization/equalitydelegates/
--rw-r--r--   0 runner    (1001) docker     (122)      139 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/xmlserialization/serialization/equalitydelegates/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.491337 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/gateway/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/gateway/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.491337 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/gateway/project/
--rw-r--r--   0 runner    (1001) docker     (122)     1159 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/gateway/project/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.491337 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/modules/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/modules/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.491337 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/modules/serial/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/modules/serial/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.491337 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/modules/serial/scripting/
--rw-r--r--   0 runner    (1001) docker     (122)     2338 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/modules/serial/scripting/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.491337 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/opccom/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/opccom/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.491337 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/opccom/hda/
--rw-r--r--   0 runner    (1001) docker     (122)     1167 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/opccom/hda/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.491337 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/perspective/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/perspective/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.491337 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/perspective/common/
--rw-r--r--   0 runner    (1001) docker     (122)      915 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/perspective/common/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.491337 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/sfc/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/sfc/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.491337 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/sfc/api/
--rw-r--r--   0 runner    (1001) docker     (122)      104 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/sfc/api/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.491337 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/vision/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/vision/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.491337 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/vision/api/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/vision/api/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.495337 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/vision/api/client/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/vision/api/client/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.495337 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/vision/api/client/components/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/vision/api/client/components/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.495337 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/vision/api/client/components/model/
--rw-r--r--   0 runner    (1001) docker     (122)      277 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/vision/api/client/components/model/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.495337 ignition_api_stubs-8.1.26.post1/stubs/com/palantir/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/palantir/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.495337 ignition_api_stubs-8.1.26.post1/stubs/com/palantir/ptoss/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/palantir/ptoss/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.495337 ignition_api_stubs-8.1.26.post1/stubs/com/palantir/ptoss/cinch/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/palantir/ptoss/cinch/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.495337 ignition_api_stubs-8.1.26.post1/stubs/com/palantir/ptoss/cinch/core/
--rw-r--r--   0 runner    (1001) docker     (122)      413 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/palantir/ptoss/cinch/core/__init__.pyi
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/com/py.typed
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.495337 ignition_api_stubs-8.1.26.post1/stubs/dev/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/dev/__init__.pyi
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/dev/py.typed
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.495337 ignition_api_stubs-8.1.26.post1/stubs/dev/thecesrom/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/dev/thecesrom/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.495337 ignition_api_stubs-8.1.26.post1/stubs/dev/thecesrom/helper/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/dev/thecesrom/helper/__init__.pyi
--rw-r--r--   0 runner    (1001) docker     (122)       88 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/dev/thecesrom/helper/types.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.495337 ignition_api_stubs-8.1.26.post1/stubs/dev/thecesrom/utils/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/dev/thecesrom/utils/__init__.pyi
--rw-r--r--   0 runner    (1001) docker     (122)       70 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/dev/thecesrom/utils/decorators.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.495337 ignition_api_stubs-8.1.26.post1/stubs/ignition_api_stubs.egg-info/
--rw-r--r--   0 runner    (1001) docker     (122)     4636 2023-04-05 06:44:37.000000 ignition_api_stubs-8.1.26.post1/stubs/ignition_api_stubs.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (122)    10742 2023-04-05 06:44:37.000000 ignition_api_stubs-8.1.26.post1/stubs/ignition_api_stubs.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (122)        1 2023-04-05 06:44:37.000000 ignition_api_stubs-8.1.26.post1/stubs/ignition_api_stubs.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (122)       34 2023-04-05 06:44:37.000000 ignition_api_stubs-8.1.26.post1/stubs/ignition_api_stubs.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (122)       33 2023-04-05 06:44:37.000000 ignition_api_stubs-8.1.26.post1/stubs/ignition_api_stubs.egg-info/top_level.txt
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.495337 ignition_api_stubs-8.1.26.post1/stubs/java/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/java/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.495337 ignition_api_stubs-8.1.26.post1/stubs/java/awt/
--rw-r--r--   0 runner    (1001) docker     (122)     3147 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/java/awt/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.495337 ignition_api_stubs-8.1.26.post1/stubs/java/awt/event/
--rw-r--r--   0 runner    (1001) docker     (122)     2583 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/java/awt/event/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.495337 ignition_api_stubs-8.1.26.post1/stubs/java/awt/geom/
--rw-r--r--   0 runner    (1001) docker     (122)     1312 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/java/awt/geom/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.495337 ignition_api_stubs-8.1.26.post1/stubs/java/awt/image/
--rw-r--r--   0 runner    (1001) docker     (122)      128 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/java/awt/image/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.495337 ignition_api_stubs-8.1.26.post1/stubs/java/awt/print/
--rw-r--r--   0 runner    (1001) docker     (122)     1107 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/java/awt/print/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.495337 ignition_api_stubs-8.1.26.post1/stubs/java/beans/
--rw-r--r--   0 runner    (1001) docker     (122)      568 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/java/beans/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.495337 ignition_api_stubs-8.1.26.post1/stubs/java/io/
--rw-r--r--   0 runner    (1001) docker     (122)     4272 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/java/io/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.499338 ignition_api_stubs-8.1.26.post1/stubs/java/lang/
--rw-r--r--   0 runner    (1001) docker     (122)     9737 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/java/lang/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.499338 ignition_api_stubs-8.1.26.post1/stubs/java/lang/reflect/
--rw-r--r--   0 runner    (1001) docker     (122)      100 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/java/lang/reflect/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.499338 ignition_api_stubs-8.1.26.post1/stubs/java/math/
--rw-r--r--   0 runner    (1001) docker     (122)      347 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/java/math/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.499338 ignition_api_stubs-8.1.26.post1/stubs/java/net/
--rw-r--r--   0 runner    (1001) docker     (122)     6194 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/java/net/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.499338 ignition_api_stubs-8.1.26.post1/stubs/java/net/http/
--rw-r--r--   0 runner    (1001) docker     (122)       84 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/java/net/http/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.499338 ignition_api_stubs-8.1.26.post1/stubs/java/nio/
--rw-r--r--   0 runner    (1001) docker     (122)     7653 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/java/nio/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.499338 ignition_api_stubs-8.1.26.post1/stubs/java/nio/channels/
--rw-r--r--   0 runner    (1001) docker     (122)     4672 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/java/nio/channels/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.499338 ignition_api_stubs-8.1.26.post1/stubs/java/nio/charset/
--rw-r--r--   0 runner    (1001) docker     (122)     2026 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/java/nio/charset/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.499338 ignition_api_stubs-8.1.26.post1/stubs/java/nio/file/
--rw-r--r--   0 runner    (1001) docker     (122)     7943 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/java/nio/file/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.499338 ignition_api_stubs-8.1.26.post1/stubs/java/nio/file/attribute/
--rw-r--r--   0 runner    (1001) docker     (122)     1813 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/java/nio/file/attribute/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.499338 ignition_api_stubs-8.1.26.post1/stubs/java/org/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/java/org/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.499338 ignition_api_stubs-8.1.26.post1/stubs/java/org/jdesktop/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/java/org/jdesktop/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.499338 ignition_api_stubs-8.1.26.post1/stubs/java/org/jdesktop/core/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/java/org/jdesktop/core/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.499338 ignition_api_stubs-8.1.26.post1/stubs/java/org/jdesktop/core/animation/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/java/org/jdesktop/core/animation/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.499338 ignition_api_stubs-8.1.26.post1/stubs/java/org/jdesktop/core/animation/timing/
--rw-r--r--   0 runner    (1001) docker     (122)      155 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/java/org/jdesktop/core/animation/timing/__init__.pyi
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/java/py.typed
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.499338 ignition_api_stubs-8.1.26.post1/stubs/java/security/
--rw-r--r--   0 runner    (1001) docker     (122)      347 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/java/security/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.499338 ignition_api_stubs-8.1.26.post1/stubs/java/text/
--rw-r--r--   0 runner    (1001) docker     (122)     8255 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/java/text/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.499338 ignition_api_stubs-8.1.26.post1/stubs/java/time/
--rw-r--r--   0 runner    (1001) docker     (122)     2432 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/java/time/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.499338 ignition_api_stubs-8.1.26.post1/stubs/java/time/format/
--rw-r--r--   0 runner    (1001) docker     (122)      221 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/java/time/format/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.499338 ignition_api_stubs-8.1.26.post1/stubs/java/time/temporal/
--rw-r--r--   0 runner    (1001) docker     (122)     3692 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/java/time/temporal/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.499338 ignition_api_stubs-8.1.26.post1/stubs/java/util/
--rw-r--r--   0 runner    (1001) docker     (122)    16259 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/java/util/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.499338 ignition_api_stubs-8.1.26.post1/stubs/java/util/concurrent/
--rw-r--r--   0 runner    (1001) docker     (122)     1919 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/java/util/concurrent/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.499338 ignition_api_stubs-8.1.26.post1/stubs/java/util/function/
--rw-r--r--   0 runner    (1001) docker     (122)     1427 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/java/util/function/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.499338 ignition_api_stubs-8.1.26.post1/stubs/java/util/regex/
--rw-r--r--   0 runner    (1001) docker     (122)     2817 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/java/util/regex/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.499338 ignition_api_stubs-8.1.26.post1/stubs/java/util/stream/
--rw-r--r--   0 runner    (1001) docker     (122)     1594 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/java/util/stream/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.499338 ignition_api_stubs-8.1.26.post1/stubs/javax/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/javax/__init__.pyi
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/javax/py.typed
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.499338 ignition_api_stubs-8.1.26.post1/stubs/javax/security/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/javax/security/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.499338 ignition_api_stubs-8.1.26.post1/stubs/javax/security/auth/
--rw-r--r--   0 runner    (1001) docker     (122)      125 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/javax/security/auth/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.503338 ignition_api_stubs-8.1.26.post1/stubs/javax/swing/
--rw-r--r--   0 runner    (1001) docker     (122)     6507 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/javax/swing/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.503338 ignition_api_stubs-8.1.26.post1/stubs/javax/swing/event/
--rw-r--r--   0 runner    (1001) docker     (122)      639 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/javax/swing/event/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.503338 ignition_api_stubs-8.1.26.post1/stubs/javax/swing/plaf/
--rw-r--r--   0 runner    (1001) docker     (122)      392 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/javax/swing/plaf/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.503338 ignition_api_stubs-8.1.26.post1/stubs/javax/swing/text/
--rw-r--r--   0 runner    (1001) docker     (122)      206 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/javax/swing/text/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.503338 ignition_api_stubs-8.1.26.post1/stubs/org/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/org/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.503338 ignition_api_stubs-8.1.26.post1/stubs/org/apache/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/org/apache/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.503338 ignition_api_stubs-8.1.26.post1/stubs/org/apache/commons/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/org/apache/commons/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.503338 ignition_api_stubs-8.1.26.post1/stubs/org/apache/commons/lang3/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/org/apache/commons/lang3/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.503338 ignition_api_stubs-8.1.26.post1/stubs/org/apache/commons/lang3/builder/
--rw-r--r--   0 runner    (1001) docker     (122)      784 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/org/apache/commons/lang3/builder/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.503338 ignition_api_stubs-8.1.26.post1/stubs/org/apache/commons/math3/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/org/apache/commons/math3/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.503338 ignition_api_stubs-8.1.26.post1/stubs/org/apache/commons/math3/exception/
--rw-r--r--   0 runner    (1001) docker     (122)      587 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/org/apache/commons/math3/exception/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.503338 ignition_api_stubs-8.1.26.post1/stubs/org/apache/commons/math3/exception/util/
--rw-r--r--   0 runner    (1001) docker     (122)      682 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/org/apache/commons/math3/exception/util/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.503338 ignition_api_stubs-8.1.26.post1/stubs/org/apache/log4j/
--rw-r--r--   0 runner    (1001) docker     (122)     2417 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/org/apache/log4j/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.503338 ignition_api_stubs-8.1.26.post1/stubs/org/apache/log4j/spi/
--rw-r--r--   0 runner    (1001) docker     (122)     2021 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/org/apache/log4j/spi/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.503338 ignition_api_stubs-8.1.26.post1/stubs/org/json/
--rw-r--r--   0 runner    (1001) docker     (122)     4118 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/org/json/__init__.pyi
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/org/py.typed
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.503338 ignition_api_stubs-8.1.26.post1/stubs/org/python/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/org/python/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.503338 ignition_api_stubs-8.1.26.post1/stubs/org/python/core/
--rw-r--r--   0 runner    (1001) docker     (122)    23088 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/org/python/core/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.503338 ignition_api_stubs-8.1.26.post1/stubs/org/python/expose/
--rw-r--r--   0 runner    (1001) docker     (122)      354 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/org/python/expose/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.503338 ignition_api_stubs-8.1.26.post1/stubs/org/slf4j/
--rw-r--r--   0 runner    (1001) docker     (122)     1126 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/org/slf4j/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.503338 ignition_api_stubs-8.1.26.post1/stubs/org/slf4j/event/
--rw-r--r--   0 runner    (1001) docker     (122)      167 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/org/slf4j/event/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.507338 ignition_api_stubs-8.1.26.post1/stubs/system/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/system/__init__.pyi
--rw-r--r--   0 runner    (1001) docker     (122)       15 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/system/__version__.pyi
--rw-r--r--   0 runner    (1001) docker     (122)     2051 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/system/alarm.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.507338 ignition_api_stubs-8.1.26.post1/stubs/system/bacnet/
--rw-r--r--   0 runner    (1001) docker     (122)      834 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/system/bacnet/__init__.pyi
--rw-r--r--   0 runner    (1001) docker     (122)    12890 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/system/bacnet/enumerated.pyi
--rw-r--r--   0 runner    (1001) docker     (122)      780 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/system/bacnet/enums.pyi
--rw-r--r--   0 runner    (1001) docker     (122)     2384 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/system/dataset.pyi
--rw-r--r--   0 runner    (1001) docker     (122)     2296 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/system/date.pyi
--rw-r--r--   0 runner    (1001) docker     (122)     3527 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/system/db.pyi
--rw-r--r--   0 runner    (1001) docker     (122)      691 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/system/device.pyi
--rw-r--r--   0 runner    (1001) docker     (122)     1279 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/system/dnp3.pyi
--rw-r--r--   0 runner    (1001) docker     (122)      722 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/system/eam.pyi
--rw-r--r--   0 runner    (1001) docker     (122)      814 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/system/file.pyi
--rw-r--r--   0 runner    (1001) docker     (122)      224 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/system/groups.pyi
--rw-r--r--   0 runner    (1001) docker     (122)     3220 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/system/gui.pyi
--rw-r--r--   0 runner    (1001) docker     (122)      730 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/system/iec61850.pyi
--rw-r--r--   0 runner    (1001) docker     (122)     1094 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/system/math.pyi
--rw-r--r--   0 runner    (1001) docker     (122)     1099 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/system/nav.pyi
--rw-r--r--   0 runner    (1001) docker     (122)     2249 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/system/net.pyi
--rw-r--r--   0 runner    (1001) docker     (122)     1504 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/system/opc.pyi
--rw-r--r--   0 runner    (1001) docker     (122)     1543 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/system/opchda.pyi
--rw-r--r--   0 runner    (1001) docker     (122)      482 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/system/opcua.pyi
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:37.511338 ignition_api_stubs-8.1.26.post1/stubs/system/perspective/
--rw-r--r--   0 runner    (1001) docker     (122)     3888 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/system/perspective/__init__.pyi
--rw-r--r--   0 runner    (1001) docker     (122)       81 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/system/perspective/workstation.pyi
--rw-r--r--   0 runner    (1001) docker     (122)      596 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/system/print.pyi
--rw-r--r--   0 runner    (1001) docker     (122)      151 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/system/project.pyi
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/system/py.typed
--rw-r--r--   0 runner    (1001) docker     (122)      741 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/system/report.pyi
--rw-r--r--   0 runner    (1001) docker     (122)      637 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/system/roster.pyi
--rw-r--r--   0 runner    (1001) docker     (122)     1280 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/system/secsgem.pyi
--rw-r--r--   0 runner    (1001) docker     (122)      708 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/system/security.pyi
--rw-r--r--   0 runner    (1001) docker     (122)     2312 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/system/serial.pyi
--rw-r--r--   0 runner    (1001) docker     (122)      870 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/system/sfc.pyi
--rw-r--r--   0 runner    (1001) docker     (122)     4733 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/system/tag.pyi
--rw-r--r--   0 runner    (1001) docker     (122)      460 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/system/twilio.pyi
--rw-r--r--   0 runner    (1001) docker     (122)     2350 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/system/user.pyi
--rw-r--r--   0 runner    (1001) docker     (122)     4728 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/system/util.pyi
--rw-r--r--   0 runner    (1001) docker     (122)       33 2023-04-05 06:44:23.000000 ignition_api_stubs-8.1.26.post1/stubs/system/vision.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:20.011675 ignition_api_stubs-8.1.26.post2/
+-rw-r--r--   0 runner    (1001) docker     (122)     6670 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/CHANGELOG.md
+-rw-r--r--   0 runner    (1001) docker     (122)     1070 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (122)       21 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (122)     4636 2023-04-06 23:22:20.011675 ignition_api_stubs-8.1.26.post2/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (122)     2031 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/README.md
+-rw-r--r--   0 runner    (1001) docker     (122)     1593 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (122)       38 2023-04-06 23:22:20.011675 ignition_api_stubs-8.1.26.post2/setup.cfg
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.971674 ignition_api_stubs-8.1.26.post2/stubs/
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.971674 ignition_api_stubs-8.1.26.post2/stubs/ch/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/ch/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.971674 ignition_api_stubs-8.1.26.post2/stubs/ch/qos/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/ch/qos/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.971674 ignition_api_stubs-8.1.26.post2/stubs/ch/qos/logback/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/ch/qos/logback/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.971674 ignition_api_stubs-8.1.26.post2/stubs/ch/qos/logback/classic/
+-rw-r--r--   0 runner    (1001) docker     (122)      650 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/ch/qos/logback/classic/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.975674 ignition_api_stubs-8.1.26.post2/stubs/com/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.975674 ignition_api_stubs-8.1.26.post2/stubs/com/codahale/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/codahale/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.975674 ignition_api_stubs-8.1.26.post2/stubs/com/codahale/metrics/
+-rw-r--r--   0 runner    (1001) docker     (122)     1271 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/codahale/metrics/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.975674 ignition_api_stubs-8.1.26.post2/stubs/com/google/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/google/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.975674 ignition_api_stubs-8.1.26.post2/stubs/com/google/common/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/google/common/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.975674 ignition_api_stubs-8.1.26.post2/stubs/com/google/common/collect/
+-rw-r--r--   0 runner    (1001) docker     (122)     2204 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/google/common/collect/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.975674 ignition_api_stubs-8.1.26.post2/stubs/com/google/common/eventbus/
+-rw-r--r--   0 runner    (1001) docker     (122)      359 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/google/common/eventbus/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.975674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.975674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/factorypmi/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/factorypmi/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.975674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/factorypmi/application/
+-rw-r--r--   0 runner    (1001) docker     (122)     1780 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/factorypmi/application/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.975674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/factorypmi/application/binding/
+-rw-r--r--   0 runner    (1001) docker     (122)      875 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/factorypmi/application/binding/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.975674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/factorypmi/application/components/
+-rw-r--r--   0 runner    (1001) docker     (122)      285 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/factorypmi/application/components/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.975674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/factorypmi/application/model/
+-rw-r--r--   0 runner    (1001) docker     (122)      193 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/factorypmi/application/model/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.975674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/factorypmi/application/script/
+-rw-r--r--   0 runner    (1001) docker     (122)      260 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/factorypmi/application/script/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.975674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/factorypmi/application/script/builtin/
+-rw-r--r--   0 runner    (1001) docker     (122)     7676 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/factorypmi/application/script/builtin/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.975674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/factorypmi/application/sqltags/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/factorypmi/application/sqltags/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.975674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/factorypmi/application/sqltags/project/
+-rw-r--r--   0 runner    (1001) docker     (122)      136 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/factorypmi/application/sqltags/project/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.975674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.975674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/alarming/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/alarming/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.975674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/alarming/common/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/alarming/common/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.975674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/alarming/common/rosters/
+-rw-r--r--   0 runner    (1001) docker     (122)      509 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/alarming/common/rosters/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.975674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/client/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/client/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.975674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/client/launch/
+-rw-r--r--   0 runner    (1001) docker     (122)     6082 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/client/launch/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.975674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/client/model/
+-rw-r--r--   0 runner    (1001) docker     (122)     4075 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/client/model/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.979674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/client/util/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/client/util/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.979674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/client/util/gui/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/client/util/gui/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.979674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/client/util/gui/progress/
+-rw-r--r--   0 runner    (1001) docker     (122)     1602 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/client/util/gui/progress/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.979674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/client/util/gui/scheduling/
+-rw-r--r--   0 runner    (1001) docker     (122)     1402 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/client/util/gui/scheduling/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.979674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/
+-rw-r--r--   0 runner    (1001) docker     (122)    10151 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.979674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/alarming/
+-rw-r--r--   0 runner    (1001) docker     (122)     3228 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/alarming/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.979674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/alarming/evaluation/
+-rw-r--r--   0 runner    (1001) docker     (122)     1228 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/alarming/evaluation/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.979674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/alarming/query/
+-rw-r--r--   0 runner    (1001) docker     (122)      818 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/alarming/query/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.979674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/binding/
+-rw-r--r--   0 runner    (1001) docker     (122)       78 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/binding/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.979674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/browsing/
+-rw-r--r--   0 runner    (1001) docker     (122)     3590 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/browsing/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.979674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/config/
+-rw-r--r--   0 runner    (1001) docker     (122)     3188 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/config/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.979674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/db/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/db/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.979674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/db/namedquery/
+-rw-r--r--   0 runner    (1001) docker     (122)      777 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/db/namedquery/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.979674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/document/
+-rw-r--r--   0 runner    (1001) docker     (122)      215 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/document/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.979674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/execution/
+-rw-r--r--   0 runner    (1001) docker     (122)     1169 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/execution/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.979674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/expressions/
+-rw-r--r--   0 runner    (1001) docker     (122)     1024 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/expressions/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.979674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/expressions/functions/
+-rw-r--r--   0 runner    (1001) docker     (122)      672 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/expressions/functions/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.979674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/functional/
+-rw-r--r--   0 runner    (1001) docker     (122)       54 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/functional/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.979674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/gson/
+-rw-r--r--   0 runner    (1001) docker     (122)     8733 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/gson/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.979674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/gson/reflect/
+-rw-r--r--   0 runner    (1001) docker     (122)      284 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/gson/reflect/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.979674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/gson/stream/
+-rw-r--r--   0 runner    (1001) docker     (122)     2056 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/gson/stream/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.979674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/gui/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/gui/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.979674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/gui/progress/
+-rw-r--r--   0 runner    (1001) docker     (122)     1374 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/gui/progress/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.983674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/i18n/
+-rw-r--r--   0 runner    (1001) docker     (122)      925 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/i18n/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.983674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/i18n/translation/
+-rw-r--r--   0 runner    (1001) docker     (122)      242 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/i18n/translation/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.983674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/jsonschema/
+-rw-r--r--   0 runner    (1001) docker     (122)     4057 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/jsonschema/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.983674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/licensing/
+-rw-r--r--   0 runner    (1001) docker     (122)     1355 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/licensing/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.983674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/logging/
+-rw-r--r--   0 runner    (1001) docker     (122)      887 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/logging/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.983674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/messages/
+-rw-r--r--   0 runner    (1001) docker     (122)     1266 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/messages/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.983674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/model/
+-rw-r--r--   0 runner    (1001) docker     (122)     3275 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/model/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.983674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/model/values/
+-rw-r--r--   0 runner    (1001) docker     (122)     4721 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/model/values/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.983674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/modules/
+-rw-r--r--   0 runner    (1001) docker     (122)     4709 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/modules/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.983674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/opc/
+-rw-r--r--   0 runner    (1001) docker     (122)     3834 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/opc/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.983674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/project/
+-rw-r--r--   0 runner    (1001) docker     (122)     3515 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/project/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.983674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/project/resource/
+-rw-r--r--   0 runner    (1001) docker     (122)     5714 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/project/resource/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.983674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/script/
+-rw-r--r--   0 runner    (1001) docker     (122)     2556 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/script/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.983674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/script/abc/
+-rw-r--r--   0 runner    (1001) docker     (122)     4504 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/script/abc/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.983674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/script/adapters/
+-rw-r--r--   0 runner    (1001) docker     (122)     1297 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/script/adapters/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.983674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/script/builtin/
+-rw-r--r--   0 runner    (1001) docker     (122)     8422 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/script/builtin/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.983674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/script/builtin/http/
+-rw-r--r--   0 runner    (1001) docker     (122)     2702 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/script/builtin/http/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.983674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/script/builtin/ialabs/
+-rw-r--r--   0 runner    (1001) docker     (122)     1802 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/script/builtin/ialabs/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.983674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/script/hints/
+-rw-r--r--   0 runner    (1001) docker     (122)      374 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/script/hints/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.983674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/script/message/
+-rw-r--r--   0 runner    (1001) docker     (122)      594 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/script/message/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.983674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/sqltags/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/sqltags/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.987674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/sqltags/history/
+-rw-r--r--   0 runner    (1001) docker     (122)      418 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/sqltags/history/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.987674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/sqltags/history/annotations/
+-rw-r--r--   0 runner    (1001) docker     (122)     1931 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/sqltags/history/annotations/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.987674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/sqltags/model/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/sqltags/model/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.987674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/sqltags/model/types/
+-rw-r--r--   0 runner    (1001) docker     (122)     1950 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/sqltags/model/types/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.987674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/tags/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/tags/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.987674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/tags/config/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/tags/config/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.987674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/tags/config/types/
+-rw-r--r--   0 runner    (1001) docker     (122)      311 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/tags/config/types/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.987674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/tags/model/
+-rw-r--r--   0 runner    (1001) docker     (122)     2030 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/tags/model/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.987674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/tags/paths/
+-rw-r--r--   0 runner    (1001) docker     (122)     1156 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/tags/paths/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.987674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/tags/paths/parser/
+-rw-r--r--   0 runner    (1001) docker     (122)      799 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/tags/paths/parser/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.987674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/tags/tagpaths/
+-rw-r--r--   0 runner    (1001) docker     (122)      248 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/tags/tagpaths/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.987674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/user/
+-rw-r--r--   0 runner    (1001) docker     (122)     4590 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/user/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.987674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/user/schedule/
+-rw-r--r--   0 runner    (1001) docker     (122)     4957 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/user/schedule/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.987674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/util/
+-rw-r--r--   0 runner    (1001) docker     (122)     6007 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/util/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.987674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/xmlserialization/
+-rw-r--r--   0 runner    (1001) docker     (122)      594 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/xmlserialization/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.987674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/xmlserialization/deserialization/
+-rw-r--r--   0 runner    (1001) docker     (122)     2818 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/xmlserialization/deserialization/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.987674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/xmlserialization/encoding/
+-rw-r--r--   0 runner    (1001) docker     (122)       63 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/xmlserialization/encoding/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.987674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/xmlserialization/serialization/
+-rw-r--r--   0 runner    (1001) docker     (122)     2238 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/xmlserialization/serialization/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.987674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/xmlserialization/serialization/equalitydelegates/
+-rw-r--r--   0 runner    (1001) docker     (122)      139 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/xmlserialization/serialization/equalitydelegates/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.987674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/gateway/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/gateway/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.987674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/gateway/project/
+-rw-r--r--   0 runner    (1001) docker     (122)     1159 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/gateway/project/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.987674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/modules/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/modules/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.987674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/modules/serial/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/modules/serial/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.987674 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/modules/serial/scripting/
+-rw-r--r--   0 runner    (1001) docker     (122)     2338 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/modules/serial/scripting/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.991675 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/opccom/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/opccom/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.991675 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/opccom/hda/
+-rw-r--r--   0 runner    (1001) docker     (122)     1167 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/opccom/hda/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.991675 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/perspective/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/perspective/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.991675 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/perspective/common/
+-rw-r--r--   0 runner    (1001) docker     (122)      915 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/perspective/common/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.991675 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/sfc/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/sfc/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.991675 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/sfc/api/
+-rw-r--r--   0 runner    (1001) docker     (122)      104 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/sfc/api/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.991675 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/vision/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/vision/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.991675 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/vision/api/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/vision/api/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.991675 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/vision/api/client/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/vision/api/client/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.991675 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/vision/api/client/components/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/vision/api/client/components/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.991675 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/vision/api/client/components/model/
+-rw-r--r--   0 runner    (1001) docker     (122)      277 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/vision/api/client/components/model/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.991675 ignition_api_stubs-8.1.26.post2/stubs/com/palantir/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/palantir/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.991675 ignition_api_stubs-8.1.26.post2/stubs/com/palantir/ptoss/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/palantir/ptoss/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.991675 ignition_api_stubs-8.1.26.post2/stubs/com/palantir/ptoss/cinch/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/palantir/ptoss/cinch/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.991675 ignition_api_stubs-8.1.26.post2/stubs/com/palantir/ptoss/cinch/core/
+-rw-r--r--   0 runner    (1001) docker     (122)      413 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/palantir/ptoss/cinch/core/__init__.pyi
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/com/py.typed
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.991675 ignition_api_stubs-8.1.26.post2/stubs/dev/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/dev/__init__.pyi
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/dev/py.typed
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.991675 ignition_api_stubs-8.1.26.post2/stubs/dev/thecesrom/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/dev/thecesrom/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.991675 ignition_api_stubs-8.1.26.post2/stubs/dev/thecesrom/helper/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/dev/thecesrom/helper/__init__.pyi
+-rw-r--r--   0 runner    (1001) docker     (122)       88 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/dev/thecesrom/helper/types.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.991675 ignition_api_stubs-8.1.26.post2/stubs/dev/thecesrom/utils/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/dev/thecesrom/utils/__init__.pyi
+-rw-r--r--   0 runner    (1001) docker     (122)       70 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/dev/thecesrom/utils/decorators.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.995675 ignition_api_stubs-8.1.26.post2/stubs/ignition_api_stubs.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (122)     4636 2023-04-06 23:22:19.000000 ignition_api_stubs-8.1.26.post2/stubs/ignition_api_stubs.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (122)    10742 2023-04-06 23:22:19.000000 ignition_api_stubs-8.1.26.post2/stubs/ignition_api_stubs.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (122)        1 2023-04-06 23:22:19.000000 ignition_api_stubs-8.1.26.post2/stubs/ignition_api_stubs.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (122)       34 2023-04-06 23:22:19.000000 ignition_api_stubs-8.1.26.post2/stubs/ignition_api_stubs.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (122)       33 2023-04-06 23:22:19.000000 ignition_api_stubs-8.1.26.post2/stubs/ignition_api_stubs.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.995675 ignition_api_stubs-8.1.26.post2/stubs/java/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/java/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.995675 ignition_api_stubs-8.1.26.post2/stubs/java/awt/
+-rw-r--r--   0 runner    (1001) docker     (122)     3147 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/java/awt/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.995675 ignition_api_stubs-8.1.26.post2/stubs/java/awt/event/
+-rw-r--r--   0 runner    (1001) docker     (122)     2583 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/java/awt/event/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.995675 ignition_api_stubs-8.1.26.post2/stubs/java/awt/geom/
+-rw-r--r--   0 runner    (1001) docker     (122)     1312 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/java/awt/geom/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.995675 ignition_api_stubs-8.1.26.post2/stubs/java/awt/image/
+-rw-r--r--   0 runner    (1001) docker     (122)      128 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/java/awt/image/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.995675 ignition_api_stubs-8.1.26.post2/stubs/java/awt/print/
+-rw-r--r--   0 runner    (1001) docker     (122)     1107 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/java/awt/print/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.995675 ignition_api_stubs-8.1.26.post2/stubs/java/beans/
+-rw-r--r--   0 runner    (1001) docker     (122)      568 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/java/beans/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.995675 ignition_api_stubs-8.1.26.post2/stubs/java/io/
+-rw-r--r--   0 runner    (1001) docker     (122)     4272 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/java/io/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.995675 ignition_api_stubs-8.1.26.post2/stubs/java/lang/
+-rw-r--r--   0 runner    (1001) docker     (122)     9737 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/java/lang/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.995675 ignition_api_stubs-8.1.26.post2/stubs/java/lang/reflect/
+-rw-r--r--   0 runner    (1001) docker     (122)      100 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/java/lang/reflect/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.995675 ignition_api_stubs-8.1.26.post2/stubs/java/math/
+-rw-r--r--   0 runner    (1001) docker     (122)      347 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/java/math/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.995675 ignition_api_stubs-8.1.26.post2/stubs/java/net/
+-rw-r--r--   0 runner    (1001) docker     (122)     6194 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/java/net/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.995675 ignition_api_stubs-8.1.26.post2/stubs/java/net/http/
+-rw-r--r--   0 runner    (1001) docker     (122)       84 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/java/net/http/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.995675 ignition_api_stubs-8.1.26.post2/stubs/java/nio/
+-rw-r--r--   0 runner    (1001) docker     (122)     7653 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/java/nio/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.995675 ignition_api_stubs-8.1.26.post2/stubs/java/nio/channels/
+-rw-r--r--   0 runner    (1001) docker     (122)     4672 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/java/nio/channels/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.999675 ignition_api_stubs-8.1.26.post2/stubs/java/nio/charset/
+-rw-r--r--   0 runner    (1001) docker     (122)     2026 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/java/nio/charset/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.999675 ignition_api_stubs-8.1.26.post2/stubs/java/nio/file/
+-rw-r--r--   0 runner    (1001) docker     (122)     7943 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/java/nio/file/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.999675 ignition_api_stubs-8.1.26.post2/stubs/java/nio/file/attribute/
+-rw-r--r--   0 runner    (1001) docker     (122)     1813 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/java/nio/file/attribute/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.999675 ignition_api_stubs-8.1.26.post2/stubs/java/org/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/java/org/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.999675 ignition_api_stubs-8.1.26.post2/stubs/java/org/jdesktop/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/java/org/jdesktop/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.999675 ignition_api_stubs-8.1.26.post2/stubs/java/org/jdesktop/core/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/java/org/jdesktop/core/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.999675 ignition_api_stubs-8.1.26.post2/stubs/java/org/jdesktop/core/animation/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/java/org/jdesktop/core/animation/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.999675 ignition_api_stubs-8.1.26.post2/stubs/java/org/jdesktop/core/animation/timing/
+-rw-r--r--   0 runner    (1001) docker     (122)      155 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/java/org/jdesktop/core/animation/timing/__init__.pyi
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/java/py.typed
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.999675 ignition_api_stubs-8.1.26.post2/stubs/java/security/
+-rw-r--r--   0 runner    (1001) docker     (122)      347 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/java/security/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.999675 ignition_api_stubs-8.1.26.post2/stubs/java/text/
+-rw-r--r--   0 runner    (1001) docker     (122)     8255 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/java/text/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.999675 ignition_api_stubs-8.1.26.post2/stubs/java/time/
+-rw-r--r--   0 runner    (1001) docker     (122)     2432 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/java/time/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.999675 ignition_api_stubs-8.1.26.post2/stubs/java/time/format/
+-rw-r--r--   0 runner    (1001) docker     (122)      221 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/java/time/format/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.999675 ignition_api_stubs-8.1.26.post2/stubs/java/time/temporal/
+-rw-r--r--   0 runner    (1001) docker     (122)     3692 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/java/time/temporal/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.999675 ignition_api_stubs-8.1.26.post2/stubs/java/util/
+-rw-r--r--   0 runner    (1001) docker     (122)    16259 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/java/util/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.999675 ignition_api_stubs-8.1.26.post2/stubs/java/util/concurrent/
+-rw-r--r--   0 runner    (1001) docker     (122)     1919 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/java/util/concurrent/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.999675 ignition_api_stubs-8.1.26.post2/stubs/java/util/function/
+-rw-r--r--   0 runner    (1001) docker     (122)     1427 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/java/util/function/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.999675 ignition_api_stubs-8.1.26.post2/stubs/java/util/regex/
+-rw-r--r--   0 runner    (1001) docker     (122)     2817 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/java/util/regex/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.999675 ignition_api_stubs-8.1.26.post2/stubs/java/util/stream/
+-rw-r--r--   0 runner    (1001) docker     (122)     1594 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/java/util/stream/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.999675 ignition_api_stubs-8.1.26.post2/stubs/javax/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/javax/__init__.pyi
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/javax/py.typed
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:19.999675 ignition_api_stubs-8.1.26.post2/stubs/javax/security/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/javax/security/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:20.003675 ignition_api_stubs-8.1.26.post2/stubs/javax/security/auth/
+-rw-r--r--   0 runner    (1001) docker     (122)      125 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/javax/security/auth/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:20.003675 ignition_api_stubs-8.1.26.post2/stubs/javax/swing/
+-rw-r--r--   0 runner    (1001) docker     (122)     6507 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/javax/swing/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:20.003675 ignition_api_stubs-8.1.26.post2/stubs/javax/swing/event/
+-rw-r--r--   0 runner    (1001) docker     (122)      639 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/javax/swing/event/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:20.003675 ignition_api_stubs-8.1.26.post2/stubs/javax/swing/plaf/
+-rw-r--r--   0 runner    (1001) docker     (122)      392 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/javax/swing/plaf/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:20.003675 ignition_api_stubs-8.1.26.post2/stubs/javax/swing/text/
+-rw-r--r--   0 runner    (1001) docker     (122)      206 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/javax/swing/text/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:20.003675 ignition_api_stubs-8.1.26.post2/stubs/org/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/org/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:20.003675 ignition_api_stubs-8.1.26.post2/stubs/org/apache/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/org/apache/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:20.003675 ignition_api_stubs-8.1.26.post2/stubs/org/apache/commons/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/org/apache/commons/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:20.003675 ignition_api_stubs-8.1.26.post2/stubs/org/apache/commons/lang3/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/org/apache/commons/lang3/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:20.003675 ignition_api_stubs-8.1.26.post2/stubs/org/apache/commons/lang3/builder/
+-rw-r--r--   0 runner    (1001) docker     (122)      784 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/org/apache/commons/lang3/builder/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:20.003675 ignition_api_stubs-8.1.26.post2/stubs/org/apache/commons/math3/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/org/apache/commons/math3/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:20.003675 ignition_api_stubs-8.1.26.post2/stubs/org/apache/commons/math3/exception/
+-rw-r--r--   0 runner    (1001) docker     (122)      587 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/org/apache/commons/math3/exception/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:20.003675 ignition_api_stubs-8.1.26.post2/stubs/org/apache/commons/math3/exception/util/
+-rw-r--r--   0 runner    (1001) docker     (122)      682 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/org/apache/commons/math3/exception/util/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:20.003675 ignition_api_stubs-8.1.26.post2/stubs/org/apache/log4j/
+-rw-r--r--   0 runner    (1001) docker     (122)     2417 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/org/apache/log4j/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:20.003675 ignition_api_stubs-8.1.26.post2/stubs/org/apache/log4j/spi/
+-rw-r--r--   0 runner    (1001) docker     (122)     2014 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/org/apache/log4j/spi/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:20.003675 ignition_api_stubs-8.1.26.post2/stubs/org/json/
+-rw-r--r--   0 runner    (1001) docker     (122)     4118 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/org/json/__init__.pyi
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/org/py.typed
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:20.003675 ignition_api_stubs-8.1.26.post2/stubs/org/python/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/org/python/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:20.003675 ignition_api_stubs-8.1.26.post2/stubs/org/python/core/
+-rw-r--r--   0 runner    (1001) docker     (122)    23038 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/org/python/core/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:20.003675 ignition_api_stubs-8.1.26.post2/stubs/org/python/expose/
+-rw-r--r--   0 runner    (1001) docker     (122)      354 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/org/python/expose/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:20.003675 ignition_api_stubs-8.1.26.post2/stubs/org/slf4j/
+-rw-r--r--   0 runner    (1001) docker     (122)     1126 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/org/slf4j/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:20.007675 ignition_api_stubs-8.1.26.post2/stubs/org/slf4j/event/
+-rw-r--r--   0 runner    (1001) docker     (122)      167 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/org/slf4j/event/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:20.011675 ignition_api_stubs-8.1.26.post2/stubs/system/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/system/__init__.pyi
+-rw-r--r--   0 runner    (1001) docker     (122)       15 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/system/__version__.pyi
+-rw-r--r--   0 runner    (1001) docker     (122)     2051 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/system/alarm.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:20.011675 ignition_api_stubs-8.1.26.post2/stubs/system/bacnet/
+-rw-r--r--   0 runner    (1001) docker     (122)      834 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/system/bacnet/__init__.pyi
+-rw-r--r--   0 runner    (1001) docker     (122)    12890 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/system/bacnet/enumerated.pyi
+-rw-r--r--   0 runner    (1001) docker     (122)      780 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/system/bacnet/enums.pyi
+-rw-r--r--   0 runner    (1001) docker     (122)     2384 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/system/dataset.pyi
+-rw-r--r--   0 runner    (1001) docker     (122)     2296 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/system/date.pyi
+-rw-r--r--   0 runner    (1001) docker     (122)     3527 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/system/db.pyi
+-rw-r--r--   0 runner    (1001) docker     (122)      691 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/system/device.pyi
+-rw-r--r--   0 runner    (1001) docker     (122)     1279 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/system/dnp3.pyi
+-rw-r--r--   0 runner    (1001) docker     (122)      722 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/system/eam.pyi
+-rw-r--r--   0 runner    (1001) docker     (122)      814 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/system/file.pyi
+-rw-r--r--   0 runner    (1001) docker     (122)      224 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/system/groups.pyi
+-rw-r--r--   0 runner    (1001) docker     (122)     3220 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/system/gui.pyi
+-rw-r--r--   0 runner    (1001) docker     (122)      730 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/system/iec61850.pyi
+-rw-r--r--   0 runner    (1001) docker     (122)     1094 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/system/math.pyi
+-rw-r--r--   0 runner    (1001) docker     (122)     1099 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/system/nav.pyi
+-rw-r--r--   0 runner    (1001) docker     (122)     2249 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/system/net.pyi
+-rw-r--r--   0 runner    (1001) docker     (122)     1504 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/system/opc.pyi
+-rw-r--r--   0 runner    (1001) docker     (122)     1543 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/system/opchda.pyi
+-rw-r--r--   0 runner    (1001) docker     (122)      482 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/system/opcua.pyi
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:20.011675 ignition_api_stubs-8.1.26.post2/stubs/system/perspective/
+-rw-r--r--   0 runner    (1001) docker     (122)     3888 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/system/perspective/__init__.pyi
+-rw-r--r--   0 runner    (1001) docker     (122)       81 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/system/perspective/workstation.pyi
+-rw-r--r--   0 runner    (1001) docker     (122)      596 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/system/print.pyi
+-rw-r--r--   0 runner    (1001) docker     (122)      151 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/system/project.pyi
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/system/py.typed
+-rw-r--r--   0 runner    (1001) docker     (122)      741 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/system/report.pyi
+-rw-r--r--   0 runner    (1001) docker     (122)      637 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/system/roster.pyi
+-rw-r--r--   0 runner    (1001) docker     (122)     1280 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/system/secsgem.pyi
+-rw-r--r--   0 runner    (1001) docker     (122)      708 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/system/security.pyi
+-rw-r--r--   0 runner    (1001) docker     (122)     2312 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/system/serial.pyi
+-rw-r--r--   0 runner    (1001) docker     (122)      870 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/system/sfc.pyi
+-rw-r--r--   0 runner    (1001) docker     (122)     4733 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/system/tag.pyi
+-rw-r--r--   0 runner    (1001) docker     (122)      460 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/system/twilio.pyi
+-rw-r--r--   0 runner    (1001) docker     (122)     2350 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/system/user.pyi
+-rw-r--r--   0 runner    (1001) docker     (122)     4728 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/system/util.pyi
+-rw-r--r--   0 runner    (1001) docker     (122)       33 2023-04-06 23:22:05.000000 ignition_api_stubs-8.1.26.post2/stubs/system/vision.pyi
```

### Comparing `ignition_api_stubs-8.1.26.post1/CHANGELOG.md` & `ignition_api_stubs-8.1.26.post2/CHANGELOG.md`

 * *Files 2% similar despite different names*

```diff
@@ -1,7 +1,15 @@
+## v8.1.26.post2 (2023-04-06)
+
+### Fix
+
+- **ia**: solve cyclic import error (#113)
+
+## v8.1.26.post1 (2023-04-04)
+
 ## v8.1.26.post1 (2023-04-04)
 
 ## v8.1.26 (2023-03-26)
 
 ## v8.1.25.post5 (2023-03-20)
 
 ### Refactor
```

### Comparing `ignition_api_stubs-8.1.26.post1/LICENSE` & `ignition_api_stubs-8.1.26.post2/LICENSE`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/PKG-INFO` & `ignition_api_stubs-8.1.26.post2/stubs/ignition_api_stubs.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
-Name: ignition_api_stubs
-Version: 8.1.26.post1
+Name: ignition-api-stubs
+Version: 8.1.26.post2
 Summary: Ignition Scripting API Stubs
 Author-email: César Román <cesar@thecesrom.dev>
 License: MIT License
         
         Copyright (c) 2022 César Román
         
         Permission is hereby granted, free of charge, to any person obtaining a copy
```

### Comparing `ignition_api_stubs-8.1.26.post1/README.md` & `ignition_api_stubs-8.1.26.post2/README.md`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/pyproject.toml` & `ignition_api_stubs-8.1.26.post2/pyproject.toml`

 * *Files 0% similar despite different names*

```diff
@@ -2,15 +2,15 @@
 build-backend = "setuptools.build_meta"
 requires = [
   "setuptools>=61.2",
 ]
 
 [project]
 name = "ignition_api_stubs"
-version = "8.1.26.post1"
+version = "8.1.26.post2"
 description = "Ignition Scripting API Stubs"
 readme = "README.md"
 keywords = [
   "hmi",
   "ignition",
   "inductive automation",
   "scada",
```

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/ch/qos/logback/classic/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/ch/qos/logback/classic/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/com/codahale/metrics/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/com/codahale/metrics/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/com/google/common/collect/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/com/google/common/collect/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/factorypmi/application/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/factorypmi/application/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/factorypmi/application/binding/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/factorypmi/application/binding/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/factorypmi/application/script/builtin/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/factorypmi/application/script/builtin/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/client/launch/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/client/launch/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/client/model/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/client/model/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/client/util/gui/progress/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/client/util/gui/progress/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/client/util/gui/scheduling/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/client/util/gui/scheduling/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/__init__.pyi`

 * *Files 11% similar despite different names*

```diff
@@ -1,19 +1,11 @@
 from typing import Any, Iterable, List, Optional, Set, Union
 
 from com.inductiveautomation.ignition.common.document import DocumentElement
 from com.inductiveautomation.ignition.common.gson import Gson, JsonElement
-from com.inductiveautomation.ignition.common.model.values import (
-    QualifiedValue,
-    QualityCode,
-)
-from com.inductiveautomation.ignition.common.sqltags.model.types import (
-    DataQuality,
-    DataType,
-)
 from dev.thecesrom.helper.types import AnyStr
 from java.awt import Color
 from java.lang import Class, Comparable, Number, Object
 from java.util import UUID, Comparator, Date, Locale
 from org.json import JSONObject
 from org.python.core import PyObject
 
@@ -23,39 +15,37 @@
     def getColumnCount(self) -> int: ...
     def getColumnIndex(self, colName: AnyStr) -> int: ...
     def getColumnName(self, col: int) -> AnyStr: ...
     def getColumnNames(self) -> List[AnyStr]: ...
     def getColumnType(self, col: int) -> Class: ...
     def getColumnTypes(self) -> List[Class]: ...
     def getPrimitiveValueAt(self, row: int, col: int) -> float: ...
-    def getQualityAt(self, row: int, col: int) -> QualityCode: ...
+    def getQualityAt(self, row: int, col: int) -> Any: ...
     def getRowCount(self) -> int: ...
     def getValueAt(self, row: int, col: Union[int, AnyStr]) -> Any: ...
     def hasQualityData(self) -> bool: ...
 
 class AbstractDataset(Dataset):
     def __init__(
         self,
         columnNames: List[AnyStr],
         columnTypes: List[Class],
-        qualityCodes: Optional[List[List[QualityCode]]] = ...,
+        qualityCodes: Optional[List[List[Any]]] = ...,
     ) -> None: ...
     @staticmethod
-    def convertToQualityCodes(
-        dataQualities: List[List[DataQuality]],
-    ) -> List[List[QualityCode]]: ...
-    def getBulkQualityCodes(self) -> List[List[QualityCode]]: ...
+    def convertToQualityCodes(dataQualities: List[List[Any]]) -> List[List[Any]]: ...
+    def getBulkQualityCodes(self) -> List[List[Any]]: ...
     def getColumnCount(self) -> int: ...
     def getColumnIndex(self, colName: AnyStr) -> int: ...
     def getColumnName(self, col: int) -> AnyStr: ...
     def getColumnNames(self) -> List[AnyStr]: ...
     def getColumnType(self, col: int) -> Class: ...
     def getColumnTypes(self) -> List[Class]: ...
     def getPrimitiveValueAt(self, row: int, col: int) -> float: ...
-    def getQualityAt(self, row: int, col: int) -> QualityCode: ...
+    def getQualityAt(self, row: int, col: int) -> Any: ...
     def getRowCount(self) -> int: ...
     def getValueAt(self, row: int, col: Union[int, AnyStr]) -> Any: ...
     def setColumnNames(self, arg: List[str]) -> None: ...
     def setColumnTypes(self, arg: List[Class]) -> None: ...
     def setDirty(self) -> None: ...
 
 class BasicDataset(AbstractDataset):
@@ -200,18 +190,15 @@
     def getWrapperType(c: Class) -> Class: ...
     @staticmethod
     def gsonToPy(element: JsonElement) -> PyObject: ...
     @staticmethod
     def hasPrimitiveType(c: Class) -> bool: ...
     @staticmethod
     def hasValueChanged(
-        currentValue: QualifiedValue,
-        previousValue: QualifiedValue,
-        expectedType: DataType,
-        deadband: float,
+        currentValue: Any, previousValue: Any, expectedType: Any, deadband: float
     ) -> bool: ...
     @staticmethod
     def isAssignable(dest: Class, source: Class) -> bool: ...
     @staticmethod
     def isBoolean(clazz: Class) -> bool: ...
     @staticmethod
     def isDirectlyAssignable(dest: Class, source: Class) -> bool: ...
@@ -230,15 +217,15 @@
     @staticmethod
     def pyToGson(
         pyObject: PyObject, customGson: Optional[Gson] = ...
     ) -> JsonElement: ...
     @staticmethod
     def pyToJava(pyObject: PyObject) -> Object: ...
     @staticmethod
-    def setArrayValue(arrayValue: Object, newVal: Object, pos: int) -> QualityCode: ...
+    def setArrayValue(arrayValue: Object, newVal: Object, pos: int) -> Any: ...
     @staticmethod
     def setClassInitializer(init: TypeUtilities.ClassInitializer) -> None: ...
     @staticmethod
     def toBool(value: Object) -> bool: ...
     @staticmethod
     def toByteArray(uuid: UUID) -> bytearray: ...
     @staticmethod
```

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/alarming/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/alarming/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/alarming/evaluation/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/alarming/evaluation/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/alarming/query/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/alarming/query/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/browsing/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/browsing/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/config/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/config/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/db/namedquery/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/db/namedquery/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/execution/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/execution/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/expressions/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/expressions/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/expressions/functions/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/expressions/functions/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/gson/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/gson/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/gson/stream/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/gson/stream/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/gui/progress/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/gui/progress/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/i18n/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/i18n/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/jsonschema/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/jsonschema/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/licensing/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/licensing/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/logging/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/logging/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/messages/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/messages/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/model/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/model/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/model/values/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/model/values/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/modules/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/modules/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/opc/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/opc/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/project/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/project/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/project/resource/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/project/resource/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/script/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/script/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/script/abc/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/script/abc/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/script/adapters/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/script/adapters/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/script/builtin/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/script/builtin/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/script/builtin/http/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/script/builtin/http/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/script/builtin/ialabs/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/script/builtin/ialabs/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/script/message/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/script/message/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/sqltags/history/annotations/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/sqltags/history/annotations/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/sqltags/model/types/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/sqltags/model/types/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/tags/model/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/tags/model/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/tags/paths/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/tags/paths/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/tags/paths/parser/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/tags/paths/parser/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/user/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/user/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/user/schedule/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/user/schedule/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/util/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/util/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/xmlserialization/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/xmlserialization/__init__.pyi`

 * *Files 20% similar despite different names*

```diff
@@ -1,16 +1,16 @@
 from typing import Any
 
-import java.lang
 from dev.thecesrom.helper.types import AnyStr
+from java.lang import Class, Exception, Object
 
-class ClassNameResolver(java.lang.Object):
+class ClassNameResolver(Object):
     def __init__(self) -> None: ...
-    def addAlias(self, clazz: java.lang.Class, alias: AnyStr) -> None: ...
+    def addAlias(self, clazz: Class, alias: AnyStr) -> None: ...
     def addDefaults(self) -> None: ...
     def addSearchPath(self, path: AnyStr) -> None: ...
-    def classForName(self, name: AnyStr) -> java.lang.Class: ...
+    def classForName(self, name: AnyStr) -> Class: ...
     def createBasic(self) -> ClassNameResolver: ...
-    def getName(self, clazz: java.lang.Class) -> AnyStr: ...
+    def getName(self, clazz: Class) -> AnyStr: ...
 
-class SerializationException(java.lang.Exception):
+class SerializationException(Exception):
     def __init__(self, *args: Any) -> None: ...
```

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/xmlserialization/deserialization/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/xmlserialization/deserialization/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/common/xmlserialization/serialization/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/common/xmlserialization/serialization/__init__.pyi`

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,7 @@
-# flake8: noqa
 from typing import Any, List
 
 from com.inductiveautomation.ignition.common.xmlserialization import ClassNameResolver
 from com.inductiveautomation.ignition.common.xmlserialization.encoding import (
     AttributeEncoder,
 )
 from com.inductiveautomation.ignition.common.xmlserialization.serialization.equalitydelegates import (
```

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/gateway/project/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/gateway/project/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/ignition/modules/serial/scripting/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/ignition/modules/serial/scripting/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/opccom/hda/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/opccom/hda/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/com/inductiveautomation/perspective/common/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/com/inductiveautomation/perspective/common/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/ignition_api_stubs.egg-info/PKG-INFO` & `ignition_api_stubs-8.1.26.post2/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
-Name: ignition-api-stubs
-Version: 8.1.26.post1
+Name: ignition_api_stubs
+Version: 8.1.26.post2
 Summary: Ignition Scripting API Stubs
 Author-email: César Román <cesar@thecesrom.dev>
 License: MIT License
         
         Copyright (c) 2022 César Román
         
         Permission is hereby granted, free of charge, to any person obtaining a copy
```

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/ignition_api_stubs.egg-info/SOURCES.txt` & `ignition_api_stubs-8.1.26.post2/stubs/ignition_api_stubs.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/java/awt/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/java/awt/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/java/awt/event/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/java/awt/event/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/java/awt/geom/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/java/awt/geom/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/java/awt/print/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/java/awt/print/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/java/beans/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/java/beans/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/java/io/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/java/io/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/java/lang/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/java/lang/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/java/net/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/java/net/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/java/nio/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/java/nio/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/java/nio/channels/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/java/nio/channels/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/java/nio/charset/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/java/nio/charset/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/java/nio/file/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/java/nio/file/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/java/nio/file/attribute/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/java/nio/file/attribute/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/java/text/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/java/text/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/java/time/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/java/time/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/java/time/temporal/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/java/time/temporal/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/java/util/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/java/util/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/java/util/concurrent/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/java/util/concurrent/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/java/util/function/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/java/util/function/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/java/util/regex/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/java/util/regex/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/java/util/stream/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/java/util/stream/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/javax/swing/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/javax/swing/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/javax/swing/event/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/javax/swing/event/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/org/apache/commons/lang3/builder/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/org/apache/commons/lang3/builder/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/org/apache/commons/math3/exception/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/org/apache/commons/math3/exception/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/org/apache/commons/math3/exception/util/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/org/apache/commons/math3/exception/util/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/org/apache/log4j/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/org/apache/log4j/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/org/apache/log4j/spi/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/org/apache/log4j/spi/__init__.pyi`

 * *Files 4% similar despite different names*

```diff
@@ -1,22 +1,22 @@
 from typing import Any, Optional
 
-import java.lang
 from dev.thecesrom.helper.types import AnyStr
+from java.lang import Exception, Object
 from java.util import Enumeration
 
 class OptionHandler:
     def activateOptions(self) -> None: ...
 
 class ErrorHandler(OptionHandler):
     def activateOptions(self) -> None: ...
     def error(
         self,
         message: AnyStr,
-        e: Optional[java.lang.Exception] = ...,
+        e: Optional[Exception] = ...,
         errorCode: Optional[int] = ...,
         event: Optional[LoggingEvent] = ...,
     ) -> None: ...
     def setAppender(self, appender: Any) -> None: ...
     def setBackupAppender(self, appender: Any) -> None: ...
     def setLogger(self, logger: Any) -> None: ...
 
@@ -39,19 +39,19 @@
     def getRootLogger(self) -> Any: ...
     def getThreshold(self) -> Any: ...
     def isDisabled(self, level: int) -> bool: ...
     def resetConfiguration(self) -> None: ...
     def setThreshold(self, arg: Any) -> None: ...
     def shutdown(self) -> None: ...
 
-class Filter(java.lang.Object, OptionHandler):
+class Filter(Object, OptionHandler):
     def activateOptions(self) -> None: ...
     def decide(self, event: LoggingEvent) -> int: ...
     def getNext(self) -> Filter: ...
     def setNext(self, next: Filter) -> None: ...
 
-class LoggingEvent(java.lang.Object):
+class LoggingEvent(Object):
     categoryName: AnyStr
     fqnOfCategoryClass: AnyStr
     level: Any
     timeStamp: long
     def __init__(self, *args: Any) -> None: ...
```

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/org/json/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/org/json/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/org/python/core/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/org/python/core/__init__.pyi`

 * *Files 7% similar despite different names*

```diff
@@ -1,15 +1,17 @@
 from copy import PyStringMap as PyStringMap  # noqa: F401
 from typing import Any, Iterable, Iterator, List, Mapping, Optional, Tuple, Union
 
-import java.util
 from dev.thecesrom.helper.types import AnyStr
 from enum import Enum
 from java.io import PrintWriter
 from java.lang import Class, Object, RuntimeException, StringBuilder
+from java.util import Collection
+from java.util import Iterator as JIterator
+from java.util import ListIterator, Properties
 from org.python.expose import TypeBuilder
 
 class PyObject(Object):
     gcMonitorGlobal: bool
     TYPE: PyType
     def __init__(self, objtype: Optional[PyType] = ...) -> None: ...
     def __abs__(self) -> PyObject: ...
@@ -311,62 +313,62 @@
 class PySequence(PyObject): ...
 
 class PySequenceList(PySequence):
     def add(self, *args: Any) -> Optional[bool]: ...
     def addAll(self, *args: Any) -> bool: ...
     def clear(self) -> None: ...
     def contains(self, o: Object) -> bool: ...
-    def containsAll(self, c: java.util.Collection) -> bool: ...
+    def containsAll(self, c: Collection) -> bool: ...
     def get(self, index: int) -> Object: ...
     def getArray(self) -> List[PyObject]: ...
     def indexOf(self, o: Object) -> int: ...
     def isEmpty(self) -> bool: ...
-    def iterator(self) -> java.util.Iterator: ...
+    def iterator(self) -> JIterator: ...
     def lastIndexOf(self, o: Object) -> int: ...
-    def listIterator(self, index: Optional[int] = ...) -> java.util.ListIterator: ...
+    def listIterator(self, index: Optional[int] = ...) -> ListIterator: ...
     def pyadd(self, *args: Any) -> Optional[bool]: ...
     def pyget(self, index: int) -> PyObject: ...
     def pyset(self, index: int, element: PyObject) -> None: ...
     def refersDirectlyTo(self, ob: PyObject) -> bool: ...
     def remove(self, *args: Any) -> Union[bool, None, Object]: ...
-    def removeAll(self, c: java.util.Collection) -> bool: ...
-    def retainAll(self, c: java.util.Collection) -> bool: ...
+    def removeAll(self, c: Collection) -> bool: ...
+    def retainAll(self, c: Collection) -> bool: ...
     def set(self, index: int, element: Object) -> Object: ...
     def size(self) -> int: ...
     def subList(self, fromIndex: int, toIndex: int) -> List[PyObject]: ...
     def toArray(self, a: Optional[List[Object]] = ...) -> List[Object]: ...
     def traverse(self, visit: Visitproc, arg: Object) -> int: ...
 
 class PyList(PySequenceList):
     def __init__(self, *args: Any) -> None: ...
     def add(self, *args: Any) -> Optional[bool]: ...
     def addAll(self, *args: Any) -> bool: ...
     def append(self, o: PyObject) -> None: ...
     def clear(self) -> None: ...
     def contains(self, o: Object) -> bool: ...
-    def containsAll(self, c: java.util.Collection) -> bool: ...
+    def containsAll(self, c: Collection) -> bool: ...
     def count(self, o: PyObject) -> int: ...
     def extend(self, o: PyObject) -> None: ...
     @staticmethod
     def fromList(list_: List[PyObject]) -> PyList: ...
     def get(self, index: int) -> Object: ...
     def getArray(self) -> List[PyObject]: ...
     def index(self, o: PyObject, *args: int) -> int: ...
     def indexOf(self, o: Object) -> int: ...
     def insert(self, o: PyObject) -> None: ...
     def isEmpty(self) -> bool: ...
-    def iterator(self) -> java.util.Iterator: ...
+    def iterator(self) -> JIterator: ...
     def lastIndexOf(self, o: Object) -> int: ...
-    def listIterator(self, index: Optional[int] = ...) -> java.util.ListIterator: ...
+    def listIterator(self, index: Optional[int] = ...) -> ListIterator: ...
     def pyadd(self, *args: Any) -> Optional[bool]: ...
     def pyget(self, index: int) -> PyObject: ...
     def pyset(self, index: int, element: PyObject) -> None: ...
     def remove(self, *args: Any) -> Union[bool, None, Object]: ...
-    def removeAll(self, c: java.util.Collection) -> bool: ...
-    def retainAll(self, c: java.util.Collection) -> bool: ...
+    def removeAll(self, c: Collection) -> bool: ...
+    def retainAll(self, c: Collection) -> bool: ...
     def reverse(self) -> None: ...
     def set(self, index: int, element: Object) -> Object: ...
     def size(self) -> int: ...
     def sort(self, *args: PyObject) -> None: ...
     def subList(self, fromIndex: int, toIndex: int) -> List[PyObject]: ...
     def toArray(self, a: Optional[List[Object]] = ...) -> List[Object]: ...
 
@@ -419,15 +421,15 @@
     @staticmethod
     def prefix() -> PyObject: ...
     def ps1(self) -> PyObject: ...
     def ps2(self) -> PyObject: ...
     @staticmethod
     def py3kwarning() -> bool: ...
     @staticmethod
-    def registry() -> java.util.Properties: ...
+    def registry() -> Properties: ...
     def stderr(self) -> PyObject: ...
     def stdin(self) -> PyObject: ...
     def stdout(self) -> PyObject: ...
     @staticmethod
     def subversion() -> PyTuple: ...
     @staticmethod
     def version() -> PyString: ...
@@ -446,32 +448,32 @@
 
 class PyTuple(PySequenceList):
     def __init__(self, *args: Any) -> None: ...
     def add(self, *args: Any) -> Optional[bool]: ...
     def addAll(self, *args: Any) -> bool: ...
     def clear(self) -> None: ...
     def contains(self, o: Object) -> bool: ...
-    def containsAll(self, c: java.util.Collection) -> bool: ...
+    def containsAll(self, c: Collection) -> bool: ...
     def count(self, value: PyObject) -> int: ...
     @staticmethod
     def fromIterable(iterable: PyObject) -> PyTuple: ...
     def get(self, index: int) -> Object: ...
     def getArray(self) -> List[PyObject]: ...
     def index(self, value: PyObject, *args: int) -> int: ...
     def indexOf(self, o: Object) -> int: ...
     def isEmpty(self) -> bool: ...
-    def iterator(self) -> java.util.Iterator: ...
+    def iterator(self) -> JIterator: ...
     def lastIndexOf(self, o: Object) -> int: ...
-    def listIterator(self, index: Optional[int] = ...) -> java.util.ListIterator: ...
+    def listIterator(self, index: Optional[int] = ...) -> ListIterator: ...
     def pyadd(self, *args: Any) -> Optional[bool]: ...
     def pyget(self, index: int) -> PyObject: ...
     def pyset(self, index: int, element: PyObject) -> None: ...
     def remove(self, *args: Any) -> Union[bool, None, Object]: ...
-    def removeAll(self, c: java.util.Collection) -> bool: ...
-    def retainAll(self, c: java.util.Collection) -> bool: ...
+    def removeAll(self, c: Collection) -> bool: ...
+    def retainAll(self, c: Collection) -> bool: ...
     def set(self, index: int, element: Object) -> Object: ...
     def size(self) -> int: ...
     def subList(self, fromIndex: int, toIndex: int) -> List[PyObject]: ...
     def toArray(self, a: Optional[List[Object]] = ...) -> List[Object]: ...
     def tuple___iter__(self) -> PyObject: ...
 
 class PyType(PyObject):
```

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/org/slf4j/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/org/slf4j/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/system/alarm.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/system/alarm.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/system/bacnet/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/system/bacnet/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/system/bacnet/enumerated.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/system/bacnet/enumerated.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/system/bacnet/enums.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/system/bacnet/enums.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/system/dataset.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/system/dataset.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/system/date.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/system/date.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/system/db.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/system/db.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/system/device.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/system/device.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/system/dnp3.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/system/dnp3.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/system/eam.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/system/eam.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/system/file.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/system/file.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/system/gui.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/system/gui.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/system/iec61850.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/system/iec61850.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/system/math.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/system/math.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/system/nav.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/system/nav.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/system/net.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/system/net.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/system/opc.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/system/opc.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/system/opchda.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/system/opchda.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/system/perspective/__init__.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/system/perspective/__init__.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/system/print.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/system/print.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/system/report.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/system/report.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/system/roster.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/system/roster.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/system/secsgem.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/system/secsgem.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/system/security.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/system/security.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/system/serial.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/system/serial.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/system/sfc.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/system/sfc.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/system/tag.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/system/tag.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/system/user.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/system/user.pyi`

 * *Files identical despite different names*

### Comparing `ignition_api_stubs-8.1.26.post1/stubs/system/util.pyi` & `ignition_api_stubs-8.1.26.post2/stubs/system/util.pyi`

 * *Files identical despite different names*

