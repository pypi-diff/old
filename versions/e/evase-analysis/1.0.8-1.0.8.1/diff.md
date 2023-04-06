# Comparing `tmp/evase-analysis-1.0.8.tar.gz` & `tmp/evase-analysis-1.0.8.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "evase-analysis-1.0.8.tar", last modified: Thu Apr  6 17:21:52 2023, max compression
+gzip compressed data, was "evase-analysis-1.0.8.1.tar", last modified: Thu Apr  6 17:27:32 2023, max compression
```

## Comparing `evase-analysis-1.0.8.tar` & `evase-analysis-1.0.8.1.tar`

### file list

```diff
@@ -1,97 +1,97 @@
-drwxrwxrwx   0        0        0        0 2023-04-06 17:21:52.531699 evase-analysis-1.0.8/
--rw-rw-rw-   0        0        0     7071 2023-04-06 17:21:52.531699 evase-analysis-1.0.8/PKG-INFO
--rw-rw-rw-   0        0        0     6230 2023-04-04 20:11:33.000000 evase-analysis-1.0.8/README.md
-drwxrwxrwx   0        0        0        0 2023-04-06 17:21:52.476575 evase-analysis-1.0.8/docs/
--rw-rw-rw-   0        0        0     1166 2023-03-30 01:19:57.000000 evase-analysis-1.0.8/docs/conf.py
-drwxrwxrwx   0        0        0        0 2023-04-06 17:21:52.477574 evase-analysis-1.0.8/evase/
--rw-rw-rw-   0        0        0        0 2023-03-27 20:42:02.000000 evase-analysis-1.0.8/evase/__init__.py
-drwxrwxrwx   0        0        0        0 2023-04-06 17:21:52.481082 evase-analysis-1.0.8/evase/depanalyze/
--rw-rw-rw-   0        0        0        0 2023-03-27 20:42:02.000000 evase-analysis-1.0.8/evase/depanalyze/__init__.py
--rw-rw-rw-   0        0        0     9152 2023-04-04 19:22:58.000000 evase-analysis-1.0.8/evase/depanalyze/codetraversalnode.py
--rw-rw-rw-   0        0        0    12059 2023-04-04 19:22:58.000000 evase-analysis-1.0.8/evase/depanalyze/importresolver.py
--rw-rw-rw-   0        0        0     3829 2023-04-04 19:22:58.000000 evase-analysis-1.0.8/evase/depanalyze/scoperesolver.py
--rw-rw-rw-   0        0        0    15873 2023-04-04 19:22:58.000000 evase-analysis-1.0.8/evase/depanalyze/searching.py
--rw-rw-rw-   0        0        0     1450 2023-04-04 19:22:58.000000 evase-analysis-1.0.8/evase/depanalyze/surfacedetector.py
-drwxrwxrwx   0        0        0        0 2023-04-06 17:21:52.482089 evase-analysis-1.0.8/evase/exceptions/
--rw-rw-rw-   0        0        0        0 2023-04-04 19:22:58.000000 evase-analysis-1.0.8/evase/exceptions/__init__.py
--rw-rw-rw-   0        0        0      626 2023-04-04 19:22:58.000000 evase-analysis-1.0.8/evase/exceptions/exceptions.py
-drwxrwxrwx   0        0        0        0 2023-04-06 17:21:52.484096 evase-analysis-1.0.8/evase/sql_injection/
--rw-rw-rw-   0        0        0        0 2023-03-27 20:42:02.000000 evase-analysis-1.0.8/evase/sql_injection/__init__.py
--rw-rw-rw-   0        0        0     4242 2023-03-27 20:42:02.000000 evase-analysis-1.0.8/evase/sql_injection/injectionutil.py
--rw-rw-rw-   0        0        0     6537 2023-04-06 16:36:00.000000 evase-analysis-1.0.8/evase/sql_injection/injectionvisitor.py
--rw-rw-rw-   0        0        0    10947 2023-04-06 16:39:55.000000 evase-analysis-1.0.8/evase/sql_injection/vulnerabletraversal.py
-drwxrwxrwx   0        0        0        0 2023-04-06 17:21:52.486096 evase-analysis-1.0.8/evase/structures/
--rw-rw-rw-   0        0        0        0 2023-03-27 20:42:02.000000 evase-analysis-1.0.8/evase/structures/__init__.py
--rw-rw-rw-   0        0        0    15018 2023-04-06 16:40:47.000000 evase-analysis-1.0.8/evase/structures/analysisperformer.py
--rw-rw-rw-   0        0        0     5410 2023-04-06 16:21:46.000000 evase-analysis-1.0.8/evase/structures/modulestructure.py
--rw-rw-rw-   0        0        0     6608 2023-04-06 16:28:41.000000 evase-analysis-1.0.8/evase/structures/projectstructure.py
-drwxrwxrwx   0        0        0        0 2023-04-06 17:21:52.488097 evase-analysis-1.0.8/evase/util/
--rw-rw-rw-   0        0        0        0 2023-03-30 01:19:57.000000 evase-analysis-1.0.8/evase/util/__init__.py
--rw-rw-rw-   0        0        0     3012 2023-04-06 16:44:37.000000 evase-analysis-1.0.8/evase/util/fileutil.py
--rw-rw-rw-   0        0        0     1444 2023-04-06 16:47:02.000000 evase-analysis-1.0.8/evase/util/logger.py
-drwxrwxrwx   0        0        0        0 2023-04-06 17:21:52.505145 evase-analysis-1.0.8/evase_analysis.egg-info/
--rw-rw-rw-   0        0        0     7071 2023-04-06 17:21:52.000000 evase-analysis-1.0.8/evase_analysis.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0     2685 2023-04-06 17:21:52.000000 evase-analysis-1.0.8/evase_analysis.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-06 17:21:52.000000 evase-analysis-1.0.8/evase_analysis.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       61 2023-04-06 17:21:52.000000 evase-analysis-1.0.8/evase_analysis.egg-info/requires.txt
--rw-rw-rw-   0        0        0       28 2023-04-06 17:21:52.000000 evase-analysis-1.0.8/evase_analysis.egg-info/top_level.txt
--rw-rw-rw-   0        0        0     1343 2023-04-06 17:21:30.000000 evase-analysis-1.0.8/pyproject.toml
--rw-rw-rw-   0        0        0       42 2023-04-06 17:21:52.531699 evase-analysis-1.0.8/setup.cfg
-drwxrwxrwx   0        0        0        0 2023-04-06 17:21:52.508149 evase-analysis-1.0.8/tests/
-drwxrwxrwx   0        0        0        0 2023-04-06 17:21:52.513670 evase-analysis-1.0.8/tests/resources/
--rw-rw-rw-   0        0        0        0 2023-03-27 20:42:02.000000 evase-analysis-1.0.8/tests/resources/__init__.py
-drwxrwxrwx   0        0        0        0 2023-04-06 17:21:52.473577 evase-analysis-1.0.8/tests/resources/demo/
-drwxrwxrwx   0        0        0        0 2023-04-06 17:21:52.518668 evase-analysis-1.0.8/tests/resources/demo/backend/
--rw-rw-rw-   0        0        0        0 2023-03-27 20:42:02.000000 evase-analysis-1.0.8/tests/resources/demo/backend/__init__.py
--rw-rw-rw-   0        0        0     1108 2023-03-30 01:20:00.000000 evase-analysis-1.0.8/tests/resources/demo/backend/app.py
--rw-rw-rw-   0        0        0     1098 2023-03-27 20:42:02.000000 evase-analysis-1.0.8/tests/resources/demo/backend/vul.py
--rw-rw-rw-   0        0        0     1140 2023-03-30 01:20:00.000000 evase-analysis-1.0.8/tests/resources/demo/backend/vul_wrapper.py
-drwxrwxrwx   0        0        0        0 2023-04-06 17:21:52.472576 evase-analysis-1.0.8/tests/resources/demo2/
-drwxrwxrwx   0        0        0        0 2023-04-06 17:21:52.515669 evase-analysis-1.0.8/tests/resources/demo2/demonstration/
--rw-rw-rw-   0        0        0        0 2023-03-27 20:42:02.000000 evase-analysis-1.0.8/tests/resources/demo2/demonstration/__init__.py
--rw-rw-rw-   0        0        0      185 2023-03-27 20:42:02.000000 evase-analysis-1.0.8/tests/resources/demo2/demonstration/api.py
--rw-rw-rw-   0        0        0      183 2023-03-27 20:42:02.000000 evase-analysis-1.0.8/tests/resources/demo2/demonstration/controller.py
--rw-rw-rw-   0        0        0      458 2023-03-27 20:42:02.000000 evase-analysis-1.0.8/tests/resources/demo2/demonstration/model.py
-drwxrwxrwx   0        0        0        0 2023-04-06 17:21:52.520175 evase-analysis-1.0.8/tests/resources/prjstructtest/
--rw-rw-rw-   0        0        0        0 2023-03-27 20:42:02.000000 evase-analysis-1.0.8/tests/resources/prjstructtest/__init__.py
--rw-rw-rw-   0        0        0      290 2023-03-27 20:42:02.000000 evase-analysis-1.0.8/tests/resources/prjstructtest/runner.py
-drwxrwxrwx   0        0        0        0 2023-04-06 17:21:52.521184 evase-analysis-1.0.8/tests/resources/prjstructtest/test/
--rw-rw-rw-   0        0        0        0 2023-03-27 20:42:02.000000 evase-analysis-1.0.8/tests/resources/prjstructtest/test/__init__.py
-drwxrwxrwx   0        0        0        0 2023-04-06 17:21:52.522183 evase-analysis-1.0.8/tests/resources/prjstructtest/util/
--rw-rw-rw-   0        0        0        0 2023-03-27 20:42:02.000000 evase-analysis-1.0.8/tests/resources/prjstructtest/util/__init__.py
--rw-rw-rw-   0        0        0      163 2023-03-27 20:42:02.000000 evase-analysis-1.0.8/tests/resources/prjstructtest/util/helper.py
-drwxrwxrwx   0        0        0        0 2023-04-06 17:21:52.523190 evase-analysis-1.0.8/tests/resources/prjstructtest/util/moreutil/
--rw-rw-rw-   0        0        0        0 2023-03-27 20:42:02.000000 evase-analysis-1.0.8/tests/resources/prjstructtest/util/moreutil/__init__.py
--rw-rw-rw-   0        0        0       79 2023-03-27 20:42:02.000000 evase-analysis-1.0.8/tests/resources/prjstructtest/util/moreutil/helper2.py
--rw-rw-rw-   0        0        0      306 2023-03-27 20:42:02.000000 evase-analysis-1.0.8/tests/resources/screstest.py
--rw-rw-rw-   0        0        0      108 2023-03-27 20:42:02.000000 evase-analysis-1.0.8/tests/resources/sql_injection_safe1.py
--rw-rw-rw-   0        0        0      150 2023-03-27 20:42:02.000000 evase-analysis-1.0.8/tests/resources/sql_injection_safe2.py
--rw-rw-rw-   0        0        0      128 2023-03-27 20:42:02.000000 evase-analysis-1.0.8/tests/resources/sql_injection_vul1.py
--rw-rw-rw-   0        0        0      122 2023-03-27 20:42:02.000000 evase-analysis-1.0.8/tests/resources/sql_injection_vul2.py
--rw-rw-rw-   0        0        0      130 2023-03-27 20:42:02.000000 evase-analysis-1.0.8/tests/resources/sql_injection_vul3.py
--rw-rw-rw-   0        0        0      122 2023-03-27 20:42:02.000000 evase-analysis-1.0.8/tests/resources/sql_injection_vul4.py
--rw-rw-rw-   0        0        0      535 2023-03-27 20:42:02.000000 evase-analysis-1.0.8/tests/resources/sql_injection_vul5.py
--rw-rw-rw-   0        0        0     5135 2023-03-27 20:42:02.000000 evase-analysis-1.0.8/tests/resources/sql_injection_vul6.py
-drwxrwxrwx   0        0        0        0 2023-04-06 17:21:52.526190 evase-analysis-1.0.8/tests/resources/type_demo/
--rw-rw-rw-   0        0        0      911 2023-03-27 20:42:02.000000 evase-analysis-1.0.8/tests/resources/type_demo/app.py
--rw-rw-rw-   0        0        0      280 2023-03-27 20:42:02.000000 evase-analysis-1.0.8/tests/resources/type_demo/create_db.py
--rw-rw-rw-   0        0        0      759 2023-03-27 20:42:02.000000 evase-analysis-1.0.8/tests/resources/type_demo/user_db_handler.py
--rw-rw-rw-   0        0        0      700 2023-03-27 20:42:02.000000 evase-analysis-1.0.8/tests/resources/type_demo/vul.py
--rw-rw-rw-   0        0        0      732 2023-03-27 20:42:02.000000 evase-analysis-1.0.8/tests/resources/type_demo/vul_wrapper.py
-drwxrwxrwx   0        0        0        0 2023-04-06 17:21:52.474577 evase-analysis-1.0.8/tests/resources/webgoat/
-drwxrwxrwx   0        0        0        0 2023-04-06 17:21:52.529190 evase-analysis-1.0.8/tests/resources/webgoat/flask_webgoat/
--rw-rw-rw-   0        0        0     1534 2023-03-30 01:20:00.000000 evase-analysis-1.0.8/tests/resources/webgoat/flask_webgoat/__init__.py
--rw-rw-rw-   0        0        0     2063 2023-03-30 01:20:00.000000 evase-analysis-1.0.8/tests/resources/webgoat/flask_webgoat/actions.py
--rw-rw-rw-   0        0        0     1633 2023-03-30 01:20:00.000000 evase-analysis-1.0.8/tests/resources/webgoat/flask_webgoat/auth.py
--rw-rw-rw-   0        0        0      232 2023-03-30 01:20:00.000000 evase-analysis-1.0.8/tests/resources/webgoat/flask_webgoat/status.py
-drwxrwxrwx   0        0        0        0 2023-04-06 17:21:52.530889 evase-analysis-1.0.8/tests/resources/webgoat/flask_webgoat/templates/
--rw-rw-rw-   0        0        0       89 2023-03-30 01:20:00.000000 evase-analysis-1.0.8/tests/resources/webgoat/flask_webgoat/templates/__init__.py
--rw-rw-rw-   0        0        0       32 2023-03-30 01:20:00.000000 evase-analysis-1.0.8/tests/resources/webgoat/flask_webgoat/templates/hello.py
--rw-rw-rw-   0        0        0       77 2023-03-30 01:20:00.000000 evase-analysis-1.0.8/tests/resources/webgoat/flask_webgoat/templates/helper.py
--rw-rw-rw-   0        0        0      850 2023-03-30 01:20:00.000000 evase-analysis-1.0.8/tests/resources/webgoat/flask_webgoat/ui.py
--rw-rw-rw-   0        0        0     1488 2023-03-30 01:20:00.000000 evase-analysis-1.0.8/tests/resources/webgoat/flask_webgoat/users.py
--rw-rw-rw-   0        0        0     2026 2023-04-04 20:06:40.000000 evase-analysis-1.0.8/tests/test_analysisperformer.py
--rw-rw-rw-   0        0        0     2593 2023-04-04 20:06:40.000000 evase-analysis-1.0.8/tests/test_fileutil.py
--rw-rw-rw-   0        0        0     1618 2023-04-04 20:06:40.000000 evase-analysis-1.0.8/tests/test_projectstructure.py
--rw-rw-rw-   0        0        0     1639 2023-04-04 20:06:40.000000 evase-analysis-1.0.8/tests/test_scoperesolver.py
--rw-rw-rw-   0        0        0     1714 2023-04-04 20:06:40.000000 evase-analysis-1.0.8/tests/testutil.py
+drwxrwxrwx   0        0        0        0 2023-04-06 17:27:32.046330 evase-analysis-1.0.8.1/
+-rw-rw-rw-   0        0        0     7073 2023-04-06 17:27:32.046330 evase-analysis-1.0.8.1/PKG-INFO
+-rw-rw-rw-   0        0        0     6230 2023-04-04 20:11:33.000000 evase-analysis-1.0.8.1/README.md
+drwxrwxrwx   0        0        0        0 2023-04-06 17:27:31.999734 evase-analysis-1.0.8.1/docs/
+-rw-rw-rw-   0        0        0     1166 2023-03-30 01:19:57.000000 evase-analysis-1.0.8.1/docs/conf.py
+drwxrwxrwx   0        0        0        0 2023-04-06 17:27:31.999734 evase-analysis-1.0.8.1/evase/
+-rw-rw-rw-   0        0        0        0 2023-03-27 20:42:02.000000 evase-analysis-1.0.8.1/evase/__init__.py
+drwxrwxrwx   0        0        0        0 2023-04-06 17:27:32.003749 evase-analysis-1.0.8.1/evase/depanalyze/
+-rw-rw-rw-   0        0        0        0 2023-03-27 20:42:02.000000 evase-analysis-1.0.8.1/evase/depanalyze/__init__.py
+-rw-rw-rw-   0        0        0     9152 2023-04-04 19:22:58.000000 evase-analysis-1.0.8.1/evase/depanalyze/codetraversalnode.py
+-rw-rw-rw-   0        0        0    12059 2023-04-04 19:22:58.000000 evase-analysis-1.0.8.1/evase/depanalyze/importresolver.py
+-rw-rw-rw-   0        0        0     3829 2023-04-04 19:22:58.000000 evase-analysis-1.0.8.1/evase/depanalyze/scoperesolver.py
+-rw-rw-rw-   0        0        0    15873 2023-04-04 19:22:58.000000 evase-analysis-1.0.8.1/evase/depanalyze/searching.py
+-rw-rw-rw-   0        0        0     1450 2023-04-04 19:22:58.000000 evase-analysis-1.0.8.1/evase/depanalyze/surfacedetector.py
+drwxrwxrwx   0        0        0        0 2023-04-06 17:27:32.004749 evase-analysis-1.0.8.1/evase/exceptions/
+-rw-rw-rw-   0        0        0        0 2023-04-04 19:22:58.000000 evase-analysis-1.0.8.1/evase/exceptions/__init__.py
+-rw-rw-rw-   0        0        0      626 2023-04-04 19:22:58.000000 evase-analysis-1.0.8.1/evase/exceptions/exceptions.py
+drwxrwxrwx   0        0        0        0 2023-04-06 17:27:32.006747 evase-analysis-1.0.8.1/evase/sql_injection/
+-rw-rw-rw-   0        0        0        0 2023-03-27 20:42:02.000000 evase-analysis-1.0.8.1/evase/sql_injection/__init__.py
+-rw-rw-rw-   0        0        0     4242 2023-03-27 20:42:02.000000 evase-analysis-1.0.8.1/evase/sql_injection/injectionutil.py
+-rw-rw-rw-   0        0        0     6537 2023-04-06 16:36:00.000000 evase-analysis-1.0.8.1/evase/sql_injection/injectionvisitor.py
+-rw-rw-rw-   0        0        0    10947 2023-04-06 16:39:55.000000 evase-analysis-1.0.8.1/evase/sql_injection/vulnerabletraversal.py
+drwxrwxrwx   0        0        0        0 2023-04-06 17:27:32.007750 evase-analysis-1.0.8.1/evase/structures/
+-rw-rw-rw-   0        0        0        0 2023-03-27 20:42:02.000000 evase-analysis-1.0.8.1/evase/structures/__init__.py
+-rw-rw-rw-   0        0        0    15046 2023-04-06 17:26:34.000000 evase-analysis-1.0.8.1/evase/structures/analysisperformer.py
+-rw-rw-rw-   0        0        0     5410 2023-04-06 16:21:46.000000 evase-analysis-1.0.8.1/evase/structures/modulestructure.py
+-rw-rw-rw-   0        0        0     6608 2023-04-06 16:28:41.000000 evase-analysis-1.0.8.1/evase/structures/projectstructure.py
+drwxrwxrwx   0        0        0        0 2023-04-06 17:27:32.010263 evase-analysis-1.0.8.1/evase/util/
+-rw-rw-rw-   0        0        0        0 2023-03-30 01:19:57.000000 evase-analysis-1.0.8.1/evase/util/__init__.py
+-rw-rw-rw-   0        0        0     3012 2023-04-06 16:44:37.000000 evase-analysis-1.0.8.1/evase/util/fileutil.py
+-rw-rw-rw-   0        0        0     1444 2023-04-06 16:47:02.000000 evase-analysis-1.0.8.1/evase/util/logger.py
+drwxrwxrwx   0        0        0        0 2023-04-06 17:27:32.022788 evase-analysis-1.0.8.1/evase_analysis.egg-info/
+-rw-rw-rw-   0        0        0     7073 2023-04-06 17:27:31.000000 evase-analysis-1.0.8.1/evase_analysis.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0     2685 2023-04-06 17:27:31.000000 evase-analysis-1.0.8.1/evase_analysis.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-06 17:27:31.000000 evase-analysis-1.0.8.1/evase_analysis.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       61 2023-04-06 17:27:31.000000 evase-analysis-1.0.8.1/evase_analysis.egg-info/requires.txt
+-rw-rw-rw-   0        0        0       28 2023-04-06 17:27:31.000000 evase-analysis-1.0.8.1/evase_analysis.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0     1345 2023-04-06 17:27:01.000000 evase-analysis-1.0.8.1/pyproject.toml
+-rw-rw-rw-   0        0        0       42 2023-04-06 17:27:32.046330 evase-analysis-1.0.8.1/setup.cfg
+drwxrwxrwx   0        0        0        0 2023-04-06 17:27:32.025786 evase-analysis-1.0.8.1/tests/
+drwxrwxrwx   0        0        0        0 2023-04-06 17:27:32.031301 evase-analysis-1.0.8.1/tests/resources/
+-rw-rw-rw-   0        0        0        0 2023-03-27 20:42:02.000000 evase-analysis-1.0.8.1/tests/resources/__init__.py
+drwxrwxrwx   0        0        0        0 2023-04-06 17:27:31.996227 evase-analysis-1.0.8.1/tests/resources/demo/
+drwxrwxrwx   0        0        0        0 2023-04-06 17:27:32.035307 evase-analysis-1.0.8.1/tests/resources/demo/backend/
+-rw-rw-rw-   0        0        0        0 2023-03-27 20:42:02.000000 evase-analysis-1.0.8.1/tests/resources/demo/backend/__init__.py
+-rw-rw-rw-   0        0        0     1108 2023-03-30 01:20:00.000000 evase-analysis-1.0.8.1/tests/resources/demo/backend/app.py
+-rw-rw-rw-   0        0        0     1098 2023-03-27 20:42:02.000000 evase-analysis-1.0.8.1/tests/resources/demo/backend/vul.py
+-rw-rw-rw-   0        0        0     1140 2023-03-30 01:20:00.000000 evase-analysis-1.0.8.1/tests/resources/demo/backend/vul_wrapper.py
+drwxrwxrwx   0        0        0        0 2023-04-06 17:27:31.996227 evase-analysis-1.0.8.1/tests/resources/demo2/
+drwxrwxrwx   0        0        0        0 2023-04-06 17:27:32.033306 evase-analysis-1.0.8.1/tests/resources/demo2/demonstration/
+-rw-rw-rw-   0        0        0        0 2023-03-27 20:42:02.000000 evase-analysis-1.0.8.1/tests/resources/demo2/demonstration/__init__.py
+-rw-rw-rw-   0        0        0      185 2023-03-27 20:42:02.000000 evase-analysis-1.0.8.1/tests/resources/demo2/demonstration/api.py
+-rw-rw-rw-   0        0        0      183 2023-03-27 20:42:02.000000 evase-analysis-1.0.8.1/tests/resources/demo2/demonstration/controller.py
+-rw-rw-rw-   0        0        0      458 2023-03-27 20:42:02.000000 evase-analysis-1.0.8.1/tests/resources/demo2/demonstration/model.py
+drwxrwxrwx   0        0        0        0 2023-04-06 17:27:32.035307 evase-analysis-1.0.8.1/tests/resources/prjstructtest/
+-rw-rw-rw-   0        0        0        0 2023-03-27 20:42:02.000000 evase-analysis-1.0.8.1/tests/resources/prjstructtest/__init__.py
+-rw-rw-rw-   0        0        0      290 2023-03-27 20:42:02.000000 evase-analysis-1.0.8.1/tests/resources/prjstructtest/runner.py
+drwxrwxrwx   0        0        0        0 2023-04-06 17:27:32.036306 evase-analysis-1.0.8.1/tests/resources/prjstructtest/test/
+-rw-rw-rw-   0        0        0        0 2023-03-27 20:42:02.000000 evase-analysis-1.0.8.1/tests/resources/prjstructtest/test/__init__.py
+drwxrwxrwx   0        0        0        0 2023-04-06 17:27:32.037307 evase-analysis-1.0.8.1/tests/resources/prjstructtest/util/
+-rw-rw-rw-   0        0        0        0 2023-03-27 20:42:02.000000 evase-analysis-1.0.8.1/tests/resources/prjstructtest/util/__init__.py
+-rw-rw-rw-   0        0        0      163 2023-03-27 20:42:02.000000 evase-analysis-1.0.8.1/tests/resources/prjstructtest/util/helper.py
+drwxrwxrwx   0        0        0        0 2023-04-06 17:27:32.038308 evase-analysis-1.0.8.1/tests/resources/prjstructtest/util/moreutil/
+-rw-rw-rw-   0        0        0        0 2023-03-27 20:42:02.000000 evase-analysis-1.0.8.1/tests/resources/prjstructtest/util/moreutil/__init__.py
+-rw-rw-rw-   0        0        0       79 2023-03-27 20:42:02.000000 evase-analysis-1.0.8.1/tests/resources/prjstructtest/util/moreutil/helper2.py
+-rw-rw-rw-   0        0        0      306 2023-03-27 20:42:02.000000 evase-analysis-1.0.8.1/tests/resources/screstest.py
+-rw-rw-rw-   0        0        0      108 2023-03-27 20:42:02.000000 evase-analysis-1.0.8.1/tests/resources/sql_injection_safe1.py
+-rw-rw-rw-   0        0        0      150 2023-03-27 20:42:02.000000 evase-analysis-1.0.8.1/tests/resources/sql_injection_safe2.py
+-rw-rw-rw-   0        0        0      128 2023-03-27 20:42:02.000000 evase-analysis-1.0.8.1/tests/resources/sql_injection_vul1.py
+-rw-rw-rw-   0        0        0      122 2023-03-27 20:42:02.000000 evase-analysis-1.0.8.1/tests/resources/sql_injection_vul2.py
+-rw-rw-rw-   0        0        0      130 2023-03-27 20:42:02.000000 evase-analysis-1.0.8.1/tests/resources/sql_injection_vul3.py
+-rw-rw-rw-   0        0        0      122 2023-03-27 20:42:02.000000 evase-analysis-1.0.8.1/tests/resources/sql_injection_vul4.py
+-rw-rw-rw-   0        0        0      535 2023-03-27 20:42:02.000000 evase-analysis-1.0.8.1/tests/resources/sql_injection_vul5.py
+-rw-rw-rw-   0        0        0     5135 2023-03-27 20:42:02.000000 evase-analysis-1.0.8.1/tests/resources/sql_injection_vul6.py
+drwxrwxrwx   0        0        0        0 2023-04-06 17:27:32.039815 evase-analysis-1.0.8.1/tests/resources/type_demo/
+-rw-rw-rw-   0        0        0      911 2023-03-27 20:42:02.000000 evase-analysis-1.0.8.1/tests/resources/type_demo/app.py
+-rw-rw-rw-   0        0        0      280 2023-03-27 20:42:02.000000 evase-analysis-1.0.8.1/tests/resources/type_demo/create_db.py
+-rw-rw-rw-   0        0        0      759 2023-03-27 20:42:02.000000 evase-analysis-1.0.8.1/tests/resources/type_demo/user_db_handler.py
+-rw-rw-rw-   0        0        0      700 2023-03-27 20:42:02.000000 evase-analysis-1.0.8.1/tests/resources/type_demo/vul.py
+-rw-rw-rw-   0        0        0      732 2023-03-27 20:42:02.000000 evase-analysis-1.0.8.1/tests/resources/type_demo/vul_wrapper.py
+drwxrwxrwx   0        0        0        0 2023-04-06 17:27:31.998227 evase-analysis-1.0.8.1/tests/resources/webgoat/
+drwxrwxrwx   0        0        0        0 2023-04-06 17:27:32.044330 evase-analysis-1.0.8.1/tests/resources/webgoat/flask_webgoat/
+-rw-rw-rw-   0        0        0     1534 2023-03-30 01:20:00.000000 evase-analysis-1.0.8.1/tests/resources/webgoat/flask_webgoat/__init__.py
+-rw-rw-rw-   0        0        0     2063 2023-03-30 01:20:00.000000 evase-analysis-1.0.8.1/tests/resources/webgoat/flask_webgoat/actions.py
+-rw-rw-rw-   0        0        0     1633 2023-03-30 01:20:00.000000 evase-analysis-1.0.8.1/tests/resources/webgoat/flask_webgoat/auth.py
+-rw-rw-rw-   0        0        0      232 2023-03-30 01:20:00.000000 evase-analysis-1.0.8.1/tests/resources/webgoat/flask_webgoat/status.py
+drwxrwxrwx   0        0        0        0 2023-04-06 17:27:32.045331 evase-analysis-1.0.8.1/tests/resources/webgoat/flask_webgoat/templates/
+-rw-rw-rw-   0        0        0       89 2023-03-30 01:20:00.000000 evase-analysis-1.0.8.1/tests/resources/webgoat/flask_webgoat/templates/__init__.py
+-rw-rw-rw-   0        0        0       32 2023-03-30 01:20:00.000000 evase-analysis-1.0.8.1/tests/resources/webgoat/flask_webgoat/templates/hello.py
+-rw-rw-rw-   0        0        0       77 2023-03-30 01:20:00.000000 evase-analysis-1.0.8.1/tests/resources/webgoat/flask_webgoat/templates/helper.py
+-rw-rw-rw-   0        0        0      850 2023-03-30 01:20:00.000000 evase-analysis-1.0.8.1/tests/resources/webgoat/flask_webgoat/ui.py
+-rw-rw-rw-   0        0        0     1488 2023-03-30 01:20:00.000000 evase-analysis-1.0.8.1/tests/resources/webgoat/flask_webgoat/users.py
+-rw-rw-rw-   0        0        0     2026 2023-04-04 20:06:40.000000 evase-analysis-1.0.8.1/tests/test_analysisperformer.py
+-rw-rw-rw-   0        0        0     2593 2023-04-04 20:06:40.000000 evase-analysis-1.0.8.1/tests/test_fileutil.py
+-rw-rw-rw-   0        0        0     1618 2023-04-04 20:06:40.000000 evase-analysis-1.0.8.1/tests/test_projectstructure.py
+-rw-rw-rw-   0        0        0     1639 2023-04-04 20:06:40.000000 evase-analysis-1.0.8.1/tests/test_scoperesolver.py
+-rw-rw-rw-   0        0        0     1714 2023-04-04 20:06:40.000000 evase-analysis-1.0.8.1/tests/testutil.py
```

### Comparing `evase-analysis-1.0.8/PKG-INFO` & `evase-analysis-1.0.8.1/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: evase-analysis
-Version: 1.0.8
+Version: 1.0.8.1
 Summary: A Python package with tools for the detection of SQL injection vulnerabilities in projects.
 Author-email: Tony Abou Zeidan <tony.azp25@gmail.com>, Anthony Dooley <anthonydooley@cmail.carleton.ca>, Ethan Chase <e281828c@gmail.com>, Shaopeng Liu <shaopengliu@cmail.carleton.ca>, Jason Jaskolka <jason.jaskolka@carleton.ca>
 Maintainer-email: Tony Abou Zeidan <tony.azp25@gmail.com>, Anthony Dooley <anthonydooley@cmail.carleton.ca>, Ethan Chase <e281828c@gmail.com>, Shaopeng Liu <shaopengliu@cmail.carleton.ca>, Jason Jaskolka <jason.jaskolka@carleton.ca>
 Keywords: attack,security,SQL,injection
 Classifier: Programming Language :: Python :: 3 :: Only
 Classifier: Programming Language :: Python :: 3
 Requires-Python: >=3.7
```

### Comparing `evase-analysis-1.0.8/README.md` & `evase-analysis-1.0.8.1/README.md`

 * *Files identical despite different names*

### Comparing `evase-analysis-1.0.8/docs/conf.py` & `evase-analysis-1.0.8.1/docs/conf.py`

 * *Files identical despite different names*

### Comparing `evase-analysis-1.0.8/evase/depanalyze/codetraversalnode.py` & `evase-analysis-1.0.8.1/evase/depanalyze/codetraversalnode.py`

 * *Files identical despite different names*

### Comparing `evase-analysis-1.0.8/evase/depanalyze/importresolver.py` & `evase-analysis-1.0.8.1/evase/depanalyze/importresolver.py`

 * *Files identical despite different names*

### Comparing `evase-analysis-1.0.8/evase/depanalyze/scoperesolver.py` & `evase-analysis-1.0.8.1/evase/depanalyze/scoperesolver.py`

 * *Files identical despite different names*

### Comparing `evase-analysis-1.0.8/evase/depanalyze/searching.py` & `evase-analysis-1.0.8.1/evase/depanalyze/searching.py`

 * *Files identical despite different names*

### Comparing `evase-analysis-1.0.8/evase/depanalyze/surfacedetector.py` & `evase-analysis-1.0.8.1/evase/depanalyze/surfacedetector.py`

 * *Files identical despite different names*

### Comparing `evase-analysis-1.0.8/evase/exceptions/exceptions.py` & `evase-analysis-1.0.8.1/evase/exceptions/exceptions.py`

 * *Files identical despite different names*

### Comparing `evase-analysis-1.0.8/evase/sql_injection/injectionutil.py` & `evase-analysis-1.0.8.1/evase/sql_injection/injectionutil.py`

 * *Files identical despite different names*

### Comparing `evase-analysis-1.0.8/evase/sql_injection/injectionvisitor.py` & `evase-analysis-1.0.8.1/evase/sql_injection/injectionvisitor.py`

 * *Files identical despite different names*

### Comparing `evase-analysis-1.0.8/evase/sql_injection/vulnerabletraversal.py` & `evase-analysis-1.0.8.1/evase/sql_injection/vulnerabletraversal.py`

 * *Files identical despite different names*

### Comparing `evase-analysis-1.0.8/evase/structures/analysisperformer.py` & `evase-analysis-1.0.8.1/evase/structures/analysisperformer.py`

 * *Files 0% similar despite different names*

```diff
@@ -179,15 +179,16 @@
         :param project_root: The root directory of the project
         """
 
         self.project_name = project_name
         self.project_root = check_path(project_root, file_ok=False, file_req=False, absolute_req=False, ret_absolute=True)
         if output_path is not None:
             output_path = check_path(output_path, file_ok=False, file_req=False, absolute_req=False, ret_absolute=True)
-            AnalysisLogger.log_path = output_path
+            AnalysisLogger.log_path = Path(output_path, 'analysis-log.log')
+
         self.analysis_results = {}
 
         self.sql_injection_detector = SQLInjectionBehaviourAnalyzer()
 
     def perform_analysis(self):
         """
         Performs analysis on the code structure that is currently loaded.
```

### Comparing `evase-analysis-1.0.8/evase/structures/modulestructure.py` & `evase-analysis-1.0.8.1/evase/structures/modulestructure.py`

 * *Files identical despite different names*

### Comparing `evase-analysis-1.0.8/evase/structures/projectstructure.py` & `evase-analysis-1.0.8.1/evase/structures/projectstructure.py`

 * *Files identical despite different names*

### Comparing `evase-analysis-1.0.8/evase/util/fileutil.py` & `evase-analysis-1.0.8.1/evase/util/fileutil.py`

 * *Files identical despite different names*

### Comparing `evase-analysis-1.0.8/evase/util/logger.py` & `evase-analysis-1.0.8.1/evase/util/logger.py`

 * *Files identical despite different names*

### Comparing `evase-analysis-1.0.8/evase_analysis.egg-info/PKG-INFO` & `evase-analysis-1.0.8.1/evase_analysis.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: evase-analysis
-Version: 1.0.8
+Version: 1.0.8.1
 Summary: A Python package with tools for the detection of SQL injection vulnerabilities in projects.
 Author-email: Tony Abou Zeidan <tony.azp25@gmail.com>, Anthony Dooley <anthonydooley@cmail.carleton.ca>, Ethan Chase <e281828c@gmail.com>, Shaopeng Liu <shaopengliu@cmail.carleton.ca>, Jason Jaskolka <jason.jaskolka@carleton.ca>
 Maintainer-email: Tony Abou Zeidan <tony.azp25@gmail.com>, Anthony Dooley <anthonydooley@cmail.carleton.ca>, Ethan Chase <e281828c@gmail.com>, Shaopeng Liu <shaopengliu@cmail.carleton.ca>, Jason Jaskolka <jason.jaskolka@carleton.ca>
 Keywords: attack,security,SQL,injection
 Classifier: Programming Language :: Python :: 3 :: Only
 Classifier: Programming Language :: Python :: 3
 Requires-Python: >=3.7
```

### Comparing `evase-analysis-1.0.8/evase_analysis.egg-info/SOURCES.txt` & `evase-analysis-1.0.8.1/evase_analysis.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `evase-analysis-1.0.8/pyproject.toml` & `evase-analysis-1.0.8.1/pyproject.toml`

 * *Files 7% similar despite different names*

```diff
@@ -18,15 +18,15 @@
     {name = "Shaopeng Liu", email="shaopengliu@cmail.carleton.ca"},
     {name = "Jason Jaskolka", email="jason.jaskolka@carleton.ca"}
 ]
 description = "A Python package with tools for the detection of SQL injection vulnerabilities in projects."
 readme = "README.md"
 requires-python = ">=3.7"
 keywords = ["attack", "security", "SQL", "injection"]
-version="1.0.8"
+version="1.0.8.1"
 classifiers=[
     "Programming Language :: Python :: 3 :: Only",
     "Programming Language :: Python :: 3"
 ]
 dependencies = [
     'Flask~=2.2.2',
     'Jinja2~=3.1.2',
```

### Comparing `evase-analysis-1.0.8/tests/resources/demo/backend/app.py` & `evase-analysis-1.0.8.1/tests/resources/demo/backend/app.py`

 * *Files identical despite different names*

### Comparing `evase-analysis-1.0.8/tests/resources/demo/backend/vul.py` & `evase-analysis-1.0.8.1/tests/resources/demo/backend/vul.py`

 * *Files identical despite different names*

### Comparing `evase-analysis-1.0.8/tests/resources/demo/backend/vul_wrapper.py` & `evase-analysis-1.0.8.1/tests/resources/demo/backend/vul_wrapper.py`

 * *Files identical despite different names*

### Comparing `evase-analysis-1.0.8/tests/resources/sql_injection_vul5.py` & `evase-analysis-1.0.8.1/tests/resources/sql_injection_vul5.py`

 * *Files identical despite different names*

### Comparing `evase-analysis-1.0.8/tests/resources/sql_injection_vul6.py` & `evase-analysis-1.0.8.1/tests/resources/sql_injection_vul6.py`

 * *Files identical despite different names*

### Comparing `evase-analysis-1.0.8/tests/resources/type_demo/app.py` & `evase-analysis-1.0.8.1/tests/resources/type_demo/app.py`

 * *Files identical despite different names*

### Comparing `evase-analysis-1.0.8/tests/resources/type_demo/user_db_handler.py` & `evase-analysis-1.0.8.1/tests/resources/type_demo/user_db_handler.py`

 * *Files identical despite different names*

### Comparing `evase-analysis-1.0.8/tests/resources/type_demo/vul.py` & `evase-analysis-1.0.8.1/tests/resources/type_demo/vul.py`

 * *Files identical despite different names*

### Comparing `evase-analysis-1.0.8/tests/resources/type_demo/vul_wrapper.py` & `evase-analysis-1.0.8.1/tests/resources/type_demo/vul_wrapper.py`

 * *Files identical despite different names*

### Comparing `evase-analysis-1.0.8/tests/resources/webgoat/flask_webgoat/__init__.py` & `evase-analysis-1.0.8.1/tests/resources/webgoat/flask_webgoat/__init__.py`

 * *Files identical despite different names*

### Comparing `evase-analysis-1.0.8/tests/resources/webgoat/flask_webgoat/actions.py` & `evase-analysis-1.0.8.1/tests/resources/webgoat/flask_webgoat/actions.py`

 * *Files identical despite different names*

### Comparing `evase-analysis-1.0.8/tests/resources/webgoat/flask_webgoat/auth.py` & `evase-analysis-1.0.8.1/tests/resources/webgoat/flask_webgoat/auth.py`

 * *Files identical despite different names*

### Comparing `evase-analysis-1.0.8/tests/resources/webgoat/flask_webgoat/ui.py` & `evase-analysis-1.0.8.1/tests/resources/webgoat/flask_webgoat/ui.py`

 * *Files identical despite different names*

### Comparing `evase-analysis-1.0.8/tests/resources/webgoat/flask_webgoat/users.py` & `evase-analysis-1.0.8.1/tests/resources/webgoat/flask_webgoat/users.py`

 * *Files identical despite different names*

### Comparing `evase-analysis-1.0.8/tests/test_analysisperformer.py` & `evase-analysis-1.0.8.1/tests/test_analysisperformer.py`

 * *Files identical despite different names*

### Comparing `evase-analysis-1.0.8/tests/test_fileutil.py` & `evase-analysis-1.0.8.1/tests/test_fileutil.py`

 * *Files identical despite different names*

### Comparing `evase-analysis-1.0.8/tests/test_projectstructure.py` & `evase-analysis-1.0.8.1/tests/test_projectstructure.py`

 * *Files identical despite different names*

### Comparing `evase-analysis-1.0.8/tests/test_scoperesolver.py` & `evase-analysis-1.0.8.1/tests/test_scoperesolver.py`

 * *Files identical despite different names*

### Comparing `evase-analysis-1.0.8/tests/testutil.py` & `evase-analysis-1.0.8.1/tests/testutil.py`

 * *Files identical despite different names*

