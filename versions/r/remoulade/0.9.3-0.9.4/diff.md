# Comparing `tmp/remoulade-0.9.3.tar.gz` & `tmp/remoulade-0.9.4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/remoulade-0.9.3.tar", last modified: Wed Feb  6 14:38:07 2019, max compression
+gzip compressed data, was "dist/remoulade-0.9.4.tar", last modified: Fri Feb 15 17:21:30 2019, max compression
```

## Comparing `remoulade-0.9.3.tar` & `remoulade-0.9.4.tar`

### file list

```diff
@@ -1,79 +1,79 @@
-drwxrwxr-x   0 arabany   (1000) arabany   (1000)        0 2019-02-06 14:38:07.000000 remoulade-0.9.3/
-drwxrwxr-x   0 arabany   (1000) arabany   (1000)        0 2019-02-06 14:38:07.000000 remoulade-0.9.3/bin/
--rwxrwxr-x   0 arabany   (1000) arabany   (1000)      274 2018-12-04 14:12:00.000000 remoulade-0.9.3/bin/remoulade-gevent
-drwxrwxr-x   0 arabany   (1000) arabany   (1000)        0 2019-02-06 14:38:07.000000 remoulade-0.9.3/remoulade/
--rw-rw-r--   0 arabany   (1000) arabany   (1000)     3617 2018-10-24 14:05:49.000000 remoulade-0.9.3/remoulade/generic.py
--rw-rw-r--   0 arabany   (1000) arabany   (1000)     2735 2018-12-07 14:54:26.000000 remoulade-0.9.3/remoulade/result.py
--rw-rw-r--   0 arabany   (1000) arabany   (1000)     7760 2018-11-20 13:15:23.000000 remoulade-0.9.3/remoulade/actor.py
-drwxrwxr-x   0 arabany   (1000) arabany   (1000)        0 2019-02-06 14:38:07.000000 remoulade-0.9.3/remoulade/brokers/
--rw-rw-r--   0 arabany   (1000) arabany   (1000)     5968 2018-10-25 07:33:12.000000 remoulade-0.9.3/remoulade/brokers/stub.py
--rw-rw-r--   0 arabany   (1000) arabany   (1000)    17532 2018-12-31 10:38:58.000000 remoulade-0.9.3/remoulade/brokers/rabbitmq.py
--rw-rw-r--   0 arabany   (1000) arabany   (1000)     2829 2019-01-28 08:58:45.000000 remoulade-0.9.3/remoulade/brokers/local.py
--rw-rw-r--   0 arabany   (1000) arabany   (1000)      750 2018-10-24 14:05:49.000000 remoulade-0.9.3/remoulade/brokers/__init__.py
--rw-rw-r--   0 arabany   (1000) arabany   (1000)     4307 2018-12-04 13:16:20.000000 remoulade-0.9.3/remoulade/common.py
-drwxrwxr-x   0 arabany   (1000) arabany   (1000)        0 2019-02-06 14:38:07.000000 remoulade-0.9.3/remoulade/cancel/
-drwxrwxr-x   0 arabany   (1000) arabany   (1000)        0 2019-02-06 14:38:07.000000 remoulade-0.9.3/remoulade/cancel/backends/
--rw-rw-r--   0 arabany   (1000) arabany   (1000)     1547 2019-01-18 13:49:20.000000 remoulade-0.9.3/remoulade/cancel/backends/stub.py
--rw-rw-r--   0 arabany   (1000) arabany   (1000)     2630 2019-01-18 13:49:20.000000 remoulade-0.9.3/remoulade/cancel/backends/redis.py
--rw-rw-r--   0 arabany   (1000) arabany   (1000)     1079 2019-01-18 13:49:20.000000 remoulade-0.9.3/remoulade/cancel/backends/__init__.py
--rw-rw-r--   0 arabany   (1000) arabany   (1000)     1657 2019-01-18 13:49:20.000000 remoulade-0.9.3/remoulade/cancel/backend.py
--rw-rw-r--   0 arabany   (1000) arabany   (1000)      915 2019-01-18 13:49:20.000000 remoulade-0.9.3/remoulade/cancel/errors.py
--rw-rw-r--   0 arabany   (1000) arabany   (1000)     3628 2019-01-18 13:49:20.000000 remoulade-0.9.3/remoulade/cancel/middleware.py
--rw-rw-r--   0 arabany   (1000) arabany   (1000)      906 2019-01-18 13:49:20.000000 remoulade-0.9.3/remoulade/cancel/__init__.py
--rw-rw-r--   0 arabany   (1000) arabany   (1000)    13769 2018-12-04 14:12:00.000000 remoulade-0.9.3/remoulade/__main__.py
--rw-rw-r--   0 arabany   (1000) arabany   (1000)     8468 2019-01-18 13:49:20.000000 remoulade-0.9.3/remoulade/composition.py
--rw-rw-r--   0 arabany   (1000) arabany   (1000)     1100 2018-10-24 14:05:49.000000 remoulade-0.9.3/remoulade/watcher.py
--rw-rw-r--   0 arabany   (1000) arabany   (1000)     5393 2019-01-18 13:49:20.000000 remoulade-0.9.3/remoulade/composition_result.py
-drwxrwxr-x   0 arabany   (1000) arabany   (1000)        0 2019-02-06 14:38:07.000000 remoulade-0.9.3/remoulade/middleware/
--rw-rw-r--   0 arabany   (1000) arabany   (1000)     9083 2019-01-18 13:49:20.000000 remoulade-0.9.3/remoulade/middleware/prometheus.py
--rw-rw-r--   0 arabany   (1000) arabany   (1000)     1765 2018-11-23 14:37:19.000000 remoulade-0.9.3/remoulade/middleware/age_limit.py
--rw-rw-r--   0 arabany   (1000) arabany   (1000)     2752 2018-10-24 14:05:49.000000 remoulade-0.9.3/remoulade/middleware/threading.py
--rw-rw-r--   0 arabany   (1000) arabany   (1000)     4528 2019-01-18 13:49:20.000000 remoulade-0.9.3/remoulade/middleware/pipelines.py
--rw-rw-r--   0 arabany   (1000) arabany   (1000)     3655 2018-11-22 09:18:01.000000 remoulade-0.9.3/remoulade/middleware/retries.py
--rw-rw-r--   0 arabany   (1000) arabany   (1000)     3459 2019-01-18 13:49:20.000000 remoulade-0.9.3/remoulade/middleware/shutdown.py
--rw-rw-r--   0 arabany   (1000) arabany   (1000)     3707 2019-01-18 13:49:20.000000 remoulade-0.9.3/remoulade/middleware/time_limit.py
--rw-rw-r--   0 arabany   (1000) arabany   (1000)     1850 2018-10-24 14:05:49.000000 remoulade-0.9.3/remoulade/middleware/callbacks.py
--rw-rw-r--   0 arabany   (1000) arabany   (1000)     5009 2019-01-18 13:49:20.000000 remoulade-0.9.3/remoulade/middleware/middleware.py
--rw-rw-r--   0 arabany   (1000) arabany   (1000)     1755 2018-11-23 14:45:42.000000 remoulade-0.9.3/remoulade/middleware/__init__.py
--rw-rw-r--   0 arabany   (1000) arabany   (1000)    17561 2019-01-18 13:49:20.000000 remoulade-0.9.3/remoulade/worker.py
--rw-rw-r--   0 arabany   (1000) arabany   (1000)     1009 2018-10-24 14:05:49.000000 remoulade-0.9.3/remoulade/logging.py
-drwxrwxr-x   0 arabany   (1000) arabany   (1000)        0 2019-02-06 14:38:07.000000 remoulade-0.9.3/remoulade/rate_limits/
--rw-rw-r--   0 arabany   (1000) arabany   (1000)     2211 2018-10-24 14:05:49.000000 remoulade-0.9.3/remoulade/rate_limits/window.py
-drwxrwxr-x   0 arabany   (1000) arabany   (1000)        0 2019-02-06 14:38:07.000000 remoulade-0.9.3/remoulade/rate_limits/backends/
--rw-rw-r--   0 arabany   (1000) arabany   (1000)     2587 2018-10-24 14:05:49.000000 remoulade-0.9.3/remoulade/rate_limits/backends/stub.py
--rw-rw-r--   0 arabany   (1000) arabany   (1000)     3756 2018-12-04 13:39:08.000000 remoulade-0.9.3/remoulade/rate_limits/backends/redis.py
--rw-rw-r--   0 arabany   (1000) arabany   (1000)     1086 2018-11-12 16:13:47.000000 remoulade-0.9.3/remoulade/rate_limits/backends/__init__.py
--rw-rw-r--   0 arabany   (1000) arabany   (1000)     1808 2018-10-24 14:05:49.000000 remoulade-0.9.3/remoulade/rate_limits/concurrent.py
--rw-rw-r--   0 arabany   (1000) arabany   (1000)     2497 2018-10-24 14:05:49.000000 remoulade-0.9.3/remoulade/rate_limits/rate_limiter.py
--rw-rw-r--   0 arabany   (1000) arabany   (1000)     3032 2018-10-24 14:05:49.000000 remoulade-0.9.3/remoulade/rate_limits/backend.py
--rw-rw-r--   0 arabany   (1000) arabany   (1000)     2637 2018-10-24 14:05:49.000000 remoulade-0.9.3/remoulade/rate_limits/bucket.py
--rw-rw-r--   0 arabany   (1000) arabany   (1000)     1118 2018-10-24 14:05:49.000000 remoulade-0.9.3/remoulade/rate_limits/__init__.py
-drwxrwxr-x   0 arabany   (1000) arabany   (1000)        0 2019-02-06 14:38:07.000000 remoulade-0.9.3/remoulade/results/
-drwxrwxr-x   0 arabany   (1000) arabany   (1000)        0 2019-02-06 14:38:07.000000 remoulade-0.9.3/remoulade/results/backends/
--rw-rw-r--   0 arabany   (1000) arabany   (1000)     2168 2018-12-04 13:16:20.000000 remoulade-0.9.3/remoulade/results/backends/stub.py
--rw-rw-r--   0 arabany   (1000) arabany   (1000)     4872 2019-01-18 09:24:43.000000 remoulade-0.9.3/remoulade/results/backends/redis.py
--rw-rw-r--   0 arabany   (1000) arabany   (1000)     1208 2018-12-04 13:16:20.000000 remoulade-0.9.3/remoulade/results/backends/local.py
--rw-rw-r--   0 arabany   (1000) arabany   (1000)     1133 2018-11-12 16:13:47.000000 remoulade-0.9.3/remoulade/results/backends/__init__.py
--rw-rw-r--   0 arabany   (1000) arabany   (1000)     6996 2018-12-07 14:54:26.000000 remoulade-0.9.3/remoulade/results/backend.py
--rw-rw-r--   0 arabany   (1000) arabany   (1000)     1287 2018-12-04 13:16:20.000000 remoulade-0.9.3/remoulade/results/errors.py
--rw-rw-r--   0 arabany   (1000) arabany   (1000)     4449 2019-02-06 14:14:11.000000 remoulade-0.9.3/remoulade/results/middleware.py
--rw-rw-r--   0 arabany   (1000) arabany   (1000)     1060 2018-12-04 13:16:20.000000 remoulade-0.9.3/remoulade/results/__init__.py
--rw-rw-r--   0 arabany   (1000) arabany   (1000)     1926 2018-12-31 10:13:22.000000 remoulade-0.9.3/remoulade/encoder.py
--rw-rw-r--   0 arabany   (1000) arabany   (1000)     2316 2019-01-18 13:49:20.000000 remoulade-0.9.3/remoulade/errors.py
--rw-rw-r--   0 arabany   (1000) arabany   (1000)    12809 2019-01-18 13:49:20.000000 remoulade-0.9.3/remoulade/broker.py
--rw-rw-r--   0 arabany   (1000) arabany   (1000)     4198 2019-01-18 13:49:20.000000 remoulade-0.9.3/remoulade/message.py
--rw-rw-r--   0 arabany   (1000) arabany   (1000)     2135 2019-02-06 14:36:43.000000 remoulade-0.9.3/remoulade/__init__.py
-drwxrwxr-x   0 arabany   (1000) arabany   (1000)        0 2019-02-06 14:38:07.000000 remoulade-0.9.3/remoulade.egg-info/
--rw-rw-r--   0 arabany   (1000) arabany   (1000)     1875 2019-02-06 14:38:07.000000 remoulade-0.9.3/remoulade.egg-info/SOURCES.txt
--rw-rw-r--   0 arabany   (1000) arabany   (1000)        1 2019-02-06 14:38:07.000000 remoulade-0.9.3/remoulade.egg-info/dependency_links.txt
--rw-rw-r--   0 arabany   (1000) arabany   (1000)     3218 2019-02-06 14:38:07.000000 remoulade-0.9.3/remoulade.egg-info/PKG-INFO
--rw-rw-r--   0 arabany   (1000) arabany   (1000)      484 2019-02-06 14:38:07.000000 remoulade-0.9.3/remoulade.egg-info/requires.txt
--rw-rw-r--   0 arabany   (1000) arabany   (1000)       55 2019-02-06 14:38:07.000000 remoulade-0.9.3/remoulade.egg-info/entry_points.txt
--rw-rw-r--   0 arabany   (1000) arabany   (1000)       10 2019-02-06 14:38:07.000000 remoulade-0.9.3/remoulade.egg-info/top_level.txt
--rw-rw-r--   0 arabany   (1000) arabany   (1000)     2485 2019-01-25 17:11:39.000000 remoulade-0.9.3/setup.py
--rw-rw-r--   0 arabany   (1000) arabany   (1000)     3218 2019-02-06 14:38:07.000000 remoulade-0.9.3/PKG-INFO
--rw-rw-r--   0 arabany   (1000) arabany   (1000)      116 2018-10-24 14:05:49.000000 remoulade-0.9.3/MANIFEST.in
--rw-rw-r--   0 arabany   (1000) arabany   (1000)     1887 2018-11-12 17:35:34.000000 remoulade-0.9.3/README.md
--rw-rw-r--   0 arabany   (1000) arabany   (1000)      453 2019-02-06 14:38:07.000000 remoulade-0.9.3/setup.cfg
--rw-rw-r--   0 arabany   (1000) arabany   (1000)     7650 2018-10-18 13:05:32.000000 remoulade-0.9.3/COPYING.LESSER
--rw-rw-r--   0 arabany   (1000) arabany   (1000)    35147 2018-10-18 13:05:32.000000 remoulade-0.9.3/COPYING
+drwxrwxr-x   0 arabany   (1000) arabany   (1000)        0 2019-02-15 17:21:30.000000 remoulade-0.9.4/
+drwxrwxr-x   0 arabany   (1000) arabany   (1000)        0 2019-02-15 17:21:30.000000 remoulade-0.9.4/bin/
+-rwxrwxr-x   0 arabany   (1000) arabany   (1000)      274 2018-12-04 14:12:00.000000 remoulade-0.9.4/bin/remoulade-gevent
+drwxrwxr-x   0 arabany   (1000) arabany   (1000)        0 2019-02-15 17:21:30.000000 remoulade-0.9.4/remoulade/
+-rw-rw-r--   0 arabany   (1000) arabany   (1000)     3617 2018-10-24 14:05:49.000000 remoulade-0.9.4/remoulade/generic.py
+-rw-rw-r--   0 arabany   (1000) arabany   (1000)     2735 2018-12-07 14:54:26.000000 remoulade-0.9.4/remoulade/result.py
+-rw-rw-r--   0 arabany   (1000) arabany   (1000)     7760 2018-11-20 13:15:23.000000 remoulade-0.9.4/remoulade/actor.py
+drwxrwxr-x   0 arabany   (1000) arabany   (1000)        0 2019-02-15 17:21:30.000000 remoulade-0.9.4/remoulade/brokers/
+-rw-rw-r--   0 arabany   (1000) arabany   (1000)     5968 2018-10-25 07:33:12.000000 remoulade-0.9.4/remoulade/brokers/stub.py
+-rw-rw-r--   0 arabany   (1000) arabany   (1000)    17532 2018-12-31 10:38:58.000000 remoulade-0.9.4/remoulade/brokers/rabbitmq.py
+-rw-rw-r--   0 arabany   (1000) arabany   (1000)     2829 2019-01-28 08:58:45.000000 remoulade-0.9.4/remoulade/brokers/local.py
+-rw-rw-r--   0 arabany   (1000) arabany   (1000)      750 2018-10-24 14:05:49.000000 remoulade-0.9.4/remoulade/brokers/__init__.py
+-rw-rw-r--   0 arabany   (1000) arabany   (1000)     4307 2018-12-04 13:16:20.000000 remoulade-0.9.4/remoulade/common.py
+drwxrwxr-x   0 arabany   (1000) arabany   (1000)        0 2019-02-15 17:21:30.000000 remoulade-0.9.4/remoulade/cancel/
+drwxrwxr-x   0 arabany   (1000) arabany   (1000)        0 2019-02-15 17:21:30.000000 remoulade-0.9.4/remoulade/cancel/backends/
+-rw-rw-r--   0 arabany   (1000) arabany   (1000)     1547 2019-01-18 13:49:20.000000 remoulade-0.9.4/remoulade/cancel/backends/stub.py
+-rw-rw-r--   0 arabany   (1000) arabany   (1000)     2630 2019-01-18 13:49:20.000000 remoulade-0.9.4/remoulade/cancel/backends/redis.py
+-rw-rw-r--   0 arabany   (1000) arabany   (1000)     1079 2019-01-18 13:49:20.000000 remoulade-0.9.4/remoulade/cancel/backends/__init__.py
+-rw-rw-r--   0 arabany   (1000) arabany   (1000)     1657 2019-01-18 13:49:20.000000 remoulade-0.9.4/remoulade/cancel/backend.py
+-rw-rw-r--   0 arabany   (1000) arabany   (1000)      915 2019-01-18 13:49:20.000000 remoulade-0.9.4/remoulade/cancel/errors.py
+-rw-rw-r--   0 arabany   (1000) arabany   (1000)     3628 2019-01-18 13:49:20.000000 remoulade-0.9.4/remoulade/cancel/middleware.py
+-rw-rw-r--   0 arabany   (1000) arabany   (1000)      906 2019-01-18 13:49:20.000000 remoulade-0.9.4/remoulade/cancel/__init__.py
+-rw-rw-r--   0 arabany   (1000) arabany   (1000)    13769 2018-12-04 14:12:00.000000 remoulade-0.9.4/remoulade/__main__.py
+-rw-rw-r--   0 arabany   (1000) arabany   (1000)     8468 2019-01-18 13:49:20.000000 remoulade-0.9.4/remoulade/composition.py
+-rw-rw-r--   0 arabany   (1000) arabany   (1000)     1100 2018-10-24 14:05:49.000000 remoulade-0.9.4/remoulade/watcher.py
+-rw-rw-r--   0 arabany   (1000) arabany   (1000)     5393 2019-01-18 13:49:20.000000 remoulade-0.9.4/remoulade/composition_result.py
+drwxrwxr-x   0 arabany   (1000) arabany   (1000)        0 2019-02-15 17:21:30.000000 remoulade-0.9.4/remoulade/middleware/
+-rw-rw-r--   0 arabany   (1000) arabany   (1000)     9083 2019-01-18 13:49:20.000000 remoulade-0.9.4/remoulade/middleware/prometheus.py
+-rw-rw-r--   0 arabany   (1000) arabany   (1000)     1765 2018-11-23 14:37:19.000000 remoulade-0.9.4/remoulade/middleware/age_limit.py
+-rw-rw-r--   0 arabany   (1000) arabany   (1000)     2752 2018-10-24 14:05:49.000000 remoulade-0.9.4/remoulade/middleware/threading.py
+-rw-rw-r--   0 arabany   (1000) arabany   (1000)     4528 2019-01-18 13:49:20.000000 remoulade-0.9.4/remoulade/middleware/pipelines.py
+-rw-rw-r--   0 arabany   (1000) arabany   (1000)     3655 2018-11-22 09:18:01.000000 remoulade-0.9.4/remoulade/middleware/retries.py
+-rw-rw-r--   0 arabany   (1000) arabany   (1000)     3459 2019-01-18 13:49:20.000000 remoulade-0.9.4/remoulade/middleware/shutdown.py
+-rw-rw-r--   0 arabany   (1000) arabany   (1000)     3707 2019-01-18 13:49:20.000000 remoulade-0.9.4/remoulade/middleware/time_limit.py
+-rw-rw-r--   0 arabany   (1000) arabany   (1000)     1850 2018-10-24 14:05:49.000000 remoulade-0.9.4/remoulade/middleware/callbacks.py
+-rw-rw-r--   0 arabany   (1000) arabany   (1000)     5009 2019-01-18 13:49:20.000000 remoulade-0.9.4/remoulade/middleware/middleware.py
+-rw-rw-r--   0 arabany   (1000) arabany   (1000)     1755 2018-11-23 14:45:42.000000 remoulade-0.9.4/remoulade/middleware/__init__.py
+-rw-rw-r--   0 arabany   (1000) arabany   (1000)    17561 2019-01-18 13:49:20.000000 remoulade-0.9.4/remoulade/worker.py
+-rw-rw-r--   0 arabany   (1000) arabany   (1000)     1009 2018-10-24 14:05:49.000000 remoulade-0.9.4/remoulade/logging.py
+drwxrwxr-x   0 arabany   (1000) arabany   (1000)        0 2019-02-15 17:21:30.000000 remoulade-0.9.4/remoulade/rate_limits/
+-rw-rw-r--   0 arabany   (1000) arabany   (1000)     2211 2018-10-24 14:05:49.000000 remoulade-0.9.4/remoulade/rate_limits/window.py
+drwxrwxr-x   0 arabany   (1000) arabany   (1000)        0 2019-02-15 17:21:30.000000 remoulade-0.9.4/remoulade/rate_limits/backends/
+-rw-rw-r--   0 arabany   (1000) arabany   (1000)     2587 2018-10-24 14:05:49.000000 remoulade-0.9.4/remoulade/rate_limits/backends/stub.py
+-rw-rw-r--   0 arabany   (1000) arabany   (1000)     3756 2018-12-04 13:39:08.000000 remoulade-0.9.4/remoulade/rate_limits/backends/redis.py
+-rw-rw-r--   0 arabany   (1000) arabany   (1000)     1086 2018-11-12 16:13:47.000000 remoulade-0.9.4/remoulade/rate_limits/backends/__init__.py
+-rw-rw-r--   0 arabany   (1000) arabany   (1000)     1808 2018-10-24 14:05:49.000000 remoulade-0.9.4/remoulade/rate_limits/concurrent.py
+-rw-rw-r--   0 arabany   (1000) arabany   (1000)     2497 2018-10-24 14:05:49.000000 remoulade-0.9.4/remoulade/rate_limits/rate_limiter.py
+-rw-rw-r--   0 arabany   (1000) arabany   (1000)     3032 2018-10-24 14:05:49.000000 remoulade-0.9.4/remoulade/rate_limits/backend.py
+-rw-rw-r--   0 arabany   (1000) arabany   (1000)     2637 2018-10-24 14:05:49.000000 remoulade-0.9.4/remoulade/rate_limits/bucket.py
+-rw-rw-r--   0 arabany   (1000) arabany   (1000)     1118 2018-10-24 14:05:49.000000 remoulade-0.9.4/remoulade/rate_limits/__init__.py
+drwxrwxr-x   0 arabany   (1000) arabany   (1000)        0 2019-02-15 17:21:30.000000 remoulade-0.9.4/remoulade/results/
+drwxrwxr-x   0 arabany   (1000) arabany   (1000)        0 2019-02-15 17:21:30.000000 remoulade-0.9.4/remoulade/results/backends/
+-rw-rw-r--   0 arabany   (1000) arabany   (1000)     2168 2018-12-04 13:16:20.000000 remoulade-0.9.4/remoulade/results/backends/stub.py
+-rw-rw-r--   0 arabany   (1000) arabany   (1000)     4993 2019-02-15 17:18:00.000000 remoulade-0.9.4/remoulade/results/backends/redis.py
+-rw-rw-r--   0 arabany   (1000) arabany   (1000)     1208 2018-12-04 13:16:20.000000 remoulade-0.9.4/remoulade/results/backends/local.py
+-rw-rw-r--   0 arabany   (1000) arabany   (1000)     1133 2018-11-12 16:13:47.000000 remoulade-0.9.4/remoulade/results/backends/__init__.py
+-rw-rw-r--   0 arabany   (1000) arabany   (1000)     6996 2018-12-07 14:54:26.000000 remoulade-0.9.4/remoulade/results/backend.py
+-rw-rw-r--   0 arabany   (1000) arabany   (1000)     1287 2018-12-04 13:16:20.000000 remoulade-0.9.4/remoulade/results/errors.py
+-rw-rw-r--   0 arabany   (1000) arabany   (1000)     4449 2019-02-06 14:14:11.000000 remoulade-0.9.4/remoulade/results/middleware.py
+-rw-rw-r--   0 arabany   (1000) arabany   (1000)     1060 2018-12-04 13:16:20.000000 remoulade-0.9.4/remoulade/results/__init__.py
+-rw-rw-r--   0 arabany   (1000) arabany   (1000)     1926 2018-12-31 10:13:22.000000 remoulade-0.9.4/remoulade/encoder.py
+-rw-rw-r--   0 arabany   (1000) arabany   (1000)     2316 2019-01-18 13:49:20.000000 remoulade-0.9.4/remoulade/errors.py
+-rw-rw-r--   0 arabany   (1000) arabany   (1000)    12809 2019-01-18 13:49:20.000000 remoulade-0.9.4/remoulade/broker.py
+-rw-rw-r--   0 arabany   (1000) arabany   (1000)     4198 2019-01-18 13:49:20.000000 remoulade-0.9.4/remoulade/message.py
+-rw-rw-r--   0 arabany   (1000) arabany   (1000)     2135 2019-02-15 17:21:07.000000 remoulade-0.9.4/remoulade/__init__.py
+drwxrwxr-x   0 arabany   (1000) arabany   (1000)        0 2019-02-15 17:21:30.000000 remoulade-0.9.4/remoulade.egg-info/
+-rw-rw-r--   0 arabany   (1000) arabany   (1000)     1875 2019-02-15 17:21:29.000000 remoulade-0.9.4/remoulade.egg-info/SOURCES.txt
+-rw-rw-r--   0 arabany   (1000) arabany   (1000)        1 2019-02-15 17:21:29.000000 remoulade-0.9.4/remoulade.egg-info/dependency_links.txt
+-rw-rw-r--   0 arabany   (1000) arabany   (1000)     3218 2019-02-15 17:21:29.000000 remoulade-0.9.4/remoulade.egg-info/PKG-INFO
+-rw-rw-r--   0 arabany   (1000) arabany   (1000)      484 2019-02-15 17:21:29.000000 remoulade-0.9.4/remoulade.egg-info/requires.txt
+-rw-rw-r--   0 arabany   (1000) arabany   (1000)       55 2019-02-15 17:21:29.000000 remoulade-0.9.4/remoulade.egg-info/entry_points.txt
+-rw-rw-r--   0 arabany   (1000) arabany   (1000)       10 2019-02-15 17:21:29.000000 remoulade-0.9.4/remoulade.egg-info/top_level.txt
+-rw-rw-r--   0 arabany   (1000) arabany   (1000)     2485 2019-01-25 17:11:39.000000 remoulade-0.9.4/setup.py
+-rw-rw-r--   0 arabany   (1000) arabany   (1000)     3218 2019-02-15 17:21:30.000000 remoulade-0.9.4/PKG-INFO
+-rw-rw-r--   0 arabany   (1000) arabany   (1000)      116 2018-10-24 14:05:49.000000 remoulade-0.9.4/MANIFEST.in
+-rw-rw-r--   0 arabany   (1000) arabany   (1000)     1887 2018-11-12 17:35:34.000000 remoulade-0.9.4/README.md
+-rw-rw-r--   0 arabany   (1000) arabany   (1000)      453 2019-02-15 17:21:30.000000 remoulade-0.9.4/setup.cfg
+-rw-rw-r--   0 arabany   (1000) arabany   (1000)     7650 2018-10-18 13:05:32.000000 remoulade-0.9.4/COPYING.LESSER
+-rw-rw-r--   0 arabany   (1000) arabany   (1000)    35147 2018-10-18 13:05:32.000000 remoulade-0.9.4/COPYING
```

### Comparing `remoulade-0.9.3/remoulade/generic.py` & `remoulade-0.9.4/remoulade/generic.py`

 * *Files identical despite different names*

### Comparing `remoulade-0.9.3/remoulade/result.py` & `remoulade-0.9.4/remoulade/result.py`

 * *Files identical despite different names*

### Comparing `remoulade-0.9.3/remoulade/actor.py` & `remoulade-0.9.4/remoulade/actor.py`

 * *Files identical despite different names*

### Comparing `remoulade-0.9.3/remoulade/brokers/stub.py` & `remoulade-0.9.4/remoulade/brokers/stub.py`

 * *Files identical despite different names*

### Comparing `remoulade-0.9.3/remoulade/brokers/rabbitmq.py` & `remoulade-0.9.4/remoulade/brokers/rabbitmq.py`

 * *Files identical despite different names*

### Comparing `remoulade-0.9.3/remoulade/brokers/local.py` & `remoulade-0.9.4/remoulade/brokers/local.py`

 * *Files identical despite different names*

### Comparing `remoulade-0.9.3/remoulade/brokers/__init__.py` & `remoulade-0.9.4/remoulade/brokers/__init__.py`

 * *Files identical despite different names*

### Comparing `remoulade-0.9.3/remoulade/common.py` & `remoulade-0.9.4/remoulade/common.py`

 * *Files identical despite different names*

### Comparing `remoulade-0.9.3/remoulade/cancel/backends/stub.py` & `remoulade-0.9.4/remoulade/cancel/backends/stub.py`

 * *Files identical despite different names*

### Comparing `remoulade-0.9.3/remoulade/cancel/backends/redis.py` & `remoulade-0.9.4/remoulade/cancel/backends/redis.py`

 * *Files identical despite different names*

### Comparing `remoulade-0.9.3/remoulade/cancel/backends/__init__.py` & `remoulade-0.9.4/remoulade/cancel/backends/__init__.py`

 * *Files identical despite different names*

### Comparing `remoulade-0.9.3/remoulade/cancel/backend.py` & `remoulade-0.9.4/remoulade/cancel/backend.py`

 * *Files identical despite different names*

### Comparing `remoulade-0.9.3/remoulade/cancel/errors.py` & `remoulade-0.9.4/remoulade/cancel/errors.py`

 * *Files identical despite different names*

### Comparing `remoulade-0.9.3/remoulade/cancel/middleware.py` & `remoulade-0.9.4/remoulade/cancel/middleware.py`

 * *Files identical despite different names*

### Comparing `remoulade-0.9.3/remoulade/cancel/__init__.py` & `remoulade-0.9.4/remoulade/cancel/__init__.py`

 * *Files identical despite different names*

### Comparing `remoulade-0.9.3/remoulade/__main__.py` & `remoulade-0.9.4/remoulade/__main__.py`

 * *Files identical despite different names*

### Comparing `remoulade-0.9.3/remoulade/composition.py` & `remoulade-0.9.4/remoulade/composition.py`

 * *Files identical despite different names*

### Comparing `remoulade-0.9.3/remoulade/watcher.py` & `remoulade-0.9.4/remoulade/watcher.py`

 * *Files identical despite different names*

### Comparing `remoulade-0.9.3/remoulade/composition_result.py` & `remoulade-0.9.4/remoulade/composition_result.py`

 * *Files identical despite different names*

### Comparing `remoulade-0.9.3/remoulade/middleware/prometheus.py` & `remoulade-0.9.4/remoulade/middleware/prometheus.py`

 * *Files identical despite different names*

### Comparing `remoulade-0.9.3/remoulade/middleware/age_limit.py` & `remoulade-0.9.4/remoulade/middleware/age_limit.py`

 * *Files identical despite different names*

### Comparing `remoulade-0.9.3/remoulade/middleware/threading.py` & `remoulade-0.9.4/remoulade/middleware/threading.py`

 * *Files identical despite different names*

### Comparing `remoulade-0.9.3/remoulade/middleware/pipelines.py` & `remoulade-0.9.4/remoulade/middleware/pipelines.py`

 * *Files identical despite different names*

### Comparing `remoulade-0.9.3/remoulade/middleware/retries.py` & `remoulade-0.9.4/remoulade/middleware/retries.py`

 * *Files identical despite different names*

### Comparing `remoulade-0.9.3/remoulade/middleware/shutdown.py` & `remoulade-0.9.4/remoulade/middleware/shutdown.py`

 * *Files identical despite different names*

### Comparing `remoulade-0.9.3/remoulade/middleware/time_limit.py` & `remoulade-0.9.4/remoulade/middleware/time_limit.py`

 * *Files identical despite different names*

### Comparing `remoulade-0.9.3/remoulade/middleware/callbacks.py` & `remoulade-0.9.4/remoulade/middleware/callbacks.py`

 * *Files identical despite different names*

### Comparing `remoulade-0.9.3/remoulade/middleware/middleware.py` & `remoulade-0.9.4/remoulade/middleware/middleware.py`

 * *Files identical despite different names*

### Comparing `remoulade-0.9.3/remoulade/middleware/__init__.py` & `remoulade-0.9.4/remoulade/middleware/__init__.py`

 * *Files identical despite different names*

### Comparing `remoulade-0.9.3/remoulade/worker.py` & `remoulade-0.9.4/remoulade/worker.py`

 * *Files identical despite different names*

### Comparing `remoulade-0.9.3/remoulade/logging.py` & `remoulade-0.9.4/remoulade/logging.py`

 * *Files identical despite different names*

### Comparing `remoulade-0.9.3/remoulade/rate_limits/window.py` & `remoulade-0.9.4/remoulade/rate_limits/window.py`

 * *Files identical despite different names*

### Comparing `remoulade-0.9.3/remoulade/rate_limits/backends/stub.py` & `remoulade-0.9.4/remoulade/rate_limits/backends/stub.py`

 * *Files identical despite different names*

### Comparing `remoulade-0.9.3/remoulade/rate_limits/backends/redis.py` & `remoulade-0.9.4/remoulade/rate_limits/backends/redis.py`

 * *Files identical despite different names*

### Comparing `remoulade-0.9.3/remoulade/rate_limits/backends/__init__.py` & `remoulade-0.9.4/remoulade/rate_limits/backends/__init__.py`

 * *Files identical despite different names*

### Comparing `remoulade-0.9.3/remoulade/rate_limits/concurrent.py` & `remoulade-0.9.4/remoulade/rate_limits/concurrent.py`

 * *Files identical despite different names*

### Comparing `remoulade-0.9.3/remoulade/rate_limits/rate_limiter.py` & `remoulade-0.9.4/remoulade/rate_limits/rate_limiter.py`

 * *Files identical despite different names*

### Comparing `remoulade-0.9.3/remoulade/rate_limits/backend.py` & `remoulade-0.9.4/remoulade/rate_limits/backend.py`

 * *Files identical despite different names*

### Comparing `remoulade-0.9.3/remoulade/rate_limits/bucket.py` & `remoulade-0.9.4/remoulade/rate_limits/bucket.py`

 * *Files identical despite different names*

### Comparing `remoulade-0.9.3/remoulade/rate_limits/__init__.py` & `remoulade-0.9.4/remoulade/rate_limits/__init__.py`

 * *Files identical despite different names*

### Comparing `remoulade-0.9.3/remoulade/results/backends/stub.py` & `remoulade-0.9.4/remoulade/results/backends/stub.py`

 * *Files identical despite different names*

### Comparing `remoulade-0.9.3/remoulade/results/backends/redis.py` & `remoulade-0.9.4/remoulade/results/backends/redis.py`

 * *Files 2% similar despite different names*

```diff
@@ -72,16 +72,20 @@
         if timeout is None:
             timeout = DEFAULT_TIMEOUT
 
         message_key = self.build_message_key(message)
         timeout = int(timeout / 1000)
         if block and timeout > 0:
             if forget:
-                _, data = self.client.brpop(message_key, timeout=timeout)
-                self.client.lpush(message_key, self.encoder.encode(ForgottenResult.asdict()))
+                result = self.client.brpop(message_key, timeout=timeout)
+                if result:
+                    _, data = result
+                    self.client.lpush(message_key, self.encoder.encode(ForgottenResult.asdict()))
+                else:
+                    data = None
             else:
                 data = self.client.brpoplpush(message_key, message_key, timeout)
 
             if data is None:
                 raise ResultTimeout(message)
 
         else:
```

### Comparing `remoulade-0.9.3/remoulade/results/backends/local.py` & `remoulade-0.9.4/remoulade/results/backends/local.py`

 * *Files identical despite different names*

### Comparing `remoulade-0.9.3/remoulade/results/backends/__init__.py` & `remoulade-0.9.4/remoulade/results/backends/__init__.py`

 * *Files identical despite different names*

### Comparing `remoulade-0.9.3/remoulade/results/backend.py` & `remoulade-0.9.4/remoulade/results/backend.py`

 * *Files identical despite different names*

### Comparing `remoulade-0.9.3/remoulade/results/errors.py` & `remoulade-0.9.4/remoulade/results/errors.py`

 * *Files identical despite different names*

### Comparing `remoulade-0.9.3/remoulade/results/middleware.py` & `remoulade-0.9.4/remoulade/results/middleware.py`

 * *Files identical despite different names*

### Comparing `remoulade-0.9.3/remoulade/results/__init__.py` & `remoulade-0.9.4/remoulade/results/__init__.py`

 * *Files identical despite different names*

### Comparing `remoulade-0.9.3/remoulade/encoder.py` & `remoulade-0.9.4/remoulade/encoder.py`

 * *Files identical despite different names*

### Comparing `remoulade-0.9.3/remoulade/errors.py` & `remoulade-0.9.4/remoulade/errors.py`

 * *Files identical despite different names*

### Comparing `remoulade-0.9.3/remoulade/broker.py` & `remoulade-0.9.4/remoulade/broker.py`

 * *Files identical despite different names*

### Comparing `remoulade-0.9.3/remoulade/message.py` & `remoulade-0.9.4/remoulade/message.py`

 * *Files identical despite different names*

### Comparing `remoulade-0.9.3/remoulade/__init__.py` & `remoulade-0.9.4/remoulade/__init__.py`

 * *Files 0% similar despite different names*

```diff
@@ -60,8 +60,8 @@
     # Middlware
     "Middleware",
 
     # Workers
     "Worker",
 ]
 
-__version__ = "0.9.3"
+__version__ = "0.9.4"
```

### Comparing `remoulade-0.9.3/remoulade.egg-info/SOURCES.txt` & `remoulade-0.9.4/remoulade.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `remoulade-0.9.3/remoulade.egg-info/PKG-INFO` & `remoulade-0.9.4/remoulade.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: remoulade
-Version: 0.9.3
+Version: 0.9.4
 Summary: Background Processing for Python 3.
 Home-page: UNKNOWN
 Author: Wiremind
 Author-email: dev@wiremind.fr
 License: UNKNOWN
 Description: <img src="https://remoulade.readthedocs.io/_static/logo.png" align="right" width="131" />
```

### Comparing `remoulade-0.9.3/setup.py` & `remoulade-0.9.4/setup.py`

 * *Files identical despite different names*

### Comparing `remoulade-0.9.3/PKG-INFO` & `remoulade-0.9.4/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: remoulade
-Version: 0.9.3
+Version: 0.9.4
 Summary: Background Processing for Python 3.
 Home-page: UNKNOWN
 Author: Wiremind
 Author-email: dev@wiremind.fr
 License: UNKNOWN
 Description: <img src="https://remoulade.readthedocs.io/_static/logo.png" align="right" width="131" />
```

### Comparing `remoulade-0.9.3/README.md` & `remoulade-0.9.4/README.md`

 * *Files identical despite different names*

### Comparing `remoulade-0.9.3/COPYING.LESSER` & `remoulade-0.9.4/COPYING.LESSER`

 * *Files identical despite different names*

### Comparing `remoulade-0.9.3/COPYING` & `remoulade-0.9.4/COPYING`

 * *Files identical despite different names*

