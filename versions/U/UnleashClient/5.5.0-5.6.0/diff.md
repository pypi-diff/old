# Comparing `tmp/UnleashClient-5.5.0.tar.gz` & `tmp/UnleashClient-5.6.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/UnleashClient-5.5.0.tar", last modified: Mon Feb 27 07:00:25 2023, max compression
+gzip compressed data, was "dist/UnleashClient-5.6.0.tar", last modified: Fri Apr  7 08:04:50 2023, max compression
```

## Comparing `UnleashClient-5.5.0.tar` & `UnleashClient-5.6.0.tar`

### file list

```diff
@@ -1,143 +1,150 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-27 07:00:25.000000 UnleashClient-5.5.0/
--rw-r--r--   0 runner    (1001) docker     (123)      101 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/.flake8
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-27 07:00:25.000000 UnleashClient-5.5.0/.github/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-27 07:00:25.000000 UnleashClient-5.5.0/.github/ISSUE_TEMPLATE/
--rw-r--r--   0 runner    (1001) docker     (123)      521 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/.github/ISSUE_TEMPLATE/bug_report.md
--rw-r--r--   0 runner    (1001) docker     (123)      560 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/.github/ISSUE_TEMPLATE/feature_request.md
--rw-r--r--   0 runner    (1001) docker     (123)     1140 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/.github/PULL_REQUEST_TEMPLATE.md
--rw-r--r--   0 runner    (1001) docker     (123)      386 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/.github/dependabot.yml
--rw-r--r--   0 runner    (1001) docker     (123)       18 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/.github/stale.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-27 07:00:25.000000 UnleashClient-5.5.0/.github/workflows/
--rw-r--r--   0 runner    (1001) docker     (123)      249 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/.github/workflows/add-to-project.yml
--rw-r--r--   0 runner    (1001) docker     (123)     2446 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/.github/workflows/codeql-analysis.yml
--rw-r--r--   0 runner    (1001) docker     (123)     2347 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/.github/workflows/pull_request.yml
--rw-r--r--   0 runner    (1001) docker     (123)      712 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/.github/workflows/release-docs.yml
--rw-r--r--   0 runner    (1001) docker     (123)     1335 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/.github/workflows/release-package.yml
--rw-r--r--   0 runner    (1001) docker     (123)     1276 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/.gitignore
--rw-r--r--   0 runner    (1001) docker     (123)     7949 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/CHANGELOG.md
--rw-r--r--   0 runner    (1001) docker     (123)     3217 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/CODE_OF_CONDUCT.md
--rw-r--r--   0 runner    (1001) docker     (123)     2626 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/CONTRIBUTING.md
--rw-r--r--   0 runner    (1001) docker     (123)     1066 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/LICENSE.md
--rw-r--r--   0 runner    (1001) docker     (123)     1509 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/Makefile
--rw-r--r--   0 runner    (1001) docker     (123)     5857 2023-02-27 07:00:25.000000 UnleashClient-5.5.0/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     4353 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-27 07:00:25.000000 UnleashClient-5.5.0/UnleashClient/
--rw-r--r--   0 runner    (1001) docker     (123)    17790 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/UnleashClient/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-27 07:00:25.000000 UnleashClient-5.5.0/UnleashClient/api/
--rw-r--r--   0 runner    (1001) docker     (123)      114 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/UnleashClient/api/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2589 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/UnleashClient/api/features.py
--rw-r--r--   0 runner    (1001) docker     (123)     1510 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/UnleashClient/api/metrics.py
--rw-r--r--   0 runner    (1001) docker     (123)     2509 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/UnleashClient/api/register.py
--rw-r--r--   0 runner    (1001) docker     (123)     4266 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/UnleashClient/cache.py
--rw-r--r--   0 runner    (1001) docker     (123)      589 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/UnleashClient/constants.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-27 07:00:25.000000 UnleashClient-5.5.0/UnleashClient/constraints/
--rw-r--r--   0 runner    (1001) docker     (123)     7798 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/UnleashClient/constraints/Constraint.py
--rw-r--r--   0 runner    (1001) docker     (123)       35 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/UnleashClient/constraints/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      766 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/UnleashClient/deprecation_warnings.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-27 07:00:25.000000 UnleashClient-5.5.0/UnleashClient/features/
--rw-r--r--   0 runner    (1001) docker     (123)     3097 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/UnleashClient/features/Feature.py
--rw-r--r--   0 runner    (1001) docker     (123)       29 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/UnleashClient/features/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4785 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/UnleashClient/loader.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-27 07:00:25.000000 UnleashClient-5.5.0/UnleashClient/periodic_tasks/
--rw-r--r--   0 runner    (1001) docker     (123)      105 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/UnleashClient/periodic_tasks/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1154 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/UnleashClient/periodic_tasks/fetch_and_load.py
--rw-r--r--   0 runner    (1001) docker     (123)     1690 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/UnleashClient/periodic_tasks/send_metrics.py
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/UnleashClient/py.typed
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-27 07:00:25.000000 UnleashClient-5.5.0/UnleashClient/strategies/
--rw-r--r--   0 runner    (1001) docker     (123)      466 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/UnleashClient/strategies/ApplicationHostname.py
--rw-r--r--   0 runner    (1001) docker     (123)      258 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/UnleashClient/strategies/Default.py
--rw-r--r--   0 runner    (1001) docker     (123)     1410 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/UnleashClient/strategies/FlexibleRolloutStrategy.py
--rw-r--r--   0 runner    (1001) docker     (123)      396 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/UnleashClient/strategies/GradualRolloutRandom.py
--rw-r--r--   0 runner    (1001) docker     (123)      540 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/UnleashClient/strategies/GradualRolloutSessionId.py
--rw-r--r--   0 runner    (1001) docker     (123)      534 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/UnleashClient/strategies/GradualRolloutUserId.py
--rw-r--r--   0 runner    (1001) docker     (123)     1991 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/UnleashClient/strategies/RemoteAddress.py
--rw-r--r--   0 runner    (1001) docker     (123)     2898 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/UnleashClient/strategies/Strategy.py
--rw-r--r--   0 runner    (1001) docker     (123)      551 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/UnleashClient/strategies/UserWithId.py
--rw-r--r--   0 runner    (1001) docker     (123)      413 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/UnleashClient/strategies/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1601 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/UnleashClient/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-27 07:00:25.000000 UnleashClient-5.5.0/UnleashClient/variants/
--rw-r--r--   0 runner    (1001) docker     (123)     3379 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/UnleashClient/variants/Variants.py
--rw-r--r--   0 runner    (1001) docker     (123)       31 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/UnleashClient/variants/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-27 07:00:25.000000 UnleashClient-5.5.0/UnleashClient.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     5857 2023-02-27 07:00:25.000000 UnleashClient-5.5.0/UnleashClient.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     3878 2023-02-27 07:00:25.000000 UnleashClient-5.5.0/UnleashClient.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-02-27 07:00:25.000000 UnleashClient-5.5.0/UnleashClient.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-02-27 07:00:24.000000 UnleashClient-5.5.0/UnleashClient.egg-info/not-zip-safe
--rw-r--r--   0 runner    (1001) docker     (123)       84 2023-02-27 07:00:25.000000 UnleashClient-5.5.0/UnleashClient.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       14 2023-02-27 07:00:25.000000 UnleashClient-5.5.0/UnleashClient.egg-info/top_level.txt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-27 07:00:25.000000 UnleashClient-5.5.0/docs/
--rw-r--r--   0 runner    (1001) docker     (123)      634 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/docs/Makefile
--rw-r--r--   0 runner    (1001) docker     (123)      272 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/docs/basecache.rst
--rw-r--r--   0 runner    (1001) docker     (123)      883 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/docs/celery.rst
--rw-r--r--   0 runner    (1001) docker     (123)      123 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/docs/changelog.rst
--rw-r--r--   0 runner    (1001) docker     (123)     2308 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/docs/conf.py
--rw-r--r--   0 runner    (1001) docker     (123)     1253 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/docs/customcache.rst
--rw-r--r--   0 runner    (1001) docker     (123)     1966 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/docs/customstrategies.rst
--rw-r--r--   0 runner    (1001) docker     (123)     2073 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/docs/development.rst
--rw-r--r--   0 runner    (1001) docker     (123)      392 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/docs/filecache.rst
--rw-r--r--   0 runner    (1001) docker     (123)      670 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/docs/index.rst
--rw-r--r--   0 runner    (1001) docker     (123)      235 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/docs/installation.rst
--rw-r--r--   0 runner    (1001) docker     (123)      800 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/docs/make.bat
--rw-r--r--   0 runner    (1001) docker     (123)      275 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/docs/strategy.rst
--rw-r--r--   0 runner    (1001) docker     (123)      295 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/docs/unleashclient.rst
--rw-r--r--   0 runner    (1001) docker     (123)     3990 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/docs/usage.rst
--rw-r--r--   0 runner    (1001) docker     (123)     1171 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/docs/wsgi.rst
--rwxr-xr-x   0 runner    (1001) docker     (123)      366 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/get-spec.sh
--rw-r--r--   0 runner    (1001) docker     (123)      846 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)      353 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/requirements.txt
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-02-27 07:00:25.000000 UnleashClient-5.5.0/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1285 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-27 07:00:25.000000 UnleashClient-5.5.0/tests/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/tests/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1664 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/tests/conftest.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-27 07:00:25.000000 UnleashClient-5.5.0/tests/integration_tests/
--rw-r--r--   0 runner    (1001) docker     (123)      560 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/tests/integration_tests/integration.py
--rw-r--r--   0 runner    (1001) docker     (123)      689 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/tests/integration_tests/integration_gitlab.py
--rw-r--r--   0 runner    (1001) docker     (123)      694 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/tests/integration_tests/integration_unleashheroku.py
--rw-r--r--   0 runner    (1001) docker     (123)     1578 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/tests/integration_tests/integration_unleashhosted.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-27 07:00:25.000000 UnleashClient-5.5.0/tests/specification_tests/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/tests/specification_tests/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2354 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/tests/specification_tests/test_client_specs.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-27 07:00:25.000000 UnleashClient-5.5.0/tests/unit_tests/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/tests/unit_tests/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-27 07:00:25.000000 UnleashClient-5.5.0/tests/unit_tests/api/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/tests/unit_tests/api/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3836 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/tests/unit_tests/api/test_feature.py
--rw-r--r--   0 runner    (1001) docker     (123)      967 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/tests/unit_tests/api/test_metrics.py
--rw-r--r--   0 runner    (1001) docker     (123)     1142 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/tests/unit_tests/api/test_register.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-27 07:00:25.000000 UnleashClient-5.5.0/tests/unit_tests/periodic/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/tests/unit_tests/periodic/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2507 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/tests/unit_tests/periodic/test_aggregate_and_send_metrics.py
--rw-r--r--   0 runner    (1001) docker     (123)     3097 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/tests/unit_tests/periodic/test_fetch_and_load.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-27 07:00:25.000000 UnleashClient-5.5.0/tests/unit_tests/strategies/
--rw-r--r--   0 runner    (1001) docker     (123)      465 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/tests/unit_tests/strategies/test_applicationhostname.py
--rw-r--r--   0 runner    (1001) docker     (123)      201 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/tests/unit_tests/strategies/test_defaultstrategy.py
--rw-r--r--   0 runner    (1001) docker     (123)     3658 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/tests/unit_tests/strategies/test_flexiblerollout.py
--rw-r--r--   0 runner    (1001) docker     (123)      251 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/tests/unit_tests/strategies/test_gradualrolloutrandom.py
--rw-r--r--   0 runner    (1001) docker     (123)      354 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/tests/unit_tests/strategies/test_gradualrolloutwithsessionid.py
--rw-r--r--   0 runner    (1001) docker     (123)      316 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/tests/unit_tests/strategies/test_gradualrolloutwithuserid.py
--rw-r--r--   0 runner    (1001) docker     (123)     1161 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/tests/unit_tests/strategies/test_remoteaddress.py
--rw-r--r--   0 runner    (1001) docker     (123)      425 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/tests/unit_tests/strategies/test_userwithids.py
--rw-r--r--   0 runner    (1001) docker     (123)    20698 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/tests/unit_tests/test_client.py
--rw-r--r--   0 runner    (1001) docker     (123)     7312 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/tests/unit_tests/test_constraints.py
--rw-r--r--   0 runner    (1001) docker     (123)     3636 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/tests/unit_tests/test_custom_strategy.py
--rw-r--r--   0 runner    (1001) docker     (123)     2240 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/tests/unit_tests/test_features.py
--rw-r--r--   0 runner    (1001) docker     (123)     3351 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/tests/unit_tests/test_loader.py
--rw-r--r--   0 runner    (1001) docker     (123)     2707 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/tests/unit_tests/test_variants.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-27 07:00:25.000000 UnleashClient-5.5.0/tests/utilities/
--rw-r--r--   0 runner    (1001) docker     (123)       65 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/tests/utilities/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      507 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/tests/utilities/data_generator.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-27 07:00:25.000000 UnleashClient-5.5.0/tests/utilities/mocks/
--rw-r--r--   0 runner    (1001) docker     (123)      200 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/tests/utilities/mocks/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5110 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/tests/utilities/mocks/mock_all_features.py
--rw-r--r--   0 runner    (1001) docker     (123)      396 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/tests/utilities/mocks/mock_bootstrap.json
--rw-r--r--   0 runner    (1001) docker     (123)     4103 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/tests/utilities/mocks/mock_constraints.py
--rw-r--r--   0 runner    (1001) docker     (123)     1661 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/tests/utilities/mocks/mock_custom_strategy.py
--rw-r--r--   0 runner    (1001) docker     (123)     5614 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/tests/utilities/mocks/mock_features.py
--rw-r--r--   0 runner    (1001) docker     (123)      425 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/tests/utilities/mocks/mock_metrics.py
--rw-r--r--   0 runner    (1001) docker     (123)     1688 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/tests/utilities/mocks/mock_variants.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-27 07:00:25.000000 UnleashClient-5.5.0/tests/utilities/old_code/
--rw-r--r--   0 runner    (1001) docker     (123)     1292 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/tests/utilities/old_code/StrategyV2.py
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/tests/utilities/old_code/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1229 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/tests/utilities/testing_constants.py
--rw-r--r--   0 runner    (1001) docker     (123)      279 2023-02-27 06:59:39.000000 UnleashClient-5.5.0/tox.ini
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 08:04:50.000000 UnleashClient-5.6.0/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 08:04:50.000000 UnleashClient-5.6.0/.devcontainer/
+-rw-r--r--   0 runner    (1001) docker     (123)      603 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/.devcontainer/Dockerfile
+-rw-r--r--   0 runner    (1001) docker     (123)     2052 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/.devcontainer/devcontainer.json
+-rwxr-xr-x   0 runner    (1001) docker     (123)      423 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/.devcontainer/post_install.sh
+-rw-r--r--   0 runner    (1001) docker     (123)      101 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/.flake8
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 08:04:50.000000 UnleashClient-5.6.0/.github/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 08:04:50.000000 UnleashClient-5.6.0/.github/ISSUE_TEMPLATE/
+-rw-r--r--   0 runner    (1001) docker     (123)      521 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/.github/ISSUE_TEMPLATE/bug_report.md
+-rw-r--r--   0 runner    (1001) docker     (123)      560 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/.github/ISSUE_TEMPLATE/feature_request.md
+-rw-r--r--   0 runner    (1001) docker     (123)     1140 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/.github/PULL_REQUEST_TEMPLATE.md
+-rw-r--r--   0 runner    (1001) docker     (123)      386 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/.github/dependabot.yml
+-rw-r--r--   0 runner    (1001) docker     (123)       18 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/.github/stale.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 08:04:50.000000 UnleashClient-5.6.0/.github/workflows/
+-rw-r--r--   0 runner    (1001) docker     (123)      249 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/.github/workflows/add-to-project.yml
+-rw-r--r--   0 runner    (1001) docker     (123)     2446 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/.github/workflows/codeql-analysis.yml
+-rw-r--r--   0 runner    (1001) docker     (123)     1585 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/.github/workflows/pull_request.yml
+-rw-r--r--   0 runner    (1001) docker     (123)      712 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/.github/workflows/release-docs.yml
+-rw-r--r--   0 runner    (1001) docker     (123)     1335 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/.github/workflows/release-package.yml
+-rw-r--r--   0 runner    (1001) docker     (123)     1276 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/.gitignore
+-rw-r--r--   0 runner    (1001) docker     (123)     8183 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/CHANGELOG.md
+-rw-r--r--   0 runner    (1001) docker     (123)     3217 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/CODE_OF_CONDUCT.md
+-rw-r--r--   0 runner    (1001) docker     (123)     2626 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/CONTRIBUTING.md
+-rw-r--r--   0 runner    (1001) docker     (123)     1066 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/LICENSE.md
+-rw-r--r--   0 runner    (1001) docker     (123)     1509 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/Makefile
+-rw-r--r--   0 runner    (1001) docker     (123)     5908 2023-04-07 08:04:50.000000 UnleashClient-5.6.0/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     4353 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 08:04:50.000000 UnleashClient-5.6.0/UnleashClient/
+-rw-r--r--   0 runner    (1001) docker     (123)    19766 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/UnleashClient/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 08:04:50.000000 UnleashClient-5.6.0/UnleashClient/api/
+-rw-r--r--   0 runner    (1001) docker     (123)      114 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/UnleashClient/api/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2578 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/UnleashClient/api/features.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1510 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/UnleashClient/api/metrics.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2509 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/UnleashClient/api/register.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4313 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/UnleashClient/cache.py
+-rw-r--r--   0 runner    (1001) docker     (123)      589 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/UnleashClient/constants.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 08:04:50.000000 UnleashClient-5.6.0/UnleashClient/constraints/
+-rw-r--r--   0 runner    (1001) docker     (123)     7798 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/UnleashClient/constraints/Constraint.py
+-rw-r--r--   0 runner    (1001) docker     (123)       35 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/UnleashClient/constraints/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      766 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/UnleashClient/deprecation_warnings.py
+-rw-r--r--   0 runner    (1001) docker     (123)      559 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/UnleashClient/events.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 08:04:50.000000 UnleashClient-5.6.0/UnleashClient/features/
+-rw-r--r--   0 runner    (1001) docker     (123)     3333 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/UnleashClient/features/Feature.py
+-rw-r--r--   0 runner    (1001) docker     (123)       29 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/UnleashClient/features/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4914 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/UnleashClient/loader.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 08:04:50.000000 UnleashClient-5.6.0/UnleashClient/periodic_tasks/
+-rw-r--r--   0 runner    (1001) docker     (123)      105 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/UnleashClient/periodic_tasks/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1154 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/UnleashClient/periodic_tasks/fetch_and_load.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1690 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/UnleashClient/periodic_tasks/send_metrics.py
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/UnleashClient/py.typed
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 08:04:50.000000 UnleashClient-5.6.0/UnleashClient/strategies/
+-rw-r--r--   0 runner    (1001) docker     (123)      466 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/UnleashClient/strategies/ApplicationHostname.py
+-rw-r--r--   0 runner    (1001) docker     (123)      258 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/UnleashClient/strategies/Default.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1410 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/UnleashClient/strategies/FlexibleRolloutStrategy.py
+-rw-r--r--   0 runner    (1001) docker     (123)      396 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/UnleashClient/strategies/GradualRolloutRandom.py
+-rw-r--r--   0 runner    (1001) docker     (123)      540 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/UnleashClient/strategies/GradualRolloutSessionId.py
+-rw-r--r--   0 runner    (1001) docker     (123)      534 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/UnleashClient/strategies/GradualRolloutUserId.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1991 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/UnleashClient/strategies/RemoteAddress.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2898 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/UnleashClient/strategies/Strategy.py
+-rw-r--r--   0 runner    (1001) docker     (123)      551 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/UnleashClient/strategies/UserWithId.py
+-rw-r--r--   0 runner    (1001) docker     (123)      413 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/UnleashClient/strategies/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1601 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/UnleashClient/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 08:04:50.000000 UnleashClient-5.6.0/UnleashClient/variants/
+-rw-r--r--   0 runner    (1001) docker     (123)     3379 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/UnleashClient/variants/Variants.py
+-rw-r--r--   0 runner    (1001) docker     (123)       31 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/UnleashClient/variants/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 08:04:50.000000 UnleashClient-5.6.0/UnleashClient.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     5908 2023-04-07 08:04:50.000000 UnleashClient-5.6.0/UnleashClient.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     4029 2023-04-07 08:04:50.000000 UnleashClient-5.6.0/UnleashClient.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 08:04:50.000000 UnleashClient-5.6.0/UnleashClient.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 08:04:48.000000 UnleashClient-5.6.0/UnleashClient.egg-info/not-zip-safe
+-rw-r--r--   0 runner    (1001) docker     (123)       90 2023-04-07 08:04:50.000000 UnleashClient-5.6.0/UnleashClient.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       14 2023-04-07 08:04:50.000000 UnleashClient-5.6.0/UnleashClient.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 08:04:50.000000 UnleashClient-5.6.0/docs/
+-rw-r--r--   0 runner    (1001) docker     (123)      634 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/docs/Makefile
+-rw-r--r--   0 runner    (1001) docker     (123)      272 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/docs/basecache.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      883 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/docs/celery.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      123 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/docs/changelog.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     2335 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/docs/conf.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1300 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/docs/customcache.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     1966 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/docs/customstrategies.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     2223 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/docs/development.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     1136 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/docs/eventcallbacks.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      193 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/docs/events.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      392 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/docs/filecache.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      700 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/docs/index.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      235 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/docs/installation.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      800 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/docs/make.bat
+-rw-r--r--   0 runner    (1001) docker     (123)      238 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/docs/strategy.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      295 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/docs/unleashclient.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     3990 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/docs/usage.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     1171 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/docs/wsgi.rst
+-rwxr-xr-x   0 runner    (1001) docker     (123)      366 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/get-spec.sh
+-rw-r--r--   0 runner    (1001) docker     (123)      846 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)      357 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/requirements.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-07 08:04:50.000000 UnleashClient-5.6.0/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1342 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 08:04:50.000000 UnleashClient-5.6.0/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/tests/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1664 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/tests/conftest.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 08:04:50.000000 UnleashClient-5.6.0/tests/integration_tests/
+-rw-r--r--   0 runner    (1001) docker     (123)      560 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/tests/integration_tests/integration.py
+-rw-r--r--   0 runner    (1001) docker     (123)      689 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/tests/integration_tests/integration_gitlab.py
+-rw-r--r--   0 runner    (1001) docker     (123)      694 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/tests/integration_tests/integration_unleashheroku.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1578 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/tests/integration_tests/integration_unleashhosted.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 08:04:50.000000 UnleashClient-5.6.0/tests/specification_tests/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/tests/specification_tests/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2354 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/tests/specification_tests/test_client_specs.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 08:04:50.000000 UnleashClient-5.6.0/tests/unit_tests/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/tests/unit_tests/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 08:04:50.000000 UnleashClient-5.6.0/tests/unit_tests/api/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/tests/unit_tests/api/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3836 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/tests/unit_tests/api/test_feature.py
+-rw-r--r--   0 runner    (1001) docker     (123)      967 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/tests/unit_tests/api/test_metrics.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1142 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/tests/unit_tests/api/test_register.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 08:04:50.000000 UnleashClient-5.6.0/tests/unit_tests/periodic/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/tests/unit_tests/periodic/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2507 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/tests/unit_tests/periodic/test_aggregate_and_send_metrics.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3097 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/tests/unit_tests/periodic/test_fetch_and_load.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 08:04:50.000000 UnleashClient-5.6.0/tests/unit_tests/strategies/
+-rw-r--r--   0 runner    (1001) docker     (123)      465 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/tests/unit_tests/strategies/test_applicationhostname.py
+-rw-r--r--   0 runner    (1001) docker     (123)      201 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/tests/unit_tests/strategies/test_defaultstrategy.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3658 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/tests/unit_tests/strategies/test_flexiblerollout.py
+-rw-r--r--   0 runner    (1001) docker     (123)      251 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/tests/unit_tests/strategies/test_gradualrolloutrandom.py
+-rw-r--r--   0 runner    (1001) docker     (123)      354 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/tests/unit_tests/strategies/test_gradualrolloutwithsessionid.py
+-rw-r--r--   0 runner    (1001) docker     (123)      316 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/tests/unit_tests/strategies/test_gradualrolloutwithuserid.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1161 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/tests/unit_tests/strategies/test_remoteaddress.py
+-rw-r--r--   0 runner    (1001) docker     (123)      425 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/tests/unit_tests/strategies/test_userwithids.py
+-rw-r--r--   0 runner    (1001) docker     (123)    22320 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/tests/unit_tests/test_client.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7312 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/tests/unit_tests/test_constraints.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3636 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/tests/unit_tests/test_custom_strategy.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2282 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/tests/unit_tests/test_features.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3400 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/tests/unit_tests/test_loader.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2707 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/tests/unit_tests/test_variants.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 08:04:50.000000 UnleashClient-5.6.0/tests/utilities/
+-rw-r--r--   0 runner    (1001) docker     (123)       65 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/tests/utilities/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      507 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/tests/utilities/data_generator.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 08:04:50.000000 UnleashClient-5.6.0/tests/utilities/mocks/
+-rw-r--r--   0 runner    (1001) docker     (123)      200 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/tests/utilities/mocks/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7194 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/tests/utilities/mocks/mock_all_features.py
+-rw-r--r--   0 runner    (1001) docker     (123)      405 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/tests/utilities/mocks/mock_bootstrap.json
+-rw-r--r--   0 runner    (1001) docker     (123)     4103 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/tests/utilities/mocks/mock_constraints.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2391 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/tests/utilities/mocks/mock_custom_strategy.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5990 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/tests/utilities/mocks/mock_features.py
+-rw-r--r--   0 runner    (1001) docker     (123)      425 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/tests/utilities/mocks/mock_metrics.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1688 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/tests/utilities/mocks/mock_variants.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 08:04:50.000000 UnleashClient-5.6.0/tests/utilities/old_code/
+-rw-r--r--   0 runner    (1001) docker     (123)     1292 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/tests/utilities/old_code/StrategyV2.py
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/tests/utilities/old_code/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1229 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/tests/utilities/testing_constants.py
+-rw-r--r--   0 runner    (1001) docker     (123)      285 2023-04-07 08:03:59.000000 UnleashClient-5.6.0/tox.ini
```

### Comparing `UnleashClient-5.5.0/.github/ISSUE_TEMPLATE/bug_report.md` & `UnleashClient-5.6.0/.github/ISSUE_TEMPLATE/bug_report.md`

 * *Files identical despite different names*

### Comparing `UnleashClient-5.5.0/.github/ISSUE_TEMPLATE/feature_request.md` & `UnleashClient-5.6.0/.github/ISSUE_TEMPLATE/feature_request.md`

 * *Files identical despite different names*

### Comparing `UnleashClient-5.5.0/.github/PULL_REQUEST_TEMPLATE.md` & `UnleashClient-5.6.0/.github/PULL_REQUEST_TEMPLATE.md`

 * *Files identical despite different names*

### Comparing `UnleashClient-5.5.0/.github/workflows/codeql-analysis.yml` & `UnleashClient-5.6.0/.github/workflows/codeql-analysis.yml`

 * *Files identical despite different names*

### Comparing `UnleashClient-5.5.0/.github/workflows/pull_request.yml` & `UnleashClient-5.6.0/.github/workflows/release-package.yml`

 * *Files 25% similar despite different names*

```diff
@@ -1,74 +1,48 @@
-name: CI
+name: Release package
 
 on:
-  push:
-  pull_request:
+  release:
+    types: [published]
 
 jobs:
   main:
     runs-on: ubuntu-latest
     steps:
       - uses: actions/checkout@v1
       - name: Set up Python 3.7
-        uses: actions/setup-python@v2
+        uses: actions/setup-python@v1
         with:
-          python-version: "3.7"
-      - name: Install packages
+          python-version: 3.7
+      - name: Install dependencies
         run: |
           python -m pip install --upgrade pip
           pip install -r requirements.txt
+          pip install wheel
           python setup.py install
-      - name: Linting
+      - name: Build package
         run: |
-          mypy UnleashClient --install-types --non-interactive
-          pylint UnleashClient
-      - name: Unit tests
+          python setup.py sdist bdist_wheel
+      - name: Upload package to pypi
         run: |
-          py.test tests/unit_tests
-      - name: Download test cases
-        run: git clone --depth 5 --branch v4.2.2 https://github.com/Unleash/client-specification.git tests/specification_tests/client-specification
-      - name: Specification tests
-        run: |
-          py.test --no-cov tests/specification_tests
-      - name: Send coverage to Coveralls
+          twine upload dist/*
         env:
-          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
+          TWINE_USERNAME: ${{ secrets.pypi_username }}
+          TWINE_PASSWORD: ${{ secrets.pypi_password }}
+      - name: Build docs
         run: |
-          coveralls --service=github
-      - name: Notify Slack of pipeline completion
-        uses: 8398a7/action-slack@v2
-        with:
-          status: ${{ job.status }}
-          author_name: Github Action
-        env:
-          GITHUB_TOKEN: ${{ secrets.github_slack_token }}
-          SLACK_WEBHOOK_URL: ${{ secrets.slack_webhook }}
-        if: ${{ github.event.pull_request.head.repo.full_name == github.event.pull_request.base.repo.full_name }} && (success() || failure())
-
-  tox:
-    runs-on: ubuntu-latest
-    strategy:
-      matrix:
-        os: [ubuntu-latest, macos-latest, windows-latest]
-        python: ["3.7", "3.8", "3.9", "3.10"]
-    steps:
-      - uses: actions/checkout@v1
-      - name: Setup Python
-        uses: actions/setup-python@v2
+          cd docs
+          make html
+      - name: Deploy docs
+        uses: peaceiris/actions-gh-pages@v3
         with:
-          python-version: ${{ matrix.python }}
-      - name: Install Tox and any other packages
-        run:  |
-          python -m pip install --upgrade pip
-          pip install tox
-      - name: Run Tox
-        run: tox -e py
+          github_token: ${{ secrets.GITHUB_TOKEN }}
+          publish_dir: ./docs/_build/html
       - name: Notify Slack of pipeline completion
         uses: 8398a7/action-slack@v2
         with:
           status: ${{ job.status }}
           author_name: Github Action
         env:
           GITHUB_TOKEN: ${{ secrets.github_slack_token }}
           SLACK_WEBHOOK_URL: ${{ secrets.slack_webhook }}
-        if: failure()
+        if: always()
```

### Comparing `UnleashClient-5.5.0/.github/workflows/release-docs.yml` & `UnleashClient-5.6.0/.github/workflows/release-docs.yml`

 * *Files identical despite different names*

### Comparing `UnleashClient-5.5.0/.gitignore` & `UnleashClient-5.6.0/.gitignore`

 * *Files identical despite different names*

### Comparing `UnleashClient-5.5.0/CHANGELOG.md` & `UnleashClient-5.6.0/CHANGELOG.md`

 * *Files 3% similar despite different names*

```diff
@@ -1,7 +1,14 @@
+## v5.6.0
+* (Major) Add support for event callbacks.
+
+## v5.5.0
+* (Minor) SDK now warns when multiple instances are created
+* (Bugfix) Fix an issue where the NOT_IN operator behaves incorrectly when inverted and no context is passed
+
 ## v5.4.1
 * (Bugfix) Fix an issue where custom stickiness fail to calculate correctly
 * (Bugfix) Fix floats not working correctly in constraints
 * (Bugfix) Fix an issue where timezones would be incorrectly handled in constraints
 * (Bugfix) Fix for NOT_IN constraint to handle failure case correctly as per spec
 * (Bugfix) Update murmurhash library to resolve correctly on Python 3.10+ without gcc
```

### Comparing `UnleashClient-5.5.0/CODE_OF_CONDUCT.md` & `UnleashClient-5.6.0/CODE_OF_CONDUCT.md`

 * *Files identical despite different names*

### Comparing `UnleashClient-5.5.0/CONTRIBUTING.md` & `UnleashClient-5.6.0/CONTRIBUTING.md`

 * *Files identical despite different names*

### Comparing `UnleashClient-5.5.0/LICENSE.md` & `UnleashClient-5.6.0/LICENSE.md`

 * *Files identical despite different names*

### Comparing `UnleashClient-5.5.0/Makefile` & `UnleashClient-5.6.0/Makefile`

 * *Files identical despite different names*

### Comparing `UnleashClient-5.5.0/PKG-INFO` & `UnleashClient-5.6.0/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: UnleashClient
-Version: 5.5.0
+Version: 5.6.0
 Summary: Python client for the Unleash feature toggle system!
 Home-page: https://github.com/Unleash/unleash-client-python
 Author: Ivan Lee
 Author-email: ivanklee86@gmail.com
 License: UNKNOWN
 Description: # unleash-client-python
         
@@ -115,8 +115,9 @@
 Classifier: Development Status :: 5 - Production/Stable
 Classifier: Intended Audience :: Developers
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10
+Classifier: Programming Language :: Python :: 3.11
 Description-Content-Type: text/markdown
```

### Comparing `UnleashClient-5.5.0/README.md` & `UnleashClient-5.6.0/README.md`

 * *Files identical despite different names*

### Comparing `UnleashClient-5.5.0/UnleashClient/__init__.py` & `UnleashClient-5.6.0/UnleashClient/__init__.py`

 * *Files 10% similar despite different names*

```diff
@@ -1,24 +1,26 @@
 # pylint: disable=invalid-name
 import warnings
 import random
 import string
+import uuid
 from datetime import datetime, timezone
 from typing import Callable, Optional
 from apscheduler.job import Job
 from apscheduler.schedulers.base import BaseScheduler
 from apscheduler.schedulers.background import BackgroundScheduler
 from apscheduler.triggers.interval import IntervalTrigger
 from apscheduler.executors.pool import ThreadPoolExecutor
 from UnleashClient.api import register_client
 from UnleashClient.periodic_tasks import fetch_and_load_features, aggregate_and_send_metrics
 from UnleashClient.strategies import ApplicationHostname, Default, GradualRolloutRandom, \
     GradualRolloutSessionId, GradualRolloutUserId, UserWithId, RemoteAddress, FlexibleRollout
 from UnleashClient.constants import METRIC_LAST_SENT_TIME, DISABLED_VARIATION, ETAG
 from UnleashClient.loader import load_features
+from UnleashClient.events import UnleashEvent, UnleashEventType
 from .utils import LOGGER, InstanceCounter, InstanceAllowType
 from .deprecation_warnings import strategy_v2xx_deprecation_check
 from .cache import BaseCache, FileCache
 
 
 INSTANCES = InstanceCounter()
 
@@ -41,14 +43,15 @@
     :param custom_strategies: Dictionary of custom strategy names : custom strategy objects.
     :param cache_directory: Location of the cache directory. When unset, FCache will determine the location.
     :param verbose_log_level: Numerical log level (https://docs.python.org/3/library/logging.html#logging-levels) for cases where checking a feature flag fails.
     :param cache: Custom cache implementation that extends UnleashClient.cache.BaseCache.  When unset, UnleashClient will use Fcache.
     :param scheduler: Custom APScheduler object.  Use this if you want to customize jobstore or executors.  When unset, UnleashClient will create it's own scheduler.
     :param scheduler_executor: Name of APSCheduler executor to use if using a custom scheduler.
     :param multiple_instance_mode: Determines how multiple instances being instantiated is handled by the SDK, when set to InstanceAllowType.BLOCK, the client constructor will fail when more than one instance is detected, when set to InstanceAllowType.WARN, multiple instances will be allowed but log a warning, when set to InstanceAllowType.SILENTLY_ALLOW, no warning or failure will be raised when instantiating multiple instances of the client. Defaults to InstanceAllowType.WARN
+    :param event_callback: Function to call if impression events are enabled.  WARNING: Depending on your event library, this may have performance implications!
     """
     def __init__(self,
                  url: str,
                  app_name: str,
                  environment: str = "default",
                  instance_id: str = "unleash-client-python",
                  refresh_interval: int = 15,
@@ -62,15 +65,16 @@
                  custom_strategies: Optional[dict] = None,
                  cache_directory: Optional[str] = None,
                  project_name: str = None,
                  verbose_log_level: int = 30,
                  cache: Optional[BaseCache] = None,
                  scheduler: Optional[BaseScheduler] = None,
                  scheduler_executor: Optional[str] = None,
-                 multiple_instance_mode: InstanceAllowType = InstanceAllowType.WARN) -> None:
+                 multiple_instance_mode: InstanceAllowType = InstanceAllowType.WARN,
+                 event_callback: Optional[Callable[[UnleashEvent], None]] = None) -> None:
         custom_headers = custom_headers or {}
         custom_options = custom_options or {}
         custom_strategies = custom_strategies or {}
 
         # Configuration
         self.unleash_url = url.rstrip('/')
         self.unleash_app_name = app_name
@@ -86,14 +90,15 @@
         self.unleash_custom_options = custom_options
         self.unleash_static_context = {
             "appName": self.unleash_app_name,
             "environment": self.unleash_environment
         }
         self.unleash_project_name = project_name
         self.unleash_verbose_log_level = verbose_log_level
+        self.unleash_event_callback = event_callback
 
         self._do_instance_check(multiple_instance_mode)
 
         # Class objects
         self.features: dict = {}
         self.fl_job: Job = None
         self.metric_job: Job = None
@@ -290,15 +295,33 @@
         base_context = self.unleash_static_context.copy()
         # Update context with static values and allow context to override environment
         base_context.update(context)
         context = base_context
 
         if self.unleash_bootstrapped or self.is_initialized:
             try:
-                return self.features[feature_name].is_enabled(context)
+                feature = self.features[feature_name]
+                feature_check = feature.is_enabled(context)
+
+                try:
+                    if self.unleash_event_callback and feature.impression_data:
+                        event = UnleashEvent(
+                            event_type=UnleashEventType.FEATURE_FLAG,
+                            event_id=uuid.uuid4(),
+                            context=context,
+                            enabled=feature_check,
+                            feature_name=feature_name
+                        )
+
+                        self.unleash_event_callback(event)
+                except Exception as excep:
+                    LOGGER.log(self.unleash_verbose_log_level, "Error in event callback: %s", excep)
+                    return feature_check
+
+                return feature_check
             except Exception as excep:
                 LOGGER.log(self.unleash_verbose_log_level, "Returning default value for feature: %s", feature_name)
                 LOGGER.log(self.unleash_verbose_log_level, "Error checking feature flag: %s", excep)
                 return self._get_fallback_value(fallback_function, feature_name, context)
         else:
             LOGGER.log(self.unleash_verbose_log_level, "Returning default value for feature: %s", feature_name)
             LOGGER.log(self.unleash_verbose_log_level, "Attempted to get feature_flag %s, but client wasn't initialized!", feature_name)
@@ -320,31 +343,49 @@
         :return: Variant and feature flag status.
         """
         context = context or {}
         context.update(self.unleash_static_context)
 
         if self.unleash_bootstrapped or self.is_initialized:
             try:
-                return self.features[feature_name].get_variant(context)
+                feature = self.features[feature_name]
+                variant_check = feature.get_variant(context)
+
+                if self.unleash_event_callback and feature.impression_data:
+                    try:
+                        event = UnleashEvent(
+                            event_type=UnleashEventType.VARIANT,
+                            event_id=uuid.uuid4(),
+                            context=context,
+                            enabled=variant_check['enabled'],
+                            feature_name=feature_name,
+                            variant=variant_check['name']
+                        )
+
+                        self.unleash_event_callback(event)
+                    except Exception as excep:
+                        LOGGER.log(self.unleash_verbose_log_level, "Error in event callback: %s", excep)
+                        return variant_check
+
+                return variant_check
             except Exception as excep:
                 LOGGER.log(self.unleash_verbose_log_level, "Returning default flag/variation for feature: %s", feature_name)
                 LOGGER.log(self.unleash_verbose_log_level, "Error checking feature flag variant: %s", excep)
                 return DISABLED_VARIATION
         else:
             LOGGER.log(self.unleash_verbose_log_level, "Returning default flag/variation for feature: %s", feature_name)
             LOGGER.log(self.unleash_verbose_log_level, "Attempted to get feature flag/variation %s, but client wasn't initialized!", feature_name)
             return DISABLED_VARIATION
 
     def _do_instance_check(self, multiple_instance_mode):
         identifier = self.__get_identifier()
         if identifier in INSTANCES:
             msg = f"You already have {INSTANCES.count(identifier)} instance(s) configured for this config: {identifier}, please double check the code where this client is being instantiated."
             if multiple_instance_mode == InstanceAllowType.BLOCK:
-                # pylint: disable=broad-exception-raised
-                raise Exception(msg)
+                raise Exception(msg)  # pylint: disable=broad-exception-raised
             if multiple_instance_mode == InstanceAllowType.WARN:
                 LOGGER.error(msg)
         INSTANCES.increment(identifier)
 
     def __get_identifier(self):
         api_key = self.unleash_custom_headers.get("Authorization") if self.unleash_custom_headers is not None else None
         return f"apiKey:{api_key} appName:{self.unleash_app_name} instanceId:{self.unleash_instance_id}"
```

### Comparing `UnleashClient-5.5.0/UnleashClient/api/features.py` & `UnleashClient-5.6.0/UnleashClient/api/features.py`

 * *Files 7% similar despite different names*

```diff
@@ -57,16 +57,15 @@
                                headers={**custom_headers, **headers},
                                params=base_params,
                                timeout=REQUEST_TIMEOUT, **custom_options)
 
         if resp.status_code not in [200, 304]:
             log_resp_info(resp)
             LOGGER.warning("Unleash Client feature fetch failed due to unexpected HTTP status code.")
-            # pylint: disable=broad-exception-raised
-            raise Exception("Unleash Client feature fetch failed!")
+            raise Exception("Unleash Client feature fetch failed!")  # pylint: disable=broad-exception-raised
 
         etag = ''
         if 'etag' in resp.headers.keys():
             etag = resp.headers['etag']
 
         if resp.status_code == 304:
             return None, etag
```

### Comparing `UnleashClient-5.5.0/UnleashClient/api/metrics.py` & `UnleashClient-5.6.0/UnleashClient/api/metrics.py`

 * *Files identical despite different names*

### Comparing `UnleashClient-5.5.0/UnleashClient/api/register.py` & `UnleashClient-5.6.0/UnleashClient/api/register.py`

 * *Files identical despite different names*

### Comparing `UnleashClient-5.5.0/UnleashClient/cache.py` & `UnleashClient-5.6.0/UnleashClient/cache.py`

 * *Files 1% similar despite different names*

```diff
@@ -8,15 +8,18 @@
 from UnleashClient.constants import FEATURES_URL, REQUEST_TIMEOUT
 
 
 class BaseCache(abc.ABC):
     """
     Abstract base class for caches used for UnleashClient.
 
-    If implementing your own bootstrapping methods, you must set the `bootstrapped` attribute to True after configuration is set.
+    If implementing your own bootstrapping methods:
+
+    - Add your custom bootstrap method.
+    - You must set the `bootstrapped` attribute to True after configuration is set.
     """
     bootstrapped = False
 
     @abc.abstractmethod
     def set(self, key: str, value: Any):
         pass
```

### Comparing `UnleashClient-5.5.0/UnleashClient/constants.py` & `UnleashClient-5.6.0/UnleashClient/constants.py`

 * *Files identical despite different names*

### Comparing `UnleashClient-5.5.0/UnleashClient/constraints/Constraint.py` & `UnleashClient-5.6.0/UnleashClient/constraints/Constraint.py`

 * *Files identical despite different names*

### Comparing `UnleashClient-5.5.0/UnleashClient/deprecation_warnings.py` & `UnleashClient-5.6.0/UnleashClient/deprecation_warnings.py`

 * *Files identical despite different names*

### Comparing `UnleashClient-5.5.0/UnleashClient/features/Feature.py` & `UnleashClient-5.6.0/UnleashClient/features/Feature.py`

 * *Files 7% similar despite different names*

```diff
@@ -1,33 +1,40 @@
 # pylint: disable=invalid-name
+from typing import Optional
+
 from UnleashClient.variants import Variants
 from UnleashClient.utils import LOGGER
 from UnleashClient.constants import DISABLED_VARIATION
 
 
 # pylint: disable=dangerous-default-value, broad-except
 class Feature:
     def __init__(self,
                  name: str,
                  enabled: bool,
                  strategies: list,
-                 variants: Variants = None) -> None:
+                 variants: Optional[Variants] = None,
+                 impression_data: bool = False) -> None:
         """
         A representation of a feature object
 
         :param name: Name of the feature.
         :param enabled: Whether feature is enabled.
         :param strategies: List of sub-classed Strategy objects representing feature strategies.
+        :param impression_data: Whether impression data is enabled.
         """
         # Experiment information
         self.name = name
         self.enabled = enabled
         self.strategies = strategies
         self.variants = variants
 
+        # Additional information
+        self.impression_data = impression_data
+
         # Stats tracking
         self.yes_count = 0
         self.no_count = 0
 
     def reset_stats(self) -> None:
         """
         Resets stats after metrics reporting
```

### Comparing `UnleashClient-5.5.0/UnleashClient/loader.py` & `UnleashClient-5.6.0/UnleashClient/loader.py`

 * *Files 3% similar despite different names*

```diff
@@ -55,19 +55,21 @@
         parsed_strategies = []
 
     if "variants" in provisioning:
         variant = Variants(provisioning['variants'], provisioning['name'])
     else:
         variant = None
 
-    return Feature(name=provisioning["name"],
-                   enabled=provisioning["enabled"],
-                   strategies=parsed_strategies,
-                   variants=variant
-                   )
+    return Feature(
+        name=provisioning["name"],
+        enabled=provisioning["enabled"],
+        strategies=parsed_strategies,
+        variants=variant,
+        impression_data=provisioning.get("impressionData", False),
+    )
 
 
 def load_features(cache: BaseCache,
                   feature_toggles: dict,
                   strategy_mapping: dict,
                   global_segments: Optional[dict] = None) -> None:
     """
@@ -115,12 +117,14 @@
 
         if 'variants' in parsed_features[feature]:
             feature_for_update.variants = Variants(
                 parsed_features[feature]['variants'],
                 parsed_features[feature]['name']
             )
 
+        feature_for_update.impression_data = parsed_features[feature].get("impressionData", False)
+
     # Handle creation or deletions
     new_features = list(set(feature_names) - set(feature_toggles.keys()))
 
     for feature in new_features:
         feature_toggles[feature] = _create_feature(parsed_features[feature], strategy_mapping, cache, global_segments)
```

### Comparing `UnleashClient-5.5.0/UnleashClient/periodic_tasks/fetch_and_load.py` & `UnleashClient-5.6.0/UnleashClient/periodic_tasks/fetch_and_load.py`

 * *Files identical despite different names*

### Comparing `UnleashClient-5.5.0/UnleashClient/periodic_tasks/send_metrics.py` & `UnleashClient-5.6.0/UnleashClient/periodic_tasks/send_metrics.py`

 * *Files identical despite different names*

### Comparing `UnleashClient-5.5.0/UnleashClient/strategies/FlexibleRolloutStrategy.py` & `UnleashClient-5.6.0/UnleashClient/strategies/FlexibleRolloutStrategy.py`

 * *Files identical despite different names*

### Comparing `UnleashClient-5.5.0/UnleashClient/strategies/GradualRolloutSessionId.py` & `UnleashClient-5.6.0/UnleashClient/strategies/GradualRolloutSessionId.py`

 * *Files identical despite different names*

### Comparing `UnleashClient-5.5.0/UnleashClient/strategies/GradualRolloutUserId.py` & `UnleashClient-5.6.0/UnleashClient/strategies/GradualRolloutUserId.py`

 * *Files identical despite different names*

### Comparing `UnleashClient-5.5.0/UnleashClient/strategies/RemoteAddress.py` & `UnleashClient-5.6.0/UnleashClient/strategies/RemoteAddress.py`

 * *Files identical despite different names*

### Comparing `UnleashClient-5.5.0/UnleashClient/strategies/Strategy.py` & `UnleashClient-5.6.0/UnleashClient/strategies/Strategy.py`

 * *Files identical despite different names*

### Comparing `UnleashClient-5.5.0/UnleashClient/strategies/UserWithId.py` & `UnleashClient-5.6.0/UnleashClient/strategies/UserWithId.py`

 * *Files identical despite different names*

### Comparing `UnleashClient-5.5.0/UnleashClient/utils.py` & `UnleashClient-5.6.0/UnleashClient/utils.py`

 * *Files identical despite different names*

### Comparing `UnleashClient-5.5.0/UnleashClient/variants/Variants.py` & `UnleashClient-5.6.0/UnleashClient/variants/Variants.py`

 * *Files identical despite different names*

### Comparing `UnleashClient-5.5.0/UnleashClient.egg-info/PKG-INFO` & `UnleashClient-5.6.0/UnleashClient.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: UnleashClient
-Version: 5.5.0
+Version: 5.6.0
 Summary: Python client for the Unleash feature toggle system!
 Home-page: https://github.com/Unleash/unleash-client-python
 Author: Ivan Lee
 Author-email: ivanklee86@gmail.com
 License: UNKNOWN
 Description: # unleash-client-python
         
@@ -115,8 +115,9 @@
 Classifier: Development Status :: 5 - Production/Stable
 Classifier: Intended Audience :: Developers
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10
+Classifier: Programming Language :: Python :: 3.11
 Description-Content-Type: text/markdown
```

### Comparing `UnleashClient-5.5.0/UnleashClient.egg-info/SOURCES.txt` & `UnleashClient-5.6.0/UnleashClient.egg-info/SOURCES.txt`

 * *Files 6% similar despite different names*

```diff
@@ -7,28 +7,32 @@
 Makefile
 README.md
 get-spec.sh
 pyproject.toml
 requirements.txt
 setup.py
 tox.ini
+.devcontainer/Dockerfile
+.devcontainer/devcontainer.json
+.devcontainer/post_install.sh
 .github/PULL_REQUEST_TEMPLATE.md
 .github/dependabot.yml
 .github/stale.yml
 .github/ISSUE_TEMPLATE/bug_report.md
 .github/ISSUE_TEMPLATE/feature_request.md
 .github/workflows/add-to-project.yml
 .github/workflows/codeql-analysis.yml
 .github/workflows/pull_request.yml
 .github/workflows/release-docs.yml
 .github/workflows/release-package.yml
 UnleashClient/__init__.py
 UnleashClient/cache.py
 UnleashClient/constants.py
 UnleashClient/deprecation_warnings.py
+UnleashClient/events.py
 UnleashClient/loader.py
 UnleashClient/py.typed
 UnleashClient/utils.py
 UnleashClient.egg-info/PKG-INFO
 UnleashClient.egg-info/SOURCES.txt
 UnleashClient.egg-info/dependency_links.txt
 UnleashClient.egg-info/not-zip-safe
@@ -61,14 +65,16 @@
 docs/basecache.rst
 docs/celery.rst
 docs/changelog.rst
 docs/conf.py
 docs/customcache.rst
 docs/customstrategies.rst
 docs/development.rst
+docs/eventcallbacks.rst
+docs/events.rst
 docs/filecache.rst
 docs/index.rst
 docs/installation.rst
 docs/make.bat
 docs/strategy.rst
 docs/unleashclient.rst
 docs/usage.rst
```

### Comparing `UnleashClient-5.5.0/docs/Makefile` & `UnleashClient-5.6.0/docs/Makefile`

 * *Files identical despite different names*

### Comparing `UnleashClient-5.5.0/docs/celery.rst` & `UnleashClient-5.6.0/docs/celery.rst`

 * *Files identical despite different names*

### Comparing `UnleashClient-5.5.0/docs/conf.py` & `UnleashClient-5.6.0/docs/conf.py`

 * *Files 3% similar despite different names*

```diff
@@ -27,15 +27,16 @@
 # extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
 # ones.
 extensions = [
     "sphinx.ext.autodoc",
     "sphinx.ext.autosectionlabel",
     "sphinx.ext.autosummary",
     "sphinx.ext.githubpages",
-    "m2r2"
+    "m2r2",
+    "enum_tools.autoenum"
 ]
 
 # Add any paths that contain templates here, relative to this directory.
 templates_path = ['_templates']
 
 # List of patterns, relative to source directory, that match files and
 # directories to ignore when looking for source files.
```

### Comparing `UnleashClient-5.5.0/docs/customcache.rst` & `UnleashClient-5.6.0/docs/customcache.rst`

 * *Files 14% similar despite different names*

```diff
@@ -2,15 +2,15 @@
 Custom Cache
 ****************************************
 
 Implementing a custom cache
 #######################################
 
 - Create a custom cache object by sub-classing the BaseCache object.
-- Overwrite all the methods from the base class.
+- Overwrite all the methods from the base class.  You can also add custom bootstraping methods!
 
 .. code-block:: python
 
     from UnleashClient.cache import BaseCache
     from fcache.cache import FileCache as _Filecache
 
     class FileCache(BaseCache):
```

### Comparing `UnleashClient-5.5.0/docs/customstrategies.rst` & `UnleashClient-5.6.0/docs/customstrategies.rst`

 * *Files identical despite different names*

### Comparing `UnleashClient-5.5.0/docs/development.rst` & `UnleashClient-5.6.0/docs/development.rst`

 * *Files 8% similar despite different names*

```diff
@@ -21,14 +21,18 @@
 #######################################
 1. Install Python versions for each supported version.
 2. Deactivate your local virtualenv (if it's activated).
 3. Run ``pyenv local 3.10.X 3.9.Y 3.8.Z 3.7.12`` (inserting appropriate patch versions).
 4. Run ``make install`` to get latest local dependencies.
 5. Run ``make tox`` to run tox.
 
+Using devcontainer
+###########################################
+This SDK ships with a devcontainer to make local (or cloud!) environment fast & easy!
+
 Upgrading the Client Specification Tests
 ###########################################
 This SDK implements tests for the `Unleash Client Specifications <https://github.com/Unleash/client-specification>`_,
 when adding a new feature set that's covered by the client specs, it's a good idea to also upgrade the client specifications.
 This can be done by updating the ``CLIENT_SPEC_VERSION`` constant found in ``UnleashClient/constants.py``.
 This constant should match the latest tag in the Client Specifications repository.
```

### Comparing `UnleashClient-5.5.0/docs/index.rst` & `UnleashClient-5.6.0/docs/index.rst`

 * *Files 8% similar despite different names*

```diff
@@ -17,27 +17,29 @@
 .. toctree::
     :caption: Advanced
     :maxdepth: 2
     :hidden:
 
     customstrategies
     customcache
+    eventcallbacks
     development
     wsgi
     celery
 
 .. toctree::
     :caption: API Documentation
     :maxdepth: 2
     :hidden:
 
     unleashclient
     strategy
     filecache
     basecache
+    events
 
 .. toctree::
     :caption: Changelog
     :maxdepth: 2
     :hidden:
 
     changelog
```

### Comparing `UnleashClient-5.5.0/docs/make.bat` & `UnleashClient-5.6.0/docs/make.bat`

 * *Files identical despite different names*

### Comparing `UnleashClient-5.5.0/docs/usage.rst` & `UnleashClient-5.6.0/docs/usage.rst`

 * *Files identical despite different names*

### Comparing `UnleashClient-5.5.0/docs/wsgi.rst` & `UnleashClient-5.6.0/docs/wsgi.rst`

 * *Files identical despite different names*

### Comparing `UnleashClient-5.5.0/pyproject.toml` & `UnleashClient-5.6.0/pyproject.toml`

 * *Files identical despite different names*

### Comparing `UnleashClient-5.5.0/setup.py` & `UnleashClient-5.6.0/setup.py`

 * *Files 8% similar despite different names*

```diff
@@ -18,15 +18,15 @@
     url='https://github.com/Unleash/unleash-client-python',
     packages=find_packages(exclude=["tests*"]),
     package_data={"UnleashClient": ["py.typed"]},
     install_requires=[
         "requests",
         "fcache",
         "mmhash3",
-        "apscheduler",
+        "apscheduler < 4.0.0",
         "importlib_metadata",
         "python-dateutil",
         "semver < 3.0.0"
     ],
     setup_requires=['setuptools_scm'],
     zip_safe=False,
     include_package_data=True,
@@ -34,9 +34,10 @@
         "Development Status :: 5 - Production/Stable",
         "Intended Audience :: Developers",
         "License :: OSI Approved :: MIT License",
         "Programming Language :: Python :: 3.7",
         "Programming Language :: Python :: 3.8",
         "Programming Language :: Python :: 3.9",
         "Programming Language :: Python :: 3.10",
+        "Programming Language :: Python :: 3.11"
     ]
 )
```

### Comparing `UnleashClient-5.5.0/tests/conftest.py` & `UnleashClient-5.6.0/tests/conftest.py`

 * *Files identical despite different names*

### Comparing `UnleashClient-5.5.0/tests/integration_tests/integration.py` & `UnleashClient-5.6.0/tests/integration_tests/integration.py`

 * *Files identical despite different names*

### Comparing `UnleashClient-5.5.0/tests/integration_tests/integration_gitlab.py` & `UnleashClient-5.6.0/tests/integration_tests/integration_gitlab.py`

 * *Files identical despite different names*

### Comparing `UnleashClient-5.5.0/tests/integration_tests/integration_unleashheroku.py` & `UnleashClient-5.6.0/tests/integration_tests/integration_unleashheroku.py`

 * *Files identical despite different names*

### Comparing `UnleashClient-5.5.0/tests/integration_tests/integration_unleashhosted.py` & `UnleashClient-5.6.0/tests/integration_tests/integration_unleashhosted.py`

 * *Files identical despite different names*

### Comparing `UnleashClient-5.5.0/tests/specification_tests/test_client_specs.py` & `UnleashClient-5.6.0/tests/specification_tests/test_client_specs.py`

 * *Files identical despite different names*

### Comparing `UnleashClient-5.5.0/tests/unit_tests/api/test_feature.py` & `UnleashClient-5.6.0/tests/unit_tests/api/test_feature.py`

 * *Files identical despite different names*

### Comparing `UnleashClient-5.5.0/tests/unit_tests/api/test_metrics.py` & `UnleashClient-5.6.0/tests/unit_tests/api/test_metrics.py`

 * *Files identical despite different names*

### Comparing `UnleashClient-5.5.0/tests/unit_tests/api/test_register.py` & `UnleashClient-5.6.0/tests/unit_tests/api/test_register.py`

 * *Files identical despite different names*

### Comparing `UnleashClient-5.5.0/tests/unit_tests/periodic/test_aggregate_and_send_metrics.py` & `UnleashClient-5.6.0/tests/unit_tests/periodic/test_aggregate_and_send_metrics.py`

 * *Files identical despite different names*

### Comparing `UnleashClient-5.5.0/tests/unit_tests/periodic/test_fetch_and_load.py` & `UnleashClient-5.6.0/tests/unit_tests/periodic/test_fetch_and_load.py`

 * *Files identical despite different names*

### Comparing `UnleashClient-5.5.0/tests/unit_tests/strategies/test_flexiblerollout.py` & `UnleashClient-5.6.0/tests/unit_tests/strategies/test_flexiblerollout.py`

 * *Files identical despite different names*

### Comparing `UnleashClient-5.5.0/tests/unit_tests/strategies/test_remoteaddress.py` & `UnleashClient-5.6.0/tests/unit_tests/strategies/test_remoteaddress.py`

 * *Files identical despite different names*

### Comparing `UnleashClient-5.5.0/tests/unit_tests/test_client.py` & `UnleashClient-5.6.0/tests/unit_tests/test_client.py`

 * *Files 4% similar despite different names*

```diff
@@ -3,24 +3,27 @@
 import warnings
 from pathlib import Path
 
 import pytest
 import responses
 from apscheduler.schedulers.background import BackgroundScheduler
 from apscheduler.executors.pool import ThreadPoolExecutor
+from blinker import signal
+
 from UnleashClient import UnleashClient, INSTANCES
 from UnleashClient.strategies import Strategy
 from UnleashClient.utils import InstanceAllowType
 from tests.utilities.testing_constants import URL, ENVIRONMENT, APP_NAME, INSTANCE_ID, REFRESH_INTERVAL, REFRESH_JITTER, \
     METRICS_INTERVAL, METRICS_JITTER, DISABLE_METRICS, DISABLE_REGISTRATION, CUSTOM_HEADERS, CUSTOM_OPTIONS, PROJECT_NAME, PROJECT_URL, \
     ETAG_VALUE
 from tests.utilities.mocks.mock_features import MOCK_FEATURE_RESPONSE, MOCK_FEATURE_RESPONSE_PROJECT
 from tests.utilities.mocks.mock_all_features import MOCK_ALL_FEATURES
 from UnleashClient.constants import REGISTER_URL, FEATURES_URL, METRICS_URL
 from UnleashClient.cache import FileCache
+from UnleashClient.events import UnleashEvent, UnleashEventType
 
 
 class EnvironmentStrategy(Strategy):
     def load_provisioning(self) -> list:
         return [x.strip() for x in self.parameters["environments"].split(',')]
 
     def apply(self, context: dict = None) -> bool:
@@ -570,7 +573,53 @@
     assert not all(["Multiple instances has been disabled" in r.msg for r in caplog.records])
 
 
 def test_multiple_instances_are_unique_on_api_key(caplog):
     UnleashClient(URL, "some-probably-unique-app-name", custom_headers={"Authorization": "penguins"})
     UnleashClient(URL, "some-probably-unique-app-name", custom_headers={"Authorization": "hamsters"})
     assert not all(["Multiple instances has been disabled" in r.msg for r in caplog.records])
+
+
+@responses.activate
+def test_signals_feature_flag(cache):
+    # Set up API
+    responses.add(responses.POST, URL + REGISTER_URL, json={}, status=202)
+    responses.add(responses.GET, URL + FEATURES_URL, json=MOCK_FEATURE_RESPONSE, status=200)
+    responses.add(responses.POST, URL + METRICS_URL, json={}, status=202)
+
+    # Set up signals
+    send_data = signal('send-data')
+
+    @send_data.connect
+    def receive_data(sender, **kw):
+        print("Caught signal from %r, data %r" % (sender, kw))
+
+        if kw['data'].event_type == UnleashEventType.FEATURE_FLAG:
+            assert kw['data'].feature_name == 'testFlag'
+            assert kw['data'].enabled
+        elif kw['data'].event_type == UnleashEventType.VARIANT:
+            assert kw['data'].feature_name == 'testVariations'
+            assert kw['data'].enabled
+            assert kw['data'].variant == 'VarA'
+
+        raise Exception("Random!")
+
+    def example_callback(event: UnleashEvent):
+        send_data.send('anonymous', data=event)
+
+    # Set up Unleash
+    unleash_client = UnleashClient(
+        URL,
+        APP_NAME,
+        refresh_interval=REFRESH_INTERVAL,
+        metrics_interval=METRICS_INTERVAL,
+        cache=cache,
+        event_callback=example_callback
+    )
+
+    # Create Unleash client and check initial load
+    unleash_client.initialize_client()
+    time.sleep(1)
+
+    assert unleash_client.is_enabled("testFlag")
+    variant = unleash_client.get_variant("testVariations", context={'userId': '2'})
+    assert variant['name'] == 'VarA'
```

### Comparing `UnleashClient-5.5.0/tests/unit_tests/test_constraints.py` & `UnleashClient-5.6.0/tests/unit_tests/test_constraints.py`

 * *Files identical despite different names*

### Comparing `UnleashClient-5.5.0/tests/unit_tests/test_custom_strategy.py` & `UnleashClient-5.6.0/tests/unit_tests/test_custom_strategy.py`

 * *Files identical despite different names*

### Comparing `UnleashClient-5.5.0/tests/unit_tests/test_features.py` & `UnleashClient-5.6.0/tests/unit_tests/test_features.py`

 * *Files 5% similar despite different names*

```diff
@@ -28,14 +28,15 @@
 
     CONTEXT["remoteAddress"] = "69.208.0.1"
     assert my_feature.is_enabled(CONTEXT)
     assert my_feature.yes_count == 1
 
     my_feature.reset_stats()
     assert my_feature.yes_count == 0
+    assert not my_feature.impression_data
 
 
 def test_create_feature_false(test_feature):
     my_feature = test_feature
 
     CONTEXT["remoteAddress"] = "1.208.0.1"
     CONTEXT["userId"] = "random@random.com"
```

### Comparing `UnleashClient-5.5.0/tests/unit_tests/test_loader.py` & `UnleashClient-5.6.0/tests/unit_tests/test_loader.py`

 * *Files 2% similar despite different names*

```diff
@@ -32,14 +32,16 @@
 
         if isinstance(strategy, FlexibleRollout):
             len(list(strategy.parsed_constraints)) > 0
 
         if isinstance(strategy, Variants):
             assert strategy.variants
 
+        assert feature.impression_data is False
+
 
 def test_loader_refresh_strategies(cache_full):  # noqa: F811
     # Set up variables
     in_memory_features = {}
     temp_cache = cache_full
 
     load_features(temp_cache, in_memory_features, DEFAULT_STRATEGY_MAPPING)
```

### Comparing `UnleashClient-5.5.0/tests/unit_tests/test_variants.py` & `UnleashClient-5.6.0/tests/unit_tests/test_variants.py`

 * *Files identical despite different names*

### Comparing `UnleashClient-5.5.0/tests/utilities/mocks/mock_all_features.py` & `UnleashClient-5.6.0/tests/utilities/mocks/mock_all_features.py`

 * *Files 27% similar despite different names*

```diff
@@ -1,214 +1,223 @@
-MOCK_ALL_FEATURES = \
-{
-  "version": 1,
-  "features": [
-    {
-      "name": "ApplicationHostname",
-      "description": "Application Hostname strategy",
-      "enabled": True,
-      "strategies": [
-        {
-          "name": "applicationHostname",
-          "parameters": {
-            "hostNames": "iMacPro.local,test1,test2"
-          }
-        }
-      ],
-      "createdAt": "2018-10-09T06:05:14.757Z"
-    },
-    {
-      "name": "Default",
-      "description": "Default feature toggle",
-      "enabled": True,
-      "strategies": [
-        {
-          "name": "default",
-          "parameters": {}
-        }
-      ],
-      "createdAt": "2018-10-09T06:04:05.667Z"
-    },
-    {
-      "name": "GradualRolloutRandom",
-      "description": "Gradual Rollout Random example",
-      "enabled": True,
-      "strategies": [
-        {
-          "name": "gradualRolloutRandom",
-          "parameters": {
-            "percentage": 50
-          }
-        }
-      ],
-      "createdAt": "2018-10-09T06:05:37.637Z"
-    },
-    {
-      "name": "GradualRolloutSessionId",
-      "description": "SessionID check!",
-      "enabled": True,
-      "strategies": [
-        {
-          "name": "gradualRolloutSessionId",
-          "parameters": {
-            "percentage": 50,
-            "groupId": "GradualRolloutSessionId"
-          }
-        }
-      ],
-      "createdAt": "2018-10-09T06:06:51.057Z"
-    },
-    {
-      "name": "GradualRolloutUserID",
-      "description": "GradualRolloutUserID strategy",
-      "enabled": True,
-      "strategies": [
-        {
-          "name": "gradualRolloutUserId",
-          "parameters": {
-            "percentage": 50,
-            "groupId": "GradualRolloutUserID"
-          }
-        }
-      ],
-      "createdAt": "2018-10-09T06:07:17.520Z"
-    },
-    {
-      "name": "RemoteAddress",
-      "description": "RemoteAddress strategies",
-      "enabled": True,
-      "strategies": [
-        {
-          "name": "remoteAddress",
-          "parameters": {
-            "IPs": "69.208.0.0/29,70.208.1.1,2001:db8:1234::/48,2002:db8:1234:0000:0000:0000:0000:0001"
-          }
-        }
-      ],
-      "createdAt": "2018-10-09T06:08:42.398Z"
-    },
-    {
-      "name": "UserWithId",
-      "description": "UserWithId strategies",
-      "enabled": True,
-      "strategies": [
-        {
-          "name": "userWithId",
-          "parameters": {
-            "userIds": "meep@meep.com,test@test.com,wat@wat.com"
-          }
-        }
-      ],
-      "createdAt": "2018-10-09T06:09:19.203Z"
-    },
-    {
-      "name": "FlexibleRollout",
-      "description": "FlexibleRollout strategies",
-      "enabled": True,
-      "strategies": [
-        {
-          "name": "flexibleRollout",
-          "parameters": {
-            "rollout": "21",
-            "stickiness": "userId",
-            "groupId": "ivantest"
-          },
-          "constraints": [
-            {
-              "contextName": "environment",
-              "operator": "IN",
-              "values": [
-                "staging",
-                "prod"
-              ]
-            },
-            {
-              "contextName": "userId",
-              "operator": "NOT_IN",
-              "values": [
-                "1",
-                "2",
-                "3"
-              ]
-            },
-            {
-              "contextName": "userId",
-              "operator": "IN",
-              "values": [
-                "4",
-                "5",
-                "6"
-              ]
-            },
-            {
-              "contextName": "appName",
-              "operator": "IN",
-              "values": [
-                "test"
-              ]
-            }
-          ]
-        }
-      ],
-      "variants": None,
-      "createdAt": "2019-10-05T07:30:29.896Z"
-    },
-    {
-      "name": "Variations",
-      "description": "Test variation",
-      "enabled": True,
-      "strategies": [
-          {
-              "name": "default"
-          }
-      ],
-      "variants": [
-          {
-              "name": "VarA",
-              "weight": 34,
-              "payload": {
-                  "type": "string",
-                  "value": "Test1"
-              },
-              "overrides": [
-                  {
-                      "contextName": "userId",
-                      "values": [
-                          "ivanklee86@gmail.com",
-                          "ivan@aaptiv.com"
-                      ]
-                  }
-              ]
-          },
-          {
-              "name": "VarB",
-              "weight": 33,
-              "payload": {
-                  "type": "string",
-                  "value": "Test 2"
-              }
-          },
-          {
-              "name": "VarC",
-              "weight": 33,
-              "payload": {
-                  "type": "string",
-                  "value": "Test 3"
-              }
-          }
-      ],
-      "createdAt": "2019-10-25T13:22:02.035Z"
-  },
-  {
-    "name": "Garbage",
-    "description": "Invalid strategy",
-    "enabled": True,
-    "strategies": [
-      {
-        "name": "blargwatisdis",
-        "parameters": {}
-      }
-    ],
-    "createdAt": "2018-10-09T06:04:05.667Z"
-  },
-  ]
+MOCK_ALL_FEATURES = {
+    "version": 1,
+    "features": [
+        {
+            "name": "ApplicationHostname",
+            "description": "Application Hostname strategy",
+            "enabled": True,
+            "strategies": [
+                {
+                    "name": "applicationHostname",
+                    "parameters": {
+                        "hostNames": "iMacPro.local,test1,test2"
+                    }
+                }
+            ],
+            "createdAt": "2018-10-09T06:05:14.757Z",
+            "impressionData": False
+        },
+        {
+            "name": "Default",
+            "description": "Default feature toggle",
+            "enabled": True,
+            "strategies": [
+                {
+                    "name": "default",
+                    "parameters": {}
+                }
+            ],
+            "createdAt": "2018-10-09T06:04:05.667Z",
+            "impressionData": False
+        },
+        {
+            "name": "GradualRolloutRandom",
+            "description": "Gradual Rollout Random example",
+            "enabled": True,
+            "strategies": [
+                {
+                    "name": "gradualRolloutRandom",
+                    "parameters": {
+                        "percentage": 50
+                    }
+                }
+            ],
+            "createdAt": "2018-10-09T06:05:37.637Z",
+            "impressionData": False
+        },
+        {
+            "name": "GradualRolloutSessionId",
+            "description": "SessionID check!",
+            "enabled": True,
+            "strategies": [
+                {
+                    "name": "gradualRolloutSessionId",
+                    "parameters": {
+                        "percentage": 50,
+                        "groupId": "GradualRolloutSessionId"
+                    }
+                }
+            ],
+            "createdAt": "2018-10-09T06:06:51.057Z",
+            "impressionData": False
+        },
+        {
+            "name": "GradualRolloutUserID",
+            "description": "GradualRolloutUserID strategy",
+            "enabled": True,
+            "strategies": [
+                {
+                    "name": "gradualRolloutUserId",
+                    "parameters": {
+                        "percentage": 50,
+                        "groupId": "GradualRolloutUserID"
+                    }
+                }
+            ],
+            "createdAt": "2018-10-09T06:07:17.520Z",
+            "impressionData": False
+        },
+        {
+            "name": "RemoteAddress",
+            "description": "RemoteAddress strategies",
+            "enabled": True,
+            "strategies": [
+                {
+                    "name": "remoteAddress",
+                    "parameters": {
+                        "IPs": "69.208.0.0/29,70.208.1.1,2001:db8:1234::/48,2002:db8:1234:0000:0000:0000:0000:0001"
+                    }
+                }
+            ],
+            "createdAt": "2018-10-09T06:08:42.398Z",
+            "impressionData": False
+        },
+        {
+            "name": "UserWithId",
+            "description": "UserWithId strategies",
+            "enabled": True,
+            "strategies": [
+                {
+                    "name": "userWithId",
+                    "parameters": {
+                        "userIds": "meep@meep.com,test@test.com,wat@wat.com"
+                    }
+                }
+            ],
+            "createdAt": "2018-10-09T06:09:19.203Z",
+            "impressionData": False
+        },
+        {
+            "name": "FlexibleRollout",
+            "description": "FlexibleRollout strategies",
+            "enabled": True,
+            "strategies": [
+                {
+                    "name": "flexibleRollout",
+                    "parameters": {
+                        "rollout": "21",
+                        "stickiness": "userId",
+                        "groupId": "ivantest"
+                    },
+                    "constraints": [
+                        {
+                            "contextName": "environment",
+                            "operator": "IN",
+                            "values": [
+                                "staging",
+                                "prod"
+                            ]
+                        },
+                        {
+                            "contextName": "userId",
+                            "operator": "NOT_IN",
+                            "values": [
+                                "1",
+                                "2",
+                                "3"
+                            ]
+                        },
+                        {
+                            "contextName": "userId",
+                            "operator": "IN",
+                            "values": [
+                                "4",
+                                "5",
+                                "6"
+                            ]
+                        },
+                        {
+                            "contextName": "appName",
+                            "operator": "IN",
+                            "values": [
+                                "test"
+                            ]
+                        }
+                    ]
+                }
+            ],
+            "variants": None,
+            "createdAt": "2019-10-05T07:30:29.896Z",
+            "impressionData": False
+        },
+        {
+            "name": "Variations",
+            "description": "Test variation",
+            "enabled": True,
+            "strategies": [
+                {
+                    "name": "default"
+                }
+            ],
+            "variants": [
+                {
+                    "name": "VarA",
+                    "weight": 34,
+                    "payload": {
+                        "type": "string",
+                        "value": "Test1"
+                    },
+                    "overrides": [
+                        {
+                            "contextName": "userId",
+                            "values": [
+                                "ivanklee86@gmail.com",
+                                "ivan@aaptiv.com"
+                            ]
+                        }
+                    ]
+                },
+                {
+                    "name": "VarB",
+                    "weight": 33,
+                    "payload": {
+                        "type": "string",
+                        "value": "Test 2"
+                    }
+                },
+                {
+                    "name": "VarC",
+                    "weight": 33,
+                    "payload": {
+                        "type": "string",
+                        "value": "Test 3"
+                    }
+                }
+            ],
+            "createdAt": "2019-10-25T13:22:02.035Z",
+            "impressionData": False
+        },
+        {
+            "name": "Garbage",
+            "description": "Invalid strategy",
+            "enabled": True,
+            "strategies": [
+                {
+                    "name": "blargwatisdis",
+                    "parameters": {}
+                }
+            ],
+            "createdAt": "2018-10-09T06:04:05.667Z",
+            "impressionData": False
+        },
+    ]
 }
```

### Comparing `UnleashClient-5.5.0/tests/utilities/mocks/mock_constraints.py` & `UnleashClient-5.6.0/tests/utilities/mocks/mock_constraints.py`

 * *Files identical despite different names*

### Comparing `UnleashClient-5.5.0/tests/utilities/mocks/mock_custom_strategy.py` & `UnleashClient-5.6.0/tests/utilities/mocks/mock_custom_strategy.py`

 * *Files 9% similar despite different names*

```diff
@@ -1,75 +1,79 @@
 MOCK_CUSTOM_STRATEGY = {
-  "version": 1,
-  "features": [
-    {
-      "name": "CustomToggle",
-      "description": "CustomToggle Test",
-      "enabled": True,
-      "strategies": [
+    "version": 1,
+    "features": [
         {
-          "name": "amIACat",
-          "parameters": {
-            "sound": "meow,nyaa"
-          },
-          "constraints": [
-            {
-              "contextName": "environment",
-              "operator": "IN",
-              "values": [
-                "staging",
-                "prod"
-              ]
-            }
-          ]
-        }
-      ],
-      "createdAt": "2018-10-13T10:15:29.009Z"
-    },
-    {
-      "name": "CustomToggleWarning",
-      "description": "CustomToggle Warning Test",
-      "enabled": True,
-      "strategies": [
-        {
-          "name": "amIADog",
-          "parameters": {
-            "sound": "arf,bark"
-          }
-        }
-      ],
-      "createdAt": "2018-10-13T10:15:29.009Z"
-    },
-    {
-      "name": "CustomToggleWarningMultiStrat",
-      "description": "CustomToggle Warning Test",
-      "enabled": True,
-      "strategies": [
+            "name": "CustomToggle",
+            "description": "CustomToggle Test",
+            "enabled": True,
+            "strategies": [
+                {
+                    "name": "amIACat",
+                    "parameters": {
+                        "sound": "meow,nyaa"
+                    },
+                    "constraints": [
+                        {
+                            "contextName": "environment",
+                            "operator": "IN",
+                            "values": [
+                                "staging",
+                                "prod"
+                            ]
+                        }
+                    ]
+                }
+            ],
+            "createdAt": "2018-10-13T10:15:29.009Z",
+            "impressionData": False
+        },
         {
-          "name": "amIADog",
-          "parameters": {
-            "sound": "arf,bark"
-          }
+            "name": "CustomToggleWarning",
+            "description": "CustomToggle Warning Test",
+            "enabled": True,
+            "strategies": [
+                {
+                    "name": "amIADog",
+                    "parameters": {
+                        "sound": "arf,bark"
+                    }
+                }
+            ],
+            "createdAt": "2018-10-13T10:15:29.009Z",
+            "impressionData": False
         },
         {
-          "name": "default",
-          "parameters": {}
-        }
-      ],
-      "createdAt": "2018-10-13T10:15:29.009Z"
-    },
-    {
-      "name": "UserWithId",
-      "description": "UserWithId",
-      "enabled": True,
-      "strategies": [
+            "name": "CustomToggleWarningMultiStrat",
+            "description": "CustomToggle Warning Test",
+            "enabled": True,
+            "strategies": [
+                {
+                    "name": "amIADog",
+                    "parameters": {
+                        "sound": "arf,bark"
+                    }
+                },
+                {
+                    "name": "default",
+                    "parameters": {}
+                }
+            ],
+            "createdAt": "2018-10-13T10:15:29.009Z",
+            "impressionData": False
+        },
         {
-          "name": "userWithId",
-          "parameters": {
-            "userIds": "meep@meep.com,test@test.com,ivan@ivan.com"
-          }
+            "name": "UserWithId",
+            "description": "UserWithId",
+            "enabled": True,
+            "strategies": [
+                {
+                    "name": "userWithId",
+                    "parameters": {
+                        "userIds": "meep@meep.com,test@test.com,ivan@ivan.com"
+                    }
+                }
+            ],
+            "createdAt": "2018-10-11T09:33:51.171Z",
+            "impressionData": False
         }
-      ],
-      "createdAt": "2018-10-11T09:33:51.171Z"
-    }
-  ]
+    ]
 }
```

### Comparing `UnleashClient-5.5.0/tests/utilities/mocks/mock_features.py` & `UnleashClient-5.6.0/tests/utilities/mocks/mock_features.py`

 * *Files 21% similar despite different names*

```diff
@@ -7,43 +7,46 @@
             "enabled": True,
             "strategies": [
                 {
                     "name": "default",
                     "parameters": {}
                 }
             ],
-            "createdAt": "2018-10-04T01:27:28.477Z"
+            "createdAt": "2018-10-04T01:27:28.477Z",
+            "impressionData": True
         },
         {
             "name": "testFlag2",
             "description": "Test flag 2",
             "enabled": True,
             "strategies": [
                 {
                     "name": "gradualRolloutRandom",
                     "parameters": {
                         "percentage": 50
                     }
                 }
             ],
-            "createdAt": "2018-10-04T11:03:56.062Z"
+            "createdAt": "2018-10-04T11:03:56.062Z",
+            "impressionData": False
         },
         {
             "name": "testContextFlag",
             "description": "This is a test for static context fileds!",
             "enabled": True,
             "strategies": [
                 {
                     "name": "custom-context",
                     "parameters": {
                         "environments": "prod"
                     }
                 }
             ],
-            "createdAt": "2018-10-04T01:27:28.477Z"
+            "createdAt": "2018-10-04T01:27:28.477Z",
+            "impressionData": False
         },
         {
             "name": "testConstraintFlag",
             "description": "This is a flag with a constraint!",
             "enabled": True,
             "strategies": [
                 {
@@ -55,65 +58,67 @@
                             "operator": "DATE_BEFORE",
                             "value": "2022-01-22T00:00:00.000Z",
                             "inverted": False
                         }
                     ],
                 },
             ],
-            "createdAt": "2018-10-04T01:27:28.477Z"
+            "createdAt": "2018-10-04T01:27:28.477Z",
+            "impressionData": False
         },
         {
-          "name": "testVariations",
-          "description": "Test variation",
-          "enabled": True,
-          "strategies": [
-              {
-                  "name": "userWithId",
-                  "parameters": {
-                      "userIds": "2"
-                  }
-              }
-          ],
-          "variants": [
-              {
-                  "name": "VarA",
-                  "weight": 34,
-                  "payload": {
-                      "type": "string",
-                      "value": "Test1"
-                  },
-                  "overrides": [
-                      {
-                          "contextName": "userId",
-                          "values": [
-                              "ivanklee86@gmail.com",
-                              "ivan@aaptiv.com"
-                          ]
-                      }
-                  ]
-              },
-              {
-                  "name": "VarB",
-                  "weight": 33,
-                  "payload": {
-                      "type": "string",
-                      "value": "Test 2"
-                  }
-              },
-              {
-                  "name": "VarC",
-                  "weight": 33,
-                  "payload": {
-                      "type": "string",
-                      "value": "Test 3"
-                  }
-              }
-          ],
-          "createdAt": "2019-10-25T13:22:02.035Z"
-      }
+            "name": "testVariations",
+            "description": "Test variation",
+            "enabled": True,
+            "strategies": [
+                {
+                    "name": "userWithId",
+                    "parameters": {
+                        "userIds": "2"
+                    }
+                }
+            ],
+            "variants": [
+                {
+                    "name": "VarA",
+                    "weight": 34,
+                    "payload": {
+                        "type": "string",
+                        "value": "Test1"
+                    },
+                    "overrides": [
+                        {
+                            "contextName": "userId",
+                            "values": [
+                                "ivanklee86@gmail.com",
+                                "ivan@aaptiv.com"
+                            ]
+                        }
+                    ]
+                },
+                {
+                    "name": "VarB",
+                    "weight": 33,
+                    "payload": {
+                        "type": "string",
+                        "value": "Test 2"
+                    }
+                },
+                {
+                    "name": "VarC",
+                    "weight": 33,
+                    "payload": {
+                        "type": "string",
+                        "value": "Test 3"
+                    }
+                }
+            ],
+            "createdAt": "2019-10-25T13:22:02.035Z",
+            "impressionData": True
+        }
     ]
 }
 
 MOCK_FEATURES_WITH_SEGMENTS_RESPONSE = {
     "version": 2,
     "features": [
         {
@@ -128,15 +133,14 @@
                 }
             ],
             "impressionData": False,
             "enabled": True,
             "name": "Test",
             "description": "",
             "project": "default",
-            "stale": False,
             "type": "release",
             "variants": []
         }
     ],
     "query": {
         "environment": "development",
         "inlineSegmentConstraints": False
@@ -176,28 +180,29 @@
             "createdBy": "admin",
             "createdAt": "2022-06-14T06:40:25.331Z"
         }
     ]
 }
 
 MOCK_FEATURE_RESPONSE_PROJECT = {
-   "version":1,
-   "features":[
-      {
-         "name":"ivan-project",
-         "type":"release",
-         "enabled": True,
-         "stale": False,
-         "strategies":[
-            {
-               "name":"default",
-               "parameters":{
+    "version": 1,
+    "features": [
+        {
+            "name": "ivan-project",
+            "type": "release",
+            "enabled": True,
+            "strategies": [
+                {
+                    "name": "default",
+                    "parameters": {
 
-               }
-            }
-         ],
-         "variants":[
+                    }
+                }
+            ],
+            "variants": [
 
-         ]
-      }
-   ]
-}
+            ],
+            "createdAt": "2023-01-24T06:40:25.331Z",
+            "impressionData": False
+        }
+    ]
+}
```

### Comparing `UnleashClient-5.5.0/tests/utilities/mocks/mock_variants.py` & `UnleashClient-5.6.0/tests/utilities/mocks/mock_variants.py`

 * *Files identical despite different names*

### Comparing `UnleashClient-5.5.0/tests/utilities/old_code/StrategyV2.py` & `UnleashClient-5.6.0/tests/utilities/old_code/StrategyV2.py`

 * *Files identical despite different names*

### Comparing `UnleashClient-5.5.0/tests/utilities/testing_constants.py` & `UnleashClient-5.6.0/tests/utilities/testing_constants.py`

 * *Files identical despite different names*

