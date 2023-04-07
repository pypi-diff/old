# Comparing `tmp/pandas_dq-1.4.tar.gz` & `tmp/pandas_dq-1.5.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pandas_dq-1.4.tar", last modified: Fri Apr  7 00:56:20 2023, max compression
+gzip compressed data, was "pandas_dq-1.5.tar", last modified: Fri Apr  7 13:52:26 2023, max compression
```

## Comparing `pandas_dq-1.4.tar` & `pandas_dq-1.5.tar`

### file list

```diff
@@ -1,15 +1,15 @@
-drwxrwxrwx   0 ram       (1000) ram       (1000)        0 2023-04-07 00:56:20.876816 pandas_dq-1.4/
--rwxrwxrwx   0 ram       (1000) ram       (1000)    11357 2023-04-02 23:27:15.000000 pandas_dq-1.4/LICENSE
--rwxrwxrwx   0 ram       (1000) ram       (1000)      610 2022-04-07 23:06:53.000000 pandas_dq-1.4/MANIFEST.in
--rwxrwxrwx   0 ram       (1000) ram       (1000)     9486 2023-04-07 00:56:20.861167 pandas_dq-1.4/PKG-INFO
--rwxrwxrwx   0 ram       (1000) ram       (1000)     7807 2023-04-07 00:49:33.000000 pandas_dq-1.4/README.md
-drwxrwxrwx   0 ram       (1000) ram       (1000)        0 2023-04-07 00:56:20.845543 pandas_dq-1.4/pandas_dq.egg-info/
--rwxrwxrwx   0 ram       (1000) ram       (1000)     9486 2023-04-07 00:56:20.000000 pandas_dq-1.4/pandas_dq.egg-info/PKG-INFO
--rwxrwxrwx   0 ram       (1000) ram       (1000)      232 2023-04-07 00:56:20.000000 pandas_dq-1.4/pandas_dq.egg-info/SOURCES.txt
--rwxrwxrwx   0 ram       (1000) ram       (1000)        1 2023-04-07 00:56:20.000000 pandas_dq-1.4/pandas_dq.egg-info/dependency_links.txt
--rwxrwxrwx   0 ram       (1000) ram       (1000)       56 2023-04-07 00:56:20.000000 pandas_dq-1.4/pandas_dq.egg-info/requires.txt
--rwxrwxrwx   0 ram       (1000) ram       (1000)       10 2023-04-07 00:56:20.000000 pandas_dq-1.4/pandas_dq.egg-info/top_level.txt
--rwxrwxrwx   0 ram       (1000) ram       (1000)    37060 2023-04-07 00:30:01.000000 pandas_dq-1.4/pandas_dq.py
--rwxrwxrwx   0 ram       (1000) ram       (1000)       60 2023-04-07 00:54:49.000000 pandas_dq-1.4/requirements.txt
--rwxrwxrwx   0 ram       (1000) ram       (1000)       38 2023-04-07 00:56:20.876816 pandas_dq-1.4/setup.cfg
--rwxrwxrwx   0 ram       (1000) ram       (1000)      902 2023-04-07 00:55:14.000000 pandas_dq-1.4/setup.py
+drwxrwxrwx   0 ram       (1000) ram       (1000)        0 2023-04-07 13:52:26.514515 pandas_dq-1.5/
+-rwxrwxrwx   0 ram       (1000) ram       (1000)    11357 2023-04-02 23:27:15.000000 pandas_dq-1.5/LICENSE
+-rwxrwxrwx   0 ram       (1000) ram       (1000)      610 2022-04-07 23:06:53.000000 pandas_dq-1.5/MANIFEST.in
+-rwxrwxrwx   0 ram       (1000) ram       (1000)     9758 2023-04-07 13:52:26.498888 pandas_dq-1.5/PKG-INFO
+-rwxrwxrwx   0 ram       (1000) ram       (1000)     8087 2023-04-07 13:15:32.000000 pandas_dq-1.5/README.md
+drwxrwxrwx   0 ram       (1000) ram       (1000)        0 2023-04-07 13:52:26.483265 pandas_dq-1.5/pandas_dq.egg-info/
+-rwxrwxrwx   0 ram       (1000) ram       (1000)     9758 2023-04-07 13:52:25.000000 pandas_dq-1.5/pandas_dq.egg-info/PKG-INFO
+-rwxrwxrwx   0 ram       (1000) ram       (1000)      232 2023-04-07 13:52:26.000000 pandas_dq-1.5/pandas_dq.egg-info/SOURCES.txt
+-rwxrwxrwx   0 ram       (1000) ram       (1000)        1 2023-04-07 13:52:25.000000 pandas_dq-1.5/pandas_dq.egg-info/dependency_links.txt
+-rwxrwxrwx   0 ram       (1000) ram       (1000)       49 2023-04-07 13:52:25.000000 pandas_dq-1.5/pandas_dq.egg-info/requires.txt
+-rwxrwxrwx   0 ram       (1000) ram       (1000)       10 2023-04-07 13:52:25.000000 pandas_dq-1.5/pandas_dq.egg-info/top_level.txt
+-rwxrwxrwx   0 ram       (1000) ram       (1000)    39889 2023-04-07 13:46:26.000000 pandas_dq-1.5/pandas_dq.py
+-rwxrwxrwx   0 ram       (1000) ram       (1000)       52 2023-04-07 12:15:09.000000 pandas_dq-1.5/requirements.txt
+-rwxrwxrwx   0 ram       (1000) ram       (1000)       38 2023-04-07 13:52:26.514515 pandas_dq-1.5/setup.cfg
+-rwxrwxrwx   0 ram       (1000) ram       (1000)      883 2023-04-07 12:14:57.000000 pandas_dq-1.5/setup.py
```

### Comparing `pandas_dq-1.4/LICENSE` & `pandas_dq-1.5/LICENSE`

 * *Files identical despite different names*

### Comparing `pandas_dq-1.4/MANIFEST.in` & `pandas_dq-1.5/MANIFEST.in`

 * *Files identical despite different names*

### Comparing `pandas_dq-1.4/PKG-INFO` & `pandas_dq-1.5/PKG-INFO`

 * *Files 5% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pandas_dq
-Version: 1.4
+Version: 1.5
 Summary: Clean your data using a scikit-learn transformer in a single line of code
 Home-page: https://github.com/AutoViML/pandas_dq
 Author: Ram Seshadri
 License: Apache License 2.0
 Description: # pandas_dq
         Analyze and clean your data in a single line of code with a Scikit-Learn compatible Transformer.
         
@@ -30,29 +30,29 @@
         ## Uses
         `pandas_dq` has two important modules: `dq_report` and `Fix_DQ`. 
         
         ### 1.  dq_report function
         
         ![dq_report_code](./images/find_dq_screenshot.png)
         
-        <p>`dq_report` is a function that is probably the most popular way to use pandas_dq and it performs following data quality analysis steps:
+        <p>`dq_report` is a function that is the most popular way to use pandas_dq and it performs following data quality analysis steps:
         <ol>
         <li>It detects missing values and suggests to impute them with mean, median, mode, or a constant value.</li>
         <li>It identifies rare categories and suggests to group them into a single category or drop them.</li>
         <li>It finds infinite values and suggests to replace them with NaN or a large value.</li>
         <li>It detects mixed data types and suggests to convert them to a single type or split them into multiple columns.</li>
         <li>It detects outliers and suggests to remove them or use robust statistics.</li>
         <li>It detects high cardinality features and suggests to reduce them using encoding techniques or feature selection methods.</li>
         <li>It detects highly correlated features and suggests to drop one of them or use dimensionality reduction techniques.</li>
         <li>It detects duplicate rows and columns and suggests to drop them or keep only one copy.</li>
         <li>It detects skewed distributions and suggests to apply transformations or scaling techniques. </li>
         <li>It detects imbalanced classes and suggests to use resampling techniques or class weights. </li>
         <li>It detects feature leakage and suggests to avoid using features that are not available at prediction time. </li>
         </ol>
-        
+        Notice that for large datasets, this report generation may take time. So please be patient while it analyzes your dataset!
         
         ### 2.  Fix_DQ class: a scikit_learn transformer which can detect data quality issues and clean them all in one line of code
         
         ![fix_dq](./images/fix_dq_screenshot.png)
         
         <p>`Fix_DQ` is a great way to clean an entire train data set and apply the same steps in an MLOps pipeline to a test dataset.  `Fix_DQ` can be used to detect most issues in your data (similar to dq_report but without the target related steps) in one step (during `fit` method). This transformer can then be saved (or "pickled") for applying the same steps on test data either at the same time or later.<br>
         
@@ -116,35 +116,34 @@
         It prints out a data quality report like this:
         
         ![dq_report](./images/dq_report_screenshot.png)
         
         ## API
         
         <p>
-        pandas_dq has a very simple API with the following inputs. You need to create a sklearn-compatible transformer pipeline object by importing Fix_DQ from pandas_dq library. <p>
-        Once you import it, you can define the object by giving several options such as:
+        pandas_dq has a very simple API with just two modules to import: one will find data quality issues in your data and the other will fix it. Simple!
         
         **Arguments**
         
         `dq_report` has only 4 arguments:
         - `data`: You can provide any kind of file format (string) or even a pandas DataFrame (df). It reads parquet, csv, feather, arrow, all kinds of file formats straight from disk. You just have to tell it the path to the file and the name of the file.
         - `target`: default: `None`. Otherwise, it should be a string name representing the name of a column in df. You can leave it as `None` if you don't want any target related issues.
-        - `csv_engine`: default is `pandas`. If you want to load your file using any other backend engine such as `arrow` or `parquet` please specify it here.
+        - `csv_engine`: default is `pandas`. If you want to load your CSV file using any other backend engine such as `arrow` or `parquet` please specify it here. This option only impacts CSV files.
         - `verbose`: This has 2 possible states:
           - `0` summary report. Prints only the summary level data quality issues in the dataset. Great for managers.
           - `1` detailed report. Prints all the gory details behind each DQ issue in your dataset and what to do about them. Great for engineers.
         
         `Fix_DQ` has slightly more arguments:
         <b>Caution:</b> X_train and y_train in Fix_DQ must be pandas Dataframes or pandas Series. I have not tested it on numpy arrays. You can try your luck.
         
         - `quantile`: float (0.75): Define a threshold for IQR for outlier detection. Could be any float between 0 and 1. If quantile is set to `None`, then no outlier detection will take place.
-        - `cat_fill_value`: string ("missing"): Define a fill value for missing categories in your object or categorical variables. This is a global default for your entire dataset. I will try to change it to a dictionary so that you can specify different values for different columns.
-        - `num_fill_value`: integer or float (999): Define a fill value for missing numbers in your integer or float variables.  This is a global default for your entire dataset. I will try to change it to a dictionary so that you can specify different values for different columns.
-        - `rare_threshold`: float (0.05):  Define a threshold for rare categories. If a certain category in a column is less 5% (say) of samples, then it will considered rare. All rare categories will be merged with a category value called "Rare". 
-        - `correlation_threshold`: float (0.8): Define a correlation limit. Anything above this limit, the variable will be dropped. 
+        - `cat_fill_value`: string ("missing") or a dictionary: Define a fill value for missing categories in your object or categorical variables. This is a global default for your entire dataset. You can also give a dictionary where you specify different fill values for different columns.
+        - `num_fill_value`: integer (99) or float value (999.0) or a dictionary: Define a fill value for missing numbers in your integer or float variables.  This is a global default for your entire dataset. You can also give a dictionary where you specify different fill values for different columns.
+        - `rare_threshold`: float (0.05):  Define a threshold for rare categories. If a certain category in a column is less than say 5% (0.05) of samples, then it will be considered rare. All rare categories in that column will be merged under a new category named "Rare". 
+        - `correlation_threshold`: float (0.8): Define a correlation limit. Anything above this limit, if two variables are correlated, one of them will be dropped. The program will tell you which variable is being dropped. You can switch the sequence of variables in your dataset if you want the one or other dropped.
         <p>
         
         ## Maintainers
         
         * [@AutoViML](https://github.com/AutoViML)
         
         ## Contributing
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: pandas_dq Version: 1.4 Summary: Clean your data
+Metadata-Version: 2.1 Name: pandas_dq Version: 1.5 Summary: Clean your data
 using a scikit-learn transformer in a single line of code Home-page: https://
 github.com/AutoViML/pandas_dq Author: Ram Seshadri License: Apache License 2.0
 Description: # pandas_dq Analyze and clean your data in a single line of code
 with a Scikit-Learn compatible Transformer. # Table of Contents
     * What_is_pandas_dq
     * How_to_use_pandas_dq
     * How_to_install_pandas_dq
@@ -13,16 +13,16 @@
     * License
 ## Introduction ### What is pandas_dq? `pandas_dq` is a new python library for
 automatically cleaning your dirty dataset using pandas scikit_learn functions.
 You can analyze your dataset and fix them - all in a single line of code! !
 [pandas_dq](./images/pandas_dq_logo.png) ## Uses `pandas_dq` has two important
 modules: `dq_report` and `Fix_DQ`. ### 1. dq_report function ![dq_report_code]
 (./images/find_dq_screenshot.png)
-`dq_report` is a function that is probably the most popular way to use
-pandas_dq and it performs following data quality analysis steps:
+`dq_report` is a function that is the most popular way to use pandas_dq and it
+performs following data quality analysis steps:
    1. It detects missing values and suggests to impute them with mean, median,
       mode, or a constant value.
    2. It identifies rare categories and suggests to group them into a single
       category or drop them.
    3. It finds infinite values and suggests to replace them with NaN or a large
       value.
    4. It detects mixed data types and suggests to convert them to a single type
@@ -36,17 +36,18 @@
       only one copy.
    9. It detects skewed distributions and suggests to apply transformations or
       scaling techniques.
   10. It detects imbalanced classes and suggests to use resampling techniques
       or class weights.
   11. It detects feature leakage and suggests to avoid using features that are
       not available at prediction time.
-### 2. Fix_DQ class: a scikit_learn transformer which can detect data quality
-issues and clean them all in one line of code ![fix_dq](./images/
-fix_dq_screenshot.png)
+Notice that for large datasets, this report generation may take time. So please
+be patient while it analyzes your dataset! ### 2. Fix_DQ class: a scikit_learn
+transformer which can detect data quality issues and clean them all in one line
+of code ![fix_dq](./images/fix_dq_screenshot.png)
 `Fix_DQ` is a great way to clean an entire train data set and apply the same
 steps in an MLOps pipeline to a test dataset. `Fix_DQ` can be used to detect
 most issues in your data (similar to dq_report but without the target related
 steps) in one step (during `fit` method). This transformer can then be saved
 (or "pickled") for applying the same steps on test data either at the same time
 or later.
 ### How can we use Fix_DQ in GridSearchCV to find the best model pipeline?
@@ -72,47 +73,48 @@
 the transformer on X_train and transform it X_train_transformed =
 fdq.fit_transform(X_train) # Transform X_test using the fitted transformer
 X_test_transformed = fdq.transform(X_test) ``` ### if you are not using the
 Transformer, you can simply call the function, dq_report ``` from pandas_dq
 import dq_report dq_report(data, target=target, csv_engine="pandas", verbose=1)
 ``` It prints out a data quality report like this: ![dq_report](./images/
 dq_report_screenshot.png) ## API
-pandas_dq has a very simple API with the following inputs. You need to create a
-sklearn-compatible transformer pipeline object by importing Fix_DQ from
-pandas_dq library.
-Once you import it, you can define the object by giving several options such
-as: **Arguments** `dq_report` has only 4 arguments: - `data`: You can provide
-any kind of file format (string) or even a pandas DataFrame (df). It reads
-parquet, csv, feather, arrow, all kinds of file formats straight from disk. You
-just have to tell it the path to the file and the name of the file. - `target`:
+pandas_dq has a very simple API with just two modules to import: one will find
+data quality issues in your data and the other will fix it. Simple!
+**Arguments** `dq_report` has only 4 arguments: - `data`: You can provide any
+kind of file format (string) or even a pandas DataFrame (df). It reads parquet,
+csv, feather, arrow, all kinds of file formats straight from disk. You just
+have to tell it the path to the file and the name of the file. - `target`:
 default: `None`. Otherwise, it should be a string name representing the name of
 a column in df. You can leave it as `None` if you don't want any target related
-issues. - `csv_engine`: default is `pandas`. If you want to load your file
+issues. - `csv_engine`: default is `pandas`. If you want to load your CSV file
 using any other backend engine such as `arrow` or `parquet` please specify it
-here. - `verbose`: This has 2 possible states: - `0` summary report. Prints
-only the summary level data quality issues in the dataset. Great for managers.
-- `1` detailed report. Prints all the gory details behind each DQ issue in your
-dataset and what to do about them. Great for engineers. `Fix_DQ` has slightly
-more arguments: Caution: X_train and y_train in Fix_DQ must be pandas
-Dataframes or pandas Series. I have not tested it on numpy arrays. You can try
-your luck. - `quantile`: float (0.75): Define a threshold for IQR for outlier
-detection. Could be any float between 0 and 1. If quantile is set to `None`,
-then no outlier detection will take place. - `cat_fill_value`: string
-("missing"): Define a fill value for missing categories in your object or
-categorical variables. This is a global default for your entire dataset. I will
-try to change it to a dictionary so that you can specify different values for
-different columns. - `num_fill_value`: integer or float (999): Define a fill
-value for missing numbers in your integer or float variables. This is a global
-default for your entire dataset. I will try to change it to a dictionary so
-that you can specify different values for different columns. -
-`rare_threshold`: float (0.05): Define a threshold for rare categories. If a
-certain category in a column is less 5% (say) of samples, then it will
-considered rare. All rare categories will be merged with a category value
-called "Rare". - `correlation_threshold`: float (0.8): Define a correlation
-limit. Anything above this limit, the variable will be dropped.
+here. This option only impacts CSV files. - `verbose`: This has 2 possible
+states: - `0` summary report. Prints only the summary level data quality issues
+in the dataset. Great for managers. - `1` detailed report. Prints all the gory
+details behind each DQ issue in your dataset and what to do about them. Great
+for engineers. `Fix_DQ` has slightly more arguments: Caution: X_train and
+y_train in Fix_DQ must be pandas Dataframes or pandas Series. I have not tested
+it on numpy arrays. You can try your luck. - `quantile`: float (0.75): Define a
+threshold for IQR for outlier detection. Could be any float between 0 and 1. If
+quantile is set to `None`, then no outlier detection will take place. -
+`cat_fill_value`: string ("missing") or a dictionary: Define a fill value for
+missing categories in your object or categorical variables. This is a global
+default for your entire dataset. You can also give a dictionary where you
+specify different fill values for different columns. - `num_fill_value`:
+integer (99) or float value (999.0) or a dictionary: Define a fill value for
+missing numbers in your integer or float variables. This is a global default
+for your entire dataset. You can also give a dictionary where you specify
+different fill values for different columns. - `rare_threshold`: float (0.05):
+Define a threshold for rare categories. If a certain category in a column is
+less than say 5% (0.05) of samples, then it will be considered rare. All rare
+categories in that column will be merged under a new category named "Rare". -
+`correlation_threshold`: float (0.8): Define a correlation limit. Anything
+above this limit, if two variables are correlated, one of them will be dropped.
+The program will tell you which variable is being dropped. You can switch the
+sequence of variables in your dataset if you want the one or other dropped.
 ## Maintainers * [@AutoViML](https://github.com/AutoViML) ## Contributing See
 [the contributing file](CONTRIBUTING.md)! PRs accepted. ## License Apache
 License 2.0 Â© 2020 Ram Seshadri ## Note of Gratitude This libray would not
 have been possible without the help of ChatGPT and Bard. This library is
 dedicated to the thousands of people who worked to create LLM's. ## DISCLAIMER
 This project is not an official Google project. It is not supported by Google
 and Google specifically disclaims all warranties as to its quality,
```

### Comparing `pandas_dq-1.4/README.md` & `pandas_dq-1.5/README.md`

 * *Files 14% similar despite different names*

```diff
@@ -23,29 +23,29 @@
 ## Uses
 `pandas_dq` has two important modules: `dq_report` and `Fix_DQ`. 
 
 ### 1.  dq_report function
 
 ![dq_report_code](./images/find_dq_screenshot.png)
 
-<p>`dq_report` is a function that is probably the most popular way to use pandas_dq and it performs following data quality analysis steps:
+<p>`dq_report` is a function that is the most popular way to use pandas_dq and it performs following data quality analysis steps:
 <ol>
 <li>It detects missing values and suggests to impute them with mean, median, mode, or a constant value.</li>
 <li>It identifies rare categories and suggests to group them into a single category or drop them.</li>
 <li>It finds infinite values and suggests to replace them with NaN or a large value.</li>
 <li>It detects mixed data types and suggests to convert them to a single type or split them into multiple columns.</li>
 <li>It detects outliers and suggests to remove them or use robust statistics.</li>
 <li>It detects high cardinality features and suggests to reduce them using encoding techniques or feature selection methods.</li>
 <li>It detects highly correlated features and suggests to drop one of them or use dimensionality reduction techniques.</li>
 <li>It detects duplicate rows and columns and suggests to drop them or keep only one copy.</li>
 <li>It detects skewed distributions and suggests to apply transformations or scaling techniques. </li>
 <li>It detects imbalanced classes and suggests to use resampling techniques or class weights. </li>
 <li>It detects feature leakage and suggests to avoid using features that are not available at prediction time. </li>
 </ol>
-
+Notice that for large datasets, this report generation may take time. So please be patient while it analyzes your dataset!
 
 ### 2.  Fix_DQ class: a scikit_learn transformer which can detect data quality issues and clean them all in one line of code
 
 ![fix_dq](./images/fix_dq_screenshot.png)
 
 <p>`Fix_DQ` is a great way to clean an entire train data set and apply the same steps in an MLOps pipeline to a test dataset.  `Fix_DQ` can be used to detect most issues in your data (similar to dq_report but without the target related steps) in one step (during `fit` method). This transformer can then be saved (or "pickled") for applying the same steps on test data either at the same time or later.<br>
 
@@ -109,35 +109,34 @@
 It prints out a data quality report like this:
 
 ![dq_report](./images/dq_report_screenshot.png)
 
 ## API
 
 <p>
-pandas_dq has a very simple API with the following inputs. You need to create a sklearn-compatible transformer pipeline object by importing Fix_DQ from pandas_dq library. <p>
-Once you import it, you can define the object by giving several options such as:
+pandas_dq has a very simple API with just two modules to import: one will find data quality issues in your data and the other will fix it. Simple!
 
 **Arguments**
 
 `dq_report` has only 4 arguments:
 - `data`: You can provide any kind of file format (string) or even a pandas DataFrame (df). It reads parquet, csv, feather, arrow, all kinds of file formats straight from disk. You just have to tell it the path to the file and the name of the file.
 - `target`: default: `None`. Otherwise, it should be a string name representing the name of a column in df. You can leave it as `None` if you don't want any target related issues.
-- `csv_engine`: default is `pandas`. If you want to load your file using any other backend engine such as `arrow` or `parquet` please specify it here.
+- `csv_engine`: default is `pandas`. If you want to load your CSV file using any other backend engine such as `arrow` or `parquet` please specify it here. This option only impacts CSV files.
 - `verbose`: This has 2 possible states:
   - `0` summary report. Prints only the summary level data quality issues in the dataset. Great for managers.
   - `1` detailed report. Prints all the gory details behind each DQ issue in your dataset and what to do about them. Great for engineers.
 
 `Fix_DQ` has slightly more arguments:
 <b>Caution:</b> X_train and y_train in Fix_DQ must be pandas Dataframes or pandas Series. I have not tested it on numpy arrays. You can try your luck.
 
 - `quantile`: float (0.75): Define a threshold for IQR for outlier detection. Could be any float between 0 and 1. If quantile is set to `None`, then no outlier detection will take place.
-- `cat_fill_value`: string ("missing"): Define a fill value for missing categories in your object or categorical variables. This is a global default for your entire dataset. I will try to change it to a dictionary so that you can specify different values for different columns.
-- `num_fill_value`: integer or float (999): Define a fill value for missing numbers in your integer or float variables.  This is a global default for your entire dataset. I will try to change it to a dictionary so that you can specify different values for different columns.
-- `rare_threshold`: float (0.05):  Define a threshold for rare categories. If a certain category in a column is less 5% (say) of samples, then it will considered rare. All rare categories will be merged with a category value called "Rare". 
-- `correlation_threshold`: float (0.8): Define a correlation limit. Anything above this limit, the variable will be dropped. 
+- `cat_fill_value`: string ("missing") or a dictionary: Define a fill value for missing categories in your object or categorical variables. This is a global default for your entire dataset. You can also give a dictionary where you specify different fill values for different columns.
+- `num_fill_value`: integer (99) or float value (999.0) or a dictionary: Define a fill value for missing numbers in your integer or float variables.  This is a global default for your entire dataset. You can also give a dictionary where you specify different fill values for different columns.
+- `rare_threshold`: float (0.05):  Define a threshold for rare categories. If a certain category in a column is less than say 5% (0.05) of samples, then it will be considered rare. All rare categories in that column will be merged under a new category named "Rare". 
+- `correlation_threshold`: float (0.8): Define a correlation limit. Anything above this limit, if two variables are correlated, one of them will be dropped. The program will tell you which variable is being dropped. You can switch the sequence of variables in your dataset if you want the one or other dropped.
 <p>
 
 ## Maintainers
 
 * [@AutoViML](https://github.com/AutoViML)
 
 ## Contributing
```

#### html2text {}

```diff
@@ -10,16 +10,16 @@
     * License
 ## Introduction ### What is pandas_dq? `pandas_dq` is a new python library for
 automatically cleaning your dirty dataset using pandas scikit_learn functions.
 You can analyze your dataset and fix them - all in a single line of code! !
 [pandas_dq](./images/pandas_dq_logo.png) ## Uses `pandas_dq` has two important
 modules: `dq_report` and `Fix_DQ`. ### 1. dq_report function ![dq_report_code]
 (./images/find_dq_screenshot.png)
-`dq_report` is a function that is probably the most popular way to use
-pandas_dq and it performs following data quality analysis steps:
+`dq_report` is a function that is the most popular way to use pandas_dq and it
+performs following data quality analysis steps:
    1. It detects missing values and suggests to impute them with mean, median,
       mode, or a constant value.
    2. It identifies rare categories and suggests to group them into a single
       category or drop them.
    3. It finds infinite values and suggests to replace them with NaN or a large
       value.
    4. It detects mixed data types and suggests to convert them to a single type
@@ -33,17 +33,18 @@
       only one copy.
    9. It detects skewed distributions and suggests to apply transformations or
       scaling techniques.
   10. It detects imbalanced classes and suggests to use resampling techniques
       or class weights.
   11. It detects feature leakage and suggests to avoid using features that are
       not available at prediction time.
-### 2. Fix_DQ class: a scikit_learn transformer which can detect data quality
-issues and clean them all in one line of code ![fix_dq](./images/
-fix_dq_screenshot.png)
+Notice that for large datasets, this report generation may take time. So please
+be patient while it analyzes your dataset! ### 2. Fix_DQ class: a scikit_learn
+transformer which can detect data quality issues and clean them all in one line
+of code ![fix_dq](./images/fix_dq_screenshot.png)
 `Fix_DQ` is a great way to clean an entire train data set and apply the same
 steps in an MLOps pipeline to a test dataset. `Fix_DQ` can be used to detect
 most issues in your data (similar to dq_report but without the target related
 steps) in one step (during `fit` method). This transformer can then be saved
 (or "pickled") for applying the same steps on test data either at the same time
 or later.
 ### How can we use Fix_DQ in GridSearchCV to find the best model pipeline?
@@ -69,47 +70,48 @@
 the transformer on X_train and transform it X_train_transformed =
 fdq.fit_transform(X_train) # Transform X_test using the fitted transformer
 X_test_transformed = fdq.transform(X_test) ``` ### if you are not using the
 Transformer, you can simply call the function, dq_report ``` from pandas_dq
 import dq_report dq_report(data, target=target, csv_engine="pandas", verbose=1)
 ``` It prints out a data quality report like this: ![dq_report](./images/
 dq_report_screenshot.png) ## API
-pandas_dq has a very simple API with the following inputs. You need to create a
-sklearn-compatible transformer pipeline object by importing Fix_DQ from
-pandas_dq library.
-Once you import it, you can define the object by giving several options such
-as: **Arguments** `dq_report` has only 4 arguments: - `data`: You can provide
-any kind of file format (string) or even a pandas DataFrame (df). It reads
-parquet, csv, feather, arrow, all kinds of file formats straight from disk. You
-just have to tell it the path to the file and the name of the file. - `target`:
+pandas_dq has a very simple API with just two modules to import: one will find
+data quality issues in your data and the other will fix it. Simple!
+**Arguments** `dq_report` has only 4 arguments: - `data`: You can provide any
+kind of file format (string) or even a pandas DataFrame (df). It reads parquet,
+csv, feather, arrow, all kinds of file formats straight from disk. You just
+have to tell it the path to the file and the name of the file. - `target`:
 default: `None`. Otherwise, it should be a string name representing the name of
 a column in df. You can leave it as `None` if you don't want any target related
-issues. - `csv_engine`: default is `pandas`. If you want to load your file
+issues. - `csv_engine`: default is `pandas`. If you want to load your CSV file
 using any other backend engine such as `arrow` or `parquet` please specify it
-here. - `verbose`: This has 2 possible states: - `0` summary report. Prints
-only the summary level data quality issues in the dataset. Great for managers.
-- `1` detailed report. Prints all the gory details behind each DQ issue in your
-dataset and what to do about them. Great for engineers. `Fix_DQ` has slightly
-more arguments: Caution: X_train and y_train in Fix_DQ must be pandas
-Dataframes or pandas Series. I have not tested it on numpy arrays. You can try
-your luck. - `quantile`: float (0.75): Define a threshold for IQR for outlier
-detection. Could be any float between 0 and 1. If quantile is set to `None`,
-then no outlier detection will take place. - `cat_fill_value`: string
-("missing"): Define a fill value for missing categories in your object or
-categorical variables. This is a global default for your entire dataset. I will
-try to change it to a dictionary so that you can specify different values for
-different columns. - `num_fill_value`: integer or float (999): Define a fill
-value for missing numbers in your integer or float variables. This is a global
-default for your entire dataset. I will try to change it to a dictionary so
-that you can specify different values for different columns. -
-`rare_threshold`: float (0.05): Define a threshold for rare categories. If a
-certain category in a column is less 5% (say) of samples, then it will
-considered rare. All rare categories will be merged with a category value
-called "Rare". - `correlation_threshold`: float (0.8): Define a correlation
-limit. Anything above this limit, the variable will be dropped.
+here. This option only impacts CSV files. - `verbose`: This has 2 possible
+states: - `0` summary report. Prints only the summary level data quality issues
+in the dataset. Great for managers. - `1` detailed report. Prints all the gory
+details behind each DQ issue in your dataset and what to do about them. Great
+for engineers. `Fix_DQ` has slightly more arguments: Caution: X_train and
+y_train in Fix_DQ must be pandas Dataframes or pandas Series. I have not tested
+it on numpy arrays. You can try your luck. - `quantile`: float (0.75): Define a
+threshold for IQR for outlier detection. Could be any float between 0 and 1. If
+quantile is set to `None`, then no outlier detection will take place. -
+`cat_fill_value`: string ("missing") or a dictionary: Define a fill value for
+missing categories in your object or categorical variables. This is a global
+default for your entire dataset. You can also give a dictionary where you
+specify different fill values for different columns. - `num_fill_value`:
+integer (99) or float value (999.0) or a dictionary: Define a fill value for
+missing numbers in your integer or float variables. This is a global default
+for your entire dataset. You can also give a dictionary where you specify
+different fill values for different columns. - `rare_threshold`: float (0.05):
+Define a threshold for rare categories. If a certain category in a column is
+less than say 5% (0.05) of samples, then it will be considered rare. All rare
+categories in that column will be merged under a new category named "Rare". -
+`correlation_threshold`: float (0.8): Define a correlation limit. Anything
+above this limit, if two variables are correlated, one of them will be dropped.
+The program will tell you which variable is being dropped. You can switch the
+sequence of variables in your dataset if you want the one or other dropped.
 ## Maintainers * [@AutoViML](https://github.com/AutoViML) ## Contributing See
 [the contributing file](CONTRIBUTING.md)! PRs accepted. ## License Apache
 License 2.0 Â© 2020 Ram Seshadri ## Note of Gratitude This libray would not
 have been possible without the help of ChatGPT and Bard. This library is
 dedicated to the thousands of people who worked to create LLM's. ## DISCLAIMER
 This project is not an official Google project. It is not supported by Google
 and Google specifically disclaims all warranties as to its quality,
```

### Comparing `pandas_dq-1.4/pandas_dq.egg-info/PKG-INFO` & `pandas_dq-1.5/pandas_dq.egg-info/PKG-INFO`

 * *Files 5% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pandas-dq
-Version: 1.4
+Version: 1.5
 Summary: Clean your data using a scikit-learn transformer in a single line of code
 Home-page: https://github.com/AutoViML/pandas_dq
 Author: Ram Seshadri
 License: Apache License 2.0
 Description: # pandas_dq
         Analyze and clean your data in a single line of code with a Scikit-Learn compatible Transformer.
         
@@ -30,29 +30,29 @@
         ## Uses
         `pandas_dq` has two important modules: `dq_report` and `Fix_DQ`. 
         
         ### 1.  dq_report function
         
         ![dq_report_code](./images/find_dq_screenshot.png)
         
-        <p>`dq_report` is a function that is probably the most popular way to use pandas_dq and it performs following data quality analysis steps:
+        <p>`dq_report` is a function that is the most popular way to use pandas_dq and it performs following data quality analysis steps:
         <ol>
         <li>It detects missing values and suggests to impute them with mean, median, mode, or a constant value.</li>
         <li>It identifies rare categories and suggests to group them into a single category or drop them.</li>
         <li>It finds infinite values and suggests to replace them with NaN or a large value.</li>
         <li>It detects mixed data types and suggests to convert them to a single type or split them into multiple columns.</li>
         <li>It detects outliers and suggests to remove them or use robust statistics.</li>
         <li>It detects high cardinality features and suggests to reduce them using encoding techniques or feature selection methods.</li>
         <li>It detects highly correlated features and suggests to drop one of them or use dimensionality reduction techniques.</li>
         <li>It detects duplicate rows and columns and suggests to drop them or keep only one copy.</li>
         <li>It detects skewed distributions and suggests to apply transformations or scaling techniques. </li>
         <li>It detects imbalanced classes and suggests to use resampling techniques or class weights. </li>
         <li>It detects feature leakage and suggests to avoid using features that are not available at prediction time. </li>
         </ol>
-        
+        Notice that for large datasets, this report generation may take time. So please be patient while it analyzes your dataset!
         
         ### 2.  Fix_DQ class: a scikit_learn transformer which can detect data quality issues and clean them all in one line of code
         
         ![fix_dq](./images/fix_dq_screenshot.png)
         
         <p>`Fix_DQ` is a great way to clean an entire train data set and apply the same steps in an MLOps pipeline to a test dataset.  `Fix_DQ` can be used to detect most issues in your data (similar to dq_report but without the target related steps) in one step (during `fit` method). This transformer can then be saved (or "pickled") for applying the same steps on test data either at the same time or later.<br>
         
@@ -116,35 +116,34 @@
         It prints out a data quality report like this:
         
         ![dq_report](./images/dq_report_screenshot.png)
         
         ## API
         
         <p>
-        pandas_dq has a very simple API with the following inputs. You need to create a sklearn-compatible transformer pipeline object by importing Fix_DQ from pandas_dq library. <p>
-        Once you import it, you can define the object by giving several options such as:
+        pandas_dq has a very simple API with just two modules to import: one will find data quality issues in your data and the other will fix it. Simple!
         
         **Arguments**
         
         `dq_report` has only 4 arguments:
         - `data`: You can provide any kind of file format (string) or even a pandas DataFrame (df). It reads parquet, csv, feather, arrow, all kinds of file formats straight from disk. You just have to tell it the path to the file and the name of the file.
         - `target`: default: `None`. Otherwise, it should be a string name representing the name of a column in df. You can leave it as `None` if you don't want any target related issues.
-        - `csv_engine`: default is `pandas`. If you want to load your file using any other backend engine such as `arrow` or `parquet` please specify it here.
+        - `csv_engine`: default is `pandas`. If you want to load your CSV file using any other backend engine such as `arrow` or `parquet` please specify it here. This option only impacts CSV files.
         - `verbose`: This has 2 possible states:
           - `0` summary report. Prints only the summary level data quality issues in the dataset. Great for managers.
           - `1` detailed report. Prints all the gory details behind each DQ issue in your dataset and what to do about them. Great for engineers.
         
         `Fix_DQ` has slightly more arguments:
         <b>Caution:</b> X_train and y_train in Fix_DQ must be pandas Dataframes or pandas Series. I have not tested it on numpy arrays. You can try your luck.
         
         - `quantile`: float (0.75): Define a threshold for IQR for outlier detection. Could be any float between 0 and 1. If quantile is set to `None`, then no outlier detection will take place.
-        - `cat_fill_value`: string ("missing"): Define a fill value for missing categories in your object or categorical variables. This is a global default for your entire dataset. I will try to change it to a dictionary so that you can specify different values for different columns.
-        - `num_fill_value`: integer or float (999): Define a fill value for missing numbers in your integer or float variables.  This is a global default for your entire dataset. I will try to change it to a dictionary so that you can specify different values for different columns.
-        - `rare_threshold`: float (0.05):  Define a threshold for rare categories. If a certain category in a column is less 5% (say) of samples, then it will considered rare. All rare categories will be merged with a category value called "Rare". 
-        - `correlation_threshold`: float (0.8): Define a correlation limit. Anything above this limit, the variable will be dropped. 
+        - `cat_fill_value`: string ("missing") or a dictionary: Define a fill value for missing categories in your object or categorical variables. This is a global default for your entire dataset. You can also give a dictionary where you specify different fill values for different columns.
+        - `num_fill_value`: integer (99) or float value (999.0) or a dictionary: Define a fill value for missing numbers in your integer or float variables.  This is a global default for your entire dataset. You can also give a dictionary where you specify different fill values for different columns.
+        - `rare_threshold`: float (0.05):  Define a threshold for rare categories. If a certain category in a column is less than say 5% (0.05) of samples, then it will be considered rare. All rare categories in that column will be merged under a new category named "Rare". 
+        - `correlation_threshold`: float (0.8): Define a correlation limit. Anything above this limit, if two variables are correlated, one of them will be dropped. The program will tell you which variable is being dropped. You can switch the sequence of variables in your dataset if you want the one or other dropped.
         <p>
         
         ## Maintainers
         
         * [@AutoViML](https://github.com/AutoViML)
         
         ## Contributing
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: pandas-dq Version: 1.4 Summary: Clean your data
+Metadata-Version: 2.1 Name: pandas-dq Version: 1.5 Summary: Clean your data
 using a scikit-learn transformer in a single line of code Home-page: https://
 github.com/AutoViML/pandas_dq Author: Ram Seshadri License: Apache License 2.0
 Description: # pandas_dq Analyze and clean your data in a single line of code
 with a Scikit-Learn compatible Transformer. # Table of Contents
     * What_is_pandas_dq
     * How_to_use_pandas_dq
     * How_to_install_pandas_dq
@@ -13,16 +13,16 @@
     * License
 ## Introduction ### What is pandas_dq? `pandas_dq` is a new python library for
 automatically cleaning your dirty dataset using pandas scikit_learn functions.
 You can analyze your dataset and fix them - all in a single line of code! !
 [pandas_dq](./images/pandas_dq_logo.png) ## Uses `pandas_dq` has two important
 modules: `dq_report` and `Fix_DQ`. ### 1. dq_report function ![dq_report_code]
 (./images/find_dq_screenshot.png)
-`dq_report` is a function that is probably the most popular way to use
-pandas_dq and it performs following data quality analysis steps:
+`dq_report` is a function that is the most popular way to use pandas_dq and it
+performs following data quality analysis steps:
    1. It detects missing values and suggests to impute them with mean, median,
       mode, or a constant value.
    2. It identifies rare categories and suggests to group them into a single
       category or drop them.
    3. It finds infinite values and suggests to replace them with NaN or a large
       value.
    4. It detects mixed data types and suggests to convert them to a single type
@@ -36,17 +36,18 @@
       only one copy.
    9. It detects skewed distributions and suggests to apply transformations or
       scaling techniques.
   10. It detects imbalanced classes and suggests to use resampling techniques
       or class weights.
   11. It detects feature leakage and suggests to avoid using features that are
       not available at prediction time.
-### 2. Fix_DQ class: a scikit_learn transformer which can detect data quality
-issues and clean them all in one line of code ![fix_dq](./images/
-fix_dq_screenshot.png)
+Notice that for large datasets, this report generation may take time. So please
+be patient while it analyzes your dataset! ### 2. Fix_DQ class: a scikit_learn
+transformer which can detect data quality issues and clean them all in one line
+of code ![fix_dq](./images/fix_dq_screenshot.png)
 `Fix_DQ` is a great way to clean an entire train data set and apply the same
 steps in an MLOps pipeline to a test dataset. `Fix_DQ` can be used to detect
 most issues in your data (similar to dq_report but without the target related
 steps) in one step (during `fit` method). This transformer can then be saved
 (or "pickled") for applying the same steps on test data either at the same time
 or later.
 ### How can we use Fix_DQ in GridSearchCV to find the best model pipeline?
@@ -72,47 +73,48 @@
 the transformer on X_train and transform it X_train_transformed =
 fdq.fit_transform(X_train) # Transform X_test using the fitted transformer
 X_test_transformed = fdq.transform(X_test) ``` ### if you are not using the
 Transformer, you can simply call the function, dq_report ``` from pandas_dq
 import dq_report dq_report(data, target=target, csv_engine="pandas", verbose=1)
 ``` It prints out a data quality report like this: ![dq_report](./images/
 dq_report_screenshot.png) ## API
-pandas_dq has a very simple API with the following inputs. You need to create a
-sklearn-compatible transformer pipeline object by importing Fix_DQ from
-pandas_dq library.
-Once you import it, you can define the object by giving several options such
-as: **Arguments** `dq_report` has only 4 arguments: - `data`: You can provide
-any kind of file format (string) or even a pandas DataFrame (df). It reads
-parquet, csv, feather, arrow, all kinds of file formats straight from disk. You
-just have to tell it the path to the file and the name of the file. - `target`:
+pandas_dq has a very simple API with just two modules to import: one will find
+data quality issues in your data and the other will fix it. Simple!
+**Arguments** `dq_report` has only 4 arguments: - `data`: You can provide any
+kind of file format (string) or even a pandas DataFrame (df). It reads parquet,
+csv, feather, arrow, all kinds of file formats straight from disk. You just
+have to tell it the path to the file and the name of the file. - `target`:
 default: `None`. Otherwise, it should be a string name representing the name of
 a column in df. You can leave it as `None` if you don't want any target related
-issues. - `csv_engine`: default is `pandas`. If you want to load your file
+issues. - `csv_engine`: default is `pandas`. If you want to load your CSV file
 using any other backend engine such as `arrow` or `parquet` please specify it
-here. - `verbose`: This has 2 possible states: - `0` summary report. Prints
-only the summary level data quality issues in the dataset. Great for managers.
-- `1` detailed report. Prints all the gory details behind each DQ issue in your
-dataset and what to do about them. Great for engineers. `Fix_DQ` has slightly
-more arguments: Caution: X_train and y_train in Fix_DQ must be pandas
-Dataframes or pandas Series. I have not tested it on numpy arrays. You can try
-your luck. - `quantile`: float (0.75): Define a threshold for IQR for outlier
-detection. Could be any float between 0 and 1. If quantile is set to `None`,
-then no outlier detection will take place. - `cat_fill_value`: string
-("missing"): Define a fill value for missing categories in your object or
-categorical variables. This is a global default for your entire dataset. I will
-try to change it to a dictionary so that you can specify different values for
-different columns. - `num_fill_value`: integer or float (999): Define a fill
-value for missing numbers in your integer or float variables. This is a global
-default for your entire dataset. I will try to change it to a dictionary so
-that you can specify different values for different columns. -
-`rare_threshold`: float (0.05): Define a threshold for rare categories. If a
-certain category in a column is less 5% (say) of samples, then it will
-considered rare. All rare categories will be merged with a category value
-called "Rare". - `correlation_threshold`: float (0.8): Define a correlation
-limit. Anything above this limit, the variable will be dropped.
+here. This option only impacts CSV files. - `verbose`: This has 2 possible
+states: - `0` summary report. Prints only the summary level data quality issues
+in the dataset. Great for managers. - `1` detailed report. Prints all the gory
+details behind each DQ issue in your dataset and what to do about them. Great
+for engineers. `Fix_DQ` has slightly more arguments: Caution: X_train and
+y_train in Fix_DQ must be pandas Dataframes or pandas Series. I have not tested
+it on numpy arrays. You can try your luck. - `quantile`: float (0.75): Define a
+threshold for IQR for outlier detection. Could be any float between 0 and 1. If
+quantile is set to `None`, then no outlier detection will take place. -
+`cat_fill_value`: string ("missing") or a dictionary: Define a fill value for
+missing categories in your object or categorical variables. This is a global
+default for your entire dataset. You can also give a dictionary where you
+specify different fill values for different columns. - `num_fill_value`:
+integer (99) or float value (999.0) or a dictionary: Define a fill value for
+missing numbers in your integer or float variables. This is a global default
+for your entire dataset. You can also give a dictionary where you specify
+different fill values for different columns. - `rare_threshold`: float (0.05):
+Define a threshold for rare categories. If a certain category in a column is
+less than say 5% (0.05) of samples, then it will be considered rare. All rare
+categories in that column will be merged under a new category named "Rare". -
+`correlation_threshold`: float (0.8): Define a correlation limit. Anything
+above this limit, if two variables are correlated, one of them will be dropped.
+The program will tell you which variable is being dropped. You can switch the
+sequence of variables in your dataset if you want the one or other dropped.
 ## Maintainers * [@AutoViML](https://github.com/AutoViML) ## Contributing See
 [the contributing file](CONTRIBUTING.md)! PRs accepted. ## License Apache
 License 2.0 Â© 2020 Ram Seshadri ## Note of Gratitude This libray would not
 have been possible without the help of ChatGPT and Bard. This library is
 dedicated to the thousands of people who worked to create LLM's. ## DISCLAIMER
 This project is not an official Google project. It is not supported by Google
 and Google specifically disclaims all warranties as to its quality,
```

### Comparing `pandas_dq-1.4/pandas_dq.py` & `pandas_dq-1.5/pandas_dq.py`

 * *Files 2% similar despite different names*

```diff
@@ -36,16 +36,14 @@
 #######  a quick and dirty data cleaning library. Since they couldn't find me any good ones,
 #######  I decided to create a simple quick and dirty data cleaning library using ChatGPT and Bard.
 #######  I dedicate this library to all the 1000's of researchers who worked to create LLM's.
 ############################################################################################
 # Define a function to print data cleaning suggestions
 # Import pandas and numpy libraries
 import pandas as pd
-import polars as pl
-import pyarrow as pa
 import numpy as np
 import copy
 import os
 # Define a function to print data quality report and suggestions to clean data
 def dq_report(data, target=None, csv_engine="pandas", verbose=0):
     """
     This is a data quality reporting tool that accepts any kind of file format as a filename or as a 
@@ -72,17 +70,19 @@
         # Load the file into a pandas dataframe based on the extension
         if ext == ".csv":
             if csv_engine == 'pandas':
                 # Upload the data file into Pandas
                 df = pd.read_csv(data, nrows=1000000)
             elif csv_engine == 'polars':
                 # Upload the data file into Polars
+                import polars as pl
                 df_polars = pl.read_csv(data, nrows=1000000)
             elif csv_engine == 'parquet':
                 # Upload the data file into Parquet
+                import pyarrow as pa
                 df_parquet = pa.read_table(data)
         elif ext == ".parquet":
             df = pd.read_parquet(data)
         elif ext in [".feather", ".arrow"]:
             df = pd.read_feather(data)
         else:
             print("Unsupported file format. Please use CSV, parquet, feather or arrow.")
@@ -429,46 +429,76 @@
         if not isinstance(X, pd.DataFrame):
             # Convert X to a pandas DataFrame
             X = pd.DataFrame(X)
             
         X = copy.deepcopy(X)
         
         # Get the numerical columns
-        num_cols = X.select_dtypes(include=["int", "float"]).columns.tolist()
+        num_cols = X.select_dtypes(include=[ "float"]).columns.tolist()
         
-        # Loop through each numerical column
+        # Loop through each float column
         for col in num_cols:
             # Check if the column has an upper bound calculated in the fit method
             if col in self.upper_bounds_:
                 # Cap the outliers using the upper bound
                 X[col] = np.where(X[col] > self.upper_bounds_[col], self.upper_bounds_[col], X[col])
+            else:
+                # Just print a message and don't cap the outliers in that column
+                print(f"No cap value found for column {col}. Continue...")                
         
         # Return the DataFrame with capped outliers
         return X
     
     # Define a function to impute the missing values in categorical and numerical columns using the constant values
     def impute_missing(self, X):
+        """
+        ### impute_missing can fill missing value using a global default value or a 
+        ### dictionary of fill values for each column and apply that fill value to each column.
+        """
         # Check if X is a pandas DataFrame
         if not isinstance(X, pd.DataFrame):
             # Convert X to a pandas DataFrame
             X = pd.DataFrame(X)
             
         X = copy.deepcopy(X)
 
         # Get the categorical columns
         cat_cols = X.select_dtypes(include=["object", "category"]).columns.tolist()
         
         # Get the numerical columns
         num_cols = X.select_dtypes(include=["int", "float"]).columns.tolist()
         
         # Impute the missing values in categorical columns with the cat_fill_value
-        X[cat_cols] = X[cat_cols].fillna(self.cat_fill_value)
+        # Loop through the columns of cat_cols
+        for col in cat_cols:
+            # Check if the column is in the fill_values dictionary
+            if isinstance(self.cat_fill_value, dict):
+                if col in self.cat_fill_value:
+                    # Impute the missing values in the column with the corresponding fill value
+                    X[col] = X[[col]].fillna(self.cat_fill_value[col]).values
+                else:
+                    ### use a default value for that column since it is not specified
+                    X[col] = X[[col]].fillna("missing").values
+            else:
+                ### use a global default value for all columns
+                X[col] = X[[col]].fillna(self.cat_fill_value).values
         
         # Impute the missing values in numerical columns with the num_fill_value
-        X[num_cols] = X[num_cols].fillna(self.num_fill_value)
+        # Loop through the columns of num_cols
+        for col in num_cols:
+            # Check if the column is in the fill_values dictionary
+            if isinstance(self.num_fill_value, dict):
+                if col in self.num_fill_value:
+                    # Impute the missing values in the column with the corresponding fill value
+                    X[col] = X[[col]].fillna(self.num_fill_value[col]).values
+                else:
+                    ### use a default value for that column since it is not specified
+                    X[col] = X[[col]].fillna(-999).values
+            else:
+                X[col] = X[[col]].fillna(self.num_fill_value).values
         
         # Return the DataFrame with imputed missing values
         return X
     
     # Define a function to identify rare categories and group them into a single category
     def group_rare_categories(self, X):
         # Check if X is a pandas DataFrame
@@ -519,36 +549,36 @@
         # Check if X is a pandas DataFrame
         if not isinstance(X, pd.DataFrame):
             # Convert X to a pandas DataFrame
             X = pd.DataFrame(X)
         
         # Drop duplicate rows
         dup_rows = X.duplicated().sum()
-        X = X.drop_duplicates()
         if dup_rows > 0:
-            print(f'Dropping {dup_rows} rows')
+            print(f'Alert: Dropping {dup_rows} rows can sometimes cause column data types to change to object. Double-check!')
+            X = X.drop_duplicates()
         
         # Drop duplicate columns
         dup_cols = X.T.duplicated().sum()
-        X = X.T.drop_duplicates().T
         if dup_cols > 0:
-            print(f'Dropping {dup_cols} cols')
+            print(f'Alert: Dropping {dup_cols} cols can sometimes cause column data types to change to object. Double-check!')
+            X = X.T.drop_duplicates().T
         
         # Return the DataFrame with no duplicates
         return X
     
     # Define a function to detect skewed distributions and apply a proper transformation to the column
     def transform_skewed(self, X):
         # Check if X is a pandas DataFrame
         if not isinstance(X, pd.DataFrame):
             # Convert X to a pandas DataFrame
             X = pd.DataFrame(X)
         
         # Get the numerical columns
-        num_cols = X.select_dtypes(include=["int", "float"]).columns.tolist()
+        num_cols = X.select_dtypes(include=["float"]).columns.tolist()
         
         # Define a threshold for skewness
         skew_threshold = 0.5
         
         # Loop through each numerical column
         for col in num_cols:
             # Find if a column transformer exists for this column
@@ -572,14 +602,15 @@
         # Check if X is a pandas DataFrame
         if not isinstance(X, pd.DataFrame):
             # Convert X to a pandas DataFrame
             X = pd.DataFrame(X)
         
         # Get the numerical columns
         num_cols = X.select_dtypes(include=["int", "float"]).columns.tolist()
+        float_cols = X.select_dtypes(include=["float"]).columns.tolist()
         
         # Detect highly correlated features
         self.drop_corr_cols_ = []
         correlation_matrix = X.corr().abs() # Get the absolute correlation matrix of numerical columns
         upper_triangle = correlation_matrix.where(np.triu(np.ones(correlation_matrix.shape), k=1).astype(bool)) # Get the upper triangle of the matrix
         high_corr_cols = [column for column in upper_triangle.columns if any(upper_triangle[column] > self.correlation_threshold)] # Get the columns with high correlation
         if len(high_corr_cols) > 0:
@@ -588,19 +619,30 @@
                     print(f"    Dropping {col} which has a high correlation with {upper_triangle[col][upper_triangle[col] > self.correlation_threshold].index.tolist()}")
         
         
         # Initialize an empty dictionary to store the upper bounds
         self.upper_bounds_ = {}
         
         # Loop through each numerical column
+        #### processing of quantiles is only for float columns or those in dict ###
         if self.quantile is None:
-            #### Don't do any processing is quantile is set to None ###
-            pass
+            ### you still need to calculate upper bounds needed capping for infinite values ##
+            base_quantile = 0.75
+            for col in float_cols:
+                # Get the third quartile
+                q3 = X[col].quantile(base_quantile)
+                # Get the interquartile range
+                iqr = X[col].quantile(base_quantile) - X[col].quantile(1 - base_quantile)
+                # Calculate the upper bound
+                upper_bound = q3 + 1.5 * iqr
+                # Store the upper bound in the dictionary
+                self.upper_bounds_[col] = upper_bound
         else:
-            for col in num_cols:
+            ### calculate upper bounds to cap outliers using quantile given ##
+            for col in float_cols:
                 # Get the third quartile
                 q3 = X[col].quantile(self.quantile)
                 # Get the interquartile range
                 iqr = X[col].quantile(self.quantile) - X[col].quantile(1 - self.quantile)
                 # Calculate the upper bound
                 upper_bound = q3 + 1.5 * iqr
                 # Store the upper bound in the dictionary
@@ -608,16 +650,16 @@
 
         # Initialize an empty dictionary to store the column transformers
         self.col_transformers_ = {}
         
         # Define a threshold for skewness
         skew_threshold = 0.5
         
-        # Loop through each numerical column
-        for col in num_cols:
+        # Loop through each float column
+        for col in float_cols:
             # Calculate the skewness of the column
             skewness = X[col].skew()
             # Check if the skewness is above the threshold
             if abs(skewness) > skew_threshold:
                 # Apply a log transformation if the column has positive values only
                 if X[col].min() > 0:
                     ### function transformer expects pandas series
@@ -650,15 +692,15 @@
     
     # Define the transform method that calls the cap_outliers and impute_missing functions on the input DataFrame
     def transform(self, X):
         # Check if X is a pandas DataFrame
         if not isinstance(X, pd.DataFrame):
             # Convert X to a pandas DataFrame
             X = pd.DataFrame(X)
-            
+        
         ### drop mixed data type columns from further processing ##
         if len(self.mixed_type_cols_) > 0:
             X = X.drop(self.mixed_type_cols_, axis=1)
             
         ### drop highly correlated columns from further processing ##
         if len(self.drop_corr_cols_) > 0:
             if len(left_subtract(self.drop_corr_cols_,self.mixed_type_cols_)) > 0:
@@ -667,34 +709,38 @@
                 extra_cols = left_subtract(self.mixed_type_cols_, self.drop_corr_cols_)
             if len(extra_cols) > 0:
                 X = X.drop(extra_cols, axis=1)
             
         # find duplicate columns and rows
         X = self.drop_duplicates(X)
         
-        # Call the cap_outliers function on X and assign it to a new variable 
-        capped_X = self.cap_outliers(X)
+        # Call the impute_missing function first and assign it to a new variable 
+        imputed_X = self.impute_missing(X)
+
+        if self.quantile is None:
+            #### Don't do any processing if quantile is set to None ###
+            capped_X = copy.deepcopy(imputed_X)
+        else:
+            # Call the cap_outliers function on X and assign it to a new variable 
+            capped_X = self.cap_outliers(imputed_X)
         
         # Call the replace_infinite function on capped_X and assign it to a new variable 
         infinite_X = self.replace_infinite(capped_X)
         
         # Call the group_rare_categories function on infinite_X and assign it to a new variable 
         rare_X = self.group_rare_categories(infinite_X)
         
         # Call the power transformer function on rare_X and assign it to a new variable 
-        power_X = self.transform_skewed(rare_X)
-        
-        # Call the impute_missing function on power_X and assign it to a new variable 
-        imputed_X = self.impute_missing(power_X)
-        
+        transformed_X = self.transform_skewed(rare_X)
+                
         # Return the transformed DataFrame
-        return imputed_X
+        return transformed_X
 
 ############################################################################################
 module_type = 'Running' if  __name__ == "__main__" else 'Imported'
-version_number =  '1.4'
+version_number =  '1.5'
 print(f"""{module_type} pandas_dq ({version_number}). Use fit and transform using:
 from pandas_dq import find_dq, Fix_DQ
 fdq = Fix_DQ(quantile=0.75, cat_fill_value="missing", num_fill_value=9999, 
                  rare_threshold=0.05, correlation_threshold=0.8)
 """)
 #################################################################################
```

