# Comparing `tmp/quantrocket-client-2.9.0.0.tar.gz` & `tmp/quantrocket-client-2.9.0.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "quantrocket-client-2.9.0.0.tar", last modified: Tue Apr  4 15:00:24 2023, max compression
+gzip compressed data, was "quantrocket-client-2.9.0.1.tar", last modified: Thu Apr  6 19:26:25 2023, max compression
```

## Comparing `quantrocket-client-2.9.0.0.tar` & `quantrocket-client-2.9.0.1.tar`

### file list

```diff
@@ -1,81 +1,81 @@
-drwxrwxrwx   0 root         (0) root         (0)        0 2023-04-04 15:00:24.565415 quantrocket-client-2.9.0.0/
--rw-rw-rw-   0 root         (0) root         (0)     9144 2023-04-04 14:59:51.000000 quantrocket-client-2.9.0.0/LICENSE.txt
--rw-rw-rw-   0 root         (0) root         (0)       54 2023-04-04 14:59:51.000000 quantrocket-client-2.9.0.0/MANIFEST.in
--rw-rw-rw-   0 root         (0) root         (0)      291 2023-04-04 15:00:24.565415 quantrocket-client-2.9.0.0/PKG-INFO
--rw-rw-rw-   0 root         (0) root         (0)      354 2023-04-04 14:59:51.000000 quantrocket-client-2.9.0.0/README.md
-drwxrwxrwx   0 root         (0) root         (0)        0 2023-04-04 15:00:24.565415 quantrocket-client-2.9.0.0/quantrocket/
--rw-rw-rw-   0 root         (0) root         (0)     3106 2023-04-04 14:59:51.000000 quantrocket-client-2.9.0.0/quantrocket/__init__.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2023-04-04 15:00:24.557415 quantrocket-client-2.9.0.0/quantrocket/_cli/
--rw-rw-rw-   0 root         (0) root         (0)        0 2023-04-04 14:59:51.000000 quantrocket-client-2.9.0.0/quantrocket/_cli/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     3792 2023-04-04 14:59:51.000000 quantrocket-client-2.9.0.0/quantrocket/_cli/commands.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2023-04-04 15:00:24.561415 quantrocket-client-2.9.0.0/quantrocket/_cli/subcommands/
--rw-rw-rw-   0 root         (0) root         (0)        0 2023-04-04 14:59:51.000000 quantrocket-client-2.9.0.0/quantrocket/_cli/subcommands/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     8604 2023-04-04 14:59:51.000000 quantrocket-client-2.9.0.0/quantrocket/_cli/subcommands/account.py
--rw-rw-rw-   0 root         (0) root         (0)    20169 2023-04-04 14:59:51.000000 quantrocket-client-2.9.0.0/quantrocket/_cli/subcommands/blotter.py
--rw-rw-rw-   0 root         (0) root         (0)     3106 2023-04-04 14:59:51.000000 quantrocket-client-2.9.0.0/quantrocket/_cli/subcommands/codeload.py
--rw-rw-rw-   0 root         (0) root         (0)     3231 2023-04-04 14:59:51.000000 quantrocket-client-2.9.0.0/quantrocket/_cli/subcommands/countdown.py
--rw-rw-rw-   0 root         (0) root         (0)     6800 2023-04-04 14:59:51.000000 quantrocket-client-2.9.0.0/quantrocket/_cli/subcommands/db.py
--rw-rw-rw-   0 root         (0) root         (0)     8308 2023-04-04 14:59:51.000000 quantrocket-client-2.9.0.0/quantrocket/_cli/subcommands/flightlog.py
--rw-rw-rw-   0 root         (0) root         (0)    42083 2023-04-04 14:59:51.000000 quantrocket-client-2.9.0.0/quantrocket/_cli/subcommands/fundamental.py
--rw-rw-rw-   0 root         (0) root         (0)    21184 2023-04-04 14:59:51.000000 quantrocket-client-2.9.0.0/quantrocket/_cli/subcommands/history.py
--rw-rw-rw-   0 root         (0) root         (0)     1253 2023-04-04 14:59:51.000000 quantrocket-client-2.9.0.0/quantrocket/_cli/subcommands/houston.py
--rw-rw-rw-   0 root         (0) root         (0)     6954 2023-04-04 14:59:51.000000 quantrocket-client-2.9.0.0/quantrocket/_cli/subcommands/ibg.py
--rw-rw-rw-   0 root         (0) root         (0)     5744 2023-04-04 14:59:51.000000 quantrocket-client-2.9.0.0/quantrocket/_cli/subcommands/license.py
--rw-rw-rw-   0 root         (0) root         (0)    38518 2023-04-04 14:59:51.000000 quantrocket-client-2.9.0.0/quantrocket/_cli/subcommands/master.py
--rw-rw-rw-   0 root         (0) root         (0)    18833 2023-04-04 14:59:51.000000 quantrocket-client-2.9.0.0/quantrocket/_cli/subcommands/moonshot.py
--rw-rw-rw-   0 root         (0) root         (0)    21551 2023-04-04 14:59:51.000000 quantrocket-client-2.9.0.0/quantrocket/_cli/subcommands/realtime.py
--rw-rw-rw-   0 root         (0) root         (0)     2896 2023-04-04 14:59:51.000000 quantrocket-client-2.9.0.0/quantrocket/_cli/subcommands/satellite.py
--rw-rw-rw-   0 root         (0) root         (0)     1583 2023-04-04 14:59:51.000000 quantrocket-client-2.9.0.0/quantrocket/_cli/subcommands/version.py
--rw-rw-rw-   0 root         (0) root         (0)    26399 2023-04-04 14:59:51.000000 quantrocket-client-2.9.0.0/quantrocket/_cli/subcommands/zipline.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2023-04-04 15:00:24.561415 quantrocket-client-2.9.0.0/quantrocket/_cli/utils/
--rw-rw-rw-   0 root         (0) root         (0)        0 2023-04-04 14:59:51.000000 quantrocket-client-2.9.0.0/quantrocket/_cli/utils/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     1561 2023-04-04 14:59:51.000000 quantrocket-client-2.9.0.0/quantrocket/_cli/utils/files.py
--rw-rw-rw-   0 root         (0) root         (0)     1963 2023-04-04 14:59:51.000000 quantrocket-client-2.9.0.0/quantrocket/_cli/utils/output.py
--rw-rw-rw-   0 root         (0) root         (0)     2371 2023-04-04 14:59:51.000000 quantrocket-client-2.9.0.0/quantrocket/_cli/utils/parse.py
--rw-rw-rw-   0 root         (0) root         (0)      844 2023-04-04 14:59:51.000000 quantrocket-client-2.9.0.0/quantrocket/_cli/utils/stream.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2023-04-04 15:00:24.561415 quantrocket-client-2.9.0.0/quantrocket/_tests/
--rw-rw-rw-   0 root         (0) root         (0)        0 2023-04-04 14:59:51.000000 quantrocket-client-2.9.0.0/quantrocket/_tests/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    29437 2023-04-04 14:59:51.000000 quantrocket-client-2.9.0.0/quantrocket/_tests/test_blotter.py
--rw-rw-rw-   0 root         (0) root         (0)   184790 2023-04-04 14:59:51.000000 quantrocket-client-2.9.0.0/quantrocket/_tests/test_fundamental.py
--rw-rw-rw-   0 root         (0) root         (0)    62221 2023-04-04 14:59:51.000000 quantrocket-client-2.9.0.0/quantrocket/_tests/test_master.py
--rw-rw-rw-   0 root         (0) root         (0)    17235 2023-04-04 14:59:51.000000 quantrocket-client-2.9.0.0/quantrocket/_tests/test_moonshot.py
--rw-rw-rw-   0 root         (0) root         (0)   152902 2023-04-04 14:59:51.000000 quantrocket-client-2.9.0.0/quantrocket/_tests/test_price.py
--rw-rw-rw-   0 root         (0) root         (0)     2562 2023-04-04 14:59:51.000000 quantrocket-client-2.9.0.0/quantrocket/_tests/test_utils.py
--rw-rw-rw-   0 root         (0) root         (0)      499 2023-04-04 15:00:24.565415 quantrocket-client-2.9.0.0/quantrocket/_version.py
--rw-rw-rw-   0 root         (0) root         (0)    10293 2023-04-04 14:59:51.000000 quantrocket-client-2.9.0.0/quantrocket/account.py
--rw-rw-rw-   0 root         (0) root         (0)    27865 2023-04-04 14:59:51.000000 quantrocket-client-2.9.0.0/quantrocket/blotter.py
--rw-rw-rw-   0 root         (0) root         (0)     3159 2023-04-04 14:59:51.000000 quantrocket-client-2.9.0.0/quantrocket/codeload.py
--rw-rw-rw-   0 root         (0) root         (0)     4027 2023-04-04 14:59:51.000000 quantrocket-client-2.9.0.0/quantrocket/countdown.py
--rw-rw-rw-   0 root         (0) root         (0)    14945 2023-04-04 14:59:51.000000 quantrocket-client-2.9.0.0/quantrocket/db.py
--rw-rw-rw-   0 root         (0) root         (0)     1309 2023-04-04 14:59:51.000000 quantrocket-client-2.9.0.0/quantrocket/exceptions.py
--rw-rw-rw-   0 root         (0) root         (0)    14874 2023-04-04 14:59:51.000000 quantrocket-client-2.9.0.0/quantrocket/flightlog.py
--rw-rw-rw-   0 root         (0) root         (0)   121781 2023-04-04 14:59:51.000000 quantrocket-client-2.9.0.0/quantrocket/fundamental.py
--rw-rw-rw-   0 root         (0) root         (0)    24358 2023-04-04 14:59:51.000000 quantrocket-client-2.9.0.0/quantrocket/history.py
--rw-rw-rw-   0 root         (0) root         (0)     7439 2023-04-04 14:59:51.000000 quantrocket-client-2.9.0.0/quantrocket/houston.py
--rw-rw-rw-   0 root         (0) root         (0)     8222 2023-04-04 14:59:51.000000 quantrocket-client-2.9.0.0/quantrocket/ibg.py
--rw-rw-rw-   0 root         (0) root         (0)     7632 2023-04-04 14:59:51.000000 quantrocket-client-2.9.0.0/quantrocket/license.py
--rw-rw-rw-   0 root         (0) root         (0)    54435 2023-04-04 14:59:51.000000 quantrocket-client-2.9.0.0/quantrocket/master.py
--rw-rw-rw-   0 root         (0) root         (0)    25014 2023-04-04 14:59:51.000000 quantrocket-client-2.9.0.0/quantrocket/moonshot.py
--rw-rw-rw-   0 root         (0) root         (0)    31387 2023-04-04 14:59:51.000000 quantrocket-client-2.9.0.0/quantrocket/price.py
--rw-rw-rw-   0 root         (0) root         (0)        0 2023-04-04 14:59:51.000000 quantrocket-client-2.9.0.0/quantrocket/py.typed
--rw-rw-rw-   0 root         (0) root         (0)    26122 2023-04-04 14:59:51.000000 quantrocket-client-2.9.0.0/quantrocket/realtime.py
--rw-rw-rw-   0 root         (0) root         (0)     4596 2023-04-04 14:59:51.000000 quantrocket-client-2.9.0.0/quantrocket/satellite.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2023-04-04 15:00:24.565415 quantrocket-client-2.9.0.0/quantrocket/utils/
--rw-rw-rw-   0 root         (0) root         (0)      804 2023-04-04 14:59:51.000000 quantrocket-client-2.9.0.0/quantrocket/utils/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     2335 2023-04-04 14:59:51.000000 quantrocket-client-2.9.0.0/quantrocket/utils/_parse.py
--rw-rw-rw-   0 root         (0) root         (0)      768 2023-04-04 14:59:51.000000 quantrocket-client-2.9.0.0/quantrocket/utils/_typing.py
--rw-rw-rw-   0 root         (0) root         (0)     1709 2023-04-04 14:59:51.000000 quantrocket-client-2.9.0.0/quantrocket/utils/_warn.py
--rw-rw-rw-   0 root         (0) root         (0)     2462 2023-04-04 14:59:51.000000 quantrocket-client-2.9.0.0/quantrocket/utils/dt.py
--rw-rw-rw-   0 root         (0) root         (0)     1896 2023-04-04 14:59:51.000000 quantrocket-client-2.9.0.0/quantrocket/version.py
--rw-rw-rw-   0 root         (0) root         (0)    40524 2023-04-04 14:59:51.000000 quantrocket-client-2.9.0.0/quantrocket/zipline.py
-drwxrwxrwx   0 root         (0) root         (0)        0 2023-04-04 15:00:24.565415 quantrocket-client-2.9.0.0/quantrocket_client.egg-info/
--rw-rw-rw-   0 root         (0) root         (0)      291 2023-04-04 15:00:24.000000 quantrocket-client-2.9.0.0/quantrocket_client.egg-info/PKG-INFO
--rw-rw-rw-   0 root         (0) root         (0)     2197 2023-04-04 15:00:24.000000 quantrocket-client-2.9.0.0/quantrocket_client.egg-info/SOURCES.txt
--rw-rw-rw-   0 root         (0) root         (0)        1 2023-04-04 15:00:24.000000 quantrocket-client-2.9.0.0/quantrocket_client.egg-info/dependency_links.txt
--rw-rw-rw-   0 root         (0) root         (0)       63 2023-04-04 15:00:24.000000 quantrocket-client-2.9.0.0/quantrocket_client.egg-info/entry_points.txt
--rw-rw-rw-   0 root         (0) root         (0)        1 2023-04-04 15:00:13.000000 quantrocket-client-2.9.0.0/quantrocket_client.egg-info/not-zip-safe
--rw-rw-rw-   0 root         (0) root         (0)       36 2023-04-04 15:00:24.000000 quantrocket-client-2.9.0.0/quantrocket_client.egg-info/requires.txt
--rw-rw-rw-   0 root         (0) root         (0)       12 2023-04-04 15:00:24.000000 quantrocket-client-2.9.0.0/quantrocket_client.egg-info/top_level.txt
--rw-rw-rw-   0 root         (0) root         (0)      229 2023-04-04 15:00:24.565415 quantrocket-client-2.9.0.0/setup.cfg
--rw-rw-rw-   0 root         (0) root         (0)     1341 2023-04-04 14:59:51.000000 quantrocket-client-2.9.0.0/setup.py
--rw-rw-rw-   0 root         (0) root         (0)    68611 2023-04-04 14:59:51.000000 quantrocket-client-2.9.0.0/versioneer.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2023-04-06 19:26:25.700506 quantrocket-client-2.9.0.1/
+-rw-rw-rw-   0 root         (0) root         (0)     9144 2023-04-06 19:25:56.000000 quantrocket-client-2.9.0.1/LICENSE.txt
+-rw-rw-rw-   0 root         (0) root         (0)       54 2023-04-06 19:25:56.000000 quantrocket-client-2.9.0.1/MANIFEST.in
+-rw-rw-rw-   0 root         (0) root         (0)      291 2023-04-06 19:26:25.700506 quantrocket-client-2.9.0.1/PKG-INFO
+-rw-rw-rw-   0 root         (0) root         (0)      354 2023-04-06 19:25:56.000000 quantrocket-client-2.9.0.1/README.md
+drwxrwxrwx   0 root         (0) root         (0)        0 2023-04-06 19:26:25.700506 quantrocket-client-2.9.0.1/quantrocket/
+-rw-rw-rw-   0 root         (0) root         (0)     3106 2023-04-06 19:25:56.000000 quantrocket-client-2.9.0.1/quantrocket/__init__.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2023-04-06 19:26:25.692506 quantrocket-client-2.9.0.1/quantrocket/_cli/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2023-04-06 19:25:56.000000 quantrocket-client-2.9.0.1/quantrocket/_cli/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     3792 2023-04-06 19:25:56.000000 quantrocket-client-2.9.0.1/quantrocket/_cli/commands.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2023-04-06 19:26:25.696506 quantrocket-client-2.9.0.1/quantrocket/_cli/subcommands/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2023-04-06 19:25:56.000000 quantrocket-client-2.9.0.1/quantrocket/_cli/subcommands/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     8604 2023-04-06 19:25:56.000000 quantrocket-client-2.9.0.1/quantrocket/_cli/subcommands/account.py
+-rw-rw-rw-   0 root         (0) root         (0)    20169 2023-04-06 19:25:56.000000 quantrocket-client-2.9.0.1/quantrocket/_cli/subcommands/blotter.py
+-rw-rw-rw-   0 root         (0) root         (0)     3106 2023-04-06 19:25:56.000000 quantrocket-client-2.9.0.1/quantrocket/_cli/subcommands/codeload.py
+-rw-rw-rw-   0 root         (0) root         (0)     3231 2023-04-06 19:25:56.000000 quantrocket-client-2.9.0.1/quantrocket/_cli/subcommands/countdown.py
+-rw-rw-rw-   0 root         (0) root         (0)     6800 2023-04-06 19:25:56.000000 quantrocket-client-2.9.0.1/quantrocket/_cli/subcommands/db.py
+-rw-rw-rw-   0 root         (0) root         (0)     8307 2023-04-06 19:25:56.000000 quantrocket-client-2.9.0.1/quantrocket/_cli/subcommands/flightlog.py
+-rw-rw-rw-   0 root         (0) root         (0)    42083 2023-04-06 19:25:56.000000 quantrocket-client-2.9.0.1/quantrocket/_cli/subcommands/fundamental.py
+-rw-rw-rw-   0 root         (0) root         (0)    21184 2023-04-06 19:25:56.000000 quantrocket-client-2.9.0.1/quantrocket/_cli/subcommands/history.py
+-rw-rw-rw-   0 root         (0) root         (0)     1253 2023-04-06 19:25:56.000000 quantrocket-client-2.9.0.1/quantrocket/_cli/subcommands/houston.py
+-rw-rw-rw-   0 root         (0) root         (0)     6954 2023-04-06 19:25:56.000000 quantrocket-client-2.9.0.1/quantrocket/_cli/subcommands/ibg.py
+-rw-rw-rw-   0 root         (0) root         (0)     5744 2023-04-06 19:25:56.000000 quantrocket-client-2.9.0.1/quantrocket/_cli/subcommands/license.py
+-rw-rw-rw-   0 root         (0) root         (0)    38518 2023-04-06 19:25:56.000000 quantrocket-client-2.9.0.1/quantrocket/_cli/subcommands/master.py
+-rw-rw-rw-   0 root         (0) root         (0)    18833 2023-04-06 19:25:56.000000 quantrocket-client-2.9.0.1/quantrocket/_cli/subcommands/moonshot.py
+-rw-rw-rw-   0 root         (0) root         (0)    21551 2023-04-06 19:25:56.000000 quantrocket-client-2.9.0.1/quantrocket/_cli/subcommands/realtime.py
+-rw-rw-rw-   0 root         (0) root         (0)     2896 2023-04-06 19:25:56.000000 quantrocket-client-2.9.0.1/quantrocket/_cli/subcommands/satellite.py
+-rw-rw-rw-   0 root         (0) root         (0)     1583 2023-04-06 19:25:56.000000 quantrocket-client-2.9.0.1/quantrocket/_cli/subcommands/version.py
+-rw-rw-rw-   0 root         (0) root         (0)    26399 2023-04-06 19:25:56.000000 quantrocket-client-2.9.0.1/quantrocket/_cli/subcommands/zipline.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2023-04-06 19:26:25.696506 quantrocket-client-2.9.0.1/quantrocket/_cli/utils/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2023-04-06 19:25:56.000000 quantrocket-client-2.9.0.1/quantrocket/_cli/utils/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     1561 2023-04-06 19:25:56.000000 quantrocket-client-2.9.0.1/quantrocket/_cli/utils/files.py
+-rw-rw-rw-   0 root         (0) root         (0)     1963 2023-04-06 19:25:56.000000 quantrocket-client-2.9.0.1/quantrocket/_cli/utils/output.py
+-rw-rw-rw-   0 root         (0) root         (0)     2371 2023-04-06 19:25:56.000000 quantrocket-client-2.9.0.1/quantrocket/_cli/utils/parse.py
+-rw-rw-rw-   0 root         (0) root         (0)      844 2023-04-06 19:25:56.000000 quantrocket-client-2.9.0.1/quantrocket/_cli/utils/stream.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2023-04-06 19:26:25.700506 quantrocket-client-2.9.0.1/quantrocket/_tests/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2023-04-06 19:25:56.000000 quantrocket-client-2.9.0.1/quantrocket/_tests/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    29437 2023-04-06 19:25:56.000000 quantrocket-client-2.9.0.1/quantrocket/_tests/test_blotter.py
+-rw-rw-rw-   0 root         (0) root         (0)   184790 2023-04-06 19:25:56.000000 quantrocket-client-2.9.0.1/quantrocket/_tests/test_fundamental.py
+-rw-rw-rw-   0 root         (0) root         (0)    62221 2023-04-06 19:25:56.000000 quantrocket-client-2.9.0.1/quantrocket/_tests/test_master.py
+-rw-rw-rw-   0 root         (0) root         (0)    17235 2023-04-06 19:25:56.000000 quantrocket-client-2.9.0.1/quantrocket/_tests/test_moonshot.py
+-rw-rw-rw-   0 root         (0) root         (0)   152902 2023-04-06 19:25:56.000000 quantrocket-client-2.9.0.1/quantrocket/_tests/test_price.py
+-rw-rw-rw-   0 root         (0) root         (0)     2562 2023-04-06 19:25:56.000000 quantrocket-client-2.9.0.1/quantrocket/_tests/test_utils.py
+-rw-rw-rw-   0 root         (0) root         (0)      499 2023-04-06 19:26:25.700506 quantrocket-client-2.9.0.1/quantrocket/_version.py
+-rw-rw-rw-   0 root         (0) root         (0)    10293 2023-04-06 19:25:56.000000 quantrocket-client-2.9.0.1/quantrocket/account.py
+-rw-rw-rw-   0 root         (0) root         (0)    27865 2023-04-06 19:25:56.000000 quantrocket-client-2.9.0.1/quantrocket/blotter.py
+-rw-rw-rw-   0 root         (0) root         (0)     3159 2023-04-06 19:25:56.000000 quantrocket-client-2.9.0.1/quantrocket/codeload.py
+-rw-rw-rw-   0 root         (0) root         (0)     4027 2023-04-06 19:25:56.000000 quantrocket-client-2.9.0.1/quantrocket/countdown.py
+-rw-rw-rw-   0 root         (0) root         (0)    14945 2023-04-06 19:25:56.000000 quantrocket-client-2.9.0.1/quantrocket/db.py
+-rw-rw-rw-   0 root         (0) root         (0)     1309 2023-04-06 19:25:56.000000 quantrocket-client-2.9.0.1/quantrocket/exceptions.py
+-rw-rw-rw-   0 root         (0) root         (0)    14874 2023-04-06 19:25:56.000000 quantrocket-client-2.9.0.1/quantrocket/flightlog.py
+-rw-rw-rw-   0 root         (0) root         (0)   121781 2023-04-06 19:25:56.000000 quantrocket-client-2.9.0.1/quantrocket/fundamental.py
+-rw-rw-rw-   0 root         (0) root         (0)    24358 2023-04-06 19:25:56.000000 quantrocket-client-2.9.0.1/quantrocket/history.py
+-rw-rw-rw-   0 root         (0) root         (0)     7439 2023-04-06 19:25:56.000000 quantrocket-client-2.9.0.1/quantrocket/houston.py
+-rw-rw-rw-   0 root         (0) root         (0)     8222 2023-04-06 19:25:56.000000 quantrocket-client-2.9.0.1/quantrocket/ibg.py
+-rw-rw-rw-   0 root         (0) root         (0)     7632 2023-04-06 19:25:56.000000 quantrocket-client-2.9.0.1/quantrocket/license.py
+-rw-rw-rw-   0 root         (0) root         (0)    54435 2023-04-06 19:25:56.000000 quantrocket-client-2.9.0.1/quantrocket/master.py
+-rw-rw-rw-   0 root         (0) root         (0)    25014 2023-04-06 19:25:56.000000 quantrocket-client-2.9.0.1/quantrocket/moonshot.py
+-rw-rw-rw-   0 root         (0) root         (0)    31387 2023-04-06 19:25:56.000000 quantrocket-client-2.9.0.1/quantrocket/price.py
+-rw-rw-rw-   0 root         (0) root         (0)        0 2023-04-06 19:25:56.000000 quantrocket-client-2.9.0.1/quantrocket/py.typed
+-rw-rw-rw-   0 root         (0) root         (0)    26122 2023-04-06 19:25:56.000000 quantrocket-client-2.9.0.1/quantrocket/realtime.py
+-rw-rw-rw-   0 root         (0) root         (0)     4729 2023-04-06 19:25:56.000000 quantrocket-client-2.9.0.1/quantrocket/satellite.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2023-04-06 19:26:25.700506 quantrocket-client-2.9.0.1/quantrocket/utils/
+-rw-rw-rw-   0 root         (0) root         (0)      804 2023-04-06 19:25:56.000000 quantrocket-client-2.9.0.1/quantrocket/utils/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     2335 2023-04-06 19:25:56.000000 quantrocket-client-2.9.0.1/quantrocket/utils/_parse.py
+-rw-rw-rw-   0 root         (0) root         (0)      768 2023-04-06 19:25:56.000000 quantrocket-client-2.9.0.1/quantrocket/utils/_typing.py
+-rw-rw-rw-   0 root         (0) root         (0)     1709 2023-04-06 19:25:56.000000 quantrocket-client-2.9.0.1/quantrocket/utils/_warn.py
+-rw-rw-rw-   0 root         (0) root         (0)     2462 2023-04-06 19:25:56.000000 quantrocket-client-2.9.0.1/quantrocket/utils/dt.py
+-rw-rw-rw-   0 root         (0) root         (0)     1896 2023-04-06 19:25:56.000000 quantrocket-client-2.9.0.1/quantrocket/version.py
+-rw-rw-rw-   0 root         (0) root         (0)    40524 2023-04-06 19:25:56.000000 quantrocket-client-2.9.0.1/quantrocket/zipline.py
+drwxrwxrwx   0 root         (0) root         (0)        0 2023-04-06 19:26:25.700506 quantrocket-client-2.9.0.1/quantrocket_client.egg-info/
+-rw-rw-rw-   0 root         (0) root         (0)      291 2023-04-06 19:26:25.000000 quantrocket-client-2.9.0.1/quantrocket_client.egg-info/PKG-INFO
+-rw-rw-rw-   0 root         (0) root         (0)     2197 2023-04-06 19:26:25.000000 quantrocket-client-2.9.0.1/quantrocket_client.egg-info/SOURCES.txt
+-rw-rw-rw-   0 root         (0) root         (0)        1 2023-04-06 19:26:25.000000 quantrocket-client-2.9.0.1/quantrocket_client.egg-info/dependency_links.txt
+-rw-rw-rw-   0 root         (0) root         (0)       63 2023-04-06 19:26:25.000000 quantrocket-client-2.9.0.1/quantrocket_client.egg-info/entry_points.txt
+-rw-rw-rw-   0 root         (0) root         (0)        1 2023-04-06 19:26:16.000000 quantrocket-client-2.9.0.1/quantrocket_client.egg-info/not-zip-safe
+-rw-rw-rw-   0 root         (0) root         (0)       36 2023-04-06 19:26:25.000000 quantrocket-client-2.9.0.1/quantrocket_client.egg-info/requires.txt
+-rw-rw-rw-   0 root         (0) root         (0)       12 2023-04-06 19:26:25.000000 quantrocket-client-2.9.0.1/quantrocket_client.egg-info/top_level.txt
+-rw-rw-rw-   0 root         (0) root         (0)      229 2023-04-06 19:26:25.700506 quantrocket-client-2.9.0.1/setup.cfg
+-rw-rw-rw-   0 root         (0) root         (0)     1341 2023-04-06 19:25:56.000000 quantrocket-client-2.9.0.1/setup.py
+-rw-rw-rw-   0 root         (0) root         (0)    68611 2023-04-06 19:25:56.000000 quantrocket-client-2.9.0.1/versioneer.py
```

### Comparing `quantrocket-client-2.9.0.0/LICENSE.txt` & `quantrocket-client-2.9.0.1/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `quantrocket-client-2.9.0.0/quantrocket/__init__.py` & `quantrocket-client-2.9.0.1/quantrocket/__init__.py`

 * *Files identical despite different names*

### Comparing `quantrocket-client-2.9.0.0/quantrocket/_cli/commands.py` & `quantrocket-client-2.9.0.1/quantrocket/_cli/commands.py`

 * *Files identical despite different names*

### Comparing `quantrocket-client-2.9.0.0/quantrocket/_cli/subcommands/account.py` & `quantrocket-client-2.9.0.1/quantrocket/_cli/subcommands/account.py`

 * *Files identical despite different names*

### Comparing `quantrocket-client-2.9.0.0/quantrocket/_cli/subcommands/blotter.py` & `quantrocket-client-2.9.0.1/quantrocket/_cli/subcommands/blotter.py`

 * *Files identical despite different names*

### Comparing `quantrocket-client-2.9.0.0/quantrocket/_cli/subcommands/codeload.py` & `quantrocket-client-2.9.0.1/quantrocket/_cli/subcommands/codeload.py`

 * *Files identical despite different names*

### Comparing `quantrocket-client-2.9.0.0/quantrocket/_cli/subcommands/countdown.py` & `quantrocket-client-2.9.0.1/quantrocket/_cli/subcommands/countdown.py`

 * *Files identical despite different names*

### Comparing `quantrocket-client-2.9.0.0/quantrocket/_cli/subcommands/db.py` & `quantrocket-client-2.9.0.1/quantrocket/_cli/subcommands/db.py`

 * *Files identical despite different names*

### Comparing `quantrocket-client-2.9.0.0/quantrocket/_cli/subcommands/flightlog.py` & `quantrocket-client-2.9.0.1/quantrocket/_cli/subcommands/flightlog.py`

 * *Files 0% similar despite different names*

```diff
@@ -215,15 +215,15 @@
         default="INFO",
         metavar="LEVEL",
         choices=("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"),
         help="the log level for the message. Possible choices: %(choices)s")
     parser.add_argument(
         "-n", "--name",
         dest="logger_name",
-        default="quantrocket._cli",
+        default="quantrocket.cli",
         help="the logger name")
     parser.set_defaults(func="quantrocket.flightlog._cli_log_message")
 
     examples = """
 Set or show the flightlog timezone.
 
 Notes
```

### Comparing `quantrocket-client-2.9.0.0/quantrocket/_cli/subcommands/fundamental.py` & `quantrocket-client-2.9.0.1/quantrocket/_cli/subcommands/fundamental.py`

 * *Files identical despite different names*

### Comparing `quantrocket-client-2.9.0.0/quantrocket/_cli/subcommands/history.py` & `quantrocket-client-2.9.0.1/quantrocket/_cli/subcommands/history.py`

 * *Files identical despite different names*

### Comparing `quantrocket-client-2.9.0.0/quantrocket/_cli/subcommands/houston.py` & `quantrocket-client-2.9.0.1/quantrocket/_cli/subcommands/houston.py`

 * *Files identical despite different names*

### Comparing `quantrocket-client-2.9.0.0/quantrocket/_cli/subcommands/ibg.py` & `quantrocket-client-2.9.0.1/quantrocket/_cli/subcommands/ibg.py`

 * *Files identical despite different names*

### Comparing `quantrocket-client-2.9.0.0/quantrocket/_cli/subcommands/license.py` & `quantrocket-client-2.9.0.1/quantrocket/_cli/subcommands/license.py`

 * *Files identical despite different names*

### Comparing `quantrocket-client-2.9.0.0/quantrocket/_cli/subcommands/master.py` & `quantrocket-client-2.9.0.1/quantrocket/_cli/subcommands/master.py`

 * *Files identical despite different names*

### Comparing `quantrocket-client-2.9.0.0/quantrocket/_cli/subcommands/moonshot.py` & `quantrocket-client-2.9.0.1/quantrocket/_cli/subcommands/moonshot.py`

 * *Files identical despite different names*

### Comparing `quantrocket-client-2.9.0.0/quantrocket/_cli/subcommands/realtime.py` & `quantrocket-client-2.9.0.1/quantrocket/_cli/subcommands/realtime.py`

 * *Files identical despite different names*

### Comparing `quantrocket-client-2.9.0.0/quantrocket/_cli/subcommands/satellite.py` & `quantrocket-client-2.9.0.1/quantrocket/_cli/subcommands/satellite.py`

 * *Files identical despite different names*

### Comparing `quantrocket-client-2.9.0.0/quantrocket/_cli/subcommands/version.py` & `quantrocket-client-2.9.0.1/quantrocket/_cli/subcommands/version.py`

 * *Files identical despite different names*

### Comparing `quantrocket-client-2.9.0.0/quantrocket/_cli/subcommands/zipline.py` & `quantrocket-client-2.9.0.1/quantrocket/_cli/subcommands/zipline.py`

 * *Files identical despite different names*

### Comparing `quantrocket-client-2.9.0.0/quantrocket/_cli/utils/files.py` & `quantrocket-client-2.9.0.1/quantrocket/_cli/utils/files.py`

 * *Files identical despite different names*

### Comparing `quantrocket-client-2.9.0.0/quantrocket/_cli/utils/output.py` & `quantrocket-client-2.9.0.1/quantrocket/_cli/utils/output.py`

 * *Files identical despite different names*

### Comparing `quantrocket-client-2.9.0.0/quantrocket/_cli/utils/parse.py` & `quantrocket-client-2.9.0.1/quantrocket/_cli/utils/parse.py`

 * *Files identical despite different names*

### Comparing `quantrocket-client-2.9.0.0/quantrocket/_cli/utils/stream.py` & `quantrocket-client-2.9.0.1/quantrocket/_cli/utils/stream.py`

 * *Files identical despite different names*

### Comparing `quantrocket-client-2.9.0.0/quantrocket/_tests/test_blotter.py` & `quantrocket-client-2.9.0.1/quantrocket/_tests/test_blotter.py`

 * *Files identical despite different names*

### Comparing `quantrocket-client-2.9.0.0/quantrocket/_tests/test_fundamental.py` & `quantrocket-client-2.9.0.1/quantrocket/_tests/test_fundamental.py`

 * *Files identical despite different names*

### Comparing `quantrocket-client-2.9.0.0/quantrocket/_tests/test_master.py` & `quantrocket-client-2.9.0.1/quantrocket/_tests/test_master.py`

 * *Files identical despite different names*

### Comparing `quantrocket-client-2.9.0.0/quantrocket/_tests/test_moonshot.py` & `quantrocket-client-2.9.0.1/quantrocket/_tests/test_moonshot.py`

 * *Files identical despite different names*

### Comparing `quantrocket-client-2.9.0.0/quantrocket/_tests/test_price.py` & `quantrocket-client-2.9.0.1/quantrocket/_tests/test_price.py`

 * *Files identical despite different names*

### Comparing `quantrocket-client-2.9.0.0/quantrocket/_tests/test_utils.py` & `quantrocket-client-2.9.0.1/quantrocket/_tests/test_utils.py`

 * *Files identical despite different names*

### Comparing `quantrocket-client-2.9.0.0/quantrocket/account.py` & `quantrocket-client-2.9.0.1/quantrocket/account.py`

 * *Files identical despite different names*

### Comparing `quantrocket-client-2.9.0.0/quantrocket/blotter.py` & `quantrocket-client-2.9.0.1/quantrocket/blotter.py`

 * *Files identical despite different names*

### Comparing `quantrocket-client-2.9.0.0/quantrocket/codeload.py` & `quantrocket-client-2.9.0.1/quantrocket/codeload.py`

 * *Files identical despite different names*

### Comparing `quantrocket-client-2.9.0.0/quantrocket/countdown.py` & `quantrocket-client-2.9.0.1/quantrocket/countdown.py`

 * *Files identical despite different names*

### Comparing `quantrocket-client-2.9.0.0/quantrocket/db.py` & `quantrocket-client-2.9.0.1/quantrocket/db.py`

 * *Files identical despite different names*

### Comparing `quantrocket-client-2.9.0.0/quantrocket/exceptions.py` & `quantrocket-client-2.9.0.1/quantrocket/exceptions.py`

 * *Files identical despite different names*

### Comparing `quantrocket-client-2.9.0.0/quantrocket/flightlog.py` & `quantrocket-client-2.9.0.1/quantrocket/flightlog.py`

 * *Files identical despite different names*

### Comparing `quantrocket-client-2.9.0.0/quantrocket/fundamental.py` & `quantrocket-client-2.9.0.1/quantrocket/fundamental.py`

 * *Files identical despite different names*

### Comparing `quantrocket-client-2.9.0.0/quantrocket/history.py` & `quantrocket-client-2.9.0.1/quantrocket/history.py`

 * *Files identical despite different names*

### Comparing `quantrocket-client-2.9.0.0/quantrocket/houston.py` & `quantrocket-client-2.9.0.1/quantrocket/houston.py`

 * *Files identical despite different names*

### Comparing `quantrocket-client-2.9.0.0/quantrocket/ibg.py` & `quantrocket-client-2.9.0.1/quantrocket/ibg.py`

 * *Files identical despite different names*

### Comparing `quantrocket-client-2.9.0.0/quantrocket/license.py` & `quantrocket-client-2.9.0.1/quantrocket/license.py`

 * *Files identical despite different names*

### Comparing `quantrocket-client-2.9.0.0/quantrocket/master.py` & `quantrocket-client-2.9.0.1/quantrocket/master.py`

 * *Files identical despite different names*

### Comparing `quantrocket-client-2.9.0.0/quantrocket/moonshot.py` & `quantrocket-client-2.9.0.1/quantrocket/moonshot.py`

 * *Files identical despite different names*

### Comparing `quantrocket-client-2.9.0.0/quantrocket/price.py` & `quantrocket-client-2.9.0.1/quantrocket/price.py`

 * *Files identical despite different names*

### Comparing `quantrocket-client-2.9.0.0/quantrocket/realtime.py` & `quantrocket-client-2.9.0.1/quantrocket/realtime.py`

 * *Files identical despite different names*

### Comparing `quantrocket-client-2.9.0.0/quantrocket/satellite.py` & `quantrocket-client-2.9.0.1/quantrocket/satellite.py`

 * *Files 4% similar despite different names*

```diff
@@ -51,14 +51,18 @@
 def execute_command(
     cmd: str,
     return_file: str = None,
     filepath_or_buffer: FilepathOrBuffer = None,
     params: dict[str, Any] = None,
     service: str = "satellite"
     ) -> dict[str, str]:
+    pass
+
+def execute_command(cmd, return_file=None, filepath_or_buffer=None,
+                    params=None, service="satellite"):
     """
     Execute a Python function or arbitrary shell command on a satellite service.
 
     Parameters
     ----------
     cmd: str, required
         the shell command to run, or the Python function in dot notation (must
```

### Comparing `quantrocket-client-2.9.0.0/quantrocket/utils/__init__.py` & `quantrocket-client-2.9.0.1/quantrocket/utils/__init__.py`

 * *Files identical despite different names*

### Comparing `quantrocket-client-2.9.0.0/quantrocket/utils/_parse.py` & `quantrocket-client-2.9.0.1/quantrocket/utils/_parse.py`

 * *Files identical despite different names*

### Comparing `quantrocket-client-2.9.0.0/quantrocket/utils/_typing.py` & `quantrocket-client-2.9.0.1/quantrocket/utils/_typing.py`

 * *Files identical despite different names*

### Comparing `quantrocket-client-2.9.0.0/quantrocket/utils/_warn.py` & `quantrocket-client-2.9.0.1/quantrocket/utils/_warn.py`

 * *Files identical despite different names*

### Comparing `quantrocket-client-2.9.0.0/quantrocket/utils/dt.py` & `quantrocket-client-2.9.0.1/quantrocket/utils/dt.py`

 * *Files identical despite different names*

### Comparing `quantrocket-client-2.9.0.0/quantrocket/version.py` & `quantrocket-client-2.9.0.1/quantrocket/version.py`

 * *Files identical despite different names*

### Comparing `quantrocket-client-2.9.0.0/quantrocket/zipline.py` & `quantrocket-client-2.9.0.1/quantrocket/zipline.py`

 * *Files identical despite different names*

### Comparing `quantrocket-client-2.9.0.0/quantrocket_client.egg-info/SOURCES.txt` & `quantrocket-client-2.9.0.1/quantrocket_client.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `quantrocket-client-2.9.0.0/setup.py` & `quantrocket-client-2.9.0.1/setup.py`

 * *Files identical despite different names*

### Comparing `quantrocket-client-2.9.0.0/versioneer.py` & `quantrocket-client-2.9.0.1/versioneer.py`

 * *Files identical despite different names*

