# Comparing `tmp/fugue_jupyter-0.2.2.tar.gz` & `tmp/fugue_jupyter-0.2.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "fugue_jupyter-0.2.2.tar", last modified: Tue Jan 31 07:51:30 2023, max compression
+gzip compressed data, was "fugue_jupyter-0.2.3.tar", last modified: Fri Apr  7 06:03:43 2023, max compression
```

## Comparing `fugue_jupyter-0.2.2.tar` & `fugue_jupyter-0.2.3.tar`

### file list

```diff
@@ -1,65 +1,65 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-31 07:51:30.594341 fugue_jupyter-0.2.2/
--rw-r--r--   0 runner    (1001) docker     (123)       86 2023-01-31 07:48:46.000000 fugue_jupyter-0.2.2/CHANGELOG.md
--rw-r--r--   0 runner    (1001) docker     (123)     1865 2023-01-31 07:48:46.000000 fugue_jupyter-0.2.2/CONTRIBUTING.md
--rw-r--r--   0 runner    (1001) docker     (123)    11357 2023-01-31 07:48:46.000000 fugue_jupyter-0.2.2/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)      439 2023-01-31 07:48:46.000000 fugue_jupyter-0.2.2/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     2351 2023-01-31 07:51:30.594341 fugue_jupyter-0.2.2/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     1321 2023-01-31 07:48:46.000000 fugue_jupyter-0.2.2/README.md
--rw-r--r--   0 runner    (1001) docker     (123)      315 2023-01-31 07:48:46.000000 fugue_jupyter-0.2.2/RELEASE.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-31 07:51:30.586341 fugue_jupyter-0.2.2/fugue_jupyter/
--rw-r--r--   0 runner    (1001) docker     (123)      853 2023-01-31 07:48:46.000000 fugue_jupyter-0.2.2/fugue_jupyter/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3015 2023-01-31 07:48:46.000000 fugue_jupyter-0.2.2/fugue_jupyter/_constants.py
--rw-r--r--   0 runner    (1001) docker     (123)     3053 2023-01-31 07:48:46.000000 fugue_jupyter-0.2.2/fugue_jupyter/cmd.py
--rw-r--r--   0 runner    (1001) docker     (123)     1541 2023-01-31 07:48:46.000000 fugue_jupyter-0.2.2/fugue_jupyter/display.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-31 07:51:30.590341 fugue_jupyter-0.2.2/fugue_jupyter/labextension/
--rw-r--r--   0 runner    (1001) docker     (123)    21274 2023-01-31 07:51:07.000000 fugue_jupyter-0.2.2/fugue_jupyter/labextension/build_log.json
--rw-r--r--   0 runner    (1001) docker     (123)     3922 2023-01-31 07:51:08.000000 fugue_jupyter-0.2.2/fugue_jupyter/labextension/package.json
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-31 07:51:30.582341 fugue_jupyter-0.2.2/fugue_jupyter/labextension/schemas/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-31 07:51:30.590341 fugue_jupyter-0.2.2/fugue_jupyter/labextension/schemas/fugue-jupyter/
--rw-r--r--   0 runner    (1001) docker     (123)     3780 2023-01-31 07:51:07.000000 fugue_jupyter-0.2.2/fugue_jupyter/labextension/schemas/fugue-jupyter/package.json.orig
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-31 07:51:30.590341 fugue_jupyter-0.2.2/fugue_jupyter/labextension/static/
--rw-r--r--   0 runner    (1001) docker     (123)    13544 2023-01-31 07:51:08.000000 fugue_jupyter-0.2.2/fugue_jupyter/labextension/static/lib_index_js.ad9a1c1d1f8d504aeb4b.js
--rw-r--r--   0 runner    (1001) docker     (123)    11735 2023-01-31 07:51:08.000000 fugue_jupyter-0.2.2/fugue_jupyter/labextension/static/lib_index_js.ad9a1c1d1f8d504aeb4b.js.map
--rw-r--r--   0 runner    (1001) docker     (123)    28476 2023-01-31 07:51:08.000000 fugue_jupyter-0.2.2/fugue_jupyter/labextension/static/remoteEntry.8a36f4b5ce59a9dca3d8.js
--rw-r--r--   0 runner    (1001) docker     (123)    27210 2023-01-31 07:51:08.000000 fugue_jupyter-0.2.2/fugue_jupyter/labextension/static/remoteEntry.8a36f4b5ce59a9dca3d8.js.map
--rw-r--r--   0 runner    (1001) docker     (123)      156 2023-01-31 07:51:07.000000 fugue_jupyter-0.2.2/fugue_jupyter/labextension/static/style.js
--rw-r--r--   0 runner    (1001) docker     (123)     4598 2023-01-31 07:51:08.000000 fugue_jupyter-0.2.2/fugue_jupyter/labextension/static/style_index_js.308b73f665deca4ee2f3.js
--rw-r--r--   0 runner    (1001) docker     (123)     1782 2023-01-31 07:51:08.000000 fugue_jupyter-0.2.2/fugue_jupyter/labextension/static/style_index_js.308b73f665deca4ee2f3.js.map
--rw-r--r--   0 runner    (1001) docker     (123)    12056 2023-01-31 07:51:08.000000 fugue_jupyter-0.2.2/fugue_jupyter/labextension/static/vendors-node_modules_css-loader_dist_runtime_api_js-node_modules_css-loader_dist_runtime_cssW-72eba1.c07606ee12302cc69c16.js
--rw-r--r--   0 runner    (1001) docker     (123)    13787 2023-01-31 07:51:08.000000 fugue_jupyter-0.2.2/fugue_jupyter/labextension/static/vendors-node_modules_css-loader_dist_runtime_api_js-node_modules_css-loader_dist_runtime_cssW-72eba1.c07606ee12302cc69c16.js.map
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-31 07:51:30.590341 fugue_jupyter-0.2.2/fugue_jupyter/nbextension/
--rw-r--r--   0 runner    (1001) docker     (123)      123 2023-01-31 07:48:46.000000 fugue_jupyter-0.2.2/fugue_jupyter/nbextension/README.md
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-31 07:48:46.000000 fugue_jupyter-0.2.2/fugue_jupyter/nbextension/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      159 2023-01-31 07:48:46.000000 fugue_jupyter-0.2.2/fugue_jupyter/nbextension/description.yaml
--rw-r--r--   0 runner    (1001) docker     (123)     3742 2023-01-31 07:48:46.000000 fugue_jupyter-0.2.2/fugue_jupyter/nbextension/main.js
--rw-r--r--   0 runner    (1001) docker     (123)     3748 2023-01-31 07:48:46.000000 fugue_jupyter-0.2.2/fugue_jupyter/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-31 07:51:30.590341 fugue_jupyter-0.2.2/fugue_jupyter.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     2351 2023-01-31 07:51:30.000000 fugue_jupyter-0.2.2/fugue_jupyter.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     1848 2023-01-31 07:51:30.000000 fugue_jupyter-0.2.2/fugue_jupyter.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-31 07:51:30.000000 fugue_jupyter-0.2.2/fugue_jupyter.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      106 2023-01-31 07:51:30.000000 fugue_jupyter-0.2.2/fugue_jupyter.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-31 07:51:30.000000 fugue_jupyter-0.2.2/fugue_jupyter.egg-info/not-zip-safe
--rw-r--r--   0 runner    (1001) docker     (123)       69 2023-01-31 07:51:30.000000 fugue_jupyter-0.2.2/fugue_jupyter.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       42 2023-01-31 07:51:30.000000 fugue_jupyter-0.2.2/fugue_jupyter.egg-info/top_level.txt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-31 07:51:30.590341 fugue_jupyter-0.2.2/fugue_jupyter_version/
--rw-r--r--   0 runner    (1001) docker     (123)       49 2023-01-31 07:48:46.000000 fugue_jupyter-0.2.2/fugue_jupyter_version/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      659 2023-01-31 07:48:46.000000 fugue_jupyter-0.2.2/fugue_jupyter_version/_version.py
--rw-r--r--   0 runner    (1001) docker     (123)      187 2023-01-31 07:48:46.000000 fugue_jupyter-0.2.2/install.json
--rw-r--r--   0 runner    (1001) docker     (123)     3780 2023-01-31 07:48:46.000000 fugue_jupyter-0.2.2/package.json
--rw-r--r--   0 runner    (1001) docker     (123)      587 2023-01-31 07:48:46.000000 fugue_jupyter-0.2.2/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)      324 2023-01-31 07:51:30.594341 fugue_jupyter-0.2.2/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     3457 2023-01-31 07:48:46.000000 fugue_jupyter-0.2.2/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-31 07:51:30.594341 fugue_jupyter-0.2.2/src/
--rw-r--r--   0 runner    (1001) docker     (123)      362 2023-01-31 07:48:46.000000 fugue_jupyter-0.2.2/src/constants.ts
--rw-r--r--   0 runner    (1001) docker     (123)     4733 2023-01-31 07:48:46.000000 fugue_jupyter-0.2.2/src/index.ts
--rw-r--r--   0 runner    (1001) docker     (123)     5345 2023-01-31 07:48:46.000000 fugue_jupyter-0.2.2/src/utils.ts
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-31 07:51:30.594341 fugue_jupyter-0.2.2/style/
--rw-r--r--   0 runner    (1001) docker     (123)      138 2023-01-31 07:48:46.000000 fugue_jupyter-0.2.2/style/base.css
--rw-r--r--   0 runner    (1001) docker     (123)       25 2023-01-31 07:48:46.000000 fugue_jupyter-0.2.2/style/index.css
--rw-r--r--   0 runner    (1001) docker     (123)       21 2023-01-31 07:48:46.000000 fugue_jupyter-0.2.2/style/index.js
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-31 07:51:30.594341 fugue_jupyter-0.2.2/tests/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-31 07:48:46.000000 fugue_jupyter-0.2.2/tests/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-31 07:51:30.594341 fugue_jupyter-0.2.2/tests/fugue_jupyter/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-31 07:48:46.000000 fugue_jupyter-0.2.2/tests/fugue_jupyter/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      554 2023-01-31 07:48:46.000000 fugue_jupyter-0.2.2/tsconfig.json
--rw-r--r--   0 runner    (1001) docker     (123)   372312 2023-01-31 07:48:46.000000 fugue_jupyter-0.2.2/yarn.lock
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 06:03:43.572638 fugue_jupyter-0.2.3/
+-rw-r--r--   0 runner    (1001) docker     (123)       86 2023-04-07 06:01:22.000000 fugue_jupyter-0.2.3/CHANGELOG.md
+-rw-r--r--   0 runner    (1001) docker     (123)     1865 2023-04-07 06:01:22.000000 fugue_jupyter-0.2.3/CONTRIBUTING.md
+-rw-r--r--   0 runner    (1001) docker     (123)    11357 2023-04-07 06:01:22.000000 fugue_jupyter-0.2.3/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)      439 2023-04-07 06:01:22.000000 fugue_jupyter-0.2.3/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     2351 2023-04-07 06:03:43.572638 fugue_jupyter-0.2.3/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     1321 2023-04-07 06:01:22.000000 fugue_jupyter-0.2.3/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)      360 2023-04-07 06:01:22.000000 fugue_jupyter-0.2.3/RELEASE.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 06:03:43.568638 fugue_jupyter-0.2.3/fugue_jupyter/
+-rw-r--r--   0 runner    (1001) docker     (123)      853 2023-04-07 06:01:22.000000 fugue_jupyter-0.2.3/fugue_jupyter/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3022 2023-04-07 06:01:22.000000 fugue_jupyter-0.2.3/fugue_jupyter/_constants.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3053 2023-04-07 06:01:22.000000 fugue_jupyter-0.2.3/fugue_jupyter/cmd.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1541 2023-04-07 06:01:22.000000 fugue_jupyter-0.2.3/fugue_jupyter/display.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 06:03:43.572638 fugue_jupyter-0.2.3/fugue_jupyter/labextension/
+-rw-r--r--   0 runner    (1001) docker     (123)    21731 2023-04-07 06:03:23.000000 fugue_jupyter-0.2.3/fugue_jupyter/labextension/build_log.json
+-rw-r--r--   0 runner    (1001) docker     (123)     3922 2023-04-07 06:03:24.000000 fugue_jupyter-0.2.3/fugue_jupyter/labextension/package.json
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 06:03:43.568638 fugue_jupyter-0.2.3/fugue_jupyter/labextension/schemas/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 06:03:43.572638 fugue_jupyter-0.2.3/fugue_jupyter/labextension/schemas/fugue-jupyter/
+-rw-r--r--   0 runner    (1001) docker     (123)     3780 2023-04-07 06:03:23.000000 fugue_jupyter-0.2.3/fugue_jupyter/labextension/schemas/fugue-jupyter/package.json.orig
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 06:03:43.572638 fugue_jupyter-0.2.3/fugue_jupyter/labextension/static/
+-rw-r--r--   0 runner    (1001) docker     (123)    13551 2023-04-07 06:03:24.000000 fugue_jupyter-0.2.3/fugue_jupyter/labextension/static/lib_index_js.1b56285a6b63fec28143.js
+-rw-r--r--   0 runner    (1001) docker     (123)    11742 2023-04-07 06:03:24.000000 fugue_jupyter-0.2.3/fugue_jupyter/labextension/static/lib_index_js.1b56285a6b63fec28143.js.map
+-rw-r--r--   0 runner    (1001) docker     (123)    28476 2023-04-07 06:03:24.000000 fugue_jupyter-0.2.3/fugue_jupyter/labextension/static/remoteEntry.99193cc822ff3f92fd07.js
+-rw-r--r--   0 runner    (1001) docker     (123)    27210 2023-04-07 06:03:24.000000 fugue_jupyter-0.2.3/fugue_jupyter/labextension/static/remoteEntry.99193cc822ff3f92fd07.js.map
+-rw-r--r--   0 runner    (1001) docker     (123)      156 2023-04-07 06:03:23.000000 fugue_jupyter-0.2.3/fugue_jupyter/labextension/static/style.js
+-rw-r--r--   0 runner    (1001) docker     (123)     4598 2023-04-07 06:03:24.000000 fugue_jupyter-0.2.3/fugue_jupyter/labextension/static/style_index_js.308b73f665deca4ee2f3.js
+-rw-r--r--   0 runner    (1001) docker     (123)     1782 2023-04-07 06:03:24.000000 fugue_jupyter-0.2.3/fugue_jupyter/labextension/static/style_index_js.308b73f665deca4ee2f3.js.map
+-rw-r--r--   0 runner    (1001) docker     (123)    12056 2023-04-07 06:03:24.000000 fugue_jupyter-0.2.3/fugue_jupyter/labextension/static/vendors-node_modules_css-loader_dist_runtime_api_js-node_modules_css-loader_dist_runtime_cssW-72eba1.c07606ee12302cc69c16.js
+-rw-r--r--   0 runner    (1001) docker     (123)    13787 2023-04-07 06:03:24.000000 fugue_jupyter-0.2.3/fugue_jupyter/labextension/static/vendors-node_modules_css-loader_dist_runtime_api_js-node_modules_css-loader_dist_runtime_cssW-72eba1.c07606ee12302cc69c16.js.map
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 06:03:43.572638 fugue_jupyter-0.2.3/fugue_jupyter/nbextension/
+-rw-r--r--   0 runner    (1001) docker     (123)      123 2023-04-07 06:01:22.000000 fugue_jupyter-0.2.3/fugue_jupyter/nbextension/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 06:01:22.000000 fugue_jupyter-0.2.3/fugue_jupyter/nbextension/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      159 2023-04-07 06:01:22.000000 fugue_jupyter-0.2.3/fugue_jupyter/nbextension/description.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)     3749 2023-04-07 06:01:22.000000 fugue_jupyter-0.2.3/fugue_jupyter/nbextension/main.js
+-rw-r--r--   0 runner    (1001) docker     (123)     3748 2023-04-07 06:01:22.000000 fugue_jupyter-0.2.3/fugue_jupyter/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 06:03:43.572638 fugue_jupyter-0.2.3/fugue_jupyter.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     2351 2023-04-07 06:03:43.000000 fugue_jupyter-0.2.3/fugue_jupyter.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     1848 2023-04-07 06:03:43.000000 fugue_jupyter-0.2.3/fugue_jupyter.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 06:03:43.000000 fugue_jupyter-0.2.3/fugue_jupyter.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      106 2023-04-07 06:03:43.000000 fugue_jupyter-0.2.3/fugue_jupyter.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 06:03:43.000000 fugue_jupyter-0.2.3/fugue_jupyter.egg-info/not-zip-safe
+-rw-r--r--   0 runner    (1001) docker     (123)       71 2023-04-07 06:03:43.000000 fugue_jupyter-0.2.3/fugue_jupyter.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       42 2023-04-07 06:03:43.000000 fugue_jupyter-0.2.3/fugue_jupyter.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 06:03:43.572638 fugue_jupyter-0.2.3/fugue_jupyter_version/
+-rw-r--r--   0 runner    (1001) docker     (123)       49 2023-04-07 06:01:22.000000 fugue_jupyter-0.2.3/fugue_jupyter_version/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      659 2023-04-07 06:01:22.000000 fugue_jupyter-0.2.3/fugue_jupyter_version/_version.py
+-rw-r--r--   0 runner    (1001) docker     (123)      187 2023-04-07 06:01:22.000000 fugue_jupyter-0.2.3/install.json
+-rw-r--r--   0 runner    (1001) docker     (123)     3780 2023-04-07 06:01:22.000000 fugue_jupyter-0.2.3/package.json
+-rw-r--r--   0 runner    (1001) docker     (123)      587 2023-04-07 06:01:22.000000 fugue_jupyter-0.2.3/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)      324 2023-04-07 06:03:43.572638 fugue_jupyter-0.2.3/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     3459 2023-04-07 06:01:22.000000 fugue_jupyter-0.2.3/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 06:03:43.572638 fugue_jupyter-0.2.3/src/
+-rw-r--r--   0 runner    (1001) docker     (123)      362 2023-04-07 06:01:22.000000 fugue_jupyter-0.2.3/src/constants.ts
+-rw-r--r--   0 runner    (1001) docker     (123)     4733 2023-04-07 06:01:22.000000 fugue_jupyter-0.2.3/src/index.ts
+-rw-r--r--   0 runner    (1001) docker     (123)     5352 2023-04-07 06:01:22.000000 fugue_jupyter-0.2.3/src/utils.ts
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 06:03:43.572638 fugue_jupyter-0.2.3/style/
+-rw-r--r--   0 runner    (1001) docker     (123)      138 2023-04-07 06:01:22.000000 fugue_jupyter-0.2.3/style/base.css
+-rw-r--r--   0 runner    (1001) docker     (123)       25 2023-04-07 06:01:22.000000 fugue_jupyter-0.2.3/style/index.css
+-rw-r--r--   0 runner    (1001) docker     (123)       21 2023-04-07 06:01:22.000000 fugue_jupyter-0.2.3/style/index.js
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 06:03:43.572638 fugue_jupyter-0.2.3/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 06:01:22.000000 fugue_jupyter-0.2.3/tests/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 06:03:43.572638 fugue_jupyter-0.2.3/tests/fugue_jupyter/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 06:01:22.000000 fugue_jupyter-0.2.3/tests/fugue_jupyter/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      554 2023-04-07 06:01:22.000000 fugue_jupyter-0.2.3/tsconfig.json
+-rw-r--r--   0 runner    (1001) docker     (123)   372312 2023-04-07 06:01:22.000000 fugue_jupyter-0.2.3/yarn.lock
```

### Comparing `fugue_jupyter-0.2.2/CONTRIBUTING.md` & `fugue_jupyter-0.2.3/CONTRIBUTING.md`

 * *Files identical despite different names*

### Comparing `fugue_jupyter-0.2.2/LICENSE` & `fugue_jupyter-0.2.3/LICENSE`

 * *Files identical despite different names*

### Comparing `fugue_jupyter-0.2.2/PKG-INFO` & `fugue_jupyter-0.2.3/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: fugue_jupyter
-Version: 0.2.2
+Version: 0.2.3
 Summary: Jupyterlab Extension for Fugue
 Home-page: https://github.com/fugue-project/fugue-jupyter
 Author: The Fugue Development Team
 Author-email: hello@fugue.ai
 License: BSD-3-Clause
 Keywords: Jupyter,JupyterLab,JupyterLab3
 Platform: Linux
```

### Comparing `fugue_jupyter-0.2.2/README.md` & `fugue_jupyter-0.2.3/README.md`

 * *Files identical despite different names*

### Comparing `fugue_jupyter-0.2.2/fugue_jupyter/__init__.py` & `fugue_jupyter-0.2.3/fugue_jupyter/__init__.py`

 * *Files identical despite different names*

### Comparing `fugue_jupyter-0.2.2/fugue_jupyter/_constants.py` & `fugue_jupyter-0.2.3/fugue_jupyter/_constants.py`

 * *Files 5% similar despite different names*

```diff
@@ -3,15 +3,15 @@
 _HIGHLIGHT_JS = r"""
 require(["codemirror/lib/codemirror"]);
 function set(str) {
     var obj = {}, words = str.split(" ");
     for (var i = 0; i < words.length; ++i) obj[words[i]] = true;
     return obj;
   }
-var fugue_keywords = "system bernoulli reservoir approx fill hash rand even presort persist broadcast params process output outtransform rowcount concurrency prepartition zip print title save append parquet csv json single checkpoint weak strong deterministic yield connect sample seed take sub callback dataframe file";
+var fugue_keywords = "system bernoulli reservoir approx fill hash rand even coarse presort persist broadcast params process output outtransform rowcount concurrency prepartition zip print title save append parquet csv json single checkpoint weak strong deterministic yield connect sample seed take sub callback dataframe file";
 CodeMirror.defineMIME("text/x-fsql", {
     name: "sql",
     keywords: set(fugue_keywords + " add after all alter analyze and anti archive array as asc at between bucket buckets by cache cascade case cast change clear cluster clustered codegen collection column columns comment commit compact compactions compute concatenate cost create cross cube current current_date current_timestamp database databases data dbproperties defined delete delimited deny desc describe dfs directories distinct distribute drop else end escaped except exchange exists explain export extended external false fields fileformat first following for format formatted from full function functions global grant group grouping having if ignore import in index indexes inner inpath inputformat insert intersect interval into is items join keys last lateral lazy left like limit lines list load local location lock locks logical macro map minus msck natural no not null nulls of on optimize option options or order out outer outputformat over overwrite partition partitioned partitions percent preceding principals purge range recordreader recordwriter recover reduce refresh regexp rename repair replace reset restrict revoke right rlike role roles rollback rollup row rows schema schemas select semi separated serde serdeproperties set sets show skewed sort sorted start statistics stored stratify struct table tables tablesample tblproperties temp temporary terminated then to touch transaction transactions transform true truncate unarchive unbounded uncache union unlock unset use using values view when where window with"),
     builtin: set("date datetime tinyint smallint int bigint boolean float double string binary timestamp decimal array map struct uniontype delimited serde sequencefile textfile rcfile inputformat outputformat"),
     atoms: set("false true null"),
     operatorChars: /^[*\/+\-%<>!=~&|^]/,
     dateSQL: set("time"),
```

### Comparing `fugue_jupyter-0.2.2/fugue_jupyter/cmd.py` & `fugue_jupyter-0.2.3/fugue_jupyter/cmd.py`

 * *Files identical despite different names*

### Comparing `fugue_jupyter-0.2.2/fugue_jupyter/display.py` & `fugue_jupyter-0.2.3/fugue_jupyter/display.py`

 * *Files identical despite different names*

### Comparing `fugue_jupyter-0.2.2/fugue_jupyter/labextension/build_log.json` & `fugue_jupyter-0.2.3/fugue_jupyter/labextension/build_log.json`

 * *Files 4% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9998973319049076%*

 * *Differences: {'0': "{'plugins': {1: {'_options': {'shared': {'@jupyterlab/application': {'requiredVersion': "*

 * *      "'^3.6.3'}, '@jupyterlab/application-extension': {'requiredVersion': '^3.6.3'}, "*

 * *      "'@jupyterlab/apputils-extension': {'requiredVersion': '^3.6.3'}, "*

 * *      "'@jupyterlab/cell-toolbar-extension': {'requiredVersion': '^3.6.3'}, "*

 * *      "'@jupyterlab/celltags-extension': {'requiredVersion': '^3.6.3'}, "*

 * *      "'@jupyterlab/codemirror-extension': {'requiredVersion': '^3.6.3'}, "*

 * *      "'@jupyterlab/compl […]*

```diff
@@ -110,434 +110,448 @@
                             "_JUPYTERLAB",
                             "fugue-jupyter"
                         ],
                         "type": "var"
                     },
                     "name": "fugue-jupyter",
                     "shared": {
+                        "@jupyter/ydoc": {
+                            "import": false,
+                            "requiredVersion": "^0.2.3",
+                            "singleton": true
+                        },
                         "@jupyterlab/application": {
                             "import": false,
-                            "requiredVersion": "^3.5.3",
+                            "requiredVersion": "^3.6.3",
                             "singleton": true
                         },
                         "@jupyterlab/application-extension": {
                             "import": false,
-                            "requiredVersion": "^3.5.3"
+                            "requiredVersion": "^3.6.3"
                         },
                         "@jupyterlab/apputils": {
                             "import": false,
-                            "requiredVersion": "^3.5.3",
+                            "requiredVersion": "^3.6.3",
                             "singleton": true
                         },
                         "@jupyterlab/apputils-extension": {
                             "import": false,
-                            "requiredVersion": "^3.5.3"
+                            "requiredVersion": "^3.6.3"
                         },
                         "@jupyterlab/attachments": {
                             "import": false,
-                            "requiredVersion": "^3.5.3"
+                            "requiredVersion": "^3.6.3"
                         },
                         "@jupyterlab/builder": {},
                         "@jupyterlab/cell-toolbar": {
                             "import": false,
-                            "requiredVersion": "^3.5.3",
+                            "requiredVersion": "^3.6.3",
                             "singleton": true
                         },
                         "@jupyterlab/cell-toolbar-extension": {
                             "import": false,
-                            "requiredVersion": "^3.5.3"
+                            "requiredVersion": "^3.6.3"
                         },
                         "@jupyterlab/cells": {
                             "import": false,
-                            "requiredVersion": "^3.5.3"
+                            "requiredVersion": "^3.6.3"
                         },
                         "@jupyterlab/celltags": {
                             "import": false,
-                            "requiredVersion": "^3.5.3"
+                            "requiredVersion": "^3.6.3"
                         },
                         "@jupyterlab/celltags-extension": {
                             "import": false,
-                            "requiredVersion": "^3.5.3"
+                            "requiredVersion": "^3.6.3"
                         },
                         "@jupyterlab/codeeditor": {
                             "import": false,
-                            "requiredVersion": "^3.5.3",
+                            "requiredVersion": "^3.6.3",
                             "singleton": true
                         },
                         "@jupyterlab/codemirror": {
                             "import": false,
-                            "requiredVersion": "^3.5.3",
+                            "requiredVersion": "^3.6.3",
                             "singleton": true
                         },
                         "@jupyterlab/codemirror-extension": {
                             "import": false,
-                            "requiredVersion": "^3.5.3"
+                            "requiredVersion": "^3.6.3"
+                        },
+                        "@jupyterlab/collaboration": {
+                            "import": false,
+                            "requiredVersion": "^3.6.3",
+                            "singleton": true
+                        },
+                        "@jupyterlab/collaboration-extension": {
+                            "import": false,
+                            "requiredVersion": "^3.6.3"
                         },
                         "@jupyterlab/completer": {
                             "import": false,
-                            "requiredVersion": "^3.5.3",
+                            "requiredVersion": "^3.6.3",
                             "singleton": true
                         },
                         "@jupyterlab/completer-extension": {
                             "import": false,
-                            "requiredVersion": "^3.5.3"
+                            "requiredVersion": "^3.6.3"
                         },
                         "@jupyterlab/console": {
                             "import": false,
-                            "requiredVersion": "^3.5.3",
+                            "requiredVersion": "^3.6.3",
                             "singleton": true
                         },
                         "@jupyterlab/console-extension": {
                             "import": false,
-                            "requiredVersion": "^3.5.3"
+                            "requiredVersion": "^3.6.3"
                         },
                         "@jupyterlab/coreutils": {
                             "import": false,
-                            "requiredVersion": "^5.5.3",
+                            "requiredVersion": "^5.6.3",
                             "singleton": true
                         },
                         "@jupyterlab/csvviewer": {
                             "import": false,
-                            "requiredVersion": "^3.5.3"
+                            "requiredVersion": "^3.6.3"
                         },
                         "@jupyterlab/csvviewer-extension": {
                             "import": false,
-                            "requiredVersion": "^3.5.3"
+                            "requiredVersion": "^3.6.3"
                         },
                         "@jupyterlab/debugger": {
                             "import": false,
-                            "requiredVersion": "^3.5.3",
+                            "requiredVersion": "^3.6.3",
                             "singleton": true
                         },
                         "@jupyterlab/debugger-extension": {
                             "import": false,
-                            "requiredVersion": "^3.5.3"
+                            "requiredVersion": "^3.6.3"
                         },
                         "@jupyterlab/docmanager": {
                             "import": false,
-                            "requiredVersion": "^3.5.3",
+                            "requiredVersion": "^3.6.3",
                             "singleton": true
                         },
                         "@jupyterlab/docmanager-extension": {
                             "import": false,
-                            "requiredVersion": "^3.5.3"
+                            "requiredVersion": "^3.6.3"
                         },
                         "@jupyterlab/docprovider": {
                             "import": false,
-                            "requiredVersion": "^3.5.3",
+                            "requiredVersion": "^3.6.3",
                             "singleton": true
                         },
                         "@jupyterlab/docprovider-extension": {
                             "import": false,
-                            "requiredVersion": "^3.5.3"
+                            "requiredVersion": "^3.6.3"
                         },
                         "@jupyterlab/docregistry": {
                             "import": false,
-                            "requiredVersion": "^3.5.3"
+                            "requiredVersion": "^3.6.3"
                         },
                         "@jupyterlab/documentsearch": {
                             "import": false,
-                            "requiredVersion": "^3.5.3",
+                            "requiredVersion": "^3.6.3",
                             "singleton": true
                         },
                         "@jupyterlab/documentsearch-extension": {
                             "import": false,
-                            "requiredVersion": "^3.5.3"
+                            "requiredVersion": "^3.6.3"
                         },
                         "@jupyterlab/extensionmanager": {
                             "import": false,
-                            "requiredVersion": "^3.5.3",
+                            "requiredVersion": "^3.6.3",
                             "singleton": true
                         },
                         "@jupyterlab/extensionmanager-extension": {
                             "import": false,
-                            "requiredVersion": "^3.5.3"
+                            "requiredVersion": "^3.6.3"
                         },
                         "@jupyterlab/filebrowser": {
                             "import": false,
-                            "requiredVersion": "^3.5.3",
+                            "requiredVersion": "^3.6.3",
                             "singleton": true
                         },
                         "@jupyterlab/filebrowser-extension": {
                             "import": false,
-                            "requiredVersion": "^3.5.3"
+                            "requiredVersion": "^3.6.3"
                         },
                         "@jupyterlab/fileeditor": {
                             "import": false,
-                            "requiredVersion": "^3.5.3",
+                            "requiredVersion": "^3.6.3",
                             "singleton": true
                         },
                         "@jupyterlab/fileeditor-extension": {
                             "import": false,
-                            "requiredVersion": "^3.5.3"
+                            "requiredVersion": "^3.6.3"
                         },
                         "@jupyterlab/help-extension": {
                             "import": false,
-                            "requiredVersion": "^3.5.3"
+                            "requiredVersion": "^3.6.3"
                         },
                         "@jupyterlab/htmlviewer": {
                             "import": false,
-                            "requiredVersion": "^3.5.3"
+                            "requiredVersion": "^3.6.3"
                         },
                         "@jupyterlab/htmlviewer-extension": {
                             "import": false,
-                            "requiredVersion": "^3.5.3"
+                            "requiredVersion": "^3.6.3"
                         },
                         "@jupyterlab/hub-extension": {
                             "import": false,
-                            "requiredVersion": "^3.5.3"
+                            "requiredVersion": "^3.6.3"
                         },
                         "@jupyterlab/imageviewer": {
                             "import": false,
-                            "requiredVersion": "^3.5.3",
+                            "requiredVersion": "^3.6.3",
                             "singleton": true
                         },
                         "@jupyterlab/imageviewer-extension": {
                             "import": false,
-                            "requiredVersion": "^3.5.3"
+                            "requiredVersion": "^3.6.3"
                         },
                         "@jupyterlab/inspector": {
                             "import": false,
-                            "requiredVersion": "^3.5.3",
+                            "requiredVersion": "^3.6.3",
                             "singleton": true
                         },
                         "@jupyterlab/inspector-extension": {
                             "import": false,
-                            "requiredVersion": "^3.5.3"
+                            "requiredVersion": "^3.6.3"
                         },
                         "@jupyterlab/javascript-extension": {
                             "import": false,
-                            "requiredVersion": "^3.5.3"
+                            "requiredVersion": "^3.6.3"
                         },
                         "@jupyterlab/json-extension": {
                             "import": false,
-                            "requiredVersion": "^3.5.3"
+                            "requiredVersion": "^3.6.3"
                         },
                         "@jupyterlab/launcher": {
                             "import": false,
-                            "requiredVersion": "^3.5.3",
+                            "requiredVersion": "^3.6.3",
                             "singleton": true
                         },
                         "@jupyterlab/launcher-extension": {
                             "import": false,
-                            "requiredVersion": "^3.5.3"
+                            "requiredVersion": "^3.6.3"
                         },
                         "@jupyterlab/logconsole": {
                             "import": false,
-                            "requiredVersion": "^3.5.3",
+                            "requiredVersion": "^3.6.3",
                             "singleton": true
                         },
                         "@jupyterlab/logconsole-extension": {
                             "import": false,
-                            "requiredVersion": "^3.5.3"
+                            "requiredVersion": "^3.6.3"
                         },
                         "@jupyterlab/mainmenu": {
                             "import": false,
-                            "requiredVersion": "^3.5.3",
+                            "requiredVersion": "^3.6.3",
                             "singleton": true
                         },
                         "@jupyterlab/mainmenu-extension": {
                             "import": false,
-                            "requiredVersion": "^3.5.3"
+                            "requiredVersion": "^3.6.3"
                         },
                         "@jupyterlab/markdownviewer": {
                             "import": false,
-                            "requiredVersion": "^3.5.3",
+                            "requiredVersion": "^3.6.3",
                             "singleton": true
                         },
                         "@jupyterlab/markdownviewer-extension": {
                             "import": false,
-                            "requiredVersion": "^3.5.3"
+                            "requiredVersion": "^3.6.3"
                         },
                         "@jupyterlab/mathjax2": {
                             "import": false,
-                            "requiredVersion": "^3.5.3"
+                            "requiredVersion": "^3.6.3"
                         },
                         "@jupyterlab/mathjax2-extension": {
                             "import": false,
-                            "requiredVersion": "^3.5.3"
+                            "requiredVersion": "^3.6.3"
                         },
                         "@jupyterlab/metapackage": {
                             "import": false,
-                            "requiredVersion": "^3.5.3"
+                            "requiredVersion": "^3.6.3"
                         },
                         "@jupyterlab/nbconvert-css": {
                             "import": false,
-                            "requiredVersion": "^3.5.3"
+                            "requiredVersion": "^3.6.3"
                         },
                         "@jupyterlab/nbformat": {
                             "import": false,
-                            "requiredVersion": "^3.5.3"
+                            "requiredVersion": "^3.6.3"
                         },
                         "@jupyterlab/notebook": {
                             "import": false,
-                            "requiredVersion": "^3.5.3",
+                            "requiredVersion": "^3.6.3",
                             "singleton": true
                         },
                         "@jupyterlab/notebook-extension": {
                             "import": false,
-                            "requiredVersion": "^3.5.3"
+                            "requiredVersion": "^3.6.3"
                         },
                         "@jupyterlab/observables": {
                             "import": false,
-                            "requiredVersion": "^4.5.3"
+                            "requiredVersion": "^4.6.3"
                         },
                         "@jupyterlab/outputarea": {
                             "import": false,
-                            "requiredVersion": "^3.5.3"
+                            "requiredVersion": "^3.6.3"
                         },
                         "@jupyterlab/pdf-extension": {
                             "import": false,
-                            "requiredVersion": "^3.5.3"
+                            "requiredVersion": "^3.6.3"
                         },
                         "@jupyterlab/property-inspector": {
                             "import": false,
-                            "requiredVersion": "^3.5.3"
+                            "requiredVersion": "^3.6.3"
                         },
                         "@jupyterlab/rendermime": {
                             "import": false,
-                            "requiredVersion": "^3.5.3",
+                            "requiredVersion": "^3.6.3",
                             "singleton": true
                         },
                         "@jupyterlab/rendermime-extension": {
                             "import": false,
-                            "requiredVersion": "^3.5.3"
+                            "requiredVersion": "^3.6.3"
                         },
                         "@jupyterlab/rendermime-interfaces": {
                             "import": false,
-                            "requiredVersion": "^3.5.3",
+                            "requiredVersion": "^3.6.3",
                             "singleton": true
                         },
                         "@jupyterlab/running": {
                             "import": false,
-                            "requiredVersion": "^3.5.3"
+                            "requiredVersion": "^3.6.3"
                         },
                         "@jupyterlab/running-extension": {
                             "import": false,
-                            "requiredVersion": "^3.5.3"
+                            "requiredVersion": "^3.6.3"
                         },
                         "@jupyterlab/services": {
                             "import": false,
-                            "requiredVersion": "^6.5.3",
+                            "requiredVersion": "^6.6.3",
                             "singleton": true
                         },
                         "@jupyterlab/settingeditor": {
                             "import": false,
-                            "requiredVersion": "^3.5.3",
+                            "requiredVersion": "^3.6.3",
                             "singleton": true
                         },
                         "@jupyterlab/settingeditor-extension": {
                             "import": false,
-                            "requiredVersion": "^3.5.3"
+                            "requiredVersion": "^3.6.3"
                         },
                         "@jupyterlab/settingregistry": {
                             "import": false,
-                            "requiredVersion": "^3.5.3",
+                            "requiredVersion": "^3.6.3",
                             "singleton": true
                         },
                         "@jupyterlab/shared-models": {
                             "import": false,
-                            "requiredVersion": "^3.5.3",
+                            "requiredVersion": "^3.6.3",
                             "singleton": true
                         },
                         "@jupyterlab/shortcuts-extension": {
                             "import": false,
-                            "requiredVersion": "^3.5.3"
+                            "requiredVersion": "^3.6.3"
                         },
                         "@jupyterlab/statedb": {
                             "import": false,
-                            "requiredVersion": "^3.5.3",
+                            "requiredVersion": "^3.6.3",
                             "singleton": true
                         },
                         "@jupyterlab/statusbar": {
                             "import": false,
-                            "requiredVersion": "^3.5.3",
+                            "requiredVersion": "^3.6.3",
                             "singleton": true
                         },
                         "@jupyterlab/statusbar-extension": {
                             "import": false,
-                            "requiredVersion": "^3.5.3"
+                            "requiredVersion": "^3.6.3"
                         },
                         "@jupyterlab/terminal": {
                             "import": false,
-                            "requiredVersion": "^3.5.3",
+                            "requiredVersion": "^3.6.3",
                             "singleton": true
                         },
                         "@jupyterlab/terminal-extension": {
                             "import": false,
-                            "requiredVersion": "^3.5.3"
+                            "requiredVersion": "^3.6.3"
                         },
                         "@jupyterlab/theme-dark-extension": {
                             "import": false,
-                            "requiredVersion": "^3.5.3"
+                            "requiredVersion": "^3.6.3"
                         },
                         "@jupyterlab/theme-light-extension": {
                             "import": false,
-                            "requiredVersion": "^3.5.3"
+                            "requiredVersion": "^3.6.3"
                         },
                         "@jupyterlab/toc": {
                             "import": false,
-                            "requiredVersion": "^5.5.3",
+                            "requiredVersion": "^5.6.3",
                             "singleton": true
                         },
                         "@jupyterlab/toc-extension": {
                             "import": false,
-                            "requiredVersion": "^5.5.3"
+                            "requiredVersion": "^5.6.3"
                         },
                         "@jupyterlab/tooltip": {
                             "import": false,
-                            "requiredVersion": "^3.5.3",
+                            "requiredVersion": "^3.6.3",
                             "singleton": true
                         },
                         "@jupyterlab/tooltip-extension": {
                             "import": false,
-                            "requiredVersion": "^3.5.3"
+                            "requiredVersion": "^3.6.3"
                         },
                         "@jupyterlab/translation": {
                             "import": false,
-                            "requiredVersion": "^3.5.3",
+                            "requiredVersion": "^3.6.3",
                             "singleton": true
                         },
                         "@jupyterlab/translation-extension": {
                             "import": false,
-                            "requiredVersion": "^3.5.3"
+                            "requiredVersion": "^3.6.3"
                         },
                         "@jupyterlab/ui-components": {
                             "import": false,
-                            "requiredVersion": "^3.5.3",
+                            "requiredVersion": "^3.6.3",
                             "singleton": true
                         },
                         "@jupyterlab/ui-components-extension": {
                             "import": false,
-                            "requiredVersion": "^3.5.3"
+                            "requiredVersion": "^3.6.3"
                         },
                         "@jupyterlab/vdom": {
                             "import": false,
-                            "requiredVersion": "^3.5.3"
+                            "requiredVersion": "^3.6.3"
                         },
                         "@jupyterlab/vdom-extension": {
                             "import": false,
-                            "requiredVersion": "^3.5.3"
+                            "requiredVersion": "^3.6.3"
                         },
                         "@jupyterlab/vega5-extension": {
                             "import": false,
-                            "requiredVersion": "^3.5.3"
+                            "requiredVersion": "^3.6.3"
                         },
                         "@krassowski/jupyterlab-lsp": {
                             "import": false,
                             "singleton": true
                         },
                         "@lumino/algorithm": {
                             "import": false,
                             "requiredVersion": "^1.9.0",
                             "singleton": true
                         },
                         "@lumino/application": {
                             "import": false,
-                            "requiredVersion": "^1.27.0",
+                            "requiredVersion": "^1.31.4",
                             "singleton": true
                         },
                         "@lumino/commands": {
                             "import": false,
                             "requiredVersion": "^1.19.0",
                             "singleton": true
                         },
@@ -579,22 +593,22 @@
                         "@lumino/virtualdom": {
                             "import": false,
                             "requiredVersion": "^1.14.0",
                             "singleton": true
                         },
                         "@lumino/widgets": {
                             "import": false,
-                            "requiredVersion": "^1.33.0",
+                            "requiredVersion": "^1.37.2",
                             "singleton": true
                         },
                         "@types/codemirror": {},
                         "fugue-jupyter": {
                             "import": "/home/runner/work/fugue-jupyter/fugue-jupyter/lib/index.js",
                             "singleton": true,
-                            "version": "0.2.2"
+                            "version": "0.2.3"
                         },
                         "json-schema": {},
                         "lsp-ws-connection": {},
                         "npm-run-all": {},
                         "react": {
                             "import": false,
                             "requiredVersion": "^17.0.1",
```

### Comparing `fugue_jupyter-0.2.2/fugue_jupyter/labextension/package.json` & `fugue_jupyter-0.2.3/fugue_jupyter/labextension/package.json`

 * *Files 5% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9768939393939394%*

 * *Differences: {"'jupyterlab'": "{'_build': {'load': 'static/remoteEntry.99193cc822ff3f92fd07.js'}}",*

 * * "'version'": "'0.2.3'"}*

```diff
@@ -62,15 +62,15 @@
                 "jlpm clean:all"
             ]
         }
     },
     "jupyterlab": {
         "_build": {
             "extension": "./extension",
-            "load": "static/remoteEntry.8a36f4b5ce59a9dca3d8.js",
+            "load": "static/remoteEntry.99193cc822ff3f92fd07.js",
             "style": "./style"
         },
         "extension": true,
         "outputDir": "fugue_jupyter/labextension",
         "schemaDir": "schema",
         "sharedPackages": {
             "@krassowski/jupyterlab-lsp": {
@@ -117,9 +117,9 @@
     "sideEffects": [
         "style/*.css",
         "style/index.js"
     ],
     "style": "style/index.css",
     "styleModule": "style/index.js",
     "types": "lib/index.d.ts",
-    "version": "0.2.2"
+    "version": "0.2.3"
 }
```

### Comparing `fugue_jupyter-0.2.2/fugue_jupyter/labextension/schemas/fugue-jupyter/package.json.orig` & `fugue_jupyter-0.2.3/fugue_jupyter/labextension/schemas/fugue-jupyter/package.json.orig`

 * *Files 0% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9772727272727273%*

 * *Differences: {"'version'": "'0.2.3'"}*

```diff
@@ -112,9 +112,9 @@
     "sideEffects": [
         "style/*.css",
         "style/index.js"
     ],
     "style": "style/index.css",
     "styleModule": "style/index.js",
     "types": "lib/index.d.ts",
-    "version": "0.2.2"
+    "version": "0.2.3"
 }
```

### Comparing `fugue_jupyter-0.2.2/fugue_jupyter/labextension/static/lib_index_js.ad9a1c1d1f8d504aeb4b.js` & `fugue_jupyter-0.2.3/fugue_jupyter/labextension/static/lib_index_js.1b56285a6b63fec28143.js`

 * *Files 1% similar despite different names*

#### js-beautify {}

```diff
@@ -254,15 +254,15 @@
                     const obj = {},
                         words = str.split(' ');
                     for (let i = 0; i < words.length; ++i) {
                         obj[words[i]] = true;
                     }
                     return obj;
                 }
-                const fugue_keywords = 'system bernoulli reservoir approx fill hash rand even presort persist broadcast params process output outtransform rowcount concurrency prepartition zip print title save append parquet csv json single checkpoint weak strong deterministic yield connect sample seed take sub callback dataframe file';
+                const fugue_keywords = 'system bernoulli reservoir approx fill hash rand even coarse presort persist broadcast params process output outtransform rowcount concurrency prepartition zip print title save append parquet csv json single checkpoint weak strong deterministic yield connect sample seed take sub callback dataframe file';
                 /**
                  * Register text editor based on file type.
                  * @param c
                  * @param language
                  */
                 function registerCodeMirrorFor(c, language) {
                     c.CodeMirror.defineMode(language, (config, modeOptions) => {
@@ -289,8 +289,8 @@
 
 
                 /***/
             })
 
     }
 ]);
-//# sourceMappingURL=lib_index_js.ad9a1c1d1f8d504aeb4b.js.map
+//# sourceMappingURL=lib_index_js.1b56285a6b63fec28143.js.map
```

### Comparing `fugue_jupyter-0.2.2/fugue_jupyter/labextension/static/lib_index_js.ad9a1c1d1f8d504aeb4b.js.map` & `fugue_jupyter-0.2.3/fugue_jupyter/labextension/static/lib_index_js.1b56285a6b63fec28143.js.map`

 * *Files 1% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.880952380952381%*

 * *Differences: {"'file'": "'lib_index_js.1b56285a6b63fec28143.js'",*

 * * "'sourcesContent'": "{insert: [(1, 'import { RegExpForeignCodeExtractor } from "*

 * *                     "\\'@krassowski/jupyterlab-lsp\\';\\nfunction cell_magic(language) {\\n    "*

 * *                     'return `%%${language}.*`;\\n}\\nfunction start(language) {\\n    return '*

 * *                     '`--start-${language}`;\\n}\\nfunction end(language) {\\n    return '*

 * *                     '`--end-${language}`;\\n}\\nfunction fsql_start() {\\n    return '*

 * *     […]*

```diff
@@ -1,15 +1,15 @@
 {
-    "file": "lib_index_js.ad9a1c1d1f8d504aeb4b.js",
+    "file": "lib_index_js.1b56285a6b63fec28143.js",
     "mappings": ";;;;;;;;;;;;;;;;;;;;;;;;AAA+D;AACQ;AAClB;AACG;AACA;AACwE;AAChI;AACA;AACA;AACA;AACA;AACA;AACA;AACA;AACA;AACA;AACA;AACA;AACA;AACA;AACA;AACA;AACA;AACA,IAAI,6DAAqB;AACzB;AACA;AACA;AACA;AACA;AACA;AACA;AACA;AACA;AACA;AACA;AACA;AACA;AACA;AACA;AACA;AACA,iCAAiC,6DAAqB;AACtD;AACA;AACA;AACA;AACA;AACA;AACA;AACA;AACA;AACA;AACA;AACA;AACA;AACA;AACA;AACA;AACA,QAAQ,+DAAW;AACnB,QAAQ,iFAAyB;AACjC,QAAQ,yEAAgB;AACxB,QAAQ,kEAAc;AACtB,QAAQ,kEAAgB;AACxB;AACA;AACA;AACA;AACA;AACA;AACA;AACA;AACA;AACA;AACA;AACA,SAAS;AACT;AACA;AACA;AACA;AACA;AACA;AACA;AACA;AACA;AACA,WAAW;AACX;AACA;AACA,kEAAkE,OAAO;AACzE;AACA,WAAW,EAAE;AACb;AACA;AACA;AACA;AACA;AACA;AACA;AACA;AACA,kCAAkC,uDAAe;AACjD,kCAAkC,0DAAkB;AACpD,kCAAkC,0DAAkB;AACpD;AACA;AACA;AACA,iEAAe,MAAM,EAAC;;;;;;;;;;;;;;;;;;;;;ACvGkD;AACxE;AACA,gBAAgB,SAAS;AACzB;AACA;AACA,sBAAsB,SAAS;AAC/B;AACA;AACA,oBAAoB,SAAS;AAC7B;AACA;AACA;AACA;AACA;AACA;AACA;AACA;AACO;AACP;AACA;AACA,qBAAqB,gBAAgB;AACrC,sBAAsB,cAAc;AACpC;AACA;AACA;AACA;AACA;AACA,SAAS;AACT;AACA,4BAA4B,aAAa;AACzC,6BAA6B,WAAW;AACxC;AACA;AACA,SAAS;AACT;AACA,4BAA4B,qBAAqB;AACjD;AACA;AACA;AACA;AACA;AACA;AACO;AACP,eAAe,kFAA0B;AACzC;AACA,oBAAoB,MAAM,EAAE,qBAAqB;AACjD;AACA;AACA;AACA,KAAK;AACL;AACO;AACP,eAAe,kFAA0B;AACzC;AACA,oBAAoB,gBAAgB,cAAc,cAAc;AAChE;AACA;AACA;AACA,KAAK;AACL;AACO;AACP,eAAe,kFAA0B;AACzC;AACA,oBAAoB,aAAa,cAAc,WAAW;AAC1D;AACA;AACA;AACA,KAAK;AACL;AACA;AACA,kBAAkB;AAClB,oBAAoB,kBAAkB;AACtC;AACA;AACA;AACA;AACA;AACA;AACA;AACA;AACA;AACA;AACO;AACP;AACA;AACA;AACA;AACA;AACA;AACA;AACA;AACA;AACA;AACA,SAAS;AACT;AACA,KAAK;AACL,sCAAsC,SAAS;AAC/C;AACA;AACA,wBAAwB,SAAS;AACjC;AACA;AACA,KAAK;AACL",
     "names": [],
     "sourceRoot": "",
     "sources": [
         "webpack://fugue-jupyter/./lib/index.js",
         "webpack://fugue-jupyter/./lib/utils.js"
     ],
     "sourcesContent": [
         "import { ISettingRegistry } from '@jupyterlab/settingregistry';\nimport { ILSPCodeExtractorsManager } from '@krassowski/jupyterlab-lsp';\nimport { ICodeMirror } from '@jupyterlab/codemirror';\nimport { INotebookTracker } from '@jupyterlab/notebook';\nimport { IEditorTracker } from '@jupyterlab/fileeditor';\nimport { cellMagicExtractor, markerExtractor, fsqlBlockExtractor, sqlCodeMirrorModesFor, registerCodeMirrorFor } from './utils';\n/*\nResults in\nLINE_MAGIC_EXTRACT\n(?:^|\\n)%sparksql(?: |-c|--cache|-e|--eager|-[a-z] [0-9a-zA-Z/._]+|--[a-zA-Z]+ [0-9a-zA-Z/._]+)*([^\\n]*)\nCELL_MAGIC_EXTRACT\n(?:^|\\n)%%sparksql(?: |-c|--cache|-e|--eager|-[a-z] [0-9a-zA-Z/._]+|--[a-zA-Z]+ [0-9a-zA-Z/._]+)*\\n([^]*)\n*/\n/**\n * Code taken from https://github.com/jupyterlab/jupyterlab/blob/master/packages/codemirror/src/codemirror-ipython.ts\n * Modified to support embedded sql syntax\n */\nfunction codeMirrorWithSqlSyntaxHighlightSupport(c) {\n    /**\n     * Define an IPython codemirror mode.\n     *\n     * It is a slightly altered Python Mode with a `?` operator.\n     */\n    registerCodeMirrorFor(c, 'fsql');\n    c.CodeMirror.defineMode('ipython', (config, modeOptions) => {\n        const pythonConf = {};\n        for (const prop in modeOptions) {\n            if (modeOptions.hasOwnProperty(prop)) {\n                pythonConf[prop] = modeOptions[prop];\n            }\n        }\n        pythonConf.name = 'python';\n        pythonConf.singleOperators = new RegExp('^[\\\\+\\\\-\\\\*/%&|@\\\\^~<>!\\\\?]');\n        pythonConf.identifiers = new RegExp('^[_A-Za-z\\u00A1-\\uFFFF][_A-Za-z0-9\\u00A1-\\uFFFF]*');\n        //return c.CodeMirror.getMode(config, pythonConf);\n        // Instead of returning this mode we multiplex it with SQL\n        const pythonMode = c.CodeMirror.getMode(config, pythonConf);\n        // get a mode for SQL\n        const sqlMode = c.CodeMirror.getMode(config, 'fsql');\n        // multiplex python with SQL and return it\n        const multiplexedModes = sqlCodeMirrorModesFor('fsql', sqlMode);\n        return c.CodeMirror.multiplexingMode(pythonMode, ...multiplexedModes);\n    }\n    // Original code has a third argument. Not sure why we don't..\n    // https://github.com/jupyterlab/jupyterlab/blob/master/packages/codemirror/src/codemirror-ipython.ts\n    // ,\n    // 'python'\n    );\n}\n/**\n * Initialization data for the jupyterlab_jc extension.\n */\nconst plugin = {\n    id: 'fugue-jupyter:plugin',\n    autoStart: true,\n    optional: [],\n    requires: [\n        ICodeMirror,\n        ILSPCodeExtractorsManager,\n        ISettingRegistry,\n        IEditorTracker,\n        INotebookTracker\n    ],\n    activate: (app, codeMirror, lspExtractorsMgr, settingRegistry, editorTracker, tracker) => {\n        /**\n         * Load the settings for this extension\n         *\n         * @param setting Extension settings\n         */\n        /*function loadSetting(settings: ISettingRegistry.ISettings): void {\n          // Read the settings and convert to the correct type\n          const formatIndent = settings.get('formatIndent').composite as string;\n          const formatUppercase = settings.get('formatUppercase').composite as boolean;\n        }*/\n        // Wait for the application to be restored and\n        // for the settings for this plugin to be loaded\n        /*Promise.all([app.restored, settingRegistry.load(Constants.SETTINGS_SECTION)])\n          .then(([, settings]) => {\n            // Read the settings\n            loadSetting(settings);\n            // Listen for your plugin setting changes using Signal\n            settings.changed.connect(loadSetting);\n    \n          })\n          .catch((reason) => {\n            console.error(\n              `Something went wrong when reading the settings.\\n${reason}`\n            );\n          });*/\n        // JupyterLab uses the CodeMirror library to syntax highlight code\n        // within the cells. Register a multiplex CodeMirror capable of\n        // highlightin SQL which is embedded in a IPython magic or within\n        // a python string (delimited by markers)\n        codeMirrorWithSqlSyntaxHighlightSupport(codeMirror);\n        // JupyterLab-LSP relies on extractors to pull the SQL out of the cell\n        // and into a virtual document which is then passed to the sql-language-server\n        // for code completion evaluation\n        lspExtractorsMgr.register(markerExtractor('fsql'), 'python');\n        lspExtractorsMgr.register(fsqlBlockExtractor('fsql'), 'python');\n        lspExtractorsMgr.register(cellMagicExtractor('fsql'), 'python');\n        console.log('fugue-jupyter LSP extractors registered');\n    }\n};\nexport default plugin;\n",
-        "import { RegExpForeignCodeExtractor } from '@krassowski/jupyterlab-lsp';\nfunction cell_magic(language) {\n    return `%%${language}.*`;\n}\nfunction start(language) {\n    return `--start-${language}`;\n}\nfunction end(language) {\n    return `--end-${language}`;\n}\nfunction fsql_start() {\n    return `(fsql|fugue_sql|fugue_sql_flow)[\\\\s\\\\S]*\\\\([\\\\s\\\\S]*\\\\\"\\\\\"\\\\\"`;\n}\nfunction fsql_end() {\n    return `\\\\\"\\\\\"\\\\\"`;\n}\nconst BEGIN = '(?:^|\\n)';\nexport function sqlCodeMirrorModesFor(language, sqlMode) {\n    return [\n        {\n            open: `${start(language)}`,\n            close: `${end(language)}`,\n            // parseDelimiters is set to true which considers\n            // the marker as part of the SQL statement\n            // it is thus syntax highlighted as a comment\n            parseDelimiters: true,\n            mode: sqlMode\n        },\n        {\n            open: RegExp(`${fsql_start()}`),\n            close: RegExp(`${fsql_end()}`),\n            parseDelimiters: false,\n            mode: sqlMode\n        },\n        {\n            open: RegExp(`${cell_magic(language)}`),\n            close: '__A MARKER THAT WILL NEVER BE MATCHED__',\n            parseDelimiters: false,\n            mode: sqlMode\n        }\n    ];\n}\nexport function cellMagicExtractor(language) {\n    return new RegExpForeignCodeExtractor({\n        language: language,\n        pattern: `${BEGIN}${cell_magic(language)}\\n([^]*)`,\n        foreign_capture_groups: [1],\n        is_standalone: true,\n        file_extension: language\n    });\n}\nexport function markerExtractor(language) {\n    return new RegExpForeignCodeExtractor({\n        language: language,\n        pattern: `${start(language)}.*?\\n([^]*?)${end(language)}`,\n        foreign_capture_groups: [1],\n        is_standalone: true,\n        file_extension: language\n    });\n}\nexport function fsqlBlockExtractor(language) {\n    return new RegExpForeignCodeExtractor({\n        language: language,\n        pattern: `${fsql_start()}.*?\\n([^]*?)${fsql_end()}`,\n        foreign_capture_groups: [1],\n        is_standalone: true,\n        file_extension: language\n    });\n}\nfunction set(str) {\n    const obj = {}, words = str.split(' ');\n    for (let i = 0; i < words.length; ++i) {\n        obj[words[i]] = true;\n    }\n    return obj;\n}\nconst fugue_keywords = 'system bernoulli reservoir approx fill hash rand even presort persist broadcast params process output outtransform rowcount concurrency prepartition zip print title save append parquet csv json single checkpoint weak strong deterministic yield connect sample seed take sub callback dataframe file';\n/**\n * Register text editor based on file type.\n * @param c\n * @param language\n */\nexport function registerCodeMirrorFor(c, language) {\n    c.CodeMirror.defineMode(language, (config, modeOptions) => {\n        const mode = c.CodeMirror.getMode(config, {\n            name: 'sql',\n            keywords: set(fugue_keywords +\n                ' add after all alter analyze and anti archive array as asc at between bucket buckets by cache cascade case cast change clear cluster clustered codegen collection column columns comment commit compact compactions compute concatenate cost create cross cube current current_date current_timestamp database databases data dbproperties defined delete delimited deny desc describe dfs directories distinct distribute drop else end escaped except exchange exists explain export extended external false fields fileformat first following for format formatted from full function functions global grant group grouping having if ignore import in index indexes inner inpath inputformat insert intersect interval into is items join keys last lateral lazy left like limit lines list load local location lock locks logical macro map minus msck natural no not null nulls of on optimize option options or order out outer outputformat over overwrite partition partitioned partitions percent preceding principals purge range recordreader recordwriter recover reduce refresh regexp rename repair replace reset restrict revoke right rlike role roles rollback rollup row rows schema schemas select semi separated serde serdeproperties set sets show skewed sort sorted start statistics stored stratify struct table tables tablesample tblproperties temp temporary terminated then to touch transaction transactions transform true truncate unarchive unbounded uncache union unlock unset use using values view when where window with'),\n            builtin: set('date datetime tinyint smallint int bigint boolean float double string binary timestamp decimal array map struct uniontype delimited serde sequencefile textfile rcfile inputformat outputformat'),\n            atoms: set('false true null'),\n            operatorChars: /^[*\\/+\\-%<>!=~&|^]/,\n            dateSQL: set('time'),\n            support: set('ODBCdotTable doubleQuote zerolessFloat')\n        });\n        return mode;\n    });\n    c.CodeMirror.defineMIME(`text/x-${language}`, language);\n    c.CodeMirror.modeInfo.push({\n        ext: [language],\n        mime: `text/x-${language}`,\n        mode: language,\n        name: language\n    });\n}\n"
+        "import { RegExpForeignCodeExtractor } from '@krassowski/jupyterlab-lsp';\nfunction cell_magic(language) {\n    return `%%${language}.*`;\n}\nfunction start(language) {\n    return `--start-${language}`;\n}\nfunction end(language) {\n    return `--end-${language}`;\n}\nfunction fsql_start() {\n    return `(fsql|fugue_sql|fugue_sql_flow)[\\\\s\\\\S]*\\\\([\\\\s\\\\S]*\\\\\"\\\\\"\\\\\"`;\n}\nfunction fsql_end() {\n    return `\\\\\"\\\\\"\\\\\"`;\n}\nconst BEGIN = '(?:^|\\n)';\nexport function sqlCodeMirrorModesFor(language, sqlMode) {\n    return [\n        {\n            open: `${start(language)}`,\n            close: `${end(language)}`,\n            // parseDelimiters is set to true which considers\n            // the marker as part of the SQL statement\n            // it is thus syntax highlighted as a comment\n            parseDelimiters: true,\n            mode: sqlMode\n        },\n        {\n            open: RegExp(`${fsql_start()}`),\n            close: RegExp(`${fsql_end()}`),\n            parseDelimiters: false,\n            mode: sqlMode\n        },\n        {\n            open: RegExp(`${cell_magic(language)}`),\n            close: '__A MARKER THAT WILL NEVER BE MATCHED__',\n            parseDelimiters: false,\n            mode: sqlMode\n        }\n    ];\n}\nexport function cellMagicExtractor(language) {\n    return new RegExpForeignCodeExtractor({\n        language: language,\n        pattern: `${BEGIN}${cell_magic(language)}\\n([^]*)`,\n        foreign_capture_groups: [1],\n        is_standalone: true,\n        file_extension: language\n    });\n}\nexport function markerExtractor(language) {\n    return new RegExpForeignCodeExtractor({\n        language: language,\n        pattern: `${start(language)}.*?\\n([^]*?)${end(language)}`,\n        foreign_capture_groups: [1],\n        is_standalone: true,\n        file_extension: language\n    });\n}\nexport function fsqlBlockExtractor(language) {\n    return new RegExpForeignCodeExtractor({\n        language: language,\n        pattern: `${fsql_start()}.*?\\n([^]*?)${fsql_end()}`,\n        foreign_capture_groups: [1],\n        is_standalone: true,\n        file_extension: language\n    });\n}\nfunction set(str) {\n    const obj = {}, words = str.split(' ');\n    for (let i = 0; i < words.length; ++i) {\n        obj[words[i]] = true;\n    }\n    return obj;\n}\nconst fugue_keywords = 'system bernoulli reservoir approx fill hash rand even coarse presort persist broadcast params process output outtransform rowcount concurrency prepartition zip print title save append parquet csv json single checkpoint weak strong deterministic yield connect sample seed take sub callback dataframe file';\n/**\n * Register text editor based on file type.\n * @param c\n * @param language\n */\nexport function registerCodeMirrorFor(c, language) {\n    c.CodeMirror.defineMode(language, (config, modeOptions) => {\n        const mode = c.CodeMirror.getMode(config, {\n            name: 'sql',\n            keywords: set(fugue_keywords +\n                ' add after all alter analyze and anti archive array as asc at between bucket buckets by cache cascade case cast change clear cluster clustered codegen collection column columns comment commit compact compactions compute concatenate cost create cross cube current current_date current_timestamp database databases data dbproperties defined delete delimited deny desc describe dfs directories distinct distribute drop else end escaped except exchange exists explain export extended external false fields fileformat first following for format formatted from full function functions global grant group grouping having if ignore import in index indexes inner inpath inputformat insert intersect interval into is items join keys last lateral lazy left like limit lines list load local location lock locks logical macro map minus msck natural no not null nulls of on optimize option options or order out outer outputformat over overwrite partition partitioned partitions percent preceding principals purge range recordreader recordwriter recover reduce refresh regexp rename repair replace reset restrict revoke right rlike role roles rollback rollup row rows schema schemas select semi separated serde serdeproperties set sets show skewed sort sorted start statistics stored stratify struct table tables tablesample tblproperties temp temporary terminated then to touch transaction transactions transform true truncate unarchive unbounded uncache union unlock unset use using values view when where window with'),\n            builtin: set('date datetime tinyint smallint int bigint boolean float double string binary timestamp decimal array map struct uniontype delimited serde sequencefile textfile rcfile inputformat outputformat'),\n            atoms: set('false true null'),\n            operatorChars: /^[*\\/+\\-%<>!=~&|^]/,\n            dateSQL: set('time'),\n            support: set('ODBCdotTable doubleQuote zerolessFloat')\n        });\n        return mode;\n    });\n    c.CodeMirror.defineMIME(`text/x-${language}`, language);\n    c.CodeMirror.modeInfo.push({\n        ext: [language],\n        mime: `text/x-${language}`,\n        mode: language,\n        name: language\n    });\n}\n"
     ],
     "version": 3
 }
```

### Comparing `fugue_jupyter-0.2.2/fugue_jupyter/labextension/static/remoteEntry.8a36f4b5ce59a9dca3d8.js` & `fugue_jupyter-0.2.3/fugue_jupyter/labextension/static/remoteEntry.99193cc822ff3f92fd07.js`

 * *Files 1% similar despite different names*

#### js-beautify {}

```diff
@@ -182,15 +182,15 @@
     (() => {
         /******/ // This function allow to reference async chunks
         /******/
         __webpack_require__.u = (chunkId) => {
             /******/ // return url for filenames based on template
             /******/
             return "" + chunkId + "." + {
-                "lib_index_js": "ad9a1c1d1f8d504aeb4b",
+                "lib_index_js": "1b56285a6b63fec28143",
                 "vendors-node_modules_css-loader_dist_runtime_api_js-node_modules_css-loader_dist_runtime_cssW-72eba1": "c07606ee12302cc69c16",
                 "style_index_js": "308b73f665deca4ee2f3"
             } [chunkId] + ".js";
             /******/
         };
         /******/
     })();
@@ -425,15 +425,15 @@
             /******/
             var promises = [];
             /******/
             switch (name) {
                 /******/
                 case "default": {
                     /******/
-                    register("fugue-jupyter", "0.2.2", () => (__webpack_require__.e("lib_index_js").then(() => (() => (__webpack_require__( /*! ./lib/index.js */ "./lib/index.js"))))));
+                    register("fugue-jupyter", "0.2.3", () => (__webpack_require__.e("lib_index_js").then(() => (() => (__webpack_require__( /*! ./lib/index.js */ "./lib/index.js"))))));
                     /******/
                 }
                 /******/
                 break;
                 /******/
             }
             /******/
@@ -814,23 +814,23 @@
             /******/
         });
         /******/
         var installedModules = {};
         /******/
         var moduleToHandlerMapping = {
             /******/
-            "webpack/sharing/consume/default/@jupyterlab/settingregistry": () => (loadSingletonVersionCheck("default", "@jupyterlab/settingregistry", [1, 3, 5, 3])),
+            "webpack/sharing/consume/default/@jupyterlab/settingregistry": () => (loadSingletonVersionCheck("default", "@jupyterlab/settingregistry", [1, 3, 6, 3])),
             /******/
             "webpack/sharing/consume/default/@krassowski/jupyterlab-lsp": () => (loadSingletonVersionCheck("default", "@krassowski/jupyterlab-lsp", [1, 3, 10, 1])),
             /******/
-            "webpack/sharing/consume/default/@jupyterlab/codemirror": () => (loadSingletonVersionCheck("default", "@jupyterlab/codemirror", [1, 3, 5, 3])),
+            "webpack/sharing/consume/default/@jupyterlab/codemirror": () => (loadSingletonVersionCheck("default", "@jupyterlab/codemirror", [1, 3, 6, 3])),
             /******/
-            "webpack/sharing/consume/default/@jupyterlab/notebook": () => (loadSingletonVersionCheck("default", "@jupyterlab/notebook", [1, 3, 5, 3])),
+            "webpack/sharing/consume/default/@jupyterlab/notebook": () => (loadSingletonVersionCheck("default", "@jupyterlab/notebook", [1, 3, 6, 3])),
             /******/
-            "webpack/sharing/consume/default/@jupyterlab/fileeditor": () => (loadSingletonVersionCheck("default", "@jupyterlab/fileeditor", [1, 3, 5, 3]))
+            "webpack/sharing/consume/default/@jupyterlab/fileeditor": () => (loadSingletonVersionCheck("default", "@jupyterlab/fileeditor", [1, 3, 6, 3]))
             /******/
         };
         /******/ // no consumes in initial chunks
         /******/
         var chunkMapping = {
             /******/
             "lib_index_js": [
@@ -1074,8 +1074,8 @@
     /******/
     var __webpack_exports__ = __webpack_require__("webpack/container/entry/fugue-jupyter");
     /******/
     (_JUPYTERLAB = typeof _JUPYTERLAB === "undefined" ? {} : _JUPYTERLAB)["fugue-jupyter"] = __webpack_exports__;
     /******/
     /******/
 })();
-//# sourceMappingURL=remoteEntry.8a36f4b5ce59a9dca3d8.js.map
+//# sourceMappingURL=remoteEntry.99193cc822ff3f92fd07.js.map
```

### Comparing `fugue_jupyter-0.2.2/fugue_jupyter/labextension/static/remoteEntry.8a36f4b5ce59a9dca3d8.js.map` & `fugue_jupyter-0.2.3/fugue_jupyter/labextension/static/remoteEntry.99193cc822ff3f92fd07.js.map`

 * *Files 0% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9081632653061226%*

 * *Differences: {"'file'": "'remoteEntry.99193cc822ff3f92fd07.js'",*

 * * "'sourcesContent'": "{insert: [(5, '// This function allow to reference async "*

 * *                     'chunks\\n__webpack_require__.u = (chunkId) => {\\n\\t// return url for '*

 * *                     'filenames based on template\\n\\treturn "" + chunkId + "." + '*

 * *                     '{"lib_index_js":"1b56285a6b63fec28143","vendors-node_modules_css-loader_dist_runtime_api_js-node_modules_css-loader_dist_runtime_cssW-72eba1":"c07606ee12302cc69c16","style_index […]*

```diff
@@ -1,9 +1,9 @@
 {
-    "file": "remoteEntry.8a36f4b5ce59a9dca3d8.js",
+    "file": "remoteEntry.99193cc822ff3f92fd07.js",
     "mappings": ";;;;;;;;;;;AAAA;AACA;AACA;AACA,EAAE;AACF;AACA;AACA,EAAE;AACF;AACA;AACA;AACA;AACA;AACA;AACA;AACA;AACA;AACA;AACA;AACA,IAAI;AACJ;AACA;AACA;AACA;AACA;AACA;AACA;AACA;AACA;AACA;AACA;AACA;;AAEA;AACA;AACA;AACA;AACA,CAAC;;;;;;UCpCD;UACA;;UAEA;UACA;UACA;UACA;UACA;UACA;UACA;UACA;UACA;UACA;UACA;UACA;UACA;;UAEA;UACA;;UAEA;UACA;UACA;;UAEA;UACA;;UAEA;UACA;;;;;WC5BA;WACA;WACA;WACA;WACA;WACA,iCAAiC,WAAW;WAC5C;WACA;;;;;WCPA;WACA;WACA;WACA;WACA,yCAAyC,wCAAwC;WACjF;WACA;WACA;;;;;WCPA;WACA;WACA;WACA;WACA;WACA;WACA;WACA,EAAE;WACF;;;;;WCRA;WACA;WACA;WACA,8BAA8B,4MAA4M;WAC1O;;;;;WCJA;WACA;WACA;WACA;WACA,GAAG;WACH;WACA;WACA,CAAC;;;;;WCPD;;;;;WCAA;WACA;WACA;WACA;WACA,uBAAuB,4BAA4B;WACnD;WACA;WACA;WACA,iBAAiB,oBAAoB;WACrC;WACA,mGAAmG,YAAY;WAC/G;WACA;WACA;WACA;WACA;;WAEA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA,mEAAmE,iCAAiC;WACpG;WACA;WACA;WACA;;;;;WCzCA;WACA;WACA;WACA,uDAAuD,iBAAiB;WACxE;WACA,gDAAgD,aAAa;WAC7D;;;;;WCNA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA,oJAAoJ;WACpJ;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA,IAAI,aAAa;WACjB;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;;;;;WC3CA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;;;;;WCfA;WACA;WACA,WAAW,6BAA6B,iBAAiB,GAAG,qEAAqE;WACjI;WACA;WACA;WACA,qCAAqC,aAAa,EAAE,wDAAwD,2BAA2B,4BAA4B,2BAA2B,+CAA+C,mCAAmC;WAChR;WACA;WACA;WACA,qBAAqB,8BAA8B,SAAS,sDAAsD,gBAAgB,eAAe,KAAK,6DAA6D,SAAS,SAAS,QAAQ,eAAe,KAAK,eAAe,qGAAqG,WAAW,aAAa;WAC7Y;WACA;WACA;WACA,gBAAgB,8BAA8B,qBAAqB,YAAY,sBAAsB,SAAS,iDAAiD,6FAA6F,WAAW,uBAAuB,2BAA2B,wBAAwB,KAAK,oCAAoC,oBAAoB,wBAAwB,oBAAoB,SAAS,KAAK,yBAAyB,KAAK,gCAAgC,yBAAyB,QAAQ,eAAe,KAAK,eAAe,4DAA4D;WACtoB;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA,EAAE;WACF;WACA;WACA;WACA;WACA;WACA;WACA,EAAE;WACF;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA,EAAE;WACF;WACA;WACA;WACA;WACA;WACA;WACA;WACA,EAAE;WACF;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA,CAAC;;WAED;WACA;WACA;WACA,CAAC;WACD;WACA;WACA,CAAC;WACD;WACA;WACA;WACA,CAAC;WACD;WACA;WACA;WACA,CAAC;WACD;WACA;WACA;WACA,CAAC;WACD;WACA;WACA;WACA,CAAC;WACD;WACA;WACA;WACA,CAAC;WACD;WACA;WACA;WACA,CAAC;WACD;WACA;WACA;WACA,CAAC;WACD;WACA;WACA;WACA,CAAC;WACD;WACA;WACA;WACA,CAAC;WACD;WACA;WACA;WACA,CAAC;WACD;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA,MAAM;WACN,KAAK,WAAW;WAChB,GAAG;WACH;WACA;;;;;WC/KA;;WAEA;WACA;WACA;WACA;WACA;WACA;;WAEA;WACA;WACA;WACA,iCAAiC;;WAEjC;WACA;WACA;WACA,KAAK;WACL,eAAe;WACf;WACA;WACA;;WAEA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA,MAAM;WACN;WACA;WACA;;WAEA;;WAEA;;WAEA;;WAEA;;WAEA;;WAEA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA;WACA,MAAM,qBAAqB;WAC3B;WACA;WACA;WACA;WACA;WACA;;WAEA;;WAEA;WACA;WACA;;;;;WCrFA;;;;;UEAA;UACA;UACA;UACA",
     "names": [],
     "sourceRoot": "",
     "sources": [
         "webpack://fugue-jupyter/webpack/container-entry",
         "webpack://fugue-jupyter/webpack/bootstrap",
         "webpack://fugue-jupyter/webpack/runtime/compat get default export",
@@ -25,22 +25,22 @@
     ],
     "sourcesContent": [
         "var moduleMap = {\n\t\"./index\": () => {\n\t\treturn __webpack_require__.e(\"lib_index_js\").then(() => (() => ((__webpack_require__(/*! ./lib/index.js */ \"./lib/index.js\")))));\n\t},\n\t\"./extension\": () => {\n\t\treturn __webpack_require__.e(\"lib_index_js\").then(() => (() => ((__webpack_require__(/*! ./lib/index.js */ \"./lib/index.js\")))));\n\t},\n\t\"./style\": () => {\n\t\treturn Promise.all([__webpack_require__.e(\"vendors-node_modules_css-loader_dist_runtime_api_js-node_modules_css-loader_dist_runtime_cssW-72eba1\"), __webpack_require__.e(\"style_index_js\")]).then(() => (() => ((__webpack_require__(/*! ./style/index.js */ \"./style/index.js\")))));\n\t}\n};\nvar get = (module, getScope) => {\n\t__webpack_require__.R = getScope;\n\tgetScope = (\n\t\t__webpack_require__.o(moduleMap, module)\n\t\t\t? moduleMap[module]()\n\t\t\t: Promise.resolve().then(() => {\n\t\t\t\tthrow new Error('Module \"' + module + '\" does not exist in container.');\n\t\t\t})\n\t);\n\t__webpack_require__.R = undefined;\n\treturn getScope;\n};\nvar init = (shareScope, initScope) => {\n\tif (!__webpack_require__.S) return;\n\tvar name = \"default\"\n\tvar oldScope = __webpack_require__.S[name];\n\tif(oldScope && oldScope !== shareScope) throw new Error(\"Container initialization failed as it has already been initialized with a different share scope\");\n\t__webpack_require__.S[name] = shareScope;\n\treturn __webpack_require__.I(name, initScope);\n};\n\n// This exports getters to disallow modifications\n__webpack_require__.d(exports, {\n\tget: () => (get),\n\tinit: () => (init)\n});",
         "// The module cache\nvar __webpack_module_cache__ = {};\n\n// The require function\nfunction __webpack_require__(moduleId) {\n\t// Check if module is in cache\n\tvar cachedModule = __webpack_module_cache__[moduleId];\n\tif (cachedModule !== undefined) {\n\t\treturn cachedModule.exports;\n\t}\n\t// Create a new module (and put it into the cache)\n\tvar module = __webpack_module_cache__[moduleId] = {\n\t\tid: moduleId,\n\t\t// no module.loaded needed\n\t\texports: {}\n\t};\n\n\t// Execute the module function\n\t__webpack_modules__[moduleId](module, module.exports, __webpack_require__);\n\n\t// Return the exports of the module\n\treturn module.exports;\n}\n\n// expose the modules object (__webpack_modules__)\n__webpack_require__.m = __webpack_modules__;\n\n// expose the module cache\n__webpack_require__.c = __webpack_module_cache__;\n\n",
         "// getDefaultExport function for compatibility with non-harmony modules\n__webpack_require__.n = (module) => {\n\tvar getter = module && module.__esModule ?\n\t\t() => (module['default']) :\n\t\t() => (module);\n\t__webpack_require__.d(getter, { a: getter });\n\treturn getter;\n};",
         "// define getter functions for harmony exports\n__webpack_require__.d = (exports, definition) => {\n\tfor(var key in definition) {\n\t\tif(__webpack_require__.o(definition, key) && !__webpack_require__.o(exports, key)) {\n\t\t\tObject.defineProperty(exports, key, { enumerable: true, get: definition[key] });\n\t\t}\n\t}\n};",
         "__webpack_require__.f = {};\n// This file contains only the entry chunk.\n// The chunk loading function for additional chunks\n__webpack_require__.e = (chunkId) => {\n\treturn Promise.all(Object.keys(__webpack_require__.f).reduce((promises, key) => {\n\t\t__webpack_require__.f[key](chunkId, promises);\n\t\treturn promises;\n\t}, []));\n};",
-        "// This function allow to reference async chunks\n__webpack_require__.u = (chunkId) => {\n\t// return url for filenames based on template\n\treturn \"\" + chunkId + \".\" + {\"lib_index_js\":\"ad9a1c1d1f8d504aeb4b\",\"vendors-node_modules_css-loader_dist_runtime_api_js-node_modules_css-loader_dist_runtime_cssW-72eba1\":\"c07606ee12302cc69c16\",\"style_index_js\":\"308b73f665deca4ee2f3\"}[chunkId] + \".js\";\n};",
+        "// This function allow to reference async chunks\n__webpack_require__.u = (chunkId) => {\n\t// return url for filenames based on template\n\treturn \"\" + chunkId + \".\" + {\"lib_index_js\":\"1b56285a6b63fec28143\",\"vendors-node_modules_css-loader_dist_runtime_api_js-node_modules_css-loader_dist_runtime_cssW-72eba1\":\"c07606ee12302cc69c16\",\"style_index_js\":\"308b73f665deca4ee2f3\"}[chunkId] + \".js\";\n};",
         "__webpack_require__.g = (function() {\n\tif (typeof globalThis === 'object') return globalThis;\n\ttry {\n\t\treturn this || new Function('return this')();\n\t} catch (e) {\n\t\tif (typeof window === 'object') return window;\n\t}\n})();",
         "__webpack_require__.o = (obj, prop) => (Object.prototype.hasOwnProperty.call(obj, prop))",
         "var inProgress = {};\nvar dataWebpackPrefix = \"fugue-jupyter:\";\n// loadScript function to load a script via script tag\n__webpack_require__.l = (url, done, key, chunkId) => {\n\tif(inProgress[url]) { inProgress[url].push(done); return; }\n\tvar script, needAttach;\n\tif(key !== undefined) {\n\t\tvar scripts = document.getElementsByTagName(\"script\");\n\t\tfor(var i = 0; i < scripts.length; i++) {\n\t\t\tvar s = scripts[i];\n\t\t\tif(s.getAttribute(\"src\") == url || s.getAttribute(\"data-webpack\") == dataWebpackPrefix + key) { script = s; break; }\n\t\t}\n\t}\n\tif(!script) {\n\t\tneedAttach = true;\n\t\tscript = document.createElement('script');\n\n\t\tscript.charset = 'utf-8';\n\t\tscript.timeout = 120;\n\t\tif (__webpack_require__.nc) {\n\t\t\tscript.setAttribute(\"nonce\", __webpack_require__.nc);\n\t\t}\n\t\tscript.setAttribute(\"data-webpack\", dataWebpackPrefix + key);\n\t\tscript.src = url;\n\t}\n\tinProgress[url] = [done];\n\tvar onScriptComplete = (prev, event) => {\n\t\t// avoid mem leaks in IE.\n\t\tscript.onerror = script.onload = null;\n\t\tclearTimeout(timeout);\n\t\tvar doneFns = inProgress[url];\n\t\tdelete inProgress[url];\n\t\tscript.parentNode && script.parentNode.removeChild(script);\n\t\tdoneFns && doneFns.forEach((fn) => (fn(event)));\n\t\tif(prev) return prev(event);\n\t}\n\t;\n\tvar timeout = setTimeout(onScriptComplete.bind(null, undefined, { type: 'timeout', target: script }), 120000);\n\tscript.onerror = onScriptComplete.bind(null, script.onerror);\n\tscript.onload = onScriptComplete.bind(null, script.onload);\n\tneedAttach && document.head.appendChild(script);\n};",
         "// define __esModule on exports\n__webpack_require__.r = (exports) => {\n\tif(typeof Symbol !== 'undefined' && Symbol.toStringTag) {\n\t\tObject.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });\n\t}\n\tObject.defineProperty(exports, '__esModule', { value: true });\n};",
-        "__webpack_require__.S = {};\nvar initPromises = {};\nvar initTokens = {};\n__webpack_require__.I = (name, initScope) => {\n\tif(!initScope) initScope = [];\n\t// handling circular init calls\n\tvar initToken = initTokens[name];\n\tif(!initToken) initToken = initTokens[name] = {};\n\tif(initScope.indexOf(initToken) >= 0) return;\n\tinitScope.push(initToken);\n\t// only runs once\n\tif(initPromises[name]) return initPromises[name];\n\t// creates a new share scope if needed\n\tif(!__webpack_require__.o(__webpack_require__.S, name)) __webpack_require__.S[name] = {};\n\t// runs all init snippets from all modules reachable\n\tvar scope = __webpack_require__.S[name];\n\tvar warn = (msg) => (typeof console !== \"undefined\" && console.warn && console.warn(msg));\n\tvar uniqueName = \"fugue-jupyter\";\n\tvar register = (name, version, factory, eager) => {\n\t\tvar versions = scope[name] = scope[name] || {};\n\t\tvar activeVersion = versions[version];\n\t\tif(!activeVersion || (!activeVersion.loaded && (!eager != !activeVersion.eager ? eager : uniqueName > activeVersion.from))) versions[version] = { get: factory, from: uniqueName, eager: !!eager };\n\t};\n\tvar initExternal = (id) => {\n\t\tvar handleError = (err) => (warn(\"Initialization of sharing external failed: \" + err));\n\t\ttry {\n\t\t\tvar module = __webpack_require__(id);\n\t\t\tif(!module) return;\n\t\t\tvar initFn = (module) => (module && module.init && module.init(__webpack_require__.S[name], initScope))\n\t\t\tif(module.then) return promises.push(module.then(initFn, handleError));\n\t\t\tvar initResult = initFn(module);\n\t\t\tif(initResult && initResult.then) return promises.push(initResult['catch'](handleError));\n\t\t} catch(err) { handleError(err); }\n\t}\n\tvar promises = [];\n\tswitch(name) {\n\t\tcase \"default\": {\n\t\t\tregister(\"fugue-jupyter\", \"0.2.2\", () => (__webpack_require__.e(\"lib_index_js\").then(() => (() => (__webpack_require__(/*! ./lib/index.js */ \"./lib/index.js\"))))));\n\t\t}\n\t\tbreak;\n\t}\n\tif(!promises.length) return initPromises[name] = 1;\n\treturn initPromises[name] = Promise.all(promises).then(() => (initPromises[name] = 1));\n};",
+        "__webpack_require__.S = {};\nvar initPromises = {};\nvar initTokens = {};\n__webpack_require__.I = (name, initScope) => {\n\tif(!initScope) initScope = [];\n\t// handling circular init calls\n\tvar initToken = initTokens[name];\n\tif(!initToken) initToken = initTokens[name] = {};\n\tif(initScope.indexOf(initToken) >= 0) return;\n\tinitScope.push(initToken);\n\t// only runs once\n\tif(initPromises[name]) return initPromises[name];\n\t// creates a new share scope if needed\n\tif(!__webpack_require__.o(__webpack_require__.S, name)) __webpack_require__.S[name] = {};\n\t// runs all init snippets from all modules reachable\n\tvar scope = __webpack_require__.S[name];\n\tvar warn = (msg) => (typeof console !== \"undefined\" && console.warn && console.warn(msg));\n\tvar uniqueName = \"fugue-jupyter\";\n\tvar register = (name, version, factory, eager) => {\n\t\tvar versions = scope[name] = scope[name] || {};\n\t\tvar activeVersion = versions[version];\n\t\tif(!activeVersion || (!activeVersion.loaded && (!eager != !activeVersion.eager ? eager : uniqueName > activeVersion.from))) versions[version] = { get: factory, from: uniqueName, eager: !!eager };\n\t};\n\tvar initExternal = (id) => {\n\t\tvar handleError = (err) => (warn(\"Initialization of sharing external failed: \" + err));\n\t\ttry {\n\t\t\tvar module = __webpack_require__(id);\n\t\t\tif(!module) return;\n\t\t\tvar initFn = (module) => (module && module.init && module.init(__webpack_require__.S[name], initScope))\n\t\t\tif(module.then) return promises.push(module.then(initFn, handleError));\n\t\t\tvar initResult = initFn(module);\n\t\t\tif(initResult && initResult.then) return promises.push(initResult['catch'](handleError));\n\t\t} catch(err) { handleError(err); }\n\t}\n\tvar promises = [];\n\tswitch(name) {\n\t\tcase \"default\": {\n\t\t\tregister(\"fugue-jupyter\", \"0.2.3\", () => (__webpack_require__.e(\"lib_index_js\").then(() => (() => (__webpack_require__(/*! ./lib/index.js */ \"./lib/index.js\"))))));\n\t\t}\n\t\tbreak;\n\t}\n\tif(!promises.length) return initPromises[name] = 1;\n\treturn initPromises[name] = Promise.all(promises).then(() => (initPromises[name] = 1));\n};",
         "var scriptUrl;\nif (__webpack_require__.g.importScripts) scriptUrl = __webpack_require__.g.location + \"\";\nvar document = __webpack_require__.g.document;\nif (!scriptUrl && document) {\n\tif (document.currentScript)\n\t\tscriptUrl = document.currentScript.src\n\tif (!scriptUrl) {\n\t\tvar scripts = document.getElementsByTagName(\"script\");\n\t\tif(scripts.length) scriptUrl = scripts[scripts.length - 1].src\n\t}\n}\n// When supporting browsers where an automatic publicPath is not supported you must specify an output.publicPath manually via configuration\n// or pass an empty string (\"\") and set the __webpack_public_path__ variable from your code to use your own logic.\nif (!scriptUrl) throw new Error(\"Automatic publicPath is not supported in this browser\");\nscriptUrl = scriptUrl.replace(/#.*$/, \"\").replace(/\\?.*$/, \"\").replace(/\\/[^\\/]+$/, \"/\");\n__webpack_require__.p = scriptUrl;",
-        "var parseVersion = (str) => {\n\t// see webpack/lib/util/semver.js for original code\n\tvar p=p=>{return p.split(\".\").map((p=>{return+p==p?+p:p}))},n=/^([^-+]+)?(?:-([^+]+))?(?:\\+(.+))?$/.exec(str),r=n[1]?p(n[1]):[];return n[2]&&(r.length++,r.push.apply(r,p(n[2]))),n[3]&&(r.push([]),r.push.apply(r,p(n[3]))),r;\n}\nvar versionLt = (a, b) => {\n\t// see webpack/lib/util/semver.js for original code\n\ta=parseVersion(a),b=parseVersion(b);for(var r=0;;){if(r>=a.length)return r<b.length&&\"u\"!=(typeof b[r])[0];var e=a[r],n=(typeof e)[0];if(r>=b.length)return\"u\"==n;var t=b[r],f=(typeof t)[0];if(n!=f)return\"o\"==n&&\"n\"==f||(\"s\"==f||\"u\"==n);if(\"o\"!=n&&\"u\"!=n&&e!=t)return e<t;r++}\n}\nvar rangeToString = (range) => {\n\t// see webpack/lib/util/semver.js for original code\n\tvar r=range[0],n=\"\";if(1===range.length)return\"*\";if(r+.5){n+=0==r?\">=\":-1==r?\"<\":1==r?\"^\":2==r?\"~\":r>0?\"=\":\"!=\";for(var e=1,a=1;a<range.length;a++){e--,n+=\"u\"==(typeof(t=range[a]))[0]?\"-\":(e>0?\".\":\"\")+(e=2,t)}return n}var g=[];for(a=1;a<range.length;a++){var t=range[a];g.push(0===t?\"not(\"+o()+\")\":1===t?\"(\"+o()+\" || \"+o()+\")\":2===t?g.pop()+\" \"+g.pop():rangeToString(t))}return o();function o(){return g.pop().replace(/^\\((.+)\\)$/,\"$1\")}\n}\nvar satisfy = (range, version) => {\n\t// see webpack/lib/util/semver.js for original code\n\tif(0 in range){version=parseVersion(version);var e=range[0],r=e<0;r&&(e=-e-1);for(var n=0,i=1,a=!0;;i++,n++){var f,s,g=i<range.length?(typeof range[i])[0]:\"\";if(n>=version.length||\"o\"==(s=(typeof(f=version[n]))[0]))return!a||(\"u\"==g?i>e&&!r:\"\"==g!=r);if(\"u\"==s){if(!a||\"u\"!=g)return!1}else if(a)if(g==s)if(i<=e){if(f!=range[i])return!1}else{if(r?f>range[i]:f<range[i])return!1;f!=range[i]&&(a=!1)}else if(\"s\"!=g&&\"n\"!=g){if(r||i<=e)return!1;a=!1,i--}else{if(i<=e||s<g!=r)return!1;a=!1}else\"s\"!=g&&\"n\"!=g&&(a=!1,i--)}}var t=[],o=t.pop.bind(t);for(n=1;n<range.length;n++){var u=range[n];t.push(1==u?o()|o():2==u?o()&o():u?satisfy(u,version):!o())}return!!o();\n}\nvar ensureExistence = (scopeName, key) => {\n\tvar scope = __webpack_require__.S[scopeName];\n\tif(!scope || !__webpack_require__.o(scope, key)) throw new Error(\"Shared module \" + key + \" doesn't exist in shared scope \" + scopeName);\n\treturn scope;\n};\nvar findVersion = (scope, key) => {\n\tvar versions = scope[key];\n\tvar key = Object.keys(versions).reduce((a, b) => {\n\t\treturn !a || versionLt(a, b) ? b : a;\n\t}, 0);\n\treturn key && versions[key]\n};\nvar findSingletonVersionKey = (scope, key) => {\n\tvar versions = scope[key];\n\treturn Object.keys(versions).reduce((a, b) => {\n\t\treturn !a || (!versions[a].loaded && versionLt(a, b)) ? b : a;\n\t}, 0);\n};\nvar getInvalidSingletonVersionMessage = (scope, key, version, requiredVersion) => {\n\treturn \"Unsatisfied version \" + version + \" from \" + (version && scope[key][version].from) + \" of shared singleton module \" + key + \" (required \" + rangeToString(requiredVersion) + \")\"\n};\nvar getSingleton = (scope, scopeName, key, requiredVersion) => {\n\tvar version = findSingletonVersionKey(scope, key);\n\treturn get(scope[key][version]);\n};\nvar getSingletonVersion = (scope, scopeName, key, requiredVersion) => {\n\tvar version = findSingletonVersionKey(scope, key);\n\tif (!satisfy(requiredVersion, version)) typeof console !== \"undefined\" && console.warn && console.warn(getInvalidSingletonVersionMessage(scope, key, version, requiredVersion));\n\treturn get(scope[key][version]);\n};\nvar getStrictSingletonVersion = (scope, scopeName, key, requiredVersion) => {\n\tvar version = findSingletonVersionKey(scope, key);\n\tif (!satisfy(requiredVersion, version)) throw new Error(getInvalidSingletonVersionMessage(scope, key, version, requiredVersion));\n\treturn get(scope[key][version]);\n};\nvar findValidVersion = (scope, key, requiredVersion) => {\n\tvar versions = scope[key];\n\tvar key = Object.keys(versions).reduce((a, b) => {\n\t\tif (!satisfy(requiredVersion, b)) return a;\n\t\treturn !a || versionLt(a, b) ? b : a;\n\t}, 0);\n\treturn key && versions[key]\n};\nvar getInvalidVersionMessage = (scope, scopeName, key, requiredVersion) => {\n\tvar versions = scope[key];\n\treturn \"No satisfying version (\" + rangeToString(requiredVersion) + \") of shared module \" + key + \" found in shared scope \" + scopeName + \".\\n\" +\n\t\t\"Available versions: \" + Object.keys(versions).map((key) => {\n\t\treturn key + \" from \" + versions[key].from;\n\t}).join(\", \");\n};\nvar getValidVersion = (scope, scopeName, key, requiredVersion) => {\n\tvar entry = findValidVersion(scope, key, requiredVersion);\n\tif(entry) return get(entry);\n\tthrow new Error(getInvalidVersionMessage(scope, scopeName, key, requiredVersion));\n};\nvar warnInvalidVersion = (scope, scopeName, key, requiredVersion) => {\n\ttypeof console !== \"undefined\" && console.warn && console.warn(getInvalidVersionMessage(scope, scopeName, key, requiredVersion));\n};\nvar get = (entry) => {\n\tentry.loaded = 1;\n\treturn entry.get()\n};\nvar init = (fn) => (function(scopeName, a, b, c) {\n\tvar promise = __webpack_require__.I(scopeName);\n\tif (promise && promise.then) return promise.then(fn.bind(fn, scopeName, __webpack_require__.S[scopeName], a, b, c));\n\treturn fn(scopeName, __webpack_require__.S[scopeName], a, b, c);\n});\n\nvar load = /*#__PURE__*/ init((scopeName, scope, key) => {\n\tensureExistence(scopeName, key);\n\treturn get(findVersion(scope, key));\n});\nvar loadFallback = /*#__PURE__*/ init((scopeName, scope, key, fallback) => {\n\treturn scope && __webpack_require__.o(scope, key) ? get(findVersion(scope, key)) : fallback();\n});\nvar loadVersionCheck = /*#__PURE__*/ init((scopeName, scope, key, version) => {\n\tensureExistence(scopeName, key);\n\treturn get(findValidVersion(scope, key, version) || warnInvalidVersion(scope, scopeName, key, version) || findVersion(scope, key));\n});\nvar loadSingleton = /*#__PURE__*/ init((scopeName, scope, key) => {\n\tensureExistence(scopeName, key);\n\treturn getSingleton(scope, scopeName, key);\n});\nvar loadSingletonVersionCheck = /*#__PURE__*/ init((scopeName, scope, key, version) => {\n\tensureExistence(scopeName, key);\n\treturn getSingletonVersion(scope, scopeName, key, version);\n});\nvar loadStrictVersionCheck = /*#__PURE__*/ init((scopeName, scope, key, version) => {\n\tensureExistence(scopeName, key);\n\treturn getValidVersion(scope, scopeName, key, version);\n});\nvar loadStrictSingletonVersionCheck = /*#__PURE__*/ init((scopeName, scope, key, version) => {\n\tensureExistence(scopeName, key);\n\treturn getStrictSingletonVersion(scope, scopeName, key, version);\n});\nvar loadVersionCheckFallback = /*#__PURE__*/ init((scopeName, scope, key, version, fallback) => {\n\tif(!scope || !__webpack_require__.o(scope, key)) return fallback();\n\treturn get(findValidVersion(scope, key, version) || warnInvalidVersion(scope, scopeName, key, version) || findVersion(scope, key));\n});\nvar loadSingletonFallback = /*#__PURE__*/ init((scopeName, scope, key, fallback) => {\n\tif(!scope || !__webpack_require__.o(scope, key)) return fallback();\n\treturn getSingleton(scope, scopeName, key);\n});\nvar loadSingletonVersionCheckFallback = /*#__PURE__*/ init((scopeName, scope, key, version, fallback) => {\n\tif(!scope || !__webpack_require__.o(scope, key)) return fallback();\n\treturn getSingletonVersion(scope, scopeName, key, version);\n});\nvar loadStrictVersionCheckFallback = /*#__PURE__*/ init((scopeName, scope, key, version, fallback) => {\n\tvar entry = scope && __webpack_require__.o(scope, key) && findValidVersion(scope, key, version);\n\treturn entry ? get(entry) : fallback();\n});\nvar loadStrictSingletonVersionCheckFallback = /*#__PURE__*/ init((scopeName, scope, key, version, fallback) => {\n\tif(!scope || !__webpack_require__.o(scope, key)) return fallback();\n\treturn getStrictSingletonVersion(scope, scopeName, key, version);\n});\nvar installedModules = {};\nvar moduleToHandlerMapping = {\n\t\"webpack/sharing/consume/default/@jupyterlab/settingregistry\": () => (loadSingletonVersionCheck(\"default\", \"@jupyterlab/settingregistry\", [1,3,5,3])),\n\t\"webpack/sharing/consume/default/@krassowski/jupyterlab-lsp\": () => (loadSingletonVersionCheck(\"default\", \"@krassowski/jupyterlab-lsp\", [1,3,10,1])),\n\t\"webpack/sharing/consume/default/@jupyterlab/codemirror\": () => (loadSingletonVersionCheck(\"default\", \"@jupyterlab/codemirror\", [1,3,5,3])),\n\t\"webpack/sharing/consume/default/@jupyterlab/notebook\": () => (loadSingletonVersionCheck(\"default\", \"@jupyterlab/notebook\", [1,3,5,3])),\n\t\"webpack/sharing/consume/default/@jupyterlab/fileeditor\": () => (loadSingletonVersionCheck(\"default\", \"@jupyterlab/fileeditor\", [1,3,5,3]))\n};\n// no consumes in initial chunks\nvar chunkMapping = {\n\t\"lib_index_js\": [\n\t\t\"webpack/sharing/consume/default/@jupyterlab/settingregistry\",\n\t\t\"webpack/sharing/consume/default/@krassowski/jupyterlab-lsp\",\n\t\t\"webpack/sharing/consume/default/@jupyterlab/codemirror\",\n\t\t\"webpack/sharing/consume/default/@jupyterlab/notebook\",\n\t\t\"webpack/sharing/consume/default/@jupyterlab/fileeditor\"\n\t]\n};\n__webpack_require__.f.consumes = (chunkId, promises) => {\n\tif(__webpack_require__.o(chunkMapping, chunkId)) {\n\t\tchunkMapping[chunkId].forEach((id) => {\n\t\t\tif(__webpack_require__.o(installedModules, id)) return promises.push(installedModules[id]);\n\t\t\tvar onFactory = (factory) => {\n\t\t\t\tinstalledModules[id] = 0;\n\t\t\t\t__webpack_require__.m[id] = (module) => {\n\t\t\t\t\tdelete __webpack_require__.c[id];\n\t\t\t\t\tmodule.exports = factory();\n\t\t\t\t}\n\t\t\t};\n\t\t\tvar onError = (error) => {\n\t\t\t\tdelete installedModules[id];\n\t\t\t\t__webpack_require__.m[id] = (module) => {\n\t\t\t\t\tdelete __webpack_require__.c[id];\n\t\t\t\t\tthrow error;\n\t\t\t\t}\n\t\t\t};\n\t\t\ttry {\n\t\t\t\tvar promise = moduleToHandlerMapping[id]();\n\t\t\t\tif(promise.then) {\n\t\t\t\t\tpromises.push(installedModules[id] = promise.then(onFactory)['catch'](onError));\n\t\t\t\t} else onFactory(promise);\n\t\t\t} catch(e) { onError(e); }\n\t\t});\n\t}\n}",
+        "var parseVersion = (str) => {\n\t// see webpack/lib/util/semver.js for original code\n\tvar p=p=>{return p.split(\".\").map((p=>{return+p==p?+p:p}))},n=/^([^-+]+)?(?:-([^+]+))?(?:\\+(.+))?$/.exec(str),r=n[1]?p(n[1]):[];return n[2]&&(r.length++,r.push.apply(r,p(n[2]))),n[3]&&(r.push([]),r.push.apply(r,p(n[3]))),r;\n}\nvar versionLt = (a, b) => {\n\t// see webpack/lib/util/semver.js for original code\n\ta=parseVersion(a),b=parseVersion(b);for(var r=0;;){if(r>=a.length)return r<b.length&&\"u\"!=(typeof b[r])[0];var e=a[r],n=(typeof e)[0];if(r>=b.length)return\"u\"==n;var t=b[r],f=(typeof t)[0];if(n!=f)return\"o\"==n&&\"n\"==f||(\"s\"==f||\"u\"==n);if(\"o\"!=n&&\"u\"!=n&&e!=t)return e<t;r++}\n}\nvar rangeToString = (range) => {\n\t// see webpack/lib/util/semver.js for original code\n\tvar r=range[0],n=\"\";if(1===range.length)return\"*\";if(r+.5){n+=0==r?\">=\":-1==r?\"<\":1==r?\"^\":2==r?\"~\":r>0?\"=\":\"!=\";for(var e=1,a=1;a<range.length;a++){e--,n+=\"u\"==(typeof(t=range[a]))[0]?\"-\":(e>0?\".\":\"\")+(e=2,t)}return n}var g=[];for(a=1;a<range.length;a++){var t=range[a];g.push(0===t?\"not(\"+o()+\")\":1===t?\"(\"+o()+\" || \"+o()+\")\":2===t?g.pop()+\" \"+g.pop():rangeToString(t))}return o();function o(){return g.pop().replace(/^\\((.+)\\)$/,\"$1\")}\n}\nvar satisfy = (range, version) => {\n\t// see webpack/lib/util/semver.js for original code\n\tif(0 in range){version=parseVersion(version);var e=range[0],r=e<0;r&&(e=-e-1);for(var n=0,i=1,a=!0;;i++,n++){var f,s,g=i<range.length?(typeof range[i])[0]:\"\";if(n>=version.length||\"o\"==(s=(typeof(f=version[n]))[0]))return!a||(\"u\"==g?i>e&&!r:\"\"==g!=r);if(\"u\"==s){if(!a||\"u\"!=g)return!1}else if(a)if(g==s)if(i<=e){if(f!=range[i])return!1}else{if(r?f>range[i]:f<range[i])return!1;f!=range[i]&&(a=!1)}else if(\"s\"!=g&&\"n\"!=g){if(r||i<=e)return!1;a=!1,i--}else{if(i<=e||s<g!=r)return!1;a=!1}else\"s\"!=g&&\"n\"!=g&&(a=!1,i--)}}var t=[],o=t.pop.bind(t);for(n=1;n<range.length;n++){var u=range[n];t.push(1==u?o()|o():2==u?o()&o():u?satisfy(u,version):!o())}return!!o();\n}\nvar ensureExistence = (scopeName, key) => {\n\tvar scope = __webpack_require__.S[scopeName];\n\tif(!scope || !__webpack_require__.o(scope, key)) throw new Error(\"Shared module \" + key + \" doesn't exist in shared scope \" + scopeName);\n\treturn scope;\n};\nvar findVersion = (scope, key) => {\n\tvar versions = scope[key];\n\tvar key = Object.keys(versions).reduce((a, b) => {\n\t\treturn !a || versionLt(a, b) ? b : a;\n\t}, 0);\n\treturn key && versions[key]\n};\nvar findSingletonVersionKey = (scope, key) => {\n\tvar versions = scope[key];\n\treturn Object.keys(versions).reduce((a, b) => {\n\t\treturn !a || (!versions[a].loaded && versionLt(a, b)) ? b : a;\n\t}, 0);\n};\nvar getInvalidSingletonVersionMessage = (scope, key, version, requiredVersion) => {\n\treturn \"Unsatisfied version \" + version + \" from \" + (version && scope[key][version].from) + \" of shared singleton module \" + key + \" (required \" + rangeToString(requiredVersion) + \")\"\n};\nvar getSingleton = (scope, scopeName, key, requiredVersion) => {\n\tvar version = findSingletonVersionKey(scope, key);\n\treturn get(scope[key][version]);\n};\nvar getSingletonVersion = (scope, scopeName, key, requiredVersion) => {\n\tvar version = findSingletonVersionKey(scope, key);\n\tif (!satisfy(requiredVersion, version)) typeof console !== \"undefined\" && console.warn && console.warn(getInvalidSingletonVersionMessage(scope, key, version, requiredVersion));\n\treturn get(scope[key][version]);\n};\nvar getStrictSingletonVersion = (scope, scopeName, key, requiredVersion) => {\n\tvar version = findSingletonVersionKey(scope, key);\n\tif (!satisfy(requiredVersion, version)) throw new Error(getInvalidSingletonVersionMessage(scope, key, version, requiredVersion));\n\treturn get(scope[key][version]);\n};\nvar findValidVersion = (scope, key, requiredVersion) => {\n\tvar versions = scope[key];\n\tvar key = Object.keys(versions).reduce((a, b) => {\n\t\tif (!satisfy(requiredVersion, b)) return a;\n\t\treturn !a || versionLt(a, b) ? b : a;\n\t}, 0);\n\treturn key && versions[key]\n};\nvar getInvalidVersionMessage = (scope, scopeName, key, requiredVersion) => {\n\tvar versions = scope[key];\n\treturn \"No satisfying version (\" + rangeToString(requiredVersion) + \") of shared module \" + key + \" found in shared scope \" + scopeName + \".\\n\" +\n\t\t\"Available versions: \" + Object.keys(versions).map((key) => {\n\t\treturn key + \" from \" + versions[key].from;\n\t}).join(\", \");\n};\nvar getValidVersion = (scope, scopeName, key, requiredVersion) => {\n\tvar entry = findValidVersion(scope, key, requiredVersion);\n\tif(entry) return get(entry);\n\tthrow new Error(getInvalidVersionMessage(scope, scopeName, key, requiredVersion));\n};\nvar warnInvalidVersion = (scope, scopeName, key, requiredVersion) => {\n\ttypeof console !== \"undefined\" && console.warn && console.warn(getInvalidVersionMessage(scope, scopeName, key, requiredVersion));\n};\nvar get = (entry) => {\n\tentry.loaded = 1;\n\treturn entry.get()\n};\nvar init = (fn) => (function(scopeName, a, b, c) {\n\tvar promise = __webpack_require__.I(scopeName);\n\tif (promise && promise.then) return promise.then(fn.bind(fn, scopeName, __webpack_require__.S[scopeName], a, b, c));\n\treturn fn(scopeName, __webpack_require__.S[scopeName], a, b, c);\n});\n\nvar load = /*#__PURE__*/ init((scopeName, scope, key) => {\n\tensureExistence(scopeName, key);\n\treturn get(findVersion(scope, key));\n});\nvar loadFallback = /*#__PURE__*/ init((scopeName, scope, key, fallback) => {\n\treturn scope && __webpack_require__.o(scope, key) ? get(findVersion(scope, key)) : fallback();\n});\nvar loadVersionCheck = /*#__PURE__*/ init((scopeName, scope, key, version) => {\n\tensureExistence(scopeName, key);\n\treturn get(findValidVersion(scope, key, version) || warnInvalidVersion(scope, scopeName, key, version) || findVersion(scope, key));\n});\nvar loadSingleton = /*#__PURE__*/ init((scopeName, scope, key) => {\n\tensureExistence(scopeName, key);\n\treturn getSingleton(scope, scopeName, key);\n});\nvar loadSingletonVersionCheck = /*#__PURE__*/ init((scopeName, scope, key, version) => {\n\tensureExistence(scopeName, key);\n\treturn getSingletonVersion(scope, scopeName, key, version);\n});\nvar loadStrictVersionCheck = /*#__PURE__*/ init((scopeName, scope, key, version) => {\n\tensureExistence(scopeName, key);\n\treturn getValidVersion(scope, scopeName, key, version);\n});\nvar loadStrictSingletonVersionCheck = /*#__PURE__*/ init((scopeName, scope, key, version) => {\n\tensureExistence(scopeName, key);\n\treturn getStrictSingletonVersion(scope, scopeName, key, version);\n});\nvar loadVersionCheckFallback = /*#__PURE__*/ init((scopeName, scope, key, version, fallback) => {\n\tif(!scope || !__webpack_require__.o(scope, key)) return fallback();\n\treturn get(findValidVersion(scope, key, version) || warnInvalidVersion(scope, scopeName, key, version) || findVersion(scope, key));\n});\nvar loadSingletonFallback = /*#__PURE__*/ init((scopeName, scope, key, fallback) => {\n\tif(!scope || !__webpack_require__.o(scope, key)) return fallback();\n\treturn getSingleton(scope, scopeName, key);\n});\nvar loadSingletonVersionCheckFallback = /*#__PURE__*/ init((scopeName, scope, key, version, fallback) => {\n\tif(!scope || !__webpack_require__.o(scope, key)) return fallback();\n\treturn getSingletonVersion(scope, scopeName, key, version);\n});\nvar loadStrictVersionCheckFallback = /*#__PURE__*/ init((scopeName, scope, key, version, fallback) => {\n\tvar entry = scope && __webpack_require__.o(scope, key) && findValidVersion(scope, key, version);\n\treturn entry ? get(entry) : fallback();\n});\nvar loadStrictSingletonVersionCheckFallback = /*#__PURE__*/ init((scopeName, scope, key, version, fallback) => {\n\tif(!scope || !__webpack_require__.o(scope, key)) return fallback();\n\treturn getStrictSingletonVersion(scope, scopeName, key, version);\n});\nvar installedModules = {};\nvar moduleToHandlerMapping = {\n\t\"webpack/sharing/consume/default/@jupyterlab/settingregistry\": () => (loadSingletonVersionCheck(\"default\", \"@jupyterlab/settingregistry\", [1,3,6,3])),\n\t\"webpack/sharing/consume/default/@krassowski/jupyterlab-lsp\": () => (loadSingletonVersionCheck(\"default\", \"@krassowski/jupyterlab-lsp\", [1,3,10,1])),\n\t\"webpack/sharing/consume/default/@jupyterlab/codemirror\": () => (loadSingletonVersionCheck(\"default\", \"@jupyterlab/codemirror\", [1,3,6,3])),\n\t\"webpack/sharing/consume/default/@jupyterlab/notebook\": () => (loadSingletonVersionCheck(\"default\", \"@jupyterlab/notebook\", [1,3,6,3])),\n\t\"webpack/sharing/consume/default/@jupyterlab/fileeditor\": () => (loadSingletonVersionCheck(\"default\", \"@jupyterlab/fileeditor\", [1,3,6,3]))\n};\n// no consumes in initial chunks\nvar chunkMapping = {\n\t\"lib_index_js\": [\n\t\t\"webpack/sharing/consume/default/@jupyterlab/settingregistry\",\n\t\t\"webpack/sharing/consume/default/@krassowski/jupyterlab-lsp\",\n\t\t\"webpack/sharing/consume/default/@jupyterlab/codemirror\",\n\t\t\"webpack/sharing/consume/default/@jupyterlab/notebook\",\n\t\t\"webpack/sharing/consume/default/@jupyterlab/fileeditor\"\n\t]\n};\n__webpack_require__.f.consumes = (chunkId, promises) => {\n\tif(__webpack_require__.o(chunkMapping, chunkId)) {\n\t\tchunkMapping[chunkId].forEach((id) => {\n\t\t\tif(__webpack_require__.o(installedModules, id)) return promises.push(installedModules[id]);\n\t\t\tvar onFactory = (factory) => {\n\t\t\t\tinstalledModules[id] = 0;\n\t\t\t\t__webpack_require__.m[id] = (module) => {\n\t\t\t\t\tdelete __webpack_require__.c[id];\n\t\t\t\t\tmodule.exports = factory();\n\t\t\t\t}\n\t\t\t};\n\t\t\tvar onError = (error) => {\n\t\t\t\tdelete installedModules[id];\n\t\t\t\t__webpack_require__.m[id] = (module) => {\n\t\t\t\t\tdelete __webpack_require__.c[id];\n\t\t\t\t\tthrow error;\n\t\t\t\t}\n\t\t\t};\n\t\t\ttry {\n\t\t\t\tvar promise = moduleToHandlerMapping[id]();\n\t\t\t\tif(promise.then) {\n\t\t\t\t\tpromises.push(installedModules[id] = promise.then(onFactory)['catch'](onError));\n\t\t\t\t} else onFactory(promise);\n\t\t\t} catch(e) { onError(e); }\n\t\t});\n\t}\n}",
         "// no baseURI\n\n// object to store loaded and loading chunks\n// undefined = chunk not loaded, null = chunk preloaded/prefetched\n// [resolve, reject, Promise] = chunk loading, 0 = chunk loaded\nvar installedChunks = {\n\t\"fugue-jupyter\": 0\n};\n\n__webpack_require__.f.j = (chunkId, promises) => {\n\t\t// JSONP chunk loading for javascript\n\t\tvar installedChunkData = __webpack_require__.o(installedChunks, chunkId) ? installedChunks[chunkId] : undefined;\n\t\tif(installedChunkData !== 0) { // 0 means \"already installed\".\n\n\t\t\t// a Promise means \"currently loading\".\n\t\t\tif(installedChunkData) {\n\t\t\t\tpromises.push(installedChunkData[2]);\n\t\t\t} else {\n\t\t\t\tif(true) { // all chunks have JS\n\t\t\t\t\t// setup Promise in chunk cache\n\t\t\t\t\tvar promise = new Promise((resolve, reject) => (installedChunkData = installedChunks[chunkId] = [resolve, reject]));\n\t\t\t\t\tpromises.push(installedChunkData[2] = promise);\n\n\t\t\t\t\t// start chunk loading\n\t\t\t\t\tvar url = __webpack_require__.p + __webpack_require__.u(chunkId);\n\t\t\t\t\t// create error before stack unwound to get useful stacktrace later\n\t\t\t\t\tvar error = new Error();\n\t\t\t\t\tvar loadingEnded = (event) => {\n\t\t\t\t\t\tif(__webpack_require__.o(installedChunks, chunkId)) {\n\t\t\t\t\t\t\tinstalledChunkData = installedChunks[chunkId];\n\t\t\t\t\t\t\tif(installedChunkData !== 0) installedChunks[chunkId] = undefined;\n\t\t\t\t\t\t\tif(installedChunkData) {\n\t\t\t\t\t\t\t\tvar errorType = event && (event.type === 'load' ? 'missing' : event.type);\n\t\t\t\t\t\t\t\tvar realSrc = event && event.target && event.target.src;\n\t\t\t\t\t\t\t\terror.message = 'Loading chunk ' + chunkId + ' failed.\\n(' + errorType + ': ' + realSrc + ')';\n\t\t\t\t\t\t\t\terror.name = 'ChunkLoadError';\n\t\t\t\t\t\t\t\terror.type = errorType;\n\t\t\t\t\t\t\t\terror.request = realSrc;\n\t\t\t\t\t\t\t\tinstalledChunkData[1](error);\n\t\t\t\t\t\t\t}\n\t\t\t\t\t\t}\n\t\t\t\t\t};\n\t\t\t\t\t__webpack_require__.l(url, loadingEnded, \"chunk-\" + chunkId, chunkId);\n\t\t\t\t} else installedChunks[chunkId] = 0;\n\t\t\t}\n\t\t}\n};\n\n// no prefetching\n\n// no preloaded\n\n// no HMR\n\n// no HMR manifest\n\n// no on chunks loaded\n\n// install a JSONP callback for chunk loading\nvar webpackJsonpCallback = (parentChunkLoadingFunction, data) => {\n\tvar [chunkIds, moreModules, runtime] = data;\n\t// add \"moreModules\" to the modules object,\n\t// then flag all \"chunkIds\" as loaded and fire callback\n\tvar moduleId, chunkId, i = 0;\n\tif(chunkIds.some((id) => (installedChunks[id] !== 0))) {\n\t\tfor(moduleId in moreModules) {\n\t\t\tif(__webpack_require__.o(moreModules, moduleId)) {\n\t\t\t\t__webpack_require__.m[moduleId] = moreModules[moduleId];\n\t\t\t}\n\t\t}\n\t\tif(runtime) var result = runtime(__webpack_require__);\n\t}\n\tif(parentChunkLoadingFunction) parentChunkLoadingFunction(data);\n\tfor(;i < chunkIds.length; i++) {\n\t\tchunkId = chunkIds[i];\n\t\tif(__webpack_require__.o(installedChunks, chunkId) && installedChunks[chunkId]) {\n\t\t\tinstalledChunks[chunkId][0]();\n\t\t}\n\t\tinstalledChunks[chunkId] = 0;\n\t}\n\n}\n\nvar chunkLoadingGlobal = self[\"webpackChunkfugue_jupyter\"] = self[\"webpackChunkfugue_jupyter\"] || [];\nchunkLoadingGlobal.forEach(webpackJsonpCallback.bind(null, 0));\nchunkLoadingGlobal.push = webpackJsonpCallback.bind(null, chunkLoadingGlobal.push.bind(chunkLoadingGlobal));",
         "__webpack_require__.nc = undefined;",
         "",
         "// module cache are used so entry inlining is disabled\n// startup\n// Load entry module and return exports\nvar __webpack_exports__ = __webpack_require__(\"webpack/container/entry/fugue-jupyter\");\n",
         ""
     ],
     "version": 3
```

### Comparing `fugue_jupyter-0.2.2/fugue_jupyter/labextension/static/style_index_js.308b73f665deca4ee2f3.js` & `fugue_jupyter-0.2.3/fugue_jupyter/labextension/static/style_index_js.308b73f665deca4ee2f3.js`

 * *Files identical despite different names*

### Comparing `fugue_jupyter-0.2.2/fugue_jupyter/labextension/static/style_index_js.308b73f665deca4ee2f3.js.map` & `fugue_jupyter-0.2.3/fugue_jupyter/labextension/static/style_index_js.308b73f665deca4ee2f3.js.map`

 * *Files identical despite different names*

### Comparing `fugue_jupyter-0.2.2/fugue_jupyter/labextension/static/vendors-node_modules_css-loader_dist_runtime_api_js-node_modules_css-loader_dist_runtime_cssW-72eba1.c07606ee12302cc69c16.js` & `fugue_jupyter-0.2.3/fugue_jupyter/labextension/static/vendors-node_modules_css-loader_dist_runtime_api_js-node_modules_css-loader_dist_runtime_cssW-72eba1.c07606ee12302cc69c16.js`

 * *Files identical despite different names*

### Comparing `fugue_jupyter-0.2.2/fugue_jupyter/labextension/static/vendors-node_modules_css-loader_dist_runtime_api_js-node_modules_css-loader_dist_runtime_cssW-72eba1.c07606ee12302cc69c16.js.map` & `fugue_jupyter-0.2.3/fugue_jupyter/labextension/static/vendors-node_modules_css-loader_dist_runtime_api_js-node_modules_css-loader_dist_runtime_cssW-72eba1.c07606ee12302cc69c16.js.map`

 * *Files identical despite different names*

### Comparing `fugue_jupyter-0.2.2/fugue_jupyter/nbextension/main.js` & `fugue_jupyter-0.2.3/fugue_jupyter/nbextension/main.js`

 * *Files 1% similar despite different names*

#### js-beautify {}

```diff
@@ -18,15 +18,15 @@
     function set(str) {
         var obj = {},
             words = str.split(" ");
         for (var i = 0; i < words.length; ++i) obj[words[i]] = true;
         return obj;
     }
 
-    var fugue_keywords = "system bernoulli reservoir approx fill hash rand even presort persist broadcast params process output outtransform rowcount concurrency prepartition zip print title save append parquet csv json single checkpoint weak strong deterministic yield connect sample seed take sub callback dataframe file";
+    var fugue_keywords = "system bernoulli reservoir approx fill hash rand even coarse presort persist broadcast params process output outtransform rowcount concurrency prepartition zip print title save append parquet csv json single checkpoint weak strong deterministic yield connect sample seed take sub callback dataframe file";
 
     function load_extension() {
 
         CodeMirror.defineMIME("text/x-fsql", {
             name: "sql",
             keywords: set(fugue_keywords + " add after all alter analyze and anti archive array as asc at between bucket buckets by cache cascade case cast change clear cluster clustered codegen collection column columns comment commit compact compactions compute concatenate cost create cross cube current current_date current_timestamp database databases data dbproperties defined delete delimited deny desc describe dfs directories distinct distribute drop else end escaped except exchange exists explain export extended external false fields fileformat first following for format formatted from full function functions global grant group grouping having if ignore import in index indexes inner inpath inputformat insert intersect interval into is items join keys last lateral lazy left like limit lines list load local location lock locks logical macro map minus msck natural no not null nulls of on optimize option options or order out outer outputformat over overwrite partition partitioned partitions percent preceding principals purge range recordreader recordwriter recover reduce refresh regexp rename repair replace reset restrict revoke right rlike role roles rollback rollup row rows schema schemas select semi separated serde serdeproperties set sets show skewed sort sorted start statistics stored stratify struct table tables tablesample tblproperties temp temporary terminated then to touch transaction transactions transform true truncate unarchive unbounded uncache union unlock unset use using values view when where window with"),
             builtin: set("date datetime tinyint smallint int bigint boolean float double string binary timestamp decimal array map struct uniontype delimited serde sequencefile textfile rcfile inputformat outputformat"),
```

### Comparing `fugue_jupyter-0.2.2/fugue_jupyter/utils.py` & `fugue_jupyter-0.2.3/fugue_jupyter/utils.py`

 * *Files identical despite different names*

### Comparing `fugue_jupyter-0.2.2/fugue_jupyter.egg-info/PKG-INFO` & `fugue_jupyter-0.2.3/fugue_jupyter.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: fugue-jupyter
-Version: 0.2.2
+Version: 0.2.3
 Summary: Jupyterlab Extension for Fugue
 Home-page: https://github.com/fugue-project/fugue-jupyter
 Author: The Fugue Development Team
 Author-email: hello@fugue.ai
 License: BSD-3-Clause
 Keywords: Jupyter,JupyterLab,JupyterLab3
 Platform: Linux
```

### Comparing `fugue_jupyter-0.2.2/fugue_jupyter.egg-info/SOURCES.txt` & `fugue_jupyter-0.2.3/fugue_jupyter.egg-info/SOURCES.txt`

 * *Files 5% similar despite different names*

```diff
@@ -22,18 +22,18 @@
 fugue_jupyter.egg-info/entry_points.txt
 fugue_jupyter.egg-info/not-zip-safe
 fugue_jupyter.egg-info/requires.txt
 fugue_jupyter.egg-info/top_level.txt
 fugue_jupyter/labextension/build_log.json
 fugue_jupyter/labextension/package.json
 fugue_jupyter/labextension/schemas/fugue-jupyter/package.json.orig
-fugue_jupyter/labextension/static/lib_index_js.ad9a1c1d1f8d504aeb4b.js
-fugue_jupyter/labextension/static/lib_index_js.ad9a1c1d1f8d504aeb4b.js.map
-fugue_jupyter/labextension/static/remoteEntry.8a36f4b5ce59a9dca3d8.js
-fugue_jupyter/labextension/static/remoteEntry.8a36f4b5ce59a9dca3d8.js.map
+fugue_jupyter/labextension/static/lib_index_js.1b56285a6b63fec28143.js
+fugue_jupyter/labextension/static/lib_index_js.1b56285a6b63fec28143.js.map
+fugue_jupyter/labextension/static/remoteEntry.99193cc822ff3f92fd07.js
+fugue_jupyter/labextension/static/remoteEntry.99193cc822ff3f92fd07.js.map
 fugue_jupyter/labextension/static/style.js
 fugue_jupyter/labextension/static/style_index_js.308b73f665deca4ee2f3.js
 fugue_jupyter/labextension/static/style_index_js.308b73f665deca4ee2f3.js.map
 fugue_jupyter/labextension/static/vendors-node_modules_css-loader_dist_runtime_api_js-node_modules_css-loader_dist_runtime_cssW-72eba1.c07606ee12302cc69c16.js
 fugue_jupyter/labextension/static/vendors-node_modules_css-loader_dist_runtime_api_js-node_modules_css-loader_dist_runtime_cssW-72eba1.c07606ee12302cc69c16.js.map
 fugue_jupyter/nbextension/README.md
 fugue_jupyter/nbextension/__init__.py
```

### Comparing `fugue_jupyter-0.2.2/fugue_jupyter_version/_version.py` & `fugue_jupyter-0.2.3/fugue_jupyter_version/_version.py`

 * *Files identical despite different names*

### Comparing `fugue_jupyter-0.2.2/package.json` & `fugue_jupyter-0.2.3/package.json`

 * *Files 0% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9772727272727273%*

 * *Differences: {"'version'": "'0.2.3'"}*

```diff
@@ -112,9 +112,9 @@
     "sideEffects": [
         "style/*.css",
         "style/index.js"
     ],
     "style": "style/index.css",
     "styleModule": "style/index.js",
     "types": "lib/index.d.ts",
-    "version": "0.2.2"
+    "version": "0.2.3"
 }
```

### Comparing `fugue_jupyter-0.2.2/pyproject.toml` & `fugue_jupyter-0.2.3/pyproject.toml`

 * *Files identical despite different names*

### Comparing `fugue_jupyter-0.2.2/setup.py` & `fugue_jupyter-0.2.3/setup.py`

 * *Files 2% similar despite different names*

```diff
@@ -62,15 +62,15 @@
     long_description=long_description,
     long_description_content_type="text/markdown",
     packages=setuptools.find_packages(),
     install_requires=[
         "fugue>=0.8.0",
         "notebook",
         "jupyterlab>=3.0",
-        "jupyterlab-lsp",
+        "jupyterlab-lsp<4",
         "ipython>=7.10.0",
     ],
     zip_safe=False,
     include_package_data=True,
     python_requires=">=3.7",
     platforms="Linux, Mac OS X, Windows",
     keywords=["Jupyter", "JupyterLab", "JupyterLab3"],
```

### Comparing `fugue_jupyter-0.2.2/src/index.ts` & `fugue_jupyter-0.2.3/src/index.ts`

 * *Files identical despite different names*

### Comparing `fugue_jupyter-0.2.2/src/utils.ts` & `fugue_jupyter-0.2.3/src/utils.ts`

 * *Files 0% similar despite different names*

```diff
@@ -87,15 +87,15 @@
   for (let i = 0; i < words.length; ++i) {
     obj[words[i]] = true;
   }
   return obj;
 }
 
 const fugue_keywords =
-  'system bernoulli reservoir approx fill hash rand even presort persist broadcast params process output outtransform rowcount concurrency prepartition zip print title save append parquet csv json single checkpoint weak strong deterministic yield connect sample seed take sub callback dataframe file';
+  'system bernoulli reservoir approx fill hash rand even coarse presort persist broadcast params process output outtransform rowcount concurrency prepartition zip print title save append parquet csv json single checkpoint weak strong deterministic yield connect sample seed take sub callback dataframe file';
 
 /**
  * Register text editor based on file type.
  * @param c
  * @param language
  */
 export function registerCodeMirrorFor(c: ICodeMirror, language: string) {
```

### Comparing `fugue_jupyter-0.2.2/tsconfig.json` & `fugue_jupyter-0.2.3/tsconfig.json`

 * *Files identical despite different names*

### Comparing `fugue_jupyter-0.2.2/yarn.lock` & `fugue_jupyter-0.2.3/yarn.lock`

 * *Files identical despite different names*

