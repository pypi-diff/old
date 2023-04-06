# Comparing `tmp/async_rmq-0.2.1.tar.gz` & `tmp/async_rmq-0.2.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "async_rmq-0.2.1.tar", last modified: Tue Apr  4 10:24:16 2023, max compression
+gzip compressed data, was "async_rmq-0.2.2.tar", last modified: Thu Apr  6 09:04:58 2023, max compression
```

## Comparing `async_rmq-0.2.1.tar` & `async_rmq-0.2.2.tar`

### file list

```diff
@@ -1,16 +1,16 @@
-drwxrwxrwx   0        0        0        0 2023-04-04 10:24:16.785838 async_rmq-0.2.1/
--rw-rw-rw-   0        0        0      162 2023-04-04 10:24:16.785838 async_rmq-0.2.1/PKG-INFO
--rw-rw-rw-   0        0        0     1039 2023-02-22 10:40:51.000000 async_rmq-0.2.1/README.md
-drwxrwxrwx   0        0        0        0 2023-04-04 10:24:16.766833 async_rmq-0.2.1/async_rmq/
--rw-rw-rw-   0        0        0        0 2023-01-30 13:24:34.000000 async_rmq-0.2.1/async_rmq/_init_.py
--rw-rw-rw-   0        0        0     2439 2023-03-15 10:40:00.000000 async_rmq-0.2.1/async_rmq/abstract_rmq_consumer.py
--rw-rw-rw-   0        0        0     1661 2023-04-03 13:09:23.000000 async_rmq-0.2.1/async_rmq/consumer_threading.py
--rw-rw-rw-   0        0        0     6227 2023-04-04 10:18:14.000000 async_rmq-0.2.1/async_rmq/rmq_functions.py
-drwxrwxrwx   0        0        0        0 2023-04-04 10:24:16.783832 async_rmq-0.2.1/async_rmq.egg-info/
--rw-rw-rw-   0        0        0      162 2023-04-04 10:24:16.000000 async_rmq-0.2.1/async_rmq.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      306 2023-04-04 10:24:16.000000 async_rmq-0.2.1/async_rmq.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-04 10:24:16.000000 async_rmq-0.2.1/async_rmq.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0        2 2023-02-20 13:54:08.000000 async_rmq-0.2.1/async_rmq.egg-info/not-zip-safe
--rw-rw-rw-   0        0        0       10 2023-04-04 10:24:16.000000 async_rmq-0.2.1/async_rmq.egg-info/top_level.txt
--rw-rw-rw-   0        0        0       42 2023-04-04 10:24:16.789836 async_rmq-0.2.1/setup.cfg
--rw-rw-rw-   0        0        0      259 2023-04-04 10:23:27.000000 async_rmq-0.2.1/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-06 09:04:58.695357 async_rmq-0.2.2/
+-rw-rw-rw-   0        0        0      162 2023-04-06 09:04:58.695357 async_rmq-0.2.2/PKG-INFO
+-rw-rw-rw-   0        0        0     1039 2023-02-22 10:40:51.000000 async_rmq-0.2.2/README.md
+drwxrwxrwx   0        0        0        0 2023-04-06 09:04:58.682390 async_rmq-0.2.2/async_rmq/
+-rw-rw-rw-   0        0        0        0 2023-01-30 13:24:34.000000 async_rmq-0.2.2/async_rmq/_init_.py
+-rw-rw-rw-   0        0        0     2439 2023-03-15 10:40:00.000000 async_rmq-0.2.2/async_rmq/abstract_rmq_consumer.py
+-rw-rw-rw-   0        0        0     1661 2023-04-06 09:04:12.000000 async_rmq-0.2.2/async_rmq/consumer_threading.py
+-rw-rw-rw-   0        0        0     6522 2023-04-06 08:56:37.000000 async_rmq-0.2.2/async_rmq/rmq_functions.py
+drwxrwxrwx   0        0        0        0 2023-04-06 09:04:58.694393 async_rmq-0.2.2/async_rmq.egg-info/
+-rw-rw-rw-   0        0        0      162 2023-04-06 09:04:58.000000 async_rmq-0.2.2/async_rmq.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      306 2023-04-06 09:04:58.000000 async_rmq-0.2.2/async_rmq.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-06 09:04:58.000000 async_rmq-0.2.2/async_rmq.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0        2 2023-02-20 13:54:08.000000 async_rmq-0.2.2/async_rmq.egg-info/not-zip-safe
+-rw-rw-rw-   0        0        0       10 2023-04-06 09:04:58.000000 async_rmq-0.2.2/async_rmq.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0       42 2023-04-06 09:04:58.697393 async_rmq-0.2.2/setup.cfg
+-rw-rw-rw-   0        0        0      259 2023-04-06 09:04:48.000000 async_rmq-0.2.2/setup.py
```

### Comparing `async_rmq-0.2.1/README.md` & `async_rmq-0.2.2/README.md`

 * *Files identical despite different names*

### Comparing `async_rmq-0.2.1/async_rmq/abstract_rmq_consumer.py` & `async_rmq-0.2.2/async_rmq/abstract_rmq_consumer.py`

 * *Files identical despite different names*

### Comparing `async_rmq-0.2.1/async_rmq/consumer_threading.py` & `async_rmq-0.2.2/async_rmq/consumer_threading.py`

 * *Files identical despite different names*

### Comparing `async_rmq-0.2.1/async_rmq/rmq_functions.py` & `async_rmq-0.2.2/async_rmq/rmq_functions.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,14 +1,15 @@
 import json
 import base64
 import asyncio
 import aio_pika
 import logging
 import copy
 from typing import Optional
+from aiormq.exceptions import ChannelNotFoundEntity
 from aio_pika import Channel, Queue, Exchange, ExchangeType
 import constants.rmq_config as rmq_config
 from .abstract_rmq_consumer import RabbitMQConsumer
 
 logger = logging.getLogger("async_rmq")
 
 
@@ -120,20 +121,27 @@
         port=port,
         login=login,
         password=password,
         virtualhost=vhost
     )
     async with connection:
         channel = await connection.channel()
-        exchange = await channel.get_exchange(exchange_name)
-        msg = aio_pika.Message(body=msg_data)
-        await exchange.publish(
-            msg,
-            routing_key=routing_key
-        )
+
+        try:
+            exchange = await channel.get_exchange(exchange_name)
+            msg = aio_pika.Message(body=msg_data)
+            await exchange.publish(
+                msg,
+                routing_key=routing_key
+            )
+
+        except ChannelNotFoundEntity:
+            logger.warning("The message could not be sent because the exchange with the name '%s' was not found"
+                           % exchange_name)
+
 
 def get_exchange_type(s):
     if s == ExchangeType.DIRECT.value:
         return ExchangeType.DIRECT
     elif s == ExchangeType.TOPIC.value:
         return ExchangeType.TOPIC
     elif s == ExchangeType.FANOUT.value:
```

