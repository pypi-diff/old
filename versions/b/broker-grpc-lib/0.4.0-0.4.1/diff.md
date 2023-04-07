# Comparing `tmp/broker_grpc_lib-0.4.0.tar.gz` & `tmp/broker_grpc_lib-0.4.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "broker_grpc_lib-0.4.0.tar", last modified: Fri Apr  7 05:47:41 2023, max compression
+gzip compressed data, was "broker_grpc_lib-0.4.1.tar", last modified: Fri Apr  7 05:59:49 2023, max compression
```

## Comparing `broker_grpc_lib-0.4.0.tar` & `broker_grpc_lib-0.4.1.tar`

### file list

```diff
@@ -1,34 +1,34 @@
-drwxr-xr-x   0 evgenykond   (501) staff       (20)        0 2023-04-07 05:47:41.884626 broker_grpc_lib-0.4.0/
--rw-r--r--   0 evgenykond   (501) staff       (20)      462 2023-04-07 05:47:41.884467 broker_grpc_lib-0.4.0/PKG-INFO
--rw-r--r--   0 evgenykond   (501) staff       (20)      578 2023-04-06 07:45:45.000000 broker_grpc_lib-0.4.0/README.md
-drwxr-xr-x   0 evgenykond   (501) staff       (20)        0 2023-04-07 05:47:41.880032 broker_grpc_lib-0.4.0/broker_grpc_lib/
--rw-r--r--   0 evgenykond   (501) staff       (20)      284 2023-04-03 07:54:32.000000 broker_grpc_lib-0.4.0/broker_grpc_lib/__init__.py
-drwxr-xr-x   0 evgenykond   (501) staff       (20)        0 2023-04-07 05:47:41.881363 broker_grpc_lib-0.4.0/broker_grpc_lib/exc/
--rw-r--r--   0 evgenykond   (501) staff       (20)      152 2023-03-31 07:43:54.000000 broker_grpc_lib-0.4.0/broker_grpc_lib/exc/__init__.py
--rw-r--r--   0 evgenykond   (501) staff       (20)      153 2023-03-31 07:43:54.000000 broker_grpc_lib-0.4.0/broker_grpc_lib/exc/no_queue_exception.py
-drwxr-xr-x   0 evgenykond   (501) staff       (20)        0 2023-04-07 05:47:41.882387 broker_grpc_lib-0.4.0/broker_grpc_lib/lib/
--rw-r--r--   0 evgenykond   (501) staff       (20)      205 2023-04-03 07:50:47.000000 broker_grpc_lib-0.4.0/broker_grpc_lib/lib/__init__.py
--rw-r--r--   0 evgenykond   (501) staff       (20)     1521 2023-04-03 08:03:27.000000 broker_grpc_lib-0.4.0/broker_grpc_lib/lib/broker_handler.py
--rw-r--r--   0 evgenykond   (501) staff       (20)      808 2023-04-05 08:36:30.000000 broker_grpc_lib-0.4.0/broker_grpc_lib/lib/grpc_client.py
--rw-r--r--   0 evgenykond   (501) staff       (20)     6085 2023-04-07 05:43:53.000000 broker_grpc_lib-0.4.0/broker_grpc_lib/lib/rabbitmq_handler.py
-drwxr-xr-x   0 evgenykond   (501) staff       (20)        0 2023-04-07 05:47:41.880937 broker_grpc_lib-0.4.0/broker_grpc_lib.egg-info/
--rw-r--r--   0 evgenykond   (501) staff       (20)      462 2023-04-07 05:47:41.000000 broker_grpc_lib-0.4.0/broker_grpc_lib.egg-info/PKG-INFO
--rw-r--r--   0 evgenykond   (501) staff       (20)      726 2023-04-07 05:47:41.000000 broker_grpc_lib-0.4.0/broker_grpc_lib.egg-info/SOURCES.txt
--rw-r--r--   0 evgenykond   (501) staff       (20)        1 2023-04-07 05:47:41.000000 broker_grpc_lib-0.4.0/broker_grpc_lib.egg-info/dependency_links.txt
--rw-r--r--   0 evgenykond   (501) staff       (20)       48 2023-04-07 05:47:41.000000 broker_grpc_lib-0.4.0/broker_grpc_lib.egg-info/requires.txt
--rw-r--r--   0 evgenykond   (501) staff       (20)       22 2023-04-07 05:47:41.000000 broker_grpc_lib-0.4.0/broker_grpc_lib.egg-info/top_level.txt
--rw-r--r--   0 evgenykond   (501) staff       (20)       38 2023-04-07 05:47:41.884672 broker_grpc_lib-0.4.0/setup.cfg
--rw-r--r--   0 evgenykond   (501) staff       (20)      687 2023-04-07 05:47:35.000000 broker_grpc_lib-0.4.0/setup.py
-drwxr-xr-x   0 evgenykond   (501) staff       (20)        0 2023-04-07 05:47:41.882649 broker_grpc_lib-0.4.0/tests/
--rw-r--r--   0 evgenykond   (501) staff       (20)        0 2023-03-31 08:10:22.000000 broker_grpc_lib-0.4.0/tests/__init__.py
-drwxr-xr-x   0 evgenykond   (501) staff       (20)        0 2023-04-07 05:47:41.882890 broker_grpc_lib-0.4.0/tests/functional/
--rw-r--r--   0 evgenykond   (501) staff       (20)        0 2023-04-06 07:09:07.000000 broker_grpc_lib-0.4.0/tests/functional/__init__.py
--rw-r--r--   0 evgenykond   (501) staff       (20)        0 2023-04-06 07:12:35.000000 broker_grpc_lib-0.4.0/tests/functional/test_rabbitmq_handler.py
-drwxr-xr-x   0 evgenykond   (501) staff       (20)        0 2023-04-07 05:47:41.883418 broker_grpc_lib-0.4.0/tests/helpers/
--rw-r--r--   0 evgenykond   (501) staff       (20)        0 2023-04-06 06:23:34.000000 broker_grpc_lib-0.4.0/tests/helpers/__init__.py
--rw-r--r--   0 evgenykond   (501) staff       (20)      323 2023-04-06 07:11:07.000000 broker_grpc_lib-0.4.0/tests/helpers/async_iterator.py
--rw-r--r--   0 evgenykond   (501) staff       (20)        0 2023-04-06 09:03:49.000000 broker_grpc_lib-0.4.0/tests/helpers/grpc_stub.py
-drwxr-xr-x   0 evgenykond   (501) staff       (20)        0 2023-04-07 05:47:41.883935 broker_grpc_lib-0.4.0/tests/units/
--rw-r--r--   0 evgenykond   (501) staff       (20)        0 2023-04-04 08:55:35.000000 broker_grpc_lib-0.4.0/tests/units/__init__.py
--rw-r--r--   0 evgenykond   (501) staff       (20)     2255 2023-04-05 11:45:02.000000 broker_grpc_lib-0.4.0/tests/units/test_grpc_client.py
--rw-r--r--   0 evgenykond   (501) staff       (20)    19569 2023-04-06 07:11:07.000000 broker_grpc_lib-0.4.0/tests/units/test_rabbitmq_handler.py
+drwxr-xr-x   0 evgenykond   (501) staff       (20)        0 2023-04-07 05:59:49.090408 broker_grpc_lib-0.4.1/
+-rw-r--r--   0 evgenykond   (501) staff       (20)      462 2023-04-07 05:59:49.090244 broker_grpc_lib-0.4.1/PKG-INFO
+-rw-r--r--   0 evgenykond   (501) staff       (20)      578 2023-04-06 07:45:45.000000 broker_grpc_lib-0.4.1/README.md
+drwxr-xr-x   0 evgenykond   (501) staff       (20)        0 2023-04-07 05:59:49.085889 broker_grpc_lib-0.4.1/broker_grpc_lib/
+-rw-r--r--   0 evgenykond   (501) staff       (20)      284 2023-04-03 07:54:32.000000 broker_grpc_lib-0.4.1/broker_grpc_lib/__init__.py
+drwxr-xr-x   0 evgenykond   (501) staff       (20)        0 2023-04-07 05:59:49.087224 broker_grpc_lib-0.4.1/broker_grpc_lib/exc/
+-rw-r--r--   0 evgenykond   (501) staff       (20)      152 2023-03-31 07:43:54.000000 broker_grpc_lib-0.4.1/broker_grpc_lib/exc/__init__.py
+-rw-r--r--   0 evgenykond   (501) staff       (20)      153 2023-03-31 07:43:54.000000 broker_grpc_lib-0.4.1/broker_grpc_lib/exc/no_queue_exception.py
+drwxr-xr-x   0 evgenykond   (501) staff       (20)        0 2023-04-07 05:59:49.088290 broker_grpc_lib-0.4.1/broker_grpc_lib/lib/
+-rw-r--r--   0 evgenykond   (501) staff       (20)      205 2023-04-03 07:50:47.000000 broker_grpc_lib-0.4.1/broker_grpc_lib/lib/__init__.py
+-rw-r--r--   0 evgenykond   (501) staff       (20)     1521 2023-04-03 08:03:27.000000 broker_grpc_lib-0.4.1/broker_grpc_lib/lib/broker_handler.py
+-rw-r--r--   0 evgenykond   (501) staff       (20)      808 2023-04-05 08:36:30.000000 broker_grpc_lib-0.4.1/broker_grpc_lib/lib/grpc_client.py
+-rw-r--r--   0 evgenykond   (501) staff       (20)     6024 2023-04-07 05:59:37.000000 broker_grpc_lib-0.4.1/broker_grpc_lib/lib/rabbitmq_handler.py
+drwxr-xr-x   0 evgenykond   (501) staff       (20)        0 2023-04-07 05:59:49.086780 broker_grpc_lib-0.4.1/broker_grpc_lib.egg-info/
+-rw-r--r--   0 evgenykond   (501) staff       (20)      462 2023-04-07 05:59:49.000000 broker_grpc_lib-0.4.1/broker_grpc_lib.egg-info/PKG-INFO
+-rw-r--r--   0 evgenykond   (501) staff       (20)      726 2023-04-07 05:59:49.000000 broker_grpc_lib-0.4.1/broker_grpc_lib.egg-info/SOURCES.txt
+-rw-r--r--   0 evgenykond   (501) staff       (20)        1 2023-04-07 05:59:49.000000 broker_grpc_lib-0.4.1/broker_grpc_lib.egg-info/dependency_links.txt
+-rw-r--r--   0 evgenykond   (501) staff       (20)       48 2023-04-07 05:59:49.000000 broker_grpc_lib-0.4.1/broker_grpc_lib.egg-info/requires.txt
+-rw-r--r--   0 evgenykond   (501) staff       (20)       22 2023-04-07 05:59:49.000000 broker_grpc_lib-0.4.1/broker_grpc_lib.egg-info/top_level.txt
+-rw-r--r--   0 evgenykond   (501) staff       (20)       38 2023-04-07 05:59:49.090457 broker_grpc_lib-0.4.1/setup.cfg
+-rw-r--r--   0 evgenykond   (501) staff       (20)      687 2023-04-07 05:59:46.000000 broker_grpc_lib-0.4.1/setup.py
+drwxr-xr-x   0 evgenykond   (501) staff       (20)        0 2023-04-07 05:59:49.088449 broker_grpc_lib-0.4.1/tests/
+-rw-r--r--   0 evgenykond   (501) staff       (20)        0 2023-03-31 08:10:22.000000 broker_grpc_lib-0.4.1/tests/__init__.py
+drwxr-xr-x   0 evgenykond   (501) staff       (20)        0 2023-04-07 05:59:49.088706 broker_grpc_lib-0.4.1/tests/functional/
+-rw-r--r--   0 evgenykond   (501) staff       (20)        0 2023-04-06 07:09:07.000000 broker_grpc_lib-0.4.1/tests/functional/__init__.py
+-rw-r--r--   0 evgenykond   (501) staff       (20)        0 2023-04-06 07:12:35.000000 broker_grpc_lib-0.4.1/tests/functional/test_rabbitmq_handler.py
+drwxr-xr-x   0 evgenykond   (501) staff       (20)        0 2023-04-07 05:59:49.089261 broker_grpc_lib-0.4.1/tests/helpers/
+-rw-r--r--   0 evgenykond   (501) staff       (20)        0 2023-04-06 06:23:34.000000 broker_grpc_lib-0.4.1/tests/helpers/__init__.py
+-rw-r--r--   0 evgenykond   (501) staff       (20)      323 2023-04-06 07:11:07.000000 broker_grpc_lib-0.4.1/tests/helpers/async_iterator.py
+-rw-r--r--   0 evgenykond   (501) staff       (20)        0 2023-04-06 09:03:49.000000 broker_grpc_lib-0.4.1/tests/helpers/grpc_stub.py
+drwxr-xr-x   0 evgenykond   (501) staff       (20)        0 2023-04-07 05:59:49.089815 broker_grpc_lib-0.4.1/tests/units/
+-rw-r--r--   0 evgenykond   (501) staff       (20)        0 2023-04-04 08:55:35.000000 broker_grpc_lib-0.4.1/tests/units/__init__.py
+-rw-r--r--   0 evgenykond   (501) staff       (20)     2255 2023-04-05 11:45:02.000000 broker_grpc_lib-0.4.1/tests/units/test_grpc_client.py
+-rw-r--r--   0 evgenykond   (501) staff       (20)    19569 2023-04-06 07:11:07.000000 broker_grpc_lib-0.4.1/tests/units/test_rabbitmq_handler.py
```

### Comparing `broker_grpc_lib-0.4.0/README.md` & `broker_grpc_lib-0.4.1/README.md`

 * *Files identical despite different names*

### Comparing `broker_grpc_lib-0.4.0/broker_grpc_lib/lib/broker_handler.py` & `broker_grpc_lib-0.4.1/broker_grpc_lib/lib/broker_handler.py`

 * *Files identical despite different names*

### Comparing `broker_grpc_lib-0.4.0/broker_grpc_lib/lib/grpc_client.py` & `broker_grpc_lib-0.4.1/broker_grpc_lib/lib/grpc_client.py`

 * *Files identical despite different names*

### Comparing `broker_grpc_lib-0.4.0/broker_grpc_lib/lib/rabbitmq_handler.py` & `broker_grpc_lib-0.4.1/broker_grpc_lib/lib/rabbitmq_handler.py`

 * *Files 1% similar despite different names*

```diff
@@ -13,15 +13,14 @@
 import grpc
 
 from pydantic.error_wrappers import ValidationError
 from typing import Any, Type, Union
 
 import logging
 logging.basicConfig(level=logging.INFO)
-logging.getLogger("aio_pika.connect_robust").disabled = True
 
 
 class RabbitMQHandler(BrokerHandler):
 
     def __init__(
             self,
             host: str,
```

### Comparing `broker_grpc_lib-0.4.0/broker_grpc_lib.egg-info/SOURCES.txt` & `broker_grpc_lib-0.4.1/broker_grpc_lib.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `broker_grpc_lib-0.4.0/setup.py` & `broker_grpc_lib-0.4.1/setup.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 from setuptools import setup, find_packages
 
 
 setup(
     name="broker_grpc_lib",
-    version="0.4.0",
+    version="0.4.1",
     description="Python package for easier use message brokers with gRPC application",
     author="multiadmin_optimus_prime",
     author_email="evgenykond@gmail.com",
     packages=find_packages(),
     install_requires=[
         "pydantic>=1.10.4",
         "aio-pika>=9.0.5",
```

### Comparing `broker_grpc_lib-0.4.0/tests/units/test_grpc_client.py` & `broker_grpc_lib-0.4.1/tests/units/test_grpc_client.py`

 * *Files identical despite different names*

### Comparing `broker_grpc_lib-0.4.0/tests/units/test_rabbitmq_handler.py` & `broker_grpc_lib-0.4.1/tests/units/test_rabbitmq_handler.py`

 * *Files identical despite different names*

