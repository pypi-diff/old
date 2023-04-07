# Comparing `tmp/fastkafka-0.4.0rc0.tar.gz` & `tmp/fastkafka-0.4.0rc1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "fastkafka-0.4.0rc0.tar", last modified: Fri Apr  7 12:25:08 2023, max compression
+gzip compressed data, was "fastkafka-0.4.0rc1.tar", last modified: Fri Apr  7 14:02:29 2023, max compression
```

## Comparing `fastkafka-0.4.0rc0.tar` & `fastkafka-0.4.0rc1.tar`

### file list

```diff
@@ -1,49 +1,49 @@
-drwxrwxr-x   0 davor     (1000) davor     (1000)        0 2023-04-07 12:25:08.735709 fastkafka-0.4.0rc0/
--rw-r--r--   0 davor     (1000) davor     (1000)    11357 2023-01-25 09:24:15.000000 fastkafka-0.4.0rc0/LICENSE
--rw-r--r--   0 davor     (1000) davor     (1000)      111 2023-01-25 09:24:15.000000 fastkafka-0.4.0rc0/MANIFEST.in
--rw-rw-r--   0 davor     (1000) davor     (1000)    31197 2023-04-07 12:25:08.731709 fastkafka-0.4.0rc0/PKG-INFO
--rw-rw-r--   0 davor     (1000) davor     (1000)    29790 2023-03-27 11:07:38.000000 fastkafka-0.4.0rc0/README.md
-drwxrwxr-x   0 davor     (1000) davor     (1000)        0 2023-04-07 12:25:08.731709 fastkafka-0.4.0rc0/fastkafka/
--rw-rw-r--   0 davor     (1000) davor     (1000)      432 2023-04-07 12:24:04.000000 fastkafka-0.4.0rc0/fastkafka/__init__.py
-drwxrwxr-x   0 davor     (1000) davor     (1000)        0 2023-04-07 12:25:08.731709 fastkafka-0.4.0rc0/fastkafka/_application/
--rw-rw-r--   0 davor     (1000) davor     (1000)        0 2023-04-07 12:24:04.000000 fastkafka-0.4.0rc0/fastkafka/_application/__init__.py
--rw-rw-r--   0 davor     (1000) davor     (1000)    27864 2023-04-07 12:24:03.000000 fastkafka-0.4.0rc0/fastkafka/_application/app.py
--rw-rw-r--   0 davor     (1000) davor     (1000)     7407 2023-04-07 12:24:03.000000 fastkafka-0.4.0rc0/fastkafka/_application/tester.py
--rw-rw-r--   0 davor     (1000) davor     (1000)     1574 2023-04-07 12:24:03.000000 fastkafka-0.4.0rc0/fastkafka/_cli.py
--rw-r--r--   0 davor     (1000) davor     (1000)     3879 2023-04-07 12:24:03.000000 fastkafka-0.4.0rc0/fastkafka/_cli_docs.py
--rw-rw-r--   0 davor     (1000) davor     (1000)      852 2023-04-07 12:24:03.000000 fastkafka-0.4.0rc0/fastkafka/_cli_testing.py
-drwxrwxr-x   0 davor     (1000) davor     (1000)        0 2023-04-07 12:25:08.731709 fastkafka-0.4.0rc0/fastkafka/_components/
--rw-rw-r--   0 davor     (1000) davor     (1000)        0 2023-04-07 12:24:04.000000 fastkafka-0.4.0rc0/fastkafka/_components/__init__.py
--rw-rw-r--   0 davor     (1000) davor     (1000)     3705 2023-04-07 12:24:03.000000 fastkafka-0.4.0rc0/fastkafka/_components/_subprocess.py
--rw-r--r--   0 davor     (1000) davor     (1000)     8769 2023-04-07 12:24:02.000000 fastkafka-0.4.0rc0/fastkafka/_components/aiokafka_consumer_loop.py
--rw-rw-r--   0 davor     (1000) davor     (1000)     2848 2023-04-07 12:24:02.000000 fastkafka-0.4.0rc0/fastkafka/_components/aiokafka_producer_manager.py
--rw-r--r--   0 davor     (1000) davor     (1000)    16362 2023-04-07 12:24:03.000000 fastkafka-0.4.0rc0/fastkafka/_components/asyncapi.py
--rw-rw-r--   0 davor     (1000) davor     (1000)     2940 2023-04-07 12:24:03.000000 fastkafka-0.4.0rc0/fastkafka/_components/benchmarking.py
--rw-r--r--   0 davor     (1000) davor     (1000)     4686 2023-04-07 12:24:04.000000 fastkafka-0.4.0rc0/fastkafka/_components/docs_dependencies.py
--rw-r--r--   0 davor     (1000) davor     (1000)     2639 2023-04-07 12:24:04.000000 fastkafka-0.4.0rc0/fastkafka/_components/helpers.py
--rw-rw-r--   0 davor     (1000) davor     (1000)     3952 2023-04-07 12:24:04.000000 fastkafka-0.4.0rc0/fastkafka/_components/logger.py
--rw-rw-r--   0 davor     (1000) davor     (1000)    12280 2023-04-07 12:24:04.000000 fastkafka-0.4.0rc0/fastkafka/_components/meta.py
--rw-rw-r--   0 davor     (1000) davor     (1000)     3154 2023-04-07 12:24:02.000000 fastkafka-0.4.0rc0/fastkafka/_components/producer_decorator.py
--rw-rw-r--   0 davor     (1000) davor     (1000)     5066 2023-04-07 12:24:04.000000 fastkafka-0.4.0rc0/fastkafka/_components/test_dependencies.py
--rw-r--r--   0 davor     (1000) davor     (1000)    11215 2023-04-07 12:24:03.000000 fastkafka-0.4.0rc0/fastkafka/_docusaurus_helper.py
--rw-r--r--   0 davor     (1000) davor     (1000)    50547 2023-04-07 12:24:04.000000 fastkafka-0.4.0rc0/fastkafka/_helpers.py
--rw-rw-r--   0 davor     (1000) davor     (1000)    66827 2023-04-07 12:24:04.000000 fastkafka-0.4.0rc0/fastkafka/_modidx.py
--rw-rw-r--   0 davor     (1000) davor     (1000)     6039 2023-04-07 12:24:03.000000 fastkafka-0.4.0rc0/fastkafka/_server.py
-drwxrwxr-x   0 davor     (1000) davor     (1000)        0 2023-04-07 12:25:08.731709 fastkafka-0.4.0rc0/fastkafka/_testing/
--rw-rw-r--   0 davor     (1000) davor     (1000)        0 2023-04-07 12:24:04.000000 fastkafka-0.4.0rc0/fastkafka/_testing/__init__.py
--rw-r--r--   0 davor     (1000) davor     (1000)    19775 2023-04-07 12:24:02.000000 fastkafka-0.4.0rc0/fastkafka/_testing/apache_kafka_broker.py
--rw-rw-r--   0 davor     (1000) davor     (1000)    18396 2023-04-07 12:24:02.000000 fastkafka-0.4.0rc0/fastkafka/_testing/in_memory_broker.py
--rw-r--r--   0 davor     (1000) davor     (1000)    12366 2023-04-07 12:24:02.000000 fastkafka-0.4.0rc0/fastkafka/_testing/local_redpanda_broker.py
--rw-r--r--   0 davor     (1000) davor     (1000)     5031 2023-04-07 12:24:02.000000 fastkafka-0.4.0rc0/fastkafka/_testing/test_utils.py
--rw-rw-r--   0 davor     (1000) davor     (1000)      849 2023-04-07 12:24:02.000000 fastkafka-0.4.0rc0/fastkafka/testing.py
-drwxrwxr-x   0 davor     (1000) davor     (1000)        0 2023-04-07 12:25:08.731709 fastkafka-0.4.0rc0/fastkafka.egg-info/
--rw-rw-r--   0 davor     (1000) davor     (1000)    31197 2023-04-07 12:25:08.000000 fastkafka-0.4.0rc0/fastkafka.egg-info/PKG-INFO
--rw-rw-r--   0 davor     (1000) davor     (1000)     1243 2023-04-07 12:25:08.000000 fastkafka-0.4.0rc0/fastkafka.egg-info/SOURCES.txt
--rw-rw-r--   0 davor     (1000) davor     (1000)        1 2023-04-07 12:25:08.000000 fastkafka-0.4.0rc0/fastkafka.egg-info/dependency_links.txt
--rw-rw-r--   0 davor     (1000) davor     (1000)      146 2023-04-07 12:25:08.000000 fastkafka-0.4.0rc0/fastkafka.egg-info/entry_points.txt
--rw-rw-r--   0 davor     (1000) davor     (1000)        1 2023-01-25 09:30:21.000000 fastkafka-0.4.0rc0/fastkafka.egg-info/not-zip-safe
--rw-rw-r--   0 davor     (1000) davor     (1000)      578 2023-04-07 12:25:08.000000 fastkafka-0.4.0rc0/fastkafka.egg-info/requires.txt
--rw-rw-r--   0 davor     (1000) davor     (1000)       10 2023-04-07 12:25:08.000000 fastkafka-0.4.0rc0/fastkafka.egg-info/top_level.txt
--rw-rw-r--   0 davor     (1000) davor     (1000)     1231 2023-04-07 12:22:16.000000 fastkafka-0.4.0rc0/settings.ini
--rw-rw-r--   0 davor     (1000) davor     (1000)       38 2023-04-07 12:25:08.735709 fastkafka-0.4.0rc0/setup.cfg
--rw-r--r--   0 davor     (1000) davor     (1000)     3570 2023-04-07 10:22:05.000000 fastkafka-0.4.0rc0/setup.py
+drwxrwxr-x   0 davor     (1000) davor     (1000)        0 2023-04-07 14:02:29.331369 fastkafka-0.4.0rc1/
+-rw-r--r--   0 davor     (1000) davor     (1000)    11357 2023-01-25 09:24:15.000000 fastkafka-0.4.0rc1/LICENSE
+-rw-r--r--   0 davor     (1000) davor     (1000)      111 2023-01-25 09:24:15.000000 fastkafka-0.4.0rc1/MANIFEST.in
+-rw-rw-r--   0 davor     (1000) davor     (1000)    32291 2023-04-07 14:02:29.331369 fastkafka-0.4.0rc1/PKG-INFO
+-rw-rw-r--   0 davor     (1000) davor     (1000)    30884 2023-04-07 14:01:48.000000 fastkafka-0.4.0rc1/README.md
+drwxrwxr-x   0 davor     (1000) davor     (1000)        0 2023-04-07 14:02:29.331369 fastkafka-0.4.0rc1/fastkafka/
+-rw-rw-r--   0 davor     (1000) davor     (1000)      432 2023-04-07 14:00:35.000000 fastkafka-0.4.0rc1/fastkafka/__init__.py
+drwxrwxr-x   0 davor     (1000) davor     (1000)        0 2023-04-07 14:02:29.331369 fastkafka-0.4.0rc1/fastkafka/_application/
+-rw-rw-r--   0 davor     (1000) davor     (1000)        0 2023-04-07 14:00:35.000000 fastkafka-0.4.0rc1/fastkafka/_application/__init__.py
+-rw-rw-r--   0 davor     (1000) davor     (1000)    27864 2023-04-07 14:00:34.000000 fastkafka-0.4.0rc1/fastkafka/_application/app.py
+-rw-rw-r--   0 davor     (1000) davor     (1000)     7407 2023-04-07 14:00:34.000000 fastkafka-0.4.0rc1/fastkafka/_application/tester.py
+-rw-rw-r--   0 davor     (1000) davor     (1000)     1574 2023-04-07 14:00:34.000000 fastkafka-0.4.0rc1/fastkafka/_cli.py
+-rw-r--r--   0 davor     (1000) davor     (1000)     3879 2023-04-07 14:00:34.000000 fastkafka-0.4.0rc1/fastkafka/_cli_docs.py
+-rw-rw-r--   0 davor     (1000) davor     (1000)      852 2023-04-07 14:00:34.000000 fastkafka-0.4.0rc1/fastkafka/_cli_testing.py
+drwxrwxr-x   0 davor     (1000) davor     (1000)        0 2023-04-07 14:02:29.331369 fastkafka-0.4.0rc1/fastkafka/_components/
+-rw-rw-r--   0 davor     (1000) davor     (1000)        0 2023-04-07 14:00:35.000000 fastkafka-0.4.0rc1/fastkafka/_components/__init__.py
+-rw-rw-r--   0 davor     (1000) davor     (1000)     3705 2023-04-07 14:00:34.000000 fastkafka-0.4.0rc1/fastkafka/_components/_subprocess.py
+-rw-r--r--   0 davor     (1000) davor     (1000)     8769 2023-04-07 14:00:33.000000 fastkafka-0.4.0rc1/fastkafka/_components/aiokafka_consumer_loop.py
+-rw-rw-r--   0 davor     (1000) davor     (1000)     2848 2023-04-07 14:00:33.000000 fastkafka-0.4.0rc1/fastkafka/_components/aiokafka_producer_manager.py
+-rw-r--r--   0 davor     (1000) davor     (1000)    16362 2023-04-07 14:00:34.000000 fastkafka-0.4.0rc1/fastkafka/_components/asyncapi.py
+-rw-rw-r--   0 davor     (1000) davor     (1000)     2940 2023-04-07 14:00:34.000000 fastkafka-0.4.0rc1/fastkafka/_components/benchmarking.py
+-rw-r--r--   0 davor     (1000) davor     (1000)     4686 2023-04-07 14:00:34.000000 fastkafka-0.4.0rc1/fastkafka/_components/docs_dependencies.py
+-rw-r--r--   0 davor     (1000) davor     (1000)     2639 2023-04-07 14:00:35.000000 fastkafka-0.4.0rc1/fastkafka/_components/helpers.py
+-rw-rw-r--   0 davor     (1000) davor     (1000)     3952 2023-04-07 14:00:35.000000 fastkafka-0.4.0rc1/fastkafka/_components/logger.py
+-rw-rw-r--   0 davor     (1000) davor     (1000)    12280 2023-04-07 14:00:34.000000 fastkafka-0.4.0rc1/fastkafka/_components/meta.py
+-rw-rw-r--   0 davor     (1000) davor     (1000)     3154 2023-04-07 14:00:33.000000 fastkafka-0.4.0rc1/fastkafka/_components/producer_decorator.py
+-rw-rw-r--   0 davor     (1000) davor     (1000)     5066 2023-04-07 14:00:35.000000 fastkafka-0.4.0rc1/fastkafka/_components/test_dependencies.py
+-rw-r--r--   0 davor     (1000) davor     (1000)    11215 2023-04-07 14:00:34.000000 fastkafka-0.4.0rc1/fastkafka/_docusaurus_helper.py
+-rw-r--r--   0 davor     (1000) davor     (1000)    50547 2023-04-07 14:00:35.000000 fastkafka-0.4.0rc1/fastkafka/_helpers.py
+-rw-rw-r--   0 davor     (1000) davor     (1000)    66827 2023-04-07 14:00:35.000000 fastkafka-0.4.0rc1/fastkafka/_modidx.py
+-rw-rw-r--   0 davor     (1000) davor     (1000)     6039 2023-04-07 14:00:34.000000 fastkafka-0.4.0rc1/fastkafka/_server.py
+drwxrwxr-x   0 davor     (1000) davor     (1000)        0 2023-04-07 14:02:29.331369 fastkafka-0.4.0rc1/fastkafka/_testing/
+-rw-rw-r--   0 davor     (1000) davor     (1000)        0 2023-04-07 14:00:35.000000 fastkafka-0.4.0rc1/fastkafka/_testing/__init__.py
+-rw-r--r--   0 davor     (1000) davor     (1000)    19775 2023-04-07 14:00:33.000000 fastkafka-0.4.0rc1/fastkafka/_testing/apache_kafka_broker.py
+-rw-rw-r--   0 davor     (1000) davor     (1000)    18396 2023-04-07 14:00:33.000000 fastkafka-0.4.0rc1/fastkafka/_testing/in_memory_broker.py
+-rw-rw-r--   0 davor     (1000) davor     (1000)    12382 2023-04-07 14:00:33.000000 fastkafka-0.4.0rc1/fastkafka/_testing/local_redpanda_broker.py
+-rw-r--r--   0 davor     (1000) davor     (1000)     5031 2023-04-07 14:00:33.000000 fastkafka-0.4.0rc1/fastkafka/_testing/test_utils.py
+-rw-rw-r--   0 davor     (1000) davor     (1000)      849 2023-04-07 14:00:33.000000 fastkafka-0.4.0rc1/fastkafka/testing.py
+drwxrwxr-x   0 davor     (1000) davor     (1000)        0 2023-04-07 14:02:29.331369 fastkafka-0.4.0rc1/fastkafka.egg-info/
+-rw-rw-r--   0 davor     (1000) davor     (1000)    32291 2023-04-07 14:02:29.000000 fastkafka-0.4.0rc1/fastkafka.egg-info/PKG-INFO
+-rw-rw-r--   0 davor     (1000) davor     (1000)     1243 2023-04-07 14:02:29.000000 fastkafka-0.4.0rc1/fastkafka.egg-info/SOURCES.txt
+-rw-rw-r--   0 davor     (1000) davor     (1000)        1 2023-04-07 14:02:29.000000 fastkafka-0.4.0rc1/fastkafka.egg-info/dependency_links.txt
+-rw-rw-r--   0 davor     (1000) davor     (1000)      146 2023-04-07 14:02:29.000000 fastkafka-0.4.0rc1/fastkafka.egg-info/entry_points.txt
+-rw-rw-r--   0 davor     (1000) davor     (1000)        1 2023-01-25 09:30:21.000000 fastkafka-0.4.0rc1/fastkafka.egg-info/not-zip-safe
+-rw-rw-r--   0 davor     (1000) davor     (1000)      578 2023-04-07 14:02:29.000000 fastkafka-0.4.0rc1/fastkafka.egg-info/requires.txt
+-rw-rw-r--   0 davor     (1000) davor     (1000)       10 2023-04-07 14:02:29.000000 fastkafka-0.4.0rc1/fastkafka.egg-info/top_level.txt
+-rw-rw-r--   0 davor     (1000) davor     (1000)     1231 2023-04-07 12:26:13.000000 fastkafka-0.4.0rc1/settings.ini
+-rw-rw-r--   0 davor     (1000) davor     (1000)       38 2023-04-07 14:02:29.331369 fastkafka-0.4.0rc1/setup.cfg
+-rw-r--r--   0 davor     (1000) davor     (1000)     3570 2023-04-07 10:22:05.000000 fastkafka-0.4.0rc1/setup.py
```

### Comparing `fastkafka-0.4.0rc0/LICENSE` & `fastkafka-0.4.0rc1/LICENSE`

 * *Files identical despite different names*

### Comparing `fastkafka-0.4.0rc0/PKG-INFO` & `fastkafka-0.4.0rc1/PKG-INFO`

 * *Files 8% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: fastkafka
-Version: 0.4.0rc0
+Version: 0.4.0rc1
 Summary: FastKafka is a powerful and easy-to-use Python library for building asynchronous web services that interact with Kafka topics. Built on top of FastAPI, Starlette, Pydantic, AIOKafka and AsyncAPI, FastKafka simplifies the process of writing producers and consumers for Kafka topics.
 Home-page: https://github.com/airtai/fastkafka
 Author: airt
 Author-email: info@airt.ai
 License: Apache Software License 2.0
 Project-URL: Bug Tracker, https://github.com/airtai/fastkafka/issues
 Project-URL: CI, https://github.com/airtai/fastkafka/actions
@@ -60,20 +60,30 @@
 With FastKafka, you can quickly prototype and develop high-performance
 Kafka-based services with minimal code, making it an ideal choice for
 developers looking to streamline their workflow and accelerate their
 projects.
 
 ------------------------------------------------------------------------
 
-#### ⭐ Stay in touch
+#### ⭐⭐⭐ Stay in touch ⭐⭐⭐
 
-Please show your support and stay in touch by giving our [GitHub
-repository](https://github.com/airtai/fastkafka/) a star! Your support
-helps us to stay in touch with you and encourages us to continue
-developing and improving the library. Thank you for your support!
+Please show your support and stay in touch by:
+
+- giving our [GitHub repository](https://github.com/airtai/fastkafka/) a
+  star, and
+
+- joining our [Discord server](https://discord.gg/CJWmYpyFbc).
+
+Your support helps us to stay in touch with you and encourages us to
+continue developing and improving the library. Thank you for your
+support!
+
+------------------------------------------------------------------------
+
+#### 🐝🐝🐝 We were busy lately 🐝🐝🐝
 
 ![Activity](https://repobeats.axiom.co/api/embed/21f36049093d5eb8e5fdad18c3c5d8df5428ca30.svg "Repobeats analytics image")
 
 ## Install
 
 FastKafka works on macOS, Linux, and most Unix-style operating systems.
 You can install base version of `fastkafka` with `pip` as usual:
@@ -102,44 +112,54 @@
 
 ## Tutorial
 
 You can start an interactive tutorial in Google Colab by clicking the
 button below:
 
 <a href="https://colab.research.google.com/github/airtai/fastkafka/blob/main/nbs/guides/Guide_00_FastKafka_Demo.ipynb" target=”_blank”>
-<img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab">
+<img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" />
 </a>
 
 ## Writing server code
 
 Here is an example python script using FastKafka that takes data from a
 Kafka topic, makes a prediction using a predictive model, and outputs
 the prediction to another Kafka topic.
 
 ### Preparing the demo model
 
 First we will prepare our model using the Iris dataset so that we can
 demonstrate the predictions using FastKafka. The following call
 downloads the dataset and trains the model.
 
+We will wrap the model creation into a lifespan of our app so that the
+model is created just before the app is started.
+
 ``` python
+from contextlib import asynccontextmanager
+
 from sklearn.datasets import load_iris
 from sklearn.linear_model import LogisticRegression
 
-X, y = load_iris(return_X_y=True)
-model = LogisticRegression(random_state=0, max_iter=500).fit(X, y)
-x = X[[0, 55, -1]]
-print(x)
-print(model.predict(x))
-```
+from fastkafka import FastKafka
+
+ml_models = {}
 
-    [[5.1 3.5 1.4 0.2]
-     [5.7 2.8 4.5 1.3]
-     [5.9 3.  5.1 1.8]]
-    [0 1 2]
+
+@asynccontextmanager
+async def lifespan(app: FastKafka):
+    # Load the ML model
+    X, y = load_iris(return_X_y=True)
+    ml_models["iris_predictor"] = LogisticRegression(random_state=0, max_iter=500).fit(
+        X, y
+    )
+    yield
+    # Clean up the ML models and release the resources
+    ml_models.clear()
+```
 
 ### Messages
 
 FastKafka uses [Pydantic](https://docs.pydantic.dev/) to parse input
 JSON-encoded data into Python objects, making it easy to work with
 structured data in your Kafka-based applications. Pydantic’s
 [`BaseModel`](https://docs.pydantic.dev/usage/models/) class allows you
@@ -193,15 +213,15 @@
 contains two entries: `"localhost"` and `"production"`, specifying local
 development and production Kafka brokers. Each entry specifies the URL,
 port, and other details of a Kafka broker. This dictionary is used for
 both generating the documentation and later to run the actual server
 against one of the given kafka broker.
 
 Next, an object of the
-[`FastKafka`](https://airtai.github.io/fastkafka/0.3.0/api/fastkafka/FastKafka/#fastkafka.FastKafka)
+[`FastKafka`](https://airtai.github.io/fastkafka/0.4.0rc1/api/fastkafka/FastKafka/#fastkafka.FastKafka)
 class is initialized with the minimum set of arguments:
 
 - `kafka_brokers`: a dictionary used for generation of documentation
 
 ``` python
 from fastkafka import FastKafka
 
@@ -219,14 +239,15 @@
         "security": {"type": "plain"},
     },
 }
 
 kafka_app = FastKafka(
     title="Iris predictions",
     kafka_brokers=kafka_brokers,
+    lifespan=lifespan,
 )
 ```
 
 ### Function decorators
 
 FastKafka provides convenient function decorators `@kafka_app.consumes`
 and `@kafka_app.produces` to allow you to delegate the actual process of
@@ -264,15 +285,15 @@
   The framework will call the `IrisPrediction.json().encode("utf-8")`
   function on the returned value and produce it to the specified topic.
 
 ``` python
 @kafka_app.consumes(topic="input_data", auto_offset_reset="latest")
 async def on_input_data(msg: IrisInputData):
     global model
-    species_class = model.predict(
+    species_class = ml_models["iris_predictor"].predict(
         [[msg.sepal_length, msg.sepal_width, msg.petal_length, msg.petal_width]]
     )[0]
 
     to_predictions(species_class)
 
 
 @kafka_app.produces(topic="predictions")
@@ -282,94 +303,83 @@
     prediction = IrisPrediction(species=iris_species[species_class])
     return prediction
 ```
 
 ## Testing the service
 
 The service can be tested using the
-[`Tester`](https://airtai.github.io/fastkafka/0.3.0/api/fastkafka/testing/Tester/#fastkafka.testing.Tester)
-instances which internally starts Kafka broker and zookeeper.
-
-Before running tests, we have to install Java runtime and Apache Kafka
-locally. To simplify the process, we provide the following convenience
-command:
-
-``` sh
-fastkafka testing install_deps
-```
-
-    [INFO] fastkafka._components.test_dependencies: Installing Java...
-    [INFO] fastkafka._components.test_dependencies:  - installing jdk...
-    [INFO] fastkafka._components.test_dependencies:  - jdk path: /home/kumaran/.jdk/jdk-11.0.18+10
-    [INFO] fastkafka._components.test_dependencies: Java installed.
-    [INFO] fastkafka._components.test_dependencies: Installing Kafka...
-    832969it [00:02, 309324.60it/s]                                                 
-    [INFO] fastkafka._components.test_dependencies: Kafka installed in /home/kumaran/.local/kafka_2.13-3.3.2.
+[`Tester`](https://airtai.github.io/fastkafka/0.4.0rc1/api/fastkafka/testing/Tester/#fastkafka.testing.Tester)
+instances which internally starts InMemory implementation of Kafka
+broker.
+
+The Tester will redirect your consumes and produces decorated functions
+to the InMemory Kafka broker so that you can quickly test your app
+without the need for a running Kafka broker and all its dependencies.
 
 ``` python
 from fastkafka.testing import Tester
 
 msg = IrisInputData(
     sepal_length=0.1,
     sepal_width=0.2,
     petal_length=0.3,
     petal_width=0.4,
 )
 
-# Start Tester app and create local Kafka broker for testing
+# Start Tester app and create InMemory Kafka broker for testing
 async with Tester(kafka_app) as tester:
     # Send IrisInputData message to input_data topic
     await tester.to_input_data(msg)
 
     # Assert that the kafka_app responded with IrisPrediction in predictions topic
     await tester.awaited_mocks.on_predictions.assert_awaited_with(
         IrisPrediction(species="setosa"), timeout=2
     )
 ```
 
-    [INFO] fastkafka._components.test_dependencies: Java is already installed.
-    [INFO] fastkafka._components.test_dependencies: But not exported to PATH, exporting...
-    [INFO] fastkafka._components.test_dependencies: Kafka is installed.
-    [INFO] fastkafka._components.test_dependencies: But not exported to PATH, exporting...
-    [INFO] fastkafka._testing.local_broker: Starting zookeeper...
-    [INFO] fastkafka._testing.local_broker: Starting kafka...
-    [INFO] fastkafka._testing.local_broker: Local Kafka broker up and running on 127.0.0.1:9092
-    [INFO] fastkafka._application.app: _create_producer() : created producer using the config: '{'bootstrap_servers': '127.0.0.1:9092'}'
+    [INFO] fastkafka._testing.in_memory_broker: InMemoryBroker._start() called
+    [INFO] fastkafka._testing.in_memory_broker: InMemoryBroker._patch_consumers_and_producers(): Patching consumers and producers!
+    [INFO] fastkafka._testing.in_memory_broker: InMemoryBroker starting
+    [INFO] fastkafka._application.app: _create_producer() : created producer using the config: '{'bootstrap_servers': 'localhost:9092'}'
     [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.start(): Entering...
+    [INFO] fastkafka._testing.in_memory_broker: AIOKafkaProducer patched start() called()
     [INFO] fastkafka._components.aiokafka_producer_manager: _aiokafka_producer_manager(): Starting...
     [INFO] fastkafka._components.aiokafka_producer_manager: _aiokafka_producer_manager(): Starting send_stream
     [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.start(): Finished.
-    [INFO] fastkafka._application.app: _create_producer() : created producer using the config: '{'bootstrap_servers': '127.0.0.1:9092'}'
+    [INFO] fastkafka._application.app: _create_producer() : created producer using the config: '{'bootstrap_servers': 'localhost:9092'}'
+    [INFO] fastkafka._testing.in_memory_broker: AIOKafkaProducer patched start() called()
     [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop() starting...
-    [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer created using the following parameters: {'bootstrap_servers': '127.0.0.1:9092', 'auto_offset_reset': 'latest', 'max_poll_records': 100}
+    [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer created using the following parameters: {'bootstrap_servers': 'localhost:9092', 'auto_offset_reset': 'latest', 'max_poll_records': 100}
+    [INFO] fastkafka._testing.in_memory_broker: AIOKafkaConsumer patched start() called()
     [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer started.
-    [INFO] aiokafka.consumer.subscription_state: Updating subscribed topics to: frozenset({'input_data'})
-    [INFO] aiokafka.consumer.consumer: Subscribed to topic(s): {'input_data'}
+    [INFO] fastkafka._testing.in_memory_broker: AIOKafkaConsumer patched subscribe() called
+    [INFO] fastkafka._testing.in_memory_broker: AIOKafkaConsumer.subscribe(), subscribing to: ['input_data']
     [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer subscribed.
     [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop() starting...
-    [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer created using the following parameters: {'bootstrap_servers': '127.0.0.1:9092', 'auto_offset_reset': 'earliest', 'max_poll_records': 100}
-    [INFO] aiokafka.consumer.group_coordinator: Metadata for topic has changed from {} to {'input_data': 1}. 
+    [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer created using the following parameters: {'bootstrap_servers': 'localhost:9092', 'auto_offset_reset': 'earliest', 'max_poll_records': 100}
+    [INFO] fastkafka._testing.in_memory_broker: AIOKafkaConsumer patched start() called()
     [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer started.
-    [INFO] aiokafka.consumer.subscription_state: Updating subscribed topics to: frozenset({'predictions'})
-    [INFO] aiokafka.consumer.consumer: Subscribed to topic(s): {'predictions'}
+    [INFO] fastkafka._testing.in_memory_broker: AIOKafkaConsumer patched subscribe() called
+    [INFO] fastkafka._testing.in_memory_broker: AIOKafkaConsumer.subscribe(), subscribing to: ['predictions']
     [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer subscribed.
-    [INFO] aiokafka.consumer.group_coordinator: Metadata for topic has changed from {} to {'predictions': 1}. 
+    [INFO] fastkafka._testing.in_memory_broker: AIOKafkaConsumer patched stop() called
     [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer stopped.
     [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop() finished.
+    [INFO] fastkafka._testing.in_memory_broker: AIOKafkaProducer patched stop() called
+    [INFO] fastkafka._testing.in_memory_broker: AIOKafkaConsumer patched stop() called
     [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer stopped.
     [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop() finished.
     [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.stop(): Entering...
     [INFO] fastkafka._components.aiokafka_producer_manager: _aiokafka_producer_manager(): Exiting send_stream
     [INFO] fastkafka._components.aiokafka_producer_manager: _aiokafka_producer_manager(): Finished.
     [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.stop(): Stoping producer...
+    [INFO] fastkafka._testing.in_memory_broker: AIOKafkaProducer patched stop() called
     [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.stop(): Finished
-    [INFO] fastkafka._components._subprocess: terminate_asyncio_process(): Terminating the process 547...
-    [INFO] fastkafka._components._subprocess: terminate_asyncio_process(): Process 547 terminated.
-    [INFO] fastkafka._components._subprocess: terminate_asyncio_process(): Terminating the process 173...
-    [INFO] fastkafka._components._subprocess: terminate_asyncio_process(): Process 173 terminated.
+    [INFO] fastkafka._testing.in_memory_broker: InMemoryBroker._stop() called
+    [INFO] fastkafka._testing.in_memory_broker: InMemoryBroker stopping
 
 ### Recap
 
 We have created a Iris classification model and encapulated it into our
 fastkafka application. The app will consume the IrisInputData from the
 `input_data` topic and produce the predictions to `predictions` topic.
 
@@ -453,129 +463,155 @@
     prediction = IrisPrediction(species=iris_species[species_class])
     return prediction
 ```
 
 To run the service, you will need a running Kafka broker on localhost as
 specified in the `kafka_brokers` parameter above. We can start the Kafka
 broker locally using the
-[`LocalKafkaBroker`](https://airtai.github.io/fastkafka/0.3.0/api/fastkafka/testing/LocalKafkaBroker/#fastkafka.testing.LocalKafkaBroker).
-Notice that the same happens automatically in the
-[`Tester`](https://airtai.github.io/fastkafka/0.3.0/api/fastkafka/testing/Tester/#fastkafka.testing.Tester)
-as shown above.
-
-    [INFO] fastkafka._testing.local_broker: LocalKafkaBroker.start(): entering...
-    [WARNING] fastkafka._testing.local_broker: LocalKafkaBroker.start(): (<_UnixSelectorEventLoop running=True closed=False debug=False>) is already running!
-    [WARNING] fastkafka._testing.local_broker: LocalKafkaBroker.start(): calling nest_asyncio.apply()
+[`ApacheKafkaBroker`](https://airtai.github.io/fastkafka/0.4.0rc1/api/fastkafka/testing/ApacheKafkaBroker/#fastkafka.testing.ApacheKafkaBroker).
+
+To use
+[`ApacheKafkaBroker`](https://airtai.github.io/fastkafka/0.4.0rc1/api/fastkafka/testing/ApacheKafkaBroker/#fastkafka.testing.ApacheKafkaBroker),
+you need to install JRE and Kafka to your environment. To simplify this
+process, fastkafka comes with a CLI command that does just that, to run
+it, in your terminal execute the following:
+
+``` sh
+fastkafka testing install_deps
+```
+
+Now we can run
+[`ApacheKafkaBroker`](https://airtai.github.io/fastkafka/0.4.0rc1/api/fastkafka/testing/ApacheKafkaBroker/#fastkafka.testing.ApacheKafkaBroker)
+that will start a Kafka broker instance for us.
+
+``` python
+from fastkafka.testing import ApacheKafkaBroker
+
+broker = ApacheKafkaBroker(apply_nest_asyncio=True)
+
+broker.start()
+```
+
+    [INFO] fastkafka._testing.apache_kafka_broker: ApacheKafkaBroker.start(): entering...
+    [WARNING] fastkafka._testing.apache_kafka_broker: ApacheKafkaBroker.start(): (<_UnixSelectorEventLoop running=True closed=False debug=False>) is already running!
+    [WARNING] fastkafka._testing.apache_kafka_broker: ApacheKafkaBroker.start(): calling nest_asyncio.apply()
     [INFO] fastkafka._components.test_dependencies: Java is already installed.
+    [INFO] fastkafka._components.test_dependencies: But not exported to PATH, exporting...
     [INFO] fastkafka._components.test_dependencies: Kafka is installed.
-    [INFO] fastkafka._testing.local_broker: Starting zookeeper...
-    [INFO] fastkafka._testing.local_broker: Starting kafka...
-    [INFO] fastkafka._testing.local_broker: Local Kafka broker up and running on 127.0.0.1:9092
-    [INFO] fastkafka._testing.local_broker: <class 'fastkafka.testing.LocalKafkaBroker'>.start(): returning 127.0.0.1:9092
-    [INFO] fastkafka._testing.local_broker: LocalKafkaBroker.start(): exited.
+    [INFO] fastkafka._components.test_dependencies: But not exported to PATH, exporting...
+    [INFO] fastkafka._testing.apache_kafka_broker: Starting zookeeper...
+    [INFO] fastkafka._testing.apache_kafka_broker: Starting kafka...
+    [INFO] fastkafka._testing.apache_kafka_broker: Local Kafka broker up and running on 127.0.0.1:9092
+    [INFO] fastkafka._testing.apache_kafka_broker: <class 'fastkafka.testing.ApacheKafkaBroker'>.start(): returning 127.0.0.1:9092
+    [INFO] fastkafka._testing.apache_kafka_broker: ApacheKafkaBroker.start(): exited.
 
     '127.0.0.1:9092'
 
 Then, we start the FastKafka service by running the following command in
 the folder where the `application.py` file is located:
 
 ``` sh
 fastkafka run --num-workers=2 --kafka-broker localhost application:kafka_app
 ```
 
 In the above command, we use `--num-workers` option to specify how many
 workers to launch and we use `--kafka-broker` option to specify which
 kafka broker configuration to use from earlier specified `kafka_brokers`
 
-    [2559]: [INFO] fastkafka._application.app: set_kafka_broker() : Setting bootstrap_servers value to 'localhost:9092'
-    [2559]: [INFO] fastkafka._application.app: _create_producer() : created producer using the config: '{'bootstrap_servers': 'localhost:9092'}'
-    [2559]: [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.start(): Entering...
-    [2561]: [INFO] fastkafka._application.app: set_kafka_broker() : Setting bootstrap_servers value to 'localhost:9092'
-    [2561]: [INFO] fastkafka._application.app: _create_producer() : created producer using the config: '{'bootstrap_servers': 'localhost:9092'}'
-    [2561]: [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.start(): Entering...
-    [2559]: [INFO] fastkafka._components.aiokafka_producer_manager: _aiokafka_producer_manager(): Starting...
-    [2559]: [INFO] fastkafka._components.aiokafka_producer_manager: _aiokafka_producer_manager(): Starting send_stream
-    [2559]: [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.start(): Finished.
-    [2561]: [INFO] fastkafka._components.aiokafka_producer_manager: _aiokafka_producer_manager(): Starting...
-    [2561]: [INFO] fastkafka._components.aiokafka_producer_manager: _aiokafka_producer_manager(): Starting send_stream
-    [2561]: [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.start(): Finished.
-    [2559]: [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop() starting...
-    [2559]: [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer created using the following parameters: {'bootstrap_servers': 'localhost:9092', 'auto_offset_reset': 'latest', 'max_poll_records': 100}
-    [2561]: [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop() starting...
-    [2561]: [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer created using the following parameters: {'bootstrap_servers': 'localhost:9092', 'auto_offset_reset': 'latest', 'max_poll_records': 100}
-    [2561]: [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer started.
-    [2559]: [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer started.
-    [2561]: [INFO] aiokafka.consumer.subscription_state: Updating subscribed topics to: frozenset({'input_data'})
-    [2561]: [INFO] aiokafka.consumer.consumer: Subscribed to topic(s): {'input_data'}
-    [2559]: [INFO] aiokafka.consumer.subscription_state: Updating subscribed topics to: frozenset({'input_data'})
-    [2561]: [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer subscribed.
-    [2559]: [INFO] aiokafka.consumer.consumer: Subscribed to topic(s): {'input_data'}
-    [2559]: [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer subscribed.
-    [2561]: [ERROR] aiokafka.cluster: Topic input_data not found in cluster metadata
-    [2561]: [INFO] aiokafka.consumer.group_coordinator: Metadata for topic has changed from {} to {'input_data': 0}. 
-    [2559]: [WARNING] aiokafka.cluster: Topic input_data is not available during auto-create initialization
-    [2559]: [INFO] aiokafka.consumer.group_coordinator: Metadata for topic has changed from {} to {'input_data': 0}. 
-    [2561]: [ERROR] aiokafka: Unable connect to node with id 0: [Errno 111] Connect call failed ('172.22.0.2', 9092)
-    [2559]: [ERROR] aiokafka: Unable connect to node with id 0: [Errno 111] Connect call failed ('172.22.0.2', 9092)
-    [2561]: [ERROR] aiokafka: Unable to update metadata from [0]
-    [2559]: [ERROR] aiokafka: Unable to update metadata from [0]
+    [558863]: [INFO] fastkafka._application.app: set_kafka_broker() : Setting bootstrap_servers value to 'localhost:9092'
+    [558863]: [INFO] fastkafka._application.app: _create_producer() : created producer using the config: '{'bootstrap_servers': 'localhost:9092'}'
+    [558863]: [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.start(): Entering...
+    [558865]: [INFO] fastkafka._application.app: set_kafka_broker() : Setting bootstrap_servers value to 'localhost:9092'
+    [558865]: [INFO] fastkafka._application.app: _create_producer() : created producer using the config: '{'bootstrap_servers': 'localhost:9092'}'
+    [558865]: [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.start(): Entering...
+    [558865]: [INFO] fastkafka._components.aiokafka_producer_manager: _aiokafka_producer_manager(): Starting...
+    [558865]: [INFO] fastkafka._components.aiokafka_producer_manager: _aiokafka_producer_manager(): Starting send_stream
+    [558865]: [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.start(): Finished.
+    [558863]: [INFO] fastkafka._components.aiokafka_producer_manager: _aiokafka_producer_manager(): Starting...
+    [558863]: [INFO] fastkafka._components.aiokafka_producer_manager: _aiokafka_producer_manager(): Starting send_stream
+    [558863]: [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.start(): Finished.
+    [558865]: [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop() starting...
+    [558865]: [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer created using the following parameters: {'bootstrap_servers': 'localhost:9092', 'auto_offset_reset': 'latest', 'max_poll_records': 100}
+    [558863]: [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop() starting...
+    [558863]: [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer created using the following parameters: {'bootstrap_servers': 'localhost:9092', 'auto_offset_reset': 'latest', 'max_poll_records': 100}
+    [558865]: [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer started.
+    [558865]: [INFO] aiokafka.consumer.subscription_state: Updating subscribed topics to: frozenset({'input_data'})
+    [558865]: [INFO] aiokafka.consumer.consumer: Subscribed to topic(s): {'input_data'}
+    [558865]: [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer subscribed.
+    [558863]: [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer started.
+    [558863]: [INFO] aiokafka.consumer.subscription_state: Updating subscribed topics to: frozenset({'input_data'})
+    [558863]: [INFO] aiokafka.consumer.consumer: Subscribed to topic(s): {'input_data'}
+    [558863]: [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer subscribed.
+    [558863]: [ERROR] aiokafka.cluster: Topic input_data not found in cluster metadata
+    [558863]: [INFO] aiokafka.consumer.group_coordinator: Metadata for topic has changed from {} to {'input_data': 0}. 
+    [558865]: [WARNING] aiokafka.cluster: Topic input_data is not available during auto-create initialization
+    [558865]: [INFO] aiokafka.consumer.group_coordinator: Metadata for topic has changed from {} to {'input_data': 0}. 
+    [558865]: [ERROR] aiokafka: Unable connect to node with id 0: [Errno 111] Connect call failed ('172.26.0.2', 9092)
+    [558863]: [ERROR] aiokafka: Unable connect to node with id 0: [Errno 111] Connect call failed ('172.26.0.2', 9092)
+    [558865]: [ERROR] aiokafka: Unable to update metadata from [0]
+    [558863]: [ERROR] aiokafka: Unable to update metadata from [0]
     ^C
     Starting process cleanup, this may take a few seconds...
-    [INFO] fastkafka._server: terminate_asyncio_process(): Terminating the process 2559...
-    [INFO] fastkafka._server: terminate_asyncio_process(): Terminating the process 2561...
-    [2561]: [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer stopped.
-    [2561]: [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop() finished.
-    [2561]: [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.stop(): Entering...
-    [2561]: [INFO] fastkafka._components.aiokafka_producer_manager: _aiokafka_producer_manager(): Exiting send_stream
-    [2561]: [INFO] fastkafka._components.aiokafka_producer_manager: _aiokafka_producer_manager(): Finished.
-    [2561]: [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.stop(): Stoping producer...
-    [2561]: [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.stop(): Finished
-    [2559]: [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer stopped.
-    [2559]: [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop() finished.
-    [2559]: [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.stop(): Entering...
-    [2559]: [INFO] fastkafka._components.aiokafka_producer_manager: _aiokafka_producer_manager(): Exiting send_stream
-    [2559]: [INFO] fastkafka._components.aiokafka_producer_manager: _aiokafka_producer_manager(): Finished.
-    [2559]: [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.stop(): Stoping producer...
-    [2559]: [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.stop(): Finished
-    [INFO] fastkafka._server: terminate_asyncio_process(): Process 2561 was already terminated.
-    [INFO] fastkafka._server: terminate_asyncio_process(): Process 2559 was already terminated.
+    [INFO] fastkafka._server: terminate_asyncio_process(): Terminating the process 558863...
+    [INFO] fastkafka._server: terminate_asyncio_process(): Terminating the process 558865...
+    [558863]: [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer stopped.
+    [558863]: [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop() finished.
+    [558863]: [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.stop(): Entering...
+    [558863]: [INFO] fastkafka._components.aiokafka_producer_manager: _aiokafka_producer_manager(): Exiting send_stream
+    [558863]: [INFO] fastkafka._components.aiokafka_producer_manager: _aiokafka_producer_manager(): Finished.
+    [558863]: [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.stop(): Stoping producer...
+    [558863]: [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.stop(): Finished
+    [558865]: [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer stopped.
+    [558865]: [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop() finished.
+    [558865]: [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.stop(): Entering...
+    [558865]: [INFO] fastkafka._components.aiokafka_producer_manager: _aiokafka_producer_manager(): Exiting send_stream
+    [558865]: [INFO] fastkafka._components.aiokafka_producer_manager: _aiokafka_producer_manager(): Finished.
+    [558865]: [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.stop(): Stoping producer...
+    [558865]: [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.stop(): Finished
+    [INFO] fastkafka._server: terminate_asyncio_process(): Process 558863 was already terminated.
+    [INFO] fastkafka._server: terminate_asyncio_process(): Process 558865 was already terminated.
 
 You need to interupt running of the cell above by selecting
 `Runtime->Interupt execution` on the toolbar above.
 
 Finally, we can stop the local Kafka Broker:
 
-    [INFO] fastkafka._testing.local_broker: LocalKafkaBroker.stop(): entering...
-    [INFO] fastkafka._components._subprocess: terminate_asyncio_process(): Terminating the process 2098...
-    [INFO] fastkafka._components._subprocess: terminate_asyncio_process(): Process 2098 was already terminated.
-    [INFO] fastkafka._components._subprocess: terminate_asyncio_process(): Terminating the process 1725...
-    [INFO] fastkafka._components._subprocess: terminate_asyncio_process(): Process 1725 was already terminated.
-    [INFO] fastkafka._testing.local_broker: LocalKafkaBroker.stop(): exited.
+``` python
+broker.stop()
+```
+
+    [INFO] fastkafka._testing.apache_kafka_broker: ApacheKafkaBroker.stop(): entering...
+    [INFO] fastkafka._components._subprocess: terminate_asyncio_process(): Terminating the process 558265...
+    [INFO] fastkafka._components._subprocess: terminate_asyncio_process(): Process 558265 was already terminated.
+    [INFO] fastkafka._components._subprocess: terminate_asyncio_process(): Terminating the process 557885...
+    [INFO] fastkafka._components._subprocess: terminate_asyncio_process(): Process 557885 was already terminated.
+    [INFO] fastkafka._testing.apache_kafka_broker: ApacheKafkaBroker.stop(): exited.
 
 ## Documentation
 
 The kafka app comes with builtin documentation generation using
 [AsyncApi HTML generator](https://www.asyncapi.com/tools/generator).
 
 AsyncApi requires Node.js to be installed and we provide the following
 convenience command line for it:
 
 ``` sh
 fastkafka docs install_deps
 ```
 
-    [INFO] fastkafka._components.asyncapi: AsyncAPI generator installed
+    [INFO] fastkafka._components.docs_dependencies: AsyncAPI generator installed
 
 To generate the documentation programatically you just need to call the
 folloving command:
 
 ``` sh
 fastkafka docs generate application:kafka_app
 ```
 
+    [INFO] fastkafka._components.asyncapi: Old async specifications at '/work/fastkafka/nbs/asyncapi/spec/asyncapi.yml' does not exist.
     [INFO] fastkafka._components.asyncapi: New async specifications generated at: '/work/fastkafka/nbs/asyncapi/spec/asyncapi.yml'
     [INFO] fastkafka._components.asyncapi: Async docs generated at 'asyncapi/docs'
     [INFO] fastkafka._components.asyncapi: Output of '$ npx -y -p @asyncapi/generator ag asyncapi/spec/asyncapi.yml @asyncapi/html-template -o asyncapi/docs --force-write'
 
     Done! ✨
     Check out your shiny new generated files at /work/fastkafka/nbs/asyncapi/docs.
 
@@ -584,16 +620,16 @@
 with:
 
 ``` sh
 ls -l asyncapi
 ```
 
     total 8
-    drwxrwxr-x 4 kumaran kumaran 4096 Mar 21 09:14 docs
-    drwxrwxr-x 2 kumaran kumaran 4096 Mar 21 09:14 spec
+    drwxrwxr-x 4 tvrtko tvrtko 4096 Apr  5 08:02 docs
+    drwxrwxr-x 2 tvrtko tvrtko 4096 Apr  5 08:02 spec
 
 In docs folder you will find the servable static html file of your
 documentation. This can also be served using our `fastkafka docs serve`
 CLI command (more on that in our guides).
 
 In spec folder you will find a asyncapi.yml file containing the async
 API specification of your application.
```

### Comparing `fastkafka-0.4.0rc0/README.md` & `fastkafka-0.4.0rc1/README.md`

 * *Files 8% similar despite different names*

```diff
@@ -31,20 +31,30 @@
 With FastKafka, you can quickly prototype and develop high-performance
 Kafka-based services with minimal code, making it an ideal choice for
 developers looking to streamline their workflow and accelerate their
 projects.
 
 ------------------------------------------------------------------------
 
-#### ⭐ Stay in touch
+#### ⭐⭐⭐ Stay in touch ⭐⭐⭐
 
-Please show your support and stay in touch by giving our [GitHub
-repository](https://github.com/airtai/fastkafka/) a star! Your support
-helps us to stay in touch with you and encourages us to continue
-developing and improving the library. Thank you for your support!
+Please show your support and stay in touch by:
+
+- giving our [GitHub repository](https://github.com/airtai/fastkafka/) a
+  star, and
+
+- joining our [Discord server](https://discord.gg/CJWmYpyFbc).
+
+Your support helps us to stay in touch with you and encourages us to
+continue developing and improving the library. Thank you for your
+support!
+
+------------------------------------------------------------------------
+
+#### 🐝🐝🐝 We were busy lately 🐝🐝🐝
 
 ![Activity](https://repobeats.axiom.co/api/embed/21f36049093d5eb8e5fdad18c3c5d8df5428ca30.svg "Repobeats analytics image")
 
 ## Install
 
 FastKafka works on macOS, Linux, and most Unix-style operating systems.
 You can install base version of `fastkafka` with `pip` as usual:
@@ -73,44 +83,54 @@
 
 ## Tutorial
 
 You can start an interactive tutorial in Google Colab by clicking the
 button below:
 
 <a href="https://colab.research.google.com/github/airtai/fastkafka/blob/main/nbs/guides/Guide_00_FastKafka_Demo.ipynb" target=”_blank”>
-<img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab">
+<img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" />
 </a>
 
 ## Writing server code
 
 Here is an example python script using FastKafka that takes data from a
 Kafka topic, makes a prediction using a predictive model, and outputs
 the prediction to another Kafka topic.
 
 ### Preparing the demo model
 
 First we will prepare our model using the Iris dataset so that we can
 demonstrate the predictions using FastKafka. The following call
 downloads the dataset and trains the model.
 
+We will wrap the model creation into a lifespan of our app so that the
+model is created just before the app is started.
+
 ``` python
+from contextlib import asynccontextmanager
+
 from sklearn.datasets import load_iris
 from sklearn.linear_model import LogisticRegression
 
-X, y = load_iris(return_X_y=True)
-model = LogisticRegression(random_state=0, max_iter=500).fit(X, y)
-x = X[[0, 55, -1]]
-print(x)
-print(model.predict(x))
-```
+from fastkafka import FastKafka
+
+ml_models = {}
 
-    [[5.1 3.5 1.4 0.2]
-     [5.7 2.8 4.5 1.3]
-     [5.9 3.  5.1 1.8]]
-    [0 1 2]
+
+@asynccontextmanager
+async def lifespan(app: FastKafka):
+    # Load the ML model
+    X, y = load_iris(return_X_y=True)
+    ml_models["iris_predictor"] = LogisticRegression(random_state=0, max_iter=500).fit(
+        X, y
+    )
+    yield
+    # Clean up the ML models and release the resources
+    ml_models.clear()
+```
 
 ### Messages
 
 FastKafka uses [Pydantic](https://docs.pydantic.dev/) to parse input
 JSON-encoded data into Python objects, making it easy to work with
 structured data in your Kafka-based applications. Pydantic’s
 [`BaseModel`](https://docs.pydantic.dev/usage/models/) class allows you
@@ -164,15 +184,15 @@
 contains two entries: `"localhost"` and `"production"`, specifying local
 development and production Kafka brokers. Each entry specifies the URL,
 port, and other details of a Kafka broker. This dictionary is used for
 both generating the documentation and later to run the actual server
 against one of the given kafka broker.
 
 Next, an object of the
-[`FastKafka`](https://airtai.github.io/fastkafka/0.3.0/api/fastkafka/FastKafka/#fastkafka.FastKafka)
+[`FastKafka`](https://airtai.github.io/fastkafka/0.4.0rc1/api/fastkafka/FastKafka/#fastkafka.FastKafka)
 class is initialized with the minimum set of arguments:
 
 - `kafka_brokers`: a dictionary used for generation of documentation
 
 ``` python
 from fastkafka import FastKafka
 
@@ -190,14 +210,15 @@
         "security": {"type": "plain"},
     },
 }
 
 kafka_app = FastKafka(
     title="Iris predictions",
     kafka_brokers=kafka_brokers,
+    lifespan=lifespan,
 )
 ```
 
 ### Function decorators
 
 FastKafka provides convenient function decorators `@kafka_app.consumes`
 and `@kafka_app.produces` to allow you to delegate the actual process of
@@ -235,15 +256,15 @@
   The framework will call the `IrisPrediction.json().encode("utf-8")`
   function on the returned value and produce it to the specified topic.
 
 ``` python
 @kafka_app.consumes(topic="input_data", auto_offset_reset="latest")
 async def on_input_data(msg: IrisInputData):
     global model
-    species_class = model.predict(
+    species_class = ml_models["iris_predictor"].predict(
         [[msg.sepal_length, msg.sepal_width, msg.petal_length, msg.petal_width]]
     )[0]
 
     to_predictions(species_class)
 
 
 @kafka_app.produces(topic="predictions")
@@ -253,94 +274,83 @@
     prediction = IrisPrediction(species=iris_species[species_class])
     return prediction
 ```
 
 ## Testing the service
 
 The service can be tested using the
-[`Tester`](https://airtai.github.io/fastkafka/0.3.0/api/fastkafka/testing/Tester/#fastkafka.testing.Tester)
-instances which internally starts Kafka broker and zookeeper.
-
-Before running tests, we have to install Java runtime and Apache Kafka
-locally. To simplify the process, we provide the following convenience
-command:
-
-``` sh
-fastkafka testing install_deps
-```
-
-    [INFO] fastkafka._components.test_dependencies: Installing Java...
-    [INFO] fastkafka._components.test_dependencies:  - installing jdk...
-    [INFO] fastkafka._components.test_dependencies:  - jdk path: /home/kumaran/.jdk/jdk-11.0.18+10
-    [INFO] fastkafka._components.test_dependencies: Java installed.
-    [INFO] fastkafka._components.test_dependencies: Installing Kafka...
-    832969it [00:02, 309324.60it/s]                                                 
-    [INFO] fastkafka._components.test_dependencies: Kafka installed in /home/kumaran/.local/kafka_2.13-3.3.2.
+[`Tester`](https://airtai.github.io/fastkafka/0.4.0rc1/api/fastkafka/testing/Tester/#fastkafka.testing.Tester)
+instances which internally starts InMemory implementation of Kafka
+broker.
+
+The Tester will redirect your consumes and produces decorated functions
+to the InMemory Kafka broker so that you can quickly test your app
+without the need for a running Kafka broker and all its dependencies.
 
 ``` python
 from fastkafka.testing import Tester
 
 msg = IrisInputData(
     sepal_length=0.1,
     sepal_width=0.2,
     petal_length=0.3,
     petal_width=0.4,
 )
 
-# Start Tester app and create local Kafka broker for testing
+# Start Tester app and create InMemory Kafka broker for testing
 async with Tester(kafka_app) as tester:
     # Send IrisInputData message to input_data topic
     await tester.to_input_data(msg)
 
     # Assert that the kafka_app responded with IrisPrediction in predictions topic
     await tester.awaited_mocks.on_predictions.assert_awaited_with(
         IrisPrediction(species="setosa"), timeout=2
     )
 ```
 
-    [INFO] fastkafka._components.test_dependencies: Java is already installed.
-    [INFO] fastkafka._components.test_dependencies: But not exported to PATH, exporting...
-    [INFO] fastkafka._components.test_dependencies: Kafka is installed.
-    [INFO] fastkafka._components.test_dependencies: But not exported to PATH, exporting...
-    [INFO] fastkafka._testing.local_broker: Starting zookeeper...
-    [INFO] fastkafka._testing.local_broker: Starting kafka...
-    [INFO] fastkafka._testing.local_broker: Local Kafka broker up and running on 127.0.0.1:9092
-    [INFO] fastkafka._application.app: _create_producer() : created producer using the config: '{'bootstrap_servers': '127.0.0.1:9092'}'
+    [INFO] fastkafka._testing.in_memory_broker: InMemoryBroker._start() called
+    [INFO] fastkafka._testing.in_memory_broker: InMemoryBroker._patch_consumers_and_producers(): Patching consumers and producers!
+    [INFO] fastkafka._testing.in_memory_broker: InMemoryBroker starting
+    [INFO] fastkafka._application.app: _create_producer() : created producer using the config: '{'bootstrap_servers': 'localhost:9092'}'
     [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.start(): Entering...
+    [INFO] fastkafka._testing.in_memory_broker: AIOKafkaProducer patched start() called()
     [INFO] fastkafka._components.aiokafka_producer_manager: _aiokafka_producer_manager(): Starting...
     [INFO] fastkafka._components.aiokafka_producer_manager: _aiokafka_producer_manager(): Starting send_stream
     [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.start(): Finished.
-    [INFO] fastkafka._application.app: _create_producer() : created producer using the config: '{'bootstrap_servers': '127.0.0.1:9092'}'
+    [INFO] fastkafka._application.app: _create_producer() : created producer using the config: '{'bootstrap_servers': 'localhost:9092'}'
+    [INFO] fastkafka._testing.in_memory_broker: AIOKafkaProducer patched start() called()
     [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop() starting...
-    [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer created using the following parameters: {'bootstrap_servers': '127.0.0.1:9092', 'auto_offset_reset': 'latest', 'max_poll_records': 100}
+    [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer created using the following parameters: {'bootstrap_servers': 'localhost:9092', 'auto_offset_reset': 'latest', 'max_poll_records': 100}
+    [INFO] fastkafka._testing.in_memory_broker: AIOKafkaConsumer patched start() called()
     [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer started.
-    [INFO] aiokafka.consumer.subscription_state: Updating subscribed topics to: frozenset({'input_data'})
-    [INFO] aiokafka.consumer.consumer: Subscribed to topic(s): {'input_data'}
+    [INFO] fastkafka._testing.in_memory_broker: AIOKafkaConsumer patched subscribe() called
+    [INFO] fastkafka._testing.in_memory_broker: AIOKafkaConsumer.subscribe(), subscribing to: ['input_data']
     [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer subscribed.
     [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop() starting...
-    [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer created using the following parameters: {'bootstrap_servers': '127.0.0.1:9092', 'auto_offset_reset': 'earliest', 'max_poll_records': 100}
-    [INFO] aiokafka.consumer.group_coordinator: Metadata for topic has changed from {} to {'input_data': 1}. 
+    [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer created using the following parameters: {'bootstrap_servers': 'localhost:9092', 'auto_offset_reset': 'earliest', 'max_poll_records': 100}
+    [INFO] fastkafka._testing.in_memory_broker: AIOKafkaConsumer patched start() called()
     [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer started.
-    [INFO] aiokafka.consumer.subscription_state: Updating subscribed topics to: frozenset({'predictions'})
-    [INFO] aiokafka.consumer.consumer: Subscribed to topic(s): {'predictions'}
+    [INFO] fastkafka._testing.in_memory_broker: AIOKafkaConsumer patched subscribe() called
+    [INFO] fastkafka._testing.in_memory_broker: AIOKafkaConsumer.subscribe(), subscribing to: ['predictions']
     [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer subscribed.
-    [INFO] aiokafka.consumer.group_coordinator: Metadata for topic has changed from {} to {'predictions': 1}. 
+    [INFO] fastkafka._testing.in_memory_broker: AIOKafkaConsumer patched stop() called
     [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer stopped.
     [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop() finished.
+    [INFO] fastkafka._testing.in_memory_broker: AIOKafkaProducer patched stop() called
+    [INFO] fastkafka._testing.in_memory_broker: AIOKafkaConsumer patched stop() called
     [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer stopped.
     [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop() finished.
     [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.stop(): Entering...
     [INFO] fastkafka._components.aiokafka_producer_manager: _aiokafka_producer_manager(): Exiting send_stream
     [INFO] fastkafka._components.aiokafka_producer_manager: _aiokafka_producer_manager(): Finished.
     [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.stop(): Stoping producer...
+    [INFO] fastkafka._testing.in_memory_broker: AIOKafkaProducer patched stop() called
     [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.stop(): Finished
-    [INFO] fastkafka._components._subprocess: terminate_asyncio_process(): Terminating the process 547...
-    [INFO] fastkafka._components._subprocess: terminate_asyncio_process(): Process 547 terminated.
-    [INFO] fastkafka._components._subprocess: terminate_asyncio_process(): Terminating the process 173...
-    [INFO] fastkafka._components._subprocess: terminate_asyncio_process(): Process 173 terminated.
+    [INFO] fastkafka._testing.in_memory_broker: InMemoryBroker._stop() called
+    [INFO] fastkafka._testing.in_memory_broker: InMemoryBroker stopping
 
 ### Recap
 
 We have created a Iris classification model and encapulated it into our
 fastkafka application. The app will consume the IrisInputData from the
 `input_data` topic and produce the predictions to `predictions` topic.
 
@@ -424,129 +434,155 @@
     prediction = IrisPrediction(species=iris_species[species_class])
     return prediction
 ```
 
 To run the service, you will need a running Kafka broker on localhost as
 specified in the `kafka_brokers` parameter above. We can start the Kafka
 broker locally using the
-[`LocalKafkaBroker`](https://airtai.github.io/fastkafka/0.3.0/api/fastkafka/testing/LocalKafkaBroker/#fastkafka.testing.LocalKafkaBroker).
-Notice that the same happens automatically in the
-[`Tester`](https://airtai.github.io/fastkafka/0.3.0/api/fastkafka/testing/Tester/#fastkafka.testing.Tester)
-as shown above.
-
-    [INFO] fastkafka._testing.local_broker: LocalKafkaBroker.start(): entering...
-    [WARNING] fastkafka._testing.local_broker: LocalKafkaBroker.start(): (<_UnixSelectorEventLoop running=True closed=False debug=False>) is already running!
-    [WARNING] fastkafka._testing.local_broker: LocalKafkaBroker.start(): calling nest_asyncio.apply()
+[`ApacheKafkaBroker`](https://airtai.github.io/fastkafka/0.4.0rc1/api/fastkafka/testing/ApacheKafkaBroker/#fastkafka.testing.ApacheKafkaBroker).
+
+To use
+[`ApacheKafkaBroker`](https://airtai.github.io/fastkafka/0.4.0rc1/api/fastkafka/testing/ApacheKafkaBroker/#fastkafka.testing.ApacheKafkaBroker),
+you need to install JRE and Kafka to your environment. To simplify this
+process, fastkafka comes with a CLI command that does just that, to run
+it, in your terminal execute the following:
+
+``` sh
+fastkafka testing install_deps
+```
+
+Now we can run
+[`ApacheKafkaBroker`](https://airtai.github.io/fastkafka/0.4.0rc1/api/fastkafka/testing/ApacheKafkaBroker/#fastkafka.testing.ApacheKafkaBroker)
+that will start a Kafka broker instance for us.
+
+``` python
+from fastkafka.testing import ApacheKafkaBroker
+
+broker = ApacheKafkaBroker(apply_nest_asyncio=True)
+
+broker.start()
+```
+
+    [INFO] fastkafka._testing.apache_kafka_broker: ApacheKafkaBroker.start(): entering...
+    [WARNING] fastkafka._testing.apache_kafka_broker: ApacheKafkaBroker.start(): (<_UnixSelectorEventLoop running=True closed=False debug=False>) is already running!
+    [WARNING] fastkafka._testing.apache_kafka_broker: ApacheKafkaBroker.start(): calling nest_asyncio.apply()
     [INFO] fastkafka._components.test_dependencies: Java is already installed.
+    [INFO] fastkafka._components.test_dependencies: But not exported to PATH, exporting...
     [INFO] fastkafka._components.test_dependencies: Kafka is installed.
-    [INFO] fastkafka._testing.local_broker: Starting zookeeper...
-    [INFO] fastkafka._testing.local_broker: Starting kafka...
-    [INFO] fastkafka._testing.local_broker: Local Kafka broker up and running on 127.0.0.1:9092
-    [INFO] fastkafka._testing.local_broker: <class 'fastkafka.testing.LocalKafkaBroker'>.start(): returning 127.0.0.1:9092
-    [INFO] fastkafka._testing.local_broker: LocalKafkaBroker.start(): exited.
+    [INFO] fastkafka._components.test_dependencies: But not exported to PATH, exporting...
+    [INFO] fastkafka._testing.apache_kafka_broker: Starting zookeeper...
+    [INFO] fastkafka._testing.apache_kafka_broker: Starting kafka...
+    [INFO] fastkafka._testing.apache_kafka_broker: Local Kafka broker up and running on 127.0.0.1:9092
+    [INFO] fastkafka._testing.apache_kafka_broker: <class 'fastkafka.testing.ApacheKafkaBroker'>.start(): returning 127.0.0.1:9092
+    [INFO] fastkafka._testing.apache_kafka_broker: ApacheKafkaBroker.start(): exited.
 
     '127.0.0.1:9092'
 
 Then, we start the FastKafka service by running the following command in
 the folder where the `application.py` file is located:
 
 ``` sh
 fastkafka run --num-workers=2 --kafka-broker localhost application:kafka_app
 ```
 
 In the above command, we use `--num-workers` option to specify how many
 workers to launch and we use `--kafka-broker` option to specify which
 kafka broker configuration to use from earlier specified `kafka_brokers`
 
-    [2559]: [INFO] fastkafka._application.app: set_kafka_broker() : Setting bootstrap_servers value to 'localhost:9092'
-    [2559]: [INFO] fastkafka._application.app: _create_producer() : created producer using the config: '{'bootstrap_servers': 'localhost:9092'}'
-    [2559]: [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.start(): Entering...
-    [2561]: [INFO] fastkafka._application.app: set_kafka_broker() : Setting bootstrap_servers value to 'localhost:9092'
-    [2561]: [INFO] fastkafka._application.app: _create_producer() : created producer using the config: '{'bootstrap_servers': 'localhost:9092'}'
-    [2561]: [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.start(): Entering...
-    [2559]: [INFO] fastkafka._components.aiokafka_producer_manager: _aiokafka_producer_manager(): Starting...
-    [2559]: [INFO] fastkafka._components.aiokafka_producer_manager: _aiokafka_producer_manager(): Starting send_stream
-    [2559]: [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.start(): Finished.
-    [2561]: [INFO] fastkafka._components.aiokafka_producer_manager: _aiokafka_producer_manager(): Starting...
-    [2561]: [INFO] fastkafka._components.aiokafka_producer_manager: _aiokafka_producer_manager(): Starting send_stream
-    [2561]: [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.start(): Finished.
-    [2559]: [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop() starting...
-    [2559]: [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer created using the following parameters: {'bootstrap_servers': 'localhost:9092', 'auto_offset_reset': 'latest', 'max_poll_records': 100}
-    [2561]: [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop() starting...
-    [2561]: [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer created using the following parameters: {'bootstrap_servers': 'localhost:9092', 'auto_offset_reset': 'latest', 'max_poll_records': 100}
-    [2561]: [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer started.
-    [2559]: [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer started.
-    [2561]: [INFO] aiokafka.consumer.subscription_state: Updating subscribed topics to: frozenset({'input_data'})
-    [2561]: [INFO] aiokafka.consumer.consumer: Subscribed to topic(s): {'input_data'}
-    [2559]: [INFO] aiokafka.consumer.subscription_state: Updating subscribed topics to: frozenset({'input_data'})
-    [2561]: [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer subscribed.
-    [2559]: [INFO] aiokafka.consumer.consumer: Subscribed to topic(s): {'input_data'}
-    [2559]: [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer subscribed.
-    [2561]: [ERROR] aiokafka.cluster: Topic input_data not found in cluster metadata
-    [2561]: [INFO] aiokafka.consumer.group_coordinator: Metadata for topic has changed from {} to {'input_data': 0}. 
-    [2559]: [WARNING] aiokafka.cluster: Topic input_data is not available during auto-create initialization
-    [2559]: [INFO] aiokafka.consumer.group_coordinator: Metadata for topic has changed from {} to {'input_data': 0}. 
-    [2561]: [ERROR] aiokafka: Unable connect to node with id 0: [Errno 111] Connect call failed ('172.22.0.2', 9092)
-    [2559]: [ERROR] aiokafka: Unable connect to node with id 0: [Errno 111] Connect call failed ('172.22.0.2', 9092)
-    [2561]: [ERROR] aiokafka: Unable to update metadata from [0]
-    [2559]: [ERROR] aiokafka: Unable to update metadata from [0]
+    [558863]: [INFO] fastkafka._application.app: set_kafka_broker() : Setting bootstrap_servers value to 'localhost:9092'
+    [558863]: [INFO] fastkafka._application.app: _create_producer() : created producer using the config: '{'bootstrap_servers': 'localhost:9092'}'
+    [558863]: [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.start(): Entering...
+    [558865]: [INFO] fastkafka._application.app: set_kafka_broker() : Setting bootstrap_servers value to 'localhost:9092'
+    [558865]: [INFO] fastkafka._application.app: _create_producer() : created producer using the config: '{'bootstrap_servers': 'localhost:9092'}'
+    [558865]: [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.start(): Entering...
+    [558865]: [INFO] fastkafka._components.aiokafka_producer_manager: _aiokafka_producer_manager(): Starting...
+    [558865]: [INFO] fastkafka._components.aiokafka_producer_manager: _aiokafka_producer_manager(): Starting send_stream
+    [558865]: [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.start(): Finished.
+    [558863]: [INFO] fastkafka._components.aiokafka_producer_manager: _aiokafka_producer_manager(): Starting...
+    [558863]: [INFO] fastkafka._components.aiokafka_producer_manager: _aiokafka_producer_manager(): Starting send_stream
+    [558863]: [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.start(): Finished.
+    [558865]: [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop() starting...
+    [558865]: [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer created using the following parameters: {'bootstrap_servers': 'localhost:9092', 'auto_offset_reset': 'latest', 'max_poll_records': 100}
+    [558863]: [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop() starting...
+    [558863]: [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer created using the following parameters: {'bootstrap_servers': 'localhost:9092', 'auto_offset_reset': 'latest', 'max_poll_records': 100}
+    [558865]: [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer started.
+    [558865]: [INFO] aiokafka.consumer.subscription_state: Updating subscribed topics to: frozenset({'input_data'})
+    [558865]: [INFO] aiokafka.consumer.consumer: Subscribed to topic(s): {'input_data'}
+    [558865]: [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer subscribed.
+    [558863]: [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer started.
+    [558863]: [INFO] aiokafka.consumer.subscription_state: Updating subscribed topics to: frozenset({'input_data'})
+    [558863]: [INFO] aiokafka.consumer.consumer: Subscribed to topic(s): {'input_data'}
+    [558863]: [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer subscribed.
+    [558863]: [ERROR] aiokafka.cluster: Topic input_data not found in cluster metadata
+    [558863]: [INFO] aiokafka.consumer.group_coordinator: Metadata for topic has changed from {} to {'input_data': 0}. 
+    [558865]: [WARNING] aiokafka.cluster: Topic input_data is not available during auto-create initialization
+    [558865]: [INFO] aiokafka.consumer.group_coordinator: Metadata for topic has changed from {} to {'input_data': 0}. 
+    [558865]: [ERROR] aiokafka: Unable connect to node with id 0: [Errno 111] Connect call failed ('172.26.0.2', 9092)
+    [558863]: [ERROR] aiokafka: Unable connect to node with id 0: [Errno 111] Connect call failed ('172.26.0.2', 9092)
+    [558865]: [ERROR] aiokafka: Unable to update metadata from [0]
+    [558863]: [ERROR] aiokafka: Unable to update metadata from [0]
     ^C
     Starting process cleanup, this may take a few seconds...
-    [INFO] fastkafka._server: terminate_asyncio_process(): Terminating the process 2559...
-    [INFO] fastkafka._server: terminate_asyncio_process(): Terminating the process 2561...
-    [2561]: [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer stopped.
-    [2561]: [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop() finished.
-    [2561]: [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.stop(): Entering...
-    [2561]: [INFO] fastkafka._components.aiokafka_producer_manager: _aiokafka_producer_manager(): Exiting send_stream
-    [2561]: [INFO] fastkafka._components.aiokafka_producer_manager: _aiokafka_producer_manager(): Finished.
-    [2561]: [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.stop(): Stoping producer...
-    [2561]: [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.stop(): Finished
-    [2559]: [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer stopped.
-    [2559]: [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop() finished.
-    [2559]: [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.stop(): Entering...
-    [2559]: [INFO] fastkafka._components.aiokafka_producer_manager: _aiokafka_producer_manager(): Exiting send_stream
-    [2559]: [INFO] fastkafka._components.aiokafka_producer_manager: _aiokafka_producer_manager(): Finished.
-    [2559]: [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.stop(): Stoping producer...
-    [2559]: [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.stop(): Finished
-    [INFO] fastkafka._server: terminate_asyncio_process(): Process 2561 was already terminated.
-    [INFO] fastkafka._server: terminate_asyncio_process(): Process 2559 was already terminated.
+    [INFO] fastkafka._server: terminate_asyncio_process(): Terminating the process 558863...
+    [INFO] fastkafka._server: terminate_asyncio_process(): Terminating the process 558865...
+    [558863]: [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer stopped.
+    [558863]: [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop() finished.
+    [558863]: [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.stop(): Entering...
+    [558863]: [INFO] fastkafka._components.aiokafka_producer_manager: _aiokafka_producer_manager(): Exiting send_stream
+    [558863]: [INFO] fastkafka._components.aiokafka_producer_manager: _aiokafka_producer_manager(): Finished.
+    [558863]: [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.stop(): Stoping producer...
+    [558863]: [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.stop(): Finished
+    [558865]: [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer stopped.
+    [558865]: [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop() finished.
+    [558865]: [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.stop(): Entering...
+    [558865]: [INFO] fastkafka._components.aiokafka_producer_manager: _aiokafka_producer_manager(): Exiting send_stream
+    [558865]: [INFO] fastkafka._components.aiokafka_producer_manager: _aiokafka_producer_manager(): Finished.
+    [558865]: [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.stop(): Stoping producer...
+    [558865]: [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.stop(): Finished
+    [INFO] fastkafka._server: terminate_asyncio_process(): Process 558863 was already terminated.
+    [INFO] fastkafka._server: terminate_asyncio_process(): Process 558865 was already terminated.
 
 You need to interupt running of the cell above by selecting
 `Runtime->Interupt execution` on the toolbar above.
 
 Finally, we can stop the local Kafka Broker:
 
-    [INFO] fastkafka._testing.local_broker: LocalKafkaBroker.stop(): entering...
-    [INFO] fastkafka._components._subprocess: terminate_asyncio_process(): Terminating the process 2098...
-    [INFO] fastkafka._components._subprocess: terminate_asyncio_process(): Process 2098 was already terminated.
-    [INFO] fastkafka._components._subprocess: terminate_asyncio_process(): Terminating the process 1725...
-    [INFO] fastkafka._components._subprocess: terminate_asyncio_process(): Process 1725 was already terminated.
-    [INFO] fastkafka._testing.local_broker: LocalKafkaBroker.stop(): exited.
+``` python
+broker.stop()
+```
+
+    [INFO] fastkafka._testing.apache_kafka_broker: ApacheKafkaBroker.stop(): entering...
+    [INFO] fastkafka._components._subprocess: terminate_asyncio_process(): Terminating the process 558265...
+    [INFO] fastkafka._components._subprocess: terminate_asyncio_process(): Process 558265 was already terminated.
+    [INFO] fastkafka._components._subprocess: terminate_asyncio_process(): Terminating the process 557885...
+    [INFO] fastkafka._components._subprocess: terminate_asyncio_process(): Process 557885 was already terminated.
+    [INFO] fastkafka._testing.apache_kafka_broker: ApacheKafkaBroker.stop(): exited.
 
 ## Documentation
 
 The kafka app comes with builtin documentation generation using
 [AsyncApi HTML generator](https://www.asyncapi.com/tools/generator).
 
 AsyncApi requires Node.js to be installed and we provide the following
 convenience command line for it:
 
 ``` sh
 fastkafka docs install_deps
 ```
 
-    [INFO] fastkafka._components.asyncapi: AsyncAPI generator installed
+    [INFO] fastkafka._components.docs_dependencies: AsyncAPI generator installed
 
 To generate the documentation programatically you just need to call the
 folloving command:
 
 ``` sh
 fastkafka docs generate application:kafka_app
 ```
 
+    [INFO] fastkafka._components.asyncapi: Old async specifications at '/work/fastkafka/nbs/asyncapi/spec/asyncapi.yml' does not exist.
     [INFO] fastkafka._components.asyncapi: New async specifications generated at: '/work/fastkafka/nbs/asyncapi/spec/asyncapi.yml'
     [INFO] fastkafka._components.asyncapi: Async docs generated at 'asyncapi/docs'
     [INFO] fastkafka._components.asyncapi: Output of '$ npx -y -p @asyncapi/generator ag asyncapi/spec/asyncapi.yml @asyncapi/html-template -o asyncapi/docs --force-write'
 
     Done! ✨
     Check out your shiny new generated files at /work/fastkafka/nbs/asyncapi/docs.
 
@@ -555,16 +591,16 @@
 with:
 
 ``` sh
 ls -l asyncapi
 ```
 
     total 8
-    drwxrwxr-x 4 kumaran kumaran 4096 Mar 21 09:14 docs
-    drwxrwxr-x 2 kumaran kumaran 4096 Mar 21 09:14 spec
+    drwxrwxr-x 4 tvrtko tvrtko 4096 Apr  5 08:02 docs
+    drwxrwxr-x 2 tvrtko tvrtko 4096 Apr  5 08:02 spec
 
 In docs folder you will find the servable static html file of your
 documentation. This can also be served using our `fastkafka docs serve`
 CLI command (more on that in our guides).
 
 In spec folder you will find a asyncapi.yml file containing the async
 API specification of your application.
```

### Comparing `fastkafka-0.4.0rc0/fastkafka/_application/app.py` & `fastkafka-0.4.0rc1/fastkafka/_application/app.py`

 * *Files identical despite different names*

### Comparing `fastkafka-0.4.0rc0/fastkafka/_application/tester.py` & `fastkafka-0.4.0rc1/fastkafka/_application/tester.py`

 * *Files identical despite different names*

### Comparing `fastkafka-0.4.0rc0/fastkafka/_cli.py` & `fastkafka-0.4.0rc1/fastkafka/_cli.py`

 * *Files identical despite different names*

### Comparing `fastkafka-0.4.0rc0/fastkafka/_cli_docs.py` & `fastkafka-0.4.0rc1/fastkafka/_cli_docs.py`

 * *Files identical despite different names*

### Comparing `fastkafka-0.4.0rc0/fastkafka/_cli_testing.py` & `fastkafka-0.4.0rc1/fastkafka/_cli_testing.py`

 * *Files identical despite different names*

### Comparing `fastkafka-0.4.0rc0/fastkafka/_components/_subprocess.py` & `fastkafka-0.4.0rc1/fastkafka/_components/_subprocess.py`

 * *Files identical despite different names*

### Comparing `fastkafka-0.4.0rc0/fastkafka/_components/aiokafka_consumer_loop.py` & `fastkafka-0.4.0rc1/fastkafka/_components/aiokafka_consumer_loop.py`

 * *Files identical despite different names*

### Comparing `fastkafka-0.4.0rc0/fastkafka/_components/aiokafka_producer_manager.py` & `fastkafka-0.4.0rc1/fastkafka/_components/aiokafka_producer_manager.py`

 * *Files identical despite different names*

### Comparing `fastkafka-0.4.0rc0/fastkafka/_components/asyncapi.py` & `fastkafka-0.4.0rc1/fastkafka/_components/asyncapi.py`

 * *Files identical despite different names*

### Comparing `fastkafka-0.4.0rc0/fastkafka/_components/benchmarking.py` & `fastkafka-0.4.0rc1/fastkafka/_components/benchmarking.py`

 * *Files identical despite different names*

### Comparing `fastkafka-0.4.0rc0/fastkafka/_components/docs_dependencies.py` & `fastkafka-0.4.0rc1/fastkafka/_components/docs_dependencies.py`

 * *Files identical despite different names*

### Comparing `fastkafka-0.4.0rc0/fastkafka/_components/helpers.py` & `fastkafka-0.4.0rc1/fastkafka/_components/helpers.py`

 * *Files identical despite different names*

### Comparing `fastkafka-0.4.0rc0/fastkafka/_components/logger.py` & `fastkafka-0.4.0rc1/fastkafka/_components/logger.py`

 * *Files identical despite different names*

### Comparing `fastkafka-0.4.0rc0/fastkafka/_components/meta.py` & `fastkafka-0.4.0rc1/fastkafka/_components/meta.py`

 * *Files identical despite different names*

### Comparing `fastkafka-0.4.0rc0/fastkafka/_components/producer_decorator.py` & `fastkafka-0.4.0rc1/fastkafka/_components/producer_decorator.py`

 * *Files identical despite different names*

### Comparing `fastkafka-0.4.0rc0/fastkafka/_components/test_dependencies.py` & `fastkafka-0.4.0rc1/fastkafka/_components/test_dependencies.py`

 * *Files identical despite different names*

### Comparing `fastkafka-0.4.0rc0/fastkafka/_docusaurus_helper.py` & `fastkafka-0.4.0rc1/fastkafka/_docusaurus_helper.py`

 * *Files identical despite different names*

### Comparing `fastkafka-0.4.0rc0/fastkafka/_helpers.py` & `fastkafka-0.4.0rc1/fastkafka/_helpers.py`

 * *Files identical despite different names*

### Comparing `fastkafka-0.4.0rc0/fastkafka/_modidx.py` & `fastkafka-0.4.0rc1/fastkafka/_modidx.py`

 * *Files identical despite different names*

### Comparing `fastkafka-0.4.0rc0/fastkafka/_server.py` & `fastkafka-0.4.0rc1/fastkafka/_server.py`

 * *Files identical despite different names*

### Comparing `fastkafka-0.4.0rc0/fastkafka/_testing/apache_kafka_broker.py` & `fastkafka-0.4.0rc1/fastkafka/_testing/apache_kafka_broker.py`

 * *Files identical despite different names*

### Comparing `fastkafka-0.4.0rc0/fastkafka/_testing/in_memory_broker.py` & `fastkafka-0.4.0rc1/fastkafka/_testing/in_memory_broker.py`

 * *Files identical despite different names*

### Comparing `fastkafka-0.4.0rc0/fastkafka/_testing/local_redpanda_broker.py` & `fastkafka-0.4.0rc1/fastkafka/_testing/local_redpanda_broker.py`

 * *Files 1% similar despite different names*

```diff
@@ -224,15 +224,15 @@
 
         redpanda_docker_cmd = get_redpanda_docker_cmd(**self.redpanda_kwargs)  # type: ignore
 
         try:
             service_task = await run_and_match(
                 *redpanda_docker_cmd,
                 capture="stderr",
-                pattern="Successfully started Redpanda",
+                pattern="Bootstrap complete",
                 timeout=30,
             )
         except Exception as e:
             logger.info(
                 f"{service} startup failed, generating a new port and retrying..."
             )
             port = get_free_port()
@@ -280,14 +280,15 @@
 async def _start(self: LocalRedpandaBroker) -> str:
     await self._check_deps()
 
     self.temporary_directory = TemporaryDirectory()
     self.temporary_directory_path = Path(self.temporary_directory.__enter__())
 
     await self._start_redpanda()
+    await asyncio.sleep(5)
 
     listener_port = self.redpanda_kwargs.get("listener_port", 9092)
     bootstrap_server = f"127.0.0.1:{listener_port}"
     logger.info(f"Local Redpanda broker up and running on {bootstrap_server}")
 
     await self._create_topics()
```

### Comparing `fastkafka-0.4.0rc0/fastkafka/_testing/test_utils.py` & `fastkafka-0.4.0rc1/fastkafka/_testing/test_utils.py`

 * *Files identical despite different names*

### Comparing `fastkafka-0.4.0rc0/fastkafka/testing.py` & `fastkafka-0.4.0rc1/fastkafka/testing.py`

 * *Files identical despite different names*

### Comparing `fastkafka-0.4.0rc0/fastkafka.egg-info/PKG-INFO` & `fastkafka-0.4.0rc1/fastkafka.egg-info/PKG-INFO`

 * *Files 8% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: fastkafka
-Version: 0.4.0rc0
+Version: 0.4.0rc1
 Summary: FastKafka is a powerful and easy-to-use Python library for building asynchronous web services that interact with Kafka topics. Built on top of FastAPI, Starlette, Pydantic, AIOKafka and AsyncAPI, FastKafka simplifies the process of writing producers and consumers for Kafka topics.
 Home-page: https://github.com/airtai/fastkafka
 Author: airt
 Author-email: info@airt.ai
 License: Apache Software License 2.0
 Project-URL: Bug Tracker, https://github.com/airtai/fastkafka/issues
 Project-URL: CI, https://github.com/airtai/fastkafka/actions
@@ -60,20 +60,30 @@
 With FastKafka, you can quickly prototype and develop high-performance
 Kafka-based services with minimal code, making it an ideal choice for
 developers looking to streamline their workflow and accelerate their
 projects.
 
 ------------------------------------------------------------------------
 
-#### ⭐ Stay in touch
+#### ⭐⭐⭐ Stay in touch ⭐⭐⭐
 
-Please show your support and stay in touch by giving our [GitHub
-repository](https://github.com/airtai/fastkafka/) a star! Your support
-helps us to stay in touch with you and encourages us to continue
-developing and improving the library. Thank you for your support!
+Please show your support and stay in touch by:
+
+- giving our [GitHub repository](https://github.com/airtai/fastkafka/) a
+  star, and
+
+- joining our [Discord server](https://discord.gg/CJWmYpyFbc).
+
+Your support helps us to stay in touch with you and encourages us to
+continue developing and improving the library. Thank you for your
+support!
+
+------------------------------------------------------------------------
+
+#### 🐝🐝🐝 We were busy lately 🐝🐝🐝
 
 ![Activity](https://repobeats.axiom.co/api/embed/21f36049093d5eb8e5fdad18c3c5d8df5428ca30.svg "Repobeats analytics image")
 
 ## Install
 
 FastKafka works on macOS, Linux, and most Unix-style operating systems.
 You can install base version of `fastkafka` with `pip` as usual:
@@ -102,44 +112,54 @@
 
 ## Tutorial
 
 You can start an interactive tutorial in Google Colab by clicking the
 button below:
 
 <a href="https://colab.research.google.com/github/airtai/fastkafka/blob/main/nbs/guides/Guide_00_FastKafka_Demo.ipynb" target=”_blank”>
-<img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab">
+<img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" />
 </a>
 
 ## Writing server code
 
 Here is an example python script using FastKafka that takes data from a
 Kafka topic, makes a prediction using a predictive model, and outputs
 the prediction to another Kafka topic.
 
 ### Preparing the demo model
 
 First we will prepare our model using the Iris dataset so that we can
 demonstrate the predictions using FastKafka. The following call
 downloads the dataset and trains the model.
 
+We will wrap the model creation into a lifespan of our app so that the
+model is created just before the app is started.
+
 ``` python
+from contextlib import asynccontextmanager
+
 from sklearn.datasets import load_iris
 from sklearn.linear_model import LogisticRegression
 
-X, y = load_iris(return_X_y=True)
-model = LogisticRegression(random_state=0, max_iter=500).fit(X, y)
-x = X[[0, 55, -1]]
-print(x)
-print(model.predict(x))
-```
+from fastkafka import FastKafka
+
+ml_models = {}
 
-    [[5.1 3.5 1.4 0.2]
-     [5.7 2.8 4.5 1.3]
-     [5.9 3.  5.1 1.8]]
-    [0 1 2]
+
+@asynccontextmanager
+async def lifespan(app: FastKafka):
+    # Load the ML model
+    X, y = load_iris(return_X_y=True)
+    ml_models["iris_predictor"] = LogisticRegression(random_state=0, max_iter=500).fit(
+        X, y
+    )
+    yield
+    # Clean up the ML models and release the resources
+    ml_models.clear()
+```
 
 ### Messages
 
 FastKafka uses [Pydantic](https://docs.pydantic.dev/) to parse input
 JSON-encoded data into Python objects, making it easy to work with
 structured data in your Kafka-based applications. Pydantic’s
 [`BaseModel`](https://docs.pydantic.dev/usage/models/) class allows you
@@ -193,15 +213,15 @@
 contains two entries: `"localhost"` and `"production"`, specifying local
 development and production Kafka brokers. Each entry specifies the URL,
 port, and other details of a Kafka broker. This dictionary is used for
 both generating the documentation and later to run the actual server
 against one of the given kafka broker.
 
 Next, an object of the
-[`FastKafka`](https://airtai.github.io/fastkafka/0.3.0/api/fastkafka/FastKafka/#fastkafka.FastKafka)
+[`FastKafka`](https://airtai.github.io/fastkafka/0.4.0rc1/api/fastkafka/FastKafka/#fastkafka.FastKafka)
 class is initialized with the minimum set of arguments:
 
 - `kafka_brokers`: a dictionary used for generation of documentation
 
 ``` python
 from fastkafka import FastKafka
 
@@ -219,14 +239,15 @@
         "security": {"type": "plain"},
     },
 }
 
 kafka_app = FastKafka(
     title="Iris predictions",
     kafka_brokers=kafka_brokers,
+    lifespan=lifespan,
 )
 ```
 
 ### Function decorators
 
 FastKafka provides convenient function decorators `@kafka_app.consumes`
 and `@kafka_app.produces` to allow you to delegate the actual process of
@@ -264,15 +285,15 @@
   The framework will call the `IrisPrediction.json().encode("utf-8")`
   function on the returned value and produce it to the specified topic.
 
 ``` python
 @kafka_app.consumes(topic="input_data", auto_offset_reset="latest")
 async def on_input_data(msg: IrisInputData):
     global model
-    species_class = model.predict(
+    species_class = ml_models["iris_predictor"].predict(
         [[msg.sepal_length, msg.sepal_width, msg.petal_length, msg.petal_width]]
     )[0]
 
     to_predictions(species_class)
 
 
 @kafka_app.produces(topic="predictions")
@@ -282,94 +303,83 @@
     prediction = IrisPrediction(species=iris_species[species_class])
     return prediction
 ```
 
 ## Testing the service
 
 The service can be tested using the
-[`Tester`](https://airtai.github.io/fastkafka/0.3.0/api/fastkafka/testing/Tester/#fastkafka.testing.Tester)
-instances which internally starts Kafka broker and zookeeper.
-
-Before running tests, we have to install Java runtime and Apache Kafka
-locally. To simplify the process, we provide the following convenience
-command:
-
-``` sh
-fastkafka testing install_deps
-```
-
-    [INFO] fastkafka._components.test_dependencies: Installing Java...
-    [INFO] fastkafka._components.test_dependencies:  - installing jdk...
-    [INFO] fastkafka._components.test_dependencies:  - jdk path: /home/kumaran/.jdk/jdk-11.0.18+10
-    [INFO] fastkafka._components.test_dependencies: Java installed.
-    [INFO] fastkafka._components.test_dependencies: Installing Kafka...
-    832969it [00:02, 309324.60it/s]                                                 
-    [INFO] fastkafka._components.test_dependencies: Kafka installed in /home/kumaran/.local/kafka_2.13-3.3.2.
+[`Tester`](https://airtai.github.io/fastkafka/0.4.0rc1/api/fastkafka/testing/Tester/#fastkafka.testing.Tester)
+instances which internally starts InMemory implementation of Kafka
+broker.
+
+The Tester will redirect your consumes and produces decorated functions
+to the InMemory Kafka broker so that you can quickly test your app
+without the need for a running Kafka broker and all its dependencies.
 
 ``` python
 from fastkafka.testing import Tester
 
 msg = IrisInputData(
     sepal_length=0.1,
     sepal_width=0.2,
     petal_length=0.3,
     petal_width=0.4,
 )
 
-# Start Tester app and create local Kafka broker for testing
+# Start Tester app and create InMemory Kafka broker for testing
 async with Tester(kafka_app) as tester:
     # Send IrisInputData message to input_data topic
     await tester.to_input_data(msg)
 
     # Assert that the kafka_app responded with IrisPrediction in predictions topic
     await tester.awaited_mocks.on_predictions.assert_awaited_with(
         IrisPrediction(species="setosa"), timeout=2
     )
 ```
 
-    [INFO] fastkafka._components.test_dependencies: Java is already installed.
-    [INFO] fastkafka._components.test_dependencies: But not exported to PATH, exporting...
-    [INFO] fastkafka._components.test_dependencies: Kafka is installed.
-    [INFO] fastkafka._components.test_dependencies: But not exported to PATH, exporting...
-    [INFO] fastkafka._testing.local_broker: Starting zookeeper...
-    [INFO] fastkafka._testing.local_broker: Starting kafka...
-    [INFO] fastkafka._testing.local_broker: Local Kafka broker up and running on 127.0.0.1:9092
-    [INFO] fastkafka._application.app: _create_producer() : created producer using the config: '{'bootstrap_servers': '127.0.0.1:9092'}'
+    [INFO] fastkafka._testing.in_memory_broker: InMemoryBroker._start() called
+    [INFO] fastkafka._testing.in_memory_broker: InMemoryBroker._patch_consumers_and_producers(): Patching consumers and producers!
+    [INFO] fastkafka._testing.in_memory_broker: InMemoryBroker starting
+    [INFO] fastkafka._application.app: _create_producer() : created producer using the config: '{'bootstrap_servers': 'localhost:9092'}'
     [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.start(): Entering...
+    [INFO] fastkafka._testing.in_memory_broker: AIOKafkaProducer patched start() called()
     [INFO] fastkafka._components.aiokafka_producer_manager: _aiokafka_producer_manager(): Starting...
     [INFO] fastkafka._components.aiokafka_producer_manager: _aiokafka_producer_manager(): Starting send_stream
     [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.start(): Finished.
-    [INFO] fastkafka._application.app: _create_producer() : created producer using the config: '{'bootstrap_servers': '127.0.0.1:9092'}'
+    [INFO] fastkafka._application.app: _create_producer() : created producer using the config: '{'bootstrap_servers': 'localhost:9092'}'
+    [INFO] fastkafka._testing.in_memory_broker: AIOKafkaProducer patched start() called()
     [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop() starting...
-    [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer created using the following parameters: {'bootstrap_servers': '127.0.0.1:9092', 'auto_offset_reset': 'latest', 'max_poll_records': 100}
+    [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer created using the following parameters: {'bootstrap_servers': 'localhost:9092', 'auto_offset_reset': 'latest', 'max_poll_records': 100}
+    [INFO] fastkafka._testing.in_memory_broker: AIOKafkaConsumer patched start() called()
     [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer started.
-    [INFO] aiokafka.consumer.subscription_state: Updating subscribed topics to: frozenset({'input_data'})
-    [INFO] aiokafka.consumer.consumer: Subscribed to topic(s): {'input_data'}
+    [INFO] fastkafka._testing.in_memory_broker: AIOKafkaConsumer patched subscribe() called
+    [INFO] fastkafka._testing.in_memory_broker: AIOKafkaConsumer.subscribe(), subscribing to: ['input_data']
     [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer subscribed.
     [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop() starting...
-    [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer created using the following parameters: {'bootstrap_servers': '127.0.0.1:9092', 'auto_offset_reset': 'earliest', 'max_poll_records': 100}
-    [INFO] aiokafka.consumer.group_coordinator: Metadata for topic has changed from {} to {'input_data': 1}. 
+    [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer created using the following parameters: {'bootstrap_servers': 'localhost:9092', 'auto_offset_reset': 'earliest', 'max_poll_records': 100}
+    [INFO] fastkafka._testing.in_memory_broker: AIOKafkaConsumer patched start() called()
     [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer started.
-    [INFO] aiokafka.consumer.subscription_state: Updating subscribed topics to: frozenset({'predictions'})
-    [INFO] aiokafka.consumer.consumer: Subscribed to topic(s): {'predictions'}
+    [INFO] fastkafka._testing.in_memory_broker: AIOKafkaConsumer patched subscribe() called
+    [INFO] fastkafka._testing.in_memory_broker: AIOKafkaConsumer.subscribe(), subscribing to: ['predictions']
     [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer subscribed.
-    [INFO] aiokafka.consumer.group_coordinator: Metadata for topic has changed from {} to {'predictions': 1}. 
+    [INFO] fastkafka._testing.in_memory_broker: AIOKafkaConsumer patched stop() called
     [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer stopped.
     [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop() finished.
+    [INFO] fastkafka._testing.in_memory_broker: AIOKafkaProducer patched stop() called
+    [INFO] fastkafka._testing.in_memory_broker: AIOKafkaConsumer patched stop() called
     [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer stopped.
     [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop() finished.
     [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.stop(): Entering...
     [INFO] fastkafka._components.aiokafka_producer_manager: _aiokafka_producer_manager(): Exiting send_stream
     [INFO] fastkafka._components.aiokafka_producer_manager: _aiokafka_producer_manager(): Finished.
     [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.stop(): Stoping producer...
+    [INFO] fastkafka._testing.in_memory_broker: AIOKafkaProducer patched stop() called
     [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.stop(): Finished
-    [INFO] fastkafka._components._subprocess: terminate_asyncio_process(): Terminating the process 547...
-    [INFO] fastkafka._components._subprocess: terminate_asyncio_process(): Process 547 terminated.
-    [INFO] fastkafka._components._subprocess: terminate_asyncio_process(): Terminating the process 173...
-    [INFO] fastkafka._components._subprocess: terminate_asyncio_process(): Process 173 terminated.
+    [INFO] fastkafka._testing.in_memory_broker: InMemoryBroker._stop() called
+    [INFO] fastkafka._testing.in_memory_broker: InMemoryBroker stopping
 
 ### Recap
 
 We have created a Iris classification model and encapulated it into our
 fastkafka application. The app will consume the IrisInputData from the
 `input_data` topic and produce the predictions to `predictions` topic.
 
@@ -453,129 +463,155 @@
     prediction = IrisPrediction(species=iris_species[species_class])
     return prediction
 ```
 
 To run the service, you will need a running Kafka broker on localhost as
 specified in the `kafka_brokers` parameter above. We can start the Kafka
 broker locally using the
-[`LocalKafkaBroker`](https://airtai.github.io/fastkafka/0.3.0/api/fastkafka/testing/LocalKafkaBroker/#fastkafka.testing.LocalKafkaBroker).
-Notice that the same happens automatically in the
-[`Tester`](https://airtai.github.io/fastkafka/0.3.0/api/fastkafka/testing/Tester/#fastkafka.testing.Tester)
-as shown above.
-
-    [INFO] fastkafka._testing.local_broker: LocalKafkaBroker.start(): entering...
-    [WARNING] fastkafka._testing.local_broker: LocalKafkaBroker.start(): (<_UnixSelectorEventLoop running=True closed=False debug=False>) is already running!
-    [WARNING] fastkafka._testing.local_broker: LocalKafkaBroker.start(): calling nest_asyncio.apply()
+[`ApacheKafkaBroker`](https://airtai.github.io/fastkafka/0.4.0rc1/api/fastkafka/testing/ApacheKafkaBroker/#fastkafka.testing.ApacheKafkaBroker).
+
+To use
+[`ApacheKafkaBroker`](https://airtai.github.io/fastkafka/0.4.0rc1/api/fastkafka/testing/ApacheKafkaBroker/#fastkafka.testing.ApacheKafkaBroker),
+you need to install JRE and Kafka to your environment. To simplify this
+process, fastkafka comes with a CLI command that does just that, to run
+it, in your terminal execute the following:
+
+``` sh
+fastkafka testing install_deps
+```
+
+Now we can run
+[`ApacheKafkaBroker`](https://airtai.github.io/fastkafka/0.4.0rc1/api/fastkafka/testing/ApacheKafkaBroker/#fastkafka.testing.ApacheKafkaBroker)
+that will start a Kafka broker instance for us.
+
+``` python
+from fastkafka.testing import ApacheKafkaBroker
+
+broker = ApacheKafkaBroker(apply_nest_asyncio=True)
+
+broker.start()
+```
+
+    [INFO] fastkafka._testing.apache_kafka_broker: ApacheKafkaBroker.start(): entering...
+    [WARNING] fastkafka._testing.apache_kafka_broker: ApacheKafkaBroker.start(): (<_UnixSelectorEventLoop running=True closed=False debug=False>) is already running!
+    [WARNING] fastkafka._testing.apache_kafka_broker: ApacheKafkaBroker.start(): calling nest_asyncio.apply()
     [INFO] fastkafka._components.test_dependencies: Java is already installed.
+    [INFO] fastkafka._components.test_dependencies: But not exported to PATH, exporting...
     [INFO] fastkafka._components.test_dependencies: Kafka is installed.
-    [INFO] fastkafka._testing.local_broker: Starting zookeeper...
-    [INFO] fastkafka._testing.local_broker: Starting kafka...
-    [INFO] fastkafka._testing.local_broker: Local Kafka broker up and running on 127.0.0.1:9092
-    [INFO] fastkafka._testing.local_broker: <class 'fastkafka.testing.LocalKafkaBroker'>.start(): returning 127.0.0.1:9092
-    [INFO] fastkafka._testing.local_broker: LocalKafkaBroker.start(): exited.
+    [INFO] fastkafka._components.test_dependencies: But not exported to PATH, exporting...
+    [INFO] fastkafka._testing.apache_kafka_broker: Starting zookeeper...
+    [INFO] fastkafka._testing.apache_kafka_broker: Starting kafka...
+    [INFO] fastkafka._testing.apache_kafka_broker: Local Kafka broker up and running on 127.0.0.1:9092
+    [INFO] fastkafka._testing.apache_kafka_broker: <class 'fastkafka.testing.ApacheKafkaBroker'>.start(): returning 127.0.0.1:9092
+    [INFO] fastkafka._testing.apache_kafka_broker: ApacheKafkaBroker.start(): exited.
 
     '127.0.0.1:9092'
 
 Then, we start the FastKafka service by running the following command in
 the folder where the `application.py` file is located:
 
 ``` sh
 fastkafka run --num-workers=2 --kafka-broker localhost application:kafka_app
 ```
 
 In the above command, we use `--num-workers` option to specify how many
 workers to launch and we use `--kafka-broker` option to specify which
 kafka broker configuration to use from earlier specified `kafka_brokers`
 
-    [2559]: [INFO] fastkafka._application.app: set_kafka_broker() : Setting bootstrap_servers value to 'localhost:9092'
-    [2559]: [INFO] fastkafka._application.app: _create_producer() : created producer using the config: '{'bootstrap_servers': 'localhost:9092'}'
-    [2559]: [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.start(): Entering...
-    [2561]: [INFO] fastkafka._application.app: set_kafka_broker() : Setting bootstrap_servers value to 'localhost:9092'
-    [2561]: [INFO] fastkafka._application.app: _create_producer() : created producer using the config: '{'bootstrap_servers': 'localhost:9092'}'
-    [2561]: [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.start(): Entering...
-    [2559]: [INFO] fastkafka._components.aiokafka_producer_manager: _aiokafka_producer_manager(): Starting...
-    [2559]: [INFO] fastkafka._components.aiokafka_producer_manager: _aiokafka_producer_manager(): Starting send_stream
-    [2559]: [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.start(): Finished.
-    [2561]: [INFO] fastkafka._components.aiokafka_producer_manager: _aiokafka_producer_manager(): Starting...
-    [2561]: [INFO] fastkafka._components.aiokafka_producer_manager: _aiokafka_producer_manager(): Starting send_stream
-    [2561]: [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.start(): Finished.
-    [2559]: [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop() starting...
-    [2559]: [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer created using the following parameters: {'bootstrap_servers': 'localhost:9092', 'auto_offset_reset': 'latest', 'max_poll_records': 100}
-    [2561]: [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop() starting...
-    [2561]: [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer created using the following parameters: {'bootstrap_servers': 'localhost:9092', 'auto_offset_reset': 'latest', 'max_poll_records': 100}
-    [2561]: [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer started.
-    [2559]: [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer started.
-    [2561]: [INFO] aiokafka.consumer.subscription_state: Updating subscribed topics to: frozenset({'input_data'})
-    [2561]: [INFO] aiokafka.consumer.consumer: Subscribed to topic(s): {'input_data'}
-    [2559]: [INFO] aiokafka.consumer.subscription_state: Updating subscribed topics to: frozenset({'input_data'})
-    [2561]: [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer subscribed.
-    [2559]: [INFO] aiokafka.consumer.consumer: Subscribed to topic(s): {'input_data'}
-    [2559]: [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer subscribed.
-    [2561]: [ERROR] aiokafka.cluster: Topic input_data not found in cluster metadata
-    [2561]: [INFO] aiokafka.consumer.group_coordinator: Metadata for topic has changed from {} to {'input_data': 0}. 
-    [2559]: [WARNING] aiokafka.cluster: Topic input_data is not available during auto-create initialization
-    [2559]: [INFO] aiokafka.consumer.group_coordinator: Metadata for topic has changed from {} to {'input_data': 0}. 
-    [2561]: [ERROR] aiokafka: Unable connect to node with id 0: [Errno 111] Connect call failed ('172.22.0.2', 9092)
-    [2559]: [ERROR] aiokafka: Unable connect to node with id 0: [Errno 111] Connect call failed ('172.22.0.2', 9092)
-    [2561]: [ERROR] aiokafka: Unable to update metadata from [0]
-    [2559]: [ERROR] aiokafka: Unable to update metadata from [0]
+    [558863]: [INFO] fastkafka._application.app: set_kafka_broker() : Setting bootstrap_servers value to 'localhost:9092'
+    [558863]: [INFO] fastkafka._application.app: _create_producer() : created producer using the config: '{'bootstrap_servers': 'localhost:9092'}'
+    [558863]: [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.start(): Entering...
+    [558865]: [INFO] fastkafka._application.app: set_kafka_broker() : Setting bootstrap_servers value to 'localhost:9092'
+    [558865]: [INFO] fastkafka._application.app: _create_producer() : created producer using the config: '{'bootstrap_servers': 'localhost:9092'}'
+    [558865]: [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.start(): Entering...
+    [558865]: [INFO] fastkafka._components.aiokafka_producer_manager: _aiokafka_producer_manager(): Starting...
+    [558865]: [INFO] fastkafka._components.aiokafka_producer_manager: _aiokafka_producer_manager(): Starting send_stream
+    [558865]: [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.start(): Finished.
+    [558863]: [INFO] fastkafka._components.aiokafka_producer_manager: _aiokafka_producer_manager(): Starting...
+    [558863]: [INFO] fastkafka._components.aiokafka_producer_manager: _aiokafka_producer_manager(): Starting send_stream
+    [558863]: [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.start(): Finished.
+    [558865]: [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop() starting...
+    [558865]: [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer created using the following parameters: {'bootstrap_servers': 'localhost:9092', 'auto_offset_reset': 'latest', 'max_poll_records': 100}
+    [558863]: [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop() starting...
+    [558863]: [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer created using the following parameters: {'bootstrap_servers': 'localhost:9092', 'auto_offset_reset': 'latest', 'max_poll_records': 100}
+    [558865]: [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer started.
+    [558865]: [INFO] aiokafka.consumer.subscription_state: Updating subscribed topics to: frozenset({'input_data'})
+    [558865]: [INFO] aiokafka.consumer.consumer: Subscribed to topic(s): {'input_data'}
+    [558865]: [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer subscribed.
+    [558863]: [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer started.
+    [558863]: [INFO] aiokafka.consumer.subscription_state: Updating subscribed topics to: frozenset({'input_data'})
+    [558863]: [INFO] aiokafka.consumer.consumer: Subscribed to topic(s): {'input_data'}
+    [558863]: [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer subscribed.
+    [558863]: [ERROR] aiokafka.cluster: Topic input_data not found in cluster metadata
+    [558863]: [INFO] aiokafka.consumer.group_coordinator: Metadata for topic has changed from {} to {'input_data': 0}. 
+    [558865]: [WARNING] aiokafka.cluster: Topic input_data is not available during auto-create initialization
+    [558865]: [INFO] aiokafka.consumer.group_coordinator: Metadata for topic has changed from {} to {'input_data': 0}. 
+    [558865]: [ERROR] aiokafka: Unable connect to node with id 0: [Errno 111] Connect call failed ('172.26.0.2', 9092)
+    [558863]: [ERROR] aiokafka: Unable connect to node with id 0: [Errno 111] Connect call failed ('172.26.0.2', 9092)
+    [558865]: [ERROR] aiokafka: Unable to update metadata from [0]
+    [558863]: [ERROR] aiokafka: Unable to update metadata from [0]
     ^C
     Starting process cleanup, this may take a few seconds...
-    [INFO] fastkafka._server: terminate_asyncio_process(): Terminating the process 2559...
-    [INFO] fastkafka._server: terminate_asyncio_process(): Terminating the process 2561...
-    [2561]: [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer stopped.
-    [2561]: [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop() finished.
-    [2561]: [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.stop(): Entering...
-    [2561]: [INFO] fastkafka._components.aiokafka_producer_manager: _aiokafka_producer_manager(): Exiting send_stream
-    [2561]: [INFO] fastkafka._components.aiokafka_producer_manager: _aiokafka_producer_manager(): Finished.
-    [2561]: [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.stop(): Stoping producer...
-    [2561]: [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.stop(): Finished
-    [2559]: [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer stopped.
-    [2559]: [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop() finished.
-    [2559]: [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.stop(): Entering...
-    [2559]: [INFO] fastkafka._components.aiokafka_producer_manager: _aiokafka_producer_manager(): Exiting send_stream
-    [2559]: [INFO] fastkafka._components.aiokafka_producer_manager: _aiokafka_producer_manager(): Finished.
-    [2559]: [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.stop(): Stoping producer...
-    [2559]: [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.stop(): Finished
-    [INFO] fastkafka._server: terminate_asyncio_process(): Process 2561 was already terminated.
-    [INFO] fastkafka._server: terminate_asyncio_process(): Process 2559 was already terminated.
+    [INFO] fastkafka._server: terminate_asyncio_process(): Terminating the process 558863...
+    [INFO] fastkafka._server: terminate_asyncio_process(): Terminating the process 558865...
+    [558863]: [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer stopped.
+    [558863]: [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop() finished.
+    [558863]: [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.stop(): Entering...
+    [558863]: [INFO] fastkafka._components.aiokafka_producer_manager: _aiokafka_producer_manager(): Exiting send_stream
+    [558863]: [INFO] fastkafka._components.aiokafka_producer_manager: _aiokafka_producer_manager(): Finished.
+    [558863]: [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.stop(): Stoping producer...
+    [558863]: [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.stop(): Finished
+    [558865]: [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop(): Consumer stopped.
+    [558865]: [INFO] fastkafka._components.aiokafka_consumer_loop: aiokafka_consumer_loop() finished.
+    [558865]: [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.stop(): Entering...
+    [558865]: [INFO] fastkafka._components.aiokafka_producer_manager: _aiokafka_producer_manager(): Exiting send_stream
+    [558865]: [INFO] fastkafka._components.aiokafka_producer_manager: _aiokafka_producer_manager(): Finished.
+    [558865]: [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.stop(): Stoping producer...
+    [558865]: [INFO] fastkafka._components.aiokafka_producer_manager: AIOKafkaProducerManager.stop(): Finished
+    [INFO] fastkafka._server: terminate_asyncio_process(): Process 558863 was already terminated.
+    [INFO] fastkafka._server: terminate_asyncio_process(): Process 558865 was already terminated.
 
 You need to interupt running of the cell above by selecting
 `Runtime->Interupt execution` on the toolbar above.
 
 Finally, we can stop the local Kafka Broker:
 
-    [INFO] fastkafka._testing.local_broker: LocalKafkaBroker.stop(): entering...
-    [INFO] fastkafka._components._subprocess: terminate_asyncio_process(): Terminating the process 2098...
-    [INFO] fastkafka._components._subprocess: terminate_asyncio_process(): Process 2098 was already terminated.
-    [INFO] fastkafka._components._subprocess: terminate_asyncio_process(): Terminating the process 1725...
-    [INFO] fastkafka._components._subprocess: terminate_asyncio_process(): Process 1725 was already terminated.
-    [INFO] fastkafka._testing.local_broker: LocalKafkaBroker.stop(): exited.
+``` python
+broker.stop()
+```
+
+    [INFO] fastkafka._testing.apache_kafka_broker: ApacheKafkaBroker.stop(): entering...
+    [INFO] fastkafka._components._subprocess: terminate_asyncio_process(): Terminating the process 558265...
+    [INFO] fastkafka._components._subprocess: terminate_asyncio_process(): Process 558265 was already terminated.
+    [INFO] fastkafka._components._subprocess: terminate_asyncio_process(): Terminating the process 557885...
+    [INFO] fastkafka._components._subprocess: terminate_asyncio_process(): Process 557885 was already terminated.
+    [INFO] fastkafka._testing.apache_kafka_broker: ApacheKafkaBroker.stop(): exited.
 
 ## Documentation
 
 The kafka app comes with builtin documentation generation using
 [AsyncApi HTML generator](https://www.asyncapi.com/tools/generator).
 
 AsyncApi requires Node.js to be installed and we provide the following
 convenience command line for it:
 
 ``` sh
 fastkafka docs install_deps
 ```
 
-    [INFO] fastkafka._components.asyncapi: AsyncAPI generator installed
+    [INFO] fastkafka._components.docs_dependencies: AsyncAPI generator installed
 
 To generate the documentation programatically you just need to call the
 folloving command:
 
 ``` sh
 fastkafka docs generate application:kafka_app
 ```
 
+    [INFO] fastkafka._components.asyncapi: Old async specifications at '/work/fastkafka/nbs/asyncapi/spec/asyncapi.yml' does not exist.
     [INFO] fastkafka._components.asyncapi: New async specifications generated at: '/work/fastkafka/nbs/asyncapi/spec/asyncapi.yml'
     [INFO] fastkafka._components.asyncapi: Async docs generated at 'asyncapi/docs'
     [INFO] fastkafka._components.asyncapi: Output of '$ npx -y -p @asyncapi/generator ag asyncapi/spec/asyncapi.yml @asyncapi/html-template -o asyncapi/docs --force-write'
 
     Done! ✨
     Check out your shiny new generated files at /work/fastkafka/nbs/asyncapi/docs.
 
@@ -584,16 +620,16 @@
 with:
 
 ``` sh
 ls -l asyncapi
 ```
 
     total 8
-    drwxrwxr-x 4 kumaran kumaran 4096 Mar 21 09:14 docs
-    drwxrwxr-x 2 kumaran kumaran 4096 Mar 21 09:14 spec
+    drwxrwxr-x 4 tvrtko tvrtko 4096 Apr  5 08:02 docs
+    drwxrwxr-x 2 tvrtko tvrtko 4096 Apr  5 08:02 spec
 
 In docs folder you will find the servable static html file of your
 documentation. This can also be served using our `fastkafka docs serve`
 CLI command (more on that in our guides).
 
 In spec folder you will find a asyncapi.yml file containing the async
 API specification of your application.
```

### Comparing `fastkafka-0.4.0rc0/fastkafka.egg-info/SOURCES.txt` & `fastkafka-0.4.0rc1/fastkafka.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `fastkafka-0.4.0rc0/fastkafka.egg-info/requires.txt` & `fastkafka-0.4.0rc1/fastkafka.egg-info/requires.txt`

 * *Files identical despite different names*

### Comparing `fastkafka-0.4.0rc0/settings.ini` & `fastkafka-0.4.0rc1/settings.ini`

 * *Files 2% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 [DEFAULT]
 # All sections below are required unless otherwise specified.
 # See https://github.com/fastai/nbdev/blob/master/settings.ini for examples.
 
 ### Python library ###
 repo = fastkafka
 lib_name = %(repo)s
-version = 0.4.0rc0
+version = 0.4.0rc1
 min_python = 3.8
 license = apache2
 
 
 ### nbdev ###
 doc_path = _docs
 lib_path = fastkafka
```

### Comparing `fastkafka-0.4.0rc0/setup.py` & `fastkafka-0.4.0rc1/setup.py`

 * *Files identical despite different names*

