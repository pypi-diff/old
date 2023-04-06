# Comparing `tmp/MazeSolvingAlgos-1.0.tar.gz` & `tmp/MazeSolvingAlgos-1.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "D:\PyModulesByCPP\MazeSolvingAlgos\dist\.tmp-zqu5pk69\MazeSolvingAlgos-1.0.tar", last modified: Thu Apr  6 12:14:45 2023, max compression
+gzip compressed data, was "D:\PyModulesByCPP\MazeSolvingAlgos\dist\.tmp-zmqoc_em\MazeSolvingAlgos-1.1.tar", last modified: Thu Apr  6 14:39:31 2023, max compression
```

## Comparing `MazeSolvingAlgos-1.0.tar` & `MazeSolvingAlgos-1.1.tar`

### file list

```diff
@@ -1,12 +1,12 @@
-drwxrwxrwx   0        0        0        0 2023-04-06 12:14:45.387833 MazeSolvingAlgos-1.0/
-drwxrwxrwx   0        0        0        0 2023-04-06 12:14:45.383837 MazeSolvingAlgos-1.0/MazeSolvingAlgos.egg-info/
--rw-rw-rw-   0        0        0     3475 2023-04-06 12:14:45.000000 MazeSolvingAlgos-1.0/MazeSolvingAlgos.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      202 2023-04-06 12:14:45.000000 MazeSolvingAlgos-1.0/MazeSolvingAlgos.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-06 12:14:45.000000 MazeSolvingAlgos-1.0/MazeSolvingAlgos.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       21 2023-04-06 12:14:45.000000 MazeSolvingAlgos-1.0/MazeSolvingAlgos.egg-info/top_level.txt
--rw-rw-rw-   0        0        0     3475 2023-04-06 12:14:45.386834 MazeSolvingAlgos-1.0/PKG-INFO
--rw-rw-rw-   0        0        0     2640 2023-04-06 11:13:56.000000 MazeSolvingAlgos-1.0/README.md
--rw-rw-rw-   0        0        0     2179 2023-04-06 12:14:05.000000 MazeSolvingAlgos-1.0/main.cpp
--rw-rw-rw-   0        0        0      940 2023-04-06 11:46:27.000000 MazeSolvingAlgos-1.0/pyproject.toml
--rw-rw-rw-   0        0        0       42 2023-04-06 12:14:45.387833 MazeSolvingAlgos-1.0/setup.cfg
--rw-rw-rw-   0        0        0      534 2023-04-06 11:57:50.000000 MazeSolvingAlgos-1.0/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-06 14:39:31.768459 MazeSolvingAlgos-1.1/
+drwxrwxrwx   0        0        0        0 2023-04-06 14:39:31.766461 MazeSolvingAlgos-1.1/MazeSolvingAlgos.egg-info/
+-rw-rw-rw-   0        0        0     3475 2023-04-06 14:39:31.000000 MazeSolvingAlgos-1.1/MazeSolvingAlgos.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      202 2023-04-06 14:39:31.000000 MazeSolvingAlgos-1.1/MazeSolvingAlgos.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-06 14:39:31.000000 MazeSolvingAlgos-1.1/MazeSolvingAlgos.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       21 2023-04-06 14:39:31.000000 MazeSolvingAlgos-1.1/MazeSolvingAlgos.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0     3475 2023-04-06 14:39:31.768459 MazeSolvingAlgos-1.1/PKG-INFO
+-rw-rw-rw-   0        0        0     2640 2023-04-06 11:13:56.000000 MazeSolvingAlgos-1.1/README.md
+-rw-rw-rw-   0        0        0     2501 2023-04-06 14:33:55.000000 MazeSolvingAlgos-1.1/main.cpp
+-rw-rw-rw-   0        0        0      940 2023-04-06 14:39:14.000000 MazeSolvingAlgos-1.1/pyproject.toml
+-rw-rw-rw-   0        0        0       42 2023-04-06 14:39:31.769459 MazeSolvingAlgos-1.1/setup.cfg
+-rw-rw-rw-   0        0        0      534 2023-04-06 11:57:50.000000 MazeSolvingAlgos-1.1/setup.py
```

### Comparing `MazeSolvingAlgos-1.0/MazeSolvingAlgos.egg-info/PKG-INFO` & `MazeSolvingAlgos-1.1/MazeSolvingAlgos.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: MazeSolvingAlgos
-Version: 1.0
+Version: 1.1
 Summary: Python module written in C++ for generating and solving rectangular Mazes with Graph Traversal Algorithms.
 Author-email: Mahmoud Hussien Mohamed <MahmoudHussienMohamed.mhm@gmail.com>
 Project-URL: Homepage, https://github.com/MahmoudHussienMohamed/MazeSolvingAlgos
 Project-URL: repository, https://github.com/MahmoudHussienMohamed/MazeSolvingAlgos
 Project-URL: Bug Tracker, https://github.com/MahmoudHussienMohamed/MazeSolvingAlgos/issues
 Project-URL: documentation, https://github.com/MahmoudHussienMohamed/MazeSolvingAlgos/wiki/Documentation
 Classifier: Programming Language :: C++
```

### Comparing `MazeSolvingAlgos-1.0/PKG-INFO` & `MazeSolvingAlgos-1.1/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: MazeSolvingAlgos
-Version: 1.0
+Version: 1.1
 Summary: Python module written in C++ for generating and solving rectangular Mazes with Graph Traversal Algorithms.
 Author-email: Mahmoud Hussien Mohamed <MahmoudHussienMohamed.mhm@gmail.com>
 Project-URL: Homepage, https://github.com/MahmoudHussienMohamed/MazeSolvingAlgos
 Project-URL: repository, https://github.com/MahmoudHussienMohamed/MazeSolvingAlgos
 Project-URL: Bug Tracker, https://github.com/MahmoudHussienMohamed/MazeSolvingAlgos/issues
 Project-URL: documentation, https://github.com/MahmoudHussienMohamed/MazeSolvingAlgos/wiki/Documentation
 Classifier: Programming Language :: C++
```

### Comparing `MazeSolvingAlgos-1.0/README.md` & `MazeSolvingAlgos-1.1/README.md`

 * *Files identical despite different names*

### Comparing `MazeSolvingAlgos-1.0/main.cpp` & `MazeSolvingAlgos-1.1/main.cpp`

 * *Files 18% similar despite different names*

```diff
@@ -1,9 +1,13 @@
 #include "C:/Users/mahmo/AppData/Roaming/Python/Python39/site-packages/pybind11/include/pybind11/pybind11.h"
 #include "C:/Users/mahmo/AppData/Roaming/Python/Python39/site-packages/pybind11/include/pybind11/detail/common.h"
+#include "C:/Users/mahmo/AppData/Roaming/Python/Python39/site-packages/pybind11/include/pybind11/stl.h"
+#include "C:/Users/mahmo/AppData/Roaming/Python/Python39/site-packages/pybind11/include/pybind11/cast.h"
+#include "C:/Users/mahmo/AppData/Roaming/Python/Python39/site-packages/pybind11/include/pybind11/complex.h"
+
 
 
 #include "D:/PyModulesByCPP/MazeSolvingAlgos/GraphTraversalAlgorithms.h"
 #include "D:/PyModulesByCPP/MazeSolvingAlgos/MazeGenerator.h"
 //#include "Graph.h"
 namespace py = pybind11;
 #define AddGTAclass(GTA /*GraphTraversalAlgorithm*/){               \
```

### Comparing `MazeSolvingAlgos-1.0/pyproject.toml` & `MazeSolvingAlgos-1.1/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 [build-system]
 requires = ["setuptools>=61.0", "wheel", "pybind11"]
 build-backend = "setuptools.build_meta"
 [project]
 name = "MazeSolvingAlgos"
-version = "1.0"
+version = "1.1"
 authors = [
   { name="Mahmoud Hussien Mohamed", email="MahmoudHussienMohamed.mhm@gmail.com" },
 ]
 description = "Python module written in C++ for generating and solving rectangular Mazes with Graph Traversal Algorithms."
 readme = "README.md"
 classifiers = [
     "Programming Language :: C++",
```

### Comparing `MazeSolvingAlgos-1.0/setup.py` & `MazeSolvingAlgos-1.1/setup.py`

 * *Files identical despite different names*

