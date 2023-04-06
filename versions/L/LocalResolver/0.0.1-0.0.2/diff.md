# Comparing `tmp/LocalResolver-0.0.1.tar.gz` & `tmp/LocalResolver-0.0.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist\LocalResolver-0.0.1.tar", last modified: Tue Jan 19 16:24:20 2021, max compression
+gzip compressed data, was "LocalResolver-0.0.2.tar", last modified: Thu Apr  6 20:40:40 2023, max compression
```

## Comparing `LocalResolver-0.0.1.tar` & `LocalResolver-0.0.2.tar`

### file list

```diff
@@ -1,18 +1,14 @@
-drwxrwxrwx   0        0        0        0 2021-01-19 16:24:20.792714 LocalResolver-0.0.1/
--rw-rw-rw-   0        0        0    35149 2021-01-18 15:47:25.000000 LocalResolver-0.0.1/LICENSE.txt
-drwxrwxrwx   0        0        0        0 2021-01-19 16:24:20.712585 LocalResolver-0.0.1/LocalResolver/
--rw-rw-rw-   0        0        0     3470 2021-01-19 15:52:30.000000 LocalResolver-0.0.1/LocalResolver/NetbiosResolver.py
--rw-rw-rw-   0        0        0     1384 2021-01-19 16:11:16.000000 LocalResolver-0.0.1/LocalResolver/__init__.py
--rw-rw-rw-   0        0        0     4318 2021-01-19 16:22:11.000000 LocalResolver-0.0.1/LocalResolver/__main__.py
-drwxrwxrwx   0        0        0        0 2021-01-19 16:24:20.772665 LocalResolver-0.0.1/LocalResolver.egg-info/
--rw-rw-rw-   0        0        0     1845 2021-01-19 16:24:20.000000 LocalResolver-0.0.1/LocalResolver.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      351 2021-01-19 16:24:20.000000 LocalResolver-0.0.1/LocalResolver.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2021-01-19 16:24:20.000000 LocalResolver-0.0.1/LocalResolver.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       60 2021-01-19 16:24:20.000000 LocalResolver-0.0.1/LocalResolver.egg-info/entry_points.txt
--rw-rw-rw-   0        0        0        6 2021-01-19 16:24:20.000000 LocalResolver-0.0.1/LocalResolver.egg-info/requires.txt
--rw-rw-rw-   0        0        0       14 2021-01-19 16:24:20.000000 LocalResolver-0.0.1/LocalResolver.egg-info/top_level.txt
--rw-rw-rw-   0        0        0       27 2021-01-18 15:47:25.000000 LocalResolver-0.0.1/MANIFEST.in
--rw-rw-rw-   0        0        0     1845 2021-01-19 16:24:20.782877 LocalResolver-0.0.1/PKG-INFO
--rw-rw-rw-   0        0        0      800 2021-01-19 16:12:04.000000 LocalResolver-0.0.1/README.md
--rw-rw-rw-   0        0        0       42 2021-01-19 16:24:20.792714 LocalResolver-0.0.1/setup.cfg
--rw-rw-rw-   0        0        0     1051 2021-01-19 16:11:46.000000 LocalResolver-0.0.1/setup.py
+drwxr-xr-x   0 kali      (1000) kali      (1000)        0 2023-04-06 20:40:40.946742 LocalResolver-0.0.2/
+-rw-r--r--   0 kali      (1000) kali      (1000)    35149 2023-04-06 19:27:34.000000 LocalResolver-0.0.2/LICENSE.txt
+drwxr-xr-x   0 kali      (1000) kali      (1000)        0 2023-04-06 20:40:40.946742 LocalResolver-0.0.2/LocalResolver.egg-info/
+-rw-r--r--   0 kali      (1000) kali      (1000)     2371 2023-04-06 20:40:40.000000 LocalResolver-0.0.2/LocalResolver.egg-info/PKG-INFO
+-rw-r--r--   0 kali      (1000) kali      (1000)      276 2023-04-06 20:40:40.000000 LocalResolver-0.0.2/LocalResolver.egg-info/SOURCES.txt
+-rw-r--r--   0 kali      (1000) kali      (1000)        1 2023-04-06 20:40:40.000000 LocalResolver-0.0.2/LocalResolver.egg-info/dependency_links.txt
+-rw-r--r--   0 kali      (1000) kali      (1000)       59 2023-04-06 20:40:40.000000 LocalResolver-0.0.2/LocalResolver.egg-info/entry_points.txt
+-rw-r--r--   0 kali      (1000) kali      (1000)        6 2023-04-06 20:40:40.000000 LocalResolver-0.0.2/LocalResolver.egg-info/requires.txt
+-rw-r--r--   0 kali      (1000) kali      (1000)       14 2023-04-06 20:40:40.000000 LocalResolver-0.0.2/LocalResolver.egg-info/top_level.txt
+-rw-r--r--   0 kali      (1000) kali      (1000)       27 2023-04-06 19:27:34.000000 LocalResolver-0.0.2/MANIFEST.in
+-rw-r--r--   0 kali      (1000) kali      (1000)     2371 2023-04-06 20:40:40.946742 LocalResolver-0.0.2/PKG-INFO
+-rw-r--r--   0 kali      (1000) kali      (1000)     1174 2023-04-06 20:12:08.000000 LocalResolver-0.0.2/README.md
+-rw-r--r--   0 kali      (1000) kali      (1000)       38 2023-04-06 20:40:40.946742 LocalResolver-0.0.2/setup.cfg
+-rw-r--r--   0 kali      (1000) kali      (1000)     1619 2023-04-06 20:40:36.000000 LocalResolver-0.0.2/setup.py
```

### Comparing `LocalResolver-0.0.1/LICENSE.txt` & `LocalResolver-0.0.2/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `LocalResolver-0.0.1/README.md` & `LocalResolver-0.0.2/README.md`

 * *Files 26% similar despite different names*

```diff
@@ -1,39 +1,52 @@
-# HostnameResolver
+![LocalResolver logo](https://mauricelambert.github.io/info/python/code/LocalResolver_small.png "LocalResolver logo")
+
+# LocalResolver
 
 ## Description
-This package implement netbios and LLMNR query tool in python and HostnameResolver command line tool.
+
+This package implements local hostname resolver tool with scapy (using netbios and LLMNR query).
 
 ## Requirements
-This package require : 
+
+This package require: 
+
  - python3
  - python3 Standard Library
  - Scapy
 
 ## Installation
+
 ```bash
 pip install LocalResolver 
 ```
 
 ## Examples
 
 ### Command lines
+
 ```bash
 HostnameResolver -h
 HostnameResolver 192.168.1.2
 HostnameResolver 192.168.1.3,192.168.1.2,WIN10,HOMEPC,example.com
 ```
 
 ### Python3
+
 ```python
 from LocalResolver import LocalResolver
 
 localResolver = LocalResolver("192.168.1.45", timeout=3)
 hostname = localResolver.resolve_NBTNS()
 hostname = localResolver.resolve_LLMNR()
 ```
 
-## Link
-[Github Page](https://github.com/mauricelambert/LocalResolver)
+## Links
+
+ - [Github Page](https://github.com/mauricelambert/LocalResolver)
+ - [Documentation](https://mauricelambert.github.io/info/python/code/LocalResolver.html)
+ - [Download as python executable](https://mauricelambert.github.io/info/python/code/LocalResolver.pyz)
+ - [Pypi package](https://pypi.org/project/LocalResolver/)
 
 ## Licence
+
 Licensed under the [GPL, version 3](https://www.gnu.org/licenses/).
```

