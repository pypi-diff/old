# Comparing `tmp/iolanta-1.0.7.tar.gz` & `tmp/iolanta-1.0.8.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "iolanta-1.0.7.tar", max compression
+gzip compressed data, was "iolanta-1.0.8.tar", max compression
```

## Comparing `iolanta-1.0.7.tar` & `iolanta-1.0.8.tar`

### file list

```diff
@@ -1,75 +1,70 @@
--rw-r--r--   0        0        0       47 2023-01-10 16:28:49.175424 iolanta-1.0.7/README.md
--rw-r--r--   0        0        0      120 2023-02-11 15:30:09.181295 iolanta-1.0.7/iolanta/__init__.py
--rw-r--r--   0        0        0       86 2023-02-11 08:59:29.937352 iolanta-1.0.7/iolanta/base_plugin.py
--rw-r--r--   0        0        0       69 2023-01-25 17:56:30.503293 iolanta-1.0.7/iolanta/cli/__init__.py
--rw-r--r--   0        0        0        0 2023-01-02 21:08:12.691702 iolanta-1.0.7/iolanta/cli/formatters/__init__.py
--rw-r--r--   0        0        0     1137 2023-01-29 17:21:53.919997 iolanta-1.0.7/iolanta/cli/formatters/choose.py
--rw-r--r--   0        0        0      753 2023-01-29 17:26:39.037862 iolanta-1.0.7/iolanta/cli/formatters/csv.py
--rw-r--r--   0        0        0      741 2023-01-29 17:26:25.997777 iolanta-1.0.7/iolanta/cli/formatters/json.py
--rw-r--r--   0        0        0      794 2023-01-29 18:25:40.783408 iolanta-1.0.7/iolanta/cli/formatters/node_to_qname.py
--rw-r--r--   0        0        0     2920 2023-02-11 15:30:09.201296 iolanta-1.0.7/iolanta/cli/formatters/pretty.py
--rw-r--r--   0        0        0     3955 2023-02-19 20:53:14.755940 iolanta-1.0.7/iolanta/cli/main.py
--rw-r--r--   0        0        0      159 2023-02-19 20:41:34.969046 iolanta-1.0.7/iolanta/cli/models.py
--rw-r--r--   0        0        0      977 2022-05-14 17:33:27.542327 iolanta-1.0.7/iolanta/cli/pretty_print.py
--rw-r--r--   0        0        0      507 2023-02-11 15:30:09.169295 iolanta-1.0.7/iolanta/context.py
--rw-r--r--   0        0        0     1188 2023-01-12 09:54:08.360278 iolanta-1.0.7/iolanta/conversions.py
--rw-r--r--   0        0        0     1307 2023-02-19 21:15:32.162088 iolanta-1.0.7/iolanta/data/context.yaml
--rw-r--r--   0        0        0      172 2023-02-19 21:16:35.030407 iolanta-1.0.7/iolanta/data/facets.yaml
--rw-r--r--   0        0        0     1647 2023-02-18 19:21:33.380349 iolanta-1.0.7/iolanta/data/iolanta.yaml
--rw-r--r--   0        0        0      717 2022-11-19 15:56:18.556420 iolanta-1.0.7/iolanta/ensure_is_context.py
--rw-r--r--   0        0        0      504 2023-01-26 13:24:50.106127 iolanta-1.0.7/iolanta/entry_points.py
--rw-r--r--   0        0        0      701 2023-02-18 21:26:00.644376 iolanta-1.0.7/iolanta/errors.py
--rw-r--r--   0        0        0       79 2023-01-28 19:03:19.327601 iolanta-1.0.7/iolanta/facet/__init__.py
--rw-r--r--   0        0        0      576 2022-12-26 10:48:35.251113 iolanta-1.0.7/iolanta/facet/base.py
--rw-r--r--   0        0        0      815 2023-01-28 19:03:19.399601 iolanta-1.0.7/iolanta/facet/by_environment.py
--rw-r--r--   0        0        0      921 2023-02-19 20:25:48.031630 iolanta-1.0.7/iolanta/facet/by_instance.py
--rw-r--r--   0        0        0     1122 2023-01-28 19:03:19.387601 iolanta-1.0.7/iolanta/facet/by_literal_datatype.py
--rw-r--r--   0        0        0     1027 2023-01-28 19:03:19.347601 iolanta-1.0.7/iolanta/facet/by_type.py
--rw-r--r--   0        0        0       40 2023-02-18 19:21:10.228210 iolanta-1.0.7/iolanta/facet/cli/__init__.py
--rw-r--r--   0        0        0      786 2023-02-19 15:12:31.288027 iolanta-1.0.7/iolanta/facet/cli/link.py
--rw-r--r--   0        0        0      163 2023-02-18 19:20:02.171800 iolanta-1.0.7/iolanta/facet/cli/sparql/link.sparql
--rw-r--r--   0        0        0     4455 2023-02-19 20:26:13.783777 iolanta-1.0.7/iolanta/facet/errors.py
--rw-r--r--   0        0        0     2157 2023-02-12 08:49:10.029428 iolanta-1.0.7/iolanta/facet/facet.py
--rw-r--r--   0        0        0      928 2023-01-28 19:03:19.411601 iolanta-1.0.7/iolanta/facet/for_literal.py
--rw-r--r--   0        0        0      156 2023-01-28 19:03:19.431601 iolanta-1.0.7/iolanta/facet/html.py
--rw-r--r--   0        0        0      271 2023-02-11 15:30:09.185296 iolanta-1.0.7/iolanta/facet/rich.py
--rw-r--r--   0        0        0      311 2022-08-07 12:35:35.538709 iolanta-1.0.7/iolanta/facet/sparql/find_facet_by_instance_types.sparql
--rw-r--r--   0        0        0      103 2022-08-07 09:33:53.366739 iolanta-1.0.7/iolanta/facet/sparql/find_facet_for_literal.sparql
--rw-r--r--   0        0        0      147 2023-02-19 21:20:17.419541 iolanta-1.0.7/iolanta/facets/__init__.py
--rw-r--r--   0        0        0      784 2023-01-28 19:00:47.882391 iolanta-1.0.7/iolanta/facets/bool_literal.py
--rw-r--r--   0        0        0      496 2023-02-11 09:00:59.513871 iolanta-1.0.7/iolanta/facets/code_literal.py
--rw-r--r--   0        0        0      550 2023-01-28 19:00:47.894391 iolanta-1.0.7/iolanta/facets/date_literal.py
--rw-r--r--   0        0        0     1829 2023-02-12 08:53:24.270916 iolanta-1.0.7/iolanta/facets/default.py
--rw-r--r--   0        0        0      519 2023-02-20 21:28:23.518223 iolanta-1.0.7/iolanta/facets/sparql/default.sparql
--rw-r--r--   0        0        0        0 2022-12-26 12:32:48.012338 iolanta-1.0.7/iolanta/graph_providers/__init__.py
--rw-r--r--   0        0        0      311 2022-12-26 12:50:41.871370 iolanta-1.0.7/iolanta/graph_providers/base.py
--rw-r--r--   0        0        0      352 2022-12-26 12:36:16.053789 iolanta-1.0.7/iolanta/graph_providers/errors.py
--rw-r--r--   0        0        0     1070 2023-01-08 17:00:02.248855 iolanta-1.0.7/iolanta/graph_providers/find.py
--rw-r--r--   0        0        0     7985 2023-02-19 20:50:07.643346 iolanta-1.0.7/iolanta/iolanta.py
--rw-r--r--   0        0        0       99 2022-11-12 16:45:59.080951 iolanta-1.0.7/iolanta/loaders/__init__.py
--rw-r--r--   0        0        0     3384 2023-02-18 16:25:33.594612 iolanta-1.0.7/iolanta/loaders/base.py
--rw-r--r--   0        0        0     1985 2023-01-28 13:24:23.703413 iolanta-1.0.7/iolanta/loaders/data_type_choice.py
--rw-r--r--   0        0        0     1696 2023-02-11 15:30:09.225296 iolanta-1.0.7/iolanta/loaders/dict_loader.py
--rw-r--r--   0        0        0      475 2023-01-28 13:17:35.321206 iolanta-1.0.7/iolanta/loaders/errors.py
--rw-r--r--   0        0        0     2900 2023-01-04 18:56:07.205184 iolanta-1.0.7/iolanta/loaders/http.py
--rw-r--r--   0        0        0     4185 2023-02-18 18:26:32.410656 iolanta-1.0.7/iolanta/loaders/local_directory.py
--rw-r--r--   0        0        0     3042 2023-02-19 20:28:50.944675 iolanta-1.0.7/iolanta/loaders/local_file.py
--rw-r--r--   0        0        0     2107 2023-01-25 18:29:16.038722 iolanta-1.0.7/iolanta/loaders/scheme_choice.py
--rw-r--r--   0        0        0     2186 2023-01-29 18:35:10.023227 iolanta-1.0.7/iolanta/models.py
--rw-r--r--   0        0        0      135 2022-03-16 16:07:28.993380 iolanta-1.0.7/iolanta/namespaces.py
--rw-r--r--   0        0        0        0 2022-03-16 16:07:28.993380 iolanta-1.0.7/iolanta/parsers/__init__.py
--rw-r--r--   0        0        0     1048 2023-02-11 15:30:09.209296 iolanta-1.0.7/iolanta/parsers/base.py
--rw-r--r--   0        0        0     7069 2023-02-11 15:30:09.213296 iolanta-1.0.7/iolanta/parsers/dict_parser.py
--rw-r--r--   0        0        0      600 2023-01-15 08:45:19.693781 iolanta-1.0.7/iolanta/parsers/errors.py
--rw-r--r--   0        0        0      970 2023-02-18 16:22:17.805402 iolanta-1.0.7/iolanta/parsers/json.py
--rw-r--r--   0        0        0     1669 2023-02-11 09:06:42.703838 iolanta-1.0.7/iolanta/parsers/markdown.py
--rw-r--r--   0        0        0     1244 2023-01-05 18:59:50.709495 iolanta-1.0.7/iolanta/parsers/yaml.py
--rw-r--r--   0        0        0     1057 2023-02-19 15:12:31.276027 iolanta-1.0.7/iolanta/plugin.py
--rw-r--r--   0        0        0      712 2022-12-26 10:48:35.507115 iolanta-1.0.7/iolanta/reformat_blank_nodes.py
--rw-r--r--   0        0        0     5885 2023-02-18 21:18:03.724032 iolanta-1.0.7/iolanta/renderer.py
--rw-r--r--   0        0        0     1895 2023-02-18 16:28:34.519729 iolanta-1.0.7/iolanta/shortcuts.py
--rw-r--r--   0        0        0       33 2022-03-16 16:07:28.993380 iolanta-1.0.7/ldflex/__init__.py
--rw-r--r--   0        0        0     3228 2023-02-11 09:06:50.559882 iolanta-1.0.7/ldflex/ldflex.py
--rw-r--r--   0        0        0      857 2023-02-26 17:34:35.237393 iolanta-1.0.7/pyproject.toml
--rw-r--r--   0        0        0     1478 1970-01-01 00:00:00.000000 iolanta-1.0.7/setup.py
--rw-r--r--   0        0        0     1047 1970-01-01 00:00:00.000000 iolanta-1.0.7/PKG-INFO
+-rw-r--r--   0        0        0       47 2023-01-10 16:28:49.175424 iolanta-1.0.8/README.md
+-rw-r--r--   0        0        0      120 2023-02-11 15:30:09.181295 iolanta-1.0.8/iolanta/__init__.py
+-rw-r--r--   0        0        0       86 2023-02-11 08:59:29.937352 iolanta-1.0.8/iolanta/base_plugin.py
+-rw-r--r--   0        0        0       69 2023-01-25 17:56:30.503293 iolanta-1.0.8/iolanta/cli/__init__.py
+-rw-r--r--   0        0        0        0 2023-01-02 21:08:12.691702 iolanta-1.0.8/iolanta/cli/formatters/__init__.py
+-rw-r--r--   0        0        0     1137 2023-01-29 17:21:53.919997 iolanta-1.0.8/iolanta/cli/formatters/choose.py
+-rw-r--r--   0        0        0      753 2023-01-29 17:26:39.037862 iolanta-1.0.8/iolanta/cli/formatters/csv.py
+-rw-r--r--   0        0        0      741 2023-01-29 17:26:25.997777 iolanta-1.0.8/iolanta/cli/formatters/json.py
+-rw-r--r--   0        0        0      794 2023-01-29 18:25:40.783408 iolanta-1.0.8/iolanta/cli/formatters/node_to_qname.py
+-rw-r--r--   0        0        0     2920 2023-02-11 15:30:09.201296 iolanta-1.0.8/iolanta/cli/formatters/pretty.py
+-rw-r--r--   0        0        0     3955 2023-02-19 20:53:14.755940 iolanta-1.0.8/iolanta/cli/main.py
+-rw-r--r--   0        0        0      159 2023-02-19 20:41:34.969046 iolanta-1.0.8/iolanta/cli/models.py
+-rw-r--r--   0        0        0      977 2022-05-14 17:33:27.542327 iolanta-1.0.8/iolanta/cli/pretty_print.py
+-rw-r--r--   0        0        0      507 2023-02-11 15:30:09.169295 iolanta-1.0.8/iolanta/context.py
+-rw-r--r--   0        0        0     1188 2023-01-12 09:54:08.360278 iolanta-1.0.8/iolanta/conversions.py
+-rw-r--r--   0        0        0      216 2023-03-04 10:53:56.058688 iolanta-1.0.8/iolanta/data/cli.yaml
+-rw-r--r--   0        0        0     1313 2023-02-27 20:25:19.126238 iolanta-1.0.8/iolanta/data/context.yaml
+-rw-r--r--   0        0        0      183 2023-03-04 13:17:36.281042 iolanta-1.0.8/iolanta/data/facets.yaml
+-rw-r--r--   0        0        0      166 2023-03-04 10:42:51.255346 iolanta-1.0.8/iolanta/data/html.yaml
+-rw-r--r--   0        0        0     1031 2023-03-04 10:44:51.979932 iolanta-1.0.8/iolanta/data/iolanta.yaml
+-rw-r--r--   0        0        0      717 2022-11-19 15:56:18.556420 iolanta-1.0.8/iolanta/ensure_is_context.py
+-rw-r--r--   0        0        0      504 2023-01-26 13:24:50.106127 iolanta-1.0.8/iolanta/entry_points.py
+-rw-r--r--   0        0        0      701 2023-02-18 21:26:00.644376 iolanta-1.0.8/iolanta/errors.py
+-rw-r--r--   0        0        0        0 2023-03-04 13:36:49.548666 iolanta-1.0.8/iolanta/facets/__init__.py
+-rw-r--r--   0        0        0      105 2023-03-04 12:09:17.881659 iolanta-1.0.8/iolanta/facets/cli/__init__.py
+-rw-r--r--   0        0        0      278 2023-03-03 18:30:04.134545 iolanta-1.0.8/iolanta/facets/cli/base.py
+-rw-r--r--   0        0        0      365 2023-03-04 12:43:47.772191 iolanta-1.0.8/iolanta/facets/cli/default.py
+-rw-r--r--   0        0        0      163 2023-02-18 19:20:02.171800 iolanta-1.0.8/iolanta/facets/cli/sparql/link.sparql
+-rw-r--r--   0        0        0     3974 2023-03-04 13:25:58.296332 iolanta-1.0.8/iolanta/facets/errors.py
+-rw-r--r--   0        0        0     2131 2023-03-02 17:56:26.555781 iolanta-1.0.8/iolanta/facets/facet.py
+-rw-r--r--   0        0        0      116 2023-03-04 13:31:02.150430 iolanta-1.0.8/iolanta/facets/generic/__init__.py
+-rw-r--r--   0        0        0      398 2023-03-04 13:25:58.280332 iolanta-1.0.8/iolanta/facets/generic/bool_literal.py
+-rw-r--r--   0        0        0      557 2023-03-03 18:30:04.002544 iolanta-1.0.8/iolanta/facets/generic/date_literal.py
+-rw-r--r--   0        0        0     1748 2023-03-04 13:31:02.150430 iolanta-1.0.8/iolanta/facets/generic/default.py
+-rw-r--r--   0        0        0      546 2023-03-04 12:16:53.996928 iolanta-1.0.8/iolanta/facets/generic/sparql/default.sparql
+-rw-r--r--   0        0        0       48 2023-03-04 12:09:27.193713 iolanta-1.0.8/iolanta/facets/html/__init__.py
+-rw-r--r--   0        0        0      163 2023-03-03 18:30:04.014544 iolanta-1.0.8/iolanta/facets/html/base.py
+-rw-r--r--   0        0        0      394 2023-03-04 13:25:58.256332 iolanta-1.0.8/iolanta/facets/html/code_literal.py
+-rw-r--r--   0        0        0      612 2023-03-04 12:46:19.601163 iolanta-1.0.8/iolanta/facets/html/default.py
+-rw-r--r--   0        0        0     3977 2023-03-03 18:30:04.098545 iolanta-1.0.8/iolanta/facets/locator.py
+-rw-r--r--   0        0        0     7941 2023-03-04 11:48:03.398235 iolanta-1.0.8/iolanta/iolanta.py
+-rw-r--r--   0        0        0       99 2022-11-12 16:45:59.080951 iolanta-1.0.8/iolanta/loaders/__init__.py
+-rw-r--r--   0        0        0     3384 2023-02-18 16:25:33.594612 iolanta-1.0.8/iolanta/loaders/base.py
+-rw-r--r--   0        0        0     1985 2023-01-28 13:24:23.703413 iolanta-1.0.8/iolanta/loaders/data_type_choice.py
+-rw-r--r--   0        0        0     1696 2023-02-11 15:30:09.225296 iolanta-1.0.8/iolanta/loaders/dict_loader.py
+-rw-r--r--   0        0        0      475 2023-01-28 13:17:35.321206 iolanta-1.0.8/iolanta/loaders/errors.py
+-rw-r--r--   0        0        0     2900 2023-01-04 18:56:07.205184 iolanta-1.0.8/iolanta/loaders/http.py
+-rw-r--r--   0        0        0     4185 2023-02-18 18:26:32.410656 iolanta-1.0.8/iolanta/loaders/local_directory.py
+-rw-r--r--   0        0        0     3042 2023-02-19 20:28:50.944675 iolanta-1.0.8/iolanta/loaders/local_file.py
+-rw-r--r--   0        0        0     2107 2023-01-25 18:29:16.038722 iolanta-1.0.8/iolanta/loaders/scheme_choice.py
+-rw-r--r--   0        0        0     2186 2023-01-29 18:35:10.023227 iolanta-1.0.8/iolanta/models.py
+-rw-r--r--   0        0        0      135 2022-03-16 16:07:28.993380 iolanta-1.0.8/iolanta/namespaces.py
+-rw-r--r--   0        0        0        0 2022-03-16 16:07:28.993380 iolanta-1.0.8/iolanta/parsers/__init__.py
+-rw-r--r--   0        0        0     1048 2023-02-11 15:30:09.209296 iolanta-1.0.8/iolanta/parsers/base.py
+-rw-r--r--   0        0        0     7069 2023-02-11 15:30:09.213296 iolanta-1.0.8/iolanta/parsers/dict_parser.py
+-rw-r--r--   0        0        0      600 2023-01-15 08:45:19.693781 iolanta-1.0.8/iolanta/parsers/errors.py
+-rw-r--r--   0        0        0      970 2023-02-18 16:22:17.805402 iolanta-1.0.8/iolanta/parsers/json.py
+-rw-r--r--   0        0        0     1669 2023-02-11 09:06:42.703838 iolanta-1.0.8/iolanta/parsers/markdown.py
+-rw-r--r--   0        0        0     1244 2023-01-05 18:59:50.709495 iolanta-1.0.8/iolanta/parsers/yaml.py
+-rw-r--r--   0        0        0     1057 2023-02-19 15:12:31.276027 iolanta-1.0.8/iolanta/plugin.py
+-rw-r--r--   0        0        0      712 2022-12-26 10:48:35.507115 iolanta-1.0.8/iolanta/reformat_blank_nodes.py
+-rw-r--r--   0        0        0        0 2023-03-02 17:35:20.688477 iolanta-1.0.8/iolanta/resolvers/__init__.py
+-rw-r--r--   0        0        0      302 2023-03-03 18:30:04.066544 iolanta-1.0.8/iolanta/resolvers/base.py
+-rw-r--r--   0        0        0     1307 2023-03-03 18:30:04.122545 iolanta-1.0.8/iolanta/resolvers/python_import.py
+-rw-r--r--   0        0        0     1895 2023-02-18 16:28:34.519729 iolanta-1.0.8/iolanta/shortcuts.py
+-rw-r--r--   0        0        0       33 2022-03-16 16:07:28.993380 iolanta-1.0.8/ldflex/__init__.py
+-rw-r--r--   0        0        0     3228 2023-02-11 09:06:50.559882 iolanta-1.0.8/ldflex/ldflex.py
+-rw-r--r--   0        0        0      857 2023-03-04 13:38:59.193474 iolanta-1.0.8/pyproject.toml
+-rw-r--r--   0        0        0     1483 1970-01-01 00:00:00.000000 iolanta-1.0.8/setup.py
+-rw-r--r--   0        0        0     1047 1970-01-01 00:00:00.000000 iolanta-1.0.8/PKG-INFO
```

### Comparing `iolanta-1.0.7/iolanta/cli/formatters/choose.py` & `iolanta-1.0.8/iolanta/cli/formatters/choose.py`

 * *Files identical despite different names*

### Comparing `iolanta-1.0.7/iolanta/cli/formatters/csv.py` & `iolanta-1.0.8/iolanta/cli/formatters/csv.py`

 * *Files identical despite different names*

### Comparing `iolanta-1.0.7/iolanta/cli/formatters/json.py` & `iolanta-1.0.8/iolanta/cli/formatters/json.py`

 * *Files identical despite different names*

### Comparing `iolanta-1.0.7/iolanta/cli/formatters/node_to_qname.py` & `iolanta-1.0.8/iolanta/cli/formatters/node_to_qname.py`

 * *Files identical despite different names*

### Comparing `iolanta-1.0.7/iolanta/cli/formatters/pretty.py` & `iolanta-1.0.8/iolanta/cli/formatters/pretty.py`

 * *Files identical despite different names*

### Comparing `iolanta-1.0.7/iolanta/cli/main.py` & `iolanta-1.0.8/iolanta/cli/main.py`

 * *Files identical despite different names*

### Comparing `iolanta-1.0.7/iolanta/cli/pretty_print.py` & `iolanta-1.0.8/iolanta/cli/pretty_print.py`

 * *Files identical despite different names*

### Comparing `iolanta-1.0.7/iolanta/conversions.py` & `iolanta-1.0.8/iolanta/conversions.py`

 * *Files identical despite different names*

### Comparing `iolanta-1.0.7/iolanta/data/context.yaml` & `iolanta-1.0.8/iolanta/data/context.yaml`

 * *Files 18% similar despite different names*

```diff
@@ -39,18 +39,18 @@
 
   # Uncommenting any of the below will lead to a complaint about "@" from PyLD.
   # "$null": "@null"
   # "$never": "@never"
   # "$once": "@once"
   # "$always": "@always"
 
-  iolanta:instanceFacet:
+  iolanta:hasInstanceFacet:
     "@type": "@id"
 
-  iolanta:datatypeFacet:
+  iolanta:hasDatatypeFacet:
     "@type": "@id"
 
   iolanta:supports:
     "@type": "@id"
 
   iolanta:hasDefaultFacet:
     "@type": "@id"
```

### Comparing `iolanta-1.0.7/iolanta/ensure_is_context.py` & `iolanta-1.0.8/iolanta/ensure_is_context.py`

 * *Files identical despite different names*

### Comparing `iolanta-1.0.7/iolanta/errors.py` & `iolanta-1.0.8/iolanta/errors.py`

 * *Files identical despite different names*

### Comparing `iolanta-1.0.7/iolanta/facet/errors.py` & `iolanta-1.0.8/iolanta/facets/errors.py`

 * *Files 15% similar despite different names*

```diff
@@ -2,16 +2,14 @@
 from dataclasses import dataclass, field
 from typing import List
 
 from documented import DocumentedError
 from rdflib import Literal, URIRef
 from rdflib.term import Node
 
-from iolanta.facet.base import FacetSearchAttempt
-
 
 @dataclass
 class PageNotFound(DocumentedError):
     """
     Page not found by IRI: `{self.iri}`.
 
     !!! error "Page not found by IRI: `{self.iri}`"
@@ -107,77 +105,66 @@
     """
     # Facet not found.
 
     No way to render the node you asked for.
 
     - **Node:** `{self.node}` *({self.node_type})*
     - **Environments tried:** `{self.environments}`
-
-    We tried the following methods:
-
-    {self.render_facet_search_attempts}
     """
 
     node: Node
     environments: List[URIRef]
-    facet_search_attempts: List[FacetSearchAttempt]
     node_types: List[URIRef] = field(default_factory=list)
 
     @property
     def node_type(self) -> str:
         """Node type."""
         node_type = type(self.node).__name__
         if isinstance(self.node, Literal):
             datatype = self.node.datatype
             node_type = f'{node_type}, datatype={datatype}'
 
         return node_type
 
-    @property
-    def render_facet_search_attempts(self):
-        """Render facet search attempts."""
-        return textwrap.dedent(
-            ''.join(
-                f'\n\n- {attempt}'
-                for attempt in self.facet_search_attempts
-            ),
-        )
-
 
 @dataclass
 class FacetError(DocumentedError):
     """
     Facet rendering failed.
 
     !!! error "Facet has thrown an unhandled exception"
         - Node: `{self.node}`
         - Facet IRI: `{self.facet_iri}`
 
         ### Exception
 
         {self.indented_error}
-
-        Why was this facet at all chosen for this node?
-
-        ### {self.render_facet_search_attempt}
     """
 
     node: Node
     facet_iri: URIRef
-    facet_search_attempt: FacetSearchAttempt
     error: Exception
 
     @property
-    def render_facet_search_attempt(self):
-        """Render facet search attempt."""
-        return textwrap.indent(
-            f'\n## {self.facet_search_attempt}',
-            '    ',
-        )
-
-    @property
     def indented_error(self):
         """Format the underlying error text."""
         return textwrap.indent(
             str(self.error),
             prefix='    ',
         )
+
+
+@dataclass
+class NotALiteral(DocumentedError):
+    """
+    Node `{self.node}` is not a literal.
+
+    It is in fact a `{self.node_type}`. `BoolLiteral` facet only supports RDF
+    literal objects.
+    """
+
+    node: Node
+
+    @property
+    def node_type(self):
+        """Node type name."""
+        return self.node.__class__.__name__
```

### Comparing `iolanta-1.0.7/iolanta/facet/facet.py` & `iolanta-1.0.8/iolanta/facets/facet.py`

 * *Files 1% similar despite different names*

```diff
@@ -2,28 +2,27 @@
 from dataclasses import dataclass
 from functools import cached_property
 from pathlib import Path
 from typing import Any, Generic, List, Optional, TypeVar, Union
 
 from rdflib.term import BNode, Node, URIRef
 
-from iolanta.iolanta import Iolanta
 from iolanta.models import NotLiteralNode
 from ldflex import LDFlex
 from ldflex.ldflex import QueryResult, SPARQLQueryArgument
 
 FacetOutput = TypeVar('FacetOutput')
 
 
 @dataclass
 class Facet(Generic[FacetOutput]):
     """Base facet class."""
 
     iri: NotLiteralNode
-    iolanta: Iolanta
+    iolanta: 'iolanta.Iolanta'
     environment: Optional[URIRef] = None
 
     @property
     def stored_queries_path(self) -> Path:
         return Path(inspect.getfile(self.__class__)).parent / 'sparql'
 
     @property
```

### Comparing `iolanta-1.0.7/iolanta/facets/date_literal.py` & `iolanta-1.0.8/iolanta/facets/generic/date_literal.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 from datetime import date, datetime
 from typing import cast
 
 from rdflib import Literal
 
-from iolanta.facet import Facet
+from iolanta.facets.facet import Facet
 
 
 class DateLiteral(Facet):
     """Render a date."""
 
     def show(self):
         """Render date or datetime as a date."""
```

### Comparing `iolanta-1.0.7/iolanta/facets/sparql/default.sparql` & `iolanta-1.0.8/iolanta/facets/generic/sparql/default.sparql`

 * *Files 21% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-SELECT * WHERE {
+SELECT ?label ?symbol ?url ?comment WHERE {
     OPTIONAL {
         {
             $iri rdfs:label ?label .
         } UNION {
             BIND($iri AS ?label) .
             FILTER(isLiteral($iri)) .
         }
```

### Comparing `iolanta-1.0.7/iolanta/iolanta.py` & `iolanta-1.0.8/iolanta/iolanta.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,30 +1,44 @@
 import functools
 import logging
 from dataclasses import dataclass, field
 from functools import cached_property
 from pathlib import Path
-from typing import Any, Dict, Iterable, List, Optional, Set, Type, Union
+from typing import (
+    Any,
+    Dict,
+    Iterable,
+    List,
+    Mapping,
+    Optional,
+    Set,
+    Type,
+    Union,
+)
 
 import funcy
 import owlrl
 from owlrl import OWLRL_Extension
 from owlrl.Closure import Core
 from rdflib import ConjunctiveGraph, Namespace, URIRef
 from rdflib.term import Node
 
 from iolanta import entry_points
 from iolanta.errors import InsufficientDataForRender
+from iolanta.facets.errors import FacetError
+from iolanta.facets.facet import Facet
+from iolanta.facets.locator import FacetFinder
 from iolanta.loaders import Loader
 from iolanta.loaders.base import SourceType
 from iolanta.loaders.local_directory import merge_contexts
 from iolanta.models import LDContext, NotLiteralNode
 from iolanta.namespaces import IOLANTA, LOCAL
 from iolanta.parsers.yaml import YAML
 from iolanta.plugin import Plugin
+from iolanta.resolvers.python_import import PythonImportResolver
 from iolanta.shortcuts import construct_root_loader
 from ldflex import LDFlex
 
 
 @dataclass
 class Iolanta:
     """Iolanta is a Semantic web browser."""
@@ -34,14 +48,18 @@
         default_factory=functools.partial(
             ConjunctiveGraph,
             identifier=LOCAL.term('_inference'),
         ),
     )
     force_plugins: List[Type[Plugin]] = field(default_factory=list)
 
+    facet_resolver: Mapping[URIRef, Type[Facet]] = field(
+        default_factory=PythonImportResolver,
+    )
+
     logger: logging.Logger = field(
         default_factory=functools.partial(
             logging.getLogger,
             name='iolanta',
         ),
     )
 
@@ -176,60 +194,48 @@
         try:
             return self.graph.namespace_manager.expand_curie(qname)
         except ValueError:
             return URIRef(qname)
 
     def render(
         self,
-        node: Union[str, Node],
-        environments: Optional[Union[str, List[NotLiteralNode]]] = None,
+        node: Node,
+        environments: List[NotLiteralNode],
     ) -> Any:
         """Find an Iolanta facet for a node and render it."""
-        # FIXME: Convert to a global import
-        from iolanta.facet.errors import FacetError
-        from iolanta.renderer import Render, resolve_facet
-
-        if isinstance(environments, str):
-            environments = [environments]
-
         if not environments:
-            environments = [IOLANTA.html]
-
-        self.logger.info('Environments: %s', environments)
-
-        self.maybe_infer()
+            raise ValueError(
+                f'Please provide at least one environment '
+                f'to render {node} against.',
+            )
 
-        facet_search_attempt = Render(
-            ldflex=self.ldflex,
-        ).search_for_facet(
+        found = FacetFinder(
+            iolanta=self,
             node=node,
             environments=environments,
-        )
+        ).facet_and_environment
 
-        facet_class = resolve_facet(
-            iri=facet_search_attempt.facet,
-        )
+        facet_class = self.facet_resolver[found['facet']]
 
         facet = facet_class(
             iri=node,
             iolanta=self,
-            environment=facet_search_attempt.environment,
+            environment=found['environment'],
         )
 
         try:
             return facet.show()
 
         except InsufficientDataForRender:
             raise
 
         except Exception as err:
             raise FacetError(
                 node=node,
-                facet_iri=facet_search_attempt.facet,
-                facet_search_attempt=facet_search_attempt,
+                facet_iri=found['facet'],
                 error=err,
             ) from err
 
     def render_with_retrieval(
         self,
         node: Union[str, Node],
         environments: Optional[Union[str, List[NotLiteralNode]]] = None,
@@ -245,15 +251,14 @@
                 if attempt_id == 0:
                     raise ValueError('Too much data to download :(((') from err
 
                 self.retrieve(
                     node=err.node,
                 )
 
-
     def retrieve(self, node: Node) -> 'Iolanta':
         """Retrieve remote data to project directory."""
         downloaded_files = list(
             funcy.flatten(
                 plugin.retrieve(node)
                 for plugin
                 in self.plugins
```

### Comparing `iolanta-1.0.7/iolanta/loaders/base.py` & `iolanta-1.0.8/iolanta/loaders/base.py`

 * *Files identical despite different names*

### Comparing `iolanta-1.0.7/iolanta/loaders/data_type_choice.py` & `iolanta-1.0.8/iolanta/loaders/data_type_choice.py`

 * *Files identical despite different names*

### Comparing `iolanta-1.0.7/iolanta/loaders/dict_loader.py` & `iolanta-1.0.8/iolanta/loaders/dict_loader.py`

 * *Files identical despite different names*

### Comparing `iolanta-1.0.7/iolanta/loaders/http.py` & `iolanta-1.0.8/iolanta/loaders/http.py`

 * *Files identical despite different names*

### Comparing `iolanta-1.0.7/iolanta/loaders/local_directory.py` & `iolanta-1.0.8/iolanta/loaders/local_directory.py`

 * *Files identical despite different names*

### Comparing `iolanta-1.0.7/iolanta/loaders/local_file.py` & `iolanta-1.0.8/iolanta/loaders/local_file.py`

 * *Files identical despite different names*

### Comparing `iolanta-1.0.7/iolanta/loaders/scheme_choice.py` & `iolanta-1.0.8/iolanta/loaders/scheme_choice.py`

 * *Files identical despite different names*

### Comparing `iolanta-1.0.7/iolanta/models.py` & `iolanta-1.0.8/iolanta/models.py`

 * *Files identical despite different names*

### Comparing `iolanta-1.0.7/iolanta/parsers/base.py` & `iolanta-1.0.8/iolanta/parsers/base.py`

 * *Files identical despite different names*

### Comparing `iolanta-1.0.7/iolanta/parsers/dict_parser.py` & `iolanta-1.0.8/iolanta/parsers/dict_parser.py`

 * *Files identical despite different names*

### Comparing `iolanta-1.0.7/iolanta/parsers/errors.py` & `iolanta-1.0.8/iolanta/parsers/errors.py`

 * *Files identical despite different names*

### Comparing `iolanta-1.0.7/iolanta/parsers/json.py` & `iolanta-1.0.8/iolanta/parsers/json.py`

 * *Files identical despite different names*

### Comparing `iolanta-1.0.7/iolanta/parsers/markdown.py` & `iolanta-1.0.8/iolanta/parsers/markdown.py`

 * *Files identical despite different names*

### Comparing `iolanta-1.0.7/iolanta/parsers/yaml.py` & `iolanta-1.0.8/iolanta/parsers/yaml.py`

 * *Files identical despite different names*

### Comparing `iolanta-1.0.7/iolanta/plugin.py` & `iolanta-1.0.8/iolanta/plugin.py`

 * *Files identical despite different names*

### Comparing `iolanta-1.0.7/iolanta/reformat_blank_nodes.py` & `iolanta-1.0.8/iolanta/reformat_blank_nodes.py`

 * *Files identical despite different names*

### Comparing `iolanta-1.0.7/iolanta/shortcuts.py` & `iolanta-1.0.8/iolanta/shortcuts.py`

 * *Files identical despite different names*

### Comparing `iolanta-1.0.7/ldflex/ldflex.py` & `iolanta-1.0.8/ldflex/ldflex.py`

 * *Files identical despite different names*

### Comparing `iolanta-1.0.7/pyproject.toml` & `iolanta-1.0.8/pyproject.toml`

 * *Files 14% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "iolanta"
-version = "1.0.7"
+version = "1.0.8"
 description = "Semantic Web browser"
 authors = ["Anatoly Scherbakov <altaisoft@gmail.com>"]
 license = "MIT"
 readme = "README.md"
 
 packages = [
   { include = "ldflex" },
```

### Comparing `iolanta-1.0.7/setup.py` & `iolanta-1.0.8/setup.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,28 +1,28 @@
 # -*- coding: utf-8 -*-
 from setuptools import setup
 
 packages = \
 ['iolanta',
  'iolanta.cli',
  'iolanta.cli.formatters',
- 'iolanta.facet',
- 'iolanta.facet.cli',
  'iolanta.facets',
- 'iolanta.graph_providers',
+ 'iolanta.facets.cli',
+ 'iolanta.facets.generic',
+ 'iolanta.facets.html',
  'iolanta.loaders',
  'iolanta.parsers',
+ 'iolanta.resolvers',
  'ldflex']
 
 package_data = \
 {'': ['*'],
  'iolanta': ['data/*'],
- 'iolanta.facet': ['sparql/*'],
- 'iolanta.facet.cli': ['sparql/*'],
- 'iolanta.facets': ['sparql/*']}
+ 'iolanta.facets.cli': ['sparql/*'],
+ 'iolanta.facets.generic': ['sparql/*']}
 
 install_requires = \
 ['PyLD>=2.0.3,<3.0.0',
  'classes>=0.4.0,<0.5.0',
  'deepmerge>=0.1.1,<0.2.0',
  'documented>=0.1.1,<0.2.0',
  'dominate>=2.6.0,<3.0.0',
@@ -38,15 +38,15 @@
 
 entry_points = \
 {'console_scripts': ['iolanta = iolanta.cli:app'],
  'iolanta.plugins': ['base = iolanta:IolantaBase']}
 
 setup_kwargs = {
     'name': 'iolanta',
-    'version': '1.0.7',
+    'version': '1.0.8',
     'description': 'Semantic Web browser',
     'long_description': '# iolanta\n\nStub repo for the iolanta browser.\n\n',
     'author': 'Anatoly Scherbakov',
     'author_email': 'altaisoft@gmail.com',
     'maintainer': 'None',
     'maintainer_email': 'None',
     'url': 'None',
```

### Comparing `iolanta-1.0.7/PKG-INFO` & `iolanta-1.0.8/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: iolanta
-Version: 1.0.7
+Version: 1.0.8
 Summary: Semantic Web browser
 License: MIT
 Author: Anatoly Scherbakov
 Author-email: altaisoft@gmail.com
 Requires-Python: >=3.10,<4.0
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Programming Language :: Python :: 3
```

