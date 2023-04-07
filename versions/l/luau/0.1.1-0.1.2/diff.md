# Comparing `tmp/luau-0.1.1.tar.gz` & `tmp/luau-0.1.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "luau-0.1.1.tar", last modified: Fri Apr  7 08:11:49 2023, max compression
+gzip compressed data, was "luau-0.1.2.tar", last modified: Fri Apr  7 08:38:25 2023, max compression
```

## Comparing `luau-0.1.1.tar` & `luau-0.1.2.tar`

### file list

```diff
@@ -1,14 +1,13 @@
-drwxrwxrwx   0        0        0        0 2023-04-07 08:11:49.747160 luau-0.1.1/
--rw-rw-rw-   0        0        0    11558 2023-04-07 07:23:56.000000 luau-0.1.1/LICENSE
--rw-rw-rw-   0        0        0      342 2023-04-07 08:11:49.746162 luau-0.1.1/PKG-INFO
--rw-rw-rw-   0        0        0       60 2023-04-07 07:23:56.000000 luau-0.1.1/README.md
-drwxrwxrwx   0        0        0        0 2023-04-07 08:11:49.742177 luau-0.1.1/luau.egg-info/
--rw-rw-rw-   0        0        0      342 2023-04-07 08:11:49.000000 luau-0.1.1/luau.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      181 2023-04-07 08:11:49.000000 luau-0.1.1/luau.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-07 08:11:49.000000 luau-0.1.1/luau.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       10 2023-04-07 08:11:49.000000 luau-0.1.1/luau.egg-info/requires.txt
--rw-rw-rw-   0        0        0        4 2023-04-07 08:11:49.000000 luau-0.1.1/luau.egg-info/top_level.txt
--rw-rw-rw-   0        0        0       42 2023-04-07 08:11:49.747160 luau-0.1.1/setup.cfg
--rw-rw-rw-   0        0        0      480 2023-04-07 08:11:46.000000 luau-0.1.1/setup.py
-drwxrwxrwx   0        0        0        0 2023-04-07 08:11:49.744167 luau-0.1.1/src/
--rw-rw-rw-   0        0        0     4309 2023-04-07 07:25:51.000000 luau-0.1.1/src/__init__.py
+drwxrwxrwx   0        0        0        0 2023-04-07 08:38:25.023844 luau-0.1.2/
+-rw-rw-rw-   0        0        0    11558 2023-04-07 07:23:56.000000 luau-0.1.2/LICENSE
+-rw-rw-rw-   0        0        0      342 2023-04-07 08:38:25.023713 luau-0.1.2/PKG-INFO
+-rw-rw-rw-   0        0        0       60 2023-04-07 07:23:56.000000 luau-0.1.2/README.md
+drwxrwxrwx   0        0        0        0 2023-04-07 08:38:25.020866 luau-0.1.2/luau.egg-info/
+-rw-rw-rw-   0        0        0      342 2023-04-07 08:38:24.000000 luau-0.1.2/luau.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      154 2023-04-07 08:38:24.000000 luau-0.1.2/luau.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-07 08:38:24.000000 luau-0.1.2/luau.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0        4 2023-04-07 08:38:24.000000 luau-0.1.2/luau.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0       42 2023-04-07 08:38:25.024843 luau-0.1.2/setup.cfg
+-rw-rw-rw-   0        0        0      466 2023-04-07 08:38:07.000000 luau-0.1.2/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-07 08:38:25.021864 luau-0.1.2/src/
+-rw-rw-rw-   0        0        0     4309 2023-04-07 07:25:51.000000 luau-0.1.2/src/__init__.py
```

### Comparing `luau-0.1.1/LICENSE` & `luau-0.1.2/LICENSE`

 * *Files identical despite different names*

### Comparing `luau-0.1.1/src/__init__.py` & `luau-0.1.2/src/__init__.py`

 * *Files identical despite different names*

