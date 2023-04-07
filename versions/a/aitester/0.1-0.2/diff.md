# Comparing `tmp/aitester-0.1.tar.gz` & `tmp/aitester-0.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "aitester-0.1.tar", last modified: Thu Apr  6 20:17:56 2023, max compression
+gzip compressed data, was "aitester-0.2.tar", last modified: Fri Apr  7 09:37:54 2023, max compression
```

## Comparing `aitester-0.1.tar` & `aitester-0.2.tar`

### file list

```diff
@@ -1,17 +1,17 @@
-drwxr-xr-x   0 voidful    (501) staff       (20)        0 2023-04-06 20:17:56.535096 aitester-0.1/
--rw-r--r--   0 voidful    (501) staff       (20)      131 2023-04-06 20:17:56.534949 aitester-0.1/PKG-INFO
--rw-r--r--   0 voidful    (501) staff       (20)     2407 2023-04-06 20:10:22.000000 aitester-0.1/README.md
-drwxr-xr-x   0 voidful    (501) staff       (20)        0 2023-04-06 20:17:56.534013 aitester-0.1/aitest/
--rw-r--r--   0 voidful    (501) staff       (20)       23 2023-04-06 19:53:32.000000 aitester-0.1/aitest/__init__.py
--rw-r--r--   0 voidful    (501) staff       (20)     2804 2023-04-06 19:53:04.000000 aitester-0.1/aitest/config_manager.py
--rw-r--r--   0 voidful    (501) staff       (20)      492 2023-04-06 19:53:04.000000 aitester-0.1/aitest/config_utils.py
--rw-r--r--   0 voidful    (501) staff       (20)     3624 2023-04-06 19:53:32.000000 aitester-0.1/aitest/main.py
-drwxr-xr-x   0 voidful    (501) staff       (20)        0 2023-04-06 20:17:56.534769 aitester-0.1/aitester.egg-info/
--rw-r--r--   0 voidful    (501) staff       (20)      131 2023-04-06 20:17:56.000000 aitester-0.1/aitester.egg-info/PKG-INFO
--rw-r--r--   0 voidful    (501) staff       (20)      294 2023-04-06 20:17:56.000000 aitester-0.1/aitester.egg-info/SOURCES.txt
--rw-r--r--   0 voidful    (501) staff       (20)        1 2023-04-06 20:17:56.000000 aitester-0.1/aitester.egg-info/dependency_links.txt
--rw-r--r--   0 voidful    (501) staff       (20)       92 2023-04-06 20:17:56.000000 aitester-0.1/aitester.egg-info/entry_points.txt
--rw-r--r--   0 voidful    (501) staff       (20)       23 2023-04-06 20:17:56.000000 aitester-0.1/aitester.egg-info/requires.txt
--rw-r--r--   0 voidful    (501) staff       (20)        7 2023-04-06 20:17:56.000000 aitester-0.1/aitester.egg-info/top_level.txt
--rw-r--r--   0 voidful    (501) staff       (20)       38 2023-04-06 20:17:56.535141 aitester-0.1/setup.cfg
--rw-r--r--   0 voidful    (501) staff       (20)      374 2023-04-06 20:17:00.000000 aitester-0.1/setup.py
+drwxr-xr-x   0 voidful    (501) staff       (20)        0 2023-04-07 09:37:54.940472 aitester-0.2/
+-rw-r--r--   0 voidful    (501) staff       (20)      131 2023-04-07 09:37:54.940354 aitester-0.2/PKG-INFO
+-rw-r--r--   0 voidful    (501) staff       (20)     4756 2023-04-07 09:34:48.000000 aitester-0.2/README.md
+drwxr-xr-x   0 voidful    (501) staff       (20)        0 2023-04-07 09:37:54.939451 aitester-0.2/aitester/
+-rw-r--r--   0 voidful    (501) staff       (20)       23 2023-04-06 19:53:32.000000 aitester-0.2/aitester/__init__.py
+-rw-r--r--   0 voidful    (501) staff       (20)     1869 2023-04-07 07:38:13.000000 aitester-0.2/aitester/config_manager.py
+-rw-r--r--   0 voidful    (501) staff       (20)      478 2023-04-06 20:19:57.000000 aitester-0.2/aitester/config_utils.py
+-rw-r--r--   0 voidful    (501) staff       (20)     5036 2023-04-07 09:27:20.000000 aitester-0.2/aitester/main.py
+drwxr-xr-x   0 voidful    (501) staff       (20)        0 2023-04-07 09:37:54.940187 aitester-0.2/aitester.egg-info/
+-rw-r--r--   0 voidful    (501) staff       (20)      131 2023-04-07 09:37:54.000000 aitester-0.2/aitester.egg-info/PKG-INFO
+-rw-r--r--   0 voidful    (501) staff       (20)      302 2023-04-07 09:37:54.000000 aitester-0.2/aitester.egg-info/SOURCES.txt
+-rw-r--r--   0 voidful    (501) staff       (20)        1 2023-04-07 09:37:54.000000 aitester-0.2/aitester.egg-info/dependency_links.txt
+-rw-r--r--   0 voidful    (501) staff       (20)      100 2023-04-07 09:37:54.000000 aitester-0.2/aitester.egg-info/entry_points.txt
+-rw-r--r--   0 voidful    (501) staff       (20)       23 2023-04-07 09:37:54.000000 aitester-0.2/aitester.egg-info/requires.txt
+-rw-r--r--   0 voidful    (501) staff       (20)        9 2023-04-07 09:37:54.000000 aitester-0.2/aitester.egg-info/top_level.txt
+-rw-r--r--   0 voidful    (501) staff       (20)       38 2023-04-07 09:37:54.940525 aitester-0.2/setup.cfg
+-rw-r--r--   0 voidful    (501) staff       (20)      382 2023-04-07 09:37:39.000000 aitester-0.2/setup.py
```

