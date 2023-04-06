# Comparing `tmp/dtwParallel-0.9.8.tar.gz` & `tmp/dtwParallel-0.9.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "C:\Users\escud\Escritorio\Git-Paquete\dtwParallel\dist\tmpk7x8cgxu\dtwParallel-0.9.8.tar", last modified: Mon Aug  8 13:52:37 2022, max compression
+gzip compressed data, was "C:\Users\escud\Escritorio\Git-Paquete\dtwParallel\dist\tmpklqakv4s\dtwParallel-0.9.9.tar", last modified: Mon Aug  8 23:11:53 2022, max compression
```

## Comparing `dtwParallel-0.9.8.tar` & `dtwParallel-0.9.9.tar`

### file list

```diff
@@ -1,23 +1,23 @@
-drwxrwxrwx   0        0        0        0 2022-08-08 13:52:37.151390 dtwParallel-0.9.8/
--rw-rw-rw-   0        0        0      263 2022-03-08 08:57:58.000000 dtwParallel-0.9.8/AUTHORS
--rw-rw-rw-   0        0        0     1362 2022-07-04 11:58:27.000000 dtwParallel-0.9.8/LICENSE
--rw-rw-rw-   0        0        0    15103 2022-08-08 13:52:37.150389 dtwParallel-0.9.8/PKG-INFO
--rw-rw-rw-   0        0        0    12644 2022-07-25 11:08:05.000000 dtwParallel-0.9.8/README.md
-drwxrwxrwx   0        0        0        0 2022-08-08 13:52:37.092387 dtwParallel-0.9.8/dtwParallel/
--rw-rw-rw-   0        0        0       21 2022-08-08 13:50:27.000000 dtwParallel-0.9.8/dtwParallel/_version.py
--rw-rw-rw-   0        0        0      198 2022-07-27 09:09:57.000000 dtwParallel-0.9.8/dtwParallel/configuration.ini
--rw-rw-rw-   0        0        0     3448 2022-08-02 22:51:59.000000 dtwParallel-0.9.8/dtwParallel/dtwParallel.py
--rw-rw-rw-   0        0        0     8184 2022-08-08 13:49:39.000000 dtwParallel-0.9.8/dtwParallel/dtw_functions.py
--rw-rw-rw-   0        0        0     1942 2022-06-10 07:12:32.000000 dtwParallel-0.9.8/dtwParallel/error_control.py
--rw-rw-rw-   0        0        0     7106 2022-08-08 13:50:24.000000 dtwParallel-0.9.8/dtwParallel/utils.py
-drwxrwxrwx   0        0        0        0 2022-08-08 13:52:37.148389 dtwParallel-0.9.8/dtwParallel.egg-info/
--rw-rw-rw-   0        0        0    15103 2022-08-08 13:52:37.000000 dtwParallel-0.9.8/dtwParallel.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      465 2022-08-08 13:52:37.000000 dtwParallel-0.9.8/dtwParallel.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2022-08-08 13:52:37.000000 dtwParallel-0.9.8/dtwParallel.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       61 2022-08-08 13:52:37.000000 dtwParallel-0.9.8/dtwParallel.egg-info/entry_points.txt
--rw-rw-rw-   0        0        0       12 2022-08-08 13:52:37.000000 dtwParallel-0.9.8/dtwParallel.egg-info/namespace_packages.txt
--rw-rw-rw-   0        0        0       55 2022-08-08 13:52:37.000000 dtwParallel-0.9.8/dtwParallel.egg-info/requires.txt
--rw-rw-rw-   0        0        0       46 2022-08-08 13:52:37.000000 dtwParallel-0.9.8/dtwParallel.egg-info/top_level.txt
--rw-rw-rw-   0        0        0     1137 2022-08-08 13:50:34.000000 dtwParallel-0.9.8/pyproject.toml
--rw-rw-rw-   0        0        0       42 2022-08-08 13:52:37.151390 dtwParallel-0.9.8/setup.cfg
--rw-rw-rw-   0        0        0     2232 2022-07-28 11:36:46.000000 dtwParallel-0.9.8/setup.py
+drwxrwxrwx   0        0        0        0 2022-08-08 23:11:53.747719 dtwParallel-0.9.9/
+-rw-rw-rw-   0        0        0      263 2022-03-08 08:57:58.000000 dtwParallel-0.9.9/AUTHORS
+-rw-rw-rw-   0        0        0     1362 2022-07-04 11:58:27.000000 dtwParallel-0.9.9/LICENSE
+-rw-rw-rw-   0        0        0    15126 2022-08-08 23:11:53.747719 dtwParallel-0.9.9/PKG-INFO
+-rw-rw-rw-   0        0        0    12667 2022-08-08 23:08:12.000000 dtwParallel-0.9.9/README.md
+drwxrwxrwx   0        0        0        0 2022-08-08 23:11:53.688716 dtwParallel-0.9.9/dtwParallel/
+-rw-rw-rw-   0        0        0       21 2022-08-08 23:09:02.000000 dtwParallel-0.9.9/dtwParallel/_version.py
+-rw-rw-rw-   0        0        0      198 2022-07-27 09:09:57.000000 dtwParallel-0.9.9/dtwParallel/configuration.ini
+-rw-rw-rw-   0        0        0     3448 2022-08-02 22:51:59.000000 dtwParallel-0.9.9/dtwParallel/dtwParallel.py
+-rw-rw-rw-   0        0        0     8428 2022-08-08 23:10:08.000000 dtwParallel-0.9.9/dtwParallel/dtw_functions.py
+-rw-rw-rw-   0        0        0     1942 2022-06-10 07:12:32.000000 dtwParallel-0.9.9/dtwParallel/error_control.py
+-rw-rw-rw-   0        0        0     7144 2022-08-08 23:09:16.000000 dtwParallel-0.9.9/dtwParallel/utils.py
+drwxrwxrwx   0        0        0        0 2022-08-08 23:11:53.745715 dtwParallel-0.9.9/dtwParallel.egg-info/
+-rw-rw-rw-   0        0        0    15126 2022-08-08 23:11:53.000000 dtwParallel-0.9.9/dtwParallel.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      465 2022-08-08 23:11:53.000000 dtwParallel-0.9.9/dtwParallel.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2022-08-08 23:11:53.000000 dtwParallel-0.9.9/dtwParallel.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       61 2022-08-08 23:11:53.000000 dtwParallel-0.9.9/dtwParallel.egg-info/entry_points.txt
+-rw-rw-rw-   0        0        0       12 2022-08-08 23:11:53.000000 dtwParallel-0.9.9/dtwParallel.egg-info/namespace_packages.txt
+-rw-rw-rw-   0        0        0       55 2022-08-08 23:11:53.000000 dtwParallel-0.9.9/dtwParallel.egg-info/requires.txt
+-rw-rw-rw-   0        0        0       46 2022-08-08 23:11:53.000000 dtwParallel-0.9.9/dtwParallel.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0     1137 2022-08-08 23:09:08.000000 dtwParallel-0.9.9/pyproject.toml
+-rw-rw-rw-   0        0        0       42 2022-08-08 23:11:53.748717 dtwParallel-0.9.9/setup.cfg
+-rw-rw-rw-   0        0        0     2232 2022-07-28 11:36:46.000000 dtwParallel-0.9.9/setup.py
```

### Comparing `dtwParallel-0.9.8/LICENSE` & `dtwParallel-0.9.9/LICENSE`

 * *Files identical despite different names*

### Comparing `dtwParallel-0.9.8/PKG-INFO` & `dtwParallel-0.9.9/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: dtwParallel
-Version: 0.9.8
+Version: 0.9.9
 Summary: Python implementation of Dynamic Time Warping (DTW), which allows computing the dtw distance between one-dimensional and multidimensional time series, with the possibility of visualisation (one-dimensional case) and parallelisation (multidimensional case).
 Home-page: https://github.com/oscarescuderoarnanz/dtwParallel
 Author: oscarescuderoarnanz
 Author-email: Óscar <escuderoarnanzoscar@gmail.com>
 License: BSD 2-Clause License
         
         Copyright (c) 2022, Universidad Rey Juan Carlos
@@ -42,24 +42,25 @@
 License-File: LICENSE
 License-File: AUTHORS
 
 # Dynamic Time Warping 
 
 This package allows to measure the similarity between two-time sequences, i.e., it finds the optimal alignment between two time-dependent sequences. It will enable the calculation of univariate and multivariate time series. Any distance available in `scipy.spatial.distance` and `gower` distance can be used. Extra functionality has been incorporated to transform the resulting DTW matrix into an exponential kernel.
 
-Univariate Time Series:
-- It incorporates the possibility of visualizing the cost matrix and the path to reach the DTW distance value. This will allow it to be used in a didactic way, providing a better understanding of the method used.
-- It allows the calculation of regular and irregular univariate time series.
-
-Multivariate Time Series: 
-- The calculation of dependent DTW and independent DTW is available.
-- The computation can be CPU parallelized by selecting the number of threads. 
-- The distance matrix obtained can be transformed into a kernel.
+Common functionalities for 2-time series (TS):
+- It incorporates the possibility of visualizing the cost matrix and the path to reach the DTW distance value between two TS. This will allow its use in a didactic way, providing a better understanding of the method used.
+- It is possible to calculate TS with the same and different lengths. 
+
+Common functionalities for N (> 2) time series (TS):
+- The calculation can be parallelized by the CPU by selecting the number of threads. As a result, we will obtain the distance matrix. 
+- It is possible to perform not only the calculation of distances but also similarities (based on an exponential kernel).
+
+Multivariate TS functionalities: 
+- Calculation of dependent DTW and independent DTW is available.
 
-Code is designed to allow working with regular and irregular time series. *Note*: for multivariate time series, only the calculation of the dependent DTW distance is available.
 
 ## Package structure 
 
 <p align="center"> <img src="./Images/schema.png"> </p>
 
 <p align="center"> <img src="./Images/fileSchema.png"> </p>
 
@@ -70,15 +71,15 @@
 for installing Python packages. To do it, run the following command:
 ```
 pip install dtwParallel
 ```
 
 ## Requirements
 
-Perceval requires Python >= 3.6.1 or later to run. For other Python
+dtwParallel requires Python >= 3.6.1 or later to run. For other Python
 dependencies, please check the `pyproject.toml` file included
 on this repository.
 
 
 Note that you should have also the following packages installed in your system:
 - numpy
 - pandas
```

### Comparing `dtwParallel-0.9.8/README.md` & `dtwParallel-0.9.9/README.md`

 * *Files 2% similar despite different names*

```diff
@@ -1,21 +1,22 @@
 # Dynamic Time Warping 
 
 This package allows to measure the similarity between two-time sequences, i.e., it finds the optimal alignment between two time-dependent sequences. It will enable the calculation of univariate and multivariate time series. Any distance available in `scipy.spatial.distance` and `gower` distance can be used. Extra functionality has been incorporated to transform the resulting DTW matrix into an exponential kernel.
 
-Univariate Time Series:
-- It incorporates the possibility of visualizing the cost matrix and the path to reach the DTW distance value. This will allow it to be used in a didactic way, providing a better understanding of the method used.
-- It allows the calculation of regular and irregular univariate time series.
-
-Multivariate Time Series: 
-- The calculation of dependent DTW and independent DTW is available.
-- The computation can be CPU parallelized by selecting the number of threads. 
-- The distance matrix obtained can be transformed into a kernel.
+Common functionalities for 2-time series (TS):
+- It incorporates the possibility of visualizing the cost matrix and the path to reach the DTW distance value between two TS. This will allow its use in a didactic way, providing a better understanding of the method used.
+- It is possible to calculate TS with the same and different lengths. 
+
+Common functionalities for N (> 2) time series (TS):
+- The calculation can be parallelized by the CPU by selecting the number of threads. As a result, we will obtain the distance matrix. 
+- It is possible to perform not only the calculation of distances but also similarities (based on an exponential kernel).
+
+Multivariate TS functionalities: 
+- Calculation of dependent DTW and independent DTW is available.
 
-Code is designed to allow working with regular and irregular time series. *Note*: for multivariate time series, only the calculation of the dependent DTW distance is available.
 
 ## Package structure 
 
 <p align="center"> <img src="./Images/schema.png"> </p>
 
 <p align="center"> <img src="./Images/fileSchema.png"> </p>
 
@@ -26,15 +27,15 @@
 for installing Python packages. To do it, run the following command:
 ```
 pip install dtwParallel
 ```
 
 ## Requirements
 
-Perceval requires Python >= 3.6.1 or later to run. For other Python
+dtwParallel requires Python >= 3.6.1 or later to run. For other Python
 dependencies, please check the `pyproject.toml` file included
 on this repository.
 
 
 Note that you should have also the following packages installed in your system:
 - numpy
 - pandas
```

### Comparing `dtwParallel-0.9.8/dtwParallel/dtwParallel.py` & `dtwParallel-0.9.9/dtwParallel/dtwParallel.py`

 * *Files identical despite different names*

### Comparing `dtwParallel-0.9.8/dtwParallel/dtw_functions.py` & `dtwParallel-0.9.9/dtwParallel/dtw_functions.py`

 * *Files 6% similar despite different names*

```diff
@@ -45,22 +45,40 @@
             cost_matrix[positions_object[index]] = list(D.values())[index][0]
             index += 1
 
     arr = np.delete(cost_matrix, np.s_[0], 1)
     return np.delete(arr, np.s_[0], 0)
 
 
+# Function to paint the cost matrix.
+def plot_cost_matrix(warp_path, cost):
+    fig, ax = plt.subplots(figsize=(12, 10))
+    ax = sbn.heatmap(cost, annot=True, square=True, linewidths=0.1, cmap="YlGnBu", ax=ax)
+
+    # Get the warp path in x and y directions
+    path_x = [p[0] for p in warp_path]
+    path_y = [p[1] for p in warp_path]
+
+    # Align the path from the center of each cell
+    path_xx = [x + 0.5 for x in path_x]
+    path_yy = [y + 0.5 for y in path_y]
+
+    ax.plot(path_xx, path_yy, color='blue', linewidth=3, alpha=0.2)
+
+
+
 # Function for the calculation of the independent DTW distance.
-def dtw_ind(x, y, dist, dtw_distance=0):
+def dtw_ind(x, y, dist, dtw_distance=0, get_visualization=False):
 	
     dim_m = x.shape[1]
+    arr_D = []
     for index_m in range(dim_m):
         x_aux = x[:, index_m]
         y_aux = y[:, index_m]
-        iter_object = [(1, 1) for i in range(x_aux.ndim) for j in range(y_aux.ndim)]
+        iter_object = [(i + 1, j + 1) for i in range(len(x)) for j in range(len(y))]
         # Starting conditions:
         # 1) D(0,0) = 0
         # 2) D(i,0) = inf
         # 3) D(0,j) = inf
         D = defaultdict(lambda: (float('inf'),))
         D[0, 0] = (0, 0, 0)
         if dist == "gower":
@@ -76,35 +94,21 @@
             for i, j in iter_object:
                 # Given the function distance as input parameter the distance between x and y is calculated.
                 # In case of using gower distance we fit the data.
                 dt = dist(x_aux, y_aux)
                 D[i, j] = min((D[i - 1, j][0] + dt, i - 1, j),
                               (D[i, j - 1][0] + dt, i, j - 1),
                               (D[i - 1, j - 1][0] + dt, i - 1, j - 1))
+        if get_visualization:
+            arr_D.append(D)
 
-        dtw_distance += D[x_aux.ndim, y_aux.ndim][0]
+        dtw_distance += D[len(x_aux), len(y_aux)][0]
 
-    return dtw_distance
-    
+    return dtw_distance, arr_D
     
-# Function to paint the cost matrix.
-def plot_cost_matrix(warp_path, cost):
-    fig, ax = plt.subplots(figsize=(12, 10))
-    ax = sbn.heatmap(cost, annot=True, square=True, linewidths=0.1, cmap="YlGnBu", ax=ax)
-
-    # Get the warp path in x and y directions
-    path_x = [p[0] for p in warp_path]
-    path_y = [p[1] for p in warp_path]
-
-    # Align the path from the center of each cell
-    path_xx = [x + 0.5 for x in path_x]
-    path_yy = [y + 0.5 for y in path_y]
-
-    ax.plot(path_xx, path_yy, color='blue', linewidth=3, alpha=0.2)
-
 
 # Function for the calculation of the dependent DTW distance.
 def dtw_dep(x, y, dist, mult_UTS=False):
     iter_object = [(i + 1, j + 1) for i in range(len(x)) for j in range(len(y))]
     # Starting conditions:
     # 1) D(0,0) = 0
     # 2) D(i,0) = inf
@@ -138,15 +142,15 @@
 def dtw(x, y=None, type_dtw="d", dist=distance.euclidean, MTS=False, get_visualization=False, check_errors=False, n_threads=-1, DTW_to_kernel=False, sigma=1):
 
     if check_errors:
         x, y = control_inputs(x, y, type_dtw, MTS)
     
     if MTS:        
         if type_dtw == "i":
-            dtw_distance = dtw_ind(x, y, dist)
+            dtw_distance, D = dtw_ind(x, y, dist, get_visualization=get_visualization)
         else:
             dtw_distance, D = dtw_dep(x, y, dist)
     else:
         # Data matrix (UTS) introduced in dataframe format
         if isinstance(x, pd.DataFrame):
             if y is None:
                 y = x.copy()
@@ -177,23 +181,26 @@
                 if y is None:
                     sys.stderr.write("You need introduce a vector -y")
                     sys.exit(0)
                 dtw_distance, D = dtw_dep(x, y, dist)
 
                 
     if get_visualization:
-        if type_dtw != "i":
+        if type_dtw == "i":
+            for i in range(len(D)):
+                path = []
+                get_path(x, y, D[i], path)
+                plot_cost_matrix(path, get_cost_matrix(D[i]))
+        else:
             path = []
             get_path(x, y, D, path)
             cost_matrix = get_cost_matrix(D)
             plot_cost_matrix(path, cost_matrix)
-        else:
-            raise ValueError('Display not allowed. Only univariate case.')
 
-    return dtw_distance
+    return dtw_distance, D
 
 
 # We transform the DTW matrix to an exponential kernel. 
 def transform_DTW_to_kernel(data, sigma):
 	
 	return np.exp(-data/(2*sigma**2))
```

### Comparing `dtwParallel-0.9.8/dtwParallel/error_control.py` & `dtwParallel-0.9.9/dtwParallel/error_control.py`

 * *Files identical despite different names*

### Comparing `dtwParallel-0.9.8/dtwParallel/utils.py` & `dtwParallel-0.9.9/dtwParallel/utils.py`

 * *Files 1% similar despite different names*

```diff
@@ -14,21 +14,21 @@
         -x   Time series 1
         -y   Time series 2
         -t   Calculation type DTW (str)
         -d   Type of distance (function or gower)
         -ce  Check data for errors (bool)
         -of Output to File (bool)
         -nf Name of file (str)
+        -vis Visualization of Time Series. only available when using dtwParallel with an API. (bool)
         -n Numero de hilos empleados para la paralelización (int)
         -k Transformación de la matriz de distancia a kernel (bool)
         -s Valor de sigma para la transformación a kernel exponencial aplicada (float)
 
     Others args:
         MTS  Bool value
-        get_visualization  Bool value
     
     Optional arguments:
         -h, --help            show this help message and exit
         -v, --version         show version
         -l, --list            show available backends
     \n
 """
@@ -38,15 +38,15 @@
     %(prog)s [<args>] | --help | --version | --list \n   
 """ \
 + str(DTW_DESC_MSG)
 
     
 DTW_VERSION_MSG = \
 """
-    %(prog)s 0.9.8 
+    %(prog)s 0.9.9 
 """
     
 
 def read_data(fname):
     return pd.read_csv(StringIO(fname.read()), header = None, sep=";")
     
 
@@ -114,16 +114,16 @@
                         help="d: dependient or i: independient.")
     parser.add_argument("-d", "--distance", nargs='?', default=input_obj.distance, type=str,
                         help="Use a possible distance of scipy.spatial.distance.")
     parser.add_argument("-ce", "--check_errors", nargs='?', default=input_obj.check_errors, type=str,
                         help="Control whether or not check for errors.")
     parser.add_argument("MTS", nargs='?', default=input_obj.MTS, type=bool,
                         help="Indicates whether the data are multivariate time series or not.")
-    parser.add_argument("visualization", nargs='?', default=input_obj.visualization, type=bool,
-                        help="Allows you to indicate whether to display the results or not. Only for the one-dimensional case.")
+    parser.add_argument("-vis", nargs='?', default=input_obj.visualization, type=bool,
+                        help="Allows you to indicate whether to display the results or not. Only for API case.")
     parser.add_argument("-of", "--output_file", nargs='?', default=input_obj.output_file, type=bool,
                         help="Output by file instead of terminal.")
     parser.add_argument("-nf", "--name_file", nargs='?', default=input_obj.name_file, type=str,
                         help="Name file.")
 
 
     # In case of working with files containing N multivariate time series, we give the possibility
```

### Comparing `dtwParallel-0.9.8/dtwParallel.egg-info/PKG-INFO` & `dtwParallel-0.9.9/dtwParallel.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: dtwParallel
-Version: 0.9.8
+Version: 0.9.9
 Summary: Python implementation of Dynamic Time Warping (DTW), which allows computing the dtw distance between one-dimensional and multidimensional time series, with the possibility of visualisation (one-dimensional case) and parallelisation (multidimensional case).
 Home-page: https://github.com/oscarescuderoarnanz/dtwParallel
 Author: oscarescuderoarnanz
 Author-email: Óscar <escuderoarnanzoscar@gmail.com>
 License: BSD 2-Clause License
         
         Copyright (c) 2022, Universidad Rey Juan Carlos
@@ -42,24 +42,25 @@
 License-File: LICENSE
 License-File: AUTHORS
 
 # Dynamic Time Warping 
 
 This package allows to measure the similarity between two-time sequences, i.e., it finds the optimal alignment between two time-dependent sequences. It will enable the calculation of univariate and multivariate time series. Any distance available in `scipy.spatial.distance` and `gower` distance can be used. Extra functionality has been incorporated to transform the resulting DTW matrix into an exponential kernel.
 
-Univariate Time Series:
-- It incorporates the possibility of visualizing the cost matrix and the path to reach the DTW distance value. This will allow it to be used in a didactic way, providing a better understanding of the method used.
-- It allows the calculation of regular and irregular univariate time series.
-
-Multivariate Time Series: 
-- The calculation of dependent DTW and independent DTW is available.
-- The computation can be CPU parallelized by selecting the number of threads. 
-- The distance matrix obtained can be transformed into a kernel.
+Common functionalities for 2-time series (TS):
+- It incorporates the possibility of visualizing the cost matrix and the path to reach the DTW distance value between two TS. This will allow its use in a didactic way, providing a better understanding of the method used.
+- It is possible to calculate TS with the same and different lengths. 
+
+Common functionalities for N (> 2) time series (TS):
+- The calculation can be parallelized by the CPU by selecting the number of threads. As a result, we will obtain the distance matrix. 
+- It is possible to perform not only the calculation of distances but also similarities (based on an exponential kernel).
+
+Multivariate TS functionalities: 
+- Calculation of dependent DTW and independent DTW is available.
 
-Code is designed to allow working with regular and irregular time series. *Note*: for multivariate time series, only the calculation of the dependent DTW distance is available.
 
 ## Package structure 
 
 <p align="center"> <img src="./Images/schema.png"> </p>
 
 <p align="center"> <img src="./Images/fileSchema.png"> </p>
 
@@ -70,15 +71,15 @@
 for installing Python packages. To do it, run the following command:
 ```
 pip install dtwParallel
 ```
 
 ## Requirements
 
-Perceval requires Python >= 3.6.1 or later to run. For other Python
+dtwParallel requires Python >= 3.6.1 or later to run. For other Python
 dependencies, please check the `pyproject.toml` file included
 on this repository.
 
 
 Note that you should have also the following packages installed in your system:
 - numpy
 - pandas
```

### Comparing `dtwParallel-0.9.8/pyproject.toml` & `dtwParallel-0.9.9/pyproject.toml`

 * *Files 0% similar despite different names*

```diff
@@ -2,15 +2,15 @@
 
 [build-system]
 requires      = ["setuptools>=61.0.0", "wheel"]
 build-backend = "setuptools.build_meta"
 
 [project]
 name = "dtwParallel"
-version = "0.9.8"
+version = "0.9.9"
 description = "Python implementation of Dynamic Time Warping (DTW), which allows computing the dtw distance between one-dimensional and multidimensional time series, with the possibility of visualisation (one-dimensional case) and parallelisation (multidimensional case)."
 readme = "README.md"
 authors = [{ name = "Óscar", email = "escuderoarnanzoscar@gmail.com" }]
 license = { file = "LICENSE" }
 
 classifiers=[
     'Intended Audience :: Science/Research',
```

### Comparing `dtwParallel-0.9.8/setup.py` & `dtwParallel-0.9.9/setup.py`

 * *Files identical despite different names*

