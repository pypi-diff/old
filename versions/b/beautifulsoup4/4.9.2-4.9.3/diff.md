# Comparing `tmp/beautifulsoup4-4.9.2.tar.gz` & `tmp/beautifulsoup4-4.9.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/beautifulsoup4-4.9.2.tar", last modified: Sat Sep 26 15:44:49 2020, max compression
+gzip compressed data, was "dist/beautifulsoup4-4.9.3.tar", last modified: Sat Oct  3 15:34:16 2020, max compression
```

## Comparing `beautifulsoup4-4.9.2.tar` & `beautifulsoup4-4.9.3.tar`

### file list

```diff
@@ -1,68 +1,68 @@
-drwxrwxr-x   0 leonardr  (1000) leonardr  (1000)        0 2020-09-26 15:44:49.451421 beautifulsoup4-4.9.2/
--rw-rw-r--   0 leonardr  (1000) leonardr  (1000)     1315 2017-01-02 14:58:02.000000 beautifulsoup4-4.9.2/COPYING.txt
--rw-r--r--   0 leonardr  (1000) leonardr  (1000)     1447 2018-12-24 15:35:20.000000 beautifulsoup4-4.9.2/LICENSE
--rw-r--r--   0 leonardr  (1000) leonardr  (1000)      219 2018-07-21 15:17:01.000000 beautifulsoup4-4.9.2/MANIFEST.in
--rw-r--r--   0 leonardr  (1000) leonardr  (1000)    59251 2020-09-26 15:42:00.000000 beautifulsoup4-4.9.2/NEWS.txt
--rw-rw-r--   0 leonardr  (1000) leonardr  (1000)     4813 2020-09-26 15:44:49.451421 beautifulsoup4-4.9.2/PKG-INFO
--rw-r--r--   0 leonardr  (1000) leonardr  (1000)     3049 2020-06-11 20:10:00.000000 beautifulsoup4-4.9.2/README.md
--rw-r--r--   0 leonardr  (1000) leonardr  (1000)     1091 2012-04-27 14:16:27.000000 beautifulsoup4-4.9.2/TODO.txt
-drwxrwxr-x   0 leonardr  (1000) leonardr  (1000)        0 2020-09-26 15:44:49.443421 beautifulsoup4-4.9.2/beautifulsoup4.egg-info/
--rw-rw-r--   0 leonardr  (1000) leonardr  (1000)     4813 2020-09-26 15:44:49.000000 beautifulsoup4-4.9.2/beautifulsoup4.egg-info/PKG-INFO
--rw-rw-r--   0 leonardr  (1000) leonardr  (1000)     1148 2020-09-26 15:44:49.000000 beautifulsoup4-4.9.2/beautifulsoup4.egg-info/SOURCES.txt
--rw-rw-r--   0 leonardr  (1000) leonardr  (1000)        1 2020-09-26 15:44:49.000000 beautifulsoup4-4.9.2/beautifulsoup4.egg-info/dependency_links.txt
--rw-rw-r--   0 leonardr  (1000) leonardr  (1000)      122 2020-09-26 15:44:49.000000 beautifulsoup4-4.9.2/beautifulsoup4.egg-info/requires.txt
--rw-rw-r--   0 leonardr  (1000) leonardr  (1000)        4 2020-09-26 15:44:49.000000 beautifulsoup4-4.9.2/beautifulsoup4.egg-info/top_level.txt
-drwxrwxr-x   0 leonardr  (1000) leonardr  (1000)        0 2020-09-26 15:44:49.443421 beautifulsoup4-4.9.2/bs4/
--rw-r--r--   0 leonardr  (1000) leonardr  (1000)    32134 2020-09-26 15:42:31.000000 beautifulsoup4-4.9.2/bs4/__init__.py
-drwxrwxr-x   0 leonardr  (1000) leonardr  (1000)        0 2020-09-26 15:44:49.443421 beautifulsoup4-4.9.2/bs4/builder/
--rw-r--r--   0 leonardr  (1000) leonardr  (1000)    19782 2020-05-30 18:17:21.000000 beautifulsoup4-4.9.2/bs4/builder/__init__.py
--rw-r--r--   0 leonardr  (1000) leonardr  (1000)    18771 2020-09-26 14:36:10.000000 beautifulsoup4-4.9.2/bs4/builder/_html5lib.py
--rw-r--r--   0 leonardr  (1000) leonardr  (1000)    18403 2020-09-26 14:36:05.000000 beautifulsoup4-4.9.2/bs4/builder/_htmlparser.py
--rw-rw-r--   0 leonardr  (1000) leonardr  (1000)    12225 2020-09-07 11:13:41.000000 beautifulsoup4-4.9.2/bs4/builder/_lxml.py
--rw-r--r--   0 leonardr  (1000) leonardr  (1000)    34168 2020-05-17 17:56:04.000000 beautifulsoup4-4.9.2/bs4/dammit.py
--rw-rw-r--   0 leonardr  (1000) leonardr  (1000)     7714 2020-05-17 17:55:43.000000 beautifulsoup4-4.9.2/bs4/diagnose.py
--rw-r--r--   0 leonardr  (1000) leonardr  (1000)    81444 2020-09-26 15:15:17.000000 beautifulsoup4-4.9.2/bs4/element.py
--rw-rw-r--   0 leonardr  (1000) leonardr  (1000)     5653 2019-12-29 15:48:17.000000 beautifulsoup4-4.9.2/bs4/formatter.py
--rw-r--r--   0 leonardr  (1000) leonardr  (1000)    45972 2020-05-30 18:54:41.000000 beautifulsoup4-4.9.2/bs4/testing.py
-drwxrwxr-x   0 leonardr  (1000) leonardr  (1000)        0 2020-09-26 15:44:49.443421 beautifulsoup4-4.9.2/bs4/tests/
--rw-r--r--   0 leonardr  (1000) leonardr  (1000)       27 2020-04-05 19:54:12.000000 beautifulsoup4-4.9.2/bs4/tests/__init__.py
--rw-r--r--   0 leonardr  (1000) leonardr  (1000)     5582 2020-04-05 19:54:12.000000 beautifulsoup4-4.9.2/bs4/tests/test_builder_registry.py
--rw-r--r--   0 leonardr  (1000) leonardr  (1000)     1067 2020-04-05 19:54:12.000000 beautifulsoup4-4.9.2/bs4/tests/test_docs.py
--rw-r--r--   0 leonardr  (1000) leonardr  (1000)     6755 2020-04-05 19:54:12.000000 beautifulsoup4-4.9.2/bs4/tests/test_html5lib.py
--rw-r--r--   0 leonardr  (1000) leonardr  (1000)     3947 2020-05-17 16:18:11.000000 beautifulsoup4-4.9.2/bs4/tests/test_htmlparser.py
--rw-r--r--   0 leonardr  (1000) leonardr  (1000)     4108 2020-04-05 19:54:12.000000 beautifulsoup4-4.9.2/bs4/tests/test_lxml.py
--rw-r--r--   0 leonardr  (1000) leonardr  (1000)    29350 2020-04-21 12:12:33.000000 beautifulsoup4-4.9.2/bs4/tests/test_soup.py
--rw-r--r--   0 leonardr  (1000) leonardr  (1000)    89530 2020-09-26 15:15:48.000000 beautifulsoup4-4.9.2/bs4/tests/test_tree.py
--rwxr-xr-x   0 leonardr  (1000) leonardr  (1000)      546 2013-08-12 15:47:12.000000 beautifulsoup4-4.9.2/convert-py3k
-drwxrwxr-x   0 leonardr  (1000) leonardr  (1000)        0 2020-09-26 15:44:49.447421 beautifulsoup4-4.9.2/doc/
--rw-r--r--   0 leonardr  (1000) leonardr  (1000)     4622 2012-01-26 16:22:55.000000 beautifulsoup4-4.9.2/doc/Makefile
-drwxrwxr-x   0 leonardr  (1000) leonardr  (1000)        0 2020-09-26 15:44:49.447421 beautifulsoup4-4.9.2/doc/source/
--rw-r--r--   0 leonardr  (1000) leonardr  (1000)    22619 2005-04-08 01:32:45.000000 beautifulsoup4-4.9.2/doc/source/6.1.jpg
--rw-rw-r--   0 leonardr  (1000) leonardr  (1000)      697 2020-07-30 01:51:50.000000 beautifulsoup4-4.9.2/doc/source/check_doc.py
--rw-r--r--   0 leonardr  (1000) leonardr  (1000)     8225 2020-04-04 22:21:49.000000 beautifulsoup4-4.9.2/doc/source/conf.py
--rw-r--r--   0 leonardr  (1000) leonardr  (1000)   119306 2020-09-26 15:16:37.000000 beautifulsoup4-4.9.2/doc/source/index.rst
-drwxrwxr-x   0 leonardr  (1000) leonardr  (1000)        0 2020-09-26 15:44:49.447421 beautifulsoup4-4.9.2/doc.ptbr/
--rw-r--r--   0 leonardr  (1000) leonardr  (1000)     4622 2019-11-11 16:34:58.000000 beautifulsoup4-4.9.2/doc.ptbr/Makefile
-drwxrwxr-x   0 leonardr  (1000) leonardr  (1000)        0 2020-09-26 15:44:49.447421 beautifulsoup4-4.9.2/doc.ptbr/source/
--rw-r--r--   0 leonardr  (1000) leonardr  (1000)    22619 2019-11-11 16:33:42.000000 beautifulsoup4-4.9.2/doc.ptbr/source/6.1.jpg
--rw-r--r--   0 leonardr  (1000) leonardr  (1000)     8205 2019-11-11 16:35:06.000000 beautifulsoup4-4.9.2/doc.ptbr/source/conf.py
--rw-rw-r--   0 leonardr  (1000) leonardr  (1000)   117253 2020-04-04 22:13:52.000000 beautifulsoup4-4.9.2/doc.ptbr/source/index.rst
-drwxrwxr-x   0 leonardr  (1000) leonardr  (1000)        0 2020-09-26 15:44:49.447421 beautifulsoup4-4.9.2/doc.ru/
--rw-r--r--   0 leonardr  (1000) leonardr  (1000)     4622 2020-04-04 22:03:25.000000 beautifulsoup4-4.9.2/doc.ru/Makefile
-drwxrwxr-x   0 leonardr  (1000) leonardr  (1000)        0 2020-09-26 15:44:49.447421 beautifulsoup4-4.9.2/doc.ru/source/
--rw-r--r--   0 leonardr  (1000) leonardr  (1000)    22619 2020-04-04 22:05:47.000000 beautifulsoup4-4.9.2/doc.ru/source/6.1.jpg
--rw-r--r--   0 leonardr  (1000) leonardr  (1000)   158626 2020-02-18 12:25:53.000000 beautifulsoup4-4.9.2/doc.ru/source/bs4ru.rst
--rw-r--r--   0 leonardr  (1000) leonardr  (1000)     8206 2020-04-04 22:04:45.000000 beautifulsoup4-4.9.2/doc.ru/source/conf.py
--rw-r--r--   0 leonardr  (1000) leonardr  (1000)      478 2020-04-04 22:19:32.000000 beautifulsoup4-4.9.2/doc.ru/source/index.rst
-drwxrwxr-x   0 leonardr  (1000) leonardr  (1000)        0 2020-09-26 15:44:49.447421 beautifulsoup4-4.9.2/doc.zh/
--rw-r--r--   0 leonardr  (1000) leonardr  (1000)     4622 2015-06-25 10:24:24.000000 beautifulsoup4-4.9.2/doc.zh/Makefile
-drwxrwxr-x   0 leonardr  (1000) leonardr  (1000)        0 2020-09-26 15:44:49.447421 beautifulsoup4-4.9.2/doc.zh/source/
--rw-r--r--   0 leonardr  (1000) leonardr  (1000)    22619 2019-11-11 16:33:46.000000 beautifulsoup4-4.9.2/doc.zh/source/6.1.jpg
--rw-r--r--   0 leonardr  (1000) leonardr  (1000)     8200 2015-06-25 10:25:24.000000 beautifulsoup4-4.9.2/doc.zh/source/conf.py
--rw-rw-r--   0 leonardr  (1000) leonardr  (1000)    96762 2020-04-04 22:14:17.000000 beautifulsoup4-4.9.2/doc.zh/source/index.rst
-drwxrwxr-x   0 leonardr  (1000) leonardr  (1000)        0 2020-09-26 15:44:49.451421 beautifulsoup4-4.9.2/scripts/
--rw-r--r--   0 leonardr  (1000) leonardr  (1000)     2976 2012-02-23 13:09:10.000000 beautifulsoup4-4.9.2/scripts/demonstrate_parser_differences.py
--rw-r--r--   0 leonardr  (1000) leonardr  (1000)     2612 2012-02-23 13:09:10.000000 beautifulsoup4-4.9.2/scripts/demonstration_markup.txt
--rw-rw-r--   0 leonardr  (1000) leonardr  (1000)       38 2020-09-26 15:44:49.451421 beautifulsoup4-4.9.2/setup.cfg
--rw-rw-r--   0 leonardr  (1000) leonardr  (1000)     1713 2020-09-26 15:43:21.000000 beautifulsoup4-4.9.2/setup.py
--rwxr--r--   0 leonardr  (1000) leonardr  (1000)       56 2012-03-30 12:30:56.000000 beautifulsoup4-4.9.2/test-all-versions
+drwxrwxr-x   0 leonardr  (1000) leonardr  (1000)        0 2020-10-03 15:34:16.005351 beautifulsoup4-4.9.3/
+-rw-rw-r--   0 leonardr  (1000) leonardr  (1000)     1315 2017-01-02 14:58:02.000000 beautifulsoup4-4.9.3/COPYING.txt
+-rw-r--r--   0 leonardr  (1000) leonardr  (1000)     1447 2018-12-24 15:35:20.000000 beautifulsoup4-4.9.3/LICENSE
+-rw-r--r--   0 leonardr  (1000) leonardr  (1000)      219 2018-07-21 15:17:01.000000 beautifulsoup4-4.9.3/MANIFEST.in
+-rw-r--r--   0 leonardr  (1000) leonardr  (1000)    59403 2020-10-03 15:30:36.000000 beautifulsoup4-4.9.3/NEWS.txt
+-rw-rw-r--   0 leonardr  (1000) leonardr  (1000)     4813 2020-10-03 15:34:16.005351 beautifulsoup4-4.9.3/PKG-INFO
+-rw-r--r--   0 leonardr  (1000) leonardr  (1000)     3049 2020-06-11 20:10:00.000000 beautifulsoup4-4.9.3/README.md
+-rw-r--r--   0 leonardr  (1000) leonardr  (1000)     1091 2012-04-27 14:16:27.000000 beautifulsoup4-4.9.3/TODO.txt
+drwxrwxr-x   0 leonardr  (1000) leonardr  (1000)        0 2020-10-03 15:34:16.001351 beautifulsoup4-4.9.3/beautifulsoup4.egg-info/
+-rw-rw-r--   0 leonardr  (1000) leonardr  (1000)     4813 2020-10-03 15:34:15.000000 beautifulsoup4-4.9.3/beautifulsoup4.egg-info/PKG-INFO
+-rw-rw-r--   0 leonardr  (1000) leonardr  (1000)     1148 2020-10-03 15:34:15.000000 beautifulsoup4-4.9.3/beautifulsoup4.egg-info/SOURCES.txt
+-rw-rw-r--   0 leonardr  (1000) leonardr  (1000)        1 2020-10-03 15:34:15.000000 beautifulsoup4-4.9.3/beautifulsoup4.egg-info/dependency_links.txt
+-rw-rw-r--   0 leonardr  (1000) leonardr  (1000)      122 2020-10-03 15:34:15.000000 beautifulsoup4-4.9.3/beautifulsoup4.egg-info/requires.txt
+-rw-rw-r--   0 leonardr  (1000) leonardr  (1000)        4 2020-10-03 15:34:15.000000 beautifulsoup4-4.9.3/beautifulsoup4.egg-info/top_level.txt
+drwxrwxr-x   0 leonardr  (1000) leonardr  (1000)        0 2020-10-03 15:34:16.001351 beautifulsoup4-4.9.3/bs4/
+-rw-r--r--   0 leonardr  (1000) leonardr  (1000)    32134 2020-10-03 15:30:53.000000 beautifulsoup4-4.9.3/bs4/__init__.py
+drwxrwxr-x   0 leonardr  (1000) leonardr  (1000)        0 2020-10-03 15:34:16.001351 beautifulsoup4-4.9.3/bs4/builder/
+-rw-r--r--   0 leonardr  (1000) leonardr  (1000)    19782 2020-05-30 18:17:21.000000 beautifulsoup4-4.9.3/bs4/builder/__init__.py
+-rw-r--r--   0 leonardr  (1000) leonardr  (1000)    18771 2020-09-26 14:36:10.000000 beautifulsoup4-4.9.3/bs4/builder/_html5lib.py
+-rw-r--r--   0 leonardr  (1000) leonardr  (1000)    18403 2020-09-26 14:36:05.000000 beautifulsoup4-4.9.3/bs4/builder/_htmlparser.py
+-rw-rw-r--   0 leonardr  (1000) leonardr  (1000)    12225 2020-09-07 11:13:41.000000 beautifulsoup4-4.9.3/bs4/builder/_lxml.py
+-rw-r--r--   0 leonardr  (1000) leonardr  (1000)    34168 2020-05-17 17:56:04.000000 beautifulsoup4-4.9.3/bs4/dammit.py
+-rw-rw-r--   0 leonardr  (1000) leonardr  (1000)     7714 2020-05-17 17:55:43.000000 beautifulsoup4-4.9.3/bs4/diagnose.py
+-rw-r--r--   0 leonardr  (1000) leonardr  (1000)    81798 2020-10-02 22:19:12.000000 beautifulsoup4-4.9.3/bs4/element.py
+-rw-rw-r--   0 leonardr  (1000) leonardr  (1000)     5653 2019-12-29 15:48:17.000000 beautifulsoup4-4.9.3/bs4/formatter.py
+-rw-r--r--   0 leonardr  (1000) leonardr  (1000)    45972 2020-05-30 18:54:41.000000 beautifulsoup4-4.9.3/bs4/testing.py
+drwxrwxr-x   0 leonardr  (1000) leonardr  (1000)        0 2020-10-03 15:34:16.001351 beautifulsoup4-4.9.3/bs4/tests/
+-rw-r--r--   0 leonardr  (1000) leonardr  (1000)       27 2020-04-05 19:54:12.000000 beautifulsoup4-4.9.3/bs4/tests/__init__.py
+-rw-r--r--   0 leonardr  (1000) leonardr  (1000)     5582 2020-04-05 19:54:12.000000 beautifulsoup4-4.9.3/bs4/tests/test_builder_registry.py
+-rw-r--r--   0 leonardr  (1000) leonardr  (1000)     1067 2020-04-05 19:54:12.000000 beautifulsoup4-4.9.3/bs4/tests/test_docs.py
+-rw-r--r--   0 leonardr  (1000) leonardr  (1000)     6755 2020-04-05 19:54:12.000000 beautifulsoup4-4.9.3/bs4/tests/test_html5lib.py
+-rw-r--r--   0 leonardr  (1000) leonardr  (1000)     3947 2020-05-17 16:18:11.000000 beautifulsoup4-4.9.3/bs4/tests/test_htmlparser.py
+-rw-r--r--   0 leonardr  (1000) leonardr  (1000)     4108 2020-04-05 19:54:12.000000 beautifulsoup4-4.9.3/bs4/tests/test_lxml.py
+-rw-r--r--   0 leonardr  (1000) leonardr  (1000)    29350 2020-04-21 12:12:33.000000 beautifulsoup4-4.9.3/bs4/tests/test_soup.py
+-rw-r--r--   0 leonardr  (1000) leonardr  (1000)    89530 2020-09-26 15:15:48.000000 beautifulsoup4-4.9.3/bs4/tests/test_tree.py
+-rwxr-xr-x   0 leonardr  (1000) leonardr  (1000)      546 2013-08-12 15:47:12.000000 beautifulsoup4-4.9.3/convert-py3k
+drwxrwxr-x   0 leonardr  (1000) leonardr  (1000)        0 2020-10-03 15:34:16.001351 beautifulsoup4-4.9.3/doc/
+-rw-r--r--   0 leonardr  (1000) leonardr  (1000)     4622 2012-01-26 16:22:55.000000 beautifulsoup4-4.9.3/doc/Makefile
+drwxrwxr-x   0 leonardr  (1000) leonardr  (1000)        0 2020-10-03 15:34:16.005351 beautifulsoup4-4.9.3/doc/source/
+-rw-r--r--   0 leonardr  (1000) leonardr  (1000)    22619 2005-04-08 01:32:45.000000 beautifulsoup4-4.9.3/doc/source/6.1.jpg
+-rw-rw-r--   0 leonardr  (1000) leonardr  (1000)      697 2020-07-30 01:51:50.000000 beautifulsoup4-4.9.3/doc/source/check_doc.py
+-rw-r--r--   0 leonardr  (1000) leonardr  (1000)     8225 2020-04-04 22:21:49.000000 beautifulsoup4-4.9.3/doc/source/conf.py
+-rw-r--r--   0 leonardr  (1000) leonardr  (1000)   119306 2020-09-26 15:54:51.000000 beautifulsoup4-4.9.3/doc/source/index.rst
+drwxrwxr-x   0 leonardr  (1000) leonardr  (1000)        0 2020-10-03 15:34:16.005351 beautifulsoup4-4.9.3/doc.ptbr/
+-rw-r--r--   0 leonardr  (1000) leonardr  (1000)     4622 2019-11-11 16:34:58.000000 beautifulsoup4-4.9.3/doc.ptbr/Makefile
+drwxrwxr-x   0 leonardr  (1000) leonardr  (1000)        0 2020-10-03 15:34:16.005351 beautifulsoup4-4.9.3/doc.ptbr/source/
+-rw-r--r--   0 leonardr  (1000) leonardr  (1000)    22619 2019-11-11 16:33:42.000000 beautifulsoup4-4.9.3/doc.ptbr/source/6.1.jpg
+-rw-r--r--   0 leonardr  (1000) leonardr  (1000)     8205 2019-11-11 16:35:06.000000 beautifulsoup4-4.9.3/doc.ptbr/source/conf.py
+-rw-rw-r--   0 leonardr  (1000) leonardr  (1000)   117253 2020-04-04 22:13:52.000000 beautifulsoup4-4.9.3/doc.ptbr/source/index.rst
+drwxrwxr-x   0 leonardr  (1000) leonardr  (1000)        0 2020-10-03 15:34:16.005351 beautifulsoup4-4.9.3/doc.ru/
+-rw-r--r--   0 leonardr  (1000) leonardr  (1000)     4622 2020-04-04 22:03:25.000000 beautifulsoup4-4.9.3/doc.ru/Makefile
+drwxrwxr-x   0 leonardr  (1000) leonardr  (1000)        0 2020-10-03 15:34:16.005351 beautifulsoup4-4.9.3/doc.ru/source/
+-rw-r--r--   0 leonardr  (1000) leonardr  (1000)    22619 2020-04-04 22:05:47.000000 beautifulsoup4-4.9.3/doc.ru/source/6.1.jpg
+-rw-r--r--   0 leonardr  (1000) leonardr  (1000)   158626 2020-02-18 12:25:53.000000 beautifulsoup4-4.9.3/doc.ru/source/bs4ru.rst
+-rw-r--r--   0 leonardr  (1000) leonardr  (1000)     8206 2020-04-04 22:04:45.000000 beautifulsoup4-4.9.3/doc.ru/source/conf.py
+-rw-r--r--   0 leonardr  (1000) leonardr  (1000)      478 2020-04-04 22:19:32.000000 beautifulsoup4-4.9.3/doc.ru/source/index.rst
+drwxrwxr-x   0 leonardr  (1000) leonardr  (1000)        0 2020-10-03 15:34:16.005351 beautifulsoup4-4.9.3/doc.zh/
+-rw-r--r--   0 leonardr  (1000) leonardr  (1000)     4622 2015-06-25 10:24:24.000000 beautifulsoup4-4.9.3/doc.zh/Makefile
+drwxrwxr-x   0 leonardr  (1000) leonardr  (1000)        0 2020-10-03 15:34:16.005351 beautifulsoup4-4.9.3/doc.zh/source/
+-rw-r--r--   0 leonardr  (1000) leonardr  (1000)    22619 2019-11-11 16:33:46.000000 beautifulsoup4-4.9.3/doc.zh/source/6.1.jpg
+-rw-r--r--   0 leonardr  (1000) leonardr  (1000)     8200 2015-06-25 10:25:24.000000 beautifulsoup4-4.9.3/doc.zh/source/conf.py
+-rw-rw-r--   0 leonardr  (1000) leonardr  (1000)    96762 2020-04-04 22:14:17.000000 beautifulsoup4-4.9.3/doc.zh/source/index.rst
+drwxrwxr-x   0 leonardr  (1000) leonardr  (1000)        0 2020-10-03 15:34:16.005351 beautifulsoup4-4.9.3/scripts/
+-rw-r--r--   0 leonardr  (1000) leonardr  (1000)     2976 2012-02-23 13:09:10.000000 beautifulsoup4-4.9.3/scripts/demonstrate_parser_differences.py
+-rw-r--r--   0 leonardr  (1000) leonardr  (1000)     2612 2012-02-23 13:09:10.000000 beautifulsoup4-4.9.3/scripts/demonstration_markup.txt
+-rw-rw-r--   0 leonardr  (1000) leonardr  (1000)       38 2020-10-03 15:34:16.009351 beautifulsoup4-4.9.3/setup.cfg
+-rw-rw-r--   0 leonardr  (1000) leonardr  (1000)     1713 2020-10-03 15:31:00.000000 beautifulsoup4-4.9.3/setup.py
+-rwxr--r--   0 leonardr  (1000) leonardr  (1000)       56 2012-03-30 12:30:56.000000 beautifulsoup4-4.9.3/test-all-versions
```

### Comparing `beautifulsoup4-4.9.2/COPYING.txt` & `beautifulsoup4-4.9.3/COPYING.txt`

 * *Files identical despite different names*

### Comparing `beautifulsoup4-4.9.2/LICENSE` & `beautifulsoup4-4.9.3/LICENSE`

 * *Files identical despite different names*

### Comparing `beautifulsoup4-4.9.2/NEWS.txt` & `beautifulsoup4-4.9.3/NEWS.txt`

 * *Files 0% similar despite different names*

```diff
@@ -1,7 +1,12 @@
+= 4.9.3 (20201003)
+
+* Implemented a significant performance optimization to the process of
+  searching the parse tree. Patch by Morotti. [bug=1898212]
+
 = 4.9.2 (20200926)
 
 * Fixed a bug that caused too many tags to be popped from the tag
   stack during tree building, when encountering a closing tag that had
   no matching opening tag. [bug=1880420]
 
 * Fixed a bug that inconsistently moved elements over when passing
```

#### html2text {}

 * *error from `html2text {}`:*

 * *File "/tmp/diffoscope_tyw1znwm_492493/tmp5ct_83xo_TarContainer/0/4.txt", line 1543, column 0: CDATA terminal not found*

 * *File "/tmp/diffoscope_tyw1znwm_492493/tmp5ct_83xo_TarContainer/0/4.txt", line 1543, column 0: CDATA terminal not found*

```diff
@@ -1,9 +1,11 @@
-= 4.9.2 (20200926) * Fixed a bug that caused too many tags to be popped from
-the tag stack during tree building, when encountering a closing tag that had no
+= 4.9.3 (20201003) * Implemented a significant performance optimization to the
+process of searching the parse tree. Patch by Morotti. [bug=1898212] = 4.9.2
+(20200926) * Fixed a bug that caused too many tags to be popped from the tag
+stack during tree building, when encountering a closing tag that had no
 matching opening tag. [bug=1880420] * Fixed a bug that inconsistently moved
 elements over when passing a Tag, rather than a list, into Tag.extend().
 [bug=1885710] * Specify the soupsieve dependency in a way that complies with
 PEP 508. Patch by Mike Nerone. [bug=1893696] * Change the signatures for
 BeautifulSoup.insert_before and insert_after (which are not implemented) to
 match PageElement.insert_before and insert_after, quieting warnings in some
 IDEs. [bug=1897120] = 4.9.1 (20200517) * Added a keyword argument
```

### Comparing `beautifulsoup4-4.9.2/PKG-INFO` & `beautifulsoup4-4.9.3/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: beautifulsoup4
-Version: 4.9.2
+Version: 4.9.3
 Summary: Screen-scraping library
 Home-page: http://www.crummy.com/software/BeautifulSoup/bs4/
 Author: Leonard Richardson
 Author-email: leonardr@segfault.org
 License: MIT
 Download-URL: http://www.crummy.com/software/BeautifulSoup/bs4/download/
 Description: Beautiful Soup is a library that makes it easy to scrape information
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: beautifulsoup4 Version: 4.9.2 Summary: Screen-
+Metadata-Version: 2.1 Name: beautifulsoup4 Version: 4.9.3 Summary: Screen-
 scraping library Home-page: http://www.crummy.com/software/BeautifulSoup/bs4/
 Author: Leonard Richardson Author-email: leonardr@segfault.org License: MIT
 Download-URL: http://www.crummy.com/software/BeautifulSoup/bs4/download/
 Description: Beautiful Soup is a library that makes it easy to scrape
 information from web pages. It sits atop an HTML or XML parser, providing
 Pythonic idioms for iterating, searching, and modifying the parse tree. # Quick
 start ``` >>> from bs4 import BeautifulSoup >>> soup = BeautifulSoup("
```

### Comparing `beautifulsoup4-4.9.2/README.md` & `beautifulsoup4-4.9.3/README.md`

 * *Files identical despite different names*

### Comparing `beautifulsoup4-4.9.2/TODO.txt` & `beautifulsoup4-4.9.3/TODO.txt`

 * *Files identical despite different names*

### Comparing `beautifulsoup4-4.9.2/beautifulsoup4.egg-info/PKG-INFO` & `beautifulsoup4-4.9.3/beautifulsoup4.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: beautifulsoup4
-Version: 4.9.2
+Version: 4.9.3
 Summary: Screen-scraping library
 Home-page: http://www.crummy.com/software/BeautifulSoup/bs4/
 Author: Leonard Richardson
 Author-email: leonardr@segfault.org
 License: MIT
 Download-URL: http://www.crummy.com/software/BeautifulSoup/bs4/download/
 Description: Beautiful Soup is a library that makes it easy to scrape information
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: beautifulsoup4 Version: 4.9.2 Summary: Screen-
+Metadata-Version: 2.1 Name: beautifulsoup4 Version: 4.9.3 Summary: Screen-
 scraping library Home-page: http://www.crummy.com/software/BeautifulSoup/bs4/
 Author: Leonard Richardson Author-email: leonardr@segfault.org License: MIT
 Download-URL: http://www.crummy.com/software/BeautifulSoup/bs4/download/
 Description: Beautiful Soup is a library that makes it easy to scrape
 information from web pages. It sits atop an HTML or XML parser, providing
 Pythonic idioms for iterating, searching, and modifying the parse tree. # Quick
 start ``` >>> from bs4 import BeautifulSoup >>> soup = BeautifulSoup("
```

### Comparing `beautifulsoup4-4.9.2/beautifulsoup4.egg-info/SOURCES.txt` & `beautifulsoup4-4.9.3/beautifulsoup4.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `beautifulsoup4-4.9.2/bs4/__init__.py` & `beautifulsoup4-4.9.3/bs4/__init__.py`

 * *Files 0% similar despite different names*

```diff
@@ -11,15 +11,15 @@
 and/or html5lib is installed.
 
 For more than you ever wanted to know about Beautiful Soup, see the
 documentation: http://www.crummy.com/software/BeautifulSoup/bs4/doc/
 """
 
 __author__ = "Leonard Richardson (leonardr@segfault.org)"
-__version__ = "4.9.2"
+__version__ = "4.9.3"
 __copyright__ = "Copyright (c) 2004-2020 Leonard Richardson"
 # Use of this source code is governed by the MIT license.
 __license__ = "MIT"
 
 __all__ = ['BeautifulSoup']
 
 from collections import Counter
```

### Comparing `beautifulsoup4-4.9.2/bs4/builder/__init__.py` & `beautifulsoup4-4.9.3/bs4/builder/__init__.py`

 * *Files identical despite different names*

### Comparing `beautifulsoup4-4.9.2/bs4/builder/_html5lib.py` & `beautifulsoup4-4.9.3/bs4/builder/_html5lib.py`

 * *Files identical despite different names*

### Comparing `beautifulsoup4-4.9.2/bs4/builder/_htmlparser.py` & `beautifulsoup4-4.9.3/bs4/builder/_htmlparser.py`

 * *Files identical despite different names*

### Comparing `beautifulsoup4-4.9.2/bs4/builder/_lxml.py` & `beautifulsoup4-4.9.3/bs4/builder/_lxml.py`

 * *Files identical despite different names*

### Comparing `beautifulsoup4-4.9.2/bs4/dammit.py` & `beautifulsoup4-4.9.3/bs4/dammit.py`

 * *Files identical despite different names*

### Comparing `beautifulsoup4-4.9.2/bs4/diagnose.py` & `beautifulsoup4-4.9.3/bs4/diagnose.py`

 * *Files identical despite different names*

### Comparing `beautifulsoup4-4.9.2/bs4/element.py` & `beautifulsoup4-4.9.3/bs4/element.py`

 * *Files 0% similar despite different names*

```diff
@@ -1991,14 +1991,22 @@
             False otherwise.
         """
         found = None
         markup = None
         if isinstance(markup_name, Tag):
             markup = markup_name
             markup_attrs = markup
+
+        if isinstance(self.name, basestring):
+            # Optimization for a very common case where the user is
+            # searching for a tag with one specific name, and we're
+            # looking at a tag with a different name.
+            if markup and not markup.prefix and self.name != markup.name:
+                 return False
+            
         call_function_with_tag_data = (
             isinstance(self.name, Callable)
             and not isinstance(markup_name, Tag))
 
         if ((not self.name)
             or call_function_with_tag_data
             or (markup and self._matches(markup, self.name))
```

### Comparing `beautifulsoup4-4.9.2/bs4/formatter.py` & `beautifulsoup4-4.9.3/bs4/formatter.py`

 * *Files identical despite different names*

### Comparing `beautifulsoup4-4.9.2/bs4/testing.py` & `beautifulsoup4-4.9.3/bs4/testing.py`

 * *Files identical despite different names*

### Comparing `beautifulsoup4-4.9.2/bs4/tests/test_builder_registry.py` & `beautifulsoup4-4.9.3/bs4/tests/test_builder_registry.py`

 * *Files identical despite different names*

### Comparing `beautifulsoup4-4.9.2/bs4/tests/test_docs.py` & `beautifulsoup4-4.9.3/bs4/tests/test_docs.py`

 * *Files identical despite different names*

### Comparing `beautifulsoup4-4.9.2/bs4/tests/test_html5lib.py` & `beautifulsoup4-4.9.3/bs4/tests/test_html5lib.py`

 * *Files identical despite different names*

### Comparing `beautifulsoup4-4.9.2/bs4/tests/test_htmlparser.py` & `beautifulsoup4-4.9.3/bs4/tests/test_htmlparser.py`

 * *Files identical despite different names*

### Comparing `beautifulsoup4-4.9.2/bs4/tests/test_lxml.py` & `beautifulsoup4-4.9.3/bs4/tests/test_lxml.py`

 * *Files identical despite different names*

### Comparing `beautifulsoup4-4.9.2/bs4/tests/test_soup.py` & `beautifulsoup4-4.9.3/bs4/tests/test_soup.py`

 * *Files identical despite different names*

### Comparing `beautifulsoup4-4.9.2/bs4/tests/test_tree.py` & `beautifulsoup4-4.9.3/bs4/tests/test_tree.py`

 * *Files identical despite different names*

### Comparing `beautifulsoup4-4.9.2/convert-py3k` & `beautifulsoup4-4.9.3/convert-py3k`

 * *Files identical despite different names*

### Comparing `beautifulsoup4-4.9.2/doc/Makefile` & `beautifulsoup4-4.9.3/doc/Makefile`

 * *Files identical despite different names*

### Comparing `beautifulsoup4-4.9.2/doc/source/6.1.jpg` & `beautifulsoup4-4.9.3/doc/source/6.1.jpg`

 * *Files identical despite different names*

### Comparing `beautifulsoup4-4.9.2/doc/source/check_doc.py` & `beautifulsoup4-4.9.3/doc/source/check_doc.py`

 * *Files identical despite different names*

### Comparing `beautifulsoup4-4.9.2/doc/source/conf.py` & `beautifulsoup4-4.9.3/doc/source/conf.py`

 * *Files identical despite different names*

### Comparing `beautifulsoup4-4.9.2/doc/source/index.rst` & `beautifulsoup4-4.9.3/doc/source/index.rst`

 * *Files 0% similar despite different names*

```diff
@@ -14,17 +14,17 @@
 hours or days of work.
 
 These instructions illustrate all major features of Beautiful Soup 4,
 with examples. I show you what the library is good for, how it works,
 how to use it, how to make it do what you want, and what to do when it
 violates your expectations.
 
-This document covers Beautiful Soup version 4.9.1. The examples in
+This document covers Beautiful Soup version 4.9.2. The examples in
 this documentation should work the same way in Python 2.7 and Python
-3.2.
+3.8.
 
 You might be looking for the documentation for `Beautiful Soup 3
 <http://www.crummy.com/software/BeautifulSoup/bs3/documentation.html>`_.
 If so, you should know that Beautiful Soup 3 is no longer being
 developed and that support for it will be dropped on or after December
 31, 2020. If you want to learn about the differences between Beautiful
 Soup 3 and Beautiful Soup 4, see `Porting code to BS4`_.
@@ -198,15 +198,15 @@
 :kbd:`$ python setup.py install`
 
 If all else fails, the license for Beautiful Soup allows you to
 package the entire library with your application. You can download the
 tarball, copy its ``bs4`` directory into your application's codebase,
 and use Beautiful Soup without installing it at all.
 
-I use Python 2.7 and Python 3.2 to develop Beautiful Soup, but it
+I use Python 2.7 and Python 3.8 to develop Beautiful Soup, but it
 should work with other recent versions.
 
 Problems after installation
 ---------------------------
 
 Beautiful Soup is packaged as Python 2 code. When you install it for
 use with Python 3, it's automatically converted to Python 3 code. If
```

#### html2text {}

 * *error from `html2text {}`:*

 * *File "/tmp/diffoscope_tyw1znwm_492493/tmp5ct_83xo_TarContainer/0/42.rst", line 3506, column 0: CDATA terminal not found*

 * *File "/tmp/diffoscope_tyw1znwm_492493/tmp5ct_83xo_TarContainer/0/42.rst", line 3506, column 0: CDATA terminal not found*

```diff
@@ -4,16 +4,16 @@
 www.crummy.com/software/BeautifulSoup/>`_ is a Python library for pulling data
 out of HTML and XML files. It works with your favorite parser to provide
 idiomatic ways of navigating, searching, and modifying the parse tree. It
 commonly saves programmers hours or days of work. These instructions illustrate
 all major features of Beautiful Soup 4, with examples. I show you what the
 library is good for, how it works, how to use it, how to make it do what you
 want, and what to do when it violates your expectations. This document covers
-Beautiful Soup version 4.9.1. The examples in this documentation should work
-the same way in Python 2.7 and Python 3.2. You might be looking for the
+Beautiful Soup version 4.9.2. The examples in this documentation should work
+the same way in Python 2.7 and Python 3.8. You might be looking for the
 documentation for `Beautiful Soup 3
 www.crummy.com/software/BeautifulSoup/bs3/documentation.html>`_. If so, you
 should know that Beautiful Soup 3 is no longer being developed and that support
 for it will be dropped on or after December 31, 2020. If you want to learn
 about the differences between Beautiful Soup 3 and Beautiful Soup 4, see
 `Porting code to BS4`_. This documentation has been translated into other
 languages by Beautiful Soup users: * `è¿ç¯ææ¡£å½ç¶è¿æä¸­æç.
@@ -82,15 +82,15 @@
 writing new code you should install ``beautifulsoup4``.) If you don't have
 ``easy_install`` or ``pip`` installed, you can `download the Beautiful Soup 4
 source tarball www.crummy.com/software/BeautifulSoup/download/4.x/>`_ and
 install it with ``setup.py``. :kbd:`$ python setup.py install` If all else
 fails, the license for Beautiful Soup allows you to package the entire library
 with your application. You can download the tarball, copy its ``bs4`` directory
 into your application's codebase, and use Beautiful Soup without installing it
-at all. I use Python 2.7 and Python 3.2 to develop Beautiful Soup, but it
+at all. I use Python 2.7 and Python 3.8 to develop Beautiful Soup, but it
 should work with other recent versions. Problems after installation -----------
 ---------------- Beautiful Soup is packaged as Python 2 code. When you install
 it for use with Python 3, it's automatically converted to Python 3 code. If you
 don't install the package, the code won't be converted. There have also been
 reports on Windows machines of the wrong version being installed. If you get
 the ``ImportError`` "No module named HTMLParser", your problem is that you're
 running the Python 2 version of the code under Python 3. If you get the
```

### Comparing `beautifulsoup4-4.9.2/doc.ptbr/Makefile` & `beautifulsoup4-4.9.3/doc.ptbr/Makefile`

 * *Files identical despite different names*

### Comparing `beautifulsoup4-4.9.2/doc.ptbr/source/6.1.jpg` & `beautifulsoup4-4.9.3/doc.ptbr/source/6.1.jpg`

 * *Files identical despite different names*

### Comparing `beautifulsoup4-4.9.2/doc.ptbr/source/conf.py` & `beautifulsoup4-4.9.3/doc.ptbr/source/conf.py`

 * *Files identical despite different names*

### Comparing `beautifulsoup4-4.9.2/doc.ptbr/source/index.rst` & `beautifulsoup4-4.9.3/doc.ptbr/source/index.rst`

 * *Files identical despite different names*

### Comparing `beautifulsoup4-4.9.2/doc.ru/Makefile` & `beautifulsoup4-4.9.3/doc.ru/Makefile`

 * *Files identical despite different names*

### Comparing `beautifulsoup4-4.9.2/doc.ru/source/6.1.jpg` & `beautifulsoup4-4.9.3/doc.ru/source/6.1.jpg`

 * *Files identical despite different names*

### Comparing `beautifulsoup4-4.9.2/doc.ru/source/bs4ru.rst` & `beautifulsoup4-4.9.3/doc.ru/source/bs4ru.rst`

 * *Files identical despite different names*

### Comparing `beautifulsoup4-4.9.2/doc.ru/source/conf.py` & `beautifulsoup4-4.9.3/doc.ru/source/conf.py`

 * *Files identical despite different names*

### Comparing `beautifulsoup4-4.9.2/doc.zh/Makefile` & `beautifulsoup4-4.9.3/doc.zh/Makefile`

 * *Files identical despite different names*

### Comparing `beautifulsoup4-4.9.2/doc.zh/source/6.1.jpg` & `beautifulsoup4-4.9.3/doc.zh/source/6.1.jpg`

 * *Files identical despite different names*

### Comparing `beautifulsoup4-4.9.2/doc.zh/source/conf.py` & `beautifulsoup4-4.9.3/doc.zh/source/conf.py`

 * *Files identical despite different names*

### Comparing `beautifulsoup4-4.9.2/doc.zh/source/index.rst` & `beautifulsoup4-4.9.3/doc.zh/source/index.rst`

 * *Files identical despite different names*

### Comparing `beautifulsoup4-4.9.2/scripts/demonstrate_parser_differences.py` & `beautifulsoup4-4.9.3/scripts/demonstrate_parser_differences.py`

 * *Files identical despite different names*

### Comparing `beautifulsoup4-4.9.2/scripts/demonstration_markup.txt` & `beautifulsoup4-4.9.3/scripts/demonstration_markup.txt`

 * *Files identical despite different names*

### Comparing `beautifulsoup4-4.9.2/setup.py` & `beautifulsoup4-4.9.3/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -8,15 +8,15 @@
     long_description = fh.read()
 
 setup(
     name="beautifulsoup4",
     # NOTE: We can't import __version__ from bs4 because bs4/__init__.py is Python 2 code,
     # and converting it to Python 3 means going through this code to run 2to3.
     # So we have to specify it twice for the time being.
-    version = '4.9.2',
+    version = '4.9.3',
     author="Leonard Richardson",
     author_email='leonardr@segfault.org',
     url="http://www.crummy.com/software/BeautifulSoup/bs4/",
     download_url = "http://www.crummy.com/software/BeautifulSoup/bs4/download/",
     description="Screen-scraping library",
     install_requires=[
         "soupsieve >1.2; python_version>='3.0'",
```

