# Comparing `tmp/parallel-principal-feature-analysis-1.0.3.tar.gz` & `tmp/parallel-principal-feature-analysis-1.0.4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "parallel-principal-feature-analysis-1.0.3.tar", last modified: Mon Jan 30 17:49:53 2023, max compression
+gzip compressed data, was "parallel-principal-feature-analysis-1.0.4.tar", last modified: Fri Apr  7 12:53:33 2023, max compression
```

## Comparing `parallel-principal-feature-analysis-1.0.3.tar` & `parallel-principal-feature-analysis-1.0.4.tar`

### file list

```diff
@@ -1,20 +1,20 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 17:49:53.067228 parallel-principal-feature-analysis-1.0.3/
--rw-r--r--   0 runner    (1001) docker     (123)     1618 2023-01-30 17:49:39.000000 parallel-principal-feature-analysis-1.0.3/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)     5470 2023-01-30 17:49:53.067228 parallel-principal-feature-analysis-1.0.3/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     5018 2023-01-30 17:49:39.000000 parallel-principal-feature-analysis-1.0.3/README.md
--rw-r--r--   0 runner    (1001) docker     (123)      107 2023-01-30 17:49:39.000000 parallel-principal-feature-analysis-1.0.3/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-01-30 17:49:53.067228 parallel-principal-feature-analysis-1.0.3/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)      867 2023-01-30 17:49:39.000000 parallel-principal-feature-analysis-1.0.3/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 17:49:53.063228 parallel-principal-feature-analysis-1.0.3/src/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 17:49:53.067228 parallel-principal-feature-analysis-1.0.3/src/parallel_principal_feature_analysis/
--rw-r--r--   0 runner    (1001) docker     (123)      239 2023-01-30 17:49:39.000000 parallel-principal-feature-analysis-1.0.3/src/parallel_principal_feature_analysis/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5279 2023-01-30 17:49:39.000000 parallel-principal-feature-analysis-1.0.3/src/parallel_principal_feature_analysis/execute_PFA.py
--rw-r--r--   0 runner    (1001) docker     (123)    10212 2023-01-30 17:49:39.000000 parallel-principal-feature-analysis-1.0.3/src/parallel_principal_feature_analysis/find_relevant_principal_features.py
--rw-r--r--   0 runner    (1001) docker     (123)     6586 2023-01-30 17:49:39.000000 parallel-principal-feature-analysis-1.0.3/src/parallel_principal_feature_analysis/get_mutual_information.py
--rw-r--r--   0 runner    (1001) docker     (123)     8838 2023-01-30 17:49:39.000000 parallel-principal-feature-analysis-1.0.3/src/parallel_principal_feature_analysis/principal_feature_analysis.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 17:49:53.067228 parallel-principal-feature-analysis-1.0.3/src/parallel_principal_feature_analysis.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     5470 2023-01-30 17:49:53.000000 parallel-principal-feature-analysis-1.0.3/src/parallel_principal_feature_analysis.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      674 2023-01-30 17:49:53.000000 parallel-principal-feature-analysis-1.0.3/src/parallel_principal_feature_analysis.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-30 17:49:53.000000 parallel-principal-feature-analysis-1.0.3/src/parallel_principal_feature_analysis.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       28 2023-01-30 17:49:53.000000 parallel-principal-feature-analysis-1.0.3/src/parallel_principal_feature_analysis.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       36 2023-01-30 17:49:53.000000 parallel-principal-feature-analysis-1.0.3/src/parallel_principal_feature_analysis.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 12:53:33.287069 parallel-principal-feature-analysis-1.0.4/
+-rw-r--r--   0 runner    (1001) docker     (123)     1618 2023-04-07 12:53:18.000000 parallel-principal-feature-analysis-1.0.4/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)     5956 2023-04-07 12:53:33.283069 parallel-principal-feature-analysis-1.0.4/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     5504 2023-04-07 12:53:18.000000 parallel-principal-feature-analysis-1.0.4/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)      107 2023-04-07 12:53:18.000000 parallel-principal-feature-analysis-1.0.4/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-07 12:53:33.287069 parallel-principal-feature-analysis-1.0.4/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)      867 2023-04-07 12:53:18.000000 parallel-principal-feature-analysis-1.0.4/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 12:53:33.283069 parallel-principal-feature-analysis-1.0.4/src/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 12:53:33.283069 parallel-principal-feature-analysis-1.0.4/src/parallel_principal_feature_analysis/
+-rw-r--r--   0 runner    (1001) docker     (123)      239 2023-04-07 12:53:18.000000 parallel-principal-feature-analysis-1.0.4/src/parallel_principal_feature_analysis/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5279 2023-04-07 12:53:18.000000 parallel-principal-feature-analysis-1.0.4/src/parallel_principal_feature_analysis/execute_PFA.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10908 2023-04-07 12:53:18.000000 parallel-principal-feature-analysis-1.0.4/src/parallel_principal_feature_analysis/find_relevant_principal_features.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6586 2023-04-07 12:53:18.000000 parallel-principal-feature-analysis-1.0.4/src/parallel_principal_feature_analysis/get_mutual_information.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9558 2023-04-07 12:53:18.000000 parallel-principal-feature-analysis-1.0.4/src/parallel_principal_feature_analysis/principal_feature_analysis.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 12:53:33.283069 parallel-principal-feature-analysis-1.0.4/src/parallel_principal_feature_analysis.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     5956 2023-04-07 12:53:33.000000 parallel-principal-feature-analysis-1.0.4/src/parallel_principal_feature_analysis.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      674 2023-04-07 12:53:33.000000 parallel-principal-feature-analysis-1.0.4/src/parallel_principal_feature_analysis.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 12:53:33.000000 parallel-principal-feature-analysis-1.0.4/src/parallel_principal_feature_analysis.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       28 2023-04-07 12:53:33.000000 parallel-principal-feature-analysis-1.0.4/src/parallel_principal_feature_analysis.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       36 2023-04-07 12:53:33.000000 parallel-principal-feature-analysis-1.0.4/src/parallel_principal_feature_analysis.egg-info/top_level.txt
```

### Comparing `parallel-principal-feature-analysis-1.0.3/LICENSE` & `parallel-principal-feature-analysis-1.0.4/LICENSE`

 * *Files identical despite different names*

### Comparing `parallel-principal-feature-analysis-1.0.3/PKG-INFO` & `parallel-principal-feature-analysis-1.0.4/PKG-INFO`

 * *Files 5% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: parallel-principal-feature-analysis
-Version: 1.0.3
+Version: 1.0.4
 Summary: The first package for (parallel) Principal Feature Analysis
 Author: Tim Breitenbach & Lauritz Rasbach
 Author-email: tim.breitenbach@mathematik.uni-wuerzburg.de, rasbachlauritz@googlemail.com
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: BSD License
 Classifier: Operating System :: OS Independent
 Requires-Python: >=3.6
@@ -34,15 +34,15 @@
 When calling the function on Windows make sure to call it like this for the parallelization to work:
 ```Python
 if __name__ == "__main__":
   par_pfa(path*, number_output_functions, number_sweeps, cluster_size, alpha, min_n_datapoints_a_bin, shuffle_feature_numbers, frac, claculate_mutual_information, basis_log_mutual_information) # function call
 ```
 
 ### Parameters
-- **path (String, required):** Path to the input CSV file.
+- **path (String, required):** Path to the input CSV file. The format of the csv file is a matrix where in each column there is a sample. The first number_output_functions rows of each sample vector represent the labels of each output function for this sample and the subsequent rows represent the value of each feature of this sample. Consequently, the format is number rows = (number_output_functions + number features) times number columns = number samples or data points, respectively. All entries in this matrix are supposed to be numeric.
 - **number_output_functions (int, default=1):** Number of output features that are to be modeled, i.e. the number of components of the vector-valued output-function. The values are stored in the first number_output_functions rows of the csv-file.
 - **number_sweeps (int, default=1):** Number of sweeps of the PFA. The result of the last sweep is returned. In addition, the return of each sweep are interesected and returned as well.
 - **cluster_size (int, default=50):** Number of nodes of a subgraph in the principal_feature_analysis.
 - **alpha (float, default=0.01):** Level of significance.
 - **min_n_data_points_a_bin (int, default=500):**: The minimum number of data points for each bin in the chi-square test.
 - **shuffle_feature_numbers (bool, default=False):** If True the number of the features is randomly shuffled.
 - **frac (int, default=1):** The fraction of the dataset that is used for the analysis. The set is randomly sampled from the input csv.
```

### Comparing `parallel-principal-feature-analysis-1.0.3/README.md` & `parallel-principal-feature-analysis-1.0.4/README.md`

 * *Files 4% similar despite different names*

```diff
@@ -21,15 +21,15 @@
 When calling the function on Windows make sure to call it like this for the parallelization to work:
 ```Python
 if __name__ == "__main__":
   par_pfa(path*, number_output_functions, number_sweeps, cluster_size, alpha, min_n_datapoints_a_bin, shuffle_feature_numbers, frac, claculate_mutual_information, basis_log_mutual_information) # function call
 ```
 
 ### Parameters
-- **path (String, required):** Path to the input CSV file.
+- **path (String, required):** Path to the input CSV file. The format of the csv file is a matrix where in each column there is a sample. The first number_output_functions rows of each sample vector represent the labels of each output function for this sample and the subsequent rows represent the value of each feature of this sample. Consequently, the format is number rows = (number_output_functions + number features) times number columns = number samples or data points, respectively. All entries in this matrix are supposed to be numeric.
 - **number_output_functions (int, default=1):** Number of output features that are to be modeled, i.e. the number of components of the vector-valued output-function. The values are stored in the first number_output_functions rows of the csv-file.
 - **number_sweeps (int, default=1):** Number of sweeps of the PFA. The result of the last sweep is returned. In addition, the return of each sweep are interesected and returned as well.
 - **cluster_size (int, default=50):** Number of nodes of a subgraph in the principal_feature_analysis.
 - **alpha (float, default=0.01):** Level of significance.
 - **min_n_data_points_a_bin (int, default=500):**: The minimum number of data points for each bin in the chi-square test.
 - **shuffle_feature_numbers (bool, default=False):** If True the number of the features is randomly shuffled.
 - **frac (int, default=1):** The fraction of the dataset that is used for the analysis. The set is randomly sampled from the input csv.
```

### Comparing `parallel-principal-feature-analysis-1.0.3/setup.py` & `parallel-principal-feature-analysis-1.0.4/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import setuptools
 
 with open("README.md", "r", encoding="utf-8") as fh:
     long_description = fh.read()
 
 setuptools.setup(
     name="parallel-principal-feature-analysis",
-    version="1.0.3",
+    version="1.0.4",
     author="Tim Breitenbach & Lauritz Rasbach",
     author_email="tim.breitenbach@mathematik.uni-wuerzburg.de, rasbachlauritz@googlemail.com",
     description="The first package for (parallel) Principal Feature Analysis",
     long_description=long_description,
     long_description_content_type="text/markdown",
     classifiers=[
         "Programming Language :: Python :: 3",
```

### Comparing `parallel-principal-feature-analysis-1.0.3/src/parallel_principal_feature_analysis/execute_PFA.py` & `parallel-principal-feature-analysis-1.0.4/src/parallel_principal_feature_analysis/execute_PFA.py`

 * *Files identical despite different names*

### Comparing `parallel-principal-feature-analysis-1.0.3/src/parallel_principal_feature_analysis/find_relevant_principal_features.py` & `parallel-principal-feature-analysis-1.0.4/src/parallel_principal_feature_analysis/find_relevant_principal_features.py`

 * *Files 8% similar despite different names*

```diff
@@ -98,16 +98,20 @@
                     freq_data_product = np.histogram2d(data[id_output, :], data[j, :],
                                                 bins=(l[id_output], l[j]))[0]
                     expfreq = np.outer(freq_data[id_output], freq_data[j]) / n
                     if sum(expfreq.flatten() < 5) > 0:
                         counter_bins_less_than5_relevant_principal_features += 1
                     if sum(expfreq.flatten() < 1) > 0:
                         counter_bins_less_than1_relevant_principal_features += 1
-                    pv = scipy.stats.chisquare(freq_data_product.flatten(), expfreq.flatten(),ddof=-1)[1]
-                    # ddof=-1 to have the degrees of freedom of the chi square eaual the number of bins, see corresponding paper (Appendix) for details
+                    pv = scipy.stats.chisquare(freq_data_product.flatten(), expfreq.flatten(),ddof=(freq_data_product.shape[0]-1)+(freq_data_product.shape[1]-1))[1]
+                    # According to the documentation of scipy.stats.chisquare, the degrees of freedom is k-1 - ddof where ddof=0 by default and k=freq_data_product.shape[0]*freq_data_product.shape[0]. 
+                    # According to literatur, the chi square test statistic for a test of independence (r x m contingency table) is approximately chi square distributed (under some assumptions) with degrees of freedom equal 
+                    # freq_data_product.shape[0]-1)*(freq_data_product.shape[1]-1) = freq_data_product.shape[0]*freq_data_product.shape[1] - freq_data_product.shape[0] - freq_data_product.shape[1] + 1. 
+                    # Consequently, ddof is set equal freq_data_product.shape[0]-1+freq_data_product.shape[1]-1 to adjust the degrees of freedom accordingly.
+
                     # if p-value pv is less than alpha the hypothesis that j is independent of the output function is rejected
                     if pv <= alpha:
                         dependent=1
                         break
                 if dependent==1:
                     intermediate_list_depending_on_system_state.append(j)
                 else:
```

### Comparing `parallel-principal-feature-analysis-1.0.3/src/parallel_principal_feature_analysis/get_mutual_information.py` & `parallel-principal-feature-analysis-1.0.4/src/parallel_principal_feature_analysis/get_mutual_information.py`

 * *Files identical despite different names*

### Comparing `parallel-principal-feature-analysis-1.0.3/src/parallel_principal_feature_analysis/principal_feature_analysis.py` & `parallel-principal-feature-analysis-1.0.4/src/parallel_principal_feature_analysis/principal_feature_analysis.py`

 * *Files 20% similar despite different names*

```diff
@@ -56,16 +56,20 @@
                                                             bins=(l[cluster[i]], l[cluster[j]]))[0]
                             expfreq = np.outer(freq_data[cluster[i]], freq_data[cluster[j]]) / n
 
                             if sum(expfreq.flatten() < 5) > 0:
                                 counter_bin_less_than5 += 1
                             if sum(expfreq.flatten() < 1) > 0:
                                 counter_bin_less_than1 += 1
-                            pv = scipy.stats.chisquare(freq_data_product.flatten(), expfreq.flatten(),ddof=-1)[1]
-                            # ddof=-1 to have the degrees of freedom of the chi square eaual the number of bins, see corresponding paper (Appendix) for details
+                            pv = scipy.stats.chisquare(freq_data_product.flatten(), expfreq.flatten(),ddof=(freq_data_product.shape[0]-1)+(freq_data_product.shape[1]-1))[1]
+                            # According to the documentation of scipy.stats.chisquare, the degrees of freedom is k-1 - ddof where ddof=0 by default and k=freq_data_product.shape[0]*freq_data_product.shape[0]. 
+                            # According to literatur, the chi square test statistic for a test of independence (r x m contingency table) is approximately chi square distributed (under some assumptions) with degrees of freedom equal 
+                            # freq_data_product.shape[0]-1)*(freq_data_product.shape[1]-1) = freq_data_product.shape[0]*freq_data_product.shape[1] - freq_data_product.shape[0] - freq_data_product.shape[1] + 1. 
+                            # Consequently, ddof is set equal freq_data_product.shape[0]-1+freq_data_product.shape[1]-1 to adjust the degrees of freedom accordingly.
+
                             # if p-value pv is less than alpha the hypothesis that j is independent of i is rejected
                             if pv <= alpha:
                                 global_adjm[cluster[i], cluster[j] ] = 1
                                 global_adjm[cluster[j], cluster[i]] = 1
                         counter_calculations += 1
                 adjm=(global_adjm[cluster,:])[:,cluster] # add the entries of the adjacency matrix of the subcluster to the global adjacency matrix
```

### Comparing `parallel-principal-feature-analysis-1.0.3/src/parallel_principal_feature_analysis.egg-info/PKG-INFO` & `parallel-principal-feature-analysis-1.0.4/src/parallel_principal_feature_analysis.egg-info/PKG-INFO`

 * *Files 5% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: parallel-principal-feature-analysis
-Version: 1.0.3
+Version: 1.0.4
 Summary: The first package for (parallel) Principal Feature Analysis
 Author: Tim Breitenbach & Lauritz Rasbach
 Author-email: tim.breitenbach@mathematik.uni-wuerzburg.de, rasbachlauritz@googlemail.com
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: BSD License
 Classifier: Operating System :: OS Independent
 Requires-Python: >=3.6
@@ -34,15 +34,15 @@
 When calling the function on Windows make sure to call it like this for the parallelization to work:
 ```Python
 if __name__ == "__main__":
   par_pfa(path*, number_output_functions, number_sweeps, cluster_size, alpha, min_n_datapoints_a_bin, shuffle_feature_numbers, frac, claculate_mutual_information, basis_log_mutual_information) # function call
 ```
 
 ### Parameters
-- **path (String, required):** Path to the input CSV file.
+- **path (String, required):** Path to the input CSV file. The format of the csv file is a matrix where in each column there is a sample. The first number_output_functions rows of each sample vector represent the labels of each output function for this sample and the subsequent rows represent the value of each feature of this sample. Consequently, the format is number rows = (number_output_functions + number features) times number columns = number samples or data points, respectively. All entries in this matrix are supposed to be numeric.
 - **number_output_functions (int, default=1):** Number of output features that are to be modeled, i.e. the number of components of the vector-valued output-function. The values are stored in the first number_output_functions rows of the csv-file.
 - **number_sweeps (int, default=1):** Number of sweeps of the PFA. The result of the last sweep is returned. In addition, the return of each sweep are interesected and returned as well.
 - **cluster_size (int, default=50):** Number of nodes of a subgraph in the principal_feature_analysis.
 - **alpha (float, default=0.01):** Level of significance.
 - **min_n_data_points_a_bin (int, default=500):**: The minimum number of data points for each bin in the chi-square test.
 - **shuffle_feature_numbers (bool, default=False):** If True the number of the features is randomly shuffled.
 - **frac (int, default=1):** The fraction of the dataset that is used for the analysis. The set is randomly sampled from the input csv.
```

### Comparing `parallel-principal-feature-analysis-1.0.3/src/parallel_principal_feature_analysis.egg-info/SOURCES.txt` & `parallel-principal-feature-analysis-1.0.4/src/parallel_principal_feature_analysis.egg-info/SOURCES.txt`

 * *Files identical despite different names*

