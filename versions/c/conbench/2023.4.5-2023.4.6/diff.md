# Comparing `tmp/conbench-2023.4.5.tar.gz` & `tmp/conbench-2023.4.6.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "conbench-2023.4.5.tar", last modified: Wed Apr  5 15:19:44 2023, max compression
+gzip compressed data, was "conbench-2023.4.6.tar", last modified: Thu Apr  6 16:04:24 2023, max compression
```

## Comparing `conbench-2023.4.5.tar` & `conbench-2023.4.6.tar`

### file list

```diff
@@ -1,133 +1,134 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 15:19:44.333168 conbench-2023.4.5/
--rw-r--r--   0 runner    (1001) docker     (123)     1071 2023-04-05 15:19:23.000000 conbench-2023.4.5/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)      127 2023-04-05 15:19:23.000000 conbench-2023.4.5/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)    35621 2023-04-05 15:19:44.333168 conbench-2023.4.5/PKG-INFO
--rwxr-xr-x   0 runner    (1001) docker     (123)    35165 2023-04-05 15:19:23.000000 conbench-2023.4.5/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 15:19:44.305168 conbench-2023.4.5/conbench/
--rwxr-xr-x   0 runner    (1001) docker     (123)     8486 2023-04-05 15:19:23.000000 conbench-2023.4.5/conbench/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)       64 2023-04-05 15:19:30.000000 conbench-2023.4.5/conbench/_version.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 15:19:44.309168 conbench-2023.4.5/conbench/api/
--rw-r--r--   0 runner    (1001) docker     (123)      781 2023-04-05 15:19:23.000000 conbench-2023.4.5/conbench/api/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4779 2023-04-05 15:19:23.000000 conbench-2023.4.5/conbench/api/_docs.py
--rw-r--r--   0 runner    (1001) docker     (123)     2607 2023-04-05 15:19:23.000000 conbench-2023.4.5/conbench/api/_endpoint.py
--rw-r--r--   0 runner    (1001) docker     (123)     1095 2023-04-05 15:19:23.000000 conbench-2023.4.5/conbench/api/_errors.py
--rw-r--r--   0 runner    (1001) docker     (123)    20069 2023-04-05 15:19:23.000000 conbench-2023.4.5/conbench/api/_examples.py
--rw-r--r--   0 runner    (1001) docker     (123)    11634 2023-04-05 15:19:23.000000 conbench-2023.4.5/conbench/api/_google.py
--rw-r--r--   0 runner    (1001) docker     (123)     3673 2023-04-05 15:19:23.000000 conbench-2023.4.5/conbench/api/auth.py
--rw-r--r--   0 runner    (1001) docker     (123)     1796 2023-04-05 15:19:23.000000 conbench-2023.4.5/conbench/api/commits.py
--rw-r--r--   0 runner    (1001) docker     (123)    10360 2023-04-05 15:19:23.000000 conbench-2023.4.5/conbench/api/compare.py
--rw-r--r--   0 runner    (1001) docker     (123)     1642 2023-04-05 15:19:23.000000 conbench-2023.4.5/conbench/api/contexts.py
--rw-r--r--   0 runner    (1001) docker     (123)     1676 2023-04-05 15:19:23.000000 conbench-2023.4.5/conbench/api/hardware.py
--rw-r--r--   0 runner    (1001) docker     (123)     1603 2023-04-05 15:19:23.000000 conbench-2023.4.5/conbench/api/history.py
--rwxr-xr-x   0 runner    (1001) docker     (123)     7038 2023-04-05 15:19:23.000000 conbench-2023.4.5/conbench/api/index.py
--rw-r--r--   0 runner    (1001) docker     (123)     1539 2023-04-05 15:19:23.000000 conbench-2023.4.5/conbench/api/info.py
--rw-r--r--   0 runner    (1001) docker     (123)    11748 2023-04-05 15:19:23.000000 conbench-2023.4.5/conbench/api/results.py
--rw-r--r--   0 runner    (1001) docker     (123)     4114 2023-04-05 15:19:23.000000 conbench-2023.4.5/conbench/api/runs.py
--rw-r--r--   0 runner    (1001) docker     (123)     5269 2023-04-05 15:19:23.000000 conbench-2023.4.5/conbench/api/users.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 15:19:44.313168 conbench-2023.4.5/conbench/app/
--rw-r--r--   0 runner    (1001) docker     (123)      879 2023-04-05 15:19:23.000000 conbench-2023.4.5/conbench/app/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     7219 2023-04-05 15:19:23.000000 conbench-2023.4.5/conbench/app/_endpoint.py
--rw-r--r--   0 runner    (1001) docker     (123)    29408 2023-04-05 15:19:23.000000 conbench-2023.4.5/conbench/app/_plots.py
--rw-r--r--   0 runner    (1001) docker     (123)     1915 2023-04-05 15:19:23.000000 conbench-2023.4.5/conbench/app/_util.py
--rw-r--r--   0 runner    (1001) docker     (123)     5659 2023-04-05 15:19:23.000000 conbench-2023.4.5/conbench/app/auth.py
--rw-r--r--   0 runner    (1001) docker     (123)     2453 2023-04-05 15:19:23.000000 conbench-2023.4.5/conbench/app/batches.py
--rw-r--r--   0 runner    (1001) docker     (123)     8754 2023-04-05 15:19:23.000000 conbench-2023.4.5/conbench/app/compare.py
--rw-r--r--   0 runner    (1001) docker     (123)     1896 2023-04-05 15:19:23.000000 conbench-2023.4.5/conbench/app/hardware.py
--rwxr-xr-x   0 runner    (1001) docker     (123)     4476 2023-04-05 15:19:23.000000 conbench-2023.4.5/conbench/app/index.py
--rw-r--r--   0 runner    (1001) docker     (123)    13774 2023-04-05 15:19:23.000000 conbench-2023.4.5/conbench/app/results.py
--rw-r--r--   0 runner    (1001) docker     (123)      649 2023-04-05 15:19:23.000000 conbench-2023.4.5/conbench/app/robots.py
--rw-r--r--   0 runner    (1001) docker     (123)     3718 2023-04-05 15:19:23.000000 conbench-2023.4.5/conbench/app/runs.py
--rw-r--r--   0 runner    (1001) docker     (123)     5392 2023-04-05 15:19:23.000000 conbench-2023.4.5/conbench/app/users.py
--rw-r--r--   0 runner    (1001) docker     (123)     1336 2023-04-05 15:19:23.000000 conbench-2023.4.5/conbench/buildinfo.py
--rwxr-xr-x   0 runner    (1001) docker     (123)     5151 2023-04-05 15:19:23.000000 conbench-2023.4.5/conbench/cli.py
--rw-r--r--   0 runner    (1001) docker     (123)     5573 2023-04-05 15:19:23.000000 conbench-2023.4.5/conbench/config.py
--rw-r--r--   0 runner    (1001) docker     (123)     5198 2023-04-05 15:19:23.000000 conbench-2023.4.5/conbench/db.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 15:19:44.317168 conbench-2023.4.5/conbench/entities/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-05 15:19:23.000000 conbench-2023.4.5/conbench/entities/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     9192 2023-04-05 15:19:23.000000 conbench-2023.4.5/conbench/entities/_comparator.py
--rw-r--r--   0 runner    (1001) docker     (123)     4919 2023-04-05 15:19:23.000000 conbench-2023.4.5/conbench/entities/_entity.py
--rw-r--r--   0 runner    (1001) docker     (123)    32531 2023-04-05 15:19:23.000000 conbench-2023.4.5/conbench/entities/benchmark_result.py
--rw-r--r--   0 runner    (1001) docker     (123)      469 2023-04-05 15:19:23.000000 conbench-2023.4.5/conbench/entities/case.py
--rw-r--r--   0 runner    (1001) docker     (123)    35656 2023-04-05 15:19:23.000000 conbench-2023.4.5/conbench/entities/commit.py
--rw-r--r--   0 runner    (1001) docker     (123)     2932 2023-04-05 15:19:23.000000 conbench-2023.4.5/conbench/entities/compare.py
--rw-r--r--   0 runner    (1001) docker     (123)      956 2023-04-05 15:19:24.000000 conbench-2023.4.5/conbench/entities/context.py
--rw-r--r--   0 runner    (1001) docker     (123)     7382 2023-04-05 15:19:24.000000 conbench-2023.4.5/conbench/entities/hardware.py
--rw-r--r--   0 runner    (1001) docker     (123)    26202 2023-04-05 15:19:24.000000 conbench-2023.4.5/conbench/entities/history.py
--rw-r--r--   0 runner    (1001) docker     (123)      920 2023-04-05 15:19:24.000000 conbench-2023.4.5/conbench/entities/info.py
--rw-r--r--   0 runner    (1001) docker     (123)    23553 2023-04-05 15:19:24.000000 conbench-2023.4.5/conbench/entities/run.py
--rw-r--r--   0 runner    (1001) docker     (123)     2077 2023-04-05 15:19:24.000000 conbench-2023.4.5/conbench/entities/user.py
--rw-r--r--   0 runner    (1001) docker     (123)      126 2023-04-05 15:19:24.000000 conbench-2023.4.5/conbench/extensions.py
--rw-r--r--   0 runner    (1001) docker     (123)     1978 2023-04-05 15:19:24.000000 conbench-2023.4.5/conbench/gunicorn-conf.py
--rw-r--r--   0 runner    (1001) docker     (123)     4507 2023-04-05 15:19:24.000000 conbench-2023.4.5/conbench/hacks.py
--rw-r--r--   0 runner    (1001) docker     (123)     3494 2023-04-05 15:19:24.000000 conbench-2023.4.5/conbench/logger.py
--rw-r--r--   0 runner    (1001) docker     (123)     9703 2023-04-05 15:19:24.000000 conbench-2023.4.5/conbench/machine_info.py
--rw-r--r--   0 runner    (1001) docker     (123)     8457 2023-04-05 15:19:24.000000 conbench-2023.4.5/conbench/metrics.py
--rw-r--r--   0 runner    (1001) docker     (123)    13326 2023-04-05 15:19:24.000000 conbench-2023.4.5/conbench/runner.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 15:19:44.321168 conbench-2023.4.5/conbench/tests/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-05 15:19:24.000000 conbench-2023.4.5/conbench/tests/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 15:19:44.325168 conbench-2023.4.5/conbench/tests/api/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-05 15:19:24.000000 conbench-2023.4.5/conbench/tests/api/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    10728 2023-04-05 15:19:24.000000 conbench-2023.4.5/conbench/tests/api/_asserts.py
--rw-r--r--   0 runner    (1001) docker     (123)   100708 2023-04-05 15:19:24.000000 conbench-2023.4.5/conbench/tests/api/_expected_docs.py
--rw-r--r--   0 runner    (1001) docker     (123)    12997 2023-04-05 15:19:24.000000 conbench-2023.4.5/conbench/tests/api/_fixtures.py
--rw-r--r--   0 runner    (1001) docker     (123)     3718 2023-04-05 15:19:24.000000 conbench-2023.4.5/conbench/tests/api/test_auth.py
--rw-r--r--   0 runner    (1001) docker     (123)     2172 2023-04-05 15:19:24.000000 conbench-2023.4.5/conbench/tests/api/test_commits.py
--rw-r--r--   0 runner    (1001) docker     (123)    23352 2023-04-05 15:19:24.000000 conbench-2023.4.5/conbench/tests/api/test_compare.py
--rw-r--r--   0 runner    (1001) docker     (123)     1045 2023-04-05 15:19:24.000000 conbench-2023.4.5/conbench/tests/api/test_contexts.py
--rw-r--r--   0 runner    (1001) docker     (123)     1614 2023-04-05 15:19:24.000000 conbench-2023.4.5/conbench/tests/api/test_docs.py
--rw-r--r--   0 runner    (1001) docker     (123)     1583 2023-04-05 15:19:24.000000 conbench-2023.4.5/conbench/tests/api/test_hardware.py
--rw-r--r--   0 runner    (1001) docker     (123)      875 2023-04-05 15:19:24.000000 conbench-2023.4.5/conbench/tests/api/test_history.py
--rwxr-xr-x   0 runner    (1001) docker     (123)     1396 2023-04-05 15:19:24.000000 conbench-2023.4.5/conbench/tests/api/test_index.py
--rw-r--r--   0 runner    (1001) docker     (123)      978 2023-04-05 15:19:24.000000 conbench-2023.4.5/conbench/tests/api/test_info.py
--rw-r--r--   0 runner    (1001) docker     (123)    43687 2023-04-05 15:19:24.000000 conbench-2023.4.5/conbench/tests/api/test_results.py
--rw-r--r--   0 runner    (1001) docker     (123)    17687 2023-04-05 15:19:24.000000 conbench-2023.4.5/conbench/tests/api/test_runs.py
--rw-r--r--   0 runner    (1001) docker     (123)     7603 2023-04-05 15:19:24.000000 conbench-2023.4.5/conbench/tests/api/test_users.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 15:19:44.329168 conbench-2023.4.5/conbench/tests/app/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-05 15:19:24.000000 conbench-2023.4.5/conbench/tests/app/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     8359 2023-04-05 15:19:24.000000 conbench-2023.4.5/conbench/tests/app/_asserts.py
--rw-r--r--   0 runner    (1001) docker     (123)    12677 2023-04-05 15:19:24.000000 conbench-2023.4.5/conbench/tests/app/test_auth.py
--rw-r--r--   0 runner    (1001) docker     (123)      308 2023-04-05 15:19:24.000000 conbench-2023.4.5/conbench/tests/app/test_batches.py
--rw-r--r--   0 runner    (1001) docker     (123)     2446 2023-04-05 15:19:24.000000 conbench-2023.4.5/conbench/tests/app/test_compare.py
--rw-r--r--   0 runner    (1001) docker     (123)     1725 2023-04-05 15:19:24.000000 conbench-2023.4.5/conbench/tests/app/test_hardware.py
--rw-r--r--   0 runner    (1001) docker     (123)      758 2023-04-05 15:19:24.000000 conbench-2023.4.5/conbench/tests/app/test_index.py
--rw-r--r--   0 runner    (1001) docker     (123)    13342 2023-04-05 15:19:24.000000 conbench-2023.4.5/conbench/tests/app/test_plots.py
--rw-r--r--   0 runner    (1001) docker     (123)     3028 2023-04-05 15:19:24.000000 conbench-2023.4.5/conbench/tests/app/test_results.py
--rw-r--r--   0 runner    (1001) docker     (123)      853 2023-04-05 15:19:24.000000 conbench-2023.4.5/conbench/tests/app/test_robots.py
--rw-r--r--   0 runner    (1001) docker     (123)     1852 2023-04-05 15:19:24.000000 conbench-2023.4.5/conbench/tests/app/test_runs.py
--rw-r--r--   0 runner    (1001) docker     (123)     5949 2023-04-05 15:19:24.000000 conbench-2023.4.5/conbench/tests/app/test_users.py
--rw-r--r--   0 runner    (1001) docker     (123)      416 2023-04-05 15:19:24.000000 conbench-2023.4.5/conbench/tests/app/test_util.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 15:19:44.329168 conbench-2023.4.5/conbench/tests/benchmark/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-05 15:19:24.000000 conbench-2023.4.5/conbench/tests/benchmark/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     7717 2023-04-05 15:19:24.000000 conbench-2023.4.5/conbench/tests/benchmark/_example_benchmarks.py
--rwxr-xr-x   0 runner    (1001) docker     (123)    11360 2023-04-05 15:19:24.000000 conbench-2023.4.5/conbench/tests/benchmark/test_cli.py
--rw-r--r--   0 runner    (1001) docker     (123)    10522 2023-04-05 15:19:24.000000 conbench-2023.4.5/conbench/tests/benchmark/test_machine_info.py
--rw-r--r--   0 runner    (1001) docker     (123)     8355 2023-04-05 15:19:24.000000 conbench-2023.4.5/conbench/tests/benchmark/test_runner.py
--rw-r--r--   0 runner    (1001) docker     (123)     1332 2023-04-05 15:19:24.000000 conbench-2023.4.5/conbench/tests/benchmark/test_units.py
--rw-r--r--   0 runner    (1001) docker     (123)     2719 2023-04-05 15:19:24.000000 conbench-2023.4.5/conbench/tests/benchmark/test_util.py
--rw-r--r--   0 runner    (1001) docker     (123)     1167 2023-04-05 15:19:24.000000 conbench-2023.4.5/conbench/tests/conftest.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 15:19:44.333168 conbench-2023.4.5/conbench/tests/entities/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-05 15:19:24.000000 conbench-2023.4.5/conbench/tests/entities/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    16144 2023-04-05 15:19:24.000000 conbench-2023.4.5/conbench/tests/entities/test_commit.py
--rw-r--r--   0 runner    (1001) docker     (123)    64400 2023-04-05 15:19:24.000000 conbench-2023.4.5/conbench/tests/entities/test_comparator.py
--rw-r--r--   0 runner    (1001) docker     (123)     9176 2023-04-05 15:19:24.000000 conbench-2023.4.5/conbench/tests/entities/test_history.py
--rw-r--r--   0 runner    (1001) docker     (123)     2173 2023-04-05 15:19:24.000000 conbench-2023.4.5/conbench/tests/entities/test_run.py
--rw-r--r--   0 runner    (1001) docker     (123)      306 2023-04-05 15:19:24.000000 conbench-2023.4.5/conbench/tests/entities/test_user.py
--rw-r--r--   0 runner    (1001) docker     (123)      544 2023-04-05 15:19:24.000000 conbench-2023.4.5/conbench/tests/helpers.py
--rw-r--r--   0 runner    (1001) docker     (123)    23249 2023-04-05 15:19:24.000000 conbench-2023.4.5/conbench/tests/populate_local_conbench.py
--rw-r--r--   0 runner    (1001) docker     (123)     1585 2023-04-05 15:19:24.000000 conbench-2023.4.5/conbench/tests/test_util.py
--rwxr-xr-x   0 runner    (1001) docker     (123)      338 2023-04-05 15:19:24.000000 conbench-2023.4.5/conbench/tests/test_version.py
--rw-r--r--   0 runner    (1001) docker     (123)     1126 2023-04-05 15:19:24.000000 conbench-2023.4.5/conbench/units.py
--rw-r--r--   0 runner    (1001) docker     (123)     9238 2023-04-05 15:19:24.000000 conbench-2023.4.5/conbench/util.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 15:19:44.305168 conbench-2023.4.5/conbench.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)    35621 2023-04-05 15:19:44.000000 conbench-2023.4.5/conbench.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     3356 2023-04-05 15:19:44.000000 conbench-2023.4.5/conbench.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-05 15:19:44.000000 conbench-2023.4.5/conbench.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       51 2023-04-05 15:19:44.000000 conbench-2023.4.5/conbench.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (123)      963 2023-04-05 15:19:44.000000 conbench-2023.4.5/conbench.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        9 2023-04-05 15:19:44.000000 conbench-2023.4.5/conbench.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)   112077 2023-04-05 15:19:23.000000 conbench-2023.4.5/conbench.png
--rw-r--r--   0 runner    (1001) docker     (123)       60 2023-04-05 15:19:24.000000 conbench-2023.4.5/requirements-cli.txt
--rw-r--r--   0 runner    (1001) docker     (123)      190 2023-04-05 15:19:24.000000 conbench-2023.4.5/requirements-dev.txt
--rwxr-xr-x   0 runner    (1001) docker     (123)      355 2023-04-05 15:19:24.000000 conbench-2023.4.5/requirements-webapp.txt
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-05 15:19:44.333168 conbench-2023.4.5/setup.cfg
--rwxr-xr-x   0 runner    (1001) docker     (123)     1528 2023-04-05 15:19:24.000000 conbench-2023.4.5/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:04:24.049589 conbench-2023.4.6/
+-rw-r--r--   0 runner    (1001) docker     (123)     1071 2023-04-06 16:03:58.000000 conbench-2023.4.6/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)      127 2023-04-06 16:03:58.000000 conbench-2023.4.6/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)    35621 2023-04-06 16:04:24.049589 conbench-2023.4.6/PKG-INFO
+-rwxr-xr-x   0 runner    (1001) docker     (123)    35165 2023-04-06 16:03:58.000000 conbench-2023.4.6/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:04:24.037588 conbench-2023.4.6/conbench/
+-rwxr-xr-x   0 runner    (1001) docker     (123)     9523 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)       64 2023-04-06 16:04:04.000000 conbench-2023.4.6/conbench/_version.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:04:24.037588 conbench-2023.4.6/conbench/api/
+-rw-r--r--   0 runner    (1001) docker     (123)      781 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/api/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4779 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/api/_docs.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2607 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/api/_endpoint.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1280 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/api/_errors.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20069 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/api/_examples.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11634 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/api/_google.py
+-rw-r--r--   0 runner    (1001) docker     (123)      765 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/api/_resp.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3673 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/api/auth.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1796 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/api/commits.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12604 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/api/compare.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1642 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/api/contexts.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1676 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/api/hardware.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1603 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/api/history.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)     7038 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/api/index.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1539 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/api/info.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11130 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/api/results.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4114 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/api/runs.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5269 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/api/users.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:04:24.041589 conbench-2023.4.6/conbench/app/
+-rw-r--r--   0 runner    (1001) docker     (123)      879 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/app/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7836 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/app/_endpoint.py
+-rw-r--r--   0 runner    (1001) docker     (123)    29408 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/app/_plots.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1665 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/app/_util.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5659 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/app/auth.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2453 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/app/batches.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11655 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/app/compare.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1896 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/app/hardware.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)     4181 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/app/index.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13748 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/app/results.py
+-rw-r--r--   0 runner    (1001) docker     (123)      649 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/app/robots.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3718 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/app/runs.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5392 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/app/users.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1336 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/buildinfo.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)     5151 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/cli.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5573 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/config.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5198 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/db.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:04:24.041589 conbench-2023.4.6/conbench/entities/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/entities/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9192 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/entities/_comparator.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4919 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/entities/_entity.py
+-rw-r--r--   0 runner    (1001) docker     (123)    32531 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/entities/benchmark_result.py
+-rw-r--r--   0 runner    (1001) docker     (123)      469 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/entities/case.py
+-rw-r--r--   0 runner    (1001) docker     (123)    35656 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/entities/commit.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2940 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/entities/compare.py
+-rw-r--r--   0 runner    (1001) docker     (123)      956 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/entities/context.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7382 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/entities/hardware.py
+-rw-r--r--   0 runner    (1001) docker     (123)    26202 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/entities/history.py
+-rw-r--r--   0 runner    (1001) docker     (123)      920 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/entities/info.py
+-rw-r--r--   0 runner    (1001) docker     (123)    23492 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/entities/run.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2077 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/entities/user.py
+-rw-r--r--   0 runner    (1001) docker     (123)      126 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/extensions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3359 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/gunicorn-conf.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4507 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/hacks.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3494 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/logger.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9703 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/machine_info.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8457 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/metrics.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14235 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/runner.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:04:24.045589 conbench-2023.4.6/conbench/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/tests/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:04:24.045589 conbench-2023.4.6/conbench/tests/api/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/tests/api/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10799 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/tests/api/_asserts.py
+-rw-r--r--   0 runner    (1001) docker     (123)   100800 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/tests/api/_expected_docs.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12997 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/tests/api/_fixtures.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3718 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/tests/api/test_auth.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2172 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/tests/api/test_commits.py
+-rw-r--r--   0 runner    (1001) docker     (123)    23352 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/tests/api/test_compare.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1045 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/tests/api/test_contexts.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1614 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/tests/api/test_docs.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1583 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/tests/api/test_hardware.py
+-rw-r--r--   0 runner    (1001) docker     (123)      875 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/tests/api/test_history.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)     1396 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/tests/api/test_index.py
+-rw-r--r--   0 runner    (1001) docker     (123)      978 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/tests/api/test_info.py
+-rw-r--r--   0 runner    (1001) docker     (123)    43687 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/tests/api/test_results.py
+-rw-r--r--   0 runner    (1001) docker     (123)    18625 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/tests/api/test_runs.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7603 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/tests/api/test_users.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:04:24.049589 conbench-2023.4.6/conbench/tests/app/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/tests/app/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8862 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/tests/app/_asserts.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12677 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/tests/app/test_auth.py
+-rw-r--r--   0 runner    (1001) docker     (123)      308 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/tests/app/test_batches.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3039 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/tests/app/test_compare.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1725 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/tests/app/test_hardware.py
+-rw-r--r--   0 runner    (1001) docker     (123)      758 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/tests/app/test_index.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13342 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/tests/app/test_plots.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3028 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/tests/app/test_results.py
+-rw-r--r--   0 runner    (1001) docker     (123)      853 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/tests/app/test_robots.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1852 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/tests/app/test_runs.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5949 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/tests/app/test_users.py
+-rw-r--r--   0 runner    (1001) docker     (123)      405 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/tests/app/test_util.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:04:24.049589 conbench-2023.4.6/conbench/tests/benchmark/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/tests/benchmark/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7717 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/tests/benchmark/_example_benchmarks.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)    11360 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/tests/benchmark/test_cli.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10522 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/tests/benchmark/test_machine_info.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8355 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/tests/benchmark/test_runner.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1332 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/tests/benchmark/test_units.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2719 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/tests/benchmark/test_util.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1167 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/tests/conftest.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:04:24.049589 conbench-2023.4.6/conbench/tests/entities/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/tests/entities/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16144 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/tests/entities/test_commit.py
+-rw-r--r--   0 runner    (1001) docker     (123)    64400 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/tests/entities/test_comparator.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9176 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/tests/entities/test_history.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1752 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/tests/entities/test_run.py
+-rw-r--r--   0 runner    (1001) docker     (123)      306 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/tests/entities/test_user.py
+-rw-r--r--   0 runner    (1001) docker     (123)      544 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/tests/helpers.py
+-rw-r--r--   0 runner    (1001) docker     (123)    23257 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/tests/populate_local_conbench.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1585 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/tests/test_util.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)      338 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/tests/test_version.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1126 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/units.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10501 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench/util.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:04:24.037588 conbench-2023.4.6/conbench.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)    35621 2023-04-06 16:04:24.000000 conbench-2023.4.6/conbench.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     3378 2023-04-06 16:04:24.000000 conbench-2023.4.6/conbench.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 16:04:24.000000 conbench-2023.4.6/conbench.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       51 2023-04-06 16:04:24.000000 conbench-2023.4.6/conbench.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      970 2023-04-06 16:04:24.000000 conbench-2023.4.6/conbench.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        9 2023-04-06 16:04:24.000000 conbench-2023.4.6/conbench.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)   112077 2023-04-06 16:03:58.000000 conbench-2023.4.6/conbench.png
+-rw-r--r--   0 runner    (1001) docker     (123)       60 2023-04-06 16:03:58.000000 conbench-2023.4.6/requirements-cli.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      197 2023-04-06 16:03:58.000000 conbench-2023.4.6/requirements-dev.txt
+-rwxr-xr-x   0 runner    (1001) docker     (123)      355 2023-04-06 16:03:58.000000 conbench-2023.4.6/requirements-webapp.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 16:04:24.049589 conbench-2023.4.6/setup.cfg
+-rwxr-xr-x   0 runner    (1001) docker     (123)     1528 2023-04-06 16:03:58.000000 conbench-2023.4.6/setup.py
```

### Comparing `conbench-2023.4.5/LICENSE` & `conbench-2023.4.6/LICENSE`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/PKG-INFO` & `conbench-2023.4.6/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: conbench
-Version: 2023.4.5
+Version: 2023.4.6
 Summary: Continuous Benchmarking (CB) Framework
 Home-page: https://github.com/conbench/conbench
 Maintainer: Apache Arrow Developers
 Maintainer-email: dev@arrow.apache.org
 Classifier: Programming Language :: Python :: 3.8
 Classifier: License :: OSI Approved :: MIT License
 Requires-Python: >=3.8
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: conbench Version: 2023.4.5 Summary: Continuous
+Metadata-Version: 2.1 Name: conbench Version: 2023.4.6 Summary: Continuous
 Benchmarking (CB) Framework Home-page: https://github.com/conbench/conbench
 Maintainer: Apache Arrow Developers Maintainer-email: dev@arrow.apache.org
 Classifier: Programming Language :: Python :: 3.8 Classifier: License :: OSI
 Approved :: MIT License Requires-Python: >=3.8 Description-Content-Type: text/
 markdown Provides-Extra: server Provides-Extra: dev License-File: LICENSE
                                                                  [Build_Status]
 # Conbench Check out the docs at https://conbench.github.io/conbench.
```

### Comparing `conbench-2023.4.5/README.md` & `conbench-2023.4.6/README.md`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/conbench/__init__.py` & `conbench-2023.4.6/conbench/__init__.py`

 * *Files 6% similar despite different names*

```diff
@@ -13,32 +13,42 @@
 Also see https://github.com/conbench/conbench/pull/662#discussion_r1097781344
 """
 
 import importlib.metadata as importlib_metadata
 import json
 import logging
 import os
+from typing import TYPE_CHECKING
 
 import conbench.logger
 
 try:
     __version__ = importlib_metadata.version(__name__)
 except Exception:
     # When is this expected to happen?
     __version__ = importlib_metadata.version("conbench")
 
 del importlib_metadata
 
 
+if TYPE_CHECKING:
+    # https://stackoverflow.com/a/39757388/145400
+    # Yes one could do `-> "flask.Response"`` but then
+    # https://github.com/PyCQA/pyflakes/issues/340  ¯\_(ツ)_/¯
+    import flask
+    import werkzeug
+    import werkzeug.exceptions
+
+
 # Pre-configure logging before reading user-given configuration.
 conbench.logger.setup(level_stderr="DEBUG", level_file=None, level_sqlalchemy="WARNING")
 log = logging.getLogger(__name__)
 
 
-def create_application(config):
+def create_application(config) -> "flask.Flask":
     import flask as f
 
     import conbench.metrics
 
     app = f.Flask(__name__)
     app.config.from_object(config)
 
@@ -161,24 +171,40 @@
         for fn_name in application.view_functions:
             if not fn_name.startswith("api."):
                 continue
             view_fn = application.view_functions[fn_name]
             spec.path(view=view_fn)
 
 
-def _json_http_errors(e):
+def _json_http_errors(exc) -> "werkzeug.wrappers.Response":
+    """
+    Turn an HTTPException object into a JSON response where exception detail
+    is emitted as part of the JSON document.
+    """
+    # Note(JP): I understand this is against cyclic imports, but having this as
+    # part of requently called error handler (even if the import machinery is
+    # fast and cached) is a code smell -- let's see about this.
     import flask as f
 
-    response = e.get_response()
-    data = {"code": e.code, "name": e.name}
-    if e.code == 400:
-        data["description"] = e.description
-    response.data = f.json.dumps(data)
-    response.content_type = "application/json"
-    return response
+    data = {"code": exc.code, "name": exc.name}
+
+    # When for example calling flask.abort(404, foo="bar") then the
+    # resulting HTTPException object has a property "foo".
+    for attr in vars(exc):
+        # denylist or allowlist? Hm.
+        if attr not in ("response", "www_authenticate"):
+            data[attr] = getattr(exc, attr)
+
+    # documented with "Get a response object. If one was passed to the
+    # exception it’s returned directly.""
+    resp = exc.get_response()
+    resp.data = f.json.dumps(data)
+    resp.content_type = "application/json"
+
+    return resp
 
 
 def dict_or_objattrs_to_nonsensitive_string(obj):
     """Generate a sorted and indented JSON string from the keys and values
     given by `obj`. Sanitize values if they appear to be sensitive.
 
     If `obj` looks like a dictionary then take keys and values from there.
```

#### encoding

```diff
@@ -1 +1 @@
-us-ascii
+utf-8
```

### Comparing `conbench-2023.4.5/conbench/api/__init__.py` & `conbench-2023.4.6/conbench/api/__init__.py`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/conbench/api/_docs.py` & `conbench-2023.4.6/conbench/api/_docs.py`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/conbench/api/_endpoint.py` & `conbench-2023.4.6/conbench/api/_endpoint.py`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/conbench/api/_errors.py` & `conbench-2023.4.6/conbench/api/_errors.py`

 * *Files 14% similar despite different names*

```diff
@@ -1,13 +1,18 @@
 import marshmallow
 
 from ..api._docs import spec
 
 
 class ErrorSchema(marshmallow.Schema):
+    # Allow for additional properties:
+    # https://marshmallow.readthedocs.io/en/stable/quickstart.html#handling-unknown-fields
+    class Meta:
+        unknown = marshmallow.INCLUDE
+
     code = marshmallow.fields.Int(
         metadata={"description": "HTTP error code"}, required=True
     )
     name = marshmallow.fields.String(
         metadata={"description": "HTTP error name"}, required=True
     )
```

### Comparing `conbench-2023.4.5/conbench/api/_examples.py` & `conbench-2023.4.6/conbench/api/_examples.py`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/conbench/api/_google.py` & `conbench-2023.4.6/conbench/api/_google.py`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/conbench/api/auth.py` & `conbench-2023.4.6/conbench/api/auth.py`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/conbench/api/commits.py` & `conbench-2023.4.6/conbench/api/commits.py`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/conbench/api/compare.py` & `conbench-2023.4.6/conbench/api/compare.py`

 * *Files 13% similar despite different names*

```diff
@@ -1,23 +1,31 @@
 import collections
+import logging
+from typing import List
 
 import flask as f
 
 from ..api import rule
 from ..api._endpoint import ApiEndpoint, maybe_login_required
 from ..entities._comparator import BenchmarkComparator, BenchmarkListComparator
 from ..entities._entity import NotFound
 from ..entities.benchmark_result import BenchmarkResult
 from ..entities.commit import Commit
 from ..entities.compare import CompareBenchmarkResultSerializer
 from ..entities.history import set_z_scores
 from ..hacks import set_display_benchmark_name, set_display_case_permutation
 
+log = logging.getLogger(__name__)
 
-def _compare_entity(benchmark_result: BenchmarkResult):
+
+def _result_dict_for_compare_api(benchmark_result: BenchmarkResult):
+    """
+    Return a dictionary representing a benchmark result, but for the compare
+    API, i.e. this is a minimal/special representation of a benchmark result.
+    """
     return {
         "id": benchmark_result.id,
         "batch_id": benchmark_result.batch_id,
         "run_id": benchmark_result.run_id,
         "case_id": benchmark_result.case_id,
         "context_id": benchmark_result.context_id,
         "value": benchmark_result.mean,
@@ -31,14 +39,16 @@
         "tags": benchmark_result.case.tags,
         "z_score": benchmark_result.z_score,
     }
 
 
 def _get_pairs(baseline_items, contender_items):
     """
+    TODO: needs concise docstring defining the goals/task of this function.
+
     You should be able to compare any run with any other run, so we can't
     just key by case_id/context_id/hardware_hash, or you couldn't compare runs
     done on different machine, nor could you compare runs done in different
     contexts.
 
     Assumptions:
         - A run contains exactly one machine.
@@ -76,36 +86,64 @@
     key = case_id if simple else f"{case_id}-{context_id}"
     if key not in pairs:
         pairs[key] = {"baseline": None, "contender": None}
     pairs[key][kind] = item
 
 
 class CompareMixin:
-    def get_args(self, compare_ids):
+    def _parse_two_ids_or_abort(self, compare_ids):
+        if "..." not in compare_ids:
+            f.abort(
+                404, description="last URL path segment must be of pattern <id>...<id>"
+            )
+
+        # I think these can be either two run IDs, two batch IDs or two
+        # benchmark result IDs?
+        baseline_id, contender_id = compare_ids.split("...", 1)
+
+        if not baseline_id:
+            f.abort(404, description="empty baseline ID")
+
+        if not contender_id:
+            f.abort(404, description="empty contender ID")
+
+        return baseline_id, contender_id
+
+    def get_query_args_from_request(self):
+        """
+        Attempt to read a specific set of query parameters from request
+        context.
+        """
+        # what is raw supposed to do?
         raw = f.request.args.get("raw", "false").lower() in ["true", "1"]
 
         threshold = f.request.args.get("threshold")
         if threshold is not None:
             threshold = float(threshold)
 
         threshold_z = f.request.args.get("threshold_z")
         if threshold_z is not None:
             threshold_z = float(threshold_z)
 
-        try:
-            baseline_id, contender_id = compare_ids.split("...", 1)
-        except ValueError:
-            self.abort_404_not_found()
+        # I think this expression can never raise ValueError.
+        # The goal here was probably to raise ValueError?
+        # try:
+        #     baseline_id, contender_id = compare_ids.split("...", 1)
+        # except ValueError:
+        #     self.abort_404_not_found()
 
-        return raw, threshold, threshold_z, baseline_id, contender_id
+        return raw, threshold, threshold_z
 
 
 class CompareEntityEndpoint(ApiEndpoint, CompareMixin):
+    def _get_results(self, rid: str) -> List[BenchmarkResult]:
+        raise NotImplementedError
+
     @maybe_login_required
-    def get(self, compare_ids):
+    def get(self, compare_ids) -> f.Response:
         """
         ---
         description: Compare benchmark results.
         responses:
             "200": "CompareEntity"
             "401": "401"
             "404": "404"
@@ -126,46 +164,54 @@
           - in: query
             name: threshold_z
             schema:
               type: number
         tags:
           - Comparisons
         """
-        args = self.get_args(compare_ids)
-        raw, threshold, threshold_z, baseline_id, contender_id = args
 
-        baseline_benchmark_result = self._get(baseline_id)
-        contender_benchmark_result = self._get(contender_id)
+        baseline_id, contender_id = self._parse_two_ids_or_abort(compare_ids)
+
+        args = self.get_query_args_from_request()
+        raw, threshold, threshold_z = args
+
+        baseline_benchmark_result = self._get_results(baseline_id)[0]
+        contender_benchmark_result = self._get_results(contender_id)[0]
+
         set_z_scores(
             contender_benchmark_results=[contender_benchmark_result],
             baseline_commit=baseline_benchmark_result.run.commit,
         )
+
         # TODO: remove baseline-z-score-related keys from this endpoint
         baseline_benchmark_result.z_score = None
 
         set_display_case_permutation(baseline_benchmark_result)
         set_display_case_permutation(contender_benchmark_result)
         set_display_benchmark_name(baseline_benchmark_result)
         set_display_benchmark_name(contender_benchmark_result)
 
-        baseline = _compare_entity(baseline_benchmark_result)
-        contender = _compare_entity(contender_benchmark_result)
+        baseline = _result_dict_for_compare_api(baseline_benchmark_result)
+        contender = _result_dict_for_compare_api(contender_benchmark_result)
         comparator = BenchmarkComparator(
             baseline,
             contender,
             threshold,
             threshold_z,
         )
 
         return comparator.compare() if raw else comparator.formatted()
 
 
 class CompareListEndpoint(ApiEndpoint, CompareMixin):
+    def _get_results(self, id: str) -> List[BenchmarkResult]:
+        raise NotImplementedError
+
     @maybe_login_required
-    def get(self, compare_ids):
+    def get(self, compare_ids) -> f.Response:
         """
         ---
         description: Compare benchmark results.
         responses:
             "200": "CompareList"
             "401": "401"
             "404": "404"
@@ -186,72 +232,88 @@
           - in: query
             name: threshold_z
             schema:
               type: number
         tags:
           - Comparisons
         """
-        args = self.get_args(compare_ids)
-        raw, threshold, threshold_z, baseline_id, contender_id = args
+        # The `baseline_id`` and `contender_id`` may be of various kinds (run
+        # ids, batch ids, .... see sub classes below.).
+
+        baseline_id, contender_id = self._parse_two_ids_or_abort(compare_ids)
+        raw, threshold, threshold_z = self.get_query_args_from_request()
+        baseline_results = self._get_results(baseline_id)
+        contender_results = self._get_results(contender_id)
 
-        baselines = self._get(baseline_id)
-        contenders = self._get(contender_id)
         set_z_scores(
-            contender_benchmark_results=contenders,
-            baseline_commit=baselines[0].run.commit,
+            contender_benchmark_results=contender_results,
+            baseline_commit=baseline_results[0].run.commit,
         )
+
         # TODO: remove baseline-z-score-related keys from this endpoint
-        for baseline in baselines:
-            baseline.z_score = None
+        for res in baseline_results:
+            res.z_score = None
 
         baseline_items, contender_items = [], []
-        for benchmark_result in baselines:
+
+        for benchmark_result in baseline_results:
             # TODO: define dynamic properties on BenchmarkResult instead of
             # mutating these objects here in-place.
             set_display_benchmark_name(benchmark_result)
             set_display_case_permutation(benchmark_result)
-            baseline_items.append(_compare_entity(benchmark_result))
-        for benchmark_result in contenders:
+
+            baseline_items.append(_result_dict_for_compare_api(benchmark_result))
+
+        for benchmark_result in contender_results:
             set_display_benchmark_name(benchmark_result)
             set_display_case_permutation(benchmark_result)
-            contender_items.append(_compare_entity(benchmark_result))
+            contender_items.append(_result_dict_for_compare_api(benchmark_result))
 
         pairs = _get_pairs(baseline_items, contender_items)
+
         comparator = BenchmarkListComparator(
             pairs,
             threshold,
             threshold_z,
         )
 
         result = comparator.compare() if raw else comparator.formatted()
         return f.jsonify(list(result))
 
 
 class CompareBenchmarksAPI(CompareEntityEndpoint):
-    def _get(self, benchmark_id):
+    def _get_results(self, benchmark_id) -> List[BenchmarkResult]:
         try:
             benchmark_result = BenchmarkResult.one(id=benchmark_id)
         except NotFound:
-            self.abort_404_not_found()
-        return benchmark_result
+            f.abort(
+                404, description="no benchmark result found with ID: '{benchmark_id}'"
+            )
+        return [benchmark_result]
 
 
 class CompareBatchesAPI(CompareListEndpoint):
-    def _get(self, batch_id):
+    def _get_results(self, batch_id) -> List[BenchmarkResult]:
         benchmark_results = BenchmarkResult.all(batch_id=batch_id)
+
         if not benchmark_results:
-            self.abort_404_not_found()
+            f.abort(
+                404,
+                description=f"no benchmark results found for batch ID: '{batch_id}'",
+            )
         return benchmark_results
 
 
 class CompareRunsAPI(CompareListEndpoint):
-    def _get(self, run_id):
+    def _get_results(self, run_id) -> List[BenchmarkResult]:
         benchmark_results = BenchmarkResult.all(run_id=run_id)
         if not benchmark_results:
-            self.abort_404_not_found()
+            f.abort(
+                404, description=f"no benchmark results found for run ID: '{run_id}'"
+            )
         return benchmark_results
 
 
 class CompareCommitsAPI(CompareListEndpoint):
     serializer = CompareBenchmarkResultSerializer()
 
     @maybe_login_required
@@ -271,24 +333,27 @@
             example: <baseline_sha>...<contender_sha>
         tags:
           - Comparisons
         """
         try:
             baseline_sha, contender_sha = compare_shas.split("...", 1)
         except ValueError:
+            # Note(JP): this cannot raise ValueError.
             self.abort_404_not_found()
+
         baseline_commit = self._get(baseline_sha)
         contender_commit = self._get(contender_sha)
         return self.serializer.one.dump([baseline_commit, contender_commit])
 
     def _get(self, sha):
         try:
             commit = Commit.one(sha=sha)
         except NotFound:
-            self.abort_404_not_found()
+            f.abort(404, description=f"commit hash not found: {sha}")
+
         return commit
 
 
 compare_benchmarks_view = CompareBenchmarksAPI.as_view("compare-benchmarks")
 compare_batches_view = CompareBatchesAPI.as_view("compare-batches")
 compare_runs_view = CompareRunsAPI.as_view("compare-runs")
 compare_commits_view = CompareCommitsAPI.as_view("compare-commits")
```

### Comparing `conbench-2023.4.5/conbench/api/contexts.py` & `conbench-2023.4.6/conbench/api/contexts.py`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/conbench/api/hardware.py` & `conbench-2023.4.6/conbench/api/hardware.py`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/conbench/api/history.py` & `conbench-2023.4.6/conbench/api/history.py`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/conbench/api/index.py` & `conbench-2023.4.6/conbench/api/index.py`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/conbench/api/info.py` & `conbench-2023.4.6/conbench/api/info.py`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/conbench/api/results.py` & `conbench-2023.4.6/conbench/api/results.py`

 * *Files 2% similar despite different names*

```diff
@@ -12,14 +12,15 @@
 from ..entities._entity import NotFound
 from ..entities.benchmark_result import (
     BenchmarkResult,
     BenchmarkResultFacadeSchema,
     BenchmarkResultSerializer,
 )
 from ..entities.case import Case
+from ._resp import json_response_for_byte_sequence, resp400
 
 log = logging.getLogger(__name__)
 
 
 class BenchmarkValidationMixin:
     def validate_benchmark(self, schema):
         return self.validate(schema)
@@ -108,15 +109,15 @@
 
 
 class BenchmarkListAPI(ApiEndpoint, BenchmarkValidationMixin):
     serializer = BenchmarkResultSerializer()
     schema = BenchmarkResultFacadeSchema()
 
     @maybe_login_required
-    def get(self):
+    def get(self) -> f.Response:
         """
         ---
         description: |
             Return a JSON array of benchmark results.
 
             Note that this endpoint does not provide on-the-fly change
             detection analysis (lookback z-score method).
@@ -194,15 +195,15 @@
         # cut JSON serialization time.
 
         jsonbytes: bytes = orjson.dumps(
             [r.to_dict_for_json_api() for r in benchmark_results],
             option=orjson.OPT_INDENT_2,
         )
 
-        return make_json_response(jsonbytes, 200)
+        return json_response_for_byte_sequence(jsonbytes, 200)
 
     @flask_login.login_required
     def post(self) -> f.Response:
         """
         ---
         description:
             Submit a BenchmarkResult within a specific Run.
@@ -284,33 +285,14 @@
         # Note(JP): in the future this will also raise further validation
         # errors that are to be exposed via a 400 response to the HTTP client
         benchmark_result = BenchmarkResult.create(data)
 
         return self.response_201_created(self.serializer.one.dump(benchmark_result))
 
 
-def make_json_response(data: bytes, status_code: int) -> f.Response:
-    # Note(JP): it's documented that a byte sequence can be passed in:
-    # https://flask.palletsprojects.com/en/2.2.x/api/#flask.Flask.make_response
-    return f.make_response((data, status_code, {"content-type": "application/json"}))
-
-
-def resp400(description: str) -> f.Response:
-    """
-    Utility for canonical generation of 400 Bad Request response with an
-    error description. Define elsewhere once used elsewhere.
-    """
-    return f.make_response(
-        # This puts a JSON body into the response with a JSON object with one
-        # key, the description
-        f.jsonify(description=description),
-        400,
-    )
-
-
 benchmark_entity_view = BenchmarkEntityAPI.as_view("benchmark")
 benchmark_list_view = BenchmarkListAPI.as_view("benchmarks")
 
 rule(
     "/benchmarks/",
     view_func=benchmark_list_view,
     methods=["GET", "POST"],
```

### Comparing `conbench-2023.4.5/conbench/api/runs.py` & `conbench-2023.4.6/conbench/api/runs.py`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/conbench/api/users.py` & `conbench-2023.4.6/conbench/api/users.py`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/conbench/app/__init__.py` & `conbench-2023.4.6/conbench/app/__init__.py`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/conbench/app/_endpoint.py` & `conbench-2023.4.6/conbench/app/_endpoint.py`

 * *Files 11% similar despite different names*

```diff
@@ -6,14 +6,15 @@
 import flask as f
 import flask.views
 import flask_login
 import werkzeug
 
 from .. import __version__
 from ..buildinfo import BUILD_INFO
+from ..config import Config
 
 log = logging.getLogger(__name__)
 
 
 # Default to importlib_metadata version string.
 VERSION_STRING_FOOTER = __version__
 
@@ -136,17 +137,33 @@
 
     def redirect(self, endpoint, **kwargs):
         return f.redirect(f.url_for(endpoint, **kwargs))
 
     def render_template(self, template, **kwargs):
         # inject/overwrite
         kwargs["version_string_footer"] = VERSION_STRING_FOOTER
-
         return f.render_template(template, **kwargs)
 
+    def error_page(self, msg: str, alert_level="danger") -> str:
+        """
+        Generate HTML text which shows an error page, presenting an error
+        message.
+
+        This is OK to be delivered in a status-200 HTTP response for now.
+        """
+        # add more as desired
+        assert alert_level in ("info", "danger", "primary", "warning")
+        return f.render_template(
+            "error.html",
+            error_message=msg,
+            application=Config.APPLICATION_NAME,
+            title=self.title,  # type: ignore
+            alert_level=alert_level,
+        )
+
     def flash(self, *args):
         return f.flash(*args)
 
     def api_post(self, endpoint, form, **kwargs):
         client = self._get_client()
         response = client.post(f.url_for(endpoint, **kwargs), json=self.data(form))
         if response.status_code == 400:
```

### Comparing `conbench-2023.4.5/conbench/app/_plots.py` & `conbench-2023.4.6/conbench/app/_plots.py`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/conbench/app/_util.py` & `conbench-2023.4.6/conbench/app/_util.py`

 * *Files 8% similar despite different names*

```diff
@@ -1,9 +1,7 @@
-import re
-
 from ..hacks import set_display_benchmark_name, set_display_case_permutation
 from ..units import formatter_for_unit
 
 
 def augment(benchmark, contexts=None):
     set_display_benchmark_name(benchmark)
     set_display_time(benchmark)
@@ -53,15 +51,7 @@
     fmt = formatter_for_unit(unit)
     benchmark["display_mean"] = fmt(mean, unit)
 
 
 def set_display_error(benchmark):
     if not benchmark["error"]:
         benchmark["error"] = ""
-
-
-def display_message(message):
-    # Note(JP): why is that important, useful?
-    # truncate git shas in commit message
-    for m in re.findall(r"\b[0-9a-f]{40}\b", message):
-        message = message.replace(m, m[:7])
-    return message
```

### Comparing `conbench-2023.4.5/conbench/app/auth.py` & `conbench-2023.4.6/conbench/app/auth.py`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/conbench/app/batches.py` & `conbench-2023.4.6/conbench/app/batches.py`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/conbench/app/compare.py` & `conbench-2023.4.6/conbench/app/compare.py`

 * *Files 23% similar despite different names*

```diff
@@ -1,21 +1,25 @@
 import copy
 import json
+import logging
+from typing import List, Optional, Tuple
 
 import bokeh
 import flask as f
 
 from ..app import rule
 from ..app._endpoint import AppEndpoint, authorize_or_terminate
 from ..app._plots import TimeSeriesPlotMixin, simple_bar_plot
 from ..app._util import augment
 from ..app.results import BenchmarkResultMixin, RunMixin
 from ..config import Config
 from ..entities.run import commit_hardware_run_map
 
+log = logging.getLogger(__name__)
+
 
 def all_keys(dict1, dict2, attr):
     if dict1 is None:
         dict1 = {}
     if dict2 is None:
         dict2 = {}
     return sorted(
@@ -35,16 +39,18 @@
         if comparisons and self.type == "batch":
             ids = {c["baseline_run_id"] for c in comparisons if c["baseline_run_id"]}
             baseline_run_id = ids.pop() if ids else None
             ids = {c["contender_run_id"] for c in comparisons if c["contender_run_id"]}
             contender_run_id = ids.pop() if ids else None
             compare = f"{baseline_run_id}...{contender_run_id}"
             compare_runs_url = f.url_for("app.compare-runs", compare_ids=compare)
+
         elif comparisons and self.type == "run":
             baseline_run_id, contender_run_id = baseline_id, contender_id
+
         elif comparisons and self.type == "benchmark":
             baseline = self.get_display_benchmark(baseline_id)
             contender = self.get_display_benchmark(contender_id)
             plot = self._get_plot(baseline, contender)
             baseline_run_id = baseline["run_id"]
             contender_run_id = contender["run_id"]
             compare = f"{baseline_run_id}...{contender_run_id}"
@@ -138,86 +144,161 @@
                 ),
                 "plot",
             ),
         )
         return plot
 
     @authorize_or_terminate
-    def get(self, compare_ids):
-        threshold = f.request.args.get("threshold")
-        threshold_z = f.request.args.get("threshold_z")
-        params = {"compare_ids": compare_ids}
-        if threshold is not None:
-            params["threshold"] = threshold
-        if threshold_z is not None:
-            params["threshold_z"] = threshold_z
-
-        try:
-            baseline_id, contender_id = compare_ids.split("...", 1)
-            comparisons, regressions, improvements = self._compare(params)
-            if not comparisons:
-                self.flash("Data is still collecting (or failed).")
-        except ValueError:
-            baseline_id, contender_id = "unknown", "unknown"
-            comparisons, regressions, improvements = [], None, None
-            self.flash("Invalid contender and baseline.")
+    def get(self, compare_ids: str) -> str:
+        """
+        The argument `compare_ids` is an user-given unvalidated string which is
+        supposed to be of the following shape:
+
+                    <baseline_id>...<contender_id>
+
+        Parse the shape here to provide some friendly UI feedback for common
+        mistakes.
+
+        However, for now rely on the API layer to check if these IDs are
+        'known'.
+
+        The API layer will parse the string `compare_ids` again, but that's OK
+        for now.
+
+        Note that the two IDs that are encoded `compare_ids` can be either two
+        run IDs, two batch IDs or two benchmark result IDs.
+        """
+
+        if "..." not in compare_ids:
+            return self.error_page(  # type: ignore
+                "Got unexpected URL path pattern. Expected: <id>...<id>"
+            )
+
+        baseline_id, contender_id = compare_ids.split("...", 1)
+
+        if not baseline_id:
+            return self.error_page(  # type: ignore
+                "No baseline ID was provided. Expected format: <baseline_id>...<contender_id>"
+            )
+
+        if not contender_id:
+            return self.error_page(  # type: ignore
+                "No contender ID was provided. Expected format: <baseline-id>...<contender-id>"
+            )
+
+        (
+            comparison_results,
+            regression_count,
+            improvement_count,
+            error_string,
+        ) = self._compare(baseline_id=baseline_id, contender_id=contender_id)
+
+        if error_string is not None:
+            return self.error_page(  # type: ignore
+                f"cannot perform comparison: {error_string}", alert_level="info"
+            )
+
+        if len(comparison_results) == 0:
+            return self.error_page(  # type: ignore
+                "comparison yielded 0 benchmark results",
+                alert_level="info",
+            )
+
+        # threshold = f.request.args.get("threshold")
+        # threshold_z = f.request.args.get("threshold_z")
+        # params = {"compare_ids": compare_ids}
+        # if threshold is not None:
+        #     params["threshold"] = threshold
+        # if threshold_z is not None:
+        #     params["threshold_z"] = threshold_z
 
         return self.page(
-            comparisons,
-            regressions,
-            improvements,
-            baseline_id,
-            contender_id,
+            comparisons=comparison_results,
+            regressions=regression_count,
+            improvements=improvement_count,
+            baseline_id=baseline_id,
+            contender_id=contender_id,
         )
 
-    def _compare(self, params):
-        response = self.api_get(self.api, **params)
+    def _compare(
+        self, baseline_id: str, contender_id: str
+    ) -> Tuple[List, int, int, Optional[str]]:
+        """
+        Return a 4-tuple.
+
+        If the last item is a string then it is an error message for why
+        the comparison failed. Do not process the first three items then.
+        """
+        # This farms out one of three API endpoints. self.api_endpoint_name is
+        # set in a child class. Re-assemble the stringified input argument for
+        # the virtual API endpoint, carrying both baseline and contender ID
+        params = {"compare_ids": f"{baseline_id}...{contender_id}"}
+        # error: "Compare" has no attribute "api_endpoint_name"  [attr-defined]
+        response = self.api_get(self.api_endpoint_name, **params)  # type: ignore
+
+        if response.status_code != 200:
+            log.error(
+                "processing req to %s -- unexpected response for virtual request: %s, %s",
+                f.request.url,
+                response.status_code,
+                response.text,
+            )
+            # poor-mans error propagation, until we remove the API
+            # layer indirection.
+            errmsg = response.text
+            try:
+                errmsg = response.json["description"]
+            except Exception:
+                pass
+            return [], 0, 0, errmsg
 
+        # below is legacy code, review for bugs and clarity
         comparisons, regressions, improvements = [], 0, 0
-        if response.status_code == 200:
-            comparisons = [response.json]
-            if isinstance(response.json, list):
-                comparisons = response.json
-
-            for c in comparisons:
-                view = "app.compare-benchmarks"
-                compare = f'{c["baseline_id"]}...{c["contender_id"]}'
-                c["compare_benchmarks_url"] = f.url_for(view, compare_ids=compare)
-
-                view = "app.compare-batches"
-                compare = f'{c["baseline_batch_id"]}...{c["contender_batch_id"]}'
-                c["compare_batches_url"] = f.url_for(view, compare_ids=compare)
-
-                if c["contender_z_regression"]:
-                    regressions += 1
-                if c["contender_z_improvement"]:
-                    improvements += 1
 
-        return comparisons, regressions, improvements
+        comparisons = [response.json]
+        if isinstance(response.json, list):
+            comparisons = response.json
+
+        # Mutate comparison objs (dictionaries) on the fly
+        for c in comparisons:
+            view = "app.compare-benchmarks"
+            compare = f'{c["baseline_id"]}...{c["contender_id"]}'
+            c["compare_benchmarks_url"] = f.url_for(view, compare_ids=compare)
+
+            view = "app.compare-batches"
+            compare = f'{c["baseline_batch_id"]}...{c["contender_batch_id"]}'
+            c["compare_batches_url"] = f.url_for(view, compare_ids=compare)
+
+            if c["contender_z_regression"]:
+                regressions += 1
+            if c["contender_z_improvement"]:
+                improvements += 1
+
+        return comparisons, regressions, improvements, None
 
 
 class CompareBenchmarks(Compare):
     type = "benchmark"
     html = "compare-entity.html"
     title = "Compare Benchmarks"
-    api = "api.compare-benchmarks"
+    api_endpoint_name = "api.compare-benchmarks"
 
 
 class CompareBatches(Compare):
     type = "batch"
     html = "compare-list.html"
     title = "Compare Batches"
-    api = "api.compare-batches"
+    api_endpoint_name = "api.compare-batches"
 
 
 class CompareRuns(Compare):
     type = "run"
     html = "compare-list.html"
     title = "Compare Runs"
-    api = "api.compare-runs"
+    api_endpoint_name = "api.compare-runs"
 
 
 rule(
     "/compare/benchmarks/<compare_ids>/",
     view_func=CompareBenchmarks.as_view("compare-benchmarks"),
     methods=["GET"],
 )
```

### Comparing `conbench-2023.4.5/conbench/app/hardware.py` & `conbench-2023.4.6/conbench/app/hardware.py`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/conbench/app/index.py` & `conbench-2023.4.6/conbench/app/index.py`

 * *Files 10% similar despite different names*

```diff
@@ -3,14 +3,16 @@
 from dataclasses import dataclass
 from typing import Optional
 from urllib.parse import urlparse
 
 import flask
 from sqlalchemy import select
 
+import conbench.util
+
 from ..app import rule
 from ..app._endpoint import AppEndpoint, authorize_or_terminate
 from ..app.results import RunMixin
 from ..config import Config
 from ..db import Session
 from ..entities.run import Run
 
@@ -57,15 +59,15 @@
         # granted: https://github.com/conbench/conbench/issues/864
 
         reponame_runs_map = defaultdict(list)
 
         for r in runs:
             rd = RunForDisplay(
                 ctime_for_table=r.timestamp.strftime("%Y-%m-%d %H:%M:%S UTC"),
-                commit_message_short=short_commit_msg(r.commit.message),
+                commit_message_short=conbench.util.short_commit_msg(r.commit.message),
                 # Temporary band-aid; we cannot fetch all last-1000-run-related
                 # BenchmarkResult objects each time we render the landing page.
                 # See https://github.com/conbench/conbench/issues/977 However,
                 # we will find a pragmatic way to still display a per-run
                 # result count (estimate). I want to leave this code intact for
                 # now and display a placeholder.
                 result_count="",
@@ -109,27 +111,10 @@
     # Expose the raw Run object (but this needs to be used with a lot of
     # care, in the template -- for VSCode supporting Python variable types and
     # auot-completion in a jinja2 template see
     # https://github.com/microsoft/pylance-release/discussions/4090)
     run: Run
 
 
-def short_commit_msg(msg: str):
-    """
-    Substitute multiple whitespace characters with a single space. Overall,
-    truncate at maxlen.
-
-    This may return an empty string.
-    """
-    result = " ".join(msg.split())
-
-    maxlen = 200
-
-    if len(result) > maxlen:
-        result = result[:maxlen] + "..."
-
-    return result
-
-
 view = Index.as_view("index")
 rule("/", view_func=view, methods=["GET"])
 rule("/index/", view_func=view, methods=["GET"])
```

### Comparing `conbench-2023.4.5/conbench/app/results.py` & `conbench-2023.4.6/conbench/app/results.py`

 * *Files 16% similar despite different names*

```diff
@@ -1,21 +1,22 @@
 import logging
+from typing import Optional
 
 import bokeh
 import flask as f
 import flask_login
 import flask_wtf
 import wtforms as w
 
 import conbench.util
 
 from ..app import rule
 from ..app._endpoint import AppEndpoint, authorize_or_terminate
 from ..app._plots import TimeSeriesPlotMixin
-from ..app._util import augment, display_message, display_time
+from ..app._util import augment, display_time
 from ..config import Config
 
 log = logging.getLogger(__name__)
 
 
 class BenchmarkResultUpdateForm(flask_wtf.FlaskForm):
     title = conbench.util.dedent_rejoin(
@@ -107,41 +108,47 @@
         if response.status_code != 200:
             self.flash("Error getting info.")
             return {}
         return response.json
 
 
 class RunMixin:
-    def get_display_run(self, run_id):
+    def get_display_run(self, run_id) -> Optional[dict]:
         run, response = self._get_run(run_id)
 
         if response.status_code == 404:
-            self.flash(f"Run ID unknown: {run_id}", "info")
+            self.flash(f"Run ID unknown: {run_id}", "info")  # type: ignore
             return None
 
         if response.status_code != 200:
-            self.flash("Error getting run.")
+            log.warning(
+                "virtual http request failed. response: %s, %s",
+                response.status_code,
+                response.text,
+            )
+            self.flash(f"Error getting run with ID: {run_id}")  # type: ignore
             return None
 
         self._augment(run)
         return run
 
     def get_display_baseline_run(self, run_url):
         run, response = self._get_run_by_url(run_url)
         if response.status_code != 200:
-            self.flash("Error getting run.")
+            # "RunMixin" has no attribute "flash"
+            self.flash("Error getting run.")  # type: ignore
             return None
 
         self._augment(run)
         return run
 
     def get_display_runs(self):
         runs, response = self._get_runs()
         if response.status_code != 200:
-            self.flash("Error getting runs.")
+            self.flash("Error getting runs.")  # type: ignore
             return []
 
         for run in runs:
             self._augment(run)
         return runs
 
     def _augment(self, run):
@@ -159,35 +166,36 @@
 
         run["display_name"] = ""
         if run["name"]:
             run["display_name"] = run["name"].split(":", 1)[0]
 
         run["commit"]["display_repository"] = repository_name
 
-        # Note(JP): does run["commit"]["message"] ever result in KeyError?
-        # I think `display_message()` may be thought of constructing the text
-        # for a URL. But.... shrug. This needs consolidation.
-        commit_message = display_message(run["commit"]["message"])
-
-        # Note(JP): run.commit.url and run.commit.display_message seem to be
-        # consumed in the HTML template. Here I am a little lost about the
-        # guarantees -- are they always available? We need to resolve this with
-        # proper type annotations and schemata. Until then, do poor-man's
-        # validation to prevent AttributeError and KeyError.
-        # display_message really seems to be name of the link
-        run["commit"]["display_message"] = commit_message
-        if not commit_message:  # None or empty string
-            # Note(JP): I wonder where the "url" ever got set.
-            # Maybe in the _Serializer(EntitySerializer) for Commit?
-            if run["commit"].get("url"):  # be real conservative
-                run["commit"]["display_message"] = run["commit"].get("url")
-            else:
-                # let the template consume these two keys.
-                run["commit"]["url"] = "#"
-                run["commit"]["display_message"] = "not commit info"
+        # For HTML template processing make it so that the commit dictionary
+        # _always_ has non-empty string value for all of the following
+        # properties:
+        # - "url"
+        # - "display_message"
+        # - "html_commit_anchor_and_msg"
+        #
+        # Expect the "sha" key to be present as a non-empty strings
+
+        c = run["commit"]
+        if c.get("url") is None:
+            # non-empty string value for HTML
+            c["url"] = "#"
+
+        # Assume that run["commit"]["message"] never results in KeyError.
+        # (we will see).
+        short_commit_message = conbench.util.short_commit_msg(c["message"])
+        commit_anchor_text = c["sha"][:7]
+        commit_html_anchor_and_msg = f'<a href="{c["url"]}">{commit_anchor_text}</a> <code>({short_commit_message})</code>'
+
+        c["display_message"] = short_commit_message
+        c["html_anchor_and_msg"] = commit_html_anchor_and_msg
 
     def _display_time(self, obj, field):
         timestring = obj[field]
 
         # Seemingly this can be `None`.
         if isinstance(timestring, str):
             obj[f"display_{field}"] = display_time(timestring)
```

### Comparing `conbench-2023.4.5/conbench/app/robots.py` & `conbench-2023.4.6/conbench/app/robots.py`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/conbench/app/runs.py` & `conbench-2023.4.6/conbench/app/runs.py`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/conbench/app/users.py` & `conbench-2023.4.6/conbench/app/users.py`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/conbench/buildinfo.py` & `conbench-2023.4.6/conbench/buildinfo.py`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/conbench/cli.py` & `conbench-2023.4.6/conbench/cli.py`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/conbench/config.py` & `conbench-2023.4.6/conbench/config.py`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/conbench/db.py` & `conbench-2023.4.6/conbench/db.py`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/conbench/entities/_comparator.py` & `conbench-2023.4.6/conbench/entities/_comparator.py`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/conbench/entities/_entity.py` & `conbench-2023.4.6/conbench/entities/_entity.py`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/conbench/entities/benchmark_result.py` & `conbench-2023.4.6/conbench/entities/benchmark_result.py`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/conbench/entities/commit.py` & `conbench-2023.4.6/conbench/entities/commit.py`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/conbench/entities/compare.py` & `conbench-2023.4.6/conbench/entities/compare.py`

 * *Files 2% similar despite different names*

```diff
@@ -4,15 +4,15 @@
 from ..entities.commit import CommitSerializer
 from ..entities.run import Run
 
 
 class _Serializer(EntitySerializer):
     def _dump(self, commits):
         def _run(contender):
-            baseline = contender.get_baseline_run()
+            baseline = contender.get_default_baseline_run()
             baseline_url, contender_url, compare_url = None, None, None
             baseline_timestamp, contender_timestamp = None, None
 
             if baseline and contender:
                 compare_ids = f"{baseline.id}...{contender.id}"
                 compare_url = f.url_for(
                     "api.compare-runs",
```

### Comparing `conbench-2023.4.5/conbench/entities/context.py` & `conbench-2023.4.6/conbench/entities/context.py`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/conbench/entities/hardware.py` & `conbench-2023.4.6/conbench/entities/hardware.py`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/conbench/entities/history.py` & `conbench-2023.4.6/conbench/entities/history.py`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/conbench/entities/info.py` & `conbench-2023.4.6/conbench/entities/info.py`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/conbench/entities/run.py` & `conbench-2023.4.6/conbench/entities/run.py`

 * *Files 2% similar despite different names*

```diff
@@ -158,25 +158,24 @@
                     f"conflict: a Run with ID {data['id']} already exists"
                 )
             else:
                 raise
 
         return run
 
-    def get_baseline_run(
+    def get_default_baseline_run(
         self,
         commit_limit: int = 20,
-        on_default_branch: bool = False,
         case_id: Optional[str] = None,
         context_id: Optional[str] = None,
     ) -> Optional["Run"]:
         """Return the closest ancestor of this Run, where the ancestor run:
 
         - is in the last ``commit_limit`` commits of this Run's commit ancestry
-        - is on the default branch, if on_default_branch is True (else on any branch)
+        - is on the default branch
         - shares this Run's hardware
         - has a BenchmarkResult with the given case_id/context_id, if those are given
         - if they aren't given, has a BenchmarkResult with the case_id/context_id of
           *any* of this Run's BenchmarkResults
 
         Returns None if there are no matches. This could be a false negative if
         ``commit_limit`` is too low (though note that the query takes longer with a
@@ -185,39 +184,39 @@
         If there are multiple matches, prefer a Run with the same reason as this Run,
         and then find the latest commit, finally tiebreaking by latest Run.timestamp.
         """
         from ..entities.benchmark_result import BenchmarkResult
 
         this_commit: Commit = self.commit
         try:
-            ancestor_commits = (
-                this_commit.commit_ancestry_query
-                # don't count this run's commit
-                .filter(Commit.id != this_commit.id)
-                .order_by(s.desc("commit_order"))
-                .limit(commit_limit)
-                .subquery()
-            )
+            ancestor_commits = this_commit.commit_ancestry_query.subquery()
         except CantFindAncestorCommitsError as e:
-            log.debug(f"Couldn't get_baseline_run() because {e}")
+            log.debug(f"Couldn't get_default_baseline_run() because {e}")
             return None
 
+        ancestor_commits = (
+            Session.query(ancestor_commits)
+            .filter(
+                # don't count this run's commit
+                ancestor_commits.c.ancestor_id != this_commit.id,
+                ancestor_commits.c.on_default_branch.is_(True),
+            )
+            .order_by(s.desc("commit_order"))
+            .limit(commit_limit)
+            .subquery()
+        )
+
         closest_run_id_query = (
             Session.query(BenchmarkResult.run_id)
             .join(Run)
             .join(Hardware)
             .join(ancestor_commits, ancestor_commits.c.ancestor_id == Run.commit_id)
             .filter(Hardware.id == self.hardware_id)
         )
 
-        if on_default_branch:
-            closest_run_id_query = closest_run_id_query.filter(
-                ancestor_commits.c.on_default_branch.is_(True)
-            )
-
         # Filter to the correct case(s)/context(s)
         if case_id and context_id:
             # filter to the given case/context
             closest_run_id_query = closest_run_id_query.filter(
                 BenchmarkResult.case_id == case_id,
                 BenchmarkResult.context_id == context_id,
             )
@@ -246,16 +245,16 @@
             log.debug(
                 "Could not find a matching benchmark_result in this Run's ancestry"
             )
             return None
 
         return Run.get(closest_run_id)
 
-    def get_baseline_id(self):
-        run = self.get_baseline_run()
+    def get_default_baseline_id(self):
+        run = self.get_default_baseline_run()
         return run.id if run else None
 
 
 def commit_fetch_info_and_create_in_db_if_not_exists(
     commit_hash, repo_url, pr_number, branch
 ) -> str:
     """
@@ -400,15 +399,15 @@
                 ),
                 "hardware": f.url_for(
                     "api.hardware", hardware_id=hardware["id"], _external=True
                 ),
             },
         }
         if not self.many:
-            baseline_id, baseline_url = run.get_baseline_id(), None
+            baseline_id, baseline_url = run.get_default_baseline_id(), None
             if baseline_id:
                 baseline_url = f.url_for("api.run", run_id=baseline_id, _external=True)
             result["links"]["baseline"] = baseline_url
         return result
 
 
 class RunSerializer:
```

### Comparing `conbench-2023.4.5/conbench/entities/user.py` & `conbench-2023.4.6/conbench/entities/user.py`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/conbench/gunicorn-conf.py` & `conbench-2023.4.6/conbench/gunicorn-conf.py`

 * *Files 24% similar despite different names*

```diff
@@ -39,7 +39,47 @@
 #
 
 from prometheus_flask_exporter.multiprocess import GunicornInternalPrometheusMetrics
 
 
 def child_exit(server, worker):
     GunicornInternalPrometheusMetrics.mark_process_dead_on_child_exit(worker.pid)
+
+
+# Canonical gunicorn config below this line.
+# https://docs.gunicorn.org/en/stable/settings.html#config-file
+
+
+bind = ["0.0.0.0:5000"]
+
+wsgi_app = "conbench:application"
+
+# Canonical format, plus response generation duration in seconds.
+access_log_format = (
+    '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" (%(L)s s)'
+)
+
+errorlog = "-"  # emit to stderr
+accesslog = "-"  # emit to stdout
+loglevel = "info"  # d efault
+
+# requires setprocname
+# proc_name = 'conbench-gunicorn'
+
+# Reduce connection backlog from default (2048)
+backlog = 300
+
+# Run gunicorn as a single-process N thread model (these are real threads,
+# based on CPython threading.Thread, using Unix pthreads). Assume that C copies
+# of this are created by higher-level orchestration (so that more than one CPU
+# core is after all serving requests).
+# https://github.com/conbench/conbench/issues/1018
+workers = 1
+threads = 10
+
+# This is the worker timeout; an observer process will terminate the observed
+# worker process if the observed process hasn't responded within that
+# timeframe. This was more relevant at times when we ran more than one worker
+# process per gunicorn, and a single HTTP request could render a single process
+# occupied. Keep a large value for now, for the case where all threads in the
+# process process genuine requests (which all take a while to respond to)
+timeout = 120
```

### Comparing `conbench-2023.4.5/conbench/hacks.py` & `conbench-2023.4.6/conbench/hacks.py`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/conbench/logger.py` & `conbench-2023.4.6/conbench/logger.py`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/conbench/machine_info.py` & `conbench-2023.4.6/conbench/machine_info.py`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/conbench/metrics.py` & `conbench-2023.4.6/conbench/metrics.py`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/conbench/runner.py` & `conbench-2023.4.6/conbench/runner.py`

 * *Files 3% similar despite different names*

```diff
@@ -155,46 +155,57 @@
         timing_options = self._get_timing_options(options)
         iterations = timing_options.pop("iterations")
         if iterations < 1:
             raise ValueError(f"Invalid iterations: {iterations}")
 
         try:
             data, output = self._get_timing(f, iterations, timing_options)
+            # It's hard to read what this next function call really does. It
+            # does _not_ publish, but I think it creates a specific data
+            # structure. Should this be in the exception handler? Within
+            # self._get_timing() above we run user-given code, so that is
+            # expected to raise exceptions, and wants to be handled. But which
+            # exceptions is  self.record() expected to raise especially when
+            # _not_ doing HTTP interaction? And why do we handle those
+            # exceptions in the same way as those exceptions that are raised by
+            # user-given code?
             benchmark, _ = self.record(
                 {"data": data, "unit": "s"},
                 name,
                 tags=tags,
                 optional_benchmark_info=optional_benchmark_info,
                 context=context,
                 info=info,
                 github=github,
                 options=options,
                 cluster_info=cluster_info,
                 publish=False,
             )
-        except Exception as e:
+        except Exception as exc:
             error = {"stack_trace": traceback.format_exc()}
             benchmark, _ = self.record(
                 None,
                 name,
                 tags=tags,
                 optional_benchmark_info=optional_benchmark_info,
                 context=context,
                 info=info,
                 github=github,
                 options=options,
                 cluster_info=cluster_info,
                 error=error,
                 publish=False,
             )
-            raise e
+            raise exc
         finally:
             if publish:
-                self.publish(benchmark)
-
+                # It's a bit unclear -- is `benchmark` defined in _all_ cases
+                # when we arrive here?
+                # https://pylint.readthedocs.io/en/latest/user_guide/messages/error/used-before-assignment.html
+                self.publish(benchmark)  # pylint: disable=used-before-assignment
         return benchmark, output
 
 
 class MixinR:
     @functools.cached_property
     def r_info(self):
         return r_info()
```

### Comparing `conbench-2023.4.5/conbench/tests/api/_asserts.py` & `conbench-2023.4.6/conbench/tests/api/_asserts.py`

 * *Files 2% similar despite different names*

```diff
@@ -62,16 +62,18 @@
         assert r.content_type == "application/json", r.content_type
         assert r.json == {"code": 401, "name": "Unauthorized"}, r.json
         errors = ErrorSchema().validate(r.json)
         assert errors == {}, errors
 
     def assert_404_not_found(self, r):
         assert r.status_code == 404, r.status_code
-        assert r.content_type == "application/json", r.content_type
-        assert r.json == {"code": 404, "name": "Not Found"}, r.json
+        assert r.content_type == "application/json", r.content_type + " " + r.text
+        assert r.json["code"] == 404
+        assert r.json["name"] == "Not Found"
+        # allow for additional properties
         errors = ErrorSchema().validate(r.json)
         assert errors == {}, errors
 
 
 class Enforcer(ApiEndpointTest):
     def test_unauthenticated(self, client):
         raise NotImplementedError()
```

### Comparing `conbench-2023.4.5/conbench/tests/api/_expected_docs.py` & `conbench-2023.4.6/conbench/tests/api/_expected_docs.py`

 * *Files 0% similar despite different names*

```diff
@@ -1132,22 +1132,24 @@
                         "type": "object",
                     },
                 },
                 "required": ["info", "name", "optional_info"],
                 "type": "object",
             },
             "Error": {
+                "additionalProperties": True,
                 "properties": {
                     "code": {"description": "HTTP error code", "type": "integer"},
                     "name": {"description": "HTTP error name", "type": "string"},
                 },
                 "required": ["code", "name"],
                 "type": "object",
             },
             "ErrorBadRequest": {
+                "additionalProperties": True,
                 "properties": {
                     "code": {"description": "HTTP error code", "type": "integer"},
                     "description": {
                         "allOf": [{"$ref": "#/components/schemas/ErrorValidation"}],
                         "description": "Additional information about the bad request",
                     },
                     "name": {"description": "HTTP error name", "type": "string"},
```

### Comparing `conbench-2023.4.5/conbench/tests/api/_fixtures.py` & `conbench-2023.4.6/conbench/tests/api/_fixtures.py`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/conbench/tests/api/test_auth.py` & `conbench-2023.4.6/conbench/tests/api/test_auth.py`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/conbench/tests/api/test_commits.py` & `conbench-2023.4.6/conbench/tests/api/test_commits.py`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/conbench/tests/api/test_compare.py` & `conbench-2023.4.6/conbench/tests/api/test_compare.py`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/conbench/tests/api/test_contexts.py` & `conbench-2023.4.6/conbench/tests/api/test_contexts.py`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/conbench/tests/api/test_docs.py` & `conbench-2023.4.6/conbench/tests/api/test_docs.py`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/conbench/tests/api/test_hardware.py` & `conbench-2023.4.6/conbench/tests/api/test_hardware.py`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/conbench/tests/api/test_history.py` & `conbench-2023.4.6/conbench/tests/api/test_history.py`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/conbench/tests/api/test_index.py` & `conbench-2023.4.6/conbench/tests/api/test_index.py`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/conbench/tests/api/test_info.py` & `conbench-2023.4.6/conbench/tests/api/test_info.py`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/conbench/tests/api/test_results.py` & `conbench-2023.4.6/conbench/tests/api/test_results.py`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/conbench/tests/api/test_runs.py` & `conbench-2023.4.6/conbench/tests/api/test_runs.py`

 * *Files 2% similar despite different names*

```diff
@@ -227,14 +227,35 @@
 
         contender_run = contender.run
         baseline_run = baseline.run
 
         response = client.get(f"/api/runs/{contender_run.id}/")
         self.assert_200_ok(response, _expected_entity(contender_run, baseline_run.id))
 
+    def test_baseline_run_always_on_default_branch(self, client):
+        self.authenticate(client)
+        _, benchmark_results = _fixtures.gen_fake_data()
+
+        successes = 0
+        for benchmark_result in benchmark_results:
+            response = client.get(f"/api/runs/{benchmark_result.run_id}/")
+            assert response.status_code == 200, f"bad response: {response.__dict__}"
+            baseline_run_link = response.json["links"].get("baseline")
+            if baseline_run_link:
+                baseline_run_response = client.get(
+                    baseline_run_link.replace("http://localhost", "")
+                )
+                assert (
+                    baseline_run_response.status_code == 200
+                ), f"bad response: {baseline_run_response.__dict__}"
+                assert baseline_run_response.json["commit"]["branch"] == "default"
+                successes += 1
+
+        assert successes == 10
+
 
 class TestRunList(_asserts.ListEnforcer):
     url = "/api/runs/"
     public = True
 
     def _create(self):
         _fixtures.benchmark_result(sha=_fixtures.PARENT)
```

### Comparing `conbench-2023.4.5/conbench/tests/api/test_users.py` & `conbench-2023.4.6/conbench/tests/api/test_users.py`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/conbench/tests/app/_asserts.py` & `conbench-2023.4.6/conbench/tests/app/_asserts.py`

 * *Files 4% similar despite different names*

```diff
@@ -201,15 +201,26 @@
         # assert new_id.encode() not in r2.data
 
         assert b"local-dev-conbench - Sign In" in r2.data, r2.data
 
     def test_unknown(self, client):
         self.authenticate(client)
         unknown_url = self.url.format("unknown")
+
         response = client.get(unknown_url, follow_redirects=True)
+
+        # Special case for the compare API where the parameter
+        # is part of the URL path (not query parameter) and needs to
+        # match a certain pattern. We can make this nicer via UI later,
+        # but for starters a non-matching URL pattern is OK / nice to be
+        # treated as 404 not found (with a hint for the user).
+        if "compare" in unknown_url and response.status_code == 404:
+            if "not found: ellipsis (...) expected as part of URL":
+                return
+
         if getattr(self, "redirect_on_unknown", True):
             assert b"local-dev-conbench - Home" in response.data, response.data
         else:
             title = f"local-dev-conbench - {self.title}".encode()
             assert title in response.data, response.data
```

### Comparing `conbench-2023.4.5/conbench/tests/app/test_auth.py` & `conbench-2023.4.6/conbench/tests/app/test_auth.py`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/conbench/tests/app/test_compare.py` & `conbench-2023.4.6/conbench/tests/app/test_compare.py`

 * *Files 18% similar despite different names*

```diff
@@ -1,30 +1,46 @@
 from ...tests.api import _fixtures
 from ...tests.app import _asserts
 
 
+def _emsg_needle(thing, thingid):
+    """
+    Generate an expected error message.
+
+    The Jinja machinery escapes the single quote (inserts the HTML entity
+    notation &#39;) -- this can be changed via using the |safe operator in the
+    template, but here in this error message we show user-given data so that is
+    the exact case for why the 'sanitization by default' has been built into
+    the templating engine
+    """
+    return f"cannot perform comparison: no benchmark results found for {thing} ID: &#39;{thingid}&#39;"
+
+
 class TestCompareBenchmark(_asserts.GetEnforcer):
     url = "/compare/benchmarks/{}/"
     title = "Compare Benchmarks"
     redirect_on_unknown = False
 
     def _create(self, client):
         benchmark_id = self.create_benchmark(client)
         return f"{benchmark_id}...{benchmark_id}"
 
     def test_flash_messages(self, client):
         self.authenticate(client)
 
-        response = client.get("/compare/benchmarks/unknown/", follow_redirects=True)
+        response = client.get(
+            "/compare/benchmarks/unknown...unknown2/", follow_redirects=True
+        )
         self.assert_page(response, "Compare Benchmarks")
-        assert b"Invalid contender and baseline." in response.data
+
+        assert "cannot perform comparison:" in response.text, response.text
 
         response = client.get("/compare/benchmarks/foo...bar/", follow_redirects=True)
         self.assert_page(response, "Compare Benchmarks")
-        assert b"Data is still collecting (or failed)." in response.data
+        assert "cannot perform comparison:" in response.text
 
 
 class TestCompareBatches(_asserts.GetEnforcer):
     url = "/compare/batches/{}/"
     title = "Compare Batches"
     redirect_on_unknown = False
 
@@ -32,36 +48,37 @@
         self.create_benchmark(client)
         batch_id = _fixtures.VALID_PAYLOAD["batch_id"]
         return f"{batch_id}...{batch_id}"
 
     def test_flash_messages(self, client):
         self.authenticate(client)
 
-        response = client.get("/compare/batches/unknown/", follow_redirects=True)
+        response = client.get(
+            "/compare/batches/unknown...unknown2/", follow_redirects=True
+        )
         self.assert_page(response, "Compare Batches")
-        assert b"Invalid contender and baseline." in response.data
-
+        assert _emsg_needle("batch", "unknown"), response.text
         response = client.get("/compare/batches/foo...bar/", follow_redirects=True)
         self.assert_page(response, "Compare Batches")
-        assert b"Data is still collecting (or failed)." in response.data
+        assert _emsg_needle("batch", "foo"), response.text
 
 
 class TestCompareRuns(_asserts.GetEnforcer):
     url = "/compare/runs/{}/"
     title = "Compare Runs"
     redirect_on_unknown = False
 
     def _create(self, client):
         self.create_benchmark(client)
         run_id = _fixtures.VALID_PAYLOAD["run_id"]
         return f"{run_id}...{run_id}"
 
     def test_flash_messages(self, client):
         self.authenticate(client)
-
-        response = client.get("/compare/runs/unknown/", follow_redirects=True)
+        response = client.get(
+            "/compare/runs/unknown3...unknown2/", follow_redirects=True
+        )
         self.assert_page(response, "Compare Runs")
-        assert b"Invalid contender and baseline." in response.data
-
+        assert _emsg_needle("run", "unknown3") in response.text
         response = client.get("/compare/runs/foo...bar/", follow_redirects=True)
         self.assert_page(response, "Compare Runs")
-        assert b"Data is still collecting (or failed)." in response.data
+        assert _emsg_needle("run", "foo") in response.text
```

### Comparing `conbench-2023.4.5/conbench/tests/app/test_hardware.py` & `conbench-2023.4.6/conbench/tests/app/test_hardware.py`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/conbench/tests/app/test_index.py` & `conbench-2023.4.6/conbench/tests/app/test_index.py`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/conbench/tests/app/test_plots.py` & `conbench-2023.4.6/conbench/tests/app/test_plots.py`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/conbench/tests/app/test_results.py` & `conbench-2023.4.6/conbench/tests/app/test_results.py`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/conbench/tests/app/test_robots.py` & `conbench-2023.4.6/conbench/tests/app/test_robots.py`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/conbench/tests/app/test_runs.py` & `conbench-2023.4.6/conbench/tests/app/test_runs.py`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/conbench/tests/app/test_users.py` & `conbench-2023.4.6/conbench/tests/app/test_users.py`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/conbench/tests/benchmark/_example_benchmarks.py` & `conbench-2023.4.6/conbench/tests/benchmark/_example_benchmarks.py`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/conbench/tests/benchmark/test_cli.py` & `conbench-2023.4.6/conbench/tests/benchmark/test_cli.py`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/conbench/tests/benchmark/test_machine_info.py` & `conbench-2023.4.6/conbench/tests/benchmark/test_machine_info.py`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/conbench/tests/benchmark/test_runner.py` & `conbench-2023.4.6/conbench/tests/benchmark/test_runner.py`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/conbench/tests/benchmark/test_units.py` & `conbench-2023.4.6/conbench/tests/benchmark/test_units.py`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/conbench/tests/benchmark/test_util.py` & `conbench-2023.4.6/conbench/tests/benchmark/test_util.py`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/conbench/tests/conftest.py` & `conbench-2023.4.6/conbench/tests/conftest.py`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/conbench/tests/entities/test_commit.py` & `conbench-2023.4.6/conbench/tests/entities/test_commit.py`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/conbench/tests/entities/test_comparator.py` & `conbench-2023.4.6/conbench/tests/entities/test_comparator.py`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/conbench/tests/entities/test_history.py` & `conbench-2023.4.6/conbench/tests/entities/test_history.py`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/conbench/tests/entities/test_run.py` & `conbench-2023.4.6/conbench/tests/entities/test_run.py`

 * *Files 24% similar despite different names*

```diff
@@ -1,53 +1,39 @@
 import pytest
 
 from ..api import _fixtures
 
 
 @pytest.mark.parametrize(
-    ["on_default_branch", "give_case_and_context", "expected_baseline_run_indexes"],
+    ["give_case_and_context", "expected_baseline_run_indexes"],
     [
         (
             False,
-            False,
-            [None, 0, 1, 2, 1, 1, 5, 6, 5, 5, None, None, None, None, None, None, 5],
-        ),
-        (
-            False,
-            True,
-            [None, 0, 1, 2, 1, 1, 5, 6, 5, 5, None, None, None, None, None, None, 5],
-        ),
-        (
-            True,
-            False,
             [None, 0, 1, 1, 1, 1, 5, 5, 5, 5, None, None, None, None, None, None, 5],
         ),
         (
             True,
-            True,
             [None, 0, 1, 1, 1, 1, 5, 5, 5, 5, None, None, None, None, None, None, 5],
         ),
     ],
 )
-def test_get_baseline_run(
-    on_default_branch, give_case_and_context, expected_baseline_run_indexes
-):
+def test_get_default_baseline_run(give_case_and_context, expected_baseline_run_indexes):
     commits, benchmark_results = _fixtures.gen_fake_data()
     assert len(benchmark_results) == len(
         expected_baseline_run_indexes
     ), "you should test all benchmark_results"
 
     for benchmark_result, expected_baseline_run_ix in zip(
         benchmark_results, expected_baseline_run_indexes
     ):
         case_id = benchmark_result.case_id if give_case_and_context else None
         context_id = benchmark_result.context_id if give_case_and_context else None
 
-        actual_baseline_run = benchmark_result.run.get_baseline_run(
-            on_default_branch=on_default_branch, case_id=case_id, context_id=context_id
+        actual_baseline_run = benchmark_result.run.get_default_baseline_run(
+            case_id=case_id, context_id=context_id
         )
         if expected_baseline_run_ix is None:
             assert actual_baseline_run is None
         else:
             assert (
                 actual_baseline_run == benchmark_results[expected_baseline_run_ix].run
             )
@@ -56,12 +42,12 @@
     new_one = _fixtures.benchmark_result(
         name=benchmark_result.case.name,
         results=[1, 2, 3],
         reason="nightly",
         commit=commits["44444"],
     )
     assert (
-        benchmark_result.run.get_baseline_run(
-            on_default_branch=on_default_branch, case_id=case_id, context_id=context_id
+        benchmark_result.run.get_default_baseline_run(
+            case_id=case_id, context_id=context_id
         )
         == new_one.run
     )
```

### Comparing `conbench-2023.4.5/conbench/tests/helpers.py` & `conbench-2023.4.6/conbench/tests/helpers.py`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/conbench/tests/populate_local_conbench.py` & `conbench-2023.4.6/conbench/tests/populate_local_conbench.py`

 * *Files 0% similar despite different names*

```diff
@@ -353,15 +353,15 @@
 
     runs = []
 
     for i in range(len(commits)):
         for hardware_type in hardware_types:
             for benchmark_language in benchmark_languages:
                 for benchmark_name in benchmark_names:
-                    run_id = f"{hardware_type}{i+1}"
+                    run_id = f"run-on-{hardware_type}-{i+1}"
                     commit, branch = commits[i], branches[i]
                     mean, reason = means[i], reasons[i]
                     timestamp = datetime.datetime.now() + datetime.timedelta(hours=i)
                     if errors[i] and benchmark_name == "csv-read":
                         benchmark_data = generate_benchmarks_data_with_error(
                             run_id,
                             commit,
```

### Comparing `conbench-2023.4.5/conbench/tests/test_util.py` & `conbench-2023.4.6/conbench/tests/test_util.py`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/conbench/units.py` & `conbench-2023.4.6/conbench/units.py`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/conbench/util.py` & `conbench-2023.4.6/conbench/util.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,35 +1,75 @@
 import json
 import logging
 import os
+import re
 import textwrap
 import time
 import urllib.parse
 from datetime import datetime, timezone
 from typing import List, Union, overload
 
 import click
 import requests
 import yaml
 from _pytest.pathlib import import_path
 from requests.adapters import HTTPAdapter
-from requests.packages.urllib3.util.retry import Retry
+
+try:
+    from urllib3.util import Retry
+except ImportError:
+    # Legacy around times where requests had version 2.3 something.
+    from requests.packages.urllib3.util.retry import Retry  # type: ignore[no-redef]
 
 retry_strategy = Retry(
     total=5,
     status_forcelist=[502, 503, 504],
     allowed_methods=frozenset(["GET", "POST"]),
     backoff_factor=4,  # will retry in 2, 4, 8, 16, 32 seconds
 )
 adapter = HTTPAdapter(max_retries=retry_strategy)
 
 
 log = logging.getLogger()
 
 
+def short_commit_msg(msg: str):
+    """
+    Return a string of non-zero length, and with predictable maximum length.
+
+    Substitute multiple whitespace characters with a single space. Overall,
+    truncate at maxlen (see implementation).
+
+    Substitute 40-char hash values with their shortened variant
+
+    If the input is an emtpy string then emit a placeholder message.
+    """
+    # Deal with empty string scenario (not sure if data model allows that),
+    # but it's better to have a definite place holder than putting an empty
+    # string into e.g. HTML.
+    if not msg:
+        return "no-message"
+
+    result = " ".join(msg.split())
+
+    # Shorten what looks like a full-length commit hash.
+    # Might want to use re-based replace, but shrug.
+    for m in re.findall(r"\b[0-9a-f]{40}\b", result):
+        result = result.replace(m, m[:7])
+
+    # Maybe this does not need to be an argument to this function,
+    # then we have consistency across entire code base.
+    maxlen = 150
+
+    if len(result) > maxlen:
+        result = result[:maxlen] + "..."
+
+    return result
+
+
 def tznaive_dt_to_aware_iso8601_for_api(dt: datetime) -> str:
     """We store datetime objects in the database in columns that are configured
     to not track timezone information. By convention, each of those tz-naive
     datetime objects in the database is to be interpreted in UTC. Before
     emitting a stringified variant of such timestamp to an API user, serialize
     to a tz-aware ISO 8601 timestring, indicating UTC (Zulu) time, via adding
     the 'Z'.
@@ -166,15 +206,15 @@
     def _post(self, url, data, expected):
         try:
             if not self.session:
                 self.session = requests.Session()
                 self.session.mount("https://", adapter)
             start = time.monotonic()
             response = self.session.post(url, json=data)
-            log.info("Time to POST", url, time.monotonic() - start)
+            log.info("Time to POST %s: %.5f s", url, time.monotonic() - start)
             if response.status_code != expected:
                 self._unexpected_response("POST", response, url)
         except requests.exceptions.ConnectionError:
             self.session = None
 
     def _unexpected_response(self, method, response, url):
         self._print_error(f"\n{method} {url} failed", red=True)
```

### Comparing `conbench-2023.4.5/conbench.egg-info/PKG-INFO` & `conbench-2023.4.6/conbench.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: conbench
-Version: 2023.4.5
+Version: 2023.4.6
 Summary: Continuous Benchmarking (CB) Framework
 Home-page: https://github.com/conbench/conbench
 Maintainer: Apache Arrow Developers
 Maintainer-email: dev@arrow.apache.org
 Classifier: Programming Language :: Python :: 3.8
 Classifier: License :: OSI Approved :: MIT License
 Requires-Python: >=3.8
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: conbench Version: 2023.4.5 Summary: Continuous
+Metadata-Version: 2.1 Name: conbench Version: 2023.4.6 Summary: Continuous
 Benchmarking (CB) Framework Home-page: https://github.com/conbench/conbench
 Maintainer: Apache Arrow Developers Maintainer-email: dev@arrow.apache.org
 Classifier: Programming Language :: Python :: 3.8 Classifier: License :: OSI
 Approved :: MIT License Requires-Python: >=3.8 Description-Content-Type: text/
 markdown Provides-Extra: server Provides-Extra: dev License-File: LICENSE
                                                                  [Build_Status]
 # Conbench Check out the docs at https://conbench.github.io/conbench.
```

### Comparing `conbench-2023.4.5/conbench.egg-info/SOURCES.txt` & `conbench-2023.4.6/conbench.egg-info/SOURCES.txt`

 * *Files 1% similar despite different names*

```diff
@@ -29,14 +29,15 @@
 conbench.egg-info/top_level.txt
 conbench/api/__init__.py
 conbench/api/_docs.py
 conbench/api/_endpoint.py
 conbench/api/_errors.py
 conbench/api/_examples.py
 conbench/api/_google.py
+conbench/api/_resp.py
 conbench/api/auth.py
 conbench/api/commits.py
 conbench/api/compare.py
 conbench/api/contexts.py
 conbench/api/hardware.py
 conbench/api/history.py
 conbench/api/index.py
```

### Comparing `conbench-2023.4.5/conbench.egg-info/requires.txt` & `conbench-2023.4.6/conbench.egg-info/requires.txt`

 * *Files 10% similar despite different names*

```diff
@@ -40,14 +40,15 @@
 SQLAlchemy>=2
 black
 bs4
 coveralls
 flake8
 isort
 lxml
+pylint
 mypy
 myst-parser
 sphinx
 sphinx-autodoc-typehints
 types-beautifulsoup4
 types-psutil
 types-PyYAML
```

### Comparing `conbench-2023.4.5/conbench.png` & `conbench-2023.4.6/conbench.png`

 * *Files identical despite different names*

### Comparing `conbench-2023.4.5/setup.py` & `conbench-2023.4.6/setup.py`

 * *Files identical despite different names*

