# Comparing `tmp/Pandora-ChatGPT-0.9.7.tar.gz` & `tmp/Pandora-ChatGPT-0.9.8.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "/home/runner/work/pandora/pandora/dist/.tmp-phys8hh7/Pandora-ChatGPT-0.9.7.tar", last modified: Mon Apr  3 02:15:29 2023, max compression
+gzip compressed data, was "/home/runner/work/pandora/pandora/dist/.tmp-bs0v6jo9/Pandora-ChatGPT-0.9.8.tar", last modified: Thu Apr  6 11:21:05 2023, max compression
```

## Comparing `Pandora-ChatGPT-0.9.7.tar` & `Pandora-ChatGPT-0.9.8.tar`

### file list

```diff
@@ -1,115 +1,115 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 02:15:29.000000 Pandora-ChatGPT-0.9.7/
--rw-r--r--   0 runner    (1001) docker     (123)    18092 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)      172 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     9188 2023-04-03 02:15:29.000000 Pandora-ChatGPT-0.9.7/PKG-INFO
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 02:15:29.000000 Pandora-ChatGPT-0.9.7/Pandora_ChatGPT.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     9188 2023-04-03 02:15:29.000000 Pandora-ChatGPT-0.9.7/Pandora_ChatGPT.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     4219 2023-04-03 02:15:29.000000 Pandora-ChatGPT-0.9.7/Pandora_ChatGPT.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-03 02:15:29.000000 Pandora-ChatGPT-0.9.7/Pandora_ChatGPT.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       92 2023-04-03 02:15:29.000000 Pandora-ChatGPT-0.9.7/Pandora_ChatGPT.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (123)      353 2023-04-03 02:15:29.000000 Pandora-ChatGPT-0.9.7/Pandora_ChatGPT.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        8 2023-04-03 02:15:29.000000 Pandora-ChatGPT-0.9.7/Pandora_ChatGPT.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)     7681 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/README.md
--rw-r--r--   0 runner    (1001) docker     (123)      249 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/requirements.txt
--rw-r--r--   0 runner    (1001) docker     (123)       64 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/requirements_api.txt
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-03 02:15:29.000000 Pandora-ChatGPT-0.9.7/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     2384 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 02:15:29.000000 Pandora-ChatGPT-0.9.7/src/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 02:15:29.000000 Pandora-ChatGPT-0.9.7/src/pandora/
--rw-r--r--   0 runner    (1001) docker     (123)       47 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      101 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/__main__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 02:15:29.000000 Pandora-ChatGPT-0.9.7/src/pandora/bots/
--rw-r--r--   0 runner    (1001) docker     (123)       24 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/bots/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    15216 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/bots/legacy.py
--rw-r--r--   0 runner    (1001) docker     (123)     9394 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/bots/server.py
--rw-r--r--   0 runner    (1001) docker     (123)     2115 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/cloud_launcher.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 02:15:29.000000 Pandora-ChatGPT-0.9.7/src/pandora/exts/
--rw-r--r--   0 runner    (1001) docker     (123)       24 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/exts/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      342 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/exts/config.py
--rw-r--r--   0 runner    (1001) docker     (123)      929 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/exts/hooks.py
--rw-r--r--   0 runner    (1001) docker     (123)      476 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/exts/sentry.py
--rw-r--r--   0 runner    (1001) docker     (123)     1530 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/exts/token.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 02:15:29.000000 Pandora-ChatGPT-0.9.7/src/pandora/flask/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 02:15:29.000000 Pandora-ChatGPT-0.9.7/src/pandora/flask/static/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 02:15:29.000000 Pandora-ChatGPT-0.9.7/src/pandora/flask/static/_next/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 02:15:29.000000 Pandora-ChatGPT-0.9.7/src/pandora/flask/static/_next/static/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 02:15:29.000000 Pandora-ChatGPT-0.9.7/src/pandora/flask/static/_next/static/chunks/
--rw-r--r--   0 runner    (1001) docker     (123)   905448 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/flask/static/_next/static/chunks/113-23682f80a24dd00d.js
--rw-r--r--   0 runner    (1001) docker     (123)    14115 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/flask/static/_next/static/chunks/14-0cb0d20affbd720d.js
--rw-r--r--   0 runner    (1001) docker     (123)     9531 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/flask/static/_next/static/chunks/174-bd28069f281ef76f.js
--rw-r--r--   0 runner    (1001) docker     (123)   264961 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/flask/static/_next/static/chunks/1f110208-44a6f43ddc5e9011.js
--rw-r--r--   0 runner    (1001) docker     (123)    13147 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/flask/static/_next/static/chunks/264-13e92c51b0315184.js
--rw-r--r--   0 runner    (1001) docker     (123)    24138 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/flask/static/_next/static/chunks/360-442b869f1ba4bb1b.js
--rw-r--r--   0 runner    (1001) docker     (123)    20480 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/flask/static/_next/static/chunks/424-d1d3bfe6a3ca6c4a.js
--rw-r--r--   0 runner    (1001) docker     (123)     3232 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/flask/static/_next/static/chunks/554.9b8bfd0762461d74.js
--rw-r--r--   0 runner    (1001) docker     (123)      389 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/flask/static/_next/static/chunks/68a27ff6-1185184b61bc22d0.js
--rw-r--r--   0 runner    (1001) docker     (123)    11674 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/flask/static/_next/static/chunks/762-222df1028c0c1555.js
--rw-r--r--   0 runner    (1001) docker     (123)     2433 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/flask/static/_next/static/chunks/949.1a6eb804b5e91f61.js
--rw-r--r--   0 runner    (1001) docker     (123)      462 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/flask/static/_next/static/chunks/bd26816a-981e1ddc27b37cc6.js
--rw-r--r--   0 runner    (1001) docker     (123)   141370 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/flask/static/_next/static/chunks/framework-7a789ee31d2a7534.js
--rw-r--r--   0 runner    (1001) docker     (123)   105264 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/flask/static/_next/static/chunks/main-149b337e061b4d04.js
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 02:15:29.000000 Pandora-ChatGPT-0.9.7/src/pandora/flask/static/_next/static/chunks/pages/
--rw-r--r--   0 runner    (1001) docker     (123)   305755 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/flask/static/_next/static/chunks/pages/_app-aaa11de1926dcafe.js
--rw-r--r--   0 runner    (1001) docker     (123)      250 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/flask/static/_next/static/chunks/pages/_error-786d27d84962122a.js
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 02:15:29.000000 Pandora-ChatGPT-0.9.7/src/pandora/flask/static/_next/static/chunks/pages/chat/
--rw-r--r--   0 runner    (1001) docker     (123)   149531 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/flask/static/_next/static/chunks/pages/chat/[[...chatId]]-76751174916fa3f7.js
--rw-r--r--   0 runner    (1001) docker     (123)    91460 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/flask/static/_next/static/chunks/polyfills-c67a75d1b6f99dc8.js
--rw-r--r--   0 runner    (1001) docker     (123)     3926 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/flask/static/_next/static/chunks/webpack-c9a868e8e0796ec6.js
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 02:15:29.000000 Pandora-ChatGPT-0.9.7/src/pandora/flask/static/_next/static/css/
--rw-r--r--   0 runner    (1001) docker     (123)   108647 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/flask/static/_next/static/css/ac221fb2caad35a6.css
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 02:15:29.000000 Pandora-ChatGPT-0.9.7/src/pandora/flask/static/_next/static/olf4sv64FWIcQ_zCGl90t/
--rw-r--r--   0 runner    (1001) docker     (123)     2308 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/flask/static/_next/static/olf4sv64FWIcQ_zCGl90t/_buildManifest.js
--rw-r--r--   0 runner    (1001) docker     (123)       77 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/flask/static/_next/static/olf4sv64FWIcQ_zCGl90t/_ssgManifest.js
--rw-r--r--   0 runner    (1001) docker     (123)     4159 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/flask/static/apple-touch-icon.png
--rw-r--r--   0 runner    (1001) docker     (123)      730 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/flask/static/favicon-16x16.png
--rw-r--r--   0 runner    (1001) docker     (123)     1292 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/flask/static/favicon-32x32.png
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 02:15:29.000000 Pandora-ChatGPT-0.9.7/src/pandora/flask/static/fonts/
--rw-r--r--   0 runner    (1001) docker     (123)     7716 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/flask/static/fonts/KaTeX_Caligraphic-Bold.woff
--rw-r--r--   0 runner    (1001) docker     (123)     7656 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/flask/static/fonts/KaTeX_Caligraphic-Regular.woff
--rw-r--r--   0 runner    (1001) docker     (123)    13296 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/flask/static/fonts/KaTeX_Fraktur-Bold.woff
--rw-r--r--   0 runner    (1001) docker     (123)    13208 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/flask/static/fonts/KaTeX_Fraktur-Regular.woff
--rw-r--r--   0 runner    (1001) docker     (123)    29912 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/flask/static/fonts/KaTeX_Main-Bold.woff
--rw-r--r--   0 runner    (1001) docker     (123)    19412 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/flask/static/fonts/KaTeX_Main-BoldItalic.woff
--rw-r--r--   0 runner    (1001) docker     (123)    19676 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/flask/static/fonts/KaTeX_Main-Italic.woff
--rw-r--r--   0 runner    (1001) docker     (123)    30772 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/flask/static/fonts/KaTeX_Main-Regular.woff
--rw-r--r--   0 runner    (1001) docker     (123)    18668 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/flask/static/fonts/KaTeX_Math-BoldItalic.woff
--rw-r--r--   0 runner    (1001) docker     (123)    18748 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/flask/static/fonts/KaTeX_Math-Italic.woff
--rw-r--r--   0 runner    (1001) docker     (123)    14408 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/flask/static/fonts/KaTeX_SansSerif-Bold.woff
--rw-r--r--   0 runner    (1001) docker     (123)    14112 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/flask/static/fonts/KaTeX_SansSerif-Italic.woff
--rw-r--r--   0 runner    (1001) docker     (123)    12316 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/flask/static/fonts/KaTeX_SansSerif-Regular.woff
--rw-r--r--   0 runner    (1001) docker     (123)    10588 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/flask/static/fonts/KaTeX_Script-Regular.woff
--rw-r--r--   0 runner    (1001) docker     (123)     6496 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/flask/static/fonts/KaTeX_Size1-Regular.woff
--rw-r--r--   0 runner    (1001) docker     (123)     6188 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/flask/static/fonts/KaTeX_Size2-Regular.woff
--rw-r--r--   0 runner    (1001) docker     (123)     4420 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/flask/static/fonts/KaTeX_Size3-Regular.woff
--rw-r--r--   0 runner    (1001) docker     (123)     5980 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/flask/static/fonts/KaTeX_Size4-Regular.woff
--rw-r--r--   0 runner    (1001) docker     (123)    16028 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/flask/static/fonts/KaTeX_Typewriter-Regular.woff
--rw-r--r--   0 runner    (1001) docker     (123)   324208 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/flask/static/fonts/Signifier-Regular.otf
--rw-r--r--   0 runner    (1001) docker     (123)   210840 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/flask/static/fonts/Sohne-Buch.otf
--rw-r--r--   0 runner    (1001) docker     (123)   230012 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/flask/static/fonts/Sohne-Halbfett.otf
--rw-r--r--   0 runner    (1001) docker     (123)    30824 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/flask/static/fonts/SohneMono-Buch.otf
--rw-r--r--   0 runner    (1001) docker     (123)    31116 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/flask/static/fonts/SohneMono-Halbfett.otf
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 02:15:29.000000 Pandora-ChatGPT-0.9.7/src/pandora/flask/static/images/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 02:15:29.000000 Pandora-ChatGPT-0.9.7/src/pandora/flask/static/images/2022/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 02:15:29.000000 Pandora-ChatGPT-0.9.7/src/pandora/flask/static/images/2022/11/
--rw-r--r--   0 runner    (1001) docker     (123)     1707 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/flask/static/images/2022/11/ChatGPT.jpg
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 02:15:29.000000 Pandora-ChatGPT-0.9.7/src/pandora/flask/templates/
--rw-r--r--   0 runner    (1001) docker     (123)     8720 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/flask/templates/chat.html
--rw-r--r--   0 runner    (1001) docker     (123)     6209 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/launcher.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 02:15:29.000000 Pandora-ChatGPT-0.9.7/src/pandora/migrations/
--rw-r--r--   0 runner    (1001) docker     (123)       24 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/migrations/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      250 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/migrations/database.py
--rw-r--r--   0 runner    (1001) docker     (123)      619 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/migrations/migrate.py
--rw-r--r--   0 runner    (1001) docker     (123)     4153 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/migrations/models.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 02:15:29.000000 Pandora-ChatGPT-0.9.7/src/pandora/migrations/scripts/
--rw-r--r--   0 runner    (1001) docker     (123)      869 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/migrations/scripts/20230308_01_7ctOr.sql
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 02:15:29.000000 Pandora-ChatGPT-0.9.7/src/pandora/openai/
--rw-r--r--   0 runner    (1001) docker     (123)       24 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/openai/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    10681 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/openai/api.py
--rw-r--r--   0 runner    (1001) docker     (123)     6071 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/openai/auth.py
--rw-r--r--   0 runner    (1001) docker     (123)      421 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/openai/token.py
--rw-r--r--   0 runner    (1001) docker     (123)     3420 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/openai/utils.py
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/py.typed
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 02:15:29.000000 Pandora-ChatGPT-0.9.7/src/pandora/turbo/
--rw-r--r--   0 runner    (1001) docker     (123)       24 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/turbo/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     6263 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/turbo/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     9789 2023-04-03 02:15:16.000000 Pandora-ChatGPT-0.9.7/src/pandora/turbo/chat.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:21:05.000000 Pandora-ChatGPT-0.9.8/
+-rw-r--r--   0 runner    (1001) docker     (123)    18092 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)      172 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)    10207 2023-04-06 11:21:05.000000 Pandora-ChatGPT-0.9.8/PKG-INFO
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:21:05.000000 Pandora-ChatGPT-0.9.8/Pandora_ChatGPT.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)    10207 2023-04-06 11:21:05.000000 Pandora-ChatGPT-0.9.8/Pandora_ChatGPT.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     4219 2023-04-06 11:21:05.000000 Pandora-ChatGPT-0.9.8/Pandora_ChatGPT.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 11:21:05.000000 Pandora-ChatGPT-0.9.8/Pandora_ChatGPT.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       92 2023-04-06 11:21:05.000000 Pandora-ChatGPT-0.9.8/Pandora_ChatGPT.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      353 2023-04-06 11:21:05.000000 Pandora-ChatGPT-0.9.8/Pandora_ChatGPT.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        8 2023-04-06 11:21:05.000000 Pandora-ChatGPT-0.9.8/Pandora_ChatGPT.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     8700 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)      249 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/requirements.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       64 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/requirements_api.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 11:21:05.000000 Pandora-ChatGPT-0.9.8/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     2384 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:21:05.000000 Pandora-ChatGPT-0.9.8/src/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:21:05.000000 Pandora-ChatGPT-0.9.8/src/pandora/
+-rw-r--r--   0 runner    (1001) docker     (123)       47 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      101 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/__main__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:21:05.000000 Pandora-ChatGPT-0.9.8/src/pandora/bots/
+-rw-r--r--   0 runner    (1001) docker     (123)       24 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/bots/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15216 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/bots/legacy.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9394 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/bots/server.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2115 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/cloud_launcher.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:21:05.000000 Pandora-ChatGPT-0.9.8/src/pandora/exts/
+-rw-r--r--   0 runner    (1001) docker     (123)       24 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/exts/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      342 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/exts/config.py
+-rw-r--r--   0 runner    (1001) docker     (123)      929 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/exts/hooks.py
+-rw-r--r--   0 runner    (1001) docker     (123)      476 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/exts/sentry.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1530 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/exts/token.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:21:05.000000 Pandora-ChatGPT-0.9.8/src/pandora/flask/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:21:05.000000 Pandora-ChatGPT-0.9.8/src/pandora/flask/static/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:21:05.000000 Pandora-ChatGPT-0.9.8/src/pandora/flask/static/_next/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:21:05.000000 Pandora-ChatGPT-0.9.8/src/pandora/flask/static/_next/static/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:21:05.000000 Pandora-ChatGPT-0.9.8/src/pandora/flask/static/_next/static/chunks/
+-rw-r--r--   0 runner    (1001) docker     (123)   905448 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/flask/static/_next/static/chunks/113-23682f80a24dd00d.js
+-rw-r--r--   0 runner    (1001) docker     (123)    14115 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/flask/static/_next/static/chunks/14-0cb0d20affbd720d.js
+-rw-r--r--   0 runner    (1001) docker     (123)     9531 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/flask/static/_next/static/chunks/174-bd28069f281ef76f.js
+-rw-r--r--   0 runner    (1001) docker     (123)   264961 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/flask/static/_next/static/chunks/1f110208-44a6f43ddc5e9011.js
+-rw-r--r--   0 runner    (1001) docker     (123)    13147 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/flask/static/_next/static/chunks/264-13e92c51b0315184.js
+-rw-r--r--   0 runner    (1001) docker     (123)    24138 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/flask/static/_next/static/chunks/360-442b869f1ba4bb1b.js
+-rw-r--r--   0 runner    (1001) docker     (123)    20480 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/flask/static/_next/static/chunks/424-d1d3bfe6a3ca6c4a.js
+-rw-r--r--   0 runner    (1001) docker     (123)     3232 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/flask/static/_next/static/chunks/554.9b8bfd0762461d74.js
+-rw-r--r--   0 runner    (1001) docker     (123)      389 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/flask/static/_next/static/chunks/68a27ff6-1185184b61bc22d0.js
+-rw-r--r--   0 runner    (1001) docker     (123)    11674 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/flask/static/_next/static/chunks/762-222df1028c0c1555.js
+-rw-r--r--   0 runner    (1001) docker     (123)     2433 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/flask/static/_next/static/chunks/949.1a6eb804b5e91f61.js
+-rw-r--r--   0 runner    (1001) docker     (123)      462 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/flask/static/_next/static/chunks/bd26816a-981e1ddc27b37cc6.js
+-rw-r--r--   0 runner    (1001) docker     (123)   141370 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/flask/static/_next/static/chunks/framework-7a789ee31d2a7534.js
+-rw-r--r--   0 runner    (1001) docker     (123)   105264 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/flask/static/_next/static/chunks/main-149b337e061b4d04.js
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:21:05.000000 Pandora-ChatGPT-0.9.8/src/pandora/flask/static/_next/static/chunks/pages/
+-rw-r--r--   0 runner    (1001) docker     (123)   305755 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/flask/static/_next/static/chunks/pages/_app-aaa11de1926dcafe.js
+-rw-r--r--   0 runner    (1001) docker     (123)      250 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/flask/static/_next/static/chunks/pages/_error-786d27d84962122a.js
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:21:05.000000 Pandora-ChatGPT-0.9.8/src/pandora/flask/static/_next/static/chunks/pages/chat/
+-rw-r--r--   0 runner    (1001) docker     (123)   149531 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/flask/static/_next/static/chunks/pages/chat/[[...chatId]]-76751174916fa3f7.js
+-rw-r--r--   0 runner    (1001) docker     (123)    91460 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/flask/static/_next/static/chunks/polyfills-c67a75d1b6f99dc8.js
+-rw-r--r--   0 runner    (1001) docker     (123)     3926 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/flask/static/_next/static/chunks/webpack-c9a868e8e0796ec6.js
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:21:05.000000 Pandora-ChatGPT-0.9.8/src/pandora/flask/static/_next/static/css/
+-rw-r--r--   0 runner    (1001) docker     (123)   108647 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/flask/static/_next/static/css/ac221fb2caad35a6.css
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:21:05.000000 Pandora-ChatGPT-0.9.8/src/pandora/flask/static/_next/static/olf4sv64FWIcQ_zCGl90t/
+-rw-r--r--   0 runner    (1001) docker     (123)     2308 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/flask/static/_next/static/olf4sv64FWIcQ_zCGl90t/_buildManifest.js
+-rw-r--r--   0 runner    (1001) docker     (123)       77 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/flask/static/_next/static/olf4sv64FWIcQ_zCGl90t/_ssgManifest.js
+-rw-r--r--   0 runner    (1001) docker     (123)     4159 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/flask/static/apple-touch-icon.png
+-rw-r--r--   0 runner    (1001) docker     (123)      730 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/flask/static/favicon-16x16.png
+-rw-r--r--   0 runner    (1001) docker     (123)     1292 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/flask/static/favicon-32x32.png
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:21:05.000000 Pandora-ChatGPT-0.9.8/src/pandora/flask/static/fonts/
+-rw-r--r--   0 runner    (1001) docker     (123)     7716 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/flask/static/fonts/KaTeX_Caligraphic-Bold.woff
+-rw-r--r--   0 runner    (1001) docker     (123)     7656 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/flask/static/fonts/KaTeX_Caligraphic-Regular.woff
+-rw-r--r--   0 runner    (1001) docker     (123)    13296 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/flask/static/fonts/KaTeX_Fraktur-Bold.woff
+-rw-r--r--   0 runner    (1001) docker     (123)    13208 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/flask/static/fonts/KaTeX_Fraktur-Regular.woff
+-rw-r--r--   0 runner    (1001) docker     (123)    29912 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/flask/static/fonts/KaTeX_Main-Bold.woff
+-rw-r--r--   0 runner    (1001) docker     (123)    19412 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/flask/static/fonts/KaTeX_Main-BoldItalic.woff
+-rw-r--r--   0 runner    (1001) docker     (123)    19676 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/flask/static/fonts/KaTeX_Main-Italic.woff
+-rw-r--r--   0 runner    (1001) docker     (123)    30772 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/flask/static/fonts/KaTeX_Main-Regular.woff
+-rw-r--r--   0 runner    (1001) docker     (123)    18668 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/flask/static/fonts/KaTeX_Math-BoldItalic.woff
+-rw-r--r--   0 runner    (1001) docker     (123)    18748 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/flask/static/fonts/KaTeX_Math-Italic.woff
+-rw-r--r--   0 runner    (1001) docker     (123)    14408 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/flask/static/fonts/KaTeX_SansSerif-Bold.woff
+-rw-r--r--   0 runner    (1001) docker     (123)    14112 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/flask/static/fonts/KaTeX_SansSerif-Italic.woff
+-rw-r--r--   0 runner    (1001) docker     (123)    12316 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/flask/static/fonts/KaTeX_SansSerif-Regular.woff
+-rw-r--r--   0 runner    (1001) docker     (123)    10588 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/flask/static/fonts/KaTeX_Script-Regular.woff
+-rw-r--r--   0 runner    (1001) docker     (123)     6496 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/flask/static/fonts/KaTeX_Size1-Regular.woff
+-rw-r--r--   0 runner    (1001) docker     (123)     6188 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/flask/static/fonts/KaTeX_Size2-Regular.woff
+-rw-r--r--   0 runner    (1001) docker     (123)     4420 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/flask/static/fonts/KaTeX_Size3-Regular.woff
+-rw-r--r--   0 runner    (1001) docker     (123)     5980 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/flask/static/fonts/KaTeX_Size4-Regular.woff
+-rw-r--r--   0 runner    (1001) docker     (123)    16028 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/flask/static/fonts/KaTeX_Typewriter-Regular.woff
+-rw-r--r--   0 runner    (1001) docker     (123)   324208 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/flask/static/fonts/Signifier-Regular.otf
+-rw-r--r--   0 runner    (1001) docker     (123)   210840 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/flask/static/fonts/Sohne-Buch.otf
+-rw-r--r--   0 runner    (1001) docker     (123)   230012 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/flask/static/fonts/Sohne-Halbfett.otf
+-rw-r--r--   0 runner    (1001) docker     (123)    30824 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/flask/static/fonts/SohneMono-Buch.otf
+-rw-r--r--   0 runner    (1001) docker     (123)    31116 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/flask/static/fonts/SohneMono-Halbfett.otf
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:21:05.000000 Pandora-ChatGPT-0.9.8/src/pandora/flask/static/images/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:21:05.000000 Pandora-ChatGPT-0.9.8/src/pandora/flask/static/images/2022/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:21:05.000000 Pandora-ChatGPT-0.9.8/src/pandora/flask/static/images/2022/11/
+-rw-r--r--   0 runner    (1001) docker     (123)     1707 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/flask/static/images/2022/11/ChatGPT.jpg
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:21:05.000000 Pandora-ChatGPT-0.9.8/src/pandora/flask/templates/
+-rw-r--r--   0 runner    (1001) docker     (123)     8720 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/flask/templates/chat.html
+-rw-r--r--   0 runner    (1001) docker     (123)     6382 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/launcher.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:21:05.000000 Pandora-ChatGPT-0.9.8/src/pandora/migrations/
+-rw-r--r--   0 runner    (1001) docker     (123)       24 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/migrations/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      250 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/migrations/database.py
+-rw-r--r--   0 runner    (1001) docker     (123)      619 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/migrations/migrate.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4153 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/migrations/models.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:21:05.000000 Pandora-ChatGPT-0.9.8/src/pandora/migrations/scripts/
+-rw-r--r--   0 runner    (1001) docker     (123)      869 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/migrations/scripts/20230308_01_7ctOr.sql
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:21:05.000000 Pandora-ChatGPT-0.9.8/src/pandora/openai/
+-rw-r--r--   0 runner    (1001) docker     (123)       24 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/openai/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10781 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/openai/api.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6184 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/openai/auth.py
+-rw-r--r--   0 runner    (1001) docker     (123)      421 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/openai/token.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3420 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/openai/utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/py.typed
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:21:05.000000 Pandora-ChatGPT-0.9.8/src/pandora/turbo/
+-rw-r--r--   0 runner    (1001) docker     (123)       24 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/turbo/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6263 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/turbo/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9789 2023-04-06 11:20:50.000000 Pandora-ChatGPT-0.9.8/src/pandora/turbo/chat.py
```

### Comparing `Pandora-ChatGPT-0.9.7/LICENSE` & `Pandora-ChatGPT-0.9.8/LICENSE`

 * *Files identical despite different names*

### Comparing `Pandora-ChatGPT-0.9.7/PKG-INFO` & `Pandora-ChatGPT-0.9.8/PKG-INFO`

 * *Files 6% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: Pandora-ChatGPT
-Version: 0.9.7
+Version: 0.9.8
 Summary: A command-line interface to ChatGPT
 Home-page: https://github.com/pengzhile/pandora
 Author: Neo Peng
 Author-email: pengzhile@gmail.com
 Project-URL: Source, https://github.com/pengzhile/pandora
 Project-URL: Tracker, https://github.com/pengzhile/pandora/issues
 Keywords: OpenAI ChatGPT ChatGPT-Plus gpt-3.5-turbo gpt-3.5-turbo-0301
@@ -191,14 +191,15 @@
 * `/version` 打印`Pandora`的版本信息。
 * `/exit` 退出`潘多拉`。
 
 ## 高阶设置
 
 * 本部分内容不理解的朋友，**请勿擅动！**
 * 环境变量 `OPENAI_API_PREFIX` 可以替换OpenAI Api的前缀`https://api.openai.com`。
+* 环境变量 `CHATGPT_API_PREFIX` 可以替换ChatGPT Api的前缀`https://chat.gateway.do`。
 * 如果你想持久存储`Docker`中`Pandora`产生的数据，你可以挂载宿主机目录至`/data`。
 * 如果你在国内使用`pip`安装缓慢，可以考虑切换至腾讯的源：```pip config set global.index-url https://mirrors.cloud.tencent.com/pypi/simple```
 * 镜像同步版本可能不及时，如果出现这种情况建议切换至官方源：```pip config set global.index-url https://pypi.org/simple```
 * 默认使用`sqlite3`存储会话数据，如果你希望更换至`mysql`，可以这么做：
   * 执行```pip install PyMySQL```安装驱动。
   * 设置环境变量：`DATABASE_URI`为类似`mysql+pymysql://user:pass@localhost/dbname`的连接字符串。
 * 环境变量指定`OPENAI_EMAIL`可以替代登录输入用户名，`OPENAI_PASSWORD`则可以替代输入密码。
@@ -206,14 +207,33 @@
 ## Cloud模式
 
 * 搭建一个跟官方很像的`ChatGPT`服务，不能说很像，只能说一样。
 * 该模式使用`pandora-cloud`启动，前提是你如前面所说安装好了。
 * Docker环境变量：`PANDORA_CLOUD` 启动`cloud`模式。
 * 该模式参数含义与普通模式相同，可`--help`查看。
 
+## 使用Cloudflare Workers代理
+
+* 如果你感觉默认的`https://chat.gateway.do`在你那里可能被墙了，可以使用如下方法自行代理。
+* 你需要一个`Cloudflare`账号，如果没有，可以[注册](https://dash.cloudflare.com/sign-up)一个。
+* 登录后，点击`Workers`，然后点击`Create a Worker`，填入服务名称后点击`创建服务`。
+* 点开你刚才创建的服务，点击`快速编辑`按钮，贴入下面的代码，然后点击`保存并部署`。
+  ```javascript
+  export default {
+    async fetch(request, env) {
+      const url = new URL(request.url);
+      url.host = 'chat.gateway.do';
+      return fetch(new Request(url, request))
+    }
+  }
+  ```
+* 点击`触发器`选项卡，可以添加自定义访问域名。
+* 参考`高阶设置`中的环境变量使用你的服务地址进行替换。
+* 这里有一个示例代理地址：`https://chat1.gateway.do`。
+
 ## 其他说明
 
 * 项目是站在其他巨人的肩膀上，感谢！
 * 报错、BUG之类的提出`Issue`，我会修复。
 * 因为之后`ChatGPT`的API变动，我可能不会跟进修复。
 * 喜欢的可以给颗星，都是老朋友了。
 * 不影响`PHP是世界上最好的编程语言！`
```

### Comparing `Pandora-ChatGPT-0.9.7/Pandora_ChatGPT.egg-info/PKG-INFO` & `Pandora-ChatGPT-0.9.8/Pandora_ChatGPT.egg-info/PKG-INFO`

 * *Files 6% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: Pandora-ChatGPT
-Version: 0.9.7
+Version: 0.9.8
 Summary: A command-line interface to ChatGPT
 Home-page: https://github.com/pengzhile/pandora
 Author: Neo Peng
 Author-email: pengzhile@gmail.com
 Project-URL: Source, https://github.com/pengzhile/pandora
 Project-URL: Tracker, https://github.com/pengzhile/pandora/issues
 Keywords: OpenAI ChatGPT ChatGPT-Plus gpt-3.5-turbo gpt-3.5-turbo-0301
@@ -191,14 +191,15 @@
 * `/version` 打印`Pandora`的版本信息。
 * `/exit` 退出`潘多拉`。
 
 ## 高阶设置
 
 * 本部分内容不理解的朋友，**请勿擅动！**
 * 环境变量 `OPENAI_API_PREFIX` 可以替换OpenAI Api的前缀`https://api.openai.com`。
+* 环境变量 `CHATGPT_API_PREFIX` 可以替换ChatGPT Api的前缀`https://chat.gateway.do`。
 * 如果你想持久存储`Docker`中`Pandora`产生的数据，你可以挂载宿主机目录至`/data`。
 * 如果你在国内使用`pip`安装缓慢，可以考虑切换至腾讯的源：```pip config set global.index-url https://mirrors.cloud.tencent.com/pypi/simple```
 * 镜像同步版本可能不及时，如果出现这种情况建议切换至官方源：```pip config set global.index-url https://pypi.org/simple```
 * 默认使用`sqlite3`存储会话数据，如果你希望更换至`mysql`，可以这么做：
   * 执行```pip install PyMySQL```安装驱动。
   * 设置环境变量：`DATABASE_URI`为类似`mysql+pymysql://user:pass@localhost/dbname`的连接字符串。
 * 环境变量指定`OPENAI_EMAIL`可以替代登录输入用户名，`OPENAI_PASSWORD`则可以替代输入密码。
@@ -206,14 +207,33 @@
 ## Cloud模式
 
 * 搭建一个跟官方很像的`ChatGPT`服务，不能说很像，只能说一样。
 * 该模式使用`pandora-cloud`启动，前提是你如前面所说安装好了。
 * Docker环境变量：`PANDORA_CLOUD` 启动`cloud`模式。
 * 该模式参数含义与普通模式相同，可`--help`查看。
 
+## 使用Cloudflare Workers代理
+
+* 如果你感觉默认的`https://chat.gateway.do`在你那里可能被墙了，可以使用如下方法自行代理。
+* 你需要一个`Cloudflare`账号，如果没有，可以[注册](https://dash.cloudflare.com/sign-up)一个。
+* 登录后，点击`Workers`，然后点击`Create a Worker`，填入服务名称后点击`创建服务`。
+* 点开你刚才创建的服务，点击`快速编辑`按钮，贴入下面的代码，然后点击`保存并部署`。
+  ```javascript
+  export default {
+    async fetch(request, env) {
+      const url = new URL(request.url);
+      url.host = 'chat.gateway.do';
+      return fetch(new Request(url, request))
+    }
+  }
+  ```
+* 点击`触发器`选项卡，可以添加自定义访问域名。
+* 参考`高阶设置`中的环境变量使用你的服务地址进行替换。
+* 这里有一个示例代理地址：`https://chat1.gateway.do`。
+
 ## 其他说明
 
 * 项目是站在其他巨人的肩膀上，感谢！
 * 报错、BUG之类的提出`Issue`，我会修复。
 * 因为之后`ChatGPT`的API变动，我可能不会跟进修复。
 * 喜欢的可以给颗星，都是老朋友了。
 * 不影响`PHP是世界上最好的编程语言！`
```

### Comparing `Pandora-ChatGPT-0.9.7/Pandora_ChatGPT.egg-info/SOURCES.txt` & `Pandora-ChatGPT-0.9.8/Pandora_ChatGPT.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `Pandora-ChatGPT-0.9.7/README.md` & `Pandora-ChatGPT-0.9.8/README.md`

 * *Files 8% similar despite different names*

```diff
@@ -154,14 +154,15 @@
 * `/version` 打印`Pandora`的版本信息。
 * `/exit` 退出`潘多拉`。
 
 ## 高阶设置
 
 * 本部分内容不理解的朋友，**请勿擅动！**
 * 环境变量 `OPENAI_API_PREFIX` 可以替换OpenAI Api的前缀`https://api.openai.com`。
+* 环境变量 `CHATGPT_API_PREFIX` 可以替换ChatGPT Api的前缀`https://chat.gateway.do`。
 * 如果你想持久存储`Docker`中`Pandora`产生的数据，你可以挂载宿主机目录至`/data`。
 * 如果你在国内使用`pip`安装缓慢，可以考虑切换至腾讯的源：```pip config set global.index-url https://mirrors.cloud.tencent.com/pypi/simple```
 * 镜像同步版本可能不及时，如果出现这种情况建议切换至官方源：```pip config set global.index-url https://pypi.org/simple```
 * 默认使用`sqlite3`存储会话数据，如果你希望更换至`mysql`，可以这么做：
   * 执行```pip install PyMySQL```安装驱动。
   * 设置环境变量：`DATABASE_URI`为类似`mysql+pymysql://user:pass@localhost/dbname`的连接字符串。
 * 环境变量指定`OPENAI_EMAIL`可以替代登录输入用户名，`OPENAI_PASSWORD`则可以替代输入密码。
@@ -169,14 +170,33 @@
 ## Cloud模式
 
 * 搭建一个跟官方很像的`ChatGPT`服务，不能说很像，只能说一样。
 * 该模式使用`pandora-cloud`启动，前提是你如前面所说安装好了。
 * Docker环境变量：`PANDORA_CLOUD` 启动`cloud`模式。
 * 该模式参数含义与普通模式相同，可`--help`查看。
 
+## 使用Cloudflare Workers代理
+
+* 如果你感觉默认的`https://chat.gateway.do`在你那里可能被墙了，可以使用如下方法自行代理。
+* 你需要一个`Cloudflare`账号，如果没有，可以[注册](https://dash.cloudflare.com/sign-up)一个。
+* 登录后，点击`Workers`，然后点击`Create a Worker`，填入服务名称后点击`创建服务`。
+* 点开你刚才创建的服务，点击`快速编辑`按钮，贴入下面的代码，然后点击`保存并部署`。
+  ```javascript
+  export default {
+    async fetch(request, env) {
+      const url = new URL(request.url);
+      url.host = 'chat.gateway.do';
+      return fetch(new Request(url, request))
+    }
+  }
+  ```
+* 点击`触发器`选项卡，可以添加自定义访问域名。
+* 参考`高阶设置`中的环境变量使用你的服务地址进行替换。
+* 这里有一个示例代理地址：`https://chat1.gateway.do`。
+
 ## 其他说明
 
 * 项目是站在其他巨人的肩膀上，感谢！
 * 报错、BUG之类的提出`Issue`，我会修复。
 * 因为之后`ChatGPT`的API变动，我可能不会跟进修复。
 * 喜欢的可以给颗星，都是老朋友了。
 * 不影响`PHP是世界上最好的编程语言！`
```

### Comparing `Pandora-ChatGPT-0.9.7/setup.py` & `Pandora-ChatGPT-0.9.8/setup.py`

 * *Files identical despite different names*

### Comparing `Pandora-ChatGPT-0.9.7/src/pandora/bots/legacy.py` & `Pandora-ChatGPT-0.9.8/src/pandora/bots/legacy.py`

 * *Files identical despite different names*

### Comparing `Pandora-ChatGPT-0.9.7/src/pandora/bots/server.py` & `Pandora-ChatGPT-0.9.8/src/pandora/bots/server.py`

 * *Files identical despite different names*

### Comparing `Pandora-ChatGPT-0.9.7/src/pandora/cloud_launcher.py` & `Pandora-ChatGPT-0.9.8/src/pandora/cloud_launcher.py`

 * *Files identical despite different names*

### Comparing `Pandora-ChatGPT-0.9.7/src/pandora/exts/hooks.py` & `Pandora-ChatGPT-0.9.8/src/pandora/exts/hooks.py`

 * *Files identical despite different names*

### Comparing `Pandora-ChatGPT-0.9.7/src/pandora/exts/token.py` & `Pandora-ChatGPT-0.9.8/src/pandora/exts/token.py`

 * *Files identical despite different names*

### Comparing `Pandora-ChatGPT-0.9.7/src/pandora/flask/static/_next/static/chunks/113-23682f80a24dd00d.js` & `Pandora-ChatGPT-0.9.8/src/pandora/flask/static/_next/static/chunks/113-23682f80a24dd00d.js`

 * *Files identical despite different names*

### Comparing `Pandora-ChatGPT-0.9.7/src/pandora/flask/static/_next/static/chunks/14-0cb0d20affbd720d.js` & `Pandora-ChatGPT-0.9.8/src/pandora/flask/static/_next/static/chunks/14-0cb0d20affbd720d.js`

 * *Files identical despite different names*

### Comparing `Pandora-ChatGPT-0.9.7/src/pandora/flask/static/_next/static/chunks/174-bd28069f281ef76f.js` & `Pandora-ChatGPT-0.9.8/src/pandora/flask/static/_next/static/chunks/174-bd28069f281ef76f.js`

 * *Files identical despite different names*

### Comparing `Pandora-ChatGPT-0.9.7/src/pandora/flask/static/_next/static/chunks/1f110208-44a6f43ddc5e9011.js` & `Pandora-ChatGPT-0.9.8/src/pandora/flask/static/_next/static/chunks/1f110208-44a6f43ddc5e9011.js`

 * *Files identical despite different names*

### Comparing `Pandora-ChatGPT-0.9.7/src/pandora/flask/static/_next/static/chunks/264-13e92c51b0315184.js` & `Pandora-ChatGPT-0.9.8/src/pandora/flask/static/_next/static/chunks/264-13e92c51b0315184.js`

 * *Files identical despite different names*

### Comparing `Pandora-ChatGPT-0.9.7/src/pandora/flask/static/_next/static/chunks/360-442b869f1ba4bb1b.js` & `Pandora-ChatGPT-0.9.8/src/pandora/flask/static/_next/static/chunks/360-442b869f1ba4bb1b.js`

 * *Files identical despite different names*

### Comparing `Pandora-ChatGPT-0.9.7/src/pandora/flask/static/_next/static/chunks/424-d1d3bfe6a3ca6c4a.js` & `Pandora-ChatGPT-0.9.8/src/pandora/flask/static/_next/static/chunks/424-d1d3bfe6a3ca6c4a.js`

 * *Files identical despite different names*

### Comparing `Pandora-ChatGPT-0.9.7/src/pandora/flask/static/_next/static/chunks/554.9b8bfd0762461d74.js` & `Pandora-ChatGPT-0.9.8/src/pandora/flask/static/_next/static/chunks/554.9b8bfd0762461d74.js`

 * *Files identical despite different names*

### Comparing `Pandora-ChatGPT-0.9.7/src/pandora/flask/static/_next/static/chunks/762-222df1028c0c1555.js` & `Pandora-ChatGPT-0.9.8/src/pandora/flask/static/_next/static/chunks/762-222df1028c0c1555.js`

 * *Files identical despite different names*

### Comparing `Pandora-ChatGPT-0.9.7/src/pandora/flask/static/_next/static/chunks/949.1a6eb804b5e91f61.js` & `Pandora-ChatGPT-0.9.8/src/pandora/flask/static/_next/static/chunks/949.1a6eb804b5e91f61.js`

 * *Files identical despite different names*

### Comparing `Pandora-ChatGPT-0.9.7/src/pandora/flask/static/_next/static/chunks/framework-7a789ee31d2a7534.js` & `Pandora-ChatGPT-0.9.8/src/pandora/flask/static/_next/static/chunks/framework-7a789ee31d2a7534.js`

 * *Files identical despite different names*

### Comparing `Pandora-ChatGPT-0.9.7/src/pandora/flask/static/_next/static/chunks/main-149b337e061b4d04.js` & `Pandora-ChatGPT-0.9.8/src/pandora/flask/static/_next/static/chunks/main-149b337e061b4d04.js`

 * *Files identical despite different names*

### Comparing `Pandora-ChatGPT-0.9.7/src/pandora/flask/static/_next/static/chunks/pages/_app-aaa11de1926dcafe.js` & `Pandora-ChatGPT-0.9.8/src/pandora/flask/static/_next/static/chunks/pages/_app-aaa11de1926dcafe.js`

 * *Files identical despite different names*

### Comparing `Pandora-ChatGPT-0.9.7/src/pandora/flask/static/_next/static/chunks/pages/chat/[[...chatId]]-76751174916fa3f7.js` & `Pandora-ChatGPT-0.9.8/src/pandora/flask/static/_next/static/chunks/pages/chat/[[...chatId]]-76751174916fa3f7.js`

 * *Files identical despite different names*

### Comparing `Pandora-ChatGPT-0.9.7/src/pandora/flask/static/_next/static/chunks/polyfills-c67a75d1b6f99dc8.js` & `Pandora-ChatGPT-0.9.8/src/pandora/flask/static/_next/static/chunks/polyfills-c67a75d1b6f99dc8.js`

 * *Files identical despite different names*

### Comparing `Pandora-ChatGPT-0.9.7/src/pandora/flask/static/_next/static/chunks/webpack-c9a868e8e0796ec6.js` & `Pandora-ChatGPT-0.9.8/src/pandora/flask/static/_next/static/chunks/webpack-c9a868e8e0796ec6.js`

 * *Files identical despite different names*

### Comparing `Pandora-ChatGPT-0.9.7/src/pandora/flask/static/_next/static/css/ac221fb2caad35a6.css` & `Pandora-ChatGPT-0.9.8/src/pandora/flask/static/_next/static/css/ac221fb2caad35a6.css`

 * *Files identical despite different names*

### Comparing `Pandora-ChatGPT-0.9.7/src/pandora/flask/static/_next/static/olf4sv64FWIcQ_zCGl90t/_buildManifest.js` & `Pandora-ChatGPT-0.9.8/src/pandora/flask/static/_next/static/olf4sv64FWIcQ_zCGl90t/_buildManifest.js`

 * *Files identical despite different names*

### Comparing `Pandora-ChatGPT-0.9.7/src/pandora/flask/static/apple-touch-icon.png` & `Pandora-ChatGPT-0.9.8/src/pandora/flask/static/apple-touch-icon.png`

 * *Files identical despite different names*

### Comparing `Pandora-ChatGPT-0.9.7/src/pandora/flask/static/favicon-16x16.png` & `Pandora-ChatGPT-0.9.8/src/pandora/flask/static/favicon-16x16.png`

 * *Files identical despite different names*

### Comparing `Pandora-ChatGPT-0.9.7/src/pandora/flask/static/favicon-32x32.png` & `Pandora-ChatGPT-0.9.8/src/pandora/flask/static/favicon-32x32.png`

 * *Files identical despite different names*

### Comparing `Pandora-ChatGPT-0.9.7/src/pandora/flask/static/fonts/KaTeX_Caligraphic-Bold.woff` & `Pandora-ChatGPT-0.9.8/src/pandora/flask/static/fonts/KaTeX_Caligraphic-Bold.woff`

 * *Files identical despite different names*

### Comparing `Pandora-ChatGPT-0.9.7/src/pandora/flask/static/fonts/KaTeX_Caligraphic-Regular.woff` & `Pandora-ChatGPT-0.9.8/src/pandora/flask/static/fonts/KaTeX_Caligraphic-Regular.woff`

 * *Files identical despite different names*

### Comparing `Pandora-ChatGPT-0.9.7/src/pandora/flask/static/fonts/KaTeX_Fraktur-Bold.woff` & `Pandora-ChatGPT-0.9.8/src/pandora/flask/static/fonts/KaTeX_Fraktur-Bold.woff`

 * *Files identical despite different names*

### Comparing `Pandora-ChatGPT-0.9.7/src/pandora/flask/static/fonts/KaTeX_Fraktur-Regular.woff` & `Pandora-ChatGPT-0.9.8/src/pandora/flask/static/fonts/KaTeX_Fraktur-Regular.woff`

 * *Files identical despite different names*

### Comparing `Pandora-ChatGPT-0.9.7/src/pandora/flask/static/fonts/KaTeX_Main-Bold.woff` & `Pandora-ChatGPT-0.9.8/src/pandora/flask/static/fonts/KaTeX_Main-Bold.woff`

 * *Files identical despite different names*

### Comparing `Pandora-ChatGPT-0.9.7/src/pandora/flask/static/fonts/KaTeX_Main-BoldItalic.woff` & `Pandora-ChatGPT-0.9.8/src/pandora/flask/static/fonts/KaTeX_Main-BoldItalic.woff`

 * *Files identical despite different names*

### Comparing `Pandora-ChatGPT-0.9.7/src/pandora/flask/static/fonts/KaTeX_Main-Italic.woff` & `Pandora-ChatGPT-0.9.8/src/pandora/flask/static/fonts/KaTeX_Main-Italic.woff`

 * *Files identical despite different names*

### Comparing `Pandora-ChatGPT-0.9.7/src/pandora/flask/static/fonts/KaTeX_Main-Regular.woff` & `Pandora-ChatGPT-0.9.8/src/pandora/flask/static/fonts/KaTeX_Main-Regular.woff`

 * *Files identical despite different names*

### Comparing `Pandora-ChatGPT-0.9.7/src/pandora/flask/static/fonts/KaTeX_Math-BoldItalic.woff` & `Pandora-ChatGPT-0.9.8/src/pandora/flask/static/fonts/KaTeX_Math-BoldItalic.woff`

 * *Files identical despite different names*

### Comparing `Pandora-ChatGPT-0.9.7/src/pandora/flask/static/fonts/KaTeX_Math-Italic.woff` & `Pandora-ChatGPT-0.9.8/src/pandora/flask/static/fonts/KaTeX_Math-Italic.woff`

 * *Files identical despite different names*

### Comparing `Pandora-ChatGPT-0.9.7/src/pandora/flask/static/fonts/KaTeX_SansSerif-Bold.woff` & `Pandora-ChatGPT-0.9.8/src/pandora/flask/static/fonts/KaTeX_SansSerif-Bold.woff`

 * *Files identical despite different names*

### Comparing `Pandora-ChatGPT-0.9.7/src/pandora/flask/static/fonts/KaTeX_SansSerif-Italic.woff` & `Pandora-ChatGPT-0.9.8/src/pandora/flask/static/fonts/KaTeX_SansSerif-Italic.woff`

 * *Files identical despite different names*

### Comparing `Pandora-ChatGPT-0.9.7/src/pandora/flask/static/fonts/KaTeX_SansSerif-Regular.woff` & `Pandora-ChatGPT-0.9.8/src/pandora/flask/static/fonts/KaTeX_SansSerif-Regular.woff`

 * *Files identical despite different names*

### Comparing `Pandora-ChatGPT-0.9.7/src/pandora/flask/static/fonts/KaTeX_Script-Regular.woff` & `Pandora-ChatGPT-0.9.8/src/pandora/flask/static/fonts/KaTeX_Script-Regular.woff`

 * *Files identical despite different names*

### Comparing `Pandora-ChatGPT-0.9.7/src/pandora/flask/static/fonts/KaTeX_Size1-Regular.woff` & `Pandora-ChatGPT-0.9.8/src/pandora/flask/static/fonts/KaTeX_Size1-Regular.woff`

 * *Files identical despite different names*

### Comparing `Pandora-ChatGPT-0.9.7/src/pandora/flask/static/fonts/KaTeX_Size2-Regular.woff` & `Pandora-ChatGPT-0.9.8/src/pandora/flask/static/fonts/KaTeX_Size2-Regular.woff`

 * *Files identical despite different names*

### Comparing `Pandora-ChatGPT-0.9.7/src/pandora/flask/static/fonts/KaTeX_Size3-Regular.woff` & `Pandora-ChatGPT-0.9.8/src/pandora/flask/static/fonts/KaTeX_Size3-Regular.woff`

 * *Files identical despite different names*

### Comparing `Pandora-ChatGPT-0.9.7/src/pandora/flask/static/fonts/KaTeX_Size4-Regular.woff` & `Pandora-ChatGPT-0.9.8/src/pandora/flask/static/fonts/KaTeX_Size4-Regular.woff`

 * *Files identical despite different names*

### Comparing `Pandora-ChatGPT-0.9.7/src/pandora/flask/static/fonts/KaTeX_Typewriter-Regular.woff` & `Pandora-ChatGPT-0.9.8/src/pandora/flask/static/fonts/KaTeX_Typewriter-Regular.woff`

 * *Files identical despite different names*

### Comparing `Pandora-ChatGPT-0.9.7/src/pandora/flask/static/fonts/Signifier-Regular.otf` & `Pandora-ChatGPT-0.9.8/src/pandora/flask/static/fonts/Signifier-Regular.otf`

 * *Files identical despite different names*

### Comparing `Pandora-ChatGPT-0.9.7/src/pandora/flask/static/fonts/Sohne-Buch.otf` & `Pandora-ChatGPT-0.9.8/src/pandora/flask/static/fonts/Sohne-Buch.otf`

 * *Files identical despite different names*

### Comparing `Pandora-ChatGPT-0.9.7/src/pandora/flask/static/fonts/Sohne-Halbfett.otf` & `Pandora-ChatGPT-0.9.8/src/pandora/flask/static/fonts/Sohne-Halbfett.otf`

 * *Files identical despite different names*

### Comparing `Pandora-ChatGPT-0.9.7/src/pandora/flask/static/fonts/SohneMono-Buch.otf` & `Pandora-ChatGPT-0.9.8/src/pandora/flask/static/fonts/SohneMono-Buch.otf`

 * *Files identical despite different names*

### Comparing `Pandora-ChatGPT-0.9.7/src/pandora/flask/static/fonts/SohneMono-Halbfett.otf` & `Pandora-ChatGPT-0.9.8/src/pandora/flask/static/fonts/SohneMono-Halbfett.otf`

 * *Files identical despite different names*

### Comparing `Pandora-ChatGPT-0.9.7/src/pandora/flask/static/images/2022/11/ChatGPT.jpg` & `Pandora-ChatGPT-0.9.8/src/pandora/flask/static/images/2022/11/ChatGPT.jpg`

 * *Files identical despite different names*

### Comparing `Pandora-ChatGPT-0.9.7/src/pandora/flask/templates/chat.html` & `Pandora-ChatGPT-0.9.8/src/pandora/flask/templates/chat.html`

 * *Files identical despite different names*

### Comparing `Pandora-ChatGPT-0.9.7/src/pandora/launcher.py` & `Pandora-ChatGPT-0.9.8/src/pandora/launcher.py`

 * *Files 6% similar despite different names*

```diff
@@ -82,20 +82,23 @@
 
     return None, True
 
 
 def main():
     global __show_verbose
 
+    api_prefix = getenv('CHATGPT_API_PREFIX', 'https://chat.gateway.do')
+    prefix_changed = 'https://chat.gateway.do' != api_prefix
+
     Console.debug_b(
         '''
             Pandora - A command-line interface to ChatGPT
             Github: https://github.com/pengzhile/pandora
-            Get access token: https://chat.gateway.do/auth
-            Version: {}'''.format(__version__), end=''
+            Get access token: {}/auth
+            Version: {}'''.format(api_prefix, __version__), end=''
     )
 
     parser = argparse.ArgumentParser()
     parser.add_argument(
         '-p',
         '--proxy',
         help='Use a proxy. Format: protocol://user:pass@ip:port',
@@ -164,15 +167,16 @@
             Console.error_bh('### You need `pip install Pandora-ChatGPT[api]` to support API mode.')
             return
 
     access_token, need_save = confirm_access_token(args.token_file, args.server, args.api)
     if not access_token:
         Console.info_b('Please enter your email and password to log in ChatGPT!')
         if not args.local:
-            Console.warn('We login via https://chat.gateway.do, but it doesn\'t retain your data.')
+            Console.warn(
+                'We login via {}{}'.format(api_prefix, '' if prefix_changed else ', but it doesn\'t retain your data.'))
         email = getenv('OPENAI_EMAIL') or Prompt.ask('  Email')
         password = getenv('OPENAI_PASSWORD') or Prompt.ask('  Password', password=True)
         Console.warn('### Do login, please wait...')
         access_token = Auth0(email, password, args.proxy).auth(args.local)
 
     if not check_access_token_out(access_token, args.api):
         return
```

### Comparing `Pandora-ChatGPT-0.9.7/src/pandora/migrations/migrate.py` & `Pandora-ChatGPT-0.9.8/src/pandora/migrations/migrate.py`

 * *Files identical despite different names*

### Comparing `Pandora-ChatGPT-0.9.7/src/pandora/migrations/models.py` & `Pandora-ChatGPT-0.9.8/src/pandora/migrations/models.py`

 * *Files identical despite different names*

### Comparing `Pandora-ChatGPT-0.9.7/src/pandora/migrations/scripts/20230308_01_7ctOr.sql` & `Pandora-ChatGPT-0.9.8/src/pandora/migrations/scripts/20230308_01_7ctOr.sql`

 * *Files identical despite different names*

### Comparing `Pandora-ChatGPT-0.9.7/src/pandora/openai/api.py` & `Pandora-ChatGPT-0.9.8/src/pandora/openai/api.py`

 * *Files 9% similar despite different names*

```diff
@@ -108,18 +108,20 @@
                           'Pandora/{} Safari/537.36'.format(__version__)
         self.basic_headers = {
             'Authorization': 'Bearer ' + self.access_token,
             'User-Agent': self.user_agent,
             'Content-Type': 'application/json',
         }
 
+        self.api_prefix = getenv('CHATGPT_API_PREFIX', 'https://chat.gateway.do')
+
         super().__init__(proxy, self.req_kwargs['verify'])
 
     def list_models(self, raw=False):
-        url = 'https://chat.gateway.do/api/models'
+        url = '{}/api/models'.format(self.api_prefix)
         resp = self.session.get(url=url, headers=self.basic_headers, **self.req_kwargs)
 
         if raw:
             return resp
 
         if resp.status_code != 200:
             raise Exception('list models failed: ' + self.__get_error(resp))
@@ -127,27 +129,27 @@
         result = resp.json()
         if 'models' not in result:
             raise Exception('list models failed: ' + resp.text)
 
         return result['models']
 
     def list_conversations(self, offset, limit, raw=False):
-        url = 'https://chat.gateway.do/api/conversations?offset={}&limit={}'.format(offset, limit)
+        url = '{}/api/conversations?offset={}&limit={}'.format(self.api_prefix, offset, limit)
         resp = self.session.get(url=url, headers=self.basic_headers, **self.req_kwargs)
 
         if raw:
             return resp
 
         if resp.status_code != 200:
             raise Exception('list conversations failed: ' + self.__get_error(resp))
 
         return resp.json()
 
     def get_conversation(self, conversation_id, raw=False):
-        url = 'https://chat.gateway.do/api/conversation/' + conversation_id
+        url = '{}/api/conversation/{}'.format(self.api_prefix, conversation_id)
         resp = self.session.get(url=url, headers=self.basic_headers, **self.req_kwargs)
 
         if raw:
             return resp
 
         if resp.status_code != 200:
             raise Exception('get conversation failed: ' + self.__get_error(resp))
@@ -155,15 +157,15 @@
         return resp.json()
 
     def clear_conversations(self, raw=False):
         data = {
             'is_visible': False,
         }
 
-        url = 'https://chat.gateway.do/api/conversations'
+        url = '{}/api/conversations'.format(self.api_prefix)
         resp = self.session.patch(url=url, headers=self.basic_headers, json=data, **self.req_kwargs)
 
         if raw:
             return resp
 
         if resp.status_code != 200:
             raise Exception('clear conversations failed: ' + self.__get_error(resp))
@@ -178,15 +180,15 @@
         data = {
             'is_visible': False,
         }
 
         return self.__update_conversation(conversation_id, data, raw)
 
     def gen_conversation_title(self, conversation_id, model, message_id, raw=False):
-        url = 'https://chat.gateway.do/api/conversation/gen_title/' + conversation_id
+        url = '{}/api/conversation/gen_title/{}'.format(self.api_prefix, conversation_id)
         data = {
             'model': model,
             'message_id': message_id,
         }
         resp = self.session.post(url=url, headers=self.basic_headers, json=data, **self.req_kwargs)
 
         if raw:
@@ -263,21 +265,21 @@
             'conversation_id': conversation_id,
             'parent_message_id': parent_message_id,
         }
 
         return self.__request_conversation(data)
 
     def __request_conversation(self, data):
-        url = 'https://chat.gateway.do/api/conversation'
+        url = '{}/api/conversation'.format(self.api_prefix)
         headers = {**self.session.headers, **self.basic_headers, 'Accept': 'text/event-stream'}
 
         return self._request_sse(url, headers, data)
 
     def __update_conversation(self, conversation_id, data, raw=False):
-        url = 'https://chat.gateway.do/api/conversation/' + conversation_id
+        url = '{}/api/conversation/{}'.format(self.api_prefix, conversation_id)
         resp = self.session.patch(url=url, headers=self.basic_headers, json=data, **self.req_kwargs)
 
         if raw:
             return resp
 
         if resp.status_code != 200:
             raise Exception('update conversation failed: ' + self.__get_error(resp))
```

### Comparing `Pandora-ChatGPT-0.9.7/src/pandora/openai/auth.py` & `Pandora-ChatGPT-0.9.8/src/pandora/openai/auth.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,12 +1,13 @@
 # -*- coding: utf-8 -*-
 
 import datetime
 import re
 from datetime import datetime as dt
+from os import getenv
 from urllib.parse import urlparse, parse_qs
 
 import requests
 from certifi import where
 from requests.exceptions import SSLError
 
 
@@ -25,14 +26,15 @@
             'verify': where(),
             'timeout': 100,
         }
         self.access_token = None
         self.expires = None
         self.user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                           'Chrome/109.0.0.0 Safari/537.36'
+        self.api_prefix = getenv('CHATGPT_API_PREFIX', 'https://chat.gateway.do')
 
     @staticmethod
     def __check_email(email: str):
         regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
         return re.fullmatch(regex, email)
 
     def auth(self, login_local=False) -> str:
@@ -41,15 +43,15 @@
 
         if not self.__check_email(self.email) or not self.password:
             raise Exception('invalid email or password.')
 
         return self.__part_two() if login_local else self.get_access_token_proxy()
 
     def __part_two(self) -> str:
-        url = 'https://chat.gateway.do/auth/endpoint'
+        url = '{}/auth/endpoint'.format(self.api_prefix)
         headers = {
             'User-Agent': self.user_agent,
         }
         resp = self.session.get(url, headers=headers, allow_redirects=False, **self.req_kwargs)
 
         if resp.status_code == 200:
             json = resp.json()
@@ -121,15 +123,15 @@
 
         if resp.status_code == 400:
             raise Exception('Wrong email or password.')
         else:
             raise Exception('Error login.')
 
     def get_access_token(self, state1: str, callback_url: str) -> str:
-        url = 'https://chat.gateway.do/auth/token'
+        url = '{}/auth/token'.format(self.api_prefix)
         headers = {
             'User-Agent': self.user_agent,
         }
         data = {
             'state': state1,
             'callbackUrl': callback_url,
         }
@@ -143,15 +145,15 @@
             self.access_token = json['accessToken']
             self.expires = dt.strptime(json['expires'], '%Y-%m-%dT%H:%M:%S.%fZ') - datetime.timedelta(minutes=5)
             return self.access_token
         else:
             raise Exception(resp.text)
 
     def get_access_token_proxy(self) -> str:
-        url = 'https://chat.gateway.do/api/auth/login'
+        url = '{}/api/auth/login'.format(self.api_prefix)
         headers = {
             'User-Agent': self.user_agent,
         }
         data = {
             'username': self.email,
             'password': self.password,
         }
```

### Comparing `Pandora-ChatGPT-0.9.7/src/pandora/openai/utils.py` & `Pandora-ChatGPT-0.9.8/src/pandora/openai/utils.py`

 * *Files identical despite different names*

### Comparing `Pandora-ChatGPT-0.9.7/src/pandora/turbo/base.py` & `Pandora-ChatGPT-0.9.8/src/pandora/turbo/base.py`

 * *Files identical despite different names*

### Comparing `Pandora-ChatGPT-0.9.7/src/pandora/turbo/chat.py` & `Pandora-ChatGPT-0.9.8/src/pandora/turbo/chat.py`

 * *Files identical despite different names*

