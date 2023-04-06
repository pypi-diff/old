# Comparing `tmp/pytest-tui-1.9.1.tar.gz` & `tmp/pytest-tui-1.9.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pytest-tui-1.9.1.tar", last modified: Thu Mar 30 17:41:13 2023, max compression
+gzip compressed data, was "pytest-tui-1.9.2.tar", last modified: Thu Apr  6 20:34:34 2023, max compression
```

## Comparing `pytest-tui-1.9.1.tar` & `pytest-tui-1.9.2.tar`

### file list

```diff
@@ -1,80 +1,80 @@
-drwxr-xr-x   0 jwr003   (623385768) 542971493        0 2023-03-30 17:41:13.700235 pytest-tui-1.9.1/
--rw-r--r--   0 jwr003   (623385768) 542971493     1138 2023-03-17 12:12:51.000000 pytest-tui-1.9.1/.gitignore
--rw-r--r--   0 jwr003   (623385768) 542971493       25 2023-03-25 06:55:50.000000 pytest-tui-1.9.1/.isort.cfg
--rw-r--r--   0 jwr003   (623385768) 542971493      202 2023-03-25 07:06:04.000000 pytest-tui-1.9.1/.pre-commit-config.yaml
--rw-r--r--   0 jwr003   (623385768) 542971493     7310 2023-03-30 02:58:34.000000 pytest-tui-1.9.1/CHANGELOG.md
--rw-r--r--   0 jwr003   (623385768) 542971493     1079 2022-04-12 03:00:30.000000 pytest-tui-1.9.1/LICENSE
--rw-r--r--   0 jwr003   (623385768) 542971493    10996 2023-03-30 17:41:13.700933 pytest-tui-1.9.1/PKG-INFO
--rw-r--r--   0 jwr003   (623385768) 542971493    10232 2023-03-30 03:07:54.000000 pytest-tui-1.9.1/README.md
--rw-r--r--   0 jwr003   (623385768) 542971493       30 2022-09-15 05:14:38.000000 pytest-tui-1.9.1/conftest.py
-drwxr-xr-x   0 jwr003   (623385768) 542971493        0 2023-03-30 17:41:13.146590 pytest-tui-1.9.1/demo-tests/
--rw-r--r--   0 jwr003   (623385768) 542971493     6240 2023-03-30 07:30:25.000000 pytest-tui-1.9.1/demo-tests/conftest.py
--rw-r--r--   0 jwr003   (623385768) 542971493     1421 2023-02-12 14:23:47.000000 pytest-tui-1.9.1/demo-tests/test_0.py
--rw-r--r--   0 jwr003   (623385768) 542971493    14208 2023-03-30 03:15:11.000000 pytest-tui-1.9.1/demo-tests/test_1.py
--rw-r--r--   0 jwr003   (623385768) 542971493     2824 2023-01-12 06:08:17.000000 pytest-tui-1.9.1/demo-tests/test_2.py
--rw-r--r--   0 jwr003   (623385768) 542971493     2685 2023-03-30 07:30:25.000000 pytest-tui-1.9.1/demo-tests/test_basic.py
--rw-r--r--   0 jwr003   (623385768) 542971493      352 2023-03-17 12:25:50.000000 pytest-tui-1.9.1/demo-tests/test_class.py
--rw-r--r--   0 jwr003   (623385768) 542971493     2227 2023-03-29 05:42:09.000000 pytest-tui-1.9.1/demo-tests/test_hoefling.py
--rw-r--r--   0 jwr003   (623385768) 542971493      276 2022-09-15 05:14:38.000000 pytest-tui-1.9.1/demo-tests/test_issue_1004.py
--rw-r--r--   0 jwr003   (623385768) 542971493    13004 2023-01-12 06:08:17.000000 pytest-tui-1.9.1/demo-tests/test_random_results.py
--rw-r--r--   0 jwr003   (623385768) 542971493      398 2023-01-17 12:50:37.000000 pytest-tui-1.9.1/demo-tests/test_rerun_fixed.py
--rw-r--r--   0 jwr003   (623385768) 542971493      824 2023-03-30 03:00:11.000000 pytest-tui-1.9.1/demo-tests/test_rerun_random.py
--rw-r--r--   0 jwr003   (623385768) 542971493      623 2023-01-12 06:08:17.000000 pytest-tui-1.9.1/demo-tests/test_single_xpass_xfail.py
--rw-r--r--   0 jwr003   (623385768) 542971493     1687 2023-01-12 06:08:17.000000 pytest-tui-1.9.1/demo-tests/test_warnings.py
--rw-r--r--   0 jwr003   (623385768) 542971493     1017 2023-01-12 06:08:17.000000 pytest-tui-1.9.1/demo-tests/test_xpass_xfail.py
-drwxr-xr-x   0 jwr003   (623385768) 542971493        0 2023-03-30 17:41:13.165412 pytest-tui-1.9.1/misc/
--rw-r--r--   0 jwr003   (623385768) 542971493     1441 2023-03-29 05:42:09.000000 pytest-tui-1.9.1/misc/RELEASE_INSTRUCTIONS
--rw-r--r--   0 jwr003   (623385768) 542971493     1453 2023-01-17 12:50:37.000000 pytest-tui-1.9.1/misc/outcome_questions.txt
--rw-r--r--   0 jwr003   (623385768) 542971493      194 2023-03-30 07:23:20.000000 pytest-tui-1.9.1/pytest.ini
-drwxr-xr-x   0 jwr003   (623385768) 542971493        0 2023-03-30 17:41:13.206215 pytest-tui-1.9.1/pytest_tui/
--rw-r--r--   0 jwr003   (623385768) 542971493      144 2023-01-30 05:13:19.000000 pytest-tui-1.9.1/pytest_tui/__init__.py
--rw-r--r--   0 jwr003   (623385768) 542971493     5805 2023-01-12 06:08:17.000000 pytest-tui-1.9.1/pytest_tui/__main__.py
--rw-r--r--   0 jwr003   (623385768) 542971493     9983 2023-03-17 12:12:07.000000 pytest-tui-1.9.1/pytest_tui/_tree_control.py
--rw-r--r--   0 jwr003   (623385768) 542971493    21276 2023-03-30 07:20:11.000000 pytest-tui-1.9.1/pytest_tui/html_gen.py
-drwxr-xr-x   0 jwr003   (623385768) 542971493        0 2023-03-30 17:41:13.260385 pytest-tui-1.9.1/pytest_tui/log_experiments/
--rw-r--r--   0 jwr003   (623385768) 542971493     1817 2023-02-10 01:38:33.000000 pytest-tui-1.9.1/pytest_tui/log_experiments/debug_context.py
--rw-r--r--   0 jwr003   (623385768) 542971493     2911 2023-03-26 08:03:35.000000 pytest-tui-1.9.1/pytest_tui/log_experiments/debug_html_logger.py
--rw-r--r--   0 jwr003   (623385768) 542971493     2888 2023-03-26 08:03:35.000000 pytest-tui-1.9.1/pytest_tui/log_experiments/foldable_loggers.py
--rw-r--r--   0 jwr003   (623385768) 542971493     1777 2023-03-30 07:25:44.000000 pytest-tui-1.9.1/pytest_tui/log_experiments/test_debug_logger_html.py
--rw-r--r--   0 jwr003   (623385768) 542971493     2830 2023-03-30 07:23:20.000000 pytest-tui-1.9.1/pytest_tui/log_experiments/test_me.py
--rw-r--r--   0 jwr003   (623385768) 542971493     4526 2023-03-28 07:44:44.000000 pytest-tui-1.9.1/pytest_tui/log_experiments/tui_logger.py
--rw-r--r--   0 jwr003   (623385768) 542971493    17468 2023-03-30 02:44:06.000000 pytest-tui-1.9.1/pytest_tui/plugin.py
-drwxr-xr-x   0 jwr003   (623385768) 542971493        0 2023-03-30 17:41:13.312641 pytest-tui-1.9.1/pytest_tui/resources/
--rw-r--r--   0 jwr003   (623385768) 542971493     2323 2023-03-30 06:46:50.000000 pytest-tui-1.9.1/pytest_tui/resources/scripts.js
--rw-r--r--   0 jwr003   (623385768) 542971493    26897 2023-03-30 17:09:21.000000 pytest-tui-1.9.1/pytest_tui/resources/styles.css
-drwxr-xr-x   0 jwr003   (623385768) 542971493        0 2023-03-30 17:41:13.394457 pytest-tui-1.9.1/pytest_tui/stuff/
--rw-r--r--   0 jwr003   (623385768) 542971493     1379 2023-03-19 21:33:39.000000 pytest-tui-1.9.1/pytest_tui/stuff/devnotes.md
--rw-r--r--   0 jwr003   (623385768) 542971493      718 2023-03-19 20:03:46.000000 pytest-tui-1.9.1/pytest_tui/stuff/nonprintable_​​characters.md
--rw-r--r--   0 jwr003   (623385768) 542971493      455 2023-03-27 04:29:46.000000 pytest-tui-1.9.1/pytest_tui/stuff/nonprintable_​​characters.txt
--rw-r--r--   0 jwr003   (623385768) 542971493     8855 2023-03-12 23:16:20.000000 pytest-tui-1.9.1/pytest_tui/tui_gen.py
--rw-r--r--   0 jwr003   (623385768) 542971493     9046 2023-03-28 07:43:44.000000 pytest-tui-1.9.1/pytest_tui/utils.py
-drwxr-xr-x   0 jwr003   (623385768) 542971493        0 2023-03-30 17:41:13.223534 pytest-tui-1.9.1/pytest_tui.egg-info/
--rw-r--r--   0 jwr003   (623385768) 542971493    10996 2023-03-30 17:41:11.000000 pytest-tui-1.9.1/pytest_tui.egg-info/PKG-INFO
--rw-r--r--   0 jwr003   (623385768) 542971493     1827 2023-03-30 17:41:12.000000 pytest-tui-1.9.1/pytest_tui.egg-info/SOURCES.txt
--rw-r--r--   0 jwr003   (623385768) 542971493        1 2023-03-30 17:41:11.000000 pytest-tui-1.9.1/pytest_tui.egg-info/dependency_links.txt
--rw-r--r--   0 jwr003   (623385768) 542971493      123 2023-03-30 17:41:11.000000 pytest-tui-1.9.1/pytest_tui.egg-info/entry_points.txt
--rw-r--r--   0 jwr003   (623385768) 542971493      113 2023-03-30 17:41:11.000000 pytest-tui-1.9.1/pytest_tui.egg-info/requires.txt
--rw-r--r--   0 jwr003   (623385768) 542971493       11 2023-03-30 17:41:11.000000 pytest-tui-1.9.1/pytest_tui.egg-info/top_level.txt
-drwxr-xr-x   0 jwr003   (623385768) 542971493        0 2023-03-30 17:41:13.547887 pytest-tui-1.9.1/requirements/
--rw-r--r--   0 jwr003   (623385768) 542971493      111 2023-03-30 03:01:46.000000 pytest-tui-1.9.1/requirements/requirements-dev.in
--rw-r--r--   0 jwr003   (623385768) 542971493     1491 2023-03-30 03:01:51.000000 pytest-tui-1.9.1/requirements/requirements-dev.txt
--rw-r--r--   0 jwr003   (623385768) 542971493      113 2023-03-30 03:01:54.000000 pytest-tui-1.9.1/requirements/requirements.in
--rw-r--r--   0 jwr003   (623385768) 542971493      992 2023-03-30 03:01:56.000000 pytest-tui-1.9.1/requirements/requirements.txt
--rw-r--r--   0 jwr003   (623385768) 542971493       67 2023-03-30 17:41:13.706759 pytest-tui-1.9.1/setup.cfg
--rw-r--r--   0 jwr003   (623385768) 542971493     1661 2023-03-30 04:35:36.000000 pytest-tui-1.9.1/setup.py
-drwxr-xr-x   0 jwr003   (623385768) 542971493        0 2023-03-30 17:41:12.797165 pytest-tui-1.9.1/testing/
-drwxr-xr-x   0 jwr003   (623385768) 542971493        0 2023-03-30 17:41:13.594573 pytest-tui-1.9.1/testing/bash/
--rwxr-xr-x   0 jwr003   (623385768) 542971493     2213 2023-02-01 13:09:09.000000 pytest-tui-1.9.1/testing/bash/test.sh
--rw-r--r--   0 jwr003   (623385768) 542971493      195 2023-02-01 13:08:57.000000 pytest-tui-1.9.1/testing/bash/tui_expect.tcl
-drwxr-xr-x   0 jwr003   (623385768) 542971493        0 2023-03-30 17:41:13.607040 pytest-tui-1.9.1/testing/python/
--rw-r--r--   0 jwr003   (623385768) 542971493        0 2023-01-30 05:37:43.000000 pytest-tui-1.9.1/testing/python/conftest.ini
--rw-r--r--   0 jwr003   (623385768) 542971493      431 2023-01-17 01:43:11.000000 pytest-tui-1.9.1/testing/python/test_pytest_tui.py
-drwxr-xr-x   0 jwr003   (623385768) 542971493        0 2023-03-30 17:41:12.799818 pytest-tui-1.9.1/testing/robot/
-drwxr-xr-x   0 jwr003   (623385768) 542971493        0 2023-03-30 17:41:13.626680 pytest-tui-1.9.1/testing/robot/Resources/
--rw-r--r--   0 jwr003   (623385768) 542971493      129 2023-02-01 13:08:57.000000 pytest-tui-1.9.1/testing/robot/Resources/common.resource
--rw-r--r--   0 jwr003   (623385768) 542971493      420 2023-01-17 12:50:37.000000 pytest-tui-1.9.1/testing/robot/Resources/vars.py
-drwxr-xr-x   0 jwr003   (623385768) 542971493        0 2023-03-30 17:41:13.698341 pytest-tui-1.9.1/testing/robot/Tests/
--rw-r--r--   0 jwr003   (623385768) 542971493     1253 2023-02-01 13:08:57.000000 pytest-tui-1.9.1/testing/robot/Tests/001_test_basic.robot
--rw-r--r--   0 jwr003   (623385768) 542971493      738 2023-02-01 13:08:57.000000 pytest-tui-1.9.1/testing/robot/Tests/002_test_tui.robot
--rw-r--r--   0 jwr003   (623385768) 542971493      345 2023-02-01 13:08:57.000000 pytest-tui-1.9.1/testing/robot/Tests/003_test_tuih.robot
--rw-r--r--   0 jwr003   (623385768) 542971493     1964 2023-02-01 13:08:57.000000 pytest-tui-1.9.1/tox.ini
+drwxr-xr-x   0 jwr003   (623385768) 542971493        0 2023-04-06 20:34:34.910988 pytest-tui-1.9.2/
+-rw-r--r--   0 jwr003   (623385768) 542971493     1138 2023-03-30 17:44:17.000000 pytest-tui-1.9.2/.gitignore
+-rw-r--r--   0 jwr003   (623385768) 542971493       25 2023-03-30 17:44:17.000000 pytest-tui-1.9.2/.isort.cfg
+-rw-r--r--   0 jwr003   (623385768) 542971493      202 2023-03-30 17:44:17.000000 pytest-tui-1.9.2/.pre-commit-config.yaml
+-rw-r--r--   0 jwr003   (623385768) 542971493     7852 2023-04-06 20:07:16.000000 pytest-tui-1.9.2/CHANGELOG.md
+-rw-r--r--   0 jwr003   (623385768) 542971493     1079 2022-04-12 03:00:30.000000 pytest-tui-1.9.2/LICENSE
+-rw-r--r--   0 jwr003   (623385768) 542971493    11442 2023-04-06 20:34:34.911276 pytest-tui-1.9.2/PKG-INFO
+-rw-r--r--   0 jwr003   (623385768) 542971493    10678 2023-04-06 17:30:25.000000 pytest-tui-1.9.2/README.md
+-rw-r--r--   0 jwr003   (623385768) 542971493       30 2022-09-15 05:14:38.000000 pytest-tui-1.9.2/conftest.py
+drwxr-xr-x   0 jwr003   (623385768) 542971493        0 2023-04-06 20:34:34.812182 pytest-tui-1.9.2/demo-tests/
+-rw-r--r--   0 jwr003   (623385768) 542971493     6240 2023-03-30 17:44:17.000000 pytest-tui-1.9.2/demo-tests/conftest.py
+-rw-r--r--   0 jwr003   (623385768) 542971493     1421 2023-02-12 14:23:47.000000 pytest-tui-1.9.2/demo-tests/test_0.py
+-rw-r--r--   0 jwr003   (623385768) 542971493    14208 2023-03-30 17:44:17.000000 pytest-tui-1.9.2/demo-tests/test_1.py
+-rw-r--r--   0 jwr003   (623385768) 542971493     2824 2023-01-12 06:08:17.000000 pytest-tui-1.9.2/demo-tests/test_2.py
+-rw-r--r--   0 jwr003   (623385768) 542971493     2685 2023-03-30 17:44:17.000000 pytest-tui-1.9.2/demo-tests/test_basic.py
+-rw-r--r--   0 jwr003   (623385768) 542971493      352 2023-03-30 17:44:17.000000 pytest-tui-1.9.2/demo-tests/test_class.py
+-rw-r--r--   0 jwr003   (623385768) 542971493     2227 2023-03-30 17:44:17.000000 pytest-tui-1.9.2/demo-tests/test_hoefling.py
+-rw-r--r--   0 jwr003   (623385768) 542971493      276 2022-09-15 05:14:38.000000 pytest-tui-1.9.2/demo-tests/test_issue_1004.py
+-rw-r--r--   0 jwr003   (623385768) 542971493    13004 2023-01-12 06:08:17.000000 pytest-tui-1.9.2/demo-tests/test_random_results.py
+-rw-r--r--   0 jwr003   (623385768) 542971493      398 2023-01-17 12:50:37.000000 pytest-tui-1.9.2/demo-tests/test_rerun_fixed.py
+-rw-r--r--   0 jwr003   (623385768) 542971493      824 2023-03-30 17:44:17.000000 pytest-tui-1.9.2/demo-tests/test_rerun_random.py
+-rw-r--r--   0 jwr003   (623385768) 542971493      623 2023-01-12 06:08:17.000000 pytest-tui-1.9.2/demo-tests/test_single_xpass_xfail.py
+-rw-r--r--   0 jwr003   (623385768) 542971493     1687 2023-01-12 06:08:17.000000 pytest-tui-1.9.2/demo-tests/test_warnings.py
+-rw-r--r--   0 jwr003   (623385768) 542971493     1017 2023-01-12 06:08:17.000000 pytest-tui-1.9.2/demo-tests/test_xpass_xfail.py
+drwxr-xr-x   0 jwr003   (623385768) 542971493        0 2023-04-06 20:34:34.822466 pytest-tui-1.9.2/misc/
+-rw-r--r--   0 jwr003   (623385768) 542971493     1441 2023-03-30 17:44:17.000000 pytest-tui-1.9.2/misc/RELEASE_INSTRUCTIONS
+-rw-r--r--   0 jwr003   (623385768) 542971493     1453 2023-03-30 17:44:17.000000 pytest-tui-1.9.2/misc/outcome_questions.txt
+-rw-r--r--   0 jwr003   (623385768) 542971493      194 2023-04-06 16:55:39.000000 pytest-tui-1.9.2/pytest.ini
+drwxr-xr-x   0 jwr003   (623385768) 542971493        0 2023-04-06 20:34:34.851798 pytest-tui-1.9.2/pytest_tui/
+-rw-r--r--   0 jwr003   (623385768) 542971493      144 2023-01-30 05:13:19.000000 pytest-tui-1.9.2/pytest_tui/__init__.py
+-rw-r--r--   0 jwr003   (623385768) 542971493     5805 2023-04-01 13:46:31.000000 pytest-tui-1.9.2/pytest_tui/__main__.py
+-rw-r--r--   0 jwr003   (623385768) 542971493     9983 2023-04-01 13:46:31.000000 pytest-tui-1.9.2/pytest_tui/_tree_control.py
+-rw-r--r--   0 jwr003   (623385768) 542971493    19487 2023-04-06 20:04:47.000000 pytest-tui-1.9.2/pytest_tui/html_gen.py
+drwxr-xr-x   0 jwr003   (623385768) 542971493        0 2023-04-06 20:34:34.862823 pytest-tui-1.9.2/pytest_tui/log_experiments/
+-rw-r--r--   0 jwr003   (623385768) 542971493     1817 2023-03-30 17:44:17.000000 pytest-tui-1.9.2/pytest_tui/log_experiments/debug_context.py
+-rw-r--r--   0 jwr003   (623385768) 542971493     2911 2023-04-01 13:46:31.000000 pytest-tui-1.9.2/pytest_tui/log_experiments/debug_html_logger.py
+-rw-r--r--   0 jwr003   (623385768) 542971493     2888 2023-04-01 13:46:31.000000 pytest-tui-1.9.2/pytest_tui/log_experiments/foldable_loggers.py
+-rw-r--r--   0 jwr003   (623385768) 542971493     1777 2023-03-30 17:44:17.000000 pytest-tui-1.9.2/pytest_tui/log_experiments/test_debug_logger_html.py
+-rw-r--r--   0 jwr003   (623385768) 542971493     2830 2023-04-01 13:46:31.000000 pytest-tui-1.9.2/pytest_tui/log_experiments/test_me.py
+-rw-r--r--   0 jwr003   (623385768) 542971493     4526 2023-04-06 17:35:00.000000 pytest-tui-1.9.2/pytest_tui/log_experiments/tui_logger.py
+-rw-r--r--   0 jwr003   (623385768) 542971493    17493 2023-04-06 16:42:20.000000 pytest-tui-1.9.2/pytest_tui/plugin.py
+drwxr-xr-x   0 jwr003   (623385768) 542971493        0 2023-04-06 20:34:34.865170 pytest-tui-1.9.2/pytest_tui/resources/
+-rw-r--r--   0 jwr003   (623385768) 542971493     2323 2023-03-30 17:44:17.000000 pytest-tui-1.9.2/pytest_tui/resources/scripts.js
+-rw-r--r--   0 jwr003   (623385768) 542971493    26897 2023-03-30 17:44:17.000000 pytest-tui-1.9.2/pytest_tui/resources/styles.css
+drwxr-xr-x   0 jwr003   (623385768) 542971493        0 2023-04-06 20:34:34.869717 pytest-tui-1.9.2/pytest_tui/stuff/
+-rw-r--r--   0 jwr003   (623385768) 542971493     1379 2023-03-30 17:44:17.000000 pytest-tui-1.9.2/pytest_tui/stuff/devnotes.md
+-rw-r--r--   0 jwr003   (623385768) 542971493      718 2023-03-30 17:44:17.000000 pytest-tui-1.9.2/pytest_tui/stuff/nonprintable_​​characters.md
+-rw-r--r--   0 jwr003   (623385768) 542971493      455 2023-03-30 17:44:17.000000 pytest-tui-1.9.2/pytest_tui/stuff/nonprintable_​​characters.txt
+-rw-r--r--   0 jwr003   (623385768) 542971493     8855 2023-04-01 13:46:31.000000 pytest-tui-1.9.2/pytest_tui/tui_gen.py
+-rw-r--r--   0 jwr003   (623385768) 542971493     9046 2023-04-06 17:35:00.000000 pytest-tui-1.9.2/pytest_tui/utils.py
+drwxr-xr-x   0 jwr003   (623385768) 542971493        0 2023-04-06 20:34:34.857082 pytest-tui-1.9.2/pytest_tui.egg-info/
+-rw-r--r--   0 jwr003   (623385768) 542971493    11442 2023-04-06 20:34:34.000000 pytest-tui-1.9.2/pytest_tui.egg-info/PKG-INFO
+-rw-r--r--   0 jwr003   (623385768) 542971493     1827 2023-04-06 20:34:34.000000 pytest-tui-1.9.2/pytest_tui.egg-info/SOURCES.txt
+-rw-r--r--   0 jwr003   (623385768) 542971493        1 2023-04-06 20:34:34.000000 pytest-tui-1.9.2/pytest_tui.egg-info/dependency_links.txt
+-rw-r--r--   0 jwr003   (623385768) 542971493      123 2023-04-06 20:34:34.000000 pytest-tui-1.9.2/pytest_tui.egg-info/entry_points.txt
+-rw-r--r--   0 jwr003   (623385768) 542971493      113 2023-04-06 20:34:34.000000 pytest-tui-1.9.2/pytest_tui.egg-info/requires.txt
+-rw-r--r--   0 jwr003   (623385768) 542971493       11 2023-04-06 20:34:34.000000 pytest-tui-1.9.2/pytest_tui.egg-info/top_level.txt
+drwxr-xr-x   0 jwr003   (623385768) 542971493        0 2023-04-06 20:34:34.876465 pytest-tui-1.9.2/requirements/
+-rw-r--r--   0 jwr003   (623385768) 542971493      111 2023-03-30 17:44:17.000000 pytest-tui-1.9.2/requirements/requirements-dev.in
+-rw-r--r--   0 jwr003   (623385768) 542971493     1491 2023-04-06 17:32:59.000000 pytest-tui-1.9.2/requirements/requirements-dev.txt
+-rw-r--r--   0 jwr003   (623385768) 542971493      113 2023-03-30 17:44:17.000000 pytest-tui-1.9.2/requirements/requirements.in
+-rw-r--r--   0 jwr003   (623385768) 542971493      992 2023-04-06 17:32:40.000000 pytest-tui-1.9.2/requirements/requirements.txt
+-rw-r--r--   0 jwr003   (623385768) 542971493       67 2023-04-06 20:34:34.919768 pytest-tui-1.9.2/setup.cfg
+-rw-r--r--   0 jwr003   (623385768) 542971493     1661 2023-04-06 17:17:01.000000 pytest-tui-1.9.2/setup.py
+drwxr-xr-x   0 jwr003   (623385768) 542971493        0 2023-04-06 20:34:34.719815 pytest-tui-1.9.2/testing/
+drwxr-xr-x   0 jwr003   (623385768) 542971493        0 2023-04-06 20:34:34.896938 pytest-tui-1.9.2/testing/bash/
+-rwxr-xr-x   0 jwr003   (623385768) 542971493     2231 2023-04-06 20:33:56.000000 pytest-tui-1.9.2/testing/bash/test.sh
+-rw-r--r--   0 jwr003   (623385768) 542971493      195 2023-02-01 13:08:57.000000 pytest-tui-1.9.2/testing/bash/tui_expect.tcl
+drwxr-xr-x   0 jwr003   (623385768) 542971493        0 2023-04-06 20:34:34.900777 pytest-tui-1.9.2/testing/python/
+-rw-r--r--   0 jwr003   (623385768) 542971493        0 2023-01-30 05:37:43.000000 pytest-tui-1.9.2/testing/python/conftest.ini
+-rw-r--r--   0 jwr003   (623385768) 542971493      431 2023-01-17 01:43:11.000000 pytest-tui-1.9.2/testing/python/test_pytest_tui.py
+drwxr-xr-x   0 jwr003   (623385768) 542971493        0 2023-04-06 20:34:34.720635 pytest-tui-1.9.2/testing/robot/
+drwxr-xr-x   0 jwr003   (623385768) 542971493        0 2023-04-06 20:34:34.904837 pytest-tui-1.9.2/testing/robot/Resources/
+-rw-r--r--   0 jwr003   (623385768) 542971493      129 2023-02-01 13:08:57.000000 pytest-tui-1.9.2/testing/robot/Resources/common.resource
+-rw-r--r--   0 jwr003   (623385768) 542971493      420 2023-01-17 12:50:37.000000 pytest-tui-1.9.2/testing/robot/Resources/vars.py
+drwxr-xr-x   0 jwr003   (623385768) 542971493        0 2023-04-06 20:34:34.910166 pytest-tui-1.9.2/testing/robot/Tests/
+-rw-r--r--   0 jwr003   (623385768) 542971493     1253 2023-02-01 13:08:57.000000 pytest-tui-1.9.2/testing/robot/Tests/001_test_basic.robot
+-rw-r--r--   0 jwr003   (623385768) 542971493      738 2023-02-01 13:08:57.000000 pytest-tui-1.9.2/testing/robot/Tests/002_test_tui.robot
+-rw-r--r--   0 jwr003   (623385768) 542971493      345 2023-02-01 13:08:57.000000 pytest-tui-1.9.2/testing/robot/Tests/003_test_tuih.robot
+-rw-r--r--   0 jwr003   (623385768) 542971493     1964 2023-02-01 13:08:57.000000 pytest-tui-1.9.2/tox.ini
```

### Comparing `pytest-tui-1.9.1/.gitignore` & `pytest-tui-1.9.2/.gitignore`

 * *Files identical despite different names*

### Comparing `pytest-tui-1.9.1/CHANGELOG.md` & `pytest-tui-1.9.2/CHANGELOG.md`

 * *Files 3% similar despite different names*

```diff
@@ -1,14 +1,19 @@
 # Changelog
 
 All notable changes to this project will be documented in this file.
 
 The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
 and this project tries to adhere to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).
 
+## [1.9.2] 2023-04-36
+- Fixed issue 100 - an unfortunate bug where if the user does not specify the `--tui-fold-level` option, the HTML report will not render individual test cases correctly (they won't open/close when clicked). `--tui-fold-level ` is still supported but now if user does not specify it, the level defaults to WARNING, and displays the new Foldedd Output section anyway.
+- Fixed minor issue with bash test script not installing faker lib.
+- Fixed exception issue when specifying non-default output filename for HTML report.
+
 ## [1.9.1] 2023-03-30
 - Re-implemented the folding feature for HTML report. This version doesn't rely on the user having to do anything with their tests other than smartly partition their log statements into the proper debug levels for their application (i.e. no clunky logfile shananigans). The folding feature automatically folds all log output that is less than a configurable level. This is controlled with new command line option '--tui-fold-level'. Also, there is a new 'Actions' button in the HTML which folds/unfolds all fold sections.
 - Fix sticky issue with topbar.
 - Pin requirements with pip-tools.
 
 ## [1.9.0] 2023-03-20
 - Added initial implementation for foldable HTML lines (see docstring on class TuiLogger in tui_logger.py for details). This feature is experimental.
```

### Comparing `pytest-tui-1.9.1/LICENSE` & `pytest-tui-1.9.2/LICENSE`

 * *Files identical despite different names*

### Comparing `pytest-tui-1.9.1/PKG-INFO` & `pytest-tui-1.9.2/PKG-INFO`

 * *Files 3% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pytest-tui
-Version: 1.9.1
+Version: 1.9.2
 Summary: Text User Interface (TUI) and HTML report for Pytest test runs
 Home-page: https://github.com/jeffwright13/pytest-tui
 Author: Jeff Wright
 Author-email: jeff.washcloth@gmail.com
 License: MIT
 Keywords: pytest pytest-plugin testing tui textual html
 Classifier: Framework :: Pytest
@@ -44,15 +44,15 @@
 The intent it to make it easier for you to find the specific results you want so you can examine it without all the other results getting in your way.
 
 How does it work in practice? Easy. You just run your Pytest campaigns like you normally would, adding the command line option `--tui` (`pytest --tui`). Your test session will proceed as it always does (always in verbose mode), showing you the familiar terminal output while running. Then, at the end of the session, a TUI or an HTML page can be launched via the included console scripts (`tui` and/or `tuih`). The results are displayed on-screen or in-browser for you to examine. When you're done, just exit the TUI to go back to the terminal, or close the HTML page. Don't worry about losing your test session data. Results are stored to local disk and you can always relaunch the TUI or HTML page using those same console scripts.
 
 Output sections and individual test results are expandable/collapsible, and test summary statistics are displayed for convenience. Both the TUI and the HTML page retain the original pytest ANSI-encoded color output, lending a familiar look and feel.
 
 ## Features
-- **New** Log message folding on the HTML page, configurable by log level!
+- **New** Log message folding on the HTML page, configurable by log level! See "Python Log Message Folding" section below.
 - Launch either or both of the [Textual](https://github.com/Textualize/textual) TUI or the HTML page using built in console scripts
 - ANSI text markup support - whatever the output on your console looks like is how things are going to show up in the TUI
 - Mouse and keyboard support (including scrolling)
 - Support for all output formats/modes:
   - `-v`, `-vv`, `-no-header`, `--showlocals`, `--color=<yes|no|auto>`
   - all variants of `--tb` except "native"
   - "live-log" (aka log_cli)
@@ -71,15 +71,18 @@
   - `loguru`
 
 ## Requirements
 - Pytest >= 6.2.5
 - Python >= 3.8 (but see "Known Limitations/Issues" below if you want to run 3.10+)
 
 ## Installation
-`pip install pytest-tui`
+
+For most users, simply issue the command `pip install pytest-tui` and you are good to go.
+
+For those users wishing to install via a requirements.txt file, they are located in the /requirements directory.
 
 ## Usage
 
 ### Running Your Tests
 
 Pretty much just run pytest like you always do, adding the `--tui` option to the list of command line options:
 
@@ -105,17 +108,17 @@
 
 ### Generating and viewing the HTML File
 
 The HTML output file is located at `<cwd>/ptt_files/html_report.html`. The HTML file is generated and launched via browser when the `tuih` script is invoked on the command line.
 
 ### Python Log Message Folding (HTML file)
 
-New in 1.9.1 is the "folding" feature, which will automatically roll up any output lines from the test run which are from the Python logger and which are at or below a configurable level. This lets you view verbose debug-level output when you need it, and fold it away, out of sight when you don't. There is no special configuration that has to be done to use this feature, other than enabling at run time with the `--tui-fold-level` option (see `pytest --help`).
+New in 1.9.1 is the "folding" feature, which will automatically roll up any output lines from the test run which are from the Python logger and which are at or below a configurable level. This lets you view verbose debug-level output when you need it, and fold it away, out of sight when you don't. There is no special configuration that has to be done to use this feature, other than enabling at run time with the `--tui-fold-level` option (see `pytest --help`). By default, this value is set to WARNING, in keeping with the default level of Python's logging module when creating a new logger.
 
-For example, specifying `--tui-fold-level=DEBUG` will produce a new section in the HTML report file called "Folded Output", which displays the test run's console output with all lines of log level DEBUG folded up. Each folded section can be individually toggled opened/closed by clicking the "Folded DEBUG" line. Or, you can toggle all "Folded DEBUG" sections by clicking the "Fold/Unfold Logs" button inside the "Fold Actions" menu at the top right of the HTML page.
+This new feature produces a section in the HTML report file called "Folded Output", which displays the test run's console output with all lines of the configured log level folded up. Each folded section can be individually toggled opened/closed by clicking the "Folded WARNING" line (or whatever level you have configured). You can toggle all folded sections by clicking the "Fold/Unfold Logs" button inside the "Fold Actions" menu at the top right of the HTML page, and they can be hidden entirely by double-clicking the "Show/Hide Fold Markers" button.
 
 
 ## Known Limitations / Issues
 
 - Python support for 3.10+ is not guaranteed. Changes were made to the `importlib.metadata` library that are not backwards-compatible, and may result in exceptions when attempting to run. I have not had the chance to chase this down definitively, so until such a time that I fully understand the issue, I recommend using Python 3.8 or 3.9. Of course, YMMV...give it a try, and let me know how things go. :-)
 - User interfaces need work:
   - Overall layouts need optimization (I am definitely not a UX guy)
```

### Comparing `pytest-tui-1.9.1/README.md` & `pytest-tui-1.9.2/README.md`

 * *Files 2% similar despite different names*

```diff
@@ -23,15 +23,15 @@
 The intent it to make it easier for you to find the specific results you want so you can examine it without all the other results getting in your way.
 
 How does it work in practice? Easy. You just run your Pytest campaigns like you normally would, adding the command line option `--tui` (`pytest --tui`). Your test session will proceed as it always does (always in verbose mode), showing you the familiar terminal output while running. Then, at the end of the session, a TUI or an HTML page can be launched via the included console scripts (`tui` and/or `tuih`). The results are displayed on-screen or in-browser for you to examine. When you're done, just exit the TUI to go back to the terminal, or close the HTML page. Don't worry about losing your test session data. Results are stored to local disk and you can always relaunch the TUI or HTML page using those same console scripts.
 
 Output sections and individual test results are expandable/collapsible, and test summary statistics are displayed for convenience. Both the TUI and the HTML page retain the original pytest ANSI-encoded color output, lending a familiar look and feel.
 
 ## Features
-- **New** Log message folding on the HTML page, configurable by log level!
+- **New** Log message folding on the HTML page, configurable by log level! See "Python Log Message Folding" section below.
 - Launch either or both of the [Textual](https://github.com/Textualize/textual) TUI or the HTML page using built in console scripts
 - ANSI text markup support - whatever the output on your console looks like is how things are going to show up in the TUI
 - Mouse and keyboard support (including scrolling)
 - Support for all output formats/modes:
   - `-v`, `-vv`, `-no-header`, `--showlocals`, `--color=<yes|no|auto>`
   - all variants of `--tb` except "native"
   - "live-log" (aka log_cli)
@@ -50,15 +50,18 @@
   - `loguru`
 
 ## Requirements
 - Pytest >= 6.2.5
 - Python >= 3.8 (but see "Known Limitations/Issues" below if you want to run 3.10+)
 
 ## Installation
-`pip install pytest-tui`
+
+For most users, simply issue the command `pip install pytest-tui` and you are good to go.
+
+For those users wishing to install via a requirements.txt file, they are located in the /requirements directory.
 
 ## Usage
 
 ### Running Your Tests
 
 Pretty much just run pytest like you always do, adding the `--tui` option to the list of command line options:
 
@@ -84,17 +87,17 @@
 
 ### Generating and viewing the HTML File
 
 The HTML output file is located at `<cwd>/ptt_files/html_report.html`. The HTML file is generated and launched via browser when the `tuih` script is invoked on the command line.
 
 ### Python Log Message Folding (HTML file)
 
-New in 1.9.1 is the "folding" feature, which will automatically roll up any output lines from the test run which are from the Python logger and which are at or below a configurable level. This lets you view verbose debug-level output when you need it, and fold it away, out of sight when you don't. There is no special configuration that has to be done to use this feature, other than enabling at run time with the `--tui-fold-level` option (see `pytest --help`).
+New in 1.9.1 is the "folding" feature, which will automatically roll up any output lines from the test run which are from the Python logger and which are at or below a configurable level. This lets you view verbose debug-level output when you need it, and fold it away, out of sight when you don't. There is no special configuration that has to be done to use this feature, other than enabling at run time with the `--tui-fold-level` option (see `pytest --help`). By default, this value is set to WARNING, in keeping with the default level of Python's logging module when creating a new logger.
 
-For example, specifying `--tui-fold-level=DEBUG` will produce a new section in the HTML report file called "Folded Output", which displays the test run's console output with all lines of log level DEBUG folded up. Each folded section can be individually toggled opened/closed by clicking the "Folded DEBUG" line. Or, you can toggle all "Folded DEBUG" sections by clicking the "Fold/Unfold Logs" button inside the "Fold Actions" menu at the top right of the HTML page.
+This new feature produces a section in the HTML report file called "Folded Output", which displays the test run's console output with all lines of the configured log level folded up. Each folded section can be individually toggled opened/closed by clicking the "Folded WARNING" line (or whatever level you have configured). You can toggle all folded sections by clicking the "Fold/Unfold Logs" button inside the "Fold Actions" menu at the top right of the HTML page, and they can be hidden entirely by double-clicking the "Show/Hide Fold Markers" button.
 
 
 ## Known Limitations / Issues
 
 - Python support for 3.10+ is not guaranteed. Changes were made to the `importlib.metadata` library that are not backwards-compatible, and may result in exceptions when attempting to run. I have not had the chance to chase this down definitively, so until such a time that I fully understand the issue, I recommend using Python 3.8 or 3.9. Of course, YMMV...give it a try, and let me know how things go. :-)
 - User interfaces need work:
   - Overall layouts need optimization (I am definitely not a UX guy)
```

### Comparing `pytest-tui-1.9.1/demo-tests/conftest.py` & `pytest-tui-1.9.2/demo-tests/conftest.py`

 * *Files identical despite different names*

### Comparing `pytest-tui-1.9.1/demo-tests/test_0.py` & `pytest-tui-1.9.2/demo-tests/test_0.py`

 * *Files identical despite different names*

### Comparing `pytest-tui-1.9.1/demo-tests/test_1.py` & `pytest-tui-1.9.2/demo-tests/test_1.py`

 * *Files identical despite different names*

### Comparing `pytest-tui-1.9.1/demo-tests/test_2.py` & `pytest-tui-1.9.2/demo-tests/test_2.py`

 * *Files identical despite different names*

### Comparing `pytest-tui-1.9.1/demo-tests/test_basic.py` & `pytest-tui-1.9.2/demo-tests/test_basic.py`

 * *Files identical despite different names*

### Comparing `pytest-tui-1.9.1/demo-tests/test_hoefling.py` & `pytest-tui-1.9.2/demo-tests/test_hoefling.py`

 * *Files identical despite different names*

### Comparing `pytest-tui-1.9.1/demo-tests/test_random_results.py` & `pytest-tui-1.9.2/demo-tests/test_random_results.py`

 * *Files identical despite different names*

### Comparing `pytest-tui-1.9.1/demo-tests/test_rerun_random.py` & `pytest-tui-1.9.2/demo-tests/test_rerun_random.py`

 * *Files identical despite different names*

### Comparing `pytest-tui-1.9.1/demo-tests/test_single_xpass_xfail.py` & `pytest-tui-1.9.2/demo-tests/test_single_xpass_xfail.py`

 * *Files identical despite different names*

### Comparing `pytest-tui-1.9.1/demo-tests/test_warnings.py` & `pytest-tui-1.9.2/demo-tests/test_warnings.py`

 * *Files identical despite different names*

### Comparing `pytest-tui-1.9.1/demo-tests/test_xpass_xfail.py` & `pytest-tui-1.9.2/demo-tests/test_xpass_xfail.py`

 * *Files identical despite different names*

### Comparing `pytest-tui-1.9.1/misc/RELEASE_INSTRUCTIONS` & `pytest-tui-1.9.2/misc/RELEASE_INSTRUCTIONS`

 * *Files identical despite different names*

### Comparing `pytest-tui-1.9.1/misc/outcome_questions.txt` & `pytest-tui-1.9.2/misc/outcome_questions.txt`

 * *Files identical despite different names*

### Comparing `pytest-tui-1.9.1/pytest_tui/__main__.py` & `pytest-tui-1.9.2/pytest_tui/__main__.py`

 * *Files identical despite different names*

### Comparing `pytest-tui-1.9.1/pytest_tui/_tree_control.py` & `pytest-tui-1.9.2/pytest_tui/_tree_control.py`

 * *Files identical despite different names*

### Comparing `pytest-tui-1.9.1/pytest_tui/html_gen.py` & `pytest-tui-1.9.2/pytest_tui/html_gen.py`

 * *Files 7% similar despite different names*

```diff
@@ -5,33 +5,33 @@
 from datetime import datetime, timezone
 from pathlib import Path
 
 import json2table
 from ansi2html import Ansi2HTMLConverter
 
 from pytest_tui import __version__
-
-# Next 3 lines are saved from earlier CLI-Config work
-# CLI CONFIG SAVED WORK
-# from pytest_tui.__main__ import Cli
-# from pytest_tui.utils import CONFIGFILE, HTML_OUTPUT_FILE, TERMINAL_OUTPUT_FILE, Results
-
 from pytest_tui.utils import (
     HTML_OUTPUT_FILE,
     LOG_LEVEL_MAP,
     PYTEST_TUI_FILES_DIR,
     TERMINAL_OUTPUT_FILE,
     TUI_FOLD_CONTENT_BEGIN,
     TUI_FOLD_CONTENT_END,
     TUI_FOLD_TITLE_BEGIN,
     TUI_FOLD_TITLE_END,
     Results,
     test_session_starts_results_grabber,
 )
 
+# Next 3 lines are saved from earlier CLI-Config work
+# CLI CONFIG SAVED WORK
+# from pytest_tui.__main__ import Cli
+# from pytest_tui.utils import CONFIGFILE, HTML_OUTPUT_FILE, TERMINAL_OUTPUT_FILE, Results
+
+
 CSS_FILE = Path(__file__).parent / "resources" / "styles.css"
 JS_FILE = Path(__file__).parent / "resources" / "scripts.js"
 
 TAB_ABOUT = ["About"]
 TAB_ABOUT_COLOR = {"About": "hsl(199, 100%, 50%)"}
 TABS_RESULTS = [
     "All Tests",
@@ -287,20 +287,14 @@
         # Dropdown for fold-section actions
         if self.results.tui_fold_level:
             tabs_links.extend(
                 [
                     """<span class="dropdown"> <button class="dropbtn" style="color: brown; background-color: #d9ead3">Fold Actions</button> <span class="dropdown-content">"""
                 ]
             )
-            # tabs_links.extend(
-            #     [
-            #         f"""<span><button class="dropdown-item tablinks" style="background-color: {TABS_ACTIONS_COLORS[action]}" onclick="openAction(event, '{action}')" >{action}</button></span>"""
-            #         for action in TABS_ACTIONS
-            #     ]
-            # )
 
             tabs_links.extend(
                 [
                     """<span><button class="dropdown-item tablinks" style="background-color: #a8b3dc" onclick="toggleAllDetails()">Fold/Unfold Logs</button> </span>"""
                 ]
             )
             tabs_links.extend(
@@ -322,21 +316,14 @@
             tabs_links.extend(
                 [
                     f"""<span><button class="tablinks" style="background-color: {TAB_FOLDED_OUTPUT_COLOR[section]}" onclick="openTab(event, '{section}')" >{section}</button></span> </div>"""
                     for section in TAB_FOLDED_OUTPUT
                 ]
             )
 
-        # tab_links_section += """</div>"""
-        # tabs_links.extend(
-        #     [
-        #         f"""<button class="dropdown-item tablinks" style="background-color: {TAB_ACTIONS_COLOR[action]}" onclick="toggleDetails()">Actions</button>"""
-        #         for action in TAB_ACTIONS
-        #     ]
-        # )
         tab_links_section = (
             """<span class="tab">""" + "".join(tabs_links) + """</span>"""
         )
 
         tab_result_content = []
         for tab in TABS_RESULTS:
             if tab == "All Tests":
@@ -479,52 +466,26 @@
         return html_str
 
     def fold_terminal_output(self, level: str) -> str:
         terminal_output_ansi = self.get_terminal_output_ansi()
         lines = terminal_output_ansi.splitlines()
         return self.fold_log_lines(lines, level)
 
-    # def fold_tracebacks(self, lines):
-    #     html_lines = []
-    #     folding = False
-    #     for line in lines:
-    #         if '_ test_' in line:
-    #             if not folding:
-    #                 html_lines.append("<details><summary>Folded DEBUG or INFO</summary>")
-    #                 folding = True
-    #         elif 'Captured log' in line and '-' in line:
-    #             if folding:
-    #                 html_lines.append('</details>')
-    #                 folding = False
-    #         html_lines.append(self.converter.convert(line, full=False))
-    #     if folding:
-    #         html_lines.append('</details>')
-    #     return '\n'.join(html_lines)
-
-    # def fold_terminal_output(self) -> str:
-    #     terminal_output_ansi = self.get_terminal_output_ansi()
-    #     lines = terminal_output_ansi.splitlines()
-    #     return self.fold_tracebacks(lines)
-
 
 def main():
     results = Results()
     page = HtmlPage(results)
     page.remove_tabs_without_content()
     html_header = page.create_header()
     html_tabs = page.create_tabs()
-    # html_action_button = """<button class="dropdown-item tablinks btn-rt" style="background-color: rgba(249, 123, 64, 0.95)" onclick="toggleDetails()">Actions</button>"""
     html_trailer = page.create_trailer()
     html_out = html_header + html_tabs + html_trailer
 
     global HTML_OUTPUT_FILE
-    if (
-        "tui_htmlfile" in results.tui_test_info
-        and results.tui_test_info["tui_htmlfile"].name
-    ):
+    if results.tui_test_info.get("tui_htmlfile"):
         HTML_OUTPUT_FILE = Path(
             PYTEST_TUI_FILES_DIR / results.tui_test_info["tui_htmlfile"]
         )
     with open(HTML_OUTPUT_FILE, "w+") as f:
         f.write(html_out)
     webbrowser.open(f"file://{HTML_OUTPUT_FILE._str}")
```

### Comparing `pytest-tui-1.9.1/pytest_tui/log_experiments/debug_context.py` & `pytest-tui-1.9.2/pytest_tui/log_experiments/debug_context.py`

 * *Files identical despite different names*

### Comparing `pytest-tui-1.9.1/pytest_tui/log_experiments/debug_html_logger.py` & `pytest-tui-1.9.2/pytest_tui/log_experiments/debug_html_logger.py`

 * *Files identical despite different names*

### Comparing `pytest-tui-1.9.1/pytest_tui/log_experiments/foldable_loggers.py` & `pytest-tui-1.9.2/pytest_tui/log_experiments/foldable_loggers.py`

 * *Files identical despite different names*

### Comparing `pytest-tui-1.9.1/pytest_tui/log_experiments/test_debug_logger_html.py` & `pytest-tui-1.9.2/pytest_tui/log_experiments/test_debug_logger_html.py`

 * *Files identical despite different names*

### Comparing `pytest-tui-1.9.1/pytest_tui/log_experiments/test_me.py` & `pytest-tui-1.9.2/pytest_tui/log_experiments/test_me.py`

 * *Files identical despite different names*

### Comparing `pytest-tui-1.9.1/pytest_tui/log_experiments/tui_logger.py` & `pytest-tui-1.9.2/pytest_tui/log_experiments/tui_logger.py`

 * *Files identical despite different names*

### Comparing `pytest-tui-1.9.1/pytest_tui/plugin.py` & `pytest-tui-1.9.2/pytest_tui/plugin.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,9 @@
 import itertools
+import logging
 import pickle
 import re
 import tempfile
 from concurrent.futures.thread import ThreadPoolExecutor
 from datetime import datetime, timezone
 from io import StringIO
 from types import SimpleNamespace
@@ -159,21 +160,21 @@
 
     # Set default fold level, if specified on the command line
     if (
         hasattr(config.option, "tui_fold_level")
         and not config.option.tui_fold_level
         or not hasattr(config.option, "tui_fold_level")
     ):
-        config._tui_fold_level = None
+        config._tui_fold_level = "WARNING"
     else:
         config._tui_fold_level = (
             config.option.tui_fold_level
             if config.option.tui_fold_level.lower()
             in ["debug", "info", "warning", "error", "critical"]
-            else None
+            else "WARNING"
         )
 
 
 def pytest_report_teststatus(report: TestReport, config: Config) -> None:
     # Don't process any TUI-specific code if the plugin is not enabled
     if not hasattr(config.option, "tui"):
         return
```

### Comparing `pytest-tui-1.9.1/pytest_tui/resources/scripts.js` & `pytest-tui-1.9.2/pytest_tui/resources/scripts.js`

 * *Files identical despite different names*

### Comparing `pytest-tui-1.9.1/pytest_tui/resources/styles.css` & `pytest-tui-1.9.2/pytest_tui/resources/styles.css`

 * *Files identical despite different names*

### Comparing `pytest-tui-1.9.1/pytest_tui/stuff/devnotes.md` & `pytest-tui-1.9.2/pytest_tui/stuff/devnotes.md`

 * *Files identical despite different names*

### Comparing `pytest-tui-1.9.1/pytest_tui/stuff/nonprintable_​​characters.md` & `pytest-tui-1.9.2/pytest_tui/stuff/nonprintable_​​characters.md`

 * *Files identical despite different names*

### Comparing `pytest-tui-1.9.1/pytest_tui/tui_gen.py` & `pytest-tui-1.9.2/pytest_tui/tui_gen.py`

 * *Files identical despite different names*

### Comparing `pytest-tui-1.9.1/pytest_tui/utils.py` & `pytest-tui-1.9.2/pytest_tui/utils.py`

 * *Files identical despite different names*

### Comparing `pytest-tui-1.9.1/pytest_tui.egg-info/PKG-INFO` & `pytest-tui-1.9.2/pytest_tui.egg-info/PKG-INFO`

 * *Files 3% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pytest-tui
-Version: 1.9.1
+Version: 1.9.2
 Summary: Text User Interface (TUI) and HTML report for Pytest test runs
 Home-page: https://github.com/jeffwright13/pytest-tui
 Author: Jeff Wright
 Author-email: jeff.washcloth@gmail.com
 License: MIT
 Keywords: pytest pytest-plugin testing tui textual html
 Classifier: Framework :: Pytest
@@ -44,15 +44,15 @@
 The intent it to make it easier for you to find the specific results you want so you can examine it without all the other results getting in your way.
 
 How does it work in practice? Easy. You just run your Pytest campaigns like you normally would, adding the command line option `--tui` (`pytest --tui`). Your test session will proceed as it always does (always in verbose mode), showing you the familiar terminal output while running. Then, at the end of the session, a TUI or an HTML page can be launched via the included console scripts (`tui` and/or `tuih`). The results are displayed on-screen or in-browser for you to examine. When you're done, just exit the TUI to go back to the terminal, or close the HTML page. Don't worry about losing your test session data. Results are stored to local disk and you can always relaunch the TUI or HTML page using those same console scripts.
 
 Output sections and individual test results are expandable/collapsible, and test summary statistics are displayed for convenience. Both the TUI and the HTML page retain the original pytest ANSI-encoded color output, lending a familiar look and feel.
 
 ## Features
-- **New** Log message folding on the HTML page, configurable by log level!
+- **New** Log message folding on the HTML page, configurable by log level! See "Python Log Message Folding" section below.
 - Launch either or both of the [Textual](https://github.com/Textualize/textual) TUI or the HTML page using built in console scripts
 - ANSI text markup support - whatever the output on your console looks like is how things are going to show up in the TUI
 - Mouse and keyboard support (including scrolling)
 - Support for all output formats/modes:
   - `-v`, `-vv`, `-no-header`, `--showlocals`, `--color=<yes|no|auto>`
   - all variants of `--tb` except "native"
   - "live-log" (aka log_cli)
@@ -71,15 +71,18 @@
   - `loguru`
 
 ## Requirements
 - Pytest >= 6.2.5
 - Python >= 3.8 (but see "Known Limitations/Issues" below if you want to run 3.10+)
 
 ## Installation
-`pip install pytest-tui`
+
+For most users, simply issue the command `pip install pytest-tui` and you are good to go.
+
+For those users wishing to install via a requirements.txt file, they are located in the /requirements directory.
 
 ## Usage
 
 ### Running Your Tests
 
 Pretty much just run pytest like you always do, adding the `--tui` option to the list of command line options:
 
@@ -105,17 +108,17 @@
 
 ### Generating and viewing the HTML File
 
 The HTML output file is located at `<cwd>/ptt_files/html_report.html`. The HTML file is generated and launched via browser when the `tuih` script is invoked on the command line.
 
 ### Python Log Message Folding (HTML file)
 
-New in 1.9.1 is the "folding" feature, which will automatically roll up any output lines from the test run which are from the Python logger and which are at or below a configurable level. This lets you view verbose debug-level output when you need it, and fold it away, out of sight when you don't. There is no special configuration that has to be done to use this feature, other than enabling at run time with the `--tui-fold-level` option (see `pytest --help`).
+New in 1.9.1 is the "folding" feature, which will automatically roll up any output lines from the test run which are from the Python logger and which are at or below a configurable level. This lets you view verbose debug-level output when you need it, and fold it away, out of sight when you don't. There is no special configuration that has to be done to use this feature, other than enabling at run time with the `--tui-fold-level` option (see `pytest --help`). By default, this value is set to WARNING, in keeping with the default level of Python's logging module when creating a new logger.
 
-For example, specifying `--tui-fold-level=DEBUG` will produce a new section in the HTML report file called "Folded Output", which displays the test run's console output with all lines of log level DEBUG folded up. Each folded section can be individually toggled opened/closed by clicking the "Folded DEBUG" line. Or, you can toggle all "Folded DEBUG" sections by clicking the "Fold/Unfold Logs" button inside the "Fold Actions" menu at the top right of the HTML page.
+This new feature produces a section in the HTML report file called "Folded Output", which displays the test run's console output with all lines of the configured log level folded up. Each folded section can be individually toggled opened/closed by clicking the "Folded WARNING" line (or whatever level you have configured). You can toggle all folded sections by clicking the "Fold/Unfold Logs" button inside the "Fold Actions" menu at the top right of the HTML page, and they can be hidden entirely by double-clicking the "Show/Hide Fold Markers" button.
 
 
 ## Known Limitations / Issues
 
 - Python support for 3.10+ is not guaranteed. Changes were made to the `importlib.metadata` library that are not backwards-compatible, and may result in exceptions when attempting to run. I have not had the chance to chase this down definitively, so until such a time that I fully understand the issue, I recommend using Python 3.8 or 3.9. Of course, YMMV...give it a try, and let me know how things go. :-)
 - User interfaces need work:
   - Overall layouts need optimization (I am definitely not a UX guy)
```

### Comparing `pytest-tui-1.9.1/pytest_tui.egg-info/SOURCES.txt` & `pytest-tui-1.9.2/pytest_tui.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `pytest-tui-1.9.1/requirements/requirements-dev.txt` & `pytest-tui-1.9.2/requirements/requirements-dev.txt`

 * *Files identical despite different names*

### Comparing `pytest-tui-1.9.1/requirements/requirements.txt` & `pytest-tui-1.9.2/requirements/requirements.txt`

 * *Files identical despite different names*

### Comparing `pytest-tui-1.9.1/setup.py` & `pytest-tui-1.9.2/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -10,15 +10,15 @@
 def read(fname):
     file_path = os.path.join(os.path.dirname(__file__), fname)
     return codecs.open(file_path, encoding="utf-8").read()
 
 
 setup(
     name="pytest-tui",
-    version="1.9.1",
+    version="1.9.2",
     author="Jeff Wright",
     author_email="jeff.washcloth@gmail.com",
     license="MIT",
     url="https://github.com/jeffwright13/pytest-tui",
     description="Text User Interface (TUI) and HTML report for Pytest test runs",
     long_description=read("README.md"),
     long_description_content_type="text/markdown",
```

### Comparing `pytest-tui-1.9.1/testing/bash/test.sh` & `pytest-tui-1.9.2/testing/bash/test.sh`

 * *Files 1% similar despite different names*

```diff
@@ -38,14 +38,15 @@
 
 printf "Upgrading build tools\n"
 pip install --upgrade pip setuptools wheel
 
 printf "Installing pytest-tui from Test-PyPi\n"
 pip install -i https://test.pypi.org/simple/ pytest-tui
 pip install pytest-rerunfailures
+pip install faker
 
 printf "Cloning pytest-tui so we can use its demo-tests\n"
 git clone git@github.com:jeffwright13/pytest-tui.git
 mkdir demo-tests
 cp pytest-tui/demo-tests/* ./demo-tests/
 clean_up pytest-tui
 ls -la demo-tests/
```

### Comparing `pytest-tui-1.9.1/testing/robot/Tests/001_test_basic.robot` & `pytest-tui-1.9.2/testing/robot/Tests/001_test_basic.robot`

 * *Files identical despite different names*

### Comparing `pytest-tui-1.9.1/testing/robot/Tests/002_test_tui.robot` & `pytest-tui-1.9.2/testing/robot/Tests/002_test_tui.robot`

 * *Files identical despite different names*

### Comparing `pytest-tui-1.9.1/tox.ini` & `pytest-tui-1.9.2/tox.ini`

 * *Files identical despite different names*

