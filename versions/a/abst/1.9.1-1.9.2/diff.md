# Comparing `tmp/abst-1.9.1.tar.gz` & `tmp/abst-1.9.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "abst-1.9.1.tar", last modified: Thu Mar 30 12:15:43 2023, max compression
+gzip compressed data, was "abst-1.9.2.tar", last modified: Thu Apr  6 09:14:12 2023, max compression
```

## Comparing `abst-1.9.1.tar` & `abst-1.9.2.tar`

### file list

```diff
@@ -1,32 +1,32 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 12:15:43.444259 abst-1.9.1/
--rw-r--r--   0 runner    (1001) docker     (123)     1069 2023-03-30 12:15:31.000000 abst-1.9.1/LICENSE.md
--rw-r--r--   0 runner    (1001) docker     (123)     4648 2023-03-30 12:15:43.444259 abst-1.9.1/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     3920 2023-03-30 12:15:31.000000 abst-1.9.1/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 12:15:43.440259 abst-1.9.1/abst/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-30 12:15:31.000000 abst-1.9.1/abst/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      493 2023-03-30 12:15:31.000000 abst-1.9.1/abst/__version__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 12:15:43.440259 abst-1.9.1/abst/bastion_support/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-30 12:15:31.000000 abst-1.9.1/abst/bastion_support/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5674 2023-03-30 12:15:31.000000 abst-1.9.1/abst/bastion_support/bastion_scheduler.py
--rw-r--r--   0 runner    (1001) docker     (123)    22731 2023-03-30 12:15:31.000000 abst-1.9.1/abst/bastion_support/oci_bastion.py
--rw-r--r--   0 runner    (1001) docker     (123)      757 2023-03-30 12:15:31.000000 abst-1.9.1/abst/cfg_func.py
--rw-r--r--   0 runner    (1001) docker     (123)      761 2023-03-30 12:15:31.000000 abst-1.9.1/abst/config.py
--rw-r--r--   0 runner    (1001) docker     (123)      519 2023-03-30 12:15:31.000000 abst-1.9.1/abst/dialogs.py
--rw-r--r--   0 runner    (1001) docker     (123)    17258 2023-03-30 12:15:31.000000 abst-1.9.1/abst/main.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 12:15:43.444259 abst-1.9.1/abst/notifier/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-30 12:15:31.000000 abst-1.9.1/abst/notifier/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1666 2023-03-30 12:15:31.000000 abst-1.9.1/abst/notifier/version_notifier.py
--rw-r--r--   0 runner    (1001) docker     (123)     1219 2023-03-30 12:15:31.000000 abst-1.9.1/abst/tools.py
--rw-r--r--   0 runner    (1001) docker     (123)      775 2023-03-30 12:15:31.000000 abst-1.9.1/abst/wrappers.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 12:15:43.440259 abst-1.9.1/abst.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     4648 2023-03-30 12:15:43.000000 abst-1.9.1/abst.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      548 2023-03-30 12:15:43.000000 abst-1.9.1/abst.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-30 12:15:43.000000 abst-1.9.1/abst.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       40 2023-03-30 12:15:43.000000 abst-1.9.1/abst.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (123)       83 2023-03-30 12:15:43.000000 abst-1.9.1/abst.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        5 2023-03-30 12:15:43.000000 abst-1.9.1/abst.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-30 12:15:43.000000 abst-1.9.1/abst.egg-info/zip-safe
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-30 12:15:43.444259 abst-1.9.1/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1512 2023-03-30 12:15:31.000000 abst-1.9.1/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-30 12:15:43.444259 abst-1.9.1/tests/
--rw-r--r--   0 runner    (1001) docker     (123)      251 2023-03-30 12:15:31.000000 abst-1.9.1/tests/test_sample_dict.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:14:12.422695 abst-1.9.2/
+-rw-r--r--   0 runner    (1001) docker     (123)     1069 2023-04-06 09:14:02.000000 abst-1.9.2/LICENSE.md
+-rw-r--r--   0 runner    (1001) docker     (123)     4648 2023-04-06 09:14:12.422695 abst-1.9.2/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     3920 2023-04-06 09:14:02.000000 abst-1.9.2/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:14:12.418695 abst-1.9.2/abst/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 09:14:02.000000 abst-1.9.2/abst/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      493 2023-04-06 09:14:02.000000 abst-1.9.2/abst/__version__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:14:12.422695 abst-1.9.2/abst/bastion_support/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 09:14:02.000000 abst-1.9.2/abst/bastion_support/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5674 2023-04-06 09:14:02.000000 abst-1.9.2/abst/bastion_support/bastion_scheduler.py
+-rw-r--r--   0 runner    (1001) docker     (123)    22731 2023-04-06 09:14:02.000000 abst-1.9.2/abst/bastion_support/oci_bastion.py
+-rw-r--r--   0 runner    (1001) docker     (123)      757 2023-04-06 09:14:02.000000 abst-1.9.2/abst/cfg_func.py
+-rw-r--r--   0 runner    (1001) docker     (123)      761 2023-04-06 09:14:02.000000 abst-1.9.2/abst/config.py
+-rw-r--r--   0 runner    (1001) docker     (123)      519 2023-04-06 09:14:02.000000 abst-1.9.2/abst/dialogs.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17258 2023-04-06 09:14:02.000000 abst-1.9.2/abst/main.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:14:12.422695 abst-1.9.2/abst/notifier/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 09:14:02.000000 abst-1.9.2/abst/notifier/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1679 2023-04-06 09:14:02.000000 abst-1.9.2/abst/notifier/version_notifier.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1219 2023-04-06 09:14:02.000000 abst-1.9.2/abst/tools.py
+-rw-r--r--   0 runner    (1001) docker     (123)      775 2023-04-06 09:14:02.000000 abst-1.9.2/abst/wrappers.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:14:12.422695 abst-1.9.2/abst.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     4648 2023-04-06 09:14:12.000000 abst-1.9.2/abst.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      548 2023-04-06 09:14:12.000000 abst-1.9.2/abst.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 09:14:12.000000 abst-1.9.2/abst.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       40 2023-04-06 09:14:12.000000 abst-1.9.2/abst.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       83 2023-04-06 09:14:12.000000 abst-1.9.2/abst.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        5 2023-04-06 09:14:12.000000 abst-1.9.2/abst.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 09:14:12.000000 abst-1.9.2/abst.egg-info/zip-safe
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 09:14:12.422695 abst-1.9.2/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1512 2023-04-06 09:14:02.000000 abst-1.9.2/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:14:12.422695 abst-1.9.2/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)      251 2023-04-06 09:14:02.000000 abst-1.9.2/tests/test_sample_dict.py
```

### Comparing `abst-1.9.1/LICENSE.md` & `abst-1.9.2/LICENSE.md`

 * *Files identical despite different names*

### Comparing `abst-1.9.1/PKG-INFO` & `abst-1.9.2/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: abst
-Version: 1.9.1
+Version: 1.9.2
 Summary: CLI Command making OCI Bastion and kubernetes usage simple and fast
 Home-page: https://github.com/jiri-otoupal/abst
 Author: Jiri Otoupal
 Author-email: jiri-otoupal@ips-database.eu
 License: MIT
 Keywords: Auto OCI Bastion
 Classifier: Development Status :: 4 - Beta
```

### Comparing `abst-1.9.1/README.md` & `abst-1.9.2/README.md`

 * *Files identical despite different names*

### Comparing `abst-1.9.1/abst/bastion_support/bastion_scheduler.py` & `abst-1.9.2/abst/bastion_support/bastion_scheduler.py`

 * *Files identical despite different names*

### Comparing `abst-1.9.1/abst/bastion_support/oci_bastion.py` & `abst-1.9.2/abst/bastion_support/oci_bastion.py`

 * *Files identical despite different names*

### Comparing `abst-1.9.1/abst/cfg_func.py` & `abst-1.9.2/abst/cfg_func.py`

 * *Files identical despite different names*

### Comparing `abst-1.9.1/abst/config.py` & `abst-1.9.2/abst/config.py`

 * *Files identical despite different names*

### Comparing `abst-1.9.1/abst/dialogs.py` & `abst-1.9.2/abst/dialogs.py`

 * *Files identical despite different names*

### Comparing `abst-1.9.1/abst/main.py` & `abst-1.9.2/abst/main.py`

 * *Files identical despite different names*

### Comparing `abst-1.9.1/abst/notifier/version_notifier.py` & `abst-1.9.2/abst/notifier/version_notifier.py`

 * *Files 6% similar despite different names*

```diff
@@ -13,25 +13,26 @@
 
 class Notifier:
     @classmethod
     def check_pypi_available(cls):
         try:
             req = requests.get("https://pypi.org/", timeout=0.2)
             return req.status_code == 200
-        except ConnectionError or ConnectTimeout:
+        except (ConnectionError, ConnectTimeout):
             return False
 
     @classmethod
     def get_last_version(cls):
         return lastversion.latest(__version__.__pypi_repo__)
 
     @classmethod
     def is_last_version(cls):
         last = cls.get_last_version()
-        return semantic_version.Version(__version__.__version__) >= semantic_version.Version(str(last))
+        return semantic_version.Version(
+            __version__.__version__) >= semantic_version.Version(str(last))
 
     @classmethod
     def notify(cls):
         from abst.bastion_support.oci_bastion import Bastion
         cfg = Bastion.load_config()
         dt = datetime.now()
         if (dt - datetime.fromtimestamp(
```

### Comparing `abst-1.9.1/abst/tools.py` & `abst-1.9.2/abst/tools.py`

 * *Files identical despite different names*

### Comparing `abst-1.9.1/abst/wrappers.py` & `abst-1.9.2/abst/wrappers.py`

 * *Files identical despite different names*

### Comparing `abst-1.9.1/abst.egg-info/PKG-INFO` & `abst-1.9.2/abst.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: abst
-Version: 1.9.1
+Version: 1.9.2
 Summary: CLI Command making OCI Bastion and kubernetes usage simple and fast
 Home-page: https://github.com/jiri-otoupal/abst
 Author: Jiri Otoupal
 Author-email: jiri-otoupal@ips-database.eu
 License: MIT
 Keywords: Auto OCI Bastion
 Classifier: Development Status :: 4 - Beta
```

### Comparing `abst-1.9.1/abst.egg-info/SOURCES.txt` & `abst-1.9.2/abst.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `abst-1.9.1/setup.py` & `abst-1.9.2/setup.py`

 * *Files identical despite different names*

