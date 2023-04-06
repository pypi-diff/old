# Comparing `tmp/DA4RDM_Vis_ProcessBased-0.1.0.tar.gz` & `tmp/DA4RDM_Vis_ProcessBased-0.1.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "DA4RDM_Vis_ProcessBased-0.1.0.tar", last modified: Thu Apr  6 15:53:17 2023, max compression
+gzip compressed data, was "DA4RDM_Vis_ProcessBased-0.1.1.tar", last modified: Thu Apr  6 16:02:36 2023, max compression
```

## Comparing `DA4RDM_Vis_ProcessBased-0.1.0.tar` & `DA4RDM_Vis_ProcessBased-0.1.1.tar`

### file list

```diff
@@ -1,26 +1,26 @@
-drwxrwxrwx   0        0        0        0 2023-04-06 15:53:17.733274 DA4RDM_Vis_ProcessBased-0.1.0/
-drwxrwxrwx   0        0        0        0 2023-04-06 15:53:17.612907 DA4RDM_Vis_ProcessBased-0.1.0/DA4RDM_Vis_ProcessBased.egg-info/
--rw-rw-rw-   0        0        0     3454 2023-04-06 15:53:17.000000 DA4RDM_Vis_ProcessBased-0.1.0/DA4RDM_Vis_ProcessBased.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      722 2023-04-06 15:53:17.000000 DA4RDM_Vis_ProcessBased-0.1.0/DA4RDM_Vis_ProcessBased.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-06 15:53:17.000000 DA4RDM_Vis_ProcessBased-0.1.0/DA4RDM_Vis_ProcessBased.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       24 2023-04-06 15:53:17.000000 DA4RDM_Vis_ProcessBased-0.1.0/DA4RDM_Vis_ProcessBased.egg-info/top_level.txt
--rw-rw-rw-   0        0        0     1072 2023-04-05 06:47:24.000000 DA4RDM_Vis_ProcessBased-0.1.0/LICENSE
--rw-rw-rw-   0        0        0       51 2023-04-05 15:44:42.000000 DA4RDM_Vis_ProcessBased-0.1.0/MANIFEST.in
--rw-rw-rw-   0        0        0     3454 2023-04-06 15:53:17.734276 DA4RDM_Vis_ProcessBased-0.1.0/PKG-INFO
--rw-rw-rw-   0        0        0     2983 2023-04-06 15:43:07.000000 DA4RDM_Vis_ProcessBased-0.1.0/README.md
--rw-rw-rw-   0        0        0      483 2023-04-06 15:52:53.000000 DA4RDM_Vis_ProcessBased-0.1.0/pyproject.toml
--rw-rw-rw-   0        0        0      303 2023-04-06 15:53:17.739315 DA4RDM_Vis_ProcessBased-0.1.0/setup.cfg
--rw-rw-rw-   0        0        0     1040 2023-04-06 15:50:04.000000 DA4RDM_Vis_ProcessBased-0.1.0/setup.py
-drwxrwxrwx   0        0        0        0 2023-04-06 15:53:17.566431 DA4RDM_Vis_ProcessBased-0.1.0/src/
-drwxrwxrwx   0        0        0        0 2023-04-06 15:53:17.656600 DA4RDM_Vis_ProcessBased-0.1.0/src/DA4RDM_Vis_ProcessBased/
--rw-rw-rw-   0        0        0     1764 2023-04-05 16:15:18.000000 DA4RDM_Vis_ProcessBased-0.1.0/src/DA4RDM_Vis_ProcessBased/Evaluate_Fitness.py
--rw-rw-rw-   0        0        0     1351 2023-04-05 06:14:11.000000 DA4RDM_Vis_ProcessBased-0.1.0/src/DA4RDM_Vis_ProcessBased/Extract.py
-drwxrwxrwx   0        0        0        0 2023-04-06 15:53:17.731273 DA4RDM_Vis_ProcessBased-0.1.0/src/DA4RDM_Vis_ProcessBased/PhaseData/
--rw-rw-rw-   0        0        0      581 2023-04-05 06:12:12.000000 DA4RDM_Vis_ProcessBased-0.1.0/src/DA4RDM_Vis_ProcessBased/PhaseData/Access.csv
--rw-rw-rw-   0        0        0      503 2023-04-05 06:12:12.000000 DA4RDM_Vis_ProcessBased-0.1.0/src/DA4RDM_Vis_ProcessBased/PhaseData/Analysis.csv
--rw-rw-rw-   0        0        0      619 2023-04-05 06:12:12.000000 DA4RDM_Vis_ProcessBased-0.1.0/src/DA4RDM_Vis_ProcessBased/PhaseData/Archival.csv
--rw-rw-rw-   0        0        0      929 2023-04-05 06:12:12.000000 DA4RDM_Vis_ProcessBased-0.1.0/src/DA4RDM_Vis_ProcessBased/PhaseData/Planning.csv
--rw-rw-rw-   0        0        0     1001 2023-04-05 06:12:12.000000 DA4RDM_Vis_ProcessBased-0.1.0/src/DA4RDM_Vis_ProcessBased/PhaseData/Production.csv
--rw-rw-rw-   0        0        0      687 2023-04-05 06:12:12.000000 DA4RDM_Vis_ProcessBased-0.1.0/src/DA4RDM_Vis_ProcessBased/PhaseData/Reuse.csv
--rw-rw-rw-   0        0        0     3586 2023-04-05 16:43:35.000000 DA4RDM_Vis_ProcessBased-0.1.0/src/DA4RDM_Vis_ProcessBased/Visualize.py
--rw-rw-rw-   0        0        0        0 2023-04-05 06:50:44.000000 DA4RDM_Vis_ProcessBased-0.1.0/src/DA4RDM_Vis_ProcessBased/__init__.py
+drwxrwxrwx   0        0        0        0 2023-04-06 16:02:36.424952 DA4RDM_Vis_ProcessBased-0.1.1/
+drwxrwxrwx   0        0        0        0 2023-04-06 16:02:36.402390 DA4RDM_Vis_ProcessBased-0.1.1/DA4RDM_Vis_ProcessBased.egg-info/
+-rw-rw-rw-   0        0        0     3503 2023-04-06 16:02:36.000000 DA4RDM_Vis_ProcessBased-0.1.1/DA4RDM_Vis_ProcessBased.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      722 2023-04-06 16:02:36.000000 DA4RDM_Vis_ProcessBased-0.1.1/DA4RDM_Vis_ProcessBased.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-06 16:02:36.000000 DA4RDM_Vis_ProcessBased-0.1.1/DA4RDM_Vis_ProcessBased.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       24 2023-04-06 16:02:36.000000 DA4RDM_Vis_ProcessBased-0.1.1/DA4RDM_Vis_ProcessBased.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0     1072 2023-04-05 06:47:24.000000 DA4RDM_Vis_ProcessBased-0.1.1/LICENSE
+-rw-rw-rw-   0        0        0       51 2023-04-05 15:44:42.000000 DA4RDM_Vis_ProcessBased-0.1.1/MANIFEST.in
+-rw-rw-rw-   0        0        0     3503 2023-04-06 16:02:36.425952 DA4RDM_Vis_ProcessBased-0.1.1/PKG-INFO
+-rw-rw-rw-   0        0        0     3031 2023-04-06 16:01:43.000000 DA4RDM_Vis_ProcessBased-0.1.1/README.md
+-rw-rw-rw-   0        0        0      483 2023-04-06 16:02:00.000000 DA4RDM_Vis_ProcessBased-0.1.1/pyproject.toml
+-rw-rw-rw-   0        0        0      303 2023-04-06 16:02:36.431952 DA4RDM_Vis_ProcessBased-0.1.1/setup.cfg
+-rw-rw-rw-   0        0        0     1040 2023-04-06 16:02:15.000000 DA4RDM_Vis_ProcessBased-0.1.1/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-06 16:02:36.368360 DA4RDM_Vis_ProcessBased-0.1.1/src/
+drwxrwxrwx   0        0        0        0 2023-04-06 16:02:36.411937 DA4RDM_Vis_ProcessBased-0.1.1/src/DA4RDM_Vis_ProcessBased/
+-rw-rw-rw-   0        0        0     1764 2023-04-05 16:15:18.000000 DA4RDM_Vis_ProcessBased-0.1.1/src/DA4RDM_Vis_ProcessBased/Evaluate_Fitness.py
+-rw-rw-rw-   0        0        0     1351 2023-04-05 06:14:11.000000 DA4RDM_Vis_ProcessBased-0.1.1/src/DA4RDM_Vis_ProcessBased/Extract.py
+drwxrwxrwx   0        0        0        0 2023-04-06 16:02:36.422959 DA4RDM_Vis_ProcessBased-0.1.1/src/DA4RDM_Vis_ProcessBased/PhaseData/
+-rw-rw-rw-   0        0        0      581 2023-04-05 06:12:12.000000 DA4RDM_Vis_ProcessBased-0.1.1/src/DA4RDM_Vis_ProcessBased/PhaseData/Access.csv
+-rw-rw-rw-   0        0        0      503 2023-04-05 06:12:12.000000 DA4RDM_Vis_ProcessBased-0.1.1/src/DA4RDM_Vis_ProcessBased/PhaseData/Analysis.csv
+-rw-rw-rw-   0        0        0      619 2023-04-05 06:12:12.000000 DA4RDM_Vis_ProcessBased-0.1.1/src/DA4RDM_Vis_ProcessBased/PhaseData/Archival.csv
+-rw-rw-rw-   0        0        0      929 2023-04-05 06:12:12.000000 DA4RDM_Vis_ProcessBased-0.1.1/src/DA4RDM_Vis_ProcessBased/PhaseData/Planning.csv
+-rw-rw-rw-   0        0        0     1001 2023-04-05 06:12:12.000000 DA4RDM_Vis_ProcessBased-0.1.1/src/DA4RDM_Vis_ProcessBased/PhaseData/Production.csv
+-rw-rw-rw-   0        0        0      687 2023-04-05 06:12:12.000000 DA4RDM_Vis_ProcessBased-0.1.1/src/DA4RDM_Vis_ProcessBased/PhaseData/Reuse.csv
+-rw-rw-rw-   0        0        0     3586 2023-04-05 16:43:35.000000 DA4RDM_Vis_ProcessBased-0.1.1/src/DA4RDM_Vis_ProcessBased/Visualize.py
+-rw-rw-rw-   0        0        0        0 2023-04-05 06:50:44.000000 DA4RDM_Vis_ProcessBased-0.1.1/src/DA4RDM_Vis_ProcessBased/__init__.py
```

### Comparing `DA4RDM_Vis_ProcessBased-0.1.0/DA4RDM_Vis_ProcessBased.egg-info/PKG-INFO` & `DA4RDM_Vis_ProcessBased-0.1.1/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
-Name: DA4RDM-Vis-ProcessBased
-Version: 0.1.0
+Name: DA4RDM_Vis_ProcessBased
+Version: 0.1.1
 Summary: Package to get visualisation of fitness values evaluated for a given projectid analyzed on different RDLC phase process models
 Classifier: Programming Language :: Python :: 3.9
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
 Description-Content-Type: text/markdown
 License-File: LICENSE
 
@@ -15,15 +15,16 @@
 
 
 ## Installation
 The package is built using Python as a programming language and utilizes basic python packages. The package also uses the pm4py process mining package for fitness evaluations. Noteworthy, it uses few visualization packages like plotly express and kaleido to get the vizualizations. Please make sure the necessary packages are installed before execution. Few other packages include scipy, json etc. The test package can be installed using the pip command provided below.
 
 **pip install DA4RDM_Vis_Processbased**
 
-## Importing the Modules 
+
+## Importing the Module 
 The package has one important module **Vizualize**. This modules invokes the necessary functions from other modules that perform the tasks of data extraction, model creation, fitness evaluation and plotting. The module can be imported using the below command:
 
 ```python
 from DA4RDM_Vis_Processbased import Vizualize
 ```
 
 ## Usage
@@ -45,13 +46,13 @@
 ```python
 from DA4RDM_Vis_ProcessBased import Visualize
 path = Visualize.process_vis('17-02-2023.csv', "f5c043a1-82bc-4c61-bce6-0acbc0062948", '2023-02-14 08:57:44.315', '2021-05-03 02:31:54.652')
 print(path)
 ```
 
 ## Output
-All the above executions invokes the function **process_vis** with the passed parameter values.The fitness values are calculated and returned by the function. Finally, the results received is vizualized and a path is returned for the saved image.
+All the above executions invokes the function **process_vis** with the passed parameter values.The fitness values are calculated and returned by the function. The generated vizualization is saved onto the local repository of the program using the package. Finally a path is returned for the saved image.
 
 ```python
- 
+C:\Users\avina\anaconda3\lib\site-packages\DA4RDM_Vis_ProcessBased\Radarchart.png
 ```
-The generated files are saved onto the local repository of the program using the package.
+
```

### Comparing `DA4RDM_Vis_ProcessBased-0.1.0/DA4RDM_Vis_ProcessBased.egg-info/SOURCES.txt` & `DA4RDM_Vis_ProcessBased-0.1.1/DA4RDM_Vis_ProcessBased.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `DA4RDM_Vis_ProcessBased-0.1.0/LICENSE` & `DA4RDM_Vis_ProcessBased-0.1.1/LICENSE`

 * *Files identical despite different names*

### Comparing `DA4RDM_Vis_ProcessBased-0.1.0/PKG-INFO` & `DA4RDM_Vis_ProcessBased-0.1.1/DA4RDM_Vis_ProcessBased.egg-info/PKG-INFO`

 * *Files 6% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
-Name: DA4RDM_Vis_ProcessBased
-Version: 0.1.0
+Name: DA4RDM-Vis-ProcessBased
+Version: 0.1.1
 Summary: Package to get visualisation of fitness values evaluated for a given projectid analyzed on different RDLC phase process models
 Classifier: Programming Language :: Python :: 3.9
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
 Description-Content-Type: text/markdown
 License-File: LICENSE
 
@@ -15,15 +15,16 @@
 
 
 ## Installation
 The package is built using Python as a programming language and utilizes basic python packages. The package also uses the pm4py process mining package for fitness evaluations. Noteworthy, it uses few visualization packages like plotly express and kaleido to get the vizualizations. Please make sure the necessary packages are installed before execution. Few other packages include scipy, json etc. The test package can be installed using the pip command provided below.
 
 **pip install DA4RDM_Vis_Processbased**
 
-## Importing the Modules 
+
+## Importing the Module 
 The package has one important module **Vizualize**. This modules invokes the necessary functions from other modules that perform the tasks of data extraction, model creation, fitness evaluation and plotting. The module can be imported using the below command:
 
 ```python
 from DA4RDM_Vis_Processbased import Vizualize
 ```
 
 ## Usage
@@ -45,13 +46,13 @@
 ```python
 from DA4RDM_Vis_ProcessBased import Visualize
 path = Visualize.process_vis('17-02-2023.csv', "f5c043a1-82bc-4c61-bce6-0acbc0062948", '2023-02-14 08:57:44.315', '2021-05-03 02:31:54.652')
 print(path)
 ```
 
 ## Output
-All the above executions invokes the function **process_vis** with the passed parameter values.The fitness values are calculated and returned by the function. Finally, the results received is vizualized and a path is returned for the saved image.
+All the above executions invokes the function **process_vis** with the passed parameter values.The fitness values are calculated and returned by the function. The generated vizualization is saved onto the local repository of the program using the package. Finally a path is returned for the saved image.
 
 ```python
- 
+C:\Users\avina\anaconda3\lib\site-packages\DA4RDM_Vis_ProcessBased\Radarchart.png
 ```
-The generated files are saved onto the local repository of the program using the package.
+
```

### Comparing `DA4RDM_Vis_ProcessBased-0.1.0/README.md` & `DA4RDM_Vis_ProcessBased-0.1.1/README.md`

 * *Files 3% similar despite different names*

```diff
@@ -5,15 +5,16 @@
 
 
 ## Installation
 The package is built using Python as a programming language and utilizes basic python packages. The package also uses the pm4py process mining package for fitness evaluations. Noteworthy, it uses few visualization packages like plotly express and kaleido to get the vizualizations. Please make sure the necessary packages are installed before execution. Few other packages include scipy, json etc. The test package can be installed using the pip command provided below.
 
 **pip install DA4RDM_Vis_Processbased**
 
-## Importing the Modules 
+
+## Importing the Module 
 The package has one important module **Vizualize**. This modules invokes the necessary functions from other modules that perform the tasks of data extraction, model creation, fitness evaluation and plotting. The module can be imported using the below command:
 
 ```python
 from DA4RDM_Vis_Processbased import Vizualize
 ```
 
 ## Usage
@@ -35,13 +36,13 @@
 ```python
 from DA4RDM_Vis_ProcessBased import Visualize
 path = Visualize.process_vis('17-02-2023.csv', "f5c043a1-82bc-4c61-bce6-0acbc0062948", '2023-02-14 08:57:44.315', '2021-05-03 02:31:54.652')
 print(path)
 ```
 
 ## Output
-All the above executions invokes the function **process_vis** with the passed parameter values.The fitness values are calculated and returned by the function. Finally, the results received is vizualized and a path is returned for the saved image.
+All the above executions invokes the function **process_vis** with the passed parameter values.The fitness values are calculated and returned by the function. The generated vizualization is saved onto the local repository of the program using the package. Finally a path is returned for the saved image.
 
 ```python
- 
+C:\Users\avina\anaconda3\lib\site-packages\DA4RDM_Vis_ProcessBased\Radarchart.png
 ```
-The generated files are saved onto the local repository of the program using the package.
+
```

### Comparing `DA4RDM_Vis_ProcessBased-0.1.0/setup.py` & `DA4RDM_Vis_ProcessBased-0.1.1/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -3,15 +3,15 @@
 
 def readme():
     with open('README.md') as f:
         return f.read()
 
 
 setup(name='DA4RDM_Vis_ProcessBased',
-      version='0.1.0',
+      version='0.1.1',
       description='Package to get visualisation of fitness values evaluated for a given projectid analyzed '
                   'on different RDLC phase process models',
       long_description=readme(),
       classifiers=[
           "Programming Language :: Python :: 3.9",
           "License :: OSI Approved :: MIT License",
           "Operating System :: OS Independent",
```

### Comparing `DA4RDM_Vis_ProcessBased-0.1.0/src/DA4RDM_Vis_ProcessBased/Evaluate_Fitness.py` & `DA4RDM_Vis_ProcessBased-0.1.1/src/DA4RDM_Vis_ProcessBased/Evaluate_Fitness.py`

 * *Files identical despite different names*

### Comparing `DA4RDM_Vis_ProcessBased-0.1.0/src/DA4RDM_Vis_ProcessBased/Extract.py` & `DA4RDM_Vis_ProcessBased-0.1.1/src/DA4RDM_Vis_ProcessBased/Extract.py`

 * *Files identical despite different names*

### Comparing `DA4RDM_Vis_ProcessBased-0.1.0/src/DA4RDM_Vis_ProcessBased/PhaseData/Access.csv` & `DA4RDM_Vis_ProcessBased-0.1.1/src/DA4RDM_Vis_ProcessBased/PhaseData/Access.csv`

 * *Files identical despite different names*

### Comparing `DA4RDM_Vis_ProcessBased-0.1.0/src/DA4RDM_Vis_ProcessBased/PhaseData/Archival.csv` & `DA4RDM_Vis_ProcessBased-0.1.1/src/DA4RDM_Vis_ProcessBased/PhaseData/Archival.csv`

 * *Files identical despite different names*

### Comparing `DA4RDM_Vis_ProcessBased-0.1.0/src/DA4RDM_Vis_ProcessBased/PhaseData/Planning.csv` & `DA4RDM_Vis_ProcessBased-0.1.1/src/DA4RDM_Vis_ProcessBased/PhaseData/Planning.csv`

 * *Files identical despite different names*

### Comparing `DA4RDM_Vis_ProcessBased-0.1.0/src/DA4RDM_Vis_ProcessBased/PhaseData/Production.csv` & `DA4RDM_Vis_ProcessBased-0.1.1/src/DA4RDM_Vis_ProcessBased/PhaseData/Production.csv`

 * *Files identical despite different names*

### Comparing `DA4RDM_Vis_ProcessBased-0.1.0/src/DA4RDM_Vis_ProcessBased/PhaseData/Reuse.csv` & `DA4RDM_Vis_ProcessBased-0.1.1/src/DA4RDM_Vis_ProcessBased/PhaseData/Reuse.csv`

 * *Files identical despite different names*

### Comparing `DA4RDM_Vis_ProcessBased-0.1.0/src/DA4RDM_Vis_ProcessBased/Visualize.py` & `DA4RDM_Vis_ProcessBased-0.1.1/src/DA4RDM_Vis_ProcessBased/Visualize.py`

 * *Files identical despite different names*

