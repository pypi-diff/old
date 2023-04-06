# Comparing `tmp/pollination-streamlit-io-0.9.2.tar.gz` & `tmp/pollination-streamlit-io-0.9.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/pollination-streamlit-io-0.9.2.tar", last modified: Mon Jan 24 18:10:58 2022, max compression
+gzip compressed data, was "dist/pollination-streamlit-io-0.9.3.tar", last modified: Mon Jan 24 19:09:43 2022, max compression
```

## Comparing `pollination-streamlit-io-0.9.2.tar` & `pollination-streamlit-io-0.9.3.tar`

### file list

```diff
@@ -1,127 +1,127 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-24 18:10:58.000000 pollination-streamlit-io-0.9.2/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-24 18:10:58.000000 pollination-streamlit-io-0.9.2/.github/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-24 18:10:58.000000 pollination-streamlit-io-0.9.2/.github/workflows/
--rw-r--r--   0 runner    (1001) docker     (121)     1070 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/.github/workflows/ci.yaml
--rw-r--r--   0 runner    (1001) docker     (121)     1912 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/.gitignore
--rw-r--r--   0 runner    (1001) docker     (121)      252 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/.releaserc.json
--rw-r--r--   0 runner    (1001) docker     (121)    11357 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/LICENSE
--rw-r--r--   0 runner    (1001) docker     (121)      231 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (121)     1051 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/Makefile
--rw-r--r--   0 runner    (1001) docker     (121)      734 2022-01-24 18:10:58.000000 pollination-streamlit-io-0.9.2/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     2688 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/README.md
--rw-r--r--   0 runner    (1001) docker     (121)      165 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/deploy.sh
--rw-r--r--   0 runner    (1001) docker     (121)      134 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/dev-requirements.txt
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-24 18:10:58.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-24 18:10:58.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/
--rw-r--r--   0 runner    (1001) docker     (121)     6190 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-24 18:10:58.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/command/
--rw-r--r--   0 runner    (1001) docker     (121)     1047 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/command/asset-manifest.json
--rw-r--r--   0 runner    (1001) docker     (121)   197413 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/command/bootstrap.min.css
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-24 18:10:58.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/command/img/
--rw-r--r--   0 runner    (1001) docker     (121)      683 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/command/img/pollination.png
--rw-r--r--   0 runner    (1001) docker     (121)     2178 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/command/index.html
--rw-r--r--   0 runner    (1001) docker     (121)      663 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/command/precache-manifest.0f4233bec0f0ede2fb1ec26c7122dc4e.js
--rw-r--r--   0 runner    (1001) docker     (121)     1183 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/command/service-worker.js
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-24 18:10:58.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/command/static/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-24 18:10:58.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/command/static/css/
--rw-r--r--   0 runner    (1001) docker     (121)     1327 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/command/static/css/main.3ccb58d0.chunk.css
--rw-r--r--   0 runner    (1001) docker     (121)     2796 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/command/static/css/main.3ccb58d0.chunk.css.map
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-24 18:10:58.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/command/static/js/
--rw-r--r--   0 runner    (1001) docker     (121)   467958 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/command/static/js/2.1408e9e6.chunk.js
--rw-r--r--   0 runner    (1001) docker     (121)     1653 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/command/static/js/2.1408e9e6.chunk.js.LICENSE.txt
--rw-r--r--   0 runner    (1001) docker     (121)  1583780 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/command/static/js/2.1408e9e6.chunk.js.map
--rw-r--r--   0 runner    (1001) docker     (121)     1968 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/command/static/js/main.205cae2d.chunk.js
--rw-r--r--   0 runner    (1001) docker     (121)     4361 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/command/static/js/main.205cae2d.chunk.js.map
--rw-r--r--   0 runner    (1001) docker     (121)     1598 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/command/static/js/runtime-main.11ec9aca.js
--rw-r--r--   0 runner    (1001) docker     (121)     8317 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/command/static/js/runtime-main.11ec9aca.js.map
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-24 18:10:58.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/get/
--rw-r--r--   0 runner    (1001) docker     (121)     1047 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/get/asset-manifest.json
--rw-r--r--   0 runner    (1001) docker     (121)   197413 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/get/bootstrap.min.css
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-24 18:10:58.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/get/img/
--rw-r--r--   0 runner    (1001) docker     (121)      683 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/get/img/pollination.png
--rw-r--r--   0 runner    (1001) docker     (121)     2178 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/get/index.html
--rw-r--r--   0 runner    (1001) docker     (121)      663 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/get/precache-manifest.5f91bb71437502227394bca7b31634e0.js
--rw-r--r--   0 runner    (1001) docker     (121)     1183 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/get/service-worker.js
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-24 18:10:58.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/get/static/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-24 18:10:58.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/get/static/css/
--rw-r--r--   0 runner    (1001) docker     (121)     1327 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/get/static/css/main.3ccb58d0.chunk.css
--rw-r--r--   0 runner    (1001) docker     (121)     2796 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/get/static/css/main.3ccb58d0.chunk.css.map
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-24 18:10:58.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/get/static/js/
--rw-r--r--   0 runner    (1001) docker     (121)   467958 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/get/static/js/2.dc22e782.chunk.js
--rw-r--r--   0 runner    (1001) docker     (121)     1653 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/get/static/js/2.dc22e782.chunk.js.LICENSE.txt
--rw-r--r--   0 runner    (1001) docker     (121)  1583770 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/get/static/js/2.dc22e782.chunk.js.map
--rw-r--r--   0 runner    (1001) docker     (121)     2690 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/get/static/js/main.a7c0ac14.chunk.js
--rw-r--r--   0 runner    (1001) docker     (121)     6364 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/get/static/js/main.a7c0ac14.chunk.js.map
--rw-r--r--   0 runner    (1001) docker     (121)     1598 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/get/static/js/runtime-main.11ec9aca.js
--rw-r--r--   0 runner    (1001) docker     (121)     8317 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/get/static/js/runtime-main.11ec9aca.js.map
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-24 18:10:58.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/send/
--rw-r--r--   0 runner    (1001) docker     (121)     1047 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/send/asset-manifest.json
--rw-r--r--   0 runner    (1001) docker     (121)   197413 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/send/bootstrap.min.css
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-24 18:10:58.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/send/img/
--rw-r--r--   0 runner    (1001) docker     (121)      683 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/send/img/pollination.png
--rw-r--r--   0 runner    (1001) docker     (121)     2178 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/send/index.html
--rw-r--r--   0 runner    (1001) docker     (121)      663 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/send/precache-manifest.fa02a73d161599b9272907462ae7a0a0.js
--rw-r--r--   0 runner    (1001) docker     (121)     1183 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/send/service-worker.js
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-24 18:10:58.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/send/static/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-24 18:10:58.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/send/static/css/
--rw-r--r--   0 runner    (1001) docker     (121)     1327 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/send/static/css/main.3ccb58d0.chunk.css
--rw-r--r--   0 runner    (1001) docker     (121)     2796 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/send/static/css/main.3ccb58d0.chunk.css.map
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-24 18:10:58.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/send/static/js/
--rw-r--r--   0 runner    (1001) docker     (121)   467958 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/send/static/js/2.542a2d66.chunk.js
--rw-r--r--   0 runner    (1001) docker     (121)     1653 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/send/static/js/2.542a2d66.chunk.js.LICENSE.txt
--rw-r--r--   0 runner    (1001) docker     (121)  1583780 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/send/static/js/2.542a2d66.chunk.js.map
--rw-r--r--   0 runner    (1001) docker     (121)     2170 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/send/static/js/main.f34693c1.chunk.js
--rw-r--r--   0 runner    (1001) docker     (121)     5156 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/send/static/js/main.f34693c1.chunk.js.map
--rw-r--r--   0 runner    (1001) docker     (121)     1598 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/send/static/js/runtime-main.11ec9aca.js
--rw-r--r--   0 runner    (1001) docker     (121)     8317 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/send/static/js/runtime-main.11ec9aca.js.map
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-24 18:10:58.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/inputs/
--rw-r--r--   0 runner    (1001) docker     (121)     2266 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/inputs/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-24 18:10:58.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/inputs/send/
--rw-r--r--   0 runner    (1001) docker     (121)     1047 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/inputs/send/asset-manifest.json
--rw-r--r--   0 runner    (1001) docker     (121)   197413 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/inputs/send/bootstrap.min.css
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-24 18:10:58.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/inputs/send/img/
--rw-r--r--   0 runner    (1001) docker     (121)      683 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/inputs/send/img/pollination.png
--rw-r--r--   0 runner    (1001) docker     (121)     2178 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/inputs/send/index.html
--rw-r--r--   0 runner    (1001) docker     (121)      663 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/inputs/send/precache-manifest.8386fb1c8be5d22d126bcefa39298394.js
--rw-r--r--   0 runner    (1001) docker     (121)     1183 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/inputs/send/service-worker.js
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-24 18:10:58.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/inputs/send/static/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-24 18:10:58.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/inputs/send/static/css/
--rw-r--r--   0 runner    (1001) docker     (121)     1456 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/inputs/send/static/css/main.96dbfc01.chunk.css
--rw-r--r--   0 runner    (1001) docker     (121)     2983 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/inputs/send/static/css/main.96dbfc01.chunk.css.map
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-24 18:10:58.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/inputs/send/static/js/
--rw-r--r--   0 runner    (1001) docker     (121)   467923 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/inputs/send/static/js/2.671b2fa3.chunk.js
--rw-r--r--   0 runner    (1001) docker     (121)     1653 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/inputs/send/static/js/2.671b2fa3.chunk.js.LICENSE.txt
--rw-r--r--   0 runner    (1001) docker     (121)  1583770 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/inputs/send/static/js/2.671b2fa3.chunk.js.map
--rw-r--r--   0 runner    (1001) docker     (121)     2459 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/inputs/send/static/js/main.daad708a.chunk.js
--rw-r--r--   0 runner    (1001) docker     (121)     6189 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/inputs/send/static/js/main.daad708a.chunk.js.map
--rw-r--r--   0 runner    (1001) docker     (121)     1598 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/inputs/send/static/js/runtime-main.11ec9aca.js
--rw-r--r--   0 runner    (1001) docker     (121)     8317 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/inputs/send/static/js/runtime-main.11ec9aca.js.map
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-24 18:10:58.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/special/
--rw-r--r--   0 runner    (1001) docker     (121)      994 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/special/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-24 18:10:58.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/special/sync/
--rw-r--r--   0 runner    (1001) docker     (121)      313 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/special/sync/index.html
--rw-r--r--   0 runner    (1001) docker     (121)     2756 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/special/sync/script.js
--rw-r--r--   0 runner    (1001) docker     (121)     1764 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io/special/sync/styles.css
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-24 18:10:58.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)      734 2022-01-24 18:10:58.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     5078 2022-01-24 18:10:58.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-01-24 18:10:58.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)       17 2022-01-24 18:10:58.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)       25 2022-01-24 18:10:58.000000 pollination-streamlit-io-0.9.2/pollination_streamlit_io.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (121)       17 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/requirements.txt
--rw-r--r--   0 runner    (1001) docker     (121)      102 2022-01-24 18:10:58.000000 pollination-streamlit-io-0.9.2/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)     1057 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-24 18:10:58.000000 pollination-streamlit-io-0.9.2/tests/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-24 18:10:58.000000 pollination-streamlit-io-0.9.2/tests/apps/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-24 18:10:58.000000 pollination-streamlit-io-0.9.2/tests/apps/context-app/
--rw-r--r--   0 runner    (1001) docker     (121)     3153 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/tests/apps/context-app/app.py
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/tests/apps/context-app/city.json
--rw-r--r--   0 runner    (1001) docker     (121)     2120 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/tests/apps/context-app/dragonfly_parser.py
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/tests/apps/context-app/lbt_city.json
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-24 18:10:58.000000 pollination-streamlit-io-0.9.2/tests/apps/sync-app/
--rw-r--r--   0 runner    (1001) docker     (121)     2606 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/tests/apps/sync-app/app.py
--rw-r--r--   0 runner    (1001) docker     (121)     1595 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/tests/apps/sync-app/geometry.vtkjs
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-24 18:10:58.000000 pollination-streamlit-io-0.9.2/tests/apps/test-app/
--rw-r--r--   0 runner    (1001) docker     (121)     2748 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/tests/apps/test-app/app.py
--rw-r--r--   0 runner    (1001) docker     (121)       62 2022-01-24 18:09:43.000000 pollination-streamlit-io-0.9.2/tests/requirements.txt
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-24 19:09:43.000000 pollination-streamlit-io-0.9.3/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-24 19:09:43.000000 pollination-streamlit-io-0.9.3/.github/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-24 19:09:43.000000 pollination-streamlit-io-0.9.3/.github/workflows/
+-rw-r--r--   0 runner    (1001) docker     (121)     1070 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/.github/workflows/ci.yaml
+-rw-r--r--   0 runner    (1001) docker     (121)     1912 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/.gitignore
+-rw-r--r--   0 runner    (1001) docker     (121)      252 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/.releaserc.json
+-rw-r--r--   0 runner    (1001) docker     (121)    11357 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (121)      231 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (121)     1051 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/Makefile
+-rw-r--r--   0 runner    (1001) docker     (121)      734 2022-01-24 19:09:43.000000 pollination-streamlit-io-0.9.3/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)     3283 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/README.md
+-rw-r--r--   0 runner    (1001) docker     (121)      165 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/deploy.sh
+-rw-r--r--   0 runner    (1001) docker     (121)      134 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/dev-requirements.txt
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-24 19:09:43.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-24 19:09:43.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/
+-rw-r--r--   0 runner    (1001) docker     (121)     6190 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-24 19:09:43.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/command/
+-rw-r--r--   0 runner    (1001) docker     (121)     1047 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/command/asset-manifest.json
+-rw-r--r--   0 runner    (1001) docker     (121)   197413 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/command/bootstrap.min.css
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-24 19:09:43.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/command/img/
+-rw-r--r--   0 runner    (1001) docker     (121)      683 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/command/img/pollination.png
+-rw-r--r--   0 runner    (1001) docker     (121)     2178 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/command/index.html
+-rw-r--r--   0 runner    (1001) docker     (121)      663 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/command/precache-manifest.0f4233bec0f0ede2fb1ec26c7122dc4e.js
+-rw-r--r--   0 runner    (1001) docker     (121)     1183 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/command/service-worker.js
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-24 19:09:43.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/command/static/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-24 19:09:43.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/command/static/css/
+-rw-r--r--   0 runner    (1001) docker     (121)     1327 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/command/static/css/main.3ccb58d0.chunk.css
+-rw-r--r--   0 runner    (1001) docker     (121)     2796 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/command/static/css/main.3ccb58d0.chunk.css.map
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-24 19:09:43.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/command/static/js/
+-rw-r--r--   0 runner    (1001) docker     (121)   467958 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/command/static/js/2.1408e9e6.chunk.js
+-rw-r--r--   0 runner    (1001) docker     (121)     1653 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/command/static/js/2.1408e9e6.chunk.js.LICENSE.txt
+-rw-r--r--   0 runner    (1001) docker     (121)  1583780 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/command/static/js/2.1408e9e6.chunk.js.map
+-rw-r--r--   0 runner    (1001) docker     (121)     1968 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/command/static/js/main.205cae2d.chunk.js
+-rw-r--r--   0 runner    (1001) docker     (121)     4361 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/command/static/js/main.205cae2d.chunk.js.map
+-rw-r--r--   0 runner    (1001) docker     (121)     1598 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/command/static/js/runtime-main.11ec9aca.js
+-rw-r--r--   0 runner    (1001) docker     (121)     8317 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/command/static/js/runtime-main.11ec9aca.js.map
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-24 19:09:43.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/get/
+-rw-r--r--   0 runner    (1001) docker     (121)     1047 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/get/asset-manifest.json
+-rw-r--r--   0 runner    (1001) docker     (121)   197413 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/get/bootstrap.min.css
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-24 19:09:43.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/get/img/
+-rw-r--r--   0 runner    (1001) docker     (121)      683 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/get/img/pollination.png
+-rw-r--r--   0 runner    (1001) docker     (121)     2178 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/get/index.html
+-rw-r--r--   0 runner    (1001) docker     (121)      663 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/get/precache-manifest.5f91bb71437502227394bca7b31634e0.js
+-rw-r--r--   0 runner    (1001) docker     (121)     1183 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/get/service-worker.js
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-24 19:09:43.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/get/static/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-24 19:09:43.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/get/static/css/
+-rw-r--r--   0 runner    (1001) docker     (121)     1327 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/get/static/css/main.3ccb58d0.chunk.css
+-rw-r--r--   0 runner    (1001) docker     (121)     2796 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/get/static/css/main.3ccb58d0.chunk.css.map
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-24 19:09:43.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/get/static/js/
+-rw-r--r--   0 runner    (1001) docker     (121)   467958 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/get/static/js/2.dc22e782.chunk.js
+-rw-r--r--   0 runner    (1001) docker     (121)     1653 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/get/static/js/2.dc22e782.chunk.js.LICENSE.txt
+-rw-r--r--   0 runner    (1001) docker     (121)  1583770 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/get/static/js/2.dc22e782.chunk.js.map
+-rw-r--r--   0 runner    (1001) docker     (121)     2690 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/get/static/js/main.a7c0ac14.chunk.js
+-rw-r--r--   0 runner    (1001) docker     (121)     6364 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/get/static/js/main.a7c0ac14.chunk.js.map
+-rw-r--r--   0 runner    (1001) docker     (121)     1598 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/get/static/js/runtime-main.11ec9aca.js
+-rw-r--r--   0 runner    (1001) docker     (121)     8317 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/get/static/js/runtime-main.11ec9aca.js.map
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-24 19:09:43.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/send/
+-rw-r--r--   0 runner    (1001) docker     (121)     1047 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/send/asset-manifest.json
+-rw-r--r--   0 runner    (1001) docker     (121)   197413 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/send/bootstrap.min.css
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-24 19:09:43.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/send/img/
+-rw-r--r--   0 runner    (1001) docker     (121)      683 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/send/img/pollination.png
+-rw-r--r--   0 runner    (1001) docker     (121)     2178 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/send/index.html
+-rw-r--r--   0 runner    (1001) docker     (121)      663 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/send/precache-manifest.fa02a73d161599b9272907462ae7a0a0.js
+-rw-r--r--   0 runner    (1001) docker     (121)     1183 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/send/service-worker.js
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-24 19:09:43.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/send/static/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-24 19:09:43.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/send/static/css/
+-rw-r--r--   0 runner    (1001) docker     (121)     1327 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/send/static/css/main.3ccb58d0.chunk.css
+-rw-r--r--   0 runner    (1001) docker     (121)     2796 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/send/static/css/main.3ccb58d0.chunk.css.map
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-24 19:09:43.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/send/static/js/
+-rw-r--r--   0 runner    (1001) docker     (121)   467958 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/send/static/js/2.542a2d66.chunk.js
+-rw-r--r--   0 runner    (1001) docker     (121)     1653 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/send/static/js/2.542a2d66.chunk.js.LICENSE.txt
+-rw-r--r--   0 runner    (1001) docker     (121)  1583780 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/send/static/js/2.542a2d66.chunk.js.map
+-rw-r--r--   0 runner    (1001) docker     (121)     2170 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/send/static/js/main.f34693c1.chunk.js
+-rw-r--r--   0 runner    (1001) docker     (121)     5156 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/send/static/js/main.f34693c1.chunk.js.map
+-rw-r--r--   0 runner    (1001) docker     (121)     1598 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/send/static/js/runtime-main.11ec9aca.js
+-rw-r--r--   0 runner    (1001) docker     (121)     8317 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/send/static/js/runtime-main.11ec9aca.js.map
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-24 19:09:43.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/inputs/
+-rw-r--r--   0 runner    (1001) docker     (121)     2266 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/inputs/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-24 19:09:43.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/inputs/send/
+-rw-r--r--   0 runner    (1001) docker     (121)     1047 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/inputs/send/asset-manifest.json
+-rw-r--r--   0 runner    (1001) docker     (121)   197413 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/inputs/send/bootstrap.min.css
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-24 19:09:43.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/inputs/send/img/
+-rw-r--r--   0 runner    (1001) docker     (121)      683 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/inputs/send/img/pollination.png
+-rw-r--r--   0 runner    (1001) docker     (121)     2178 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/inputs/send/index.html
+-rw-r--r--   0 runner    (1001) docker     (121)      663 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/inputs/send/precache-manifest.8386fb1c8be5d22d126bcefa39298394.js
+-rw-r--r--   0 runner    (1001) docker     (121)     1183 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/inputs/send/service-worker.js
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-24 19:09:43.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/inputs/send/static/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-24 19:09:43.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/inputs/send/static/css/
+-rw-r--r--   0 runner    (1001) docker     (121)     1456 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/inputs/send/static/css/main.96dbfc01.chunk.css
+-rw-r--r--   0 runner    (1001) docker     (121)     2983 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/inputs/send/static/css/main.96dbfc01.chunk.css.map
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-24 19:09:43.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/inputs/send/static/js/
+-rw-r--r--   0 runner    (1001) docker     (121)   467923 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/inputs/send/static/js/2.671b2fa3.chunk.js
+-rw-r--r--   0 runner    (1001) docker     (121)     1653 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/inputs/send/static/js/2.671b2fa3.chunk.js.LICENSE.txt
+-rw-r--r--   0 runner    (1001) docker     (121)  1583770 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/inputs/send/static/js/2.671b2fa3.chunk.js.map
+-rw-r--r--   0 runner    (1001) docker     (121)     2459 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/inputs/send/static/js/main.daad708a.chunk.js
+-rw-r--r--   0 runner    (1001) docker     (121)     6189 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/inputs/send/static/js/main.daad708a.chunk.js.map
+-rw-r--r--   0 runner    (1001) docker     (121)     1598 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/inputs/send/static/js/runtime-main.11ec9aca.js
+-rw-r--r--   0 runner    (1001) docker     (121)     8317 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/inputs/send/static/js/runtime-main.11ec9aca.js.map
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-24 19:09:43.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/special/
+-rw-r--r--   0 runner    (1001) docker     (121)      994 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/special/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-24 19:09:43.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/special/sync/
+-rw-r--r--   0 runner    (1001) docker     (121)      299 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/special/sync/index.html
+-rw-r--r--   0 runner    (1001) docker     (121)     2756 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/special/sync/script.js
+-rw-r--r--   0 runner    (1001) docker     (121)     1764 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io/special/sync/styles.css
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-24 19:09:43.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (121)      734 2022-01-24 19:09:43.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)     5078 2022-01-24 19:09:43.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-01-24 19:09:43.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       17 2022-01-24 19:09:43.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       25 2022-01-24 19:09:43.000000 pollination-streamlit-io-0.9.3/pollination_streamlit_io.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       17 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/requirements.txt
+-rw-r--r--   0 runner    (1001) docker     (121)      102 2022-01-24 19:09:43.000000 pollination-streamlit-io-0.9.3/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (121)     1057 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-24 19:09:43.000000 pollination-streamlit-io-0.9.3/tests/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-24 19:09:43.000000 pollination-streamlit-io-0.9.3/tests/apps/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-24 19:09:43.000000 pollination-streamlit-io-0.9.3/tests/apps/context-app/
+-rw-r--r--   0 runner    (1001) docker     (121)     3153 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/tests/apps/context-app/app.py
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/tests/apps/context-app/city.json
+-rw-r--r--   0 runner    (1001) docker     (121)     2120 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/tests/apps/context-app/dragonfly_parser.py
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/tests/apps/context-app/lbt_city.json
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-24 19:09:43.000000 pollination-streamlit-io-0.9.3/tests/apps/sync-app/
+-rw-r--r--   0 runner    (1001) docker     (121)     2606 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/tests/apps/sync-app/app.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1595 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/tests/apps/sync-app/geometry.vtkjs
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-24 19:09:43.000000 pollination-streamlit-io-0.9.3/tests/apps/test-app/
+-rw-r--r--   0 runner    (1001) docker     (121)     2748 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/tests/apps/test-app/app.py
+-rw-r--r--   0 runner    (1001) docker     (121)       62 2022-01-24 19:08:33.000000 pollination-streamlit-io-0.9.3/tests/requirements.txt
```

### Comparing `pollination-streamlit-io-0.9.2/.github/workflows/ci.yaml` & `pollination-streamlit-io-0.9.3/.github/workflows/ci.yaml`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/.gitignore` & `pollination-streamlit-io-0.9.3/.gitignore`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/LICENSE` & `pollination-streamlit-io-0.9.3/LICENSE`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/Makefile` & `pollination-streamlit-io-0.9.3/Makefile`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/PKG-INFO` & `pollination-streamlit-io-0.9.3/PKG-INFO`

 * *Files 17% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pollination-streamlit-io
-Version: 0.9.2
+Version: 0.9.3
 Summary: Pollination input/output components for Streamlit
 Home-page: https://github.com/pollination/pollination-streamlit-io
 Author: Ladybug Tools
 Author-email: info@ladybug.tools
 License: Apache-2.0 License
 Platform: UNKNOWN
 Classifier: Development Status :: 3 - Alpha
```

### Comparing `pollination-streamlit-io-0.9.2/README.md` & `pollination-streamlit-io-0.9.3/README.md`

 * *Files 8% similar despite different names*

```diff
@@ -4,14 +4,15 @@
 WebView2 technology to interact with the Pollination CAD plugins.
 
 ## Controls
 * button.send = Send a ladybug geometry or a HBjson to Rhino.
 * button.get = Get a ladybug geometry or a HBjson from Rhino.
 * button.command = Run a Rhino command from inside Streamlit.
 * inputs.send = Preview of a ladybug geometry to Rhino.
+* special.sync = Generate a token to use with button.get. A token is generated by the target software and broadcasted to streamlit.
 
 ## UX (for developers)
 It is easy to use.
 
 How to show pollination controls only if platform is Rhino
 
 ### Example of url `https://my-special-app.something?__platform__=Rhino`
@@ -79,13 +80,34 @@
 
 st.subheader("Pollination, Run a Rhino command")
 name_input = st.text_input("Enter the command here!", value="PO_AddRooms")
 command = button.command(commandString=name_input, key="my-secret-key")
 st.write(command)
 ```
 
+### Example of mini-app Rhino > Streamlit with Sync!
+
+```python
+import streamlit as st
+from pollination_streamlit_io import (button,
+    special)
+
+# special controls
+# ONLY ONE FOR APP
+st.subheader('Pollination Token for Sync')
+po_token = special.sync(key="my-po-sync")
+st.write(po_token)
+
+# common controls
+st.subheader('Pollination, Get Geometry Button')
+geometry = button.get(key='my-geometry',
+    syncToken=po_token)
+if geometry:
+    st.write(geometry)
+```
+
 ## Make (for developers)
 Use `make generate-frontend` to create build from react
 
 Use `make copy-build` to copy build from dev folder to the py package
 
 Create a virtual env in tests folder. Install requirements.txt with `pip install -r requirements.txt`. Install the package in dev mode with `pip install -e ../.`
```

### Comparing `pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/__init__.py` & `pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/__init__.py`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/command/asset-manifest.json` & `pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/command/asset-manifest.json`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/command/bootstrap.min.css` & `pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/command/bootstrap.min.css`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/command/img/pollination.png` & `pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/command/img/pollination.png`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/command/index.html` & `pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/command/index.html`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/command/precache-manifest.0f4233bec0f0ede2fb1ec26c7122dc4e.js` & `pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/command/precache-manifest.0f4233bec0f0ede2fb1ec26c7122dc4e.js`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/command/service-worker.js` & `pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/command/service-worker.js`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/command/static/css/main.3ccb58d0.chunk.css` & `pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/command/static/css/main.3ccb58d0.chunk.css`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/command/static/css/main.3ccb58d0.chunk.css.map` & `pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/command/static/css/main.3ccb58d0.chunk.css.map`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/command/static/js/2.1408e9e6.chunk.js` & `pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/command/static/js/2.1408e9e6.chunk.js`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/command/static/js/2.1408e9e6.chunk.js.LICENSE.txt` & `pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/command/static/js/2.1408e9e6.chunk.js.LICENSE.txt`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/command/static/js/2.1408e9e6.chunk.js.map` & `pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/command/static/js/2.1408e9e6.chunk.js.map`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/command/static/js/main.205cae2d.chunk.js` & `pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/command/static/js/main.205cae2d.chunk.js`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/command/static/js/main.205cae2d.chunk.js.map` & `pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/command/static/js/main.205cae2d.chunk.js.map`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/command/static/js/runtime-main.11ec9aca.js` & `pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/command/static/js/runtime-main.11ec9aca.js`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/command/static/js/runtime-main.11ec9aca.js.map` & `pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/command/static/js/runtime-main.11ec9aca.js.map`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/get/asset-manifest.json` & `pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/get/asset-manifest.json`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/get/bootstrap.min.css` & `pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/get/bootstrap.min.css`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/get/img/pollination.png` & `pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/get/img/pollination.png`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/get/index.html` & `pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/get/index.html`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/get/precache-manifest.5f91bb71437502227394bca7b31634e0.js` & `pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/get/precache-manifest.5f91bb71437502227394bca7b31634e0.js`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/get/service-worker.js` & `pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/get/service-worker.js`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/get/static/css/main.3ccb58d0.chunk.css` & `pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/get/static/css/main.3ccb58d0.chunk.css`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/get/static/css/main.3ccb58d0.chunk.css.map` & `pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/get/static/css/main.3ccb58d0.chunk.css.map`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/get/static/js/2.dc22e782.chunk.js` & `pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/get/static/js/2.dc22e782.chunk.js`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/get/static/js/2.dc22e782.chunk.js.LICENSE.txt` & `pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/get/static/js/2.dc22e782.chunk.js.LICENSE.txt`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/get/static/js/2.dc22e782.chunk.js.map` & `pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/get/static/js/2.dc22e782.chunk.js.map`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/get/static/js/main.a7c0ac14.chunk.js` & `pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/get/static/js/main.a7c0ac14.chunk.js`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/get/static/js/main.a7c0ac14.chunk.js.map` & `pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/get/static/js/main.a7c0ac14.chunk.js.map`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/get/static/js/runtime-main.11ec9aca.js` & `pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/get/static/js/runtime-main.11ec9aca.js`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/get/static/js/runtime-main.11ec9aca.js.map` & `pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/get/static/js/runtime-main.11ec9aca.js.map`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/send/asset-manifest.json` & `pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/send/asset-manifest.json`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/send/bootstrap.min.css` & `pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/send/bootstrap.min.css`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/send/img/pollination.png` & `pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/send/img/pollination.png`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/send/index.html` & `pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/send/index.html`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/send/precache-manifest.fa02a73d161599b9272907462ae7a0a0.js` & `pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/send/precache-manifest.fa02a73d161599b9272907462ae7a0a0.js`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/send/service-worker.js` & `pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/send/service-worker.js`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/send/static/css/main.3ccb58d0.chunk.css` & `pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/send/static/css/main.3ccb58d0.chunk.css`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/send/static/css/main.3ccb58d0.chunk.css.map` & `pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/send/static/css/main.3ccb58d0.chunk.css.map`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/send/static/js/2.542a2d66.chunk.js` & `pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/send/static/js/2.542a2d66.chunk.js`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/send/static/js/2.542a2d66.chunk.js.LICENSE.txt` & `pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/send/static/js/2.542a2d66.chunk.js.LICENSE.txt`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/send/static/js/2.542a2d66.chunk.js.map` & `pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/send/static/js/2.542a2d66.chunk.js.map`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/send/static/js/main.f34693c1.chunk.js` & `pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/send/static/js/main.f34693c1.chunk.js`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/send/static/js/main.f34693c1.chunk.js.map` & `pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/send/static/js/main.f34693c1.chunk.js.map`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/send/static/js/runtime-main.11ec9aca.js` & `pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/send/static/js/runtime-main.11ec9aca.js`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/pollination_streamlit_io/button/send/static/js/runtime-main.11ec9aca.js.map` & `pollination-streamlit-io-0.9.3/pollination_streamlit_io/button/send/static/js/runtime-main.11ec9aca.js.map`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/pollination_streamlit_io/inputs/__init__.py` & `pollination-streamlit-io-0.9.3/pollination_streamlit_io/inputs/__init__.py`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/pollination_streamlit_io/inputs/send/asset-manifest.json` & `pollination-streamlit-io-0.9.3/pollination_streamlit_io/inputs/send/asset-manifest.json`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/pollination_streamlit_io/inputs/send/bootstrap.min.css` & `pollination-streamlit-io-0.9.3/pollination_streamlit_io/inputs/send/bootstrap.min.css`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/pollination_streamlit_io/inputs/send/img/pollination.png` & `pollination-streamlit-io-0.9.3/pollination_streamlit_io/inputs/send/img/pollination.png`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/pollination_streamlit_io/inputs/send/index.html` & `pollination-streamlit-io-0.9.3/pollination_streamlit_io/inputs/send/index.html`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/pollination_streamlit_io/inputs/send/precache-manifest.8386fb1c8be5d22d126bcefa39298394.js` & `pollination-streamlit-io-0.9.3/pollination_streamlit_io/inputs/send/precache-manifest.8386fb1c8be5d22d126bcefa39298394.js`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/pollination_streamlit_io/inputs/send/service-worker.js` & `pollination-streamlit-io-0.9.3/pollination_streamlit_io/inputs/send/service-worker.js`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/pollination_streamlit_io/inputs/send/static/css/main.96dbfc01.chunk.css` & `pollination-streamlit-io-0.9.3/pollination_streamlit_io/inputs/send/static/css/main.96dbfc01.chunk.css`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/pollination_streamlit_io/inputs/send/static/css/main.96dbfc01.chunk.css.map` & `pollination-streamlit-io-0.9.3/pollination_streamlit_io/inputs/send/static/css/main.96dbfc01.chunk.css.map`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/pollination_streamlit_io/inputs/send/static/js/2.671b2fa3.chunk.js` & `pollination-streamlit-io-0.9.3/pollination_streamlit_io/inputs/send/static/js/2.671b2fa3.chunk.js`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/pollination_streamlit_io/inputs/send/static/js/2.671b2fa3.chunk.js.LICENSE.txt` & `pollination-streamlit-io-0.9.3/pollination_streamlit_io/inputs/send/static/js/2.671b2fa3.chunk.js.LICENSE.txt`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/pollination_streamlit_io/inputs/send/static/js/2.671b2fa3.chunk.js.map` & `pollination-streamlit-io-0.9.3/pollination_streamlit_io/inputs/send/static/js/2.671b2fa3.chunk.js.map`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/pollination_streamlit_io/inputs/send/static/js/main.daad708a.chunk.js` & `pollination-streamlit-io-0.9.3/pollination_streamlit_io/inputs/send/static/js/main.daad708a.chunk.js`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/pollination_streamlit_io/inputs/send/static/js/main.daad708a.chunk.js.map` & `pollination-streamlit-io-0.9.3/pollination_streamlit_io/inputs/send/static/js/main.daad708a.chunk.js.map`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/pollination_streamlit_io/inputs/send/static/js/runtime-main.11ec9aca.js` & `pollination-streamlit-io-0.9.3/pollination_streamlit_io/inputs/send/static/js/runtime-main.11ec9aca.js`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/pollination_streamlit_io/inputs/send/static/js/runtime-main.11ec9aca.js.map` & `pollination-streamlit-io-0.9.3/pollination_streamlit_io/inputs/send/static/js/runtime-main.11ec9aca.js.map`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/pollination_streamlit_io/special/__init__.py` & `pollination-streamlit-io-0.9.3/pollination_streamlit_io/special/__init__.py`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/pollination_streamlit_io/special/sync/script.js` & `pollination-streamlit-io-0.9.3/pollination_streamlit_io/special/sync/script.js`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/pollination_streamlit_io/special/sync/styles.css` & `pollination-streamlit-io-0.9.3/pollination_streamlit_io/special/sync/styles.css`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/pollination_streamlit_io.egg-info/PKG-INFO` & `pollination-streamlit-io-0.9.3/pollination_streamlit_io.egg-info/PKG-INFO`

 * *Files 17% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pollination-streamlit-io
-Version: 0.9.2
+Version: 0.9.3
 Summary: Pollination input/output components for Streamlit
 Home-page: https://github.com/pollination/pollination-streamlit-io
 Author: Ladybug Tools
 Author-email: info@ladybug.tools
 License: Apache-2.0 License
 Platform: UNKNOWN
 Classifier: Development Status :: 3 - Alpha
```

### Comparing `pollination-streamlit-io-0.9.2/pollination_streamlit_io.egg-info/SOURCES.txt` & `pollination-streamlit-io-0.9.3/pollination_streamlit_io.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/setup.py` & `pollination-streamlit-io-0.9.3/setup.py`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/tests/apps/context-app/app.py` & `pollination-streamlit-io-0.9.3/tests/apps/context-app/app.py`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/tests/apps/context-app/dragonfly_parser.py` & `pollination-streamlit-io-0.9.3/tests/apps/context-app/dragonfly_parser.py`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/tests/apps/sync-app/app.py` & `pollination-streamlit-io-0.9.3/tests/apps/sync-app/app.py`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/tests/apps/sync-app/geometry.vtkjs` & `pollination-streamlit-io-0.9.3/tests/apps/sync-app/geometry.vtkjs`

 * *Files identical despite different names*

### Comparing `pollination-streamlit-io-0.9.2/tests/apps/test-app/app.py` & `pollination-streamlit-io-0.9.3/tests/apps/test-app/app.py`

 * *Files identical despite different names*

