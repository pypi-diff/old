# Comparing `tmp/streamcpy-1.0.tar.gz` & `tmp/streamcpy-1.0.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "streamcpy-1.0.tar", last modified: Fri Apr  7 11:47:53 2023, max compression
+gzip compressed data, was "streamcpy-1.0.1.tar", last modified: Fri Apr  7 11:59:13 2023, max compression
```

## Comparing `streamcpy-1.0.tar` & `streamcpy-1.0.1.tar`

### file list

```diff
@@ -1,13 +1,12 @@
-drwxrwxrwx   0 littlebutt  (1000) littlebutt  (1000)        0 2023-04-07 11:47:53.198387 streamcpy-1.0/
--rwxrwxrwx   0 littlebutt  (1000) littlebutt  (1000)    35823 2023-02-25 09:50:44.000000 streamcpy-1.0/LICENSE
--rwxrwxrwx   0 littlebutt  (1000) littlebutt  (1000)    10880 2023-04-07 11:47:53.186895 streamcpy-1.0/PKG-INFO
--rwxrwxrwx   0 littlebutt  (1000) littlebutt  (1000)     3269 2023-04-07 11:26:24.000000 streamcpy-1.0/README.md
--rwxrwxrwx   0 littlebutt  (1000) littlebutt  (1000)     3403 2023-04-07 11:22:54.000000 streamcpy-1.0/README.rst
--rwxrwxrwx   0 littlebutt  (1000) littlebutt  (1000)       38 2023-04-07 11:47:53.198387 streamcpy-1.0/setup.cfg
--rwxrwxrwx   0 littlebutt  (1000) littlebutt  (1000)     1140 2023-04-07 11:47:07.000000 streamcpy-1.0/setup.py
--rwxrwxrwx   0 littlebutt  (1000) littlebutt  (1000)     1392 2023-03-15 14:04:05.000000 streamcpy-1.0/streamcpy.c
-drwxrwxrwx   0 littlebutt  (1000) littlebutt  (1000)        0 2023-04-07 11:47:53.181857 streamcpy-1.0/streamcpy.egg-info/
--rwxrwxrwx   0 littlebutt  (1000) littlebutt  (1000)    10880 2023-04-07 11:47:53.000000 streamcpy-1.0/streamcpy.egg-info/PKG-INFO
--rwxrwxrwx   0 littlebutt  (1000) littlebutt  (1000)      181 2023-04-07 11:47:53.000000 streamcpy-1.0/streamcpy.egg-info/SOURCES.txt
--rwxrwxrwx   0 littlebutt  (1000) littlebutt  (1000)        1 2023-04-07 11:47:53.000000 streamcpy-1.0/streamcpy.egg-info/dependency_links.txt
--rwxrwxrwx   0 littlebutt  (1000) littlebutt  (1000)       10 2023-04-07 11:47:53.000000 streamcpy-1.0/streamcpy.egg-info/top_level.txt
+drwxrwxrwx   0        0        0        0 2023-04-07 11:59:13.023441 streamcpy-1.0.1/
+-rw-rw-rw-   0        0        0    35823 2023-02-25 09:50:44.000000 streamcpy-1.0.1/LICENSE
+-rw-rw-rw-   0        0        0     3809 2023-04-07 11:59:13.022444 streamcpy-1.0.1/PKG-INFO
+-rw-rw-rw-   0        0        0     3403 2023-04-07 11:52:47.000000 streamcpy-1.0.1/README.rst
+-rw-rw-rw-   0        0        0       42 2023-04-07 11:59:13.024443 streamcpy-1.0.1/setup.cfg
+-rw-rw-rw-   0        0        0      554 2023-04-07 11:57:13.000000 streamcpy-1.0.1/setup.py
+-rw-rw-rw-   0        0        0     1392 2023-03-15 14:04:05.000000 streamcpy-1.0.1/streamcpy.c
+drwxrwxrwx   0        0        0        0 2023-04-07 11:59:13.020449 streamcpy-1.0.1/streamcpy.egg-info/
+-rw-rw-rw-   0        0        0     3809 2023-04-07 11:59:12.000000 streamcpy-1.0.1/streamcpy.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      171 2023-04-07 11:59:12.000000 streamcpy-1.0.1/streamcpy.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-07 11:59:12.000000 streamcpy-1.0.1/streamcpy.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       10 2023-04-07 11:59:12.000000 streamcpy-1.0.1/streamcpy.egg-info/top_level.txt
```

### Comparing `streamcpy-1.0/LICENSE` & `streamcpy-1.0.1/LICENSE`

 * *Files identical despite different names*

### Comparing `streamcpy-1.0/README.md` & `streamcpy-1.0.1/README.rst`

 * *Files 21% similar despite different names*

```diff
@@ -1,101 +1,132 @@
-# streamcpy: The Stream Api in Python
-
-Streamcpy can provide an approach of processing the data in a high-effenciency way. Like in [Java](https://docs.oracle.com/javase/8/docs/api/java/util/stream/Stream.html), you can use stream-like  methods ( ``map`` , ``filter`` , ``for_each`` and so on) to do parrallel calculation and lazy calculation, which can accelerating your programs. What's more, The package is implemented in pure C, which means its runtime speed is even higher!
-
-Currently, the methods bellow is implemented.
-
-- [x] filter
-- [x] map
-- [x] for_each
-- [x] collect
-- [x] distinct
-- [x] limit
-- [x] reduce
-- [x] sorted
-- [x] max/min
-- [x] count
-- [x] any_match/all_match
-
-## Installation
-
-(Not Uploaded yet)
-
-## Usage
-
-Like Stream Api in Java but slightly different in details
-
-```python
-from streampy import *
-
-Stream.of([1, 2, 3])
-    .map(lambda x: x * x)
-    .for_each(lambda x: print(x))
-
-```
-
-This api supports various [Iterable](https://docs.python.org/3/library/stdtypes.html#typeiter) object in Python, like list, tuple and generator. As a result, you can call it in these ways:
-
-```python
-from streampy import *
-
-Stream.of((1, 2, 3))
-    .map(lambda x: x * x)
-    .for_each(lambda x: print(x))
-
-# OR
-
-def gen():
-    l = [1, 2, 3]
-    for i in l:
-        yield i
-
-g = gen()
-
-Stream.of(g)
-    .map(lambda x: x * x)
-    .for_each(lambda x: print(x))
-
-# OR
-
-Stream.of(open("foo.txt", 'r'))
-    .map(lambda x: x * x)
-    .for_each(lambda x: print(x))   
-```
-
-## Contribution
-
-Welcome to contribute to the project. The project is written in C. If you cannot understand Python's C API, you can refer to the code in __python__ package. It is the streamcpy implemented in python but will not be packed in the package. Here is the detailed description for each directory or file:
-
-- benchmark: a roughly comparison between Python and C++ (*Python wins*)
-- build: the built file of the package ( ``.pyd`` for Windows and ``.so`` for Linux or Mac)
-- modules: the source code for streamcpy in C
-- python: the source code for streamcpy in python and only for reference
-- vs: the project files for Visual Studio
-- setup.py: the setup file for python
-- streamcpy.c: the entrance file for streamcpy package
-- streamcpy.pyi: the ``.pyi`` file for streamcpy package
-  
-### Build on Windows
-
-- Download and install the latest [Visual Studio](https://visualstudio.microsoft.com/)
-- Install Python Development workload. The workload includes the Python native development tools, which bring in the C++ workload and toolsets that are necessary for native extensions
-- Install Desktop Development with C++ workload. It comes with the default core editor, which includes basic code editing support for C/C++
-- Double-click the ``.vcxproj`` in vs folder and build the ``.sln`` file
-- Run the project!
-
-### Build on Linux/Mac
-
-- Download the Python interpreter from the offcial website
-- Download the gcc(>7.5.0)
-- Run the command below for building
-  
-```shell
-python setup.py build
-```
-
-- Run the command below for installing
-  
-```shell
-python setup.py install
-```
-> NOTE: The method is also suitable for Windows if Visual Studio or Visual Studio Build Tools installed.
+streamcpy: The Stream Api in Python
+===================================
+
+Streamcpy can provide an approach of processing the data in a
+high-effenciency way. Like in
+`Java <https://docs.oracle.com/javase/8/docs/api/java/util/stream/Stream.html>`__,
+you can use stream-like methods (``map``, ``filter``, ``for_each`` and
+so on) to do parrallel calculation and lazy calculation, which can
+accelerating your programs. What’s more, The package is implemented in
+pure C, which means its runtime speed is even higher!
+
+Currently, the methods bellow is implemented.
+
+-  ☒ filter
+-  ☒ map
+-  ☒ for_each
+-  ☒ collect
+-  ☒ distinct
+-  ☒ limit
+-  ☒ reduce
+-  ☒ sorted
+-  ☒ max/min
+-  ☒ count
+-  ☒ any_match/all_match
+
+Installation
+------------
+
+(Not Uploaded yet)
+
+Usage
+-----
+
+Like Stream Api in Java but slightly different in details
+
+.. code:: python
+
+   from streampy import *
+
+   Stream.of([1, 2, 3])
+       .map(lambda x: x * x)
+       .for_each(lambda x: print(x))
+
+This api supports various
+`Iterable <https://docs.python.org/3/library/stdtypes.html#typeiter>`__
+object in Python, like list, tuple and generator. As a result, you can
+call it in these ways:
+
+.. code:: python
+
+   from streampy import *
+
+   Stream.of((1, 2, 3))
+       .map(lambda x: x * x)
+       .for_each(lambda x: print(x))
+
+   # OR
+
+   def gen():
+       l = [1, 2, 3]
+       for i in l:
+           yield i
+
+   g = gen()
+
+   Stream.of(g)
+       .map(lambda x: x * x)
+       .for_each(lambda x: print(x))
+
+   # OR
+
+   Stream.of(open("foo.txt", 'r'))
+       .map(lambda x: x * x)
+       .for_each(lambda x: print(x))   
+
+Contribution
+------------
+
+Welcome to contribute to the project. The project is written in C. If
+you cannot understand Python’s C API, you can refer to the code in
+**python** package. It is the streamcpy implemented in python but will
+not be packed in the package. Here is the detailed description for each
+directory or file:
+
+-  benchmark: a roughly comparison between Python and C++ (*Python
+   wins*)
+-  build: the built file of the package (``.pyd`` for Windows and
+   ``.so`` for Linux or Mac)
+-  modules: the source code for streamcpy in C
+-  python: the source code for streamcpy in python and only for
+   reference
+-  vs: the project files for Visual Studio
+-  setup.py: the setup file for python
+-  streamcpy.c: the entrance file for streamcpy package
+-  streamcpy.pyi: the ``.pyi`` file for streamcpy package
+
+Build on Windows
+~~~~~~~~~~~~~~~~
+
+-  Download and install the latest `Visual
+   Studio <https://visualstudio.microsoft.com/>`__
+-  Install Python Development workload. The workload includes the Python
+   native development tools, which bring in the C++ workload and
+   toolsets that are necessary for native extensions
+-  Install Desktop Development with C++ workload. It comes with the
+   default core editor, which includes basic code editing support for
+   C/C++
+-  Double-click the ``.vcxproj`` in vs folder and build the ``.sln``
+   file
+-  Run the project!
+
+Build on Linux/Mac
+~~~~~~~~~~~~~~~~~~
+
+-  Download the Python interpreter from the offcial website
+-  Download the gcc(>7.5.0)
+-  Run the command below for building
+
+.. code:: shell
+
+   python setup.py build
+
+-  Run the command below for installing
+
+.. code:: shell
+
+   python setup.py install
+
+..
+
+   NOTE: The method is also suitable for Windows if Visual Studio or
+   Visual Studio Build Tools installed.
```

#### encoding

```diff
@@ -1 +1 @@
-us-ascii
+utf-8
```

### Comparing `streamcpy-1.0/README.rst` & `streamcpy-1.0.1/PKG-INFO`

 * *Files 20% similar despite different names*

```diff
@@ -1,132 +1,145 @@
-streamcpy: The Stream Api in Python
-===================================
-
-Streamcpy can provide an approach of processing the data in a
-high-effenciency way. Like in
-`Java <https://docs.oracle.com/javase/8/docs/api/java/util/stream/Stream.html>`__,
-you can use stream-like methods (``map``, ``filter``, ``for_each`` and
-so on) to do parrallel calculation and lazy calculation, which can
-accelerating your programs. What’s more, The package is implemented in
-pure C, which means its runtime speed is even higher!
-
-Currently, the methods bellow is implemented.
-
--  ☒ filter
--  ☒ map
--  ☒ for_each
--  ☒ collect
--  ☒ distinct
--  ☒ limit
--  ☒ reduce
--  ☒ sorted
--  ☒ max/min
--  ☒ count
--  ☒ any_match/all_match
-
-Installation
-------------
-
-(Not Uploaded yet)
-
-Usage
------
-
-Like Stream Api in Java but slightly different in details
-
-.. code:: python
-
-   from streampy import *
-
-   Stream.of([1, 2, 3])
-       .map(lambda x: x * x)
-       .for_each(lambda x: print(x))
-
-This api supports various
-`Iterable <https://docs.python.org/3/library/stdtypes.html#typeiter>`__
-object in Python, like list, tuple and generator. As a result, you can
-call it in these ways:
-
-.. code:: python
-
-   from streampy import *
-
-   Stream.of((1, 2, 3))
-       .map(lambda x: x * x)
-       .for_each(lambda x: print(x))
-
-   # OR
-
-   def gen():
-       l = [1, 2, 3]
-       for i in l:
-           yield i
-
-   g = gen()
-
-   Stream.of(g)
-       .map(lambda x: x * x)
-       .for_each(lambda x: print(x))
-
-   # OR
-
-   Stream.of(open("foo.txt", 'r'))
-       .map(lambda x: x * x)
-       .for_each(lambda x: print(x))   
-
-Contribution
-------------
-
-Welcome to contribute to the project. The project is written in C. If
-you cannot understand Python’s C API, you can refer to the code in
-**python** package. It is the streamcpy implemented in python but will
-not be packed in the package. Here is the detailed description for each
-directory or file:
-
--  benchmark: a roughly comparison between Python and C++ (*Python
-   wins*)
--  build: the built file of the package (``.pyd`` for Windows and
-   ``.so`` for Linux or Mac)
--  modules: the source code for streamcpy in C
--  python: the source code for streamcpy in python and only for
-   reference
--  vs: the project files for Visual Studio
--  setup.py: the setup file for python
--  streamcpy.c: the entrance file for streamcpy package
--  streamcpy.pyi: the ``.pyi`` file for streamcpy package
-
-Build on Windows
-~~~~~~~~~~~~~~~~
-
--  Download and install the latest `Visual
-   Studio <https://visualstudio.microsoft.com/>`__
--  Install Python Development workload. The workload includes the Python
-   native development tools, which bring in the C++ workload and
-   toolsets that are necessary for native extensions
--  Install Desktop Development with C++ workload. It comes with the
-   default core editor, which includes basic code editing support for
-   C/C++
--  Double-click the ``.vcxproj`` in vs folder and build the ``.sln``
-   file
--  Run the project!
-
-Build on Linux/Mac
-~~~~~~~~~~~~~~~~~~
-
--  Download the Python interpreter from the offcial website
--  Download the gcc(>7.5.0)
--  Run the command below for building
-
-.. code:: shell
-
-   python setup.py build
-
--  Run the command below for installing
-
-.. code:: shell
-
-   python setup.py install
-
-..
-
-   NOTE: The method is also suitable for Windows if Visual Studio or
-   Visual Studio Build Tools installed.
+Metadata-Version: 2.1
+Name: streamcpy
+Version: 1.0.1
+Summary: The Stream Api in Python
+Home-page: https://github.com/littlebutt/streamcpy
+Author: littlebutt
+Author-email: luogan1996@icloud.com
+License: GPL-3.0 license
+Platform: UNKNOWN
+License-File: LICENSE
+
+streamcpy: The Stream Api in Python
+===================================
+
+Streamcpy can provide an approach of processing the data in a
+high-effenciency way. Like in
+`Java <https://docs.oracle.com/javase/8/docs/api/java/util/stream/Stream.html>`__,
+you can use stream-like methods (``map``, ``filter``, ``for_each`` and
+so on) to do parrallel calculation and lazy calculation, which can
+accelerating your programs. What’s more, The package is implemented in
+pure C, which means its runtime speed is even higher!
+
+Currently, the methods bellow is implemented.
+
+-  ☒ filter
+-  ☒ map
+-  ☒ for_each
+-  ☒ collect
+-  ☒ distinct
+-  ☒ limit
+-  ☒ reduce
+-  ☒ sorted
+-  ☒ max/min
+-  ☒ count
+-  ☒ any_match/all_match
+
+Installation
+------------
+
+(Not Uploaded yet)
+
+Usage
+-----
+
+Like Stream Api in Java but slightly different in details
+
+.. code:: python
+
+   from streampy import *
+
+   Stream.of([1, 2, 3])
+       .map(lambda x: x * x)
+       .for_each(lambda x: print(x))
+
+This api supports various
+`Iterable <https://docs.python.org/3/library/stdtypes.html#typeiter>`__
+object in Python, like list, tuple and generator. As a result, you can
+call it in these ways:
+
+.. code:: python
+
+   from streampy import *
+
+   Stream.of((1, 2, 3))
+       .map(lambda x: x * x)
+       .for_each(lambda x: print(x))
+
+   # OR
+
+   def gen():
+       l = [1, 2, 3]
+       for i in l:
+           yield i
+
+   g = gen()
+
+   Stream.of(g)
+       .map(lambda x: x * x)
+       .for_each(lambda x: print(x))
+
+   # OR
+
+   Stream.of(open("foo.txt", 'r'))
+       .map(lambda x: x * x)
+       .for_each(lambda x: print(x))   
+
+Contribution
+------------
+
+Welcome to contribute to the project. The project is written in C. If
+you cannot understand Python’s C API, you can refer to the code in
+**python** package. It is the streamcpy implemented in python but will
+not be packed in the package. Here is the detailed description for each
+directory or file:
+
+-  benchmark: a roughly comparison between Python and C++ (*Python
+   wins*)
+-  build: the built file of the package (``.pyd`` for Windows and
+   ``.so`` for Linux or Mac)
+-  modules: the source code for streamcpy in C
+-  python: the source code for streamcpy in python and only for
+   reference
+-  vs: the project files for Visual Studio
+-  setup.py: the setup file for python
+-  streamcpy.c: the entrance file for streamcpy package
+-  streamcpy.pyi: the ``.pyi`` file for streamcpy package
+
+Build on Windows
+~~~~~~~~~~~~~~~~
+
+-  Download and install the latest `Visual
+   Studio <https://visualstudio.microsoft.com/>`__
+-  Install Python Development workload. The workload includes the Python
+   native development tools, which bring in the C++ workload and
+   toolsets that are necessary for native extensions
+-  Install Desktop Development with C++ workload. It comes with the
+   default core editor, which includes basic code editing support for
+   C/C++
+-  Double-click the ``.vcxproj`` in vs folder and build the ``.sln``
+   file
+-  Run the project!
+
+Build on Linux/Mac
+~~~~~~~~~~~~~~~~~~
+
+-  Download the Python interpreter from the offcial website
+-  Download the gcc(>7.5.0)
+-  Run the command below for building
+
+.. code:: shell
+
+   python setup.py build
+
+-  Run the command below for installing
+
+.. code:: shell
+
+   python setup.py install
+
+..
+
+   NOTE: The method is also suitable for Windows if Visual Studio or
+   Visual Studio Build Tools installed.
+
+
```

### Comparing `streamcpy-1.0/streamcpy.c` & `streamcpy-1.0.1/streamcpy.c`

 * *Files identical despite different names*

