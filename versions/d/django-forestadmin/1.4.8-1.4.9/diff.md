# Comparing `tmp/django-forestadmin-1.4.8.tar.gz` & `tmp/django-forestadmin-1.4.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "django-forestadmin-1.4.8.tar", last modified: Thu Apr  6 14:36:34 2023, max compression
+gzip compressed data, was "django-forestadmin-1.4.9.tar", last modified: Fri Apr  7 07:52:06 2023, max compression
```

## Comparing `django-forestadmin-1.4.8.tar` & `django-forestadmin-1.4.9.tar`

### file list

```diff
@@ -1,249 +1,249 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:36:34.956766 django-forestadmin-1.4.8/
--rw-r--r--   0 runner    (1001) docker     (123)    34494 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/LICENCE
--rw-r--r--   0 runner    (1001) docker     (123)       34 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     8996 2023-04-06 14:36:34.956766 django-forestadmin-1.4.8/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     7724 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:36:34.932766 django-forestadmin-1.4.8/django_forest/
--rw-r--r--   0 runner    (1001) docker     (123)      375 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:36:34.932766 django-forestadmin-1.4.8/django_forest/actions/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/actions/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:36:34.932766 django-forestadmin-1.4.8/django_forest/actions/hooks/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/actions/hooks/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      289 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/actions/hooks/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:36:34.932766 django-forestadmin-1.4.8/django_forest/actions/hooks/views/
--rw-r--r--   0 runner    (1001) docker     (123)      162 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/actions/hooks/views/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      515 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/actions/hooks/views/change.py
--rw-r--r--   0 runner    (1001) docker     (123)      276 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/actions/hooks/views/load.py
--rw-r--r--   0 runner    (1001) docker     (123)     2062 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/actions/hooks/views/utils.py
--rw-r--r--   0 runner    (1001) docker     (123)      177 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/actions/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:36:34.932766 django-forestadmin-1.4.8/django_forest/actions/views/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/actions/views/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      502 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/apps.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:36:34.932766 django-forestadmin-1.4.8/django_forest/authentication/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/authentication/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      378 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/authentication/exception.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:36:34.936766 django-forestadmin-1.4.8/django_forest/authentication/oidc/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/authentication/oidc/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1498 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/authentication/oidc/client_manager.py
--rw-r--r--   0 runner    (1001) docker     (123)     1155 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/authentication/oidc/configuration_retriever.py
--rw-r--r--   0 runner    (1001) docker     (123)     1489 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/authentication/oidc/dynamic_client_registrator.py
--rw-r--r--   0 runner    (1001) docker     (123)      365 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/authentication/urls.py
--rw-r--r--   0 runner    (1001) docker     (123)      399 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/authentication/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:36:34.936766 django-forestadmin-1.4.8/django_forest/authentication/views/
--rw-r--r--   0 runner    (1001) docker     (123)      150 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/authentication/views/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5948 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/authentication/views/callback.py
--rw-r--r--   0 runner    (1001) docker     (123)     2219 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/authentication/views/index.py
--rw-r--r--   0 runner    (1001) docker     (123)      187 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/authentication/views/logout.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:36:34.936766 django-forestadmin-1.4.8/django_forest/middleware/
--rw-r--r--   0 runner    (1001) docker     (123)      312 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/middleware/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1429 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/middleware/deactivate_count.py
--rw-r--r--   0 runner    (1001) docker     (123)     1457 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/middleware/ip_whitelist.py
--rw-r--r--   0 runner    (1001) docker     (123)     3298 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/middleware/permissions.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:36:34.936766 django-forestadmin-1.4.8/django_forest/resources/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/resources/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:36:34.936766 django-forestadmin-1.4.8/django_forest/resources/associations/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/resources/associations/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      427 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/resources/associations/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:36:34.936766 django-forestadmin-1.4.8/django_forest/resources/associations/utils/
--rw-r--r--   0 runner    (1001) docker     (123)      114 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/resources/associations/utils/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      881 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/resources/associations/utils/association.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:36:34.936766 django-forestadmin-1.4.8/django_forest/resources/associations/views/
--rw-r--r--   0 runner    (1001) docker     (123)      255 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/resources/associations/views/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      575 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/resources/associations/views/count.py
--rw-r--r--   0 runner    (1001) docker     (123)     1793 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/resources/associations/views/csv.py
--rw-r--r--   0 runner    (1001) docker     (123)     3385 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/resources/associations/views/list.py
--rw-r--r--   0 runner    (1001) docker     (123)      537 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/resources/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:36:34.936766 django-forestadmin-1.4.8/django_forest/resources/utils/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/resources/utils/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1902 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/resources/utils/csv.py
--rw-r--r--   0 runner    (1001) docker     (123)     1908 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/resources/utils/decorators.py
--rw-r--r--   0 runner    (1001) docker     (123)     1824 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/resources/utils/format.py
--rw-r--r--   0 runner    (1001) docker     (123)      103 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/resources/utils/in_search_fields.py
--rw-r--r--   0 runner    (1001) docker     (123)     4089 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/resources/utils/json_api_serializer.py
--rw-r--r--   0 runner    (1001) docker     (123)      548 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/resources/utils/query_parameters.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:36:34.940766 django-forestadmin-1.4.8/django_forest/resources/utils/queryset/
--rw-r--r--   0 runner    (1001) docker     (123)     1896 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/resources/utils/queryset/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:36:34.940766 django-forestadmin-1.4.8/django_forest/resources/utils/queryset/filters/
--rw-r--r--   0 runner    (1001) docker     (123)      484 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/resources/utils/queryset/filters/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:36:34.940766 django-forestadmin-1.4.8/django_forest/resources/utils/queryset/filters/date/
--rw-r--r--   0 runner    (1001) docker     (123)     1729 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/resources/utils/queryset/filters/date/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1894 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/resources/utils/queryset/filters/date/conditions.py
--rw-r--r--   0 runner    (1001) docker     (123)     7684 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/resources/utils/queryset/filters/date/factory.py
--rw-r--r--   0 runner    (1001) docker     (123)     2827 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/resources/utils/queryset/filters/date/utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     5812 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/resources/utils/queryset/filters/utils.py
--rw-r--r--   0 runner    (1001) docker     (123)      838 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/resources/utils/queryset/limit_fields.py
--rw-r--r--   0 runner    (1001) docker     (123)      397 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/resources/utils/queryset/pagination.py
--rw-r--r--   0 runner    (1001) docker     (123)      521 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/resources/utils/queryset/scope.py
--rw-r--r--   0 runner    (1001) docker     (123)     4723 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/resources/utils/queryset/search.py
--rw-r--r--   0 runner    (1001) docker     (123)      751 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/resources/utils/resource.py
--rw-r--r--   0 runner    (1001) docker     (123)     2607 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/resources/utils/smart_field.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:36:34.940766 django-forestadmin-1.4.8/django_forest/resources/views/
--rw-r--r--   0 runner    (1001) docker     (123)      290 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/resources/views/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      262 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/resources/views/count.py
--rw-r--r--   0 runner    (1001) docker     (123)     1619 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/resources/views/csv.py
--rw-r--r--   0 runner    (1001) docker     (123)     3019 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/resources/views/detail.py
--rw-r--r--   0 runner    (1001) docker     (123)     2225 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/resources/views/list.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:36:34.940766 django-forestadmin-1.4.8/django_forest/stats/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/stats/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      333 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/stats/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:36:34.940766 django-forestadmin-1.4.8/django_forest/stats/utils/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/stats/utils/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1624 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/stats/utils/stats.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:36:34.940766 django-forestadmin-1.4.8/django_forest/stats/views/
--rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/stats/views/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:36:34.940766 django-forestadmin-1.4.8/django_forest/stats/views/live_queries/
--rw-r--r--   0 runner    (1001) docker     (123)     1609 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/stats/views/live_queries/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1204 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/stats/views/live_queries/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:36:34.940766 django-forestadmin-1.4.8/django_forest/stats/views/stats_with_parameters/
--rw-r--r--   0 runner    (1001) docker     (123)     3959 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/stats/views/stats_with_parameters/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2817 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/stats/views/stats_with_parameters/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:36:34.940766 django-forestadmin-1.4.8/django_forest/tests/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:36:34.940766 django-forestadmin-1.4.8/django_forest/tests/actions/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/actions/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:36:34.940766 django-forestadmin-1.4.8/django_forest/tests/actions/hooks/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/actions/hooks/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:36:34.944766 django-forestadmin-1.4.8/django_forest/tests/actions/hooks/views/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/actions/hooks/views/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4677 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/actions/hooks/views/test_change.py
--rw-r--r--   0 runner    (1001) docker     (123)     4291 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/actions/hooks/views/test_load.py
--rw-r--r--   0 runner    (1001) docker     (123)      535 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/actions/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:36:34.944766 django-forestadmin-1.4.8/django_forest/tests/actions/views/
--rw-r--r--   0 runner    (1001) docker     (123)      308 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/actions/views/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      747 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/actions/views/generate_invoice.py
--rw-r--r--   0 runner    (1001) docker     (123)      510 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/actions/views/mark_as_live.py
--rw-r--r--   0 runner    (1001) docker     (123)      337 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/actions/views/not_exists.py
--rw-r--r--   0 runner    (1001) docker     (123)      389 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/actions/views/send_invoice.py
--rw-r--r--   0 runner    (1001) docker     (123)      156 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/apps.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:36:34.944766 django-forestadmin-1.4.8/django_forest/tests/authentication/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/authentication/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:36:34.944766 django-forestadmin-1.4.8/django_forest/tests/authentication/oidc/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/authentication/oidc/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3353 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/authentication/oidc/test_client_manager.py
--rw-r--r--   0 runner    (1001) docker     (123)     2274 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/authentication/oidc/test_configuration_retriever.py
--rw-r--r--   0 runner    (1001) docker     (123)     2774 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/authentication/oidc/test_dynamic_client_registrator.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:36:34.944766 django-forestadmin-1.4.8/django_forest/tests/authentication/views/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/authentication/views/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    15283 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/authentication/views/test_callback.py
--rw-r--r--   0 runner    (1001) docker     (123)     3579 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/authentication/views/test_index.py
--rw-r--r--   0 runner    (1001) docker     (123)      275 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/authentication/views/test_logout.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:36:34.944766 django-forestadmin-1.4.8/django_forest/tests/fixtures/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/fixtures/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    92340 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/fixtures/schema.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:36:34.944766 django-forestadmin-1.4.8/django_forest/tests/forest/
--rw-r--r--   0 runner    (1001) docker     (123)      168 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/forest/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      582 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/forest/choice.py
--rw-r--r--   0 runner    (1001) docker     (123)     4682 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/forest/question.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:36:34.944766 django-forestadmin-1.4.8/django_forest/tests/middleware/
--rw-r--r--   0 runner    (1001) docker     (123)     1893 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/middleware/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     8470 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/middleware/test_ip_whitelist.py
--rw-r--r--   0 runner    (1001) docker     (123)    27474 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/middleware/test_permissions.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:36:34.944766 django-forestadmin-1.4.8/django_forest/tests/migrations/
--rw-r--r--   0 runner    (1001) docker     (123)     4684 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/migrations/0001_initial.py
--rw-r--r--   0 runner    (1001) docker     (123)      646 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/migrations/0002_auto_20210615_0942.py
--rw-r--r--   0 runner    (1001) docker     (123)      758 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/migrations/0003_auto_20210701_1508.py
--rw-r--r--   0 runner    (1001) docker     (123)      416 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/migrations/0004_serial.py
--rw-r--r--   0 runner    (1001) docker     (123)      438 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/migrations/0005_alter_serial_uuid.py
--rw-r--r--   0 runner    (1001) docker     (123)      758 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/migrations/0006_auto_20210806_2254.py
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/migrations/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3237 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/models.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:36:34.944766 django-forestadmin-1.4.8/django_forest/tests/resources/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/resources/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:36:34.948766 django-forestadmin-1.4.8/django_forest/tests/resources/associations/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/resources/associations/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:36:34.948766 django-forestadmin-1.4.8/django_forest/tests/resources/associations/views/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/resources/associations/views/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5120 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/resources/associations/views/test_count.py
--rw-r--r--   0 runner    (1001) docker     (123)     3759 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/resources/associations/views/test_csv.py
--rw-r--r--   0 runner    (1001) docker     (123)    15203 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/resources/associations/views/test_list.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:36:34.948766 django-forestadmin-1.4.8/django_forest/tests/resources/utils/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/resources/utils/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:36:34.948766 django-forestadmin-1.4.8/django_forest/tests/resources/utils/queryset/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/resources/utils/queryset/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:36:34.948766 django-forestadmin-1.4.8/django_forest/tests/resources/utils/queryset/filters/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/resources/utils/queryset/filters/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:36:34.948766 django-forestadmin-1.4.8/django_forest/tests/resources/utils/queryset/filters/date/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/resources/utils/queryset/filters/date/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    36732 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/resources/utils/queryset/filters/date/test_factory.py
--rw-r--r--   0 runner    (1001) docker     (123)    24252 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/resources/utils/queryset/filters/date/test_utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:36:34.948766 django-forestadmin-1.4.8/django_forest/tests/resources/views/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/resources/views/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:36:34.948766 django-forestadmin-1.4.8/django_forest/tests/resources/views/list/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/resources/views/list/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    15746 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/resources/views/list/test_list.py
--rw-r--r--   0 runner    (1001) docker     (123)    20934 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/resources/views/list/test_list_filters.py
--rw-r--r--   0 runner    (1001) docker     (123)    17018 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/resources/views/list/test_list_filters_date.py
--rw-r--r--   0 runner    (1001) docker     (123)     9345 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/resources/views/list/test_list_scope.py
--rw-r--r--   0 runner    (1001) docker     (123)    19805 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/resources/views/list/test_list_search.py
--rw-r--r--   0 runner    (1001) docker     (123)    11534 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/resources/views/list/test_list_smart_fields.py
--rw-r--r--   0 runner    (1001) docker     (123)     4773 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/resources/views/list/test_list_smart_relationship.py
--rw-r--r--   0 runner    (1001) docker     (123)     3990 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/resources/views/list/test_list_smart_segment.py
--rw-r--r--   0 runner    (1001) docker     (123)     7434 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/resources/views/list/test_list_sort.py
--rw-r--r--   0 runner    (1001) docker     (123)     4950 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/resources/views/test_count.py
--rw-r--r--   0 runner    (1001) docker     (123)     4932 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/resources/views/test_csv.py
--rw-r--r--   0 runner    (1001) docker     (123)    17234 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/resources/views/test_detail.py
--rw-r--r--   0 runner    (1001) docker     (123)     3896 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/settings.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:36:34.948766 django-forestadmin-1.4.8/django_forest/tests/stats/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/stats/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:36:34.948766 django-forestadmin-1.4.8/django_forest/tests/stats/views/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/stats/views/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     8872 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/stats/views/test_live_queries.py
--rw-r--r--   0 runner    (1001) docker     (123)    17160 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/stats/views/test_stats_with_parameters.py
--rw-r--r--   0 runner    (1001) docker     (123)      290 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:36:34.952766 django-forestadmin-1.4.8/django_forest/tests/utils/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/utils/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    12081 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/utils/test_collection.py
--rw-r--r--   0 runner    (1001) docker     (123)     2798 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/utils/test_cors.py
--rw-r--r--   0 runner    (1001) docker     (123)      633 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/utils/test_date.py
--rw-r--r--   0 runner    (1001) docker     (123)     3371 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/utils/test_forest_api_requester.py
--rw-r--r--   0 runner    (1001) docker     (123)     1679 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/utils/test_get_forest_setting.py
--rw-r--r--   0 runner    (1001) docker     (123)    10651 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/utils/test_json_api_schema.py
--rw-r--r--   0 runner    (1001) docker     (123)      436 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/utils/test_middlewares.py
--rw-r--r--   0 runner    (1001) docker     (123)      397 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/utils/test_models.py
--rw-r--r--   0 runner    (1001) docker     (123)    14315 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/utils/test_schema.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:36:34.952766 django-forestadmin-1.4.8/django_forest/tests/views/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/views/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      242 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/views/test_index.py
--rw-r--r--   0 runner    (1001) docker     (123)     2217 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/tests/views/test_scope_cache_invalidation.py
--rw-r--r--   0 runner    (1001) docker     (123)      735 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:36:34.952766 django-forestadmin-1.4.8/django_forest/utils/
--rw-r--r--   0 runner    (1001) docker     (123)     1254 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/utils/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4148 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/utils/collection.py
--rw-r--r--   0 runner    (1001) docker     (123)     1880 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/utils/cors.py
--rw-r--r--   0 runner    (1001) docker     (123)      310 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/utils/date.py
--rw-r--r--   0 runner    (1001) docker     (123)     1699 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/utils/error_handler.py
--rw-r--r--   0 runner    (1001) docker     (123)     2898 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/utils/forest_api_requester.py
--rw-r--r--   0 runner    (1001) docker     (123)      491 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/utils/forest_setting.py
--rw-r--r--   0 runner    (1001) docker     (123)     2194 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/utils/ip_whitelist.py
--rw-r--r--   0 runner    (1001) docker     (123)      225 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/utils/middlewares.py
--rw-r--r--   0 runner    (1001) docker     (123)      960 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/utils/models.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:36:34.952766 django-forestadmin-1.4.8/django_forest/utils/permissions/
--rw-r--r--   0 runner    (1001) docker     (123)     3473 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/utils/permissions/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1700 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/utils/permissions/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:36:34.952766 django-forestadmin-1.4.8/django_forest/utils/schema/
--rw-r--r--   0 runner    (1001) docker     (123)     8599 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/utils/schema/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      657 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/utils/schema/apimap_errors.py
--rw-r--r--   0 runner    (1001) docker     (123)      322 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/utils/schema/default.py
--rw-r--r--   0 runner    (1001) docker     (123)     1094 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/utils/schema/definitions.py
--rw-r--r--   0 runner    (1001) docker     (123)      416 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/utils/schema/enums.py
--rw-r--r--   0 runner    (1001) docker     (123)     5732 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/utils/schema/json_api_schema.py
--rw-r--r--   0 runner    (1001) docker     (123)     2864 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/utils/schema/validations.py
--rw-r--r--   0 runner    (1001) docker     (123)      310 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/utils/schema/version.py
--rw-r--r--   0 runner    (1001) docker     (123)     2614 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/utils/scope.py
--rw-r--r--   0 runner    (1001) docker     (123)     2248 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/utils/type_mapping.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:36:34.956766 django-forestadmin-1.4.8/django_forest/utils/views/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/utils/views/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1508 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/utils/views/action.py
--rw-r--r--   0 runner    (1001) docker     (123)     2750 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/utils/views/base.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:36:34.956766 django-forestadmin-1.4.8/django_forest/views/
--rw-r--r--   0 runner    (1001) docker     (123)      187 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/views/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      185 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/views/index.py
--rw-r--r--   0 runner    (1001) docker     (123)      770 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/django_forest/views/scope_cache_invalidation.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:36:34.956766 django-forestadmin-1.4.8/django_forestadmin.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     8996 2023-04-06 14:36:34.000000 django-forestadmin-1.4.8/django_forestadmin.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     8788 2023-04-06 14:36:34.000000 django-forestadmin-1.4.8/django_forestadmin.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 14:36:34.000000 django-forestadmin-1.4.8/django_forestadmin.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      339 2023-04-06 14:36:34.000000 django-forestadmin-1.4.8/django_forestadmin.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       14 2023-04-06 14:36:34.000000 django-forestadmin-1.4.8/django_forestadmin.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)     2080 2023-04-06 14:36:34.956766 django-forestadmin-1.4.8/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 14:35:55.000000 django-forestadmin-1.4.8/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:52:06.703165 django-forestadmin-1.4.9/
+-rw-r--r--   0 runner    (1001) docker     (123)    34494 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/LICENCE
+-rw-r--r--   0 runner    (1001) docker     (123)       34 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     8996 2023-04-07 07:52:06.703165 django-forestadmin-1.4.9/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     7724 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:52:06.683166 django-forestadmin-1.4.9/django_forest/
+-rw-r--r--   0 runner    (1001) docker     (123)      375 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:52:06.683166 django-forestadmin-1.4.9/django_forest/actions/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/actions/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:52:06.683166 django-forestadmin-1.4.9/django_forest/actions/hooks/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/actions/hooks/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      289 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/actions/hooks/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:52:06.683166 django-forestadmin-1.4.9/django_forest/actions/hooks/views/
+-rw-r--r--   0 runner    (1001) docker     (123)      162 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/actions/hooks/views/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      515 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/actions/hooks/views/change.py
+-rw-r--r--   0 runner    (1001) docker     (123)      276 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/actions/hooks/views/load.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2062 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/actions/hooks/views/utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)      177 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/actions/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:52:06.683166 django-forestadmin-1.4.9/django_forest/actions/views/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/actions/views/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      502 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/apps.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:52:06.683166 django-forestadmin-1.4.9/django_forest/authentication/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/authentication/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      378 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/authentication/exception.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:52:06.687166 django-forestadmin-1.4.9/django_forest/authentication/oidc/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/authentication/oidc/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1498 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/authentication/oidc/client_manager.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1155 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/authentication/oidc/configuration_retriever.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1489 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/authentication/oidc/dynamic_client_registrator.py
+-rw-r--r--   0 runner    (1001) docker     (123)      365 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/authentication/urls.py
+-rw-r--r--   0 runner    (1001) docker     (123)      399 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/authentication/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:52:06.687166 django-forestadmin-1.4.9/django_forest/authentication/views/
+-rw-r--r--   0 runner    (1001) docker     (123)      150 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/authentication/views/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5948 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/authentication/views/callback.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2219 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/authentication/views/index.py
+-rw-r--r--   0 runner    (1001) docker     (123)      187 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/authentication/views/logout.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:52:06.687166 django-forestadmin-1.4.9/django_forest/middleware/
+-rw-r--r--   0 runner    (1001) docker     (123)      312 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/middleware/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1428 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/middleware/deactivate_count.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1457 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/middleware/ip_whitelist.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3298 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/middleware/permissions.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:52:06.687166 django-forestadmin-1.4.9/django_forest/resources/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/resources/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:52:06.687166 django-forestadmin-1.4.9/django_forest/resources/associations/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/resources/associations/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      427 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/resources/associations/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:52:06.687166 django-forestadmin-1.4.9/django_forest/resources/associations/utils/
+-rw-r--r--   0 runner    (1001) docker     (123)      114 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/resources/associations/utils/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      881 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/resources/associations/utils/association.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:52:06.687166 django-forestadmin-1.4.9/django_forest/resources/associations/views/
+-rw-r--r--   0 runner    (1001) docker     (123)      255 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/resources/associations/views/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      575 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/resources/associations/views/count.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1793 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/resources/associations/views/csv.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3385 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/resources/associations/views/list.py
+-rw-r--r--   0 runner    (1001) docker     (123)      537 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/resources/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:52:06.687166 django-forestadmin-1.4.9/django_forest/resources/utils/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/resources/utils/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1902 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/resources/utils/csv.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1908 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/resources/utils/decorators.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1824 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/resources/utils/format.py
+-rw-r--r--   0 runner    (1001) docker     (123)      103 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/resources/utils/in_search_fields.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4089 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/resources/utils/json_api_serializer.py
+-rw-r--r--   0 runner    (1001) docker     (123)      548 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/resources/utils/query_parameters.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:52:06.687166 django-forestadmin-1.4.9/django_forest/resources/utils/queryset/
+-rw-r--r--   0 runner    (1001) docker     (123)     1896 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/resources/utils/queryset/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:52:06.691166 django-forestadmin-1.4.9/django_forest/resources/utils/queryset/filters/
+-rw-r--r--   0 runner    (1001) docker     (123)      484 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/resources/utils/queryset/filters/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:52:06.691166 django-forestadmin-1.4.9/django_forest/resources/utils/queryset/filters/date/
+-rw-r--r--   0 runner    (1001) docker     (123)     1729 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/resources/utils/queryset/filters/date/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1894 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/resources/utils/queryset/filters/date/conditions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7684 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/resources/utils/queryset/filters/date/factory.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2827 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/resources/utils/queryset/filters/date/utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5812 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/resources/utils/queryset/filters/utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)      838 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/resources/utils/queryset/limit_fields.py
+-rw-r--r--   0 runner    (1001) docker     (123)      397 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/resources/utils/queryset/pagination.py
+-rw-r--r--   0 runner    (1001) docker     (123)      521 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/resources/utils/queryset/scope.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4723 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/resources/utils/queryset/search.py
+-rw-r--r--   0 runner    (1001) docker     (123)      751 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/resources/utils/resource.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2607 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/resources/utils/smart_field.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:52:06.691166 django-forestadmin-1.4.9/django_forest/resources/views/
+-rw-r--r--   0 runner    (1001) docker     (123)      290 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/resources/views/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      262 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/resources/views/count.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1619 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/resources/views/csv.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3019 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/resources/views/detail.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2225 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/resources/views/list.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:52:06.691166 django-forestadmin-1.4.9/django_forest/stats/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/stats/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      333 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/stats/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:52:06.691166 django-forestadmin-1.4.9/django_forest/stats/utils/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/stats/utils/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1624 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/stats/utils/stats.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:52:06.691166 django-forestadmin-1.4.9/django_forest/stats/views/
+-rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/stats/views/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:52:06.691166 django-forestadmin-1.4.9/django_forest/stats/views/live_queries/
+-rw-r--r--   0 runner    (1001) docker     (123)     1609 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/stats/views/live_queries/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1204 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/stats/views/live_queries/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:52:06.691166 django-forestadmin-1.4.9/django_forest/stats/views/stats_with_parameters/
+-rw-r--r--   0 runner    (1001) docker     (123)     3959 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/stats/views/stats_with_parameters/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2817 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/stats/views/stats_with_parameters/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:52:06.691166 django-forestadmin-1.4.9/django_forest/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:52:06.691166 django-forestadmin-1.4.9/django_forest/tests/actions/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/actions/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:52:06.691166 django-forestadmin-1.4.9/django_forest/tests/actions/hooks/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/actions/hooks/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:52:06.691166 django-forestadmin-1.4.9/django_forest/tests/actions/hooks/views/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/actions/hooks/views/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4677 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/actions/hooks/views/test_change.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4291 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/actions/hooks/views/test_load.py
+-rw-r--r--   0 runner    (1001) docker     (123)      535 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/actions/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:52:06.691166 django-forestadmin-1.4.9/django_forest/tests/actions/views/
+-rw-r--r--   0 runner    (1001) docker     (123)      308 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/actions/views/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      747 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/actions/views/generate_invoice.py
+-rw-r--r--   0 runner    (1001) docker     (123)      510 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/actions/views/mark_as_live.py
+-rw-r--r--   0 runner    (1001) docker     (123)      337 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/actions/views/not_exists.py
+-rw-r--r--   0 runner    (1001) docker     (123)      389 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/actions/views/send_invoice.py
+-rw-r--r--   0 runner    (1001) docker     (123)      156 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/apps.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:52:06.691166 django-forestadmin-1.4.9/django_forest/tests/authentication/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/authentication/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:52:06.695165 django-forestadmin-1.4.9/django_forest/tests/authentication/oidc/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/authentication/oidc/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3353 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/authentication/oidc/test_client_manager.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2274 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/authentication/oidc/test_configuration_retriever.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2774 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/authentication/oidc/test_dynamic_client_registrator.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:52:06.695165 django-forestadmin-1.4.9/django_forest/tests/authentication/views/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/authentication/views/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15283 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/authentication/views/test_callback.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3579 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/authentication/views/test_index.py
+-rw-r--r--   0 runner    (1001) docker     (123)      275 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/authentication/views/test_logout.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:52:06.695165 django-forestadmin-1.4.9/django_forest/tests/fixtures/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/fixtures/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    92340 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/fixtures/schema.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:52:06.695165 django-forestadmin-1.4.9/django_forest/tests/forest/
+-rw-r--r--   0 runner    (1001) docker     (123)      168 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/forest/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      582 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/forest/choice.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4682 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/forest/question.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:52:06.695165 django-forestadmin-1.4.9/django_forest/tests/middleware/
+-rw-r--r--   0 runner    (1001) docker     (123)     1893 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/middleware/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8470 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/middleware/test_ip_whitelist.py
+-rw-r--r--   0 runner    (1001) docker     (123)    27474 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/middleware/test_permissions.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:52:06.695165 django-forestadmin-1.4.9/django_forest/tests/migrations/
+-rw-r--r--   0 runner    (1001) docker     (123)     4684 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/migrations/0001_initial.py
+-rw-r--r--   0 runner    (1001) docker     (123)      646 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/migrations/0002_auto_20210615_0942.py
+-rw-r--r--   0 runner    (1001) docker     (123)      758 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/migrations/0003_auto_20210701_1508.py
+-rw-r--r--   0 runner    (1001) docker     (123)      416 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/migrations/0004_serial.py
+-rw-r--r--   0 runner    (1001) docker     (123)      438 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/migrations/0005_alter_serial_uuid.py
+-rw-r--r--   0 runner    (1001) docker     (123)      758 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/migrations/0006_auto_20210806_2254.py
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/migrations/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3237 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/models.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:52:06.695165 django-forestadmin-1.4.9/django_forest/tests/resources/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/resources/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:52:06.695165 django-forestadmin-1.4.9/django_forest/tests/resources/associations/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/resources/associations/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:52:06.695165 django-forestadmin-1.4.9/django_forest/tests/resources/associations/views/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/resources/associations/views/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5118 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/resources/associations/views/test_count.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3759 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/resources/associations/views/test_csv.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15203 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/resources/associations/views/test_list.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:52:06.695165 django-forestadmin-1.4.9/django_forest/tests/resources/utils/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/resources/utils/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:52:06.695165 django-forestadmin-1.4.9/django_forest/tests/resources/utils/queryset/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/resources/utils/queryset/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:52:06.695165 django-forestadmin-1.4.9/django_forest/tests/resources/utils/queryset/filters/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/resources/utils/queryset/filters/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:52:06.699165 django-forestadmin-1.4.9/django_forest/tests/resources/utils/queryset/filters/date/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/resources/utils/queryset/filters/date/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    36732 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/resources/utils/queryset/filters/date/test_factory.py
+-rw-r--r--   0 runner    (1001) docker     (123)    24252 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/resources/utils/queryset/filters/date/test_utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:52:06.699165 django-forestadmin-1.4.9/django_forest/tests/resources/views/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/resources/views/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:52:06.699165 django-forestadmin-1.4.9/django_forest/tests/resources/views/list/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/resources/views/list/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15746 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/resources/views/list/test_list.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20934 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/resources/views/list/test_list_filters.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17018 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/resources/views/list/test_list_filters_date.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9345 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/resources/views/list/test_list_scope.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19805 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/resources/views/list/test_list_search.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11534 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/resources/views/list/test_list_smart_fields.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4773 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/resources/views/list/test_list_smart_relationship.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3990 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/resources/views/list/test_list_smart_segment.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7434 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/resources/views/list/test_list_sort.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4948 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/resources/views/test_count.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4932 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/resources/views/test_csv.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17234 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/resources/views/test_detail.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3896 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/settings.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:52:06.699165 django-forestadmin-1.4.9/django_forest/tests/stats/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/stats/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:52:06.699165 django-forestadmin-1.4.9/django_forest/tests/stats/views/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/stats/views/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8872 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/stats/views/test_live_queries.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17160 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/stats/views/test_stats_with_parameters.py
+-rw-r--r--   0 runner    (1001) docker     (123)      290 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:52:06.699165 django-forestadmin-1.4.9/django_forest/tests/utils/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/utils/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12081 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/utils/test_collection.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2798 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/utils/test_cors.py
+-rw-r--r--   0 runner    (1001) docker     (123)      633 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/utils/test_date.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3371 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/utils/test_forest_api_requester.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1679 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/utils/test_get_forest_setting.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10651 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/utils/test_json_api_schema.py
+-rw-r--r--   0 runner    (1001) docker     (123)      436 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/utils/test_middlewares.py
+-rw-r--r--   0 runner    (1001) docker     (123)      397 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/utils/test_models.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14315 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/utils/test_schema.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:52:06.699165 django-forestadmin-1.4.9/django_forest/tests/views/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/views/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      242 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/views/test_index.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2217 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/tests/views/test_scope_cache_invalidation.py
+-rw-r--r--   0 runner    (1001) docker     (123)      735 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:52:06.703165 django-forestadmin-1.4.9/django_forest/utils/
+-rw-r--r--   0 runner    (1001) docker     (123)     1254 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/utils/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4148 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/utils/collection.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1880 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/utils/cors.py
+-rw-r--r--   0 runner    (1001) docker     (123)      310 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/utils/date.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1699 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/utils/error_handler.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2898 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/utils/forest_api_requester.py
+-rw-r--r--   0 runner    (1001) docker     (123)      491 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/utils/forest_setting.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2194 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/utils/ip_whitelist.py
+-rw-r--r--   0 runner    (1001) docker     (123)      225 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/utils/middlewares.py
+-rw-r--r--   0 runner    (1001) docker     (123)      960 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/utils/models.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:52:06.703165 django-forestadmin-1.4.9/django_forest/utils/permissions/
+-rw-r--r--   0 runner    (1001) docker     (123)     3473 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/utils/permissions/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1700 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/utils/permissions/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:52:06.703165 django-forestadmin-1.4.9/django_forest/utils/schema/
+-rw-r--r--   0 runner    (1001) docker     (123)     8599 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/utils/schema/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      657 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/utils/schema/apimap_errors.py
+-rw-r--r--   0 runner    (1001) docker     (123)      322 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/utils/schema/default.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1094 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/utils/schema/definitions.py
+-rw-r--r--   0 runner    (1001) docker     (123)      416 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/utils/schema/enums.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5732 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/utils/schema/json_api_schema.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2864 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/utils/schema/validations.py
+-rw-r--r--   0 runner    (1001) docker     (123)      310 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/utils/schema/version.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2614 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/utils/scope.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2248 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/utils/type_mapping.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:52:06.703165 django-forestadmin-1.4.9/django_forest/utils/views/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/utils/views/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1508 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/utils/views/action.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2750 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/utils/views/base.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:52:06.703165 django-forestadmin-1.4.9/django_forest/views/
+-rw-r--r--   0 runner    (1001) docker     (123)      187 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/views/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      185 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/views/index.py
+-rw-r--r--   0 runner    (1001) docker     (123)      770 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/django_forest/views/scope_cache_invalidation.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:52:06.703165 django-forestadmin-1.4.9/django_forestadmin.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     8996 2023-04-07 07:52:06.000000 django-forestadmin-1.4.9/django_forestadmin.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     8788 2023-04-07 07:52:06.000000 django-forestadmin-1.4.9/django_forestadmin.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 07:52:06.000000 django-forestadmin-1.4.9/django_forestadmin.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      339 2023-04-07 07:52:06.000000 django-forestadmin-1.4.9/django_forestadmin.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       14 2023-04-07 07:52:06.000000 django-forestadmin-1.4.9/django_forestadmin.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     2080 2023-04-07 07:52:06.707165 django-forestadmin-1.4.9/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-07 07:51:24.000000 django-forestadmin-1.4.9/setup.py
```

### Comparing `django-forestadmin-1.4.8/LICENCE` & `django-forestadmin-1.4.9/LICENCE`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/PKG-INFO` & `django-forestadmin-1.4.9/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: django-forestadmin
-Version: 1.4.8
+Version: 1.4.9
 Summary: The Django Liana for Forest Admin.
 Home-page: https://forestadmin.com/
 Author: Guillaume Cisco
 Author-email: guillaumec@forestadmin.com
 License: GNU General Public License v3 or later (GPLv3+)
 Classifier: Environment :: Web Environment
 Classifier: Framework :: Django
```

### Comparing `django-forestadmin-1.4.8/README.md` & `django-forestadmin-1.4.9/README.md`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/actions/hooks/views/change.py` & `django-forestadmin-1.4.9/django_forest/actions/hooks/views/change.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/actions/hooks/views/utils.py` & `django-forestadmin-1.4.9/django_forest/actions/hooks/views/utils.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/authentication/oidc/client_manager.py` & `django-forestadmin-1.4.9/django_forest/authentication/oidc/client_manager.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/authentication/oidc/configuration_retriever.py` & `django-forestadmin-1.4.9/django_forest/authentication/oidc/configuration_retriever.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/authentication/oidc/dynamic_client_registrator.py` & `django-forestadmin-1.4.9/django_forest/authentication/oidc/dynamic_client_registrator.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/authentication/views/callback.py` & `django-forestadmin-1.4.9/django_forest/authentication/views/callback.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/authentication/views/index.py` & `django-forestadmin-1.4.9/django_forest/authentication/views/index.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/middleware/deactivate_count.py` & `django-forestadmin-1.4.9/django_forest/middleware/deactivate_count.py`

 * *Files 4% similar despite different names*

```diff
@@ -27,9 +27,9 @@
             all_associations = self.build_association_resource(resource, '*')
             resource = self.build_association_resource(resource, association_resource)
 
         return is_count_request and any([resource in deactivated_count, all_associations in deactivated_count])
 
     def process_view(self, request, view_func, *args, **kwargs):
         if self.is_deactivated(request, view_func, *args, **kwargs):
-            return JsonResponse({"meta": {"count": "deactivated "}})
+            return JsonResponse({"meta": {"count": "deactivated"}})
         return None
```

### Comparing `django-forestadmin-1.4.8/django_forest/middleware/ip_whitelist.py` & `django-forestadmin-1.4.9/django_forest/middleware/ip_whitelist.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/middleware/permissions.py` & `django-forestadmin-1.4.9/django_forest/middleware/permissions.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/resources/associations/utils/association.py` & `django-forestadmin-1.4.9/django_forest/resources/associations/utils/association.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/resources/associations/views/count.py` & `django-forestadmin-1.4.9/django_forest/resources/associations/views/count.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/resources/associations/views/csv.py` & `django-forestadmin-1.4.9/django_forest/resources/associations/views/csv.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/resources/associations/views/list.py` & `django-forestadmin-1.4.9/django_forest/resources/associations/views/list.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/resources/urls.py` & `django-forestadmin-1.4.9/django_forest/resources/urls.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/resources/utils/csv.py` & `django-forestadmin-1.4.9/django_forest/resources/utils/csv.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/resources/utils/decorators.py` & `django-forestadmin-1.4.9/django_forest/resources/utils/decorators.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/resources/utils/format.py` & `django-forestadmin-1.4.9/django_forest/resources/utils/format.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/resources/utils/json_api_serializer.py` & `django-forestadmin-1.4.9/django_forest/resources/utils/json_api_serializer.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/resources/utils/query_parameters.py` & `django-forestadmin-1.4.9/django_forest/resources/utils/query_parameters.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/resources/utils/queryset/__init__.py` & `django-forestadmin-1.4.9/django_forest/resources/utils/queryset/__init__.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/resources/utils/queryset/filters/date/__init__.py` & `django-forestadmin-1.4.9/django_forest/resources/utils/queryset/filters/date/__init__.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/resources/utils/queryset/filters/date/conditions.py` & `django-forestadmin-1.4.9/django_forest/resources/utils/queryset/filters/date/conditions.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/resources/utils/queryset/filters/date/factory.py` & `django-forestadmin-1.4.9/django_forest/resources/utils/queryset/filters/date/factory.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/resources/utils/queryset/filters/date/utils.py` & `django-forestadmin-1.4.9/django_forest/resources/utils/queryset/filters/date/utils.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/resources/utils/queryset/filters/utils.py` & `django-forestadmin-1.4.9/django_forest/resources/utils/queryset/filters/utils.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/resources/utils/queryset/limit_fields.py` & `django-forestadmin-1.4.9/django_forest/resources/utils/queryset/limit_fields.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/resources/utils/queryset/scope.py` & `django-forestadmin-1.4.9/django_forest/resources/utils/queryset/scope.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/resources/utils/queryset/search.py` & `django-forestadmin-1.4.9/django_forest/resources/utils/queryset/search.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/resources/utils/resource.py` & `django-forestadmin-1.4.9/django_forest/resources/utils/resource.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/resources/utils/smart_field.py` & `django-forestadmin-1.4.9/django_forest/resources/utils/smart_field.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/resources/views/csv.py` & `django-forestadmin-1.4.9/django_forest/resources/views/csv.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/resources/views/detail.py` & `django-forestadmin-1.4.9/django_forest/resources/views/detail.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/resources/views/list.py` & `django-forestadmin-1.4.9/django_forest/resources/views/list.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/stats/utils/stats.py` & `django-forestadmin-1.4.9/django_forest/stats/utils/stats.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/stats/views/live_queries/__init__.py` & `django-forestadmin-1.4.9/django_forest/stats/views/live_queries/__init__.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/stats/views/live_queries/utils.py` & `django-forestadmin-1.4.9/django_forest/stats/views/live_queries/utils.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/stats/views/stats_with_parameters/__init__.py` & `django-forestadmin-1.4.9/django_forest/stats/views/stats_with_parameters/__init__.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/stats/views/stats_with_parameters/utils.py` & `django-forestadmin-1.4.9/django_forest/stats/views/stats_with_parameters/utils.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/tests/actions/hooks/views/test_change.py` & `django-forestadmin-1.4.9/django_forest/tests/actions/hooks/views/test_change.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/tests/actions/hooks/views/test_load.py` & `django-forestadmin-1.4.9/django_forest/tests/actions/hooks/views/test_load.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/tests/actions/urls.py` & `django-forestadmin-1.4.9/django_forest/tests/actions/urls.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/tests/actions/views/generate_invoice.py` & `django-forestadmin-1.4.9/django_forest/tests/actions/views/generate_invoice.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/tests/authentication/oidc/test_client_manager.py` & `django-forestadmin-1.4.9/django_forest/tests/authentication/oidc/test_client_manager.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/tests/authentication/oidc/test_configuration_retriever.py` & `django-forestadmin-1.4.9/django_forest/tests/authentication/oidc/test_configuration_retriever.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/tests/authentication/oidc/test_dynamic_client_registrator.py` & `django-forestadmin-1.4.9/django_forest/tests/authentication/oidc/test_dynamic_client_registrator.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/tests/authentication/views/test_callback.py` & `django-forestadmin-1.4.9/django_forest/tests/authentication/views/test_callback.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/tests/authentication/views/test_index.py` & `django-forestadmin-1.4.9/django_forest/tests/authentication/views/test_index.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/tests/fixtures/schema.py` & `django-forestadmin-1.4.9/django_forest/tests/fixtures/schema.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/tests/forest/choice.py` & `django-forestadmin-1.4.9/django_forest/tests/forest/choice.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/tests/forest/question.py` & `django-forestadmin-1.4.9/django_forest/tests/forest/question.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/tests/middleware/__init__.py` & `django-forestadmin-1.4.9/django_forest/tests/middleware/__init__.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/tests/middleware/test_ip_whitelist.py` & `django-forestadmin-1.4.9/django_forest/tests/middleware/test_ip_whitelist.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/tests/middleware/test_permissions.py` & `django-forestadmin-1.4.9/django_forest/tests/middleware/test_permissions.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/tests/migrations/0001_initial.py` & `django-forestadmin-1.4.9/django_forest/tests/migrations/0001_initial.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/tests/migrations/0002_auto_20210615_0942.py` & `django-forestadmin-1.4.9/django_forest/tests/migrations/0002_auto_20210615_0942.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/tests/migrations/0003_auto_20210701_1508.py` & `django-forestadmin-1.4.9/django_forest/tests/migrations/0003_auto_20210701_1508.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/tests/migrations/0006_auto_20210806_2254.py` & `django-forestadmin-1.4.9/django_forest/tests/migrations/0006_auto_20210806_2254.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/tests/models.py` & `django-forestadmin-1.4.9/django_forest/tests/models.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/tests/resources/associations/views/test_count.py` & `django-forestadmin-1.4.9/django_forest/tests/resources/associations/views/test_count.py`

 * *Files 0% similar despite different names*

```diff
@@ -51,22 +51,22 @@
         self.assertEqual(data, {'count': 2})
         
         settings.FOREST['DEACTIVATED_COUNT'] = ['tests_question:*']
         url = reverse('django_forest:resources:associations:count', kwargs={'resource': 'tests_question', 'pk': 1, 'association_resource': 'choice_set'})
         response = self.client.get(url)
         data = response.json()
         self.assertEqual(response.status_code, 200)
-        self.assertEqual(data, {'meta': {'count': 'deactivated '}})
+        self.assertEqual(data, {'meta': {'count': 'deactivated'}})
 
         settings.FOREST['DEACTIVATED_COUNT'] = ['tests_question:choice_set']
         url = reverse('django_forest:resources:associations:count', kwargs={'resource': 'tests_question', 'pk': 1, 'association_resource': 'choice_set'})
         response = self.client.get(url)
         data = response.json()
         self.assertEqual(response.status_code, 200)
-        self.assertEqual(data, {'meta': {'count': 'deactivated '}})
+        self.assertEqual(data, {'meta': {'count': 'deactivated'}})
 
         settings.FOREST['DEACTIVATED_COUNT'] = ['tests_question:fake']
         url = reverse('django_forest:resources:associations:count', kwargs={'resource': 'tests_question', 'pk': 1, 'association_resource': 'choice_set'})
         response = self.client.get(url)
         data = response.json()
         self.assertEqual(response.status_code, 200)
         self.assertEqual(data, {'count': 2})
```

### Comparing `django-forestadmin-1.4.8/django_forest/tests/resources/associations/views/test_csv.py` & `django-forestadmin-1.4.9/django_forest/tests/resources/associations/views/test_csv.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/tests/resources/associations/views/test_list.py` & `django-forestadmin-1.4.9/django_forest/tests/resources/associations/views/test_list.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/tests/resources/utils/queryset/filters/date/test_factory.py` & `django-forestadmin-1.4.9/django_forest/tests/resources/utils/queryset/filters/date/test_factory.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/tests/resources/utils/queryset/filters/date/test_utils.py` & `django-forestadmin-1.4.9/django_forest/tests/resources/utils/queryset/filters/date/test_utils.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/tests/resources/views/list/test_list.py` & `django-forestadmin-1.4.9/django_forest/tests/resources/views/list/test_list.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/tests/resources/views/list/test_list_filters.py` & `django-forestadmin-1.4.9/django_forest/tests/resources/views/list/test_list_filters.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/tests/resources/views/list/test_list_filters_date.py` & `django-forestadmin-1.4.9/django_forest/tests/resources/views/list/test_list_filters_date.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/tests/resources/views/list/test_list_scope.py` & `django-forestadmin-1.4.9/django_forest/tests/resources/views/list/test_list_scope.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/tests/resources/views/list/test_list_search.py` & `django-forestadmin-1.4.9/django_forest/tests/resources/views/list/test_list_search.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/tests/resources/views/list/test_list_smart_fields.py` & `django-forestadmin-1.4.9/django_forest/tests/resources/views/list/test_list_smart_fields.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/tests/resources/views/list/test_list_smart_relationship.py` & `django-forestadmin-1.4.9/django_forest/tests/resources/views/list/test_list_smart_relationship.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/tests/resources/views/list/test_list_smart_segment.py` & `django-forestadmin-1.4.9/django_forest/tests/resources/views/list/test_list_smart_segment.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/tests/resources/views/list/test_list_sort.py` & `django-forestadmin-1.4.9/django_forest/tests/resources/views/list/test_list_sort.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/tests/resources/views/test_count.py` & `django-forestadmin-1.4.9/django_forest/tests/resources/views/test_count.py`

 * *Files 0% similar despite different names*

```diff
@@ -53,15 +53,15 @@
     def test_deactivate(self, *args, **kwargs):
         settings.MIDDLEWARE.insert(0, 'django_forest.middleware.DeactivateCountMiddleware')
         settings.FOREST['DEACTIVATED_COUNT'] = ['tests_question']
         url = reverse('django_forest:resources:count', kwargs={'resource': 'tests_question'})
         response = self.client.get(url)
         data = response.json()
         self.assertEqual(response.status_code, 200)
-        self.assertEqual(data, {'meta': {'count': 'deactivated '}})
+        self.assertEqual(data, {'meta': {'count': 'deactivated'}})
         
         settings.FOREST['DEACTIVATED_COUNT'] = ['tests_fake']
         url = reverse('django_forest:resources:count', kwargs={'resource': 'tests_question'})
         response = self.client.get(url)
         data = response.json()
         self.assertEqual(response.status_code, 200)
         self.assertEqual(data, {'count': 3})
@@ -84,15 +84,15 @@
 
         url = reverse('django_forest:resources:count', kwargs={'resource': 'tests_question'})
         response = self.client.get(url, {
             'search': 'yes',
         })
         data = response.json()
         self.assertEqual(response.status_code, 200)
-        self.assertEqual(data, {'meta': {'count': 'deactivated '}})
+        self.assertEqual(data, {'meta': {'count': 'deactivated'}})
         del settings.MIDDLEWARE[0]
 
     @mock.patch('jose.jwt.decode', return_value={'id': 1})
     def test_get_invalid_token(self, *args, **kwargs):
         url = reverse('django_forest:resources:count', kwargs={'resource': 'tests_question'})
         response = self.client.get(url)
         data = response.json()
```

### Comparing `django-forestadmin-1.4.8/django_forest/tests/resources/views/test_csv.py` & `django-forestadmin-1.4.9/django_forest/tests/resources/views/test_csv.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/tests/resources/views/test_detail.py` & `django-forestadmin-1.4.9/django_forest/tests/resources/views/test_detail.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/tests/settings.py` & `django-forestadmin-1.4.9/django_forest/tests/settings.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/tests/stats/views/test_live_queries.py` & `django-forestadmin-1.4.9/django_forest/tests/stats/views/test_live_queries.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/tests/stats/views/test_stats_with_parameters.py` & `django-forestadmin-1.4.9/django_forest/tests/stats/views/test_stats_with_parameters.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/tests/utils/test_collection.py` & `django-forestadmin-1.4.9/django_forest/tests/utils/test_collection.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/tests/utils/test_cors.py` & `django-forestadmin-1.4.9/django_forest/tests/utils/test_cors.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/tests/utils/test_date.py` & `django-forestadmin-1.4.9/django_forest/tests/utils/test_date.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/tests/utils/test_forest_api_requester.py` & `django-forestadmin-1.4.9/django_forest/tests/utils/test_forest_api_requester.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/tests/utils/test_get_forest_setting.py` & `django-forestadmin-1.4.9/django_forest/tests/utils/test_get_forest_setting.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/tests/utils/test_json_api_schema.py` & `django-forestadmin-1.4.9/django_forest/tests/utils/test_json_api_schema.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/tests/utils/test_schema.py` & `django-forestadmin-1.4.9/django_forest/tests/utils/test_schema.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/tests/views/test_scope_cache_invalidation.py` & `django-forestadmin-1.4.9/django_forest/tests/views/test_scope_cache_invalidation.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/urls.py` & `django-forestadmin-1.4.9/django_forest/urls.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/utils/__init__.py` & `django-forestadmin-1.4.9/django_forest/utils/__init__.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/utils/collection.py` & `django-forestadmin-1.4.9/django_forest/utils/collection.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/utils/cors.py` & `django-forestadmin-1.4.9/django_forest/utils/cors.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/utils/error_handler.py` & `django-forestadmin-1.4.9/django_forest/utils/error_handler.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/utils/forest_api_requester.py` & `django-forestadmin-1.4.9/django_forest/utils/forest_api_requester.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/utils/ip_whitelist.py` & `django-forestadmin-1.4.9/django_forest/utils/ip_whitelist.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/utils/models.py` & `django-forestadmin-1.4.9/django_forest/utils/models.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/utils/permissions/__init__.py` & `django-forestadmin-1.4.9/django_forest/utils/permissions/__init__.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/utils/permissions/utils.py` & `django-forestadmin-1.4.9/django_forest/utils/permissions/utils.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/utils/schema/__init__.py` & `django-forestadmin-1.4.9/django_forest/utils/schema/__init__.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/utils/schema/apimap_errors.py` & `django-forestadmin-1.4.9/django_forest/utils/schema/apimap_errors.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/utils/schema/definitions.py` & `django-forestadmin-1.4.9/django_forest/utils/schema/definitions.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/utils/schema/json_api_schema.py` & `django-forestadmin-1.4.9/django_forest/utils/schema/json_api_schema.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/utils/schema/validations.py` & `django-forestadmin-1.4.9/django_forest/utils/schema/validations.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/utils/scope.py` & `django-forestadmin-1.4.9/django_forest/utils/scope.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/utils/type_mapping.py` & `django-forestadmin-1.4.9/django_forest/utils/type_mapping.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/utils/views/action.py` & `django-forestadmin-1.4.9/django_forest/utils/views/action.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/utils/views/base.py` & `django-forestadmin-1.4.9/django_forest/utils/views/base.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forest/views/scope_cache_invalidation.py` & `django-forestadmin-1.4.9/django_forest/views/scope_cache_invalidation.py`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/django_forestadmin.egg-info/PKG-INFO` & `django-forestadmin-1.4.9/django_forestadmin.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: django-forestadmin
-Version: 1.4.8
+Version: 1.4.9
 Summary: The Django Liana for Forest Admin.
 Home-page: https://forestadmin.com/
 Author: Guillaume Cisco
 Author-email: guillaumec@forestadmin.com
 License: GNU General Public License v3 or later (GPLv3+)
 Classifier: Environment :: Web Environment
 Classifier: Framework :: Django
```

### Comparing `django-forestadmin-1.4.8/django_forestadmin.egg-info/SOURCES.txt` & `django-forestadmin-1.4.9/django_forestadmin.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `django-forestadmin-1.4.8/setup.cfg` & `django-forestadmin-1.4.9/setup.cfg`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [metadata]
 name = django-forestadmin
-version = 1.4.8
+version = 1.4.9
 description = The Django Liana for Forest Admin.
 long_description = file: README.md
 long_description_content_type = text/markdown
 url = https://forestadmin.com/
 author = Guillaume Cisco
 author_email = guillaumec@forestadmin.com
 license = GNU General Public License v3 or later (GPLv3+)
```

