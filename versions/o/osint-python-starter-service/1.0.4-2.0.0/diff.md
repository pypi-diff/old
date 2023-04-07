# Comparing `tmp/osint-python-starter-service-1.0.4.tar.gz` & `tmp/osint-python-starter-service-2.0.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/osint-python-starter-service-1.0.4.tar", last modified: Mon Sep 12 13:54:34 2022, max compression
+gzip compressed data, was "osint-python-starter-service-2.0.0.tar", last modified: Thu Apr  6 23:57:29 2023, max compression
```

## Comparing `osint-python-starter-service-1.0.4.tar` & `osint-python-starter-service-2.0.0.tar`

### file list

```diff
@@ -1,15 +1,34 @@
-drwxr-xr-x   0 mindpetk  (1000) mindpetk  (1000)        0 2022-09-12 13:54:34.000000 osint-python-starter-service-1.0.4/
--rw-r--r--   0 mindpetk  (1000) mindpetk  (1000)      501 2022-09-12 13:54:34.000000 osint-python-starter-service-1.0.4/PKG-INFO
-drwxr-xr-x   0 mindpetk  (1000) mindpetk  (1000)        0 2022-09-12 13:54:34.000000 osint-python-starter-service-1.0.4/osint_python_starter_service.egg-info/
--rw-r--r--   0 mindpetk  (1000) mindpetk  (1000)       16 2022-09-12 13:54:34.000000 osint-python-starter-service-1.0.4/osint_python_starter_service.egg-info/top_level.txt
--rw-r--r--   0 mindpetk  (1000) mindpetk  (1000)      501 2022-09-12 13:54:34.000000 osint-python-starter-service-1.0.4/osint_python_starter_service.egg-info/PKG-INFO
--rw-r--r--   0 mindpetk  (1000) mindpetk  (1000)       69 2022-09-12 13:54:34.000000 osint-python-starter-service-1.0.4/osint_python_starter_service.egg-info/requires.txt
--rw-r--r--   0 mindpetk  (1000) mindpetk  (1000)        1 2022-09-12 13:54:34.000000 osint-python-starter-service-1.0.4/osint_python_starter_service.egg-info/dependency_links.txt
--rw-r--r--   0 mindpetk  (1000) mindpetk  (1000)      345 2022-09-12 13:54:34.000000 osint-python-starter-service-1.0.4/osint_python_starter_service.egg-info/SOURCES.txt
--rw-r--r--   0 mindpetk  (1000) mindpetk  (1000)       30 2022-06-04 20:59:27.000000 osint-python-starter-service-1.0.4/README.md
-drwxr-xr-x   0 mindpetk  (1000) mindpetk  (1000)        0 2022-09-12 13:54:34.000000 osint-python-starter-service-1.0.4/starter_service/
--rw-r--r--   0 mindpetk  (1000) mindpetk  (1000)        0 2022-06-04 21:05:58.000000 osint-python-starter-service-1.0.4/starter_service/__init__.py
--rw-r--r--   0 mindpetk  (1000) mindpetk  (1000)     5222 2022-09-12 13:52:40.000000 osint-python-starter-service-1.0.4/starter_service/base_service.py
--rw-r--r--   0 mindpetk  (1000) mindpetk  (1000)      778 2022-09-12 13:53:42.000000 osint-python-starter-service-1.0.4/setup.py
--rw-r--r--   0 mindpetk  (1000) mindpetk  (1000)     1064 2022-04-23 22:07:41.000000 osint-python-starter-service-1.0.4/LICENSE
--rw-r--r--   0 mindpetk  (1000) mindpetk  (1000)       38 2022-09-12 13:54:34.000000 osint-python-starter-service-1.0.4/setup.cfg
+drwxr-xr-x   0 mindpetk  (1000) mindpetk  (1000)        0 2023-04-06 23:57:29.128998 osint-python-starter-service-2.0.0/
+-rw-r--r--   0 mindpetk  (1000) mindpetk  (1000)     1064 2022-04-23 22:07:41.000000 osint-python-starter-service-2.0.0/LICENSE
+-rw-r--r--   0 mindpetk  (1000) mindpetk  (1000)      501 2023-04-06 23:57:29.128998 osint-python-starter-service-2.0.0/PKG-INFO
+-rw-r--r--   0 mindpetk  (1000) mindpetk  (1000)       30 2022-06-04 20:59:27.000000 osint-python-starter-service-2.0.0/README.md
+drwxr-xr-x   0 mindpetk  (1000) mindpetk  (1000)        0 2023-04-06 23:57:29.125664 osint-python-starter-service-2.0.0/osint_python_starter_service.egg-info/
+-rw-r--r--   0 mindpetk  (1000) mindpetk  (1000)      501 2023-04-06 23:57:29.000000 osint-python-starter-service-2.0.0/osint_python_starter_service.egg-info/PKG-INFO
+-rw-r--r--   0 mindpetk  (1000) mindpetk  (1000)      925 2023-04-06 23:57:29.000000 osint-python-starter-service-2.0.0/osint_python_starter_service.egg-info/SOURCES.txt
+-rw-r--r--   0 mindpetk  (1000) mindpetk  (1000)        1 2023-04-06 23:57:29.000000 osint-python-starter-service-2.0.0/osint_python_starter_service.egg-info/dependency_links.txt
+-rw-r--r--   0 mindpetk  (1000) mindpetk  (1000)      108 2023-04-06 23:57:29.000000 osint-python-starter-service-2.0.0/osint_python_starter_service.egg-info/requires.txt
+-rw-r--r--   0 mindpetk  (1000) mindpetk  (1000)       16 2023-04-06 23:57:29.000000 osint-python-starter-service-2.0.0/osint_python_starter_service.egg-info/top_level.txt
+-rw-r--r--   0 mindpetk  (1000) mindpetk  (1000)       38 2023-04-06 23:57:29.128998 osint-python-starter-service-2.0.0/setup.cfg
+-rw-r--r--   0 mindpetk  (1000) mindpetk  (1000)      778 2023-04-06 23:45:43.000000 osint-python-starter-service-2.0.0/setup.py
+drwxr-xr-x   0 mindpetk  (1000) mindpetk  (1000)        0 2023-04-06 23:57:29.128998 osint-python-starter-service-2.0.0/starter_service/
+-rw-r--r--   0 mindpetk  (1000) mindpetk  (1000)        0 2022-06-04 21:05:58.000000 osint-python-starter-service-2.0.0/starter_service/__init__.py
+-rw-r--r--   0 mindpetk  (1000) mindpetk  (1000)      973 2023-04-06 22:41:55.000000 osint-python-starter-service-2.0.0/starter_service/api.py
+-rw-r--r--   0 mindpetk  (1000) mindpetk  (1000)     6750 2023-04-06 23:24:14.000000 osint-python-starter-service-2.0.0/starter_service/api_server.py
+-rw-r--r--   0 mindpetk  (1000) mindpetk  (1000)     4731 2023-04-06 18:13:23.000000 osint-python-starter-service-2.0.0/starter_service/avro_parser.py
+-rw-r--r--   0 mindpetk  (1000) mindpetk  (1000)     2735 2023-04-06 23:22:10.000000 osint-python-starter-service-2.0.0/starter_service/base_service.py
+drwxr-xr-x   0 mindpetk  (1000) mindpetk  (1000)        0 2023-04-06 23:57:29.128998 osint-python-starter-service-2.0.0/starter_service/classes/
+-rw-r--r--   0 mindpetk  (1000) mindpetk  (1000)        0 2023-04-04 14:29:02.000000 osint-python-starter-service-2.0.0/starter_service/classes/__init__.py
+-rw-r--r--   0 mindpetk  (1000) mindpetk  (1000)     2569 2023-04-06 23:50:18.000000 osint-python-starter-service-2.0.0/starter_service/classes/article_raw_en.py
+-rw-r--r--   0 mindpetk  (1000) mindpetk  (1000)     2569 2023-04-06 23:50:18.000000 osint-python-starter-service-2.0.0/starter_service/classes/article_raw_lt.py
+-rw-r--r--   0 mindpetk  (1000) mindpetk  (1000)     2569 2023-04-06 23:50:18.000000 osint-python-starter-service-2.0.0/starter_service/classes/article_raw_nl.py
+-rw-r--r--   0 mindpetk  (1000) mindpetk  (1000)     2569 2023-04-06 23:50:18.000000 osint-python-starter-service-2.0.0/starter_service/classes/article_raw_xx.py
+-rw-r--r--   0 mindpetk  (1000) mindpetk  (1000)     1275 2023-04-04 14:58:16.000000 osint-python-starter-service-2.0.0/starter_service/env.py
+drwxr-xr-x   0 mindpetk  (1000) mindpetk  (1000)        0 2023-04-06 23:57:29.128998 osint-python-starter-service-2.0.0/starter_service/examples/
+-rw-r--r--   0 mindpetk  (1000) mindpetk  (1000)        0 2023-03-29 02:03:27.000000 osint-python-starter-service-2.0.0/starter_service/examples/__init__.py
+-rw-r--r--   0 mindpetk  (1000) mindpetk  (1000)      684 2023-04-06 23:48:55.000000 osint-python-starter-service-2.0.0/starter_service/examples/error.py
+-rw-r--r--   0 mindpetk  (1000) mindpetk  (1000)      895 2023-04-06 23:08:31.000000 osint-python-starter-service-2.0.0/starter_service/examples/manual_kafka.py
+-rw-r--r--   0 mindpetk  (1000) mindpetk  (1000)     1281 2023-04-06 23:03:14.000000 osint-python-starter-service-2.0.0/starter_service/examples/multi.py
+-rw-r--r--   0 mindpetk  (1000) mindpetk  (1000)     1030 2023-04-06 23:48:55.000000 osint-python-starter-service-2.0.0/starter_service/examples/single.py
+-rw-r--r--   0 mindpetk  (1000) mindpetk  (1000)     6839 2023-04-06 23:22:10.000000 osint-python-starter-service-2.0.0/starter_service/kafka_adapter.py
+-rw-r--r--   0 mindpetk  (1000) mindpetk  (1000)     1048 2023-04-06 23:52:13.000000 osint-python-starter-service-2.0.0/starter_service/messages.py
+-rw-r--r--   0 mindpetk  (1000) mindpetk  (1000)     6483 2023-04-06 23:52:50.000000 osint-python-starter-service-2.0.0/starter_service/schemas.py
```

### filetype from file(1)

```diff
@@ -1 +1 @@
-POSIX tar archive (GNU)
+POSIX tar archive
```

### Comparing `osint-python-starter-service-1.0.4/setup.py` & `osint-python-starter-service-2.0.0/setup.py`

 * *Files 3% similar despite different names*

```diff
@@ -2,15 +2,15 @@
 
 with open("README.md", "r") as fh:
     long_description = fh.read()
 with open('requirements.txt') as f:
     required = f.read().splitlines()
 setuptools.setup(
     name="osint-python-starter-service",
-    version="1.0.4",
+    version="2.0.0",
     author="mindpetk",
     author_email="petkeviciusm@gmail.com",
     description="Python starter service",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/OSINT-VDU-TNO/python-starter-service",
     include_package_data=True,
```

### Comparing `osint-python-starter-service-1.0.4/LICENSE` & `osint-python-starter-service-2.0.0/LICENSE`

 * *Files identical despite different names*

