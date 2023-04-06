# Comparing `tmp/libprobe-0.2.8.tar.gz` & `tmp/libprobe-0.2.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "libprobe-0.2.8.tar", last modified: Wed Nov 16 21:05:00 2022, max compression
+gzip compressed data, was "libprobe-0.2.9.tar", last modified: Fri Nov 18 08:41:15 2022, max compression
```

## Comparing `libprobe-0.2.8.tar` & `libprobe-0.2.9.tar`

### file list

```diff
@@ -1,26 +1,26 @@
-drwxrwxr-x   0 joente    (1000) joente    (1000)        0 2022-11-16 21:05:00.779899 libprobe-0.2.8/
--rw-rw-r--   0 joente    (1000) joente    (1000)    35149 2022-07-05 11:43:02.000000 libprobe-0.2.8/LICENSE
--rw-rw-r--   0 joente    (1000) joente    (1000)     4548 2022-11-16 21:05:00.779899 libprobe-0.2.8/PKG-INFO
--rw-rw-r--   0 joente    (1000) joente    (1000)     3661 2022-11-11 12:53:37.000000 libprobe-0.2.8/README.md
-drwxrwxr-x   0 joente    (1000) joente    (1000)        0 2022-11-16 21:05:00.779899 libprobe-0.2.8/libprobe/
--rw-rw-r--   0 joente    (1000) joente    (1000)        0 2022-07-04 09:31:51.000000 libprobe-0.2.8/libprobe/__init__.py
--rw-rw-r--   0 joente    (1000) joente    (1000)      330 2022-11-10 12:19:56.000000 libprobe-0.2.8/libprobe/asset.py
--rw-rw-r--   0 joente    (1000) joente    (1000)     1656 2022-10-20 10:01:54.000000 libprobe-0.2.8/libprobe/config.py
--rw-rw-r--   0 joente    (1000) joente    (1000)     1604 2022-07-06 11:10:44.000000 libprobe-0.2.8/libprobe/exceptions.py
--rw-rw-r--   0 joente    (1000) joente    (1000)     1565 2022-07-05 13:02:05.000000 libprobe-0.2.8/libprobe/logger.py
-drwxrwxr-x   0 joente    (1000) joente    (1000)        0 2022-11-16 21:05:00.779899 libprobe-0.2.8/libprobe/net/
--rw-rw-r--   0 joente    (1000) joente    (1000)        0 2021-01-07 12:50:31.000000 libprobe-0.2.8/libprobe/net/__init__.py
--rw-rw-r--   0 joente    (1000) joente    (1000)     1699 2022-07-04 09:19:45.000000 libprobe-0.2.8/libprobe/net/package.py
--rw-rw-r--   0 joente    (1000) joente    (1000)     3160 2022-07-07 13:07:52.000000 libprobe-0.2.8/libprobe/net/protocol.py
--rw-rw-r--   0 joente    (1000) joente    (1000)    12746 2022-11-16 21:03:48.000000 libprobe-0.2.8/libprobe/probe.py
--rw-rw-r--   0 joente    (1000) joente    (1000)     2322 2022-11-11 07:23:21.000000 libprobe-0.2.8/libprobe/protocol.py
--rw-rw-r--   0 joente    (1000) joente    (1000)       86 2022-07-06 09:55:46.000000 libprobe-0.2.8/libprobe/severity.py
--rw-rw-r--   0 joente    (1000) joente    (1000)       22 2022-11-16 21:04:03.000000 libprobe-0.2.8/libprobe/version.py
-drwxrwxr-x   0 joente    (1000) joente    (1000)        0 2022-11-16 21:05:00.779899 libprobe-0.2.8/libprobe.egg-info/
--rw-rw-r--   0 joente    (1000) joente    (1000)     4548 2022-11-16 21:05:00.000000 libprobe-0.2.8/libprobe.egg-info/PKG-INFO
--rw-rw-r--   0 joente    (1000) joente    (1000)      439 2022-11-16 21:05:00.000000 libprobe-0.2.8/libprobe.egg-info/SOURCES.txt
--rw-rw-r--   0 joente    (1000) joente    (1000)        1 2022-11-16 21:05:00.000000 libprobe-0.2.8/libprobe.egg-info/dependency_links.txt
--rw-rw-r--   0 joente    (1000) joente    (1000)       50 2022-11-16 21:05:00.000000 libprobe-0.2.8/libprobe.egg-info/requires.txt
--rw-rw-r--   0 joente    (1000) joente    (1000)        9 2022-11-16 21:05:00.000000 libprobe-0.2.8/libprobe.egg-info/top_level.txt
--rw-rw-r--   0 joente    (1000) joente    (1000)       38 2022-11-16 21:05:00.779899 libprobe-0.2.8/setup.cfg
--rw-rw-r--   0 joente    (1000) joente    (1000)     1560 2022-11-11 11:25:20.000000 libprobe-0.2.8/setup.py
+drwxrwxr-x   0 joente    (1000) joente    (1000)        0 2022-11-18 08:41:15.374033 libprobe-0.2.9/
+-rw-rw-r--   0 joente    (1000) joente    (1000)    35149 2022-07-05 11:43:02.000000 libprobe-0.2.9/LICENSE
+-rw-rw-r--   0 joente    (1000) joente    (1000)     4548 2022-11-18 08:41:15.374033 libprobe-0.2.9/PKG-INFO
+-rw-rw-r--   0 joente    (1000) joente    (1000)     3661 2022-11-11 12:53:37.000000 libprobe-0.2.9/README.md
+drwxrwxr-x   0 joente    (1000) joente    (1000)        0 2022-11-18 08:41:15.370033 libprobe-0.2.9/libprobe/
+-rw-rw-r--   0 joente    (1000) joente    (1000)        0 2022-07-04 09:31:51.000000 libprobe-0.2.9/libprobe/__init__.py
+-rw-rw-r--   0 joente    (1000) joente    (1000)      330 2022-11-10 12:19:56.000000 libprobe-0.2.9/libprobe/asset.py
+-rw-rw-r--   0 joente    (1000) joente    (1000)     1656 2022-10-20 10:01:54.000000 libprobe-0.2.9/libprobe/config.py
+-rw-rw-r--   0 joente    (1000) joente    (1000)     1604 2022-07-06 11:10:44.000000 libprobe-0.2.9/libprobe/exceptions.py
+-rw-rw-r--   0 joente    (1000) joente    (1000)     1565 2022-07-05 13:02:05.000000 libprobe-0.2.9/libprobe/logger.py
+drwxrwxr-x   0 joente    (1000) joente    (1000)        0 2022-11-18 08:41:15.374033 libprobe-0.2.9/libprobe/net/
+-rw-rw-r--   0 joente    (1000) joente    (1000)        0 2021-01-07 12:50:31.000000 libprobe-0.2.9/libprobe/net/__init__.py
+-rw-rw-r--   0 joente    (1000) joente    (1000)     1699 2022-07-04 09:19:45.000000 libprobe-0.2.9/libprobe/net/package.py
+-rw-rw-r--   0 joente    (1000) joente    (1000)     3160 2022-07-07 13:07:52.000000 libprobe-0.2.9/libprobe/net/protocol.py
+-rw-rw-r--   0 joente    (1000) joente    (1000)    12817 2022-11-18 08:39:38.000000 libprobe-0.2.9/libprobe/probe.py
+-rw-rw-r--   0 joente    (1000) joente    (1000)     2322 2022-11-11 07:23:21.000000 libprobe-0.2.9/libprobe/protocol.py
+-rw-rw-r--   0 joente    (1000) joente    (1000)       86 2022-07-06 09:55:46.000000 libprobe-0.2.9/libprobe/severity.py
+-rw-rw-r--   0 joente    (1000) joente    (1000)       22 2022-11-18 08:38:19.000000 libprobe-0.2.9/libprobe/version.py
+drwxrwxr-x   0 joente    (1000) joente    (1000)        0 2022-11-18 08:41:15.370033 libprobe-0.2.9/libprobe.egg-info/
+-rw-rw-r--   0 joente    (1000) joente    (1000)     4548 2022-11-18 08:41:14.000000 libprobe-0.2.9/libprobe.egg-info/PKG-INFO
+-rw-rw-r--   0 joente    (1000) joente    (1000)      439 2022-11-18 08:41:15.000000 libprobe-0.2.9/libprobe.egg-info/SOURCES.txt
+-rw-rw-r--   0 joente    (1000) joente    (1000)        1 2022-11-18 08:41:14.000000 libprobe-0.2.9/libprobe.egg-info/dependency_links.txt
+-rw-rw-r--   0 joente    (1000) joente    (1000)       50 2022-11-18 08:41:15.000000 libprobe-0.2.9/libprobe.egg-info/requires.txt
+-rw-rw-r--   0 joente    (1000) joente    (1000)        9 2022-11-18 08:41:15.000000 libprobe-0.2.9/libprobe.egg-info/top_level.txt
+-rw-rw-r--   0 joente    (1000) joente    (1000)       38 2022-11-18 08:41:15.374033 libprobe-0.2.9/setup.cfg
+-rw-rw-r--   0 joente    (1000) joente    (1000)     1560 2022-11-11 11:25:20.000000 libprobe-0.2.9/setup.py
```

### Comparing `libprobe-0.2.8/LICENSE` & `libprobe-0.2.9/LICENSE`

 * *Files identical despite different names*

### Comparing `libprobe-0.2.8/PKG-INFO` & `libprobe-0.2.9/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 Metadata-Version: 2.1
 Name: libprobe
-Version: 0.2.8
+Version: 0.2.9
 Summary: Library for building InfraSonar probes
 Home-page: https://github.com/infrasonar/python-libprobe
-Download-URL: https://github.com/infrasonar/python-libprobe/tarball/v0.2.8
+Download-URL: https://github.com/infrasonar/python-libprobe/tarball/v0.2.9
 Author: Cesbit
 Author-email: info@cesbit.com
 License: UNKNOWN
 Keywords: monitoring,infrasonar,probe
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
 Classifier: Operating System :: OS Independent
```

### Comparing `libprobe-0.2.8/README.md` & `libprobe-0.2.9/README.md`

 * *Files identical despite different names*

### Comparing `libprobe-0.2.8/libprobe/config.py` & `libprobe-0.2.9/libprobe/config.py`

 * *Files identical despite different names*

### Comparing `libprobe-0.2.8/libprobe/exceptions.py` & `libprobe-0.2.9/libprobe/exceptions.py`

 * *Files identical despite different names*

### Comparing `libprobe-0.2.8/libprobe/logger.py` & `libprobe-0.2.9/libprobe/logger.py`

 * *Files identical despite different names*

### Comparing `libprobe-0.2.8/libprobe/net/package.py` & `libprobe-0.2.9/libprobe/net/package.py`

 * *Files identical despite different names*

### Comparing `libprobe-0.2.8/libprobe/net/protocol.py` & `libprobe-0.2.9/libprobe/net/protocol.py`

 * *Files identical despite different names*

### Comparing `libprobe-0.2.8/libprobe/probe.py` & `libprobe-0.2.9/libprobe/probe.py`

 * *Files 2% similar despite different names*

```diff
@@ -65,15 +65,15 @@
         name: str,
         version: str,
         checks: Dict[str, Callable[[Asset, dict, dict], dict]],
         config_path: Optional[str] = INFRASONAR_CONF_FN
     ):
         setproctitle(name)
         setup_logger()
-
+        logging.warning(f'starting probe collector: {name} v{version}')
         self.name: str = name
         self.version: str = version
         self._checks_funs: Dict[
             str,
             Callable[[Asset, dict, dict], dict]] = checks
         self._config_path: Path = Path(config_path)
         self._connecting: bool = False
```

### Comparing `libprobe-0.2.8/libprobe/protocol.py` & `libprobe-0.2.9/libprobe/protocol.py`

 * *Files identical despite different names*

### Comparing `libprobe-0.2.8/libprobe.egg-info/PKG-INFO` & `libprobe-0.2.9/libprobe.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 Metadata-Version: 2.1
 Name: libprobe
-Version: 0.2.8
+Version: 0.2.9
 Summary: Library for building InfraSonar probes
 Home-page: https://github.com/infrasonar/python-libprobe
-Download-URL: https://github.com/infrasonar/python-libprobe/tarball/v0.2.8
+Download-URL: https://github.com/infrasonar/python-libprobe/tarball/v0.2.9
 Author: Cesbit
 Author-email: info@cesbit.com
 License: UNKNOWN
 Keywords: monitoring,infrasonar,probe
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
 Classifier: Operating System :: OS Independent
```

### Comparing `libprobe-0.2.8/setup.py` & `libprobe-0.2.9/setup.py`

 * *Files identical despite different names*

