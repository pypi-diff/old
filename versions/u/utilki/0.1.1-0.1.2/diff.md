# Comparing `tmp/utilki-0.1.1.tar.gz` & `tmp/utilki-0.1.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "utilki-0.1.1.tar", max compression
+gzip compressed data, was "utilki-0.1.2.tar", max compression
```

## Comparing `utilki-0.1.1.tar` & `utilki-0.1.2.tar`

### file list

```diff
@@ -1,6 +1,7 @@
--rw-r--r--   0        0        0      458 2023-04-07 09:26:35.281023 utilki-0.1.1/pyproject.toml
--rw-r--r--   0        0        0       73 2023-04-06 19:12:02.029197 utilki-0.1.1/utilki/__init__.py
--rw-r--r--   0        0        0     2196 2023-04-07 09:24:46.978148 utilki-0.1.1/utilki/cli.py
--rw-r--r--   0        0        0     2148 2023-04-07 09:04:04.272868 utilki-0.1.1/utilki/task_mixin.py
--rw-r--r--   0        0        0      681 2023-04-07 09:26:42.611338 utilki-0.1.1/setup.py
--rw-r--r--   0        0        0      330 2023-04-07 09:26:42.611572 utilki-0.1.1/PKG-INFO
+-rw-r--r--   0        0        0      859 2023-04-07 09:22:40.435495 utilki-0.1.2/README.md
+-rw-r--r--   0        0        0      511 2023-04-07 09:30:50.493727 utilki-0.1.2/pyproject.toml
+-rw-r--r--   0        0        0       73 2023-04-06 19:12:02.029197 utilki-0.1.2/utilki/__init__.py
+-rw-r--r--   0        0        0     2196 2023-04-07 09:24:46.978148 utilki-0.1.2/utilki/cli.py
+-rw-r--r--   0        0        0     2148 2023-04-07 09:04:04.272868 utilki-0.1.2/utilki/task_mixin.py
+-rw-r--r--   0        0        0     1614 2023-04-07 09:33:11.828525 utilki-0.1.2/setup.py
+-rw-r--r--   0        0        0     1263 2023-04-07 09:33:11.828776 utilki-0.1.2/PKG-INFO
```

### Comparing `utilki-0.1.1/utilki/cli.py` & `utilki-0.1.2/utilki/cli.py`

 * *Files identical despite different names*

### Comparing `utilki-0.1.1/utilki/task_mixin.py` & `utilki-0.1.2/utilki/task_mixin.py`

 * *Files identical despite different names*

