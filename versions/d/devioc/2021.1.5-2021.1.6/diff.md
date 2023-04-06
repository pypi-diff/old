# Comparing `tmp/devioc-2021.1.5.tar.gz` & `tmp/devioc-2021.1.6.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "devioc-2021.1.5.tar", last modified: Mon Jan 11 22:26:02 2021, max compression
+gzip compressed data, was "devioc-2021.1.6.tar", last modified: Mon Jan  3 21:00:14 2022, max compression
```

## Comparing `devioc-2021.1.5.tar` & `devioc-2021.1.6.tar`

### file list

```diff
@@ -1,21 +1,22 @@
-drwxrwxr-x   0 michel    (1000) michel    (1000)        0 2021-01-11 22:26:02.850851 devioc-2021.1.5/
--rw-rw-r--   0 michel    (1000) michel    (1000)     1177 2021-01-11 22:26:02.850851 devioc-2021.1.5/PKG-INFO
--rw-rw-r--   0 michel    (1000) michel    (1000)      568 2020-05-11 01:30:54.000000 devioc-2021.1.5/README.md
-drwxrwxr-x   0 michel    (1000) michel    (1000)        0 2021-01-11 22:26:02.849851 devioc-2021.1.5/bin/
--rwxrwxr-x   0 michel    (1000) michel    (1000)     9503 2021-01-11 21:20:03.000000 devioc-2021.1.5/bin/devioc-startproject
-drwxrwxr-x   0 michel    (1000) michel    (1000)        0 2021-01-11 22:26:02.849851 devioc-2021.1.5/devioc/
--rw-rw-r--   0 michel    (1000) michel    (1000)        0 2020-05-10 23:36:10.000000 devioc-2021.1.5/devioc/__init__.py
--rw-rw-r--   0 michel    (1000) michel    (1000)     2819 2020-05-10 23:36:10.000000 devioc-2021.1.5/devioc/log.py
--rw-rw-r--   0 michel    (1000) michel    (1000)    15929 2020-12-08 21:06:39.000000 devioc-2021.1.5/devioc/models.py
-drwxrwxr-x   0 michel    (1000) michel    (1000)        0 2021-01-11 22:26:02.849851 devioc-2021.1.5/devioc/tests/
--rw-rw-r--   0 michel    (1000) michel    (1000)        0 2020-05-10 23:36:10.000000 devioc-2021.1.5/devioc/tests/__init__.py
--rw-rw-r--   0 michel    (1000) michel    (1000)     4181 2021-01-11 21:48:26.000000 devioc-2021.1.5/devioc/tests/test_ioc.py
--rw-r--r--   0 michel    (1000) michel    (1000)     1366 2020-05-10 23:50:35.000000 devioc-2021.1.5/devioc/version.py
-drwxrwxr-x   0 michel    (1000) michel    (1000)        0 2021-01-11 22:26:02.849851 devioc-2021.1.5/devioc.egg-info/
--rw-rw-r--   0 michel    (1000) michel    (1000)     1177 2021-01-11 22:26:02.000000 devioc-2021.1.5/devioc.egg-info/PKG-INFO
--rw-rw-r--   0 michel    (1000) michel    (1000)      309 2021-01-11 22:26:02.000000 devioc-2021.1.5/devioc.egg-info/SOURCES.txt
--rw-rw-r--   0 michel    (1000) michel    (1000)        1 2021-01-11 22:26:02.000000 devioc-2021.1.5/devioc.egg-info/dependency_links.txt
--rw-rw-r--   0 michel    (1000) michel    (1000)       82 2021-01-11 22:26:02.000000 devioc-2021.1.5/devioc.egg-info/requires.txt
--rw-rw-r--   0 michel    (1000) michel    (1000)        7 2021-01-11 22:26:02.000000 devioc-2021.1.5/devioc.egg-info/top_level.txt
--rw-rw-r--   0 michel    (1000) michel    (1000)       38 2021-01-11 22:26:02.850851 devioc-2021.1.5/setup.cfg
--rw-rw-r--   0 michel    (1000) michel    (1000)     1018 2021-01-11 22:20:40.000000 devioc-2021.1.5/setup.py
+drwxrwxr-x   0 michel    (1000) michel    (1000)        0 2022-01-03 21:00:14.186146 devioc-2021.1.6/
+-rw-rw-r--   0 michel    (1000) michel    (1000)     1066 2020-05-10 23:36:10.000000 devioc-2021.1.6/LICENSE
+-rw-rw-r--   0 michel    (1000) michel    (1000)     1100 2022-01-03 21:00:14.186146 devioc-2021.1.6/PKG-INFO
+-rw-rw-r--   0 michel    (1000) michel    (1000)      568 2020-05-11 01:30:54.000000 devioc-2021.1.6/README.md
+drwxrwxr-x   0 michel    (1000) michel    (1000)        0 2022-01-03 21:00:14.185146 devioc-2021.1.6/bin/
+-rwxrwxr-x   0 michel    (1000) michel    (1000)     9503 2021-01-11 21:20:03.000000 devioc-2021.1.6/bin/devioc-startproject
+drwxrwxr-x   0 michel    (1000) michel    (1000)        0 2022-01-03 21:00:14.185146 devioc-2021.1.6/devioc/
+-rw-rw-r--   0 michel    (1000) michel    (1000)        0 2020-05-10 23:36:10.000000 devioc-2021.1.6/devioc/__init__.py
+-rw-rw-r--   0 michel    (1000) michel    (1000)     2819 2020-05-10 23:36:10.000000 devioc-2021.1.6/devioc/log.py
+-rw-rw-r--   0 michel    (1000) michel    (1000)    15929 2022-01-03 20:57:05.000000 devioc-2021.1.6/devioc/models.py
+drwxrwxr-x   0 michel    (1000) michel    (1000)        0 2022-01-03 21:00:14.186146 devioc-2021.1.6/devioc/tests/
+-rw-rw-r--   0 michel    (1000) michel    (1000)        0 2020-05-10 23:36:10.000000 devioc-2021.1.6/devioc/tests/__init__.py
+-rw-rw-r--   0 michel    (1000) michel    (1000)     4181 2021-01-11 21:48:26.000000 devioc-2021.1.6/devioc/tests/test_ioc.py
+-rw-r--r--   0 michel    (1000) michel    (1000)     1366 2020-05-10 23:50:35.000000 devioc-2021.1.6/devioc/version.py
+drwxrwxr-x   0 michel    (1000) michel    (1000)        0 2022-01-03 21:00:14.186146 devioc-2021.1.6/devioc.egg-info/
+-rw-rw-r--   0 michel    (1000) michel    (1000)     1100 2022-01-03 21:00:14.000000 devioc-2021.1.6/devioc.egg-info/PKG-INFO
+-rw-rw-r--   0 michel    (1000) michel    (1000)      317 2022-01-03 21:00:14.000000 devioc-2021.1.6/devioc.egg-info/SOURCES.txt
+-rw-rw-r--   0 michel    (1000) michel    (1000)        1 2022-01-03 21:00:14.000000 devioc-2021.1.6/devioc.egg-info/dependency_links.txt
+-rw-rw-r--   0 michel    (1000) michel    (1000)       82 2022-01-03 21:00:14.000000 devioc-2021.1.6/devioc.egg-info/requires.txt
+-rw-rw-r--   0 michel    (1000) michel    (1000)        7 2022-01-03 21:00:14.000000 devioc-2021.1.6/devioc.egg-info/top_level.txt
+-rw-rw-r--   0 michel    (1000) michel    (1000)       38 2022-01-03 21:00:14.186146 devioc-2021.1.6/setup.cfg
+-rw-rw-r--   0 michel    (1000) michel    (1000)     1018 2021-01-11 22:20:40.000000 devioc-2021.1.6/setup.py
```

### Comparing `devioc-2021.1.5/PKG-INFO` & `devioc-2021.1.6/PKG-INFO`

 * *Files 23% similar despite different names*

```diff
@@ -1,27 +1,30 @@
 Metadata-Version: 2.1
 Name: devioc
-Version: 2021.1.5
+Version: 2021.1.6
 Summary: Simple Python based EPICS Device IOC Support
 Home-page: https://github.com/michel4j/devioc
 Author: Michel Fodje
 Author-email: michel4j@gmail.com
 License: MIT
-Description: # DevIOC
-        Simple Python Device IOC Support for EPICS
-        
-        DevIOC is a package which enables python based EPICS IOC Soft Device support all within python. It
-        allows you to define the IOC database model in a manner similar to Django Database models, and to use
-        the model to develop dynamic, IOC servers.
-        
-        To use the full capabilities, it is is highly recommended to use a GObject compatible main loop, such as the
-        one provided by `PyGObject` or even better, the GObject compatible `Twisted` reactor.
-        
-        Detailed documentation is available at https://michel4j.github.io/devioc/
-        
 Keywords: epics device ioc development
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
 Description-Content-Type: text/markdown
+License-File: LICENSE
+
+# DevIOC
+Simple Python Device IOC Support for EPICS
+
+DevIOC is a package which enables python based EPICS IOC Soft Device support all within python. It
+allows you to define the IOC database model in a manner similar to Django Database models, and to use
+the model to develop dynamic, IOC servers.
+
+To use the full capabilities, it is is highly recommended to use a GObject compatible main loop, such as the
+one provided by `PyGObject` or even better, the GObject compatible `Twisted` reactor.
+
+Detailed documentation is available at https://michel4j.github.io/devioc/
+
+
```

### Comparing `devioc-2021.1.5/README.md` & `devioc-2021.1.6/README.md`

 * *Files identical despite different names*

### Comparing `devioc-2021.1.5/bin/devioc-startproject` & `devioc-2021.1.6/bin/devioc-startproject`

 * *Files identical despite different names*

### Comparing `devioc-2021.1.5/devioc/log.py` & `devioc-2021.1.6/devioc/log.py`

 * *Files identical despite different names*

### Comparing `devioc-2021.1.5/devioc/models.py` & `devioc-2021.1.6/devioc/models.py`

 * *Files 0% similar despite different names*

```diff
@@ -261,18 +261,18 @@
     :keyword units:  engineering units (str), default empty string. Sets the EGU field
     :keyword *: Extra keyword arguments
     """
 
     record = 'ao'
     required = ['units']
     fields = {
-        'DRVL': '{max_val:0.4e}',
-        'DRVH': '{min_val:0.4e}',
-        'LOPR': '{max_val:0.4e}',
-        'HOPR': '{min_val:0.4e}',
+        'DRVH': '{max_val:0.4e}',
+        'DRVL': '{min_val:0.4e}',
+        'HOPR': '{max_val:0.4e}',
+        'LOPR': '{min_val:0.4e}',
         'PREC': '{prec}',
         'EGU': '{units}',
         'VAL': '{default}'
     }
 
     def __init__(self, name, max_val=0, min_val=0, default=0.0, prec=4, units='', **kwargs):
         kwargs.update(max_val=max_val, min_val=min_val, default=default, prec=prec, units=units)
```

### Comparing `devioc-2021.1.5/devioc/tests/test_ioc.py` & `devioc-2021.1.6/devioc/tests/test_ioc.py`

 * *Files identical despite different names*

### Comparing `devioc-2021.1.5/devioc/version.py` & `devioc-2021.1.6/devioc/version.py`

 * *Files identical despite different names*

### Comparing `devioc-2021.1.5/devioc.egg-info/PKG-INFO` & `devioc-2021.1.6/devioc.egg-info/PKG-INFO`

 * *Files 23% similar despite different names*

```diff
@@ -1,27 +1,30 @@
 Metadata-Version: 2.1
 Name: devioc
-Version: 2021.1.5
+Version: 2021.1.6
 Summary: Simple Python based EPICS Device IOC Support
 Home-page: https://github.com/michel4j/devioc
 Author: Michel Fodje
 Author-email: michel4j@gmail.com
 License: MIT
-Description: # DevIOC
-        Simple Python Device IOC Support for EPICS
-        
-        DevIOC is a package which enables python based EPICS IOC Soft Device support all within python. It
-        allows you to define the IOC database model in a manner similar to Django Database models, and to use
-        the model to develop dynamic, IOC servers.
-        
-        To use the full capabilities, it is is highly recommended to use a GObject compatible main loop, such as the
-        one provided by `PyGObject` or even better, the GObject compatible `Twisted` reactor.
-        
-        Detailed documentation is available at https://michel4j.github.io/devioc/
-        
 Keywords: epics device ioc development
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
 Description-Content-Type: text/markdown
+License-File: LICENSE
+
+# DevIOC
+Simple Python Device IOC Support for EPICS
+
+DevIOC is a package which enables python based EPICS IOC Soft Device support all within python. It
+allows you to define the IOC database model in a manner similar to Django Database models, and to use
+the model to develop dynamic, IOC servers.
+
+To use the full capabilities, it is is highly recommended to use a GObject compatible main loop, such as the
+one provided by `PyGObject` or even better, the GObject compatible `Twisted` reactor.
+
+Detailed documentation is available at https://michel4j.github.io/devioc/
+
+
```

### Comparing `devioc-2021.1.5/setup.py` & `devioc-2021.1.6/setup.py`

 * *Files identical despite different names*

