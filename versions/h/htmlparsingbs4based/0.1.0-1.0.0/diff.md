# Comparing `tmp/htmlparsingbs4based-0.1.0.tar.gz` & `tmp/htmlparsingbs4based-1.0.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "htmlparsingbs4based-0.1.0.tar", last modified: Tue Apr  4 07:17:36 2023, max compression
+gzip compressed data, was "htmlparsingbs4based-1.0.0.tar", last modified: Fri Apr  7 09:29:17 2023, max compression
```

## Comparing `htmlparsingbs4based-0.1.0.tar` & `htmlparsingbs4based-1.0.0.tar`

### file list

```diff
@@ -1,62 +1,62 @@
-drwxrwxr-x   0 yaxiong   (1006) yaxiong   (1006)        0 2023-04-04 07:17:36.101295 htmlparsingbs4based-0.1.0/
--rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)     1014 2023-04-04 07:17:36.101295 htmlparsingbs4based-0.1.0/PKG-INFO
--rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)      582 2023-04-04 07:14:35.000000 htmlparsingbs4based-0.1.0/README.md
-drwxrwxr-x   0 yaxiong   (1006) yaxiong   (1006)        0 2023-04-04 07:17:36.093295 htmlparsingbs4based-0.1.0/htmlparsingbs4based/
--rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)        0 2023-04-03 15:22:50.000000 htmlparsingbs4based-0.1.0/htmlparsingbs4based/__init__.py
-drwxrwxr-x   0 yaxiong   (1006) yaxiong   (1006)        0 2023-04-04 07:17:36.097295 htmlparsingbs4based-0.1.0/htmlparsingbs4based/html_parsing/
--rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)        0 2023-04-03 15:23:03.000000 htmlparsingbs4based-0.1.0/htmlparsingbs4based/html_parsing/__init__.py
-drwxrwxr-x   0 yaxiong   (1006) yaxiong   (1006)        0 2023-04-04 07:17:36.097295 htmlparsingbs4based-0.1.0/htmlparsingbs4based/html_parsing/html2text_cp/
--rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)    38536 2023-02-11 21:06:06.000000 htmlparsingbs4based-0.1.0/htmlparsingbs4based/html_parsing/html2text_cp/__init__.py
--rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)       33 2023-02-11 21:06:06.000000 htmlparsingbs4based-0.1.0/htmlparsingbs4based/html_parsing/html2text_cp/__main__.py
--rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)     9592 2023-02-11 21:06:06.000000 htmlparsingbs4based-0.1.0/htmlparsingbs4based/html_parsing/html2text_cp/cli.py
--rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)     4026 2023-02-11 21:06:06.000000 htmlparsingbs4based-0.1.0/htmlparsingbs4based/html_parsing/html2text_cp/config.py
--rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)     4000 2023-02-11 21:06:06.000000 htmlparsingbs4based-0.1.0/htmlparsingbs4based/html_parsing/html2text_cp/config_bp.py
--rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)      441 2023-02-11 21:06:06.000000 htmlparsingbs4based-0.1.0/htmlparsingbs4based/html_parsing/html2text_cp/elements.py
--rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)       74 2023-02-11 21:06:06.000000 htmlparsingbs4based-0.1.0/htmlparsingbs4based/html_parsing/html2text_cp/typing.py
--rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)     8319 2023-02-11 21:06:06.000000 htmlparsingbs4based-0.1.0/htmlparsingbs4based/html_parsing/html2text_cp/utils.py
--rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)    10450 2023-02-11 21:06:06.000000 htmlparsingbs4based-0.1.0/htmlparsingbs4based/html_parsing/html_.py
--rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)    31997 2023-04-03 19:45:03.000000 htmlparsingbs4based-0.1.0/htmlparsingbs4based/html_parsing/html_parser_bs4_concise.py
--rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)    35306 2023-04-03 19:36:41.000000 htmlparsingbs4based-0.1.0/htmlparsingbs4based/html_parsing/html_parsing_custombs4.py
-drwxrwxr-x   0 yaxiong   (1006) yaxiong   (1006)        0 2023-04-04 07:17:36.097295 htmlparsingbs4based-0.1.0/htmlparsingbs4based/html_parsing/inscriptis_cp/
--rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)     4360 2023-04-03 20:32:51.000000 htmlparsingbs4based-0.1.0/htmlparsingbs4based/html_parsing/inscriptis_cp/__init__.py
-drwxrwxr-x   0 yaxiong   (1006) yaxiong   (1006)        0 2023-04-04 07:17:36.097295 htmlparsingbs4based-0.1.0/htmlparsingbs4based/html_parsing/inscriptis_cp/annotation/
--rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)     2283 2023-04-03 20:34:03.000000 htmlparsingbs4based-0.1.0/htmlparsingbs4based/html_parsing/inscriptis_cp/annotation/__init__.py
-drwxrwxr-x   0 yaxiong   (1006) yaxiong   (1006)        0 2023-04-04 07:17:36.097295 htmlparsingbs4based-0.1.0/htmlparsingbs4based/html_parsing/inscriptis_cp/annotation/output/
--rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)     2003 2023-02-11 21:06:06.000000 htmlparsingbs4based-0.1.0/htmlparsingbs4based/html_parsing/inscriptis_cp/annotation/output/__init__.py
--rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)     3970 2023-02-11 21:06:06.000000 htmlparsingbs4based-0.1.0/htmlparsingbs4based/html_parsing/inscriptis_cp/annotation/output/html.py
--rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)      986 2023-02-11 21:06:06.000000 htmlparsingbs4based-0.1.0/htmlparsingbs4based/html_parsing/inscriptis_cp/annotation/output/surface.py
--rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)     1641 2023-02-11 21:06:06.000000 htmlparsingbs4based-0.1.0/htmlparsingbs4based/html_parsing/inscriptis_cp/annotation/output/xml.py
--rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)     3654 2023-04-03 20:34:13.000000 htmlparsingbs4based-0.1.0/htmlparsingbs4based/html_parsing/inscriptis_cp/annotation/parser.py
--rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)     3769 2023-04-03 20:33:39.000000 htmlparsingbs4based-0.1.0/htmlparsingbs4based/html_parsing/inscriptis_cp/css_profiles.py
--rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)    13666 2023-04-03 20:35:03.000000 htmlparsingbs4based-0.1.0/htmlparsingbs4based/html_parsing/inscriptis_cp/html_engine.py
--rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)     1486 2023-02-11 21:06:06.000000 htmlparsingbs4based-0.1.0/htmlparsingbs4based/html_parsing/inscriptis_cp/html_properties.py
--rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)      281 2023-02-11 21:06:06.000000 htmlparsingbs4based-0.1.0/htmlparsingbs4based/html_parsing/inscriptis_cp/metadata.py
-drwxrwxr-x   0 yaxiong   (1006) yaxiong   (1006)        0 2023-04-04 07:17:36.101295 htmlparsingbs4based-0.1.0/htmlparsingbs4based/html_parsing/inscriptis_cp/model/
--rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)      280 2023-02-11 21:06:06.000000 htmlparsingbs4based-0.1.0/htmlparsingbs4based/html_parsing/inscriptis_cp/model/__init__.py
--rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)     2420 2023-04-03 20:34:28.000000 htmlparsingbs4based-0.1.0/htmlparsingbs4based/html_parsing/inscriptis_cp/model/attribute.py
-drwxrwxr-x   0 yaxiong   (1006) yaxiong   (1006)        0 2023-04-04 07:17:36.101295 htmlparsingbs4based-0.1.0/htmlparsingbs4based/html_parsing/inscriptis_cp/model/canvas/
--rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)     6409 2023-04-03 20:35:21.000000 htmlparsingbs4based-0.1.0/htmlparsingbs4based/html_parsing/inscriptis_cp/model/canvas/__init__.py
--rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)     3029 2023-04-03 20:35:50.000000 htmlparsingbs4based-0.1.0/htmlparsingbs4based/html_parsing/inscriptis_cp/model/canvas/block.py
--rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)     3272 2023-02-11 21:06:06.000000 htmlparsingbs4based-0.1.0/htmlparsingbs4based/html_parsing/inscriptis_cp/model/canvas/prefix.py
--rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)     3201 2023-04-03 20:33:21.000000 htmlparsingbs4based-0.1.0/htmlparsingbs4based/html_parsing/inscriptis_cp/model/config.py
--rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)     4854 2023-04-03 20:34:43.000000 htmlparsingbs4based-0.1.0/htmlparsingbs4based/html_parsing/inscriptis_cp/model/css.py
--rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)     6049 2023-04-03 20:33:53.000000 htmlparsingbs4based-0.1.0/htmlparsingbs4based/html_parsing/inscriptis_cp/model/html_element.py
--rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)    10122 2023-04-03 20:36:04.000000 htmlparsingbs4based-0.1.0/htmlparsingbs4based/html_parsing/inscriptis_cp/model/table.py
-drwxrwxr-x   0 yaxiong   (1006) yaxiong   (1006)        0 2023-04-04 07:17:36.101295 htmlparsingbs4based-0.1.0/htmlparsingbs4based/html_parsing/inscriptis_cp/service/
--rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)       35 2023-02-11 21:06:06.000000 htmlparsingbs4based-0.1.0/htmlparsingbs4based/html_parsing/inscriptis_cp/service/__init__.py
--rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)     1462 2023-02-11 21:06:06.000000 htmlparsingbs4based-0.1.0/htmlparsingbs4based/html_parsing/inscriptis_cp/service/web.py
-drwxrwxr-x   0 yaxiong   (1006) yaxiong   (1006)        0 2023-04-04 07:17:36.101295 htmlparsingbs4based-0.1.0/htmlparsingbs4based/utils/
--rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)        0 2023-04-03 15:23:07.000000 htmlparsingbs4based-0.1.0/htmlparsingbs4based/utils/__init__.py
--rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)     1715 2023-04-03 19:42:38.000000 htmlparsingbs4based-0.1.0/htmlparsingbs4based/utils/elastic.py
--rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)     1290 2023-04-03 18:06:11.000000 htmlparsingbs4based-0.1.0/htmlparsingbs4based/utils/helpers.py
--rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)     3103 2023-03-22 15:52:03.000000 htmlparsingbs4based-0.1.0/htmlparsingbs4based/utils/visualization.py
-drwxrwxr-x   0 yaxiong   (1006) yaxiong   (1006)        0 2023-04-04 07:17:36.097295 htmlparsingbs4based-0.1.0/htmlparsingbs4based.egg-info/
--rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)     1014 2023-04-04 07:17:36.000000 htmlparsingbs4based-0.1.0/htmlparsingbs4based.egg-info/PKG-INFO
--rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)     2606 2023-04-04 07:17:36.000000 htmlparsingbs4based-0.1.0/htmlparsingbs4based.egg-info/SOURCES.txt
--rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)        1 2023-04-04 07:17:36.000000 htmlparsingbs4based-0.1.0/htmlparsingbs4based.egg-info/dependency_links.txt
--rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)      101 2023-04-04 07:17:36.000000 htmlparsingbs4based-0.1.0/htmlparsingbs4based.egg-info/entry_points.txt
--rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)      276 2023-04-04 07:17:36.000000 htmlparsingbs4based-0.1.0/htmlparsingbs4based.egg-info/requires.txt
--rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)       29 2023-04-04 07:17:36.000000 htmlparsingbs4based-0.1.0/htmlparsingbs4based.egg-info/top_level.txt
--rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)      335 2023-04-03 19:46:02.000000 htmlparsingbs4based-0.1.0/settings.py
--rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)       38 2023-04-04 07:17:36.101295 htmlparsingbs4based-0.1.0/setup.cfg
--rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)      884 2023-04-04 07:17:13.000000 htmlparsingbs4based-0.1.0/setup.py
+drwxrwxr-x   0 yaxiong   (1006) yaxiong   (1006)        0 2023-04-07 09:29:17.818593 htmlparsingbs4based-1.0.0/
+-rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)     1253 2023-04-07 09:29:17.818593 htmlparsingbs4based-1.0.0/PKG-INFO
+-rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)      857 2023-04-07 09:19:47.000000 htmlparsingbs4based-1.0.0/README.md
+drwxrwxr-x   0 yaxiong   (1006) yaxiong   (1006)        0 2023-04-07 09:29:17.810593 htmlparsingbs4based-1.0.0/htmlparsingbs4based/
+-rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)        0 2023-04-03 15:22:50.000000 htmlparsingbs4based-1.0.0/htmlparsingbs4based/__init__.py
+drwxrwxr-x   0 yaxiong   (1006) yaxiong   (1006)        0 2023-04-07 09:29:17.810593 htmlparsingbs4based-1.0.0/htmlparsingbs4based/html_parsing/
+-rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)        0 2023-04-03 15:23:03.000000 htmlparsingbs4based-1.0.0/htmlparsingbs4based/html_parsing/__init__.py
+drwxrwxr-x   0 yaxiong   (1006) yaxiong   (1006)        0 2023-04-07 09:29:17.814593 htmlparsingbs4based-1.0.0/htmlparsingbs4based/html_parsing/html2text_cp/
+-rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)    38536 2023-02-11 21:06:06.000000 htmlparsingbs4based-1.0.0/htmlparsingbs4based/html_parsing/html2text_cp/__init__.py
+-rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)       33 2023-02-11 21:06:06.000000 htmlparsingbs4based-1.0.0/htmlparsingbs4based/html_parsing/html2text_cp/__main__.py
+-rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)     9592 2023-02-11 21:06:06.000000 htmlparsingbs4based-1.0.0/htmlparsingbs4based/html_parsing/html2text_cp/cli.py
+-rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)     4026 2023-02-11 21:06:06.000000 htmlparsingbs4based-1.0.0/htmlparsingbs4based/html_parsing/html2text_cp/config.py
+-rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)     4000 2023-02-11 21:06:06.000000 htmlparsingbs4based-1.0.0/htmlparsingbs4based/html_parsing/html2text_cp/config_bp.py
+-rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)      441 2023-02-11 21:06:06.000000 htmlparsingbs4based-1.0.0/htmlparsingbs4based/html_parsing/html2text_cp/elements.py
+-rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)       74 2023-02-11 21:06:06.000000 htmlparsingbs4based-1.0.0/htmlparsingbs4based/html_parsing/html2text_cp/typing.py
+-rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)     8319 2023-02-11 21:06:06.000000 htmlparsingbs4based-1.0.0/htmlparsingbs4based/html_parsing/html2text_cp/utils.py
+-rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)    10443 2023-04-06 07:51:01.000000 htmlparsingbs4based-1.0.0/htmlparsingbs4based/html_parsing/html_.py
+-rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)    31861 2023-04-07 08:44:54.000000 htmlparsingbs4based-1.0.0/htmlparsingbs4based/html_parsing/html_parser_custombs4_script.py
+-rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)    35132 2023-04-07 09:02:50.000000 htmlparsingbs4based-1.0.0/htmlparsingbs4based/html_parsing/html_parsing_custombs4.py
+drwxrwxr-x   0 yaxiong   (1006) yaxiong   (1006)        0 2023-04-07 09:29:17.814593 htmlparsingbs4based-1.0.0/htmlparsingbs4based/html_parsing/inscriptis_cp/
+-rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)     4360 2023-04-03 20:32:51.000000 htmlparsingbs4based-1.0.0/htmlparsingbs4based/html_parsing/inscriptis_cp/__init__.py
+drwxrwxr-x   0 yaxiong   (1006) yaxiong   (1006)        0 2023-04-07 09:29:17.814593 htmlparsingbs4based-1.0.0/htmlparsingbs4based/html_parsing/inscriptis_cp/annotation/
+-rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)     2283 2023-04-03 20:34:03.000000 htmlparsingbs4based-1.0.0/htmlparsingbs4based/html_parsing/inscriptis_cp/annotation/__init__.py
+drwxrwxr-x   0 yaxiong   (1006) yaxiong   (1006)        0 2023-04-07 09:29:17.814593 htmlparsingbs4based-1.0.0/htmlparsingbs4based/html_parsing/inscriptis_cp/annotation/output/
+-rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)     2003 2023-02-11 21:06:06.000000 htmlparsingbs4based-1.0.0/htmlparsingbs4based/html_parsing/inscriptis_cp/annotation/output/__init__.py
+-rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)     3970 2023-02-11 21:06:06.000000 htmlparsingbs4based-1.0.0/htmlparsingbs4based/html_parsing/inscriptis_cp/annotation/output/html.py
+-rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)      986 2023-02-11 21:06:06.000000 htmlparsingbs4based-1.0.0/htmlparsingbs4based/html_parsing/inscriptis_cp/annotation/output/surface.py
+-rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)     1641 2023-02-11 21:06:06.000000 htmlparsingbs4based-1.0.0/htmlparsingbs4based/html_parsing/inscriptis_cp/annotation/output/xml.py
+-rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)     3654 2023-04-03 20:34:13.000000 htmlparsingbs4based-1.0.0/htmlparsingbs4based/html_parsing/inscriptis_cp/annotation/parser.py
+-rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)     3769 2023-04-03 20:33:39.000000 htmlparsingbs4based-1.0.0/htmlparsingbs4based/html_parsing/inscriptis_cp/css_profiles.py
+-rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)    13666 2023-04-03 20:35:03.000000 htmlparsingbs4based-1.0.0/htmlparsingbs4based/html_parsing/inscriptis_cp/html_engine.py
+-rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)     1486 2023-02-11 21:06:06.000000 htmlparsingbs4based-1.0.0/htmlparsingbs4based/html_parsing/inscriptis_cp/html_properties.py
+-rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)      281 2023-02-11 21:06:06.000000 htmlparsingbs4based-1.0.0/htmlparsingbs4based/html_parsing/inscriptis_cp/metadata.py
+drwxrwxr-x   0 yaxiong   (1006) yaxiong   (1006)        0 2023-04-07 09:29:17.814593 htmlparsingbs4based-1.0.0/htmlparsingbs4based/html_parsing/inscriptis_cp/model/
+-rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)      280 2023-02-11 21:06:06.000000 htmlparsingbs4based-1.0.0/htmlparsingbs4based/html_parsing/inscriptis_cp/model/__init__.py
+-rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)     2420 2023-04-03 20:34:28.000000 htmlparsingbs4based-1.0.0/htmlparsingbs4based/html_parsing/inscriptis_cp/model/attribute.py
+drwxrwxr-x   0 yaxiong   (1006) yaxiong   (1006)        0 2023-04-07 09:29:17.814593 htmlparsingbs4based-1.0.0/htmlparsingbs4based/html_parsing/inscriptis_cp/model/canvas/
+-rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)     6409 2023-04-03 20:35:21.000000 htmlparsingbs4based-1.0.0/htmlparsingbs4based/html_parsing/inscriptis_cp/model/canvas/__init__.py
+-rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)     3029 2023-04-03 20:35:50.000000 htmlparsingbs4based-1.0.0/htmlparsingbs4based/html_parsing/inscriptis_cp/model/canvas/block.py
+-rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)     3272 2023-02-11 21:06:06.000000 htmlparsingbs4based-1.0.0/htmlparsingbs4based/html_parsing/inscriptis_cp/model/canvas/prefix.py
+-rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)     3201 2023-04-03 20:33:21.000000 htmlparsingbs4based-1.0.0/htmlparsingbs4based/html_parsing/inscriptis_cp/model/config.py
+-rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)     4854 2023-04-03 20:34:43.000000 htmlparsingbs4based-1.0.0/htmlparsingbs4based/html_parsing/inscriptis_cp/model/css.py
+-rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)     6049 2023-04-03 20:33:53.000000 htmlparsingbs4based-1.0.0/htmlparsingbs4based/html_parsing/inscriptis_cp/model/html_element.py
+-rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)    10122 2023-04-03 20:36:04.000000 htmlparsingbs4based-1.0.0/htmlparsingbs4based/html_parsing/inscriptis_cp/model/table.py
+drwxrwxr-x   0 yaxiong   (1006) yaxiong   (1006)        0 2023-04-07 09:29:17.818593 htmlparsingbs4based-1.0.0/htmlparsingbs4based/html_parsing/inscriptis_cp/service/
+-rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)       35 2023-02-11 21:06:06.000000 htmlparsingbs4based-1.0.0/htmlparsingbs4based/html_parsing/inscriptis_cp/service/__init__.py
+-rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)     1462 2023-02-11 21:06:06.000000 htmlparsingbs4based-1.0.0/htmlparsingbs4based/html_parsing/inscriptis_cp/service/web.py
+drwxrwxr-x   0 yaxiong   (1006) yaxiong   (1006)        0 2023-04-07 09:29:17.818593 htmlparsingbs4based-1.0.0/htmlparsingbs4based/utils/
+-rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)        0 2023-04-03 15:23:07.000000 htmlparsingbs4based-1.0.0/htmlparsingbs4based/utils/__init__.py
+-rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)     1715 2023-04-03 19:42:38.000000 htmlparsingbs4based-1.0.0/htmlparsingbs4based/utils/elastic.py
+-rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)     1290 2023-04-03 18:06:11.000000 htmlparsingbs4based-1.0.0/htmlparsingbs4based/utils/helpers.py
+-rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)     3103 2023-03-22 15:52:03.000000 htmlparsingbs4based-1.0.0/htmlparsingbs4based/utils/visualization.py
+drwxrwxr-x   0 yaxiong   (1006) yaxiong   (1006)        0 2023-04-07 09:29:17.810593 htmlparsingbs4based-1.0.0/htmlparsingbs4based.egg-info/
+-rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)     1253 2023-04-07 09:29:17.000000 htmlparsingbs4based-1.0.0/htmlparsingbs4based.egg-info/PKG-INFO
+-rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)     2611 2023-04-07 09:29:17.000000 htmlparsingbs4based-1.0.0/htmlparsingbs4based.egg-info/SOURCES.txt
+-rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)        1 2023-04-07 09:29:17.000000 htmlparsingbs4based-1.0.0/htmlparsingbs4based.egg-info/dependency_links.txt
+-rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)      100 2023-04-07 09:29:17.000000 htmlparsingbs4based-1.0.0/htmlparsingbs4based.egg-info/entry_points.txt
+-rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)      276 2023-04-07 09:29:17.000000 htmlparsingbs4based-1.0.0/htmlparsingbs4based.egg-info/requires.txt
+-rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)       29 2023-04-07 09:29:17.000000 htmlparsingbs4based-1.0.0/htmlparsingbs4based.egg-info/top_level.txt
+-rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)      335 2023-04-03 19:46:02.000000 htmlparsingbs4based-1.0.0/settings.py
+-rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)       38 2023-04-07 09:29:17.818593 htmlparsingbs4based-1.0.0/setup.cfg
+-rw-rw-r--   0 yaxiong   (1006) yaxiong   (1006)      884 2023-04-07 09:04:37.000000 htmlparsingbs4based-1.0.0/setup.py
```

### Comparing `htmlparsingbs4based-0.1.0/htmlparsingbs4based/html_parsing/html2text_cp/__init__.py` & `htmlparsingbs4based-1.0.0/htmlparsingbs4based/html_parsing/html2text_cp/__init__.py`

 * *Files identical despite different names*

### Comparing `htmlparsingbs4based-0.1.0/htmlparsingbs4based/html_parsing/html2text_cp/cli.py` & `htmlparsingbs4based-1.0.0/htmlparsingbs4based/html_parsing/html2text_cp/cli.py`

 * *Files identical despite different names*

### Comparing `htmlparsingbs4based-0.1.0/htmlparsingbs4based/html_parsing/html2text_cp/config.py` & `htmlparsingbs4based-1.0.0/htmlparsingbs4based/html_parsing/html2text_cp/config.py`

 * *Files identical despite different names*

### Comparing `htmlparsingbs4based-0.1.0/htmlparsingbs4based/html_parsing/html2text_cp/config_bp.py` & `htmlparsingbs4based-1.0.0/htmlparsingbs4based/html_parsing/html2text_cp/config_bp.py`

 * *Files identical despite different names*

### Comparing `htmlparsingbs4based-0.1.0/htmlparsingbs4based/html_parsing/html2text_cp/utils.py` & `htmlparsingbs4based-1.0.0/htmlparsingbs4based/html_parsing/html2text_cp/utils.py`

 * *Files identical despite different names*

### Comparing `htmlparsingbs4based-0.1.0/htmlparsingbs4based/html_parsing/html_.py` & `htmlparsingbs4based-1.0.0/htmlparsingbs4based/html_parsing/html_.py`

 * *Files 1% similar despite different names*

```diff
@@ -2,15 +2,15 @@
 
 from boilerpy3.extractors import ArticleExtractor
 from bs4 import BeautifulSoup, Comment, NavigableString
 import unidecode
 import re
 from description_extraction.utils.langdetect import detect
 from googletrans import Translator
-from description_extraction.crawling.helpers import crawl, get_crawling_results
+from description_extraction.crawling.helpers import get_crawling_results
 
 googlemt_model = Translator() # google translation model api configure
 cookie_keywords = set(
     ['accept', 'policy', 'analytics', 'agree', 'collect', 'site', 'experience', 'data', 'help', 'traffic',
      'information', 'setting', 'performance', 'read', 'change', 'preference', 'enable',
      'security', 'analys', 'improve', 'use', 'gather', 'find', 'advertis', 'click', 'consent', 'enhance',
      'provide', '3rd', 'third', 'terms', 'statement', 'review', 'store', 'deliver', 'technolog', 'disclaim'])
```

### Comparing `htmlparsingbs4based-0.1.0/htmlparsingbs4based/html_parsing/html_parser_bs4_concise.py` & `htmlparsingbs4based-1.0.0/htmlparsingbs4based/html_parsing/html_parser_custombs4_script.py`

 * *Files 1% similar despite different names*

```diff
@@ -227,38 +227,32 @@
                 else:
                     content = content_str(child.find_all(text=True, recursive=False)).strip()
 
             '''form get_child with tag name with extract content
             **if tag name is <a> or <img>, include the metadata
             append get_child to res(ult)'''
             if containsLetterOrNumber(content) is True:
+                printnote = True
                 contents = content.split('\n')
                 for line in contents: # if '\n' included in content, we should split it now
-                    if (str(child.name) == 'footer' or 'a') and content_str([line.strip()]) not in ['#IMAGE#', '#FOOTER#']:
+                    if (str(child.name) == 'footer' or str(child.name) == 'a') and content_str([line.strip()]) not in ['#IMAGE#', '#FOOTER#']:
                         get_child = "<<" + str(child.name) + ">>" + '\t'*(i+1) +  content_str([line.strip()])
                     else:
                         get_child = "<<" + str(child.name) + ">>" + '\t'*(i) +  content_str([line.strip()])
                     if child.name in ['a'] and child.get('href') != None:
                         get_child = [get_child, ['hyperlink', unquote(child.get('href'))]]
                     if child.name in ['img'] and child.get('alt') != None:
                         get_child = [get_child, ['image', unquote(child.get('alt'))]]
-                    res.append(get_child)
-                # if len(contents) == 2 and (contents[0].strip() == '#BLOCK#' and contents[1].strip() == ''):
-                #     printnote = False
-                # elif len(contents) == 1 and (contents[0].strip() == '#FOOTER#'):
-                #     printnote = False
-                # else:    
-                printnote = True
+                    res.append(get_child)                 
             
             '''if embed_text_list is not empty, append the item to res(ult)'''
             if embed_text_list != []:
+                printnote = True
                 for get_child_embed in embed_text_list:
                     res.append(get_child_embed)
-                printnote = True
-            
             '''if there is nothing print out, we should reduce the current level by 1'''
             j = i + 1
             if printnote == False:
                 j = j - 1
 
             '''walker the child if child name is not <th>, <td>'''
             if child.name not in ['th', 'td']:
@@ -601,19 +595,24 @@
     except:
         print('ERROR:cannot get html ', input_url)
         file_exist = False
     
     if file_exist:
         doc_dict = traverse_html_with_bs(html_page, html_url, min_length, prefix)
         text = doc_dict["text"]
-        #print(text)
-        my_file = open('my_file.txt', 'w')
+        labels = doc_dict["labels"]
+        
+        my_file = open('parser_output.txt', 'w')
         my_file.write(text)
         my_file.close()
-        print(doc_dict["labels"])
+        
+        my_file2 = open('labels_output.txt', 'w')
+        my_file2.write(str(labels))
+        my_file2.close()
+        
         meta_cont = doc_dict["metadata"]
         meta_conta = []
         for itema in meta_cont:
             meta_conta.append([itema[0], itema[1], itema[3]])
 
 
 if __name__ == '__main__':
@@ -638,12 +637,12 @@
     https://www.talaviation.com/News
     https://vincoconstruction.com/
     https://www.mineexcellence.com/
     https://www.felcaroroldan.com/ # order/level problem
 
     https://www.metex.it/it/azienda
     '''
-    parse_single_page(input_url='http://www.mineracamargo.com/MCA_Investors.html', 
-                      path_to_crawled_files='/home/yaxiong/crawled_websites2',
+    parse_single_page(input_url='https://bryansfuel.on.ca/about/', 
+                      path_to_crawled_files='/home/yaxiong/data_crawled_websites/crawled_websites_first_batch',
                       min_length=1, 
                       prefix="")
```

### Comparing `htmlparsingbs4based-0.1.0/htmlparsingbs4based/html_parsing/html_parsing_custombs4.py` & `htmlparsingbs4based-1.0.0/htmlparsingbs4based/html_parsing/html_parsing_custombs4.py`

 * *Files 0% similar despite different names*

```diff
@@ -7,15 +7,15 @@
 import pandas as pd
 from tqdm import tqdm
 from urllib.parse import unquote
 from settings import ELASTIC_PRODUCT_INDEX
 import argparse
 
 parser = argparse.ArgumentParser(description='Arguments for HTML parser')
-parser.add_argument("-i", "--input_url", help="Input an url you want to parse", required=True)
+parser.add_argument("-i", "--input_url", help="Input an url you want to parse", default="")
 parser.add_argument("-gpf", "--get_pages_from", help="Option: 'local' or 'elasticsearch'", default="local")
 parser.add_argument("-f", "--file_path", help="File path to the crawled html", default="")
 parser.add_argument("-esusr", "--elastic_user", help="User of elasticsearch", default="")
 parser.add_argument("-espw", "--elastic_password", help="Password of elasticsearch", default="")
 parser.add_argument("-v", "--visualization", help="Generate visulized labels file", default=False)
 parser.add_argument("-p", "--prefix", help="Define the prefix to the labels", default="")
 parser.add_argument("-m", "--min_length", help="Define the min number of words for each line", default=1, type=int)
@@ -243,37 +243,32 @@
                 else:
                     content = content_str(child.find_all(text=True, recursive=False)).strip()
 
             '''form get_child with tag name with extract content
             **if tag name is <a> or <img>, include the metadata
             append get_child to res(ult)'''
             if containsLetterOrNumber(content) is True:
+                printnote = True
                 contents = content.split('\n')
                 for line in contents: # if '\n' included in content, we should split it now
-                    if (str(child.name) == 'footer' or 'a') and content_str([line.strip()]) not in ['#IMAGE#', '#FOOTER#']:
+                    if (str(child.name) == 'footer' or str(child.name) == 'a') and content_str([line.strip()]) not in ['#IMAGE#', '#FOOTER#']:
                         get_child = "<<" + str(child.name) + ">>" + '\t'*(i+1) +  content_str([line.strip()])
                     else:
                         get_child = "<<" + str(child.name) + ">>" + '\t'*(i) +  content_str([line.strip()])
                     if child.name in ['a'] and child.get('href') != None:
                         get_child = [get_child, ['hyperlink', unquote(child.get('href'))]]
                     if child.name in ['img'] and child.get('alt') != None:
                         get_child = [get_child, ['image', unquote(child.get('alt'))]]
                     res.append(get_child)
-                # if len(contents) == 2 and (contents[0].strip() == '#BLOCK#' and contents[1].strip() == ''):
-                #     printnote = False
-                # elif len(contents) == 1 and (contents[0].strip() == '#FOOTER#'):
-                #     printnote = False
-                # else:    
-                printnote = True
             
             '''if embed_text_list is not empty, append the item to res(ult)'''
             if embed_text_list != []:
+                printnote = True
                 for get_child_embed in embed_text_list:
                     res.append(get_child_embed)
-                printnote = True
             
             '''if there is nothing print out, we should reduce the current level by 1'''
             j = i + 1
             if printnote == False:
                 j = j - 1
 
             '''walker the child if child name is not <th>, <td>'''
@@ -601,32 +596,35 @@
                     break
                 except:
                     pass
     
     if file_exist:
         doc_dict = traverse_html_with_bs(html_page, html_url, min_length, prefix)
         text = doc_dict["text"]
-        #print(text)
-        my_file = open('my_file.txt', 'w')
+        labels = doc_dict["labels"]
+        
+        my_file = open('parser_output.txt', 'w')
         my_file.write(text)
         my_file.close()
-        print(doc_dict["labels"])
-        #print(text[7117:7470])
+        
+        my_file2 = open('labels_output.txt', 'w')
+        my_file2.write(str(labels))
+        my_file2.close()
         meta_cont = doc_dict["metadata"]
         meta_conta = []
         for itema in meta_cont:
             meta_conta.append([itema[0], itema[1], itema[3]])
         if visualization:
             visual(text, doc_dict["labels"], "./v_example1.html")
             visual(text, meta_conta, "./v_example_m1.html")
     else:
         print('ERROR: cannot get html ', input_url)
 
-def generate_jl(file_path):
-    with open(file_path) as f:
+def generate_jl(file_path_webpage):
+    with open(file_path_webpage) as f:
         lines = f.read().splitlines()
     my_dict = {}
     for i, line in enumerate(lines):
         try:
             my_dict[i] = json.loads(line)
         except:
             pass
@@ -699,9 +697,9 @@
     https://vincoconstruction.com/
     https://www.mineexcellence.com/
     https://www.felcaroroldan.com/ # order/level problem
 
     https://www.metex.it/it/azienda
     '''
     parse_single_page()
-    #generate_jl(file_path='/home/yaxiong/backupfiles/descriptionextraction_data/description_annotation_final_dontdelete.jl')
+    #generate_jl(file_path_webpage='/home/yaxiong/data_backupfiles/descriptionextraction_data/description_annotation_final_dontdelete.jl')
```

### Comparing `htmlparsingbs4based-0.1.0/htmlparsingbs4based/html_parsing/inscriptis_cp/__init__.py` & `htmlparsingbs4based-1.0.0/htmlparsingbs4based/html_parsing/inscriptis_cp/__init__.py`

 * *Files identical despite different names*

### Comparing `htmlparsingbs4based-0.1.0/htmlparsingbs4based/html_parsing/inscriptis_cp/annotation/__init__.py` & `htmlparsingbs4based-1.0.0/htmlparsingbs4based/html_parsing/inscriptis_cp/annotation/__init__.py`

 * *Files identical despite different names*

### Comparing `htmlparsingbs4based-0.1.0/htmlparsingbs4based/html_parsing/inscriptis_cp/annotation/output/__init__.py` & `htmlparsingbs4based-1.0.0/htmlparsingbs4based/html_parsing/inscriptis_cp/annotation/output/__init__.py`

 * *Files identical despite different names*

### Comparing `htmlparsingbs4based-0.1.0/htmlparsingbs4based/html_parsing/inscriptis_cp/annotation/output/html.py` & `htmlparsingbs4based-1.0.0/htmlparsingbs4based/html_parsing/inscriptis_cp/annotation/output/html.py`

 * *Files identical despite different names*

### Comparing `htmlparsingbs4based-0.1.0/htmlparsingbs4based/html_parsing/inscriptis_cp/annotation/output/surface.py` & `htmlparsingbs4based-1.0.0/htmlparsingbs4based/html_parsing/inscriptis_cp/annotation/output/surface.py`

 * *Files identical despite different names*

### Comparing `htmlparsingbs4based-0.1.0/htmlparsingbs4based/html_parsing/inscriptis_cp/annotation/output/xml.py` & `htmlparsingbs4based-1.0.0/htmlparsingbs4based/html_parsing/inscriptis_cp/annotation/output/xml.py`

 * *Files identical despite different names*

### Comparing `htmlparsingbs4based-0.1.0/htmlparsingbs4based/html_parsing/inscriptis_cp/annotation/parser.py` & `htmlparsingbs4based-1.0.0/htmlparsingbs4based/html_parsing/inscriptis_cp/annotation/parser.py`

 * *Files identical despite different names*

### Comparing `htmlparsingbs4based-0.1.0/htmlparsingbs4based/html_parsing/inscriptis_cp/css_profiles.py` & `htmlparsingbs4based-1.0.0/htmlparsingbs4based/html_parsing/inscriptis_cp/css_profiles.py`

 * *Files identical despite different names*

### Comparing `htmlparsingbs4based-0.1.0/htmlparsingbs4based/html_parsing/inscriptis_cp/html_engine.py` & `htmlparsingbs4based-1.0.0/htmlparsingbs4based/html_parsing/inscriptis_cp/html_engine.py`

 * *Files identical despite different names*

### Comparing `htmlparsingbs4based-0.1.0/htmlparsingbs4based/html_parsing/inscriptis_cp/html_properties.py` & `htmlparsingbs4based-1.0.0/htmlparsingbs4based/html_parsing/inscriptis_cp/html_properties.py`

 * *Files identical despite different names*

### Comparing `htmlparsingbs4based-0.1.0/htmlparsingbs4based/html_parsing/inscriptis_cp/model/attribute.py` & `htmlparsingbs4based-1.0.0/htmlparsingbs4based/html_parsing/inscriptis_cp/model/attribute.py`

 * *Files identical despite different names*

### Comparing `htmlparsingbs4based-0.1.0/htmlparsingbs4based/html_parsing/inscriptis_cp/model/canvas/__init__.py` & `htmlparsingbs4based-1.0.0/htmlparsingbs4based/html_parsing/inscriptis_cp/model/canvas/__init__.py`

 * *Files identical despite different names*

### Comparing `htmlparsingbs4based-0.1.0/htmlparsingbs4based/html_parsing/inscriptis_cp/model/canvas/block.py` & `htmlparsingbs4based-1.0.0/htmlparsingbs4based/html_parsing/inscriptis_cp/model/canvas/block.py`

 * *Files identical despite different names*

### Comparing `htmlparsingbs4based-0.1.0/htmlparsingbs4based/html_parsing/inscriptis_cp/model/canvas/prefix.py` & `htmlparsingbs4based-1.0.0/htmlparsingbs4based/html_parsing/inscriptis_cp/model/canvas/prefix.py`

 * *Files identical despite different names*

### Comparing `htmlparsingbs4based-0.1.0/htmlparsingbs4based/html_parsing/inscriptis_cp/model/config.py` & `htmlparsingbs4based-1.0.0/htmlparsingbs4based/html_parsing/inscriptis_cp/model/config.py`

 * *Files identical despite different names*

### Comparing `htmlparsingbs4based-0.1.0/htmlparsingbs4based/html_parsing/inscriptis_cp/model/css.py` & `htmlparsingbs4based-1.0.0/htmlparsingbs4based/html_parsing/inscriptis_cp/model/css.py`

 * *Files identical despite different names*

### Comparing `htmlparsingbs4based-0.1.0/htmlparsingbs4based/html_parsing/inscriptis_cp/model/html_element.py` & `htmlparsingbs4based-1.0.0/htmlparsingbs4based/html_parsing/inscriptis_cp/model/html_element.py`

 * *Files identical despite different names*

### Comparing `htmlparsingbs4based-0.1.0/htmlparsingbs4based/html_parsing/inscriptis_cp/model/table.py` & `htmlparsingbs4based-1.0.0/htmlparsingbs4based/html_parsing/inscriptis_cp/model/table.py`

 * *Files identical despite different names*

### Comparing `htmlparsingbs4based-0.1.0/htmlparsingbs4based/html_parsing/inscriptis_cp/service/web.py` & `htmlparsingbs4based-1.0.0/htmlparsingbs4based/html_parsing/inscriptis_cp/service/web.py`

 * *Files identical despite different names*

### Comparing `htmlparsingbs4based-0.1.0/htmlparsingbs4based/utils/elastic.py` & `htmlparsingbs4based-1.0.0/htmlparsingbs4based/utils/elastic.py`

 * *Files identical despite different names*

### Comparing `htmlparsingbs4based-0.1.0/htmlparsingbs4based/utils/helpers.py` & `htmlparsingbs4based-1.0.0/htmlparsingbs4based/utils/helpers.py`

 * *Files identical despite different names*

### Comparing `htmlparsingbs4based-0.1.0/htmlparsingbs4based/utils/visualization.py` & `htmlparsingbs4based-1.0.0/htmlparsingbs4based/utils/visualization.py`

 * *Files identical despite different names*

### Comparing `htmlparsingbs4based-0.1.0/htmlparsingbs4based.egg-info/SOURCES.txt` & `htmlparsingbs4based-1.0.0/htmlparsingbs4based.egg-info/SOURCES.txt`

 * *Files 1% similar despite different names*

```diff
@@ -6,15 +6,15 @@
 htmlparsingbs4based.egg-info/SOURCES.txt
 htmlparsingbs4based.egg-info/dependency_links.txt
 htmlparsingbs4based.egg-info/entry_points.txt
 htmlparsingbs4based.egg-info/requires.txt
 htmlparsingbs4based.egg-info/top_level.txt
 htmlparsingbs4based/html_parsing/__init__.py
 htmlparsingbs4based/html_parsing/html_.py
-htmlparsingbs4based/html_parsing/html_parser_bs4_concise.py
+htmlparsingbs4based/html_parsing/html_parser_custombs4_script.py
 htmlparsingbs4based/html_parsing/html_parsing_custombs4.py
 htmlparsingbs4based/html_parsing/html2text_cp/__init__.py
 htmlparsingbs4based/html_parsing/html2text_cp/__main__.py
 htmlparsingbs4based/html_parsing/html2text_cp/cli.py
 htmlparsingbs4based/html_parsing/html2text_cp/config.py
 htmlparsingbs4based/html_parsing/html2text_cp/config_bp.py
 htmlparsingbs4based/html_parsing/html2text_cp/elements.py
```

### Comparing `htmlparsingbs4based-0.1.0/setup.py` & `htmlparsingbs4based-1.0.0/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 from setuptools import setup, find_packages
 
 with open('/home/yaxiong/html_parsing/requirements.txt') as f:
     requirements = f.read().splitlines()
 
 setup(
     name='htmlparsingbs4based',
-    version='0.1.0',
+    version='1.0.0',
     author='Yaxiong Yuan',
     author_email='yaxiong.yuan@finquest.com',
     packages=find_packages(),
     py_modules=['settings'],
     url='https://finquest.com/',
     description='This package extracts/parses information from source HTML.',
     long_description=open('README.md', 'r').read(),
```

