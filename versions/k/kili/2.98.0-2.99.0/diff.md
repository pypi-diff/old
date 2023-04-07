# Comparing `tmp/kili-2.98.0.tar.gz` & `tmp/kili-2.99.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/kili-2.98.0.tar", last modified: Thu Nov  4 16:39:07 2021, max compression
+gzip compressed data, was "kili-2.99.0.tar", last modified: Wed Nov 17 08:13:54 2021, max compression
```

## Comparing `kili-2.98.0.tar` & `kili-2.99.0.tar`

### file list

```diff
@@ -1,108 +1,114 @@
-drwxr-xr-x   0 hugomailfait   (501) staff       (20)        0 2021-11-04 16:39:07.642077 kili-2.98.0/
--rw-r--r--   0 hugomailfait   (501) staff       (20)    10765 2021-03-31 15:02:08.000000 kili-2.98.0/LICENSE.txt
--rw-r--r--   0 hugomailfait   (501) staff       (20)       13 2021-03-31 15:02:08.000000 kili-2.98.0/MANIFEST.in
--rw-r--r--   0 hugomailfait   (501) staff       (20)     6635 2021-11-04 16:39:07.642223 kili-2.98.0/PKG-INFO
--rw-r--r--   0 hugomailfait   (501) staff       (20)     5506 2021-07-16 16:02:36.000000 kili-2.98.0/README.md
-drwxr-xr-x   0 hugomailfait   (501) staff       (20)        0 2021-11-04 16:39:07.590070 kili-2.98.0/kili/
--rw-r--r--   0 hugomailfait   (501) staff       (20)       95 2021-11-04 16:37:06.000000 kili-2.98.0/kili/__init__.py
--rw-r--r--   0 hugomailfait   (501) staff       (20)     3305 2021-10-18 15:13:16.000000 kili-2.98.0/kili/authentication.py
--rw-r--r--   0 hugomailfait   (501) staff       (20)     2868 2021-10-18 15:13:16.000000 kili-2.98.0/kili/client.py
--rw-r--r--   0 hugomailfait   (501) staff       (20)      179 2021-09-29 16:50:54.000000 kili-2.98.0/kili/constants.py
--rw-r--r--   0 hugomailfait   (501) staff       (20)     9369 2021-09-29 16:50:54.000000 kili-2.98.0/kili/graphql_client.py
--rw-r--r--   0 hugomailfait   (501) staff       (20)     9360 2021-09-29 16:50:54.000000 kili-2.98.0/kili/helpers.py
-drwxr-xr-x   0 hugomailfait   (501) staff       (20)        0 2021-11-04 16:39:07.592994 kili-2.98.0/kili/mutations/
--rw-r--r--   0 hugomailfait   (501) staff       (20)        0 2021-03-31 15:02:08.000000 kili-2.98.0/kili/mutations/__init__.py
-drwxr-xr-x   0 hugomailfait   (501) staff       (20)        0 2021-11-04 16:39:07.594288 kili-2.98.0/kili/mutations/api_key/
--rw-r--r--   0 hugomailfait   (501) staff       (20)     1127 2021-10-18 15:13:16.000000 kili-2.98.0/kili/mutations/api_key/__init__.py
--rw-r--r--   0 hugomailfait   (501) staff       (20)       85 2021-10-18 15:13:16.000000 kili-2.98.0/kili/mutations/api_key/fragments.py
--rw-r--r--   0 hugomailfait   (501) staff       (20)      264 2021-10-18 15:13:16.000000 kili-2.98.0/kili/mutations/api_key/queries.py
-drwxr-xr-x   0 hugomailfait   (501) staff       (20)        0 2021-11-04 16:39:07.596192 kili-2.98.0/kili/mutations/asset/
--rw-r--r--   0 hugomailfait   (501) staff       (20)    14318 2021-09-29 16:50:54.000000 kili-2.98.0/kili/mutations/asset/__init__.py
--rw-r--r--   0 hugomailfait   (501) staff       (20)       66 2021-09-29 16:50:54.000000 kili-2.98.0/kili/mutations/asset/fragments.py
--rw-r--r--   0 hugomailfait   (501) staff       (20)      682 2021-09-29 16:50:54.000000 kili-2.98.0/kili/mutations/asset/queries.py
-drwxr-xr-x   0 hugomailfait   (501) staff       (20)        0 2021-11-04 16:39:07.598646 kili-2.98.0/kili/mutations/dataset/
--rw-r--r--   0 hugomailfait   (501) staff       (20)     6536 2021-09-29 16:50:54.000000 kili-2.98.0/kili/mutations/dataset/__init__.py
--rw-r--r--   0 hugomailfait   (501) staff       (20)       70 2021-09-29 16:50:54.000000 kili-2.98.0/kili/mutations/dataset/fragments.py
--rw-r--r--   0 hugomailfait   (501) staff       (20)     1310 2021-09-29 16:50:54.000000 kili-2.98.0/kili/mutations/dataset/queries.py
-drwxr-xr-x   0 hugomailfait   (501) staff       (20)        0 2021-11-04 16:39:07.601288 kili-2.98.0/kili/mutations/dataset_asset/
--rw-r--r--   0 hugomailfait   (501) staff       (20)     5275 2021-09-29 16:50:54.000000 kili-2.98.0/kili/mutations/dataset_asset/__init__.py
--rw-r--r--   0 hugomailfait   (501) staff       (20)       74 2021-09-29 16:50:54.000000 kili-2.98.0/kili/mutations/dataset_asset/fragments.py
--rw-r--r--   0 hugomailfait   (501) staff       (20)      483 2021-09-29 16:50:54.000000 kili-2.98.0/kili/mutations/dataset_asset/queries.py
-drwxr-xr-x   0 hugomailfait   (501) staff       (20)        0 2021-11-04 16:39:07.604376 kili-2.98.0/kili/mutations/label/
--rw-r--r--   0 hugomailfait   (501) staff       (20)     8912 2021-09-29 16:50:54.000000 kili-2.98.0/kili/mutations/label/__init__.py
--rw-r--r--   0 hugomailfait   (501) staff       (20)      204 2021-09-29 16:50:54.000000 kili-2.98.0/kili/mutations/label/fragments.py
--rw-r--r--   0 hugomailfait   (501) staff       (20)     1076 2021-09-29 16:50:54.000000 kili-2.98.0/kili/mutations/label/queries.py
-drwxr-xr-x   0 hugomailfait   (501) staff       (20)        0 2021-11-04 16:39:07.606862 kili-2.98.0/kili/mutations/notification/
--rw-r--r--   0 hugomailfait   (501) staff       (20)     2328 2021-09-29 16:50:54.000000 kili-2.98.0/kili/mutations/notification/__init__.py
--rw-r--r--   0 hugomailfait   (501) staff       (20)       80 2021-09-29 16:50:54.000000 kili-2.98.0/kili/mutations/notification/fragments.py
--rw-r--r--   0 hugomailfait   (501) staff       (20)      604 2021-09-29 16:50:54.000000 kili-2.98.0/kili/mutations/notification/queries.py
-drwxr-xr-x   0 hugomailfait   (501) staff       (20)        0 2021-11-04 16:39:07.608852 kili-2.98.0/kili/mutations/organization/
--rw-r--r--   0 hugomailfait   (501) staff       (20)     3236 2021-09-29 16:50:54.000000 kili-2.98.0/kili/mutations/organization/__init__.py
--rw-r--r--   0 hugomailfait   (501) staff       (20)       80 2021-09-29 16:50:54.000000 kili-2.98.0/kili/mutations/organization/fragments.py
--rw-r--r--   0 hugomailfait   (501) staff       (20)      717 2021-09-29 16:50:54.000000 kili-2.98.0/kili/mutations/organization/queries.py
-drwxr-xr-x   0 hugomailfait   (501) staff       (20)        0 2021-11-04 16:39:07.611586 kili-2.98.0/kili/mutations/project/
--rw-r--r--   0 hugomailfait   (501) staff       (20)    15512 2021-11-04 16:21:59.000000 kili-2.98.0/kili/mutations/project/__init__.py
--rw-r--r--   0 hugomailfait   (501) staff       (20)      233 2021-09-29 16:50:54.000000 kili-2.98.0/kili/mutations/project/fragments.py
--rw-r--r--   0 hugomailfait   (501) staff       (20)     3322 2021-09-29 16:50:54.000000 kili-2.98.0/kili/mutations/project/queries.py
-drwxr-xr-x   0 hugomailfait   (501) staff       (20)        0 2021-11-04 16:39:07.613995 kili-2.98.0/kili/mutations/project_version/
--rw-r--r--   0 hugomailfait   (501) staff       (20)     1575 2021-09-29 16:50:54.000000 kili-2.98.0/kili/mutations/project_version/__init__.py
--rw-r--r--   0 hugomailfait   (501) staff       (20)      109 2021-09-29 16:50:54.000000 kili-2.98.0/kili/mutations/project_version/fragments.py
--rw-r--r--   0 hugomailfait   (501) staff       (20)      351 2021-09-29 16:50:54.000000 kili-2.98.0/kili/mutations/project_version/queries.py
-drwxr-xr-x   0 hugomailfait   (501) staff       (20)        0 2021-11-04 16:39:07.615888 kili-2.98.0/kili/mutations/user/
--rw-r--r--   0 hugomailfait   (501) staff       (20)     5093 2021-10-18 15:13:16.000000 kili-2.98.0/kili/mutations/user/__init__.py
--rw-r--r--   0 hugomailfait   (501) staff       (20)      120 2021-09-29 16:50:54.000000 kili-2.98.0/kili/mutations/user/fragments.py
--rw-r--r--   0 hugomailfait   (501) staff       (20)      989 2021-10-18 15:13:16.000000 kili-2.98.0/kili/mutations/user/queries.py
--rw-r--r--   0 hugomailfait   (501) staff       (20)     4868 2021-11-04 16:21:59.000000 kili-2.98.0/kili/orm.py
-drwxr-xr-x   0 hugomailfait   (501) staff       (20)        0 2021-11-04 16:39:07.616595 kili-2.98.0/kili/queries/
--rw-r--r--   0 hugomailfait   (501) staff       (20)        0 2021-03-31 15:02:08.000000 kili-2.98.0/kili/queries/__init__.py
-drwxr-xr-x   0 hugomailfait   (501) staff       (20)        0 2021-11-04 16:39:07.618735 kili-2.98.0/kili/queries/asset/
--rw-r--r--   0 hugomailfait   (501) staff       (20)    19327 2021-09-29 16:50:54.000000 kili-2.98.0/kili/queries/asset/__init__.py
--rw-r--r--   0 hugomailfait   (501) staff       (20)      374 2021-09-29 16:50:54.000000 kili-2.98.0/kili/queries/asset/queries.py
-drwxr-xr-x   0 hugomailfait   (501) staff       (20)        0 2021-11-04 16:39:07.623004 kili-2.98.0/kili/queries/dataset_asset/
--rw-r--r--   0 hugomailfait   (501) staff       (20)     5098 2021-09-29 16:50:54.000000 kili-2.98.0/kili/queries/dataset_asset/__init__.py
--rw-r--r--   0 hugomailfait   (501) staff       (20)      425 2021-09-29 16:50:54.000000 kili-2.98.0/kili/queries/dataset_asset/queries.py
-drwxr-xr-x   0 hugomailfait   (501) staff       (20)        0 2021-11-04 16:39:07.626425 kili-2.98.0/kili/queries/issue/
--rw-r--r--   0 hugomailfait   (501) staff       (20)     1960 2021-09-29 16:50:54.000000 kili-2.98.0/kili/queries/issue/__init__.py
--rw-r--r--   0 hugomailfait   (501) staff       (20)      375 2021-09-29 16:50:54.000000 kili-2.98.0/kili/queries/issue/queries.py
-drwxr-xr-x   0 hugomailfait   (501) staff       (20)        0 2021-11-04 16:39:07.633185 kili-2.98.0/kili/queries/label/
--rw-r--r--   0 hugomailfait   (501) staff       (20)    15403 2021-09-29 16:50:54.000000 kili-2.98.0/kili/queries/label/__init__.py
--rw-r--r--   0 hugomailfait   (501) staff       (20)      375 2021-09-29 16:50:54.000000 kili-2.98.0/kili/queries/label/queries.py
-drwxr-xr-x   0 hugomailfait   (501) staff       (20)        0 2021-11-04 16:39:07.634555 kili-2.98.0/kili/queries/lock/
--rw-r--r--   0 hugomailfait   (501) staff       (20)     2546 2021-09-29 16:50:54.000000 kili-2.98.0/kili/queries/lock/__init__.py
--rw-r--r--   0 hugomailfait   (501) staff       (20)      366 2021-09-29 16:50:54.000000 kili-2.98.0/kili/queries/lock/queries.py
-drwxr-xr-x   0 hugomailfait   (501) staff       (20)        0 2021-11-04 16:39:07.635339 kili-2.98.0/kili/queries/notification/
--rw-r--r--   0 hugomailfait   (501) staff       (20)     3924 2021-09-29 16:50:54.000000 kili-2.98.0/kili/queries/notification/__init__.py
--rw-r--r--   0 hugomailfait   (501) staff       (20)      431 2021-09-29 16:50:54.000000 kili-2.98.0/kili/queries/notification/queries.py
-drwxr-xr-x   0 hugomailfait   (501) staff       (20)        0 2021-11-04 16:39:07.636336 kili-2.98.0/kili/queries/organization/
--rw-r--r--   0 hugomailfait   (501) staff       (20)     4509 2021-09-29 16:50:54.000000 kili-2.98.0/kili/queries/organization/__init__.py
--rw-r--r--   0 hugomailfait   (501) staff       (20)      629 2021-09-29 16:50:54.000000 kili-2.98.0/kili/queries/organization/queries.py
-drwxr-xr-x   0 hugomailfait   (501) staff       (20)        0 2021-11-04 16:39:07.637347 kili-2.98.0/kili/queries/project/
--rw-r--r--   0 hugomailfait   (501) staff       (20)     6279 2021-09-29 16:50:54.000000 kili-2.98.0/kili/queries/project/__init__.py
--rw-r--r--   0 hugomailfait   (501) staff       (20)      395 2021-09-29 16:50:54.000000 kili-2.98.0/kili/queries/project/queries.py
-drwxr-xr-x   0 hugomailfait   (501) staff       (20)        0 2021-11-04 16:39:07.638303 kili-2.98.0/kili/queries/project_user/
--rw-r--r--   0 hugomailfait   (501) staff       (20)     4418 2021-09-29 16:50:54.000000 kili-2.98.0/kili/queries/project_user/__init__.py
--rw-r--r--   0 hugomailfait   (501) staff       (20)      425 2021-09-29 16:50:54.000000 kili-2.98.0/kili/queries/project_user/queries.py
-drwxr-xr-x   0 hugomailfait   (501) staff       (20)        0 2021-11-04 16:39:07.639094 kili-2.98.0/kili/queries/project_version/
--rw-r--r--   0 hugomailfait   (501) staff       (20)     3105 2021-09-29 16:50:54.000000 kili-2.98.0/kili/queries/project_version/__init__.py
--rw-r--r--   0 hugomailfait   (501) staff       (20)      447 2021-09-29 16:50:54.000000 kili-2.98.0/kili/queries/project_version/queries.py
-drwxr-xr-x   0 hugomailfait   (501) staff       (20)        0 2021-11-04 16:39:07.639913 kili-2.98.0/kili/queries/user/
--rw-r--r--   0 hugomailfait   (501) staff       (20)     3314 2021-09-29 16:50:54.000000 kili-2.98.0/kili/queries/user/__init__.py
--rw-r--r--   0 hugomailfait   (501) staff       (20)      366 2021-09-29 16:50:54.000000 kili-2.98.0/kili/queries/user/queries.py
-drwxr-xr-x   0 hugomailfait   (501) staff       (20)        0 2021-11-04 16:39:07.640303 kili-2.98.0/kili/subscriptions/
--rw-r--r--   0 hugomailfait   (501) staff       (20)        0 2021-03-31 15:02:08.000000 kili-2.98.0/kili/subscriptions/__init__.py
-drwxr-xr-x   0 hugomailfait   (501) staff       (20)        0 2021-11-04 16:39:07.641430 kili-2.98.0/kili/subscriptions/label/
--rw-r--r--   0 hugomailfait   (501) staff       (20)     1873 2021-09-29 16:50:54.000000 kili-2.98.0/kili/subscriptions/label/__init__.py
--rw-r--r--   0 hugomailfait   (501) staff       (20)       82 2021-09-29 16:50:54.000000 kili-2.98.0/kili/subscriptions/label/fragments.py
--rw-r--r--   0 hugomailfait   (501) staff       (20)      236 2021-09-29 16:50:54.000000 kili-2.98.0/kili/subscriptions/label/subscriptions.py
--rw-r--r--   0 hugomailfait   (501) staff       (20)     5219 2021-09-29 16:50:54.000000 kili-2.98.0/kili/transfer_learning.py
--rw-r--r--   0 hugomailfait   (501) staff       (20)     9035 2021-11-04 16:21:59.000000 kili-2.98.0/kili/types.py
-drwxr-xr-x   0 hugomailfait   (501) staff       (20)        0 2021-11-04 16:39:07.592584 kili-2.98.0/kili.egg-info/
--rw-r--r--   0 hugomailfait   (501) staff       (20)     6635 2021-11-04 16:39:07.000000 kili-2.98.0/kili.egg-info/PKG-INFO
--rw-r--r--   0 hugomailfait   (501) staff       (20)     2461 2021-11-04 16:39:07.000000 kili-2.98.0/kili.egg-info/SOURCES.txt
--rw-r--r--   0 hugomailfait   (501) staff       (20)        1 2021-11-04 16:39:07.000000 kili-2.98.0/kili.egg-info/dependency_links.txt
--rw-r--r--   0 hugomailfait   (501) staff       (20)       20 2021-11-04 16:39:07.000000 kili-2.98.0/kili.egg-info/entry_points.txt
--rw-r--r--   0 hugomailfait   (501) staff       (20)       59 2021-11-04 16:39:07.000000 kili-2.98.0/kili.egg-info/requires.txt
--rw-r--r--   0 hugomailfait   (501) staff       (20)        5 2021-11-04 16:39:07.000000 kili-2.98.0/kili.egg-info/top_level.txt
--rw-r--r--   0 hugomailfait   (501) staff       (20)      142 2021-03-31 15:02:08.000000 kili-2.98.0/pull_request_template.md
--rw-r--r--   0 hugomailfait   (501) staff       (20)       79 2021-11-04 16:39:07.642732 kili-2.98.0/setup.cfg
--rw-r--r--   0 hugomailfait   (501) staff       (20)     2388 2021-09-29 16:50:54.000000 kili-2.98.0/setup.py
+drwxr-xr-x   0 theodullin   (501) staff       (20)        0 2021-11-17 08:13:54.993244 kili-2.99.0/
+-rw-r--r--   0 theodullin   (501) staff       (20)    10765 2021-04-12 16:58:09.000000 kili-2.99.0/LICENSE.txt
+-rw-r--r--   0 theodullin   (501) staff       (20)       13 2021-04-12 16:58:09.000000 kili-2.99.0/MANIFEST.in
+-rw-r--r--   0 theodullin   (501) staff       (20)     6635 2021-11-17 08:13:54.993591 kili-2.99.0/PKG-INFO
+-rw-r--r--   0 theodullin   (501) staff       (20)     5506 2021-05-05 14:44:21.000000 kili-2.99.0/README.md
+drwxr-xr-x   0 theodullin   (501) staff       (20)        0 2021-11-17 08:13:54.942820 kili-2.99.0/kili/
+-rw-r--r--   0 theodullin   (501) staff       (20)       95 2021-11-17 08:12:06.000000 kili-2.99.0/kili/__init__.py
+-rw-r--r--   0 theodullin   (501) staff       (20)     4367 2021-11-10 08:40:53.000000 kili-2.99.0/kili/authentication.py
+-rw-r--r--   0 theodullin   (501) staff       (20)     3010 2021-11-16 08:43:33.000000 kili-2.99.0/kili/client.py
+-rw-r--r--   0 theodullin   (501) staff       (20)      179 2021-09-21 14:24:57.000000 kili-2.99.0/kili/constants.py
+-rw-r--r--   0 theodullin   (501) staff       (20)     9369 2021-09-21 14:24:57.000000 kili-2.99.0/kili/graphql_client.py
+-rw-r--r--   0 theodullin   (501) staff       (20)     9360 2021-09-21 14:24:57.000000 kili-2.99.0/kili/helpers.py
+drwxr-xr-x   0 theodullin   (501) staff       (20)        0 2021-11-17 08:13:54.947240 kili-2.99.0/kili/mutations/
+-rw-r--r--   0 theodullin   (501) staff       (20)        0 2021-04-12 16:58:09.000000 kili-2.99.0/kili/mutations/__init__.py
+drwxr-xr-x   0 theodullin   (501) staff       (20)        0 2021-11-17 08:13:54.948869 kili-2.99.0/kili/mutations/api_key/
+-rw-r--r--   0 theodullin   (501) staff       (20)     1127 2021-10-25 08:54:31.000000 kili-2.99.0/kili/mutations/api_key/__init__.py
+-rw-r--r--   0 theodullin   (501) staff       (20)       85 2021-10-25 08:54:31.000000 kili-2.99.0/kili/mutations/api_key/fragments.py
+-rw-r--r--   0 theodullin   (501) staff       (20)      264 2021-10-25 08:54:31.000000 kili-2.99.0/kili/mutations/api_key/queries.py
+drwxr-xr-x   0 theodullin   (501) staff       (20)        0 2021-11-17 08:13:54.950172 kili-2.99.0/kili/mutations/asset/
+-rw-r--r--   0 theodullin   (501) staff       (20)    14318 2021-09-21 14:24:57.000000 kili-2.99.0/kili/mutations/asset/__init__.py
+-rw-r--r--   0 theodullin   (501) staff       (20)       66 2021-09-21 14:24:57.000000 kili-2.99.0/kili/mutations/asset/fragments.py
+-rw-r--r--   0 theodullin   (501) staff       (20)      682 2021-09-21 14:24:57.000000 kili-2.99.0/kili/mutations/asset/queries.py
+drwxr-xr-x   0 theodullin   (501) staff       (20)        0 2021-11-17 08:13:54.951267 kili-2.99.0/kili/mutations/dataset/
+-rw-r--r--   0 theodullin   (501) staff       (20)     6536 2021-09-23 07:53:48.000000 kili-2.99.0/kili/mutations/dataset/__init__.py
+-rw-r--r--   0 theodullin   (501) staff       (20)       70 2021-09-21 14:24:57.000000 kili-2.99.0/kili/mutations/dataset/fragments.py
+-rw-r--r--   0 theodullin   (501) staff       (20)     1310 2021-09-23 07:53:48.000000 kili-2.99.0/kili/mutations/dataset/queries.py
+drwxr-xr-x   0 theodullin   (501) staff       (20)        0 2021-11-17 08:13:54.952192 kili-2.99.0/kili/mutations/dataset_asset/
+-rw-r--r--   0 theodullin   (501) staff       (20)     5275 2021-09-21 14:24:57.000000 kili-2.99.0/kili/mutations/dataset_asset/__init__.py
+-rw-r--r--   0 theodullin   (501) staff       (20)       74 2021-09-21 14:24:57.000000 kili-2.99.0/kili/mutations/dataset_asset/fragments.py
+-rw-r--r--   0 theodullin   (501) staff       (20)      483 2021-09-21 14:24:57.000000 kili-2.99.0/kili/mutations/dataset_asset/queries.py
+drwxr-xr-x   0 theodullin   (501) staff       (20)        0 2021-11-17 08:13:54.953194 kili-2.99.0/kili/mutations/label/
+-rw-r--r--   0 theodullin   (501) staff       (20)     8912 2021-09-21 14:24:57.000000 kili-2.99.0/kili/mutations/label/__init__.py
+-rw-r--r--   0 theodullin   (501) staff       (20)      204 2021-09-21 14:24:57.000000 kili-2.99.0/kili/mutations/label/fragments.py
+-rw-r--r--   0 theodullin   (501) staff       (20)     1076 2021-09-21 14:24:57.000000 kili-2.99.0/kili/mutations/label/queries.py
+drwxr-xr-x   0 theodullin   (501) staff       (20)        0 2021-11-17 08:13:54.953948 kili-2.99.0/kili/mutations/notification/
+-rw-r--r--   0 theodullin   (501) staff       (20)     2328 2021-09-21 14:24:57.000000 kili-2.99.0/kili/mutations/notification/__init__.py
+-rw-r--r--   0 theodullin   (501) staff       (20)       80 2021-09-21 14:24:57.000000 kili-2.99.0/kili/mutations/notification/fragments.py
+-rw-r--r--   0 theodullin   (501) staff       (20)      604 2021-09-21 14:24:57.000000 kili-2.99.0/kili/mutations/notification/queries.py
+drwxr-xr-x   0 theodullin   (501) staff       (20)        0 2021-11-17 08:13:54.954929 kili-2.99.0/kili/mutations/organization/
+-rw-r--r--   0 theodullin   (501) staff       (20)     3447 2021-11-12 14:40:01.000000 kili-2.99.0/kili/mutations/organization/__init__.py
+-rw-r--r--   0 theodullin   (501) staff       (20)       80 2021-09-21 14:24:57.000000 kili-2.99.0/kili/mutations/organization/fragments.py
+-rw-r--r--   0 theodullin   (501) staff       (20)      717 2021-09-21 14:24:57.000000 kili-2.99.0/kili/mutations/organization/queries.py
+drwxr-xr-x   0 theodullin   (501) staff       (20)        0 2021-11-17 08:13:54.956337 kili-2.99.0/kili/mutations/project/
+-rw-r--r--   0 theodullin   (501) staff       (20)    15512 2021-10-25 08:54:31.000000 kili-2.99.0/kili/mutations/project/__init__.py
+-rw-r--r--   0 theodullin   (501) staff       (20)      233 2021-09-21 14:24:57.000000 kili-2.99.0/kili/mutations/project/fragments.py
+-rw-r--r--   0 theodullin   (501) staff       (20)     3322 2021-09-21 14:24:57.000000 kili-2.99.0/kili/mutations/project/queries.py
+drwxr-xr-x   0 theodullin   (501) staff       (20)        0 2021-11-17 08:13:54.957387 kili-2.99.0/kili/mutations/project_version/
+-rw-r--r--   0 theodullin   (501) staff       (20)     1575 2021-09-21 14:24:57.000000 kili-2.99.0/kili/mutations/project_version/__init__.py
+-rw-r--r--   0 theodullin   (501) staff       (20)      109 2021-09-21 14:24:57.000000 kili-2.99.0/kili/mutations/project_version/fragments.py
+-rw-r--r--   0 theodullin   (501) staff       (20)      351 2021-09-21 14:24:57.000000 kili-2.99.0/kili/mutations/project_version/queries.py
+drwxr-xr-x   0 theodullin   (501) staff       (20)        0 2021-11-17 08:13:54.958585 kili-2.99.0/kili/mutations/user/
+-rw-r--r--   0 theodullin   (501) staff       (20)     5093 2021-10-25 08:54:31.000000 kili-2.99.0/kili/mutations/user/__init__.py
+-rw-r--r--   0 theodullin   (501) staff       (20)      120 2021-09-21 14:24:57.000000 kili-2.99.0/kili/mutations/user/fragments.py
+-rw-r--r--   0 theodullin   (501) staff       (20)      989 2021-10-25 08:54:31.000000 kili-2.99.0/kili/mutations/user/queries.py
+-rw-r--r--   0 theodullin   (501) staff       (20)     4868 2021-10-25 08:54:31.000000 kili-2.99.0/kili/orm.py
+drwxr-xr-x   0 theodullin   (501) staff       (20)        0 2021-11-17 08:13:54.959270 kili-2.99.0/kili/queries/
+-rw-r--r--   0 theodullin   (501) staff       (20)        0 2021-04-12 16:58:09.000000 kili-2.99.0/kili/queries/__init__.py
+drwxr-xr-x   0 theodullin   (501) staff       (20)        0 2021-11-17 08:13:54.960312 kili-2.99.0/kili/queries/api_key/
+-rw-r--r--   0 theodullin   (501) staff       (20)     3968 2021-11-10 08:40:53.000000 kili-2.99.0/kili/queries/api_key/__init__.py
+-rw-r--r--   0 theodullin   (501) staff       (20)      382 2021-11-10 08:40:53.000000 kili-2.99.0/kili/queries/api_key/queries.py
+drwxr-xr-x   0 theodullin   (501) staff       (20)        0 2021-11-17 08:13:54.961614 kili-2.99.0/kili/queries/asset/
+-rw-r--r--   0 theodullin   (501) staff       (20)    19327 2021-09-21 14:24:57.000000 kili-2.99.0/kili/queries/asset/__init__.py
+-rw-r--r--   0 theodullin   (501) staff       (20)      374 2021-09-21 14:24:57.000000 kili-2.99.0/kili/queries/asset/queries.py
+drwxr-xr-x   0 theodullin   (501) staff       (20)        0 2021-11-17 08:13:54.962501 kili-2.99.0/kili/queries/dataset/
+-rw-r--r--   0 theodullin   (501) staff       (20)     3321 2021-11-16 08:43:33.000000 kili-2.99.0/kili/queries/dataset/__init__.py
+-rw-r--r--   0 theodullin   (501) staff       (20)      395 2021-11-16 08:43:33.000000 kili-2.99.0/kili/queries/dataset/queries.py
+drwxr-xr-x   0 theodullin   (501) staff       (20)        0 2021-11-17 08:13:54.963434 kili-2.99.0/kili/queries/dataset_asset/
+-rw-r--r--   0 theodullin   (501) staff       (20)     5098 2021-09-21 14:24:57.000000 kili-2.99.0/kili/queries/dataset_asset/__init__.py
+-rw-r--r--   0 theodullin   (501) staff       (20)      425 2021-09-21 14:24:57.000000 kili-2.99.0/kili/queries/dataset_asset/queries.py
+drwxr-xr-x   0 theodullin   (501) staff       (20)        0 2021-11-17 08:13:54.976278 kili-2.99.0/kili/queries/issue/
+-rw-r--r--   0 theodullin   (501) staff       (20)     1960 2021-09-21 14:24:57.000000 kili-2.99.0/kili/queries/issue/__init__.py
+-rw-r--r--   0 theodullin   (501) staff       (20)      375 2021-09-21 14:24:57.000000 kili-2.99.0/kili/queries/issue/queries.py
+drwxr-xr-x   0 theodullin   (501) staff       (20)        0 2021-11-17 08:13:54.977592 kili-2.99.0/kili/queries/label/
+-rw-r--r--   0 theodullin   (501) staff       (20)    15403 2021-09-21 14:24:57.000000 kili-2.99.0/kili/queries/label/__init__.py
+-rw-r--r--   0 theodullin   (501) staff       (20)      375 2021-09-21 14:24:57.000000 kili-2.99.0/kili/queries/label/queries.py
+drwxr-xr-x   0 theodullin   (501) staff       (20)        0 2021-11-17 08:13:54.978729 kili-2.99.0/kili/queries/lock/
+-rw-r--r--   0 theodullin   (501) staff       (20)     2546 2021-09-21 14:24:57.000000 kili-2.99.0/kili/queries/lock/__init__.py
+-rw-r--r--   0 theodullin   (501) staff       (20)      366 2021-09-21 14:24:57.000000 kili-2.99.0/kili/queries/lock/queries.py
+drwxr-xr-x   0 theodullin   (501) staff       (20)        0 2021-11-17 08:13:54.979868 kili-2.99.0/kili/queries/notification/
+-rw-r--r--   0 theodullin   (501) staff       (20)     3924 2021-09-21 14:24:57.000000 kili-2.99.0/kili/queries/notification/__init__.py
+-rw-r--r--   0 theodullin   (501) staff       (20)      431 2021-09-21 14:24:57.000000 kili-2.99.0/kili/queries/notification/queries.py
+drwxr-xr-x   0 theodullin   (501) staff       (20)        0 2021-11-17 08:13:54.981011 kili-2.99.0/kili/queries/organization/
+-rw-r--r--   0 theodullin   (501) staff       (20)     4509 2021-09-21 14:24:57.000000 kili-2.99.0/kili/queries/organization/__init__.py
+-rw-r--r--   0 theodullin   (501) staff       (20)      629 2021-09-21 14:24:57.000000 kili-2.99.0/kili/queries/organization/queries.py
+drwxr-xr-x   0 theodullin   (501) staff       (20)        0 2021-11-17 08:13:54.982049 kili-2.99.0/kili/queries/project/
+-rw-r--r--   0 theodullin   (501) staff       (20)     6279 2021-09-21 14:24:57.000000 kili-2.99.0/kili/queries/project/__init__.py
+-rw-r--r--   0 theodullin   (501) staff       (20)      395 2021-09-21 14:24:57.000000 kili-2.99.0/kili/queries/project/queries.py
+drwxr-xr-x   0 theodullin   (501) staff       (20)        0 2021-11-17 08:13:54.983159 kili-2.99.0/kili/queries/project_user/
+-rw-r--r--   0 theodullin   (501) staff       (20)     4418 2021-09-21 14:24:57.000000 kili-2.99.0/kili/queries/project_user/__init__.py
+-rw-r--r--   0 theodullin   (501) staff       (20)      425 2021-09-21 14:24:57.000000 kili-2.99.0/kili/queries/project_user/queries.py
+drwxr-xr-x   0 theodullin   (501) staff       (20)        0 2021-11-17 08:13:54.984442 kili-2.99.0/kili/queries/project_version/
+-rw-r--r--   0 theodullin   (501) staff       (20)     3105 2021-09-21 14:24:57.000000 kili-2.99.0/kili/queries/project_version/__init__.py
+-rw-r--r--   0 theodullin   (501) staff       (20)      447 2021-09-21 14:24:57.000000 kili-2.99.0/kili/queries/project_version/queries.py
+drwxr-xr-x   0 theodullin   (501) staff       (20)        0 2021-11-17 08:13:54.985770 kili-2.99.0/kili/queries/user/
+-rw-r--r--   0 theodullin   (501) staff       (20)     3314 2021-09-21 14:24:57.000000 kili-2.99.0/kili/queries/user/__init__.py
+-rw-r--r--   0 theodullin   (501) staff       (20)      366 2021-09-21 14:24:57.000000 kili-2.99.0/kili/queries/user/queries.py
+drwxr-xr-x   0 theodullin   (501) staff       (20)        0 2021-11-17 08:13:54.990151 kili-2.99.0/kili/subscriptions/
+-rw-r--r--   0 theodullin   (501) staff       (20)        0 2021-04-12 16:58:09.000000 kili-2.99.0/kili/subscriptions/__init__.py
+drwxr-xr-x   0 theodullin   (501) staff       (20)        0 2021-11-17 08:13:54.992398 kili-2.99.0/kili/subscriptions/label/
+-rw-r--r--   0 theodullin   (501) staff       (20)     1873 2021-09-21 14:24:57.000000 kili-2.99.0/kili/subscriptions/label/__init__.py
+-rw-r--r--   0 theodullin   (501) staff       (20)       82 2021-09-21 14:24:57.000000 kili-2.99.0/kili/subscriptions/label/fragments.py
+-rw-r--r--   0 theodullin   (501) staff       (20)      236 2021-09-21 14:24:57.000000 kili-2.99.0/kili/subscriptions/label/subscriptions.py
+-rw-r--r--   0 theodullin   (501) staff       (20)     5219 2021-09-21 14:24:57.000000 kili-2.99.0/kili/transfer_learning.py
+-rw-r--r--   0 theodullin   (501) staff       (20)     9811 2021-11-16 08:43:33.000000 kili-2.99.0/kili/types.py
+drwxr-xr-x   0 theodullin   (501) staff       (20)        0 2021-11-17 08:13:54.946540 kili-2.99.0/kili.egg-info/
+-rw-r--r--   0 theodullin   (501) staff       (20)     6635 2021-11-17 08:13:54.000000 kili-2.99.0/kili.egg-info/PKG-INFO
+-rw-r--r--   0 theodullin   (501) staff       (20)     2591 2021-11-17 08:13:54.000000 kili-2.99.0/kili.egg-info/SOURCES.txt
+-rw-r--r--   0 theodullin   (501) staff       (20)        1 2021-11-17 08:13:54.000000 kili-2.99.0/kili.egg-info/dependency_links.txt
+-rw-r--r--   0 theodullin   (501) staff       (20)       20 2021-11-17 08:13:54.000000 kili-2.99.0/kili.egg-info/entry_points.txt
+-rw-r--r--   0 theodullin   (501) staff       (20)       59 2021-11-17 08:13:54.000000 kili-2.99.0/kili.egg-info/requires.txt
+-rw-r--r--   0 theodullin   (501) staff       (20)        5 2021-11-17 08:13:54.000000 kili-2.99.0/kili.egg-info/top_level.txt
+-rw-r--r--   0 theodullin   (501) staff       (20)      142 2021-04-12 16:58:09.000000 kili-2.99.0/pull_request_template.md
+-rw-r--r--   0 theodullin   (501) staff       (20)       79 2021-11-17 08:13:54.994662 kili-2.99.0/setup.cfg
+-rw-r--r--   0 theodullin   (501) staff       (20)     2388 2021-09-21 14:24:57.000000 kili-2.99.0/setup.py
```

### Comparing `kili-2.98.0/LICENSE.txt` & `kili-2.99.0/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `kili-2.98.0/PKG-INFO` & `kili-2.99.0/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: kili
-Version: 2.98.0
+Version: 2.99.0
 Summary: Python client for Kili Technology labeling tool
 Home-page: https://github.com/kili-technology/kili-playground
 Author: Kili Technology
 Author-email: contact@kili-technology.com
 License: UNKNOWN
 Platform: UNKNOWN
 Classifier: Intended Audience :: Science/Research
```

### Comparing `kili-2.98.0/README.md` & `kili-2.99.0/README.md`

 * *Files identical despite different names*

### Comparing `kili-2.98.0/kili/authentication.py` & `kili-2.99.0/kili/authentication.py`

 * *Files 22% similar despite different names*

```diff
@@ -1,19 +1,21 @@
 """
 API authentication module
 """
 
 import os
 import warnings
+from datetime import datetime, timedelta
 
 import requests
 
 from . import __version__
 from .graphql_client import GraphQLClient
 from .queries.user import QueriesUser
+from .queries.api_key import QueriesApiKey
 
 MAX_RETRIES = 20
 
 warnings.filterwarnings("default", module='kili', category=DeprecationWarning)
 
 
 def get_version_without_patch(version):
@@ -69,14 +71,15 @@
         self.client.inject_token('X-API-Key: ' + api_key)
         queries = QueriesUser(self)
         users = queries.users(api_key=api_key, fields=['id', 'email'])
         if len(users) == 0:
             raise Exception('No user attached to the API key was found')
         self.user_id = users[0]['id']
         self.user_email = users[0]['email']
+        self.check_expiry_of_key_is_close(api_key)
 
     def __del__(self):
         self.session.close()
 
     def check_versions_match(self, api_endpoint):
         """
         Checks that the versions of Kili Playground and Kili API are the same
@@ -88,7 +91,29 @@
         url = api_endpoint.replace('/graphql', '/version')
         response = requests.get(url, verify=self.verify).json()
         version = response['version']
         if get_version_without_patch(version) != get_version_without_patch(__version__):
             message = 'Kili Playground version should match with Kili API version.\n' + \
                       f'Please install version: "pip install kili=={version}"'
             warnings.warn(message, UserWarning)
+
+    def check_expiry_of_key_is_close(self, api_key):
+        """
+        Checks that the expiration date of the api_key is not too close
+
+        Parameters
+        ----------
+        - api_key: key used to connect to the Kili API
+        """
+        duration_days = 365
+        warn_days = 30
+        queries = QueriesApiKey(self)
+        key_object = queries.api_keys(api_key=api_key, fields=['createdAt'])
+        key_creation = datetime.strptime(key_object[0]['createdAt'], '%Y-%m-%dT%H:%M:%S.%fZ')
+        key_expiry = key_creation + timedelta(days=duration_days)
+        key_remaining_time = key_expiry - datetime.now()
+        key_soon_deprecated = key_remaining_time < timedelta(days=warn_days)
+        if key_soon_deprecated:
+            message = f"""
+Your api key will be deprecated on {key_expiry:%Y-%m-%d}.
+You should generate a new one on My account > API KEY."""
+            warnings.warn(message, UserWarning)
```

### Comparing `kili-2.98.0/kili/client.py` & `kili-2.99.0/kili/client.py`

 * *Files 14% similar despite different names*

```diff
@@ -9,15 +9,17 @@
 from kili.mutations.dataset_asset import MutationsDatasetAsset
 from kili.mutations.label import MutationsLabel
 from kili.mutations.notification import MutationsNotification
 from kili.mutations.organization import MutationsOrganization
 from kili.mutations.project import MutationsProject
 from kili.mutations.project_version import MutationsProjectVersion
 from kili.mutations.user import MutationsUser
+from kili.queries.api_key import QueriesApiKey
 from kili.queries.asset import QueriesAsset
+from kili.queries.dataset import QueriesDataset
 from kili.queries.dataset_asset import QueriesDatasetAsset
 from kili.queries.issue import QueriesIssue
 from kili.queries.label import QueriesLabel
 from kili.queries.lock import QueriesLock
 from kili.queries.organization import QueriesOrganization
 from kili.queries.notification import QueriesNotification
 from kili.queries.project import QueriesProject
@@ -37,15 +39,17 @@
         MutationsDatasetAsset,
         MutationsLabel,
         MutationsNotification,
         MutationsOrganization,
         MutationsProject,
         MutationsProjectVersion,
         MutationsUser,
+        QueriesApiKey,
         QueriesAsset,
+        QueriesDataset,
         QueriesDatasetAsset,
         QueriesIssue,
         QueriesLabel,
         QueriesLock,
         QueriesOrganization,
         QueriesNotification,
         QueriesProject,
```

### Comparing `kili-2.98.0/kili/graphql_client.py` & `kili-2.99.0/kili/graphql_client.py`

 * *Files identical despite different names*

### Comparing `kili-2.98.0/kili/helpers.py` & `kili-2.99.0/kili/helpers.py`

 * *Files identical despite different names*

### Comparing `kili-2.98.0/kili/mutations/api_key/__init__.py` & `kili-2.99.0/kili/mutations/api_key/__init__.py`

 * *Files identical despite different names*

### Comparing `kili-2.98.0/kili/mutations/asset/__init__.py` & `kili-2.99.0/kili/mutations/asset/__init__.py`

 * *Files identical despite different names*

### Comparing `kili-2.98.0/kili/mutations/asset/queries.py` & `kili-2.99.0/kili/mutations/asset/queries.py`

 * *Files identical despite different names*

### Comparing `kili-2.98.0/kili/mutations/dataset/__init__.py` & `kili-2.99.0/kili/mutations/dataset/__init__.py`

 * *Files identical despite different names*

### Comparing `kili-2.98.0/kili/mutations/dataset/queries.py` & `kili-2.99.0/kili/mutations/dataset/queries.py`

 * *Files identical despite different names*

### Comparing `kili-2.98.0/kili/mutations/dataset_asset/__init__.py` & `kili-2.99.0/kili/mutations/dataset_asset/__init__.py`

 * *Files identical despite different names*

### Comparing `kili-2.98.0/kili/mutations/label/__init__.py` & `kili-2.99.0/kili/mutations/label/__init__.py`

 * *Files identical despite different names*

### Comparing `kili-2.98.0/kili/mutations/label/queries.py` & `kili-2.99.0/kili/mutations/label/queries.py`

 * *Files identical despite different names*

### Comparing `kili-2.98.0/kili/mutations/notification/__init__.py` & `kili-2.99.0/kili/mutations/notification/__init__.py`

 * *Files identical despite different names*

### Comparing `kili-2.98.0/kili/mutations/notification/queries.py` & `kili-2.99.0/kili/mutations/notification/queries.py`

 * *Files identical despite different names*

### Comparing `kili-2.98.0/kili/mutations/organization/__init__.py` & `kili-2.99.0/kili/mutations/organization/__init__.py`

 * *Files 4% similar despite different names*

```diff
@@ -58,26 +58,28 @@
         result = self.auth.client.execute(GQL_CREATE_ORGANIZATION, variables)
         return format_result('data', result)
 
     @Compatible(['v1', 'v2'])
     @typechecked
     def update_properties_in_organization(self,
                                           organization_id: str,
+                                          can_see_dataset: Optional[bool] = None,
                                           name: Optional[str] = None,
                                           address: Optional[str] = None,
                                           zip_code: Optional[str] = None,
                                           city: Optional[str] = None,
                                           country: Optional[str] = None,
                                           license: Optional[dict] = None):  # pylint: disable=redefined-builtin
         """
         Modify an organization
 
         Parameters
         ----------
         - organization_id : str
+        - can_see_dataset: bool
         - name : str
         - address : str
         - license : dict
         - zip_code : str
         - city : str
         - country : str
 
@@ -85,14 +87,16 @@
         -------
         - a result object which indicates if the mutation was successful, or an error message else.
         """
         license_str = None if not license else json.dumps(license)
         variables = {
             'id': organization_id
         }
+        if can_see_dataset is not None:
+            variables['canSeeDataset'] = can_see_dataset
         if name is not None:
             variables['name'] = name
         if address is not None:
             variables['address'] = address
         if license_str is not None:
             variables['license'] = license_str
         if zip_code is not None:
```

### Comparing `kili-2.98.0/kili/mutations/organization/queries.py` & `kili-2.99.0/kili/mutations/organization/queries.py`

 * *Files identical despite different names*

### Comparing `kili-2.98.0/kili/mutations/project/__init__.py` & `kili-2.99.0/kili/mutations/project/__init__.py`

 * *Files identical despite different names*

### Comparing `kili-2.98.0/kili/mutations/project/queries.py` & `kili-2.99.0/kili/mutations/project/queries.py`

 * *Files identical despite different names*

### Comparing `kili-2.98.0/kili/mutations/project_version/__init__.py` & `kili-2.99.0/kili/mutations/project_version/__init__.py`

 * *Files identical despite different names*

### Comparing `kili-2.98.0/kili/mutations/user/__init__.py` & `kili-2.99.0/kili/mutations/user/__init__.py`

 * *Files identical despite different names*

### Comparing `kili-2.98.0/kili/mutations/user/queries.py` & `kili-2.99.0/kili/mutations/user/queries.py`

 * *Files identical despite different names*

### Comparing `kili-2.98.0/kili/orm.py` & `kili-2.99.0/kili/orm.py`

 * *Files identical despite different names*

### Comparing `kili-2.98.0/kili/queries/asset/__init__.py` & `kili-2.99.0/kili/queries/asset/__init__.py`

 * *Files identical despite different names*

### Comparing `kili-2.98.0/kili/queries/dataset_asset/__init__.py` & `kili-2.99.0/kili/queries/dataset_asset/__init__.py`

 * *Files identical despite different names*

### Comparing `kili-2.98.0/kili/queries/issue/__init__.py` & `kili-2.99.0/kili/queries/issue/__init__.py`

 * *Files identical despite different names*

### Comparing `kili-2.98.0/kili/queries/label/__init__.py` & `kili-2.99.0/kili/queries/label/__init__.py`

 * *Files identical despite different names*

### Comparing `kili-2.98.0/kili/queries/lock/__init__.py` & `kili-2.99.0/kili/queries/lock/__init__.py`

 * *Files identical despite different names*

### Comparing `kili-2.98.0/kili/queries/notification/__init__.py` & `kili-2.99.0/kili/queries/notification/__init__.py`

 * *Files identical despite different names*

### Comparing `kili-2.98.0/kili/queries/organization/__init__.py` & `kili-2.99.0/kili/queries/organization/__init__.py`

 * *Files identical despite different names*

### Comparing `kili-2.98.0/kili/queries/organization/queries.py` & `kili-2.99.0/kili/queries/organization/queries.py`

 * *Files identical despite different names*

### Comparing `kili-2.98.0/kili/queries/project/__init__.py` & `kili-2.99.0/kili/queries/project/__init__.py`

 * *Files identical despite different names*

### Comparing `kili-2.98.0/kili/queries/project_user/__init__.py` & `kili-2.99.0/kili/queries/project_user/__init__.py`

 * *Files identical despite different names*

### Comparing `kili-2.98.0/kili/queries/project_version/__init__.py` & `kili-2.99.0/kili/queries/project_version/__init__.py`

 * *Files identical despite different names*

### Comparing `kili-2.98.0/kili/queries/user/__init__.py` & `kili-2.99.0/kili/queries/user/__init__.py`

 * *Files identical despite different names*

### Comparing `kili-2.98.0/kili/subscriptions/label/__init__.py` & `kili-2.99.0/kili/subscriptions/label/__init__.py`

 * *Files identical despite different names*

### Comparing `kili-2.98.0/kili/transfer_learning.py` & `kili-2.99.0/kili/transfer_learning.py`

 * *Files identical despite different names*

### Comparing `kili-2.98.0/kili/types.py` & `kili-2.99.0/kili/types.py`

 * *Files 2% similar despite different names*

```diff
@@ -11,14 +11,15 @@
 class OrganizationWithoutUser:
     """
     A wrapper for Organization GraphQL object.
     Defined in two steps to avoid cyclical dependencies.
     """
     id = 'id'
     address = 'address'
+    canSeeDataset = 'canSeeDataset'
     city = 'city'
     country = 'country'
     license = 'license'
     name = 'name'
     numberOfAnnotations = 'numberOfAnnotations'
     numberOfLabeledAssets = 'numberOfLabeledAssets'
     numberOfHours = 'numberOfHours'
@@ -130,20 +131,39 @@
     """
     A wrapper for ProjectUser GraphQL object.
     """
     project = ProjectWithoutDataset
 
 
 @dataclass
-class User(UserWithoutProjectUsers):
+class UserWithoutApiKey(UserWithoutProjectUsers):
     """
     A wrapper for User GraphQL object.
     """
     projectUsers = ProjectUser
 
+@dataclass
+class ApiKey:
+    """
+    A wrapper for DatasetAsset GraphQL object.
+    """
+    createdAt = 'createdAt'
+    id = 'id'
+    key = 'key'
+    name = 'name'
+    revoked = 'revoked'
+    user = UserWithoutApiKey
+    userId = 'userId'
+
+@dataclass
+class User(UserWithoutApiKey):
+    """
+    A wrapper for User GraphQL object.
+    """
+    apiKeys = ApiKey
 
 @dataclass
 class LabelWithoutLabelOf:
     """
     A wrapper for Label GraphQL object.
     Defined in two steps to avoid cyclical dependencies.
     """
@@ -227,14 +247,15 @@
     consensusMark = 'consensusMark'
     consensusMarkCompute = 'consensusMarkCompute'
     consensusMarkPerCategory = 'consensusMarkPerCategory'
     content = 'content'
     contentJson = 'contentJson'
     contentJsonCompute = 'contentJsonCompute'
     createdAt = 'createdAt'
+    datasetAssetId = 'datasetAssetId'
     duration = 'duration'
     durationCompute = 'durationCompute'
     externalId = 'externalId'
     honeypotMark = 'honeypotMark'
     honeypotMarkCompute = 'honeypotMarkCompute'
     inferenceMark = 'inferenceMark'
     inferenceMarkCompute = 'inferenceMarkCompute'
@@ -249,26 +270,30 @@
     locks = Lock
     metadataCompute = 'metadataCompute'
     metadata = 'metadata'
     numberOfValidLocks = 'numberOfValidLocks'
     numberOfValidLocksCompute = 'numberOfValidLocksCompute'
     priority = 'priority'
     project = ProjectWithoutDataset
+    projectId = 'projectId'
     projectIdCompute = 'projectIdCompute'
     readPermissionsFromLabels = 'readPermissionsFromLabels'
     skippedCompute = 'skippedCompute'
     skipped = 'skipped'
     status = 'status'
     statusCompute = 'statusCompute'
     thumbnail = 'thumbnail'
     thumbnailCompute = 'thumbnailCompute'
     toBeLabeledBy = ProjectUser
     updatedAt = 'updatedAt'
 
 
+
+
+
 @dataclass
 class DatasetAsset:
     """
     A wrapper for DatasetAsset GraphQL object.
     """
     id = 'id'
     assets = Asset
@@ -283,14 +308,29 @@
     metadata = 'metadata'
     thumbnail = 'thumbnail'
     thumbnailCompute = 'thumbnailCompute'
     updatedAt = 'updatedAt'
 
 
 @dataclass
+class Dataset:
+    """
+    A wrapper for Dataset GraphQL object.
+    """
+    id = 'id'
+    assets = DatasetAsset
+    createdAt = 'createdAt'
+    name = 'name'
+    numberOfAssets = 'numberOfAssets'
+    projectId = 'projectId'
+    type = 'type'
+    updatedAt = 'updatedAt'
+    users = User
+
+@dataclass
 class Label(LabelWithoutLabelOf):
     """
     A wrapper for Label GraphQL object.
     """
     labelOf = Asset
```

### Comparing `kili-2.98.0/kili.egg-info/PKG-INFO` & `kili-2.99.0/kili.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: kili
-Version: 2.98.0
+Version: 2.99.0
 Summary: Python client for Kili Technology labeling tool
 Home-page: https://github.com/kili-technology/kili-playground
 Author: Kili Technology
 Author-email: contact@kili-technology.com
 License: UNKNOWN
 Platform: UNKNOWN
 Classifier: Intended Audience :: Science/Research
```

### Comparing `kili-2.98.0/kili.egg-info/SOURCES.txt` & `kili-2.99.0/kili.egg-info/SOURCES.txt`

 * *Files 5% similar despite different names*

```diff
@@ -47,16 +47,20 @@
 kili/mutations/project_version/__init__.py
 kili/mutations/project_version/fragments.py
 kili/mutations/project_version/queries.py
 kili/mutations/user/__init__.py
 kili/mutations/user/fragments.py
 kili/mutations/user/queries.py
 kili/queries/__init__.py
+kili/queries/api_key/__init__.py
+kili/queries/api_key/queries.py
 kili/queries/asset/__init__.py
 kili/queries/asset/queries.py
+kili/queries/dataset/__init__.py
+kili/queries/dataset/queries.py
 kili/queries/dataset_asset/__init__.py
 kili/queries/dataset_asset/queries.py
 kili/queries/issue/__init__.py
 kili/queries/issue/queries.py
 kili/queries/label/__init__.py
 kili/queries/label/queries.py
 kili/queries/lock/__init__.py
```

### Comparing `kili-2.98.0/setup.py` & `kili-2.99.0/setup.py`

 * *Files identical despite different names*

