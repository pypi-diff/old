# Comparing `tmp/jupyterlab_nbgallery-2.0.0a2.tar.gz` & `tmp/jupyterlab_nbgallery-2.0.0a3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "jupyterlab_nbgallery-2.0.0a2.tar", last modified: Fri Apr  7 10:31:34 2023, max compression
+gzip compressed data, was "jupyterlab_nbgallery-2.0.0a3.tar", last modified: Fri Apr  7 13:28:16 2023, max compression
```

## Comparing `jupyterlab_nbgallery-2.0.0a2.tar` & `jupyterlab_nbgallery-2.0.0a3.tar`

### file list

```diff
@@ -1,119 +1,119 @@
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 10:31:34.132135 jupyterlab_nbgallery-2.0.0a2/
--rw-r--r--   0 jovyan    (1000) users      (100)     1066 2023-04-07 09:27:02.000000 jupyterlab_nbgallery-2.0.0a2/LICENSE
--rw-r--r--   0 jovyan    (1000) users      (100)      388 2023-04-07 09:27:02.000000 jupyterlab_nbgallery-2.0.0a2/MANIFEST.in
--rw-r--r--   0 jovyan    (1000) users      (100)     2694 2023-04-07 10:31:34.128134 jupyterlab_nbgallery-2.0.0a2/PKG-INFO
--rw-r--r--   0 jovyan    (1000) users      (100)     2014 2023-04-07 09:27:02.000000 jupyterlab_nbgallery-2.0.0a2/README.md
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 10:31:34.112135 jupyterlab_nbgallery-2.0.0a2/jupyter-config/
--rw-r--r--   0 jovyan    (1000) users      (100)       96 2023-04-07 09:27:02.000000 jupyterlab_nbgallery-2.0.0a2/jupyter-config/jupyterlab_nbgallery.json
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 10:31:34.112135 jupyterlab_nbgallery-2.0.0a2/jupyterlab_nbgallery/
--rw-r--r--   0 jovyan    (1000) users      (100)      596 2023-04-07 09:27:02.000000 jupyterlab_nbgallery-2.0.0a2/jupyterlab_nbgallery/__init__.py
--rw-r--r--   0 jovyan    (1000) users      (100)       76 2023-04-07 10:30:10.000000 jupyterlab_nbgallery-2.0.0a2/jupyterlab_nbgallery/_version.py
--rw-r--r--   0 jovyan    (1000) users      (100)     3640 2023-04-07 09:27:02.000000 jupyterlab_nbgallery-2.0.0a2/jupyterlab_nbgallery/handlers.py
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 10:31:34.116135 jupyterlab_nbgallery-2.0.0a2/jupyterlab_nbgallery.egg-info/
--rw-r--r--   0 jovyan    (1000) users      (100)     2694 2023-04-07 10:31:33.000000 jupyterlab_nbgallery-2.0.0a2/jupyterlab_nbgallery.egg-info/PKG-INFO
--rw-r--r--   0 jovyan    (1000) users      (100)     4503 2023-04-07 10:31:33.000000 jupyterlab_nbgallery-2.0.0a2/jupyterlab_nbgallery.egg-info/SOURCES.txt
--rw-r--r--   0 jovyan    (1000) users      (100)        1 2023-04-07 10:31:33.000000 jupyterlab_nbgallery-2.0.0a2/jupyterlab_nbgallery.egg-info/dependency_links.txt
--rw-r--r--   0 jovyan    (1000) users      (100)        1 2023-04-07 09:29:38.000000 jupyterlab_nbgallery-2.0.0a2/jupyterlab_nbgallery.egg-info/not-zip-safe
--rw-r--r--   0 jovyan    (1000) users      (100)       61 2023-04-07 10:31:33.000000 jupyterlab_nbgallery-2.0.0a2/jupyterlab_nbgallery.egg-info/requires.txt
--rw-r--r--   0 jovyan    (1000) users      (100)       21 2023-04-07 10:31:33.000000 jupyterlab_nbgallery-2.0.0a2/jupyterlab_nbgallery.egg-info/top_level.txt
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 10:31:34.112135 jupyterlab_nbgallery-2.0.0a2/labextension/
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 10:31:34.116135 jupyterlab_nbgallery-2.0.0a2/labextension/autodownload/
--rw-r--r--   0 jovyan    (1000) users      (100)     2596 2023-04-07 10:31:04.000000 jupyterlab_nbgallery-2.0.0a2/labextension/autodownload/package.json
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 10:31:34.108134 jupyterlab_nbgallery-2.0.0a2/labextension/autodownload/schemas/
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 10:31:34.108134 jupyterlab_nbgallery-2.0.0a2/labextension/autodownload/schemas/@jupyterlab-nbgallery/
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 10:31:34.116135 jupyterlab_nbgallery-2.0.0a2/labextension/autodownload/schemas/@jupyterlab-nbgallery/autodownload/
--rw-r--r--   0 jovyan    (1000) users      (100)      335 2023-04-07 10:30:54.000000 jupyterlab_nbgallery-2.0.0a2/labextension/autodownload/schemas/@jupyterlab-nbgallery/autodownload/autodownload.json
--rw-r--r--   0 jovyan    (1000) users      (100)     2505 2023-04-07 10:30:54.000000 jupyterlab_nbgallery-2.0.0a2/labextension/autodownload/schemas/@jupyterlab-nbgallery/autodownload/package.json.orig
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 10:31:34.116135 jupyterlab_nbgallery-2.0.0a2/labextension/autodownload/static/
--rw-r--r--   0 jovyan    (1000) users      (100)     3438 2023-04-07 10:31:04.000000 jupyterlab_nbgallery-2.0.0a2/labextension/autodownload/static/542.51fb91347d8a3d9a657a.js
--rw-r--r--   0 jovyan    (1000) users      (100)     1968 2023-04-07 10:31:04.000000 jupyterlab_nbgallery-2.0.0a2/labextension/autodownload/static/568.088b227a0b6b6168ee16.js
--rw-r--r--   0 jovyan    (1000) users      (100)    90038 2023-04-07 10:31:04.000000 jupyterlab_nbgallery-2.0.0a2/labextension/autodownload/static/638.0ed295d9378dea7c5c7b.js
--rw-r--r--   0 jovyan    (1000) users      (100)      476 2023-04-07 10:31:04.000000 jupyterlab_nbgallery-2.0.0a2/labextension/autodownload/static/638.0ed295d9378dea7c5c7b.js.LICENSE.txt
--rw-r--r--   0 jovyan    (1000) users      (100)     6914 2023-04-07 10:31:04.000000 jupyterlab_nbgallery-2.0.0a2/labextension/autodownload/static/remoteEntry.fa15592bca73423b04a4.js
--rw-r--r--   0 jovyan    (1000) users      (100)      178 2023-04-07 10:30:54.000000 jupyterlab_nbgallery-2.0.0a2/labextension/autodownload/static/style.js
--rw-r--r--   0 jovyan    (1000) users      (100)     3692 2023-04-07 10:31:04.000000 jupyterlab_nbgallery-2.0.0a2/labextension/autodownload/static/third-party-licenses.json
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 10:31:34.116135 jupyterlab_nbgallery-2.0.0a2/labextension/environment-life/
--rw-r--r--   0 jovyan    (1000) users      (100)     2618 2023-04-07 10:30:56.000000 jupyterlab_nbgallery-2.0.0a2/labextension/environment-life/package.json
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 10:31:34.108134 jupyterlab_nbgallery-2.0.0a2/labextension/environment-life/schemas/
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 10:31:34.108134 jupyterlab_nbgallery-2.0.0a2/labextension/environment-life/schemas/@jupyterlab-nbgallery/
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 10:31:34.116135 jupyterlab_nbgallery-2.0.0a2/labextension/environment-life/schemas/@jupyterlab-nbgallery/environment-life/
--rw-r--r--   0 jovyan    (1000) users      (100)     2527 2023-04-07 10:30:54.000000 jupyterlab_nbgallery-2.0.0a2/labextension/environment-life/schemas/@jupyterlab-nbgallery/environment-life/package.json.orig
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 10:31:34.120134 jupyterlab_nbgallery-2.0.0a2/labextension/environment-life/static/
--rw-r--r--   0 jovyan    (1000) users      (100)     1213 2023-04-07 10:30:56.000000 jupyterlab_nbgallery-2.0.0a2/labextension/environment-life/static/248.1d3351413b89920be9fb.js
--rw-r--r--   0 jovyan    (1000) users      (100)     3446 2023-04-07 10:30:56.000000 jupyterlab_nbgallery-2.0.0a2/labextension/environment-life/static/542.e4d405f3b0e4f693ab53.js
--rw-r--r--   0 jovyan    (1000) users      (100)     6651 2023-04-07 10:30:56.000000 jupyterlab_nbgallery-2.0.0a2/labextension/environment-life/static/remoteEntry.dd7691336809bc6771e3.js
--rw-r--r--   0 jovyan    (1000) users      (100)      182 2023-04-07 10:30:54.000000 jupyterlab_nbgallery-2.0.0a2/labextension/environment-life/static/style.js
--rw-r--r--   0 jovyan    (1000) users      (100)     2452 2023-04-07 10:30:56.000000 jupyterlab_nbgallery-2.0.0a2/labextension/environment-life/static/third-party-licenses.json
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 10:31:34.120134 jupyterlab_nbgallery-2.0.0a2/labextension/environment-registration/
--rw-r--r--   0 jovyan    (1000) users      (100)     2579 2023-04-07 10:31:04.000000 jupyterlab_nbgallery-2.0.0a2/labextension/environment-registration/package.json
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 10:31:34.108134 jupyterlab_nbgallery-2.0.0a2/labextension/environment-registration/schemas/
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 10:31:34.108134 jupyterlab_nbgallery-2.0.0a2/labextension/environment-registration/schemas/@jupyterlab-nbgallery/
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 10:31:34.120134 jupyterlab_nbgallery-2.0.0a2/labextension/environment-registration/schemas/@jupyterlab-nbgallery/environment-registration/
--rw-r--r--   0 jovyan    (1000) users      (100)      680 2023-04-07 10:30:55.000000 jupyterlab_nbgallery-2.0.0a2/labextension/environment-registration/schemas/@jupyterlab-nbgallery/environment-registration/environment-registration.json
--rw-r--r--   0 jovyan    (1000) users      (100)     2488 2023-04-07 10:30:55.000000 jupyterlab_nbgallery-2.0.0a2/labextension/environment-registration/schemas/@jupyterlab-nbgallery/environment-registration/package.json.orig
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 10:31:34.120134 jupyterlab_nbgallery-2.0.0a2/labextension/environment-registration/static/
--rw-r--r--   0 jovyan    (1000) users      (100)     3460 2023-04-07 10:31:04.000000 jupyterlab_nbgallery-2.0.0a2/labextension/environment-registration/static/542.feae6c397f33f9138fea.js
--rw-r--r--   0 jovyan    (1000) users      (100)    90062 2023-04-07 10:31:04.000000 jupyterlab_nbgallery-2.0.0a2/labextension/environment-registration/static/638.36e464d3233849b6b07a.js
--rw-r--r--   0 jovyan    (1000) users      (100)      476 2023-04-07 10:31:04.000000 jupyterlab_nbgallery-2.0.0a2/labextension/environment-registration/static/638.36e464d3233849b6b07a.js.LICENSE.txt
--rw-r--r--   0 jovyan    (1000) users      (100)     1519 2023-04-07 10:31:04.000000 jupyterlab_nbgallery-2.0.0a2/labextension/environment-registration/static/784.c5c708b87c266cbabd98.js
--rw-r--r--   0 jovyan    (1000) users      (100)     7044 2023-04-07 10:31:04.000000 jupyterlab_nbgallery-2.0.0a2/labextension/environment-registration/static/remoteEntry.00e0256ee314fd224ea3.js
--rw-r--r--   0 jovyan    (1000) users      (100)      190 2023-04-07 10:30:55.000000 jupyterlab_nbgallery-2.0.0a2/labextension/environment-registration/static/style.js
--rw-r--r--   0 jovyan    (1000) users      (100)     3692 2023-04-07 10:31:04.000000 jupyterlab_nbgallery-2.0.0a2/labextension/environment-registration/static/third-party-licenses.json
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 10:31:34.120134 jupyterlab_nbgallery-2.0.0a2/labextension/gallerymenu/
--rw-r--r--   0 jovyan    (1000) users      (100)     2698 2023-04-07 10:31:04.000000 jupyterlab_nbgallery-2.0.0a2/labextension/gallerymenu/package.json
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 10:31:34.108134 jupyterlab_nbgallery-2.0.0a2/labextension/gallerymenu/schemas/
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 10:31:34.108134 jupyterlab_nbgallery-2.0.0a2/labextension/gallerymenu/schemas/@jupyterlab-nbgallery/
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 10:31:34.120134 jupyterlab_nbgallery-2.0.0a2/labextension/gallerymenu/schemas/@jupyterlab-nbgallery/gallerymenu/
--rw-r--r--   0 jovyan    (1000) users      (100)     2607 2023-04-07 10:30:55.000000 jupyterlab_nbgallery-2.0.0a2/labextension/gallerymenu/schemas/@jupyterlab-nbgallery/gallerymenu/package.json.orig
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 10:31:34.124134 jupyterlab_nbgallery-2.0.0a2/labextension/gallerymenu/static/
--rw-r--r--   0 jovyan    (1000) users      (100)     4018 2023-04-07 10:31:04.000000 jupyterlab_nbgallery-2.0.0a2/labextension/gallerymenu/static/542.18fd91d86aaf6286edd0.js
--rw-r--r--   0 jovyan    (1000) users      (100)    10415 2023-04-07 10:31:04.000000 jupyterlab_nbgallery-2.0.0a2/labextension/gallerymenu/static/56.8dc3eaf446ef31335c65.js
--rw-r--r--   0 jovyan    (1000) users      (100)    90036 2023-04-07 10:31:04.000000 jupyterlab_nbgallery-2.0.0a2/labextension/gallerymenu/static/638.95e0186307171588df5b.js
--rw-r--r--   0 jovyan    (1000) users      (100)      476 2023-04-07 10:31:04.000000 jupyterlab_nbgallery-2.0.0a2/labextension/gallerymenu/static/638.95e0186307171588df5b.js.LICENSE.txt
--rw-r--r--   0 jovyan    (1000) users      (100)     7164 2023-04-07 10:31:04.000000 jupyterlab_nbgallery-2.0.0a2/labextension/gallerymenu/static/remoteEntry.3280b8022411403d2f46.js
--rw-r--r--   0 jovyan    (1000) users      (100)      177 2023-04-07 10:30:55.000000 jupyterlab_nbgallery-2.0.0a2/labextension/gallerymenu/static/style.js
--rw-r--r--   0 jovyan    (1000) users      (100)     3692 2023-04-07 10:31:04.000000 jupyterlab_nbgallery-2.0.0a2/labextension/gallerymenu/static/third-party-licenses.json
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 10:31:34.124134 jupyterlab_nbgallery-2.0.0a2/labextension/inject-uuid/
--rw-r--r--   0 jovyan    (1000) users      (100)     2444 2023-04-07 10:31:25.000000 jupyterlab_nbgallery-2.0.0a2/labextension/inject-uuid/package.json
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 10:31:34.108134 jupyterlab_nbgallery-2.0.0a2/labextension/inject-uuid/schemas/
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 10:31:34.108134 jupyterlab_nbgallery-2.0.0a2/labextension/inject-uuid/schemas/@jupyterlab-nbgallery/
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 10:31:34.124134 jupyterlab_nbgallery-2.0.0a2/labextension/inject-uuid/schemas/@jupyterlab-nbgallery/inject-uuid/
--rw-r--r--   0 jovyan    (1000) users      (100)     2379 2023-04-07 10:31:24.000000 jupyterlab_nbgallery-2.0.0a2/labextension/inject-uuid/schemas/@jupyterlab-nbgallery/inject-uuid/package.json.orig
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 10:31:34.124134 jupyterlab_nbgallery-2.0.0a2/labextension/inject-uuid/static/
--rw-r--r--   0 jovyan    (1000) users      (100)      931 2023-04-07 10:31:25.000000 jupyterlab_nbgallery-2.0.0a2/labextension/inject-uuid/static/568.1dcbb7bee8ca1152cf60.js
--rw-r--r--   0 jovyan    (1000) users      (100)     6305 2023-04-07 10:31:25.000000 jupyterlab_nbgallery-2.0.0a2/labextension/inject-uuid/static/remoteEntry.02ddda09f0305fa467f4.js
--rw-r--r--   0 jovyan    (1000) users      (100)      118 2023-04-07 10:31:24.000000 jupyterlab_nbgallery-2.0.0a2/labextension/inject-uuid/static/style.js
--rw-r--r--   0 jovyan    (1000) users      (100)       20 2023-04-07 10:31:25.000000 jupyterlab_nbgallery-2.0.0a2/labextension/inject-uuid/static/third-party-licenses.json
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 10:31:34.124134 jupyterlab_nbgallery-2.0.0a2/labextension/instrumentation/
--rw-r--r--   0 jovyan    (1000) users      (100)     2527 2023-04-07 10:31:33.000000 jupyterlab_nbgallery-2.0.0a2/labextension/instrumentation/package.json
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 10:31:34.108134 jupyterlab_nbgallery-2.0.0a2/labextension/instrumentation/schemas/
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 10:31:34.108134 jupyterlab_nbgallery-2.0.0a2/labextension/instrumentation/schemas/@jupyterlab-nbgallery/
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 10:31:34.124134 jupyterlab_nbgallery-2.0.0a2/labextension/instrumentation/schemas/@jupyterlab-nbgallery/instrumentation/
--rw-r--r--   0 jovyan    (1000) users      (100)      345 2023-04-07 10:31:28.000000 jupyterlab_nbgallery-2.0.0a2/labextension/instrumentation/schemas/@jupyterlab-nbgallery/instrumentation/instrumentation.json
--rw-r--r--   0 jovyan    (1000) users      (100)     2466 2023-04-07 10:31:28.000000 jupyterlab_nbgallery-2.0.0a2/labextension/instrumentation/schemas/@jupyterlab-nbgallery/instrumentation/package.json.orig
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 10:31:34.128134 jupyterlab_nbgallery-2.0.0a2/labextension/instrumentation/static/
--rw-r--r--   0 jovyan    (1000) users      (100)     1720 2023-04-07 10:31:33.000000 jupyterlab_nbgallery-2.0.0a2/labextension/instrumentation/static/568.0d3998aabd22f1867c40.js
--rw-r--r--   0 jovyan    (1000) users      (100)    90044 2023-04-07 10:31:33.000000 jupyterlab_nbgallery-2.0.0a2/labextension/instrumentation/static/638.b95125ed695cee42aae4.js
--rw-r--r--   0 jovyan    (1000) users      (100)      476 2023-04-07 10:31:33.000000 jupyterlab_nbgallery-2.0.0a2/labextension/instrumentation/static/638.b95125ed695cee42aae4.js.LICENSE.txt
--rw-r--r--   0 jovyan    (1000) users      (100)     8425 2023-04-07 10:31:33.000000 jupyterlab_nbgallery-2.0.0a2/labextension/instrumentation/static/701.d81800f5926ab62cc8b2.js
--rw-r--r--   0 jovyan    (1000) users      (100)     7555 2023-04-07 10:31:33.000000 jupyterlab_nbgallery-2.0.0a2/labextension/instrumentation/static/remoteEntry.53ed33a8ef1f603e0fc8.js
--rw-r--r--   0 jovyan    (1000) users      (100)      118 2023-04-07 10:31:28.000000 jupyterlab_nbgallery-2.0.0a2/labextension/instrumentation/static/style.js
--rw-r--r--   0 jovyan    (1000) users      (100)     2479 2023-04-07 10:31:33.000000 jupyterlab_nbgallery-2.0.0a2/labextension/instrumentation/static/third-party-licenses.json
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 10:31:34.128134 jupyterlab_nbgallery-2.0.0a2/labextension/userpreferences/
--rw-r--r--   0 jovyan    (1000) users      (100)     2709 2023-04-07 10:31:33.000000 jupyterlab_nbgallery-2.0.0a2/labextension/userpreferences/package.json
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 10:31:34.112135 jupyterlab_nbgallery-2.0.0a2/labextension/userpreferences/schemas/
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 10:31:34.112135 jupyterlab_nbgallery-2.0.0a2/labextension/userpreferences/schemas/@jupyterlab-nbgallery/
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 10:31:34.128134 jupyterlab_nbgallery-2.0.0a2/labextension/userpreferences/schemas/@jupyterlab-nbgallery/userpreferences/
--rw-r--r--   0 jovyan    (1000) users      (100)     2618 2023-04-07 10:31:28.000000 jupyterlab_nbgallery-2.0.0a2/labextension/userpreferences/schemas/@jupyterlab-nbgallery/userpreferences/package.json.orig
-drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 10:31:34.128134 jupyterlab_nbgallery-2.0.0a2/labextension/userpreferences/static/
--rw-r--r--   0 jovyan    (1000) users      (100)     4026 2023-04-07 10:31:33.000000 jupyterlab_nbgallery-2.0.0a2/labextension/userpreferences/static/542.d1718a50e23f3808ba62.js
--rw-r--r--   0 jovyan    (1000) users      (100)     4114 2023-04-07 10:31:33.000000 jupyterlab_nbgallery-2.0.0a2/labextension/userpreferences/static/568.00695541aaa15d567580.js
--rw-r--r--   0 jovyan    (1000) users      (100)    90044 2023-04-07 10:31:33.000000 jupyterlab_nbgallery-2.0.0a2/labextension/userpreferences/static/638.e5080f99954048969f76.js
--rw-r--r--   0 jovyan    (1000) users      (100)      476 2023-04-07 10:31:33.000000 jupyterlab_nbgallery-2.0.0a2/labextension/userpreferences/static/638.e5080f99954048969f76.js.LICENSE.txt
--rw-r--r--   0 jovyan    (1000) users      (100)     7095 2023-04-07 10:31:33.000000 jupyterlab_nbgallery-2.0.0a2/labextension/userpreferences/static/remoteEntry.03bf745401d2317e1d7d.js
--rw-r--r--   0 jovyan    (1000) users      (100)      181 2023-04-07 10:31:28.000000 jupyterlab_nbgallery-2.0.0a2/labextension/userpreferences/static/style.js
--rw-r--r--   0 jovyan    (1000) users      (100)     3692 2023-04-07 10:31:33.000000 jupyterlab_nbgallery-2.0.0a2/labextension/userpreferences/static/third-party-licenses.json
--rw-r--r--   0 jovyan    (1000) users      (100)     1103 2023-04-07 09:27:02.000000 jupyterlab_nbgallery-2.0.0a2/package.json
--rw-r--r--   0 jovyan    (1000) users      (100)      145 2023-04-07 09:27:02.000000 jupyterlab_nbgallery-2.0.0a2/pyproject.toml
--rw-r--r--   0 jovyan    (1000) users      (100)       38 2023-04-07 10:31:34.132135 jupyterlab_nbgallery-2.0.0a2/setup.cfg
--rw-r--r--   0 jovyan    (1000) users      (100)     3928 2023-04-07 09:27:02.000000 jupyterlab_nbgallery-2.0.0a2/setup.py
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.733590 jupyterlab_nbgallery-2.0.0a3/
+-rw-r--r--   0 jovyan    (1000) users      (100)     1066 2023-04-07 13:26:25.000000 jupyterlab_nbgallery-2.0.0a3/LICENSE
+-rw-r--r--   0 jovyan    (1000) users      (100)      388 2023-04-07 13:26:25.000000 jupyterlab_nbgallery-2.0.0a3/MANIFEST.in
+-rw-r--r--   0 jovyan    (1000) users      (100)     2694 2023-04-07 13:28:16.733590 jupyterlab_nbgallery-2.0.0a3/PKG-INFO
+-rw-r--r--   0 jovyan    (1000) users      (100)     2014 2023-04-07 13:26:25.000000 jupyterlab_nbgallery-2.0.0a3/README.md
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.717589 jupyterlab_nbgallery-2.0.0a3/jupyter-config/
+-rw-r--r--   0 jovyan    (1000) users      (100)       96 2023-04-07 13:26:25.000000 jupyterlab_nbgallery-2.0.0a3/jupyter-config/jupyterlab_nbgallery.json
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.717589 jupyterlab_nbgallery-2.0.0a3/jupyterlab_nbgallery/
+-rw-r--r--   0 jovyan    (1000) users      (100)      596 2023-04-07 13:26:25.000000 jupyterlab_nbgallery-2.0.0a3/jupyterlab_nbgallery/__init__.py
+-rw-r--r--   0 jovyan    (1000) users      (100)       76 2023-04-07 13:26:25.000000 jupyterlab_nbgallery-2.0.0a3/jupyterlab_nbgallery/_version.py
+-rw-r--r--   0 jovyan    (1000) users      (100)     3640 2023-04-07 13:26:25.000000 jupyterlab_nbgallery-2.0.0a3/jupyterlab_nbgallery/handlers.py
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.717589 jupyterlab_nbgallery-2.0.0a3/jupyterlab_nbgallery.egg-info/
+-rw-r--r--   0 jovyan    (1000) users      (100)     2694 2023-04-07 13:28:16.000000 jupyterlab_nbgallery-2.0.0a3/jupyterlab_nbgallery.egg-info/PKG-INFO
+-rw-r--r--   0 jovyan    (1000) users      (100)     4503 2023-04-07 13:28:16.000000 jupyterlab_nbgallery-2.0.0a3/jupyterlab_nbgallery.egg-info/SOURCES.txt
+-rw-r--r--   0 jovyan    (1000) users      (100)        1 2023-04-07 13:28:16.000000 jupyterlab_nbgallery-2.0.0a3/jupyterlab_nbgallery.egg-info/dependency_links.txt
+-rw-r--r--   0 jovyan    (1000) users      (100)        1 2023-04-07 09:29:38.000000 jupyterlab_nbgallery-2.0.0a3/jupyterlab_nbgallery.egg-info/not-zip-safe
+-rw-r--r--   0 jovyan    (1000) users      (100)       61 2023-04-07 13:28:16.000000 jupyterlab_nbgallery-2.0.0a3/jupyterlab_nbgallery.egg-info/requires.txt
+-rw-r--r--   0 jovyan    (1000) users      (100)       21 2023-04-07 13:28:16.000000 jupyterlab_nbgallery-2.0.0a3/jupyterlab_nbgallery.egg-info/top_level.txt
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.713590 jupyterlab_nbgallery-2.0.0a3/labextension/
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.717589 jupyterlab_nbgallery-2.0.0a3/labextension/autodownload/
+-rw-r--r--   0 jovyan    (1000) users      (100)     2596 2023-04-07 13:27:45.000000 jupyterlab_nbgallery-2.0.0a3/labextension/autodownload/package.json
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.709589 jupyterlab_nbgallery-2.0.0a3/labextension/autodownload/schemas/
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.709589 jupyterlab_nbgallery-2.0.0a3/labextension/autodownload/schemas/@jupyterlab-nbgallery/
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.717589 jupyterlab_nbgallery-2.0.0a3/labextension/autodownload/schemas/@jupyterlab-nbgallery/autodownload/
+-rw-r--r--   0 jovyan    (1000) users      (100)      335 2023-04-07 13:27:36.000000 jupyterlab_nbgallery-2.0.0a3/labextension/autodownload/schemas/@jupyterlab-nbgallery/autodownload/autodownload.json
+-rw-r--r--   0 jovyan    (1000) users      (100)     2505 2023-04-07 13:27:36.000000 jupyterlab_nbgallery-2.0.0a3/labextension/autodownload/schemas/@jupyterlab-nbgallery/autodownload/package.json.orig
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.721589 jupyterlab_nbgallery-2.0.0a3/labextension/autodownload/static/
+-rw-r--r--   0 jovyan    (1000) users      (100)     3438 2023-04-07 13:27:45.000000 jupyterlab_nbgallery-2.0.0a3/labextension/autodownload/static/542.51fb91347d8a3d9a657a.js
+-rw-r--r--   0 jovyan    (1000) users      (100)     1968 2023-04-07 13:27:45.000000 jupyterlab_nbgallery-2.0.0a3/labextension/autodownload/static/568.088b227a0b6b6168ee16.js
+-rw-r--r--   0 jovyan    (1000) users      (100)    90038 2023-04-07 13:27:45.000000 jupyterlab_nbgallery-2.0.0a3/labextension/autodownload/static/638.0ed295d9378dea7c5c7b.js
+-rw-r--r--   0 jovyan    (1000) users      (100)      476 2023-04-07 13:27:45.000000 jupyterlab_nbgallery-2.0.0a3/labextension/autodownload/static/638.0ed295d9378dea7c5c7b.js.LICENSE.txt
+-rw-r--r--   0 jovyan    (1000) users      (100)     6914 2023-04-07 13:27:45.000000 jupyterlab_nbgallery-2.0.0a3/labextension/autodownload/static/remoteEntry.fa15592bca73423b04a4.js
+-rw-r--r--   0 jovyan    (1000) users      (100)      178 2023-04-07 13:27:36.000000 jupyterlab_nbgallery-2.0.0a3/labextension/autodownload/static/style.js
+-rw-r--r--   0 jovyan    (1000) users      (100)     3692 2023-04-07 13:27:45.000000 jupyterlab_nbgallery-2.0.0a3/labextension/autodownload/static/third-party-licenses.json
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.721589 jupyterlab_nbgallery-2.0.0a3/labextension/environment-life/
+-rw-r--r--   0 jovyan    (1000) users      (100)     2618 2023-04-07 13:27:40.000000 jupyterlab_nbgallery-2.0.0a3/labextension/environment-life/package.json
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.709589 jupyterlab_nbgallery-2.0.0a3/labextension/environment-life/schemas/
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.709589 jupyterlab_nbgallery-2.0.0a3/labextension/environment-life/schemas/@jupyterlab-nbgallery/
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.721589 jupyterlab_nbgallery-2.0.0a3/labextension/environment-life/schemas/@jupyterlab-nbgallery/environment-life/
+-rw-r--r--   0 jovyan    (1000) users      (100)     2527 2023-04-07 13:27:37.000000 jupyterlab_nbgallery-2.0.0a3/labextension/environment-life/schemas/@jupyterlab-nbgallery/environment-life/package.json.orig
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.721589 jupyterlab_nbgallery-2.0.0a3/labextension/environment-life/static/
+-rw-r--r--   0 jovyan    (1000) users      (100)     1213 2023-04-07 13:27:40.000000 jupyterlab_nbgallery-2.0.0a3/labextension/environment-life/static/248.1d3351413b89920be9fb.js
+-rw-r--r--   0 jovyan    (1000) users      (100)     3446 2023-04-07 13:27:40.000000 jupyterlab_nbgallery-2.0.0a3/labextension/environment-life/static/542.e4d405f3b0e4f693ab53.js
+-rw-r--r--   0 jovyan    (1000) users      (100)     6651 2023-04-07 13:27:40.000000 jupyterlab_nbgallery-2.0.0a3/labextension/environment-life/static/remoteEntry.dd7691336809bc6771e3.js
+-rw-r--r--   0 jovyan    (1000) users      (100)      182 2023-04-07 13:27:37.000000 jupyterlab_nbgallery-2.0.0a3/labextension/environment-life/static/style.js
+-rw-r--r--   0 jovyan    (1000) users      (100)     2452 2023-04-07 13:27:40.000000 jupyterlab_nbgallery-2.0.0a3/labextension/environment-life/static/third-party-licenses.json
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.721589 jupyterlab_nbgallery-2.0.0a3/labextension/environment-registration/
+-rw-r--r--   0 jovyan    (1000) users      (100)     2579 2023-04-07 13:27:44.000000 jupyterlab_nbgallery-2.0.0a3/labextension/environment-registration/package.json
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.709589 jupyterlab_nbgallery-2.0.0a3/labextension/environment-registration/schemas/
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.713590 jupyterlab_nbgallery-2.0.0a3/labextension/environment-registration/schemas/@jupyterlab-nbgallery/
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.721589 jupyterlab_nbgallery-2.0.0a3/labextension/environment-registration/schemas/@jupyterlab-nbgallery/environment-registration/
+-rw-r--r--   0 jovyan    (1000) users      (100)      680 2023-04-07 13:27:36.000000 jupyterlab_nbgallery-2.0.0a3/labextension/environment-registration/schemas/@jupyterlab-nbgallery/environment-registration/environment-registration.json
+-rw-r--r--   0 jovyan    (1000) users      (100)     2488 2023-04-07 13:27:36.000000 jupyterlab_nbgallery-2.0.0a3/labextension/environment-registration/schemas/@jupyterlab-nbgallery/environment-registration/package.json.orig
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.725589 jupyterlab_nbgallery-2.0.0a3/labextension/environment-registration/static/
+-rw-r--r--   0 jovyan    (1000) users      (100)     3460 2023-04-07 13:27:44.000000 jupyterlab_nbgallery-2.0.0a3/labextension/environment-registration/static/542.feae6c397f33f9138fea.js
+-rw-r--r--   0 jovyan    (1000) users      (100)    90062 2023-04-07 13:27:44.000000 jupyterlab_nbgallery-2.0.0a3/labextension/environment-registration/static/638.36e464d3233849b6b07a.js
+-rw-r--r--   0 jovyan    (1000) users      (100)      476 2023-04-07 13:27:44.000000 jupyterlab_nbgallery-2.0.0a3/labextension/environment-registration/static/638.36e464d3233849b6b07a.js.LICENSE.txt
+-rw-r--r--   0 jovyan    (1000) users      (100)     1519 2023-04-07 13:27:44.000000 jupyterlab_nbgallery-2.0.0a3/labextension/environment-registration/static/784.c5c708b87c266cbabd98.js
+-rw-r--r--   0 jovyan    (1000) users      (100)     7044 2023-04-07 13:27:44.000000 jupyterlab_nbgallery-2.0.0a3/labextension/environment-registration/static/remoteEntry.00e0256ee314fd224ea3.js
+-rw-r--r--   0 jovyan    (1000) users      (100)      190 2023-04-07 13:27:36.000000 jupyterlab_nbgallery-2.0.0a3/labextension/environment-registration/static/style.js
+-rw-r--r--   0 jovyan    (1000) users      (100)     3692 2023-04-07 13:27:44.000000 jupyterlab_nbgallery-2.0.0a3/labextension/environment-registration/static/third-party-licenses.json
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.725589 jupyterlab_nbgallery-2.0.0a3/labextension/gallerymenu/
+-rw-r--r--   0 jovyan    (1000) users      (100)     2698 2023-04-07 13:27:47.000000 jupyterlab_nbgallery-2.0.0a3/labextension/gallerymenu/package.json
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.713590 jupyterlab_nbgallery-2.0.0a3/labextension/gallerymenu/schemas/
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.713590 jupyterlab_nbgallery-2.0.0a3/labextension/gallerymenu/schemas/@jupyterlab-nbgallery/
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.725589 jupyterlab_nbgallery-2.0.0a3/labextension/gallerymenu/schemas/@jupyterlab-nbgallery/gallerymenu/
+-rw-r--r--   0 jovyan    (1000) users      (100)     2607 2023-04-07 13:27:38.000000 jupyterlab_nbgallery-2.0.0a3/labextension/gallerymenu/schemas/@jupyterlab-nbgallery/gallerymenu/package.json.orig
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.725589 jupyterlab_nbgallery-2.0.0a3/labextension/gallerymenu/static/
+-rw-r--r--   0 jovyan    (1000) users      (100)     4018 2023-04-07 13:27:47.000000 jupyterlab_nbgallery-2.0.0a3/labextension/gallerymenu/static/542.18fd91d86aaf6286edd0.js
+-rw-r--r--   0 jovyan    (1000) users      (100)    10492 2023-04-07 13:27:47.000000 jupyterlab_nbgallery-2.0.0a3/labextension/gallerymenu/static/56.00b49e0c37b3050cbc14.js
+-rw-r--r--   0 jovyan    (1000) users      (100)    90036 2023-04-07 13:27:47.000000 jupyterlab_nbgallery-2.0.0a3/labextension/gallerymenu/static/638.95e0186307171588df5b.js
+-rw-r--r--   0 jovyan    (1000) users      (100)      476 2023-04-07 13:27:47.000000 jupyterlab_nbgallery-2.0.0a3/labextension/gallerymenu/static/638.95e0186307171588df5b.js.LICENSE.txt
+-rw-r--r--   0 jovyan    (1000) users      (100)     7164 2023-04-07 13:27:47.000000 jupyterlab_nbgallery-2.0.0a3/labextension/gallerymenu/static/remoteEntry.ae9dddbb4a23b1552c19.js
+-rw-r--r--   0 jovyan    (1000) users      (100)      177 2023-04-07 13:27:38.000000 jupyterlab_nbgallery-2.0.0a3/labextension/gallerymenu/static/style.js
+-rw-r--r--   0 jovyan    (1000) users      (100)     3692 2023-04-07 13:27:47.000000 jupyterlab_nbgallery-2.0.0a3/labextension/gallerymenu/static/third-party-licenses.json
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.725589 jupyterlab_nbgallery-2.0.0a3/labextension/inject-uuid/
+-rw-r--r--   0 jovyan    (1000) users      (100)     2444 2023-04-07 13:28:08.000000 jupyterlab_nbgallery-2.0.0a3/labextension/inject-uuid/package.json
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.713590 jupyterlab_nbgallery-2.0.0a3/labextension/inject-uuid/schemas/
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.713590 jupyterlab_nbgallery-2.0.0a3/labextension/inject-uuid/schemas/@jupyterlab-nbgallery/
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.725589 jupyterlab_nbgallery-2.0.0a3/labextension/inject-uuid/schemas/@jupyterlab-nbgallery/inject-uuid/
+-rw-r--r--   0 jovyan    (1000) users      (100)     2379 2023-04-07 13:28:06.000000 jupyterlab_nbgallery-2.0.0a3/labextension/inject-uuid/schemas/@jupyterlab-nbgallery/inject-uuid/package.json.orig
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.729589 jupyterlab_nbgallery-2.0.0a3/labextension/inject-uuid/static/
+-rw-r--r--   0 jovyan    (1000) users      (100)      931 2023-04-07 13:28:08.000000 jupyterlab_nbgallery-2.0.0a3/labextension/inject-uuid/static/568.1dcbb7bee8ca1152cf60.js
+-rw-r--r--   0 jovyan    (1000) users      (100)     6305 2023-04-07 13:28:08.000000 jupyterlab_nbgallery-2.0.0a3/labextension/inject-uuid/static/remoteEntry.02ddda09f0305fa467f4.js
+-rw-r--r--   0 jovyan    (1000) users      (100)      118 2023-04-07 13:28:06.000000 jupyterlab_nbgallery-2.0.0a3/labextension/inject-uuid/static/style.js
+-rw-r--r--   0 jovyan    (1000) users      (100)       20 2023-04-07 13:28:08.000000 jupyterlab_nbgallery-2.0.0a3/labextension/inject-uuid/static/third-party-licenses.json
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.729589 jupyterlab_nbgallery-2.0.0a3/labextension/instrumentation/
+-rw-r--r--   0 jovyan    (1000) users      (100)     2527 2023-04-07 13:28:16.000000 jupyterlab_nbgallery-2.0.0a3/labextension/instrumentation/package.json
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.713590 jupyterlab_nbgallery-2.0.0a3/labextension/instrumentation/schemas/
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.713590 jupyterlab_nbgallery-2.0.0a3/labextension/instrumentation/schemas/@jupyterlab-nbgallery/
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.729589 jupyterlab_nbgallery-2.0.0a3/labextension/instrumentation/schemas/@jupyterlab-nbgallery/instrumentation/
+-rw-r--r--   0 jovyan    (1000) users      (100)      345 2023-04-07 13:28:10.000000 jupyterlab_nbgallery-2.0.0a3/labextension/instrumentation/schemas/@jupyterlab-nbgallery/instrumentation/instrumentation.json
+-rw-r--r--   0 jovyan    (1000) users      (100)     2466 2023-04-07 13:28:10.000000 jupyterlab_nbgallery-2.0.0a3/labextension/instrumentation/schemas/@jupyterlab-nbgallery/instrumentation/package.json.orig
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.729589 jupyterlab_nbgallery-2.0.0a3/labextension/instrumentation/static/
+-rw-r--r--   0 jovyan    (1000) users      (100)     1720 2023-04-07 13:28:16.000000 jupyterlab_nbgallery-2.0.0a3/labextension/instrumentation/static/568.0d3998aabd22f1867c40.js
+-rw-r--r--   0 jovyan    (1000) users      (100)    90044 2023-04-07 13:28:16.000000 jupyterlab_nbgallery-2.0.0a3/labextension/instrumentation/static/638.b95125ed695cee42aae4.js
+-rw-r--r--   0 jovyan    (1000) users      (100)      476 2023-04-07 13:28:16.000000 jupyterlab_nbgallery-2.0.0a3/labextension/instrumentation/static/638.b95125ed695cee42aae4.js.LICENSE.txt
+-rw-r--r--   0 jovyan    (1000) users      (100)     8425 2023-04-07 13:28:16.000000 jupyterlab_nbgallery-2.0.0a3/labextension/instrumentation/static/701.d81800f5926ab62cc8b2.js
+-rw-r--r--   0 jovyan    (1000) users      (100)     7555 2023-04-07 13:28:16.000000 jupyterlab_nbgallery-2.0.0a3/labextension/instrumentation/static/remoteEntry.53ed33a8ef1f603e0fc8.js
+-rw-r--r--   0 jovyan    (1000) users      (100)      118 2023-04-07 13:28:10.000000 jupyterlab_nbgallery-2.0.0a3/labextension/instrumentation/static/style.js
+-rw-r--r--   0 jovyan    (1000) users      (100)     2479 2023-04-07 13:28:16.000000 jupyterlab_nbgallery-2.0.0a3/labextension/instrumentation/static/third-party-licenses.json
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.729589 jupyterlab_nbgallery-2.0.0a3/labextension/userpreferences/
+-rw-r--r--   0 jovyan    (1000) users      (100)     2709 2023-04-07 13:28:15.000000 jupyterlab_nbgallery-2.0.0a3/labextension/userpreferences/package.json
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.713590 jupyterlab_nbgallery-2.0.0a3/labextension/userpreferences/schemas/
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.713590 jupyterlab_nbgallery-2.0.0a3/labextension/userpreferences/schemas/@jupyterlab-nbgallery/
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.729589 jupyterlab_nbgallery-2.0.0a3/labextension/userpreferences/schemas/@jupyterlab-nbgallery/userpreferences/
+-rw-r--r--   0 jovyan    (1000) users      (100)     2618 2023-04-07 13:28:10.000000 jupyterlab_nbgallery-2.0.0a3/labextension/userpreferences/schemas/@jupyterlab-nbgallery/userpreferences/package.json.orig
+drwxr-sr-x   0 jovyan    (1000) users      (100)        0 2023-04-07 13:28:16.733590 jupyterlab_nbgallery-2.0.0a3/labextension/userpreferences/static/
+-rw-r--r--   0 jovyan    (1000) users      (100)     4026 2023-04-07 13:28:15.000000 jupyterlab_nbgallery-2.0.0a3/labextension/userpreferences/static/542.d1718a50e23f3808ba62.js
+-rw-r--r--   0 jovyan    (1000) users      (100)     4114 2023-04-07 13:28:15.000000 jupyterlab_nbgallery-2.0.0a3/labextension/userpreferences/static/568.00695541aaa15d567580.js
+-rw-r--r--   0 jovyan    (1000) users      (100)    90044 2023-04-07 13:28:15.000000 jupyterlab_nbgallery-2.0.0a3/labextension/userpreferences/static/638.e5080f99954048969f76.js
+-rw-r--r--   0 jovyan    (1000) users      (100)      476 2023-04-07 13:28:15.000000 jupyterlab_nbgallery-2.0.0a3/labextension/userpreferences/static/638.e5080f99954048969f76.js.LICENSE.txt
+-rw-r--r--   0 jovyan    (1000) users      (100)     7095 2023-04-07 13:28:15.000000 jupyterlab_nbgallery-2.0.0a3/labextension/userpreferences/static/remoteEntry.03bf745401d2317e1d7d.js
+-rw-r--r--   0 jovyan    (1000) users      (100)      181 2023-04-07 13:28:10.000000 jupyterlab_nbgallery-2.0.0a3/labextension/userpreferences/static/style.js
+-rw-r--r--   0 jovyan    (1000) users      (100)     3692 2023-04-07 13:28:15.000000 jupyterlab_nbgallery-2.0.0a3/labextension/userpreferences/static/third-party-licenses.json
+-rw-r--r--   0 jovyan    (1000) users      (100)     1103 2023-04-07 13:26:25.000000 jupyterlab_nbgallery-2.0.0a3/package.json
+-rw-r--r--   0 jovyan    (1000) users      (100)      145 2023-04-07 13:26:25.000000 jupyterlab_nbgallery-2.0.0a3/pyproject.toml
+-rw-r--r--   0 jovyan    (1000) users      (100)       38 2023-04-07 13:28:16.733590 jupyterlab_nbgallery-2.0.0a3/setup.cfg
+-rw-r--r--   0 jovyan    (1000) users      (100)     3928 2023-04-07 13:26:25.000000 jupyterlab_nbgallery-2.0.0a3/setup.py
```

### Comparing `jupyterlab_nbgallery-2.0.0a2/LICENSE` & `jupyterlab_nbgallery-2.0.0a3/LICENSE`

 * *Files identical despite different names*

### Comparing `jupyterlab_nbgallery-2.0.0a2/PKG-INFO` & `jupyterlab_nbgallery-2.0.0a3/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: jupyterlab_nbgallery
-Version: 2.0.0a2
+Version: 2.0.0a3
 Summary: A JupyterLab Extension for NBGallery integration
 Home-page: https://github.com/nbgallery/lab-extensions
 Author: NBGallery
 License: MIT
 Keywords: Jupyter,JupyterLab
 Platform: Linux
 Platform: Mac OS X
```

### Comparing `jupyterlab_nbgallery-2.0.0a2/README.md` & `jupyterlab_nbgallery-2.0.0a3/README.md`

 * *Files identical despite different names*

### Comparing `jupyterlab_nbgallery-2.0.0a2/jupyterlab_nbgallery/__init__.py` & `jupyterlab_nbgallery-2.0.0a3/jupyterlab_nbgallery/__init__.py`

 * *Files identical despite different names*

### Comparing `jupyterlab_nbgallery-2.0.0a2/jupyterlab_nbgallery/handlers.py` & `jupyterlab_nbgallery-2.0.0a3/jupyterlab_nbgallery/handlers.py`

 * *Files identical despite different names*

### Comparing `jupyterlab_nbgallery-2.0.0a2/jupyterlab_nbgallery.egg-info/PKG-INFO` & `jupyterlab_nbgallery-2.0.0a3/jupyterlab_nbgallery.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: jupyterlab-nbgallery
-Version: 2.0.0a2
+Version: 2.0.0a3
 Summary: A JupyterLab Extension for NBGallery integration
 Home-page: https://github.com/nbgallery/lab-extensions
 Author: NBGallery
 License: MIT
 Keywords: Jupyter,JupyterLab
 Platform: Linux
 Platform: Mac OS X
```

### Comparing `jupyterlab_nbgallery-2.0.0a2/jupyterlab_nbgallery.egg-info/SOURCES.txt` & `jupyterlab_nbgallery-2.0.0a3/jupyterlab_nbgallery.egg-info/SOURCES.txt`

 * *Files 2% similar despite different names*

```diff
@@ -40,18 +40,18 @@
 labextension/environment-registration/static/784.c5c708b87c266cbabd98.js
 labextension/environment-registration/static/remoteEntry.00e0256ee314fd224ea3.js
 labextension/environment-registration/static/style.js
 labextension/environment-registration/static/third-party-licenses.json
 labextension/gallerymenu/package.json
 labextension/gallerymenu/schemas/@jupyterlab-nbgallery/gallerymenu/package.json.orig
 labextension/gallerymenu/static/542.18fd91d86aaf6286edd0.js
-labextension/gallerymenu/static/56.8dc3eaf446ef31335c65.js
+labextension/gallerymenu/static/56.00b49e0c37b3050cbc14.js
 labextension/gallerymenu/static/638.95e0186307171588df5b.js
 labextension/gallerymenu/static/638.95e0186307171588df5b.js.LICENSE.txt
-labextension/gallerymenu/static/remoteEntry.3280b8022411403d2f46.js
+labextension/gallerymenu/static/remoteEntry.ae9dddbb4a23b1552c19.js
 labextension/gallerymenu/static/style.js
 labextension/gallerymenu/static/third-party-licenses.json
 labextension/inject-uuid/package.json
 labextension/inject-uuid/schemas/@jupyterlab-nbgallery/inject-uuid/package.json.orig
 labextension/inject-uuid/static/568.1dcbb7bee8ca1152cf60.js
 labextension/inject-uuid/static/remoteEntry.02ddda09f0305fa467f4.js
 labextension/inject-uuid/static/style.js
```

### Comparing `jupyterlab_nbgallery-2.0.0a2/labextension/autodownload/package.json` & `jupyterlab_nbgallery-2.0.0a3/labextension/autodownload/package.json`

 * *Files identical despite different names*

### Comparing `jupyterlab_nbgallery-2.0.0a2/labextension/autodownload/schemas/@jupyterlab-nbgallery/autodownload/package.json.orig` & `jupyterlab_nbgallery-2.0.0a3/labextension/autodownload/schemas/@jupyterlab-nbgallery/autodownload/package.json.orig`

 * *Files identical despite different names*

### Comparing `jupyterlab_nbgallery-2.0.0a2/labextension/autodownload/static/542.51fb91347d8a3d9a657a.js` & `jupyterlab_nbgallery-2.0.0a3/labextension/autodownload/static/542.51fb91347d8a3d9a657a.js`

 * *Files identical despite different names*

### Comparing `jupyterlab_nbgallery-2.0.0a2/labextension/autodownload/static/568.088b227a0b6b6168ee16.js` & `jupyterlab_nbgallery-2.0.0a3/labextension/autodownload/static/568.088b227a0b6b6168ee16.js`

 * *Files identical despite different names*

### Comparing `jupyterlab_nbgallery-2.0.0a2/labextension/autodownload/static/638.0ed295d9378dea7c5c7b.js` & `jupyterlab_nbgallery-2.0.0a3/labextension/autodownload/static/638.0ed295d9378dea7c5c7b.js`

 * *Files identical despite different names*

### Comparing `jupyterlab_nbgallery-2.0.0a2/labextension/autodownload/static/remoteEntry.fa15592bca73423b04a4.js` & `jupyterlab_nbgallery-2.0.0a3/labextension/autodownload/static/remoteEntry.fa15592bca73423b04a4.js`

 * *Files identical despite different names*

### Comparing `jupyterlab_nbgallery-2.0.0a2/labextension/autodownload/static/third-party-licenses.json` & `jupyterlab_nbgallery-2.0.0a3/labextension/autodownload/static/third-party-licenses.json`

 * *Files identical despite different names*

### Comparing `jupyterlab_nbgallery-2.0.0a2/labextension/environment-life/package.json` & `jupyterlab_nbgallery-2.0.0a3/labextension/environment-life/package.json`

 * *Files identical despite different names*

### Comparing `jupyterlab_nbgallery-2.0.0a2/labextension/environment-life/schemas/@jupyterlab-nbgallery/environment-life/package.json.orig` & `jupyterlab_nbgallery-2.0.0a3/labextension/environment-life/schemas/@jupyterlab-nbgallery/environment-life/package.json.orig`

 * *Files identical despite different names*

### Comparing `jupyterlab_nbgallery-2.0.0a2/labextension/environment-life/static/248.1d3351413b89920be9fb.js` & `jupyterlab_nbgallery-2.0.0a3/labextension/environment-life/static/248.1d3351413b89920be9fb.js`

 * *Files identical despite different names*

### Comparing `jupyterlab_nbgallery-2.0.0a2/labextension/environment-life/static/542.e4d405f3b0e4f693ab53.js` & `jupyterlab_nbgallery-2.0.0a3/labextension/environment-life/static/542.e4d405f3b0e4f693ab53.js`

 * *Files identical despite different names*

### Comparing `jupyterlab_nbgallery-2.0.0a2/labextension/environment-life/static/remoteEntry.dd7691336809bc6771e3.js` & `jupyterlab_nbgallery-2.0.0a3/labextension/environment-life/static/remoteEntry.dd7691336809bc6771e3.js`

 * *Files identical despite different names*

### Comparing `jupyterlab_nbgallery-2.0.0a2/labextension/environment-life/static/third-party-licenses.json` & `jupyterlab_nbgallery-2.0.0a3/labextension/environment-life/static/third-party-licenses.json`

 * *Files identical despite different names*

### Comparing `jupyterlab_nbgallery-2.0.0a2/labextension/environment-registration/package.json` & `jupyterlab_nbgallery-2.0.0a3/labextension/environment-registration/package.json`

 * *Files identical despite different names*

### Comparing `jupyterlab_nbgallery-2.0.0a2/labextension/environment-registration/schemas/@jupyterlab-nbgallery/environment-registration/environment-registration.json` & `jupyterlab_nbgallery-2.0.0a3/labextension/environment-registration/schemas/@jupyterlab-nbgallery/environment-registration/environment-registration.json`

 * *Files identical despite different names*

### Comparing `jupyterlab_nbgallery-2.0.0a2/labextension/environment-registration/schemas/@jupyterlab-nbgallery/environment-registration/package.json.orig` & `jupyterlab_nbgallery-2.0.0a3/labextension/environment-registration/schemas/@jupyterlab-nbgallery/environment-registration/package.json.orig`

 * *Files identical despite different names*

### Comparing `jupyterlab_nbgallery-2.0.0a2/labextension/environment-registration/static/542.feae6c397f33f9138fea.js` & `jupyterlab_nbgallery-2.0.0a3/labextension/environment-registration/static/542.feae6c397f33f9138fea.js`

 * *Files identical despite different names*

### Comparing `jupyterlab_nbgallery-2.0.0a2/labextension/environment-registration/static/638.36e464d3233849b6b07a.js` & `jupyterlab_nbgallery-2.0.0a3/labextension/environment-registration/static/638.36e464d3233849b6b07a.js`

 * *Files identical despite different names*

### Comparing `jupyterlab_nbgallery-2.0.0a2/labextension/environment-registration/static/784.c5c708b87c266cbabd98.js` & `jupyterlab_nbgallery-2.0.0a3/labextension/environment-registration/static/784.c5c708b87c266cbabd98.js`

 * *Files identical despite different names*

### Comparing `jupyterlab_nbgallery-2.0.0a2/labextension/environment-registration/static/remoteEntry.00e0256ee314fd224ea3.js` & `jupyterlab_nbgallery-2.0.0a3/labextension/environment-registration/static/remoteEntry.00e0256ee314fd224ea3.js`

 * *Files identical despite different names*

### Comparing `jupyterlab_nbgallery-2.0.0a2/labextension/environment-registration/static/third-party-licenses.json` & `jupyterlab_nbgallery-2.0.0a3/labextension/environment-registration/static/third-party-licenses.json`

 * *Files identical despite different names*

### Comparing `jupyterlab_nbgallery-2.0.0a2/labextension/gallerymenu/package.json` & `jupyterlab_nbgallery-2.0.0a3/labextension/gallerymenu/schemas/@jupyterlab-nbgallery/gallerymenu/package.json.orig`

 * *Files 4% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9930555555555556%*

 * *Differences: {"'jupyterlab'": "{delete: ['_build']}"}*

```diff
@@ -29,19 +29,14 @@
     "files": [
         "lib/**/*.{d.ts,eot,gif,html,jpg,js,js.map,json,png,svg,woff2,ttf}",
         "style/**/*.{css,eot,gif,html,jpg,json,png,svg,woff2,ttf}",
         "schema/**/*.json"
     ],
     "homepage": "https://github.com/nbgallery/lab-extensions",
     "jupyterlab": {
-        "_build": {
-            "extension": "./extension",
-            "load": "static/remoteEntry.3280b8022411403d2f46.js",
-            "style": "./style"
-        },
         "extension": true,
         "outputDir": "../labextension/gallerymenu",
         "schemaDir": "schema"
     },
     "keywords": [
         "jupyter",
         "jupyterlab",
```

### Comparing `jupyterlab_nbgallery-2.0.0a2/labextension/gallerymenu/schemas/@jupyterlab-nbgallery/gallerymenu/package.json.orig` & `jupyterlab_nbgallery-2.0.0a3/labextension/gallerymenu/package.json`

 * *Files 4% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9930555555555556%*

 * *Differences: {"'jupyterlab'": "{'_build': OrderedDict([('load', 'static/remoteEntry.ae9dddbb4a23b1552c19.js'), "*

 * *                 "('extension', './extension'), ('style', './style')])}"}*

```diff
@@ -29,14 +29,19 @@
     "files": [
         "lib/**/*.{d.ts,eot,gif,html,jpg,js,js.map,json,png,svg,woff2,ttf}",
         "style/**/*.{css,eot,gif,html,jpg,json,png,svg,woff2,ttf}",
         "schema/**/*.json"
     ],
     "homepage": "https://github.com/nbgallery/lab-extensions",
     "jupyterlab": {
+        "_build": {
+            "extension": "./extension",
+            "load": "static/remoteEntry.ae9dddbb4a23b1552c19.js",
+            "style": "./style"
+        },
         "extension": true,
         "outputDir": "../labextension/gallerymenu",
         "schemaDir": "schema"
     },
     "keywords": [
         "jupyter",
         "jupyterlab",
```

### Comparing `jupyterlab_nbgallery-2.0.0a2/labextension/gallerymenu/static/542.18fd91d86aaf6286edd0.js` & `jupyterlab_nbgallery-2.0.0a3/labextension/gallerymenu/static/542.18fd91d86aaf6286edd0.js`

 * *Files identical despite different names*

### Comparing `jupyterlab_nbgallery-2.0.0a2/labextension/gallerymenu/static/56.8dc3eaf446ef31335c65.js` & `jupyterlab_nbgallery-2.0.0a3/labextension/gallerymenu/static/56.00b49e0c37b3050cbc14.js`

 * *Files 2% similar despite different names*

#### js-beautify {}

```diff
@@ -190,15 +190,15 @@
                             data: JSON.stringify(this.stripOutput(e))
                         })
                     } catch (e) {
                         return void(0, i.showErrorMessage)("Staging Failed", "An error occured attempting to upload the specified notebook.  Please ensure that you are logged in to the Gallery.")
                     }
                 }
                 finishUpload(e, t, a, l, i, o) {
-                    t ? i ? window.open(l.origin + "/notebook/" + t.uuid + "?staged=" + a.staging_id + "#CHANGE_REQ") : t.link ? window.open(l.origin + "/notebook/" + a.link + "?staged=" + a.staging_id + "#UPDATE") : window.open(l.origin + "?staged=" + a.staging_id + "#STAGE") : window.open(l.origin + "?staged=" + a.staging_id + "&tags=" + encodeURIComponent(o) + "#STAGE")
+                    t ? i ? window.open(l.origin + "/notebook/" + t.uuid + "?staged=" + a.staging_id + "#CHANGE_REQ") : t.link ? window.open(l.origin + "/notebook/" + a.link + "?staged=" + a.staging_id + "#UPDATE") : window.open(l.origin + "?staged=" + a.staging_id + "&parent_uuid=" + t.parent_uuid + "#STAGE") : window.open(l.origin + "?staged=" + a.staging_id + "&tags=" + encodeURIComponent(o) + "#STAGE")
                 }
                 async uploadCallback() {
                     let e;
                     this.triggerSave(), e = this.currentNotebook();
                     let t = this.getGalleryMetadata(e),
                         a = this.getGalleryLink(),
                         l = await this.stageNotebook(e, a, null),
@@ -352,16 +352,19 @@
                             this.saveCallback()
                         }
                     }), e.addCommand("gallery-fork", {
                         label: "Upload as a New Notebook (Fork)",
                         isEnabled: () => this.hasUUID(),
                         isVisible: () => this.hasUUID(),
                         execute: () => {
-                            let e = this.currentNotebook();
-                            this.setGalleryMetadata(e, {}), this.uploadCallback()
+                            let e = this.currentNotebook(),
+                                t = this.getGalleryMetadata(e).uuid;
+                            this.setGalleryMetadata(e, {
+                                parent_uuid: t
+                            }), this.uploadCallback()
                         }
                     }), e.addCommand("gallery-changereq", {
                         label: "Submit Change Request",
                         isEnabled: () => this.hasUUID(),
                         isVisible: () => this.hasUUID(),
                         execute: () => {
                             this.changereqCallback()
```

### Comparing `jupyterlab_nbgallery-2.0.0a2/labextension/gallerymenu/static/638.95e0186307171588df5b.js` & `jupyterlab_nbgallery-2.0.0a3/labextension/gallerymenu/static/638.95e0186307171588df5b.js`

 * *Files identical despite different names*

### Comparing `jupyterlab_nbgallery-2.0.0a2/labextension/gallerymenu/static/remoteEntry.3280b8022411403d2f46.js` & `jupyterlab_nbgallery-2.0.0a3/labextension/gallerymenu/static/remoteEntry.ae9dddbb4a23b1552c19.js`

 * *Files 4% similar despite different names*

#### js-beautify {}

```diff
@@ -1,11 +1,11 @@
 var _JUPYTERLAB;
 (() => {
     "use strict";
-    var e, r, t, n, a, o, l, i, u, f, s, d, p, c, h, v, b, y, g = {
+    var e, r, t, n, a, o, l, i, u, f, s, d, c, p, h, v, y, g, b = {
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
-        return g[e].call(t.exports, t, t.exports, w), t.exports
+        return b[e].call(t.exports, t, t.exports, w), t.exports
     }
-    w.m = g, w.c = m, w.n = e => {
+    w.m = b, w.c = m, w.n = e => {
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
-        56: "8dc3eaf446ef31335c65",
+        56: "00b49e0c37b3050cbc14",
         542: "18fd91d86aaf6286edd0",
         638: "95e0186307171588df5b"
     } [e] + ".js?v=" + {
-        56: "8dc3eaf446ef31335c65",
+        56: "00b49e0c37b3050cbc14",
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
-                    l.onerror = l.onload = null, clearTimeout(p);
+                    l.onerror = l.onload = null, clearTimeout(c);
                     var a = e[t];
                     if (delete e[t], l.parentNode && l.parentNode.removeChild(l), a && a.forEach((e => e(n))), r) return r(n)
                 },
-                p = setTimeout(d.bind(null, void 0, {
+                c = setTimeout(d.bind(null, void 0, {
                     type: "timeout",
                     target: l
                 }), 12e4);
             l.onerror = d.bind(null, l.onerror), l.onload = d.bind(null, l.onload), i && document.head.appendChild(l)
         }
     }, w.r = e => {
         "undefined" != typeof Symbol && Symbol.toStringTag && Object.defineProperty(e, Symbol.toStringTag, {
@@ -187,66 +187,66 @@
                     u = !1, i--
                 } else {
                     if (i <= n || s < d != a) return !1;
                     u = !1
                 } else "s" != d && "n" != d && (u = !1, i--)
             }
         }
-        var p = [],
-            c = p.pop.bind(p);
+        var c = [],
+            p = c.pop.bind(c);
         for (l = 1; l < e.length; l++) {
             var h = e[l];
-            p.push(1 == h ? c() | c() : 2 == h ? c() & c() : h ? o(h, r) : !c())
+            c.push(1 == h ? p() | p() : 2 == h ? p() & p() : h ? o(h, r) : !p())
         }
-        return !!c()
+        return !!p()
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
-    }, d = e => (e.loaded = 1, e.get()), c = (p = e => function(r, t, n, a) {
+    }, d = e => (e.loaded = 1, e.get()), p = (c = e => function(r, t, n, a) {
         var o = w.I(r);
         return o && o.then ? o.then(e.bind(e, r, w.S[r], t, n, a)) : e(r, w.S[r], t, n, a)
-    })(((e, r, t, n) => (l(e, t), f(r, 0, t, n)))), h = p(((e, r, t, n, a) => {
+    })(((e, r, t, n) => (l(e, t), f(r, 0, t, n)))), h = c(((e, r, t, n, a) => {
         var o = r && w.o(r, t) && s(r, t, n);
         return o ? d(o) : a()
-    })), v = {}, b = {
-        33: () => c("default", "@jupyterlab/apputils", [1, 3, 6, 3]),
-        123: () => c("default", "@jupyterlab/notebook", [1, 3, 6, 3]),
-        142: () => c("default", "@jupyterlab/coreutils", [1, 5, 6, 3]),
-        271: () => c("default", "react", [1, 17, 0, 1]),
-        344: () => c("default", "@jupyterlab/mainmenu", [1, 3, 6, 3]),
+    })), v = {}, y = {
+        33: () => p("default", "@jupyterlab/apputils", [1, 3, 6, 3]),
+        123: () => p("default", "@jupyterlab/notebook", [1, 3, 6, 3]),
+        142: () => p("default", "@jupyterlab/coreutils", [1, 5, 6, 3]),
+        271: () => p("default", "react", [1, 17, 0, 1]),
+        344: () => p("default", "@jupyterlab/mainmenu", [1, 3, 6, 3]),
         569: () => h("default", "jquery", [1, 3, 5, 0], (() => w.e(638).then((() => () => w(638))))),
-        820: () => c("default", "@jupyterlab/services", [1, 6, 6, 3]),
-        832: () => c("default", "@lumino/widgets", [1, 1, 37, 2])
-    }, y = {
+        820: () => p("default", "@jupyterlab/services", [1, 6, 6, 3]),
+        832: () => p("default", "@lumino/widgets", [1, 1, 37, 2])
+    }, g = {
         56: [33, 123, 142, 271, 344, 569, 820, 832]
     }, w.f.consumes = (e, r) => {
-        w.o(y, e) && y[e].forEach((e => {
+        w.o(g, e) && g[e].forEach((e => {
             if (w.o(v, e)) return r.push(v[e]);
             var t = r => {
                     v[e] = 0, w.m[e] = t => {
                         delete w.c[e], t.exports = r()
                     }
                 },
                 n = r => {
                     delete v[e], w.m[e] = t => {
                         throw delete w.c[e], r
                     }
                 };
             try {
-                var a = b[e]();
+                var a = y[e]();
                 a.then ? r.push(v[e] = a.then(t).catch(n)) : t(a)
             } catch (e) {
                 n(e)
             }
         }))
     }, (() => {
         var e = {
```

### Comparing `jupyterlab_nbgallery-2.0.0a2/labextension/gallerymenu/static/third-party-licenses.json` & `jupyterlab_nbgallery-2.0.0a3/labextension/gallerymenu/static/third-party-licenses.json`

 * *Files identical despite different names*

### Comparing `jupyterlab_nbgallery-2.0.0a2/labextension/inject-uuid/package.json` & `jupyterlab_nbgallery-2.0.0a3/labextension/inject-uuid/package.json`

 * *Files identical despite different names*

### Comparing `jupyterlab_nbgallery-2.0.0a2/labextension/inject-uuid/schemas/@jupyterlab-nbgallery/inject-uuid/package.json.orig` & `jupyterlab_nbgallery-2.0.0a3/labextension/inject-uuid/schemas/@jupyterlab-nbgallery/inject-uuid/package.json.orig`

 * *Files identical despite different names*

### Comparing `jupyterlab_nbgallery-2.0.0a2/labextension/inject-uuid/static/568.1dcbb7bee8ca1152cf60.js` & `jupyterlab_nbgallery-2.0.0a3/labextension/inject-uuid/static/568.1dcbb7bee8ca1152cf60.js`

 * *Files identical despite different names*

### Comparing `jupyterlab_nbgallery-2.0.0a2/labextension/inject-uuid/static/remoteEntry.02ddda09f0305fa467f4.js` & `jupyterlab_nbgallery-2.0.0a3/labextension/inject-uuid/static/remoteEntry.02ddda09f0305fa467f4.js`

 * *Files identical despite different names*

### Comparing `jupyterlab_nbgallery-2.0.0a2/labextension/instrumentation/package.json` & `jupyterlab_nbgallery-2.0.0a3/labextension/instrumentation/package.json`

 * *Files identical despite different names*

### Comparing `jupyterlab_nbgallery-2.0.0a2/labextension/instrumentation/schemas/@jupyterlab-nbgallery/instrumentation/package.json.orig` & `jupyterlab_nbgallery-2.0.0a3/labextension/instrumentation/schemas/@jupyterlab-nbgallery/instrumentation/package.json.orig`

 * *Files identical despite different names*

### Comparing `jupyterlab_nbgallery-2.0.0a2/labextension/instrumentation/static/568.0d3998aabd22f1867c40.js` & `jupyterlab_nbgallery-2.0.0a3/labextension/instrumentation/static/568.0d3998aabd22f1867c40.js`

 * *Files identical despite different names*

### Comparing `jupyterlab_nbgallery-2.0.0a2/labextension/instrumentation/static/638.b95125ed695cee42aae4.js` & `jupyterlab_nbgallery-2.0.0a3/labextension/instrumentation/static/638.b95125ed695cee42aae4.js`

 * *Files identical despite different names*

### Comparing `jupyterlab_nbgallery-2.0.0a2/labextension/instrumentation/static/701.d81800f5926ab62cc8b2.js` & `jupyterlab_nbgallery-2.0.0a3/labextension/instrumentation/static/701.d81800f5926ab62cc8b2.js`

 * *Files identical despite different names*

### Comparing `jupyterlab_nbgallery-2.0.0a2/labextension/instrumentation/static/remoteEntry.53ed33a8ef1f603e0fc8.js` & `jupyterlab_nbgallery-2.0.0a3/labextension/instrumentation/static/remoteEntry.53ed33a8ef1f603e0fc8.js`

 * *Files identical despite different names*

### Comparing `jupyterlab_nbgallery-2.0.0a2/labextension/instrumentation/static/third-party-licenses.json` & `jupyterlab_nbgallery-2.0.0a3/labextension/instrumentation/static/third-party-licenses.json`

 * *Files identical despite different names*

### Comparing `jupyterlab_nbgallery-2.0.0a2/labextension/userpreferences/package.json` & `jupyterlab_nbgallery-2.0.0a3/labextension/userpreferences/package.json`

 * *Files identical despite different names*

### Comparing `jupyterlab_nbgallery-2.0.0a2/labextension/userpreferences/schemas/@jupyterlab-nbgallery/userpreferences/package.json.orig` & `jupyterlab_nbgallery-2.0.0a3/labextension/userpreferences/schemas/@jupyterlab-nbgallery/userpreferences/package.json.orig`

 * *Files identical despite different names*

### Comparing `jupyterlab_nbgallery-2.0.0a2/labextension/userpreferences/static/542.d1718a50e23f3808ba62.js` & `jupyterlab_nbgallery-2.0.0a3/labextension/userpreferences/static/542.d1718a50e23f3808ba62.js`

 * *Files identical despite different names*

### Comparing `jupyterlab_nbgallery-2.0.0a2/labextension/userpreferences/static/568.00695541aaa15d567580.js` & `jupyterlab_nbgallery-2.0.0a3/labextension/userpreferences/static/568.00695541aaa15d567580.js`

 * *Files identical despite different names*

### Comparing `jupyterlab_nbgallery-2.0.0a2/labextension/userpreferences/static/638.e5080f99954048969f76.js` & `jupyterlab_nbgallery-2.0.0a3/labextension/userpreferences/static/638.e5080f99954048969f76.js`

 * *Files identical despite different names*

### Comparing `jupyterlab_nbgallery-2.0.0a2/labextension/userpreferences/static/remoteEntry.03bf745401d2317e1d7d.js` & `jupyterlab_nbgallery-2.0.0a3/labextension/userpreferences/static/remoteEntry.03bf745401d2317e1d7d.js`

 * *Files identical despite different names*

### Comparing `jupyterlab_nbgallery-2.0.0a2/labextension/userpreferences/static/third-party-licenses.json` & `jupyterlab_nbgallery-2.0.0a3/labextension/userpreferences/static/third-party-licenses.json`

 * *Files identical despite different names*

### Comparing `jupyterlab_nbgallery-2.0.0a2/package.json` & `jupyterlab_nbgallery-2.0.0a3/package.json`

 * *Files identical despite different names*

### Comparing `jupyterlab_nbgallery-2.0.0a2/setup.py` & `jupyterlab_nbgallery-2.0.0a3/setup.py`

 * *Files identical despite different names*

