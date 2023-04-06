# Comparing `tmp/nvchecker-2.8.post1.tar.gz` & `tmp/nvchecker-2.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "nvchecker-2.8.post1.tar", last modified: Mon Apr 11 11:14:56 2022, max compression
+gzip compressed data, was "nvchecker-2.9.tar", last modified: Mon Jun 27 12:38:17 2022, max compression
```

## Comparing `nvchecker-2.8.post1.tar` & `nvchecker-2.9.tar`

### file list

```diff
@@ -1,73 +1,73 @@
-drwxr-xr-x   0 lilydjwg  (1000) lilydjwg  (1000)        0 2022-04-11 11:14:56.101871 nvchecker-2.8.post1/
--rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)     1099 2017-02-28 07:12:21.000000 nvchecker-2.8.post1/LICENSE
--rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)     3048 2022-04-11 11:14:56.101871 nvchecker-2.8.post1/PKG-INFO
--rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)     1768 2021-12-29 08:28:19.000000 nvchecker-2.8.post1/README.rst
-drwxr-xr-x   0 lilydjwg  (1000) lilydjwg  (1000)        0 2022-04-11 11:14:56.095204 nvchecker-2.8.post1/nvchecker/
--rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)      106 2022-04-11 11:14:50.000000 nvchecker-2.8.post1/nvchecker/__init__.py
--rwxr-xr-x   0 lilydjwg  (1000) lilydjwg  (1000)     3322 2022-02-04 08:53:56.000000 nvchecker-2.8.post1/nvchecker/__main__.py
--rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)      387 2021-10-05 03:29:35.000000 nvchecker-2.8.post1/nvchecker/api.py
--rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)    10985 2022-01-20 06:41:49.000000 nvchecker-2.8.post1/nvchecker/core.py
--rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)      671 2021-10-05 03:29:35.000000 nvchecker-2.8.post1/nvchecker/ctxvars.py
-drwxr-xr-x   0 lilydjwg  (1000) lilydjwg  (1000)        0 2022-04-11 11:14:56.098537 nvchecker-2.8.post1/nvchecker/httpclient/
--rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)     1121 2021-10-05 03:29:35.000000 nvchecker-2.8.post1/nvchecker/httpclient/__init__.py
--rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)     2279 2022-04-07 05:43:15.000000 nvchecker-2.8.post1/nvchecker/httpclient/aiohttp_httpclient.py
--rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)     3016 2021-10-05 03:29:35.000000 nvchecker-2.8.post1/nvchecker/httpclient/base.py
--rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)     2059 2022-04-07 05:38:17.000000 nvchecker-2.8.post1/nvchecker/httpclient/httpx_httpclient.py
--rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)     2377 2021-10-05 03:29:35.000000 nvchecker-2.8.post1/nvchecker/httpclient/tornado_httpclient.py
-drwxr-xr-x   0 lilydjwg  (1000) lilydjwg  (1000)        0 2022-04-11 11:14:56.098537 nvchecker-2.8.post1/nvchecker/lib/
--rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)        0 2021-07-18 09:07:36.000000 nvchecker-2.8.post1/nvchecker/lib/__init__.py
--rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)     3634 2021-10-05 03:29:35.000000 nvchecker-2.8.post1/nvchecker/lib/nicelogger.py
--rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)    17385 2021-10-05 03:29:35.000000 nvchecker-2.8.post1/nvchecker/lib/packaging_version.py
--rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)     3306 2021-10-05 03:29:35.000000 nvchecker-2.8.post1/nvchecker/slogconf.py
--rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)      600 2021-10-05 03:29:35.000000 nvchecker-2.8.post1/nvchecker/sortversion.py
--rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)     5662 2022-04-02 04:07:13.000000 nvchecker-2.8.post1/nvchecker/tools.py
--rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)     7738 2021-12-29 08:36:03.000000 nvchecker-2.8.post1/nvchecker/util.py
-drwxr-xr-x   0 lilydjwg  (1000) lilydjwg  (1000)        0 2022-04-11 11:14:56.095204 nvchecker-2.8.post1/nvchecker.egg-info/
--rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)     3048 2022-04-11 11:14:56.000000 nvchecker-2.8.post1/nvchecker.egg-info/PKG-INFO
--rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)     1740 2022-04-11 11:14:56.000000 nvchecker-2.8.post1/nvchecker.egg-info/SOURCES.txt
--rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)        1 2022-04-11 11:14:56.000000 nvchecker-2.8.post1/nvchecker.egg-info/dependency_links.txt
--rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)      113 2022-04-11 11:14:56.000000 nvchecker-2.8.post1/nvchecker.egg-info/entry_points.txt
--rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)      134 2022-04-11 11:14:56.000000 nvchecker-2.8.post1/nvchecker.egg-info/requires.txt
--rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)       27 2022-04-11 11:14:56.000000 nvchecker-2.8.post1/nvchecker.egg-info/top_level.txt
--rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)        1 2022-04-11 11:14:00.000000 nvchecker-2.8.post1/nvchecker.egg-info/zip-safe
-drwxr-xr-x   0 lilydjwg  (1000) lilydjwg  (1000)        0 2022-04-11 11:14:56.101871 nvchecker-2.8.post1/nvchecker_source/
--rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)     1200 2021-10-05 03:29:35.000000 nvchecker-2.8.post1/nvchecker_source/alpm.py
--rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)     2180 2022-04-02 04:05:58.000000 nvchecker-2.8.post1/nvchecker_source/android_sdk.py
--rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)      310 2021-10-05 03:29:35.000000 nvchecker-2.8.post1/nvchecker_source/anitya.py
--rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)     4245 2021-10-05 03:29:35.000000 nvchecker-2.8.post1/nvchecker_source/apt.py
--rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)      961 2021-10-05 03:29:35.000000 nvchecker-2.8.post1/nvchecker_source/archpkg.py
--rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)     2841 2021-10-05 03:29:35.000000 nvchecker-2.8.post1/nvchecker_source/aur.py
--rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)     1970 2022-02-08 06:41:51.000000 nvchecker-2.8.post1/nvchecker_source/bitbucket.py
--rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)     1001 2021-10-05 03:29:35.000000 nvchecker-2.8.post1/nvchecker_source/cmd.py
--rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)      539 2021-10-05 03:29:35.000000 nvchecker-2.8.post1/nvchecker_source/combiner.py
--rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)     3221 2021-10-05 03:29:35.000000 nvchecker-2.8.post1/nvchecker_source/container.py
--rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)      314 2021-10-05 03:29:35.000000 nvchecker-2.8.post1/nvchecker_source/cpan.py
--rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)      710 2022-02-23 03:11:51.000000 nvchecker-2.8.post1/nvchecker_source/cran.py
--rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)      355 2021-10-05 03:29:35.000000 nvchecker-2.8.post1/nvchecker_source/cratesio.py
--rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)      748 2021-10-05 03:29:35.000000 nvchecker-2.8.post1/nvchecker_source/debianpkg.py
--rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)      314 2021-10-05 03:29:35.000000 nvchecker-2.8.post1/nvchecker_source/gems.py
--rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)      688 2021-10-05 03:29:35.000000 nvchecker-2.8.post1/nvchecker_source/git.py
--rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)     1237 2021-10-05 03:29:35.000000 nvchecker-2.8.post1/nvchecker_source/gitea.py
--rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)     3930 2021-11-04 08:28:14.000000 nvchecker-2.8.post1/nvchecker_source/github.py
--rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)     1886 2021-10-05 03:29:35.000000 nvchecker-2.8.post1/nvchecker_source/gitlab.py
--rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)      325 2021-10-05 03:29:35.000000 nvchecker-2.8.post1/nvchecker_source/hackage.py
--rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)     1111 2021-10-05 03:29:35.000000 nvchecker-2.8.post1/nvchecker_source/htmlparser.py
--rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)     1027 2021-10-05 03:29:35.000000 nvchecker-2.8.post1/nvchecker_source/httpheader.py
--rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)      174 2021-10-05 03:29:35.000000 nvchecker-2.8.post1/nvchecker_source/manual.py
--rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)      427 2021-10-05 03:29:35.000000 nvchecker-2.8.post1/nvchecker_source/none.py
--rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)      740 2021-10-05 03:29:35.000000 nvchecker-2.8.post1/nvchecker_source/npm.py
--rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)      427 2021-10-05 03:29:35.000000 nvchecker-2.8.post1/nvchecker_source/openvsx.py
--rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)      509 2021-10-05 03:29:35.000000 nvchecker-2.8.post1/nvchecker_source/packagist.py
--rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)      526 2021-10-05 03:29:35.000000 nvchecker-2.8.post1/nvchecker_source/pacman.py
--rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)      604 2021-10-05 03:29:35.000000 nvchecker-2.8.post1/nvchecker_source/pagure.py
--rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)      529 2021-10-05 03:29:35.000000 nvchecker-2.8.post1/nvchecker_source/pypi.py
--rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)     1067 2021-11-06 02:42:16.000000 nvchecker-2.8.post1/nvchecker_source/regex.py
--rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)      896 2021-10-05 03:29:35.000000 nvchecker-2.8.post1/nvchecker_source/repology.py
--rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)     1066 2022-02-23 03:10:49.000000 nvchecker-2.8.post1/nvchecker_source/sparkle.py
--rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)     1246 2021-10-05 03:29:35.000000 nvchecker-2.8.post1/nvchecker_source/ubuntupkg.py
--rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)     1212 2021-10-05 03:29:35.000000 nvchecker-2.8.post1/nvchecker_source/vsmarketplace.py
-drwxr-xr-x   0 lilydjwg  (1000) lilydjwg  (1000)        0 2022-04-11 11:14:56.101871 nvchecker-2.8.post1/scripts/
--rwxr-xr-x   0 lilydjwg  (1000) lilydjwg  (1000)     1997 2021-10-05 03:29:35.000000 nvchecker-2.8.post1/scripts/nvchecker-ini2toml
--rwxr-xr-x   0 lilydjwg  (1000) lilydjwg  (1000)     1580 2021-10-05 03:29:35.000000 nvchecker-2.8.post1/scripts/nvchecker-notify
--rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)      119 2022-04-11 11:14:56.101871 nvchecker-2.8.post1/setup.cfg
--rwxr-xr-x   0 lilydjwg  (1000) lilydjwg  (1000)     2117 2022-04-11 11:10:57.000000 nvchecker-2.8.post1/setup.py
+drwxr-xr-x   0 lilydjwg  (1000) lilydjwg  (1000)        0 2022-06-27 12:38:17.043736 nvchecker-2.9/
+-rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)     1099 2017-02-28 07:12:21.000000 nvchecker-2.9/LICENSE
+-rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)     3073 2022-06-27 12:38:17.043736 nvchecker-2.9/PKG-INFO
+-rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)     1768 2021-12-29 08:28:19.000000 nvchecker-2.9/README.rst
+drwxr-xr-x   0 lilydjwg  (1000) lilydjwg  (1000)        0 2022-06-27 12:38:17.037069 nvchecker-2.9/nvchecker/
+-rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)      100 2022-06-27 12:33:36.000000 nvchecker-2.9/nvchecker/__init__.py
+-rwxr-xr-x   0 lilydjwg  (1000) lilydjwg  (1000)     3322 2022-02-04 08:53:56.000000 nvchecker-2.9/nvchecker/__main__.py
+-rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)      387 2021-10-05 03:29:35.000000 nvchecker-2.9/nvchecker/api.py
+-rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)    11119 2022-06-12 06:18:06.000000 nvchecker-2.9/nvchecker/core.py
+-rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)      671 2021-10-05 03:29:35.000000 nvchecker-2.9/nvchecker/ctxvars.py
+drwxr-xr-x   0 lilydjwg  (1000) lilydjwg  (1000)        0 2022-06-27 12:38:17.037069 nvchecker-2.9/nvchecker/httpclient/
+-rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)     1121 2021-10-05 03:29:35.000000 nvchecker-2.9/nvchecker/httpclient/__init__.py
+-rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)     2279 2022-04-07 05:43:15.000000 nvchecker-2.9/nvchecker/httpclient/aiohttp_httpclient.py
+-rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)     3018 2022-04-21 09:14:37.000000 nvchecker-2.9/nvchecker/httpclient/base.py
+-rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)     2059 2022-04-07 05:38:17.000000 nvchecker-2.9/nvchecker/httpclient/httpx_httpclient.py
+-rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)     2377 2021-10-05 03:29:35.000000 nvchecker-2.9/nvchecker/httpclient/tornado_httpclient.py
+drwxr-xr-x   0 lilydjwg  (1000) lilydjwg  (1000)        0 2022-06-27 12:38:17.037069 nvchecker-2.9/nvchecker/lib/
+-rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)        0 2021-07-18 09:07:36.000000 nvchecker-2.9/nvchecker/lib/__init__.py
+-rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)     3634 2021-10-05 03:29:35.000000 nvchecker-2.9/nvchecker/lib/nicelogger.py
+-rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)    17385 2021-10-05 03:29:35.000000 nvchecker-2.9/nvchecker/lib/packaging_version.py
+-rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)     3306 2021-10-05 03:29:35.000000 nvchecker-2.9/nvchecker/slogconf.py
+-rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)      905 2022-06-05 06:41:18.000000 nvchecker-2.9/nvchecker/sortversion.py
+-rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)     5717 2022-06-05 06:41:29.000000 nvchecker-2.9/nvchecker/tools.py
+-rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)     7723 2022-06-05 06:36:16.000000 nvchecker-2.9/nvchecker/util.py
+drwxr-xr-x   0 lilydjwg  (1000) lilydjwg  (1000)        0 2022-06-27 12:38:17.037069 nvchecker-2.9/nvchecker.egg-info/
+-rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)     3073 2022-06-27 12:38:16.000000 nvchecker-2.9/nvchecker.egg-info/PKG-INFO
+-rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)     1740 2022-06-27 12:38:16.000000 nvchecker-2.9/nvchecker.egg-info/SOURCES.txt
+-rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)        1 2022-06-27 12:38:16.000000 nvchecker-2.9/nvchecker.egg-info/dependency_links.txt
+-rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)      112 2022-06-27 12:38:16.000000 nvchecker-2.9/nvchecker.egg-info/entry_points.txt
+-rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)      167 2022-06-27 12:38:16.000000 nvchecker-2.9/nvchecker.egg-info/requires.txt
+-rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)       27 2022-06-27 12:38:16.000000 nvchecker-2.9/nvchecker.egg-info/top_level.txt
+-rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)        1 2022-04-11 11:14:00.000000 nvchecker-2.9/nvchecker.egg-info/zip-safe
+drwxr-xr-x   0 lilydjwg  (1000) lilydjwg  (1000)        0 2022-06-27 12:38:17.040403 nvchecker-2.9/nvchecker_source/
+-rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)     1200 2021-10-05 03:29:35.000000 nvchecker-2.9/nvchecker_source/alpm.py
+-rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)     2180 2022-04-02 04:05:58.000000 nvchecker-2.9/nvchecker_source/android_sdk.py
+-rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)      310 2021-10-05 03:29:35.000000 nvchecker-2.9/nvchecker_source/anitya.py
+-rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)     4245 2022-04-21 09:14:52.000000 nvchecker-2.9/nvchecker_source/apt.py
+-rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)      961 2021-10-05 03:29:35.000000 nvchecker-2.9/nvchecker_source/archpkg.py
+-rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)     2841 2021-10-05 03:29:35.000000 nvchecker-2.9/nvchecker_source/aur.py
+-rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)     1970 2022-02-08 06:41:51.000000 nvchecker-2.9/nvchecker_source/bitbucket.py
+-rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)     1001 2021-10-05 03:29:35.000000 nvchecker-2.9/nvchecker_source/cmd.py
+-rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)      539 2021-10-05 03:29:35.000000 nvchecker-2.9/nvchecker_source/combiner.py
+-rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)     3221 2021-10-05 03:29:35.000000 nvchecker-2.9/nvchecker_source/container.py
+-rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)      314 2021-10-05 03:29:35.000000 nvchecker-2.9/nvchecker_source/cpan.py
+-rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)      710 2022-02-23 03:11:51.000000 nvchecker-2.9/nvchecker_source/cran.py
+-rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)      355 2021-10-05 03:29:35.000000 nvchecker-2.9/nvchecker_source/cratesio.py
+-rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)      748 2021-10-05 03:29:35.000000 nvchecker-2.9/nvchecker_source/debianpkg.py
+-rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)      314 2021-10-05 03:29:35.000000 nvchecker-2.9/nvchecker_source/gems.py
+-rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)      688 2021-10-05 03:29:35.000000 nvchecker-2.9/nvchecker_source/git.py
+-rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)     1237 2021-10-05 03:29:35.000000 nvchecker-2.9/nvchecker_source/gitea.py
+-rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)     3930 2021-11-04 08:28:14.000000 nvchecker-2.9/nvchecker_source/github.py
+-rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)     1886 2021-10-05 03:29:35.000000 nvchecker-2.9/nvchecker_source/gitlab.py
+-rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)      325 2021-10-05 03:29:35.000000 nvchecker-2.9/nvchecker_source/hackage.py
+-rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)     1215 2022-06-12 04:30:59.000000 nvchecker-2.9/nvchecker_source/htmlparser.py
+-rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)     1027 2021-10-05 03:29:35.000000 nvchecker-2.9/nvchecker_source/httpheader.py
+-rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)      174 2021-10-05 03:29:35.000000 nvchecker-2.9/nvchecker_source/manual.py
+-rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)      427 2021-10-05 03:29:35.000000 nvchecker-2.9/nvchecker_source/none.py
+-rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)      740 2021-10-05 03:29:35.000000 nvchecker-2.9/nvchecker_source/npm.py
+-rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)      427 2021-10-05 03:29:35.000000 nvchecker-2.9/nvchecker_source/openvsx.py
+-rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)      509 2021-10-05 03:29:35.000000 nvchecker-2.9/nvchecker_source/packagist.py
+-rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)      526 2021-10-05 03:29:35.000000 nvchecker-2.9/nvchecker_source/pacman.py
+-rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)      604 2021-10-05 03:29:35.000000 nvchecker-2.9/nvchecker_source/pagure.py
+-rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)      529 2021-10-05 03:29:35.000000 nvchecker-2.9/nvchecker_source/pypi.py
+-rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)     1067 2021-11-06 02:42:16.000000 nvchecker-2.9/nvchecker_source/regex.py
+-rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)      896 2021-10-05 03:29:35.000000 nvchecker-2.9/nvchecker_source/repology.py
+-rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)     1066 2022-02-23 03:10:49.000000 nvchecker-2.9/nvchecker_source/sparkle.py
+-rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)     1246 2021-10-05 03:29:35.000000 nvchecker-2.9/nvchecker_source/ubuntupkg.py
+-rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)     1212 2022-06-18 08:23:00.000000 nvchecker-2.9/nvchecker_source/vsmarketplace.py
+drwxr-xr-x   0 lilydjwg  (1000) lilydjwg  (1000)        0 2022-06-27 12:38:17.040403 nvchecker-2.9/scripts/
+-rwxr-xr-x   0 lilydjwg  (1000) lilydjwg  (1000)     1997 2021-10-05 03:29:35.000000 nvchecker-2.9/scripts/nvchecker-ini2toml
+-rwxr-xr-x   0 lilydjwg  (1000) lilydjwg  (1000)     1580 2021-10-05 03:29:35.000000 nvchecker-2.9/scripts/nvchecker-notify
+-rw-r--r--   0 lilydjwg  (1000) lilydjwg  (1000)      119 2022-06-27 12:38:17.043736 nvchecker-2.9/setup.cfg
+-rwxr-xr-x   0 lilydjwg  (1000) lilydjwg  (1000)     2159 2022-06-05 06:29:41.000000 nvchecker-2.9/setup.py
```

### Comparing `nvchecker-2.8.post1/LICENSE` & `nvchecker-2.9/LICENSE`

 * *Files identical despite different names*

### Comparing `nvchecker-2.8.post1/PKG-INFO` & `nvchecker-2.9/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: nvchecker
-Version: 2.8.post1
+Version: 2.9
 Summary: New version checker for software
 Home-page: https://github.com/lilydjwg/nvchecker
 Author: lilydjwg
 Author-email: lilydjwg@gmail.com
 License: MIT
 Keywords: new version build check
 Platform: any
@@ -25,14 +25,15 @@
 Classifier: Topic :: Internet :: WWW/HTTP
 Classifier: Topic :: Software Development
 Classifier: Topic :: System :: Archiving :: Packaging
 Classifier: Topic :: System :: Software Distribution
 Classifier: Topic :: Utilities
 Description-Content-Type: text/x-rst
 Provides-Extra: vercmp
+Provides-Extra: awesomeversion
 Provides-Extra: pypi
 Provides-Extra: htmlparser
 License-File: LICENSE
 
 **nvchecker** (short for *new version checker*) is for checking if a new version of some software has been released.
 
 This is the version 2.0 branch. For the old version 1.x, please switch to the ``v1.x`` branch.
```

### Comparing `nvchecker-2.8.post1/README.rst` & `nvchecker-2.9/README.rst`

 * *Files identical despite different names*

### Comparing `nvchecker-2.8.post1/nvchecker/__main__.py` & `nvchecker-2.9/nvchecker/__main__.py`

 * *Files identical despite different names*

### Comparing `nvchecker-2.8.post1/nvchecker/core.py` & `nvchecker-2.9/nvchecker/core.py`

 * *Files 2% similar despite different names*

```diff
@@ -307,15 +307,15 @@
     versions = [x for x in versions if x not in ignored]
 
   if not versions:
     return None
 
   sort_version_key = sort_version_keys[
     conf.get("sort_version_key", "parse_version")]
-  versions.sort(key=sort_version_key)
+  versions.sort(key=sort_version_key) # type: ignore
 
   return versions[-1]
 
 def _process_result(r: RawResult) -> Union[Result, Exception]:
   version = r.version
   conf = r.conf
   name = r.name
@@ -362,15 +362,19 @@
   entry_waiter: EntryWaiter,
 ) -> Tuple[VersData, bool]:
   ret = {}
   has_failures = False
   try:
     while True:
       r = await result_q.get()
-      r1 = _process_result(r)
+      try:
+        r1 = _process_result(r)
+      except Exception as e:
+        logger.exception('error processing result', result=r)
+        r1 = e
       if isinstance(r1, Exception):
         entry_waiter.set_exception(r.name, r1)
         has_failures = True
         continue
       check_version_update(oldvers, r1.name, r1.version)
       entry_waiter.set_result(r1.name, r1.version)
       ret[r1.name] = r1.version
```

### Comparing `nvchecker-2.8.post1/nvchecker/ctxvars.py` & `nvchecker-2.9/nvchecker/ctxvars.py`

 * *Files identical despite different names*

### Comparing `nvchecker-2.8.post1/nvchecker/httpclient/__init__.py` & `nvchecker-2.9/nvchecker/httpclient/__init__.py`

 * *Files identical despite different names*

### Comparing `nvchecker-2.8.post1/nvchecker/httpclient/aiohttp_httpclient.py` & `nvchecker-2.9/nvchecker/httpclient/aiohttp_httpclient.py`

 * *Files identical despite different names*

### Comparing `nvchecker-2.8.post1/nvchecker/httpclient/base.py` & `nvchecker-2.9/nvchecker/httpclient/base.py`

 * *Files 5% similar despite different names*

```diff
@@ -23,15 +23,15 @@
     headers: Mapping[str, str],
     body: bytes,
   ) -> None:
     self.headers = headers
     self.body = body
 
   def json(self):
-    '''Convert reponse content to JSON.'''
+    '''Convert response content to JSON.'''
     return _json.loads(self.body.decode('utf-8'))
 
 class BaseSession:
   '''The base class for different HTTP backend.'''
   def setup(
     self,
     concurreny: int = 20,
@@ -91,15 +91,15 @@
         if i == t:
           raise
         else:
           logger.warning('temporary error, retrying',
                          tries = i, exc_info = e)
           continue
 
-    raise Exception('shoud not reach')
+    raise Exception('should not reach')
 
   async def request_impl(
     self, url: str, *,
     method: str,
     proxy: Optional[str] = None,
     headers: Dict[str, str] = {},
     follow_redirects: bool = True,
```

### Comparing `nvchecker-2.8.post1/nvchecker/httpclient/httpx_httpclient.py` & `nvchecker-2.9/nvchecker/httpclient/httpx_httpclient.py`

 * *Files identical despite different names*

### Comparing `nvchecker-2.8.post1/nvchecker/httpclient/tornado_httpclient.py` & `nvchecker-2.9/nvchecker/httpclient/tornado_httpclient.py`

 * *Files identical despite different names*

### Comparing `nvchecker-2.8.post1/nvchecker/lib/nicelogger.py` & `nvchecker-2.9/nvchecker/lib/nicelogger.py`

 * *Files identical despite different names*

### Comparing `nvchecker-2.8.post1/nvchecker/lib/packaging_version.py` & `nvchecker-2.9/nvchecker/lib/packaging_version.py`

 * *Files identical despite different names*

### Comparing `nvchecker-2.8.post1/nvchecker/slogconf.py` & `nvchecker-2.9/nvchecker/slogconf.py`

 * *Files identical despite different names*

### Comparing `nvchecker-2.8.post1/nvchecker/tools.py` & `nvchecker-2.9/nvchecker/tools.py`

 * *Files 2% similar despite different names*

```diff
@@ -74,15 +74,16 @@
                       help='Output JSON array of dictionaries with {name, newver, oldver, [delta]} '
                            '(or array of names if --quiet)')
   parser.add_argument('-q', '--quiet', action='store_true',
                       help="Quiet mode, output only the names.")
   parser.add_argument('-a', '--all', action='store_true',
                       help="Include unchanged versions.")
   parser.add_argument('-s', '--sort',
-                      choices=('parse_version', 'vercmp', 'none'), default='parse_version',
+                      choices=('parse_version', 'vercmp', 'awesomeversion', 'none'),
+                      default='parse_version',
                       help='Version compare method to backwards the arrow '
                            '(default: parse_version)')
   parser.add_argument('-n', '--newer', action='store_true',
                       help='Shows only the newer ones according to --sort.')
   parser.add_argument('--exit-status', action='store_true',
                       help="exit with status 4 if there are updates")
   args = parser.parse_args()
@@ -121,15 +122,15 @@
       elif args.sort == "none":
         diff['delta'] = 'new'  # assume it's a new version if we're not comparing
 
       else:
         from .sortversion import sort_version_keys
         version = sort_version_keys[args.sort]
 
-        if version(oldver) > version(newver):
+        if version(oldver) > version(newver): # type: ignore
           if args.newer:
             continue  # don't store this diff
           diff['delta'] = 'old'
         else:
           diff['delta'] = 'new'
 
     elif oldver is None:
```

### Comparing `nvchecker-2.8.post1/nvchecker/util.py` & `nvchecker-2.9/nvchecker/util.py`

 * *Files 1% similar despite different names*

```diff
@@ -190,15 +190,15 @@
       cached = self.cache.get(key)
       if cached is None:
         coro = func(key)
         fu = asyncio.create_task(coro)
         self.cache[key] = fu
 
     if asyncio.isfuture(cached): # pending
-      return await cached # type: ignore
+      return await cached
     elif cached is not None: # cached
       return cached
     else: # not cached
       r = await fu
       self.cache[key] = r
       return r
```

### Comparing `nvchecker-2.8.post1/nvchecker.egg-info/PKG-INFO` & `nvchecker-2.9/nvchecker.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: nvchecker
-Version: 2.8.post1
+Version: 2.9
 Summary: New version checker for software
 Home-page: https://github.com/lilydjwg/nvchecker
 Author: lilydjwg
 Author-email: lilydjwg@gmail.com
 License: MIT
 Keywords: new version build check
 Platform: any
@@ -25,14 +25,15 @@
 Classifier: Topic :: Internet :: WWW/HTTP
 Classifier: Topic :: Software Development
 Classifier: Topic :: System :: Archiving :: Packaging
 Classifier: Topic :: System :: Software Distribution
 Classifier: Topic :: Utilities
 Description-Content-Type: text/x-rst
 Provides-Extra: vercmp
+Provides-Extra: awesomeversion
 Provides-Extra: pypi
 Provides-Extra: htmlparser
 License-File: LICENSE
 
 **nvchecker** (short for *new version checker*) is for checking if a new version of some software has been released.
 
 This is the version 2.0 branch. For the old version 1.x, please switch to the ``v1.x`` branch.
```

### Comparing `nvchecker-2.8.post1/nvchecker.egg-info/SOURCES.txt` & `nvchecker-2.9/nvchecker.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `nvchecker-2.8.post1/nvchecker_source/alpm.py` & `nvchecker-2.9/nvchecker_source/alpm.py`

 * *Files identical despite different names*

### Comparing `nvchecker-2.8.post1/nvchecker_source/android_sdk.py` & `nvchecker-2.9/nvchecker_source/android_sdk.py`

 * *Files identical despite different names*

### Comparing `nvchecker-2.8.post1/nvchecker_source/apt.py` & `nvchecker-2.9/nvchecker_source/apt.py`

 * *Files 1% similar despite different names*

```diff
@@ -131,15 +131,15 @@
   mirror = conf['mirror']
   suite = conf['suite']
   repo = conf.get('repo', 'main')
   arch = conf.get('arch', 'amd64')
   strip_release = conf.get('strip_release', False)
 
   if srcpkg and pkg:
-    raise GetVersionError('Setting both srcpkg and pkg is ambigious')
+    raise GetVersionError('Setting both srcpkg and pkg is ambiguous')
   elif not srcpkg and not pkg:
     pkg = name
 
   apt_release = await cache.get(
     APT_RELEASE_URL % (mirror, suite), get_url) # type: ignore
   for suffix in APT_PACKAGES_SUFFIX_PREFER:
     packages_path = APT_PACKAGES_PATH % (repo, arch, suffix)
```

### Comparing `nvchecker-2.8.post1/nvchecker_source/archpkg.py` & `nvchecker-2.9/nvchecker_source/archpkg.py`

 * *Files identical despite different names*

### Comparing `nvchecker-2.8.post1/nvchecker_source/aur.py` & `nvchecker-2.9/nvchecker_source/aur.py`

 * *Files identical despite different names*

### Comparing `nvchecker-2.8.post1/nvchecker_source/bitbucket.py` & `nvchecker-2.9/nvchecker_source/bitbucket.py`

 * *Files identical despite different names*

### Comparing `nvchecker-2.8.post1/nvchecker_source/cmd.py` & `nvchecker-2.9/nvchecker_source/cmd.py`

 * *Files identical despite different names*

### Comparing `nvchecker-2.8.post1/nvchecker_source/combiner.py` & `nvchecker-2.9/nvchecker_source/combiner.py`

 * *Files identical despite different names*

### Comparing `nvchecker-2.8.post1/nvchecker_source/container.py` & `nvchecker-2.9/nvchecker_source/container.py`

 * *Files identical despite different names*

### Comparing `nvchecker-2.8.post1/nvchecker_source/cran.py` & `nvchecker-2.9/nvchecker_source/cran.py`

 * *Files identical despite different names*

### Comparing `nvchecker-2.8.post1/nvchecker_source/debianpkg.py` & `nvchecker-2.9/nvchecker_source/debianpkg.py`

 * *Files identical despite different names*

### Comparing `nvchecker-2.8.post1/nvchecker_source/git.py` & `nvchecker-2.9/nvchecker_source/git.py`

 * *Files identical despite different names*

### Comparing `nvchecker-2.8.post1/nvchecker_source/gitea.py` & `nvchecker-2.9/nvchecker_source/gitea.py`

 * *Files identical despite different names*

### Comparing `nvchecker-2.8.post1/nvchecker_source/github.py` & `nvchecker-2.9/nvchecker_source/github.py`

 * *Files identical despite different names*

### Comparing `nvchecker-2.8.post1/nvchecker_source/gitlab.py` & `nvchecker-2.9/nvchecker_source/gitlab.py`

 * *Files identical despite different names*

### Comparing `nvchecker-2.8.post1/nvchecker_source/htmlparser.py` & `nvchecker-2.9/nvchecker_source/htmlparser.py`

 * *Files 16% similar despite different names*

```diff
@@ -21,14 +21,21 @@
   else:
     res = await session.post(conf['url'], body = data, headers = {
         'Content-Type': conf.get('post_data_type', 'application/x-www-form-urlencoded')
       })
   doc = html.fromstring(res.body, base_url=conf['url'], parser=parser)
 
   try:
-    version = doc.xpath(conf.get('xpath'))
+    els = doc.xpath(conf.get('xpath'))
   except ValueError:
     if not conf.get('missing_ok', False):
       raise GetVersionError('version string not found.')
   except etree.XPathEvalError as e:
     raise GetVersionError('bad xpath', exc_info=e)
+
+  version = [
+    str(el)
+    if isinstance(el, str)
+    else str(el.text_content())
+    for el in els
+  ]
   return version
```

### Comparing `nvchecker-2.8.post1/nvchecker_source/httpheader.py` & `nvchecker-2.9/nvchecker_source/httpheader.py`

 * *Files identical despite different names*

### Comparing `nvchecker-2.8.post1/nvchecker_source/npm.py` & `nvchecker-2.9/nvchecker_source/npm.py`

 * *Files identical despite different names*

### Comparing `nvchecker-2.8.post1/nvchecker_source/pacman.py` & `nvchecker-2.9/nvchecker_source/pacman.py`

 * *Files identical despite different names*

### Comparing `nvchecker-2.8.post1/nvchecker_source/pagure.py` & `nvchecker-2.9/nvchecker_source/pagure.py`

 * *Files identical despite different names*

### Comparing `nvchecker-2.8.post1/nvchecker_source/pypi.py` & `nvchecker-2.9/nvchecker_source/pypi.py`

 * *Files identical despite different names*

### Comparing `nvchecker-2.8.post1/nvchecker_source/regex.py` & `nvchecker-2.9/nvchecker_source/regex.py`

 * *Files identical despite different names*

### Comparing `nvchecker-2.8.post1/nvchecker_source/repology.py` & `nvchecker-2.9/nvchecker_source/repology.py`

 * *Files identical despite different names*

### Comparing `nvchecker-2.8.post1/nvchecker_source/sparkle.py` & `nvchecker-2.9/nvchecker_source/sparkle.py`

 * *Files identical despite different names*

### Comparing `nvchecker-2.8.post1/nvchecker_source/ubuntupkg.py` & `nvchecker-2.9/nvchecker_source/ubuntupkg.py`

 * *Files identical despite different names*

### Comparing `nvchecker-2.8.post1/nvchecker_source/vsmarketplace.py` & `nvchecker-2.9/nvchecker_source/vsmarketplace.py`

 * *Files 1% similar despite different names*

```diff
@@ -21,15 +21,15 @@
       {
         'criteria': [
           {
             'filterType': 8,
             'value': 'Microsoft.VisualStudio.Code'
           },
           {
-            'filterType': 10,
+            'filterType': 7,
             'value': name
           },
           {
             'filterType': 12,
             'value': '4096'
           }
         ],
@@ -47,8 +47,8 @@
     API_URL,
     headers = HEADERS,
     json = q,
   )
   j = res.json()
 
   version = j['results'][0]['extensions'][0]['versions'][0]['version']
-  return version
+  return version
```

### Comparing `nvchecker-2.8.post1/scripts/nvchecker-ini2toml` & `nvchecker-2.9/scripts/nvchecker-ini2toml`

 * *Files identical despite different names*

### Comparing `nvchecker-2.8.post1/scripts/nvchecker-notify` & `nvchecker-2.9/scripts/nvchecker-notify`

 * *Files identical despite different names*

### Comparing `nvchecker-2.8.post1/setup.py` & `nvchecker-2.9/setup.py`

 * *Files 4% similar despite different names*

```diff
@@ -20,14 +20,15 @@
   platforms = 'any',
   zip_safe = True,
 
   packages = find_namespace_packages(include=['nvchecker*']),
   install_requires = ['setuptools; python_version<"3.8"', 'tomli', 'structlog', 'appdirs', 'tornado>=6', 'pycurl'],
   extras_require = {
     'vercmp': ['pyalpm'],
+    'awesomeversion': ['awesomeversion'],
     'pypi': ['packaging'],
     'htmlparser': ['lxml'],
   },
   tests_require = [
     'pytest',
     'pytest-asyncio',
     'pytest-httpbin',
```

