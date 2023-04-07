# Comparing `tmp/botocore-a-la-carte-ec2-1.29.98.tar.gz` & `tmp/botocore-a-la-carte-ec2-1.29.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "botocore-a-la-carte-ec2-1.29.98.tar", last modified: Fri Mar 24 01:24:16 2023, max compression
+gzip compressed data, was "botocore-a-la-carte-ec2-1.29.99.tar", last modified: Sat Mar 25 01:22:37 2023, max compression
```

## Comparing `botocore-a-la-carte-ec2-1.29.98.tar` & `botocore-a-la-carte-ec2-1.29.99.tar`

### file list

```diff
@@ -1,57 +1,57 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 01:24:16.785915 botocore-a-la-carte-ec2-1.29.98/
--rw-r--r--   0 runner    (1001) docker     (123)    10174 2023-03-24 01:24:16.000000 botocore-a-la-carte-ec2-1.29.98/LICENSE.txt
--rw-r--r--   0 runner    (1001) docker     (123)      950 2023-03-24 01:24:16.785915 botocore-a-la-carte-ec2-1.29.98/PKG-INFO
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 01:24:16.773914 botocore-a-la-carte-ec2-1.29.98/botocore/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 01:24:16.773914 botocore-a-la-carte-ec2-1.29.98/botocore/data/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 01:24:16.773914 botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 01:24:16.773914 botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2014-09-01/
--rw-r--r--   0 runner    (1001) docker     (123)    14695 2023-03-24 01:23:57.000000 botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2014-09-01/endpoint-rule-set-1.json
--rw-r--r--   0 runner    (1001) docker     (123)     1271 2023-03-24 01:23:57.000000 botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2014-09-01/paginators-1.json
--rw-r--r--   0 runner    (1001) docker     (123)   539923 2023-03-24 01:23:57.000000 botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2014-09-01/service-2.json
--rw-r--r--   0 runner    (1001) docker     (123)     8548 2023-03-24 01:23:57.000000 botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2014-09-01/waiters-2.json
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 01:24:16.777914 botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2014-10-01/
--rw-r--r--   0 runner    (1001) docker     (123)    14695 2023-03-24 01:23:57.000000 botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2014-10-01/endpoint-rule-set-1.json
--rw-r--r--   0 runner    (1001) docker     (123)     1439 2023-03-24 01:23:57.000000 botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2014-10-01/paginators-1.json
--rw-r--r--   0 runner    (1001) docker     (123)   566499 2023-03-24 01:23:57.000000 botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2014-10-01/service-2.json
--rw-r--r--   0 runner    (1001) docker     (123)    11040 2023-03-24 01:23:57.000000 botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2014-10-01/waiters-2.json
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 01:24:16.777914 botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2015-03-01/
--rw-r--r--   0 runner    (1001) docker     (123)    14695 2023-03-24 01:23:57.000000 botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2015-03-01/endpoint-rule-set-1.json
--rw-r--r--   0 runner    (1001) docker     (123)     1439 2023-03-24 01:23:57.000000 botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2015-03-01/paginators-1.json
--rw-r--r--   0 runner    (1001) docker     (123)   588390 2023-03-24 01:23:57.000000 botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2015-03-01/service-2.json
--rw-r--r--   0 runner    (1001) docker     (123)    11040 2023-03-24 01:23:57.000000 botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2015-03-01/waiters-2.json
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 01:24:16.777914 botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2015-04-15/
--rw-r--r--   0 runner    (1001) docker     (123)    14695 2023-03-24 01:23:57.000000 botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2015-04-15/endpoint-rule-set-1.json
--rw-r--r--   0 runner    (1001) docker     (123)     1439 2023-03-24 01:23:57.000000 botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2015-04-15/paginators-1.json
--rw-r--r--   0 runner    (1001) docker     (123)   715324 2023-03-24 01:23:57.000000 botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2015-04-15/service-2.json
--rw-r--r--   0 runner    (1001) docker     (123)    11546 2023-03-24 01:23:57.000000 botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2015-04-15/waiters-2.json
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 01:24:16.777914 botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2015-10-01/
--rw-r--r--   0 runner    (1001) docker     (123)    14695 2023-03-24 01:23:57.000000 botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2015-10-01/endpoint-rule-set-1.json
--rw-r--r--   0 runner    (1001) docker     (123)       44 2023-03-24 01:23:57.000000 botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2015-10-01/examples-1.json
--rw-r--r--   0 runner    (1001) docker     (123)     1793 2023-03-24 01:23:57.000000 botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2015-10-01/paginators-1.json
--rw-r--r--   0 runner    (1001) docker     (123)   847080 2023-03-24 01:23:57.000000 botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2015-10-01/service-2.json
--rw-r--r--   0 runner    (1001) docker     (123)    14823 2023-03-24 01:23:57.000000 botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2015-10-01/waiters-2.json
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 01:24:16.781914 botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2016-04-01/
--rw-r--r--   0 runner    (1001) docker     (123)    14695 2023-03-24 01:23:57.000000 botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2016-04-01/endpoint-rule-set-1.json
--rw-r--r--   0 runner    (1001) docker     (123)   109914 2023-03-24 01:23:57.000000 botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2016-04-01/examples-1.json
--rw-r--r--   0 runner    (1001) docker     (123)     1793 2023-03-24 01:23:57.000000 botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2016-04-01/paginators-1.json
--rw-r--r--   0 runner    (1001) docker     (123)   878250 2023-03-24 01:23:57.000000 botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2016-04-01/service-2.json
--rw-r--r--   0 runner    (1001) docker     (123)    15259 2023-03-24 01:23:57.000000 botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2016-04-01/waiters-2.json
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 01:24:16.781914 botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2016-09-15/
--rw-r--r--   0 runner    (1001) docker     (123)    14695 2023-03-24 01:23:57.000000 botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2016-09-15/endpoint-rule-set-1.json
--rw-r--r--   0 runner    (1001) docker     (123)   110174 2023-03-24 01:23:57.000000 botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2016-09-15/examples-1.json
--rw-r--r--   0 runner    (1001) docker     (123)     1793 2023-03-24 01:23:57.000000 botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2016-09-15/paginators-1.json
--rw-r--r--   0 runner    (1001) docker     (123)   891280 2023-03-24 01:23:57.000000 botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2016-09-15/service-2.json
--rw-r--r--   0 runner    (1001) docker     (123)    14875 2023-03-24 01:23:57.000000 botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2016-09-15/waiters-2.json
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 01:24:16.785915 botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2016-11-15/
--rw-r--r--   0 runner    (1001) docker     (123)    21857 2023-03-24 01:23:57.000000 botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2016-11-15/endpoint-rule-set-1.json
--rw-r--r--   0 runner    (1001) docker     (123)   147949 2023-03-24 01:23:57.000000 botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2016-11-15/examples-1.json
--rw-r--r--   0 runner    (1001) docker     (123)    25701 2023-03-24 01:23:57.000000 botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2016-11-15/paginators-1.json
--rw-r--r--   0 runner    (1001) docker     (123)  2861108 2023-03-24 01:23:57.000000 botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2016-11-15/service-2.json
--rw-r--r--   0 runner    (1001) docker     (123)    17748 2023-03-24 01:23:57.000000 botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2016-11-15/waiters-2.json
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 01:24:16.785915 botocore-a-la-carte-ec2-1.29.98/botocore_a_la_carte_ec2.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)      950 2023-03-24 01:24:16.000000 botocore-a-la-carte-ec2-1.29.98/botocore_a_la_carte_ec2.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     1900 2023-03-24 01:24:16.000000 botocore-a-la-carte-ec2-1.29.98/botocore_a_la_carte_ec2.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-24 01:24:16.000000 botocore-a-la-carte-ec2-1.29.98/botocore_a_la_carte_ec2.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)        9 2023-03-24 01:24:16.000000 botocore-a-la-carte-ec2-1.29.98/botocore_a_la_carte_ec2.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-24 01:24:16.785915 botocore-a-la-carte-ec2-1.29.98/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1130 2023-03-24 01:24:16.000000 botocore-a-la-carte-ec2-1.29.98/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-25 01:22:37.655241 botocore-a-la-carte-ec2-1.29.99/
+-rw-r--r--   0 runner    (1001) docker     (123)    10174 2023-03-25 01:22:37.000000 botocore-a-la-carte-ec2-1.29.99/LICENSE.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      950 2023-03-25 01:22:37.651241 botocore-a-la-carte-ec2-1.29.99/PKG-INFO
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-25 01:22:37.631239 botocore-a-la-carte-ec2-1.29.99/botocore/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-25 01:22:37.631239 botocore-a-la-carte-ec2-1.29.99/botocore/data/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-25 01:22:37.635239 botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-25 01:22:37.635239 botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2014-09-01/
+-rw-r--r--   0 runner    (1001) docker     (123)    14695 2023-03-25 01:22:12.000000 botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2014-09-01/endpoint-rule-set-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)     1271 2023-03-25 01:22:12.000000 botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2014-09-01/paginators-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)   539923 2023-03-25 01:22:12.000000 botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2014-09-01/service-2.json
+-rw-r--r--   0 runner    (1001) docker     (123)     8548 2023-03-25 01:22:12.000000 botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2014-09-01/waiters-2.json
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-25 01:22:37.635239 botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2014-10-01/
+-rw-r--r--   0 runner    (1001) docker     (123)    14695 2023-03-25 01:22:12.000000 botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2014-10-01/endpoint-rule-set-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)     1439 2023-03-25 01:22:12.000000 botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2014-10-01/paginators-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)   566499 2023-03-25 01:22:12.000000 botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2014-10-01/service-2.json
+-rw-r--r--   0 runner    (1001) docker     (123)    11040 2023-03-25 01:22:12.000000 botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2014-10-01/waiters-2.json
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-25 01:22:37.635239 botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2015-03-01/
+-rw-r--r--   0 runner    (1001) docker     (123)    14695 2023-03-25 01:22:12.000000 botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2015-03-01/endpoint-rule-set-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)     1439 2023-03-25 01:22:12.000000 botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2015-03-01/paginators-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)   588390 2023-03-25 01:22:12.000000 botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2015-03-01/service-2.json
+-rw-r--r--   0 runner    (1001) docker     (123)    11040 2023-03-25 01:22:12.000000 botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2015-03-01/waiters-2.json
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-25 01:22:37.639240 botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2015-04-15/
+-rw-r--r--   0 runner    (1001) docker     (123)    14695 2023-03-25 01:22:12.000000 botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2015-04-15/endpoint-rule-set-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)     1439 2023-03-25 01:22:12.000000 botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2015-04-15/paginators-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)   715324 2023-03-25 01:22:12.000000 botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2015-04-15/service-2.json
+-rw-r--r--   0 runner    (1001) docker     (123)    11546 2023-03-25 01:22:12.000000 botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2015-04-15/waiters-2.json
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-25 01:22:37.639240 botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2015-10-01/
+-rw-r--r--   0 runner    (1001) docker     (123)    14695 2023-03-25 01:22:12.000000 botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2015-10-01/endpoint-rule-set-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)       44 2023-03-25 01:22:12.000000 botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2015-10-01/examples-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)     1793 2023-03-25 01:22:12.000000 botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2015-10-01/paginators-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)   847080 2023-03-25 01:22:12.000000 botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2015-10-01/service-2.json
+-rw-r--r--   0 runner    (1001) docker     (123)    14823 2023-03-25 01:22:12.000000 botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2015-10-01/waiters-2.json
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-25 01:22:37.643240 botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2016-04-01/
+-rw-r--r--   0 runner    (1001) docker     (123)    14695 2023-03-25 01:22:12.000000 botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2016-04-01/endpoint-rule-set-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)   109914 2023-03-25 01:22:12.000000 botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2016-04-01/examples-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)     1793 2023-03-25 01:22:12.000000 botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2016-04-01/paginators-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)   878250 2023-03-25 01:22:12.000000 botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2016-04-01/service-2.json
+-rw-r--r--   0 runner    (1001) docker     (123)    15259 2023-03-25 01:22:12.000000 botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2016-04-01/waiters-2.json
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-25 01:22:37.643240 botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2016-09-15/
+-rw-r--r--   0 runner    (1001) docker     (123)    14695 2023-03-25 01:22:12.000000 botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2016-09-15/endpoint-rule-set-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)   110174 2023-03-25 01:22:12.000000 botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2016-09-15/examples-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)     1793 2023-03-25 01:22:12.000000 botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2016-09-15/paginators-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)   891280 2023-03-25 01:22:12.000000 botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2016-09-15/service-2.json
+-rw-r--r--   0 runner    (1001) docker     (123)    14875 2023-03-25 01:22:12.000000 botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2016-09-15/waiters-2.json
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-25 01:22:37.651241 botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2016-11-15/
+-rw-r--r--   0 runner    (1001) docker     (123)    21857 2023-03-25 01:22:12.000000 botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2016-11-15/endpoint-rule-set-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)   147949 2023-03-25 01:22:12.000000 botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2016-11-15/examples-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)    25701 2023-03-25 01:22:12.000000 botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2016-11-15/paginators-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)  2861108 2023-03-25 01:22:12.000000 botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2016-11-15/service-2.json
+-rw-r--r--   0 runner    (1001) docker     (123)    17748 2023-03-25 01:22:12.000000 botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2016-11-15/waiters-2.json
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-25 01:22:37.651241 botocore-a-la-carte-ec2-1.29.99/botocore_a_la_carte_ec2.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)      950 2023-03-25 01:22:37.000000 botocore-a-la-carte-ec2-1.29.99/botocore_a_la_carte_ec2.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     1900 2023-03-25 01:22:37.000000 botocore-a-la-carte-ec2-1.29.99/botocore_a_la_carte_ec2.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-25 01:22:37.000000 botocore-a-la-carte-ec2-1.29.99/botocore_a_la_carte_ec2.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        9 2023-03-25 01:22:37.000000 botocore-a-la-carte-ec2-1.29.99/botocore_a_la_carte_ec2.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-25 01:22:37.655241 botocore-a-la-carte-ec2-1.29.99/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1130 2023-03-25 01:22:37.000000 botocore-a-la-carte-ec2-1.29.99/setup.py
```

### Comparing `botocore-a-la-carte-ec2-1.29.98/LICENSE.txt` & `botocore-a-la-carte-ec2-1.29.99/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `botocore-a-la-carte-ec2-1.29.98/PKG-INFO` & `botocore-a-la-carte-ec2-1.29.99/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: botocore-a-la-carte-ec2
-Version: 1.29.98
+Version: 1.29.99
 Summary: ec2 data for botocore. See the `botocore-a-la-carte` package for more info.
 Home-page: https://github.com/thejcannon/botocore-a-la-carte
 Author: Amazon Web Services
 License: Apache License 2.0
 Platform: UNKNOWN
 Classifier: Development Status :: 5 - Production/Stable
 Classifier: Intended Audience :: Developers
```

### Comparing `botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2014-09-01/endpoint-rule-set-1.json` & `botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2014-09-01/endpoint-rule-set-1.json`

 * *Files identical despite different names*

### Comparing `botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2014-09-01/paginators-1.json` & `botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2014-09-01/paginators-1.json`

 * *Files identical despite different names*

### Comparing `botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2014-09-01/service-2.json` & `botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2014-09-01/service-2.json`

 * *Files identical despite different names*

### Comparing `botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2014-09-01/waiters-2.json` & `botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2014-09-01/waiters-2.json`

 * *Files identical despite different names*

### Comparing `botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2014-10-01/endpoint-rule-set-1.json` & `botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2014-10-01/endpoint-rule-set-1.json`

 * *Files identical despite different names*

### Comparing `botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2014-10-01/paginators-1.json` & `botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2014-10-01/paginators-1.json`

 * *Files identical despite different names*

### Comparing `botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2014-10-01/service-2.json` & `botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2014-10-01/service-2.json`

 * *Files identical despite different names*

### Comparing `botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2014-10-01/waiters-2.json` & `botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2014-10-01/waiters-2.json`

 * *Files identical despite different names*

### Comparing `botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2015-03-01/endpoint-rule-set-1.json` & `botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2015-03-01/endpoint-rule-set-1.json`

 * *Files identical despite different names*

### Comparing `botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2015-03-01/paginators-1.json` & `botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2015-03-01/paginators-1.json`

 * *Files identical despite different names*

### Comparing `botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2015-03-01/service-2.json` & `botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2015-03-01/service-2.json`

 * *Files identical despite different names*

### Comparing `botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2015-03-01/waiters-2.json` & `botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2015-03-01/waiters-2.json`

 * *Files identical despite different names*

### Comparing `botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2015-04-15/endpoint-rule-set-1.json` & `botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2015-04-15/endpoint-rule-set-1.json`

 * *Files identical despite different names*

### Comparing `botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2015-04-15/paginators-1.json` & `botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2015-04-15/paginators-1.json`

 * *Files identical despite different names*

### Comparing `botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2015-04-15/service-2.json` & `botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2015-04-15/service-2.json`

 * *Files identical despite different names*

### Comparing `botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2015-04-15/waiters-2.json` & `botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2015-04-15/waiters-2.json`

 * *Files identical despite different names*

### Comparing `botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2015-10-01/endpoint-rule-set-1.json` & `botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2015-10-01/endpoint-rule-set-1.json`

 * *Files identical despite different names*

### Comparing `botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2015-10-01/paginators-1.json` & `botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2015-10-01/paginators-1.json`

 * *Files identical despite different names*

### Comparing `botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2015-10-01/service-2.json` & `botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2015-10-01/service-2.json`

 * *Files identical despite different names*

### Comparing `botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2015-10-01/waiters-2.json` & `botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2015-10-01/waiters-2.json`

 * *Files identical despite different names*

### Comparing `botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2016-04-01/endpoint-rule-set-1.json` & `botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2016-04-01/endpoint-rule-set-1.json`

 * *Files identical despite different names*

### Comparing `botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2016-04-01/examples-1.json` & `botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2016-04-01/examples-1.json`

 * *Files identical despite different names*

### Comparing `botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2016-04-01/paginators-1.json` & `botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2016-04-01/paginators-1.json`

 * *Files identical despite different names*

### Comparing `botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2016-04-01/service-2.json` & `botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2016-04-01/service-2.json`

 * *Files identical despite different names*

### Comparing `botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2016-04-01/waiters-2.json` & `botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2016-04-01/waiters-2.json`

 * *Files identical despite different names*

### Comparing `botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2016-09-15/endpoint-rule-set-1.json` & `botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2016-09-15/endpoint-rule-set-1.json`

 * *Files identical despite different names*

### Comparing `botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2016-09-15/examples-1.json` & `botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2016-09-15/examples-1.json`

 * *Files identical despite different names*

### Comparing `botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2016-09-15/paginators-1.json` & `botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2016-09-15/paginators-1.json`

 * *Files identical despite different names*

### Comparing `botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2016-09-15/service-2.json` & `botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2016-09-15/service-2.json`

 * *Files identical despite different names*

### Comparing `botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2016-09-15/waiters-2.json` & `botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2016-09-15/waiters-2.json`

 * *Files identical despite different names*

### Comparing `botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2016-11-15/endpoint-rule-set-1.json` & `botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2016-11-15/endpoint-rule-set-1.json`

 * *Files identical despite different names*

### Comparing `botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2016-11-15/examples-1.json` & `botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2016-11-15/examples-1.json`

 * *Files identical despite different names*

### Comparing `botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2016-11-15/paginators-1.json` & `botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2016-11-15/paginators-1.json`

 * *Files identical despite different names*

### Comparing `botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2016-11-15/service-2.json` & `botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2016-11-15/service-2.json`

 * *Files identical despite different names*

### Comparing `botocore-a-la-carte-ec2-1.29.98/botocore/data/ec2/2016-11-15/waiters-2.json` & `botocore-a-la-carte-ec2-1.29.99/botocore/data/ec2/2016-11-15/waiters-2.json`

 * *Files identical despite different names*

### Comparing `botocore-a-la-carte-ec2-1.29.98/botocore_a_la_carte_ec2.egg-info/PKG-INFO` & `botocore-a-la-carte-ec2-1.29.99/botocore_a_la_carte_ec2.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: botocore-a-la-carte-ec2
-Version: 1.29.98
+Version: 1.29.99
 Summary: ec2 data for botocore. See the `botocore-a-la-carte` package for more info.
 Home-page: https://github.com/thejcannon/botocore-a-la-carte
 Author: Amazon Web Services
 License: Apache License 2.0
 Platform: UNKNOWN
 Classifier: Development Status :: 5 - Production/Stable
 Classifier: Intended Audience :: Developers
```

### Comparing `botocore-a-la-carte-ec2-1.29.98/botocore_a_la_carte_ec2.egg-info/SOURCES.txt` & `botocore-a-la-carte-ec2-1.29.99/botocore_a_la_carte_ec2.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `botocore-a-la-carte-ec2-1.29.98/setup.py` & `botocore-a-la-carte-ec2-1.29.99/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 #!/usr/bin/env python
 from setuptools import setup
 
 setup(
     name='botocore-a-la-carte-ec2',
-    version="1.29.98",
+    version="1.29.99",
     description='ec2 data for botocore. See the `botocore-a-la-carte` package for more info.',
     author='Amazon Web Services',
     url='https://github.com/thejcannon/botocore-a-la-carte',
     scripts=[],
     packages=["botocore"],
     package_data={
         'botocore': ['data/ec2/*/*.json'],
```

