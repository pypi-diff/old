# Comparing `tmp/MazeSolvingAlgos-1.3.tar.gz` & `tmp/MazeSolvingAlgos-1.4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "D:\PyModulesByCPP\MazeSolvingAlgos\dist\.tmp-l4humbxb\MazeSolvingAlgos-1.3.tar", last modified: Thu Apr  6 14:53:15 2023, max compression
+gzip compressed data, was "D:\PyModulesByCPP\MazeSolvingAlgos\dist\.tmp-o6klm5kz\MazeSolvingAlgos-1.4.tar", last modified: Thu Apr  6 15:01:23 2023, max compression
```

## Comparing `MazeSolvingAlgos-1.3.tar` & `MazeSolvingAlgos-1.4.tar`

### file list

```diff
@@ -1,12 +1,12 @@
-drwxrwxrwx   0        0        0        0 2023-04-06 14:53:15.282138 MazeSolvingAlgos-1.3/
-drwxrwxrwx   0        0        0        0 2023-04-06 14:53:15.278142 MazeSolvingAlgos-1.3/MazeSolvingAlgos.egg-info/
--rw-rw-rw-   0        0        0     3819 2023-04-06 14:53:15.000000 MazeSolvingAlgos-1.3/MazeSolvingAlgos.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      202 2023-04-06 14:53:15.000000 MazeSolvingAlgos-1.3/MazeSolvingAlgos.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-06 14:53:15.000000 MazeSolvingAlgos-1.3/MazeSolvingAlgos.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       21 2023-04-06 14:53:15.000000 MazeSolvingAlgos-1.3/MazeSolvingAlgos.egg-info/top_level.txt
--rw-rw-rw-   0        0        0     3819 2023-04-06 14:53:15.280139 MazeSolvingAlgos-1.3/PKG-INFO
--rw-rw-rw-   0        0        0     2984 2023-04-06 14:52:52.000000 MazeSolvingAlgos-1.3/README.md
--rw-rw-rw-   0        0        0     2501 2023-04-06 14:33:55.000000 MazeSolvingAlgos-1.3/main.cpp
--rw-rw-rw-   0        0        0      940 2023-04-06 14:52:32.000000 MazeSolvingAlgos-1.3/pyproject.toml
--rw-rw-rw-   0        0        0       42 2023-04-06 14:53:15.282138 MazeSolvingAlgos-1.3/setup.cfg
--rw-rw-rw-   0        0        0      534 2023-04-06 11:57:50.000000 MazeSolvingAlgos-1.3/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-06 15:01:23.242438 MazeSolvingAlgos-1.4/
+drwxrwxrwx   0        0        0        0 2023-04-06 15:01:23.236122 MazeSolvingAlgos-1.4/MazeSolvingAlgos.egg-info/
+-rw-rw-rw-   0        0        0     3646 2023-04-06 15:01:23.000000 MazeSolvingAlgos-1.4/MazeSolvingAlgos.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      202 2023-04-06 15:01:23.000000 MazeSolvingAlgos-1.4/MazeSolvingAlgos.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-06 15:01:23.000000 MazeSolvingAlgos-1.4/MazeSolvingAlgos.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       21 2023-04-06 15:01:23.000000 MazeSolvingAlgos-1.4/MazeSolvingAlgos.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0     3646 2023-04-06 15:01:23.241435 MazeSolvingAlgos-1.4/PKG-INFO
+-rw-rw-rw-   0        0        0     2811 2023-04-06 14:58:37.000000 MazeSolvingAlgos-1.4/README.md
+-rw-rw-rw-   0        0        0     2501 2023-04-06 14:33:55.000000 MazeSolvingAlgos-1.4/main.cpp
+-rw-rw-rw-   0        0        0      940 2023-04-06 15:00:59.000000 MazeSolvingAlgos-1.4/pyproject.toml
+-rw-rw-rw-   0        0        0       42 2023-04-06 15:01:23.243441 MazeSolvingAlgos-1.4/setup.cfg
+-rw-rw-rw-   0        0        0      534 2023-04-06 11:57:50.000000 MazeSolvingAlgos-1.4/setup.py
```

### Comparing `MazeSolvingAlgos-1.3/MazeSolvingAlgos.egg-info/PKG-INFO` & `MazeSolvingAlgos-1.4/MazeSolvingAlgos.egg-info/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: MazeSolvingAlgos
-Version: 1.3
+Version: 1.4
 Summary: Python module written in C++ for generating and solving rectangular Mazes with Graph Traversal Algorithms.
 Author-email: Mahmoud Hussien Mohamed <MahmoudHussienMohamed.mhm@gmail.com>
 Project-URL: Homepage, https://github.com/MahmoudHussienMohamed/MazeSolvingAlgos
 Project-URL: repository, https://github.com/MahmoudHussienMohamed/MazeSolvingAlgos
 Project-URL: Bug Tracker, https://github.com/MahmoudHussienMohamed/MazeSolvingAlgos/issues
 Project-URL: documentation, https://github.com/MahmoudHussienMohamed/MazeSolvingAlgos/wiki/Documentation
 Classifier: Programming Language :: C++
@@ -33,18 +33,14 @@
 ## How to use
 ### RandomMazeGenerator
 Use `RandomMazeGenerator` class with arguments `H`, `W`: Height and Width of the maze respectively and call `generate()` to get **W** × **H** random maze (`H`, `W` must be unsigned integers and prefered to be even numbers).
 ``` Python
 RMG = RandomMazeGenerator(50, 50) 
 maze = RMG.generate()             # Now, maze is 50 * 50 random cells 
 ```
-50 × 50 random maze from ***TurtleInTheMaze*** project:
-
-![sample output](https://github.com/MahmoudHussienMohamed/MazeSolvingAlgos/blob/main/Imgs/rand50by50maze.png)
-
 ### Index
 Use `Index` class with arguments `row`, `col` to encapsulate a 2D cell's position and to pass `start` and `end` parameters to any ***Graph Traversal Algorithm*** (***Note that `row` and `col` must be unsigned integers***).
 
 ``` Python
 idx = Index(2, 13) 
 print(idx)             # output: "2, 13" 
 print(f"cell's column = {idx.col}, cell's row = {idx.row}")
```

### Comparing `MazeSolvingAlgos-1.3/PKG-INFO` & `MazeSolvingAlgos-1.4/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: MazeSolvingAlgos
-Version: 1.3
+Version: 1.4
 Summary: Python module written in C++ for generating and solving rectangular Mazes with Graph Traversal Algorithms.
 Author-email: Mahmoud Hussien Mohamed <MahmoudHussienMohamed.mhm@gmail.com>
 Project-URL: Homepage, https://github.com/MahmoudHussienMohamed/MazeSolvingAlgos
 Project-URL: repository, https://github.com/MahmoudHussienMohamed/MazeSolvingAlgos
 Project-URL: Bug Tracker, https://github.com/MahmoudHussienMohamed/MazeSolvingAlgos/issues
 Project-URL: documentation, https://github.com/MahmoudHussienMohamed/MazeSolvingAlgos/wiki/Documentation
 Classifier: Programming Language :: C++
@@ -33,18 +33,14 @@
 ## How to use
 ### RandomMazeGenerator
 Use `RandomMazeGenerator` class with arguments `H`, `W`: Height and Width of the maze respectively and call `generate()` to get **W** × **H** random maze (`H`, `W` must be unsigned integers and prefered to be even numbers).
 ``` Python
 RMG = RandomMazeGenerator(50, 50) 
 maze = RMG.generate()             # Now, maze is 50 * 50 random cells 
 ```
-50 × 50 random maze from ***TurtleInTheMaze*** project:
-
-![sample output](https://github.com/MahmoudHussienMohamed/MazeSolvingAlgos/blob/main/Imgs/rand50by50maze.png)
-
 ### Index
 Use `Index` class with arguments `row`, `col` to encapsulate a 2D cell's position and to pass `start` and `end` parameters to any ***Graph Traversal Algorithm*** (***Note that `row` and `col` must be unsigned integers***).
 
 ``` Python
 idx = Index(2, 13) 
 print(idx)             # output: "2, 13" 
 print(f"cell's column = {idx.col}, cell's row = {idx.row}")
```

### Comparing `MazeSolvingAlgos-1.3/README.md` & `MazeSolvingAlgos-1.4/README.md`

 * *Files 4% similar despite different names*

```diff
@@ -19,18 +19,14 @@
 ## How to use
 ### RandomMazeGenerator
 Use `RandomMazeGenerator` class with arguments `H`, `W`: Height and Width of the maze respectively and call `generate()` to get **W** × **H** random maze (`H`, `W` must be unsigned integers and prefered to be even numbers).
 ``` Python
 RMG = RandomMazeGenerator(50, 50) 
 maze = RMG.generate()             # Now, maze is 50 * 50 random cells 
 ```
-50 × 50 random maze from ***TurtleInTheMaze*** project:
-
-![sample output](https://github.com/MahmoudHussienMohamed/MazeSolvingAlgos/blob/main/Imgs/rand50by50maze.png)
-
 ### Index
 Use `Index` class with arguments `row`, `col` to encapsulate a 2D cell's position and to pass `start` and `end` parameters to any ***Graph Traversal Algorithm*** (***Note that `row` and `col` must be unsigned integers***).
 
 ``` Python
 idx = Index(2, 13) 
 print(idx)             # output: "2, 13" 
 print(f"cell's column = {idx.col}, cell's row = {idx.row}")
```

### Comparing `MazeSolvingAlgos-1.3/main.cpp` & `MazeSolvingAlgos-1.4/main.cpp`

 * *Files identical despite different names*

### Comparing `MazeSolvingAlgos-1.3/pyproject.toml` & `MazeSolvingAlgos-1.4/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 [build-system]
 requires = ["setuptools>=61.0", "wheel", "pybind11"]
 build-backend = "setuptools.build_meta"
 [project]
 name = "MazeSolvingAlgos"
-version = "1.3"
+version = "1.4"
 authors = [
   { name="Mahmoud Hussien Mohamed", email="MahmoudHussienMohamed.mhm@gmail.com" },
 ]
 description = "Python module written in C++ for generating and solving rectangular Mazes with Graph Traversal Algorithms."
 readme = "README.md"
 classifiers = [
     "Programming Language :: C++",
```

### Comparing `MazeSolvingAlgos-1.3/setup.py` & `MazeSolvingAlgos-1.4/setup.py`

 * *Files identical despite different names*

