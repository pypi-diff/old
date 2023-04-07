# Comparing `tmp/opq-2.tar.gz` & `tmp/opq-3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "opq-2.tar", last modified: Mon Feb  6 02:33:16 2023, max compression
+gzip compressed data, was "opq-3.tar", last modified: Mon Feb  6 17:21:18 2023, max compression
```

## Comparing `opq-2.tar` & `opq-3.tar`

### file list

```diff
@@ -1,29 +1,21 @@
-drwxr-xr-x   0 bart      (1000) bart      (1001)        0 2023-02-06 02:33:16.521487 opq-2/
--rw-r--r--   0 bart      (1000) bart      (1001)     2726 2023-02-06 02:33:16.521487 opq-2/PKG-INFO
--rw-r--r--   0 bart      (1000) bart      (1001)     1618 2023-02-06 02:07:56.000000 opq-2/README.rst
-drwxr-xr-x   0 bart      (1000) bart      (1001)        0 2023-02-06 02:33:16.517487 opq-2/opq/
--rw-r--r--   0 bart      (1000) bart      (1001)      110 2023-02-06 02:32:50.000000 opq-2/opq/__init__.py
--rw-r--r--   0 bart      (1000) bart      (1001)     2714 2023-02-06 02:16:34.000000 opq-2/opq/dbs.py
--rw-r--r--   0 bart      (1000) bart      (1001)      416 2023-02-06 00:09:43.000000 opq-2/opq/dft.py
--rw-r--r--   0 bart      (1000) bart      (1001)     1615 2023-02-06 02:14:57.000000 opq-2/opq/jsn.py
--rw-r--r--   0 bart      (1000) bart      (1001)     2761 2023-02-06 02:14:12.000000 opq-2/opq/obj.py
--rw-r--r--   0 bart      (1000) bart      (1001)      509 2023-02-06 02:13:42.000000 opq-2/opq/pst.py
--rw-r--r--   0 bart      (1000) bart      (1001)     2899 2023-02-06 02:12:44.000000 opq-2/opq/utl.py
--rw-r--r--   0 bart      (1000) bart      (1001)      896 2023-02-06 00:09:43.000000 opq-2/opq/wdr.py
-drwxr-xr-x   0 bart      (1000) bart      (1001)        0 2023-02-06 02:33:16.521487 opq-2/opq.egg-info/
--rw-r--r--   0 bart      (1000) bart      (1001)     2726 2023-02-06 02:33:16.000000 opq-2/opq.egg-info/PKG-INFO
--rw-r--r--   0 bart      (1000) bart      (1001)      378 2023-02-06 02:33:16.000000 opq-2/opq.egg-info/SOURCES.txt
--rw-r--r--   0 bart      (1000) bart      (1001)        1 2023-02-06 02:33:16.000000 opq-2/opq.egg-info/dependency_links.txt
--rw-r--r--   0 bart      (1000) bart      (1001)        4 2023-02-06 02:33:16.000000 opq-2/opq.egg-info/top_level.txt
--rw-r--r--   0 bart      (1000) bart      (1001)       38 2023-02-06 02:33:16.521487 opq-2/setup.cfg
--rw-r--r--   0 bart      (1000) bart      (1001)      711 2023-02-06 02:26:34.000000 opq-2/setup.py
-drwxr-xr-x   0 bart      (1000) bart      (1001)        0 2023-02-06 02:33:16.521487 opq-2/test/
--rw-r--r--   0 bart      (1000) bart      (1001)      245 2023-02-06 00:09:43.000000 opq-2/test/test_cls.py
--rw-r--r--   0 bart      (1000) bart      (1001)      231 2023-02-06 00:09:43.000000 opq-2/test/test_dft.py
--rw-r--r--   0 bart      (1000) bart      (1001)      825 2023-02-06 02:08:53.000000 opq-2/test/test_inherit.py
--rw-r--r--   0 bart      (1000) bart      (1001)      467 2023-02-06 00:09:43.000000 opq-2/test/test_jsn.py
--rw-r--r--   0 bart      (1000) bart      (1001)     4567 2023-02-06 00:09:43.000000 opq-2/test/test_obj.py
--rw-r--r--   0 bart      (1000) bart      (1001)      320 2023-02-06 00:09:43.000000 opq-2/test/test_path.py
--rw-r--r--   0 bart      (1000) bart      (1001)      357 2023-02-06 02:26:13.000000 opq-2/test/test_pst.py
--rw-r--r--   0 bart      (1000) bart      (1001)      382 2023-02-06 00:09:43.000000 opq-2/test/test_utl.py
--rw-r--r--   0 bart      (1000) bart      (1001)      227 2023-02-06 00:09:43.000000 opq-2/test/test_wdr.py
+drwxr-xr-x   0 bart      (1000) bart      (1001)        0 2023-02-06 17:21:18.383780 opq-3/
+-rw-r--r--   0 bart      (1000) bart      (1001)     2475 2023-02-06 17:21:18.383780 opq-3/PKG-INFO
+-rw-r--r--   0 bart      (1000) bart      (1001)     1410 2023-02-06 16:42:15.000000 opq-3/README.rst
+drwxr-xr-x   0 bart      (1000) bart      (1001)        0 2023-02-06 17:21:18.379780 opq-3/bin/
+-rwxr-xr-x   0 bart      (1000) bart      (1001)     2641 2023-02-06 16:59:19.000000 opq-3/bin/opq
+drwxr-xr-x   0 bart      (1000) bart      (1001)        0 2023-02-06 17:21:18.383780 opq-3/opq/
+-rw-r--r--   0 bart      (1000) bart      (1001)      755 2023-02-06 16:58:00.000000 opq-3/opq/__init__.py
+-rw-r--r--   0 bart      (1000) bart      (1001)      407 2023-02-06 15:37:07.000000 opq-3/opq/default.py
+-rw-r--r--   0 bart      (1000) bart      (1001)     1637 2023-02-06 15:37:07.000000 opq-3/opq/encoder.py
+-rw-r--r--   0 bart      (1000) bart      (1001)     2762 2023-02-06 17:20:04.000000 opq-3/opq/objects.py
+-rw-r--r--   0 bart      (1000) bart      (1001)      116 2023-02-06 16:51:46.000000 opq-3/opq/opqueue.py
+-rw-r--r--   0 bart      (1000) bart      (1001)     3761 2023-02-06 17:18:21.000000 opq-3/opq/storage.py
+-rw-r--r--   0 bart      (1000) bart      (1001)     2899 2023-02-06 17:21:04.000000 opq-3/opq/utility.py
+drwxr-xr-x   0 bart      (1000) bart      (1001)        0 2023-02-06 17:21:18.383780 opq-3/opq.egg-info/
+-rw-r--r--   0 bart      (1000) bart      (1001)     2475 2023-02-06 17:21:18.000000 opq-3/opq.egg-info/PKG-INFO
+-rw-r--r--   0 bart      (1000) bart      (1001)      263 2023-02-06 17:21:18.000000 opq-3/opq.egg-info/SOURCES.txt
+-rw-r--r--   0 bart      (1000) bart      (1001)        1 2023-02-06 17:21:18.000000 opq-3/opq.egg-info/dependency_links.txt
+-rw-r--r--   0 bart      (1000) bart      (1001)        4 2023-02-06 17:21:18.000000 opq-3/opq.egg-info/top_level.txt
+-rw-r--r--   0 bart      (1000) bart      (1001)        1 2023-02-06 17:21:18.000000 opq-3/opq.egg-info/zip-safe
+-rw-r--r--   0 bart      (1000) bart      (1001)       38 2023-02-06 17:21:18.383780 opq-3/setup.cfg
+-rw-r--r--   0 bart      (1000) bart      (1001)      744 2023-02-06 15:44:08.000000 opq-3/setup.py
```

### Comparing `opq-2/PKG-INFO` & `opq-3/PKG-INFO`

 * *Files 11% similar despite different names*

```diff
@@ -1,38 +1,34 @@
 Metadata-Version: 2.1
 Name: opq
-Version: 2
-Summary: functional programming with objects
+Version: 3
+Summary: object programming queue
 Home-page: http://github.com/operbot/opq
 Author: Bart Thate
 Author-email: operbot100@gmail.com
 License: Public Domain
 Description: README
         ######
         
         **NAME**
         
         |
-        | ``opq`` - object programming
+        | ``opq`` - object programming queue
         |
         
         **SYNOPSIS**
         
         
         The ``opq`` package provides an Object class, that allows for save/load to/from
-        json files on disk. Objects can be searched with database functions and uses
-        read-only files to improve persistence and a type in filename for
-        reconstruction. Methods are factored out into functions to have a clean
-        namespace to read JSON data into.
-        
-        ``opq`` stores it's data on disk where objects are time versioned and the
-        last version saved on disk is served to the user layer. Files are JSON dumps
-        that are read-only so thus should provide (disk) persistence. Paths carry the
-        type in the path name what makes reconstruction from filename easier then
-        reading type from the object.
+        json files on disk. Objects can be searched with database functions and have a 
+        type in filename for reconstruction. Methods are factored out into functions to
+        have a clean namespace to read JSON data into.
+        
+        This package should result in a Queue derived (or compatible) class that can
+        keep objects in sync on a multiprocessor environment.
         
         |
         
         **INSTALL**
         
         |
         | ``python3 -m pip install opq``
@@ -65,22 +61,22 @@
          >>> 'value'
         
         great for giving objects peristence by having their state stored in files::
         
          >>> from opq import Object, save
          >>> o = Object()
          >>> save(o)
-         'opq.Object/2021-08-31/15:31:05.717063'
+         'opq.objects.Object/2021-08-31/15:31:05.717063'
         
         |
         
         **AUTHOR**
         
         |
-        | B.H.J. Thate 
+        | B.H.J. Thate <operbot100@gmail.com>
         |
         
         **COPYRIGHT**
         
         |
         | ``opq`` is placed in the Public Domain.
         |
```

### Comparing `opq-2/README.rst` & `opq-3/README.rst`

 * *Files 21% similar despite different names*

```diff
@@ -1,30 +1,26 @@
 README
 ######
 
 **NAME**
 
 |
-| ``opq`` - object programming
+| ``opq`` - object programming queue
 |
 
 **SYNOPSIS**
 
 
 The ``opq`` package provides an Object class, that allows for save/load to/from
-json files on disk. Objects can be searched with database functions and uses
-read-only files to improve persistence and a type in filename for
-reconstruction. Methods are factored out into functions to have a clean
-namespace to read JSON data into.
-
-``opq`` stores it's data on disk where objects are time versioned and the
-last version saved on disk is served to the user layer. Files are JSON dumps
-that are read-only so thus should provide (disk) persistence. Paths carry the
-type in the path name what makes reconstruction from filename easier then
-reading type from the object.
+json files on disk. Objects can be searched with database functions and have a 
+type in filename for reconstruction. Methods are factored out into functions to
+have a clean namespace to read JSON data into.
+
+This package should result in a Queue derived (or compatible) class that can
+keep objects in sync on a multiprocessor environment.
 
 |
 
 **INSTALL**
 
 |
 | ``python3 -m pip install opq``
@@ -57,22 +53,22 @@
  >>> 'value'
 
 great for giving objects peristence by having their state stored in files::
 
  >>> from opq import Object, save
  >>> o = Object()
  >>> save(o)
- 'opq.Object/2021-08-31/15:31:05.717063'
+ 'opq.objects.Object/2021-08-31/15:31:05.717063'
 
 |
 
 **AUTHOR**
 
 |
-| B.H.J. Thate 
+| B.H.J. Thate <operbot100@gmail.com>
 |
 
 **COPYRIGHT**
 
 |
 | ``opq`` is placed in the Public Domain.
 |
```

### Comparing `opq-2/opq/dbs.py` & `opq-3/opq/storage.py`

 * *Files 19% similar despite different names*

```diff
@@ -1,63 +1,34 @@
 # This file is placed in the Public Domain.
 
 
 "database"
 
 
 import os
-import _thread
 
 
-from .jsn import load
-from .obj import Object, search
-from .utl import fnclass, fntime
-from .wdr import Wd
+from .encoder import dump, load
+from .objects import Object, kind, oid, search, update
+from .utility import fnclass, fntime
 
 
 def __dir__():
     return (
             'Classes',
             'Db',
-            'load',
+            'Wd',
+            'last',
+            'save'
            )
 
 
 __all__ = __dir__()
 
 
-disklock = _thread.allocate_lock()
-
-
-class Classes:
-
-    cls = {}
-
-    @staticmethod
-    def add(clz):
-        Classes.cls["%s.%s" % (clz.__module__, clz.__name__)] =  clz
-
-    @staticmethod
-    def all(oname=None):
-        res = []
-        for key, value in Classes.cls.items():
-            if oname is not None and oname not in key:
-                continue
-            res.append(value)
-        return res
-
-    @staticmethod
-    def get(oname):
-        return Classes.cls.get(oname, None)
-
-
-    @staticmethod
-    def remove(oname):
-        del Classes.cls[oname]
-
 
 class Db:
 
     @staticmethod
     def all(otp, selector=None):
         names = Wd.types(otp)
         for nme in names:
@@ -75,15 +46,15 @@
             if selector and not search(obj, selector):
                 continue
             yield fnm, obj
 
     @staticmethod
     def fns(otp):
         assert Wd.workdir
-        path = os.path.join(Wd.workdir, "store", otp) + os.sep
+        path = Wd.getpath(otp)
         dname = ""
         for rootdir, dirs, _files in os.walk(path, topdown=False):
             if dirs:
                 dname = sorted(dirs)[-1]
                 if dname.count("-") == 2:
                     ddd = os.path.join(rootdir, dname)
                     fls = sorted(os.listdir(ddd))
@@ -117,8 +88,88 @@
         for nme in names:
             item = Db.last(nme, selector)
             if item:
                 return item
         return None, None
 
 
+class Classes:
+
+    cls = {}
+
+    @staticmethod
+    def add(clz):
+        Classes.cls["%s.%s" % (clz.__module__, clz.__name__)] =  clz
+
+    @staticmethod
+    def all(oname=None):
+        res = []
+        for key, value in Classes.cls.items():
+            if oname is not None and oname not in key:
+                continue
+            res.append(value)
+        return res
+
+    @staticmethod
+    def get(oname):
+        return Classes.cls.get(oname, None)
+
+
+    @staticmethod
+    def remove(oname):
+        del Classes.cls[oname]
+
+
+class Wd:
+
+    workdir = ".opq"
+
+    @staticmethod
+    def get():
+        assert Wd.workdir
+        return Wd.workdir
+
+    @staticmethod
+    def getpath(path):
+        return os.path.join(Wd.get(), "store", path)
+
+    @staticmethod
+    def set(path):
+        Wd.workdir = path
+
+    @staticmethod
+    def storedir():
+        return os.path.join(Wd.get(), "store")
+
+    @staticmethod
+    def strip(path):
+        return path.split("store")[-1][1:]
+
+    @staticmethod
+    def types(oname=None):
+        res = []
+        path = Wd.storedir()
+        if not os.path.exists(path):
+            return res
+        for fnm in os.listdir(path):
+            if oname and oname.lower() not in fnm.split(".")[-1].lower():
+                continue
+            if fnm not in res:
+                res.append(fnm)
+        return res
+
+
 Classes.add(Object)
+
+
+def last(obj, selector=None):
+    if selector is None:
+        selector = {}
+    _fn, ooo = Db.last(kind(obj), selector)
+    if ooo:
+        update(obj, ooo)
+
+
+def save(obj):
+    opath = Wd.getpath(oid(obj))
+    dump(obj, opath)
+    return Wd.strip(opath)
```

### Comparing `opq-2/opq/jsn.py` & `opq-3/opq/encoder.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,19 +1,19 @@
 # This file is placed in the Public Domain.
 
 
-"json"
+"json encoder/decoder"
 
 
 import json
 import _thread
 
 
-from .obj import Object, update
-from .utl import cdir, locked
+from .objects import Object, update
+from .utility import cdir, locked
 
 
 def __dir__():
     return (
             'ObjectDecoder',
             'ObjectEncoder',
             'dump',
@@ -63,16 +63,16 @@
     with open(opath, "w", encoding="utf-8") as ofile:
         json.dump(
             obj.__dict__, ofile, cls=ObjectEncoder, indent=4, sort_keys=True
         )
     return opath
 
 
-def dumps(self):
-    return json.dumps(self, cls=ObjectEncoder)
+def dumps(obj):
+    return json.dumps(obj, cls=ObjectEncoder)
 
 
 @locked(disklock)
 def load(obj, opath):
     with open(opath, "r", encoding="utf-8") as ofile:
         res = json.load(ofile, cls=ObjectDecoder)
         update(obj, res)
```

### Comparing `opq-2/opq/obj.py` & `opq-3/opq/objects.py`

 * *Files 0% similar despite different names*

```diff
@@ -22,14 +22,15 @@
             'values'
             )
 
 
 __all__ = __dir__()
 
 
+
 class Object:
 
     def __init__(self, *args, **kwargs):
         if args:
             val = args[0]
             if isinstance(val, list):
                 update(self, dict(val))
```

### Comparing `opq-2/opq/utl.py` & `opq-3/opq/utility.py`

 * *Files identical despite different names*

### Comparing `opq-2/opq.egg-info/PKG-INFO` & `opq-3/opq.egg-info/PKG-INFO`

 * *Files 11% similar despite different names*

```diff
@@ -1,38 +1,34 @@
 Metadata-Version: 2.1
 Name: opq
-Version: 2
-Summary: functional programming with objects
+Version: 3
+Summary: object programming queue
 Home-page: http://github.com/operbot/opq
 Author: Bart Thate
 Author-email: operbot100@gmail.com
 License: Public Domain
 Description: README
         ######
         
         **NAME**
         
         |
-        | ``opq`` - object programming
+        | ``opq`` - object programming queue
         |
         
         **SYNOPSIS**
         
         
         The ``opq`` package provides an Object class, that allows for save/load to/from
-        json files on disk. Objects can be searched with database functions and uses
-        read-only files to improve persistence and a type in filename for
-        reconstruction. Methods are factored out into functions to have a clean
-        namespace to read JSON data into.
-        
-        ``opq`` stores it's data on disk where objects are time versioned and the
-        last version saved on disk is served to the user layer. Files are JSON dumps
-        that are read-only so thus should provide (disk) persistence. Paths carry the
-        type in the path name what makes reconstruction from filename easier then
-        reading type from the object.
+        json files on disk. Objects can be searched with database functions and have a 
+        type in filename for reconstruction. Methods are factored out into functions to
+        have a clean namespace to read JSON data into.
+        
+        This package should result in a Queue derived (or compatible) class that can
+        keep objects in sync on a multiprocessor environment.
         
         |
         
         **INSTALL**
         
         |
         | ``python3 -m pip install opq``
@@ -65,22 +61,22 @@
          >>> 'value'
         
         great for giving objects peristence by having their state stored in files::
         
          >>> from opq import Object, save
          >>> o = Object()
          >>> save(o)
-         'opq.Object/2021-08-31/15:31:05.717063'
+         'opq.objects.Object/2021-08-31/15:31:05.717063'
         
         |
         
         **AUTHOR**
         
         |
-        | B.H.J. Thate 
+        | B.H.J. Thate <operbot100@gmail.com>
         |
         
         **COPYRIGHT**
         
         |
         | ``opq`` is placed in the Public Domain.
         |
```

### Comparing `opq-2/setup.py` & `opq-3/setup.py`

 * *Files 19% similar despite different names*

```diff
@@ -9,23 +9,25 @@
 
 def read():
     return open("README.rst", "r").read()
 
 
 setup(
     name="opq",
-    version="2",
+    version="3",
     author="Bart Thate",
     author_email="operbot100@gmail.com",
     url="http://github.com/operbot/opq",
-    description="functional programming with objects",
+    zip_safe=True,
+    description="object programming queue",
     long_description=read(),
     long_description_content_type="text/x-rst",
     license="Public Domain",
     packages=["opq"],
+    scripts=["bin/opq"],
     classifiers=[
         "Development Status :: 4 - Beta",
         "License :: Public Domain",
         "Programming Language :: Python :: 3 :: Only",
         "Topic :: Software Development :: Libraries :: Python Modules",
      ],
 )
```

