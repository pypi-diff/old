# Comparing `tmp/piperider-nightly-0.9.0.20220920.tar.gz` & `tmp/piperider-nightly-0.9.0.20220921.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "piperider-nightly-0.9.0.20220920.tar", last modified: Tue Sep 20 18:05:46 2022, max compression
+gzip compressed data, was "piperider-nightly-0.9.0.20220921.tar", last modified: Wed Sep 21 18:05:36 2022, max compression
```

## Comparing `piperider-nightly-0.9.0.20220920.tar` & `piperider-nightly-0.9.0.20220921.tar`

### file list

```diff
@@ -1,276 +1,276 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-20 18:05:46.536831 piperider-nightly-0.9.0.20220920/
--rw-r--r--   0 runner    (1001) docker     (121)    11357 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/LICENSE
--rw-r--r--   0 runner    (1001) docker     (121)     8714 2022-09-20 18:05:46.536831 piperider-nightly-0.9.0.20220920/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     7867 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/README.md
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-20 18:05:46.504831 piperider-nightly-0.9.0.20220920/piperider_cli/
--rw-r--r--   0 runner    (1001) docker     (121)       75 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/SENTRY_DNS
--rw-r--r--   0 runner    (1001) docker     (121)       15 2022-09-20 18:05:24.000000 piperider-nightly-0.9.0.20220920/piperider_cli/VERSION
--rw-r--r--   0 runner    (1001) docker     (121)     3771 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)       59 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/__main__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-20 18:05:46.504831 piperider-nightly-0.9.0.20220920/piperider_cli/adapter/
--rw-r--r--   0 runner    (1001) docker     (121)       48 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/adapter/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    11325 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/adapter/dbt_adapter.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-20 18:05:46.504831 piperider-nightly-0.9.0.20220920/piperider_cli/assertion_engine/
--rw-r--r--   0 runner    (1001) docker     (121)       92 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/assertion_engine/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    24636 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/assertion_engine/assertion.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-20 18:05:46.504831 piperider-nightly-0.9.0.20220920/piperider_cli/assertion_engine/recommended_rules/
--rw-r--r--   0 runner    (1001) docker     (121)      103 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/assertion_engine/recommended_rules/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      500 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/assertion_engine/recommended_rules/recommender_assertion.py
--rw-r--r--   0 runner    (1001) docker     (121)     4458 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/assertion_engine/recommended_rules/table_assertions.py
--rw-r--r--   0 runner    (1001) docker     (121)     4531 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/assertion_engine/recommender.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-20 18:05:46.504831 piperider-nightly-0.9.0.20220920/piperider_cli/assertion_engine/types/
--rw-r--r--   0 runner    (1001) docker     (121)     2500 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/assertion_engine/types/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     4567 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/assertion_engine/types/assert_column_misc.py
--rw-r--r--   0 runner    (1001) docker     (121)     5430 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/assertion_engine/types/assert_column_ranges.py
--rw-r--r--   0 runner    (1001) docker     (121)     4936 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/assertion_engine/types/assert_column_types.py
--rw-r--r--   0 runner    (1001) docker     (121)     4110 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/assertion_engine/types/assert_rows.py
--rw-r--r--   0 runner    (1001) docker     (121)      586 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/assertion_engine/types/base.py
--rw-r--r--   0 runner    (1001) docker     (121)     3315 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/assertion_generator.py
--rw-r--r--   0 runner    (1001) docker     (121)    10924 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/cli.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-20 18:05:46.504831 piperider-nightly-0.9.0.20220920/piperider_cli/cloud/
--rw-r--r--   0 runner    (1001) docker     (121)     4192 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/cloud/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     3486 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/cloud_connector.py
--rw-r--r--   0 runner    (1001) docker     (121)    10957 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/compare_report.py
--rw-r--r--   0 runner    (1001) docker     (121)    12644 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/configuration.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-20 18:05:46.504831 piperider-nightly-0.9.0.20220920/piperider_cli/data/
--rw-r--r--   0 runner    (1001) docker     (121)       41 2022-09-20 18:05:24.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/COMMIT
--rw-r--r--   0 runner    (1001) docker     (121)       48 2022-09-20 18:05:24.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/CONFIG
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-20 18:05:46.504831 piperider-nightly-0.9.0.20220920/piperider_cli/data/piperider-init-template/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-20 18:05:46.504831 piperider-nightly-0.9.0.20220920/piperider_cli/data/piperider-init-template/assertions/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/piperider-init-template/assertions/placeholder.txt
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/piperider-init-template/config.yml
--rw-r--r--   0 runner    (1001) docker     (121)       92 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/piperider-init-template/gitignore
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-20 18:05:46.504831 piperider-nightly-0.9.0.20220920/piperider_cli/data/piperider-init-template/plugins/
--rw-r--r--   0 runner    (1001) docker     (121)     3048 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/piperider-init-template/plugins/customized_assertions.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-20 18:05:46.500831 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-20 18:05:46.508831 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-20 18:05:46.508831 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/Discord/
--rw-r--r--   0 runner    (1001) docker     (121)     2094 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/Discord/Discord-Logo.svg
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-20 18:05:46.508831 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/GitHub/
--rw-r--r--   0 runner    (1001) docker     (121)     6215 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/GitHub/GitHub-Logo.svg
--rw-r--r--   0 runner    (1001) docker     (121)     5972 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/asset-manifest.json
--rw-r--r--   0 runner    (1001) docker     (121)     1676 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/index.html
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-20 18:05:46.508831 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/logo/
--rw-r--r--   0 runner    (1001) docker     (121)     4504 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/logo/android-icon-144x144.png
--rw-r--r--   0 runner    (1001) docker     (121)     5132 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/logo/android-icon-192x192.png
--rw-r--r--   0 runner    (1001) docker     (121)     1393 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/logo/android-icon-36x36.png
--rw-r--r--   0 runner    (1001) docker     (121)     1737 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/logo/android-icon-48x48.png
--rw-r--r--   0 runner    (1001) docker     (121)     2003 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/logo/android-icon-72x72.png
--rw-r--r--   0 runner    (1001) docker     (121)     2491 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/logo/android-icon-96x96.png
--rw-r--r--   0 runner    (1001) docker     (121)     3530 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/logo/apple-icon-114x114.png
--rw-r--r--   0 runner    (1001) docker     (121)     3647 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/logo/apple-icon-120x120.png
--rw-r--r--   0 runner    (1001) docker     (121)     4504 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/logo/apple-icon-144x144.png
--rw-r--r--   0 runner    (1001) docker     (121)     4819 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/logo/apple-icon-152x152.png
--rw-r--r--   0 runner    (1001) docker     (121)     5783 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/logo/apple-icon-180x180.png
--rw-r--r--   0 runner    (1001) docker     (121)     1763 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/logo/apple-icon-57x57.png
--rw-r--r--   0 runner    (1001) docker     (121)     1876 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/logo/apple-icon-60x60.png
--rw-r--r--   0 runner    (1001) docker     (121)     2003 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/logo/apple-icon-72x72.png
--rw-r--r--   0 runner    (1001) docker     (121)     2096 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/logo/apple-icon-76x76.png
--rw-r--r--   0 runner    (1001) docker     (121)     5676 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/logo/apple-icon-precomposed.png
--rw-r--r--   0 runner    (1001) docker     (121)     5676 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/logo/apple-icon.png
--rw-r--r--   0 runner    (1001) docker     (121)      281 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/logo/browserconfig.xml
--rw-r--r--   0 runner    (1001) docker     (121)      975 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/logo/favicon-16x16.png
--rw-r--r--   0 runner    (1001) docker     (121)     1372 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/logo/favicon-32x32.png
--rw-r--r--   0 runner    (1001) docker     (121)     2491 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/logo/favicon-96x96.png
--rw-r--r--   0 runner    (1001) docker     (121)     1150 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/logo/favicon.ico
--rw-r--r--   0 runner    (1001) docker     (121)     7789 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/logo/logo.svg
--rw-r--r--   0 runner    (1001) docker     (121)      720 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/logo/manifest.json
--rw-r--r--   0 runner    (1001) docker     (121)     4504 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/logo/ms-icon-144x144.png
--rw-r--r--   0 runner    (1001) docker     (121)     4743 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/logo/ms-icon-150x150.png
--rw-r--r--   0 runner    (1001) docker     (121)    12342 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/logo/ms-icon-310x310.png
--rw-r--r--   0 runner    (1001) docker     (121)     2005 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/logo/ms-icon-70x70.png
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-20 18:05:46.500831 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-20 18:05:46.508831 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/css/
--rw-r--r--   0 runner    (1001) docker     (121)     5632 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/css/main.fcbcb80f.css
--rw-r--r--   0 runner    (1001) docker     (121)     8287 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/css/main.fcbcb80f.css.map
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-20 18:05:46.512831 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/js/
--rw-r--r--   0 runner    (1001) docker     (121)    20055 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/js/183.b8accd6c.chunk.js
--rw-r--r--   0 runner    (1001) docker     (121)    14053 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/js/276.fcb4db01.chunk.js
--rw-r--r--   0 runner    (1001) docker     (121)    11803 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/js/357.5328e62e.chunk.js
--rw-r--r--   0 runner    (1001) docker     (121)     4613 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/js/787.20f148af.chunk.js
--rw-r--r--   0 runner    (1001) docker     (121)     2096 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/js/836.945208d8.chunk.js
--rw-r--r--   0 runner    (1001) docker     (121)   104944 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/js/903.4ec9ff75.chunk.js
--rw-r--r--   0 runner    (1001) docker     (121)      336 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/js/903.4ec9ff75.chunk.js.LICENSE.txt
--rw-r--r--   0 runner    (1001) docker     (121)    12434 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/js/906.9eefb2c7.chunk.js
--rw-r--r--   0 runner    (1001) docker     (121)     2935 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/js/914.035c9fb2.chunk.js
--rw-r--r--   0 runner    (1001) docker     (121)    27742 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/js/982.4539617f.chunk.js
--rw-r--r--   0 runner    (1001) docker     (121)  1199840 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/js/main.3dd694e2.js
--rw-r--r--   0 runner    (1001) docker     (121)     1781 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/js/main.3dd694e2.js.LICENSE.txt
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-20 18:05:46.520831 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/
--rw-r--r--   0 runner    (1001) docker     (121)    32632 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-Black.ab57b908749eb205e3ad.woff
--rw-r--r--   0 runner    (1001) docker     (121)    24116 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-Black.cadfd7434852779eb395.woff2
--rw-r--r--   0 runner    (1001) docker     (121)    25732 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-BlackItalic.9bb4dd54e5afbea2e0ac.woff2
--rw-r--r--   0 runner    (1001) docker     (121)    34940 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-BlackItalic.f0098e273d2a3758b89c.woff
--rw-r--r--   0 runner    (1001) docker     (121)    33900 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-Bold.1577ca92013647c816b5.woff
--rw-r--r--   0 runner    (1001) docker     (121)    25152 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-Bold.f57c31edca48068386d7.woff2
--rw-r--r--   0 runner    (1001) docker     (121)    36168 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-BoldItalic.52e97aac5945285c9933.woff
--rw-r--r--   0 runner    (1001) docker     (121)    26684 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-BoldItalic.5b7f79817b551400186a.woff2
--rw-r--r--   0 runner    (1001) docker     (121)    33960 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-ExtraBold.0321ea88d696270daf4b.woff
--rw-r--r--   0 runner    (1001) docker     (121)    25220 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-ExtraBold.a611efd96602ca47acd9.woff2
--rw-r--r--   0 runner    (1001) docker     (121)    26736 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-ExtraBoldItalic.43f46f665391ff324c72.woff2
--rw-r--r--   0 runner    (1001) docker     (121)    36220 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-ExtraBoldItalic.dc0b36ae1c1bdac232e7.woff
--rw-r--r--   0 runner    (1001) docker     (121)    33248 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-ExtraLight.4e029f034c7e7263df9a.woff
--rw-r--r--   0 runner    (1001) docker     (121)    24852 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-ExtraLight.bafff4ae7f2a3395aa13.woff2
--rw-r--r--   0 runner    (1001) docker     (121)    26648 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-ExtraLightItalic.124644177779db0a8867.woff2
--rw-r--r--   0 runner    (1001) docker     (121)    35756 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-ExtraLightItalic.ff3def84a34422de5487.woff
--rw-r--r--   0 runner    (1001) docker     (121)    25872 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-Italic.9736c3faff86c01270b2.woff2
--rw-r--r--   0 runner    (1001) docker     (121)    34924 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-Italic.ce6bab8bc932d6080ec1.woff
--rw-r--r--   0 runner    (1001) docker     (121)    33248 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-Light.919d6ffdd987dc2e4717.woff
--rw-r--r--   0 runner    (1001) docker     (121)    24764 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-Light.aafd1643606ee83ad4cb.woff2
--rw-r--r--   0 runner    (1001) docker     (121)    26696 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-LightItalic.7f7cde8e1548e11231fb.woff2
--rw-r--r--   0 runner    (1001) docker     (121)    35788 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-LightItalic.e66e7a760a286c694d2b.woff
--rw-r--r--   0 runner    (1001) docker     (121)    33884 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-Medium.5a92f7b05463ecd61f45.woff
--rw-r--r--   0 runner    (1001) docker     (121)    25132 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-Medium.a6ca36dde32b3a1d0fd4.woff2
--rw-r--r--   0 runner    (1001) docker     (121)    26824 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-MediumItalic.dbc1ed152c7b11f501a3.woff2
--rw-r--r--   0 runner    (1001) docker     (121)    36236 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-MediumItalic.e3618413f59e00041fb3.woff
--rw-r--r--   0 runner    (1001) docker     (121)    23980 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-Regular.222064f2a764069868f4.woff2
--rw-r--r--   0 runner    (1001) docker     (121)    32236 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-Regular.67a27362108220436ffb.woff
--rw-r--r--   0 runner    (1001) docker     (121)    25240 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-SemiBold.599ce7634f46c5024ad0.woff2
--rw-r--r--   0 runner    (1001) docker     (121)    33944 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-SemiBold.c2e7341dd6ac6502be69.woff
--rw-r--r--   0 runner    (1001) docker     (121)    26892 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-SemiBoldItalic.09bc481607bd529abda7.woff2
--rw-r--r--   0 runner    (1001) docker     (121)    36280 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-SemiBoldItalic.43f7c276720845c6bb59.woff
--rw-r--r--   0 runner    (1001) docker     (121)    23636 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-Thin.92cada3d91581eb5112d.woff2
--rw-r--r--   0 runner    (1001) docker     (121)    32084 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-Thin.df0b1bcf558ccd5b48a2.woff
--rw-r--r--   0 runner    (1001) docker     (121)    34704 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-ThinItalic.78bf87d2ea41ac4365c1.woff
--rw-r--r--   0 runner    (1001) docker     (121)    25664 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-ThinItalic.82dd2dc2fb674d8273e4.woff2
--rw-r--r--   0 runner    (1001) docker     (121)    58892 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-italic.var.28904cc0eac675e1d19e.woff2
--rw-r--r--   0 runner    (1001) docker     (121)    53832 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-roman.var.f05060926bf5023f9930.woff2
--rw-r--r--   0 runner    (1001) docker     (121)    78400 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter.var.c3f97a25f56b5b416e49.woff2
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-20 18:05:46.520831 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-20 18:05:46.520831 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/Discord/
--rw-r--r--   0 runner    (1001) docker     (121)     2094 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/Discord/Discord-Logo.svg
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-20 18:05:46.520831 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/GitHub/
--rw-r--r--   0 runner    (1001) docker     (121)     6215 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/GitHub/GitHub-Logo.svg
--rw-r--r--   0 runner    (1001) docker     (121)     5972 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/asset-manifest.json
--rw-r--r--   0 runner    (1001) docker     (121)     1676 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/index.html
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-20 18:05:46.520831 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/logo/
--rw-r--r--   0 runner    (1001) docker     (121)     4504 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/logo/android-icon-144x144.png
--rw-r--r--   0 runner    (1001) docker     (121)     5132 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/logo/android-icon-192x192.png
--rw-r--r--   0 runner    (1001) docker     (121)     1393 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/logo/android-icon-36x36.png
--rw-r--r--   0 runner    (1001) docker     (121)     1737 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/logo/android-icon-48x48.png
--rw-r--r--   0 runner    (1001) docker     (121)     2003 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/logo/android-icon-72x72.png
--rw-r--r--   0 runner    (1001) docker     (121)     2491 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/logo/android-icon-96x96.png
--rw-r--r--   0 runner    (1001) docker     (121)     3530 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/logo/apple-icon-114x114.png
--rw-r--r--   0 runner    (1001) docker     (121)     3647 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/logo/apple-icon-120x120.png
--rw-r--r--   0 runner    (1001) docker     (121)     4504 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/logo/apple-icon-144x144.png
--rw-r--r--   0 runner    (1001) docker     (121)     4819 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/logo/apple-icon-152x152.png
--rw-r--r--   0 runner    (1001) docker     (121)     5783 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/logo/apple-icon-180x180.png
--rw-r--r--   0 runner    (1001) docker     (121)     1763 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/logo/apple-icon-57x57.png
--rw-r--r--   0 runner    (1001) docker     (121)     1876 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/logo/apple-icon-60x60.png
--rw-r--r--   0 runner    (1001) docker     (121)     2003 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/logo/apple-icon-72x72.png
--rw-r--r--   0 runner    (1001) docker     (121)     2096 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/logo/apple-icon-76x76.png
--rw-r--r--   0 runner    (1001) docker     (121)     5676 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/logo/apple-icon-precomposed.png
--rw-r--r--   0 runner    (1001) docker     (121)     5676 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/logo/apple-icon.png
--rw-r--r--   0 runner    (1001) docker     (121)      281 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/logo/browserconfig.xml
--rw-r--r--   0 runner    (1001) docker     (121)      975 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/logo/favicon-16x16.png
--rw-r--r--   0 runner    (1001) docker     (121)     1372 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/logo/favicon-32x32.png
--rw-r--r--   0 runner    (1001) docker     (121)     2491 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/logo/favicon-96x96.png
--rw-r--r--   0 runner    (1001) docker     (121)     1150 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/logo/favicon.ico
--rw-r--r--   0 runner    (1001) docker     (121)     7789 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/logo/logo.svg
--rw-r--r--   0 runner    (1001) docker     (121)      720 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/logo/manifest.json
--rw-r--r--   0 runner    (1001) docker     (121)     4504 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/logo/ms-icon-144x144.png
--rw-r--r--   0 runner    (1001) docker     (121)     4743 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/logo/ms-icon-150x150.png
--rw-r--r--   0 runner    (1001) docker     (121)    12342 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/logo/ms-icon-310x310.png
--rw-r--r--   0 runner    (1001) docker     (121)     2005 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/logo/ms-icon-70x70.png
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-20 18:05:46.500831 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-20 18:05:46.520831 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/css/
--rw-r--r--   0 runner    (1001) docker     (121)     5632 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/css/main.fcbcb80f.css
--rw-r--r--   0 runner    (1001) docker     (121)     8287 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/css/main.fcbcb80f.css.map
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-20 18:05:46.524831 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/js/
--rw-r--r--   0 runner    (1001) docker     (121)    20055 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/js/183.b8accd6c.chunk.js
--rw-r--r--   0 runner    (1001) docker     (121)    14053 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/js/276.fcb4db01.chunk.js
--rw-r--r--   0 runner    (1001) docker     (121)    11803 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/js/357.5328e62e.chunk.js
--rw-r--r--   0 runner    (1001) docker     (121)     4613 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/js/787.20f148af.chunk.js
--rw-r--r--   0 runner    (1001) docker     (121)     2096 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/js/836.945208d8.chunk.js
--rw-r--r--   0 runner    (1001) docker     (121)   104944 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/js/903.4ec9ff75.chunk.js
--rw-r--r--   0 runner    (1001) docker     (121)      336 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/js/903.4ec9ff75.chunk.js.LICENSE.txt
--rw-r--r--   0 runner    (1001) docker     (121)    12434 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/js/906.9eefb2c7.chunk.js
--rw-r--r--   0 runner    (1001) docker     (121)     2935 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/js/914.035c9fb2.chunk.js
--rw-r--r--   0 runner    (1001) docker     (121)    27742 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/js/982.4539617f.chunk.js
--rw-r--r--   0 runner    (1001) docker     (121)  1191712 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/js/main.a918e51a.js
--rw-r--r--   0 runner    (1001) docker     (121)     1781 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/js/main.a918e51a.js.LICENSE.txt
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-20 18:05:46.532831 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/
--rw-r--r--   0 runner    (1001) docker     (121)    32632 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-Black.ab57b908749eb205e3ad.woff
--rw-r--r--   0 runner    (1001) docker     (121)    24116 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-Black.cadfd7434852779eb395.woff2
--rw-r--r--   0 runner    (1001) docker     (121)    25732 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-BlackItalic.9bb4dd54e5afbea2e0ac.woff2
--rw-r--r--   0 runner    (1001) docker     (121)    34940 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-BlackItalic.f0098e273d2a3758b89c.woff
--rw-r--r--   0 runner    (1001) docker     (121)    33900 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-Bold.1577ca92013647c816b5.woff
--rw-r--r--   0 runner    (1001) docker     (121)    25152 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-Bold.f57c31edca48068386d7.woff2
--rw-r--r--   0 runner    (1001) docker     (121)    36168 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-BoldItalic.52e97aac5945285c9933.woff
--rw-r--r--   0 runner    (1001) docker     (121)    26684 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-BoldItalic.5b7f79817b551400186a.woff2
--rw-r--r--   0 runner    (1001) docker     (121)    33960 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-ExtraBold.0321ea88d696270daf4b.woff
--rw-r--r--   0 runner    (1001) docker     (121)    25220 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-ExtraBold.a611efd96602ca47acd9.woff2
--rw-r--r--   0 runner    (1001) docker     (121)    26736 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-ExtraBoldItalic.43f46f665391ff324c72.woff2
--rw-r--r--   0 runner    (1001) docker     (121)    36220 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-ExtraBoldItalic.dc0b36ae1c1bdac232e7.woff
--rw-r--r--   0 runner    (1001) docker     (121)    33248 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-ExtraLight.4e029f034c7e7263df9a.woff
--rw-r--r--   0 runner    (1001) docker     (121)    24852 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-ExtraLight.bafff4ae7f2a3395aa13.woff2
--rw-r--r--   0 runner    (1001) docker     (121)    26648 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-ExtraLightItalic.124644177779db0a8867.woff2
--rw-r--r--   0 runner    (1001) docker     (121)    35756 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-ExtraLightItalic.ff3def84a34422de5487.woff
--rw-r--r--   0 runner    (1001) docker     (121)    25872 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-Italic.9736c3faff86c01270b2.woff2
--rw-r--r--   0 runner    (1001) docker     (121)    34924 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-Italic.ce6bab8bc932d6080ec1.woff
--rw-r--r--   0 runner    (1001) docker     (121)    33248 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-Light.919d6ffdd987dc2e4717.woff
--rw-r--r--   0 runner    (1001) docker     (121)    24764 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-Light.aafd1643606ee83ad4cb.woff2
--rw-r--r--   0 runner    (1001) docker     (121)    26696 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-LightItalic.7f7cde8e1548e11231fb.woff2
--rw-r--r--   0 runner    (1001) docker     (121)    35788 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-LightItalic.e66e7a760a286c694d2b.woff
--rw-r--r--   0 runner    (1001) docker     (121)    33884 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-Medium.5a92f7b05463ecd61f45.woff
--rw-r--r--   0 runner    (1001) docker     (121)    25132 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-Medium.a6ca36dde32b3a1d0fd4.woff2
--rw-r--r--   0 runner    (1001) docker     (121)    26824 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-MediumItalic.dbc1ed152c7b11f501a3.woff2
--rw-r--r--   0 runner    (1001) docker     (121)    36236 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-MediumItalic.e3618413f59e00041fb3.woff
--rw-r--r--   0 runner    (1001) docker     (121)    23980 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-Regular.222064f2a764069868f4.woff2
--rw-r--r--   0 runner    (1001) docker     (121)    32236 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-Regular.67a27362108220436ffb.woff
--rw-r--r--   0 runner    (1001) docker     (121)    25240 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-SemiBold.599ce7634f46c5024ad0.woff2
--rw-r--r--   0 runner    (1001) docker     (121)    33944 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-SemiBold.c2e7341dd6ac6502be69.woff
--rw-r--r--   0 runner    (1001) docker     (121)    26892 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-SemiBoldItalic.09bc481607bd529abda7.woff2
--rw-r--r--   0 runner    (1001) docker     (121)    36280 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-SemiBoldItalic.43f7c276720845c6bb59.woff
--rw-r--r--   0 runner    (1001) docker     (121)    23636 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-Thin.92cada3d91581eb5112d.woff2
--rw-r--r--   0 runner    (1001) docker     (121)    32084 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-Thin.df0b1bcf558ccd5b48a2.woff
--rw-r--r--   0 runner    (1001) docker     (121)    34704 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-ThinItalic.78bf87d2ea41ac4365c1.woff
--rw-r--r--   0 runner    (1001) docker     (121)    25664 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-ThinItalic.82dd2dc2fb674d8273e4.woff2
--rw-r--r--   0 runner    (1001) docker     (121)    58892 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-italic.var.28904cc0eac675e1d19e.woff2
--rw-r--r--   0 runner    (1001) docker     (121)    53832 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-roman.var.f05060926bf5023f9930.woff2
--rw-r--r--   0 runner    (1001) docker     (121)    78400 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter.var.c3f97a25f56b5b416e49.woff2
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-20 18:05:46.532831 piperider-nightly-0.9.0.20220920/piperider_cli/datasource/
--rw-r--r--   0 runner    (1001) docker     (121)     7654 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/datasource/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     9549 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/datasource/bigquery.py
--rw-r--r--   0 runner    (1001) docker     (121)     7658 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/datasource/duckdb.py
--rw-r--r--   0 runner    (1001) docker     (121)     6898 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/datasource/field.py
--rw-r--r--   0 runner    (1001) docker     (121)     1542 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/datasource/postgres.py
--rw-r--r--   0 runner    (1001) docker     (121)     6824 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/datasource/redshift.py
--rw-r--r--   0 runner    (1001) docker     (121)     2293 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/datasource/snowflake.py
--rw-r--r--   0 runner    (1001) docker     (121)     1421 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/datasource/sqlite.py
--rw-r--r--   0 runner    (1001) docker     (121)     1618 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/datasource/survey.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-20 18:05:46.532831 piperider-nightly-0.9.0.20220920/piperider_cli/docgen/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/docgen/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2810 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/docgen/__main__.py
--rw-r--r--   0 runner    (1001) docker     (121)     6966 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/error.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-20 18:05:46.532831 piperider-nightly-0.9.0.20220920/piperider_cli/event/
--rw-r--r--   0 runner    (1001) docker     (121)     3578 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/event/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     4762 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/event/collector.py
--rw-r--r--   0 runner    (1001) docker     (121)     2851 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/event/track.py
--rw-r--r--   0 runner    (1001) docker     (121)     2153 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/feedback.py
--rw-r--r--   0 runner    (1001) docker     (121)     1449 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/filesystem.py
--rw-r--r--   0 runner    (1001) docker     (121)     4735 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/generate_report.py
--rw-r--r--   0 runner    (1001) docker     (121)     2609 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/guide.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-20 18:05:46.532831 piperider-nightly-0.9.0.20220920/piperider_cli/hack/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/hack/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      863 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/hack/datasource_inquirer_prompt.py
--rw-r--r--   0 runner    (1001) docker     (121)     3744 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/hack/inquirer.py
--rw-r--r--   0 runner    (1001) docker     (121)     3927 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/initializer.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-20 18:05:46.532831 piperider-nightly-0.9.0.20220920/piperider_cli/profiler/
--rw-r--r--   0 runner    (1001) docker     (121)      100 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/profiler/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2395 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/profiler/event.py
--rw-r--r--   0 runner    (1001) docker     (121)    46473 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/profiler/profiler.py
--rw-r--r--   0 runner    (1001) docker     (121)    14500 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/profiler/schema.json
--rw-r--r--   0 runner    (1001) docker     (121)      349 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/profiler/version.py
--rw-r--r--   0 runner    (1001) docker     (121)    25292 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/runner.py
--rw-r--r--   0 runner    (1001) docker     (121)     7341 2022-09-20 18:05:14.000000 piperider-nightly-0.9.0.20220920/piperider_cli/validator.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-20 18:05:46.532831 piperider-nightly-0.9.0.20220920/piperider_nightly.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)     8714 2022-09-20 18:05:46.000000 piperider-nightly-0.9.0.20220920/piperider_nightly.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)    16569 2022-09-20 18:05:46.000000 piperider-nightly-0.9.0.20220920/piperider_nightly.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-09-20 18:05:46.000000 piperider-nightly-0.9.0.20220920/piperider_nightly.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)       52 2022-09-20 18:05:46.000000 piperider-nightly-0.9.0.20220920/piperider_nightly.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (121)      634 2022-09-20 18:05:46.000000 piperider-nightly-0.9.0.20220920/piperider_nightly.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)       14 2022-09-20 18:05:46.000000 piperider-nightly-0.9.0.20220920/piperider_nightly.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (121)       38 2022-09-20 18:05:46.536831 piperider-nightly-0.9.0.20220920/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)     2769 2022-09-20 18:05:24.000000 piperider-nightly-0.9.0.20220920/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-21 18:05:36.184953 piperider-nightly-0.9.0.20220921/
+-rw-r--r--   0 runner    (1001) docker     (121)    11357 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (121)     9057 2022-09-21 18:05:36.184953 piperider-nightly-0.9.0.20220921/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)     8210 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/README.md
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-21 18:05:36.156953 piperider-nightly-0.9.0.20220921/piperider_cli/
+-rw-r--r--   0 runner    (1001) docker     (121)       75 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/SENTRY_DNS
+-rw-r--r--   0 runner    (1001) docker     (121)       15 2022-09-21 18:05:19.000000 piperider-nightly-0.9.0.20220921/piperider_cli/VERSION
+-rw-r--r--   0 runner    (1001) docker     (121)     3771 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)       59 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/__main__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-21 18:05:36.160953 piperider-nightly-0.9.0.20220921/piperider_cli/adapter/
+-rw-r--r--   0 runner    (1001) docker     (121)       48 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/adapter/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11325 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/adapter/dbt_adapter.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-21 18:05:36.160953 piperider-nightly-0.9.0.20220921/piperider_cli/assertion_engine/
+-rw-r--r--   0 runner    (1001) docker     (121)       92 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/assertion_engine/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    24636 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/assertion_engine/assertion.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-21 18:05:36.160953 piperider-nightly-0.9.0.20220921/piperider_cli/assertion_engine/recommended_rules/
+-rw-r--r--   0 runner    (1001) docker     (121)      103 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/assertion_engine/recommended_rules/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      500 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/assertion_engine/recommended_rules/recommender_assertion.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4458 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/assertion_engine/recommended_rules/table_assertions.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4531 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/assertion_engine/recommender.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-21 18:05:36.160953 piperider-nightly-0.9.0.20220921/piperider_cli/assertion_engine/types/
+-rw-r--r--   0 runner    (1001) docker     (121)     2500 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/assertion_engine/types/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4567 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/assertion_engine/types/assert_column_misc.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5430 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/assertion_engine/types/assert_column_ranges.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4936 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/assertion_engine/types/assert_column_types.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4110 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/assertion_engine/types/assert_rows.py
+-rw-r--r--   0 runner    (1001) docker     (121)      586 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/assertion_engine/types/base.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3315 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/assertion_generator.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10924 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/cli.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-21 18:05:36.160953 piperider-nightly-0.9.0.20220921/piperider_cli/cloud/
+-rw-r--r--   0 runner    (1001) docker     (121)     4192 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/cloud/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3486 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/cloud_connector.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10957 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/compare_report.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12644 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/configuration.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-21 18:05:36.160953 piperider-nightly-0.9.0.20220921/piperider_cli/data/
+-rw-r--r--   0 runner    (1001) docker     (121)       41 2022-09-21 18:05:19.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/COMMIT
+-rw-r--r--   0 runner    (1001) docker     (121)       48 2022-09-21 18:05:19.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/CONFIG
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-21 18:05:36.160953 piperider-nightly-0.9.0.20220921/piperider_cli/data/piperider-init-template/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-21 18:05:36.160953 piperider-nightly-0.9.0.20220921/piperider_cli/data/piperider-init-template/assertions/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/piperider-init-template/assertions/placeholder.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/piperider-init-template/config.yml
+-rw-r--r--   0 runner    (1001) docker     (121)       92 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/piperider-init-template/gitignore
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-21 18:05:36.160953 piperider-nightly-0.9.0.20220921/piperider_cli/data/piperider-init-template/plugins/
+-rw-r--r--   0 runner    (1001) docker     (121)     3048 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/piperider-init-template/plugins/customized_assertions.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-21 18:05:36.156953 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-21 18:05:36.160953 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-21 18:05:36.160953 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/Discord/
+-rw-r--r--   0 runner    (1001) docker     (121)     2094 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/Discord/Discord-Logo.svg
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-21 18:05:36.160953 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/GitHub/
+-rw-r--r--   0 runner    (1001) docker     (121)     6215 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/GitHub/GitHub-Logo.svg
+-rw-r--r--   0 runner    (1001) docker     (121)     5972 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/asset-manifest.json
+-rw-r--r--   0 runner    (1001) docker     (121)     1676 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/index.html
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-21 18:05:36.164953 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/logo/
+-rw-r--r--   0 runner    (1001) docker     (121)     4504 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/logo/android-icon-144x144.png
+-rw-r--r--   0 runner    (1001) docker     (121)     5132 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/logo/android-icon-192x192.png
+-rw-r--r--   0 runner    (1001) docker     (121)     1393 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/logo/android-icon-36x36.png
+-rw-r--r--   0 runner    (1001) docker     (121)     1737 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/logo/android-icon-48x48.png
+-rw-r--r--   0 runner    (1001) docker     (121)     2003 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/logo/android-icon-72x72.png
+-rw-r--r--   0 runner    (1001) docker     (121)     2491 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/logo/android-icon-96x96.png
+-rw-r--r--   0 runner    (1001) docker     (121)     3530 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/logo/apple-icon-114x114.png
+-rw-r--r--   0 runner    (1001) docker     (121)     3647 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/logo/apple-icon-120x120.png
+-rw-r--r--   0 runner    (1001) docker     (121)     4504 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/logo/apple-icon-144x144.png
+-rw-r--r--   0 runner    (1001) docker     (121)     4819 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/logo/apple-icon-152x152.png
+-rw-r--r--   0 runner    (1001) docker     (121)     5783 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/logo/apple-icon-180x180.png
+-rw-r--r--   0 runner    (1001) docker     (121)     1763 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/logo/apple-icon-57x57.png
+-rw-r--r--   0 runner    (1001) docker     (121)     1876 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/logo/apple-icon-60x60.png
+-rw-r--r--   0 runner    (1001) docker     (121)     2003 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/logo/apple-icon-72x72.png
+-rw-r--r--   0 runner    (1001) docker     (121)     2096 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/logo/apple-icon-76x76.png
+-rw-r--r--   0 runner    (1001) docker     (121)     5676 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/logo/apple-icon-precomposed.png
+-rw-r--r--   0 runner    (1001) docker     (121)     5676 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/logo/apple-icon.png
+-rw-r--r--   0 runner    (1001) docker     (121)      281 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/logo/browserconfig.xml
+-rw-r--r--   0 runner    (1001) docker     (121)      975 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/logo/favicon-16x16.png
+-rw-r--r--   0 runner    (1001) docker     (121)     1372 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/logo/favicon-32x32.png
+-rw-r--r--   0 runner    (1001) docker     (121)     2491 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/logo/favicon-96x96.png
+-rw-r--r--   0 runner    (1001) docker     (121)     1150 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/logo/favicon.ico
+-rw-r--r--   0 runner    (1001) docker     (121)     7789 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/logo/logo.svg
+-rw-r--r--   0 runner    (1001) docker     (121)      720 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/logo/manifest.json
+-rw-r--r--   0 runner    (1001) docker     (121)     4504 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/logo/ms-icon-144x144.png
+-rw-r--r--   0 runner    (1001) docker     (121)     4743 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/logo/ms-icon-150x150.png
+-rw-r--r--   0 runner    (1001) docker     (121)    12342 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/logo/ms-icon-310x310.png
+-rw-r--r--   0 runner    (1001) docker     (121)     2005 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/logo/ms-icon-70x70.png
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-21 18:05:36.156953 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-21 18:05:36.164953 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/css/
+-rw-r--r--   0 runner    (1001) docker     (121)     5632 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/css/main.fcbcb80f.css
+-rw-r--r--   0 runner    (1001) docker     (121)     8287 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/css/main.fcbcb80f.css.map
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-21 18:05:36.164953 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/js/
+-rw-r--r--   0 runner    (1001) docker     (121)    20055 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/js/183.b8accd6c.chunk.js
+-rw-r--r--   0 runner    (1001) docker     (121)    14053 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/js/276.fcb4db01.chunk.js
+-rw-r--r--   0 runner    (1001) docker     (121)    11803 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/js/357.5328e62e.chunk.js
+-rw-r--r--   0 runner    (1001) docker     (121)     4613 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/js/787.20f148af.chunk.js
+-rw-r--r--   0 runner    (1001) docker     (121)     2096 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/js/836.945208d8.chunk.js
+-rw-r--r--   0 runner    (1001) docker     (121)   104944 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/js/903.4ec9ff75.chunk.js
+-rw-r--r--   0 runner    (1001) docker     (121)      336 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/js/903.4ec9ff75.chunk.js.LICENSE.txt
+-rw-r--r--   0 runner    (1001) docker     (121)    12434 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/js/906.9eefb2c7.chunk.js
+-rw-r--r--   0 runner    (1001) docker     (121)     2935 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/js/914.035c9fb2.chunk.js
+-rw-r--r--   0 runner    (1001) docker     (121)    27742 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/js/982.4539617f.chunk.js
+-rw-r--r--   0 runner    (1001) docker     (121)  1199840 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/js/main.3dd694e2.js
+-rw-r--r--   0 runner    (1001) docker     (121)     1781 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/js/main.3dd694e2.js.LICENSE.txt
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-21 18:05:36.168953 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/
+-rw-r--r--   0 runner    (1001) docker     (121)    32632 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-Black.ab57b908749eb205e3ad.woff
+-rw-r--r--   0 runner    (1001) docker     (121)    24116 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-Black.cadfd7434852779eb395.woff2
+-rw-r--r--   0 runner    (1001) docker     (121)    25732 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-BlackItalic.9bb4dd54e5afbea2e0ac.woff2
+-rw-r--r--   0 runner    (1001) docker     (121)    34940 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-BlackItalic.f0098e273d2a3758b89c.woff
+-rw-r--r--   0 runner    (1001) docker     (121)    33900 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-Bold.1577ca92013647c816b5.woff
+-rw-r--r--   0 runner    (1001) docker     (121)    25152 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-Bold.f57c31edca48068386d7.woff2
+-rw-r--r--   0 runner    (1001) docker     (121)    36168 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-BoldItalic.52e97aac5945285c9933.woff
+-rw-r--r--   0 runner    (1001) docker     (121)    26684 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-BoldItalic.5b7f79817b551400186a.woff2
+-rw-r--r--   0 runner    (1001) docker     (121)    33960 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-ExtraBold.0321ea88d696270daf4b.woff
+-rw-r--r--   0 runner    (1001) docker     (121)    25220 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-ExtraBold.a611efd96602ca47acd9.woff2
+-rw-r--r--   0 runner    (1001) docker     (121)    26736 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-ExtraBoldItalic.43f46f665391ff324c72.woff2
+-rw-r--r--   0 runner    (1001) docker     (121)    36220 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-ExtraBoldItalic.dc0b36ae1c1bdac232e7.woff
+-rw-r--r--   0 runner    (1001) docker     (121)    33248 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-ExtraLight.4e029f034c7e7263df9a.woff
+-rw-r--r--   0 runner    (1001) docker     (121)    24852 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-ExtraLight.bafff4ae7f2a3395aa13.woff2
+-rw-r--r--   0 runner    (1001) docker     (121)    26648 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-ExtraLightItalic.124644177779db0a8867.woff2
+-rw-r--r--   0 runner    (1001) docker     (121)    35756 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-ExtraLightItalic.ff3def84a34422de5487.woff
+-rw-r--r--   0 runner    (1001) docker     (121)    25872 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-Italic.9736c3faff86c01270b2.woff2
+-rw-r--r--   0 runner    (1001) docker     (121)    34924 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-Italic.ce6bab8bc932d6080ec1.woff
+-rw-r--r--   0 runner    (1001) docker     (121)    33248 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-Light.919d6ffdd987dc2e4717.woff
+-rw-r--r--   0 runner    (1001) docker     (121)    24764 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-Light.aafd1643606ee83ad4cb.woff2
+-rw-r--r--   0 runner    (1001) docker     (121)    26696 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-LightItalic.7f7cde8e1548e11231fb.woff2
+-rw-r--r--   0 runner    (1001) docker     (121)    35788 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-LightItalic.e66e7a760a286c694d2b.woff
+-rw-r--r--   0 runner    (1001) docker     (121)    33884 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-Medium.5a92f7b05463ecd61f45.woff
+-rw-r--r--   0 runner    (1001) docker     (121)    25132 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-Medium.a6ca36dde32b3a1d0fd4.woff2
+-rw-r--r--   0 runner    (1001) docker     (121)    26824 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-MediumItalic.dbc1ed152c7b11f501a3.woff2
+-rw-r--r--   0 runner    (1001) docker     (121)    36236 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-MediumItalic.e3618413f59e00041fb3.woff
+-rw-r--r--   0 runner    (1001) docker     (121)    23980 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-Regular.222064f2a764069868f4.woff2
+-rw-r--r--   0 runner    (1001) docker     (121)    32236 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-Regular.67a27362108220436ffb.woff
+-rw-r--r--   0 runner    (1001) docker     (121)    25240 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-SemiBold.599ce7634f46c5024ad0.woff2
+-rw-r--r--   0 runner    (1001) docker     (121)    33944 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-SemiBold.c2e7341dd6ac6502be69.woff
+-rw-r--r--   0 runner    (1001) docker     (121)    26892 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-SemiBoldItalic.09bc481607bd529abda7.woff2
+-rw-r--r--   0 runner    (1001) docker     (121)    36280 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-SemiBoldItalic.43f7c276720845c6bb59.woff
+-rw-r--r--   0 runner    (1001) docker     (121)    23636 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-Thin.92cada3d91581eb5112d.woff2
+-rw-r--r--   0 runner    (1001) docker     (121)    32084 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-Thin.df0b1bcf558ccd5b48a2.woff
+-rw-r--r--   0 runner    (1001) docker     (121)    34704 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-ThinItalic.78bf87d2ea41ac4365c1.woff
+-rw-r--r--   0 runner    (1001) docker     (121)    25664 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-ThinItalic.82dd2dc2fb674d8273e4.woff2
+-rw-r--r--   0 runner    (1001) docker     (121)    58892 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-italic.var.28904cc0eac675e1d19e.woff2
+-rw-r--r--   0 runner    (1001) docker     (121)    53832 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-roman.var.f05060926bf5023f9930.woff2
+-rw-r--r--   0 runner    (1001) docker     (121)    78400 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter.var.c3f97a25f56b5b416e49.woff2
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-21 18:05:36.168953 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-21 18:05:36.168953 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/Discord/
+-rw-r--r--   0 runner    (1001) docker     (121)     2094 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/Discord/Discord-Logo.svg
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-21 18:05:36.168953 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/GitHub/
+-rw-r--r--   0 runner    (1001) docker     (121)     6215 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/GitHub/GitHub-Logo.svg
+-rw-r--r--   0 runner    (1001) docker     (121)     5972 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/asset-manifest.json
+-rw-r--r--   0 runner    (1001) docker     (121)     1676 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/index.html
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-21 18:05:36.172953 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/logo/
+-rw-r--r--   0 runner    (1001) docker     (121)     4504 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/logo/android-icon-144x144.png
+-rw-r--r--   0 runner    (1001) docker     (121)     5132 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/logo/android-icon-192x192.png
+-rw-r--r--   0 runner    (1001) docker     (121)     1393 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/logo/android-icon-36x36.png
+-rw-r--r--   0 runner    (1001) docker     (121)     1737 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/logo/android-icon-48x48.png
+-rw-r--r--   0 runner    (1001) docker     (121)     2003 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/logo/android-icon-72x72.png
+-rw-r--r--   0 runner    (1001) docker     (121)     2491 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/logo/android-icon-96x96.png
+-rw-r--r--   0 runner    (1001) docker     (121)     3530 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/logo/apple-icon-114x114.png
+-rw-r--r--   0 runner    (1001) docker     (121)     3647 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/logo/apple-icon-120x120.png
+-rw-r--r--   0 runner    (1001) docker     (121)     4504 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/logo/apple-icon-144x144.png
+-rw-r--r--   0 runner    (1001) docker     (121)     4819 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/logo/apple-icon-152x152.png
+-rw-r--r--   0 runner    (1001) docker     (121)     5783 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/logo/apple-icon-180x180.png
+-rw-r--r--   0 runner    (1001) docker     (121)     1763 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/logo/apple-icon-57x57.png
+-rw-r--r--   0 runner    (1001) docker     (121)     1876 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/logo/apple-icon-60x60.png
+-rw-r--r--   0 runner    (1001) docker     (121)     2003 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/logo/apple-icon-72x72.png
+-rw-r--r--   0 runner    (1001) docker     (121)     2096 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/logo/apple-icon-76x76.png
+-rw-r--r--   0 runner    (1001) docker     (121)     5676 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/logo/apple-icon-precomposed.png
+-rw-r--r--   0 runner    (1001) docker     (121)     5676 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/logo/apple-icon.png
+-rw-r--r--   0 runner    (1001) docker     (121)      281 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/logo/browserconfig.xml
+-rw-r--r--   0 runner    (1001) docker     (121)      975 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/logo/favicon-16x16.png
+-rw-r--r--   0 runner    (1001) docker     (121)     1372 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/logo/favicon-32x32.png
+-rw-r--r--   0 runner    (1001) docker     (121)     2491 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/logo/favicon-96x96.png
+-rw-r--r--   0 runner    (1001) docker     (121)     1150 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/logo/favicon.ico
+-rw-r--r--   0 runner    (1001) docker     (121)     7789 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/logo/logo.svg
+-rw-r--r--   0 runner    (1001) docker     (121)      720 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/logo/manifest.json
+-rw-r--r--   0 runner    (1001) docker     (121)     4504 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/logo/ms-icon-144x144.png
+-rw-r--r--   0 runner    (1001) docker     (121)     4743 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/logo/ms-icon-150x150.png
+-rw-r--r--   0 runner    (1001) docker     (121)    12342 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/logo/ms-icon-310x310.png
+-rw-r--r--   0 runner    (1001) docker     (121)     2005 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/logo/ms-icon-70x70.png
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-21 18:05:36.156953 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-21 18:05:36.172953 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/css/
+-rw-r--r--   0 runner    (1001) docker     (121)     5632 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/css/main.fcbcb80f.css
+-rw-r--r--   0 runner    (1001) docker     (121)     8287 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/css/main.fcbcb80f.css.map
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-21 18:05:36.176953 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/js/
+-rw-r--r--   0 runner    (1001) docker     (121)    20055 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/js/183.b8accd6c.chunk.js
+-rw-r--r--   0 runner    (1001) docker     (121)    14053 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/js/276.fcb4db01.chunk.js
+-rw-r--r--   0 runner    (1001) docker     (121)    11803 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/js/357.5328e62e.chunk.js
+-rw-r--r--   0 runner    (1001) docker     (121)     4613 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/js/787.20f148af.chunk.js
+-rw-r--r--   0 runner    (1001) docker     (121)     2096 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/js/836.945208d8.chunk.js
+-rw-r--r--   0 runner    (1001) docker     (121)   104944 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/js/903.4ec9ff75.chunk.js
+-rw-r--r--   0 runner    (1001) docker     (121)      336 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/js/903.4ec9ff75.chunk.js.LICENSE.txt
+-rw-r--r--   0 runner    (1001) docker     (121)    12434 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/js/906.9eefb2c7.chunk.js
+-rw-r--r--   0 runner    (1001) docker     (121)     2935 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/js/914.035c9fb2.chunk.js
+-rw-r--r--   0 runner    (1001) docker     (121)    27742 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/js/982.4539617f.chunk.js
+-rw-r--r--   0 runner    (1001) docker     (121)  1191712 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/js/main.a918e51a.js
+-rw-r--r--   0 runner    (1001) docker     (121)     1781 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/js/main.a918e51a.js.LICENSE.txt
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-21 18:05:36.180953 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/
+-rw-r--r--   0 runner    (1001) docker     (121)    32632 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-Black.ab57b908749eb205e3ad.woff
+-rw-r--r--   0 runner    (1001) docker     (121)    24116 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-Black.cadfd7434852779eb395.woff2
+-rw-r--r--   0 runner    (1001) docker     (121)    25732 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-BlackItalic.9bb4dd54e5afbea2e0ac.woff2
+-rw-r--r--   0 runner    (1001) docker     (121)    34940 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-BlackItalic.f0098e273d2a3758b89c.woff
+-rw-r--r--   0 runner    (1001) docker     (121)    33900 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-Bold.1577ca92013647c816b5.woff
+-rw-r--r--   0 runner    (1001) docker     (121)    25152 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-Bold.f57c31edca48068386d7.woff2
+-rw-r--r--   0 runner    (1001) docker     (121)    36168 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-BoldItalic.52e97aac5945285c9933.woff
+-rw-r--r--   0 runner    (1001) docker     (121)    26684 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-BoldItalic.5b7f79817b551400186a.woff2
+-rw-r--r--   0 runner    (1001) docker     (121)    33960 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-ExtraBold.0321ea88d696270daf4b.woff
+-rw-r--r--   0 runner    (1001) docker     (121)    25220 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-ExtraBold.a611efd96602ca47acd9.woff2
+-rw-r--r--   0 runner    (1001) docker     (121)    26736 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-ExtraBoldItalic.43f46f665391ff324c72.woff2
+-rw-r--r--   0 runner    (1001) docker     (121)    36220 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-ExtraBoldItalic.dc0b36ae1c1bdac232e7.woff
+-rw-r--r--   0 runner    (1001) docker     (121)    33248 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-ExtraLight.4e029f034c7e7263df9a.woff
+-rw-r--r--   0 runner    (1001) docker     (121)    24852 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-ExtraLight.bafff4ae7f2a3395aa13.woff2
+-rw-r--r--   0 runner    (1001) docker     (121)    26648 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-ExtraLightItalic.124644177779db0a8867.woff2
+-rw-r--r--   0 runner    (1001) docker     (121)    35756 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-ExtraLightItalic.ff3def84a34422de5487.woff
+-rw-r--r--   0 runner    (1001) docker     (121)    25872 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-Italic.9736c3faff86c01270b2.woff2
+-rw-r--r--   0 runner    (1001) docker     (121)    34924 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-Italic.ce6bab8bc932d6080ec1.woff
+-rw-r--r--   0 runner    (1001) docker     (121)    33248 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-Light.919d6ffdd987dc2e4717.woff
+-rw-r--r--   0 runner    (1001) docker     (121)    24764 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-Light.aafd1643606ee83ad4cb.woff2
+-rw-r--r--   0 runner    (1001) docker     (121)    26696 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-LightItalic.7f7cde8e1548e11231fb.woff2
+-rw-r--r--   0 runner    (1001) docker     (121)    35788 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-LightItalic.e66e7a760a286c694d2b.woff
+-rw-r--r--   0 runner    (1001) docker     (121)    33884 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-Medium.5a92f7b05463ecd61f45.woff
+-rw-r--r--   0 runner    (1001) docker     (121)    25132 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-Medium.a6ca36dde32b3a1d0fd4.woff2
+-rw-r--r--   0 runner    (1001) docker     (121)    26824 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-MediumItalic.dbc1ed152c7b11f501a3.woff2
+-rw-r--r--   0 runner    (1001) docker     (121)    36236 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-MediumItalic.e3618413f59e00041fb3.woff
+-rw-r--r--   0 runner    (1001) docker     (121)    23980 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-Regular.222064f2a764069868f4.woff2
+-rw-r--r--   0 runner    (1001) docker     (121)    32236 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-Regular.67a27362108220436ffb.woff
+-rw-r--r--   0 runner    (1001) docker     (121)    25240 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-SemiBold.599ce7634f46c5024ad0.woff2
+-rw-r--r--   0 runner    (1001) docker     (121)    33944 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-SemiBold.c2e7341dd6ac6502be69.woff
+-rw-r--r--   0 runner    (1001) docker     (121)    26892 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-SemiBoldItalic.09bc481607bd529abda7.woff2
+-rw-r--r--   0 runner    (1001) docker     (121)    36280 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-SemiBoldItalic.43f7c276720845c6bb59.woff
+-rw-r--r--   0 runner    (1001) docker     (121)    23636 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-Thin.92cada3d91581eb5112d.woff2
+-rw-r--r--   0 runner    (1001) docker     (121)    32084 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-Thin.df0b1bcf558ccd5b48a2.woff
+-rw-r--r--   0 runner    (1001) docker     (121)    34704 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-ThinItalic.78bf87d2ea41ac4365c1.woff
+-rw-r--r--   0 runner    (1001) docker     (121)    25664 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-ThinItalic.82dd2dc2fb674d8273e4.woff2
+-rw-r--r--   0 runner    (1001) docker     (121)    58892 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-italic.var.28904cc0eac675e1d19e.woff2
+-rw-r--r--   0 runner    (1001) docker     (121)    53832 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-roman.var.f05060926bf5023f9930.woff2
+-rw-r--r--   0 runner    (1001) docker     (121)    78400 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter.var.c3f97a25f56b5b416e49.woff2
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-21 18:05:36.180953 piperider-nightly-0.9.0.20220921/piperider_cli/datasource/
+-rw-r--r--   0 runner    (1001) docker     (121)     7654 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/datasource/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9549 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/datasource/bigquery.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7658 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/datasource/duckdb.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6898 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/datasource/field.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1542 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/datasource/postgres.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6824 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/datasource/redshift.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2293 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/datasource/snowflake.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1421 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/datasource/sqlite.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1618 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/datasource/survey.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-21 18:05:36.180953 piperider-nightly-0.9.0.20220921/piperider_cli/docgen/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/docgen/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2810 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/docgen/__main__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6966 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/error.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-21 18:05:36.180953 piperider-nightly-0.9.0.20220921/piperider_cli/event/
+-rw-r--r--   0 runner    (1001) docker     (121)     3578 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/event/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4762 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/event/collector.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2851 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/event/track.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2153 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/feedback.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1449 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/filesystem.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4735 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/generate_report.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2609 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/guide.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-21 18:05:36.180953 piperider-nightly-0.9.0.20220921/piperider_cli/hack/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/hack/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      863 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/hack/datasource_inquirer_prompt.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3744 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/hack/inquirer.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3927 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/initializer.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-21 18:05:36.180953 piperider-nightly-0.9.0.20220921/piperider_cli/profiler/
+-rw-r--r--   0 runner    (1001) docker     (121)      100 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/profiler/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2395 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/profiler/event.py
+-rw-r--r--   0 runner    (1001) docker     (121)    46473 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/profiler/profiler.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14500 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/profiler/schema.json
+-rw-r--r--   0 runner    (1001) docker     (121)      349 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/profiler/version.py
+-rw-r--r--   0 runner    (1001) docker     (121)    25292 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/runner.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7341 2022-09-21 18:05:11.000000 piperider-nightly-0.9.0.20220921/piperider_cli/validator.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-09-21 18:05:36.180953 piperider-nightly-0.9.0.20220921/piperider_nightly.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (121)     9057 2022-09-21 18:05:36.000000 piperider-nightly-0.9.0.20220921/piperider_nightly.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)    16569 2022-09-21 18:05:36.000000 piperider-nightly-0.9.0.20220921/piperider_nightly.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-09-21 18:05:36.000000 piperider-nightly-0.9.0.20220921/piperider_nightly.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       52 2022-09-21 18:05:36.000000 piperider-nightly-0.9.0.20220921/piperider_nightly.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (121)      634 2022-09-21 18:05:36.000000 piperider-nightly-0.9.0.20220921/piperider_nightly.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       14 2022-09-21 18:05:36.000000 piperider-nightly-0.9.0.20220921/piperider_nightly.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       38 2022-09-21 18:05:36.184953 piperider-nightly-0.9.0.20220921/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (121)     2769 2022-09-21 18:05:19.000000 piperider-nightly-0.9.0.20220921/setup.py
```

### Comparing `piperider-nightly-0.9.0.20220920/LICENSE` & `piperider-nightly-0.9.0.20220921/LICENSE`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/PKG-INFO` & `piperider-nightly-0.9.0.20220921/PKG-INFO`

 * *Files 16% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: piperider-nightly
-Version: 0.9.0.20220920
+Version: 0.9.0.20220921
 Summary: PiperRider CLI
 Home-page: https://github.com/InfuseAI/piperider
 Author: InfuseAI Dev Team
 Author-email: dev@infuseai.io
 Project-URL: Bug Tracker, https://github.com/InfuseAI/piperider/issues
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
@@ -58,15 +58,15 @@
 
 
 
 ## Made for the modern data team
 **For data engineers**
 * :zap: 2 min install & set-up
 * :relieved: Non-intrusive & open-source: install and use locally
-* :money_with_wings: Fast & cheap: 10M rows, 8 columns takes only 16s to profile
+* :money_with_wings: Fast & cheap: 100M rows & 8 columns (or 50M & 16 columns) takes only 18s to profile
 * :ledger: Cloud DataWarehouse native & auto-config for dbt
 
 
 
 **For data analysts**
 * :bowtie: Never waste time on analyzing wrong data: collects various metadata metrics such as freshness, uniqueness, distribution... [check all metrics](https://docs.piperider.io/data-profile-and-metrics/metrics)
 * :speech_balloon: Communicate easily your data expectations by showing the report
@@ -93,30 +93,30 @@
 * [Get involved](#get-involved)
     * [Support](#support)
     * [Contributions](#contributions)
  -->
 
 
 ## Key features
-* [Generate an HTML Report](how-to-guides/generate-report.md) featuring your data profile and data assertion test results ([interactive sample](https://piperider-github-readme.s3.ap-northeast-1.amazonaws.com/run-0.8.0/index.html))
-* [Compare two reports](how-to-guides/compare-reports.md) to understand how your data has changed over time ([interactive sample](https://piperider-github-readme.s3.ap-northeast-1.amazonaws.com/comparison-0.8.0/index.html))
+* [Generate an HTML Report](https://docs.piperider.io/how-to-guides/generate-report) featuring your data profile and data assertion test results ([interactive sample](https://piperider-github-readme.s3.ap-northeast-1.amazonaws.com/run-0.8.0/index.html))
+* [Compare two reports](https://docs.piperider.io/how-to-guides/compare-reports) to understand how your data has changed over time ([interactive sample](https://piperider-github-readme.s3.ap-northeast-1.amazonaws.com/comparison-0.8.0/index.html))
 * Test your data with data assertions:
-  * Built-in [data assertions](data-quality-assertions/assertion-configuration.md)
-  * Extensible through [custom assertions](data-quality-assertions/custom-assertions.md)
+  * Built-in [data assertions](https://docs.piperider.io/data-quality-assertions/assertion-configuration)
+  * Extensible through [custom assertions](https://docs.piperider.io/data-quality-assertions/custom-assertions)
   * Auto-generated data assertions
-* Currently supports [Postgres](data-sources/postgres-connector.md), [Snowflake](data-sources/snowflake-connector.md), SQLite, [BigQuery](data-sources/bigquery-connector.md), [Redshift](data-sources/redshift-connector.md), [DuckDB](data-sources/duckdb-connector.md), [CSV](data-sources/csv-connector.md) and [Parquet](data-sources/parquet-connector.md).
-* Zero-config [support for dbt](dbt-integration/) projects
-* Automation through [GitHub Actions](how-to-guides/github-action.md), [save reports in S3](how-to-guides/aws-s3-+-github-ci.md)
+* Currently supports [Postgres](https://docs.piperider.io/data-sources/postgres-connector), [Snowflake](https://docs.piperider.io/data-sources/snowflake-connector), SQLite, [BigQuery](https://docs.piperider.io/data-sources/bigquery-connector), [Redshift](https://docs.piperider.io/data-sources/redshift-connector), [DuckDB](https://docs.piperider.io/data-sources/duckdb-connector/), [CSV](https://docs.piperider.io/data-sources/csv-connector/) and [Parquet](https://docs.piperider.io/data-sources/parquet-connector/).
+* Zero-config [support for dbt](https://docs.piperider.io/dbt-integration/) projects
+* Automation through [GitHub Actions](https://docs.piperider.io/how-to-guides/github-action/), [save reports in S3](https://docs.piperider.io/how-to-guides/aws-s3-+-github-ci/)
 
 
 
 
 # Getting started
 
-Get started quickly below, go to [the docs](https://dochttps://docs.piperider.io/), or check out this article on [how to add data observability using PipeRider ](https://blog.infuseai.io/adding-data-observability-and-alerts-to-your-data-pipeline-is-easier-than-you-think-4e005daca55b)
+Get started quickly below, go to [the docs](https://docs.piperider.io/), or check out this article on [how to add data observability using PipeRider ](https://blog.infuseai.io/adding-data-observability-and-alerts-to-your-data-pipeline-is-easier-than-you-think-4e005daca55b)
 
 ## Install PipeRider
 
 ```bash
 pip install piperider
 ```
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: piperider-nightly Version: 0.9.0.20220920 Summary:
+Metadata-Version: 2.1 Name: piperider-nightly Version: 0.9.0.20220921 Summary:
 PiperRider CLI Home-page: https://github.com/InfuseAI/piperider Author:
 InfuseAI Dev Team Author-email: dev@infuseai.io Project-URL: Bug Tracker,
 https://github.com/InfuseAI/piperider/issues Classifier: Programming Language
 :: Python :: 3.7 Classifier: Programming Language :: Python :: 3.8 Classifier:
 Programming Language :: Python :: 3.9 Classifier: License :: OSI Approved ::
 Apache Software License Classifier: Operating System :: OS Independent
 Classifier: Development Status :: 4 - Beta Requires-Python: >=3.7 Description-
@@ -33,44 +33,48 @@
 strategy PipeRider will make your life easier by: 1. Building a data profile so
 you can easily understand your data 2. Creating test suggestions based on the
 profiling 3. Comparing data profile reports, so you track changes over time
 [Read how to implement a data quality strategy using profiling + testing]
 (https://blog.infuseai.io/add-data-profiling-and-assertions-to-dbt-with-
 piperider-732ca0821e3a) ## Made for the modern data team **For data engineers**
 * :zap: 2 min install & set-up * :relieved: Non-intrusive & open-source:
-install and use locally * :money_with_wings: Fast & cheap: 10M rows, 8 columns
-takes only 16s to profile * :ledger: Cloud DataWarehouse native & auto-config
-for dbt **For data analysts** * :bowtie: Never waste time on analyzing wrong
-data: collects various metadata metrics such as freshness, uniqueness,
-distribution... [check all metrics](https://docs.piperider.io/data-profile-and-
-metrics/metrics) * :speech_balloon: Communicate easily your data expectations
-by showing the report * Zero-config dbt integration ## Live Demo [![](https://
-i.imgur.com/WuFC4H6.png)](https://piperider-github-readme.s3.ap-northeast-
-1.amazonaws.com/run-0.7.0/index.html) [Click here or on image to interact]
-(https://piperider-github-readme.s3.ap-northeast-1.amazonaws.com/run-0.7.0/
-index.html)  ## Key features * [Generate an HTML Report](how-to-guides/
-generate-report.md) featuring your data profile and data assertion test results
-([interactive sample](https://piperider-github-readme.s3.ap-northeast-
-1.amazonaws.com/run-0.8.0/index.html)) * [Compare two reports](how-to-guides/
-compare-reports.md) to understand how your data has changed over time (
-[interactive sample](https://piperider-github-readme.s3.ap-northeast-
-1.amazonaws.com/comparison-0.8.0/index.html)) * Test your data with data
-assertions: * Built-in [data assertions](data-quality-assertions/assertion-
-configuration.md) * Extensible through [custom assertions](data-quality-
-assertions/custom-assertions.md) * Auto-generated data assertions * Currently
-supports [Postgres](data-sources/postgres-connector.md), [Snowflake](data-
-sources/snowflake-connector.md), SQLite, [BigQuery](data-sources/bigquery-
-connector.md), [Redshift](data-sources/redshift-connector.md), [DuckDB](data-
-sources/duckdb-connector.md), [CSV](data-sources/csv-connector.md) and
-[Parquet](data-sources/parquet-connector.md). * Zero-config [support for dbt]
-(dbt-integration/) projects * Automation through [GitHub Actions](how-to-
-guides/github-action.md), [save reports in S3](how-to-guides/aws-s3-+-github-
-ci.md) # Getting started Get started quickly below, go to [the docs](https://
-dochttps://docs.piperider.io/), or check out this article on [how to add data
-observability using PipeRider ](https://blog.infuseai.io/adding-data-
+install and use locally * :money_with_wings: Fast & cheap: 100M rows & 8
+columns (or 50M & 16 columns) takes only 18s to profile * :ledger: Cloud
+DataWarehouse native & auto-config for dbt **For data analysts** * :bowtie:
+Never waste time on analyzing wrong data: collects various metadata metrics
+such as freshness, uniqueness, distribution... [check all metrics](https://
+docs.piperider.io/data-profile-and-metrics/metrics) * :speech_balloon:
+Communicate easily your data expectations by showing the report * Zero-config
+dbt integration ## Live Demo [![](https://i.imgur.com/WuFC4H6.png)](https://
+piperider-github-readme.s3.ap-northeast-1.amazonaws.com/run-0.7.0/index.html)
+[Click here or on image to interact](https://piperider-github-readme.s3.ap-
+northeast-1.amazonaws.com/run-0.7.0/index.html)  ## Key features * [Generate an
+HTML Report](https://docs.piperider.io/how-to-guides/generate-report) featuring
+your data profile and data assertion test results ([interactive sample](https:/
+/piperider-github-readme.s3.ap-northeast-1.amazonaws.com/run-0.8.0/index.html))
+* [Compare two reports](https://docs.piperider.io/how-to-guides/compare-
+reports) to understand how your data has changed over time ([interactive
+sample](https://piperider-github-readme.s3.ap-northeast-1.amazonaws.com/
+comparison-0.8.0/index.html)) * Test your data with data assertions: * Built-in
+[data assertions](https://docs.piperider.io/data-quality-assertions/assertion-
+configuration) * Extensible through [custom assertions](https://
+docs.piperider.io/data-quality-assertions/custom-assertions) * Auto-generated
+data assertions * Currently supports [Postgres](https://docs.piperider.io/data-
+sources/postgres-connector), [Snowflake](https://docs.piperider.io/data-
+sources/snowflake-connector), SQLite, [BigQuery](https://docs.piperider.io/
+data-sources/bigquery-connector), [Redshift](https://docs.piperider.io/data-
+sources/redshift-connector), [DuckDB](https://docs.piperider.io/data-sources/
+duckdb-connector/), [CSV](https://docs.piperider.io/data-sources/csv-connector/
+) and [Parquet](https://docs.piperider.io/data-sources/parquet-connector/). *
+Zero-config [support for dbt](https://docs.piperider.io/dbt-integration/
+) projects * Automation through [GitHub Actions](https://docs.piperider.io/how-
+to-guides/github-action/), [save reports in S3](https://docs.piperider.io/how-
+to-guides/aws-s3-+-github-ci/) # Getting started Get started quickly below, go
+to [the docs](https://docs.piperider.io/), or check out this article on [how to
+add data observability using PipeRider ](https://blog.infuseai.io/adding-data-
 observability-and-alerts-to-your-data-pipeline-is-easier-than-you-think-
 4e005daca55b) ## Install PipeRider ```bash pip install piperider ``` By
 default, PipeRider supports built-in SQLite connector, extra connectors are
 available: | connectors | install | supported since | |---|---|----------------
 --| | snowflake | pip install 'piperider[snowflake]' | | | postgres | pip
 install 'piperider[postgres]' | | | bigquery | pip install 'piperider
 [bigquery]' | PipeRider v0.7.0 | | redshift | pip install 'piperider[redshift]'
```

### Comparing `piperider-nightly-0.9.0.20220920/README.md` & `piperider-nightly-0.9.0.20220921/README.md`

 * *Files 15% similar despite different names*

```diff
@@ -32,15 +32,15 @@
 
 
 
 ## Made for the modern data team
 **For data engineers**
 * :zap: 2 min install & set-up
 * :relieved: Non-intrusive & open-source: install and use locally
-* :money_with_wings: Fast & cheap: 10M rows, 8 columns takes only 16s to profile
+* :money_with_wings: Fast & cheap: 100M rows & 8 columns (or 50M & 16 columns) takes only 18s to profile
 * :ledger: Cloud DataWarehouse native & auto-config for dbt
 
 
 
 **For data analysts**
 * :bowtie: Never waste time on analyzing wrong data: collects various metadata metrics such as freshness, uniqueness, distribution... [check all metrics](https://docs.piperider.io/data-profile-and-metrics/metrics)
 * :speech_balloon: Communicate easily your data expectations by showing the report
@@ -67,30 +67,30 @@
 * [Get involved](#get-involved)
     * [Support](#support)
     * [Contributions](#contributions)
  -->
 
 
 ## Key features
-* [Generate an HTML Report](how-to-guides/generate-report.md) featuring your data profile and data assertion test results ([interactive sample](https://piperider-github-readme.s3.ap-northeast-1.amazonaws.com/run-0.8.0/index.html))
-* [Compare two reports](how-to-guides/compare-reports.md) to understand how your data has changed over time ([interactive sample](https://piperider-github-readme.s3.ap-northeast-1.amazonaws.com/comparison-0.8.0/index.html))
+* [Generate an HTML Report](https://docs.piperider.io/how-to-guides/generate-report) featuring your data profile and data assertion test results ([interactive sample](https://piperider-github-readme.s3.ap-northeast-1.amazonaws.com/run-0.8.0/index.html))
+* [Compare two reports](https://docs.piperider.io/how-to-guides/compare-reports) to understand how your data has changed over time ([interactive sample](https://piperider-github-readme.s3.ap-northeast-1.amazonaws.com/comparison-0.8.0/index.html))
 * Test your data with data assertions:
-  * Built-in [data assertions](data-quality-assertions/assertion-configuration.md)
-  * Extensible through [custom assertions](data-quality-assertions/custom-assertions.md)
+  * Built-in [data assertions](https://docs.piperider.io/data-quality-assertions/assertion-configuration)
+  * Extensible through [custom assertions](https://docs.piperider.io/data-quality-assertions/custom-assertions)
   * Auto-generated data assertions
-* Currently supports [Postgres](data-sources/postgres-connector.md), [Snowflake](data-sources/snowflake-connector.md), SQLite, [BigQuery](data-sources/bigquery-connector.md), [Redshift](data-sources/redshift-connector.md), [DuckDB](data-sources/duckdb-connector.md), [CSV](data-sources/csv-connector.md) and [Parquet](data-sources/parquet-connector.md).
-* Zero-config [support for dbt](dbt-integration/) projects
-* Automation through [GitHub Actions](how-to-guides/github-action.md), [save reports in S3](how-to-guides/aws-s3-+-github-ci.md)
+* Currently supports [Postgres](https://docs.piperider.io/data-sources/postgres-connector), [Snowflake](https://docs.piperider.io/data-sources/snowflake-connector), SQLite, [BigQuery](https://docs.piperider.io/data-sources/bigquery-connector), [Redshift](https://docs.piperider.io/data-sources/redshift-connector), [DuckDB](https://docs.piperider.io/data-sources/duckdb-connector/), [CSV](https://docs.piperider.io/data-sources/csv-connector/) and [Parquet](https://docs.piperider.io/data-sources/parquet-connector/).
+* Zero-config [support for dbt](https://docs.piperider.io/dbt-integration/) projects
+* Automation through [GitHub Actions](https://docs.piperider.io/how-to-guides/github-action/), [save reports in S3](https://docs.piperider.io/how-to-guides/aws-s3-+-github-ci/)
 
 
 
 
 # Getting started
 
-Get started quickly below, go to [the docs](https://dochttps://docs.piperider.io/), or check out this article on [how to add data observability using PipeRider ](https://blog.infuseai.io/adding-data-observability-and-alerts-to-your-data-pipeline-is-easier-than-you-think-4e005daca55b)
+Get started quickly below, go to [the docs](https://docs.piperider.io/), or check out this article on [how to add data observability using PipeRider ](https://blog.infuseai.io/adding-data-observability-and-alerts-to-your-data-pipeline-is-easier-than-you-think-4e005daca55b)
 
 ## Install PipeRider
 
 ```bash
 pip install piperider
 ```
```

#### html2text {}

```diff
@@ -22,44 +22,48 @@
 strategy PipeRider will make your life easier by: 1. Building a data profile so
 you can easily understand your data 2. Creating test suggestions based on the
 profiling 3. Comparing data profile reports, so you track changes over time
 [Read how to implement a data quality strategy using profiling + testing]
 (https://blog.infuseai.io/add-data-profiling-and-assertions-to-dbt-with-
 piperider-732ca0821e3a) ## Made for the modern data team **For data engineers**
 * :zap: 2 min install & set-up * :relieved: Non-intrusive & open-source:
-install and use locally * :money_with_wings: Fast & cheap: 10M rows, 8 columns
-takes only 16s to profile * :ledger: Cloud DataWarehouse native & auto-config
-for dbt **For data analysts** * :bowtie: Never waste time on analyzing wrong
-data: collects various metadata metrics such as freshness, uniqueness,
-distribution... [check all metrics](https://docs.piperider.io/data-profile-and-
-metrics/metrics) * :speech_balloon: Communicate easily your data expectations
-by showing the report * Zero-config dbt integration ## Live Demo [![](https://
-i.imgur.com/WuFC4H6.png)](https://piperider-github-readme.s3.ap-northeast-
-1.amazonaws.com/run-0.7.0/index.html) [Click here or on image to interact]
-(https://piperider-github-readme.s3.ap-northeast-1.amazonaws.com/run-0.7.0/
-index.html)  ## Key features * [Generate an HTML Report](how-to-guides/
-generate-report.md) featuring your data profile and data assertion test results
-([interactive sample](https://piperider-github-readme.s3.ap-northeast-
-1.amazonaws.com/run-0.8.0/index.html)) * [Compare two reports](how-to-guides/
-compare-reports.md) to understand how your data has changed over time (
-[interactive sample](https://piperider-github-readme.s3.ap-northeast-
-1.amazonaws.com/comparison-0.8.0/index.html)) * Test your data with data
-assertions: * Built-in [data assertions](data-quality-assertions/assertion-
-configuration.md) * Extensible through [custom assertions](data-quality-
-assertions/custom-assertions.md) * Auto-generated data assertions * Currently
-supports [Postgres](data-sources/postgres-connector.md), [Snowflake](data-
-sources/snowflake-connector.md), SQLite, [BigQuery](data-sources/bigquery-
-connector.md), [Redshift](data-sources/redshift-connector.md), [DuckDB](data-
-sources/duckdb-connector.md), [CSV](data-sources/csv-connector.md) and
-[Parquet](data-sources/parquet-connector.md). * Zero-config [support for dbt]
-(dbt-integration/) projects * Automation through [GitHub Actions](how-to-
-guides/github-action.md), [save reports in S3](how-to-guides/aws-s3-+-github-
-ci.md) # Getting started Get started quickly below, go to [the docs](https://
-dochttps://docs.piperider.io/), or check out this article on [how to add data
-observability using PipeRider ](https://blog.infuseai.io/adding-data-
+install and use locally * :money_with_wings: Fast & cheap: 100M rows & 8
+columns (or 50M & 16 columns) takes only 18s to profile * :ledger: Cloud
+DataWarehouse native & auto-config for dbt **For data analysts** * :bowtie:
+Never waste time on analyzing wrong data: collects various metadata metrics
+such as freshness, uniqueness, distribution... [check all metrics](https://
+docs.piperider.io/data-profile-and-metrics/metrics) * :speech_balloon:
+Communicate easily your data expectations by showing the report * Zero-config
+dbt integration ## Live Demo [![](https://i.imgur.com/WuFC4H6.png)](https://
+piperider-github-readme.s3.ap-northeast-1.amazonaws.com/run-0.7.0/index.html)
+[Click here or on image to interact](https://piperider-github-readme.s3.ap-
+northeast-1.amazonaws.com/run-0.7.0/index.html)  ## Key features * [Generate an
+HTML Report](https://docs.piperider.io/how-to-guides/generate-report) featuring
+your data profile and data assertion test results ([interactive sample](https:/
+/piperider-github-readme.s3.ap-northeast-1.amazonaws.com/run-0.8.0/index.html))
+* [Compare two reports](https://docs.piperider.io/how-to-guides/compare-
+reports) to understand how your data has changed over time ([interactive
+sample](https://piperider-github-readme.s3.ap-northeast-1.amazonaws.com/
+comparison-0.8.0/index.html)) * Test your data with data assertions: * Built-in
+[data assertions](https://docs.piperider.io/data-quality-assertions/assertion-
+configuration) * Extensible through [custom assertions](https://
+docs.piperider.io/data-quality-assertions/custom-assertions) * Auto-generated
+data assertions * Currently supports [Postgres](https://docs.piperider.io/data-
+sources/postgres-connector), [Snowflake](https://docs.piperider.io/data-
+sources/snowflake-connector), SQLite, [BigQuery](https://docs.piperider.io/
+data-sources/bigquery-connector), [Redshift](https://docs.piperider.io/data-
+sources/redshift-connector), [DuckDB](https://docs.piperider.io/data-sources/
+duckdb-connector/), [CSV](https://docs.piperider.io/data-sources/csv-connector/
+) and [Parquet](https://docs.piperider.io/data-sources/parquet-connector/). *
+Zero-config [support for dbt](https://docs.piperider.io/dbt-integration/
+) projects * Automation through [GitHub Actions](https://docs.piperider.io/how-
+to-guides/github-action/), [save reports in S3](https://docs.piperider.io/how-
+to-guides/aws-s3-+-github-ci/) # Getting started Get started quickly below, go
+to [the docs](https://docs.piperider.io/), or check out this article on [how to
+add data observability using PipeRider ](https://blog.infuseai.io/adding-data-
 observability-and-alerts-to-your-data-pipeline-is-easier-than-you-think-
 4e005daca55b) ## Install PipeRider ```bash pip install piperider ``` By
 default, PipeRider supports built-in SQLite connector, extra connectors are
 available: | connectors | install | supported since | |---|---|----------------
 --| | snowflake | pip install 'piperider[snowflake]' | | | postgres | pip
 install 'piperider[postgres]' | | | bigquery | pip install 'piperider
 [bigquery]' | PipeRider v0.7.0 | | redshift | pip install 'piperider[redshift]'
```

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/__init__.py` & `piperider-nightly-0.9.0.20220921/piperider_cli/__init__.py`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/adapter/dbt_adapter.py` & `piperider-nightly-0.9.0.20220921/piperider_cli/adapter/dbt_adapter.py`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/assertion_engine/assertion.py` & `piperider-nightly-0.9.0.20220921/piperider_cli/assertion_engine/assertion.py`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/assertion_engine/recommended_rules/table_assertions.py` & `piperider-nightly-0.9.0.20220921/piperider_cli/assertion_engine/recommended_rules/table_assertions.py`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/assertion_engine/recommender.py` & `piperider-nightly-0.9.0.20220921/piperider_cli/assertion_engine/recommender.py`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/assertion_engine/types/__init__.py` & `piperider-nightly-0.9.0.20220921/piperider_cli/assertion_engine/types/__init__.py`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/assertion_engine/types/assert_column_misc.py` & `piperider-nightly-0.9.0.20220921/piperider_cli/assertion_engine/types/assert_column_misc.py`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/assertion_engine/types/assert_column_ranges.py` & `piperider-nightly-0.9.0.20220921/piperider_cli/assertion_engine/types/assert_column_ranges.py`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/assertion_engine/types/assert_column_types.py` & `piperider-nightly-0.9.0.20220921/piperider_cli/assertion_engine/types/assert_column_types.py`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/assertion_engine/types/assert_rows.py` & `piperider-nightly-0.9.0.20220921/piperider_cli/assertion_engine/types/assert_rows.py`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/assertion_engine/types/base.py` & `piperider-nightly-0.9.0.20220921/piperider_cli/assertion_engine/types/base.py`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/assertion_generator.py` & `piperider-nightly-0.9.0.20220921/piperider_cli/assertion_generator.py`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/cli.py` & `piperider-nightly-0.9.0.20220921/piperider_cli/cli.py`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/cloud/__init__.py` & `piperider-nightly-0.9.0.20220921/piperider_cli/cloud/__init__.py`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/cloud_connector.py` & `piperider-nightly-0.9.0.20220921/piperider_cli/cloud_connector.py`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/compare_report.py` & `piperider-nightly-0.9.0.20220921/piperider_cli/compare_report.py`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/configuration.py` & `piperider-nightly-0.9.0.20220921/piperider_cli/configuration.py`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/piperider-init-template/plugins/customized_assertions.py` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/piperider-init-template/plugins/customized_assertions.py`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/Discord/Discord-Logo.svg` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/Discord/Discord-Logo.svg`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/GitHub/GitHub-Logo.svg` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/GitHub/GitHub-Logo.svg`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/asset-manifest.json` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/asset-manifest.json`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/index.html` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/index.html`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/logo/android-icon-144x144.png` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/logo/android-icon-144x144.png`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/logo/android-icon-192x192.png` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/logo/android-icon-192x192.png`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/logo/android-icon-36x36.png` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/logo/android-icon-36x36.png`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/logo/android-icon-48x48.png` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/logo/android-icon-48x48.png`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/logo/android-icon-72x72.png` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/logo/android-icon-72x72.png`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/logo/android-icon-96x96.png` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/logo/android-icon-96x96.png`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/logo/apple-icon-114x114.png` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/logo/apple-icon-114x114.png`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/logo/apple-icon-120x120.png` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/logo/apple-icon-120x120.png`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/logo/apple-icon-144x144.png` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/logo/apple-icon-144x144.png`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/logo/apple-icon-152x152.png` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/logo/apple-icon-152x152.png`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/logo/apple-icon-180x180.png` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/logo/apple-icon-180x180.png`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/logo/apple-icon-57x57.png` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/logo/apple-icon-57x57.png`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/logo/apple-icon-60x60.png` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/logo/apple-icon-60x60.png`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/logo/apple-icon-72x72.png` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/logo/apple-icon-72x72.png`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/logo/apple-icon-76x76.png` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/logo/apple-icon-76x76.png`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/logo/apple-icon-precomposed.png` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/logo/apple-icon-precomposed.png`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/logo/apple-icon.png` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/logo/apple-icon.png`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/logo/favicon-16x16.png` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/logo/favicon-16x16.png`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/logo/favicon-32x32.png` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/logo/favicon-32x32.png`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/logo/favicon-96x96.png` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/logo/favicon-96x96.png`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/logo/favicon.ico` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/logo/favicon.ico`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/logo/logo.svg` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/logo/logo.svg`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/logo/manifest.json` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/logo/manifest.json`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/logo/ms-icon-144x144.png` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/logo/ms-icon-144x144.png`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/logo/ms-icon-150x150.png` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/logo/ms-icon-150x150.png`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/logo/ms-icon-310x310.png` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/logo/ms-icon-310x310.png`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/logo/ms-icon-70x70.png` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/logo/ms-icon-70x70.png`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/css/main.fcbcb80f.css` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/css/main.fcbcb80f.css`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/css/main.fcbcb80f.css.map` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/css/main.fcbcb80f.css.map`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/js/183.b8accd6c.chunk.js` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/js/183.b8accd6c.chunk.js`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/js/276.fcb4db01.chunk.js` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/js/276.fcb4db01.chunk.js`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/js/357.5328e62e.chunk.js` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/js/357.5328e62e.chunk.js`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/js/787.20f148af.chunk.js` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/js/787.20f148af.chunk.js`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/js/836.945208d8.chunk.js` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/js/836.945208d8.chunk.js`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/js/903.4ec9ff75.chunk.js` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/js/903.4ec9ff75.chunk.js`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/js/906.9eefb2c7.chunk.js` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/js/906.9eefb2c7.chunk.js`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/js/914.035c9fb2.chunk.js` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/js/914.035c9fb2.chunk.js`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/js/982.4539617f.chunk.js` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/js/982.4539617f.chunk.js`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/js/main.3dd694e2.js` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/js/main.3dd694e2.js`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/js/main.3dd694e2.js.LICENSE.txt` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/js/main.3dd694e2.js.LICENSE.txt`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-Black.ab57b908749eb205e3ad.woff` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-Black.ab57b908749eb205e3ad.woff`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-Black.cadfd7434852779eb395.woff2` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-Black.cadfd7434852779eb395.woff2`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-BlackItalic.9bb4dd54e5afbea2e0ac.woff2` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-BlackItalic.9bb4dd54e5afbea2e0ac.woff2`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-BlackItalic.f0098e273d2a3758b89c.woff` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-BlackItalic.f0098e273d2a3758b89c.woff`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-Bold.1577ca92013647c816b5.woff` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-Bold.1577ca92013647c816b5.woff`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-Bold.f57c31edca48068386d7.woff2` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-Bold.f57c31edca48068386d7.woff2`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-BoldItalic.52e97aac5945285c9933.woff` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-BoldItalic.52e97aac5945285c9933.woff`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-BoldItalic.5b7f79817b551400186a.woff2` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-BoldItalic.5b7f79817b551400186a.woff2`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-ExtraBold.0321ea88d696270daf4b.woff` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-ExtraBold.0321ea88d696270daf4b.woff`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-ExtraBold.a611efd96602ca47acd9.woff2` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-ExtraBold.a611efd96602ca47acd9.woff2`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-ExtraBoldItalic.43f46f665391ff324c72.woff2` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-ExtraBoldItalic.43f46f665391ff324c72.woff2`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-ExtraBoldItalic.dc0b36ae1c1bdac232e7.woff` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-ExtraBoldItalic.dc0b36ae1c1bdac232e7.woff`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-ExtraLight.4e029f034c7e7263df9a.woff` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-ExtraLight.4e029f034c7e7263df9a.woff`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-ExtraLight.bafff4ae7f2a3395aa13.woff2` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-ExtraLight.bafff4ae7f2a3395aa13.woff2`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-ExtraLightItalic.124644177779db0a8867.woff2` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-ExtraLightItalic.124644177779db0a8867.woff2`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-ExtraLightItalic.ff3def84a34422de5487.woff` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-ExtraLightItalic.ff3def84a34422de5487.woff`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-Italic.9736c3faff86c01270b2.woff2` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-Italic.9736c3faff86c01270b2.woff2`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-Italic.ce6bab8bc932d6080ec1.woff` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-Italic.ce6bab8bc932d6080ec1.woff`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-Light.919d6ffdd987dc2e4717.woff` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-Light.919d6ffdd987dc2e4717.woff`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-Light.aafd1643606ee83ad4cb.woff2` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-Light.aafd1643606ee83ad4cb.woff2`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-LightItalic.7f7cde8e1548e11231fb.woff2` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-LightItalic.7f7cde8e1548e11231fb.woff2`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-LightItalic.e66e7a760a286c694d2b.woff` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-LightItalic.e66e7a760a286c694d2b.woff`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-Medium.5a92f7b05463ecd61f45.woff` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-Medium.5a92f7b05463ecd61f45.woff`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-Medium.a6ca36dde32b3a1d0fd4.woff2` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-Medium.a6ca36dde32b3a1d0fd4.woff2`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-MediumItalic.dbc1ed152c7b11f501a3.woff2` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-MediumItalic.dbc1ed152c7b11f501a3.woff2`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-MediumItalic.e3618413f59e00041fb3.woff` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-MediumItalic.e3618413f59e00041fb3.woff`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-Regular.222064f2a764069868f4.woff2` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-Regular.222064f2a764069868f4.woff2`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-Regular.67a27362108220436ffb.woff` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-Regular.67a27362108220436ffb.woff`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-SemiBold.599ce7634f46c5024ad0.woff2` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-SemiBold.599ce7634f46c5024ad0.woff2`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-SemiBold.c2e7341dd6ac6502be69.woff` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-SemiBold.c2e7341dd6ac6502be69.woff`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-SemiBoldItalic.09bc481607bd529abda7.woff2` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-SemiBoldItalic.09bc481607bd529abda7.woff2`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-SemiBoldItalic.43f7c276720845c6bb59.woff` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-SemiBoldItalic.43f7c276720845c6bb59.woff`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-Thin.92cada3d91581eb5112d.woff2` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-Thin.92cada3d91581eb5112d.woff2`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-Thin.df0b1bcf558ccd5b48a2.woff` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-Thin.df0b1bcf558ccd5b48a2.woff`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-ThinItalic.78bf87d2ea41ac4365c1.woff` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-ThinItalic.78bf87d2ea41ac4365c1.woff`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-ThinItalic.82dd2dc2fb674d8273e4.woff2` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-ThinItalic.82dd2dc2fb674d8273e4.woff2`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-italic.var.28904cc0eac675e1d19e.woff2` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-italic.var.28904cc0eac675e1d19e.woff2`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter-roman.var.f05060926bf5023f9930.woff2` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter-roman.var.f05060926bf5023f9930.woff2`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/comparison-report/static/media/Inter.var.c3f97a25f56b5b416e49.woff2` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/comparison-report/static/media/Inter.var.c3f97a25f56b5b416e49.woff2`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/Discord/Discord-Logo.svg` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/Discord/Discord-Logo.svg`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/GitHub/GitHub-Logo.svg` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/GitHub/GitHub-Logo.svg`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/asset-manifest.json` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/asset-manifest.json`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/index.html` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/index.html`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/logo/android-icon-144x144.png` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/logo/android-icon-144x144.png`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/logo/android-icon-192x192.png` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/logo/android-icon-192x192.png`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/logo/android-icon-36x36.png` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/logo/android-icon-36x36.png`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/logo/android-icon-48x48.png` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/logo/android-icon-48x48.png`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/logo/android-icon-72x72.png` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/logo/android-icon-72x72.png`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/logo/android-icon-96x96.png` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/logo/android-icon-96x96.png`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/logo/apple-icon-114x114.png` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/logo/apple-icon-114x114.png`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/logo/apple-icon-120x120.png` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/logo/apple-icon-120x120.png`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/logo/apple-icon-144x144.png` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/logo/apple-icon-144x144.png`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/logo/apple-icon-152x152.png` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/logo/apple-icon-152x152.png`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/logo/apple-icon-180x180.png` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/logo/apple-icon-180x180.png`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/logo/apple-icon-57x57.png` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/logo/apple-icon-57x57.png`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/logo/apple-icon-60x60.png` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/logo/apple-icon-60x60.png`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/logo/apple-icon-72x72.png` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/logo/apple-icon-72x72.png`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/logo/apple-icon-76x76.png` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/logo/apple-icon-76x76.png`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/logo/apple-icon-precomposed.png` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/logo/apple-icon-precomposed.png`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/logo/apple-icon.png` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/logo/apple-icon.png`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/logo/favicon-16x16.png` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/logo/favicon-16x16.png`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/logo/favicon-32x32.png` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/logo/favicon-32x32.png`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/logo/favicon-96x96.png` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/logo/favicon-96x96.png`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/logo/favicon.ico` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/logo/favicon.ico`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/logo/logo.svg` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/logo/logo.svg`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/logo/manifest.json` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/logo/manifest.json`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/logo/ms-icon-144x144.png` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/logo/ms-icon-144x144.png`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/logo/ms-icon-150x150.png` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/logo/ms-icon-150x150.png`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/logo/ms-icon-310x310.png` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/logo/ms-icon-310x310.png`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/logo/ms-icon-70x70.png` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/logo/ms-icon-70x70.png`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/css/main.fcbcb80f.css` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/css/main.fcbcb80f.css`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/css/main.fcbcb80f.css.map` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/css/main.fcbcb80f.css.map`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/js/183.b8accd6c.chunk.js` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/js/183.b8accd6c.chunk.js`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/js/276.fcb4db01.chunk.js` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/js/276.fcb4db01.chunk.js`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/js/357.5328e62e.chunk.js` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/js/357.5328e62e.chunk.js`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/js/787.20f148af.chunk.js` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/js/787.20f148af.chunk.js`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/js/836.945208d8.chunk.js` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/js/836.945208d8.chunk.js`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/js/903.4ec9ff75.chunk.js` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/js/903.4ec9ff75.chunk.js`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/js/906.9eefb2c7.chunk.js` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/js/906.9eefb2c7.chunk.js`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/js/914.035c9fb2.chunk.js` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/js/914.035c9fb2.chunk.js`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/js/982.4539617f.chunk.js` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/js/982.4539617f.chunk.js`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/js/main.a918e51a.js` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/js/main.a918e51a.js`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/js/main.a918e51a.js.LICENSE.txt` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/js/main.a918e51a.js.LICENSE.txt`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-Black.ab57b908749eb205e3ad.woff` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-Black.ab57b908749eb205e3ad.woff`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-Black.cadfd7434852779eb395.woff2` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-Black.cadfd7434852779eb395.woff2`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-BlackItalic.9bb4dd54e5afbea2e0ac.woff2` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-BlackItalic.9bb4dd54e5afbea2e0ac.woff2`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-BlackItalic.f0098e273d2a3758b89c.woff` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-BlackItalic.f0098e273d2a3758b89c.woff`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-Bold.1577ca92013647c816b5.woff` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-Bold.1577ca92013647c816b5.woff`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-Bold.f57c31edca48068386d7.woff2` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-Bold.f57c31edca48068386d7.woff2`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-BoldItalic.52e97aac5945285c9933.woff` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-BoldItalic.52e97aac5945285c9933.woff`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-BoldItalic.5b7f79817b551400186a.woff2` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-BoldItalic.5b7f79817b551400186a.woff2`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-ExtraBold.0321ea88d696270daf4b.woff` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-ExtraBold.0321ea88d696270daf4b.woff`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-ExtraBold.a611efd96602ca47acd9.woff2` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-ExtraBold.a611efd96602ca47acd9.woff2`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-ExtraBoldItalic.43f46f665391ff324c72.woff2` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-ExtraBoldItalic.43f46f665391ff324c72.woff2`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-ExtraBoldItalic.dc0b36ae1c1bdac232e7.woff` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-ExtraBoldItalic.dc0b36ae1c1bdac232e7.woff`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-ExtraLight.4e029f034c7e7263df9a.woff` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-ExtraLight.4e029f034c7e7263df9a.woff`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-ExtraLight.bafff4ae7f2a3395aa13.woff2` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-ExtraLight.bafff4ae7f2a3395aa13.woff2`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-ExtraLightItalic.124644177779db0a8867.woff2` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-ExtraLightItalic.124644177779db0a8867.woff2`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-ExtraLightItalic.ff3def84a34422de5487.woff` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-ExtraLightItalic.ff3def84a34422de5487.woff`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-Italic.9736c3faff86c01270b2.woff2` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-Italic.9736c3faff86c01270b2.woff2`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-Italic.ce6bab8bc932d6080ec1.woff` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-Italic.ce6bab8bc932d6080ec1.woff`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-Light.919d6ffdd987dc2e4717.woff` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-Light.919d6ffdd987dc2e4717.woff`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-Light.aafd1643606ee83ad4cb.woff2` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-Light.aafd1643606ee83ad4cb.woff2`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-LightItalic.7f7cde8e1548e11231fb.woff2` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-LightItalic.7f7cde8e1548e11231fb.woff2`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-LightItalic.e66e7a760a286c694d2b.woff` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-LightItalic.e66e7a760a286c694d2b.woff`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-Medium.5a92f7b05463ecd61f45.woff` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-Medium.5a92f7b05463ecd61f45.woff`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-Medium.a6ca36dde32b3a1d0fd4.woff2` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-Medium.a6ca36dde32b3a1d0fd4.woff2`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-MediumItalic.dbc1ed152c7b11f501a3.woff2` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-MediumItalic.dbc1ed152c7b11f501a3.woff2`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-MediumItalic.e3618413f59e00041fb3.woff` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-MediumItalic.e3618413f59e00041fb3.woff`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-Regular.222064f2a764069868f4.woff2` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-Regular.222064f2a764069868f4.woff2`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-Regular.67a27362108220436ffb.woff` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-Regular.67a27362108220436ffb.woff`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-SemiBold.599ce7634f46c5024ad0.woff2` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-SemiBold.599ce7634f46c5024ad0.woff2`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-SemiBold.c2e7341dd6ac6502be69.woff` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-SemiBold.c2e7341dd6ac6502be69.woff`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-SemiBoldItalic.09bc481607bd529abda7.woff2` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-SemiBoldItalic.09bc481607bd529abda7.woff2`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-SemiBoldItalic.43f7c276720845c6bb59.woff` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-SemiBoldItalic.43f7c276720845c6bb59.woff`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-Thin.92cada3d91581eb5112d.woff2` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-Thin.92cada3d91581eb5112d.woff2`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-Thin.df0b1bcf558ccd5b48a2.woff` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-Thin.df0b1bcf558ccd5b48a2.woff`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-ThinItalic.78bf87d2ea41ac4365c1.woff` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-ThinItalic.78bf87d2ea41ac4365c1.woff`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-ThinItalic.82dd2dc2fb674d8273e4.woff2` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-ThinItalic.82dd2dc2fb674d8273e4.woff2`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-italic.var.28904cc0eac675e1d19e.woff2` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-italic.var.28904cc0eac675e1d19e.woff2`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter-roman.var.f05060926bf5023f9930.woff2` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter-roman.var.f05060926bf5023f9930.woff2`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/data/report/single-report/static/media/Inter.var.c3f97a25f56b5b416e49.woff2` & `piperider-nightly-0.9.0.20220921/piperider_cli/data/report/single-report/static/media/Inter.var.c3f97a25f56b5b416e49.woff2`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/datasource/__init__.py` & `piperider-nightly-0.9.0.20220921/piperider_cli/datasource/__init__.py`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/datasource/bigquery.py` & `piperider-nightly-0.9.0.20220921/piperider_cli/datasource/bigquery.py`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/datasource/duckdb.py` & `piperider-nightly-0.9.0.20220921/piperider_cli/datasource/duckdb.py`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/datasource/field.py` & `piperider-nightly-0.9.0.20220921/piperider_cli/datasource/field.py`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/datasource/postgres.py` & `piperider-nightly-0.9.0.20220921/piperider_cli/datasource/postgres.py`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/datasource/redshift.py` & `piperider-nightly-0.9.0.20220921/piperider_cli/datasource/redshift.py`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/datasource/snowflake.py` & `piperider-nightly-0.9.0.20220921/piperider_cli/datasource/snowflake.py`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/datasource/sqlite.py` & `piperider-nightly-0.9.0.20220921/piperider_cli/datasource/sqlite.py`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/datasource/survey.py` & `piperider-nightly-0.9.0.20220921/piperider_cli/datasource/survey.py`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/docgen/__main__.py` & `piperider-nightly-0.9.0.20220921/piperider_cli/docgen/__main__.py`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/error.py` & `piperider-nightly-0.9.0.20220921/piperider_cli/error.py`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/event/__init__.py` & `piperider-nightly-0.9.0.20220921/piperider_cli/event/__init__.py`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/event/collector.py` & `piperider-nightly-0.9.0.20220921/piperider_cli/event/collector.py`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/event/track.py` & `piperider-nightly-0.9.0.20220921/piperider_cli/event/track.py`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/feedback.py` & `piperider-nightly-0.9.0.20220921/piperider_cli/feedback.py`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/filesystem.py` & `piperider-nightly-0.9.0.20220921/piperider_cli/filesystem.py`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/generate_report.py` & `piperider-nightly-0.9.0.20220921/piperider_cli/generate_report.py`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/guide.py` & `piperider-nightly-0.9.0.20220921/piperider_cli/guide.py`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/hack/datasource_inquirer_prompt.py` & `piperider-nightly-0.9.0.20220921/piperider_cli/hack/datasource_inquirer_prompt.py`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/hack/inquirer.py` & `piperider-nightly-0.9.0.20220921/piperider_cli/hack/inquirer.py`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/initializer.py` & `piperider-nightly-0.9.0.20220921/piperider_cli/initializer.py`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/profiler/event.py` & `piperider-nightly-0.9.0.20220921/piperider_cli/profiler/event.py`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/profiler/profiler.py` & `piperider-nightly-0.9.0.20220921/piperider_cli/profiler/profiler.py`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/profiler/schema.json` & `piperider-nightly-0.9.0.20220921/piperider_cli/profiler/schema.json`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/runner.py` & `piperider-nightly-0.9.0.20220921/piperider_cli/runner.py`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_cli/validator.py` & `piperider-nightly-0.9.0.20220921/piperider_cli/validator.py`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_nightly.egg-info/PKG-INFO` & `piperider-nightly-0.9.0.20220921/piperider_nightly.egg-info/PKG-INFO`

 * *Files 16% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: piperider-nightly
-Version: 0.9.0.20220920
+Version: 0.9.0.20220921
 Summary: PiperRider CLI
 Home-page: https://github.com/InfuseAI/piperider
 Author: InfuseAI Dev Team
 Author-email: dev@infuseai.io
 Project-URL: Bug Tracker, https://github.com/InfuseAI/piperider/issues
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
@@ -58,15 +58,15 @@
 
 
 
 ## Made for the modern data team
 **For data engineers**
 * :zap: 2 min install & set-up
 * :relieved: Non-intrusive & open-source: install and use locally
-* :money_with_wings: Fast & cheap: 10M rows, 8 columns takes only 16s to profile
+* :money_with_wings: Fast & cheap: 100M rows & 8 columns (or 50M & 16 columns) takes only 18s to profile
 * :ledger: Cloud DataWarehouse native & auto-config for dbt
 
 
 
 **For data analysts**
 * :bowtie: Never waste time on analyzing wrong data: collects various metadata metrics such as freshness, uniqueness, distribution... [check all metrics](https://docs.piperider.io/data-profile-and-metrics/metrics)
 * :speech_balloon: Communicate easily your data expectations by showing the report
@@ -93,30 +93,30 @@
 * [Get involved](#get-involved)
     * [Support](#support)
     * [Contributions](#contributions)
  -->
 
 
 ## Key features
-* [Generate an HTML Report](how-to-guides/generate-report.md) featuring your data profile and data assertion test results ([interactive sample](https://piperider-github-readme.s3.ap-northeast-1.amazonaws.com/run-0.8.0/index.html))
-* [Compare two reports](how-to-guides/compare-reports.md) to understand how your data has changed over time ([interactive sample](https://piperider-github-readme.s3.ap-northeast-1.amazonaws.com/comparison-0.8.0/index.html))
+* [Generate an HTML Report](https://docs.piperider.io/how-to-guides/generate-report) featuring your data profile and data assertion test results ([interactive sample](https://piperider-github-readme.s3.ap-northeast-1.amazonaws.com/run-0.8.0/index.html))
+* [Compare two reports](https://docs.piperider.io/how-to-guides/compare-reports) to understand how your data has changed over time ([interactive sample](https://piperider-github-readme.s3.ap-northeast-1.amazonaws.com/comparison-0.8.0/index.html))
 * Test your data with data assertions:
-  * Built-in [data assertions](data-quality-assertions/assertion-configuration.md)
-  * Extensible through [custom assertions](data-quality-assertions/custom-assertions.md)
+  * Built-in [data assertions](https://docs.piperider.io/data-quality-assertions/assertion-configuration)
+  * Extensible through [custom assertions](https://docs.piperider.io/data-quality-assertions/custom-assertions)
   * Auto-generated data assertions
-* Currently supports [Postgres](data-sources/postgres-connector.md), [Snowflake](data-sources/snowflake-connector.md), SQLite, [BigQuery](data-sources/bigquery-connector.md), [Redshift](data-sources/redshift-connector.md), [DuckDB](data-sources/duckdb-connector.md), [CSV](data-sources/csv-connector.md) and [Parquet](data-sources/parquet-connector.md).
-* Zero-config [support for dbt](dbt-integration/) projects
-* Automation through [GitHub Actions](how-to-guides/github-action.md), [save reports in S3](how-to-guides/aws-s3-+-github-ci.md)
+* Currently supports [Postgres](https://docs.piperider.io/data-sources/postgres-connector), [Snowflake](https://docs.piperider.io/data-sources/snowflake-connector), SQLite, [BigQuery](https://docs.piperider.io/data-sources/bigquery-connector), [Redshift](https://docs.piperider.io/data-sources/redshift-connector), [DuckDB](https://docs.piperider.io/data-sources/duckdb-connector/), [CSV](https://docs.piperider.io/data-sources/csv-connector/) and [Parquet](https://docs.piperider.io/data-sources/parquet-connector/).
+* Zero-config [support for dbt](https://docs.piperider.io/dbt-integration/) projects
+* Automation through [GitHub Actions](https://docs.piperider.io/how-to-guides/github-action/), [save reports in S3](https://docs.piperider.io/how-to-guides/aws-s3-+-github-ci/)
 
 
 
 
 # Getting started
 
-Get started quickly below, go to [the docs](https://dochttps://docs.piperider.io/), or check out this article on [how to add data observability using PipeRider ](https://blog.infuseai.io/adding-data-observability-and-alerts-to-your-data-pipeline-is-easier-than-you-think-4e005daca55b)
+Get started quickly below, go to [the docs](https://docs.piperider.io/), or check out this article on [how to add data observability using PipeRider ](https://blog.infuseai.io/adding-data-observability-and-alerts-to-your-data-pipeline-is-easier-than-you-think-4e005daca55b)
 
 ## Install PipeRider
 
 ```bash
 pip install piperider
 ```
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: piperider-nightly Version: 0.9.0.20220920 Summary:
+Metadata-Version: 2.1 Name: piperider-nightly Version: 0.9.0.20220921 Summary:
 PiperRider CLI Home-page: https://github.com/InfuseAI/piperider Author:
 InfuseAI Dev Team Author-email: dev@infuseai.io Project-URL: Bug Tracker,
 https://github.com/InfuseAI/piperider/issues Classifier: Programming Language
 :: Python :: 3.7 Classifier: Programming Language :: Python :: 3.8 Classifier:
 Programming Language :: Python :: 3.9 Classifier: License :: OSI Approved ::
 Apache Software License Classifier: Operating System :: OS Independent
 Classifier: Development Status :: 4 - Beta Requires-Python: >=3.7 Description-
@@ -33,44 +33,48 @@
 strategy PipeRider will make your life easier by: 1. Building a data profile so
 you can easily understand your data 2. Creating test suggestions based on the
 profiling 3. Comparing data profile reports, so you track changes over time
 [Read how to implement a data quality strategy using profiling + testing]
 (https://blog.infuseai.io/add-data-profiling-and-assertions-to-dbt-with-
 piperider-732ca0821e3a) ## Made for the modern data team **For data engineers**
 * :zap: 2 min install & set-up * :relieved: Non-intrusive & open-source:
-install and use locally * :money_with_wings: Fast & cheap: 10M rows, 8 columns
-takes only 16s to profile * :ledger: Cloud DataWarehouse native & auto-config
-for dbt **For data analysts** * :bowtie: Never waste time on analyzing wrong
-data: collects various metadata metrics such as freshness, uniqueness,
-distribution... [check all metrics](https://docs.piperider.io/data-profile-and-
-metrics/metrics) * :speech_balloon: Communicate easily your data expectations
-by showing the report * Zero-config dbt integration ## Live Demo [![](https://
-i.imgur.com/WuFC4H6.png)](https://piperider-github-readme.s3.ap-northeast-
-1.amazonaws.com/run-0.7.0/index.html) [Click here or on image to interact]
-(https://piperider-github-readme.s3.ap-northeast-1.amazonaws.com/run-0.7.0/
-index.html)  ## Key features * [Generate an HTML Report](how-to-guides/
-generate-report.md) featuring your data profile and data assertion test results
-([interactive sample](https://piperider-github-readme.s3.ap-northeast-
-1.amazonaws.com/run-0.8.0/index.html)) * [Compare two reports](how-to-guides/
-compare-reports.md) to understand how your data has changed over time (
-[interactive sample](https://piperider-github-readme.s3.ap-northeast-
-1.amazonaws.com/comparison-0.8.0/index.html)) * Test your data with data
-assertions: * Built-in [data assertions](data-quality-assertions/assertion-
-configuration.md) * Extensible through [custom assertions](data-quality-
-assertions/custom-assertions.md) * Auto-generated data assertions * Currently
-supports [Postgres](data-sources/postgres-connector.md), [Snowflake](data-
-sources/snowflake-connector.md), SQLite, [BigQuery](data-sources/bigquery-
-connector.md), [Redshift](data-sources/redshift-connector.md), [DuckDB](data-
-sources/duckdb-connector.md), [CSV](data-sources/csv-connector.md) and
-[Parquet](data-sources/parquet-connector.md). * Zero-config [support for dbt]
-(dbt-integration/) projects * Automation through [GitHub Actions](how-to-
-guides/github-action.md), [save reports in S3](how-to-guides/aws-s3-+-github-
-ci.md) # Getting started Get started quickly below, go to [the docs](https://
-dochttps://docs.piperider.io/), or check out this article on [how to add data
-observability using PipeRider ](https://blog.infuseai.io/adding-data-
+install and use locally * :money_with_wings: Fast & cheap: 100M rows & 8
+columns (or 50M & 16 columns) takes only 18s to profile * :ledger: Cloud
+DataWarehouse native & auto-config for dbt **For data analysts** * :bowtie:
+Never waste time on analyzing wrong data: collects various metadata metrics
+such as freshness, uniqueness, distribution... [check all metrics](https://
+docs.piperider.io/data-profile-and-metrics/metrics) * :speech_balloon:
+Communicate easily your data expectations by showing the report * Zero-config
+dbt integration ## Live Demo [![](https://i.imgur.com/WuFC4H6.png)](https://
+piperider-github-readme.s3.ap-northeast-1.amazonaws.com/run-0.7.0/index.html)
+[Click here or on image to interact](https://piperider-github-readme.s3.ap-
+northeast-1.amazonaws.com/run-0.7.0/index.html)  ## Key features * [Generate an
+HTML Report](https://docs.piperider.io/how-to-guides/generate-report) featuring
+your data profile and data assertion test results ([interactive sample](https:/
+/piperider-github-readme.s3.ap-northeast-1.amazonaws.com/run-0.8.0/index.html))
+* [Compare two reports](https://docs.piperider.io/how-to-guides/compare-
+reports) to understand how your data has changed over time ([interactive
+sample](https://piperider-github-readme.s3.ap-northeast-1.amazonaws.com/
+comparison-0.8.0/index.html)) * Test your data with data assertions: * Built-in
+[data assertions](https://docs.piperider.io/data-quality-assertions/assertion-
+configuration) * Extensible through [custom assertions](https://
+docs.piperider.io/data-quality-assertions/custom-assertions) * Auto-generated
+data assertions * Currently supports [Postgres](https://docs.piperider.io/data-
+sources/postgres-connector), [Snowflake](https://docs.piperider.io/data-
+sources/snowflake-connector), SQLite, [BigQuery](https://docs.piperider.io/
+data-sources/bigquery-connector), [Redshift](https://docs.piperider.io/data-
+sources/redshift-connector), [DuckDB](https://docs.piperider.io/data-sources/
+duckdb-connector/), [CSV](https://docs.piperider.io/data-sources/csv-connector/
+) and [Parquet](https://docs.piperider.io/data-sources/parquet-connector/). *
+Zero-config [support for dbt](https://docs.piperider.io/dbt-integration/
+) projects * Automation through [GitHub Actions](https://docs.piperider.io/how-
+to-guides/github-action/), [save reports in S3](https://docs.piperider.io/how-
+to-guides/aws-s3-+-github-ci/) # Getting started Get started quickly below, go
+to [the docs](https://docs.piperider.io/), or check out this article on [how to
+add data observability using PipeRider ](https://blog.infuseai.io/adding-data-
 observability-and-alerts-to-your-data-pipeline-is-easier-than-you-think-
 4e005daca55b) ## Install PipeRider ```bash pip install piperider ``` By
 default, PipeRider supports built-in SQLite connector, extra connectors are
 available: | connectors | install | supported since | |---|---|----------------
 --| | snowflake | pip install 'piperider[snowflake]' | | | postgres | pip
 install 'piperider[postgres]' | | | bigquery | pip install 'piperider
 [bigquery]' | PipeRider v0.7.0 | | redshift | pip install 'piperider[redshift]'
```

### Comparing `piperider-nightly-0.9.0.20220920/piperider_nightly.egg-info/SOURCES.txt` & `piperider-nightly-0.9.0.20220921/piperider_nightly.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/piperider_nightly.egg-info/requires.txt` & `piperider-nightly-0.9.0.20220921/piperider_nightly.egg-info/requires.txt`

 * *Files identical despite different names*

### Comparing `piperider-nightly-0.9.0.20220920/setup.py` & `piperider-nightly-0.9.0.20220921/setup.py`

 * *Files identical despite different names*

