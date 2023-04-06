# Comparing `tmp/sentry-kafka-schemas-0.0.8.tar.gz` & `tmp/sentry-kafka-schemas-0.0.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "sentry-kafka-schemas-0.0.8.tar", last modified: Tue Mar 14 20:17:34 2023, max compression
+gzip compressed data, was "sentry-kafka-schemas-0.0.9.tar", last modified: Mon Mar 20 10:09:48 2023, max compression
```

## Comparing `sentry-kafka-schemas-0.0.8.tar` & `sentry-kafka-schemas-0.0.9.tar`

### file list

```diff
@@ -1,66 +1,69 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-14 20:17:34.663820 sentry-kafka-schemas-0.0.8/
--rw-r--r--   0 runner    (1001) docker     (123)     4732 2023-03-14 20:17:10.000000 sentry-kafka-schemas-0.0.8/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)      200 2023-03-14 20:17:10.000000 sentry-kafka-schemas-0.0.8/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)      269 2023-03-14 20:17:34.663820 sentry-kafka-schemas-0.0.8/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     2227 2023-03-14 20:17:10.000000 sentry-kafka-schemas-0.0.8/README.md
--rw-r--r--   0 runner    (1001) docker     (123)      366 2023-03-14 20:17:10.000000 sentry-kafka-schemas-0.0.8/pyproject.toml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-14 20:17:34.659820 sentry-kafka-schemas-0.0.8/python/
--rw-r--r--   0 runner    (1001) docker     (123)       59 2023-03-14 20:17:10.000000 sentry-kafka-schemas-0.0.8/python/requirements.txt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-14 20:17:34.659820 sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas/
--rw-r--r--   0 runner    (1001) docker     (123)      174 2023-03-14 20:17:10.000000 sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-14 20:17:34.659820 sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas/examples/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-14 20:17:34.659820 sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas/examples/events/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-14 20:17:34.659820 sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas/examples/events/1/
--rw-r--r--   0 runner    (1001) docker     (123)      216 2023-03-14 20:17:10.000000 sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas/examples/events/1/end-delete-groups.json
--rw-r--r--   0 runner    (1001) docker     (123)      152 2023-03-14 20:17:10.000000 sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas/examples/events/1/end-delete-tag.json
--rw-r--r--   0 runner    (1001) docker     (123)      250 2023-03-14 20:17:10.000000 sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas/examples/events/1/end-merge.json
--rw-r--r--   0 runner    (1001) docker     (123)      316 2023-03-14 20:17:10.000000 sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas/examples/events/1/end-unmerge-hierarchical.json
--rw-r--r--   0 runner    (1001) docker     (123)      268 2023-03-14 20:17:10.000000 sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas/examples/events/1/end-unmerge.json
--rw-r--r--   0 runner    (1001) docker     (123)     1008 2023-03-14 20:17:10.000000 sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas/examples/events/1/errors1
--rw-r--r--   0 runner    (1001) docker     (123)       95 2023-03-14 20:17:10.000000 sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas/examples/events/1/exclude-groups.json
--rw-r--r--   0 runner    (1001) docker     (123)     1639 2023-03-14 20:17:10.000000 sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas/examples/events/1/null-tag-keys.json
--rw-r--r--   0 runner    (1001) docker     (123)     1063 2023-03-14 20:17:10.000000 sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas/examples/events/1/null-values.json
--rw-r--r--   0 runner    (1001) docker     (123)      207 2023-03-14 20:17:10.000000 sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas/examples/events/1/replace-group.json
--rw-r--r--   0 runner    (1001) docker     (123)      216 2023-03-14 20:17:10.000000 sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas/examples/events/1/start-delete-groups.json
--rw-r--r--   0 runner    (1001) docker     (123)      247 2023-03-14 20:17:10.000000 sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas/examples/events/1/start-merge.json
--rw-r--r--   0 runner    (1001) docker     (123)      295 2023-03-14 20:17:10.000000 sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas/examples/events/1/tombstone-events-timestamp.json
--rw-r--r--   0 runner    (1001) docker     (123)      183 2023-03-14 20:17:10.000000 sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas/examples/events/1/tombstone-events.json
--rw-r--r--   0 runner    (1001) docker     (123)     1852 2023-03-14 20:17:10.000000 sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas/examples/events/1/weird-transaction-source.json
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-14 20:17:34.659820 sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas/examples/snuba-generic-metrics/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-14 20:17:34.659820 sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas/examples/snuba-generic-metrics/1/
--rw-r--r--   0 runner    (1001) docker     (123)      373 2023-03-14 20:17:10.000000 sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas/examples/snuba-generic-metrics/1/snuba-generic-metrics1
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-14 20:17:34.659820 sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas/examples/snuba-metrics/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-14 20:17:34.663820 sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas/examples/snuba-metrics/1/
--rw-r--r--   0 runner    (1001) docker     (123)      475 2023-03-14 20:17:10.000000 sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas/examples/snuba-metrics/1/snuba-metrics1
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-14 20:17:34.659820 sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas/examples/snuba-queries/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-14 20:17:34.663820 sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas/examples/snuba-queries/1/
--rw-r--r--   0 runner    (1001) docker     (123)     2630 2023-03-14 20:17:10.000000 sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas/examples/snuba-queries/1/rate-limited-real.json
--rw-r--r--   0 runner    (1001) docker     (123)     5422 2023-03-14 20:17:10.000000 sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas/examples/snuba-queries/1/snuba-queries1.json
--rw-r--r--   0 runner    (1001) docker     (123)     5445 2023-03-14 20:17:10.000000 sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas/examples/snuba-queries/1/with-organization-id.json
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-14 20:17:34.663820 sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas/schema_types/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-14 20:17:32.000000 sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas/schema_types/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    74617 2023-03-14 20:17:32.000000 sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas/schema_types/events_v1.py
--rw-r--r--   0 runner    (1001) docker     (123)      971 2023-03-14 20:17:31.000000 sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas/schema_types/snuba_generic_metrics_v1.py
--rw-r--r--   0 runner    (1001) docker     (123)      932 2023-03-14 20:17:32.000000 sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas/schema_types/snuba_metrics_v1.py
--rw-r--r--   0 runner    (1001) docker     (123)     2794 2023-03-14 20:17:32.000000 sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas/schema_types/snuba_queries_v1.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-14 20:17:34.663820 sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas/schemas/
--rw-r--r--   0 runner    (1001) docker     (123)   107120 2023-03-14 20:17:10.000000 sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas/schemas/events.v1.schema.json
--rw-r--r--   0 runner    (1001) docker     (123)     1946 2023-03-14 20:17:10.000000 sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas/schemas/snuba-generic-metrics.v1.schema.json
--rw-r--r--   0 runner    (1001) docker     (123)     1856 2023-03-14 20:17:10.000000 sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas/schemas/snuba-metrics.v1.schema.json
--rw-r--r--   0 runner    (1001) docker     (123)     6079 2023-03-14 20:17:10.000000 sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas/schemas/snuba-queries.v1.schema.json
--rw-r--r--   0 runner    (1001) docker     (123)     4592 2023-03-14 20:17:10.000000 sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas/sentry_kafka_schemas.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-14 20:17:34.663820 sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas/topics/
--rw-r--r--   0 runner    (1001) docker     (123)      185 2023-03-14 20:17:10.000000 sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas/topics/events.yaml
--rw-r--r--   0 runner    (1001) docker     (123)      234 2023-03-14 20:17:10.000000 sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas/topics/snuba-generic-metrics.yaml
--rw-r--r--   0 runner    (1001) docker     (123)      207 2023-03-14 20:17:10.000000 sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas/topics/snuba-metrics.yaml
--rw-r--r--   0 runner    (1001) docker     (123)      199 2023-03-14 20:17:10.000000 sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas/topics/snuba-queries.yaml
--rw-r--r--   0 runner    (1001) docker     (123)     1076 2023-03-14 20:17:10.000000 sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas/types.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-14 20:17:34.659820 sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)      269 2023-03-14 20:17:34.000000 sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     2670 2023-03-14 20:17:34.000000 sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-14 20:17:34.000000 sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-14 20:17:34.000000 sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas.egg-info/not-zip-safe
--rw-r--r--   0 runner    (1001) docker     (123)       59 2023-03-14 20:17:34.000000 sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       21 2023-03-14 20:17:34.000000 sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-14 20:17:34.663820 sentry-kafka-schemas-0.0.8/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)      770 2023-03-14 20:17:10.000000 sentry-kafka-schemas-0.0.8/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-20 10:09:48.888929 sentry-kafka-schemas-0.0.9/
+-rw-r--r--   0 runner    (1001) docker     (123)     4732 2023-03-20 10:09:24.000000 sentry-kafka-schemas-0.0.9/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)      200 2023-03-20 10:09:24.000000 sentry-kafka-schemas-0.0.9/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)      269 2023-03-20 10:09:48.888929 sentry-kafka-schemas-0.0.9/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     2227 2023-03-20 10:09:24.000000 sentry-kafka-schemas-0.0.9/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)      366 2023-03-20 10:09:24.000000 sentry-kafka-schemas-0.0.9/pyproject.toml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-20 10:09:48.884929 sentry-kafka-schemas-0.0.9/python/
+-rw-r--r--   0 runner    (1001) docker     (123)       59 2023-03-20 10:09:24.000000 sentry-kafka-schemas-0.0.9/python/requirements.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-20 10:09:48.884929 sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas/
+-rw-r--r--   0 runner    (1001) docker     (123)      174 2023-03-20 10:09:24.000000 sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-20 10:09:48.884929 sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas/examples/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-20 10:09:48.884929 sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas/examples/events/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-20 10:09:48.884929 sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas/examples/events/1/
+-rw-r--r--   0 runner    (1001) docker     (123)      216 2023-03-20 10:09:24.000000 sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas/examples/events/1/end-delete-groups.json
+-rw-r--r--   0 runner    (1001) docker     (123)      152 2023-03-20 10:09:24.000000 sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas/examples/events/1/end-delete-tag.json
+-rw-r--r--   0 runner    (1001) docker     (123)      250 2023-03-20 10:09:24.000000 sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas/examples/events/1/end-merge.json
+-rw-r--r--   0 runner    (1001) docker     (123)      316 2023-03-20 10:09:24.000000 sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas/examples/events/1/end-unmerge-hierarchical.json
+-rw-r--r--   0 runner    (1001) docker     (123)      268 2023-03-20 10:09:24.000000 sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas/examples/events/1/end-unmerge.json
+-rw-r--r--   0 runner    (1001) docker     (123)    14995 2023-03-20 10:09:24.000000 sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas/examples/events/1/error-with-null-threads.json
+-rw-r--r--   0 runner    (1001) docker     (123)    15027 2023-03-20 10:09:24.000000 sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas/examples/events/1/error-with-null-values-threads.json
+-rw-r--r--   0 runner    (1001) docker     (123)    65960 2023-03-20 10:09:24.000000 sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas/examples/events/1/error-with-threads.json
+-rw-r--r--   0 runner    (1001) docker     (123)     1008 2023-03-20 10:09:24.000000 sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas/examples/events/1/errors1.json
+-rw-r--r--   0 runner    (1001) docker     (123)       95 2023-03-20 10:09:24.000000 sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas/examples/events/1/exclude-groups.json
+-rw-r--r--   0 runner    (1001) docker     (123)     1639 2023-03-20 10:09:24.000000 sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas/examples/events/1/null-tag-keys.json
+-rw-r--r--   0 runner    (1001) docker     (123)     1063 2023-03-20 10:09:24.000000 sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas/examples/events/1/null-values.json
+-rw-r--r--   0 runner    (1001) docker     (123)      207 2023-03-20 10:09:24.000000 sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas/examples/events/1/replace-group.json
+-rw-r--r--   0 runner    (1001) docker     (123)      216 2023-03-20 10:09:24.000000 sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas/examples/events/1/start-delete-groups.json
+-rw-r--r--   0 runner    (1001) docker     (123)      247 2023-03-20 10:09:24.000000 sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas/examples/events/1/start-merge.json
+-rw-r--r--   0 runner    (1001) docker     (123)      295 2023-03-20 10:09:24.000000 sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas/examples/events/1/tombstone-events-timestamp.json
+-rw-r--r--   0 runner    (1001) docker     (123)      183 2023-03-20 10:09:24.000000 sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas/examples/events/1/tombstone-events.json
+-rw-r--r--   0 runner    (1001) docker     (123)     1852 2023-03-20 10:09:24.000000 sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas/examples/events/1/weird-transaction-source.json
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-20 10:09:48.884929 sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas/examples/snuba-generic-metrics/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-20 10:09:48.884929 sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas/examples/snuba-generic-metrics/1/
+-rw-r--r--   0 runner    (1001) docker     (123)      373 2023-03-20 10:09:24.000000 sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas/examples/snuba-generic-metrics/1/snuba-generic-metrics1
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-20 10:09:48.884929 sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas/examples/snuba-metrics/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-20 10:09:48.884929 sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas/examples/snuba-metrics/1/
+-rw-r--r--   0 runner    (1001) docker     (123)      475 2023-03-20 10:09:24.000000 sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas/examples/snuba-metrics/1/snuba-metrics1
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-20 10:09:48.884929 sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas/examples/snuba-queries/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-20 10:09:48.884929 sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas/examples/snuba-queries/1/
+-rw-r--r--   0 runner    (1001) docker     (123)     2630 2023-03-20 10:09:24.000000 sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas/examples/snuba-queries/1/rate-limited-real.json
+-rw-r--r--   0 runner    (1001) docker     (123)     5422 2023-03-20 10:09:24.000000 sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas/examples/snuba-queries/1/snuba-queries1.json
+-rw-r--r--   0 runner    (1001) docker     (123)     5445 2023-03-20 10:09:24.000000 sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas/examples/snuba-queries/1/with-organization-id.json
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-20 10:09:48.888929 sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas/schema_types/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-20 10:09:46.000000 sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas/schema_types/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    75651 2023-03-20 10:09:46.000000 sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas/schema_types/events_v1.py
+-rw-r--r--   0 runner    (1001) docker     (123)      971 2023-03-20 10:09:46.000000 sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas/schema_types/snuba_generic_metrics_v1.py
+-rw-r--r--   0 runner    (1001) docker     (123)      932 2023-03-20 10:09:46.000000 sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas/schema_types/snuba_metrics_v1.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2794 2023-03-20 10:09:45.000000 sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas/schema_types/snuba_queries_v1.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-20 10:09:48.888929 sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas/schemas/
+-rw-r--r--   0 runner    (1001) docker     (123)   108826 2023-03-20 10:09:24.000000 sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas/schemas/events.v1.schema.json
+-rw-r--r--   0 runner    (1001) docker     (123)     1946 2023-03-20 10:09:24.000000 sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas/schemas/snuba-generic-metrics.v1.schema.json
+-rw-r--r--   0 runner    (1001) docker     (123)     1856 2023-03-20 10:09:24.000000 sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas/schemas/snuba-metrics.v1.schema.json
+-rw-r--r--   0 runner    (1001) docker     (123)     6079 2023-03-20 10:09:24.000000 sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas/schemas/snuba-queries.v1.schema.json
+-rw-r--r--   0 runner    (1001) docker     (123)     4592 2023-03-20 10:09:24.000000 sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas/sentry_kafka_schemas.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-20 10:09:48.888929 sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas/topics/
+-rw-r--r--   0 runner    (1001) docker     (123)      185 2023-03-20 10:09:24.000000 sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas/topics/events.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)      234 2023-03-20 10:09:24.000000 sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas/topics/snuba-generic-metrics.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)      207 2023-03-20 10:09:24.000000 sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas/topics/snuba-metrics.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)      199 2023-03-20 10:09:24.000000 sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas/topics/snuba-queries.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)     1076 2023-03-20 10:09:24.000000 sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas/types.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-20 10:09:48.884929 sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)      269 2023-03-20 10:09:48.000000 sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     2902 2023-03-20 10:09:48.000000 sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-20 10:09:48.000000 sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-20 10:09:48.000000 sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas.egg-info/not-zip-safe
+-rw-r--r--   0 runner    (1001) docker     (123)       59 2023-03-20 10:09:48.000000 sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       21 2023-03-20 10:09:48.000000 sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-20 10:09:48.888929 sentry-kafka-schemas-0.0.9/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)      770 2023-03-20 10:09:24.000000 sentry-kafka-schemas-0.0.9/setup.py
```

### Comparing `sentry-kafka-schemas-0.0.8/LICENSE` & `sentry-kafka-schemas-0.0.9/LICENSE`

 * *Files identical despite different names*

### Comparing `sentry-kafka-schemas-0.0.8/README.md` & `sentry-kafka-schemas-0.0.9/README.md`

 * *Files identical despite different names*

### Comparing `sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas/examples/events/1/errors1` & `sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas/examples/events/1/errors1.json`

 * *Files identical despite different names*

### Comparing `sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas/examples/events/1/null-tag-keys.json` & `sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas/examples/events/1/null-tag-keys.json`

 * *Files identical despite different names*

### Comparing `sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas/examples/events/1/null-values.json` & `sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas/examples/events/1/null-values.json`

 * *Files identical despite different names*

### Comparing `sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas/examples/events/1/weird-transaction-source.json` & `sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas/examples/events/1/weird-transaction-source.json`

 * *Files identical despite different names*

### Comparing `sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas/examples/snuba-queries/1/rate-limited-real.json` & `sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas/examples/snuba-queries/1/rate-limited-real.json`

 * *Files identical despite different names*

### Comparing `sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas/examples/snuba-queries/1/snuba-queries1.json` & `sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas/examples/snuba-queries/1/snuba-queries1.json`

 * *Files identical despite different names*

### Comparing `sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas/examples/snuba-queries/1/with-organization-id.json` & `sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas/examples/snuba-queries/1/with-organization-id.json`

 * *Files identical despite different names*

### Comparing `sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas/schema_types/events_v1.py` & `sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas/schema_types/events_v1.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-from typing import Any, TypedDict, Literal, Tuple, List, Dict, Union
+from typing import List, Any, TypedDict, Union, Tuple, Literal, Dict
 from typing_extensions import Required
 
 
 ClientSdkInfo = Union["_ClientSdkInfoAnyof0"]
 """
 client_sdk_info.
 
@@ -177,15 +177,15 @@
     required
 
     required
     """
 
 
 
-EventStreamMessage = Union[Tuple[Literal[2], Literal["insert"], "InsertEvent", "_Base"], Tuple[Literal[2], Literal["start_delete_groups"], "_BaseGen885349"], Tuple[Literal[2], Literal["start_merge"], "StartMergeMessageBody"], Tuple[Literal[2], Literal["start_unmerge"], Dict[str, Any]], Tuple[Literal[2], Literal["start_unmerge_hierarchical"], Dict[str, Any]], Tuple[Literal[2], Literal["start_delete_tag"], Dict[str, Any]], Tuple[Literal[2], Literal["end_delete_groups"], "EndDeleteGroupsMessageBody"], Tuple[Literal[2], Literal["end_merge"], "EndMergeMessageBody"], Tuple[Literal[2], Literal["end_unmerge"], "EndUnmergeMessageBody"], Tuple[Literal[2], Literal["end_unmerge_hierarchical"], "EndUnmergeHierarchicalMessageBody"], Tuple[Literal[2], Literal["end_delete_tag"], "EndDeleteTagMessageBody"], Tuple[Literal[2], Literal["tombstone_events"], "TombstoneEventsMessageBody"], Tuple[Literal[2], Literal["replace_group"], "ReplaceGroupMessageBody"], Tuple[Literal[2], Literal["exclude_groups"], "ExcludeGroupsMessageBody"]]
+EventStreamMessage = Union[Tuple[Literal[2], Literal["insert"], "InsertEvent", "_Base"], Tuple[Literal[2], Literal["start_delete_groups"], "_BaseGen760261"], Tuple[Literal[2], Literal["start_merge"], "StartMergeMessageBody"], Tuple[Literal[2], Literal["start_unmerge"], Dict[str, Any]], Tuple[Literal[2], Literal["start_unmerge_hierarchical"], Dict[str, Any]], Tuple[Literal[2], Literal["start_delete_tag"], Dict[str, Any]], Tuple[Literal[2], Literal["end_delete_groups"], "EndDeleteGroupsMessageBody"], Tuple[Literal[2], Literal["end_merge"], "EndMergeMessageBody"], Tuple[Literal[2], Literal["end_unmerge"], "EndUnmergeMessageBody"], Tuple[Literal[2], Literal["end_unmerge_hierarchical"], "EndUnmergeHierarchicalMessageBody"], Tuple[Literal[2], Literal["end_delete_tag"], "EndDeleteTagMessageBody"], Tuple[Literal[2], Literal["tombstone_events"], "TombstoneEventsMessageBody"], Tuple[Literal[2], Literal["replace_group"], "ReplaceGroupMessageBody"], Tuple[Literal[2], Literal["exclude_groups"], "ExcludeGroupsMessageBody"]]
 """
 event_stream_message.
 
 The snuba eventstream message.
 """
 
 
@@ -352,14 +352,15 @@
      {
        "event_id": "fc6d8c0c43fc4630ad850ee518f1b9d0"
      }
      ```
     """
 
     exception: Union["SentryExceptionChain", None]
+    threads: Union["SentryThreadChain", None]
     extra: Union[Dict[str, Any], None]
     """
      Arbitrary extra information set by the user.
 
      ```json
      {
          "extra": {
@@ -598,14 +599,26 @@
    }
  }
  ```
 """
 
 
 
+class SentryThreadChain(TypedDict, total=False):
+    """
+    sentry_thread_chain.
+
+     One or multiple threads.
+    """
+
+    values: Required[Union[None, List[Union["_SentryThreadChainValuesArrayItemAnyof0", None]]]]
+    """required"""
+
+
+
 SentryUser = Union["_SentryUserAnyof0"]
 """
 sentry_user.
 
  Information about the user who triggered an event.
 
  ```json
@@ -700,15 +713,15 @@
 
 
 _BaseAnyof0 = Union[str]
 """ A "into-string" type that normalizes header names."""
 
 
 
-class _BaseGen885349(TypedDict, total=False):
+class _BaseGen760261(TypedDict, total=False):
     transaction_id: str
     project_id: Required[int]
     """required"""
 
     group_ids: Required[List[int]]
     """required"""
 
@@ -2337,14 +2350,37 @@
 """
 maxItems: 2
 minItems: 2
 """
 
 
 
+_SentryThreadChainValuesArrayItemAnyof0 = Union["_SentryThreadChainValuesArrayItemAnyof0Anyof0"]
+"""
+ A single thread.
+
+ The Threads Interface specifies threads that were running at the time an event happened.
+ These threads can also contain stack traces.
+"""
+
+
+
+class _SentryThreadChainValuesArrayItemAnyof0Anyof0(TypedDict, total=False):
+    id: Union["_SentryExceptionChainValuesArrayItemAnyof0Anyof0ThreadIdAnyof0", None]
+    """ An optional value that refers to a [thread](#typedef-Thread)."""
+
+    main: Union[bool, None]
+    """
+     If applicable, a flag indicating whether the thread was responsible for rendering the user interface.
+
+     On mobile platforms this is oftentimes referred to as the `main thread` or `ui thread`.
+    """
+
+
+
 class _SentryUserAnyof0(TypedDict, total=False):
     data: Union[Dict[str, Any], None]
     """
      Additional arbitrary fields, as stored in the database (and sometimes as sent by clients).
      All data from `self.other` should end up here after store normalization.
     """
```

### Comparing `sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas/schema_types/snuba_generic_metrics_v1.py` & `sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas/schema_types/snuba_generic_metrics_v1.py`

 * *Files 7% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-from typing import List, Dict, Any, TypedDict, Union, Literal
+from typing import TypedDict, Dict, Any, Literal, Union, List
 from typing_extensions import Required
 
 
 class GenericMetric(TypedDict, total=False):
     """generic_metric."""
 
     version: Literal[2]
```

### Comparing `sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas/schema_types/snuba_metrics_v1.py` & `sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas/schema_types/snuba_metrics_v1.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-from typing import Dict, List, TypedDict, Literal, Union, Any
+from typing import Any, Union, Literal, TypedDict, List, Dict
 from typing_extensions import Required
 
 
 class Metric(TypedDict, total=False):
     """metric."""
 
     version: Literal[1]
```

### Comparing `sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas/schema_types/snuba_queries_v1.py` & `sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas/schema_types/snuba_queries_v1.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-from typing import TypedDict, Union, Any, Dict, List
+from typing import Dict, Any, List, Union, TypedDict
 from typing_extensions import Required
 
 
 class ClickhouseQueryProfile(TypedDict, total=False):
     """clickhouse_query_profile."""
 
     time_range: Required[Union[int, None]]
```

### Comparing `sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas/schemas/events.v1.schema.json` & `sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas/schemas/events.v1.schema.json`

 * *Files 1% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.997466535719482%*

 * *Differences: {"'definitions'": "{'Event': {'properties': {'threads': OrderedDict([('anyOf', "*

 * *                  "[OrderedDict([('$ref', '#/definitions/ThreadChain')]), OrderedDict([('type', "*

 * *                  "'null')])])])}}, 'ThreadChain': OrderedDict([('title', 'sentry_thread_chain'), "*

 * *                  "('description', ' One or multiple threads.'), ('type', 'object'), ('required', "*

 * *                  "['values']), ('properties', OrderedDict([('values', OrderedDict([('type', "*

 * *                  "['null', 'array']), […]*

```diff
@@ -1088,14 +1088,24 @@
                         },
                         {
                             "type": "null"
                         }
                     ],
                     "description": " Custom tags for this event.\n\n A map or list of tags for this event. Each tag must be less than 200 characters."
                 },
+                "threads": {
+                    "anyOf": [
+                        {
+                            "$ref": "#/definitions/ThreadChain"
+                        },
+                        {
+                            "type": "null"
+                        }
+                    ]
+                },
                 "time_spent": {
                     "description": " Time since the start of the transaction until the error occurred.",
                     "minimum": 0,
                     "type": [
                         "integer",
                         "null"
                     ]
@@ -2879,14 +2889,69 @@
         "Tags": {
             "description": " Manual key/value tag pairs.",
             "items": {
                 "$ref": "#/definitions/TagEntry"
             },
             "type": "array"
         },
+        "Thread": {
+            "anyOf": [
+                {
+                    "additionalProperties": true,
+                    "properties": {
+                        "id": {
+                            "anyOf": [
+                                {
+                                    "$ref": "#/definitions/ThreadId"
+                                },
+                                {
+                                    "type": "null"
+                                }
+                            ],
+                            "description": " An optional value that refers to a [thread](#typedef-Thread)."
+                        },
+                        "main": {
+                            "description": " If applicable, a flag indicating whether the thread was responsible for rendering the user interface.\n\n On mobile platforms this is oftentimes referred to as the `main thread` or `ui thread`.",
+                            "type": [
+                                "boolean",
+                                "null"
+                            ]
+                        }
+                    },
+                    "type": "object"
+                }
+            ],
+            "description": " A single thread.\n\n The Threads Interface specifies threads that were running at the time an event happened.\n These threads can also contain stack traces."
+        },
+        "ThreadChain": {
+            "description": " One or multiple threads.",
+            "properties": {
+                "values": {
+                    "items": {
+                        "anyOf": [
+                            {
+                                "$ref": "#/definitions/Thread"
+                            },
+                            {
+                                "type": "null"
+                            }
+                        ]
+                    },
+                    "type": [
+                        "null",
+                        "array"
+                    ]
+                }
+            },
+            "required": [
+                "values"
+            ],
+            "title": "sentry_thread_chain",
+            "type": "object"
+        },
         "ThreadId": {
             "anyOf": [
                 {
                     "minimum": 0,
                     "type": "integer"
                 },
                 {
```

### Comparing `sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas/schemas/snuba-generic-metrics.v1.schema.json` & `sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas/schemas/snuba-generic-metrics.v1.schema.json`

 * *Files identical despite different names*

### Comparing `sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas/schemas/snuba-metrics.v1.schema.json` & `sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas/schemas/snuba-metrics.v1.schema.json`

 * *Files identical despite different names*

### Comparing `sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas/schemas/snuba-queries.v1.schema.json` & `sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas/schemas/snuba-queries.v1.schema.json`

 * *Files identical despite different names*

### Comparing `sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas/sentry_kafka_schemas.py` & `sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas/sentry_kafka_schemas.py`

 * *Files identical despite different names*

### Comparing `sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas/types.py` & `sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas/types.py`

 * *Files identical despite different names*

### Comparing `sentry-kafka-schemas-0.0.8/python/sentry_kafka_schemas.egg-info/SOURCES.txt` & `sentry-kafka-schemas-0.0.9/python/sentry_kafka_schemas.egg-info/SOURCES.txt`

 * *Files 3% similar despite different names*

```diff
@@ -14,15 +14,18 @@
 python/sentry_kafka_schemas.egg-info/requires.txt
 python/sentry_kafka_schemas.egg-info/top_level.txt
 python/sentry_kafka_schemas/examples/events/1/end-delete-groups.json
 python/sentry_kafka_schemas/examples/events/1/end-delete-tag.json
 python/sentry_kafka_schemas/examples/events/1/end-merge.json
 python/sentry_kafka_schemas/examples/events/1/end-unmerge-hierarchical.json
 python/sentry_kafka_schemas/examples/events/1/end-unmerge.json
-python/sentry_kafka_schemas/examples/events/1/errors1
+python/sentry_kafka_schemas/examples/events/1/error-with-null-threads.json
+python/sentry_kafka_schemas/examples/events/1/error-with-null-values-threads.json
+python/sentry_kafka_schemas/examples/events/1/error-with-threads.json
+python/sentry_kafka_schemas/examples/events/1/errors1.json
 python/sentry_kafka_schemas/examples/events/1/exclude-groups.json
 python/sentry_kafka_schemas/examples/events/1/null-tag-keys.json
 python/sentry_kafka_schemas/examples/events/1/null-values.json
 python/sentry_kafka_schemas/examples/events/1/replace-group.json
 python/sentry_kafka_schemas/examples/events/1/start-delete-groups.json
 python/sentry_kafka_schemas/examples/events/1/start-merge.json
 python/sentry_kafka_schemas/examples/events/1/tombstone-events-timestamp.json
```

### Comparing `sentry-kafka-schemas-0.0.8/setup.py` & `sentry-kafka-schemas-0.0.9/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -5,15 +5,15 @@
 
 def get_requirements() -> Sequence[str]:
     with open("python/requirements.txt") as fp:
         return [x.strip() for x in fp if not x.startswith("#")]
 
 setup(
     name="sentry-kafka-schemas",
-    version="0.0.8",
+    version="0.0.9",
     author="Sentry",
     author_email="oss@sentry.io",
     url="https://github.com/getsentry/sentry-kafka-schemas",
     description="Kafka topics and schemas for Sentry",
     zip_safe=False,
     install_requires=get_requirements(),
     packages=["sentry_kafka_schemas", "sentry_kafka_schemas.schema_types"],
```

