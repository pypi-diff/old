# Comparing `tmp/jupyterlab_nbgallery-2.0.0a3.tar.gz` & `tmp/jupyterlab_nbgallery-2.0.0a4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "jupyterlab_nbgallery-2.0.0a3.tar", last modified: Fri Apr  7 13:28:16 2023, max compression
+gzip compressed data, was "jupyterlab_nbgallery-2.0.0a4.tar", last modified: Fri Apr  7 14:55:54 2023, max compression
```

## Comparing `jupyterlab_nbgallery-2.0.0a3.tar` & `jupyterlab_nbgallery-2.0.0a4.tar`

### file list

```diff
@@ -1,119 +1,119 @@
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.733590 jupyterlab_nbgallery-2.0.0a3/
--rw-r--r--   0 jovyan    (1000) users      (100)     1066 2023-04-07 13:26:25.000000 jupyterlab_nbgallery-2.0.0a3/LICENSE
--rw-r--r--   0 jovyan    (1000) users      (100)      388 2023-04-07 13:26:25.000000 jupyterlab_nbgallery-2.0.0a3/MANIFEST.in
--rw-r--r--   0 jovyan    (1000) users      (100)     2694 2023-04-07 13:28:16.733590 jupyterlab_nbgallery-2.0.0a3/PKG-INFO
--rw-r--r--   0 jovyan    (1000) users      (100)     2014 2023-04-07 13:26:25.000000 jupyterlab_nbgallery-2.0.0a3/README.md
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.717589 jupyterlab_nbgallery-2.0.0a3/jupyter-config/
--rw-r--r--   0 jovyan    (1000) users      (100)       96 2023-04-07 13:26:25.000000 jupyterlab_nbgallery-2.0.0a3/jupyter-config/jupyterlab_nbgallery.json
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.717589 jupyterlab_nbgallery-2.0.0a3/jupyterlab_nbgallery/
--rw-r--r--   0 jovyan    (1000) users      (100)      596 2023-04-07 13:26:25.000000 jupyterlab_nbgallery-2.0.0a3/jupyterlab_nbgallery/__init__.py
--rw-r--r--   0 jovyan    (1000) users      (100)       76 2023-04-07 13:26:25.000000 jupyterlab_nbgallery-2.0.0a3/jupyterlab_nbgallery/_version.py
--rw-r--r--   0 jovyan    (1000) users      (100)     3640 2023-04-07 13:26:25.000000 jupyterlab_nbgallery-2.0.0a3/jupyterlab_nbgallery/handlers.py
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.717589 jupyterlab_nbgallery-2.0.0a3/jupyterlab_nbgallery.egg-info/
--rw-r--r--   0 jovyan    (1000) users      (100)     2694 2023-04-07 13:28:16.000000 jupyterlab_nbgallery-2.0.0a3/jupyterlab_nbgallery.egg-info/PKG-INFO
--rw-r--r--   0 jovyan    (1000) users      (100)     4503 2023-04-07 13:28:16.000000 jupyterlab_nbgallery-2.0.0a3/jupyterlab_nbgallery.egg-info/SOURCES.txt
--rw-r--r--   0 jovyan    (1000) users      (100)        1 2023-04-07 13:28:16.000000 jupyterlab_nbgallery-2.0.0a3/jupyterlab_nbgallery.egg-info/dependency_links.txt
--rw-r--r--   0 jovyan    (1000) users      (100)        1 2023-04-07 09:29:38.000000 jupyterlab_nbgallery-2.0.0a3/jupyterlab_nbgallery.egg-info/not-zip-safe
--rw-r--r--   0 jovyan    (1000) users      (100)       61 2023-04-07 13:28:16.000000 jupyterlab_nbgallery-2.0.0a3/jupyterlab_nbgallery.egg-info/requires.txt
--rw-r--r--   0 jovyan    (1000) users      (100)       21 2023-04-07 13:28:16.000000 jupyterlab_nbgallery-2.0.0a3/jupyterlab_nbgallery.egg-info/top_level.txt
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.713590 jupyterlab_nbgallery-2.0.0a3/labextension/
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.717589 jupyterlab_nbgallery-2.0.0a3/labextension/autodownload/
--rw-r--r--   0 jovyan    (1000) users      (100)     2596 2023-04-07 13:27:45.000000 jupyterlab_nbgallery-2.0.0a3/labextension/autodownload/package.json
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.709589 jupyterlab_nbgallery-2.0.0a3/labextension/autodownload/schemas/
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.709589 jupyterlab_nbgallery-2.0.0a3/labextension/autodownload/schemas/@jupyterlab-nbgallery/
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.717589 jupyterlab_nbgallery-2.0.0a3/labextension/autodownload/schemas/@jupyterlab-nbgallery/autodownload/
--rw-r--r--   0 jovyan    (1000) users      (100)      335 2023-04-07 13:27:36.000000 jupyterlab_nbgallery-2.0.0a3/labextension/autodownload/schemas/@jupyterlab-nbgallery/autodownload/autodownload.json
--rw-r--r--   0 jovyan    (1000) users      (100)     2505 2023-04-07 13:27:36.000000 jupyterlab_nbgallery-2.0.0a3/labextension/autodownload/schemas/@jupyterlab-nbgallery/autodownload/package.json.orig
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.721589 jupyterlab_nbgallery-2.0.0a3/labextension/autodownload/static/
--rw-r--r--   0 jovyan    (1000) users      (100)     3438 2023-04-07 13:27:45.000000 jupyterlab_nbgallery-2.0.0a3/labextension/autodownload/static/542.51fb91347d8a3d9a657a.js
--rw-r--r--   0 jovyan    (1000) users      (100)     1968 2023-04-07 13:27:45.000000 jupyterlab_nbgallery-2.0.0a3/labextension/autodownload/static/568.088b227a0b6b6168ee16.js
--rw-r--r--   0 jovyan    (1000) users      (100)    90038 2023-04-07 13:27:45.000000 jupyterlab_nbgallery-2.0.0a3/labextension/autodownload/static/638.0ed295d9378dea7c5c7b.js
--rw-r--r--   0 jovyan    (1000) users      (100)      476 2023-04-07 13:27:45.000000 jupyterlab_nbgallery-2.0.0a3/labextension/autodownload/static/638.0ed295d9378dea7c5c7b.js.LICENSE.txt
--rw-r--r--   0 jovyan    (1000) users      (100)     6914 2023-04-07 13:27:45.000000 jupyterlab_nbgallery-2.0.0a3/labextension/autodownload/static/remoteEntry.fa15592bca73423b04a4.js
--rw-r--r--   0 jovyan    (1000) users      (100)      178 2023-04-07 13:27:36.000000 jupyterlab_nbgallery-2.0.0a3/labextension/autodownload/static/style.js
--rw-r--r--   0 jovyan    (1000) users      (100)     3692 2023-04-07 13:27:45.000000 jupyterlab_nbgallery-2.0.0a3/labextension/autodownload/static/third-party-licenses.json
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.721589 jupyterlab_nbgallery-2.0.0a3/labextension/environment-life/
--rw-r--r--   0 jovyan    (1000) users      (100)     2618 2023-04-07 13:27:40.000000 jupyterlab_nbgallery-2.0.0a3/labextension/environment-life/package.json
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.709589 jupyterlab_nbgallery-2.0.0a3/labextension/environment-life/schemas/
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.709589 jupyterlab_nbgallery-2.0.0a3/labextension/environment-life/schemas/@jupyterlab-nbgallery/
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.721589 jupyterlab_nbgallery-2.0.0a3/labextension/environment-life/schemas/@jupyterlab-nbgallery/environment-life/
--rw-r--r--   0 jovyan    (1000) users      (100)     2527 2023-04-07 13:27:37.000000 jupyterlab_nbgallery-2.0.0a3/labextension/environment-life/schemas/@jupyterlab-nbgallery/environment-life/package.json.orig
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.721589 jupyterlab_nbgallery-2.0.0a3/labextension/environment-life/static/
--rw-r--r--   0 jovyan    (1000) users      (100)     1213 2023-04-07 13:27:40.000000 jupyterlab_nbgallery-2.0.0a3/labextension/environment-life/static/248.1d3351413b89920be9fb.js
--rw-r--r--   0 jovyan    (1000) users      (100)     3446 2023-04-07 13:27:40.000000 jupyterlab_nbgallery-2.0.0a3/labextension/environment-life/static/542.e4d405f3b0e4f693ab53.js
--rw-r--r--   0 jovyan    (1000) users      (100)     6651 2023-04-07 13:27:40.000000 jupyterlab_nbgallery-2.0.0a3/labextension/environment-life/static/remoteEntry.dd7691336809bc6771e3.js
--rw-r--r--   0 jovyan    (1000) users      (100)      182 2023-04-07 13:27:37.000000 jupyterlab_nbgallery-2.0.0a3/labextension/environment-life/static/style.js
--rw-r--r--   0 jovyan    (1000) users      (100)     2452 2023-04-07 13:27:40.000000 jupyterlab_nbgallery-2.0.0a3/labextension/environment-life/static/third-party-licenses.json
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.721589 jupyterlab_nbgallery-2.0.0a3/labextension/environment-registration/
--rw-r--r--   0 jovyan    (1000) users      (100)     2579 2023-04-07 13:27:44.000000 jupyterlab_nbgallery-2.0.0a3/labextension/environment-registration/package.json
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.709589 jupyterlab_nbgallery-2.0.0a3/labextension/environment-registration/schemas/
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.713590 jupyterlab_nbgallery-2.0.0a3/labextension/environment-registration/schemas/@jupyterlab-nbgallery/
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.721589 jupyterlab_nbgallery-2.0.0a3/labextension/environment-registration/schemas/@jupyterlab-nbgallery/environment-registration/
--rw-r--r--   0 jovyan    (1000) users      (100)      680 2023-04-07 13:27:36.000000 jupyterlab_nbgallery-2.0.0a3/labextension/environment-registration/schemas/@jupyterlab-nbgallery/environment-registration/environment-registration.json
--rw-r--r--   0 jovyan    (1000) users      (100)     2488 2023-04-07 13:27:36.000000 jupyterlab_nbgallery-2.0.0a3/labextension/environment-registration/schemas/@jupyterlab-nbgallery/environment-registration/package.json.orig
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.725589 jupyterlab_nbgallery-2.0.0a3/labextension/environment-registration/static/
--rw-r--r--   0 jovyan    (1000) users      (100)     3460 2023-04-07 13:27:44.000000 jupyterlab_nbgallery-2.0.0a3/labextension/environment-registration/static/542.feae6c397f33f9138fea.js
--rw-r--r--   0 jovyan    (1000) users      (100)    90062 2023-04-07 13:27:44.000000 jupyterlab_nbgallery-2.0.0a3/labextension/environment-registration/static/638.36e464d3233849b6b07a.js
--rw-r--r--   0 jovyan    (1000) users      (100)      476 2023-04-07 13:27:44.000000 jupyterlab_nbgallery-2.0.0a3/labextension/environment-registration/static/638.36e464d3233849b6b07a.js.LICENSE.txt
--rw-r--r--   0 jovyan    (1000) users      (100)     1519 2023-04-07 13:27:44.000000 jupyterlab_nbgallery-2.0.0a3/labextension/environment-registration/static/784.c5c708b87c266cbabd98.js
--rw-r--r--   0 jovyan    (1000) users      (100)     7044 2023-04-07 13:27:44.000000 jupyterlab_nbgallery-2.0.0a3/labextension/environment-registration/static/remoteEntry.00e0256ee314fd224ea3.js
--rw-r--r--   0 jovyan    (1000) users      (100)      190 2023-04-07 13:27:36.000000 jupyterlab_nbgallery-2.0.0a3/labextension/environment-registration/static/style.js
--rw-r--r--   0 jovyan    (1000) users      (100)     3692 2023-04-07 13:27:44.000000 jupyterlab_nbgallery-2.0.0a3/labextension/environment-registration/static/third-party-licenses.json
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.725589 jupyterlab_nbgallery-2.0.0a3/labextension/gallerymenu/
--rw-r--r--   0 jovyan    (1000) users      (100)     2698 2023-04-07 13:27:47.000000 jupyterlab_nbgallery-2.0.0a3/labextension/gallerymenu/package.json
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.713590 jupyterlab_nbgallery-2.0.0a3/labextension/gallerymenu/schemas/
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.713590 jupyterlab_nbgallery-2.0.0a3/labextension/gallerymenu/schemas/@jupyterlab-nbgallery/
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.725589 jupyterlab_nbgallery-2.0.0a3/labextension/gallerymenu/schemas/@jupyterlab-nbgallery/gallerymenu/
--rw-r--r--   0 jovyan    (1000) users      (100)     2607 2023-04-07 13:27:38.000000 jupyterlab_nbgallery-2.0.0a3/labextension/gallerymenu/schemas/@jupyterlab-nbgallery/gallerymenu/package.json.orig
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.725589 jupyterlab_nbgallery-2.0.0a3/labextension/gallerymenu/static/
--rw-r--r--   0 jovyan    (1000) users      (100)     4018 2023-04-07 13:27:47.000000 jupyterlab_nbgallery-2.0.0a3/labextension/gallerymenu/static/542.18fd91d86aaf6286edd0.js
--rw-r--r--   0 jovyan    (1000) users      (100)    10492 2023-04-07 13:27:47.000000 jupyterlab_nbgallery-2.0.0a3/labextension/gallerymenu/static/56.00b49e0c37b3050cbc14.js
--rw-r--r--   0 jovyan    (1000) users      (100)    90036 2023-04-07 13:27:47.000000 jupyterlab_nbgallery-2.0.0a3/labextension/gallerymenu/static/638.95e0186307171588df5b.js
--rw-r--r--   0 jovyan    (1000) users      (100)      476 2023-04-07 13:27:47.000000 jupyterlab_nbgallery-2.0.0a3/labextension/gallerymenu/static/638.95e0186307171588df5b.js.LICENSE.txt
--rw-r--r--   0 jovyan    (1000) users      (100)     7164 2023-04-07 13:27:47.000000 jupyterlab_nbgallery-2.0.0a3/labextension/gallerymenu/static/remoteEntry.ae9dddbb4a23b1552c19.js
--rw-r--r--   0 jovyan    (1000) users      (100)      177 2023-04-07 13:27:38.000000 jupyterlab_nbgallery-2.0.0a3/labextension/gallerymenu/static/style.js
--rw-r--r--   0 jovyan    (1000) users      (100)     3692 2023-04-07 13:27:47.000000 jupyterlab_nbgallery-2.0.0a3/labextension/gallerymenu/static/third-party-licenses.json
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.725589 jupyterlab_nbgallery-2.0.0a3/labextension/inject-uuid/
--rw-r--r--   0 jovyan    (1000) users      (100)     2444 2023-04-07 13:28:08.000000 jupyterlab_nbgallery-2.0.0a3/labextension/inject-uuid/package.json
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.713590 jupyterlab_nbgallery-2.0.0a3/labextension/inject-uuid/schemas/
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.713590 jupyterlab_nbgallery-2.0.0a3/labextension/inject-uuid/schemas/@jupyterlab-nbgallery/
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.725589 jupyterlab_nbgallery-2.0.0a3/labextension/inject-uuid/schemas/@jupyterlab-nbgallery/inject-uuid/
--rw-r--r--   0 jovyan    (1000) users      (100)     2379 2023-04-07 13:28:06.000000 jupyterlab_nbgallery-2.0.0a3/labextension/inject-uuid/schemas/@jupyterlab-nbgallery/inject-uuid/package.json.orig
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.729589 jupyterlab_nbgallery-2.0.0a3/labextension/inject-uuid/static/
--rw-r--r--   0 jovyan    (1000) users      (100)      931 2023-04-07 13:28:08.000000 jupyterlab_nbgallery-2.0.0a3/labextension/inject-uuid/static/568.1dcbb7bee8ca1152cf60.js
--rw-r--r--   0 jovyan    (1000) users      (100)     6305 2023-04-07 13:28:08.000000 jupyterlab_nbgallery-2.0.0a3/labextension/inject-uuid/static/remoteEntry.02ddda09f0305fa467f4.js
--rw-r--r--   0 jovyan    (1000) users      (100)      118 2023-04-07 13:28:06.000000 jupyterlab_nbgallery-2.0.0a3/labextension/inject-uuid/static/style.js
--rw-r--r--   0 jovyan    (1000) users      (100)       20 2023-04-07 13:28:08.000000 jupyterlab_nbgallery-2.0.0a3/labextension/inject-uuid/static/third-party-licenses.json
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.729589 jupyterlab_nbgallery-2.0.0a3/labextension/instrumentation/
--rw-r--r--   0 jovyan    (1000) users      (100)     2527 2023-04-07 13:28:16.000000 jupyterlab_nbgallery-2.0.0a3/labextension/instrumentation/package.json
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.713590 jupyterlab_nbgallery-2.0.0a3/labextension/instrumentation/schemas/
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.713590 jupyterlab_nbgallery-2.0.0a3/labextension/instrumentation/schemas/@jupyterlab-nbgallery/
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.729589 jupyterlab_nbgallery-2.0.0a3/labextension/instrumentation/schemas/@jupyterlab-nbgallery/instrumentation/
--rw-r--r--   0 jovyan    (1000) users      (100)      345 2023-04-07 13:28:10.000000 jupyterlab_nbgallery-2.0.0a3/labextension/instrumentation/schemas/@jupyterlab-nbgallery/instrumentation/instrumentation.json
--rw-r--r--   0 jovyan    (1000) users      (100)     2466 2023-04-07 13:28:10.000000 jupyterlab_nbgallery-2.0.0a3/labextension/instrumentation/schemas/@jupyterlab-nbgallery/instrumentation/package.json.orig
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.729589 jupyterlab_nbgallery-2.0.0a3/labextension/instrumentation/static/
--rw-r--r--   0 jovyan    (1000) users      (100)     1720 2023-04-07 13:28:16.000000 jupyterlab_nbgallery-2.0.0a3/labextension/instrumentation/static/568.0d3998aabd22f1867c40.js
--rw-r--r--   0 jovyan    (1000) users      (100)    90044 2023-04-07 13:28:16.000000 jupyterlab_nbgallery-2.0.0a3/labextension/instrumentation/static/638.b95125ed695cee42aae4.js
--rw-r--r--   0 jovyan    (1000) users      (100)      476 2023-04-07 13:28:16.000000 jupyterlab_nbgallery-2.0.0a3/labextension/instrumentation/static/638.b95125ed695cee42aae4.js.LICENSE.txt
--rw-r--r--   0 jovyan    (1000) users      (100)     8425 2023-04-07 13:28:16.000000 jupyterlab_nbgallery-2.0.0a3/labextension/instrumentation/static/701.d81800f5926ab62cc8b2.js
--rw-r--r--   0 jovyan    (1000) users      (100)     7555 2023-04-07 13:28:16.000000 jupyterlab_nbgallery-2.0.0a3/labextension/instrumentation/static/remoteEntry.53ed33a8ef1f603e0fc8.js
--rw-r--r--   0 jovyan    (1000) users      (100)      118 2023-04-07 13:28:10.000000 jupyterlab_nbgallery-2.0.0a3/labextension/instrumentation/static/style.js
--rw-r--r--   0 jovyan    (1000) users      (100)     2479 2023-04-07 13:28:16.000000 jupyterlab_nbgallery-2.0.0a3/labextension/instrumentation/static/third-party-licenses.json
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.729589 jupyterlab_nbgallery-2.0.0a3/labextension/userpreferences/
--rw-r--r--   0 jovyan    (1000) users      (100)     2709 2023-04-07 13:28:15.000000 jupyterlab_nbgallery-2.0.0a3/labextension/userpreferences/package.json
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.713590 jupyterlab_nbgallery-2.0.0a3/labextension/userpreferences/schemas/
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.713590 jupyterlab_nbgallery-2.0.0a3/labextension/userpreferences/schemas/@jupyterlab-nbgallery/
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.729589 jupyterlab_nbgallery-2.0.0a3/labextension/userpreferences/schemas/@jupyterlab-nbgallery/userpreferences/
--rw-r--r--   0 jovyan    (1000) users      (100)     2618 2023-04-07 13:28:10.000000 jupyterlab_nbgallery-2.0.0a3/labextension/userpreferences/schemas/@jupyterlab-nbgallery/userpreferences/package.json.orig
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.733590 jupyterlab_nbgallery-2.0.0a3/labextension/userpreferences/static/
--rw-r--r--   0 jovyan    (1000) users      (100)     4026 2023-04-07 13:28:15.000000 jupyterlab_nbgallery-2.0.0a3/labextension/userpreferences/static/542.d1718a50e23f3808ba62.js
--rw-r--r--   0 jovyan    (1000) users      (100)     4114 2023-04-07 13:28:15.000000 jupyterlab_nbgallery-2.0.0a3/labextension/userpreferences/static/568.00695541aaa15d567580.js
--rw-r--r--   0 jovyan    (1000) users      (100)    90044 2023-04-07 13:28:15.000000 jupyterlab_nbgallery-2.0.0a3/labextension/userpreferences/static/638.e5080f99954048969f76.js
--rw-r--r--   0 jovyan    (1000) users      (100)      476 2023-04-07 13:28:15.000000 jupyterlab_nbgallery-2.0.0a3/labextension/userpreferences/static/638.e5080f99954048969f76.js.LICENSE.txt
--rw-r--r--   0 jovyan    (1000) users      (100)     7095 2023-04-07 13:28:15.000000 jupyterlab_nbgallery-2.0.0a3/labextension/userpreferences/static/remoteEntry.03bf745401d2317e1d7d.js
--rw-r--r--   0 jovyan    (1000) users      (100)      181 2023-04-07 13:28:10.000000 jupyterlab_nbgallery-2.0.0a3/labextension/userpreferences/static/style.js
--rw-r--r--   0 jovyan    (1000) users      (100)     3692 2023-04-07 13:28:15.000000 jupyterlab_nbgallery-2.0.0a3/labextension/userpreferences/static/third-party-licenses.json
--rw-r--r--   0 jovyan    (1000) users      (100)     1103 2023-04-07 13:26:25.000000 jupyterlab_nbgallery-2.0.0a3/package.json
--rw-r--r--   0 jovyan    (1000) users      (100)      145 2023-04-07 13:26:25.000000 jupyterlab_nbgallery-2.0.0a3/pyproject.toml
--rw-r--r--   0 jovyan    (1000) users      (100)       38 2023-04-07 13:28:16.733590 jupyterlab_nbgallery-2.0.0a3/setup.cfg
--rw-r--r--   0 jovyan    (1000) users      (100)     3928 2023-04-07 13:26:25.000000 jupyterlab_nbgallery-2.0.0a3/setup.py
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 14:55:54.357939 jupyterlab_nbgallery-2.0.0a4/
+-rw-r--r--   0 jovyan    (1000) users      (100)     1066 2023-04-07 14:52:37.000000 jupyterlab_nbgallery-2.0.0a4/LICENSE
+-rw-r--r--   0 jovyan    (1000) users      (100)      388 2023-04-07 14:52:37.000000 jupyterlab_nbgallery-2.0.0a4/MANIFEST.in
+-rw-r--r--   0 jovyan    (1000) users      (100)     2694 2023-04-07 14:55:54.357939 jupyterlab_nbgallery-2.0.0a4/PKG-INFO
+-rw-r--r--   0 jovyan    (1000) users      (100)     2014 2023-04-07 14:52:37.000000 jupyterlab_nbgallery-2.0.0a4/README.md
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 14:55:54.341940 jupyterlab_nbgallery-2.0.0a4/jupyter-config/
+-rw-r--r--   0 jovyan    (1000) users      (100)       96 2023-04-07 14:52:37.000000 jupyterlab_nbgallery-2.0.0a4/jupyter-config/jupyterlab_nbgallery.json
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 14:55:54.341940 jupyterlab_nbgallery-2.0.0a4/jupyterlab_nbgallery/
+-rw-r--r--   0 jovyan    (1000) users      (100)      596 2023-04-07 14:52:37.000000 jupyterlab_nbgallery-2.0.0a4/jupyterlab_nbgallery/__init__.py
+-rw-r--r--   0 jovyan    (1000) users      (100)       76 2023-04-07 14:52:37.000000 jupyterlab_nbgallery-2.0.0a4/jupyterlab_nbgallery/_version.py
+-rw-r--r--   0 jovyan    (1000) users      (100)     3640 2023-04-07 14:52:37.000000 jupyterlab_nbgallery-2.0.0a4/jupyterlab_nbgallery/handlers.py
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 14:55:54.341940 jupyterlab_nbgallery-2.0.0a4/jupyterlab_nbgallery.egg-info/
+-rw-r--r--   0 jovyan    (1000) users      (100)     2694 2023-04-07 14:55:54.000000 jupyterlab_nbgallery-2.0.0a4/jupyterlab_nbgallery.egg-info/PKG-INFO
+-rw-r--r--   0 jovyan    (1000) users      (100)     4503 2023-04-07 14:55:54.000000 jupyterlab_nbgallery-2.0.0a4/jupyterlab_nbgallery.egg-info/SOURCES.txt
+-rw-r--r--   0 jovyan    (1000) users      (100)        1 2023-04-07 14:55:54.000000 jupyterlab_nbgallery-2.0.0a4/jupyterlab_nbgallery.egg-info/dependency_links.txt
+-rw-r--r--   0 jovyan    (1000) users      (100)        1 2023-04-07 14:46:08.000000 jupyterlab_nbgallery-2.0.0a4/jupyterlab_nbgallery.egg-info/not-zip-safe
+-rw-r--r--   0 jovyan    (1000) users      (100)       61 2023-04-07 14:55:54.000000 jupyterlab_nbgallery-2.0.0a4/jupyterlab_nbgallery.egg-info/requires.txt
+-rw-r--r--   0 jovyan    (1000) users      (100)       21 2023-04-07 14:55:54.000000 jupyterlab_nbgallery-2.0.0a4/jupyterlab_nbgallery.egg-info/top_level.txt
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 14:55:54.337939 jupyterlab_nbgallery-2.0.0a4/labextension/
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 14:55:54.341940 jupyterlab_nbgallery-2.0.0a4/labextension/autodownload/
+-rw-r--r--   0 jovyan    (1000) users      (100)     2596 2023-04-07 14:55:18.000000 jupyterlab_nbgallery-2.0.0a4/labextension/autodownload/package.json
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 14:55:54.333939 jupyterlab_nbgallery-2.0.0a4/labextension/autodownload/schemas/
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 14:55:54.333939 jupyterlab_nbgallery-2.0.0a4/labextension/autodownload/schemas/@jupyterlab-nbgallery/
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 14:55:54.341940 jupyterlab_nbgallery-2.0.0a4/labextension/autodownload/schemas/@jupyterlab-nbgallery/autodownload/
+-rw-r--r--   0 jovyan    (1000) users      (100)      335 2023-04-07 14:55:10.000000 jupyterlab_nbgallery-2.0.0a4/labextension/autodownload/schemas/@jupyterlab-nbgallery/autodownload/autodownload.json
+-rw-r--r--   0 jovyan    (1000) users      (100)     2454 2023-04-07 14:55:10.000000 jupyterlab_nbgallery-2.0.0a4/labextension/autodownload/schemas/@jupyterlab-nbgallery/autodownload/package.json.orig
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 14:55:54.345939 jupyterlab_nbgallery-2.0.0a4/labextension/autodownload/static/
+-rw-r--r--   0 jovyan    (1000) users      (100)     3438 2023-04-07 14:55:18.000000 jupyterlab_nbgallery-2.0.0a4/labextension/autodownload/static/542.51fb91347d8a3d9a657a.js
+-rw-r--r--   0 jovyan    (1000) users      (100)     1969 2023-04-07 14:55:18.000000 jupyterlab_nbgallery-2.0.0a4/labextension/autodownload/static/568.017b32a913356ad383e7.js
+-rw-r--r--   0 jovyan    (1000) users      (100)    90038 2023-04-07 14:55:18.000000 jupyterlab_nbgallery-2.0.0a4/labextension/autodownload/static/638.0ed295d9378dea7c5c7b.js
+-rw-r--r--   0 jovyan    (1000) users      (100)      476 2023-04-07 14:55:18.000000 jupyterlab_nbgallery-2.0.0a4/labextension/autodownload/static/638.0ed295d9378dea7c5c7b.js.LICENSE.txt
+-rw-r--r--   0 jovyan    (1000) users      (100)     6936 2023-04-07 14:55:18.000000 jupyterlab_nbgallery-2.0.0a4/labextension/autodownload/static/remoteEntry.1353121aacb4a50d2fe1.js
+-rw-r--r--   0 jovyan    (1000) users      (100)      178 2023-04-07 14:55:10.000000 jupyterlab_nbgallery-2.0.0a4/labextension/autodownload/static/style.js
+-rw-r--r--   0 jovyan    (1000) users      (100)     3692 2023-04-07 14:55:18.000000 jupyterlab_nbgallery-2.0.0a4/labextension/autodownload/static/third-party-licenses.json
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 14:55:54.345939 jupyterlab_nbgallery-2.0.0a4/labextension/environment-life/
+-rw-r--r--   0 jovyan    (1000) users      (100)     2618 2023-04-07 14:55:13.000000 jupyterlab_nbgallery-2.0.0a4/labextension/environment-life/package.json
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 14:55:54.333939 jupyterlab_nbgallery-2.0.0a4/labextension/environment-life/schemas/
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 14:55:54.333939 jupyterlab_nbgallery-2.0.0a4/labextension/environment-life/schemas/@jupyterlab-nbgallery/
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 14:55:54.345939 jupyterlab_nbgallery-2.0.0a4/labextension/environment-life/schemas/@jupyterlab-nbgallery/environment-life/
+-rw-r--r--   0 jovyan    (1000) users      (100)     2476 2023-04-07 14:55:09.000000 jupyterlab_nbgallery-2.0.0a4/labextension/environment-life/schemas/@jupyterlab-nbgallery/environment-life/package.json.orig
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 14:55:54.345939 jupyterlab_nbgallery-2.0.0a4/labextension/environment-life/static/
+-rw-r--r--   0 jovyan    (1000) users      (100)     1213 2023-04-07 14:55:12.000000 jupyterlab_nbgallery-2.0.0a4/labextension/environment-life/static/248.644879940d9faca2b389.js
+-rw-r--r--   0 jovyan    (1000) users      (100)     3446 2023-04-07 14:55:12.000000 jupyterlab_nbgallery-2.0.0a4/labextension/environment-life/static/542.e4d405f3b0e4f693ab53.js
+-rw-r--r--   0 jovyan    (1000) users      (100)     6680 2023-04-07 14:55:12.000000 jupyterlab_nbgallery-2.0.0a4/labextension/environment-life/static/remoteEntry.c977e6e35771b75265ee.js
+-rw-r--r--   0 jovyan    (1000) users      (100)      182 2023-04-07 14:55:09.000000 jupyterlab_nbgallery-2.0.0a4/labextension/environment-life/static/style.js
+-rw-r--r--   0 jovyan    (1000) users      (100)     2452 2023-04-07 14:55:12.000000 jupyterlab_nbgallery-2.0.0a4/labextension/environment-life/static/third-party-licenses.json
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 14:55:54.345939 jupyterlab_nbgallery-2.0.0a4/labextension/environment-registration/
+-rw-r--r--   0 jovyan    (1000) users      (100)     2579 2023-04-07 14:55:19.000000 jupyterlab_nbgallery-2.0.0a4/labextension/environment-registration/package.json
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 14:55:54.333939 jupyterlab_nbgallery-2.0.0a4/labextension/environment-registration/schemas/
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 14:55:54.333939 jupyterlab_nbgallery-2.0.0a4/labextension/environment-registration/schemas/@jupyterlab-nbgallery/
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 14:55:54.345939 jupyterlab_nbgallery-2.0.0a4/labextension/environment-registration/schemas/@jupyterlab-nbgallery/environment-registration/
+-rw-r--r--   0 jovyan    (1000) users      (100)      680 2023-04-07 14:55:10.000000 jupyterlab_nbgallery-2.0.0a4/labextension/environment-registration/schemas/@jupyterlab-nbgallery/environment-registration/environment-registration.json
+-rw-r--r--   0 jovyan    (1000) users      (100)     2437 2023-04-07 14:55:10.000000 jupyterlab_nbgallery-2.0.0a4/labextension/environment-registration/schemas/@jupyterlab-nbgallery/environment-registration/package.json.orig
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 14:55:54.349939 jupyterlab_nbgallery-2.0.0a4/labextension/environment-registration/static/
+-rw-r--r--   0 jovyan    (1000) users      (100)     3460 2023-04-07 14:55:19.000000 jupyterlab_nbgallery-2.0.0a4/labextension/environment-registration/static/542.feae6c397f33f9138fea.js
+-rw-r--r--   0 jovyan    (1000) users      (100)    90062 2023-04-07 14:55:19.000000 jupyterlab_nbgallery-2.0.0a4/labextension/environment-registration/static/638.36e464d3233849b6b07a.js
+-rw-r--r--   0 jovyan    (1000) users      (100)      476 2023-04-07 14:55:19.000000 jupyterlab_nbgallery-2.0.0a4/labextension/environment-registration/static/638.36e464d3233849b6b07a.js.LICENSE.txt
+-rw-r--r--   0 jovyan    (1000) users      (100)     1520 2023-04-07 14:55:19.000000 jupyterlab_nbgallery-2.0.0a4/labextension/environment-registration/static/784.f151a96d5dde1a095c86.js
+-rw-r--r--   0 jovyan    (1000) users      (100)     7076 2023-04-07 14:55:19.000000 jupyterlab_nbgallery-2.0.0a4/labextension/environment-registration/static/remoteEntry.5a586807c39202b9c488.js
+-rw-r--r--   0 jovyan    (1000) users      (100)      190 2023-04-07 14:55:10.000000 jupyterlab_nbgallery-2.0.0a4/labextension/environment-registration/static/style.js
+-rw-r--r--   0 jovyan    (1000) users      (100)     3692 2023-04-07 14:55:19.000000 jupyterlab_nbgallery-2.0.0a4/labextension/environment-registration/static/third-party-licenses.json
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 14:55:54.349939 jupyterlab_nbgallery-2.0.0a4/labextension/gallerymenu/
+-rw-r--r--   0 jovyan    (1000) users      (100)     2698 2023-04-07 14:55:19.000000 jupyterlab_nbgallery-2.0.0a4/labextension/gallerymenu/package.json
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 14:55:54.333939 jupyterlab_nbgallery-2.0.0a4/labextension/gallerymenu/schemas/
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 14:55:54.333939 jupyterlab_nbgallery-2.0.0a4/labextension/gallerymenu/schemas/@jupyterlab-nbgallery/
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 14:55:54.349939 jupyterlab_nbgallery-2.0.0a4/labextension/gallerymenu/schemas/@jupyterlab-nbgallery/gallerymenu/
+-rw-r--r--   0 jovyan    (1000) users      (100)     2556 2023-04-07 14:55:10.000000 jupyterlab_nbgallery-2.0.0a4/labextension/gallerymenu/schemas/@jupyterlab-nbgallery/gallerymenu/package.json.orig
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 14:55:54.349939 jupyterlab_nbgallery-2.0.0a4/labextension/gallerymenu/static/
+-rw-r--r--   0 jovyan    (1000) users      (100)     4018 2023-04-07 14:55:19.000000 jupyterlab_nbgallery-2.0.0a4/labextension/gallerymenu/static/542.18fd91d86aaf6286edd0.js
+-rw-r--r--   0 jovyan    (1000) users      (100)    10503 2023-04-07 14:55:19.000000 jupyterlab_nbgallery-2.0.0a4/labextension/gallerymenu/static/56.a4862cb4315ce0eea068.js
+-rw-r--r--   0 jovyan    (1000) users      (100)    90036 2023-04-07 14:55:19.000000 jupyterlab_nbgallery-2.0.0a4/labextension/gallerymenu/static/638.95e0186307171588df5b.js
+-rw-r--r--   0 jovyan    (1000) users      (100)      476 2023-04-07 14:55:19.000000 jupyterlab_nbgallery-2.0.0a4/labextension/gallerymenu/static/638.95e0186307171588df5b.js.LICENSE.txt
+-rw-r--r--   0 jovyan    (1000) users      (100)     7213 2023-04-07 14:55:19.000000 jupyterlab_nbgallery-2.0.0a4/labextension/gallerymenu/static/remoteEntry.f6acbd64cdadb94c1dff.js
+-rw-r--r--   0 jovyan    (1000) users      (100)      177 2023-04-07 14:55:10.000000 jupyterlab_nbgallery-2.0.0a4/labextension/gallerymenu/static/style.js
+-rw-r--r--   0 jovyan    (1000) users      (100)     3692 2023-04-07 14:55:19.000000 jupyterlab_nbgallery-2.0.0a4/labextension/gallerymenu/static/third-party-licenses.json
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 14:55:54.349939 jupyterlab_nbgallery-2.0.0a4/labextension/inject-uuid/
+-rw-r--r--   0 jovyan    (1000) users      (100)     2444 2023-04-07 14:55:46.000000 jupyterlab_nbgallery-2.0.0a4/labextension/inject-uuid/package.json
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 14:55:54.337939 jupyterlab_nbgallery-2.0.0a4/labextension/inject-uuid/schemas/
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 14:55:54.337939 jupyterlab_nbgallery-2.0.0a4/labextension/inject-uuid/schemas/@jupyterlab-nbgallery/
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 14:55:54.349939 jupyterlab_nbgallery-2.0.0a4/labextension/inject-uuid/schemas/@jupyterlab-nbgallery/inject-uuid/
+-rw-r--r--   0 jovyan    (1000) users      (100)     2328 2023-04-07 14:55:45.000000 jupyterlab_nbgallery-2.0.0a4/labextension/inject-uuid/schemas/@jupyterlab-nbgallery/inject-uuid/package.json.orig
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 14:55:54.353939 jupyterlab_nbgallery-2.0.0a4/labextension/inject-uuid/static/
+-rw-r--r--   0 jovyan    (1000) users      (100)      931 2023-04-07 14:55:46.000000 jupyterlab_nbgallery-2.0.0a4/labextension/inject-uuid/static/568.0616ffe42e5ee3230288.js
+-rw-r--r--   0 jovyan    (1000) users      (100)     6315 2023-04-07 14:55:46.000000 jupyterlab_nbgallery-2.0.0a4/labextension/inject-uuid/static/remoteEntry.6def7b207d91856938f3.js
+-rw-r--r--   0 jovyan    (1000) users      (100)      118 2023-04-07 14:55:45.000000 jupyterlab_nbgallery-2.0.0a4/labextension/inject-uuid/static/style.js
+-rw-r--r--   0 jovyan    (1000) users      (100)       20 2023-04-07 14:55:46.000000 jupyterlab_nbgallery-2.0.0a4/labextension/inject-uuid/static/third-party-licenses.json
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 14:55:54.353939 jupyterlab_nbgallery-2.0.0a4/labextension/instrumentation/
+-rw-r--r--   0 jovyan    (1000) users      (100)     2527 2023-04-07 14:55:52.000000 jupyterlab_nbgallery-2.0.0a4/labextension/instrumentation/package.json
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 14:55:54.337939 jupyterlab_nbgallery-2.0.0a4/labextension/instrumentation/schemas/
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 14:55:54.337939 jupyterlab_nbgallery-2.0.0a4/labextension/instrumentation/schemas/@jupyterlab-nbgallery/
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 14:55:54.353939 jupyterlab_nbgallery-2.0.0a4/labextension/instrumentation/schemas/@jupyterlab-nbgallery/instrumentation/
+-rw-r--r--   0 jovyan    (1000) users      (100)      345 2023-04-07 14:55:47.000000 jupyterlab_nbgallery-2.0.0a4/labextension/instrumentation/schemas/@jupyterlab-nbgallery/instrumentation/instrumentation.json
+-rw-r--r--   0 jovyan    (1000) users      (100)     2411 2023-04-07 14:55:47.000000 jupyterlab_nbgallery-2.0.0a4/labextension/instrumentation/schemas/@jupyterlab-nbgallery/instrumentation/package.json.orig
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 14:55:54.353939 jupyterlab_nbgallery-2.0.0a4/labextension/instrumentation/static/
+-rw-r--r--   0 jovyan    (1000) users      (100)     1721 2023-04-07 14:55:52.000000 jupyterlab_nbgallery-2.0.0a4/labextension/instrumentation/static/568.7f1ab65a55b54297cd7b.js
+-rw-r--r--   0 jovyan    (1000) users      (100)    90044 2023-04-07 14:55:52.000000 jupyterlab_nbgallery-2.0.0a4/labextension/instrumentation/static/638.b95125ed695cee42aae4.js
+-rw-r--r--   0 jovyan    (1000) users      (100)      476 2023-04-07 14:55:52.000000 jupyterlab_nbgallery-2.0.0a4/labextension/instrumentation/static/638.b95125ed695cee42aae4.js.LICENSE.txt
+-rw-r--r--   0 jovyan    (1000) users      (100)     8425 2023-04-07 14:55:52.000000 jupyterlab_nbgallery-2.0.0a4/labextension/instrumentation/static/701.d81800f5926ab62cc8b2.js
+-rw-r--r--   0 jovyan    (1000) users      (100)     7597 2023-04-07 14:55:52.000000 jupyterlab_nbgallery-2.0.0a4/labextension/instrumentation/static/remoteEntry.ae4d1ce402e6ac0dddb5.js
+-rw-r--r--   0 jovyan    (1000) users      (100)      118 2023-04-07 14:55:47.000000 jupyterlab_nbgallery-2.0.0a4/labextension/instrumentation/static/style.js
+-rw-r--r--   0 jovyan    (1000) users      (100)     2479 2023-04-07 14:55:52.000000 jupyterlab_nbgallery-2.0.0a4/labextension/instrumentation/static/third-party-licenses.json
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 14:55:54.353939 jupyterlab_nbgallery-2.0.0a4/labextension/userpreferences/
+-rw-r--r--   0 jovyan    (1000) users      (100)     2709 2023-04-07 14:55:53.000000 jupyterlab_nbgallery-2.0.0a4/labextension/userpreferences/package.json
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 14:55:54.337939 jupyterlab_nbgallery-2.0.0a4/labextension/userpreferences/schemas/
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 14:55:54.337939 jupyterlab_nbgallery-2.0.0a4/labextension/userpreferences/schemas/@jupyterlab-nbgallery/
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 14:55:54.357939 jupyterlab_nbgallery-2.0.0a4/labextension/userpreferences/schemas/@jupyterlab-nbgallery/userpreferences/
+-rw-r--r--   0 jovyan    (1000) users      (100)     2567 2023-04-07 14:55:48.000000 jupyterlab_nbgallery-2.0.0a4/labextension/userpreferences/schemas/@jupyterlab-nbgallery/userpreferences/package.json.orig
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 14:55:54.357939 jupyterlab_nbgallery-2.0.0a4/labextension/userpreferences/static/
+-rw-r--r--   0 jovyan    (1000) users      (100)     4026 2023-04-07 14:55:53.000000 jupyterlab_nbgallery-2.0.0a4/labextension/userpreferences/static/542.d1718a50e23f3808ba62.js
+-rw-r--r--   0 jovyan    (1000) users      (100)     4115 2023-04-07 14:55:53.000000 jupyterlab_nbgallery-2.0.0a4/labextension/userpreferences/static/568.0ac7cbac0996e718a0d9.js
+-rw-r--r--   0 jovyan    (1000) users      (100)    90044 2023-04-07 14:55:53.000000 jupyterlab_nbgallery-2.0.0a4/labextension/userpreferences/static/638.e5080f99954048969f76.js
+-rw-r--r--   0 jovyan    (1000) users      (100)      476 2023-04-07 14:55:53.000000 jupyterlab_nbgallery-2.0.0a4/labextension/userpreferences/static/638.e5080f99954048969f76.js.LICENSE.txt
+-rw-r--r--   0 jovyan    (1000) users      (100)     7136 2023-04-07 14:55:53.000000 jupyterlab_nbgallery-2.0.0a4/labextension/userpreferences/static/remoteEntry.3f8d9d3f425bc3ff0a80.js
+-rw-r--r--   0 jovyan    (1000) users      (100)      181 2023-04-07 14:55:48.000000 jupyterlab_nbgallery-2.0.0a4/labextension/userpreferences/static/style.js
+-rw-r--r--   0 jovyan    (1000) users      (100)     3692 2023-04-07 14:55:53.000000 jupyterlab_nbgallery-2.0.0a4/labextension/userpreferences/static/third-party-licenses.json
+-rw-r--r--   0 jovyan    (1000) users      (100)     1103 2023-04-07 14:52:37.000000 jupyterlab_nbgallery-2.0.0a4/package.json
+-rw-r--r--   0 jovyan    (1000) users      (100)      145 2023-04-07 14:52:37.000000 jupyterlab_nbgallery-2.0.0a4/pyproject.toml
+-rw-r--r--   0 jovyan    (1000) users      (100)       38 2023-04-07 14:55:54.357939 jupyterlab_nbgallery-2.0.0a4/setup.cfg
+-rw-r--r--   0 jovyan    (1000) users      (100)     3928 2023-04-07 14:52:37.000000 jupyterlab_nbgallery-2.0.0a4/setup.py
```

### Comparing `jupyterlab_nbgallery-2.0.0a3/LICENSE` & `jupyterlab_nbgallery-2.0.0a4/LICENSE`

 * *Files identical despite different names*

### Comparing `jupyterlab_nbgallery-2.0.0a3/PKG-INFO` & `jupyterlab_nbgallery-2.0.0a4/jupyterlab_nbgallery.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
-Name: jupyterlab_nbgallery
-Version: 2.0.0a3
+Name: jupyterlab-nbgallery
+Version: 2.0.0a4
 Summary: A JupyterLab Extension for NBGallery integration
 Home-page: https://github.com/nbgallery/lab-extensions
 Author: NBGallery
 License: MIT
 Keywords: Jupyter,JupyterLab
 Platform: Linux
 Platform: Mac OS X
```

### Comparing `jupyterlab_nbgallery-2.0.0a3/README.md` & `jupyterlab_nbgallery-2.0.0a4/README.md`

 * *Files identical despite different names*

### Comparing `jupyterlab_nbgallery-2.0.0a3/jupyterlab_nbgallery/__init__.py` & `jupyterlab_nbgallery-2.0.0a4/jupyterlab_nbgallery/__init__.py`

 * *Files identical despite different names*

### Comparing `jupyterlab_nbgallery-2.0.0a3/jupyterlab_nbgallery/handlers.py` & `jupyterlab_nbgallery-2.0.0a4/jupyterlab_nbgallery/handlers.py`

 * *Files identical despite different names*

### Comparing `jupyterlab_nbgallery-2.0.0a3/jupyterlab_nbgallery.egg-info/PKG-INFO` & `jupyterlab_nbgallery-2.0.0a4/PKG-INFO`

 * *Files 5% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
-Name: jupyterlab-nbgallery
-Version: 2.0.0a3
+Name: jupyterlab_nbgallery
+Version: 2.0.0a4
 Summary: A JupyterLab Extension for NBGallery integration
 Home-page: https://github.com/nbgallery/lab-extensions
 Author: NBGallery
 License: MIT
 Keywords: Jupyter,JupyterLab
 Platform: Linux
 Platform: Mac OS X
```

### Comparing `jupyterlab_nbgallery-2.0.0a3/jupyterlab_nbgallery.egg-info/SOURCES.txt` & `jupyterlab_nbgallery-2.0.0a4/jupyterlab_nbgallery.egg-info/SOURCES.txt`

 * *Files 7% similar despite different names*

```diff
@@ -14,64 +14,64 @@
 jupyterlab_nbgallery.egg-info/not-zip-safe
 jupyterlab_nbgallery.egg-info/requires.txt
 jupyterlab_nbgallery.egg-info/top_level.txt
 labextension/autodownload/package.json
 labextension/autodownload/schemas/@jupyterlab-nbgallery/autodownload/autodownload.json
 labextension/autodownload/schemas/@jupyterlab-nbgallery/autodownload/package.json.orig
 labextension/autodownload/static/542.51fb91347d8a3d9a657a.js
-labextension/autodownload/static/568.088b227a0b6b6168ee16.js
+labextension/autodownload/static/568.017b32a913356ad383e7.js
 labextension/autodownload/static/638.0ed295d9378dea7c5c7b.js
 labextension/autodownload/static/638.0ed295d9378dea7c5c7b.js.LICENSE.txt
-labextension/autodownload/static/remoteEntry.fa15592bca73423b04a4.js
+labextension/autodownload/static/remoteEntry.1353121aacb4a50d2fe1.js
 labextension/autodownload/static/style.js
 labextension/autodownload/static/third-party-licenses.json
 labextension/environment-life/package.json
 labextension/environment-life/schemas/@jupyterlab-nbgallery/environment-life/package.json.orig
-labextension/environment-life/static/248.1d3351413b89920be9fb.js
+labextension/environment-life/static/248.644879940d9faca2b389.js
 labextension/environment-life/static/542.e4d405f3b0e4f693ab53.js
-labextension/environment-life/static/remoteEntry.dd7691336809bc6771e3.js
+labextension/environment-life/static/remoteEntry.c977e6e35771b75265ee.js
 labextension/environment-life/static/style.js
 labextension/environment-life/static/third-party-licenses.json
 labextension/environment-registration/package.json
 labextension/environment-registration/schemas/@jupyterlab-nbgallery/environment-registration/environment-registration.json
 labextension/environment-registration/schemas/@jupyterlab-nbgallery/environment-registration/package.json.orig
 labextension/environment-registration/static/542.feae6c397f33f9138fea.js
 labextension/environment-registration/static/638.36e464d3233849b6b07a.js
 labextension/environment-registration/static/638.36e464d3233849b6b07a.js.LICENSE.txt
-labextension/environment-registration/static/784.c5c708b87c266cbabd98.js
-labextension/environment-registration/static/remoteEntry.00e0256ee314fd224ea3.js
+labextension/environment-registration/static/784.f151a96d5dde1a095c86.js
+labextension/environment-registration/static/remoteEntry.5a586807c39202b9c488.js
 labextension/environment-registration/static/style.js
 labextension/environment-registration/static/third-party-licenses.json
 labextension/gallerymenu/package.json
 labextension/gallerymenu/schemas/@jupyterlab-nbgallery/gallerymenu/package.json.orig
 labextension/gallerymenu/static/542.18fd91d86aaf6286edd0.js
-labextension/gallerymenu/static/56.00b49e0c37b3050cbc14.js
+labextension/gallerymenu/static/56.a4862cb4315ce0eea068.js
 labextension/gallerymenu/static/638.95e0186307171588df5b.js
 labextension/gallerymenu/static/638.95e0186307171588df5b.js.LICENSE.txt
-labextension/gallerymenu/static/remoteEntry.ae9dddbb4a23b1552c19.js
+labextension/gallerymenu/static/remoteEntry.f6acbd64cdadb94c1dff.js
 labextension/gallerymenu/static/style.js
 labextension/gallerymenu/static/third-party-licenses.json
 labextension/inject-uuid/package.json
 labextension/inject-uuid/schemas/@jupyterlab-nbgallery/inject-uuid/package.json.orig
-labextension/inject-uuid/static/568.1dcbb7bee8ca1152cf60.js
-labextension/inject-uuid/static/remoteEntry.02ddda09f0305fa467f4.js
+labextension/inject-uuid/static/568.0616ffe42e5ee3230288.js
+labextension/inject-uuid/static/remoteEntry.6def7b207d91856938f3.js
 labextension/inject-uuid/static/style.js
 labextension/inject-uuid/static/third-party-licenses.json
 labextension/instrumentation/package.json
 labextension/instrumentation/schemas/@jupyterlab-nbgallery/instrumentation/instrumentation.json
 labextension/instrumentation/schemas/@jupyterlab-nbgallery/instrumentation/package.json.orig
-labextension/instrumentation/static/568.0d3998aabd22f1867c40.js
+labextension/instrumentation/static/568.7f1ab65a55b54297cd7b.js
 labextension/instrumentation/static/638.b95125ed695cee42aae4.js
 labextension/instrumentation/static/638.b95125ed695cee42aae4.js.LICENSE.txt
 labextension/instrumentation/static/701.d81800f5926ab62cc8b2.js
-labextension/instrumentation/static/remoteEntry.53ed33a8ef1f603e0fc8.js
+labextension/instrumentation/static/remoteEntry.ae4d1ce402e6ac0dddb5.js
 labextension/instrumentation/static/style.js
 labextension/instrumentation/static/third-party-licenses.json
 labextension/userpreferences/package.json
 labextension/userpreferences/schemas/@jupyterlab-nbgallery/userpreferences/package.json.orig
 labextension/userpreferences/static/542.d1718a50e23f3808ba62.js
-labextension/userpreferences/static/568.00695541aaa15d567580.js
+labextension/userpreferences/static/568.0ac7cbac0996e718a0d9.js
 labextension/userpreferences/static/638.e5080f99954048969f76.js
 labextension/userpreferences/static/638.e5080f99954048969f76.js.LICENSE.txt
-labextension/userpreferences/static/remoteEntry.03bf745401d2317e1d7d.js
+labextension/userpreferences/static/remoteEntry.3f8d9d3f425bc3ff0a80.js
 labextension/userpreferences/static/style.js
 labextension/userpreferences/static/third-party-licenses.json
```

### Comparing `jupyterlab_nbgallery-2.0.0a3/labextension/autodownload/package.json` & `jupyterlab_nbgallery-2.0.0a4/labextension/environment-registration/package.json`

 * *Files 4% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9403935185185185%*

 * *Differences: {"'description'": "'Register NBGallery Environment'",*

 * * "'jupyterlab'": "{'outputDir': '../labextension/environment-registration', '_build': {'load': "*

 * *                 "'static/remoteEntry.5a586807c39202b9c488.js'}}",*

 * * "'name'": "'@jupyterlab-nbgallery/environment-registration'"}*

```diff
@@ -5,15 +5,15 @@
     },
     "dependencies": {
         "@jupyterlab/application": ">=3.6.0",
         "@jupyterlab/coreutils": ">=5.2.0",
         "@jupyterlab/settingregistry": ">=3.6.0",
         "jquery": "^3.5.0"
     },
-    "description": "NBGallery Auto Download Notebooks that are starred or recently executed",
+    "description": "Register NBGallery Environment",
     "devDependencies": {
         "@jupyterlab/builder": ">=3.3.2",
         "@types/jquery": "^3.5.0",
         "@typescript-eslint/eslint-plugin": "^4.8.1",
         "@typescript-eslint/parser": "^4.8.1",
         "eslint": "^8.0.0",
         "eslint-config-prettier": "^6.15.0",
@@ -29,29 +29,29 @@
         "style/**/*.{css,eot,gif,html,jpg,json,png,svg,woff2,ttf}",
         "schema/**/*.json"
     ],
     "homepage": "https://github.com/nbgallery/lab-extensions",
     "jupyterlab": {
         "_build": {
             "extension": "./extension",
-            "load": "static/remoteEntry.fa15592bca73423b04a4.js",
+            "load": "static/remoteEntry.5a586807c39202b9c488.js",
             "style": "./style"
         },
         "extension": true,
-        "outputDir": "../labextension/autodownload",
+        "outputDir": "../labextension/environment-registration",
         "schemaDir": "schema"
     },
     "keywords": [
         "jupyter",
         "jupyterlab",
         "jupyterlab-extension"
     ],
     "license": "MIT",
     "main": "lib/index.js",
-    "name": "@jupyterlab-nbgallery/autodownload",
+    "name": "@jupyterlab-nbgallery/environment-registration",
     "repository": {
         "type": "git",
         "url": "https://github.com/nbgallery/lab-extensions"
     },
     "scripts": {
         "build": "jlpm run build:lib && jlpm run build:labextension:dev",
         "build:all": "jlpm run build:prod",
```

### Comparing `jupyterlab_nbgallery-2.0.0a3/labextension/autodownload/schemas/@jupyterlab-nbgallery/autodownload/package.json.orig` & `jupyterlab_nbgallery-2.0.0a4/labextension/autodownload/schemas/@jupyterlab-nbgallery/autodownload/package.json.orig`

 * *Files 4% similar despite different names*

#### Pretty-printed

 * *Ordering differences only*

```diff
@@ -41,23 +41,23 @@
         "eslint": "eslint . --ext .ts,.tsx --fix",
         "eslint:check": "eslint . --ext .ts,.tsx",
         "watch:src": "tsc -w",
         "watch:labextension": "jupyter labextension watch ."
     },
     "dependencies": {
         "@jupyterlab/application": ">=3.6.0",
-        "@jupyterlab/settingregistry": ">=3.6.0",
         "@jupyterlab/coreutils": ">=5.2.0",
+        "@jupyterlab/settingregistry": ">=3.6.0",
         "jquery": "^3.5.0"
     },
     "devDependencies": {
         "@jupyterlab/builder": ">=3.3.2",
+        "@types/jquery": "^3.5.0",
         "@typescript-eslint/eslint-plugin": "^4.8.1",
         "@typescript-eslint/parser": "^4.8.1",
-        "@types/jquery": "^3.5.0",
         "eslint": "^8.0.0",
         "eslint-config-prettier": "^6.15.0",
         "eslint-plugin-jsdoc": "^39.0.0",
         "eslint-plugin-prettier": "^3.1.4",
         "eslint-plugin-react": "^7.18.3",
         "npm-run-all": "^4.1.5",
         "rimraf": "^3.0.2",
```

### Comparing `jupyterlab_nbgallery-2.0.0a3/labextension/autodownload/static/542.51fb91347d8a3d9a657a.js` & `jupyterlab_nbgallery-2.0.0a4/labextension/autodownload/static/542.51fb91347d8a3d9a657a.js`

 * *Files identical despite different names*

### Comparing `jupyterlab_nbgallery-2.0.0a3/labextension/autodownload/static/568.088b227a0b6b6168ee16.js` & `jupyterlab_nbgallery-2.0.0a4/labextension/autodownload/static/568.017b32a913356ad383e7.js`

 * *Files 5% similar despite different names*

#### js-beautify {}

```diff
@@ -1,16 +1,16 @@
 "use strict";
 (self.webpackChunk_jupyterlab_nbgallery_autodownload = self.webpackChunk_jupyterlab_nbgallery_autodownload || []).push([
     [568], {
         568: (e, o, t) => {
             t.r(o), t.d(o, {
                 default: () => s
             });
-            var n = t(38),
-                a = t(142),
+            var n = t(225),
+                a = t(281),
                 c = t(569),
                 r = t.n(c);
             const s = {
                 id: "@jupyterlab-nbgallery/autodownload",
                 autoStart: !0,
                 requires: [n.ISettingRegistry],
                 activate: async (e, o) => {
```

### Comparing `jupyterlab_nbgallery-2.0.0a3/labextension/autodownload/static/638.0ed295d9378dea7c5c7b.js` & `jupyterlab_nbgallery-2.0.0a4/labextension/autodownload/static/638.0ed295d9378dea7c5c7b.js`

 * *Files identical despite different names*

### Comparing `jupyterlab_nbgallery-2.0.0a3/labextension/autodownload/static/remoteEntry.fa15592bca73423b04a4.js` & `jupyterlab_nbgallery-2.0.0a4/labextension/autodownload/static/remoteEntry.1353121aacb4a50d2fe1.js`

 * *Files 4% similar despite different names*

#### js-beautify {}

```diff
@@ -1,11 +1,11 @@
 var _JUPYTERLAB;
 (() => {
     "use strict";
-    var e, r, t, n, o, a, i, l, u, d, s, f, p, c, h, v, b, g, y = {
+    var e, r, t, n, o, a, i, l, u, d, s, f, p, c, h, b, v, g, y = {
             735: (e, r, t) => {
                 var n = {
                         "./index": () => t.e(568).then((() => () => t(568))),
                         "./extension": () => t.e(568).then((() => () => t(568))),
                         "./style": () => t.e(542).then((() => () => t(542)))
                     },
                     o = (e, r) => (t.R = r, r = t.o(n, e) ? n[e]() : Promise.resolve().then((() => {
@@ -44,19 +44,19 @@
     }, w.d = (e, r) => {
         for (var t in r) w.o(r, t) && !w.o(e, t) && Object.defineProperty(e, t, {
             enumerable: !0,
             get: r[t]
         })
     }, w.f = {}, w.e = e => Promise.all(Object.keys(w.f).reduce(((r, t) => (w.f[t](e, r), r)), [])), w.u = e => e + "." + {
         542: "51fb91347d8a3d9a657a",
-        568: "088b227a0b6b6168ee16",
+        568: "017b32a913356ad383e7",
         638: "0ed295d9378dea7c5c7b"
     } [e] + ".js?v=" + {
         542: "51fb91347d8a3d9a657a",
-        568: "088b227a0b6b6168ee16",
+        568: "017b32a913356ad383e7",
         638: "0ed295d9378dea7c5c7b"
     } [e], w.g = function() {
         if ("object" == typeof globalThis) return globalThis;
         try {
             return this || new Function("return this")()
         } catch (e) {
             if ("object" == typeof window) return window
@@ -213,36 +213,36 @@
         return (r = Object.keys(o).reduce(((e, r) => !a(t, r) || e && !n(e, r) ? e : r), 0)) && o[r]
     }, f = e => (e.loaded = 1, e.get()), c = (p = e => function(r, t, n, o) {
         var a = w.I(r);
         return a && a.then ? a.then(e.bind(e, r, w.S[r], t, n, o)) : e(r, w.S[r], t, n, o)
     })(((e, r, t, n) => (i(e, t), d(r, 0, t, n)))), h = p(((e, r, t, n, o) => {
         var a = r && w.o(r, t) && s(r, t, n);
         return a ? f(a) : o()
-    })), v = {}, b = {
-        38: () => c("default", "@jupyterlab/settingregistry", [1, 3, 6, 3]),
-        142: () => c("default", "@jupyterlab/coreutils", [1, 5, 6, 3]),
+    })), b = {}, v = {
+        225: () => c("default", "@jupyterlab/settingregistry", [1, 4, 0, 0, , "beta", 0]),
+        281: () => c("default", "@jupyterlab/coreutils", [1, 6, 0, 0, , "beta", 0]),
         569: () => h("default", "jquery", [1, 3, 5, 0], (() => w.e(638).then((() => () => w(638)))))
     }, g = {
-        568: [38, 142, 569]
+        568: [225, 281, 569]
     }, w.f.consumes = (e, r) => {
         w.o(g, e) && g[e].forEach((e => {
-            if (w.o(v, e)) return r.push(v[e]);
+            if (w.o(b, e)) return r.push(b[e]);
             var t = r => {
-                    v[e] = 0, w.m[e] = t => {
+                    b[e] = 0, w.m[e] = t => {
                         delete w.c[e], t.exports = r()
                     }
                 },
                 n = r => {
-                    delete v[e], w.m[e] = t => {
+                    delete b[e], w.m[e] = t => {
                         throw delete w.c[e], r
                     }
                 };
             try {
-                var o = b[e]();
-                o.then ? r.push(v[e] = o.then(t).catch(n)) : t(o)
+                var o = v[e]();
+                o.then ? r.push(b[e] = o.then(t).catch(n)) : t(o)
             } catch (e) {
                 n(e)
             }
         }))
     }, (() => {
         var e = {
             263: 0
```

### Comparing `jupyterlab_nbgallery-2.0.0a3/labextension/autodownload/static/third-party-licenses.json` & `jupyterlab_nbgallery-2.0.0a4/labextension/autodownload/static/third-party-licenses.json`

 * *Files identical despite different names*

### Comparing `jupyterlab_nbgallery-2.0.0a3/labextension/environment-life/package.json` & `jupyterlab_nbgallery-2.0.0a4/labextension/environment-life/package.json`

 * *Files 2% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9994212962962963%*

 * *Differences: {"'jupyterlab'": "{'_build': {'load': 'static/remoteEntry.c977e6e35771b75265ee.js'}}"}*

```diff
@@ -27,15 +27,15 @@
         "lib/**/*.{d.ts,eot,gif,html,jpg,js,js.map,json,png,svg,woff2,ttf}",
         "style/**/*.{css,eot,gif,html,jpg,json,png,svg,woff2,ttf}"
     ],
     "homepage": "https://github.com/nbgallery/lab-extensions",
     "jupyterlab": {
         "_build": {
             "extension": "./extension",
-            "load": "static/remoteEntry.dd7691336809bc6771e3.js",
+            "load": "static/remoteEntry.c977e6e35771b75265ee.js",
             "style": "./style"
         },
         "extension": true,
         "outputDir": "../labextension/environment-life",
         "schemaDir": "schema"
     },
     "keywords": [
```

### Comparing `jupyterlab_nbgallery-2.0.0a3/labextension/environment-life/schemas/@jupyterlab-nbgallery/environment-life/package.json.orig` & `jupyterlab_nbgallery-2.0.0a4/labextension/environment-life/schemas/@jupyterlab-nbgallery/environment-life/package.json.orig`

 * *Files 3% similar despite different names*

#### Pretty-printed

 * *Ordering differences only*

```diff
@@ -45,17 +45,17 @@
     "dependencies": {
         "@jupyterlab/application": ">=3.6.0",
         "@jupyterlab/settingregistry": ">=3.6.0",
         "jquery": "^3.5.0"
     },
     "devDependencies": {
         "@jupyterlab/builder": ">=3.3.2",
+        "@types/jquery": "^3.5.0",
         "@typescript-eslint/eslint-plugin": "^4.8.1",
         "@typescript-eslint/parser": "^4.8.1",
-        "@types/jquery": "^3.5.0",
         "eslint": "^8.0.0",
         "eslint-config-prettier": "^6.15.0",
         "eslint-plugin-jsdoc": "^39.0.0",
         "eslint-plugin-prettier": "^3.1.4",
         "eslint-plugin-react": "^7.18.3",
         "npm-run-all": "^4.1.5",
         "rimraf": "^3.0.2",
```

### Comparing `jupyterlab_nbgallery-2.0.0a3/labextension/environment-life/static/248.1d3351413b89920be9fb.js` & `jupyterlab_nbgallery-2.0.0a4/labextension/environment-life/static/248.644879940d9faca2b389.js`

 * *Files 4% similar despite different names*

#### js-beautify {}

```diff
@@ -1,18 +1,18 @@
 "use strict";
 (self.webpackChunk_jupyterlab_nbgallery_environment_life = self.webpackChunk_jupyterlab_nbgallery_environment_life || []).push([
     [248], {
         248: (e, t, n) => {
             n.r(t), n.d(t, {
                 default: () => s
             });
-            var r = n(832),
-                i = n(583),
-                o = n(142),
-                a = n(820);
+            var r = n(144),
+                i = n(791),
+                o = n(281),
+                a = n(530);
             const s = {
                 id: "@jupyterlab-nbgallery/environment-life",
                 autoStart: !0,
                 requires: [i.IStatusBar],
                 activate: async (e, t) => {
                     let n = "";
                     try {
```

### Comparing `jupyterlab_nbgallery-2.0.0a3/labextension/environment-life/static/542.e4d405f3b0e4f693ab53.js` & `jupyterlab_nbgallery-2.0.0a4/labextension/environment-life/static/542.e4d405f3b0e4f693ab53.js`

 * *Files identical despite different names*

### Comparing `jupyterlab_nbgallery-2.0.0a3/labextension/environment-life/static/remoteEntry.dd7691336809bc6771e3.js` & `jupyterlab_nbgallery-2.0.0a4/labextension/environment-life/static/remoteEntry.c977e6e35771b75265ee.js`

 * *Files 4% similar despite different names*

#### js-beautify {}

```diff
@@ -43,18 +43,18 @@
         }), r
     }, g.d = (e, r) => {
         for (var t in r) g.o(r, t) && !g.o(e, t) && Object.defineProperty(e, t, {
             enumerable: !0,
             get: r[t]
         })
     }, g.f = {}, g.e = e => Promise.all(Object.keys(g.f).reduce(((r, t) => (g.f[t](e, r), r)), [])), g.u = e => e + "." + {
-        248: "1d3351413b89920be9fb",
+        248: "644879940d9faca2b389",
         542: "e4d405f3b0e4f693ab53"
     } [e] + ".js?v=" + {
-        248: "1d3351413b89920be9fb",
+        248: "644879940d9faca2b389",
         542: "e4d405f3b0e4f693ab53"
     } [e], g.g = function() {
         if ("object" == typeof globalThis) return globalThis;
         try {
             return this || new Function("return this")()
         } catch (e) {
             if ("object" == typeof window) return window
@@ -205,20 +205,20 @@
     }, u = (e, r, t, n) => "Unsatisfied version " + t + " from " + (t && e[r][t].from) + " of shared singleton module " + r + " (required " + o(n) + ")", f = (e, r, t, n) => {
         var o = l(e, t);
         return a(n, o) || "undefined" != typeof console && console.warn && console.warn(u(e, t, o, n)), s(e[t][o])
     }, s = e => (e.loaded = 1, e.get()), d = (e => function(r, t, n, o) {
         var a = g.I(r);
         return a && a.then ? a.then(e.bind(e, r, g.S[r], t, n, o)) : e(r, g.S[r], t, n)
     })(((e, r, t, n) => (i(e, t), f(r, 0, t, n)))), p = {}, c = {
-        142: () => d("default", "@jupyterlab/coreutils", [1, 5, 6, 3]),
-        583: () => d("default", "@jupyterlab/statusbar", [1, 3, 6, 3]),
-        820: () => d("default", "@jupyterlab/services", [1, 6, 6, 3]),
-        832: () => d("default", "@lumino/widgets", [1, 1, 37, 2])
+        144: () => d("default", "@lumino/widgets", [1, 2, 0, 0]),
+        281: () => d("default", "@jupyterlab/coreutils", [1, 6, 0, 0, , "beta", 0]),
+        530: () => d("default", "@jupyterlab/services", [1, 7, 0, 0, , "beta", 0]),
+        791: () => d("default", "@jupyterlab/statusbar", [1, 4, 0, 0, , "beta", 0])
     }, h = {
-        248: [142, 583, 820, 832]
+        248: [144, 281, 530, 791]
     }, g.f.consumes = (e, r) => {
         g.o(h, e) && h[e].forEach((e => {
             if (g.o(p, e)) return r.push(p[e]);
             var t = r => {
                     p[e] = 0, g.m[e] = t => {
                         delete g.c[e], t.exports = r()
                     }
```

### Comparing `jupyterlab_nbgallery-2.0.0a3/labextension/environment-life/static/third-party-licenses.json` & `jupyterlab_nbgallery-2.0.0a4/labextension/environment-life/static/third-party-licenses.json`

 * *Files identical despite different names*

### Comparing `jupyterlab_nbgallery-2.0.0a3/labextension/environment-registration/package.json` & `jupyterlab_nbgallery-2.0.0a4/labextension/inject-uuid/package.json`

 * *Files 4% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.839699074074074%*

 * *Differences: {"'dependencies'": "{delete: ['@jupyterlab/coreutils']}",*

 * * "'description'": "'Inject the notebook UUID into the kernel.'",*

 * * "'files'": '{delete: [2]}',*

 * * "'jupyterlab'": "{'outputDir': '../labextension/inject-uuid', '_build': {'load': "*

 * *                 "'static/remoteEntry.6def7b207d91856938f3.js', delete: ['style']}}",*

 * * "'name'": "'@jupyterlab-nbgallery/inject-uuid'",*

 * * "'version'": "'2.0.0'",*

 * * 'delete': "['style']"}*

```diff
@@ -1,19 +1,18 @@
 {
     "author": "Team@NBG",
     "bugs": {
         "url": "https://github.com/nbgallery/lab-extensions/issues"
     },
     "dependencies": {
         "@jupyterlab/application": ">=3.6.0",
-        "@jupyterlab/coreutils": ">=5.2.0",
         "@jupyterlab/settingregistry": ">=3.6.0",
         "jquery": "^3.5.0"
     },
-    "description": "Register NBGallery Environment",
+    "description": "Inject the notebook UUID into the kernel.",
     "devDependencies": {
         "@jupyterlab/builder": ">=3.3.2",
         "@types/jquery": "^3.5.0",
         "@typescript-eslint/eslint-plugin": "^4.8.1",
         "@typescript-eslint/parser": "^4.8.1",
         "eslint": "^8.0.0",
         "eslint-config-prettier": "^6.15.0",
@@ -22,36 +21,34 @@
         "eslint-plugin-react": "^7.18.3",
         "npm-run-all": "^4.1.5",
         "rimraf": "^3.0.2",
         "typescript": "~4.1.3"
     },
     "files": [
         "lib/**/*.{d.ts,eot,gif,html,jpg,js,js.map,json,png,svg,woff2,ttf}",
-        "style/**/*.{css,eot,gif,html,jpg,json,png,svg,woff2,ttf}",
-        "schema/**/*.json"
+        "style/**/*.{css,eot,gif,html,jpg,json,png,svg,woff2,ttf}"
     ],
     "homepage": "https://github.com/nbgallery/lab-extensions",
     "jupyterlab": {
         "_build": {
             "extension": "./extension",
-            "load": "static/remoteEntry.00e0256ee314fd224ea3.js",
-            "style": "./style"
+            "load": "static/remoteEntry.6def7b207d91856938f3.js"
         },
         "extension": true,
-        "outputDir": "../labextension/environment-registration",
+        "outputDir": "../labextension/inject-uuid",
         "schemaDir": "schema"
     },
     "keywords": [
         "jupyter",
         "jupyterlab",
         "jupyterlab-extension"
     ],
     "license": "MIT",
     "main": "lib/index.js",
-    "name": "@jupyterlab-nbgallery/environment-registration",
+    "name": "@jupyterlab-nbgallery/inject-uuid",
     "repository": {
         "type": "git",
         "url": "https://github.com/nbgallery/lab-extensions"
     },
     "scripts": {
         "build": "jlpm run build:lib && jlpm run build:labextension:dev",
         "build:all": "jlpm run build:prod",
@@ -69,11 +66,10 @@
         "install-ext": "jlpm run build",
         "watch:labextension": "jupyter labextension watch .",
         "watch:src": "tsc -w"
     },
     "sideEffects": [
         "style/*.css"
     ],
-    "style": "style/index.css",
     "types": "lib/index.d.ts",
-    "version": "1.0.3"
+    "version": "2.0.0"
 }
```

### Comparing `jupyterlab_nbgallery-2.0.0a3/labextension/environment-registration/schemas/@jupyterlab-nbgallery/environment-registration/environment-registration.json` & `jupyterlab_nbgallery-2.0.0a4/labextension/environment-registration/schemas/@jupyterlab-nbgallery/environment-registration/environment-registration.json`

 * *Files identical despite different names*

### Comparing `jupyterlab_nbgallery-2.0.0a3/labextension/environment-registration/schemas/@jupyterlab-nbgallery/environment-registration/package.json.orig` & `jupyterlab_nbgallery-2.0.0a4/labextension/inject-uuid/schemas/@jupyterlab-nbgallery/inject-uuid/package.json.orig`

 * *Files 6% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.8402777777777777%*

 * *Differences: {"'dependencies'": "{delete: ['@jupyterlab/coreutils']}",*

 * * "'description'": "'Inject the notebook UUID into the kernel.'",*

 * * "'files'": '{delete: [2]}',*

 * * "'jupyterlab'": "{'outputDir': '../labextension/inject-uuid'}",*

 * * "'name'": "'@jupyterlab-nbgallery/inject-uuid'",*

 * * "'version'": "'2.0.0'",*

 * * 'delete': "['style']"}*

```diff
@@ -1,19 +1,18 @@
 {
     "author": "Team@NBG",
     "bugs": {
         "url": "https://github.com/nbgallery/lab-extensions/issues"
     },
     "dependencies": {
         "@jupyterlab/application": ">=3.6.0",
-        "@jupyterlab/coreutils": ">=5.2.0",
         "@jupyterlab/settingregistry": ">=3.6.0",
         "jquery": "^3.5.0"
     },
-    "description": "Register NBGallery Environment",
+    "description": "Inject the notebook UUID into the kernel.",
     "devDependencies": {
         "@jupyterlab/builder": ">=3.3.2",
         "@types/jquery": "^3.5.0",
         "@typescript-eslint/eslint-plugin": "^4.8.1",
         "@typescript-eslint/parser": "^4.8.1",
         "eslint": "^8.0.0",
         "eslint-config-prettier": "^6.15.0",
@@ -22,31 +21,30 @@
         "eslint-plugin-react": "^7.18.3",
         "npm-run-all": "^4.1.5",
         "rimraf": "^3.0.2",
         "typescript": "~4.1.3"
     },
     "files": [
         "lib/**/*.{d.ts,eot,gif,html,jpg,js,js.map,json,png,svg,woff2,ttf}",
-        "style/**/*.{css,eot,gif,html,jpg,json,png,svg,woff2,ttf}",
-        "schema/**/*.json"
+        "style/**/*.{css,eot,gif,html,jpg,json,png,svg,woff2,ttf}"
     ],
     "homepage": "https://github.com/nbgallery/lab-extensions",
     "jupyterlab": {
         "extension": true,
-        "outputDir": "../labextension/environment-registration",
+        "outputDir": "../labextension/inject-uuid",
         "schemaDir": "schema"
     },
     "keywords": [
         "jupyter",
         "jupyterlab",
         "jupyterlab-extension"
     ],
     "license": "MIT",
     "main": "lib/index.js",
-    "name": "@jupyterlab-nbgallery/environment-registration",
+    "name": "@jupyterlab-nbgallery/inject-uuid",
     "repository": {
         "type": "git",
         "url": "https://github.com/nbgallery/lab-extensions"
     },
     "scripts": {
         "build": "jlpm run build:lib && jlpm run build:labextension:dev",
         "build:all": "jlpm run build:prod",
@@ -64,11 +62,10 @@
         "install-ext": "jlpm run build",
         "watch:labextension": "jupyter labextension watch .",
         "watch:src": "tsc -w"
     },
     "sideEffects": [
         "style/*.css"
     ],
-    "style": "style/index.css",
     "types": "lib/index.d.ts",
-    "version": "1.0.3"
+    "version": "2.0.0"
 }
```

### Comparing `jupyterlab_nbgallery-2.0.0a3/labextension/environment-registration/static/542.feae6c397f33f9138fea.js` & `jupyterlab_nbgallery-2.0.0a4/labextension/environment-registration/static/542.feae6c397f33f9138fea.js`

 * *Files identical despite different names*

### Comparing `jupyterlab_nbgallery-2.0.0a3/labextension/environment-registration/static/638.36e464d3233849b6b07a.js` & `jupyterlab_nbgallery-2.0.0a4/labextension/environment-registration/static/638.36e464d3233849b6b07a.js`

 * *Files identical despite different names*

### Comparing `jupyterlab_nbgallery-2.0.0a3/labextension/environment-registration/static/784.c5c708b87c266cbabd98.js` & `jupyterlab_nbgallery-2.0.0a4/labextension/environment-registration/static/784.f151a96d5dde1a095c86.js`

 * *Files 9% similar despite different names*

#### js-beautify {}

```diff
@@ -1,17 +1,17 @@
 "use strict";
 (self.webpackChunk_jupyterlab_nbgallery_environment_registration = self.webpackChunk_jupyterlab_nbgallery_environment_registration || []).push([
     [784], {
         784: (e, n, t) => {
             t.r(n), t.d(n, {
                 default: () => s
             });
-            var r = t(38),
-                a = t(142),
-                o = t(820),
+            var r = t(225),
+                a = t(281),
+                o = t(530),
                 i = t(569),
                 l = t.n(i);
             const s = {
                 id: "@jupyterlab-nbgallery/environment-registration",
                 autoStart: !0,
                 requires: [r.ISettingRegistry],
                 activate: async (e, n) => {
```

### Comparing `jupyterlab_nbgallery-2.0.0a3/labextension/environment-registration/static/remoteEntry.00e0256ee314fd224ea3.js` & `jupyterlab_nbgallery-2.0.0a4/labextension/environment-registration/static/remoteEntry.5a586807c39202b9c488.js`

 * *Files 4% similar despite different names*

#### js-beautify {}

```diff
@@ -45,19 +45,19 @@
         for (var t in r) w.o(r, t) && !w.o(e, t) && Object.defineProperty(e, t, {
             enumerable: !0,
             get: r[t]
         })
     }, w.f = {}, w.e = e => Promise.all(Object.keys(w.f).reduce(((r, t) => (w.f[t](e, r), r)), [])), w.u = e => e + "." + {
         542: "feae6c397f33f9138fea",
         638: "36e464d3233849b6b07a",
-        784: "c5c708b87c266cbabd98"
+        784: "f151a96d5dde1a095c86"
     } [e] + ".js?v=" + {
         542: "feae6c397f33f9138fea",
         638: "36e464d3233849b6b07a",
-        784: "c5c708b87c266cbabd98"
+        784: "f151a96d5dde1a095c86"
     } [e], w.g = function() {
         if ("object" == typeof globalThis) return globalThis;
         try {
             return this || new Function("return this")()
         } catch (e) {
             if ("object" == typeof window) return window
         }
@@ -214,20 +214,20 @@
     }, d = e => (e.loaded = 1, e.get()), p = (c = e => function(r, t, n, a) {
         var o = w.I(r);
         return o && o.then ? o.then(e.bind(e, r, w.S[r], t, n, a)) : e(r, w.S[r], t, n, a)
     })(((e, r, t, n) => (i(e, t), s(r, 0, t, n)))), h = c(((e, r, t, n, a) => {
         var o = r && w.o(r, t) && f(r, t, n);
         return o ? d(o) : a()
     })), v = {}, g = {
-        38: () => p("default", "@jupyterlab/settingregistry", [1, 3, 6, 3]),
-        142: () => p("default", "@jupyterlab/coreutils", [1, 5, 6, 3]),
-        569: () => h("default", "jquery", [1, 3, 5, 0], (() => w.e(638).then((() => () => w(638))))),
-        820: () => p("default", "@jupyterlab/services", [1, 6, 6, 3])
+        225: () => p("default", "@jupyterlab/settingregistry", [1, 4, 0, 0, , "beta", 0]),
+        281: () => p("default", "@jupyterlab/coreutils", [1, 6, 0, 0, , "beta", 0]),
+        530: () => p("default", "@jupyterlab/services", [1, 7, 0, 0, , "beta", 0]),
+        569: () => h("default", "jquery", [1, 3, 5, 0], (() => w.e(638).then((() => () => w(638)))))
     }, b = {
-        784: [38, 142, 569, 820]
+        784: [225, 281, 530, 569]
     }, w.f.consumes = (e, r) => {
         w.o(b, e) && b[e].forEach((e => {
             if (w.o(v, e)) return r.push(v[e]);
             var t = r => {
                     v[e] = 0, w.m[e] = t => {
                         delete w.c[e], t.exports = r()
                     }
```

### Comparing `jupyterlab_nbgallery-2.0.0a3/labextension/environment-registration/static/third-party-licenses.json` & `jupyterlab_nbgallery-2.0.0a4/labextension/environment-registration/static/third-party-licenses.json`

 * *Files identical despite different names*

### Comparing `jupyterlab_nbgallery-2.0.0a3/labextension/gallerymenu/package.json` & `jupyterlab_nbgallery-2.0.0a4/labextension/gallerymenu/package.json`

 * *Files 1% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9994212962962963%*

 * *Differences: {"'jupyterlab'": "{'_build': {'load': 'static/remoteEntry.f6acbd64cdadb94c1dff.js'}}"}*

```diff
@@ -31,15 +31,15 @@
         "style/**/*.{css,eot,gif,html,jpg,json,png,svg,woff2,ttf}",
         "schema/**/*.json"
     ],
     "homepage": "https://github.com/nbgallery/lab-extensions",
     "jupyterlab": {
         "_build": {
             "extension": "./extension",
-            "load": "static/remoteEntry.ae9dddbb4a23b1552c19.js",
+            "load": "static/remoteEntry.f6acbd64cdadb94c1dff.js",
             "style": "./style"
         },
         "extension": true,
         "outputDir": "../labextension/gallerymenu",
         "schemaDir": "schema"
     },
     "keywords": [
```

### Comparing `jupyterlab_nbgallery-2.0.0a3/labextension/gallerymenu/schemas/@jupyterlab-nbgallery/gallerymenu/package.json.orig` & `jupyterlab_nbgallery-2.0.0a4/labextension/userpreferences/schemas/@jupyterlab-nbgallery/userpreferences/package.json.orig`

 * *Files 3% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9363425925925927%*

 * *Differences: {"'dependencies'": "{'@jupyterlab/mainmenu': '>=3.6.0 ||'}",*

 * * "'devDependencies'": "{'@jupyterlab/builder': '>=3.3.2'}",*

 * * "'jupyterlab'": "{'outputDir': '../labextension/userpreferences'}",*

 * * "'name'": "'@jupyterlab-nbgallery/userpreferences'",*

 * * "'version'": "'1.0.2'"}*

```diff
@@ -1,23 +1,23 @@
 {
     "author": "Team@NBG",
     "bugs": {
         "url": "https://github.com/nbgallery/lab-extensions/issues"
     },
     "dependencies": {
         "@jupyterlab/application": ">=3.6.0",
-        "@jupyterlab/mainmenu": ">=3.6.0",
+        "@jupyterlab/mainmenu": ">=3.6.0 ||",
         "@jupyterlab/notebook": ">=3.6.0",
         "@jupyterlab/settingregistry": ">=3.6.0",
         "fa-icons": "^0.2.0",
         "jquery": "^3.5.0"
     },
     "description": "All the menu capabilities needed for saving/forking notebooks and submitting change request to Notebook Gallery",
     "devDependencies": {
-        "@jupyterlab/builder": ">=3.6.0",
+        "@jupyterlab/builder": ">=3.3.2",
         "@types/jquery": "^3.5.0",
         "@typescript-eslint/eslint-plugin": "^4.8.1",
         "@typescript-eslint/parser": "^4.8.1",
         "eslint": "^8.0.0",
         "eslint-config-prettier": "^6.15.0",
         "eslint-plugin-jsdoc": "^39.0.0",
         "eslint-plugin-prettier": "^3.1.4",
@@ -30,25 +30,25 @@
         "lib/**/*.{d.ts,eot,gif,html,jpg,js,js.map,json,png,svg,woff2,ttf}",
         "style/**/*.{css,eot,gif,html,jpg,json,png,svg,woff2,ttf}",
         "schema/**/*.json"
     ],
     "homepage": "https://github.com/nbgallery/lab-extensions",
     "jupyterlab": {
         "extension": true,
-        "outputDir": "../labextension/gallerymenu",
+        "outputDir": "../labextension/userpreferences",
         "schemaDir": "schema"
     },
     "keywords": [
         "jupyter",
         "jupyterlab",
         "jupyterlab-extension"
     ],
     "license": "MIT",
     "main": "lib/index.js",
-    "name": "@jupyterlab-nbgallery/gallerymenu",
+    "name": "@jupyterlab-nbgallery/userpreferences",
     "repository": {
         "type": "git",
         "url": "https://github.com/nbgallery/lab-extensions"
     },
     "scripts": {
         "build": "jlpm run build:lib && jlpm run build:labextension:dev",
         "build:all": "jlpm run build:prod",
@@ -68,9 +68,9 @@
         "watch:src": "tsc -w"
     },
     "sideEffects": [
         "style/*.css"
     ],
     "style": "style/index.css",
     "types": "lib/index.d.ts",
-    "version": "2.0.0"
+    "version": "1.0.2"
 }
```

### Comparing `jupyterlab_nbgallery-2.0.0a3/labextension/gallerymenu/static/542.18fd91d86aaf6286edd0.js` & `jupyterlab_nbgallery-2.0.0a4/labextension/gallerymenu/static/542.18fd91d86aaf6286edd0.js`

 * *Files identical despite different names*

### Comparing `jupyterlab_nbgallery-2.0.0a3/labextension/gallerymenu/static/56.00b49e0c37b3050cbc14.js` & `jupyterlab_nbgallery-2.0.0a4/labextension/gallerymenu/static/56.a4862cb4315ce0eea068.js`

 * *Files 1% similar despite different names*

#### js-beautify {}

```diff
@@ -1,21 +1,21 @@
 "use strict";
 (self.webpackChunk_jupyterlab_nbgallery_gallerymenu = self.webpackChunk_jupyterlab_nbgallery_gallerymenu || []).push([
     [56], {
         56: (e, t, a) => {
             a.r(t), a.d(t, {
                 default: () => k
             });
-            var l = a(344),
-                i = a(33),
-                o = a(832),
-                n = a(123),
-                s = a(820),
-                r = a(142),
-                d = a(271);
+            var l = a(551),
+                i = a(678),
+                o = a(144),
+                n = a(598),
+                s = a(530),
+                r = a(281),
+                d = a(29);
             class h extends i.ReactWidget {
                 constructor() {
                     super(), this.addClass("jp-ReactWidget")
                 }
                 render() {
                     return d.createElement("div", {
                         dangerouslySetInnerHTML: {
@@ -68,15 +68,15 @@
                         rank: 50
                     }), setTimeout(this.gallery_menu.update, 4e3)
                 }
                 getGalleryMetadata(e) {
                     return e.model.sharedModel.metadata.gallery
                 }
                 setGalleryMetadata(e, t) {
-                    e.model.metadata.set("gallery", t), this.triggerSave()
+                    e.model.sharedModel.setMetadata("gallery", t), this.triggerSave()
                 }
                 updateMetadata(e, t, a) {
                     let l = !1,
                         i = !1;
                     t && t.link && (l = !0), t && t.clone && (i = !0), t || (t = {}), t.commit = a.commit, t.staging_id = a.staging_id, t.filename = a.filename, a.link ? t.uuid = a.link : t.uuid = a.clone, l ? t.link = t.uuid : i ? t.clone = t.uuid : a.link ? t.link = t.uuid : a.clone && (t.clone = t.uuid), this.setGalleryMetadata(e, t), this.triggerSave()
                 }
                 triggerSave() {
```

### Comparing `jupyterlab_nbgallery-2.0.0a3/labextension/gallerymenu/static/638.95e0186307171588df5b.js` & `jupyterlab_nbgallery-2.0.0a4/labextension/gallerymenu/static/638.95e0186307171588df5b.js`

 * *Files identical despite different names*

### Comparing `jupyterlab_nbgallery-2.0.0a3/labextension/gallerymenu/static/remoteEntry.ae9dddbb4a23b1552c19.js` & `jupyterlab_nbgallery-2.0.0a4/labextension/gallerymenu/static/remoteEntry.f6acbd64cdadb94c1dff.js`

 * *Files 6% similar despite different names*

#### js-beautify {}

```diff
@@ -1,11 +1,11 @@
 var _JUPYTERLAB;
 (() => {
     "use strict";
-    var e, r, t, n, a, o, l, i, u, f, s, d, c, p, h, v, y, g, b = {
+    var e, r, t, n, a, o, l, i, u, f, s, d, p, c, h, b, v, y, g = {
             421: (e, r, t) => {
                 var n = {
                         "./index": () => t.e(56).then((() => () => t(56))),
                         "./extension": () => t.e(56).then((() => () => t(56))),
                         "./style": () => t.e(542).then((() => () => t(542)))
                     },
                     a = (e, r) => (t.R = r, r = t.o(n, e) ? n[e]() : Promise.resolve().then((() => {
@@ -30,32 +30,32 @@
     function w(e) {
         var r = m[e];
         if (void 0 !== r) return r.exports;
         var t = m[e] = {
             id: e,
             exports: {}
         };
-        return b[e].call(t.exports, t, t.exports, w), t.exports
+        return g[e].call(t.exports, t, t.exports, w), t.exports
     }
-    w.m = b, w.c = m, w.n = e => {
+    w.m = g, w.c = m, w.n = e => {
         var r = e && e.__esModule ? () => e.default : () => e;
         return w.d(r, {
             a: r
         }), r
     }, w.d = (e, r) => {
         for (var t in r) w.o(r, t) && !w.o(e, t) && Object.defineProperty(e, t, {
             enumerable: !0,
             get: r[t]
         })
     }, w.f = {}, w.e = e => Promise.all(Object.keys(w.f).reduce(((r, t) => (w.f[t](e, r), r)), [])), w.u = e => e + "." + {
-        56: "00b49e0c37b3050cbc14",
+        56: "a4862cb4315ce0eea068",
         542: "18fd91d86aaf6286edd0",
         638: "95e0186307171588df5b"
     } [e] + ".js?v=" + {
-        56: "00b49e0c37b3050cbc14",
+        56: "a4862cb4315ce0eea068",
         542: "18fd91d86aaf6286edd0",
         638: "95e0186307171588df5b"
     } [e], w.g = function() {
         if ("object" == typeof globalThis) return globalThis;
         try {
             return this || new Function("return this")()
         } catch (e) {
@@ -71,19 +71,19 @@
                     if (s.getAttribute("src") == t || s.getAttribute("data-webpack") == r + a) {
                         l = s;
                         break
                     }
                 }
             l || (i = !0, (l = document.createElement("script")).charset = "utf-8", l.timeout = 120, w.nc && l.setAttribute("nonce", w.nc), l.setAttribute("data-webpack", r + a), l.src = t), e[t] = [n];
             var d = (r, n) => {
-                    l.onerror = l.onload = null, clearTimeout(c);
+                    l.onerror = l.onload = null, clearTimeout(p);
                     var a = e[t];
                     if (delete e[t], l.parentNode && l.parentNode.removeChild(l), a && a.forEach((e => e(n))), r) return r(n)
                 },
-                c = setTimeout(d.bind(null, void 0, {
+                p = setTimeout(d.bind(null, void 0, {
                     type: "timeout",
                     target: l
                 }), 12e4);
             l.onerror = d.bind(null, l.onerror), l.onload = d.bind(null, l.onload), i && document.head.appendChild(l)
         }
     }, w.r = e => {
         "undefined" != typeof Symbol && Symbol.toStringTag && Object.defineProperty(e, Symbol.toStringTag, {
@@ -187,67 +187,67 @@
                     u = !1, i--
                 } else {
                     if (i <= n || s < d != a) return !1;
                     u = !1
                 } else "s" != d && "n" != d && (u = !1, i--)
             }
         }
-        var c = [],
-            p = c.pop.bind(c);
+        var p = [],
+            c = p.pop.bind(p);
         for (l = 1; l < e.length; l++) {
             var h = e[l];
-            c.push(1 == h ? p() | p() : 2 == h ? p() & p() : h ? o(h, r) : !p())
+            p.push(1 == h ? c() | c() : 2 == h ? c() & c() : h ? o(h, r) : !c())
         }
-        return !!p()
+        return !!c()
     }, l = (e, r) => {
         var t = w.S[e];
         if (!t || !w.o(t, r)) throw new Error("Shared module " + r + " doesn't exist in shared scope " + e);
         return t
     }, i = (e, r) => {
         var t = e[r];
         return Object.keys(t).reduce(((e, r) => !e || !t[e].loaded && n(e, r) ? r : e), 0)
     }, u = (e, r, t, n) => "Unsatisfied version " + t + " from " + (t && e[r][t].from) + " of shared singleton module " + r + " (required " + a(n) + ")", f = (e, r, t, n) => {
         var a = i(e, t);
         return o(n, a) || "undefined" != typeof console && console.warn && console.warn(u(e, t, a, n)), d(e[t][a])
     }, s = (e, r, t) => {
         var a = e[r];
         return (r = Object.keys(a).reduce(((e, r) => !o(t, r) || e && !n(e, r) ? e : r), 0)) && a[r]
-    }, d = e => (e.loaded = 1, e.get()), p = (c = e => function(r, t, n, a) {
+    }, d = e => (e.loaded = 1, e.get()), c = (p = e => function(r, t, n, a) {
         var o = w.I(r);
         return o && o.then ? o.then(e.bind(e, r, w.S[r], t, n, a)) : e(r, w.S[r], t, n, a)
-    })(((e, r, t, n) => (l(e, t), f(r, 0, t, n)))), h = c(((e, r, t, n, a) => {
+    })(((e, r, t, n) => (l(e, t), f(r, 0, t, n)))), h = p(((e, r, t, n, a) => {
         var o = r && w.o(r, t) && s(r, t, n);
         return o ? d(o) : a()
-    })), v = {}, y = {
-        33: () => p("default", "@jupyterlab/apputils", [1, 3, 6, 3]),
-        123: () => p("default", "@jupyterlab/notebook", [1, 3, 6, 3]),
-        142: () => p("default", "@jupyterlab/coreutils", [1, 5, 6, 3]),
-        271: () => p("default", "react", [1, 17, 0, 1]),
-        344: () => p("default", "@jupyterlab/mainmenu", [1, 3, 6, 3]),
+    })), b = {}, v = {
+        29: () => c("default", "react", [1, 18, 2, 0]),
+        144: () => c("default", "@lumino/widgets", [1, 2, 0, 0]),
+        281: () => c("default", "@jupyterlab/coreutils", [1, 6, 0, 0, , "beta", 0]),
+        530: () => c("default", "@jupyterlab/services", [1, 7, 0, 0, , "beta", 0]),
+        551: () => c("default", "@jupyterlab/mainmenu", [1, 4, 0, 0, , "beta", 0]),
         569: () => h("default", "jquery", [1, 3, 5, 0], (() => w.e(638).then((() => () => w(638))))),
-        820: () => p("default", "@jupyterlab/services", [1, 6, 6, 3]),
-        832: () => p("default", "@lumino/widgets", [1, 1, 37, 2])
-    }, g = {
-        56: [33, 123, 142, 271, 344, 569, 820, 832]
+        598: () => c("default", "@jupyterlab/notebook", [1, 4, 0, 0, , "beta", 0]),
+        678: () => c("default", "@jupyterlab/apputils", [1, 4, 0, 0, , "beta", 0])
+    }, y = {
+        56: [29, 144, 281, 530, 551, 569, 598, 678]
     }, w.f.consumes = (e, r) => {
-        w.o(g, e) && g[e].forEach((e => {
-            if (w.o(v, e)) return r.push(v[e]);
+        w.o(y, e) && y[e].forEach((e => {
+            if (w.o(b, e)) return r.push(b[e]);
             var t = r => {
-                    v[e] = 0, w.m[e] = t => {
+                    b[e] = 0, w.m[e] = t => {
                         delete w.c[e], t.exports = r()
                     }
                 },
                 n = r => {
-                    delete v[e], w.m[e] = t => {
+                    delete b[e], w.m[e] = t => {
                         throw delete w.c[e], r
                     }
                 };
             try {
-                var a = y[e]();
-                a.then ? r.push(v[e] = a.then(t).catch(n)) : t(a)
+                var a = v[e]();
+                a.then ? r.push(b[e] = a.then(t).catch(n)) : t(a)
             } catch (e) {
                 n(e)
             }
         }))
     }, (() => {
         var e = {
             567: 0
```

### Comparing `jupyterlab_nbgallery-2.0.0a3/labextension/gallerymenu/static/third-party-licenses.json` & `jupyterlab_nbgallery-2.0.0a4/labextension/gallerymenu/static/third-party-licenses.json`

 * *Files identical despite different names*

### Comparing `jupyterlab_nbgallery-2.0.0a3/labextension/inject-uuid/package.json` & `jupyterlab_nbgallery-2.0.0a4/labextension/instrumentation/package.json`

 * *Files 7% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9150122549019608%*

 * *Differences: {"'dependencies'": "{'@jupyterlab/coreutils': '>=5.2.0', 'ts-md5': '^1.2.9'}",*

 * * "'description'": "'Track cell execution Metrics'",*

 * * "'files'": "{insert: [(2, 'schema/**/*.json')]}",*

 * * "'jupyterlab'": "{'outputDir': '../labextension/instrumentation', '_build': {'load': "*

 * *                 "'static/remoteEntry.ae4d1ce402e6ac0dddb5.js'}}",*

 * * "'name'": "'@jupyterlab-nbgallery/instrumentation'"}*

```diff
@@ -1,18 +1,20 @@
 {
     "author": "Team@NBG",
     "bugs": {
         "url": "https://github.com/nbgallery/lab-extensions/issues"
     },
     "dependencies": {
         "@jupyterlab/application": ">=3.6.0",
+        "@jupyterlab/coreutils": ">=5.2.0",
         "@jupyterlab/settingregistry": ">=3.6.0",
-        "jquery": "^3.5.0"
+        "jquery": "^3.5.0",
+        "ts-md5": "^1.2.9"
     },
-    "description": "Inject the notebook UUID into the kernel.",
+    "description": "Track cell execution Metrics",
     "devDependencies": {
         "@jupyterlab/builder": ">=3.3.2",
         "@types/jquery": "^3.5.0",
         "@typescript-eslint/eslint-plugin": "^4.8.1",
         "@typescript-eslint/parser": "^4.8.1",
         "eslint": "^8.0.0",
         "eslint-config-prettier": "^6.15.0",
@@ -21,34 +23,35 @@
         "eslint-plugin-react": "^7.18.3",
         "npm-run-all": "^4.1.5",
         "rimraf": "^3.0.2",
         "typescript": "~4.1.3"
     },
     "files": [
         "lib/**/*.{d.ts,eot,gif,html,jpg,js,js.map,json,png,svg,woff2,ttf}",
-        "style/**/*.{css,eot,gif,html,jpg,json,png,svg,woff2,ttf}"
+        "style/**/*.{css,eot,gif,html,jpg,json,png,svg,woff2,ttf}",
+        "schema/**/*.json"
     ],
     "homepage": "https://github.com/nbgallery/lab-extensions",
     "jupyterlab": {
         "_build": {
             "extension": "./extension",
-            "load": "static/remoteEntry.02ddda09f0305fa467f4.js"
+            "load": "static/remoteEntry.ae4d1ce402e6ac0dddb5.js"
         },
         "extension": true,
-        "outputDir": "../labextension/inject-uuid",
+        "outputDir": "../labextension/instrumentation",
         "schemaDir": "schema"
     },
     "keywords": [
         "jupyter",
         "jupyterlab",
         "jupyterlab-extension"
     ],
     "license": "MIT",
     "main": "lib/index.js",
-    "name": "@jupyterlab-nbgallery/inject-uuid",
+    "name": "@jupyterlab-nbgallery/instrumentation",
     "repository": {
         "type": "git",
         "url": "https://github.com/nbgallery/lab-extensions"
     },
     "scripts": {
         "build": "jlpm run build:lib && jlpm run build:labextension:dev",
         "build:all": "jlpm run build:prod",
```

### Comparing `jupyterlab_nbgallery-2.0.0a3/labextension/inject-uuid/schemas/@jupyterlab-nbgallery/inject-uuid/package.json.orig` & `jupyterlab_nbgallery-2.0.0a4/labextension/instrumentation/schemas/@jupyterlab-nbgallery/instrumentation/package.json.orig`

 * *Files 4% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9147058823529411%*

 * *Differences: {"'dependencies'": "{'@jupyterlab/coreutils': '>=5.2.0', 'ts-md5': '^1.2.9'}",*

 * * "'description'": "'Track cell execution Metrics'",*

 * * "'files'": "{insert: [(2, 'schema/**/*.json')]}",*

 * * "'jupyterlab'": "{'outputDir': '../labextension/instrumentation'}",*

 * * "'name'": "'@jupyterlab-nbgallery/instrumentation'"}*

```diff
@@ -1,18 +1,20 @@
 {
     "author": "Team@NBG",
     "bugs": {
         "url": "https://github.com/nbgallery/lab-extensions/issues"
     },
     "dependencies": {
         "@jupyterlab/application": ">=3.6.0",
+        "@jupyterlab/coreutils": ">=5.2.0",
         "@jupyterlab/settingregistry": ">=3.6.0",
-        "jquery": "^3.5.0"
+        "jquery": "^3.5.0",
+        "ts-md5": "^1.2.9"
     },
-    "description": "Inject the notebook UUID into the kernel.",
+    "description": "Track cell execution Metrics",
     "devDependencies": {
         "@jupyterlab/builder": ">=3.3.2",
         "@types/jquery": "^3.5.0",
         "@typescript-eslint/eslint-plugin": "^4.8.1",
         "@typescript-eslint/parser": "^4.8.1",
         "eslint": "^8.0.0",
         "eslint-config-prettier": "^6.15.0",
@@ -21,30 +23,31 @@
         "eslint-plugin-react": "^7.18.3",
         "npm-run-all": "^4.1.5",
         "rimraf": "^3.0.2",
         "typescript": "~4.1.3"
     },
     "files": [
         "lib/**/*.{d.ts,eot,gif,html,jpg,js,js.map,json,png,svg,woff2,ttf}",
-        "style/**/*.{css,eot,gif,html,jpg,json,png,svg,woff2,ttf}"
+        "style/**/*.{css,eot,gif,html,jpg,json,png,svg,woff2,ttf}",
+        "schema/**/*.json"
     ],
     "homepage": "https://github.com/nbgallery/lab-extensions",
     "jupyterlab": {
         "extension": true,
-        "outputDir": "../labextension/inject-uuid",
+        "outputDir": "../labextension/instrumentation",
         "schemaDir": "schema"
     },
     "keywords": [
         "jupyter",
         "jupyterlab",
         "jupyterlab-extension"
     ],
     "license": "MIT",
     "main": "lib/index.js",
-    "name": "@jupyterlab-nbgallery/inject-uuid",
+    "name": "@jupyterlab-nbgallery/instrumentation",
     "repository": {
         "type": "git",
         "url": "https://github.com/nbgallery/lab-extensions"
     },
     "scripts": {
         "build": "jlpm run build:lib && jlpm run build:labextension:dev",
         "build:all": "jlpm run build:prod",
```

### Comparing `jupyterlab_nbgallery-2.0.0a3/labextension/inject-uuid/static/568.1dcbb7bee8ca1152cf60.js` & `jupyterlab_nbgallery-2.0.0a4/labextension/inject-uuid/static/568.0616ffe42e5ee3230288.js`

 * *Files 0% similar despite different names*

#### js-beautify {}

```diff
@@ -25,15 +25,15 @@
             }
             o.r(t), o.d(t, {
                 default: () => r
             });
             const r = {
                 id: "@jupyterlab-nbgallery/inject-uuid",
                 autoStart: !0,
-                requires: [o(123).INotebookTracker],
+                requires: [o(598).INotebookTracker],
                 activate: (e, t) => {
                     t.forEach(n), t.widgetAdded.connect(((e, t) => n(t)))
                 }
             }
         }
     }
 ]);
```

### Comparing `jupyterlab_nbgallery-2.0.0a3/labextension/inject-uuid/static/remoteEntry.02ddda09f0305fa467f4.js` & `jupyterlab_nbgallery-2.0.0a4/labextension/inject-uuid/static/remoteEntry.6def7b207d91856938f3.js`

 * *Files 6% similar despite different names*

#### js-beautify {}

```diff
@@ -1,11 +1,11 @@
 var _JUPYTERLAB;
 (() => {
     "use strict";
-    var e, r, t, n, o, a, i, u, l, f, s, d, p, c, h, v = {
+    var e, r, t, n, o, a, i, u, l, s, d, f, p, c, h, v = {
             711: (e, r, t) => {
                 var n = {
                         "./index": () => t.e(568).then((() => () => t(568))),
                         "./extension": () => t.e(568).then((() => () => t(568)))
                     },
                     o = (e, r) => (t.R = r, r = t.o(n, e) ? n[e]() : Promise.resolve().then((() => {
                         throw new Error('Module "' + e + '" does not exist in container.')
@@ -40,44 +40,44 @@
             a: r
         }), r
     }, g.d = (e, r) => {
         for (var t in r) g.o(r, t) && !g.o(e, t) && Object.defineProperty(e, t, {
             enumerable: !0,
             get: r[t]
         })
-    }, g.f = {}, g.e = e => Promise.all(Object.keys(g.f).reduce(((r, t) => (g.f[t](e, r), r)), [])), g.u = e => e + ".1dcbb7bee8ca1152cf60.js?v=1dcbb7bee8ca1152cf60", g.g = function() {
+    }, g.f = {}, g.e = e => Promise.all(Object.keys(g.f).reduce(((r, t) => (g.f[t](e, r), r)), [])), g.u = e => e + ".0616ffe42e5ee3230288.js?v=0616ffe42e5ee3230288", g.g = function() {
         if ("object" == typeof globalThis) return globalThis;
         try {
             return this || new Function("return this")()
         } catch (e) {
             if ("object" == typeof window) return window
         }
     }(), g.o = (e, r) => Object.prototype.hasOwnProperty.call(e, r), e = {}, r = "@jupyterlab-nbgallery/inject-uuid:", g.l = (t, n, o, a) => {
         if (e[t]) e[t].push(n);
         else {
             var i, u;
             if (void 0 !== o)
-                for (var l = document.getElementsByTagName("script"), f = 0; f < l.length; f++) {
-                    var s = l[f];
-                    if (s.getAttribute("src") == t || s.getAttribute("data-webpack") == r + o) {
-                        i = s;
+                for (var l = document.getElementsByTagName("script"), s = 0; s < l.length; s++) {
+                    var d = l[s];
+                    if (d.getAttribute("src") == t || d.getAttribute("data-webpack") == r + o) {
+                        i = d;
                         break
                     }
                 }
             i || (u = !0, (i = document.createElement("script")).charset = "utf-8", i.timeout = 120, g.nc && i.setAttribute("nonce", g.nc), i.setAttribute("data-webpack", r + o), i.src = t), e[t] = [n];
-            var d = (r, n) => {
+            var f = (r, n) => {
                     i.onerror = i.onload = null, clearTimeout(p);
                     var o = e[t];
                     if (delete e[t], i.parentNode && i.parentNode.removeChild(i), o && o.forEach((e => e(n))), r) return r(n)
                 },
-                p = setTimeout(d.bind(null, void 0, {
+                p = setTimeout(f.bind(null, void 0, {
                     type: "timeout",
                     target: i
                 }), 12e4);
-            i.onerror = d.bind(null, i.onerror), i.onload = d.bind(null, i.onload), u && document.head.appendChild(i)
+            i.onerror = f.bind(null, i.onerror), i.onload = f.bind(null, i.onload), u && document.head.appendChild(i)
         }
     }, g.r = e => {
         "undefined" != typeof Symbol && Symbol.toStringTag && Object.defineProperty(e, Symbol.toStringTag, {
             value: "Module"
         }), Object.defineProperty(e, "__esModule", {
             value: !0
         })
@@ -155,33 +155,33 @@
     }, a = (e, r) => {
         if (0 in e) {
             r = t(r);
             var n = e[0],
                 o = n < 0;
             o && (n = -n - 1);
             for (var i = 0, u = 1, l = !0;; u++, i++) {
-                var f, s, d = u < e.length ? (typeof e[u])[0] : "";
-                if (i >= r.length || "o" == (s = (typeof(f = r[i]))[0])) return !l || ("u" == d ? u > n && !o : "" == d != o);
-                if ("u" == s) {
-                    if (!l || "u" != d) return !1
+                var s, d, f = u < e.length ? (typeof e[u])[0] : "";
+                if (i >= r.length || "o" == (d = (typeof(s = r[i]))[0])) return !l || ("u" == f ? u > n && !o : "" == f != o);
+                if ("u" == d) {
+                    if (!l || "u" != f) return !1
                 } else if (l)
-                    if (d == s)
+                    if (f == d)
                         if (u <= n) {
-                            if (f != e[u]) return !1
+                            if (s != e[u]) return !1
                         } else {
-                            if (o ? f > e[u] : f < e[u]) return !1;
-                            f != e[u] && (l = !1)
+                            if (o ? s > e[u] : s < e[u]) return !1;
+                            s != e[u] && (l = !1)
                         }
-                else if ("s" != d && "n" != d) {
+                else if ("s" != f && "n" != f) {
                     if (o || u <= n) return !1;
                     l = !1, u--
                 } else {
-                    if (u <= n || s < d != o) return !1;
+                    if (u <= n || d < f != o) return !1;
                     l = !1
-                } else "s" != d && "n" != d && (l = !1, u--)
+                } else "s" != f && "n" != f && (l = !1, u--)
             }
         }
         var p = [],
             c = p.pop.bind(p);
         for (i = 1; i < e.length; i++) {
             var h = e[i];
             p.push(1 == h ? c() | c() : 2 == h ? c() & c() : h ? a(h, r) : !c())
@@ -190,24 +190,24 @@
     }, i = (e, r) => {
         var t = g.S[e];
         if (!t || !g.o(t, r)) throw new Error("Shared module " + r + " doesn't exist in shared scope " + e);
         return t
     }, u = (e, r) => {
         var t = e[r];
         return Object.keys(t).reduce(((e, r) => !e || !t[e].loaded && n(e, r) ? r : e), 0)
-    }, l = (e, r, t, n) => "Unsatisfied version " + t + " from " + (t && e[r][t].from) + " of shared singleton module " + r + " (required " + o(n) + ")", f = (e, r, t, n) => {
+    }, l = (e, r, t, n) => "Unsatisfied version " + t + " from " + (t && e[r][t].from) + " of shared singleton module " + r + " (required " + o(n) + ")", s = (e, r, t, n) => {
         var o = u(e, t);
-        return a(n, o) || "undefined" != typeof console && console.warn && console.warn(l(e, t, o, n)), s(e[t][o])
-    }, s = e => (e.loaded = 1, e.get()), d = (e => function(r, t, n, o) {
+        return a(n, o) || "undefined" != typeof console && console.warn && console.warn(l(e, t, o, n)), d(e[t][o])
+    }, d = e => (e.loaded = 1, e.get()), f = (e => function(r, t, n, o) {
         var a = g.I(r);
         return a && a.then ? a.then(e.bind(e, r, g.S[r], t, n, o)) : e(r, g.S[r], t, n)
-    })(((e, r, t, n) => (i(e, t), f(r, 0, t, n)))), p = {}, c = {
-        123: () => d("default", "@jupyterlab/notebook", [1, 3, 6, 3])
+    })(((e, r, t, n) => (i(e, t), s(r, 0, t, n)))), p = {}, c = {
+        598: () => f("default", "@jupyterlab/notebook", [1, 4, 0, 0, , "beta", 0])
     }, h = {
-        568: [123]
+        568: [598]
     }, g.f.consumes = (e, r) => {
         g.o(h, e) && h[e].forEach((e => {
             if (g.o(p, e)) return r.push(p[e]);
             var t = r => {
                     p[e] = 0, g.m[e] = t => {
                         delete g.c[e], t.exports = r()
                     }
```

### Comparing `jupyterlab_nbgallery-2.0.0a3/labextension/instrumentation/package.json` & `jupyterlab_nbgallery-2.0.0a4/labextension/environment-registration/schemas/@jupyterlab-nbgallery/environment-registration/package.json.orig`

 * *Files 4% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.8451388888888889%*

 * *Differences: {"'dependencies'": "{delete: ['ts-md5']}",*

 * * "'description'": "'Register NBGallery Environment'",*

 * * "'jupyterlab'": "{'outputDir': '../labextension/environment-registration', delete: ['_build']}",*

 * * "'name'": "'@jupyterlab-nbgallery/environment-registration'",*

 * * "'style'": "'style/index.css'",*

 * * "'version'": "'1.0.3'"}*

```diff
@@ -3,18 +3,17 @@
     "bugs": {
         "url": "https://github.com/nbgallery/lab-extensions/issues"
     },
     "dependencies": {
         "@jupyterlab/application": ">=3.6.0",
         "@jupyterlab/coreutils": ">=5.2.0",
         "@jupyterlab/settingregistry": ">=3.6.0",
-        "jquery": "^3.5.0",
-        "ts-md5": "^1.2.9"
+        "jquery": "^3.5.0"
     },
-    "description": "Track cell execution Metrics",
+    "description": "Register NBGallery Environment",
     "devDependencies": {
         "@jupyterlab/builder": ">=3.3.2",
         "@types/jquery": "^3.5.0",
         "@typescript-eslint/eslint-plugin": "^4.8.1",
         "@typescript-eslint/parser": "^4.8.1",
         "eslint": "^8.0.0",
         "eslint-config-prettier": "^6.15.0",
@@ -28,30 +27,26 @@
     "files": [
         "lib/**/*.{d.ts,eot,gif,html,jpg,js,js.map,json,png,svg,woff2,ttf}",
         "style/**/*.{css,eot,gif,html,jpg,json,png,svg,woff2,ttf}",
         "schema/**/*.json"
     ],
     "homepage": "https://github.com/nbgallery/lab-extensions",
     "jupyterlab": {
-        "_build": {
-            "extension": "./extension",
-            "load": "static/remoteEntry.53ed33a8ef1f603e0fc8.js"
-        },
         "extension": true,
-        "outputDir": "../labextension/instrumentation",
+        "outputDir": "../labextension/environment-registration",
         "schemaDir": "schema"
     },
     "keywords": [
         "jupyter",
         "jupyterlab",
         "jupyterlab-extension"
     ],
     "license": "MIT",
     "main": "lib/index.js",
-    "name": "@jupyterlab-nbgallery/instrumentation",
+    "name": "@jupyterlab-nbgallery/environment-registration",
     "repository": {
         "type": "git",
         "url": "https://github.com/nbgallery/lab-extensions"
     },
     "scripts": {
         "build": "jlpm run build:lib && jlpm run build:labextension:dev",
         "build:all": "jlpm run build:prod",
@@ -69,10 +64,11 @@
         "install-ext": "jlpm run build",
         "watch:labextension": "jupyter labextension watch .",
         "watch:src": "tsc -w"
     },
     "sideEffects": [
         "style/*.css"
     ],
+    "style": "style/index.css",
     "types": "lib/index.d.ts",
-    "version": "2.0.0"
+    "version": "1.0.3"
 }
```

### Comparing `jupyterlab_nbgallery-2.0.0a3/labextension/instrumentation/schemas/@jupyterlab-nbgallery/instrumentation/package.json.orig` & `jupyterlab_nbgallery-2.0.0a4/labextension/autodownload/package.json`

 * *Files 17% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.8451388888888889%*

 * *Differences: {"'dependencies'": "{delete: ['ts-md5']}",*

 * * "'description'": "'NBGallery Auto Download Notebooks that are starred or recently executed'",*

 * * "'jupyterlab'": "{'outputDir': '../labextension/autodownload', '_build': OrderedDict([('load', "*

 * *                 "'static/remoteEntry.1353121aacb4a50d2fe1.js'), ('extension', './extension'), "*

 * *                 "('style', './style')])}",*

 * * "'name'": "'@jupyterlab-nbgallery/autodownload'",*

 * * "'style'": "'style/index.css'",*

 * * "'version'": "'1.0.3'"}*

```diff
@@ -3,18 +3,17 @@
     "bugs": {
         "url": "https://github.com/nbgallery/lab-extensions/issues"
     },
     "dependencies": {
         "@jupyterlab/application": ">=3.6.0",
         "@jupyterlab/coreutils": ">=5.2.0",
         "@jupyterlab/settingregistry": ">=3.6.0",
-        "jquery": "^3.5.0",
-        "ts-md5": "^1.2.9"
+        "jquery": "^3.5.0"
     },
-    "description": "Track cell execution Metrics",
+    "description": "NBGallery Auto Download Notebooks that are starred or recently executed",
     "devDependencies": {
         "@jupyterlab/builder": ">=3.3.2",
         "@types/jquery": "^3.5.0",
         "@typescript-eslint/eslint-plugin": "^4.8.1",
         "@typescript-eslint/parser": "^4.8.1",
         "eslint": "^8.0.0",
         "eslint-config-prettier": "^6.15.0",
@@ -28,26 +27,31 @@
     "files": [
         "lib/**/*.{d.ts,eot,gif,html,jpg,js,js.map,json,png,svg,woff2,ttf}",
         "style/**/*.{css,eot,gif,html,jpg,json,png,svg,woff2,ttf}",
         "schema/**/*.json"
     ],
     "homepage": "https://github.com/nbgallery/lab-extensions",
     "jupyterlab": {
+        "_build": {
+            "extension": "./extension",
+            "load": "static/remoteEntry.1353121aacb4a50d2fe1.js",
+            "style": "./style"
+        },
         "extension": true,
-        "outputDir": "../labextension/instrumentation",
+        "outputDir": "../labextension/autodownload",
         "schemaDir": "schema"
     },
     "keywords": [
         "jupyter",
         "jupyterlab",
         "jupyterlab-extension"
     ],
     "license": "MIT",
     "main": "lib/index.js",
-    "name": "@jupyterlab-nbgallery/instrumentation",
+    "name": "@jupyterlab-nbgallery/autodownload",
     "repository": {
         "type": "git",
         "url": "https://github.com/nbgallery/lab-extensions"
     },
     "scripts": {
         "build": "jlpm run build:lib && jlpm run build:labextension:dev",
         "build:all": "jlpm run build:prod",
@@ -65,10 +69,11 @@
         "install-ext": "jlpm run build",
         "watch:labextension": "jupyter labextension watch .",
         "watch:src": "tsc -w"
     },
     "sideEffects": [
         "style/*.css"
     ],
+    "style": "style/index.css",
     "types": "lib/index.d.ts",
-    "version": "2.0.0"
+    "version": "1.0.3"
 }
```

### Comparing `jupyterlab_nbgallery-2.0.0a3/labextension/instrumentation/static/568.0d3998aabd22f1867c40.js` & `jupyterlab_nbgallery-2.0.0a4/labextension/instrumentation/static/568.7f1ab65a55b54297cd7b.js`

 * *Files 6% similar despite different names*

#### js-beautify {}

```diff
@@ -1,18 +1,18 @@
 "use strict";
 (self.webpackChunk_jupyterlab_nbgallery_instrumentation = self.webpackChunk_jupyterlab_nbgallery_instrumentation || []).push([
     [568], {
         568: (e, t, n) => {
             n.r(t), n.d(t, {
                 default: () => u
             });
-            var l = n(38),
-                o = n(142),
-                i = n(123),
-                a = n(191),
+            var l = n(225),
+                o = n(281),
+                i = n(598),
+                a = n(941),
                 s = n(24),
                 c = n(569),
                 r = n.n(c);
             const u = {
                 id: "@juptyerlab-nbgallery/instrumentation",
                 autoStart: !0,
                 requires: [l.ISettingRegistry],
```

### Comparing `jupyterlab_nbgallery-2.0.0a3/labextension/instrumentation/static/638.b95125ed695cee42aae4.js` & `jupyterlab_nbgallery-2.0.0a4/labextension/instrumentation/static/638.b95125ed695cee42aae4.js`

 * *Files identical despite different names*

### Comparing `jupyterlab_nbgallery-2.0.0a3/labextension/instrumentation/static/701.d81800f5926ab62cc8b2.js` & `jupyterlab_nbgallery-2.0.0a4/labextension/instrumentation/static/701.d81800f5926ab62cc8b2.js`

 * *Files identical despite different names*

### Comparing `jupyterlab_nbgallery-2.0.0a3/labextension/instrumentation/static/remoteEntry.53ed33a8ef1f603e0fc8.js` & `jupyterlab_nbgallery-2.0.0a4/labextension/instrumentation/static/remoteEntry.ae4d1ce402e6ac0dddb5.js`

 * *Files 10% similar despite different names*

#### js-beautify {}

```diff
@@ -1,11 +1,11 @@
 var _JUPYTERLAB;
 (() => {
     "use strict";
-    var e, r, t, n, a, o, i, u, l, s, f, d, c, p, h, v, b, y, g, m, w, j, S = {
+    var e, r, t, n, a, o, i, u, l, s, d, f, c, p, h, v, b, y, g, m, w, j, S = {
             250: (e, r, t) => {
                 var n = {
                         "./index": () => t.e(568).then((() => () => t(568))),
                         "./extension": () => t.e(568).then((() => () => t(568)))
                     },
                     a = (e, r) => (t.R = r, r = t.o(n, e) ? n[e]() : Promise.resolve().then((() => {
                         throw new Error('Module "' + e + '" does not exist in container.')
@@ -41,19 +41,19 @@
         }), r
     }, E.d = (e, r) => {
         for (var t in r) E.o(r, t) && !E.o(e, t) && Object.defineProperty(e, t, {
             enumerable: !0,
             get: r[t]
         })
     }, E.f = {}, E.e = e => Promise.all(Object.keys(E.f).reduce(((r, t) => (E.f[t](e, r), r)), [])), E.u = e => e + "." + {
-        568: "0d3998aabd22f1867c40",
+        568: "7f1ab65a55b54297cd7b",
         638: "b95125ed695cee42aae4",
         701: "d81800f5926ab62cc8b2"
     } [e] + ".js?v=" + {
-        568: "0d3998aabd22f1867c40",
+        568: "7f1ab65a55b54297cd7b",
         638: "b95125ed695cee42aae4",
         701: "d81800f5926ab62cc8b2"
     } [e], E.g = function() {
         if ("object" == typeof globalThis) return globalThis;
         try {
             return this || new Function("return this")()
         } catch (e) {
@@ -61,31 +61,31 @@
         }
     }(), E.o = (e, r) => Object.prototype.hasOwnProperty.call(e, r), e = {}, r = "@jupyterlab-nbgallery/instrumentation:", E.l = (t, n, a, o) => {
         if (e[t]) e[t].push(n);
         else {
             var i, u;
             if (void 0 !== a)
                 for (var l = document.getElementsByTagName("script"), s = 0; s < l.length; s++) {
-                    var f = l[s];
-                    if (f.getAttribute("src") == t || f.getAttribute("data-webpack") == r + a) {
-                        i = f;
+                    var d = l[s];
+                    if (d.getAttribute("src") == t || d.getAttribute("data-webpack") == r + a) {
+                        i = d;
                         break
                     }
                 }
             i || (u = !0, (i = document.createElement("script")).charset = "utf-8", i.timeout = 120, E.nc && i.setAttribute("nonce", E.nc), i.setAttribute("data-webpack", r + a), i.src = t), e[t] = [n];
-            var d = (r, n) => {
+            var f = (r, n) => {
                     i.onerror = i.onload = null, clearTimeout(c);
                     var a = e[t];
                     if (delete e[t], i.parentNode && i.parentNode.removeChild(i), a && a.forEach((e => e(n))), r) return r(n)
                 },
-                c = setTimeout(d.bind(null, void 0, {
+                c = setTimeout(f.bind(null, void 0, {
                     type: "timeout",
                     target: i
                 }), 12e4);
-            i.onerror = d.bind(null, i.onerror), i.onload = d.bind(null, i.onload), u && document.head.appendChild(i)
+            i.onerror = f.bind(null, i.onerror), i.onload = f.bind(null, i.onload), u && document.head.appendChild(i)
         }
     }, E.r = e => {
         "undefined" != typeof Symbol && Symbol.toStringTag && Object.defineProperty(e, Symbol.toStringTag, {
             value: "Module"
         }), Object.defineProperty(e, "__esModule", {
             value: !0
         })
@@ -164,33 +164,33 @@
     }, o = (e, r) => {
         if (0 in e) {
             r = t(r);
             var n = e[0],
                 a = n < 0;
             a && (n = -n - 1);
             for (var i = 0, u = 1, l = !0;; u++, i++) {
-                var s, f, d = u < e.length ? (typeof e[u])[0] : "";
-                if (i >= r.length || "o" == (f = (typeof(s = r[i]))[0])) return !l || ("u" == d ? u > n && !a : "" == d != a);
-                if ("u" == f) {
-                    if (!l || "u" != d) return !1
+                var s, d, f = u < e.length ? (typeof e[u])[0] : "";
+                if (i >= r.length || "o" == (d = (typeof(s = r[i]))[0])) return !l || ("u" == f ? u > n && !a : "" == f != a);
+                if ("u" == d) {
+                    if (!l || "u" != f) return !1
                 } else if (l)
-                    if (d == f)
+                    if (f == d)
                         if (u <= n) {
                             if (s != e[u]) return !1
                         } else {
                             if (a ? s > e[u] : s < e[u]) return !1;
                             s != e[u] && (l = !1)
                         }
-                else if ("s" != d && "n" != d) {
+                else if ("s" != f && "n" != f) {
                     if (a || u <= n) return !1;
                     l = !1, u--
                 } else {
-                    if (u <= n || f < d != a) return !1;
+                    if (u <= n || d < f != a) return !1;
                     l = !1
-                } else "s" != d && "n" != d && (l = !1, u--)
+                } else "s" != f && "n" != f && (l = !1, u--)
             }
         }
         var c = [],
             p = c.pop.bind(c);
         for (i = 1; i < e.length; i++) {
             var h = e[i];
             c.push(1 == h ? p() | p() : 2 == h ? p() & p() : h ? o(h, r) : !p())
@@ -202,40 +202,40 @@
         return t
     }, u = (e, r) => {
         var t = e[r];
         return (r = Object.keys(t).reduce(((e, r) => !e || n(e, r) ? r : e), 0)) && t[r]
     }, l = (e, r) => {
         var t = e[r];
         return Object.keys(t).reduce(((e, r) => !e || !t[e].loaded && n(e, r) ? r : e), 0)
-    }, s = (e, r, t, n) => "Unsatisfied version " + t + " from " + (t && e[r][t].from) + " of shared singleton module " + r + " (required " + a(n) + ")", f = (e, r, t, n) => {
+    }, s = (e, r, t, n) => "Unsatisfied version " + t + " from " + (t && e[r][t].from) + " of shared singleton module " + r + " (required " + a(n) + ")", d = (e, r, t, n) => {
         var a = l(e, t);
         return o(n, a) || "undefined" != typeof console && console.warn && console.warn(s(e, t, a, n)), h(e[t][a])
-    }, d = (e, r, t) => {
+    }, f = (e, r, t) => {
         var a = e[r];
         return (r = Object.keys(a).reduce(((e, r) => !o(t, r) || e && !n(e, r) ? e : r), 0)) && a[r]
     }, c = (e, r, t, n) => {
         var o = e[t];
         return "No satisfying version (" + a(n) + ") of shared module " + t + " found in shared scope " + r + ".\nAvailable versions: " + Object.keys(o).map((e => e + " from " + o[e].from)).join(", ")
     }, p = (e, r, t, n) => {
         "undefined" != typeof console && console.warn && console.warn(c(e, r, t, n))
     }, h = e => (e.loaded = 1, e.get()), b = (v = e => function(r, t, n, a) {
         var o = E.I(r);
         return o && o.then ? o.then(e.bind(e, r, E.S[r], t, n, a)) : e(r, E.S[r], t, n, a)
-    })(((e, r, t, n) => (i(e, t), h(d(r, t, n) || p(r, e, t, n) || u(r, t))))), y = v(((e, r, t, n) => (i(e, t), f(r, 0, t, n)))), g = v(((e, r, t, n, a) => {
-        var o = r && E.o(r, t) && d(r, t, n);
+    })(((e, r, t, n) => (i(e, t), h(f(r, t, n) || p(r, e, t, n) || u(r, t))))), y = v(((e, r, t, n) => (i(e, t), d(r, 0, t, n)))), g = v(((e, r, t, n, a) => {
+        var o = r && E.o(r, t) && f(r, t, n);
         return o ? h(o) : a()
     })), m = {}, w = {
         24: () => g("default", "ts-md5", [1, 1, 2, 9], (() => E.e(701).then((() => () => E(701))))),
-        38: () => y("default", "@jupyterlab/settingregistry", [1, 3, 6, 3]),
-        123: () => y("default", "@jupyterlab/notebook", [1, 3, 6, 3]),
-        142: () => y("default", "@jupyterlab/coreutils", [1, 5, 6, 3]),
-        191: () => b("default", "@jupyterlab/cells", [1, 3, 6, 3]),
-        569: () => g("default", "jquery", [1, 3, 5, 0], (() => E.e(638).then((() => () => E(638)))))
+        225: () => y("default", "@jupyterlab/settingregistry", [1, 4, 0, 0, , "beta", 0]),
+        281: () => y("default", "@jupyterlab/coreutils", [1, 6, 0, 0, , "beta", 0]),
+        569: () => g("default", "jquery", [1, 3, 5, 0], (() => E.e(638).then((() => () => E(638))))),
+        598: () => y("default", "@jupyterlab/notebook", [1, 4, 0, 0, , "beta", 0]),
+        941: () => b("default", "@jupyterlab/cells", [1, 4, 0, 0, , "beta", 0])
     }, j = {
-        568: [24, 38, 123, 142, 191, 569]
+        568: [24, 225, 281, 569, 598, 941]
     }, E.f.consumes = (e, r) => {
         E.o(j, e) && j[e].forEach((e => {
             if (E.o(m, e)) return r.push(m[e]);
             var t = r => {
                     m[e] = 0, E.m[e] = t => {
                         delete E.c[e], t.exports = r()
                     }
```

### Comparing `jupyterlab_nbgallery-2.0.0a3/labextension/instrumentation/static/third-party-licenses.json` & `jupyterlab_nbgallery-2.0.0a4/labextension/instrumentation/static/third-party-licenses.json`

 * *Files identical despite different names*

### Comparing `jupyterlab_nbgallery-2.0.0a3/labextension/userpreferences/package.json` & `jupyterlab_nbgallery-2.0.0a4/labextension/userpreferences/package.json`

 * *Files 5% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9994212962962963%*

 * *Differences: {"'jupyterlab'": "{'_build': {'load': 'static/remoteEntry.3f8d9d3f425bc3ff0a80.js'}}"}*

```diff
@@ -31,15 +31,15 @@
         "style/**/*.{css,eot,gif,html,jpg,json,png,svg,woff2,ttf}",
         "schema/**/*.json"
     ],
     "homepage": "https://github.com/nbgallery/lab-extensions",
     "jupyterlab": {
         "_build": {
             "extension": "./extension",
-            "load": "static/remoteEntry.03bf745401d2317e1d7d.js",
+            "load": "static/remoteEntry.3f8d9d3f425bc3ff0a80.js",
             "style": "./style"
         },
         "extension": true,
         "outputDir": "../labextension/userpreferences",
         "schemaDir": "schema"
     },
     "keywords": [
```

### Comparing `jupyterlab_nbgallery-2.0.0a3/labextension/userpreferences/schemas/@jupyterlab-nbgallery/userpreferences/package.json.orig` & `jupyterlab_nbgallery-2.0.0a4/labextension/gallerymenu/schemas/@jupyterlab-nbgallery/gallerymenu/package.json.orig`

 * *Files 13% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9363425925925927%*

 * *Differences: {"'dependencies'": "{'@jupyterlab/mainmenu': '>=3.6.0'}",*

 * * "'devDependencies'": "{'@jupyterlab/builder': '>=3.6.0'}",*

 * * "'jupyterlab'": "{'outputDir': '../labextension/gallerymenu'}",*

 * * "'name'": "'@jupyterlab-nbgallery/gallerymenu'",*

 * * "'version'": "'2.0.0'"}*

```diff
@@ -1,23 +1,23 @@
 {
     "author": "Team@NBG",
     "bugs": {
         "url": "https://github.com/nbgallery/lab-extensions/issues"
     },
     "dependencies": {
         "@jupyterlab/application": ">=3.6.0",
-        "@jupyterlab/mainmenu": ">=3.6.0 ||",
+        "@jupyterlab/mainmenu": ">=3.6.0",
         "@jupyterlab/notebook": ">=3.6.0",
         "@jupyterlab/settingregistry": ">=3.6.0",
         "fa-icons": "^0.2.0",
         "jquery": "^3.5.0"
     },
     "description": "All the menu capabilities needed for saving/forking notebooks and submitting change request to Notebook Gallery",
     "devDependencies": {
-        "@jupyterlab/builder": ">=3.3.2",
+        "@jupyterlab/builder": ">=3.6.0",
         "@types/jquery": "^3.5.0",
         "@typescript-eslint/eslint-plugin": "^4.8.1",
         "@typescript-eslint/parser": "^4.8.1",
         "eslint": "^8.0.0",
         "eslint-config-prettier": "^6.15.0",
         "eslint-plugin-jsdoc": "^39.0.0",
         "eslint-plugin-prettier": "^3.1.4",
@@ -30,25 +30,25 @@
         "lib/**/*.{d.ts,eot,gif,html,jpg,js,js.map,json,png,svg,woff2,ttf}",
         "style/**/*.{css,eot,gif,html,jpg,json,png,svg,woff2,ttf}",
         "schema/**/*.json"
     ],
     "homepage": "https://github.com/nbgallery/lab-extensions",
     "jupyterlab": {
         "extension": true,
-        "outputDir": "../labextension/userpreferences",
+        "outputDir": "../labextension/gallerymenu",
         "schemaDir": "schema"
     },
     "keywords": [
         "jupyter",
         "jupyterlab",
         "jupyterlab-extension"
     ],
     "license": "MIT",
     "main": "lib/index.js",
-    "name": "@jupyterlab-nbgallery/userpreferences",
+    "name": "@jupyterlab-nbgallery/gallerymenu",
     "repository": {
         "type": "git",
         "url": "https://github.com/nbgallery/lab-extensions"
     },
     "scripts": {
         "build": "jlpm run build:lib && jlpm run build:labextension:dev",
         "build:all": "jlpm run build:prod",
@@ -68,9 +68,9 @@
         "watch:src": "tsc -w"
     },
     "sideEffects": [
         "style/*.css"
     ],
     "style": "style/index.css",
     "types": "lib/index.d.ts",
-    "version": "1.0.2"
+    "version": "2.0.0"
 }
```

### Comparing `jupyterlab_nbgallery-2.0.0a3/labextension/userpreferences/static/542.d1718a50e23f3808ba62.js` & `jupyterlab_nbgallery-2.0.0a4/labextension/userpreferences/static/542.d1718a50e23f3808ba62.js`

 * *Files identical despite different names*

### Comparing `jupyterlab_nbgallery-2.0.0a3/labextension/userpreferences/static/568.00695541aaa15d567580.js` & `jupyterlab_nbgallery-2.0.0a4/labextension/userpreferences/static/568.0ac7cbac0996e718a0d9.js`

 * *Files 2% similar despite different names*

#### js-beautify {}

```diff
@@ -1,19 +1,19 @@
 "use strict";
 (self.webpackChunk_jupyterlab_nbgallery_userpreferences = self.webpackChunk_jupyterlab_nbgallery_userpreferences || []).push([
     [568], {
         568: (e, r, t) => {
             t.r(r), t.d(r, {
                 default: () => p
             });
-            var a = t(344),
-                s = t(33),
-                n = t(832),
-                l = t(820),
-                o = t(142),
+            var a = t(551),
+                s = t(678),
+                n = t(144),
+                l = t(530),
+                o = t(281),
                 i = t(569),
                 c = t.n(i);
             const u = {
                 id: "@jupyterlab-nbgallery/userpreferences",
                 autoStart: !0,
                 requires: [a.IMainMenu],
                 activate: function(e, r) {
```

### Comparing `jupyterlab_nbgallery-2.0.0a3/labextension/userpreferences/static/638.e5080f99954048969f76.js` & `jupyterlab_nbgallery-2.0.0a4/labextension/userpreferences/static/638.e5080f99954048969f76.js`

 * *Files identical despite different names*

### Comparing `jupyterlab_nbgallery-2.0.0a3/labextension/userpreferences/static/remoteEntry.03bf745401d2317e1d7d.js` & `jupyterlab_nbgallery-2.0.0a4/labextension/userpreferences/static/remoteEntry.3f8d9d3f425bc3ff0a80.js`

 * *Files 7% similar despite different names*

#### js-beautify {}

```diff
@@ -1,11 +1,11 @@
 var _JUPYTERLAB;
 (() => {
     "use strict";
-    var e, r, t, n, a, o, i, u, l, s, f, p, c, d, h, v, b, g, y = {
+    var e, r, t, n, a, o, i, u, l, s, f, d, p, c, h, b, v, g, y = {
             130: (e, r, t) => {
                 var n = {
                         "./index": () => t.e(568).then((() => () => t(568))),
                         "./extension": () => t.e(568).then((() => () => t(568))),
                         "./style": () => t.e(542).then((() => () => t(542)))
                     },
                     a = (e, r) => (t.R = r, r = t.o(n, e) ? n[e]() : Promise.resolve().then((() => {
@@ -44,19 +44,19 @@
     }, w.d = (e, r) => {
         for (var t in r) w.o(r, t) && !w.o(e, t) && Object.defineProperty(e, t, {
             enumerable: !0,
             get: r[t]
         })
     }, w.f = {}, w.e = e => Promise.all(Object.keys(w.f).reduce(((r, t) => (w.f[t](e, r), r)), [])), w.u = e => e + "." + {
         542: "d1718a50e23f3808ba62",
-        568: "00695541aaa15d567580",
+        568: "0ac7cbac0996e718a0d9",
         638: "e5080f99954048969f76"
     } [e] + ".js?v=" + {
         542: "d1718a50e23f3808ba62",
-        568: "00695541aaa15d567580",
+        568: "0ac7cbac0996e718a0d9",
         638: "e5080f99954048969f76"
     } [e], w.g = function() {
         if ("object" == typeof globalThis) return globalThis;
         try {
             return this || new Function("return this")()
         } catch (e) {
             if ("object" == typeof window) return window
@@ -70,24 +70,24 @@
                     var f = l[s];
                     if (f.getAttribute("src") == t || f.getAttribute("data-webpack") == r + a) {
                         i = f;
                         break
                     }
                 }
             i || (u = !0, (i = document.createElement("script")).charset = "utf-8", i.timeout = 120, w.nc && i.setAttribute("nonce", w.nc), i.setAttribute("data-webpack", r + a), i.src = t), e[t] = [n];
-            var p = (r, n) => {
-                    i.onerror = i.onload = null, clearTimeout(c);
+            var d = (r, n) => {
+                    i.onerror = i.onload = null, clearTimeout(p);
                     var a = e[t];
                     if (delete e[t], i.parentNode && i.parentNode.removeChild(i), a && a.forEach((e => e(n))), r) return r(n)
                 },
-                c = setTimeout(p.bind(null, void 0, {
+                p = setTimeout(d.bind(null, void 0, {
                     type: "timeout",
                     target: i
                 }), 12e4);
-            i.onerror = p.bind(null, i.onerror), i.onload = p.bind(null, i.onload), u && document.head.appendChild(i)
+            i.onerror = d.bind(null, i.onerror), i.onload = d.bind(null, i.onload), u && document.head.appendChild(i)
         }
     }, w.r = e => {
         "undefined" != typeof Symbol && Symbol.toStringTag && Object.defineProperty(e, Symbol.toStringTag, {
             value: "Module"
         }), Object.defineProperty(e, "__esModule", {
             value: !0
         })
@@ -166,86 +166,86 @@
     }, o = (e, r) => {
         if (0 in e) {
             r = t(r);
             var n = e[0],
                 a = n < 0;
             a && (n = -n - 1);
             for (var i = 0, u = 1, l = !0;; u++, i++) {
-                var s, f, p = u < e.length ? (typeof e[u])[0] : "";
-                if (i >= r.length || "o" == (f = (typeof(s = r[i]))[0])) return !l || ("u" == p ? u > n && !a : "" == p != a);
+                var s, f, d = u < e.length ? (typeof e[u])[0] : "";
+                if (i >= r.length || "o" == (f = (typeof(s = r[i]))[0])) return !l || ("u" == d ? u > n && !a : "" == d != a);
                 if ("u" == f) {
-                    if (!l || "u" != p) return !1
+                    if (!l || "u" != d) return !1
                 } else if (l)
-                    if (p == f)
+                    if (d == f)
                         if (u <= n) {
                             if (s != e[u]) return !1
                         } else {
                             if (a ? s > e[u] : s < e[u]) return !1;
                             s != e[u] && (l = !1)
                         }
-                else if ("s" != p && "n" != p) {
+                else if ("s" != d && "n" != d) {
                     if (a || u <= n) return !1;
                     l = !1, u--
                 } else {
-                    if (u <= n || f < p != a) return !1;
+                    if (u <= n || f < d != a) return !1;
                     l = !1
-                } else "s" != p && "n" != p && (l = !1, u--)
+                } else "s" != d && "n" != d && (l = !1, u--)
             }
         }
-        var c = [],
-            d = c.pop.bind(c);
+        var p = [],
+            c = p.pop.bind(p);
         for (i = 1; i < e.length; i++) {
             var h = e[i];
-            c.push(1 == h ? d() | d() : 2 == h ? d() & d() : h ? o(h, r) : !d())
+            p.push(1 == h ? c() | c() : 2 == h ? c() & c() : h ? o(h, r) : !c())
         }
-        return !!d()
+        return !!c()
     }, i = (e, r) => {
         var t = w.S[e];
         if (!t || !w.o(t, r)) throw new Error("Shared module " + r + " doesn't exist in shared scope " + e);
         return t
     }, u = (e, r) => {
         var t = e[r];
         return Object.keys(t).reduce(((e, r) => !e || !t[e].loaded && n(e, r) ? r : e), 0)
     }, l = (e, r, t, n) => "Unsatisfied version " + t + " from " + (t && e[r][t].from) + " of shared singleton module " + r + " (required " + a(n) + ")", s = (e, r, t, n) => {
         var a = u(e, t);
-        return o(n, a) || "undefined" != typeof console && console.warn && console.warn(l(e, t, a, n)), p(e[t][a])
+        return o(n, a) || "undefined" != typeof console && console.warn && console.warn(l(e, t, a, n)), d(e[t][a])
     }, f = (e, r, t) => {
         var a = e[r];
         return (r = Object.keys(a).reduce(((e, r) => !o(t, r) || e && !n(e, r) ? e : r), 0)) && a[r]
-    }, p = e => (e.loaded = 1, e.get()), d = (c = e => function(r, t, n, a) {
+    }, d = e => (e.loaded = 1, e.get()), c = (p = e => function(r, t, n, a) {
         var o = w.I(r);
         return o && o.then ? o.then(e.bind(e, r, w.S[r], t, n, a)) : e(r, w.S[r], t, n, a)
-    })(((e, r, t, n) => (i(e, t), s(r, 0, t, n)))), h = c(((e, r, t, n, a) => {
+    })(((e, r, t, n) => (i(e, t), s(r, 0, t, n)))), h = p(((e, r, t, n, a) => {
         var o = r && w.o(r, t) && f(r, t, n);
-        return o ? p(o) : a()
-    })), v = {}, b = {
-        33: () => d("default", "@jupyterlab/apputils", [1, 3, 6, 3]),
-        142: () => d("default", "@jupyterlab/coreutils", [1, 5, 6, 3]),
-        344: () => d("default", "@jupyterlab/mainmenu", [1, 3, 6, 3]),
+        return o ? d(o) : a()
+    })), b = {}, v = {
+        144: () => c("default", "@lumino/widgets", [1, 2, 0, 0]),
+        281: () => c("default", "@jupyterlab/coreutils", [1, 6, 0, 0, , "beta", 0]),
+        530: () => c("default", "@jupyterlab/services", [1, 7, 0, 0, , "beta", 0]),
+        551: () => c("default", "@jupyterlab/mainmenu", [1, 4, 0, 0, , "beta", 0]),
         569: () => h("default", "jquery", [1, 3, 5, 0], (() => w.e(638).then((() => () => w(638))))),
-        820: () => d("default", "@jupyterlab/services", [1, 6, 6, 3]),
-        832: () => d("default", "@lumino/widgets", [1, 1, 37, 2])
+        678: () => c("default", "@jupyterlab/apputils", [1, 4, 0, 0, , "beta", 0])
     }, g = {
-        568: [33, 142, 344, 569, 820, 832]
+        568: [144, 281, 530, 551, 569, 678]
     }, w.f.consumes = (e, r) => {
         w.o(g, e) && g[e].forEach((e => {
-            if (w.o(v, e)) return r.push(v[e]);
+            if (w.o(b, e)) return r.push(b[e]);
             var t = r => {
-                    v[e] = 0, w.m[e] = t => {
+                    b[e] = 0, w.m[e] = t => {
                         delete w.c[e], t.exports = r()
                     }
                 },
                 n = r => {
-                    delete v[e], w.m[e] = t => {
+                    delete b[e], w.m[e] = t => {
                         throw delete w.c[e], r
                     }
                 };
             try {
-                var a = b[e]();
-                a.then ? r.push(v[e] = a.then(t).catch(n)) : t(a)
+                var a = v[e]();
+                a.then ? r.push(b[e] = a.then(t).catch(n)) : t(a)
             } catch (e) {
                 n(e)
             }
         }))
     }, (() => {
         var e = {
             480: 0
```

### Comparing `jupyterlab_nbgallery-2.0.0a3/labextension/userpreferences/static/third-party-licenses.json` & `jupyterlab_nbgallery-2.0.0a4/labextension/userpreferences/static/third-party-licenses.json`

 * *Files identical despite different names*

### Comparing `jupyterlab_nbgallery-2.0.0a3/package.json` & `jupyterlab_nbgallery-2.0.0a4/package.json`

 * *Files identical despite different names*

### Comparing `jupyterlab_nbgallery-2.0.0a3/setup.py` & `jupyterlab_nbgallery-2.0.0a4/setup.py`

 * *Files identical despite different names*

