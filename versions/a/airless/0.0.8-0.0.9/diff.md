# Comparing `tmp/airless-0.0.8.tar.gz` & `tmp/airless-0.0.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "airless-0.0.8.tar", last modified: Wed Nov 23 19:47:45 2022, max compression
+gzip compressed data, was "airless-0.0.9.tar", last modified: Wed Nov 23 20:22:29 2022, max compression
```

## Comparing `airless-0.0.8.tar` & `airless-0.0.9.tar`

### file list

```diff
@@ -1,41 +1,46 @@
-drwxrwxr-x   0 luizyamaoka  (1000) luizyamaoka  (1000)        0 2022-11-23 19:47:45.985662 airless-0.0.8/
--rw-rw-r--   0 luizyamaoka  (1000) luizyamaoka  (1000)     1068 2022-11-16 19:01:48.000000 airless-0.0.8/LICENSE
--rw-rw-r--   0 luizyamaoka  (1000) luizyamaoka  (1000)      209 2022-11-23 19:47:45.985662 airless-0.0.8/PKG-INFO
--rw-rw-r--   0 luizyamaoka  (1000) luizyamaoka  (1000)      273 2022-11-22 19:28:42.000000 airless-0.0.8/README.md
-drwxrwxr-x   0 luizyamaoka  (1000) luizyamaoka  (1000)        0 2022-11-23 19:47:45.969662 airless-0.0.8/airless/
--rw-rw-r--   0 luizyamaoka  (1000) luizyamaoka  (1000)        0 2022-11-22 20:28:19.000000 airless-0.0.8/airless/__init__.py
--rw-rw-r--   0 luizyamaoka  (1000) luizyamaoka  (1000)      246 2022-11-22 19:28:42.000000 airless-0.0.8/airless/config.py
-drwxrwxr-x   0 luizyamaoka  (1000) luizyamaoka  (1000)        0 2022-11-23 19:47:45.977662 airless-0.0.8/airless/hook/
--rw-rw-r--   0 luizyamaoka  (1000) luizyamaoka  (1000)        0 2022-11-22 20:28:30.000000 airless-0.0.8/airless/hook/__init__.py
--rw-rw-r--   0 luizyamaoka  (1000) luizyamaoka  (1000)      104 2022-11-22 19:28:42.000000 airless-0.0.8/airless/hook/base.py
-drwxrwxr-x   0 luizyamaoka  (1000) luizyamaoka  (1000)        0 2022-11-23 19:47:45.977662 airless-0.0.8/airless/hook/google/
--rw-rw-r--   0 luizyamaoka  (1000) luizyamaoka  (1000)        0 2022-11-22 20:36:54.000000 airless-0.0.8/airless/hook/google/__init__.py
--rw-rw-r--   0 luizyamaoka  (1000) luizyamaoka  (1000)     6336 2022-11-23 19:16:48.000000 airless-0.0.8/airless/hook/google/bigquery.py
--rw-rw-r--   0 luizyamaoka  (1000) luizyamaoka  (1000)      844 2022-11-22 19:28:42.000000 airless-0.0.8/airless/hook/google/pubsub.py
--rw-rw-r--   0 luizyamaoka  (1000) luizyamaoka  (1000)     1763 2022-11-22 19:28:42.000000 airless-0.0.8/airless/hook/google/secret_manager.py
--rw-rw-r--   0 luizyamaoka  (1000) luizyamaoka  (1000)     2773 2022-11-22 19:28:42.000000 airless-0.0.8/airless/hook/google/storage.py
-drwxrwxr-x   0 luizyamaoka  (1000) luizyamaoka  (1000)        0 2022-11-23 19:47:45.981662 airless-0.0.8/airless/hook/local/
--rw-rw-r--   0 luizyamaoka  (1000) luizyamaoka  (1000)        0 2022-11-22 20:28:30.000000 airless-0.0.8/airless/hook/local/__init__.py
--rw-rw-r--   0 luizyamaoka  (1000) luizyamaoka  (1000)      889 2022-11-22 19:28:42.000000 airless-0.0.8/airless/hook/local/file.py
-drwxrwxr-x   0 luizyamaoka  (1000) luizyamaoka  (1000)        0 2022-11-23 19:47:45.981662 airless-0.0.8/airless/hook/notification/
--rw-rw-r--   0 luizyamaoka  (1000) luizyamaoka  (1000)        0 2022-11-22 20:28:30.000000 airless-0.0.8/airless/hook/notification/__init__.py
--rw-rw-r--   0 luizyamaoka  (1000) luizyamaoka  (1000)     1811 2022-11-22 19:28:42.000000 airless-0.0.8/airless/hook/notification/email.py
--rw-rw-r--   0 luizyamaoka  (1000) luizyamaoka  (1000)      937 2022-11-22 19:28:42.000000 airless-0.0.8/airless/hook/notification/slack.py
-drwxrwxr-x   0 luizyamaoka  (1000) luizyamaoka  (1000)        0 2022-11-23 19:47:45.985662 airless-0.0.8/airless/operator/
--rw-rw-r--   0 luizyamaoka  (1000) luizyamaoka  (1000)     3475 2022-11-23 17:54:11.000000 airless-0.0.8/airless/operator/base.py
--rw-rw-r--   0 luizyamaoka  (1000) luizyamaoka  (1000)     3714 2022-11-23 19:29:46.000000 airless-0.0.8/airless/operator/error.py
-drwxrwxr-x   0 luizyamaoka  (1000) luizyamaoka  (1000)        0 2022-11-23 19:47:45.985662 airless-0.0.8/airless/operator/google/
--rw-rw-r--   0 luizyamaoka  (1000) luizyamaoka  (1000)        0 2022-11-22 20:28:30.000000 airless-0.0.8/airless/operator/google/__init__.py
--rw-rw-r--   0 luizyamaoka  (1000) luizyamaoka  (1000)     2827 2022-11-23 19:38:32.000000 airless-0.0.8/airless/operator/google/bigquery.py
-drwxrwxr-x   0 luizyamaoka  (1000) luizyamaoka  (1000)        0 2022-11-23 19:47:45.985662 airless-0.0.8/airless/operator/notification/
--rw-rw-r--   0 luizyamaoka  (1000) luizyamaoka  (1000)        0 2022-11-22 20:28:30.000000 airless-0.0.8/airless/operator/notification/__init__.py
--rw-rw-r--   0 luizyamaoka  (1000) luizyamaoka  (1000)      934 2022-11-22 19:28:42.000000 airless-0.0.8/airless/operator/notification/email.py
--rw-rw-r--   0 luizyamaoka  (1000) luizyamaoka  (1000)      435 2022-11-22 19:28:42.000000 airless-0.0.8/airless/operator/notification/slack.py
-drwxrwxr-x   0 luizyamaoka  (1000) luizyamaoka  (1000)        0 2022-11-23 19:47:45.973662 airless-0.0.8/airless.egg-info/
--rw-rw-r--   0 luizyamaoka  (1000) luizyamaoka  (1000)      209 2022-11-23 19:47:45.000000 airless-0.0.8/airless.egg-info/PKG-INFO
--rw-rw-r--   0 luizyamaoka  (1000) luizyamaoka  (1000)      852 2022-11-23 19:47:45.000000 airless-0.0.8/airless.egg-info/SOURCES.txt
--rw-rw-r--   0 luizyamaoka  (1000) luizyamaoka  (1000)        1 2022-11-23 19:47:45.000000 airless-0.0.8/airless.egg-info/dependency_links.txt
--rw-rw-r--   0 luizyamaoka  (1000) luizyamaoka  (1000)      122 2022-11-23 19:47:45.000000 airless-0.0.8/airless.egg-info/requires.txt
--rw-rw-r--   0 luizyamaoka  (1000) luizyamaoka  (1000)        8 2022-11-23 19:47:45.000000 airless-0.0.8/airless.egg-info/top_level.txt
--rw-rw-r--   0 luizyamaoka  (1000) luizyamaoka  (1000)      262 2022-11-23 19:47:12.000000 airless-0.0.8/pyproject.toml
--rw-rw-r--   0 luizyamaoka  (1000) luizyamaoka  (1000)      255 2022-11-23 19:47:45.989662 airless-0.0.8/setup.cfg
+drwxrwxr-x   0 luizyamaoka  (1000) luizyamaoka  (1000)        0 2022-11-23 20:22:29.665904 airless-0.0.9/
+-rw-rw-r--   0 luizyamaoka  (1000) luizyamaoka  (1000)     1068 2022-11-16 19:01:48.000000 airless-0.0.9/LICENSE
+-rw-rw-r--   0 luizyamaoka  (1000) luizyamaoka  (1000)      209 2022-11-23 20:22:29.665904 airless-0.0.9/PKG-INFO
+-rw-rw-r--   0 luizyamaoka  (1000) luizyamaoka  (1000)      273 2022-11-22 19:28:42.000000 airless-0.0.9/README.md
+drwxrwxr-x   0 luizyamaoka  (1000) luizyamaoka  (1000)        0 2022-11-23 20:22:29.645904 airless-0.0.9/airless/
+-rw-rw-r--   0 luizyamaoka  (1000) luizyamaoka  (1000)        0 2022-11-22 20:28:19.000000 airless-0.0.9/airless/__init__.py
+-rw-rw-r--   0 luizyamaoka  (1000) luizyamaoka  (1000)      246 2022-11-22 19:28:42.000000 airless-0.0.9/airless/config.py
+drwxrwxr-x   0 luizyamaoka  (1000) luizyamaoka  (1000)        0 2022-11-23 20:22:29.649904 airless-0.0.9/airless/dto/
+-rw-rw-r--   0 luizyamaoka  (1000) luizyamaoka  (1000)        0 2022-11-23 20:14:39.000000 airless-0.0.9/airless/dto/__init__.py
+-rw-rw-r--   0 luizyamaoka  (1000) luizyamaoka  (1000)     2357 2022-11-23 19:39:56.000000 airless-0.0.9/airless/dto/pubsub_to_bq.py
+drwxrwxr-x   0 luizyamaoka  (1000) luizyamaoka  (1000)        0 2022-11-23 20:22:29.653904 airless-0.0.9/airless/hook/
+-rw-rw-r--   0 luizyamaoka  (1000) luizyamaoka  (1000)        0 2022-11-22 20:28:30.000000 airless-0.0.9/airless/hook/__init__.py
+-rw-rw-r--   0 luizyamaoka  (1000) luizyamaoka  (1000)      104 2022-11-22 19:28:42.000000 airless-0.0.9/airless/hook/base.py
+drwxrwxr-x   0 luizyamaoka  (1000) luizyamaoka  (1000)        0 2022-11-23 20:22:29.657904 airless-0.0.9/airless/hook/google/
+-rw-rw-r--   0 luizyamaoka  (1000) luizyamaoka  (1000)        0 2022-11-22 20:36:54.000000 airless-0.0.9/airless/hook/google/__init__.py
+-rw-rw-r--   0 luizyamaoka  (1000) luizyamaoka  (1000)     6336 2022-11-23 19:16:48.000000 airless-0.0.9/airless/hook/google/bigquery.py
+-rw-rw-r--   0 luizyamaoka  (1000) luizyamaoka  (1000)      844 2022-11-22 19:28:42.000000 airless-0.0.9/airless/hook/google/pubsub.py
+-rw-rw-r--   0 luizyamaoka  (1000) luizyamaoka  (1000)     1763 2022-11-22 19:28:42.000000 airless-0.0.9/airless/hook/google/secret_manager.py
+-rw-rw-r--   0 luizyamaoka  (1000) luizyamaoka  (1000)     2773 2022-11-22 19:28:42.000000 airless-0.0.9/airless/hook/google/storage.py
+drwxrwxr-x   0 luizyamaoka  (1000) luizyamaoka  (1000)        0 2022-11-23 20:22:29.657904 airless-0.0.9/airless/hook/local/
+-rw-rw-r--   0 luizyamaoka  (1000) luizyamaoka  (1000)        0 2022-11-22 20:28:30.000000 airless-0.0.9/airless/hook/local/__init__.py
+-rw-rw-r--   0 luizyamaoka  (1000) luizyamaoka  (1000)      889 2022-11-22 19:28:42.000000 airless-0.0.9/airless/hook/local/file.py
+drwxrwxr-x   0 luizyamaoka  (1000) luizyamaoka  (1000)        0 2022-11-23 20:22:29.657904 airless-0.0.9/airless/hook/notification/
+-rw-rw-r--   0 luizyamaoka  (1000) luizyamaoka  (1000)        0 2022-11-22 20:28:30.000000 airless-0.0.9/airless/hook/notification/__init__.py
+-rw-rw-r--   0 luizyamaoka  (1000) luizyamaoka  (1000)     1811 2022-11-22 19:28:42.000000 airless-0.0.9/airless/hook/notification/email.py
+-rw-rw-r--   0 luizyamaoka  (1000) luizyamaoka  (1000)      937 2022-11-22 19:28:42.000000 airless-0.0.9/airless/hook/notification/slack.py
+drwxrwxr-x   0 luizyamaoka  (1000) luizyamaoka  (1000)        0 2022-11-23 20:22:29.661904 airless-0.0.9/airless/operator/
+-rw-rw-r--   0 luizyamaoka  (1000) luizyamaoka  (1000)        0 2022-11-23 20:22:03.000000 airless-0.0.9/airless/operator/__init__.py
+-rw-rw-r--   0 luizyamaoka  (1000) luizyamaoka  (1000)     3475 2022-11-23 17:54:11.000000 airless-0.0.9/airless/operator/base.py
+-rw-rw-r--   0 luizyamaoka  (1000) luizyamaoka  (1000)     3714 2022-11-23 19:29:46.000000 airless-0.0.9/airless/operator/error.py
+drwxrwxr-x   0 luizyamaoka  (1000) luizyamaoka  (1000)        0 2022-11-23 20:22:29.661904 airless-0.0.9/airless/operator/google/
+-rw-rw-r--   0 luizyamaoka  (1000) luizyamaoka  (1000)        0 2022-11-22 20:28:30.000000 airless-0.0.9/airless/operator/google/__init__.py
+-rw-rw-r--   0 luizyamaoka  (1000) luizyamaoka  (1000)     2827 2022-11-23 19:38:32.000000 airless-0.0.9/airless/operator/google/bigquery.py
+drwxrwxr-x   0 luizyamaoka  (1000) luizyamaoka  (1000)        0 2022-11-23 20:22:29.661904 airless-0.0.9/airless/operator/notification/
+-rw-rw-r--   0 luizyamaoka  (1000) luizyamaoka  (1000)        0 2022-11-22 20:28:30.000000 airless-0.0.9/airless/operator/notification/__init__.py
+-rw-rw-r--   0 luizyamaoka  (1000) luizyamaoka  (1000)      934 2022-11-22 19:28:42.000000 airless-0.0.9/airless/operator/notification/email.py
+-rw-rw-r--   0 luizyamaoka  (1000) luizyamaoka  (1000)      435 2022-11-22 19:28:42.000000 airless-0.0.9/airless/operator/notification/slack.py
+-rw-rw-r--   0 luizyamaoka  (1000) luizyamaoka  (1000)     2204 2022-11-23 19:20:39.000000 airless-0.0.9/airless/operator/redirect.py
+drwxrwxr-x   0 luizyamaoka  (1000) luizyamaoka  (1000)        0 2022-11-23 20:22:29.649904 airless-0.0.9/airless.egg-info/
+-rw-rw-r--   0 luizyamaoka  (1000) luizyamaoka  (1000)      209 2022-11-23 20:22:29.000000 airless-0.0.9/airless.egg-info/PKG-INFO
+-rw-rw-r--   0 luizyamaoka  (1000) luizyamaoka  (1000)      962 2022-11-23 20:22:29.000000 airless-0.0.9/airless.egg-info/SOURCES.txt
+-rw-rw-r--   0 luizyamaoka  (1000) luizyamaoka  (1000)        1 2022-11-23 20:22:29.000000 airless-0.0.9/airless.egg-info/dependency_links.txt
+-rw-rw-r--   0 luizyamaoka  (1000) luizyamaoka  (1000)      122 2022-11-23 20:22:29.000000 airless-0.0.9/airless.egg-info/requires.txt
+-rw-rw-r--   0 luizyamaoka  (1000) luizyamaoka  (1000)        8 2022-11-23 20:22:29.000000 airless-0.0.9/airless.egg-info/top_level.txt
+-rw-rw-r--   0 luizyamaoka  (1000) luizyamaoka  (1000)      262 2022-11-23 20:15:07.000000 airless-0.0.9/pyproject.toml
+-rw-rw-r--   0 luizyamaoka  (1000) luizyamaoka  (1000)      255 2022-11-23 20:22:29.665904 airless-0.0.9/setup.cfg
```

### Comparing `airless-0.0.8/LICENSE` & `airless-0.0.9/LICENSE`

 * *Files identical despite different names*

### Comparing `airless-0.0.8/airless/hook/google/bigquery.py` & `airless-0.0.9/airless/hook/google/bigquery.py`

 * *Files identical despite different names*

### Comparing `airless-0.0.8/airless/hook/google/pubsub.py` & `airless-0.0.9/airless/hook/google/pubsub.py`

 * *Files identical despite different names*

### Comparing `airless-0.0.8/airless/hook/google/secret_manager.py` & `airless-0.0.9/airless/hook/google/secret_manager.py`

 * *Files identical despite different names*

### Comparing `airless-0.0.8/airless/hook/google/storage.py` & `airless-0.0.9/airless/hook/google/storage.py`

 * *Files identical despite different names*

### Comparing `airless-0.0.8/airless/hook/local/file.py` & `airless-0.0.9/airless/hook/local/file.py`

 * *Files identical despite different names*

### Comparing `airless-0.0.8/airless/hook/notification/email.py` & `airless-0.0.9/airless/hook/notification/email.py`

 * *Files identical despite different names*

### Comparing `airless-0.0.8/airless/hook/notification/slack.py` & `airless-0.0.9/airless/hook/notification/slack.py`

 * *Files identical despite different names*

### Comparing `airless-0.0.8/airless/operator/base.py` & `airless-0.0.9/airless/operator/base.py`

 * *Files identical despite different names*

### Comparing `airless-0.0.8/airless/operator/error.py` & `airless-0.0.9/airless/operator/error.py`

 * *Files identical despite different names*

### Comparing `airless-0.0.8/airless/operator/google/bigquery.py` & `airless-0.0.9/airless/operator/google/bigquery.py`

 * *Files identical despite different names*

### Comparing `airless-0.0.8/airless/operator/notification/email.py` & `airless-0.0.9/airless/operator/notification/email.py`

 * *Files identical despite different names*

### Comparing `airless-0.0.8/airless.egg-info/SOURCES.txt` & `airless-0.0.9/airless.egg-info/SOURCES.txt`

 * *Files 5% similar despite different names*

```diff
@@ -5,26 +5,30 @@
 airless/__init__.py
 airless/config.py
 airless.egg-info/PKG-INFO
 airless.egg-info/SOURCES.txt
 airless.egg-info/dependency_links.txt
 airless.egg-info/requires.txt
 airless.egg-info/top_level.txt
+airless/dto/__init__.py
+airless/dto/pubsub_to_bq.py
 airless/hook/__init__.py
 airless/hook/base.py
 airless/hook/google/__init__.py
 airless/hook/google/bigquery.py
 airless/hook/google/pubsub.py
 airless/hook/google/secret_manager.py
 airless/hook/google/storage.py
 airless/hook/local/__init__.py
 airless/hook/local/file.py
 airless/hook/notification/__init__.py
 airless/hook/notification/email.py
 airless/hook/notification/slack.py
+airless/operator/__init__.py
 airless/operator/base.py
 airless/operator/error.py
+airless/operator/redirect.py
 airless/operator/google/__init__.py
 airless/operator/google/bigquery.py
 airless/operator/notification/__init__.py
 airless/operator/notification/email.py
 airless/operator/notification/slack.py
```

