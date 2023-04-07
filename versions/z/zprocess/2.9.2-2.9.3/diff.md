# Comparing `tmp/zprocess-2.9.2.tar.gz` & `tmp/zprocess-2.9.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/zprocess-2.9.2.tar", last modified: Wed Oct 17 20:32:34 2018, max compression
+gzip compressed data, was "dist/zprocess-2.9.3.tar", last modified: Fri Oct 26 15:25:11 2018, max compression
```

## Comparing `zprocess-2.9.2.tar` & `zprocess-2.9.3.tar`

### file list

```diff
@@ -1,33 +1,33 @@
-drwxr-xr-x   0 bilbo     (1000) bilbo     (1000)        0 2018-10-17 20:32:34.000000 zprocess-2.9.2/
--rw-rw-r--   0 bilbo     (1000) bilbo     (1000)       39 2016-01-21 05:04:25.000000 zprocess-2.9.2/MANIFEST.in
--rw-rw-r--   0 bilbo     (1000) bilbo     (1000)      250 2016-01-21 05:04:25.000000 zprocess-2.9.2/README.txt
--rw-r--r--   0 bilbo     (1000) bilbo     (1000)      287 2018-10-17 20:32:34.000000 zprocess-2.9.2/PKG-INFO
--rw-rw-r--   0 bilbo     (1000) bilbo     (1000)      380 2016-01-21 05:04:25.000000 zprocess-2.9.2/README.md
-drwxr-xr-x   0 bilbo     (1000) bilbo     (1000)        0 2018-10-17 20:32:34.000000 zprocess-2.9.2/zprocess.egg-info/
--rw-r--r--   0 bilbo     (1000) bilbo     (1000)       52 2018-10-17 20:32:34.000000 zprocess-2.9.2/zprocess.egg-info/requires.txt
--rw-r--r--   0 bilbo     (1000) bilbo     (1000)      622 2018-10-17 20:32:34.000000 zprocess-2.9.2/zprocess.egg-info/SOURCES.txt
--rw-r--r--   0 bilbo     (1000) bilbo     (1000)        1 2018-10-17 20:32:34.000000 zprocess-2.9.2/zprocess.egg-info/dependency_links.txt
--rw-r--r--   0 bilbo     (1000) bilbo     (1000)      287 2018-10-17 20:32:34.000000 zprocess-2.9.2/zprocess.egg-info/PKG-INFO
--rw-r--r--   0 bilbo     (1000) bilbo     (1000)        9 2018-10-17 20:32:34.000000 zprocess-2.9.2/zprocess.egg-info/top_level.txt
--rw-rw-r--   0 bilbo     (1000) bilbo     (1000)     1039 2018-10-17 20:30:01.000000 zprocess-2.9.2/setup.py
--rw-rw-r--   0 bilbo     (1000) bilbo     (1000)     1333 2016-01-21 05:04:25.000000 zprocess-2.9.2/LICENSE.txt
-drwxr-xr-x   0 bilbo     (1000) bilbo     (1000)        0 2018-10-17 20:32:34.000000 zprocess-2.9.2/zprocess/
--rw-r--r--   0 bilbo     (1000) bilbo     (1000)       22 2018-10-17 20:32:34.000000 zprocess-2.9.2/zprocess/__version__.py
--rw-r--r--   0 bilbo     (1000) bilbo     (1000)     3530 2018-09-21 00:50:39.000000 zprocess-2.9.2/zprocess/tasks.py
-drwxr-xr-x   0 bilbo     (1000) bilbo     (1000)        0 2018-10-17 20:32:34.000000 zprocess-2.9.2/zprocess/locking/
--rw-r--r--   0 bilbo     (1000) bilbo     (1000)    10149 2018-09-21 00:50:39.000000 zprocess-2.9.2/zprocess/locking/__init__.py
--rw-r--r--   0 bilbo     (1000) bilbo     (1000)     7358 2018-08-07 20:06:27.000000 zprocess-2.9.2/zprocess/locking/server_asyncio.py
--rw-r--r--   0 bilbo     (1000) bilbo     (1000)    21919 2018-09-21 00:50:39.000000 zprocess-2.9.2/zprocess/locking/server.py
--rw-r--r--   0 bilbo     (1000) bilbo     (1000)     5876 2018-09-21 00:50:39.000000 zprocess-2.9.2/zprocess/locking/__main__.py
--rw-r--r--   0 bilbo     (1000) bilbo     (1000)    17382 2018-08-08 02:45:00.000000 zprocess-2.9.2/zprocess/locking/server2.py
--rw-r--r--   0 bilbo     (1000) bilbo     (1000)     4557 2018-03-14 03:21:43.000000 zprocess-2.9.2/zprocess/utils.py
--rw-r--r--   0 bilbo     (1000) bilbo     (1000)     2487 2018-08-06 16:35:18.000000 zprocess-2.9.2/zprocess/__init__.py
--rw-rw-r--   0 bilbo     (1000) bilbo     (1000)     3610 2018-10-17 16:15:26.000000 zprocess-2.9.2/zprocess/process_class_wrapper.py
-drwxr-xr-x   0 bilbo     (1000) bilbo     (1000)        0 2018-10-17 20:32:34.000000 zprocess-2.9.2/zprocess/zlog/
--rw-rw-r--   0 bilbo     (1000) bilbo     (1000)     7875 2018-10-17 16:11:45.000000 zprocess-2.9.2/zprocess/zlog/__init__.py
--rw-rw-r--   0 bilbo     (1000) bilbo     (1000)    12654 2018-10-17 16:11:45.000000 zprocess-2.9.2/zprocess/zlog/server.py
--rw-r--r--   0 bilbo     (1000) bilbo     (1000)     6442 2018-09-22 00:20:54.000000 zprocess-2.9.2/zprocess/zlog/__main__.py
--rw-r--r--   0 bilbo     (1000) bilbo     (1000)     9182 2018-03-20 00:42:01.000000 zprocess-2.9.2/zprocess/security.py
--rw-rw-r--   0 bilbo     (1000) bilbo     (1000)    14828 2018-07-23 17:53:32.000000 zprocess-2.9.2/zprocess/clientserver.py
--rw-rw-r--   0 bilbo     (1000) bilbo     (1000)    44233 2018-10-17 20:31:15.000000 zprocess-2.9.2/zprocess/process_tree.py
--rw-r--r--   0 bilbo     (1000) bilbo     (1000)       38 2018-10-17 20:32:34.000000 zprocess-2.9.2/setup.cfg
+drwxr-xr-x   0 bilbo     (1000) bilbo     (1000)        0 2018-10-26 15:25:11.000000 zprocess-2.9.3/
+-rw-rw-r--   0 bilbo     (1000) bilbo     (1000)       39 2016-01-21 05:04:25.000000 zprocess-2.9.3/MANIFEST.in
+-rw-rw-r--   0 bilbo     (1000) bilbo     (1000)      250 2016-01-21 05:04:25.000000 zprocess-2.9.3/README.txt
+-rw-r--r--   0 bilbo     (1000) bilbo     (1000)      287 2018-10-26 15:25:11.000000 zprocess-2.9.3/PKG-INFO
+-rw-rw-r--   0 bilbo     (1000) bilbo     (1000)      380 2016-01-21 05:04:25.000000 zprocess-2.9.3/README.md
+drwxr-xr-x   0 bilbo     (1000) bilbo     (1000)        0 2018-10-26 15:25:11.000000 zprocess-2.9.3/zprocess.egg-info/
+-rw-r--r--   0 bilbo     (1000) bilbo     (1000)       52 2018-10-26 15:25:11.000000 zprocess-2.9.3/zprocess.egg-info/requires.txt
+-rw-r--r--   0 bilbo     (1000) bilbo     (1000)      622 2018-10-26 15:25:11.000000 zprocess-2.9.3/zprocess.egg-info/SOURCES.txt
+-rw-r--r--   0 bilbo     (1000) bilbo     (1000)        1 2018-10-26 15:25:11.000000 zprocess-2.9.3/zprocess.egg-info/dependency_links.txt
+-rw-r--r--   0 bilbo     (1000) bilbo     (1000)      287 2018-10-26 15:25:11.000000 zprocess-2.9.3/zprocess.egg-info/PKG-INFO
+-rw-r--r--   0 bilbo     (1000) bilbo     (1000)        9 2018-10-26 15:25:11.000000 zprocess-2.9.3/zprocess.egg-info/top_level.txt
+-rw-rw-r--   0 bilbo     (1000) bilbo     (1000)     1039 2018-10-26 15:24:31.000000 zprocess-2.9.3/setup.py
+-rw-rw-r--   0 bilbo     (1000) bilbo     (1000)     1333 2016-01-21 05:04:25.000000 zprocess-2.9.3/LICENSE.txt
+drwxr-xr-x   0 bilbo     (1000) bilbo     (1000)        0 2018-10-26 15:25:11.000000 zprocess-2.9.3/zprocess/
+-rw-r--r--   0 bilbo     (1000) bilbo     (1000)       22 2018-10-26 15:25:11.000000 zprocess-2.9.3/zprocess/__version__.py
+-rw-r--r--   0 bilbo     (1000) bilbo     (1000)     3530 2018-09-21 00:50:39.000000 zprocess-2.9.3/zprocess/tasks.py
+drwxr-xr-x   0 bilbo     (1000) bilbo     (1000)        0 2018-10-26 15:25:11.000000 zprocess-2.9.3/zprocess/locking/
+-rw-r--r--   0 bilbo     (1000) bilbo     (1000)    10149 2018-09-21 00:50:39.000000 zprocess-2.9.3/zprocess/locking/__init__.py
+-rw-r--r--   0 bilbo     (1000) bilbo     (1000)     7358 2018-08-07 20:06:27.000000 zprocess-2.9.3/zprocess/locking/server_asyncio.py
+-rw-r--r--   0 bilbo     (1000) bilbo     (1000)    21919 2018-09-21 00:50:39.000000 zprocess-2.9.3/zprocess/locking/server.py
+-rw-r--r--   0 bilbo     (1000) bilbo     (1000)     5876 2018-09-21 00:50:39.000000 zprocess-2.9.3/zprocess/locking/__main__.py
+-rw-r--r--   0 bilbo     (1000) bilbo     (1000)    17382 2018-08-08 02:45:00.000000 zprocess-2.9.3/zprocess/locking/server2.py
+-rw-r--r--   0 bilbo     (1000) bilbo     (1000)     4557 2018-03-14 03:21:43.000000 zprocess-2.9.3/zprocess/utils.py
+-rw-r--r--   0 bilbo     (1000) bilbo     (1000)     2487 2018-08-06 16:35:18.000000 zprocess-2.9.3/zprocess/__init__.py
+-rw-rw-r--   0 bilbo     (1000) bilbo     (1000)     3610 2018-10-17 16:15:26.000000 zprocess-2.9.3/zprocess/process_class_wrapper.py
+drwxr-xr-x   0 bilbo     (1000) bilbo     (1000)        0 2018-10-26 15:25:11.000000 zprocess-2.9.3/zprocess/zlog/
+-rw-rw-r--   0 bilbo     (1000) bilbo     (1000)     7875 2018-10-17 16:11:45.000000 zprocess-2.9.3/zprocess/zlog/__init__.py
+-rw-rw-r--   0 bilbo     (1000) bilbo     (1000)    12654 2018-10-17 16:11:45.000000 zprocess-2.9.3/zprocess/zlog/server.py
+-rw-r--r--   0 bilbo     (1000) bilbo     (1000)     6442 2018-09-22 00:20:54.000000 zprocess-2.9.3/zprocess/zlog/__main__.py
+-rw-r--r--   0 bilbo     (1000) bilbo     (1000)     9182 2018-03-20 00:42:01.000000 zprocess-2.9.3/zprocess/security.py
+-rw-rw-r--   0 bilbo     (1000) bilbo     (1000)    14828 2018-07-23 17:53:32.000000 zprocess-2.9.3/zprocess/clientserver.py
+-rw-rw-r--   0 bilbo     (1000) bilbo     (1000)    44335 2018-10-26 15:22:49.000000 zprocess-2.9.3/zprocess/process_tree.py
+-rw-r--r--   0 bilbo     (1000) bilbo     (1000)       38 2018-10-26 15:25:11.000000 zprocess-2.9.3/setup.cfg
```

### Comparing `zprocess-2.9.2/zprocess.egg-info/SOURCES.txt` & `zprocess-2.9.3/zprocess.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `zprocess-2.9.2/setup.py` & `zprocess-2.9.3/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -7,15 +7,15 @@
 # If the package is not registered with PyPI yet, do so with:
 #
 # python setup.py register
 
 from setuptools import setup
 import os
 
-VERSION = '2.9.2'
+VERSION = '2.9.3'
 
 # Auto generate a __version__ package for the package to import
 with open(os.path.join('zprocess', '__version__.py'), 'w') as f:
     f.write("__version__ = '%s'\n"%VERSION)
 
 dependencies = ['pyzmq >= 15.3', 'xmlrunner']
```

### Comparing `zprocess-2.9.2/LICENSE.txt` & `zprocess-2.9.3/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `zprocess-2.9.2/zprocess/tasks.py` & `zprocess-2.9.3/zprocess/tasks.py`

 * *Files identical despite different names*

### Comparing `zprocess-2.9.2/zprocess/locking/__init__.py` & `zprocess-2.9.3/zprocess/locking/__init__.py`

 * *Files identical despite different names*

### Comparing `zprocess-2.9.2/zprocess/locking/server_asyncio.py` & `zprocess-2.9.3/zprocess/locking/server_asyncio.py`

 * *Files identical despite different names*

### Comparing `zprocess-2.9.2/zprocess/locking/server.py` & `zprocess-2.9.3/zprocess/locking/server.py`

 * *Files identical despite different names*

### Comparing `zprocess-2.9.2/zprocess/locking/__main__.py` & `zprocess-2.9.3/zprocess/locking/__main__.py`

 * *Files identical despite different names*

### Comparing `zprocess-2.9.2/zprocess/locking/server2.py` & `zprocess-2.9.3/zprocess/locking/server2.py`

 * *Files identical despite different names*

### Comparing `zprocess-2.9.2/zprocess/utils.py` & `zprocess-2.9.3/zprocess/utils.py`

 * *Files identical despite different names*

### Comparing `zprocess-2.9.2/zprocess/__init__.py` & `zprocess-2.9.3/zprocess/__init__.py`

 * *Files identical despite different names*

### Comparing `zprocess-2.9.2/zprocess/process_class_wrapper.py` & `zprocess-2.9.3/zprocess/process_class_wrapper.py`

 * *Files identical despite different names*

### Comparing `zprocess-2.9.2/zprocess/zlog/__init__.py` & `zprocess-2.9.3/zprocess/zlog/__init__.py`

 * *Files identical despite different names*

### Comparing `zprocess-2.9.2/zprocess/zlog/server.py` & `zprocess-2.9.3/zprocess/zlog/server.py`

 * *Files identical despite different names*

### Comparing `zprocess-2.9.2/zprocess/zlog/__main__.py` & `zprocess-2.9.3/zprocess/zlog/__main__.py`

 * *Files identical despite different names*

### Comparing `zprocess-2.9.2/zprocess/security.py` & `zprocess-2.9.3/zprocess/security.py`

 * *Files identical despite different names*

### Comparing `zprocess-2.9.2/zprocess/clientserver.py` & `zprocess-2.9.3/zprocess/clientserver.py`

 * *Files identical despite different names*

### Comparing `zprocess-2.9.2/zprocess/process_tree.py` & `zprocess-2.9.3/zprocess/process_tree.py`

 * *Files 1% similar despite different names*

```diff
@@ -621,25 +621,27 @@
 class Process(object):
     """A class providing similar functionality to multiprocessing.Process, but
     using zmq for communication and creating processes in a fresh environment
     rather than by forking (or imitation forking as in Windows). Do not override
     its methods other than run()."""
 
     def __init__(self, process_tree, output_redirection_port=None,
-                 remote_process_client=None, subclass_fullname=None):
+                 remote_process_client=None, subclass_fullname=None,
+                 startup_timeout=5):
         self._redirection_port = output_redirection_port
         self.process_tree = process_tree
         self.to_child = None
         self.from_child = None
         self.child = None
         self.to_parent = None
         self.from_parent = None
         self.kill_lock = None
         self.remote_process_client = remote_process_client
         self.subclass_fullname = subclass_fullname
+        self.startup_timeout = startup_timeout
         if subclass_fullname is not None:
             if self.__class__ is not Process:
                 msg = ("Can only pass subclass_fullname to Process directly, " +
                        "not to a subclass")
                 raise ValueError(msg)
 
     def start(self, *args, **kwargs):
@@ -679,15 +681,15 @@
             self.to_child.put(self.__class__)
         else:
             # No module info - the child process will find the class all on its own
             # from the fully qualified name:
             self.to_child.put([None, None, None])
             self.to_child.put(self.subclass_fullname)
 
-        response = self.from_child.get(timeout=5)
+        response = self.from_child.get(timeout=self.startup_timeout)
         if response != 'ok':
             msg = "Error in child process importing specified Process subclass:\n\n%s"
             raise Exception(msg % str(response))
             
         self.to_child.put([args, kwargs])
         return self.to_child, self.from_child
```

