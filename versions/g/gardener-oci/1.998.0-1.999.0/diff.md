# Comparing `tmp/gardener-oci-1.998.0.tar.gz` & `tmp/gardener-oci-1.999.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/gardener-oci-1.998.0.tar", last modified: Tue Dec 29 21:02:30 2020, max compression
+gzip compressed data, was "dist/gardener-oci-1.999.0.tar", last modified: Tue Dec 29 21:27:22 2020, max compression
```

## Comparing `gardener-oci-1.998.0.tar` & `gardener-oci-1.999.0.tar`

### file list

```diff
@@ -1,19 +1,19 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2020-12-29 21:02:30.755998 gardener-oci-1.998.0/
--rw-r--r--   0 root         (0) root         (0)      187 2020-12-29 21:02:30.755998 gardener-oci-1.998.0/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)     1810 2020-12-29 20:49:34.000000 gardener-oci-1.998.0/README.md
-drwxr-xr-x   0 root         (0) root         (0)        0 2020-12-29 21:02:30.755998 gardener-oci-1.998.0/gardener_oci.egg-info/
--rw-r--r--   0 root         (0) root         (0)      187 2020-12-29 21:02:30.000000 gardener-oci-1.998.0/gardener_oci.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)      300 2020-12-29 21:02:30.000000 gardener-oci-1.998.0/gardener_oci.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2020-12-29 21:02:30.000000 gardener-oci-1.998.0/gardener_oci.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)       80 2020-12-29 21:02:30.000000 gardener-oci-1.998.0/gardener_oci.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)        4 2020-12-29 21:02:30.000000 gardener-oci-1.998.0/gardener_oci.egg-info/top_level.txt
-drwxr-xr-x   0 root         (0) root         (0)        0 2020-12-29 21:02:30.755998 gardener-oci-1.998.0/oci/
--rw-r--r--   0 root         (0) root         (0)     8557 2020-12-29 20:49:34.000000 gardener-oci-1.998.0/oci/__init__.py
--rw-r--r--   0 root         (0) root         (0)     9372 2020-12-29 20:49:34.000000 gardener-oci-1.998.0/oci/_util.py
--rw-r--r--   0 root         (0) root         (0)     3205 2020-12-29 20:49:34.000000 gardener-oci-1.998.0/oci/auth.py
--rw-r--r--   0 root         (0) root         (0)    16776 2020-12-29 20:49:34.000000 gardener-oci-1.998.0/oci/client.py
--rw-r--r--   0 root         (0) root         (0)     1536 2020-12-29 20:49:34.000000 gardener-oci-1.998.0/oci/model.py
--rw-r--r--   0 root         (0) root         (0)     1037 2020-12-29 20:49:34.000000 gardener-oci-1.998.0/oci/util.py
--rw-r--r--   0 root         (0) root         (0)      174 2020-12-29 21:02:30.759998 gardener-oci-1.998.0/setup.cfg
--rw-r--r--   0 root         (0) root         (0)      784 2020-12-29 20:49:34.000000 gardener-oci-1.998.0/setup.oci.py
--rw-r--r--   0 root         (0) root         (0)     1781 2020-12-29 20:49:34.000000 gardener-oci-1.998.0/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2020-12-29 21:27:22.635198 gardener-oci-1.999.0/
+-rw-r--r--   0 root         (0) root         (0)      187 2020-12-29 21:27:22.635198 gardener-oci-1.999.0/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)     1810 2020-12-29 21:26:02.000000 gardener-oci-1.999.0/README.md
+drwxr-xr-x   0 root         (0) root         (0)        0 2020-12-29 21:27:22.635198 gardener-oci-1.999.0/gardener_oci.egg-info/
+-rw-r--r--   0 root         (0) root         (0)      187 2020-12-29 21:27:22.000000 gardener-oci-1.999.0/gardener_oci.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)      300 2020-12-29 21:27:22.000000 gardener-oci-1.999.0/gardener_oci.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2020-12-29 21:27:22.000000 gardener-oci-1.999.0/gardener_oci.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)       80 2020-12-29 21:27:22.000000 gardener-oci-1.999.0/gardener_oci.egg-info/requires.txt
+-rw-r--r--   0 root         (0) root         (0)        4 2020-12-29 21:27:22.000000 gardener-oci-1.999.0/gardener_oci.egg-info/top_level.txt
+drwxr-xr-x   0 root         (0) root         (0)        0 2020-12-29 21:27:22.635198 gardener-oci-1.999.0/oci/
+-rw-r--r--   0 root         (0) root         (0)     8557 2020-12-29 21:26:02.000000 gardener-oci-1.999.0/oci/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     9372 2020-12-29 21:26:02.000000 gardener-oci-1.999.0/oci/_util.py
+-rw-r--r--   0 root         (0) root         (0)     3205 2020-12-29 21:26:02.000000 gardener-oci-1.999.0/oci/auth.py
+-rw-r--r--   0 root         (0) root         (0)    16776 2020-12-29 21:26:02.000000 gardener-oci-1.999.0/oci/client.py
+-rw-r--r--   0 root         (0) root         (0)     1536 2020-12-29 21:26:02.000000 gardener-oci-1.999.0/oci/model.py
+-rw-r--r--   0 root         (0) root         (0)     1037 2020-12-29 21:26:02.000000 gardener-oci-1.999.0/oci/util.py
+-rw-r--r--   0 root         (0) root         (0)      174 2020-12-29 21:27:22.635198 gardener-oci-1.999.0/setup.cfg
+-rw-r--r--   0 root         (0) root         (0)      784 2020-12-29 21:26:02.000000 gardener-oci-1.999.0/setup.oci.py
+-rw-r--r--   0 root         (0) root         (0)     1781 2020-12-29 21:26:02.000000 gardener-oci-1.999.0/setup.py
```

### Comparing `gardener-oci-1.998.0/README.md` & `gardener-oci-1.999.0/README.md`

 * *Files identical despite different names*

### Comparing `gardener-oci-1.998.0/oci/__init__.py` & `gardener-oci-1.999.0/oci/__init__.py`

 * *Files identical despite different names*

### Comparing `gardener-oci-1.998.0/oci/_util.py` & `gardener-oci-1.999.0/oci/_util.py`

 * *Files identical despite different names*

### Comparing `gardener-oci-1.998.0/oci/auth.py` & `gardener-oci-1.999.0/oci/auth.py`

 * *Files identical despite different names*

### Comparing `gardener-oci-1.998.0/oci/client.py` & `gardener-oci-1.999.0/oci/client.py`

 * *Files identical despite different names*

### Comparing `gardener-oci-1.998.0/oci/model.py` & `gardener-oci-1.999.0/oci/model.py`

 * *Files identical despite different names*

### Comparing `gardener-oci-1.998.0/oci/util.py` & `gardener-oci-1.999.0/oci/util.py`

 * *Files identical despite different names*

### Comparing `gardener-oci-1.998.0/setup.oci.py` & `gardener-oci-1.999.0/setup.oci.py`

 * *Files identical despite different names*

### Comparing `gardener-oci-1.998.0/setup.py` & `gardener-oci-1.999.0/setup.py`

 * *Files identical despite different names*

