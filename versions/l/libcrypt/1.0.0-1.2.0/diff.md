# Comparing `tmp/libcrypt-1.0.0.tar.gz` & `tmp/libcrypt-1.2.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "libcrypt-1.0.0.tar", last modified: Thu Apr  6 20:29:36 2023, max compression
+gzip compressed data, was "libcrypt-1.2.0.tar", last modified: Thu Apr  6 22:17:20 2023, max compression
```

## Comparing `libcrypt-1.0.0.tar` & `libcrypt-1.2.0.tar`

### file list

```diff
@@ -1,11 +1,11 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 20:29:36.398769 libcrypt-1.0.0/
--rw-r--r--   0 root         (0) root         (0)      302 2023-04-06 20:29:36.398769 libcrypt-1.0.0/PKG-INFO
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 20:29:36.398769 libcrypt-1.0.0/libcrypt/
--rw-r--r--   0 root         (0) root         (0)       21 2023-04-06 20:29:35.000000 libcrypt-1.0.0/libcrypt/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 20:29:36.398769 libcrypt-1.0.0/libcrypt.egg-info/
--rw-r--r--   0 root         (0) root         (0)      302 2023-04-06 20:29:36.000000 libcrypt-1.0.0/libcrypt.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)      157 2023-04-06 20:29:36.000000 libcrypt-1.0.0/libcrypt.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2023-04-06 20:29:36.000000 libcrypt-1.0.0/libcrypt.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)        9 2023-04-06 20:29:36.000000 libcrypt-1.0.0/libcrypt.egg-info/top_level.txt
--rw-r--r--   0 root         (0) root         (0)       38 2023-04-06 20:29:36.398769 libcrypt-1.0.0/setup.cfg
--rw-r--r--   0 root         (0) root         (0)      515 2023-04-06 20:29:35.000000 libcrypt-1.0.0/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 22:17:20.818488 libcrypt-1.2.0/
+-rw-r--r--   0 root         (0) root         (0)      420 2023-04-06 22:17:20.818488 libcrypt-1.2.0/PKG-INFO
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 22:17:20.818488 libcrypt-1.2.0/libcrypt/
+-rw-r--r--   0 root         (0) root         (0)    70957 2023-04-06 22:17:20.000000 libcrypt-1.2.0/libcrypt/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 22:17:20.818488 libcrypt-1.2.0/libcrypt.egg-info/
+-rw-r--r--   0 root         (0) root         (0)      420 2023-04-06 22:17:20.000000 libcrypt-1.2.0/libcrypt.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)      157 2023-04-06 22:17:20.000000 libcrypt-1.2.0/libcrypt.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2023-04-06 22:17:20.000000 libcrypt-1.2.0/libcrypt.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)        9 2023-04-06 22:17:20.000000 libcrypt-1.2.0/libcrypt.egg-info/top_level.txt
+-rw-r--r--   0 root         (0) root         (0)       38 2023-04-06 22:17:20.818488 libcrypt-1.2.0/setup.cfg
+-rw-r--r--   0 root         (0) root         (0)      633 2023-04-06 22:17:19.000000 libcrypt-1.2.0/setup.py
```

