# Comparing `tmp/sysnet-pyutils-0.0.9.tar.gz` & `tmp/sysnet-pyutils-1.0.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "sysnet-pyutils-0.0.9.tar", last modified: Mon Mar 27 20:13:17 2023, max compression
+gzip compressed data, was "sysnet-pyutils-1.0.0.tar", last modified: Thu Apr  6 10:29:43 2023, max compression
```

## Comparing `sysnet-pyutils-0.0.9.tar` & `sysnet-pyutils-1.0.0.tar`

### file list

```diff
@@ -1,16 +1,18 @@
-drwxrwxrwx   0        0        0        0 2023-03-27 20:13:17.815519 sysnet-pyutils-0.0.9/
--rw-rw-rw-   0        0        0    35184 2023-03-27 14:59:40.000000 sysnet-pyutils-0.0.9/LICENSE
--rw-rw-rw-   0        0        0      562 2023-03-27 20:13:17.815519 sysnet-pyutils-0.0.9/PKG-INFO
--rw-rw-rw-   0        0        0       36 2023-03-27 14:59:40.000000 sysnet-pyutils-0.0.9/README.md
--rw-rw-rw-   0        0        0      778 2023-03-27 20:12:42.000000 sysnet-pyutils-0.0.9/pyproject.toml
--rw-rw-rw-   0        0        0       47 2023-03-27 16:22:12.000000 sysnet-pyutils-0.0.9/requirements.txt
--rw-rw-rw-   0        0        0       42 2023-03-27 20:13:17.831147 sysnet-pyutils-0.0.9/setup.cfg
-drwxrwxrwx   0        0        0        0 2023-03-27 20:13:17.815519 sysnet-pyutils-0.0.9/sysnet_pyutils/
--rw-rw-rw-   0        0        0        0 2023-03-27 15:02:04.000000 sysnet-pyutils-0.0.9/sysnet_pyutils/__init__.py
--rw-rw-rw-   0        0        0     4788 2023-03-27 20:12:42.000000 sysnet-pyutils-0.0.9/sysnet_pyutils/utils.py
-drwxrwxrwx   0        0        0        0 2023-03-27 20:13:17.815519 sysnet-pyutils-0.0.9/sysnet_pyutils.egg-info/
--rw-rw-rw-   0        0        0      562 2023-03-27 20:13:17.000000 sysnet-pyutils-0.0.9/sysnet_pyutils.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      289 2023-03-27 20:13:17.000000 sysnet-pyutils-0.0.9/sysnet_pyutils.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-03-27 20:13:17.000000 sysnet-pyutils-0.0.9/sysnet_pyutils.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       48 2023-03-27 20:13:17.000000 sysnet-pyutils-0.0.9/sysnet_pyutils.egg-info/requires.txt
--rw-rw-rw-   0        0        0       15 2023-03-27 20:13:17.000000 sysnet-pyutils-0.0.9/sysnet_pyutils.egg-info/top_level.txt
+drwxrwxrwx   0        0        0        0 2023-04-06 10:29:43.799494 sysnet-pyutils-1.0.0/
+-rw-rw-rw-   0        0        0    35184 2023-03-27 14:59:40.000000 sysnet-pyutils-1.0.0/LICENSE
+-rw-rw-rw-   0        0        0     5807 2023-04-06 10:29:43.799494 sysnet-pyutils-1.0.0/PKG-INFO
+-rw-rw-rw-   0        0        0     5185 2023-04-06 10:22:58.000000 sysnet-pyutils-1.0.0/README.md
+-rw-rw-rw-   0        0        0      862 2023-04-06 10:26:51.000000 sysnet-pyutils-1.0.0/pyproject.toml
+-rw-rw-rw-   0        0        0       47 2023-03-27 16:22:12.000000 sysnet-pyutils-1.0.0/requirements.txt
+-rw-rw-rw-   0        0        0       42 2023-04-06 10:29:43.799494 sysnet-pyutils-1.0.0/setup.cfg
+drwxrwxrwx   0        0        0        0 2023-04-06 10:29:43.790486 sysnet-pyutils-1.0.0/sysnet_pyutils/
+-rw-rw-rw-   0        0        0        0 2023-03-27 15:02:04.000000 sysnet-pyutils-1.0.0/sysnet_pyutils/__init__.py
+-rw-rw-rw-   0        0        0     2622 2023-04-06 08:45:17.000000 sysnet-pyutils-1.0.0/sysnet_pyutils/barcode.py
+-rw-rw-rw-   0        0        0     2737 2023-04-06 08:45:17.000000 sysnet-pyutils-1.0.0/sysnet_pyutils/ident.py
+-rw-rw-rw-   0        0        0     8632 2023-04-06 10:28:59.000000 sysnet-pyutils-1.0.0/sysnet_pyutils/utils.py
+drwxrwxrwx   0        0        0        0 2023-04-06 10:29:43.799494 sysnet-pyutils-1.0.0/sysnet_pyutils.egg-info/
+-rw-rw-rw-   0        0        0     5807 2023-04-06 10:29:43.000000 sysnet-pyutils-1.0.0/sysnet_pyutils.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      339 2023-04-06 10:29:43.000000 sysnet-pyutils-1.0.0/sysnet_pyutils.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-06 10:29:43.000000 sysnet-pyutils-1.0.0/sysnet_pyutils.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       48 2023-04-06 10:29:43.000000 sysnet-pyutils-1.0.0/sysnet_pyutils.egg-info/requires.txt
+-rw-rw-rw-   0        0        0       15 2023-04-06 10:29:43.000000 sysnet-pyutils-1.0.0/sysnet_pyutils.egg-info/top_level.txt
```

### Comparing `sysnet-pyutils-0.0.9/LICENSE` & `sysnet-pyutils-1.0.0/LICENSE`

 * *Files identical despite different names*

### Comparing `sysnet-pyutils-0.0.9/pyproject.toml` & `sysnet-pyutils-1.0.0/pyproject.toml`

 * *Files 20% similar despite different names*

```diff
@@ -1,25 +1,27 @@
 [build-system]
 requires = ["setuptools>=61.0"]
 build-backend = "setuptools.build_meta"
 
 [project]
 name = "sysnet-pyutils"
-version = "0.0.9"
+version = "1.0.0"
 authors = [
   { name="Data Developer", email="info@sysnet.cz" },
 ]
 description = "Python Utilities"
 readme = "README.md"
 license = { file="LICENSE.md" }
 requires-python = ">=3.9"
 classifiers = [
-    "Development Status :: 3 - Alpha",
+    "Development Status :: 5 - Production/Stable",
     "Programming Language :: Python :: 3",
+    "Intended Audience :: Developers",
     "License :: Free For Home Use",
+    "Natural Language :: Czech",
     "Operating System :: OS Independent",
     "Topic :: Software Development :: Libraries"
 ]
 dynamic = ["dependencies"]
 [tool.setuptools.dynamic]
 dependencies = {file = ["requirements.txt"]}
```

