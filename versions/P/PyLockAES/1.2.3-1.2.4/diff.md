# Comparing `tmp/PyLockAES-1.2.3.tar.gz` & `tmp/PyLockAES-1.2.4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "PyLockAES-1.2.3.tar", last modified: Thu Apr  6 11:18:10 2023, max compression
+gzip compressed data, was "PyLockAES-1.2.4.tar", last modified: Thu Apr  6 11:27:12 2023, max compression
```

## Comparing `PyLockAES-1.2.3.tar` & `PyLockAES-1.2.4.tar`

### file list

```diff
@@ -1,12 +1,12 @@
-drwxrwxr-x   0 leonardo  (1000) leonardo  (1000)        0 2023-04-06 11:18:10.716941 PyLockAES-1.2.3/
--rw-rw-r--   0 leonardo  (1000) leonardo  (1000)      160 2023-04-06 11:18:10.712941 PyLockAES-1.2.3/PKG-INFO
-drwxrwxr-x   0 leonardo  (1000) leonardo  (1000)        0 2023-04-06 11:18:10.712941 PyLockAES-1.2.3/PyLockAES.egg-info/
--rw-rw-r--   0 leonardo  (1000) leonardo  (1000)      160 2023-04-06 11:18:10.000000 PyLockAES-1.2.3/PyLockAES.egg-info/PKG-INFO
--rw-rw-r--   0 leonardo  (1000) leonardo  (1000)      191 2023-04-06 11:18:10.000000 PyLockAES-1.2.3/PyLockAES.egg-info/SOURCES.txt
--rw-rw-r--   0 leonardo  (1000) leonardo  (1000)        1 2023-04-06 11:18:10.000000 PyLockAES-1.2.3/PyLockAES.egg-info/dependency_links.txt
--rw-rw-r--   0 leonardo  (1000) leonardo  (1000)       10 2023-04-06 11:18:10.000000 PyLockAES-1.2.3/PyLockAES.egg-info/top_level.txt
-drwxrwxr-x   0 leonardo  (1000) leonardo  (1000)        0 2023-04-06 11:18:10.712941 PyLockAES-1.2.3/pylockaes/
--rw-rw-r--   0 leonardo  (1000) leonardo  (1000)     1838 2023-04-06 11:16:55.000000 PyLockAES-1.2.3/pylockaes/__init__.py
--rw-rw-r--   0 leonardo  (1000) leonardo  (1000)     1838 2023-04-06 11:18:07.000000 PyLockAES-1.2.3/pylockaes/encrypt_decrypt.py
--rw-rw-r--   0 leonardo  (1000) leonardo  (1000)       38 2023-04-06 11:18:10.716941 PyLockAES-1.2.3/setup.cfg
--rw-rw-r--   0 leonardo  (1000) leonardo  (1000)      237 2023-04-06 11:18:07.000000 PyLockAES-1.2.3/setup.py
+drwxrwxr-x   0 leonardo  (1000) leonardo  (1000)        0 2023-04-06 11:27:12.263233 PyLockAES-1.2.4/
+-rw-rw-r--   0 leonardo  (1000) leonardo  (1000)      160 2023-04-06 11:27:12.259232 PyLockAES-1.2.4/PKG-INFO
+drwxrwxr-x   0 leonardo  (1000) leonardo  (1000)        0 2023-04-06 11:27:12.259232 PyLockAES-1.2.4/PyLockAES.egg-info/
+-rw-rw-r--   0 leonardo  (1000) leonardo  (1000)      160 2023-04-06 11:27:11.000000 PyLockAES-1.2.4/PyLockAES.egg-info/PKG-INFO
+-rw-rw-r--   0 leonardo  (1000) leonardo  (1000)      191 2023-04-06 11:27:12.000000 PyLockAES-1.2.4/PyLockAES.egg-info/SOURCES.txt
+-rw-rw-r--   0 leonardo  (1000) leonardo  (1000)        1 2023-04-06 11:27:11.000000 PyLockAES-1.2.4/PyLockAES.egg-info/dependency_links.txt
+-rw-rw-r--   0 leonardo  (1000) leonardo  (1000)       10 2023-04-06 11:27:11.000000 PyLockAES-1.2.4/PyLockAES.egg-info/top_level.txt
+drwxrwxr-x   0 leonardo  (1000) leonardo  (1000)        0 2023-04-06 11:27:12.259232 PyLockAES-1.2.4/pylockaes/
+-rw-rw-r--   0 leonardo  (1000) leonardo  (1000)     1248 2023-04-06 11:26:45.000000 PyLockAES-1.2.4/pylockaes/__init__.py
+-rw-rw-r--   0 leonardo  (1000) leonardo  (1000)     1247 2023-04-06 11:26:45.000000 PyLockAES-1.2.4/pylockaes/encrypt_decrypt.py
+-rw-rw-r--   0 leonardo  (1000) leonardo  (1000)       38 2023-04-06 11:27:12.263233 PyLockAES-1.2.4/setup.cfg
+-rw-rw-r--   0 leonardo  (1000) leonardo  (1000)      237 2023-04-06 11:27:08.000000 PyLockAES-1.2.4/setup.py
```

