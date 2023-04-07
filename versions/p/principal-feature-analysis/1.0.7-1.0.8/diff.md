# Comparing `tmp/principal-feature-analysis-1.0.7.tar.gz` & `tmp/principal-feature-analysis-1.0.8.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "principal-feature-analysis-1.0.7.tar", last modified: Mon Jan 30 17:47:09 2023, max compression
+gzip compressed data, was "principal-feature-analysis-1.0.8.tar", last modified: Fri Apr  7 12:46:49 2023, max compression
```

## Comparing `principal-feature-analysis-1.0.7.tar` & `principal-feature-analysis-1.0.8.tar`

### file list

```diff
@@ -1,20 +1,20 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 17:47:09.654879 principal-feature-analysis-1.0.7/
--rw-r--r--   0 runner    (1001) docker     (123)     1618 2023-01-30 17:46:58.000000 principal-feature-analysis-1.0.7/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)     5052 2023-01-30 17:47:09.654879 principal-feature-analysis-1.0.7/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     4614 2023-01-30 17:46:58.000000 principal-feature-analysis-1.0.7/README.md
--rw-r--r--   0 runner    (1001) docker     (123)      107 2023-01-30 17:46:58.000000 principal-feature-analysis-1.0.7/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-01-30 17:47:09.654879 principal-feature-analysis-1.0.7/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)      847 2023-01-30 17:46:58.000000 principal-feature-analysis-1.0.7/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 17:47:09.654879 principal-feature-analysis-1.0.7/src/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 17:47:09.654879 principal-feature-analysis-1.0.7/src/principal_feature_analysis/
--rw-r--r--   0 runner    (1001) docker     (123)      235 2023-01-30 17:46:58.000000 principal-feature-analysis-1.0.7/src/principal_feature_analysis/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5369 2023-01-30 17:46:58.000000 principal-feature-analysis-1.0.7/src/principal_feature_analysis/execute_PFA.py
--rw-r--r--   0 runner    (1001) docker     (123)    10212 2023-01-30 17:46:58.000000 principal-feature-analysis-1.0.7/src/principal_feature_analysis/find_relevant_principal_features.py
--rw-r--r--   0 runner    (1001) docker     (123)     6586 2023-01-30 17:46:58.000000 principal-feature-analysis-1.0.7/src/principal_feature_analysis/get_mutual_information.py
--rw-r--r--   0 runner    (1001) docker     (123)     7634 2023-01-30 17:46:58.000000 principal-feature-analysis-1.0.7/src/principal_feature_analysis/principal_feature_analysis.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 17:47:09.654879 principal-feature-analysis-1.0.7/src/principal_feature_analysis.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     5052 2023-01-30 17:47:09.000000 principal-feature-analysis-1.0.7/src/principal_feature_analysis.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      584 2023-01-30 17:47:09.000000 principal-feature-analysis-1.0.7/src/principal_feature_analysis.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-30 17:47:09.000000 principal-feature-analysis-1.0.7/src/principal_feature_analysis.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       28 2023-01-30 17:47:09.000000 principal-feature-analysis-1.0.7/src/principal_feature_analysis.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       27 2023-01-30 17:47:09.000000 principal-feature-analysis-1.0.7/src/principal_feature_analysis.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 12:46:49.528861 principal-feature-analysis-1.0.8/
+-rw-r--r--   0 runner    (1001) docker     (123)     1618 2023-04-07 12:46:39.000000 principal-feature-analysis-1.0.8/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)     5538 2023-04-07 12:46:49.528861 principal-feature-analysis-1.0.8/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     5100 2023-04-07 12:46:39.000000 principal-feature-analysis-1.0.8/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)      107 2023-04-07 12:46:39.000000 principal-feature-analysis-1.0.8/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-07 12:46:49.528861 principal-feature-analysis-1.0.8/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)      847 2023-04-07 12:46:39.000000 principal-feature-analysis-1.0.8/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 12:46:49.524861 principal-feature-analysis-1.0.8/src/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 12:46:49.528861 principal-feature-analysis-1.0.8/src/principal_feature_analysis/
+-rw-r--r--   0 runner    (1001) docker     (123)      235 2023-04-07 12:46:39.000000 principal-feature-analysis-1.0.8/src/principal_feature_analysis/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5369 2023-04-07 12:46:39.000000 principal-feature-analysis-1.0.8/src/principal_feature_analysis/execute_PFA.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10908 2023-04-07 12:46:39.000000 principal-feature-analysis-1.0.8/src/principal_feature_analysis/find_relevant_principal_features.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6586 2023-04-07 12:46:39.000000 principal-feature-analysis-1.0.8/src/principal_feature_analysis/get_mutual_information.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8342 2023-04-07 12:46:39.000000 principal-feature-analysis-1.0.8/src/principal_feature_analysis/principal_feature_analysis.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 12:46:49.528861 principal-feature-analysis-1.0.8/src/principal_feature_analysis.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     5538 2023-04-07 12:46:49.000000 principal-feature-analysis-1.0.8/src/principal_feature_analysis.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      584 2023-04-07 12:46:49.000000 principal-feature-analysis-1.0.8/src/principal_feature_analysis.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 12:46:49.000000 principal-feature-analysis-1.0.8/src/principal_feature_analysis.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       28 2023-04-07 12:46:49.000000 principal-feature-analysis-1.0.8/src/principal_feature_analysis.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       27 2023-04-07 12:46:49.000000 principal-feature-analysis-1.0.8/src/principal_feature_analysis.egg-info/top_level.txt
```

### Comparing `principal-feature-analysis-1.0.7/LICENSE` & `principal-feature-analysis-1.0.8/LICENSE`

 * *Files identical despite different names*

### Comparing `principal-feature-analysis-1.0.7/PKG-INFO` & `principal-feature-analysis-1.0.8/README.md`

 * *Files 16% similar despite different names*

```diff
@@ -1,66 +1,53 @@
-Metadata-Version: 2.1
-Name: principal-feature-analysis
-Version: 1.0.7
-Summary: The first package for Principal Feature Analysis
-Author: Tim Breitenbach & Lauritz Rasbach
-Author-email: tim.breitenbach@mathematik.uni-wuerzburg.de, rasbachlauritz@googlemail.com
-Classifier: Programming Language :: Python :: 3
-Classifier: License :: OSI Approved :: BSD License
-Classifier: Operating System :: OS Independent
-Requires-Python: >=3.6
-Description-Content-Type: text/markdown
-License-File: LICENSE
-
-# Principal-Feature-Analysis (PFA)
-If you use the presented PFA method or the provided Python scripts inspired you for further extensions or variations of this framework, we’ll be happy if you cite our paper “A principal feature analysis” (https://doi.org/10.1016/j.jocs.2021.101502) in course of which the Python implementations of this git repository have been worked out.
-
-
-https://arxiv.org/abs/2101.12720
-
-A parallelized version of the algorithm can be found here: https://github.com/LauritzR/Parallel-Principal-Feature-Analysis
-## Installation
-```
-pip install principal-feature-analysis
-```
-
-## Usage
-
-```Python
-from principal_feature_analysis import pfa # import the main pfa function
-
-pfa(path*, number_output_functions, number_sweeps, cluster_size, alpha, min_n_datapoints_a_bin, shuffle_feature_numbers, frac, claculate_mutual_information, basis_log_mutual_information) # function call
-```
-
-### Parameters
-- **path (String, required):** Path to the input CSV file.
-- **number_output_functions (int, default=1):** Number of output features that are to be modeled, i.e. the number of components of the vector-valued output-function. The values are stored in the first number_output_functions rows of the csv-file.
-- **number_sweeps (int, default=1):** Number of sweeps of the PFA. The result of the last sweep is returned. In addition, the return of each sweep are interesected and returned as well.
-- **cluster_size (int, default=50):** Number of nodes of a subgraph in the principal_feature_analysis.
-- **alpha (float, default=0.01):** Level of significance.
-- **min_n_data_points_a_bin (int, default=500):**: The minimum number of data points for each bin in the chi-square test.
-- **shuffle_feature_numbers (bool, default=False):** If True the number of the features is randomly shuffled.
-- **frac (int, default=1):** The fraction of the dataset that is used for the analysis. The set is randomly sampled from the input csv.
-- **calculate_mutual_information (bool, default=False):** If True the mutual information with features from the PFA with the system state is calculated.
-- **basis_log_mutual_information (int. default=2):** Basis of the logarithm used in the calculation of the mutual information.
-
-### Output Files
-- **principal_features_depending_system_state[i].txt:**
-Lists the indices (related to the rows of the input csv) of the features that depend on the system state (row 0) where [i] is replaced by the number of sweeps. Each row of this file is a subgraph that could not be divided further where a * separates the features on which the system state depends (before *) and the ones on which the system state does not depend (after *).
-- **principal_features_depending_system_state_intersection.txt:**
-Analog to the “principal_features_depending_system_state[i].txt”. Due to the intersection the information of subgraphs is missed and there is only one feature a row.
-- **principal_features_global_indices[i].txt:**
-is the result from the dissection of the graph of all input features before testing for dependence to the system state of the sweep [i]. Each row corresponds to a subgraph that could not have been dissected further where the numbers refer to the features stored in the corresponding row of the input csv.
-- **global_indices_and_principal_features_state_dependency[i].csv:**
-A csv file where for each sweep [i] the first column is the feature number referring to the row of the input csv file and the second row is the p-value from the chi2 test of the feature with the system state. A p-value of 1.1 means that it was not possible to make at least two bins for corresponding feature due to for a second not at least min_n_datapoints_a_bin where left. Consequently the feature is considered as constant and thus independent of the system state.
-
-
-### Returns
-- **pf_from_intersection (list):** A list with content analog to the file principal_features_depending_system_state_intersection.txt.
-- **data_frame_feature_mutual_information (pandas.DataFrame, if calculate_mutual_information=True):** A Pandas data frame that contains the mutual information with the feature (index related to the row in the input csv) with the system state (row 0 in the input csv).
-
-
-## Advanced
-The principal_feature_analysis package also grants access to other functions used for the principal component analysis algorithm. In case you want to access those you can import them like this.
-```Python
-from principal_feature_analysis import find_relevant_principal_features, get_mutual_information, principal_feature_analysis
-```
+# Principal-Feature-Analysis (PFA)
+If you use the presented PFA method or the provided Python scripts inspired you for further extensions or variations of this framework, we’ll be happy if you cite our paper “A principal feature analysis” (https://doi.org/10.1016/j.jocs.2021.101502) in course of which the Python implementations of this git repository have been worked out.
+
+
+https://arxiv.org/abs/2101.12720
+
+A parallelized version of the algorithm can be found here: https://github.com/LauritzR/Parallel-Principal-Feature-Analysis
+## Installation
+```
+pip install principal-feature-analysis
+```
+
+## Usage
+
+```Python
+from principal_feature_analysis import pfa # import the main pfa function
+
+pfa(path*, number_output_functions, number_sweeps, cluster_size, alpha, min_n_datapoints_a_bin, shuffle_feature_numbers, frac, claculate_mutual_information, basis_log_mutual_information) # function call
+```
+
+### Parameters
+- **path (String, required):** Path to the input CSV file. The format of the csv file is a matrix where in each column there is a sample. The first number_output_functions rows of each sample vector represent the labels of each output function for this sample and the subsequent rows represent the value of each feature of this sample. Consequently, the format is number rows = (number_output_functions + number features) times number columns = number samples or data points, respectively. All entries in this matrix are supposed to be numeric.
+- **number_output_functions (int, default=1):** Number of output features that are to be modeled, i.e. the number of components of the vector-valued output-function. The values are stored in the first number_output_functions rows of the csv-file.
+- **number_sweeps (int, default=1):** Number of sweeps of the PFA. The result of the last sweep is returned. In addition, the return of each sweep are interesected and returned as well.
+- **cluster_size (int, default=50):** Number of nodes of a subgraph in the principal_feature_analysis.
+- **alpha (float, default=0.01):** Level of significance.
+- **min_n_data_points_a_bin (int, default=500):**: The minimum number of data points for each bin in the chi-square test.
+- **shuffle_feature_numbers (bool, default=False):** If True the number of the features is randomly shuffled.
+- **frac (int, default=1):** The fraction of the dataset that is used for the analysis. The set is randomly sampled from the input csv.
+- **calculate_mutual_information (bool, default=False):** If True the mutual information with features from the PFA with the system state is calculated.
+- **basis_log_mutual_information (int. default=2):** Basis of the logarithm used in the calculation of the mutual information.
+
+### Output Files
+- **principal_features_depending_system_state[i].txt:**
+Lists the indices (related to the rows of the input csv) of the features that depend on the system state (row 0) where [i] is replaced by the number of sweeps. Each row of this file is a subgraph that could not be divided further where a * separates the features on which the system state depends (before *) and the ones on which the system state does not depend (after *).
+- **principal_features_depending_system_state_intersection.txt:**
+Analog to the “principal_features_depending_system_state[i].txt”. Due to the intersection the information of subgraphs is missed and there is only one feature a row.
+- **principal_features_global_indices[i].txt:**
+is the result from the dissection of the graph of all input features before testing for dependence to the system state of the sweep [i]. Each row corresponds to a subgraph that could not have been dissected further where the numbers refer to the features stored in the corresponding row of the input csv.
+- **global_indices_and_principal_features_state_dependency[i].csv:**
+A csv file where for each sweep [i] the first column is the feature number referring to the row of the input csv file and the second row is the p-value from the chi2 test of the feature with the system state. A p-value of 1.1 means that it was not possible to make at least two bins for corresponding feature due to for a second not at least min_n_datapoints_a_bin where left. Consequently the feature is considered as constant and thus independent of the system state.
+
+
+### Returns
+- **pf_from_intersection (list):** A list with content analog to the file principal_features_depending_system_state_intersection.txt.
+- **data_frame_feature_mutual_information (pandas.DataFrame, if calculate_mutual_information=True):** A Pandas data frame that contains the mutual information with the feature (index related to the row in the input csv) with the system state (row 0 in the input csv).
+
+
+## Advanced
+The principal_feature_analysis package also grants access to other functions used for the principal component analysis algorithm. In case you want to access those you can import them like this.
+```Python
+from principal_feature_analysis import find_relevant_principal_features, get_mutual_information, principal_feature_analysis
+```
```

### Comparing `principal-feature-analysis-1.0.7/setup.py` & `principal-feature-analysis-1.0.8/setup.py`

 * *Files 18% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import setuptools
 
 with open("README.md", "r", encoding="utf-8") as fh:
     long_description = fh.read()
 
 setuptools.setup(
     name="principal-feature-analysis",
-    version="1.0.7",
+    version="1.0.8",
     author="Tim Breitenbach & Lauritz Rasbach",
     author_email="tim.breitenbach@mathematik.uni-wuerzburg.de, rasbachlauritz@googlemail.com",
     description="The first package for Principal Feature Analysis",
     long_description=long_description,
     long_description_content_type="text/markdown",
     classifiers=[
         "Programming Language :: Python :: 3",
```

### Comparing `principal-feature-analysis-1.0.7/src/principal_feature_analysis/execute_PFA.py` & `principal-feature-analysis-1.0.8/src/principal_feature_analysis/execute_PFA.py`

 * *Files identical despite different names*

### Comparing `principal-feature-analysis-1.0.7/src/principal_feature_analysis/find_relevant_principal_features.py` & `principal-feature-analysis-1.0.8/src/principal_feature_analysis/find_relevant_principal_features.py`

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

### Comparing `principal-feature-analysis-1.0.7/src/principal_feature_analysis/get_mutual_information.py` & `principal-feature-analysis-1.0.8/src/principal_feature_analysis/get_mutual_information.py`

 * *Files identical despite different names*

### Comparing `principal-feature-analysis-1.0.7/src/principal_feature_analysis/principal_feature_analysis.py` & `principal-feature-analysis-1.0.8/src/principal_feature_analysis/principal_feature_analysis.py`

 * *Files 12% similar despite different names*

```diff
@@ -52,16 +52,20 @@
                                                        bins=(l[cluster[i]], l[cluster[j]]))[0]
                         expfreq = np.outer(freq_data[cluster[i]], freq_data[cluster[j]]) / n
 
                         if sum(expfreq.flatten() < 5) > 0:
                             counter_bin_less_than5 += 1
                         if sum(expfreq.flatten() < 1) > 0:
                             counter_bin_less_than1 += 1
-                        pv = scipy.stats.chisquare(freq_data_product.flatten(), expfreq.flatten(),ddof=-1)[1]
-                        # ddof=-1 to have the degrees of freedom of the chi square eaual the number of bins, see corresponding paper (Appendix) for details
+                        pv = scipy.stats.chisquare(freq_data_product.flatten(), expfreq.flatten(),ddof=(freq_data_product.shape[0]-1)+(freq_data_product.shape[1]-1))[1]
+                        # According to the documentation of scipy.stats.chisquare, the degrees of freedom is k-1 - ddof where ddof=0 by default and k=freq_data_product.shape[0]*freq_data_product.shape[0]. 
+                        # According to literatur, the chi square test statistic for a test of independence (r x m contingency table) is approximately chi square distributed (under some assumptions) with degrees of freedom equal 
+                        # freq_data_product.shape[0]-1)*(freq_data_product.shape[1]-1) = freq_data_product.shape[0]*freq_data_product.shape[1] - freq_data_product.shape[0] - freq_data_product.shape[1] + 1. 
+                        # Consequently, ddof is set equal freq_data_product.shape[0]-1+freq_data_product.shape[1]-1 to adjust the degrees of freedom accordingly.
+
                         # if p-value pv is less than alpha the hypothesis that j is independent of i is rejected
                         if pv <= alpha:
                             global_adjm[cluster[i], cluster[j] ] = 1
                             global_adjm[cluster[j], cluster[i]] = 1
                     counter_calculations += 1
             adjm=(global_adjm[cluster,:])[:,cluster] # add the entries of the adjacency matrix of the subcluster to the global adjacency matrix
```

### Comparing `principal-feature-analysis-1.0.7/src/principal_feature_analysis.egg-info/PKG-INFO` & `principal-feature-analysis-1.0.8/PKG-INFO`

 * *Files 21% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: principal-feature-analysis
-Version: 1.0.7
+Version: 1.0.8
 Summary: The first package for Principal Feature Analysis
 Author: Tim Breitenbach & Lauritz Rasbach
 Author-email: tim.breitenbach@mathematik.uni-wuerzburg.de, rasbachlauritz@googlemail.com
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: BSD License
 Classifier: Operating System :: OS Independent
 Requires-Python: >=3.6
@@ -28,15 +28,15 @@
 ```Python
 from principal_feature_analysis import pfa # import the main pfa function
 
 pfa(path*, number_output_functions, number_sweeps, cluster_size, alpha, min_n_datapoints_a_bin, shuffle_feature_numbers, frac, claculate_mutual_information, basis_log_mutual_information) # function call
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

### Comparing `principal-feature-analysis-1.0.7/src/principal_feature_analysis.egg-info/SOURCES.txt` & `principal-feature-analysis-1.0.8/src/principal_feature_analysis.egg-info/SOURCES.txt`

 * *Files identical despite different names*

