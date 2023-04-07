# Comparing `tmp/stactools-sentinel1-0.5.2.tar.gz` & `tmp/stactools-sentinel1-0.5.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "stactools-sentinel1-0.5.2.tar", last modified: Thu Apr  6 21:00:07 2023, max compression
+gzip compressed data, was "stactools-sentinel1-0.5.3.tar", last modified: Fri Apr  7 13:56:33 2023, max compression
```

## Comparing `stactools-sentinel1-0.5.2.tar` & `stactools-sentinel1-0.5.3.tar`

### file list

```diff
@@ -1,32 +1,32 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:00:07.711086 stactools-sentinel1-0.5.2/
--rw-r--r--   0 runner    (1001) docker     (123)      641 2023-04-06 20:59:48.000000 stactools-sentinel1-0.5.2/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)     4356 2023-04-06 21:00:07.711086 stactools-sentinel1-0.5.2/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     3569 2023-04-06 20:59:48.000000 stactools-sentinel1-0.5.2/README.md
--rw-r--r--   0 runner    (1001) docker     (123)      122 2023-04-06 20:59:48.000000 stactools-sentinel1-0.5.2/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)      971 2023-04-06 21:00:07.711086 stactools-sentinel1-0.5.2/setup.cfg
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:00:07.707086 stactools-sentinel1-0.5.2/src/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:00:07.707086 stactools-sentinel1-0.5.2/src/stactools/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:00:07.707086 stactools-sentinel1-0.5.2/src/stactools/sentinel1/
--rw-r--r--   0 runner    (1001) docker     (123)      311 2023-04-06 20:59:48.000000 stactools-sentinel1-0.5.2/src/stactools/sentinel1/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      421 2023-04-06 20:59:48.000000 stactools-sentinel1-0.5.2/src/stactools/sentinel1/commands.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:00:07.711086 stactools-sentinel1-0.5.2/src/stactools/sentinel1/grd/
--rw-r--r--   0 runner    (1001) docker     (123)      101 2023-04-06 20:59:48.000000 stactools-sentinel1-0.5.2/src/stactools/sentinel1/grd/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1677 2023-04-06 20:59:48.000000 stactools-sentinel1-0.5.2/src/stactools/sentinel1/grd/bands.py
--rw-r--r--   0 runner    (1001) docker     (123)     1598 2023-04-06 20:59:48.000000 stactools-sentinel1-0.5.2/src/stactools/sentinel1/grd/commands.py
--rw-r--r--   0 runner    (1001) docker     (123)    12244 2023-04-06 20:59:48.000000 stactools-sentinel1-0.5.2/src/stactools/sentinel1/grd/constants.py
--rw-r--r--   0 runner    (1001) docker     (123)     9320 2023-04-06 20:59:48.000000 stactools-sentinel1-0.5.2/src/stactools/sentinel1/grd/metadata_links.py
--rw-r--r--   0 runner    (1001) docker     (123)     7240 2023-04-06 20:59:48.000000 stactools-sentinel1-0.5.2/src/stactools/sentinel1/grd/product_metadata.py
--rw-r--r--   0 runner    (1001) docker     (123)     4144 2023-04-06 20:59:48.000000 stactools-sentinel1-0.5.2/src/stactools/sentinel1/grd/properties.py
--rw-r--r--   0 runner    (1001) docker     (123)     7134 2023-04-06 20:59:48.000000 stactools-sentinel1-0.5.2/src/stactools/sentinel1/grd/stac.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:00:07.711086 stactools-sentinel1-0.5.2/src/stactools/sentinel1/rtc/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 20:59:48.000000 stactools-sentinel1-0.5.2/src/stactools/sentinel1/rtc/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2058 2023-04-06 20:59:48.000000 stactools-sentinel1-0.5.2/src/stactools/sentinel1/rtc/commands.py
--rw-r--r--   0 runner    (1001) docker     (123)     3307 2023-04-06 20:59:48.000000 stactools-sentinel1-0.5.2/src/stactools/sentinel1/rtc/constants.py
--rw-r--r--   0 runner    (1001) docker     (123)     7789 2023-04-06 20:59:48.000000 stactools-sentinel1-0.5.2/src/stactools/sentinel1/rtc/rtc_metadata.py
--rw-r--r--   0 runner    (1001) docker     (123)     7072 2023-04-06 20:59:48.000000 stactools-sentinel1-0.5.2/src/stactools/sentinel1/rtc/stac.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:00:07.711086 stactools-sentinel1-0.5.2/src/stactools_sentinel1.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     4356 2023-04-06 21:00:07.000000 stactools-sentinel1-0.5.2/src/stactools_sentinel1.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      879 2023-04-06 21:00:07.000000 stactools-sentinel1-0.5.2/src/stactools_sentinel1.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 21:00:07.000000 stactools-sentinel1-0.5.2/src/stactools_sentinel1.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       17 2023-04-06 21:00:07.000000 stactools-sentinel1-0.5.2/src/stactools_sentinel1.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       10 2023-04-06 21:00:07.000000 stactools-sentinel1-0.5.2/src/stactools_sentinel1.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:56:33.534365 stactools-sentinel1-0.5.3/
+-rw-r--r--   0 runner    (1001) docker     (123)      641 2023-04-07 13:56:14.000000 stactools-sentinel1-0.5.3/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)     4356 2023-04-07 13:56:33.534365 stactools-sentinel1-0.5.3/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     3569 2023-04-07 13:56:14.000000 stactools-sentinel1-0.5.3/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)      122 2023-04-07 13:56:14.000000 stactools-sentinel1-0.5.3/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)      971 2023-04-07 13:56:33.534365 stactools-sentinel1-0.5.3/setup.cfg
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:56:33.530365 stactools-sentinel1-0.5.3/src/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:56:33.530365 stactools-sentinel1-0.5.3/src/stactools/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:56:33.534365 stactools-sentinel1-0.5.3/src/stactools/sentinel1/
+-rw-r--r--   0 runner    (1001) docker     (123)      311 2023-04-07 13:56:14.000000 stactools-sentinel1-0.5.3/src/stactools/sentinel1/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      421 2023-04-07 13:56:14.000000 stactools-sentinel1-0.5.3/src/stactools/sentinel1/commands.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:56:33.534365 stactools-sentinel1-0.5.3/src/stactools/sentinel1/grd/
+-rw-r--r--   0 runner    (1001) docker     (123)      101 2023-04-07 13:56:14.000000 stactools-sentinel1-0.5.3/src/stactools/sentinel1/grd/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1677 2023-04-07 13:56:14.000000 stactools-sentinel1-0.5.3/src/stactools/sentinel1/grd/bands.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1598 2023-04-07 13:56:14.000000 stactools-sentinel1-0.5.3/src/stactools/sentinel1/grd/commands.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12244 2023-04-07 13:56:14.000000 stactools-sentinel1-0.5.3/src/stactools/sentinel1/grd/constants.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9320 2023-04-07 13:56:14.000000 stactools-sentinel1-0.5.3/src/stactools/sentinel1/grd/metadata_links.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7240 2023-04-07 13:56:14.000000 stactools-sentinel1-0.5.3/src/stactools/sentinel1/grd/product_metadata.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4144 2023-04-07 13:56:14.000000 stactools-sentinel1-0.5.3/src/stactools/sentinel1/grd/properties.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7134 2023-04-07 13:56:14.000000 stactools-sentinel1-0.5.3/src/stactools/sentinel1/grd/stac.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:56:33.534365 stactools-sentinel1-0.5.3/src/stactools/sentinel1/rtc/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 13:56:14.000000 stactools-sentinel1-0.5.3/src/stactools/sentinel1/rtc/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2058 2023-04-07 13:56:14.000000 stactools-sentinel1-0.5.3/src/stactools/sentinel1/rtc/commands.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3307 2023-04-07 13:56:14.000000 stactools-sentinel1-0.5.3/src/stactools/sentinel1/rtc/constants.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7789 2023-04-07 13:56:14.000000 stactools-sentinel1-0.5.3/src/stactools/sentinel1/rtc/rtc_metadata.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7072 2023-04-07 13:56:14.000000 stactools-sentinel1-0.5.3/src/stactools/sentinel1/rtc/stac.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:56:33.534365 stactools-sentinel1-0.5.3/src/stactools_sentinel1.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     4356 2023-04-07 13:56:33.000000 stactools-sentinel1-0.5.3/src/stactools_sentinel1.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      879 2023-04-07 13:56:33.000000 stactools-sentinel1-0.5.3/src/stactools_sentinel1.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 13:56:33.000000 stactools-sentinel1-0.5.3/src/stactools_sentinel1.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       17 2023-04-07 13:56:33.000000 stactools-sentinel1-0.5.3/src/stactools_sentinel1.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       10 2023-04-07 13:56:33.000000 stactools-sentinel1-0.5.3/src/stactools_sentinel1.egg-info/top_level.txt
```

### Comparing `stactools-sentinel1-0.5.2/LICENSE` & `stactools-sentinel1-0.5.3/LICENSE`

 * *Files identical despite different names*

### Comparing `stactools-sentinel1-0.5.2/PKG-INFO` & `stactools-sentinel1-0.5.3/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: stactools-sentinel1
-Version: 0.5.2
+Version: 0.5.3
 Summary: stactools subpackage for creating sentinel1 STACs
 Home-page: https://github.com/stactools-packages/sentinel1
 Author: stac-utils
 Author-email: stac@radiant.earth
 Project-URL: Documentation, https://github.com/stactools-packages/sentinel1
 Project-URL: Issues, https://github.com/stactools-packages/sentinel1/issues
 Keywords: stactools,pystac,catalog,STAC,sentinel,GRD,radar
```

### Comparing `stactools-sentinel1-0.5.2/README.md` & `stactools-sentinel1-0.5.3/README.md`

 * *Files identical despite different names*

### Comparing `stactools-sentinel1-0.5.2/setup.cfg` & `stactools-sentinel1-0.5.3/setup.cfg`

 * *Files 1% similar despite different names*

```diff
@@ -27,15 +27,15 @@
 
 [options]
 package_dir = 
 	= src
 packages = find_namespace:
 python_requires = >= 3.8
 install_requires = 
-	stactools == 0.4.3
+	stactools == 0.4.5
 
 [options.packages.find]
 where = src
 
 [egg_info]
 tag_build = 
 tag_date = 0
```

### Comparing `stactools-sentinel1-0.5.2/src/stactools/sentinel1/grd/bands.py` & `stactools-sentinel1-0.5.3/src/stactools/sentinel1/grd/bands.py`

 * *Files identical despite different names*

### Comparing `stactools-sentinel1-0.5.2/src/stactools/sentinel1/grd/commands.py` & `stactools-sentinel1-0.5.3/src/stactools/sentinel1/grd/commands.py`

 * *Files identical despite different names*

### Comparing `stactools-sentinel1-0.5.2/src/stactools/sentinel1/grd/constants.py` & `stactools-sentinel1-0.5.3/src/stactools/sentinel1/grd/constants.py`

 * *Files identical despite different names*

### Comparing `stactools-sentinel1-0.5.2/src/stactools/sentinel1/grd/metadata_links.py` & `stactools-sentinel1-0.5.3/src/stactools/sentinel1/grd/metadata_links.py`

 * *Files identical despite different names*

### Comparing `stactools-sentinel1-0.5.2/src/stactools/sentinel1/grd/product_metadata.py` & `stactools-sentinel1-0.5.3/src/stactools/sentinel1/grd/product_metadata.py`

 * *Files identical despite different names*

### Comparing `stactools-sentinel1-0.5.2/src/stactools/sentinel1/grd/properties.py` & `stactools-sentinel1-0.5.3/src/stactools/sentinel1/grd/properties.py`

 * *Files identical despite different names*

### Comparing `stactools-sentinel1-0.5.2/src/stactools/sentinel1/grd/stac.py` & `stactools-sentinel1-0.5.3/src/stactools/sentinel1/grd/stac.py`

 * *Files identical despite different names*

### Comparing `stactools-sentinel1-0.5.2/src/stactools/sentinel1/rtc/commands.py` & `stactools-sentinel1-0.5.3/src/stactools/sentinel1/rtc/commands.py`

 * *Files identical despite different names*

### Comparing `stactools-sentinel1-0.5.2/src/stactools/sentinel1/rtc/constants.py` & `stactools-sentinel1-0.5.3/src/stactools/sentinel1/rtc/constants.py`

 * *Files identical despite different names*

### Comparing `stactools-sentinel1-0.5.2/src/stactools/sentinel1/rtc/rtc_metadata.py` & `stactools-sentinel1-0.5.3/src/stactools/sentinel1/rtc/rtc_metadata.py`

 * *Files identical despite different names*

### Comparing `stactools-sentinel1-0.5.2/src/stactools/sentinel1/rtc/stac.py` & `stactools-sentinel1-0.5.3/src/stactools/sentinel1/rtc/stac.py`

 * *Files identical despite different names*

### Comparing `stactools-sentinel1-0.5.2/src/stactools_sentinel1.egg-info/PKG-INFO` & `stactools-sentinel1-0.5.3/src/stactools_sentinel1.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: stactools-sentinel1
-Version: 0.5.2
+Version: 0.5.3
 Summary: stactools subpackage for creating sentinel1 STACs
 Home-page: https://github.com/stactools-packages/sentinel1
 Author: stac-utils
 Author-email: stac@radiant.earth
 Project-URL: Documentation, https://github.com/stactools-packages/sentinel1
 Project-URL: Issues, https://github.com/stactools-packages/sentinel1/issues
 Keywords: stactools,pystac,catalog,STAC,sentinel,GRD,radar
```

### Comparing `stactools-sentinel1-0.5.2/src/stactools_sentinel1.egg-info/SOURCES.txt` & `stactools-sentinel1-0.5.3/src/stactools_sentinel1.egg-info/SOURCES.txt`

 * *Files identical despite different names*

