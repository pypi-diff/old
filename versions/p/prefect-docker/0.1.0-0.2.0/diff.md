# Comparing `tmp/prefect-docker-0.1.0.tar.gz` & `tmp/prefect-docker-0.2.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "/home/runner/work/prefect-docker/prefect-docker/dist/tmppwu4t6xs/prefect-docker-0.1.0.tar", last modified: Fri Oct 21 16:59:52 2022, max compression
+gzip compressed data, was "/home/runner/work/prefect-docker/prefect-docker/dist/.tmp-1xbtepcy/prefect-docker-0.2.0.tar", last modified: Thu Apr  6 10:45:55 2023, max compression
```

## Comparing `prefect-docker-0.1.0.tar` & `prefect-docker-0.2.0.tar`

### file list

```diff
@@ -1,24 +1,34 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-21 16:59:52.000000 prefect-docker-0.1.0/
--rw-r--r--   0 runner    (1001) docker     (121)    11356 2022-10-21 16:59:10.000000 prefect-docker-0.1.0/LICENSE
--rw-r--r--   0 runner    (1001) docker     (121)      321 2022-10-21 16:59:10.000000 prefect-docker-0.1.0/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (121)     5652 2022-10-21 16:59:52.000000 prefect-docker-0.1.0/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     4754 2022-10-21 16:59:10.000000 prefect-docker-0.1.0/README.md
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-21 16:59:52.000000 prefect-docker-0.1.0/prefect_docker/
--rw-r--r--   0 runner    (1001) docker     (121)      169 2022-10-21 16:59:10.000000 prefect-docker-0.1.0/prefect_docker/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      497 2022-10-21 16:59:52.000000 prefect-docker-0.1.0/prefect_docker/_version.py
--rw-r--r--   0 runner    (1001) docker     (121)     7987 2022-10-21 16:59:10.000000 prefect-docker-0.1.0/prefect_docker/containers.py
--rw-r--r--   0 runner    (1001) docker     (121)     2394 2022-10-21 16:59:10.000000 prefect-docker-0.1.0/prefect_docker/credentials.py
--rw-r--r--   0 runner    (1001) docker     (121)     3857 2022-10-21 16:59:10.000000 prefect-docker-0.1.0/prefect_docker/host.py
--rw-r--r--   0 runner    (1001) docker     (121)     2909 2022-10-21 16:59:10.000000 prefect-docker-0.1.0/prefect_docker/images.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-21 16:59:52.000000 prefect-docker-0.1.0/prefect_docker.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)     5652 2022-10-21 16:59:52.000000 prefect-docker-0.1.0/prefect_docker.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)      491 2022-10-21 16:59:52.000000 prefect-docker-0.1.0/prefect_docker.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-10-21 16:59:52.000000 prefect-docker-0.1.0/prefect_docker.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)       54 2022-10-21 16:59:52.000000 prefect-docker-0.1.0/prefect_docker.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (121)      217 2022-10-21 16:59:52.000000 prefect-docker-0.1.0/prefect_docker.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)       15 2022-10-21 16:59:52.000000 prefect-docker-0.1.0/prefect_docker.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (121)      175 2022-10-21 16:59:10.000000 prefect-docker-0.1.0/requirements-dev.txt
--rw-r--r--   0 runner    (1001) docker     (121)       29 2022-10-21 16:59:10.000000 prefect-docker-0.1.0/requirements.txt
--rw-r--r--   0 runner    (1001) docker     (121)      767 2022-10-21 16:59:52.000000 prefect-docker-0.1.0/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)     1644 2022-10-21 16:59:10.000000 prefect-docker-0.1.0/setup.py
--rw-r--r--   0 runner    (1001) docker     (121)    80049 2022-10-21 16:59:10.000000 prefect-docker-0.1.0/versioneer.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:45:55.000000 prefect-docker-0.2.0/
+-rw-r--r--   0 runner    (1001) docker     (123)    11356 2023-04-06 10:44:28.000000 prefect-docker-0.2.0/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)      321 2023-04-06 10:44:28.000000 prefect-docker-0.2.0/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     5652 2023-04-06 10:45:55.000000 prefect-docker-0.2.0/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     4754 2023-04-06 10:44:28.000000 prefect-docker-0.2.0/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:45:55.000000 prefect-docker-0.2.0/prefect_docker/
+-rw-r--r--   0 runner    (1001) docker     (123)      210 2023-04-06 10:44:28.000000 prefect-docker-0.2.0/prefect_docker/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      497 2023-04-06 10:45:55.000000 prefect-docker-0.2.0/prefect_docker/_version.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8023 2023-04-06 10:44:28.000000 prefect-docker-0.2.0/prefect_docker/containers.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2394 2023-04-06 10:44:28.000000 prefect-docker-0.2.0/prefect_docker/credentials.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3857 2023-04-06 10:44:28.000000 prefect-docker-0.2.0/prefect_docker/host.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2909 2023-04-06 10:44:28.000000 prefect-docker-0.2.0/prefect_docker/images.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:45:55.000000 prefect-docker-0.2.0/prefect_docker/projects/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 10:44:28.000000 prefect-docker-0.2.0/prefect_docker/projects/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5360 2023-04-06 10:44:28.000000 prefect-docker-0.2.0/prefect_docker/projects/steps.py
+-rw-r--r--   0 runner    (1001) docker     (123)    24258 2023-04-06 10:44:28.000000 prefect-docker-0.2.0/prefect_docker/worker.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:45:55.000000 prefect-docker-0.2.0/prefect_docker.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     5652 2023-04-06 10:45:55.000000 prefect-docker-0.2.0/prefect_docker.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      697 2023-04-06 10:45:55.000000 prefect-docker-0.2.0/prefect_docker.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 10:45:55.000000 prefect-docker-0.2.0/prefect_docker.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       54 2023-04-06 10:45:55.000000 prefect-docker-0.2.0/prefect_docker.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      253 2023-04-06 10:45:55.000000 prefect-docker-0.2.0/prefect_docker.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       15 2023-04-06 10:45:55.000000 prefect-docker-0.2.0/prefect_docker.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      211 2023-04-06 10:44:28.000000 prefect-docker-0.2.0/requirements-dev.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       29 2023-04-06 10:44:28.000000 prefect-docker-0.2.0/requirements.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      794 2023-04-06 10:45:55.000000 prefect-docker-0.2.0/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1644 2023-04-06 10:44:28.000000 prefect-docker-0.2.0/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:45:55.000000 prefect-docker-0.2.0/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)     2942 2023-04-06 10:44:28.000000 prefect-docker-0.2.0/tests/test_containers.py
+-rw-r--r--   0 runner    (1001) docker     (123)      391 2023-04-06 10:44:28.000000 prefect-docker-0.2.0/tests/test_credentials.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2705 2023-04-06 10:44:28.000000 prefect-docker-0.2.0/tests/test_host.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2529 2023-04-06 10:44:28.000000 prefect-docker-0.2.0/tests/test_images.py
+-rw-r--r--   0 runner    (1001) docker     (123)    38685 2023-04-06 10:44:28.000000 prefect-docker-0.2.0/tests/test_worker.py
+-rw-r--r--   0 runner    (1001) docker     (123)    80049 2023-04-06 10:44:28.000000 prefect-docker-0.2.0/versioneer.py
```

### Comparing `prefect-docker-0.1.0/LICENSE` & `prefect-docker-0.2.0/LICENSE`

 * *Files identical despite different names*

### Comparing `prefect-docker-0.1.0/PKG-INFO` & `prefect-docker-0.2.0/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: prefect-docker
-Version: 0.1.0
+Version: 0.2.0
 Summary: Prefect integrations for working with Docker
 Home-page: https://github.com/PrefectHQ/prefect-docker
 Author: Prefect Technologies, Inc.
 Author-email: help@prefect.io
 License: Apache License 2.0
 Keywords: prefect
 Classifier: Natural Language :: English
```

### Comparing `prefect-docker-0.1.0/README.md` & `prefect-docker-0.2.0/README.md`

 * *Files identical despite different names*

### Comparing `prefect-docker-0.1.0/prefect_docker/containers.py` & `prefect-docker-0.2.0/prefect_docker/containers.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,11 +1,12 @@
 """Integrations with Docker Containers."""
 
-from typing import Any, Container, Dict, List, Optional, Union
+from typing import Any, Dict, List, Optional, Union
 
+from docker.models.containers import Container
 from prefect import get_run_logger, task
 from prefect.utilities.asyncutils import run_sync_in_worker_thread
 
 from prefect_docker.host import DockerHost
 
 
 @task
```

### Comparing `prefect-docker-0.1.0/prefect_docker/credentials.py` & `prefect-docker-0.2.0/prefect_docker/credentials.py`

 * *Files identical despite different names*

### Comparing `prefect-docker-0.1.0/prefect_docker/host.py` & `prefect-docker-0.2.0/prefect_docker/host.py`

 * *Files identical despite different names*

### Comparing `prefect-docker-0.1.0/prefect_docker/images.py` & `prefect-docker-0.2.0/prefect_docker/images.py`

 * *Files identical despite different names*

### Comparing `prefect-docker-0.1.0/prefect_docker.egg-info/PKG-INFO` & `prefect-docker-0.2.0/prefect_docker.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: prefect-docker
-Version: 0.1.0
+Version: 0.2.0
 Summary: Prefect integrations for working with Docker
 Home-page: https://github.com/PrefectHQ/prefect-docker
 Author: Prefect Technologies, Inc.
 Author-email: help@prefect.io
 License: Apache License 2.0
 Keywords: prefect
 Classifier: Natural Language :: English
```

### Comparing `prefect-docker-0.1.0/setup.cfg` & `prefect-docker-0.2.0/setup.cfg`

 * *Files 14% similar despite different names*

```diff
@@ -25,19 +25,21 @@
 ignore_init_method = True
 exclude = prefect_docker/_version.py, tests, setup.py, versioneer.py, docs, site
 fail-under = 95
 omit-covered-files = True
 
 [coverage:run]
 omit = tests/*, prefect_docker/_version.py
+branch = True
 
 [coverage:report]
 fail_under = 80
 show_missing = True
 
 [tool:pytest]
 asyncio_mode = auto
+timeout = 60
 
 [egg_info]
 tag_build = 
 tag_date = 0
```

### Comparing `prefect-docker-0.1.0/setup.py` & `prefect-docker-0.2.0/setup.py`

 * *Files identical despite different names*

### Comparing `prefect-docker-0.1.0/versioneer.py` & `prefect-docker-0.2.0/versioneer.py`

 * *Files identical despite different names*

