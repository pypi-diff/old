# Comparing `tmp/webdav3_cli-0.1.0a1.tar.gz` & `tmp/webdav3_cli-1.0.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "webdav3_cli-0.1.0a1.tar", max compression
+gzip compressed data, was "webdav3_cli-1.0.0.tar", max compression
```

## Comparing `webdav3_cli-0.1.0a1.tar` & `webdav3_cli-1.0.0.tar`

### file list

```diff
@@ -1,13 +1,14 @@
--rw-r--r--   0        0        0      521 2023-04-06 20:54:34.452935 webdav3_cli-0.1.0a1/pyproject.toml
--rw-r--r--   0        0        0        0 2023-04-06 16:53:31.973265 webdav3_cli-0.1.0a1/src/webdav3_cli/__init__.py
--rw-r--r--   0        0        0      984 2023-04-06 20:40:14.662015 webdav3_cli-0.1.0a1/src/webdav3_cli/cli.py
--rw-r--r--   0        0        0       43 2023-04-06 16:53:31.975271 webdav3_cli-0.1.0a1/src/webdav3_cli/cli_parsers/__init__.py
--rw-r--r--   0        0        0      204 2023-04-06 16:53:31.976270 webdav3_cli-0.1.0a1/src/webdav3_cli/cli_parsers/ArgumentParser.py
--rw-r--r--   0        0        0     2750 2023-04-06 21:46:05.311037 webdav3_cli-0.1.0a1/src/webdav3_cli/cli_parsers/ConfigCommandParser.py
--rw-r--r--   0        0        0      147 2022-11-16 17:42:43.829354 webdav3_cli-0.1.0a1/src/webdav3_cli/cli_parsers/DebugParser.py
--rw-r--r--   0        0        0      721 2023-04-06 22:07:59.208799 webdav3_cli-0.1.0a1/src/webdav3_cli/cli_parsers/ListCommandParser.py
--rw-r--r--   0        0        0      997 2023-04-06 22:07:21.275405 webdav3_cli-0.1.0a1/src/webdav3_cli/cli_parsers/UploadCommandParser.py
--rw-r--r--   0        0        0      722 2023-04-06 21:40:54.746363 webdav3_cli-0.1.0a1/src/webdav3_cli/Configuration.py
--rw-r--r--   0        0        0     1752 2023-04-06 21:56:55.150793 webdav3_cli-0.1.0a1/src/webdav3_cli/webdav3client_wrapper.py
--rw-r--r--   0        0        0      873 1970-01-01 00:00:00.000000 webdav3_cli-0.1.0a1/setup.py
--rw-r--r--   0        0        0      480 1970-01-01 00:00:00.000000 webdav3_cli-0.1.0a1/PKG-INFO
+-rw-r--r--   0        0        0      518 2023-04-06 22:17:25.949780 webdav3_cli-1.0.0/pyproject.toml
+-rw-r--r--   0        0        0      811 2023-04-06 22:17:18.838882 webdav3_cli-1.0.0/README.md
+-rw-r--r--   0        0        0        0 2023-04-06 16:53:31.973265 webdav3_cli-1.0.0/src/webdav3_cli/__init__.py
+-rw-r--r--   0        0        0      982 2023-04-06 22:17:33.380019 webdav3_cli-1.0.0/src/webdav3_cli/cli.py
+-rw-r--r--   0        0        0       43 2023-04-06 16:53:31.975271 webdav3_cli-1.0.0/src/webdav3_cli/cli_parsers/__init__.py
+-rw-r--r--   0        0        0      204 2023-04-06 16:53:31.976270 webdav3_cli-1.0.0/src/webdav3_cli/cli_parsers/ArgumentParser.py
+-rw-r--r--   0        0        0     2750 2023-04-06 21:46:05.311037 webdav3_cli-1.0.0/src/webdav3_cli/cli_parsers/ConfigCommandParser.py
+-rw-r--r--   0        0        0      147 2022-11-16 17:42:43.829354 webdav3_cli-1.0.0/src/webdav3_cli/cli_parsers/DebugParser.py
+-rw-r--r--   0        0        0      721 2023-04-06 22:07:59.208799 webdav3_cli-1.0.0/src/webdav3_cli/cli_parsers/ListCommandParser.py
+-rw-r--r--   0        0        0      997 2023-04-06 22:07:21.275405 webdav3_cli-1.0.0/src/webdav3_cli/cli_parsers/UploadCommandParser.py
+-rw-r--r--   0        0        0      722 2023-04-06 21:40:54.746363 webdav3_cli-1.0.0/src/webdav3_cli/Configuration.py
+-rw-r--r--   0        0        0     1752 2023-04-06 21:56:55.150793 webdav3_cli-1.0.0/src/webdav3_cli/webdav3client_wrapper.py
+-rw-r--r--   0        0        0     1678 1970-01-01 00:00:00.000000 webdav3_cli-1.0.0/setup.py
+-rw-r--r--   0        0        0     1303 1970-01-01 00:00:00.000000 webdav3_cli-1.0.0/PKG-INFO
```

### Comparing `webdav3_cli-0.1.0a1/pyproject.toml` & `webdav3_cli-1.0.0/pyproject.toml`

 * *Files 22% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 [tool.poetry]
 name = "webdav3-cli"
-version = "0.1.0a1"
+version = "1.0.0"
 description = "Command line interface for webdav3"
 authors = ["Nicholas Johnson <nicholas.m.j@gmail.com>"]
-#readme = "README.md"
+readme = "README.md"
 packages = [ { include = "webdav3_cli", from = "src" }]
 
 [tool.poetry.dependencies]
 python = "^3.9"
 webdavclient3 = "^3.14.6"
 tomlkit = "^0.11.7"
```

### Comparing `webdav3_cli-0.1.0a1/src/webdav3_cli/cli.py` & `webdav3_cli-1.0.0/src/webdav3_cli/cli.py`

 * *Files 10% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 from webdav3_cli.cli_parsers import ArgumentParser
 from webdav3_cli.cli_parsers import UploadCommandParser, ListCommandParser, ConfigCommandParser
 
 import logging
 import sys
 
 
-__version = "0.1.0a1"
+__version = "1.0.0"
 
 
 def _setup_logging():
     logging.basicConfig(level=logging.DEBUG)
 
 
 def _setup_parser():
```

### Comparing `webdav3_cli-0.1.0a1/src/webdav3_cli/cli_parsers/ConfigCommandParser.py` & `webdav3_cli-1.0.0/src/webdav3_cli/cli_parsers/ConfigCommandParser.py`

 * *Files identical despite different names*

### Comparing `webdav3_cli-0.1.0a1/src/webdav3_cli/cli_parsers/ListCommandParser.py` & `webdav3_cli-1.0.0/src/webdav3_cli/cli_parsers/ListCommandParser.py`

 * *Files identical despite different names*

### Comparing `webdav3_cli-0.1.0a1/src/webdav3_cli/cli_parsers/UploadCommandParser.py` & `webdav3_cli-1.0.0/src/webdav3_cli/cli_parsers/UploadCommandParser.py`

 * *Files identical despite different names*

### Comparing `webdav3_cli-0.1.0a1/src/webdav3_cli/Configuration.py` & `webdav3_cli-1.0.0/src/webdav3_cli/Configuration.py`

 * *Files identical despite different names*

### Comparing `webdav3_cli-0.1.0a1/src/webdav3_cli/webdav3client_wrapper.py` & `webdav3_cli-1.0.0/src/webdav3_cli/webdav3client_wrapper.py`

 * *Files identical despite different names*

