# Comparing `tmp/inmanta-core-8.1.0.tar.gz` & `tmp/inmanta-core-8.2.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "inmanta-core-8.1.0.tar", last modified: Mon Feb  6 15:21:11 2023, max compression
+gzip compressed data, was "inmanta-core-8.2.0.tar", last modified: Thu Feb  9 10:00:27 2023, max compression
```

## Comparing `inmanta-core-8.1.0.tar` & `inmanta-core-8.2.0.tar`

### file list

```diff
@@ -1,202 +1,245 @@
-drwxrwxr-x   0 jenkins    (989) jenkins    (987)        0 2023-02-06 15:21:11.344027 inmanta-core-8.1.0/
--rw-rw-r--   0 jenkins    (989) jenkins    (987)    10174 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/LICENSE
--rw-rw-r--   0 jenkins    (989) jenkins    (987)      311 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/MANIFEST.in
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     3182 2023-02-06 15:21:11.345027 inmanta-core-8.1.0/PKG-INFO
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     2225 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/README.md
-drwxrwxr-x   0 jenkins    (989) jenkins    (987)        0 2023-02-06 15:21:11.326026 inmanta-core-8.1.0/misc/
--rw-rw-r--   0 jenkins    (989) jenkins    (987)       31 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/misc/extensions.cfg
--rw-rw-r--   0 jenkins    (989) jenkins    (987)      402 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/misc/inmanta-agent.service
--rw-rw-r--   0 jenkins    (989) jenkins    (987)      333 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/misc/inmanta-server.service
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     7608 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/misc/inmanta-workon-register.sh
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     2906 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/misc/inmanta.cfg
--rw-rw-r--   0 jenkins    (989) jenkins    (987)    12162 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/misc/inmanta.lang
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     1205 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/misc/inmanta.vim
--rw-rw-r--   0 jenkins    (989) jenkins    (987)      141 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/misc/logrotation_config
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     1432 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/pyproject.toml
--rw-rw-r--   0 jenkins    (989) jenkins    (987)      918 2023-02-06 15:21:11.345027 inmanta-core-8.1.0/setup.cfg
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     3306 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/setup.py
-drwxrwxr-x   0 jenkins    (989) jenkins    (987)        0 2023-02-06 15:21:11.325026 inmanta-core-8.1.0/src/
-drwxrwxr-x   0 jenkins    (989) jenkins    (987)        0 2023-02-06 15:21:11.329026 inmanta-core-8.1.0/src/inmanta/
--rw-rw-r--   0 jenkins    (989) jenkins    (987)      914 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/__init__.py
-drwxrwxr-x   0 jenkins    (989) jenkins    (987)        0 2023-02-06 15:21:11.330026 inmanta-core-8.1.0/src/inmanta/agent/
--rw-rw-r--   0 jenkins    (989) jenkins    (987)      738 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/agent/__init__.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)    58982 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/agent/agent.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)    10115 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/agent/cache.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     4634 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/agent/config.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)    42405 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/agent/handler.py
-drwxrwxr-x   0 jenkins    (989) jenkins    (987)        0 2023-02-06 15:21:11.330026 inmanta-core-8.1.0/src/inmanta/agent/io/
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     2815 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/agent/io/__init__.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)    19870 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/agent/io/local.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     6362 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/agent/io/remote.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     3395 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/agent/reporting.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)    31738 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/app.py
-drwxrwxr-x   0 jenkins    (989) jenkins    (987)        0 2023-02-06 15:21:11.331026 inmanta-core-8.1.0/src/inmanta/ast/
--rw-rw-r--   0 jenkins    (989) jenkins    (987)    30203 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/ast/__init__.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     7103 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/ast/attribute.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     6355 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/ast/blocks.py
-drwxrwxr-x   0 jenkins    (989) jenkins    (987)        0 2023-02-06 15:21:11.331026 inmanta-core-8.1.0/src/inmanta/ast/constraint/
--rw-rw-r--   0 jenkins    (989) jenkins    (987)      627 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/ast/constraint/__init__.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)    17187 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/ast/constraint/expression.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)    18701 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/ast/entity.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     2783 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/ast/export.py
-drwxrwxr-x   0 jenkins    (989) jenkins    (987)        0 2023-02-06 15:21:11.332026 inmanta-core-8.1.0/src/inmanta/ast/statements/
--rw-rw-r--   0 jenkins    (989) jenkins    (987)    22445 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/ast/statements/__init__.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)    21870 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/ast/statements/assign.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)    12251 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/ast/statements/call.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)    24368 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/ast/statements/define.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)    37332 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/ast/statements/generator.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)    20697 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/ast/type.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)    12047 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/ast/variables.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     2985 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/command.py
-drwxrwxr-x   0 jenkins    (989) jenkins    (987)        0 2023-02-06 15:21:11.332026 inmanta-core-8.1.0/src/inmanta/compiler/
--rw-rw-r--   0 jenkins    (989) jenkins    (987)    13889 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/compiler/__init__.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     1963 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/compiler/config.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     1110 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/compiler/data.py
-drwxrwxr-x   0 jenkins    (989) jenkins    (987)        0 2023-02-06 15:21:11.332026 inmanta-core-8.1.0/src/inmanta/compiler/help/
--rw-rw-r--   0 jenkins    (989) jenkins    (987)      627 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/compiler/help/__init__.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     8327 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/compiler/help/explainer.py
-drwxrwxr-x   0 jenkins    (989) jenkins    (987)        0 2023-02-06 15:21:11.333026 inmanta-core-8.1.0/src/inmanta/compiler/help/templates/
--rw-rw-r--   0 jenkins    (989) jenkins    (987)      235 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/compiler/help/templates/index_collision.j2
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     3604 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/compiler/help/templates/modified_after_freeze.j2
--rw-rw-r--   0 jenkins    (989) jenkins    (987)      733 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/compiler/help/templates/module_v2_in_v1_path.j2
--rw-rw-r--   0 jenkins    (989) jenkins    (987)    20658 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/config.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     9187 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/const.py
-drwxrwxr-x   0 jenkins    (989) jenkins    (987)        0 2023-02-06 15:21:11.333026 inmanta-core-8.1.0/src/inmanta/data/
--rw-rw-r--   0 jenkins    (989) jenkins    (987)   224939 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/data/__init__.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)    43652 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/data/dataview.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)    21756 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/data/model.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)    12205 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/data/schema.py
-drwxrwxr-x   0 jenkins    (989) jenkins    (987)        0 2023-02-06 15:21:11.334026 inmanta-core-8.1.0/src/inmanta/db/
--rw-rw-r--   0 jenkins    (989) jenkins    (987)      627 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/db/__init__.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     5462 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/db/util.py
-drwxrwxr-x   0 jenkins    (989) jenkins    (987)        0 2023-02-06 15:21:11.337026 inmanta-core-8.1.0/src/inmanta/db/versions/
--rw-rw-r--   0 jenkins    (989) jenkins    (987)      627 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/db/versions/__init__.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)    12131 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/db/versions/v1.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     1737 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/db/versions/v17.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     1393 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/db/versions/v2.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     2443 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/db/versions/v202105170.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)      915 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/db/versions/v202106080.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     1247 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/db/versions/v202106210.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     1826 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/db/versions/v202109100.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)      979 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/db/versions/v202111260.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     1581 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/db/versions/v202203140.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     2200 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/db/versions/v202203160.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)      910 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/db/versions/v202205250.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)      979 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/db/versions/v202206290.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)      948 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/db/versions/v202208180.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     1881 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/db/versions/v202208190.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)      976 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/db/versions/v202209090.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     3957 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/db/versions/v202209130.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)      861 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/db/versions/v202209160.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     2919 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/db/versions/v202211230.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     1430 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/db/versions/v202212010.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     1494 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/db/versions/v202301100.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)      924 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/db/versions/v202301110.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)      977 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/db/versions/v202301120.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)      929 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/db/versions/v202301160.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)      896 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/db/versions/v202301170.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     1313 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/db/versions/v202301190.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     1471 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/db/versions/v3.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     3556 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/db/versions/v4.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     1529 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/db/versions/v5.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     1043 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/db/versions/v6.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     1558 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/db/versions/v7.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)    16438 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/deploy.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     2694 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/docstring_parser.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)    56383 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/env.py
-drwxrwxr-x   0 jenkins    (989) jenkins    (987)        0 2023-02-06 15:21:11.337026 inmanta-core-8.1.0/src/inmanta/execute/
--rw-rw-r--   0 jenkins    (989) jenkins    (987)      627 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/execute/__init__.py
-drwxrwxr-x   0 jenkins    (989) jenkins    (987)        0 2023-02-06 15:21:11.338026 inmanta-core-8.1.0/src/inmanta/execute/dataflow/
--rw-rw-r--   0 jenkins    (989) jenkins    (987)    41029 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/execute/dataflow/__init__.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     9488 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/execute/dataflow/datatrace.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     7405 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/execute/dataflow/graphic.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     7152 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/execute/dataflow/root_cause.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     8478 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/execute/proxy.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)    46717 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/execute/runtime.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)    30085 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/execute/scheduler.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     1807 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/execute/tracking.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     1451 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/execute/util.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)    25455 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/export.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     5488 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/file_parser.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)    24386 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/loader.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)    35363 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/main.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     9146 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/model.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)   140687 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/module.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)    81338 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/moduletool.py
-drwxrwxr-x   0 jenkins    (989) jenkins    (987)        0 2023-02-06 15:21:11.339026 inmanta-core-8.1.0/src/inmanta/parser/
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     2934 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/parser/__init__.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     5591 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/parser/cache.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)   505683 2023-02-06 15:21:02.000000 inmanta-core-8.1.0/src/inmanta/parser/parser.out
--rw-rw-r--   0 jenkins    (989) jenkins    (987)    66421 2023-02-06 15:21:02.000000 inmanta-core-8.1.0/src/inmanta/parser/parsetab.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     1563 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/parser/pickle.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     7799 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/parser/plyInmantaLex.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)    36122 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/parser/plyInmantaParser.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)    21187 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/plugins.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     5509 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/postgresproc.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)      734 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/profile_mem.py
-drwxrwxr-x   0 jenkins    (989) jenkins    (987)        0 2023-02-06 15:21:11.340026 inmanta-core-8.1.0/src/inmanta/protocol/
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     3131 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/protocol/__init__.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)    40283 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/protocol/common.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     8549 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/protocol/decorators.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)    17519 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/protocol/endpoints.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     4455 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/protocol/exceptions.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)    32908 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/protocol/methods.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)    59046 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/protocol/methods_v2.py
-drwxrwxr-x   0 jenkins    (989) jenkins    (987)        0 2023-02-06 15:21:11.340026 inmanta-core-8.1.0/src/inmanta/protocol/openapi/
--rw-rw-r--   0 jenkins    (989) jenkins    (987)      627 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/protocol/openapi/__init__.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)    19132 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/protocol/openapi/converter.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     8343 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/protocol/openapi/model.py
-drwxrwxr-x   0 jenkins    (989) jenkins    (987)        0 2023-02-06 15:21:11.341026 inmanta-core-8.1.0/src/inmanta/protocol/rest/
--rw-rw-r--   0 jenkins    (989) jenkins    (987)    21717 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/protocol/rest/__init__.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     6064 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/protocol/rest/client.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)    13872 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/protocol/rest/server.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     2158 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/protocol/return_value_meta.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)        0 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/py.typed
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     6273 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/reporter.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)    23112 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/resources.py
-drwxrwxr-x   0 jenkins    (989) jenkins    (987)        0 2023-02-06 15:21:11.342027 inmanta-core-8.1.0/src/inmanta/server/
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     1338 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/server/__init__.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)    56391 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/server/agentmanager.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     9731 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/server/bootloader.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)      688 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/server/compilerservice.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)    10111 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/server/config.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     7314 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/server/diff.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     7672 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/server/extensions.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)    27495 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/server/protocol.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     7036 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/server/server.py
-drwxrwxr-x   0 jenkins    (989) jenkins    (987)        0 2023-02-06 15:21:11.343026 inmanta-core-8.1.0/src/inmanta/server/services/
--rw-rw-r--   0 jenkins    (989) jenkins    (987)      627 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/server/services/__init__.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     5702 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/server/services/codeservice.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)    38106 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/server/services/compilerservice.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     4850 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/server/services/databaseservice.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)    11640 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/server/services/dryrunservice.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)    25390 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/server/services/environment_metrics_service.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)    27831 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/server/services/environmentservice.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     6242 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/server/services/fileservice.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     4551 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/server/services/metricservice.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     7970 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/server/services/notificationservice.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)    48458 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/server/services/orchestrationservice.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)    13605 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/server/services/paramservice.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     6154 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/server/services/projectservice.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)    43300 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/server/services/resourceservice.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)    11714 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/server/validate_filter.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)      865 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/stable_api.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     2927 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/types.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)    24125 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/util.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     6487 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta/warnings.py
-drwxrwxr-x   0 jenkins    (989) jenkins    (987)        0 2023-02-06 15:21:11.344027 inmanta-core-8.1.0/src/inmanta_core.egg-info/
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     3182 2023-02-06 15:21:11.000000 inmanta-core-8.1.0/src/inmanta_core.egg-info/PKG-INFO
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     5625 2023-02-06 15:21:11.000000 inmanta-core-8.1.0/src/inmanta_core.egg-info/SOURCES.txt
--rw-rw-r--   0 jenkins    (989) jenkins    (987)        1 2023-02-06 15:21:11.000000 inmanta-core-8.1.0/src/inmanta_core.egg-info/dependency_links.txt
--rw-rw-r--   0 jenkins    (989) jenkins    (987)       76 2023-02-06 15:21:11.000000 inmanta-core-8.1.0/src/inmanta_core.egg-info/entry_points.txt
--rw-rw-r--   0 jenkins    (989) jenkins    (987)        1 2023-02-06 15:20:54.000000 inmanta-core-8.1.0/src/inmanta_core.egg-info/not-zip-safe
--rw-rw-r--   0 jenkins    (989) jenkins    (987)      577 2023-02-06 15:21:11.000000 inmanta-core-8.1.0/src/inmanta_core.egg-info/requires.txt
--rw-rw-r--   0 jenkins    (989) jenkins    (987)       36 2023-02-06 15:21:11.000000 inmanta-core-8.1.0/src/inmanta_core.egg-info/top_level.txt
-drwxrwxr-x   0 jenkins    (989) jenkins    (987)        0 2023-02-06 15:21:11.325026 inmanta-core-8.1.0/src/inmanta_ext/
-drwxrwxr-x   0 jenkins    (989) jenkins    (987)        0 2023-02-06 15:21:11.344027 inmanta-core-8.1.0/src/inmanta_ext/core/
--rw-rw-r--   0 jenkins    (989) jenkins    (987)      627 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta_ext/core/__init__.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     2163 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta_ext/core/extension.py
-drwxrwxr-x   0 jenkins    (989) jenkins    (987)        0 2023-02-06 15:21:11.325026 inmanta-core-8.1.0/src/inmanta_plugins/
-drwxrwxr-x   0 jenkins    (989) jenkins    (987)        0 2023-02-06 15:21:11.344027 inmanta-core-8.1.0/src/inmanta_plugins/1/
--rw-rw-r--   0 jenkins    (989) jenkins    (987)      627 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/src/inmanta_plugins/1/__init__.py
--rw-rw-r--   0 jenkins    (989) jenkins    (987)     1924 2023-02-06 15:19:08.000000 inmanta-core-8.1.0/tox.ini
+drwxrwxr-x   0 jenkins    (989) jenkins    (987)        0 2023-02-09 10:00:27.838055 inmanta-core-8.2.0/
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)    10174 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/LICENSE
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)      311 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/MANIFEST.in
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     3182 2023-02-09 10:00:27.838055 inmanta-core-8.2.0/PKG-INFO
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     2225 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/README.md
+drwxrwxr-x   0 jenkins    (989) jenkins    (987)        0 2023-02-09 10:00:27.814053 inmanta-core-8.2.0/misc/
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)       31 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/misc/extensions.cfg
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)      402 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/misc/inmanta-agent.service
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)      333 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/misc/inmanta-server.service
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     7608 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/misc/inmanta-workon-register.sh
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     2906 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/misc/inmanta.cfg
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)    12162 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/misc/inmanta.lang
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     1205 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/misc/inmanta.vim
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)      141 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/misc/logrotation_config
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     1432 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/pyproject.toml
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)      918 2023-02-09 10:00:27.839054 inmanta-core-8.2.0/setup.cfg
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     3306 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/setup.py
+drwxrwxr-x   0 jenkins    (989) jenkins    (987)        0 2023-02-09 10:00:27.812053 inmanta-core-8.2.0/src/
+drwxrwxr-x   0 jenkins    (989) jenkins    (987)        0 2023-02-09 10:00:27.817054 inmanta-core-8.2.0/src/inmanta/
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)      914 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/__init__.py
+drwxrwxr-x   0 jenkins    (989) jenkins    (987)        0 2023-02-09 10:00:27.818054 inmanta-core-8.2.0/src/inmanta/agent/
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)      738 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/agent/__init__.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)    58982 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/agent/agent.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)    10115 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/agent/cache.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     4634 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/agent/config.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)    42405 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/agent/handler.py
+drwxrwxr-x   0 jenkins    (989) jenkins    (987)        0 2023-02-09 10:00:27.818054 inmanta-core-8.2.0/src/inmanta/agent/io/
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     2815 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/agent/io/__init__.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)    19870 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/agent/io/local.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     6362 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/agent/io/remote.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     3395 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/agent/reporting.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)    31738 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/app.py
+drwxrwxr-x   0 jenkins    (989) jenkins    (987)        0 2023-02-09 10:00:27.819054 inmanta-core-8.2.0/src/inmanta/ast/
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)    30203 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/ast/__init__.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     7103 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/ast/attribute.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     6355 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/ast/blocks.py
+drwxrwxr-x   0 jenkins    (989) jenkins    (987)        0 2023-02-09 10:00:27.819054 inmanta-core-8.2.0/src/inmanta/ast/constraint/
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)      627 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/ast/constraint/__init__.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)    17187 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/ast/constraint/expression.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)    18701 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/ast/entity.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     2783 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/ast/export.py
+drwxrwxr-x   0 jenkins    (989) jenkins    (987)        0 2023-02-09 10:00:27.820054 inmanta-core-8.2.0/src/inmanta/ast/statements/
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)    22445 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/ast/statements/__init__.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)    21870 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/ast/statements/assign.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)    12251 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/ast/statements/call.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)    24368 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/ast/statements/define.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)    37332 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/ast/statements/generator.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)    20697 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/ast/type.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)    12047 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/ast/variables.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     2985 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/command.py
+drwxrwxr-x   0 jenkins    (989) jenkins    (987)        0 2023-02-09 10:00:27.820054 inmanta-core-8.2.0/src/inmanta/compiler/
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)    13889 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/compiler/__init__.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     1963 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/compiler/config.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     1110 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/compiler/data.py
+drwxrwxr-x   0 jenkins    (989) jenkins    (987)        0 2023-02-09 10:00:27.820054 inmanta-core-8.2.0/src/inmanta/compiler/help/
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)      627 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/compiler/help/__init__.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     8327 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/compiler/help/explainer.py
+drwxrwxr-x   0 jenkins    (989) jenkins    (987)        0 2023-02-09 10:00:27.821054 inmanta-core-8.2.0/src/inmanta/compiler/help/templates/
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)      235 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/compiler/help/templates/index_collision.j2
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     3604 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/compiler/help/templates/modified_after_freeze.j2
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)      733 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/compiler/help/templates/module_v2_in_v1_path.j2
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)    20658 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/config.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     9187 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/const.py
+drwxrwxr-x   0 jenkins    (989) jenkins    (987)        0 2023-02-09 10:00:27.821054 inmanta-core-8.2.0/src/inmanta/data/
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)   224939 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/data/__init__.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)    43652 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/data/dataview.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)    21756 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/data/model.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)    12205 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/data/schema.py
+drwxrwxr-x   0 jenkins    (989) jenkins    (987)        0 2023-02-09 10:00:27.822054 inmanta-core-8.2.0/src/inmanta/db/
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)      627 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/db/__init__.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     5462 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/db/util.py
+drwxrwxr-x   0 jenkins    (989) jenkins    (987)        0 2023-02-09 10:00:27.825054 inmanta-core-8.2.0/src/inmanta/db/versions/
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)      627 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/db/versions/__init__.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)    12131 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/db/versions/v1.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     1737 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/db/versions/v17.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     1393 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/db/versions/v2.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     2443 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/db/versions/v202105170.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)      915 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/db/versions/v202106080.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     1247 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/db/versions/v202106210.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     1826 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/db/versions/v202109100.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)      979 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/db/versions/v202111260.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     1581 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/db/versions/v202203140.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     2200 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/db/versions/v202203160.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)      910 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/db/versions/v202205250.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)      979 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/db/versions/v202206290.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)      948 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/db/versions/v202208180.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     1881 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/db/versions/v202208190.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)      976 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/db/versions/v202209090.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     3957 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/db/versions/v202209130.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)      861 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/db/versions/v202209160.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     2919 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/db/versions/v202211230.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     1430 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/db/versions/v202212010.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     1494 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/db/versions/v202301100.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)      924 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/db/versions/v202301110.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)      977 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/db/versions/v202301120.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)      929 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/db/versions/v202301160.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)      896 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/db/versions/v202301170.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     1313 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/db/versions/v202301190.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     1471 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/db/versions/v3.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     3556 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/db/versions/v4.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     1529 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/db/versions/v5.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     1043 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/db/versions/v6.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     1558 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/db/versions/v7.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)    16438 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/deploy.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     2694 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/docstring_parser.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)    56383 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/env.py
+drwxrwxr-x   0 jenkins    (989) jenkins    (987)        0 2023-02-09 10:00:27.826054 inmanta-core-8.2.0/src/inmanta/execute/
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)      627 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/execute/__init__.py
+drwxrwxr-x   0 jenkins    (989) jenkins    (987)        0 2023-02-09 10:00:27.826054 inmanta-core-8.2.0/src/inmanta/execute/dataflow/
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)    41029 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/execute/dataflow/__init__.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     9488 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/execute/dataflow/datatrace.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     7405 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/execute/dataflow/graphic.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     7152 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/execute/dataflow/root_cause.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     8478 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/execute/proxy.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)    46717 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/execute/runtime.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)    30085 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/execute/scheduler.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     1807 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/execute/tracking.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     1451 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/execute/util.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)    25455 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/export.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     5488 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/file_parser.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)    24386 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/loader.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)    35363 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/main.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     9146 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/model.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)   140687 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/module.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)    81102 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/moduletool.py
+drwxrwxr-x   0 jenkins    (989) jenkins    (987)        0 2023-02-09 10:00:27.827054 inmanta-core-8.2.0/src/inmanta/parser/
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     2934 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/parser/__init__.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     5591 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/parser/cache.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)   505683 2023-02-09 10:00:17.000000 inmanta-core-8.2.0/src/inmanta/parser/parser.out
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)    66421 2023-02-09 10:00:17.000000 inmanta-core-8.2.0/src/inmanta/parser/parsetab.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     1563 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/parser/pickle.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     7799 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/parser/plyInmantaLex.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)    36122 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/parser/plyInmantaParser.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)    21187 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/plugins.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     5509 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/postgresproc.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)      734 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/profile_mem.py
+drwxrwxr-x   0 jenkins    (989) jenkins    (987)        0 2023-02-09 10:00:27.828054 inmanta-core-8.2.0/src/inmanta/protocol/
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     3131 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/protocol/__init__.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)    40283 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/protocol/common.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     8549 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/protocol/decorators.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)    17519 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/protocol/endpoints.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     4455 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/protocol/exceptions.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)    32908 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/protocol/methods.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)    59046 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/protocol/methods_v2.py
+drwxrwxr-x   0 jenkins    (989) jenkins    (987)        0 2023-02-09 10:00:27.829054 inmanta-core-8.2.0/src/inmanta/protocol/openapi/
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)      627 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/protocol/openapi/__init__.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)    19132 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/protocol/openapi/converter.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     8343 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/protocol/openapi/model.py
+drwxrwxr-x   0 jenkins    (989) jenkins    (987)        0 2023-02-09 10:00:27.829054 inmanta-core-8.2.0/src/inmanta/protocol/rest/
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)    21717 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/protocol/rest/__init__.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     6064 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/protocol/rest/client.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)    13872 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/protocol/rest/server.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     2158 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/protocol/return_value_meta.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)        0 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/py.typed
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     6273 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/reporter.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)    23112 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/resources.py
+drwxrwxr-x   0 jenkins    (989) jenkins    (987)        0 2023-02-09 10:00:27.830054 inmanta-core-8.2.0/src/inmanta/server/
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     1338 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/server/__init__.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)    56391 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/server/agentmanager.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     9731 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/server/bootloader.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)      688 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/server/compilerservice.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)    10111 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/server/config.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     7314 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/server/diff.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     7672 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/server/extensions.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)    27495 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/server/protocol.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     7036 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/server/server.py
+drwxrwxr-x   0 jenkins    (989) jenkins    (987)        0 2023-02-09 10:00:27.832054 inmanta-core-8.2.0/src/inmanta/server/services/
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)      627 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/server/services/__init__.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     5702 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/server/services/codeservice.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)    38106 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/server/services/compilerservice.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     4850 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/server/services/databaseservice.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)    11640 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/server/services/dryrunservice.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)    25390 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/server/services/environment_metrics_service.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)    27831 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/server/services/environmentservice.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     6242 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/server/services/fileservice.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     4551 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/server/services/metricservice.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     7970 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/server/services/notificationservice.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)    48458 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/server/services/orchestrationservice.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)    13605 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/server/services/paramservice.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     6154 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/server/services/projectservice.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)    43300 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/server/services/resourceservice.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)    11714 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/server/validate_filter.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)      865 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/stable_api.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     2927 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/types.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)    24125 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/util.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     6487 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta/warnings.py
+drwxrwxr-x   0 jenkins    (989) jenkins    (987)        0 2023-02-09 10:00:27.833054 inmanta-core-8.2.0/src/inmanta_core.egg-info/
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     3182 2023-02-09 10:00:27.000000 inmanta-core-8.2.0/src/inmanta_core.egg-info/PKG-INFO
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     6618 2023-02-09 10:00:27.000000 inmanta-core-8.2.0/src/inmanta_core.egg-info/SOURCES.txt
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)        1 2023-02-09 10:00:27.000000 inmanta-core-8.2.0/src/inmanta_core.egg-info/dependency_links.txt
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)       76 2023-02-09 10:00:27.000000 inmanta-core-8.2.0/src/inmanta_core.egg-info/entry_points.txt
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)        1 2023-02-09 10:00:09.000000 inmanta-core-8.2.0/src/inmanta_core.egg-info/not-zip-safe
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)      577 2023-02-09 10:00:27.000000 inmanta-core-8.2.0/src/inmanta_core.egg-info/requires.txt
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)       36 2023-02-09 10:00:27.000000 inmanta-core-8.2.0/src/inmanta_core.egg-info/top_level.txt
+drwxrwxr-x   0 jenkins    (989) jenkins    (987)        0 2023-02-09 10:00:27.812053 inmanta-core-8.2.0/src/inmanta_ext/
+drwxrwxr-x   0 jenkins    (989) jenkins    (987)        0 2023-02-09 10:00:27.833054 inmanta-core-8.2.0/src/inmanta_ext/core/
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)      627 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta_ext/core/__init__.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     2163 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta_ext/core/extension.py
+drwxrwxr-x   0 jenkins    (989) jenkins    (987)        0 2023-02-09 10:00:27.812053 inmanta-core-8.2.0/src/inmanta_plugins/
+drwxrwxr-x   0 jenkins    (989) jenkins    (987)        0 2023-02-09 10:00:27.833054 inmanta-core-8.2.0/src/inmanta_plugins/1/
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)      627 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/src/inmanta_plugins/1/__init__.py
+drwxrwxr-x   0 jenkins    (989) jenkins    (987)        0 2023-02-09 10:00:27.838055 inmanta-core-8.2.0/tests/
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     7790 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/tests/test_2way_protocol.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     7692 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/tests/test_agent.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)    55229 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/tests/test_agent_manager.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)    16768 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/tests/test_app.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)    12682 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/tests/test_app_cli.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)    12792 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/tests/test_cache.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)    18793 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/tests/test_cli.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     4624 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/tests/test_compilation.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     4819 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/tests/test_compiler_entrypoints.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)    11567 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/tests/test_config.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     1301 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/tests/test_const.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)   116677 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/tests/test_data.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     8116 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/tests/test_data_concurrency.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     4378 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/tests/test_data_model.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     3912 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/tests/test_deploy.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     5151 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/tests/test_docs_snippets.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     3047 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/tests/test_docstring_parser.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)    27232 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/tests/test_env.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)    21255 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/tests/test_export.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     9103 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/tests/test_extension_loading.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     2789 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/tests/test_file_parser.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     6670 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/tests/test_handler.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     4111 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/tests/test_import_entry_points.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     5982 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/tests/test_influxdbreporting.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     8541 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/tests/test_io.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     5352 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/tests/test_jwt.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)    18512 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/tests/test_loader.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)    54161 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/tests/test_module_loader.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)    18976 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/tests/test_modules.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)    29095 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/tests/test_openapi.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)      988 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/tests/test_param.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)    62820 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/tests/test_parser.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     6299 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/tests/test_postgres.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     2110 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/tests/test_postgres_proc.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)    22771 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/tests/test_project.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     3346 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/tests/test_projectmetadata.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)    76126 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/tests/test_protocol.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     3038 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/tests/test_proxy.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)    11167 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/tests/test_resource.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)    53410 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/tests/test_server.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     3664 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/tests/test_type.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)    16966 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/tests/test_util.py
+-rw-rw-r--   0 jenkins    (989) jenkins    (987)     1924 2023-02-09 09:57:10.000000 inmanta-core-8.2.0/tox.ini
```

### Comparing `inmanta-core-8.1.0/LICENSE` & `inmanta-core-8.2.0/LICENSE`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/PKG-INFO` & `inmanta-core-8.2.0/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: inmanta-core
-Version: 8.1.0
+Version: 8.2.0
 Summary: Inmanta deployment tool
 Home-page: https://github.com/inmanta/inmanta-core
 Author: Inmanta
 Author-email: code@inmanta.com
 License: Apache Software License 2
 Project-URL: Bug Tracker, https://github.com/inmanta/inmanta-core/issues
 Project-URL: Documentation, https://docs.inmanta.com/community/latest/
```

### Comparing `inmanta-core-8.1.0/README.md` & `inmanta-core-8.2.0/README.md`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/misc/inmanta-workon-register.sh` & `inmanta-core-8.2.0/misc/inmanta-workon-register.sh`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/misc/inmanta.cfg` & `inmanta-core-8.2.0/misc/inmanta.cfg`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/misc/inmanta.lang` & `inmanta-core-8.2.0/misc/inmanta.lang`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/misc/inmanta.vim` & `inmanta-core-8.2.0/misc/inmanta.vim`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/pyproject.toml` & `inmanta-core-8.2.0/pyproject.toml`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/setup.cfg` & `inmanta-core-8.2.0/setup.cfg`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/setup.py` & `inmanta-core-8.2.0/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -39,15 +39,15 @@
 
 
 # read the contents of your README file
 this_directory = path.abspath(path.dirname(__file__))
 with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
     long_description = f.read()
 
-version = "8.1.0"
+version = "8.2.0"
 
 setup(
     version=version,
     python_requires=">=3.9",  # also update classifiers
     # Meta data
     name="inmanta-core",
     description="Inmanta deployment tool",
```

### Comparing `inmanta-core-8.1.0/src/inmanta/__init__.py` & `inmanta-core-8.2.0/src/inmanta/__init__.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/agent/__init__.py` & `inmanta-core-8.2.0/src/inmanta/agent/__init__.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/agent/agent.py` & `inmanta-core-8.2.0/src/inmanta/agent/agent.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/agent/cache.py` & `inmanta-core-8.2.0/src/inmanta/agent/cache.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/agent/config.py` & `inmanta-core-8.2.0/src/inmanta/agent/config.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/agent/handler.py` & `inmanta-core-8.2.0/src/inmanta/agent/handler.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/agent/io/__init__.py` & `inmanta-core-8.2.0/src/inmanta/agent/io/__init__.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/agent/io/local.py` & `inmanta-core-8.2.0/src/inmanta/agent/io/local.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/agent/io/remote.py` & `inmanta-core-8.2.0/src/inmanta/agent/io/remote.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/agent/reporting.py` & `inmanta-core-8.2.0/src/inmanta/agent/reporting.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/app.py` & `inmanta-core-8.2.0/src/inmanta/app.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/ast/__init__.py` & `inmanta-core-8.2.0/src/inmanta/ast/__init__.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/ast/attribute.py` & `inmanta-core-8.2.0/src/inmanta/ast/attribute.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/ast/blocks.py` & `inmanta-core-8.2.0/src/inmanta/ast/blocks.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/ast/constraint/__init__.py` & `inmanta-core-8.2.0/src/inmanta/ast/constraint/__init__.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/ast/constraint/expression.py` & `inmanta-core-8.2.0/src/inmanta/ast/constraint/expression.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/ast/entity.py` & `inmanta-core-8.2.0/src/inmanta/ast/entity.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/ast/export.py` & `inmanta-core-8.2.0/src/inmanta/ast/export.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/ast/statements/__init__.py` & `inmanta-core-8.2.0/src/inmanta/ast/statements/__init__.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/ast/statements/assign.py` & `inmanta-core-8.2.0/src/inmanta/ast/statements/assign.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/ast/statements/call.py` & `inmanta-core-8.2.0/src/inmanta/ast/statements/call.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/ast/statements/define.py` & `inmanta-core-8.2.0/src/inmanta/ast/statements/define.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/ast/statements/generator.py` & `inmanta-core-8.2.0/src/inmanta/ast/statements/generator.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/ast/type.py` & `inmanta-core-8.2.0/src/inmanta/ast/type.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/ast/variables.py` & `inmanta-core-8.2.0/src/inmanta/ast/variables.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/command.py` & `inmanta-core-8.2.0/src/inmanta/command.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/compiler/__init__.py` & `inmanta-core-8.2.0/src/inmanta/compiler/__init__.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/compiler/config.py` & `inmanta-core-8.2.0/src/inmanta/compiler/config.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/compiler/data.py` & `inmanta-core-8.2.0/src/inmanta/compiler/data.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/compiler/help/__init__.py` & `inmanta-core-8.2.0/src/inmanta/compiler/help/__init__.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/compiler/help/explainer.py` & `inmanta-core-8.2.0/src/inmanta/compiler/help/explainer.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/compiler/help/templates/modified_after_freeze.j2` & `inmanta-core-8.2.0/src/inmanta/compiler/help/templates/modified_after_freeze.j2`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/compiler/help/templates/module_v2_in_v1_path.j2` & `inmanta-core-8.2.0/src/inmanta/compiler/help/templates/module_v2_in_v1_path.j2`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/config.py` & `inmanta-core-8.2.0/src/inmanta/config.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/const.py` & `inmanta-core-8.2.0/src/inmanta/const.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/data/__init__.py` & `inmanta-core-8.2.0/src/inmanta/data/__init__.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/data/dataview.py` & `inmanta-core-8.2.0/src/inmanta/data/dataview.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/data/model.py` & `inmanta-core-8.2.0/src/inmanta/data/model.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/data/schema.py` & `inmanta-core-8.2.0/src/inmanta/data/schema.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/db/__init__.py` & `inmanta-core-8.2.0/src/inmanta/db/__init__.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/db/util.py` & `inmanta-core-8.2.0/src/inmanta/db/util.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/db/versions/__init__.py` & `inmanta-core-8.2.0/src/inmanta/db/versions/__init__.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/db/versions/v1.py` & `inmanta-core-8.2.0/src/inmanta/db/versions/v1.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/db/versions/v17.py` & `inmanta-core-8.2.0/src/inmanta/db/versions/v17.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/db/versions/v2.py` & `inmanta-core-8.2.0/src/inmanta/db/versions/v2.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/db/versions/v202105170.py` & `inmanta-core-8.2.0/src/inmanta/db/versions/v202105170.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/db/versions/v202106080.py` & `inmanta-core-8.2.0/src/inmanta/db/versions/v202106080.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/db/versions/v202106210.py` & `inmanta-core-8.2.0/src/inmanta/db/versions/v202106210.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/db/versions/v202109100.py` & `inmanta-core-8.2.0/src/inmanta/db/versions/v202109100.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/db/versions/v202111260.py` & `inmanta-core-8.2.0/src/inmanta/db/versions/v202111260.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/db/versions/v202203140.py` & `inmanta-core-8.2.0/src/inmanta/db/versions/v202203140.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/db/versions/v202203160.py` & `inmanta-core-8.2.0/src/inmanta/db/versions/v202203160.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/db/versions/v202205250.py` & `inmanta-core-8.2.0/src/inmanta/db/versions/v202205250.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/db/versions/v202206290.py` & `inmanta-core-8.2.0/src/inmanta/db/versions/v202206290.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/db/versions/v202208180.py` & `inmanta-core-8.2.0/src/inmanta/db/versions/v202208180.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/db/versions/v202208190.py` & `inmanta-core-8.2.0/src/inmanta/db/versions/v202208190.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/db/versions/v202209090.py` & `inmanta-core-8.2.0/src/inmanta/db/versions/v202209090.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/db/versions/v202209130.py` & `inmanta-core-8.2.0/src/inmanta/db/versions/v202209130.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/db/versions/v202209160.py` & `inmanta-core-8.2.0/src/inmanta/db/versions/v202209160.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/db/versions/v202211230.py` & `inmanta-core-8.2.0/src/inmanta/db/versions/v202211230.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/db/versions/v202212010.py` & `inmanta-core-8.2.0/src/inmanta/db/versions/v202212010.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/db/versions/v202301100.py` & `inmanta-core-8.2.0/src/inmanta/db/versions/v202301100.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/db/versions/v202301110.py` & `inmanta-core-8.2.0/src/inmanta/db/versions/v202301110.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/db/versions/v202301120.py` & `inmanta-core-8.2.0/src/inmanta/db/versions/v202301120.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/db/versions/v202301160.py` & `inmanta-core-8.2.0/src/inmanta/db/versions/v202301160.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/db/versions/v202301170.py` & `inmanta-core-8.2.0/src/inmanta/db/versions/v202301170.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/db/versions/v202301190.py` & `inmanta-core-8.2.0/src/inmanta/db/versions/v202301190.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/db/versions/v3.py` & `inmanta-core-8.2.0/src/inmanta/db/versions/v3.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/db/versions/v4.py` & `inmanta-core-8.2.0/src/inmanta/db/versions/v4.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/db/versions/v5.py` & `inmanta-core-8.2.0/src/inmanta/db/versions/v5.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/db/versions/v6.py` & `inmanta-core-8.2.0/src/inmanta/db/versions/v6.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/db/versions/v7.py` & `inmanta-core-8.2.0/src/inmanta/db/versions/v7.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/deploy.py` & `inmanta-core-8.2.0/src/inmanta/deploy.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/docstring_parser.py` & `inmanta-core-8.2.0/src/inmanta/docstring_parser.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/env.py` & `inmanta-core-8.2.0/src/inmanta/env.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/execute/__init__.py` & `inmanta-core-8.2.0/src/inmanta/execute/__init__.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/execute/dataflow/__init__.py` & `inmanta-core-8.2.0/src/inmanta/execute/dataflow/__init__.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/execute/dataflow/datatrace.py` & `inmanta-core-8.2.0/src/inmanta/execute/dataflow/datatrace.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/execute/dataflow/graphic.py` & `inmanta-core-8.2.0/src/inmanta/execute/dataflow/graphic.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/execute/dataflow/root_cause.py` & `inmanta-core-8.2.0/src/inmanta/execute/dataflow/root_cause.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/execute/proxy.py` & `inmanta-core-8.2.0/src/inmanta/execute/proxy.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/execute/runtime.py` & `inmanta-core-8.2.0/src/inmanta/execute/runtime.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/execute/scheduler.py` & `inmanta-core-8.2.0/src/inmanta/execute/scheduler.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/execute/tracking.py` & `inmanta-core-8.2.0/src/inmanta/execute/tracking.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/execute/util.py` & `inmanta-core-8.2.0/src/inmanta/execute/util.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/export.py` & `inmanta-core-8.2.0/src/inmanta/export.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/file_parser.py` & `inmanta-core-8.2.0/src/inmanta/file_parser.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/loader.py` & `inmanta-core-8.2.0/src/inmanta/loader.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/main.py` & `inmanta-core-8.2.0/src/inmanta/main.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/model.py` & `inmanta-core-8.2.0/src/inmanta/model.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/module.py` & `inmanta-core-8.2.0/src/inmanta/module.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/moduletool.py` & `inmanta-core-8.2.0/src/inmanta/moduletool.py`

 * *Files 1% similar despite different names*

```diff
@@ -696,35 +696,35 @@
             help="Create a development version. The new version number will have the .dev0 build tag.",
             action="store_true",
             default=False,
         )
         release.add_argument(
             "--major",
             dest="major",
-            help="Do a major version bump compared to the previous stable release. Ignored when --dev is not set.",
+            help="Do a major version bump compared to the previous stable release.",
             action="store_true",
         )
         release.add_argument(
             "--minor",
             dest="minor",
-            help="Do a minor version bump compared to the previous stable release. Ignored when --dev is not set.",
+            help="Do a minor version bump compared to the previous stable release.",
             action="store_true",
         )
         release.add_argument(
             "--patch",
             dest="patch",
-            help="Do a patch version bump compared to the previous stable release. Ignored when --dev is not set.",
+            help="Do a patch version bump compared to the previous stable release.",
             action="store_true",
         )
         release.add_argument("-m", "--message", help="Commit message")
         release.add_argument(
             "-c",
             "--changelog-message",
             help="This changelog message will be written to the changelog file. If the -m option is not provided, "
-            "this message will also be used as the commit message. This option is ignored when --dev is not provided.",
+            "this message will also be used as the commit message.",
         )
 
     def add(self, module_req: str, v1: bool = False, v2: bool = False, override: bool = False) -> None:
         """
         Add a module dependency to an Inmanta module or project.
 
         :param module_req: The module to add, optionally with a version constraint.
@@ -1175,84 +1175,98 @@
         self,
         dev: bool,
         message: Optional[str] = None,
         patch: bool = False,
         minor: bool = False,
         major: bool = False,
         changelog_message: Optional[str] = None,
-        add_new_version_to_changelog: bool = False,
     ) -> None:
         """
         Execute the release command.
-
-        :param add_new_version_to_changelog: Indicate that the new version has to be added to the changelog instead of
-                                             bumping the current version. This is used by the recursive call to prevent
-                                             bumping the latest stable release.
         """
+
+        # Validate patch, minor, major
         nb_version_bump_arguments_set = sum([patch, minor, major])
         if nb_version_bump_arguments_set > 1:
             raise click.UsageError("Only one of --patch, --minor and --major can be set at the same time.")
+
+        # Make module
         module_dir = os.path.abspath(os.getcwd())
         module: Module[ModuleMetadata] = self.construct_module(project=DummyProject(), path=module_dir)
         if not gitprovider.is_git_repository(repo=module_dir):
             raise click.ClickException(f"Directory {module_dir} is not a git repository.")
+
+        # Validate current state of the module
         current_version: Version = module.version
         if current_version.epoch != 0:
             raise click.ClickException("Version with an epoch value larger than zero are not supported by this tool.")
         gitprovider.fetch(module_dir)
+
+        # Get history
         stable_releases: list[Version] = gitprovider.get_version_tags(module_dir, only_return_stable_versions=True)
+
         path_changelog_file = os.path.join(module_dir, const.MODULE_CHANGELOG_FILE)
         changelog: Optional[ModuleChangelog] = (
             ModuleChangelog(path_changelog_file) if os.path.exists(path_changelog_file) else None
         )
-        if dev:
-            requested_version_bump: Optional[ChangeType] = ChangeType.parse_from_bools(patch, minor, major)
+
+        requested_version_bump: Optional[ChangeType] = ChangeType.parse_from_bools(patch, minor, major)
+        if not requested_version_bump and dev:
+            # Dev always bumps
+            requested_version_bump = ChangeType.PATCH
+
+        if requested_version_bump:
             new_version: Version = self._get_dev_version_with_minimal_distance_to_previous_stable_release(
-                current_version, stable_releases, requested_version_bump if requested_version_bump else ChangeType.PATCH
+                current_version, stable_releases, requested_version_bump
             )
+        else:
+            # Never happens for dev release
+            new_version = current_version
+
+        if not changelog and changelog_message:
+            changelog = ModuleChangelog.create_changelog_file(path_changelog_file, new_version, changelog_message)
+        elif changelog:
+            if current_version.is_devrelease:
+                # Update the existing dev version to the new dev version
+                changelog.rewrite_version_in_changelog_header(old_version=current_version, new_version=new_version)
+            else:
+                changelog.add_section_for_version(current_version, new_version)
+
+            if changelog_message:
+                changelog.add_changelog_entry(current_version, new_version, changelog_message)
+
+        if dev:
             assert new_version.dev is not None and new_version.dev == 0
             new_base_version_str, version_tag = str(new_version).rsplit(".", maxsplit=1)
             module.rewrite_version(new_version=new_base_version_str, version_tag=version_tag)
-            if not changelog and changelog_message:
-                changelog = ModuleChangelog.create_changelog_file(path_changelog_file, new_version, changelog_message)
-            elif changelog:
-                if add_new_version_to_changelog:
-                    changelog.add_section_for_version(current_version, new_version)
-                else:
-                    changelog.rewrite_version_in_changelog_header(old_version=current_version, new_version=new_version)
-                if changelog_message:
-                    changelog.add_changelog_entry(current_version, new_version, changelog_message)
+            # If no changes, commit will not happen
             gitprovider.commit(
                 repo=module_dir,
                 message=changelog_message if changelog_message else message if message else f"Bump version to {new_version}",
                 commit_all=True,
                 add=[module.get_metadata_file_path()] + [changelog.get_path()] if changelog else [],
                 raise_exc_when_nothing_to_commit=False,
             )
         else:
-            if nb_version_bump_arguments_set > 0:
-                LOGGER.warning("Performing a stable release. The --patch, --minor and --major arguments will be ignored.")
-            release_tag: Version = VersionOperation.set_version_tag(current_version, version_tag="")
+            release_tag: Version = VersionOperation.set_version_tag(new_version, version_tag="")
             if release_tag in stable_releases:
                 raise click.ClickException(f"A Git version tag already exists for version {release_tag}")
             module.rewrite_version(new_version=str(release_tag), version_tag="")
             if changelog:
                 changelog.set_release_date_for_version(release_tag)
             gitprovider.commit(
                 repo=module_dir,
                 message=message if message else f"Release version {module.metadata.get_full_version()}",
                 commit_all=True,
                 add=[module.get_metadata_file_path()] + [changelog.get_path()] if changelog else [],
                 raise_exc_when_nothing_to_commit=False,
             )
             gitprovider.tag(repo=module_dir, tag=str(release_tag))
             # bump to the next dev version
-            self.release(
-                dev=True, message="Bump version to next development version", patch=True, add_new_version_to_changelog=True
-            )
+            self.release(dev=True, message="Bump version to next development version", patch=True)
 
 
 class ModuleChangelog:
     """
     This class represent the changelog file in an Inmanta module.
 
     The expected format of the changelog is the following:
@@ -1309,23 +1323,24 @@
     @classmethod
     def _get_top_level_header(cls) -> str:
         """
         Return the top-level header of the changelog file.
         """
         return "# Changelog"
 
+    def regex_for_changelog_line(self, version: Version) -> re.Pattern[str]:
+        return re.compile(rf"(^#{{1,2}} [vV]?{re.escape(version.base_version)}[^\n]*$)", re.MULTILINE)
+
     def _add_changelog_section(self, content_changelog: str, old_version: Version, new_version: Version) -> str:
         """
         Add a new section for the given new_version to the changelog, given the current content of the changelog file.
         """
         header_for_new_version: str = self._get_header_for_version(new_version)
         # Try to insert the section before the section of the previous version if such a section exists
-        regex_header_previous_version: re.Pattern[str] = re.compile(
-            rf"(^{re.escape(f'## v{old_version.base_version}')}[^\n]*$)", re.MULTILINE
-        )
+        regex_header_previous_version: re.Pattern[str] = self.regex_for_changelog_line(old_version)
         new_content_changelog = regex_header_previous_version.sub(
             repl=f"{header_for_new_version}\n\n\n\\g<1>",
             string=content_changelog,
             count=1,
         )
         if new_content_changelog != content_changelog:
             return new_content_changelog
@@ -1355,15 +1370,15 @@
             fh.truncate()
 
     def _has_section_for_version(self, version: Version) -> bool:
         """
         Return True iff this changelog contains a section of the given version.
         """
         with open(self.path_changelog_file, "r", encoding="utf-8") as fh:
-            regex_version_header: re.Pattern[str] = re.compile(rf"^{re.escape(f'## v{version.base_version} - ')}", re.MULTILINE)
+            regex_version_header: re.Pattern[str] = self.regex_for_changelog_line(version)
             content = fh.read()
             return regex_version_header.search(content) is not None
 
     def rewrite_version_in_changelog_header(self, old_version: Version, new_version: Version) -> None:
         """
         Replaces the first occurrence of the given old_version in this changelog file with new_version.
         This operation is performed in-place.
```

### Comparing `inmanta-core-8.1.0/src/inmanta/parser/__init__.py` & `inmanta-core-8.2.0/src/inmanta/parser/__init__.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/parser/cache.py` & `inmanta-core-8.2.0/src/inmanta/parser/cache.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/parser/parser.out` & `inmanta-core-8.2.0/src/inmanta/parser/parser.out`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/parser/parsetab.py` & `inmanta-core-8.2.0/src/inmanta/parser/parsetab.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/parser/pickle.py` & `inmanta-core-8.2.0/src/inmanta/parser/pickle.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/parser/plyInmantaLex.py` & `inmanta-core-8.2.0/src/inmanta/parser/plyInmantaLex.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/parser/plyInmantaParser.py` & `inmanta-core-8.2.0/src/inmanta/parser/plyInmantaParser.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/plugins.py` & `inmanta-core-8.2.0/src/inmanta/plugins.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/postgresproc.py` & `inmanta-core-8.2.0/src/inmanta/postgresproc.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/profile_mem.py` & `inmanta-core-8.2.0/src/inmanta/profile_mem.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/protocol/__init__.py` & `inmanta-core-8.2.0/src/inmanta/protocol/__init__.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/protocol/common.py` & `inmanta-core-8.2.0/src/inmanta/protocol/common.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/protocol/decorators.py` & `inmanta-core-8.2.0/src/inmanta/protocol/decorators.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/protocol/endpoints.py` & `inmanta-core-8.2.0/src/inmanta/protocol/endpoints.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/protocol/exceptions.py` & `inmanta-core-8.2.0/src/inmanta/protocol/exceptions.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/protocol/methods.py` & `inmanta-core-8.2.0/src/inmanta/protocol/methods.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/protocol/methods_v2.py` & `inmanta-core-8.2.0/src/inmanta/protocol/methods_v2.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/protocol/openapi/__init__.py` & `inmanta-core-8.2.0/src/inmanta/protocol/openapi/__init__.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/protocol/openapi/converter.py` & `inmanta-core-8.2.0/src/inmanta/protocol/openapi/converter.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/protocol/openapi/model.py` & `inmanta-core-8.2.0/src/inmanta/protocol/openapi/model.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/protocol/rest/__init__.py` & `inmanta-core-8.2.0/src/inmanta/protocol/rest/__init__.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/protocol/rest/client.py` & `inmanta-core-8.2.0/src/inmanta/protocol/rest/client.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/protocol/rest/server.py` & `inmanta-core-8.2.0/src/inmanta/protocol/rest/server.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/protocol/return_value_meta.py` & `inmanta-core-8.2.0/src/inmanta/protocol/return_value_meta.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/reporter.py` & `inmanta-core-8.2.0/src/inmanta/reporter.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/resources.py` & `inmanta-core-8.2.0/src/inmanta/resources.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/server/__init__.py` & `inmanta-core-8.2.0/src/inmanta/server/__init__.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/server/agentmanager.py` & `inmanta-core-8.2.0/src/inmanta/server/agentmanager.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/server/bootloader.py` & `inmanta-core-8.2.0/src/inmanta/server/bootloader.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/server/compilerservice.py` & `inmanta-core-8.2.0/src/inmanta/server/compilerservice.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/server/config.py` & `inmanta-core-8.2.0/src/inmanta/server/config.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/server/diff.py` & `inmanta-core-8.2.0/src/inmanta/server/diff.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/server/extensions.py` & `inmanta-core-8.2.0/src/inmanta/server/extensions.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/server/protocol.py` & `inmanta-core-8.2.0/src/inmanta/server/protocol.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/server/server.py` & `inmanta-core-8.2.0/src/inmanta/server/server.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/server/services/__init__.py` & `inmanta-core-8.2.0/src/inmanta/server/services/__init__.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/server/services/codeservice.py` & `inmanta-core-8.2.0/src/inmanta/server/services/codeservice.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/server/services/compilerservice.py` & `inmanta-core-8.2.0/src/inmanta/server/services/compilerservice.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/server/services/databaseservice.py` & `inmanta-core-8.2.0/src/inmanta/server/services/databaseservice.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/server/services/dryrunservice.py` & `inmanta-core-8.2.0/src/inmanta/server/services/dryrunservice.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/server/services/environment_metrics_service.py` & `inmanta-core-8.2.0/src/inmanta/server/services/environment_metrics_service.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/server/services/environmentservice.py` & `inmanta-core-8.2.0/src/inmanta/server/services/environmentservice.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/server/services/fileservice.py` & `inmanta-core-8.2.0/src/inmanta/server/services/fileservice.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/server/services/metricservice.py` & `inmanta-core-8.2.0/src/inmanta/server/services/metricservice.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/server/services/notificationservice.py` & `inmanta-core-8.2.0/src/inmanta/server/services/notificationservice.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/server/services/orchestrationservice.py` & `inmanta-core-8.2.0/src/inmanta/server/services/orchestrationservice.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/server/services/paramservice.py` & `inmanta-core-8.2.0/src/inmanta/server/services/paramservice.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/server/services/projectservice.py` & `inmanta-core-8.2.0/src/inmanta/server/services/projectservice.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/server/services/resourceservice.py` & `inmanta-core-8.2.0/src/inmanta/server/services/resourceservice.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/server/validate_filter.py` & `inmanta-core-8.2.0/src/inmanta/server/validate_filter.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/stable_api.py` & `inmanta-core-8.2.0/src/inmanta/stable_api.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/types.py` & `inmanta-core-8.2.0/src/inmanta/types.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/util.py` & `inmanta-core-8.2.0/src/inmanta/util.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta/warnings.py` & `inmanta-core-8.2.0/src/inmanta/warnings.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta_core.egg-info/PKG-INFO` & `inmanta-core-8.2.0/src/inmanta_core.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: inmanta-core
-Version: 8.1.0
+Version: 8.2.0
 Summary: Inmanta deployment tool
 Home-page: https://github.com/inmanta/inmanta-core
 Author: Inmanta
 Author-email: code@inmanta.com
 License: Apache Software License 2
 Project-URL: Bug Tracker, https://github.com/inmanta/inmanta-core/issues
 Project-URL: Documentation, https://docs.inmanta.com/community/latest/
```

### Comparing `inmanta-core-8.1.0/src/inmanta_core.egg-info/requires.txt` & `inmanta-core-8.2.0/src/inmanta_core.egg-info/requires.txt`

 * *Files 23% similar despite different names*

```diff
@@ -30,8 +30,8 @@
 [datatrace]
 graphviz
 
 [debug]
 rpdb
 
 [pytest-inmanta-extensions]
-pytest-inmanta-extensions~=8.1.0.0.dev
+pytest-inmanta-extensions~=8.2.0.0.dev
```

### Comparing `inmanta-core-8.1.0/src/inmanta_ext/core/__init__.py` & `inmanta-core-8.2.0/src/inmanta_ext/core/__init__.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta_ext/core/extension.py` & `inmanta-core-8.2.0/src/inmanta_ext/core/extension.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/src/inmanta_plugins/1/__init__.py` & `inmanta-core-8.2.0/src/inmanta_plugins/1/__init__.py`

 * *Files identical despite different names*

### Comparing `inmanta-core-8.1.0/tox.ini` & `inmanta-core-8.2.0/tox.ini`

 * *Files identical despite different names*

