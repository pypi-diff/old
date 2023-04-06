# Comparing `tmp/ytsaurus-spyt-1.69.1b439.post23515129.dev5.tar.gz` & `tmp/ytsaurus-spyt-1.69.1b439.post23515129.dev9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/ytsaurus-spyt-1.69.1b439.post23515129.dev5.tar", last modified: Tue Apr  4 15:16:56 2023, max compression
+gzip compressed data, was "dist/ytsaurus-spyt-1.69.1b439.post23515129.dev9.tar", last modified: Thu Apr  6 08:54:06 2023, max compression
```

## Comparing `ytsaurus-spyt-1.69.1b439.post23515129.dev5.tar` & `ytsaurus-spyt-1.69.1b439.post23515129.dev9.tar`

### file list

```diff
@@ -1,31 +1,31 @@
-drwxrwxr-x   0 alex-shishkin (323389) dpt_yandex_infra_tech_ytdev_dep8 (246647)        0 2023-04-04 15:16:56.000000 ytsaurus-spyt-1.69.1b439.post23515129.dev5/
-drwxrwxr-x   0 alex-shishkin (323389) dpt_yandex_infra_tech_ytdev_dep8 (246647)        0 2023-04-04 15:16:56.000000 ytsaurus-spyt-1.69.1b439.post23515129.dev5/deps/
-drwxrwxr-x   0 alex-shishkin (323389) dpt_yandex_infra_tech_ytdev_dep8 (246647)        0 2023-04-04 15:16:56.000000 ytsaurus-spyt-1.69.1b439.post23515129.dev5/deps/bin/
--rwxrw-r--   0 alex-shishkin (323389) dpt_yandex_infra_tech_ytdev_dep8 (246647)     1245 2023-04-04 15:16:56.000000 ytsaurus-spyt-1.69.1b439.post23515129.dev5/deps/bin/spark-discovery-yt
--rwxrw-r--   0 alex-shishkin (323389) dpt_yandex_infra_tech_ytdev_dep8 (246647)    11097 2023-04-04 15:16:56.000000 ytsaurus-spyt-1.69.1b439.post23515129.dev5/deps/bin/spark-launch-yt
--rwxrw-r--   0 alex-shishkin (323389) dpt_yandex_infra_tech_ytdev_dep8 (246647)     2351 2023-04-04 15:16:56.000000 ytsaurus-spyt-1.69.1b439.post23515129.dev5/deps/bin/spark-manage-yt
--rwxrw-r--   0 alex-shishkin (323389) dpt_yandex_infra_tech_ytdev_dep8 (246647)      813 2023-04-04 15:16:56.000000 ytsaurus-spyt-1.69.1b439.post23515129.dev5/deps/bin/spark-shell-yt
--rwxrw-r--   0 alex-shishkin (323389) dpt_yandex_infra_tech_ytdev_dep8 (246647)     1063 2023-04-04 15:16:56.000000 ytsaurus-spyt-1.69.1b439.post23515129.dev5/deps/bin/spark-submit-yt
-drwxrwxr-x   0 alex-shishkin (323389) dpt_yandex_infra_tech_ytdev_dep8 (246647)        0 2023-04-04 15:16:56.000000 ytsaurus-spyt-1.69.1b439.post23515129.dev5/deps/jars/
--rw-rw-r--   0 alex-shishkin (323389) dpt_yandex_infra_tech_ytdev_dep8 (246647)  1798359 2023-04-04 15:16:56.000000 ytsaurus-spyt-1.69.1b439.post23515129.dev5/deps/jars/spark-yt-submit.jar
-drwxrwxr-x   0 alex-shishkin (323389) dpt_yandex_infra_tech_ytdev_dep8 (246647)        0 2023-04-04 15:16:56.000000 ytsaurus-spyt-1.69.1b439.post23515129.dev5/spyt/
--rw-rw-r--   0 alex-shishkin (323389) dpt_yandex_infra_tech_ytdev_dep8 (246647)       95 2023-02-22 20:15:30.000000 ytsaurus-spyt-1.69.1b439.post23515129.dev5/spyt/__init__.py
--rw-rw-r--   0 alex-shishkin (323389) dpt_yandex_infra_tech_ytdev_dep8 (246647)    16556 2023-04-04 15:16:01.000000 ytsaurus-spyt-1.69.1b439.post23515129.dev5/spyt/client.py
--rw-rw-r--   0 alex-shishkin (323389) dpt_yandex_infra_tech_ytdev_dep8 (246647)     1106 2023-03-14 10:41:35.000000 ytsaurus-spyt-1.69.1b439.post23515129.dev5/spyt/common.py
--rw-rw-r--   0 alex-shishkin (323389) dpt_yandex_infra_tech_ytdev_dep8 (246647)     7436 2023-04-04 15:16:01.000000 ytsaurus-spyt-1.69.1b439.post23515129.dev5/spyt/conf.py
--rw-rw-r--   0 alex-shishkin (323389) dpt_yandex_infra_tech_ytdev_dep8 (246647)     3493 2023-03-18 23:30:06.000000 ytsaurus-spyt-1.69.1b439.post23515129.dev5/spyt/enabler.py
--rw-rw-r--   0 alex-shishkin (323389) dpt_yandex_infra_tech_ytdev_dep8 (246647)    34102 2023-04-04 15:16:01.000000 ytsaurus-spyt-1.69.1b439.post23515129.dev5/spyt/standalone.py
--rw-rw-r--   0 alex-shishkin (323389) dpt_yandex_infra_tech_ytdev_dep8 (246647)     9779 2023-03-14 10:41:35.000000 ytsaurus-spyt-1.69.1b439.post23515129.dev5/spyt/submit.py
--rw-rw-r--   0 alex-shishkin (323389) dpt_yandex_infra_tech_ytdev_dep8 (246647)     4003 2023-03-14 10:41:35.000000 ytsaurus-spyt-1.69.1b439.post23515129.dev5/spyt/types.py
--rw-rw-r--   0 alex-shishkin (323389) dpt_yandex_infra_tech_ytdev_dep8 (246647)    10373 2023-04-04 15:16:01.000000 ytsaurus-spyt-1.69.1b439.post23515129.dev5/spyt/utils.py
--rw-rw-r--   0 alex-shishkin (323389) dpt_yandex_infra_tech_ytdev_dep8 (246647)      181 2023-04-04 15:16:42.000000 ytsaurus-spyt-1.69.1b439.post23515129.dev5/spyt/version.py
-drwxrwxr-x   0 alex-shishkin (323389) dpt_yandex_infra_tech_ytdev_dep8 (246647)        0 2023-04-04 15:16:56.000000 ytsaurus-spyt-1.69.1b439.post23515129.dev5/ytsaurus_spyt.egg-info/
--rw-rw-r--   0 alex-shishkin (323389) dpt_yandex_infra_tech_ytdev_dep8 (246647)      333 2023-04-04 15:16:56.000000 ytsaurus-spyt-1.69.1b439.post23515129.dev5/ytsaurus_spyt.egg-info/PKG-INFO
--rw-rw-r--   0 alex-shishkin (323389) dpt_yandex_infra_tech_ytdev_dep8 (246647)      515 2023-04-04 15:16:56.000000 ytsaurus-spyt-1.69.1b439.post23515129.dev5/ytsaurus_spyt.egg-info/SOURCES.txt
--rw-rw-r--   0 alex-shishkin (323389) dpt_yandex_infra_tech_ytdev_dep8 (246647)        1 2023-04-04 15:16:56.000000 ytsaurus-spyt-1.69.1b439.post23515129.dev5/ytsaurus_spyt.egg-info/dependency_links.txt
--rw-rw-r--   0 alex-shishkin (323389) dpt_yandex_infra_tech_ytdev_dep8 (246647)       40 2023-04-04 15:16:56.000000 ytsaurus-spyt-1.69.1b439.post23515129.dev5/ytsaurus_spyt.egg-info/requires.txt
--rw-rw-r--   0 alex-shishkin (323389) dpt_yandex_infra_tech_ytdev_dep8 (246647)        5 2023-04-04 15:16:56.000000 ytsaurus-spyt-1.69.1b439.post23515129.dev5/ytsaurus_spyt.egg-info/top_level.txt
--rw-rw-r--   0 alex-shishkin (323389) dpt_yandex_infra_tech_ytdev_dep8 (246647)      110 2023-02-22 20:15:30.000000 ytsaurus-spyt-1.69.1b439.post23515129.dev5/MANIFEST.in
--rw-rw-r--   0 alex-shishkin (323389) dpt_yandex_infra_tech_ytdev_dep8 (246647)     1011 2023-04-04 15:16:01.000000 ytsaurus-spyt-1.69.1b439.post23515129.dev5/setup.py
--rw-rw-r--   0 alex-shishkin (323389) dpt_yandex_infra_tech_ytdev_dep8 (246647)      333 2023-04-04 15:16:56.000000 ytsaurus-spyt-1.69.1b439.post23515129.dev5/PKG-INFO
--rw-rw-r--   0 alex-shishkin (323389) dpt_yandex_infra_tech_ytdev_dep8 (246647)       38 2023-04-04 15:16:56.000000 ytsaurus-spyt-1.69.1b439.post23515129.dev5/setup.cfg
+drwxrwxr-x   0 alex-shishkin (323389) dpt_yandex_infra_tech_ytdev_dep8 (246647)        0 2023-04-06 08:54:06.000000 ytsaurus-spyt-1.69.1b439.post23515129.dev9/
+drwxrwxr-x   0 alex-shishkin (323389) dpt_yandex_infra_tech_ytdev_dep8 (246647)        0 2023-04-06 08:54:06.000000 ytsaurus-spyt-1.69.1b439.post23515129.dev9/deps/
+drwxrwxr-x   0 alex-shishkin (323389) dpt_yandex_infra_tech_ytdev_dep8 (246647)        0 2023-04-06 08:54:06.000000 ytsaurus-spyt-1.69.1b439.post23515129.dev9/deps/bin/
+-rwxrw-r--   0 alex-shishkin (323389) dpt_yandex_infra_tech_ytdev_dep8 (246647)     1245 2023-04-06 08:54:06.000000 ytsaurus-spyt-1.69.1b439.post23515129.dev9/deps/bin/spark-discovery-yt
+-rwxrw-r--   0 alex-shishkin (323389) dpt_yandex_infra_tech_ytdev_dep8 (246647)    11097 2023-04-06 08:54:06.000000 ytsaurus-spyt-1.69.1b439.post23515129.dev9/deps/bin/spark-launch-yt
+-rwxrw-r--   0 alex-shishkin (323389) dpt_yandex_infra_tech_ytdev_dep8 (246647)     2351 2023-04-06 08:54:06.000000 ytsaurus-spyt-1.69.1b439.post23515129.dev9/deps/bin/spark-manage-yt
+-rwxrw-r--   0 alex-shishkin (323389) dpt_yandex_infra_tech_ytdev_dep8 (246647)      813 2023-04-06 08:54:06.000000 ytsaurus-spyt-1.69.1b439.post23515129.dev9/deps/bin/spark-shell-yt
+-rwxrw-r--   0 alex-shishkin (323389) dpt_yandex_infra_tech_ytdev_dep8 (246647)     1063 2023-04-06 08:54:06.000000 ytsaurus-spyt-1.69.1b439.post23515129.dev9/deps/bin/spark-submit-yt
+drwxrwxr-x   0 alex-shishkin (323389) dpt_yandex_infra_tech_ytdev_dep8 (246647)        0 2023-04-06 08:54:06.000000 ytsaurus-spyt-1.69.1b439.post23515129.dev9/deps/jars/
+-rw-rw-r--   0 alex-shishkin (323389) dpt_yandex_infra_tech_ytdev_dep8 (246647)  1798359 2023-04-06 08:54:06.000000 ytsaurus-spyt-1.69.1b439.post23515129.dev9/deps/jars/spark-yt-submit.jar
+drwxrwxr-x   0 alex-shishkin (323389) dpt_yandex_infra_tech_ytdev_dep8 (246647)        0 2023-04-06 08:54:06.000000 ytsaurus-spyt-1.69.1b439.post23515129.dev9/spyt/
+-rw-rw-r--   0 alex-shishkin (323389) dpt_yandex_infra_tech_ytdev_dep8 (246647)       95 2023-02-22 20:15:30.000000 ytsaurus-spyt-1.69.1b439.post23515129.dev9/spyt/__init__.py
+-rw-rw-r--   0 alex-shishkin (323389) dpt_yandex_infra_tech_ytdev_dep8 (246647)    16556 2023-04-06 08:51:29.000000 ytsaurus-spyt-1.69.1b439.post23515129.dev9/spyt/client.py
+-rw-rw-r--   0 alex-shishkin (323389) dpt_yandex_infra_tech_ytdev_dep8 (246647)     1106 2023-03-14 10:41:35.000000 ytsaurus-spyt-1.69.1b439.post23515129.dev9/spyt/common.py
+-rw-rw-r--   0 alex-shishkin (323389) dpt_yandex_infra_tech_ytdev_dep8 (246647)     7436 2023-04-06 08:51:29.000000 ytsaurus-spyt-1.69.1b439.post23515129.dev9/spyt/conf.py
+-rw-rw-r--   0 alex-shishkin (323389) dpt_yandex_infra_tech_ytdev_dep8 (246647)     3493 2023-03-18 23:30:06.000000 ytsaurus-spyt-1.69.1b439.post23515129.dev9/spyt/enabler.py
+-rw-rw-r--   0 alex-shishkin (323389) dpt_yandex_infra_tech_ytdev_dep8 (246647)    34102 2023-04-06 08:51:29.000000 ytsaurus-spyt-1.69.1b439.post23515129.dev9/spyt/standalone.py
+-rw-rw-r--   0 alex-shishkin (323389) dpt_yandex_infra_tech_ytdev_dep8 (246647)     9779 2023-03-14 10:41:35.000000 ytsaurus-spyt-1.69.1b439.post23515129.dev9/spyt/submit.py
+-rw-rw-r--   0 alex-shishkin (323389) dpt_yandex_infra_tech_ytdev_dep8 (246647)     4003 2023-03-14 10:41:35.000000 ytsaurus-spyt-1.69.1b439.post23515129.dev9/spyt/types.py
+-rw-rw-r--   0 alex-shishkin (323389) dpt_yandex_infra_tech_ytdev_dep8 (246647)    10373 2023-04-06 08:51:29.000000 ytsaurus-spyt-1.69.1b439.post23515129.dev9/spyt/utils.py
+-rw-rw-r--   0 alex-shishkin (323389) dpt_yandex_infra_tech_ytdev_dep8 (246647)      181 2023-04-06 08:53:46.000000 ytsaurus-spyt-1.69.1b439.post23515129.dev9/spyt/version.py
+drwxrwxr-x   0 alex-shishkin (323389) dpt_yandex_infra_tech_ytdev_dep8 (246647)        0 2023-04-06 08:54:06.000000 ytsaurus-spyt-1.69.1b439.post23515129.dev9/ytsaurus_spyt.egg-info/
+-rw-rw-r--   0 alex-shishkin (323389) dpt_yandex_infra_tech_ytdev_dep8 (246647)      333 2023-04-06 08:54:06.000000 ytsaurus-spyt-1.69.1b439.post23515129.dev9/ytsaurus_spyt.egg-info/PKG-INFO
+-rw-rw-r--   0 alex-shishkin (323389) dpt_yandex_infra_tech_ytdev_dep8 (246647)      515 2023-04-06 08:54:06.000000 ytsaurus-spyt-1.69.1b439.post23515129.dev9/ytsaurus_spyt.egg-info/SOURCES.txt
+-rw-rw-r--   0 alex-shishkin (323389) dpt_yandex_infra_tech_ytdev_dep8 (246647)        1 2023-04-06 08:54:06.000000 ytsaurus-spyt-1.69.1b439.post23515129.dev9/ytsaurus_spyt.egg-info/dependency_links.txt
+-rw-rw-r--   0 alex-shishkin (323389) dpt_yandex_infra_tech_ytdev_dep8 (246647)       40 2023-04-06 08:54:06.000000 ytsaurus-spyt-1.69.1b439.post23515129.dev9/ytsaurus_spyt.egg-info/requires.txt
+-rw-rw-r--   0 alex-shishkin (323389) dpt_yandex_infra_tech_ytdev_dep8 (246647)        5 2023-04-06 08:54:06.000000 ytsaurus-spyt-1.69.1b439.post23515129.dev9/ytsaurus_spyt.egg-info/top_level.txt
+-rw-rw-r--   0 alex-shishkin (323389) dpt_yandex_infra_tech_ytdev_dep8 (246647)      110 2023-02-22 20:15:30.000000 ytsaurus-spyt-1.69.1b439.post23515129.dev9/MANIFEST.in
+-rw-rw-r--   0 alex-shishkin (323389) dpt_yandex_infra_tech_ytdev_dep8 (246647)     1011 2023-04-06 08:51:29.000000 ytsaurus-spyt-1.69.1b439.post23515129.dev9/setup.py
+-rw-rw-r--   0 alex-shishkin (323389) dpt_yandex_infra_tech_ytdev_dep8 (246647)      333 2023-04-06 08:54:06.000000 ytsaurus-spyt-1.69.1b439.post23515129.dev9/PKG-INFO
+-rw-rw-r--   0 alex-shishkin (323389) dpt_yandex_infra_tech_ytdev_dep8 (246647)       38 2023-04-06 08:54:06.000000 ytsaurus-spyt-1.69.1b439.post23515129.dev9/setup.cfg
```

### Comparing `ytsaurus-spyt-1.69.1b439.post23515129.dev5/deps/bin/spark-discovery-yt` & `ytsaurus-spyt-1.69.1b439.post23515129.dev9/deps/bin/spark-discovery-yt`

 * *Files identical despite different names*

### Comparing `ytsaurus-spyt-1.69.1b439.post23515129.dev5/deps/bin/spark-launch-yt` & `ytsaurus-spyt-1.69.1b439.post23515129.dev9/deps/bin/spark-launch-yt`

 * *Files identical despite different names*

### Comparing `ytsaurus-spyt-1.69.1b439.post23515129.dev5/deps/bin/spark-manage-yt` & `ytsaurus-spyt-1.69.1b439.post23515129.dev9/deps/bin/spark-manage-yt`

 * *Files identical despite different names*

### Comparing `ytsaurus-spyt-1.69.1b439.post23515129.dev5/deps/bin/spark-shell-yt` & `ytsaurus-spyt-1.69.1b439.post23515129.dev9/deps/bin/spark-shell-yt`

 * *Files identical despite different names*

### Comparing `ytsaurus-spyt-1.69.1b439.post23515129.dev5/deps/bin/spark-submit-yt` & `ytsaurus-spyt-1.69.1b439.post23515129.dev9/deps/bin/spark-submit-yt`

 * *Files identical despite different names*

### Comparing `ytsaurus-spyt-1.69.1b439.post23515129.dev5/deps/jars/spark-yt-submit.jar` & `ytsaurus-spyt-1.69.1b439.post23515129.dev9/deps/jars/spark-yt-submit.jar`

 * *Files identical despite different names*

### Comparing `ytsaurus-spyt-1.69.1b439.post23515129.dev5/spyt/client.py` & `ytsaurus-spyt-1.69.1b439.post23515129.dev9/spyt/client.py`

 * *Files identical despite different names*

### Comparing `ytsaurus-spyt-1.69.1b439.post23515129.dev5/spyt/common.py` & `ytsaurus-spyt-1.69.1b439.post23515129.dev9/spyt/common.py`

 * *Files identical despite different names*

### Comparing `ytsaurus-spyt-1.69.1b439.post23515129.dev5/spyt/conf.py` & `ytsaurus-spyt-1.69.1b439.post23515129.dev9/spyt/conf.py`

 * *Files identical despite different names*

### Comparing `ytsaurus-spyt-1.69.1b439.post23515129.dev5/spyt/enabler.py` & `ytsaurus-spyt-1.69.1b439.post23515129.dev9/spyt/enabler.py`

 * *Files identical despite different names*

### Comparing `ytsaurus-spyt-1.69.1b439.post23515129.dev5/spyt/standalone.py` & `ytsaurus-spyt-1.69.1b439.post23515129.dev9/spyt/standalone.py`

 * *Files identical despite different names*

### Comparing `ytsaurus-spyt-1.69.1b439.post23515129.dev5/spyt/submit.py` & `ytsaurus-spyt-1.69.1b439.post23515129.dev9/spyt/submit.py`

 * *Files identical despite different names*

### Comparing `ytsaurus-spyt-1.69.1b439.post23515129.dev5/spyt/types.py` & `ytsaurus-spyt-1.69.1b439.post23515129.dev9/spyt/types.py`

 * *Files identical despite different names*

### Comparing `ytsaurus-spyt-1.69.1b439.post23515129.dev5/spyt/utils.py` & `ytsaurus-spyt-1.69.1b439.post23515129.dev9/spyt/utils.py`

 * *Files identical despite different names*

### Comparing `ytsaurus-spyt-1.69.1b439.post23515129.dev5/ytsaurus_spyt.egg-info/SOURCES.txt` & `ytsaurus-spyt-1.69.1b439.post23515129.dev9/ytsaurus_spyt.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `ytsaurus-spyt-1.69.1b439.post23515129.dev5/setup.py` & `ytsaurus-spyt-1.69.1b439.post23515129.dev9/setup.py`

 * *Files identical despite different names*

