# Comparing `tmp/dataiku-api-client-9.0.0.tar.gz` & `tmp/dataiku-api-client-9.0.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/dataiku-api-client-9.0.0.tar", last modified: Fri May  7 12:05:03 2021, max compression
+gzip compressed data, was "dist/dataiku-api-client-9.0.1.tar", last modified: Fri Dec 17 09:43:48 2021, max compression
```

## Comparing `dataiku-api-client-9.0.0.tar` & `dataiku-api-client-9.0.1.tar`

### file list

```diff
@@ -1,61 +1,61 @@
-drwxr-xr-x   0 clement    (502) staff       (20)        0 2021-05-07 12:05:03.000000 dataiku-api-client-9.0.0/
--rw-r--r--   0 clement    (502) staff       (20)     2314 2021-05-07 12:05:03.000000 dataiku-api-client-9.0.0/PKG-INFO
--rw-r--r--   0 clement    (502) staff       (20)       35 2020-07-03 06:32:51.000000 dataiku-api-client-9.0.0/requirements.txt
-drwxr-xr-x   0 clement    (502) staff       (20)        0 2021-05-07 12:05:03.000000 dataiku-api-client-9.0.0/dataikuapi/
--rw-r--r--   0 clement    (502) staff       (20)     1721 2020-04-20 12:24:19.000000 dataiku-api-client-9.0.0/dataikuapi/base_client.py
--rw-r--r--   0 clement    (502) staff       (20)    45470 2021-05-07 12:00:27.000000 dataiku-api-client-9.0.0/dataikuapi/dssclient.py
--rw-r--r--   0 clement    (502) staff       (20)     8114 2020-09-15 07:13:50.000000 dataiku-api-client-9.0.0/dataikuapi/apinode_client.py
--rw-r--r--   0 clement    (502) staff       (20)      563 2020-03-23 09:39:58.000000 dataiku-api-client-9.0.0/dataikuapi/__init__.py
-drwxr-xr-x   0 clement    (502) staff       (20)        0 2021-05-07 12:05:03.000000 dataiku-api-client-9.0.0/dataikuapi/dss/
--rw-r--r--   0 clement    (502) staff       (20)     7941 2021-04-23 09:24:30.000000 dataiku-api-client-9.0.0/dataikuapi/dss/savedmodel.py
--rw-r--r--   0 clement    (502) staff       (20)     1946 2016-08-23 07:06:36.000000 dataiku-api-client-9.0.0/dataikuapi/dss/metrics.py
--rw-r--r--   0 clement    (502) staff       (20)    21255 2021-04-23 09:24:35.000000 dataiku-api-client-9.0.0/dataikuapi/dss/projectdeployer.py
--rw-r--r--   0 clement    (502) staff       (20)    21676 2021-02-21 14:38:22.000000 dataiku-api-client-9.0.0/dataikuapi/dss/apideployer.py
--rw-r--r--   0 clement    (502) staff       (20)    14527 2021-02-21 14:38:22.000000 dataiku-api-client-9.0.0/dataikuapi/dss/analysis.py
--rw-r--r--   0 clement    (502) staff       (20)    42791 2020-01-22 08:39:48.000000 dataiku-api-client-9.0.0/dataikuapi/dss/dataiku_app.py
--rw-r--r--   0 clement    (502) staff       (20)     1998 2021-02-21 14:38:22.000000 dataiku-api-client-9.0.0/dataikuapi/dss/job.py
--rw-r--r--   0 clement    (502) staff       (20)     4966 2021-04-23 09:24:35.000000 dataiku-api-client-9.0.0/dataikuapi/dss/apiservice.py
--rw-r--r--   0 clement    (502) staff       (20)        0 2015-07-31 12:07:25.000000 dataiku-api-client-9.0.0/dataikuapi/dss/__init__.py
--rw-r--r--   0 clement    (502) staff       (20)    26527 2021-02-21 14:38:22.000000 dataiku-api-client-9.0.0/dataikuapi/dss/flow.py
--rw-r--r--   0 clement    (502) staff       (20)     1553 2021-04-19 10:36:45.000000 dataiku-api-client-9.0.0/dataikuapi/dss/export.py
--rw-r--r--   0 clement    (502) staff       (20)   151363 2021-04-23 09:24:35.000000 dataiku-api-client-9.0.0/dataikuapi/dss/ml.py
--rw-r--r--   0 clement    (502) staff       (20)     1180 2018-04-30 06:28:17.000000 dataiku-api-client-9.0.0/dataikuapi/dss/meaning.py
--rw-r--r--   0 clement    (502) staff       (20)    35061 2021-04-14 06:59:19.000000 dataiku-api-client-9.0.0/dataikuapi/dss/dataset.py
--rw-r--r--   0 clement    (502) staff       (20)     8369 2021-02-21 14:38:22.000000 dataiku-api-client-9.0.0/dataikuapi/dss/managedfolder.py
--rw-r--r--   0 clement    (502) staff       (20)    35737 2021-02-21 14:38:22.000000 dataiku-api-client-9.0.0/dataikuapi/dss/admin.py
--rw-r--r--   0 clement    (502) staff       (20)     1319 2021-02-21 14:38:22.000000 dataiku-api-client-9.0.0/dataikuapi/dss/continuousactivity.py
--rw-r--r--   0 clement    (502) staff       (20)     8271 2021-02-21 14:38:22.000000 dataiku-api-client-9.0.0/dataikuapi/dss/utils.py
--rw-r--r--   0 clement    (502) staff       (20)    10805 2021-02-21 14:38:22.000000 dataiku-api-client-9.0.0/dataikuapi/dss/modelevaluationstore.py
--rw-r--r--   0 clement    (502) staff       (20)    27731 2021-05-07 12:00:27.000000 dataiku-api-client-9.0.0/dataikuapi/dss/scenario.py
--rw-r--r--   0 clement    (502) staff       (20)     4976 2021-02-21 14:38:22.000000 dataiku-api-client-9.0.0/dataikuapi/dss/app.py
--rw-r--r--   0 clement    (502) staff       (20)     9916 2021-02-21 14:38:22.000000 dataiku-api-client-9.0.0/dataikuapi/dss/plugin.py
--rw-r--r--   0 clement    (502) staff       (20)     3054 2021-05-07 12:00:27.000000 dataiku-api-client-9.0.0/dataikuapi/dss/future.py
--rw-r--r--   0 clement    (502) staff       (20)     8724 2020-07-03 06:32:51.000000 dataiku-api-client-9.0.0/dataikuapi/dss/statistics.py
--rw-r--r--   0 clement    (502) staff       (20)     6982 2020-07-03 06:32:51.000000 dataiku-api-client-9.0.0/dataikuapi/dss/discussion.py
--rw-r--r--   0 clement    (502) staff       (20)    14474 2021-02-21 14:38:22.000000 dataiku-api-client-9.0.0/dataikuapi/dss/streaming_endpoint.py
--rw-r--r--   0 clement    (502) staff       (20)    52561 2021-02-21 14:38:22.000000 dataiku-api-client-9.0.0/dataikuapi/dss/recipe.py
--rw-r--r--   0 clement    (502) staff       (20)     2665 2021-04-23 09:24:35.000000 dataiku-api-client-9.0.0/dataikuapi/dss/notebook.py
--rw-r--r--   0 clement    (502) staff       (20)     3063 2021-02-21 14:38:22.000000 dataiku-api-client-9.0.0/dataikuapi/dss/sqlquery.py
--rw-r--r--   0 clement    (502) staff       (20)    15427 2021-02-21 14:38:22.000000 dataiku-api-client-9.0.0/dataikuapi/dss/wiki.py
--rw-r--r--   0 clement    (502) staff       (20)     9451 2021-02-21 14:38:22.000000 dataiku-api-client-9.0.0/dataikuapi/dss/projectfolder.py
--rw-r--r--   0 clement    (502) staff       (20)     6326 2021-04-23 09:24:35.000000 dataiku-api-client-9.0.0/dataikuapi/dss/jupyternotebook.py
--rw-r--r--   0 clement    (502) staff       (20)     3887 2021-02-21 14:38:22.000000 dataiku-api-client-9.0.0/dataikuapi/dss/macro.py
--rw-r--r--   0 clement    (502) staff       (20)    76273 2021-04-23 09:35:05.000000 dataiku-api-client-9.0.0/dataikuapi/dss/project.py
--rw-r--r--   0 clement    (502) staff       (20)     2749 2021-02-21 14:38:22.000000 dataiku-api-client-9.0.0/dataikuapi/utils.py
-drwxr-xr-x   0 clement    (502) staff       (20)        0 2021-05-07 12:05:03.000000 dataiku-api-client-9.0.0/dataikuapi/apinode_admin/
--rw-r--r--   0 clement    (502) staff       (20)      715 2015-10-22 07:29:24.000000 dataiku-api-client-9.0.0/dataikuapi/apinode_admin/auth.py
--rw-r--r--   0 clement    (502) staff       (20)     2173 2016-08-23 07:06:36.000000 dataiku-api-client-9.0.0/dataikuapi/apinode_admin/service.py
--rw-r--r--   0 clement    (502) staff       (20)        0 2015-10-13 08:51:03.000000 dataiku-api-client-9.0.0/dataikuapi/apinode_admin/__init__.py
--rw-r--r--   0 clement    (502) staff       (20)     1228 2018-01-10 09:59:16.000000 dataiku-api-client-9.0.0/dataikuapi/apinode_admin_client.py
--rw-r--r--   0 clement    (502) staff       (20)       58 2017-01-03 07:27:57.000000 dataiku-api-client-9.0.0/MANIFEST.in
--rw-r--r--   0 clement    (502) staff       (20)      143 2020-07-03 06:32:51.000000 dataiku-api-client-9.0.0/README
-drwxr-xr-x   0 clement    (502) staff       (20)        0 2021-05-07 12:05:03.000000 dataiku-api-client-9.0.0/dataiku_api_client.egg-info/
--rw-r--r--   0 clement    (502) staff       (20)     2314 2021-05-07 12:05:03.000000 dataiku-api-client-9.0.0/dataiku_api_client.egg-info/PKG-INFO
--rw-r--r--   0 clement    (502) staff       (20)     1483 2021-05-07 12:05:03.000000 dataiku-api-client-9.0.0/dataiku_api_client.egg-info/SOURCES.txt
--rw-r--r--   0 clement    (502) staff       (20)       34 2021-05-07 12:05:03.000000 dataiku-api-client-9.0.0/dataiku_api_client.egg-info/requires.txt
--rw-r--r--   0 clement    (502) staff       (20)       11 2021-05-07 12:05:03.000000 dataiku-api-client-9.0.0/dataiku_api_client.egg-info/top_level.txt
--rw-r--r--   0 clement    (502) staff       (20)        1 2021-05-07 12:05:03.000000 dataiku-api-client-9.0.0/dataiku_api_client.egg-info/dependency_links.txt
--rw-r--r--   0 clement    (502) staff       (20)     1124 2021-02-21 14:39:04.000000 dataiku-api-client-9.0.0/setup.py
--rw-r--r--   0 clement    (502) staff       (20)       38 2021-05-07 12:05:03.000000 dataiku-api-client-9.0.0/setup.cfg
--rw-r--r--   0 clement    (502) staff       (20)      914 2021-05-07 12:02:01.000000 dataiku-api-client-9.0.0/HISTORY.txt
--rw-r--r--   0 clement    (502) staff       (20)      557 2021-05-07 12:02:23.000000 dataiku-api-client-9.0.0/LICENSE.txt
+drwxr-xr-x   0 clement    (502) staff       (20)        0 2021-12-17 09:43:48.000000 dataiku-api-client-9.0.1/
+-rw-r--r--   0 clement    (502) staff       (20)     2399 2021-12-17 09:43:48.000000 dataiku-api-client-9.0.1/PKG-INFO
+-rw-r--r--   0 clement    (502) staff       (20)       32 2021-12-17 09:38:40.000000 dataiku-api-client-9.0.1/requirements.txt
+drwxr-xr-x   0 clement    (502) staff       (20)        0 2021-12-17 09:43:48.000000 dataiku-api-client-9.0.1/dataikuapi/
+-rw-r--r--   0 clement    (502) staff       (20)     1721 2020-04-20 12:24:19.000000 dataiku-api-client-9.0.1/dataikuapi/base_client.py
+-rw-r--r--   0 clement    (502) staff       (20)    46640 2021-12-17 09:38:05.000000 dataiku-api-client-9.0.1/dataikuapi/dssclient.py
+-rw-r--r--   0 clement    (502) staff       (20)     8114 2020-09-15 07:13:50.000000 dataiku-api-client-9.0.1/dataikuapi/apinode_client.py
+-rw-r--r--   0 clement    (502) staff       (20)      563 2021-12-17 09:38:00.000000 dataiku-api-client-9.0.1/dataikuapi/__init__.py
+drwxr-xr-x   0 clement    (502) staff       (20)        0 2021-12-17 09:43:48.000000 dataiku-api-client-9.0.1/dataikuapi/dss/
+-rw-r--r--   0 clement    (502) staff       (20)     7941 2021-12-17 09:38:00.000000 dataiku-api-client-9.0.1/dataikuapi/dss/savedmodel.py
+-rw-r--r--   0 clement    (502) staff       (20)     1946 2021-12-17 09:38:00.000000 dataiku-api-client-9.0.1/dataikuapi/dss/metrics.py
+-rw-r--r--   0 clement    (502) staff       (20)    21255 2021-10-13 08:14:51.000000 dataiku-api-client-9.0.1/dataikuapi/dss/projectdeployer.py
+-rw-r--r--   0 clement    (502) staff       (20)    22336 2021-12-17 09:38:00.000000 dataiku-api-client-9.0.1/dataikuapi/dss/apideployer.py
+-rw-r--r--   0 clement    (502) staff       (20)    14527 2021-02-21 14:38:22.000000 dataiku-api-client-9.0.1/dataikuapi/dss/analysis.py
+-rw-r--r--   0 clement    (502) staff       (20)    42791 2020-01-22 08:39:48.000000 dataiku-api-client-9.0.1/dataikuapi/dss/dataiku_app.py
+-rw-r--r--   0 clement    (502) staff       (20)     1998 2021-02-21 14:38:22.000000 dataiku-api-client-9.0.1/dataikuapi/dss/job.py
+-rw-r--r--   0 clement    (502) staff       (20)     4966 2021-10-13 08:14:51.000000 dataiku-api-client-9.0.1/dataikuapi/dss/apiservice.py
+-rw-r--r--   0 clement    (502) staff       (20)        0 2015-07-31 12:07:25.000000 dataiku-api-client-9.0.1/dataikuapi/dss/__init__.py
+-rw-r--r--   0 clement    (502) staff       (20)    26527 2021-02-21 14:38:22.000000 dataiku-api-client-9.0.1/dataikuapi/dss/flow.py
+-rw-r--r--   0 clement    (502) staff       (20)     1553 2021-04-19 10:36:45.000000 dataiku-api-client-9.0.1/dataikuapi/dss/export.py
+-rw-r--r--   0 clement    (502) staff       (20)   157847 2021-12-17 09:38:00.000000 dataiku-api-client-9.0.1/dataikuapi/dss/ml.py
+-rw-r--r--   0 clement    (502) staff       (20)     1180 2018-04-30 06:28:17.000000 dataiku-api-client-9.0.1/dataikuapi/dss/meaning.py
+-rw-r--r--   0 clement    (502) staff       (20)    35668 2021-10-13 08:14:51.000000 dataiku-api-client-9.0.1/dataikuapi/dss/dataset.py
+-rw-r--r--   0 clement    (502) staff       (20)     8369 2021-02-21 14:38:22.000000 dataiku-api-client-9.0.1/dataikuapi/dss/managedfolder.py
+-rw-r--r--   0 clement    (502) staff       (20)    47555 2021-12-09 21:59:29.000000 dataiku-api-client-9.0.1/dataikuapi/dss/admin.py
+-rw-r--r--   0 clement    (502) staff       (20)     1319 2021-02-21 14:38:22.000000 dataiku-api-client-9.0.1/dataikuapi/dss/continuousactivity.py
+-rw-r--r--   0 clement    (502) staff       (20)     8271 2021-02-21 14:38:22.000000 dataiku-api-client-9.0.1/dataikuapi/dss/utils.py
+-rw-r--r--   0 clement    (502) staff       (20)    10805 2021-12-17 09:38:00.000000 dataiku-api-client-9.0.1/dataikuapi/dss/modelevaluationstore.py
+-rw-r--r--   0 clement    (502) staff       (20)    27731 2021-10-13 08:14:51.000000 dataiku-api-client-9.0.1/dataikuapi/dss/scenario.py
+-rw-r--r--   0 clement    (502) staff       (20)     4976 2021-12-17 09:38:00.000000 dataiku-api-client-9.0.1/dataikuapi/dss/app.py
+-rw-r--r--   0 clement    (502) staff       (20)     9916 2021-02-21 14:38:22.000000 dataiku-api-client-9.0.1/dataikuapi/dss/plugin.py
+-rw-r--r--   0 clement    (502) staff       (20)     3054 2021-10-13 08:14:51.000000 dataiku-api-client-9.0.1/dataikuapi/dss/future.py
+-rw-r--r--   0 clement    (502) staff       (20)     8724 2020-07-03 06:32:51.000000 dataiku-api-client-9.0.1/dataikuapi/dss/statistics.py
+-rw-r--r--   0 clement    (502) staff       (20)     6982 2020-07-03 06:32:51.000000 dataiku-api-client-9.0.1/dataikuapi/dss/discussion.py
+-rw-r--r--   0 clement    (502) staff       (20)    14474 2021-02-21 14:38:22.000000 dataiku-api-client-9.0.1/dataikuapi/dss/streaming_endpoint.py
+-rw-r--r--   0 clement    (502) staff       (20)    51101 2021-12-17 09:38:00.000000 dataiku-api-client-9.0.1/dataikuapi/dss/recipe.py
+-rw-r--r--   0 clement    (502) staff       (20)     2665 2021-10-13 08:14:51.000000 dataiku-api-client-9.0.1/dataikuapi/dss/notebook.py
+-rw-r--r--   0 clement    (502) staff       (20)     3063 2021-02-21 14:38:22.000000 dataiku-api-client-9.0.1/dataikuapi/dss/sqlquery.py
+-rw-r--r--   0 clement    (502) staff       (20)    15427 2021-02-21 14:38:22.000000 dataiku-api-client-9.0.1/dataikuapi/dss/wiki.py
+-rw-r--r--   0 clement    (502) staff       (20)     9451 2021-02-21 14:38:22.000000 dataiku-api-client-9.0.1/dataikuapi/dss/projectfolder.py
+-rw-r--r--   0 clement    (502) staff       (20)     6326 2021-10-13 08:14:51.000000 dataiku-api-client-9.0.1/dataikuapi/dss/jupyternotebook.py
+-rw-r--r--   0 clement    (502) staff       (20)     3887 2021-02-21 14:38:22.000000 dataiku-api-client-9.0.1/dataikuapi/dss/macro.py
+-rw-r--r--   0 clement    (502) staff       (20)    78507 2021-12-17 09:38:00.000000 dataiku-api-client-9.0.1/dataikuapi/dss/project.py
+-rw-r--r--   0 clement    (502) staff       (20)     2749 2021-12-17 09:38:00.000000 dataiku-api-client-9.0.1/dataikuapi/utils.py
+drwxr-xr-x   0 clement    (502) staff       (20)        0 2021-12-17 09:43:48.000000 dataiku-api-client-9.0.1/dataikuapi/apinode_admin/
+-rw-r--r--   0 clement    (502) staff       (20)      715 2015-10-22 07:29:24.000000 dataiku-api-client-9.0.1/dataikuapi/apinode_admin/auth.py
+-rw-r--r--   0 clement    (502) staff       (20)     2173 2016-08-23 07:06:36.000000 dataiku-api-client-9.0.1/dataikuapi/apinode_admin/service.py
+-rw-r--r--   0 clement    (502) staff       (20)        0 2015-10-13 08:51:03.000000 dataiku-api-client-9.0.1/dataikuapi/apinode_admin/__init__.py
+-rw-r--r--   0 clement    (502) staff       (20)     1228 2018-01-10 09:59:16.000000 dataiku-api-client-9.0.1/dataikuapi/apinode_admin_client.py
+-rw-r--r--   0 clement    (502) staff       (20)       58 2017-01-03 07:27:57.000000 dataiku-api-client-9.0.1/MANIFEST.in
+-rw-r--r--   0 clement    (502) staff       (20)      143 2020-07-03 06:32:51.000000 dataiku-api-client-9.0.1/README
+drwxr-xr-x   0 clement    (502) staff       (20)        0 2021-12-17 09:43:48.000000 dataiku-api-client-9.0.1/dataiku_api_client.egg-info/
+-rw-r--r--   0 clement    (502) staff       (20)     2399 2021-12-17 09:43:48.000000 dataiku-api-client-9.0.1/dataiku_api_client.egg-info/PKG-INFO
+-rw-r--r--   0 clement    (502) staff       (20)     1483 2021-12-17 09:43:48.000000 dataiku-api-client-9.0.1/dataiku_api_client.egg-info/SOURCES.txt
+-rw-r--r--   0 clement    (502) staff       (20)       27 2021-12-17 09:43:48.000000 dataiku-api-client-9.0.1/dataiku_api_client.egg-info/requires.txt
+-rw-r--r--   0 clement    (502) staff       (20)       11 2021-12-17 09:43:48.000000 dataiku-api-client-9.0.1/dataiku_api_client.egg-info/top_level.txt
+-rw-r--r--   0 clement    (502) staff       (20)        1 2021-12-17 09:43:48.000000 dataiku-api-client-9.0.1/dataiku_api_client.egg-info/dependency_links.txt
+-rw-r--r--   0 clement    (502) staff       (20)     1117 2021-12-17 09:43:34.000000 dataiku-api-client-9.0.1/setup.py
+-rw-r--r--   0 clement    (502) staff       (20)       38 2021-12-17 09:43:48.000000 dataiku-api-client-9.0.1/setup.cfg
+-rw-r--r--   0 clement    (502) staff       (20)      993 2021-12-17 09:38:28.000000 dataiku-api-client-9.0.1/HISTORY.txt
+-rw-r--r--   0 clement    (502) staff       (20)      557 2021-10-13 08:14:51.000000 dataiku-api-client-9.0.1/LICENSE.txt
```

### Comparing `dataiku-api-client-9.0.0/PKG-INFO` & `dataiku-api-client-9.0.1/PKG-INFO`

 * *Files 6% similar despite different names*

```diff
@@ -1,25 +1,29 @@
 Metadata-Version: 1.1
 Name: dataiku-api-client
-Version: 9.0.0
+Version: 9.0.1
 Summary: Python API client for Dataiku APIs
 Home-page: https://www.dataiku.com
 Author: Dataiku
 Author-email: support@dataiku.com
 License: Apache Software License
-Download-URL: https://github.com/dataiku/dataiku-api-client-python/tarball/9.0.0
-Description-Content-Type: UNKNOWN
+Download-URL: https://github.com/dataiku/dataiku-api-client-python/tarball/9.0.1
 Description: API client for Dataiku Data Science Studio
         
         For more information, see:
         https://doc.dataiku.com/dss/latest/python-api/rest-api-client/index.html
         
         Changelog
         ==========
         
+        9.0.1 (2021-12-17)
+        ------------------
+        
+        * Relax version constraint on requests
+        
         9.0.0 (2021-05-07)
         ------------------
         
         * Initial release for DSS 9.0
         
         8.0.0 (2020-08-14)
         -------------------
```

### Comparing `dataiku-api-client-9.0.0/dataikuapi/base_client.py` & `dataiku-api-client-9.0.1/dataikuapi/base_client.py`

 * *Files identical despite different names*

### Comparing `dataiku-api-client-9.0.0/dataikuapi/dssclient.py` & `dataiku-api-client-9.0.1/dataikuapi/dssclient.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,27 +1,27 @@
 import json
 
 from requests import Session
 from requests import exceptions
 from requests.auth import HTTPBasicAuth
 
-from dataikuapi.dss.notebook import DSSNotebook
+from .dss.notebook import DSSNotebook
 from .dss.future import DSSFuture
 from .dss.projectfolder import DSSProjectFolder
 from .dss.project import DSSProject
 from .dss.app import DSSApp
 from .dss.plugin import DSSPlugin
-from .dss.admin import DSSUser, DSSOwnUser, DSSGroup, DSSConnection, DSSGeneralSettings, DSSCodeEnv, DSSGlobalApiKey, DSSCluster
+from .dss.admin import DSSUser, DSSOwnUser, DSSGroup, DSSConnection, DSSGeneralSettings, DSSCodeEnv, DSSGlobalApiKey, DSSCluster, DSSGlobalUsageSummary
 from .dss.meaning import DSSMeaning
 from .dss.sqlquery import DSSSQLQuery
 from .dss.discussion import DSSObjectDiscussions
 from .dss.apideployer import DSSAPIDeployer
 from .dss.projectdeployer import DSSProjectDeployer
 import os.path as osp
-from .utils import DataikuException
+from .utils import DataikuException, dku_basestring_type
 
 class DSSClient(object):
     """Entry point for the DSS API client"""
 
     def __init__(self, host, api_key=None, internal_ticket = None, extra_headers = None):
         """
         Instantiate a new DSS API client on the given host with the given API key.
@@ -110,24 +110,24 @@
     ########################################################
     # Project folders
     ########################################################
     def get_root_project_folder(self):
         """
         Get a handle to interact with the root project folder.
 
-        :returns: A :class:`dataikuapi.dss.projectfolder.DSSProjectFolder`to interact with this project folder
+        :returns: A :class:`dataikuapi.dss.projectfolder.DSSProjectFolder` to interact with this project folder
         """
         return self.get_project_folder("ROOT")
 
     def get_project_folder(self, project_folder_id):
         """
         Get a handle to interact with a project folder.
 
         :param str project_folder_id: the project folder ID of the desired project folder
-        :returns: A :class:`dataikuapi.dss.projectfolder.DSSProjectFolder`to interact with this project folder
+        :returns: A :class:`dataikuapi.dss.projectfolder.DSSProjectFolder` to interact with this project folder
         """
         data = self._perform_json("GET", "/project-folders/%s" % project_folder_id)
         return DSSProjectFolder(self, data)
 
     ########################################################
     # Projects
     ########################################################
@@ -175,15 +175,15 @@
         :param str project_key: the identifier to use for the project. Must be globally unique
         :param str name: the display name for the project.
         :param str owner: the login of the owner of the project.
         :param str description: a description for the project.
         :param dict settings: Initial settings for the project (can be modified later). The exact possible settings are not documented.
         :param str project_folder_id: the project folder ID in which the project will be created (root project folder if not specified)
         
-        :returns: A class:`dataikuapi.dss.project.DSSProject` project handle to interact with this project
+        :returns: A :class:`dataikuapi.dss.project.DSSProject` project handle to interact with this project
         """
         params = {}
         if project_folder_id is not None:
             params["projectFolderId"] = project_folder_id
         resp = self._perform_text(
                "POST", "/projects/", body={
                    "projectKey" : project_key,
@@ -482,30 +482,36 @@
                })
         return DSSConnection(self, name)
 
     ########################################################
     # Code envs
     ########################################################
 
-    def list_code_envs(self):
+    def list_code_envs(self, as_objects=False):
         """
         List all code envs setup on the DSS instance
 
         Note: this call requires an API key with admin rights
         
+        :param boolean as_objects: if True, each returned item will be a :class:`dataikuapi.dss.future.DSSCodeEnv`
         :returns: a list of code envs. Each code env is a dict containing at least "name", "type" and "language"
         """
-        return self._perform_json(
+        list = self._perform_json(
             "GET", "/admin/code-envs/")
+        if as_objects:
+            return [DSSCodeEnv(self, e.get("envLang"), e.get("envName")) for e in list]
+        else:
+            return list
 
     def get_code_env(self, env_lang, env_name):
         """
         Get a handle to interact with a specific code env
         
-        :param str name: the name of the desired code env
+        :param env_lang: the language (PYTHON or R) of the new code env
+        :param env_name: the name of the new code env
         :returns: A :class:`dataikuapi.dss.admin.DSSCodeEnv` code env  handle
         """
         return DSSCodeEnv(self, env_lang, env_name)
 
     def create_code_env(self, env_lang, env_name, deployment_mode, params=None):
         """
         Create a code env, and return a handle to interact with it
@@ -524,14 +530,23 @@
                "POST", "/admin/code-envs/%s/%s" % (env_lang, env_name), body=params)
         if resp is None:
             raise Exception('Env creation returned no data')
         if resp.get('messages', {}).get('error', False):
             raise Exception('Env creation failed : %s' % (json.dumps(resp.get('messages', {}).get('messages', {}))))
         return DSSCodeEnv(self, env_lang, env_name)
 
+    def list_code_env_usages(self):
+        """
+        List all usages of a code env in the instance
+
+        :return: a list of objects where the code env is used
+        """
+        return self._perform_json("GET", "/admin/code-envs/usages")
+
+
     ########################################################
     # Clusters
     ########################################################
 
     def list_clusters(self):
         """
         List all clusters setup on the DSS instance
@@ -675,15 +690,15 @@
             mode to use for value matching. One of 'EXACT', 'LOWERCASE', or 'NORMALIZED' (not available
             for 'PATTERN' type). Defaults to 'EXACT'.
         :param detectable (optional): whether DSS should consider assigning the meaning to columns set to 'Auto-detect'. Defaults to False.
 
         :returns: A :class:`dataikuapi.dss.meaning.DSSMeaning` meaning handle
         """
         def make_entry(v):
-            if isinstance(v, str) or isinstance(v, unicode):
+            if isinstance(v, dku_basestring_type):
                 return {'value':v}
             else:
                 return v
         def make_mapping(v):
             return {'from':v.get('from', None), 'to':make_entry(v.get('to', None))}
         entries = None
         if values is not None:
@@ -739,14 +754,27 @@
         if custom_params is None:
             custom_params = {}
         return self._perform_empty("POST",
             "/admin/audit/custom/%s" % custom_type,
             body = custom_params)
 
     ########################################################
+    # Monitoring
+    ########################################################
+
+    def get_global_usage_summary(self, with_per_project=False):
+        """
+        Gets a summary of the global usage of this DSS instance (number of projects, datasets, ...)
+        :returns: a summary object
+        """
+        data = self._perform_json(
+            "GET", "/admin/monitoring/global-usage-summary", params={'withPerProject':with_per_project})
+        return DSSGlobalUsageSummary(data)
+
+   ########################################################
     # Variables
     ########################################################
 
     def get_variables(self):
         """
         Get the DSS instance's variables, as a Python dictionary
```

### Comparing `dataiku-api-client-9.0.0/dataikuapi/apinode_client.py` & `dataiku-api-client-9.0.1/dataikuapi/apinode_client.py`

 * *Files identical despite different names*

### Comparing `dataiku-api-client-9.0.0/dataikuapi/__init__.py` & `dataiku-api-client-9.0.1/dataikuapi/__init__.py`

 * *Files identical despite different names*

### Comparing `dataiku-api-client-9.0.0/dataikuapi/dss/savedmodel.py` & `dataiku-api-client-9.0.1/dataikuapi/dss/savedmodel.py`

 * *Files identical despite different names*

### Comparing `dataiku-api-client-9.0.0/dataikuapi/dss/metrics.py` & `dataiku-api-client-9.0.1/dataikuapi/dss/metrics.py`

 * *Files identical despite different names*

### Comparing `dataiku-api-client-9.0.0/dataikuapi/dss/projectdeployer.py` & `dataiku-api-client-9.0.1/dataikuapi/dss/projectdeployer.py`

 * *Files identical despite different names*

### Comparing `dataiku-api-client-9.0.0/dataikuapi/dss/apideployer.py` & `dataiku-api-client-9.0.1/dataikuapi/dss/apideployer.py`

 * *Files 4% similar despite different names*

```diff
@@ -330,23 +330,37 @@
                    to wait for completion (or failure)
         """
         future_response = self.client._perform_json(
             "POST", "/api-deployer/deployments/%s/actions/update" % (self.deployment_id))
 
         return DSSFuture(self.client, future_response.get('jobId', None), future_response)
 
-    def delete(self):
+    def delete(self, disable_first=False):
         """
-        Deletes this deployment
+        Deletes this deployment. The disable_first flag automatically disables the deployment
+        before its deletion.
+
+        :param boolean disable_first: If True, automatically disables this deployment before deleting it.
+        If False, will raise an Exception if this deployment is enabled.
 
-        You may only delete a deployment if it is disabled and has been updated after disabling it.
         """
-        return self.client._perform_empty(
-            "DELETE", "/api-deployer/deployments/%s" % (self.deployment_id))
 
+        # Check if the deployment is disabled
+        is_enabled = self.get_status().light_status["deploymentBasicInfo"].get("enabled")
+        if is_enabled and not disable_first:
+            raise Exception("Deployment {} deletion failed: deployment must be disabled first.".format(self.deployment_id))
+        if is_enabled:
+            settings = self.get_settings()
+            settings.set_enabled(enabled=False)
+            settings.save()
+        self.client._perform_empty(
+                "DELETE", "/api-deployer/deployments/%s" % (self.deployment_id))
+
+                
+            
 
 class DSSAPIDeployerDeploymentSettings(object):
     """
     The settings of an API Deployer deployment. 
 
     Do not create this directly, use :meth:`~dataikuapi.dss.apideployer.DSSAPIDeployerDeployment.get_settings`
     """
@@ -514,15 +528,15 @@
 
     def delete(self):
         """
         Deletes this service
 
         You may only delete a service if it has no deployments on it anymore.
         """
-        return self.client._perform_empty(
+        self.client._perform_empty(
             "DELETE", "/api-deployer/services/%s" % (self.service_id))
 
 
 class DSSAPIDeployerServiceSettings(object):
     """
     The settings of an API Deployer Service.
```

### Comparing `dataiku-api-client-9.0.0/dataikuapi/dss/analysis.py` & `dataiku-api-client-9.0.1/dataikuapi/dss/analysis.py`

 * *Files identical despite different names*

### Comparing `dataiku-api-client-9.0.0/dataikuapi/dss/dataiku_app.py` & `dataiku-api-client-9.0.1/dataikuapi/dss/dataiku_app.py`

 * *Files identical despite different names*

### Comparing `dataiku-api-client-9.0.0/dataikuapi/dss/job.py` & `dataiku-api-client-9.0.1/dataikuapi/dss/job.py`

 * *Files identical despite different names*

### Comparing `dataiku-api-client-9.0.0/dataikuapi/dss/apiservice.py` & `dataiku-api-client-9.0.1/dataikuapi/dss/apiservice.py`

 * *Files identical despite different names*

### Comparing `dataiku-api-client-9.0.0/dataikuapi/dss/flow.py` & `dataiku-api-client-9.0.1/dataikuapi/dss/flow.py`

 * *Files identical despite different names*

### Comparing `dataiku-api-client-9.0.0/dataikuapi/dss/export.py` & `dataiku-api-client-9.0.1/dataikuapi/dss/export.py`

 * *Files identical despite different names*

### Comparing `dataiku-api-client-9.0.0/dataikuapi/dss/ml.py` & `dataiku-api-client-9.0.1/dataikuapi/dss/ml.py`

 * *Files 2% similar despite different names*

```diff
@@ -789,15 +789,15 @@
     def set_explicit_values(self, values):
         """
         Sets both:
         - the explicit values to search over for the current numerical hyperparameter
         - the definition mode of the current numerical hyperparameter to "EXPLICIT"
 
         :param values: the explicit list of numerical values considered for this hyperparameter in the search
-        :type values: list of float | int
+        :type values: list of float | list of int
         """
         self.values = values
         self.definition_mode = "EXPLICIT"
 
     @property
     def values(self):
         """
@@ -806,15 +806,15 @@
         """
         return self._algo_settings[self.name]["values"]
 
     @values.setter
     def values(self, values):
         """
         :param values: the explicit list of numerical values considered for this hyperparameter in the search
-        :type values: list of float | int
+        :type values: list of float | list of int
         """
         error_message = "Invalid values input type for hyperparameter " \
                         "\"{}\": ".format(self.name) + \
                         " expecting a non-empty list of numbers"
         assert values is not None and isinstance(values, list) and len(values) > 0, error_message
         for val in values:
             assert isinstance(val, int) or isinstance(val, float), error_message
@@ -857,92 +857,116 @@
             if min is not None:
                 self._algo_settings[self.name]["range"]["min"] = min
             if max is not None:
                 self._algo_settings[self.name]["range"]["max"] = max
             if nb_values is not None:
                 self._algo_settings[self.name]["range"]["nbValues"] = nb_values
 
+    class RangeSettings(object):
+        """
+        [Internal] Range of a numerical hyperparameter (points to the algorithm settings)
+        Should not be used directly by end users of the API
+        """
+
+        def __init__(self, numerical_hyperparameter_settings):
+            self._numerical_hyperparameter_settings = numerical_hyperparameter_settings
+            self._range_dict = self._numerical_hyperparameter_settings._algo_settings[numerical_hyperparameter_settings.name]["range"]
+
+        def __repr__(self):
+            return "RangeSettings(min={}, max={}, nb_values={})".format(self.min, self.max, self.nb_values)
+
+        @property
+        def min(self):
+            """
+            :return: the lower bound of the range for this hyperparameter
+            :rtype: float | int
+            """
+            return self._range_dict["min"]
+
+        @min.setter
+        def min(self, value):
+            """
+            :param value: the lower bound of the range for this hyperparameter
+            :type value: float | int
+            """
+            self._numerical_hyperparameter_settings._set_range(min=value)
+
+        @property
+        def max(self):
+            """
+            :return: the upper bound of the range for this hyperparameter
+            :rtype: float | int
+            """
+            return self._range_dict["max"]
+
+        @max.setter
+        def max(self, value):
+            """
+            :param value: the upper bound of the range for this hyperparameter
+            :type value: float | int
+            """
+            self._numerical_hyperparameter_settings._set_range(max=value)
+
+        @property
+        def nb_values(self):
+            """
+            :return: for grid-search ("GRID" strategy) only, the number of values between min and max to consider
+            :rtype: int
+            """
+            return self._range_dict["nbValues"]
+
+        @nb_values.setter
+        def nb_values(self, value):
+            """
+            :param value: for grid-search ("GRID" strategy) only, the number of values between min and max to consider
+            :type value: int
+            """
+            self._numerical_hyperparameter_settings._set_range(nb_values=value)
+
     def set_range(self, min=None, max=None, nb_values=None):
         """
         Sets both:
-        - the Range parameters to search over for the current numerical hyperparameter
+        - the range parameters to search over for the current numerical hyperparameter
         - the definition mode of the current numerical hyperparameter to "RANGE"
 
-        :param min: the lower bound of the Range for this hyperparameter
+        :param min: the lower bound of the range for this hyperparameter
         :type min: float | int
-        :param max: the upper bound of the Range for this hyperparameter
+        :param max: the upper bound of the range for this hyperparameter
         :type max: float | int
         :param nb_values: for grid-search ("GRID" strategy) only, the number of values between min and max to consider
         :type nb_values: int
         """
         self._set_range(min=min, max=max, nb_values=nb_values)
         self.definition_mode = "RANGE"
 
     @property
     def range(self):
-        return Range(self)
+        return NumericalHyperparameterSettings.RangeSettings(self)
 
 
 class Range(object):
+    """
+    Range of a numerical hyperparameter (min, max, nb_values)
+    Use this class to define explicitly the parameters of the range of a numerical hyperparameter
+    """
+
+    def _check_input(self, value):
+        assert isinstance(value, (int, float)), "Invalid input type for Range: {}".format(type(value))
 
-    def __init__(self, numerical_hyperparameter_settings):
-        self._numerical_hyperparameter_settings = numerical_hyperparameter_settings
-        self._range_dict = self._numerical_hyperparameter_settings._algo_settings[numerical_hyperparameter_settings.name]["range"]
+    def __init__(self, min, max, nb_values=None):
+        self._check_input(min)
+        self._check_input(max)
+        assert min <= max, "Invalid Range: min must be lower than max"
+        self.min = min
+        self.max = max
+        self.nb_values = nb_values
 
     def __repr__(self):
         return "Range(min={}, max={}, nb_values={})".format(self.min, self.max, self.nb_values)
 
-    @property
-    def min(self):
-        """
-        :return: the lower bound of the Range for this hyperparameter
-        :rtype: float | int
-        """
-        return self._range_dict["min"]
-
-    @min.setter
-    def min(self, value):
-        """
-        :param value: the lower bound of the Range this hyperparameter
-        :type value: float | int
-        """
-        self._numerical_hyperparameter_settings._set_range(min=value)
-
-    @property
-    def max(self):
-        """
-        :return: the upper bound of the Range this hyperparameter
-        :rtype: float | int
-        """
-        return self._range_dict["max"]
-
-    @max.setter
-    def max(self, value):
-        """
-        :param value: the upper bound of the Range for this hyperparameter
-        :type value: float | int
-        """
-        self._numerical_hyperparameter_settings._set_range(max=value)
-
-    @property
-    def nb_values(self):
-        """
-        :return: for grid-search ("GRID" strategy) only, the number of values between min and max to consider
-        :rtype: int
-        """
-        return self._range_dict["nbValues"]
-
-    @nb_values.setter
-    def nb_values(self, value):
-        """
-        :param value: for grid-search ("GRID" strategy) only, the number of values between min and max to consider
-        :type value: int
-        """
-        self._numerical_hyperparameter_settings._set_range(nb_values=value)
-
 
 class CategoricalHyperparameterSettings(HyperparameterSettings):
 
     def __repr__(self):
         return self.__class__.__name__ + "(hyperparameter=\"{}\", settings={})".format(self.name, json.dumps(self._algo_settings[self.name]))
 
     __str__ = __repr__
@@ -1093,15 +1117,28 @@
                 # syntactic sugars
                 target = self._hyperparameters_registry[json_key]
                 if isinstance(target, (SingleValueHyperparameterSettings, SingleCategoryHyperparameterSettings)):
                     target.set_value(value)
                 elif isinstance(target, CategoricalHyperparameterSettings):
                     target.set_values(value)
                 elif isinstance(target, NumericalHyperparameterSettings):
-                    raise Exception("Invalid assignment of a NumericalHyperparameterSettings object")
+                    if isinstance(value, list):
+                        # algo.hyperparam = [x, y, z]
+                        target.set_explicit_values(values=value)
+                    elif isinstance(value, Range):
+                        # algo.hyperparam = Range(min=x, max=y, nb_values=z)
+                        target.set_range(min=value.min, max=value.max, nb_values=value.nb_values)
+                    elif isinstance(value, NumericalHyperparameterSettings):
+                        # algo.hyperparam = other_algo.other_hyperparam
+                        target.set_range(min=value.range.min, max=value.range.max, nb_values=value.range.nb_values)
+                        target.set_explicit_values(values=list(value.values))
+                        target.definition_mode = value.definition_mode
+                    else:
+                        raise TypeError(("Invalid type for NumericalHyperparameterSettings {}\n" +
+                                        "Expecting either list, Range or NumericalHyperparameterSettings").format(attr_name))
                 else:
                     # simple parameter
                     assert isinstance(value, type(target)), "Invalid type {} for parameter {}: expected {}".format(type(value), attr_name, type(target))
                     super(PredictionAlgorithmSettings, self).__setattr__(attr_name, value)  # update attribute value
                     self[json_key] = value  # update underlying dict value for key json_key
                     self._hyperparameters_registry[json_key] = value
             else:
@@ -1798,14 +1835,92 @@
 
         :returns: list of diagnostics
         :rtype: list of type `dataikuapi.dss.ml.DSSMLDiagnostic`
         """
         diagnostics = self.details.get("trainDiagnostics", {})
         return [DSSMLDiagnostic(d) for d in diagnostics.get("diagnostics", [])]
 
+    def generate_documentation(self, folder_id=None, path=None):
+        """
+        Start the model document generation from a template docx file in a managed folder,
+        or from the default template if no folder id and path are specified.
+
+        :param folder_id: (optional) the id of the managed folder
+        :param path: (optional) the path to the file from the root of the folder
+        :return: A :class:`~dataikuapi.dss.future.DSSFuture` representing the model document generation process
+        """
+        if bool(folder_id) != bool(path):
+            raise ValueError("Both folder id and path arguments are required to use a template from folder. Use without argument to generate the model documentation using the default template")
+
+        template_mode_url = "default-template" if folder_id is None and path is None else "template-in-folder"
+
+        if self.mltask is not None:
+            f = self.mltask.client._perform_json(
+                "POST", "/projects/%s/models/lab/%s/%s/models/%s/generate-documentation-from-%s" %
+                        (self.mltask.project_key, self.mltask.analysis_id, self.mltask.mltask_id, self.mltask_model_id, template_mode_url),
+                params={"folderId": folder_id, "path": path})
+            return DSSFuture(self.mltask.client, f["jobId"])
+        else:
+            f = self.saved_model.client._perform_json(
+                "POST", "/projects/%s/savedmodels/%s/versions/%s/generate-documentation-from-%s" %
+                        (self.saved_model.project_key, self.saved_model.sm_id, self.saved_model_version, template_mode_url),
+                params={"folderId": folder_id, "path": path})
+            return DSSFuture(self.saved_model.client, job_id=f["jobId"])
+
+    def generate_documentation_from_custom_template(self, fp):
+        """
+        Start the model document generation from a docx template (as a file object).
+
+        :param object fp: A file-like object pointing to a template docx file
+        :return: A :class:`~dataikuapi.dss.future.DSSFuture` representing the model document generation process
+        """
+        files = {'file': fp}
+        if self.mltask is not None:
+            f = self.mltask.client._perform_json(
+                "POST", "/projects/%s/models/lab/%s/%s/models/%s/generate-documentation-from-custom-template" %
+                        (self.mltask.project_key, self.mltask.analysis_id, self.mltask.mltask_id, self.mltask_model_id),
+                files=files)
+            return DSSFuture(self.mltask.client, f["jobId"])
+        else:
+            f = self.saved_model.client._perform_json(
+                "POST", "/projects/%s/savedmodels/%s/versions/%s/generate-documentation-from-custom-template" %
+                        (self.saved_model.project_key, self.saved_model.sm_id, self.saved_model_version),
+                files=files)
+            return DSSFuture(self.saved_model.client, job_id=f["jobId"])
+
+    def download_documentation_stream(self, export_id):
+        """
+        Download a model documentation, as a binary stream.
+
+        Warning: this stream will monopolize the DSSClient until closed.
+
+        :param export_id: the id of the generated model documentation returned as the result of the future
+        :return: A :class:`~dataikuapi.dss.future.DSSFuture` representing the model document generation process
+        """
+        if self.mltask is not None:
+            return self.mltask.client._perform_raw(
+                "GET", "/projects/%s/models/lab/documentations/%s" % (self.mltask.project_key, export_id))
+        else:
+            return self.saved_model.client._perform_raw(
+                "GET", "/projects/%s/savedmodels/documentations/%s" % (self.saved_model.project_key, export_id))
+
+    def download_documentation_to_file(self, export_id, path):
+        """
+        Download a model documentation into the given output file.
+
+        :param export_id: the id of the generated model documentation returned as the result of the future
+        :param path: the path where to download the model documentation
+        :return: None
+        """
+        stream = self.download_documentation_stream(export_id)
+        with open(path, 'wb') as f:
+            for chunk in stream.iter_content(chunk_size=10000):
+                if chunk:
+                    f.write(chunk)
+                    f.flush()
 
 class DSSMLDiagnostic(object):
     """
     Object that represents a computed Diagnostic on a trained model
 
     Do not create this object directly, use :meth:`DSSTrainedModelDetails.get_diagnostics()` instead
     """
@@ -2508,14 +2623,15 @@
                 "GET", "/projects/%s/models/lab/%s/%s/models/%s/scoring-pmml" %
                 (self.mltask.project_key, self.mltask.analysis_id, self.mltask.mltask_id, self.mltask_model_id))
         else:
             return self.saved_model.client._perform_raw(
                 "GET", "/projects/%s/savedmodels/%s/versions/%s/scoring-pmml" %
                 (self.saved_model.project_key, self.saved_model.sm_id, self.saved_model_version))
 
+
     ## Post-train computations
 
     def compute_subpopulation_analyses(self, split_by, wait=True, sample_size=1000, random_state=1337, n_jobs=1, debug_mode=False):
         """
         Launch computation of Subpopulation analyses for this trained model.
 
         :param list|str split_by: column(s) on which subpopulation analyses are to be computed (one analysis per column)
```

### Comparing `dataiku-api-client-9.0.0/dataikuapi/dss/meaning.py` & `dataiku-api-client-9.0.1/dataikuapi/dss/meaning.py`

 * *Files identical despite different names*

### Comparing `dataiku-api-client-9.0.0/dataikuapi/dss/dataset.py` & `dataiku-api-client-9.0.1/dataikuapi/dss/dataset.py`

 * *Files 1% similar despite different names*

```diff
@@ -604,14 +604,19 @@
                 "/projects/%s/datasets/%s/actions/testAndDetectSettings/fsLike"% (self.project_key, self.dataset_name),
                 body = {"detectPossibleFormats" : True, "inferStorageTypes" : infer_storage_types })
 
             return DSSFuture(self.client, future_resp.get('jobId', None), future_resp)
         elif settings.type in self.__class__._SQL_TYPES:
             return self.client._perform_json("POST",
                 "/projects/%s/datasets/%s/actions/testAndDetectSettings/externalSQL"% (self.project_key, self.dataset_name))
+        
+        elif settings.type == "ElasticSearch":
+            return self.client._perform_json("POST",
+                "/projects/%s/datasets/%s/actions/testAndDetectSettings/elasticsearch"% (self.project_key, self.dataset_name))
+
         else:
             raise ValueError("don't know how to test/detect on dataset type:%s" % settings.type)
 
     def autodetect_settings(self, infer_storage_types=False):
         """
         Detects appropriate settings for this dataset using Dataiku detection engine
 
@@ -638,14 +643,23 @@
             result = self.test_and_detect()
 
             if not "schemaDetection" in result:
                 raise DataikuException("Format detection failed, complete response is " + json.dumps(result))
 
             settings.get_raw()["schema"] = result["schemaDetection"]["newSchema"]
             return settings
+        
+        elif settings.type == "ElasticSearch":
+            result = self.test_and_detect()
+
+            if not "schemaDetection" in result:
+                raise DataikuException("Format detection failed, complete response is " + json.dumps(result))
+
+            settings.get_raw()["schema"] = result["schemaDetection"]["newSchema"]
+            return settings
 
         else:
             raise ValueError("don't know how to test/detect on dataset type:%s" % settings.type)
 
     def get_as_core_dataset(self):
         """Returns the :class:`dataiku.Dataset` object corresponding to this dataset"""
         import dataiku
```

### Comparing `dataiku-api-client-9.0.0/dataikuapi/dss/managedfolder.py` & `dataiku-api-client-9.0.1/dataikuapi/dss/managedfolder.py`

 * *Files identical despite different names*

### Comparing `dataiku-api-client-9.0.0/dataikuapi/dss/admin.py` & `dataiku-api-client-9.0.1/dataikuapi/dss/admin.py`

 * *Files 20% similar despite different names*

```diff
@@ -691,30 +691,80 @@
         """
         Set the code env's definition. The definition should come from a call to :meth:`get_definition`
 
         Fields that can be updated in design node:
 
         * env.permissions, env.usableByAll, env.desc.owner
         * env.specCondaEnvironment, env.specPackageList, env.externalCondaEnvName, env.desc.installCorePackages,
-          env.desc.installJupyterSupport, env.desc.yarnPythonBin
+          env.desc.corePackagesSet, env.desc.installJupyterSupport, env.desc.yarnPythonBin, env.desc.yarnRBin
+          env.desc.envSettings, env.desc.allContainerConfs, env.desc.containerConfs, 
+          env.desc.allSparkKubernetesConfs, env.desc.sparkKubernetesConfs
 
         Fields that can be updated in automation node (where {version} is the updated version):
 
-        * env.permissions, env.usableByAll, env.owner
+        * env.permissions, env.usableByAll, env.owner, env.envSettings
         * env.{version}.specCondaEnvironment, env.{version}.specPackageList, env.{version}.externalCondaEnvName, 
-          env.{version}.desc.installCorePackages, env.{version}.desc.installJupyterSupport, env.{version}.desc.yarnPythonBin
+          env.{version}.desc.installCorePackages, env.{version}.corePackagesSet, env.{version}.desc.installJupyterSupport
+          env.{version}.desc.yarnPythonBin, env.{version}.desc.yarnRBin, env.{version}.desc.allContainerConfs, 
+          env.{version}.desc.containerConfs, env.{version}.desc.allSparkKubernetesConfs, 
+          env.{version}.{version}.desc.sparkKubernetesConfs
 
         Note: this call requires an API key with admin rights
         
         :param dict data: a code env definition
         :return: the updated code env definition, as a dict
         """
         return self.client._perform_json(
             "PUT", "/admin/code-envs/%s/%s" % (self.env_lang, self.env_name), body=env)
-    
+
+    def get_version_for_project(self, project_key):
+        """
+        Resolve the code env version for a given project
+
+        Note: version will only be non-empty for versioned code envs actually used by the project
+
+        :returns: the code env reference, with a version field
+        """
+        return self.client._perform_json(
+            "GET", "/admin/code-envs/%s/%s/%s/version" % (self.env_lang, self.env_name, project_key))
+
+
+    def get_settings(self):
+        """
+        Returns the settings of this code env as a :class:`DSSCodeEnvSettings`, or one of its subclasses.
+
+        Known subclasses of :class:`DSSCodeEnvSettings` include :class:`DSSDesignCodeEnvSettings` 
+        and :class:`DSSAutomationCodeEnvSettings`
+
+        You must use :meth:`~DSSCodeEnvSettings.save()` on the returned object to make your changes effective
+        on the code env.
+
+        .. code-block:: python
+
+            # Example: setting the required packagd
+            codeenv = client.get_code_env("PYTHON", "code_env_name")
+            settings = codeenv.get_settings()
+            settings.set_required_packages("dash==2.0.0", "bokeh<2.0")
+            settings.save()
+            # then proceed to update_packages()
+
+        :rtype: :class:`DSSCodeEnvSettings`
+        """
+        data = self.client._perform_json(
+            "GET", "/admin/code-envs/%s/%s" % (self.env_lang, self.env_name))
+
+        # you can't just use deploymentMode to check if it's an automation code
+        # env, because some modes are common to both types of nodes. So we rely 
+        # on a non-null field that only the automation code envs have
+        if data.get("versions", None) is not None:
+            return DSSAutomationCodeEnvSettings(self, data)
+        else:
+            return DSSDesignCodeEnvSettings(self, data)
+
+   
     ########################################################
     # Code env actions
     ########################################################
 
     def set_jupyter_support(self, active):
         """
         Update the code env jupyter support
@@ -743,14 +793,225 @@
             params={"forceRebuildEnv": force_rebuild_env})
         if resp is None:
             raise Exception('Env update returned no data')
         if resp.get('messages', {}).get('error', False):
             raise Exception('Env update failed : %s' % (json.dumps(resp.get('messages', {}).get('messages', {}))))
         return resp
 
+    def update_images(self, env_version=None):
+        """
+        Rebuild the docker image of the code env
+        
+        Note: this call requires an API key with admin rights
+        """
+        resp = self.client._perform_json(
+            "POST", "/admin/code-envs/%s/%s/images" % (self.env_lang, self.env_name),
+            params={"envVersion": env_version})
+        if resp is None:
+            raise Exception('Env image build returned no data')
+        if resp.get('messages', {}).get('error', False):
+            raise Exception('Env image build failed : %s' % (json.dumps(resp.get('messages', {}).get('messages', {}))))
+        return resp
+
+    def list_usages(self, env_version=None):
+        """
+        List usages of the code env in the instance
+
+        :return: a list of objects where the code env is used
+        """
+        return self.client._perform_json(
+            "GET", "/admin/code-envs/%s/%s/usages" % (self.env_lang, self.env_name), params={"envVersion": env_version})
+
+    def list_logs(self, env_version=None):
+        """
+        List logs of the code env in the instance
+
+        :return: a list of log descriptions
+        """
+        return self.client._perform_json(
+            "GET", "/admin/code-envs/%s/%s/logs" % (self.env_lang, self.env_name), params={"envVersion": env_version})
+
+    def get_log(self, log_name):
+        """
+        Get the logs of the code env
+        
+        Args:
+            log_name: name of the log to fetch
+            
+           Returns:
+               the log, as a string
+        """
+        return self.client._perform_text(
+            "GET", "/admin/code-envs/%s/%s/logs/%s" % (self.env_lang, self.env_name, log_name))
+
+
+class DSSCodeEnvSettings(object):
+    """
+    Base settings class for a DSS code env.
+    Do not instantiate this class directly, use :meth:`DSSCodeEnv.get_settings`
+
+    Use :meth:`save` to save your changes
+    """
+
+    def __init__(self, codeenv, settings):
+        self.codeenv = codeenv
+        self.settings = settings
+
+    def get_raw(self):
+        """Get the raw code env settings as a dict"""
+        return self.settings
+
+    @property
+    def env_lang(self):
+        return self.codeenv.env_lang
+
+    @property
+    def env_name(self):
+        return self.codeenv.env_name
+
+    def save(self):
+        self.codeenv.client._perform_json(
+            "PUT", "/admin/code-envs/%s/%s" % (self.env_lang, self.env_name), body=self.settings)
+
+class DSSCodeEnvPackageListBearer(object):
+    def get_required_packages(self, as_list=False):
+        """
+        Return the list of required packages, as a single string
+
+        :param boolean as_list: if True, return the spec as a list of lines; if False, return as a single multiline string
+        """
+        x = self.settings.get("specPackageList", "")
+        return x.split('\n') if as_list else x
+    def set_required_packages(self, *packages):
+        """
+        Set the list of required packages
+        """
+        self.settings["specPackageList"] = '\n'.join(packages)
+
+    def get_required_conda_spec(self, as_list=False):
+        """
+        Return the list of required conda packages, as a single string
+
+        :param boolean as_list: if True, return the spec as a list of lines; if False, return as a single multiline string
+        """
+        x = self.settings.get("specCondaEnvironment", "")
+        return x.split('\n') if as_list else x
+    def set_required_conda_spec(self, *spec):
+        """
+        Set the list of required conda packages
+        """
+        self.settings["specCondaEnvironment"] = '\n'.join(packages)
+
+class DSSCodeEnvContainerConfsBearer(object):
+    def get_built_for_all_container_confs(self):
+        """
+        Return whether the code env creates an image for each container config
+        """
+        return self.settings.get("allContainerConfs", False)
+    def get_built_container_confs(self):
+        """
+        Return the list of container configs for which the code env builds an image (if not all)
+        """
+        return self.settings.get("containerConfs", [])
+    def set_built_container_confs(self, *configs, **kwargs):
+        """
+        Set the list of container configs for which the code env builds an image
+
+        :param boolean all: if True, an image is built for each config
+        :param list configs: list of configuration names to build images for
+        """
+        all = kwargs.get("all", False)
+        self.settings['allContainerConfs'] = all
+        if not all:
+            self.settings['containerConfs'] = configs
+    def built_for_all_spark_kubernetes_confs(self):
+        """
+        Return whether the code env creates an image for each managed Spark over Kubernetes config
+        """
+        return self.settings.get("allSparkKubernetesConfs", False)
+    def get_built_spark_kubernetes_confs(self):
+        """
+        Return the list of managed Spark over Kubernetes configs for which the code env builds an image (if not all)
+        """
+        return self.settings.get("sparkKubernetesConfs", [])
+    def set_built_spark_kubernetes_confs(self, *configs, **kwargs):
+        """
+        Set the list of managed Spark over Kubernetes configs for which the code env builds an image
+
+        :param boolean all: if True, an image is built for each config
+        :param list configs: list of configuration names to build images for
+        """
+        all = kwargs.get("all", False)
+        self.settings['allSparkKubernetesConfs'] = all
+        if not all:
+            self.settings['sparkKubernetesConfs'] = configs
+
+
+class DSSDesignCodeEnvSettings(DSSCodeEnvSettings, DSSCodeEnvPackageListBearer, DSSCodeEnvContainerConfsBearer):
+    """
+    Base settings class for a DSS code env on a design node.
+    Do not instantiate this class directly, use :meth:`DSSCodeEnv.get_settings`
+
+    Use :meth:`save` to save your changes
+    """
+
+    def __init__(self, codeenv, settings):
+        super(DSSDesignCodeEnvSettings, self).__init__(codeenv, settings)
+
+
+class DSSAutomationCodeEnvSettings(DSSCodeEnvSettings, DSSCodeEnvContainerConfsBearer):
+    """
+    Base settings class for a DSS code env on an automation node.
+    Do not instantiate this class directly, use :meth:`DSSCodeEnv.get_settings`
+
+    Use :meth:`save` to save your changes
+    """
+
+    def __init__(self, codeenv, settings):
+        super(DSSAutomationCodeEnvSettings, self).__init__(codeenv, settings)
+
+
+    def get_version(self, version_id=None):
+        """
+        Get a specific code env version (for versioned envs) or the single
+        version
+
+        :param string version_id: for versioned code env, identifier of the desired version 
+
+        :rtype: :class:`DSSAutomationCodeEnvVersionSettings`
+        """
+        deployment_mode = self.settings.get("deploymentMode", None)
+        if deployment_mode in ['AUTOMATION_SINGLE']:
+            return DSSAutomationCodeEnvVersionSettings(self.codeenv, self.settings.get('currentVersion', {}))
+        elif deployment_mode in ['AUTOMATION_VERSIONED']:
+            versions = self.settings.get("versions", [])
+            version_ids = [v.get('versionId') for v in versions]
+            if version_id is None:
+                raise Exception("A version id is required in a versioned code env. Existing ids: %s" % ', '.join(version_ids))
+            for version in versions:
+                if version_id == version.get("versionId"):
+                    return DSSAutomationCodeEnvVersionSettings(self.codeenv, version)
+            raise Exception("Version %s not found in : %s" % (version_id, ', '.join(version_ids)))
+        elif deployment_mode in ['PLUGIN_NON_MANAGED', 'PLUGIN_MANAGED', 'AUTOMATION_NON_MANAGED_PATH', 'EXTERNAL_CONDA_NAMED']:
+            return DSSAutomationCodeEnvVersionSettings(self.codeenv, self.settings.get('noVersion', {}))
+        else:
+            raise Exception("Unexpected deployment mode %s for an automation node code env. Alter the settings directly with get_raw()", deployment_mode)
+
+class DSSAutomationCodeEnvVersionSettings(DSSCodeEnvPackageListBearer):
+    """
+    Base settings class for a DSS code env version on an automation node.
+    Do not instantiate this class directly, use :meth:`DSSAutomationCodeEnvSettings.get_version`
+
+    Use :meth:`save` on the :class:`DSSAutomationCodeEnvSettings` to save your changes
+    """
+
+    def __init__(self, codeenv_settings, version_settings):
+        self.codeenv_settings = codeenv_settings
+        self.settings = version_settings
+
 
 class DSSGlobalApiKey(object):
     """
     A global API key on the DSS instance
     """
     def __init__(self, client, key):
         self.client = client
@@ -942,7 +1203,47 @@
         self.status = status
 
     def get_raw(self):
         """
         Gets the whole status as a raw dictionary.
         """
         return self.status
+
+class DSSGlobalUsageSummary(object):
+    """
+    The summary of the usage of the DSS instance.
+    Do not create this directly, use :meth:`dataikuapi.dss.DSSClient.get_global_usage_summary`
+    """
+    def __init__(self, data):
+        self.data = data
+
+    @property
+    def raw(self):
+        return self.data
+
+    @property
+    def projects_count(self):
+        return self.data["projects"]
+
+    @property
+    def total_datasets_count(self):
+        return self.data["datasets"]["all"]
+
+    @property
+    def total_recipes_count(self):
+        return self.data["recipes"]["all"]
+
+    @property
+    def total_jupyter_notebooks_count(self):
+        return self.data["notebooks"]["nbJupyterNotebooks"]
+
+    @property
+    def total_sql_notebooks_count(self):
+        return self.data["notebooks"]["nbSqlNotebooks"]
+
+    @property
+    def total_scenarios_count(self):
+        return self.data["scenarios"]["all"]
+
+    @property
+    def total_active_with_trigger_scenarios_count(self):
+        return self.data["scenarios"]["activeWithTriggers"]
```

### Comparing `dataiku-api-client-9.0.0/dataikuapi/dss/continuousactivity.py` & `dataiku-api-client-9.0.1/dataikuapi/dss/continuousactivity.py`

 * *Files identical despite different names*

### Comparing `dataiku-api-client-9.0.0/dataikuapi/dss/utils.py` & `dataiku-api-client-9.0.1/dataikuapi/dss/utils.py`

 * *Files identical despite different names*

### Comparing `dataiku-api-client-9.0.0/dataikuapi/dss/modelevaluationstore.py` & `dataiku-api-client-9.0.1/dataikuapi/dss/modelevaluationstore.py`

 * *Files identical despite different names*

### Comparing `dataiku-api-client-9.0.0/dataikuapi/dss/scenario.py` & `dataiku-api-client-9.0.1/dataikuapi/dss/scenario.py`

 * *Files identical despite different names*

### Comparing `dataiku-api-client-9.0.0/dataikuapi/dss/app.py` & `dataiku-api-client-9.0.1/dataikuapi/dss/app.py`

 * *Files identical despite different names*

### Comparing `dataiku-api-client-9.0.0/dataikuapi/dss/plugin.py` & `dataiku-api-client-9.0.1/dataikuapi/dss/plugin.py`

 * *Files identical despite different names*

### Comparing `dataiku-api-client-9.0.0/dataikuapi/dss/future.py` & `dataiku-api-client-9.0.1/dataikuapi/dss/future.py`

 * *Files identical despite different names*

### Comparing `dataiku-api-client-9.0.0/dataikuapi/dss/statistics.py` & `dataiku-api-client-9.0.1/dataikuapi/dss/statistics.py`

 * *Files identical despite different names*

### Comparing `dataiku-api-client-9.0.0/dataikuapi/dss/discussion.py` & `dataiku-api-client-9.0.1/dataikuapi/dss/discussion.py`

 * *Files identical despite different names*

### Comparing `dataiku-api-client-9.0.0/dataikuapi/dss/streaming_endpoint.py` & `dataiku-api-client-9.0.1/dataikuapi/dss/streaming_endpoint.py`

 * *Files identical despite different names*

### Comparing `dataiku-api-client-9.0.0/dataikuapi/dss/recipe.py` & `dataiku-api-client-9.0.1/dataikuapi/dss/recipe.py`

 * *Files 2% similar despite different names*

```diff
@@ -1339,48 +1339,7 @@
 
     def __init__(self, name, project):
         SingleOutputRecipeCreator.__init__(self, 'clustering_scoring', name, project)
 
     def with_input_model(self, model_id):
         """Sets the input model"""
         return self._with_input(model_id, self.project.project_key, "model")
-
-
-class DownloadRecipeCreator(SingleOutputRecipeCreator):
-    """
-    Create a Download recipe
-    """
-    def __init__(self, name, project):
-        SingleOutputRecipeCreator.__init__(self, 'download', name, project)
-
-
-class RequiredSchemaUpdates(object):
-    """
-    Representation of the updates required to the schema of the outputs of a recipe.
-    Do not create this class directly, use :meth:`DSSRecipe.compute_schema_updates`
-    """
-
-    def __init__(self, recipe, data):
-        self.recipe = recipe
-        self.data = data
-        self.drop_and_recreate = True
-        self.synchronize_metastore = True
-
-    def any_action_required(self):
-        return self.data["totalIncompatibilities"] > 0
-
-    def apply(self):
-        results  = []
-        for computable in self.data["computables"]:
-            osu = {
-                "computableType": computable["type"],
-                # dirty
-                "computableId": computable["type"] == "DATASET" and computable["datasetName"] or computable["id"],
-                "newSchema": computable["newSchema"],
-                "dropAndRecreate": self.drop_and_recreate,
-                "synchronizeMetastore" : self.synchronize_metastore
-            }
-
-            results.append(self.recipe.client._perform_json("POST",
-                    "/projects/%s/recipes/%s/actions/updateOutputSchema" % (self.recipe.project_key, self.recipe.recipe_name),
-                    body=osu))
-        return results
```

### Comparing `dataiku-api-client-9.0.0/dataikuapi/dss/notebook.py` & `dataiku-api-client-9.0.1/dataikuapi/dss/notebook.py`

 * *Files identical despite different names*

### Comparing `dataiku-api-client-9.0.0/dataikuapi/dss/sqlquery.py` & `dataiku-api-client-9.0.1/dataikuapi/dss/sqlquery.py`

 * *Files identical despite different names*

### Comparing `dataiku-api-client-9.0.0/dataikuapi/dss/wiki.py` & `dataiku-api-client-9.0.1/dataikuapi/dss/wiki.py`

 * *Files identical despite different names*

### Comparing `dataiku-api-client-9.0.0/dataikuapi/dss/projectfolder.py` & `dataiku-api-client-9.0.1/dataikuapi/dss/projectfolder.py`

 * *Files identical despite different names*

### Comparing `dataiku-api-client-9.0.0/dataikuapi/dss/jupyternotebook.py` & `dataiku-api-client-9.0.1/dataikuapi/dss/jupyternotebook.py`

 * *Files identical despite different names*

### Comparing `dataiku-api-client-9.0.0/dataikuapi/dss/macro.py` & `dataiku-api-client-9.0.1/dataikuapi/dss/macro.py`

 * *Files identical despite different names*

### Comparing `dataiku-api-client-9.0.0/dataikuapi/dss/project.py` & `dataiku-api-client-9.0.1/dataikuapi/dss/project.py`

 * *Files 1% similar despite different names*

```diff
@@ -22,15 +22,15 @@
 from .app import DSSAppManifest
 
 
 class DSSProject(object):
     """
     A handle to interact with a project on the DSS instance.
 
-    Do not create this class directly, instead use :meth:`dataikuapi.DSSClient.get_project``
+    Do not create this class directly, instead use :meth:`dataikuapi.DSSClient.get_project`
     """
     def __init__(self, client, project_key):
        self.client = client
        self.project_key = project_key
 
     def get_summary(self):
         """
@@ -65,15 +65,15 @@
             return found_in
         else:
             return root
 
     def move_to_folder(self, folder):
         """
         Moves this project to a project folder
-        :param folder :class:`dataikuapi.dss.projectfolder.DSSProjectFolder
+        :param folder :class:`dataikuapi.dss.projectfolder.DSSProjectFolder`
         """
         current_folder = self.get_project_folder()
         current_folder.move_project_to(self.project_key, folder)
 
     ########################################################
     # Project deletion
     ########################################################
@@ -819,35 +819,34 @@
         """
         return DSSJob(self.client, self.project_key, id)
 
     def start_job(self, definition):
         """
         Create a new job, and return a handle to interact with it
         
-        Args:
-            definition: the definition for the job to create. The definition must contain the type of job (RECURSIVE_BUILD, 
-            NON_RECURSIVE_FORCED_BUILD, RECURSIVE_FORCED_BUILD, RECURSIVE_MISSING_ONLY_BUILD) and a list of outputs to build.
-            Optionally, a refreshHiveMetastore field can specify whether to re-synchronize the Hive metastore for recomputed
-            HDFS datasets.
+        :param dict definition: The definition should contain: 
+            
+            * the type of job (RECURSIVE_BUILD, NON_RECURSIVE_FORCED_BUILD, RECURSIVE_FORCED_BUILD, RECURSIVE_MISSING_ONLY_BUILD)
+            * a list of outputs to build from the available types: (DATASET, MANAGED_FOLDER, SAVED_MODEL, STREAMING_ENDPOINT)
+            * (Optional) a refreshHiveMetastore field (True or False) to specify whether to re-synchronize the Hive metastore for recomputed HDFS datasets.
         
-        Returns:
-            A :class:`dataikuapi.dss.job.DSSJob` job handle
+        :returns: A :class:`dataikuapi.dss.job.DSSJob` job handle
         """
         job_def = self.client._perform_json("POST", "/projects/%s/jobs/" % self.project_key, body = definition)
         return DSSJob(self.client, self.project_key, job_def['id'])
 
     def start_job_and_wait(self, definition, no_fail=False):
         """
         Starts a new job and waits for it to complete.
         
-        Args:
-            definition: the definition for the job to create. The definition must contain the type of job (RECURSIVE_BUILD, 
-            NON_RECURSIVE_FORCED_BUILD, RECURSIVE_FORCED_BUILD, RECURSIVE_MISSING_ONLY_BUILD) and a list of outputs to build.
-            Optionally, a refreshHiveMetastore field can specify whether to re-synchronize the Hive metastore for recomputed
-            HDFS datasets.
+        :param dict definition: The definition should contain:
+            
+            * the type of job (RECURSIVE_BUILD, NON_RECURSIVE_FORCED_BUILD, RECURSIVE_FORCED_BUILD, RECURSIVE_MISSING_ONLY_BUILD)
+            * a list of outputs to build from the available types: (DATASET, MANAGED_FOLDER, SAVED_MODEL, STREAMING_ENDPOINT)
+            * (Optional) a refreshHiveMetastore field (True or False) to specify whether to re-synchronize the Hive metastore for recomputed HDFS datasets.
         """
         job_def = self.client._perform_json("POST", "/projects/%s/jobs/" % self.project_key, body = definition)
         job = DSSJob(self.client, self.project_key, job_def['id'])
         waiter = DSSJobWaiter(job)
         return waiter.wait(no_fail)
 
     def new_job(self, job_type='NON_RECURSIVE_FORCED_BUILD'):
@@ -879,16 +878,16 @@
     def list_jupyter_notebooks(self, active=False, as_type="object"):
         """
         List the jupyter notebooks of a project.
 
         :param bool as_type: How to return the list. Supported values are "listitems" and "objects".
         :param bool active: if True, only return currently running jupyter notebooks.
 
-        :returns: The list of the notebooks. If "as_type" is "listitems", each one as a :class:`dataikuapi.dss.notebook.DSSJupyterNotebookListItem`,
-        if "as_type" is "objects", each one as a :class:`dataikuapi.dss.notebook.DSSJupyterNotebook`
+        :returns: The list of the notebooks. If "as_type" is "listitems", each one as a :class:`dataikuapi.dss.notebook.DSSJupyterNotebookListItem`, if "as_type" is "objects", each one as a :class:`dataikuapi.dss.notebook.DSSJupyterNotebook`
+        
         :rtype: list of :class:`dataikuapi.dss.notebook.DSSJupyterNotebook` or list of :class:`dataikuapi.dss.notebook.DSSJupyterNotebookListItem`
         """
         notebook_items = self.client._perform_json("GET", "/projects/%s/jupyter-notebooks/" % self.project_key, params={"active": active})
         if as_type == "listitems" or as_type == "listitem":
             return [DSSJupyterNotebookListItem(self.client, notebook_item) for notebook_item in notebook_items]
         elif as_type == "objects" or as_type == "object":
             return [DSSJupyterNotebook(self.client, self.project_key, notebook_item["name"]) for notebook_item in notebook_items]
@@ -964,15 +963,15 @@
 
     def set_variables(self, obj):
         """
         Sets the variables of this project.
         WARNING: if executed from a python recipe, the changes made by `set_variables` will not be "seen" in that recipe.
                  Use the internal API dataiku.get_custom_variables() instead if this behavior is needed
 
-        @param dict obj: must be a modified version of the object returned by get_variables
+        :param dict obj: must be a modified version of the object returned by get_variables
         """
         if not "standard" in obj:
             raise ValueError("Missing 'standard' key in argument")
         if not "local" in obj:
             raise ValueError("Missing 'local' key in argument")
 
         self.client._perform_empty(
@@ -1031,34 +1030,56 @@
         return DSSAPIService(self.client, self.project_key, service_id)
 
     ########################################################
     # Bundles / Export and Publish (Design node)
     ########################################################
 
     def list_exported_bundles(self):
+        """
+        :returns: A dictionary of all bundles for a project on the Design node.
+        """
         return self.client._perform_json("GET",
                 "/projects/%s/bundles/exported" % self.project_key)
 
     def export_bundle(self, bundle_id):
+        """
+        Creates a new project bundle on the Design node 
+        
+        :param str bundle_id: bundle id tag 
+        """
         return self.client._perform_json("PUT",
                 "/projects/%s/bundles/exported/%s" % (self.project_key, bundle_id))
 
     def get_exported_bundle_archive_stream(self, bundle_id):
         """
         Download a bundle archive that can be deployed in a DSS automation Node, as a binary stream.
-        Warning: this stream will monopolize the DSSClient until closed.
+        
+        .. warning::
+            
+            The stream must be closed after use. Use a ``with`` statement to handle closing the stream at the end of the block by default. For example:
+            
+            .. code-block:: python 
+        
+                    with project.get_exported_bundle_archive_stream('v1') as fp:
+                        # use fp 
+                    
+                    # or explicitly close the stream after use
+                    fp = project.get_exported_bundle_archive_stream('v1')
+                    # use fp, then close 
+                    fp.close()
+                    
         """
         return self.client._perform_raw("GET",
                 "/projects/%s/bundles/exported/%s/archive" % (self.project_key, bundle_id))
 
     def download_exported_bundle_archive_to_file(self, bundle_id, path):
         """
         Download a bundle archive that can be deployed in a DSS automation Node into the given output file.
         
-        :param path if "-", will write to /dev/stdout
+        :param string path: if "-", will write to /dev/stdout
         """
         if path == "-":
             path= "/dev/stdout"
         stream = self.get_exported_bundle_archive_stream(bundle_id)
 
         with open(path, 'wb') as f:
             for chunk in stream.iter_content(chunk_size=10000):
@@ -1086,23 +1107,42 @@
         return self.client._perform_json("POST", "/projects/%s/bundles/%s/publish" % (self.project_key, bundle_id), params=params)
 
     ########################################################
     # Bundles / Import (Automation node)
     ########################################################
 
     def list_imported_bundles(self):
+        """
+        :returns: a dict containing bundle imports for a project, on the Automation node.
+        """
         return self.client._perform_json("GET",
                 "/projects/%s/bundles/imported" % self.project_key)
 
     def import_bundle_from_archive(self, archive_path):
+        """
+        Imports a bundle from a zip archive path on the Automation node.
+        
+        :param str archive_path: A full path to a zip archive, for example `/home/dataiku/my-bundle-v1.zip`
+        """
         return self.client._perform_json("POST",
                 "/projects/%s/bundles/imported/actions/importFromArchive" % (self.project_key),
                  params = { "archivePath" : osp.abspath(archive_path) })
 
     def import_bundle_from_stream(self, fp):
+        """
+        Imports a bundle from a file stream, on the Automation node. 
+        
+        :param file-like fp: file handler. Usage example: 
+        
+        .. code-block:: python
+
+            project = client.get_project('MY_PROJECT')
+            with open('/home/dataiku/my-bundle-v1.zip', 'rb') as f:
+                project.import_bundle_from_stream(f)
+        """
         files = {'file': fp}
         return self.client._perform_empty("POST",
                 "/projects/%s/bundles/imported/actions/importFromStream" % (self.project_key),
                 files=files)
 
     def activate_bundle(self, bundle_id, scenarios_to_enable=None):
         """
@@ -1116,14 +1156,19 @@
         """
         options = {"scenariosActiveOnActivation": scenarios_to_enable} if scenarios_to_enable else {}
 
         return self.client._perform_json("POST",
                 "/projects/%s/bundles/imported/%s/actions/activate" % (self.project_key, bundle_id), body=options)
 
     def preload_bundle(self, bundle_id):
+        """
+        Preloads a bundle that has been imported on the Automation node 
+        
+        :param str bundle_id: the bundle_id for an existing imported bundle
+        """
         return self.client._perform_json("POST",
                 "/projects/%s/bundles/imported/%s/actions/preload" % (self.project_key, bundle_id))
 
 
     ########################################################
     # Scenarios
     ########################################################
@@ -1196,16 +1241,17 @@
         else:
             raise ValueError("Unknown as_type")
 
 
     def get_recipe(self, recipe_name):
         """
         Gets a :class:`dataikuapi.dss.recipe.DSSRecipe` handle to interact with a recipe
+        
         :param str recipe_name: The name of the recipe
-        :rtype :class:`dataikuapi.dss.recipe.DSSRecipe`
+        :rtype: :class:`dataikuapi.dss.recipe.DSSRecipe`
         """
         return DSSRecipe(self.client, self.project_key, recipe_name)
 
     def create_recipe(self, recipe_proto, creation_settings):
         """
         Create a new recipe in the project, and return a handle to interact with it.
         We strongly recommend that you use the creator helpers instead of calling this directly.
@@ -1291,14 +1337,17 @@
             return recipe.CodeRecipeCreator(name, type, self)
 
     ########################################################
     # Flow
     ########################################################
 
     def get_flow(self):
+        """
+        :rtype: A :class:`dataikuapi.dss.flow.DSSProjectFlow`
+        """
         return DSSProjectFlow(self.client, self)
 
     ########################################################
     # Security
     ########################################################
     
     def sync_datasets_acls(self):
@@ -1677,14 +1726,19 @@
         """
         self.definition['refreshHiveMetastore'] = refresh_metastore
         return self
 
     def with_output(self, name, object_type=None, object_project_key=None, partition=None):
         """
         Adds an item to build in this job
+        
+        :param name: name of the output object
+        :param object_type: type of object to build from: DATASET, MANAGED_FOLDER, SAVED_MODEL, STREAMING_ENDPOINT
+        :param object_project_key: PROJECT_KEY for the project that contains the object to build 
+        :param partition: specify partition to build
         """
         self.definition['outputs'].append({'type':object_type, 'id':name, 'projectKey':object_project_key, 'partition':partition})
         return self
 
     def get_definition(self):
         """Gets the internal definition for this job"""
         return self.definition
```

### Comparing `dataiku-api-client-9.0.0/dataikuapi/utils.py` & `dataiku-api-client-9.0.1/dataikuapi/utils.py`

 * *Files identical despite different names*

### Comparing `dataiku-api-client-9.0.0/dataikuapi/apinode_admin/auth.py` & `dataiku-api-client-9.0.1/dataikuapi/apinode_admin/auth.py`

 * *Files identical despite different names*

### Comparing `dataiku-api-client-9.0.0/dataikuapi/apinode_admin/service.py` & `dataiku-api-client-9.0.1/dataikuapi/apinode_admin/service.py`

 * *Files identical despite different names*

### Comparing `dataiku-api-client-9.0.0/dataikuapi/apinode_admin_client.py` & `dataiku-api-client-9.0.1/dataikuapi/apinode_admin_client.py`

 * *Files identical despite different names*

### Comparing `dataiku-api-client-9.0.0/dataiku_api_client.egg-info/PKG-INFO` & `dataiku-api-client-9.0.1/dataiku_api_client.egg-info/PKG-INFO`

 * *Files 6% similar despite different names*

```diff
@@ -1,25 +1,29 @@
 Metadata-Version: 1.1
 Name: dataiku-api-client
-Version: 9.0.0
+Version: 9.0.1
 Summary: Python API client for Dataiku APIs
 Home-page: https://www.dataiku.com
 Author: Dataiku
 Author-email: support@dataiku.com
 License: Apache Software License
-Download-URL: https://github.com/dataiku/dataiku-api-client-python/tarball/9.0.0
-Description-Content-Type: UNKNOWN
+Download-URL: https://github.com/dataiku/dataiku-api-client-python/tarball/9.0.1
 Description: API client for Dataiku Data Science Studio
         
         For more information, see:
         https://doc.dataiku.com/dss/latest/python-api/rest-api-client/index.html
         
         Changelog
         ==========
         
+        9.0.1 (2021-12-17)
+        ------------------
+        
+        * Relax version constraint on requests
+        
         9.0.0 (2021-05-07)
         ------------------
         
         * Initial release for DSS 9.0
         
         8.0.0 (2020-08-14)
         -------------------
```

### Comparing `dataiku-api-client-9.0.0/dataiku_api_client.egg-info/SOURCES.txt` & `dataiku-api-client-9.0.1/dataiku_api_client.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `dataiku-api-client-9.0.0/setup.py` & `dataiku-api-client-9.0.1/setup.py`

 * *Files 3% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 #!/usr/bin/env python
 
 from setuptools import setup
 
-VERSION = "9.0.0"
+VERSION = "9.0.1"
 
 long_description = (open('README').read() +
     '\n\n' + open('HISTORY.txt').read())
 
 setup(
         name='dataiku-api-client',
         version=VERSION,
@@ -23,11 +23,11 @@
             'Intended Audience :: Developers',
             'License :: OSI Approved :: Apache Software License',
             'Topic :: Software Development :: Libraries',
             'Programming Language :: Python',
             'Operating System :: OS Independent'
         ],
         install_requires = [
-            "requests>=2,<2.22",
+            "requests<3",
             "python-dateutil"
         ]
      )
```

### Comparing `dataiku-api-client-9.0.0/HISTORY.txt` & `dataiku-api-client-9.0.1/HISTORY.txt`

 * *Files 3% similar despite different names*

```diff
@@ -1,10 +1,15 @@
 Changelog
 ==========
 
+9.0.1 (2021-12-17)
+------------------
+
+* Relax version constraint on requests
+
 9.0.0 (2021-05-07)
 ------------------
 
 * Initial release for DSS 9.0
 
 8.0.0 (2020-08-14)
 -------------------
```

### Comparing `dataiku-api-client-9.0.0/LICENSE.txt` & `dataiku-api-client-9.0.1/LICENSE.txt`

 * *Files identical despite different names*

