# Comparing `tmp/allstar-1.1.4.tar.gz` & `tmp/allstar-1.1.5.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "allstar-1.1.4.tar", last modified: Tue Apr  4 04:20:12 2023, max compression
+gzip compressed data, was "allstar-1.1.5.tar", last modified: Thu Apr  6 17:38:37 2023, max compression
```

## Comparing `allstar-1.1.4.tar` & `allstar-1.1.5.tar`

### file list

```diff
@@ -1,15 +1,15 @@
-drwxrwxrwx   0        0        0        0 2023-04-04 04:20:12.901895 allstar-1.1.4/
--rw-rw-rw-   0        0        0     1089 2023-04-01 00:02:21.000000 allstar-1.1.4/LICENSE
--rw-rw-rw-   0        0        0     1992 2023-04-04 04:20:12.901895 allstar-1.1.4/PKG-INFO
-drwxrwxrwx   0        0        0        0 2023-04-04 04:20:12.889898 allstar-1.1.4/allstar/
--rw-rw-rw-   0        0        0       22 2023-04-01 01:16:06.000000 allstar-1.1.4/allstar/__init__.py
--rw-rw-rw-   0        0        0        0 2023-03-31 23:52:40.000000 allstar-1.1.4/allstar/__main__.py
--rw-rw-rw-   0        0        0     7850 2023-04-04 04:17:20.000000 allstar-1.1.4/allstar/star.py
-drwxrwxrwx   0        0        0        0 2023-04-04 04:20:12.899896 allstar-1.1.4/allstar.egg-info/
--rw-rw-rw-   0        0        0     1992 2023-04-04 04:20:12.000000 allstar-1.1.4/allstar.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      212 2023-04-04 04:20:12.000000 allstar-1.1.4/allstar.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-04 04:20:12.000000 allstar-1.1.4/allstar.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0        8 2023-04-04 04:20:12.000000 allstar-1.1.4/allstar.egg-info/top_level.txt
--rw-rw-rw-   0        0        0      636 2023-04-04 04:17:50.000000 allstar-1.1.4/pyproject.toml
--rw-rw-rw-   0        0        0     1436 2023-04-01 01:44:56.000000 allstar-1.1.4/readme.md
--rw-rw-rw-   0        0        0       42 2023-04-04 04:20:12.902897 allstar-1.1.4/setup.cfg
+drwxrwxrwx   0        0        0        0 2023-04-06 17:38:37.293414 allstar-1.1.5/
+-rw-rw-rw-   0        0        0     1089 2023-04-01 00:02:21.000000 allstar-1.1.5/LICENSE
+-rw-rw-rw-   0        0        0     3375 2023-04-06 17:38:37.291414 allstar-1.1.5/PKG-INFO
+drwxrwxrwx   0        0        0        0 2023-04-06 17:38:37.275416 allstar-1.1.5/allstar/
+-rw-rw-rw-   0        0        0       22 2023-04-01 01:16:06.000000 allstar-1.1.5/allstar/__init__.py
+-rw-rw-rw-   0        0        0        0 2023-03-31 23:52:40.000000 allstar-1.1.5/allstar/__main__.py
+-rw-rw-rw-   0        0        0     9241 2023-04-06 17:35:25.000000 allstar-1.1.5/allstar/star.py
+drwxrwxrwx   0        0        0        0 2023-04-06 17:38:37.288453 allstar-1.1.5/allstar.egg-info/
+-rw-rw-rw-   0        0        0     3375 2023-04-06 17:38:37.000000 allstar-1.1.5/allstar.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      212 2023-04-06 17:38:37.000000 allstar-1.1.5/allstar.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-06 17:38:37.000000 allstar-1.1.5/allstar.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0        8 2023-04-06 17:38:37.000000 allstar-1.1.5/allstar.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0      636 2023-04-06 17:36:21.000000 allstar-1.1.5/pyproject.toml
+-rw-rw-rw-   0        0        0     2821 2023-04-06 17:34:57.000000 allstar-1.1.5/readme.md
+-rw-rw-rw-   0        0        0       42 2023-04-06 17:38:37.293414 allstar-1.1.5/setup.cfg
```

### Comparing `allstar-1.1.4/LICENSE` & `allstar-1.1.5/LICENSE`

 * *Files identical despite different names*

### Comparing `allstar-1.1.4/pyproject.toml` & `allstar-1.1.5/pyproject.toml`

 * *Files 2% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 [build-system]
 requires = ["setuptools>=62.0"]
 build-backend = "setuptools.build_meta"
 
 [project]
 name = "allstar"
-version = "1.1.4"
+version = "1.1.5"
 authors = [
   { name="Virtual Items", email="virtualitemsuniverse@gmail.com" },
 ]
 description = "A Python manager for the modules __all__ variable."
 readme = "readme.md"
 requires-python = ">=3.7"
 classifiers = [
```

