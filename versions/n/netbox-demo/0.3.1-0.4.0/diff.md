# Comparing `tmp/netbox-demo-0.3.1.tar.gz` & `tmp/netbox-demo-0.4.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "/home/jstretch/projects/netbox-demo/dist/tmpndsnssc_/netbox-demo-0.3.1.tar", last modified: Wed Aug 17 17:35:23 2022, max compression
+gzip compressed data, was "netbox-demo-0.4.0.tar", last modified: Thu Apr  6 14:31:42 2023, max compression
```

## Comparing `netbox-demo-0.3.1.tar` & `netbox-demo-0.4.0.tar`

### file list

```diff
@@ -1,16 +1,22 @@
-drwxrwxr-x   0 jstretch  (1000) jstretch  (1000)        0 2022-08-17 17:35:23.000000 netbox-demo-0.3.1/
-drwxrwxr-x   0 jstretch  (1000) jstretch  (1000)        0 2022-08-17 17:35:23.000000 netbox-demo-0.3.1/netbox_demo.egg-info/
--rw-rw-r--   0 jstretch  (1000) jstretch  (1000)        1 2022-08-17 17:35:23.000000 netbox-demo-0.3.1/netbox_demo.egg-info/dependency_links.txt
--rw-rw-r--   0 jstretch  (1000) jstretch  (1000)      266 2022-08-17 17:35:23.000000 netbox-demo-0.3.1/netbox_demo.egg-info/SOURCES.txt
--rw-rw-r--   0 jstretch  (1000) jstretch  (1000)       12 2022-08-17 17:35:23.000000 netbox-demo-0.3.1/netbox_demo.egg-info/top_level.txt
--rw-rw-r--   0 jstretch  (1000) jstretch  (1000)      272 2022-08-17 17:35:23.000000 netbox-demo-0.3.1/netbox_demo.egg-info/PKG-INFO
--rw-rw-r--   0 jstretch  (1000) jstretch  (1000)        1 2021-12-07 19:19:47.000000 netbox-demo-0.3.1/netbox_demo.egg-info/not-zip-safe
--rw-rw-r--   0 jstretch  (1000) jstretch  (1000)      390 2022-08-17 17:25:31.000000 netbox-demo-0.3.1/setup.py
--rw-rw-r--   0 jstretch  (1000) jstretch  (1000)       38 2022-08-17 17:35:23.000000 netbox-demo-0.3.1/setup.cfg
-drwxrwxr-x   0 jstretch  (1000) jstretch  (1000)        0 2022-08-17 17:35:23.000000 netbox-demo-0.3.1/netbox_demo/
--rw-rw-r--   0 jstretch  (1000) jstretch  (1000)      348 2022-08-17 17:25:20.000000 netbox-demo-0.3.1/netbox_demo/__init__.py
--rw-rw-r--   0 jstretch  (1000) jstretch  (1000)      980 2022-08-17 17:06:46.000000 netbox-demo-0.3.1/netbox_demo/signals.py
--rw-rw-r--   0 jstretch  (1000) jstretch  (1000)    10174 2021-12-07 19:17:36.000000 netbox-demo-0.3.1/LICENSE.txt
--rw-rw-r--   0 jstretch  (1000) jstretch  (1000)      272 2022-08-17 17:35:23.000000 netbox-demo-0.3.1/PKG-INFO
--rw-rw-r--   0 jstretch  (1000) jstretch  (1000)      277 2022-08-17 17:07:41.000000 netbox-demo-0.3.1/README.md
--rw-rw-r--   0 jstretch  (1000) jstretch  (1000)      104 2021-12-07 19:36:49.000000 netbox-demo-0.3.1/pyproject.toml
+drwxrwxr-x   0 jstretch  (1000) jstretch  (1000)        0 2023-04-06 14:31:42.882149 netbox-demo-0.4.0/
+-rw-rw-r--   0 jstretch  (1000) jstretch  (1000)    10174 2021-12-07 19:17:36.000000 netbox-demo-0.4.0/LICENSE.txt
+-rw-rw-r--   0 jstretch  (1000) jstretch  (1000)       47 2023-04-06 14:23:25.000000 netbox-demo-0.4.0/MANIFEST.in
+-rw-rw-r--   0 jstretch  (1000) jstretch  (1000)    12413 2023-04-06 14:31:42.882149 netbox-demo-0.4.0/PKG-INFO
+-rw-rw-r--   0 jstretch  (1000) jstretch  (1000)      624 2023-04-05 21:09:06.000000 netbox-demo-0.4.0/README.md
+drwxrwxr-x   0 jstretch  (1000) jstretch  (1000)        0 2023-04-06 14:31:42.882149 netbox-demo-0.4.0/netbox_demo/
+-rw-rw-r--   0 jstretch  (1000) jstretch  (1000)      370 2023-04-05 19:08:02.000000 netbox-demo-0.4.0/netbox_demo/__init__.py
+-rw-rw-r--   0 jstretch  (1000) jstretch  (1000)      447 2023-04-05 20:53:24.000000 netbox-demo-0.4.0/netbox_demo/forms.py
+-rw-rw-r--   0 jstretch  (1000) jstretch  (1000)      980 2022-08-17 17:06:46.000000 netbox-demo-0.4.0/netbox_demo/signals.py
+drwxrwxr-x   0 jstretch  (1000) jstretch  (1000)        0 2023-04-06 14:31:42.882149 netbox-demo-0.4.0/netbox_demo/templates/
+drwxrwxr-x   0 jstretch  (1000) jstretch  (1000)        0 2023-04-06 14:31:42.882149 netbox-demo-0.4.0/netbox_demo/templates/netbox_demo/
+-rw-rw-r--   0 jstretch  (1000) jstretch  (1000)      883 2023-04-05 21:00:49.000000 netbox-demo-0.4.0/netbox_demo/templates/netbox_demo/login.html
+-rw-rw-r--   0 jstretch  (1000) jstretch  (1000)      134 2023-04-05 20:45:57.000000 netbox-demo-0.4.0/netbox_demo/urls.py
+-rw-rw-r--   0 jstretch  (1000) jstretch  (1000)      822 2023-04-05 20:04:07.000000 netbox-demo-0.4.0/netbox_demo/utils.py
+-rw-rw-r--   0 jstretch  (1000) jstretch  (1000)     1152 2023-04-05 20:58:45.000000 netbox-demo-0.4.0/netbox_demo/views.py
+drwxrwxr-x   0 jstretch  (1000) jstretch  (1000)        0 2023-04-06 14:31:42.882149 netbox-demo-0.4.0/netbox_demo.egg-info/
+-rw-rw-r--   0 jstretch  (1000) jstretch  (1000)    12413 2023-04-06 14:31:42.000000 netbox-demo-0.4.0/netbox_demo.egg-info/PKG-INFO
+-rw-rw-r--   0 jstretch  (1000) jstretch  (1000)      363 2023-04-06 14:31:42.000000 netbox-demo-0.4.0/netbox_demo.egg-info/SOURCES.txt
+-rw-rw-r--   0 jstretch  (1000) jstretch  (1000)        1 2023-04-06 14:31:42.000000 netbox-demo-0.4.0/netbox_demo.egg-info/dependency_links.txt
+-rw-rw-r--   0 jstretch  (1000) jstretch  (1000)       12 2023-04-06 14:31:42.000000 netbox-demo-0.4.0/netbox_demo.egg-info/top_level.txt
+-rw-rw-r--   0 jstretch  (1000) jstretch  (1000)      284 2023-04-06 14:18:44.000000 netbox-demo-0.4.0/pyproject.toml
+-rw-rw-r--   0 jstretch  (1000) jstretch  (1000)       38 2023-04-06 14:31:42.882149 netbox-demo-0.4.0/setup.cfg
```

### filetype from file(1)

```diff
@@ -1 +1 @@
-POSIX tar archive (GNU)
+POSIX tar archive
```

### Comparing `netbox-demo-0.3.1/netbox_demo/signals.py` & `netbox-demo-0.4.0/netbox_demo/signals.py`

 * *Files identical despite different names*

### Comparing `netbox-demo-0.3.1/LICENSE.txt` & `netbox-demo-0.4.0/LICENSE.txt`

 * *Files identical despite different names*

