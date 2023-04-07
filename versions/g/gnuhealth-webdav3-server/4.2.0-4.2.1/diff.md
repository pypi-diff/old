# Comparing `tmp/gnuhealth_webdav3_server-4.2.0.tar.gz` & `tmp/gnuhealth_webdav3_server-4.2.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "gnuhealth_webdav3_server-4.2.0.tar", last modified: Sat Feb 11 21:58:06 2023, max compression
+gzip compressed data, was "gnuhealth_webdav3_server-4.2.1.tar", last modified: Fri Apr  7 10:20:03 2023, max compression
```

## Comparing `gnuhealth_webdav3_server-4.2.0.tar` & `gnuhealth_webdav3_server-4.2.1.tar`

### file list

```diff
@@ -1,56 +1,56 @@
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:58:06.634980 gnuhealth_webdav3_server-4.2.0/
--rw-r--r--   0 lfm       (1001) lfm       (1001)      121 2023-01-18 16:33:08.000000 gnuhealth_webdav3_server-4.2.0/MANIFEST.in
--rw-r--r--   0 lfm       (1001) lfm       (1001)     5754 2023-02-11 21:58:06.634830 gnuhealth_webdav3_server-4.2.0/PKG-INFO
--rw-r--r--   0 lfm       (1001) lfm       (1001)     4826 2023-01-18 16:33:08.000000 gnuhealth_webdav3_server-4.2.0/README.rst
--rw-r--r--   0 lfm       (1001) lfm       (1001)      916 2023-01-18 16:33:08.000000 gnuhealth_webdav3_server-4.2.0/__init__.py
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:58:06.633737 gnuhealth_webdav3_server-4.2.0/bin/
--rwxr-xr-x   0 lfm       (1001) lfm       (1001)     2576 2023-01-18 16:33:08.000000 gnuhealth_webdav3_server-4.2.0/bin/gnuhealth-webdav-server
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:58:06.630911 gnuhealth_webdav3_server-4.2.0/data/
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:58:06.632015 gnuhealth_webdav3_server-4.2.0/data/messages/
--rw-r--r--   0 lfm       (1001) lfm       (1001)      684 2023-01-18 16:33:08.000000 gnuhealth_webdav3_server-4.2.0/data/messages/messages.xml
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:58:06.633805 gnuhealth_webdav3_server-4.2.0/doc/
--rw-r--r--   0 lfm       (1001) lfm       (1001)      613 2023-01-18 16:33:08.000000 gnuhealth_webdav3_server-4.2.0/doc/index.rst
--rw-r--r--   0 lfm       (1001) lfm       (1001)      304 2023-01-18 16:33:08.000000 gnuhealth_webdav3_server-4.2.0/exceptions.py
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:58:06.634279 gnuhealth_webdav3_server-4.2.0/gnuhealth_webdav3_server.egg-info/
--rw-r--r--   0 lfm       (1001) lfm       (1001)     5754 2023-02-11 21:58:06.000000 gnuhealth_webdav3_server-4.2.0/gnuhealth_webdav3_server.egg-info/PKG-INFO
--rw-r--r--   0 lfm       (1001) lfm       (1001)     1396 2023-02-11 21:58:06.000000 gnuhealth_webdav3_server-4.2.0/gnuhealth_webdav3_server.egg-info/SOURCES.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)        1 2023-02-11 21:58:06.000000 gnuhealth_webdav3_server-4.2.0/gnuhealth_webdav3_server.egg-info/dependency_links.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)       80 2023-02-11 21:58:06.000000 gnuhealth_webdav3_server-4.2.0/gnuhealth_webdav3_server.egg-info/entry_points.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)        1 2023-02-11 21:58:06.000000 gnuhealth_webdav3_server-4.2.0/gnuhealth_webdav3_server.egg-info/not-zip-safe
--rw-r--r--   0 lfm       (1001) lfm       (1001)       28 2023-02-11 21:58:06.000000 gnuhealth_webdav3_server-4.2.0/gnuhealth_webdav3_server.egg-info/requires.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)        8 2023-02-11 21:58:06.000000 gnuhealth_webdav3_server-4.2.0/gnuhealth_webdav3_server.egg-info/top_level.txt
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:58:06.633145 gnuhealth_webdav3_server-4.2.0/locale/
--rw-r--r--   0 lfm       (1001) lfm       (1001)     4110 2022-11-28 22:17:48.000000 gnuhealth_webdav3_server-4.2.0/locale/bg.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)     4452 2022-11-28 22:17:48.000000 gnuhealth_webdav3_server-4.2.0/locale/ca.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)     3146 2022-11-28 22:17:48.000000 gnuhealth_webdav3_server-4.2.0/locale/cs.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)     4485 2022-11-28 22:17:48.000000 gnuhealth_webdav3_server-4.2.0/locale/de.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)     4514 2022-11-28 22:17:48.000000 gnuhealth_webdav3_server-4.2.0/locale/es.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)     4429 2022-11-28 22:17:48.000000 gnuhealth_webdav3_server-4.2.0/locale/fr.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)     3640 2022-11-28 22:17:48.000000 gnuhealth_webdav3_server-4.2.0/locale/hu_HU.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)     4109 2023-01-18 16:33:08.000000 gnuhealth_webdav3_server-4.2.0/locale/it_IT.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)     3234 2022-11-28 22:17:48.000000 gnuhealth_webdav3_server-4.2.0/locale/ja_JP.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)     3734 2022-11-28 22:17:48.000000 gnuhealth_webdav3_server-4.2.0/locale/lo.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)     3146 2022-11-28 22:17:48.000000 gnuhealth_webdav3_server-4.2.0/locale/lt.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)     3780 2022-11-28 22:17:48.000000 gnuhealth_webdav3_server-4.2.0/locale/nl.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)     3234 2022-11-28 22:17:48.000000 gnuhealth_webdav3_server-4.2.0/locale/pl.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)     4069 2022-11-28 22:17:48.000000 gnuhealth_webdav3_server-4.2.0/locale/pt_BR.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)     5125 2022-11-28 22:17:48.000000 gnuhealth_webdav3_server-4.2.0/locale/ru.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)     3909 2022-11-28 22:17:48.000000 gnuhealth_webdav3_server-4.2.0/locale/sl.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)     2935 2023-01-18 16:33:08.000000 gnuhealth_webdav3_server-4.2.0/locale/zh_CN.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)    22514 2023-01-18 16:33:08.000000 gnuhealth_webdav3_server-4.2.0/protocol.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)     3607 2023-01-18 16:33:08.000000 gnuhealth_webdav3_server-4.2.0/server.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)       38 2023-02-11 21:58:06.635015 gnuhealth_webdav3_server-4.2.0/setup.cfg
--rw-r--r--   0 lfm       (1001) lfm       (1001)     4035 2023-01-18 16:33:08.000000 gnuhealth_webdav3_server-4.2.0/setup.py
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:58:06.633271 gnuhealth_webdav3_server-4.2.0/tests/
--rw-r--r--   0 lfm       (1001) lfm       (1001)      441 2023-01-18 16:33:08.000000 gnuhealth_webdav3_server-4.2.0/tests/__init__.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)      763 2023-01-18 16:33:08.000000 gnuhealth_webdav3_server-4.2.0/tests/test_webdav.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)       98 2023-02-11 12:44:33.000000 gnuhealth_webdav3_server-4.2.0/tryton.cfg
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:58:06.633671 gnuhealth_webdav3_server-4.2.0/view/
--rw-r--r--   0 lfm       (1001) lfm       (1001)      631 2023-01-18 16:33:08.000000 gnuhealth_webdav3_server-4.2.0/view/attachment_form.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)      531 2023-01-18 16:33:08.000000 gnuhealth_webdav3_server-4.2.0/view/collection_form.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)      333 2023-01-18 16:33:08.000000 gnuhealth_webdav3_server-4.2.0/view/collection_list.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)      425 2023-01-18 16:33:08.000000 gnuhealth_webdav3_server-4.2.0/view/collection_tree.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)      760 2023-01-18 16:33:08.000000 gnuhealth_webdav3_server-4.2.0/view/share_form.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)      368 2023-01-18 16:33:08.000000 gnuhealth_webdav3_server-4.2.0/view/share_list.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)    33952 2023-01-18 16:33:08.000000 gnuhealth_webdav3_server-4.2.0/webdav.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)     6864 2023-01-18 16:33:08.000000 gnuhealth_webdav3_server-4.2.0/webdav.xml
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:20:03.084992 gnuhealth_webdav3_server-4.2.1/
+-rw-r--r--   0 lfm       (1001) wheel        (0)      121 2023-04-07 09:17:52.000000 gnuhealth_webdav3_server-4.2.1/MANIFEST.in
+-rw-r--r--   0 lfm       (1001) wheel        (0)     5754 2023-04-07 10:20:03.084849 gnuhealth_webdav3_server-4.2.1/PKG-INFO
+-rw-r--r--   0 lfm       (1001) wheel        (0)     4826 2023-04-07 09:17:52.000000 gnuhealth_webdav3_server-4.2.1/README.rst
+-rw-r--r--   0 lfm       (1001) wheel        (0)      916 2023-04-07 09:17:52.000000 gnuhealth_webdav3_server-4.2.1/__init__.py
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:20:03.083696 gnuhealth_webdav3_server-4.2.1/bin/
+-rwxr-xr-x   0 lfm       (1001) wheel        (0)     2576 2023-01-18 16:33:08.000000 gnuhealth_webdav3_server-4.2.1/bin/gnuhealth-webdav-server
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:20:03.080667 gnuhealth_webdav3_server-4.2.1/data/
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:20:03.081728 gnuhealth_webdav3_server-4.2.1/data/messages/
+-rw-r--r--   0 lfm       (1001) wheel        (0)      684 2023-04-07 09:17:52.000000 gnuhealth_webdav3_server-4.2.1/data/messages/messages.xml
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:20:03.083795 gnuhealth_webdav3_server-4.2.1/doc/
+-rw-r--r--   0 lfm       (1001) wheel        (0)      613 2023-04-07 09:17:52.000000 gnuhealth_webdav3_server-4.2.1/doc/index.rst
+-rw-r--r--   0 lfm       (1001) wheel        (0)      304 2023-04-07 09:17:52.000000 gnuhealth_webdav3_server-4.2.1/exceptions.py
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:20:03.084286 gnuhealth_webdav3_server-4.2.1/gnuhealth_webdav3_server.egg-info/
+-rw-r--r--   0 lfm       (1001) wheel        (0)     5754 2023-04-07 10:20:03.000000 gnuhealth_webdav3_server-4.2.1/gnuhealth_webdav3_server.egg-info/PKG-INFO
+-rw-r--r--   0 lfm       (1001) wheel        (0)     1396 2023-04-07 10:20:03.000000 gnuhealth_webdav3_server-4.2.1/gnuhealth_webdav3_server.egg-info/SOURCES.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)        1 2023-04-07 10:20:03.000000 gnuhealth_webdav3_server-4.2.1/gnuhealth_webdav3_server.egg-info/dependency_links.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)       80 2023-04-07 10:20:03.000000 gnuhealth_webdav3_server-4.2.1/gnuhealth_webdav3_server.egg-info/entry_points.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)        1 2023-04-07 10:20:03.000000 gnuhealth_webdav3_server-4.2.1/gnuhealth_webdav3_server.egg-info/not-zip-safe
+-rw-r--r--   0 lfm       (1001) wheel        (0)       28 2023-04-07 10:20:03.000000 gnuhealth_webdav3_server-4.2.1/gnuhealth_webdav3_server.egg-info/requires.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)        8 2023-04-07 10:20:03.000000 gnuhealth_webdav3_server-4.2.1/gnuhealth_webdav3_server.egg-info/top_level.txt
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:20:03.082809 gnuhealth_webdav3_server-4.2.1/locale/
+-rw-r--r--   0 lfm       (1001) wheel        (0)     4110 2022-11-28 22:17:48.000000 gnuhealth_webdav3_server-4.2.1/locale/bg.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)     4452 2022-11-28 22:17:48.000000 gnuhealth_webdav3_server-4.2.1/locale/ca.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)     3146 2022-11-28 22:17:48.000000 gnuhealth_webdav3_server-4.2.1/locale/cs.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)     4485 2022-11-28 22:17:48.000000 gnuhealth_webdav3_server-4.2.1/locale/de.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)     4514 2022-11-28 22:17:48.000000 gnuhealth_webdav3_server-4.2.1/locale/es.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)     4429 2022-11-28 22:17:48.000000 gnuhealth_webdav3_server-4.2.1/locale/fr.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)     3640 2022-11-28 22:17:48.000000 gnuhealth_webdav3_server-4.2.1/locale/hu_HU.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)     4109 2023-04-07 09:17:52.000000 gnuhealth_webdav3_server-4.2.1/locale/it_IT.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)     3234 2022-11-28 22:17:48.000000 gnuhealth_webdav3_server-4.2.1/locale/ja_JP.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)     3734 2022-11-28 22:17:48.000000 gnuhealth_webdav3_server-4.2.1/locale/lo.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)     3146 2022-11-28 22:17:48.000000 gnuhealth_webdav3_server-4.2.1/locale/lt.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)     3780 2022-11-28 22:17:48.000000 gnuhealth_webdav3_server-4.2.1/locale/nl.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)     3234 2022-11-28 22:17:48.000000 gnuhealth_webdav3_server-4.2.1/locale/pl.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)     4069 2022-11-28 22:17:48.000000 gnuhealth_webdav3_server-4.2.1/locale/pt_BR.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)     5125 2022-11-28 22:17:48.000000 gnuhealth_webdav3_server-4.2.1/locale/ru.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)     3909 2022-11-28 22:17:48.000000 gnuhealth_webdav3_server-4.2.1/locale/sl.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)     2935 2023-04-07 09:17:52.000000 gnuhealth_webdav3_server-4.2.1/locale/zh_CN.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)    22514 2023-04-07 09:17:52.000000 gnuhealth_webdav3_server-4.2.1/protocol.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)     3607 2023-04-07 09:17:52.000000 gnuhealth_webdav3_server-4.2.1/server.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)       38 2023-04-07 10:20:03.085028 gnuhealth_webdav3_server-4.2.1/setup.cfg
+-rw-r--r--   0 lfm       (1001) wheel        (0)     4035 2023-04-07 09:17:52.000000 gnuhealth_webdav3_server-4.2.1/setup.py
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:20:03.082969 gnuhealth_webdav3_server-4.2.1/tests/
+-rw-r--r--   0 lfm       (1001) wheel        (0)      441 2023-04-07 09:17:52.000000 gnuhealth_webdav3_server-4.2.1/tests/__init__.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)      763 2023-04-07 09:17:52.000000 gnuhealth_webdav3_server-4.2.1/tests/test_webdav.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)       98 2023-04-07 09:37:21.000000 gnuhealth_webdav3_server-4.2.1/tryton.cfg
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:20:03.083597 gnuhealth_webdav3_server-4.2.1/view/
+-rw-r--r--   0 lfm       (1001) wheel        (0)      631 2023-04-07 09:17:52.000000 gnuhealth_webdav3_server-4.2.1/view/attachment_form.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)      531 2023-04-07 09:17:52.000000 gnuhealth_webdav3_server-4.2.1/view/collection_form.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)      333 2023-04-07 09:17:52.000000 gnuhealth_webdav3_server-4.2.1/view/collection_list.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)      425 2023-04-07 09:17:52.000000 gnuhealth_webdav3_server-4.2.1/view/collection_tree.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)      760 2023-04-07 09:17:52.000000 gnuhealth_webdav3_server-4.2.1/view/share_form.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)      368 2023-04-07 09:17:52.000000 gnuhealth_webdav3_server-4.2.1/view/share_list.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)    33952 2023-04-07 09:17:52.000000 gnuhealth_webdav3_server-4.2.1/webdav.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)     6864 2023-04-07 09:17:52.000000 gnuhealth_webdav3_server-4.2.1/webdav.xml
```

### Comparing `gnuhealth_webdav3_server-4.2.0/PKG-INFO` & `gnuhealth_webdav3_server-4.2.1/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: gnuhealth_webdav3_server
-Version: 4.2.0
+Version: 4.2.1
 Summary: GNU Health WebDAV server for Python 3
 Home-page: https://www.gnuhealth.org
 Download-URL: https://ftp.gnu.org/gnu/health/
 Author: GNU Solidario
 Author-email: health@gnusolidario.org
 License: GPL-3
 Keywords: webdav GNUHealth
```

### Comparing `gnuhealth_webdav3_server-4.2.0/README.rst` & `gnuhealth_webdav3_server-4.2.1/README.rst`

 * *Files identical despite different names*

### Comparing `gnuhealth_webdav3_server-4.2.0/__init__.py` & `gnuhealth_webdav3_server-4.2.1/__init__.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_webdav3_server-4.2.0/bin/gnuhealth-webdav-server` & `gnuhealth_webdav3_server-4.2.1/bin/gnuhealth-webdav-server`

 * *Files identical despite different names*

### Comparing `gnuhealth_webdav3_server-4.2.0/data/messages/messages.xml` & `gnuhealth_webdav3_server-4.2.1/data/messages/messages.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_webdav3_server-4.2.0/doc/index.rst` & `gnuhealth_webdav3_server-4.2.1/doc/index.rst`

 * *Files identical despite different names*

### Comparing `gnuhealth_webdav3_server-4.2.0/gnuhealth_webdav3_server.egg-info/PKG-INFO` & `gnuhealth_webdav3_server-4.2.1/gnuhealth_webdav3_server.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: gnuhealth-webdav3-server
-Version: 4.2.0
+Version: 4.2.1
 Summary: GNU Health WebDAV server for Python 3
 Home-page: https://www.gnuhealth.org
 Download-URL: https://ftp.gnu.org/gnu/health/
 Author: GNU Solidario
 Author-email: health@gnusolidario.org
 License: GPL-3
 Keywords: webdav GNUHealth
```

### Comparing `gnuhealth_webdav3_server-4.2.0/gnuhealth_webdav3_server.egg-info/SOURCES.txt` & `gnuhealth_webdav3_server-4.2.1/gnuhealth_webdav3_server.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `gnuhealth_webdav3_server-4.2.0/locale/bg.po` & `gnuhealth_webdav3_server-4.2.1/locale/bg.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_webdav3_server-4.2.0/locale/ca.po` & `gnuhealth_webdav3_server-4.2.1/locale/ca.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_webdav3_server-4.2.0/locale/cs.po` & `gnuhealth_webdav3_server-4.2.1/locale/cs.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_webdav3_server-4.2.0/locale/de.po` & `gnuhealth_webdav3_server-4.2.1/locale/de.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_webdav3_server-4.2.0/locale/es.po` & `gnuhealth_webdav3_server-4.2.1/locale/es.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_webdav3_server-4.2.0/locale/fr.po` & `gnuhealth_webdav3_server-4.2.1/locale/fr.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_webdav3_server-4.2.0/locale/hu_HU.po` & `gnuhealth_webdav3_server-4.2.1/locale/hu_HU.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_webdav3_server-4.2.0/locale/it_IT.po` & `gnuhealth_webdav3_server-4.2.1/locale/it_IT.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_webdav3_server-4.2.0/locale/ja_JP.po` & `gnuhealth_webdav3_server-4.2.1/locale/ja_JP.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_webdav3_server-4.2.0/locale/lo.po` & `gnuhealth_webdav3_server-4.2.1/locale/lo.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_webdav3_server-4.2.0/locale/lt.po` & `gnuhealth_webdav3_server-4.2.1/locale/lt.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_webdav3_server-4.2.0/locale/nl.po` & `gnuhealth_webdav3_server-4.2.1/locale/nl.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_webdav3_server-4.2.0/locale/pl.po` & `gnuhealth_webdav3_server-4.2.1/locale/pl.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_webdav3_server-4.2.0/locale/pt_BR.po` & `gnuhealth_webdav3_server-4.2.1/locale/pt_BR.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_webdav3_server-4.2.0/locale/ru.po` & `gnuhealth_webdav3_server-4.2.1/locale/ru.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_webdav3_server-4.2.0/locale/sl.po` & `gnuhealth_webdav3_server-4.2.1/locale/sl.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_webdav3_server-4.2.0/locale/zh_CN.po` & `gnuhealth_webdav3_server-4.2.1/locale/zh_CN.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_webdav3_server-4.2.0/protocol.py` & `gnuhealth_webdav3_server-4.2.1/protocol.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_webdav3_server-4.2.0/server.py` & `gnuhealth_webdav3_server-4.2.1/server.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_webdav3_server-4.2.0/setup.py` & `gnuhealth_webdav3_server-4.2.1/setup.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_webdav3_server-4.2.0/tests/test_webdav.py` & `gnuhealth_webdav3_server-4.2.1/tests/test_webdav.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_webdav3_server-4.2.0/view/attachment_form.xml` & `gnuhealth_webdav3_server-4.2.1/view/attachment_form.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_webdav3_server-4.2.0/view/collection_form.xml` & `gnuhealth_webdav3_server-4.2.1/view/collection_form.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_webdav3_server-4.2.0/view/share_form.xml` & `gnuhealth_webdav3_server-4.2.1/view/share_form.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_webdav3_server-4.2.0/webdav.py` & `gnuhealth_webdav3_server-4.2.1/webdav.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_webdav3_server-4.2.0/webdav.xml` & `gnuhealth_webdav3_server-4.2.1/webdav.xml`

 * *Files identical despite different names*

