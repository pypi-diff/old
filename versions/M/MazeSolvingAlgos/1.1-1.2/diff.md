# Comparing `tmp/MazeSolvingAlgos-1.1.tar.gz` & `tmp/MazeSolvingAlgos-1.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "D:\PyModulesByCPP\MazeSolvingAlgos\dist\.tmp-zmqoc_em\MazeSolvingAlgos-1.1.tar", last modified: Thu Apr  6 14:39:31 2023, max compression
+gzip compressed data, was "D:\PyModulesByCPP\MazeSolvingAlgos\dist\.tmp-1i5b9u7d\MazeSolvingAlgos-1.2.tar", last modified: Thu Apr  6 14:50:13 2023, max compression
```

## Comparing `MazeSolvingAlgos-1.1.tar` & `MazeSolvingAlgos-1.2.tar`

### file list

```diff
@@ -1,12 +1,12 @@
-drwxrwxrwx   0        0        0        0 2023-04-06 14:39:31.768459 MazeSolvingAlgos-1.1/
-drwxrwxrwx   0        0        0        0 2023-04-06 14:39:31.766461 MazeSolvingAlgos-1.1/MazeSolvingAlgos.egg-info/
--rw-rw-rw-   0        0        0     3475 2023-04-06 14:39:31.000000 MazeSolvingAlgos-1.1/MazeSolvingAlgos.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      202 2023-04-06 14:39:31.000000 MazeSolvingAlgos-1.1/MazeSolvingAlgos.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-06 14:39:31.000000 MazeSolvingAlgos-1.1/MazeSolvingAlgos.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       21 2023-04-06 14:39:31.000000 MazeSolvingAlgos-1.1/MazeSolvingAlgos.egg-info/top_level.txt
--rw-rw-rw-   0        0        0     3475 2023-04-06 14:39:31.768459 MazeSolvingAlgos-1.1/PKG-INFO
--rw-rw-rw-   0        0        0     2640 2023-04-06 11:13:56.000000 MazeSolvingAlgos-1.1/README.md
--rw-rw-rw-   0        0        0     2501 2023-04-06 14:33:55.000000 MazeSolvingAlgos-1.1/main.cpp
--rw-rw-rw-   0        0        0      940 2023-04-06 14:39:14.000000 MazeSolvingAlgos-1.1/pyproject.toml
--rw-rw-rw-   0        0        0       42 2023-04-06 14:39:31.769459 MazeSolvingAlgos-1.1/setup.cfg
--rw-rw-rw-   0        0        0      534 2023-04-06 11:57:50.000000 MazeSolvingAlgos-1.1/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-06 14:50:13.005233 MazeSolvingAlgos-1.2/
+drwxrwxrwx   0        0        0        0 2023-04-06 14:50:12.980250 MazeSolvingAlgos-1.2/MazeSolvingAlgos.egg-info/
+-rw-rw-rw-   0        0        0     3751 2023-04-06 14:50:12.000000 MazeSolvingAlgos-1.2/MazeSolvingAlgos.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      202 2023-04-06 14:50:12.000000 MazeSolvingAlgos-1.2/MazeSolvingAlgos.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-06 14:50:12.000000 MazeSolvingAlgos-1.2/MazeSolvingAlgos.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       21 2023-04-06 14:50:12.000000 MazeSolvingAlgos-1.2/MazeSolvingAlgos.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0     3751 2023-04-06 14:50:12.982247 MazeSolvingAlgos-1.2/PKG-INFO
+-rw-rw-rw-   0        0        0     2916 2023-04-06 14:50:04.000000 MazeSolvingAlgos-1.2/README.md
+-rw-rw-rw-   0        0        0     2501 2023-04-06 14:33:55.000000 MazeSolvingAlgos-1.2/main.cpp
+-rw-rw-rw-   0        0        0      940 2023-04-06 14:48:46.000000 MazeSolvingAlgos-1.2/pyproject.toml
+-rw-rw-rw-   0        0        0       42 2023-04-06 14:50:13.006233 MazeSolvingAlgos-1.2/setup.cfg
+-rw-rw-rw-   0        0        0      534 2023-04-06 11:57:50.000000 MazeSolvingAlgos-1.2/setup.py
```

### Comparing `MazeSolvingAlgos-1.1/MazeSolvingAlgos.egg-info/PKG-INFO` & `MazeSolvingAlgos-1.2/MazeSolvingAlgos.egg-info/PKG-INFO`

 * *Files 9% similar despite different names*

```diff
@@ -1,44 +1,51 @@
 Metadata-Version: 2.1
 Name: MazeSolvingAlgos
-Version: 1.1
+Version: 1.2
 Summary: Python module written in C++ for generating and solving rectangular Mazes with Graph Traversal Algorithms.
 Author-email: Mahmoud Hussien Mohamed <MahmoudHussienMohamed.mhm@gmail.com>
 Project-URL: Homepage, https://github.com/MahmoudHussienMohamed/MazeSolvingAlgos
 Project-URL: repository, https://github.com/MahmoudHussienMohamed/MazeSolvingAlgos
 Project-URL: Bug Tracker, https://github.com/MahmoudHussienMohamed/MazeSolvingAlgos/issues
 Project-URL: documentation, https://github.com/MahmoudHussienMohamed/MazeSolvingAlgos/wiki/Documentation
 Classifier: Programming Language :: C++
 Classifier: License :: OSI Approved :: GNU General Public License v3 (GPLv3)
 Classifier: Operating System :: Microsoft :: Windows
 Description-Content-Type: text/markdown
 
-# MazeSolvingAlgos Documentation
-***MazeSolvingAlgos*** is a Python module written in C++ for generating and solving rectangular Mazes with **Graph Traversal Algorithms**. This Module is a part of **TurtleInTheMaze** Project so it's especially created for ***2D grids***.
+# MazeSolvingAlgos
+***MazeSolvingAlgos*** is a Python module written in C++ for generating and solving rectangular Mazes with **Graph Traversal Algorithms**. This Module is a part of **TurtleInTheMaze** Project so it's especially created for ***2D grids***. *You can see **full documentation [here](https://github.com/MahmoudHussienMohamed/MazeSolvingAlgos/wiki/Documentation)***.
 ## Content of module
 * Helper Classes
     * Index 
     * RandomMazeGenerator 
 * Solving Algorithms Classes
     - DepthFirstSearch
     - BreadthFirstSearch
     - DijkstraAlgorithm
     - AStar
     - BellmanFord
     - FloydWarshall
 
+## How to install
+Simply with pip:
+
+`pip install MazeSolvingAlgos`
 ## How to use
 ### RandomMazeGenerator
-Use `RandomMazeGenerator` class with arguments `H`, `W`: Height and Width of the maze respectively and call `generate()` to get **W** � **H** random maze (`H`, `W` must be unsigned integers and prefered to be even numbers).
+Use `RandomMazeGenerator` class with arguments `H`, `W`: Height and Width of the maze respectively and call `generate()` to get **W** × **H** random maze (`H`, `W` must be unsigned integers and prefered to be even numbers).
 ``` Python
 RMG = RandomMazeGenerator(50, 50) 
 maze = RMG.generate()             # Now, maze is 50 * 50 random cells 
 ```
+50 × 50 random maze from ***TurtleInTheMaze*** project:
+
+![sample output](Imgs/rand50by50maze.png)
 
-### 2.2 - Index
+### Index
 Use `Index` class with arguments `row`, `col` to encapsulate a 2D cell's position and to pass `start` and `end` parameters to any ***Graph Traversal Algorithm*** (***Note that `row` and `col` must be unsigned integers***).
 
 ``` Python
 idx = Index(2, 13) 
 print(idx)             # output: "2, 13" 
 print(f"cell's column = {idx.col}, cell's row = {idx.row}")             
 # output: "cell's column = 13, cell's row = 2"
```

### Comparing `MazeSolvingAlgos-1.1/PKG-INFO` & `MazeSolvingAlgos-1.2/PKG-INFO`

 * *Files 9% similar despite different names*

```diff
@@ -1,44 +1,51 @@
 Metadata-Version: 2.1
 Name: MazeSolvingAlgos
-Version: 1.1
+Version: 1.2
 Summary: Python module written in C++ for generating and solving rectangular Mazes with Graph Traversal Algorithms.
 Author-email: Mahmoud Hussien Mohamed <MahmoudHussienMohamed.mhm@gmail.com>
 Project-URL: Homepage, https://github.com/MahmoudHussienMohamed/MazeSolvingAlgos
 Project-URL: repository, https://github.com/MahmoudHussienMohamed/MazeSolvingAlgos
 Project-URL: Bug Tracker, https://github.com/MahmoudHussienMohamed/MazeSolvingAlgos/issues
 Project-URL: documentation, https://github.com/MahmoudHussienMohamed/MazeSolvingAlgos/wiki/Documentation
 Classifier: Programming Language :: C++
 Classifier: License :: OSI Approved :: GNU General Public License v3 (GPLv3)
 Classifier: Operating System :: Microsoft :: Windows
 Description-Content-Type: text/markdown
 
-# MazeSolvingAlgos Documentation
-***MazeSolvingAlgos*** is a Python module written in C++ for generating and solving rectangular Mazes with **Graph Traversal Algorithms**. This Module is a part of **TurtleInTheMaze** Project so it's especially created for ***2D grids***.
+# MazeSolvingAlgos
+***MazeSolvingAlgos*** is a Python module written in C++ for generating and solving rectangular Mazes with **Graph Traversal Algorithms**. This Module is a part of **TurtleInTheMaze** Project so it's especially created for ***2D grids***. *You can see **full documentation [here](https://github.com/MahmoudHussienMohamed/MazeSolvingAlgos/wiki/Documentation)***.
 ## Content of module
 * Helper Classes
     * Index 
     * RandomMazeGenerator 
 * Solving Algorithms Classes
     - DepthFirstSearch
     - BreadthFirstSearch
     - DijkstraAlgorithm
     - AStar
     - BellmanFord
     - FloydWarshall
 
+## How to install
+Simply with pip:
+
+`pip install MazeSolvingAlgos`
 ## How to use
 ### RandomMazeGenerator
-Use `RandomMazeGenerator` class with arguments `H`, `W`: Height and Width of the maze respectively and call `generate()` to get **W** � **H** random maze (`H`, `W` must be unsigned integers and prefered to be even numbers).
+Use `RandomMazeGenerator` class with arguments `H`, `W`: Height and Width of the maze respectively and call `generate()` to get **W** × **H** random maze (`H`, `W` must be unsigned integers and prefered to be even numbers).
 ``` Python
 RMG = RandomMazeGenerator(50, 50) 
 maze = RMG.generate()             # Now, maze is 50 * 50 random cells 
 ```
+50 × 50 random maze from ***TurtleInTheMaze*** project:
+
+![sample output](Imgs/rand50by50maze.png)
 
-### 2.2 - Index
+### Index
 Use `Index` class with arguments `row`, `col` to encapsulate a 2D cell's position and to pass `start` and `end` parameters to any ***Graph Traversal Algorithm*** (***Note that `row` and `col` must be unsigned integers***).
 
 ``` Python
 idx = Index(2, 13) 
 print(idx)             # output: "2, 13" 
 print(f"cell's column = {idx.col}, cell's row = {idx.row}")             
 # output: "cell's column = 13, cell's row = 2"
```

### Comparing `MazeSolvingAlgos-1.1/README.md` & `MazeSolvingAlgos-1.2/README.md`

 * *Files 10% similar despite different names*

```diff
@@ -1,30 +1,37 @@
-# MazeSolvingAlgos Documentation
-***MazeSolvingAlgos*** is a Python module written in C++ for generating and solving rectangular Mazes with **Graph Traversal Algorithms**. This Module is a part of **TurtleInTheMaze** Project so it's especially created for ***2D grids***.
+# MazeSolvingAlgos
+***MazeSolvingAlgos*** is a Python module written in C++ for generating and solving rectangular Mazes with **Graph Traversal Algorithms**. This Module is a part of **TurtleInTheMaze** Project so it's especially created for ***2D grids***. *You can see **full documentation [here](https://github.com/MahmoudHussienMohamed/MazeSolvingAlgos/wiki/Documentation)***.
 ## Content of module
 * Helper Classes
     * Index 
     * RandomMazeGenerator 
 * Solving Algorithms Classes
     - DepthFirstSearch
     - BreadthFirstSearch
     - DijkstraAlgorithm
     - AStar
     - BellmanFord
     - FloydWarshall
 
+## How to install
+Simply with pip:
+
+`pip install MazeSolvingAlgos`
 ## How to use
 ### RandomMazeGenerator
-Use `RandomMazeGenerator` class with arguments `H`, `W`: Height and Width of the maze respectively and call `generate()` to get **W** � **H** random maze (`H`, `W` must be unsigned integers and prefered to be even numbers).
+Use `RandomMazeGenerator` class with arguments `H`, `W`: Height and Width of the maze respectively and call `generate()` to get **W** × **H** random maze (`H`, `W` must be unsigned integers and prefered to be even numbers).
 ``` Python
 RMG = RandomMazeGenerator(50, 50) 
 maze = RMG.generate()             # Now, maze is 50 * 50 random cells 
 ```
+50 × 50 random maze from ***TurtleInTheMaze*** project:
+
+![sample output](Imgs/rand50by50maze.png)
 
-### 2.2 - Index
+### Index
 Use `Index` class with arguments `row`, `col` to encapsulate a 2D cell's position and to pass `start` and `end` parameters to any ***Graph Traversal Algorithm*** (***Note that `row` and `col` must be unsigned integers***).
 
 ``` Python
 idx = Index(2, 13) 
 print(idx)             # output: "2, 13" 
 print(f"cell's column = {idx.col}, cell's row = {idx.row}")             
 # output: "cell's column = 13, cell's row = 2"
```

### Comparing `MazeSolvingAlgos-1.1/main.cpp` & `MazeSolvingAlgos-1.2/main.cpp`

 * *Files identical despite different names*

### Comparing `MazeSolvingAlgos-1.1/pyproject.toml` & `MazeSolvingAlgos-1.2/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 [build-system]
 requires = ["setuptools>=61.0", "wheel", "pybind11"]
 build-backend = "setuptools.build_meta"
 [project]
 name = "MazeSolvingAlgos"
-version = "1.1"
+version = "1.2"
 authors = [
   { name="Mahmoud Hussien Mohamed", email="MahmoudHussienMohamed.mhm@gmail.com" },
 ]
 description = "Python module written in C++ for generating and solving rectangular Mazes with Graph Traversal Algorithms."
 readme = "README.md"
 classifiers = [
     "Programming Language :: C++",
```

### Comparing `MazeSolvingAlgos-1.1/setup.py` & `MazeSolvingAlgos-1.2/setup.py`

 * *Files identical despite different names*

