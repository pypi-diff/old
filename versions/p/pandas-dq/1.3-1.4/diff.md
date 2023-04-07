# Comparing `tmp/pandas_dq-1.3.tar.gz` & `tmp/pandas_dq-1.4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pandas_dq-1.3.tar", last modified: Thu Apr  6 13:45:48 2023, max compression
+gzip compressed data, was "pandas_dq-1.4.tar", last modified: Fri Apr  7 00:56:20 2023, max compression
```

## Comparing `pandas_dq-1.3.tar` & `pandas_dq-1.4.tar`

### file list

```diff
@@ -1,15 +1,15 @@
-drwxrwxrwx   0 ram       (1000) ram       (1000)        0 2023-04-06 13:45:48.149118 pandas_dq-1.3/
--rwxrwxrwx   0 ram       (1000) ram       (1000)    11357 2023-04-02 23:27:15.000000 pandas_dq-1.3/LICENSE
--rwxrwxrwx   0 ram       (1000) ram       (1000)      610 2022-04-07 23:06:53.000000 pandas_dq-1.3/MANIFEST.in
--rwxrwxrwx   0 ram       (1000) ram       (1000)     9263 2023-04-06 13:45:48.143108 pandas_dq-1.3/PKG-INFO
--rwxrwxrwx   0 ram       (1000) ram       (1000)     7600 2023-04-06 13:42:11.000000 pandas_dq-1.3/README.md
-drwxrwxrwx   0 ram       (1000) ram       (1000)        0 2023-04-06 13:45:48.108118 pandas_dq-1.3/pandas_dq.egg-info/
--rwxrwxrwx   0 ram       (1000) ram       (1000)     9263 2023-04-06 13:45:47.000000 pandas_dq-1.3/pandas_dq.egg-info/PKG-INFO
--rwxrwxrwx   0 ram       (1000) ram       (1000)      232 2023-04-06 13:45:47.000000 pandas_dq-1.3/pandas_dq.egg-info/SOURCES.txt
--rwxrwxrwx   0 ram       (1000) ram       (1000)        1 2023-04-06 13:45:47.000000 pandas_dq-1.3/pandas_dq.egg-info/dependency_links.txt
--rwxrwxrwx   0 ram       (1000) ram       (1000)       49 2023-04-06 13:45:47.000000 pandas_dq-1.3/pandas_dq.egg-info/requires.txt
--rwxrwxrwx   0 ram       (1000) ram       (1000)       10 2023-04-06 13:45:47.000000 pandas_dq-1.3/pandas_dq.egg-info/top_level.txt
--rwxrwxrwx   0 ram       (1000) ram       (1000)    36614 2023-04-06 13:37:47.000000 pandas_dq-1.3/pandas_dq.py
--rwxrwxrwx   0 ram       (1000) ram       (1000)       52 2023-04-03 00:50:45.000000 pandas_dq-1.3/requirements.txt
--rwxrwxrwx   0 ram       (1000) ram       (1000)       38 2023-04-06 13:45:48.152119 pandas_dq-1.3/setup.cfg
--rwxrwxrwx   0 ram       (1000) ram       (1000)      883 2023-04-06 12:40:45.000000 pandas_dq-1.3/setup.py
+drwxrwxrwx   0 ram       (1000) ram       (1000)        0 2023-04-07 00:56:20.876816 pandas_dq-1.4/
+-rwxrwxrwx   0 ram       (1000) ram       (1000)    11357 2023-04-02 23:27:15.000000 pandas_dq-1.4/LICENSE
+-rwxrwxrwx   0 ram       (1000) ram       (1000)      610 2022-04-07 23:06:53.000000 pandas_dq-1.4/MANIFEST.in
+-rwxrwxrwx   0 ram       (1000) ram       (1000)     9486 2023-04-07 00:56:20.861167 pandas_dq-1.4/PKG-INFO
+-rwxrwxrwx   0 ram       (1000) ram       (1000)     7807 2023-04-07 00:49:33.000000 pandas_dq-1.4/README.md
+drwxrwxrwx   0 ram       (1000) ram       (1000)        0 2023-04-07 00:56:20.845543 pandas_dq-1.4/pandas_dq.egg-info/
+-rwxrwxrwx   0 ram       (1000) ram       (1000)     9486 2023-04-07 00:56:20.000000 pandas_dq-1.4/pandas_dq.egg-info/PKG-INFO
+-rwxrwxrwx   0 ram       (1000) ram       (1000)      232 2023-04-07 00:56:20.000000 pandas_dq-1.4/pandas_dq.egg-info/SOURCES.txt
+-rwxrwxrwx   0 ram       (1000) ram       (1000)        1 2023-04-07 00:56:20.000000 pandas_dq-1.4/pandas_dq.egg-info/dependency_links.txt
+-rwxrwxrwx   0 ram       (1000) ram       (1000)       56 2023-04-07 00:56:20.000000 pandas_dq-1.4/pandas_dq.egg-info/requires.txt
+-rwxrwxrwx   0 ram       (1000) ram       (1000)       10 2023-04-07 00:56:20.000000 pandas_dq-1.4/pandas_dq.egg-info/top_level.txt
+-rwxrwxrwx   0 ram       (1000) ram       (1000)    37060 2023-04-07 00:30:01.000000 pandas_dq-1.4/pandas_dq.py
+-rwxrwxrwx   0 ram       (1000) ram       (1000)       60 2023-04-07 00:54:49.000000 pandas_dq-1.4/requirements.txt
+-rwxrwxrwx   0 ram       (1000) ram       (1000)       38 2023-04-07 00:56:20.876816 pandas_dq-1.4/setup.cfg
+-rwxrwxrwx   0 ram       (1000) ram       (1000)      902 2023-04-07 00:55:14.000000 pandas_dq-1.4/setup.py
```

### Comparing `pandas_dq-1.3/LICENSE` & `pandas_dq-1.4/LICENSE`

 * *Files identical despite different names*

### Comparing `pandas_dq-1.3/MANIFEST.in` & `pandas_dq-1.4/MANIFEST.in`

 * *Files identical despite different names*

### Comparing `pandas_dq-1.3/PKG-INFO` & `pandas_dq-1.4/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pandas_dq
-Version: 1.3
+Version: 1.4
 Summary: Clean your data using a scikit-learn transformer in a single line of code
 Home-page: https://github.com/AutoViML/pandas_dq
 Author: Ram Seshadri
 License: Apache License 2.0
 Description: # pandas_dq
         Analyze and clean your data in a single line of code with a Scikit-Learn compatible Transformer.
         
@@ -24,21 +24,21 @@
         ## Introduction
         ### What is pandas_dq?
         `pandas_dq` is a new python library for automatically cleaning your dirty dataset using pandas scikit_learn functions. You can analyze your dataset and fix them - all in a single line of code!
         
         ![pandas_dq](./images/pandas_dq_logo.png)
         
         ## Uses
-        `pandas_dq` has two important modules: `find_dq` and `Fix_DQ`. 
+        `pandas_dq` has two important modules: `dq_report` and `Fix_DQ`. 
         
-        ### 1.  find_dq function
+        ### 1.  dq_report function
         
-        ![find_dq](./images/find_dq_screenshot.png)
+        ![dq_report_code](./images/find_dq_screenshot.png)
         
-        <p>`find_dq` is a function that is probably the most popular way to use pandas_dq and it performs following data quality analysis steps:
+        <p>`dq_report` is a function that is probably the most popular way to use pandas_dq and it performs following data quality analysis steps:
         <ol>
         <li>It detects missing values and suggests to impute them with mean, median, mode, or a constant value.</li>
         <li>It identifies rare categories and suggests to group them into a single category or drop them.</li>
         <li>It finds infinite values and suggests to replace them with NaN or a large value.</li>
         <li>It detects mixed data types and suggests to convert them to a single type or split them into multiple columns.</li>
         <li>It detects outliers and suggests to remove them or use robust statistics.</li>
         <li>It detects high cardinality features and suggests to reduce them using encoding techniques or feature selection methods.</li>
@@ -50,22 +50,20 @@
         </ol>
         
         
         ### 2.  Fix_DQ class: a scikit_learn transformer which can detect data quality issues and clean them all in one line of code
         
         ![fix_dq](./images/fix_dq_screenshot.png)
         
-        <p>`Fix_DQ` is a great way to clean an entire train data set and apply the same steps in an MLOps pipeline to a test dataset.  `Fix_DQ` can be used to detect most issues in your data (similar to find_dq but without the target related steps) in one step (during `fit` method). This transformer can then be saved (or "pickled") for applying the same steps on test data either at the same time or later.<br>
+        <p>`Fix_DQ` is a great way to clean an entire train data set and apply the same steps in an MLOps pipeline to a test dataset.  `Fix_DQ` can be used to detect most issues in your data (similar to dq_report but without the target related steps) in one step (during `fit` method). This transformer can then be saved (or "pickled") for applying the same steps on test data either at the same time or later.<br>
         
         
         ###  How can we use Fix_DQ in GridSearchCV to find the best model pipeline?
         <p>This is another way to find the best data cleaning steps for your train data and then use the cleaned data in hyper parameter tuning using GridSearchCV or RandomizedSearchCV along with a LightGBM or an XGBoost or a scikit-learn model.<br>
         
-        
-        
         ## Install
         <p>
         
         **Prerequsites:**
         <ol>
         <li><b>pandas_dq is built using pandas, numpy and scikit-learn - that's all.</b> It should run on almost all Python3 Anaconda installations without additional installs. You won't have to import any special libraries.</li>
         </ol>
@@ -104,40 +102,44 @@
         # Fit the transformer on X_train and transform it
         X_train_transformed = fdq.fit_transform(X_train)
         
         # Transform X_test using the fitted transformer
         X_test_transformed = fdq.transform(X_test)
         ```
         
-        ### if you are not using the Transformer, you can simply call the function, find_dq
+        ### if you are not using the Transformer, you can simply call the function, dq_report
         
         ```
-        from pandas_dq import find_dq
-        find_dq(df, target=target, verbose=0)
+        from pandas_dq import dq_report
+        dq_report(data, target=target, csv_engine="pandas", verbose=1)
         ```
         
+        It prints out a data quality report like this:
+        
+        ![dq_report](./images/dq_report_screenshot.png)
+        
         ## API
         
         <p>
         pandas_dq has a very simple API with the following inputs. You need to create a sklearn-compatible transformer pipeline object by importing Fix_DQ from pandas_dq library. <p>
         Once you import it, you can define the object by giving several options such as:
         
         **Arguments**
         
-        <b>Caution:</b> X_train and y_train must be pandas Dataframes or pandas Series. I have not tested it on numpy arrays. You can try your luck.
-        
-        `find_dq` has only 3 arguments:
+        `dq_report` has only 4 arguments:
         - `data`: You can provide any kind of file format (string) or even a pandas DataFrame (df). It reads parquet, csv, feather, arrow, all kinds of file formats straight from disk. You just have to tell it the path to the file and the name of the file.
         - `target`: default: `None`. Otherwise, it should be a string name representing the name of a column in df. You can leave it as `None` if you don't want any target related issues.
         - `csv_engine`: default is `pandas`. If you want to load your file using any other backend engine such as `arrow` or `parquet` please specify it here.
-         - `verbose`: This has 2 possible states:
-          - `0` silent output. Great for running where it prints only high level data quality issues.
-          - `1` more verbiage. Great for knowing details behind each issue and what the suggestions are.
+        - `verbose`: This has 2 possible states:
+          - `0` summary report. Prints only the summary level data quality issues in the dataset. Great for managers.
+          - `1` detailed report. Prints all the gory details behind each DQ issue in your dataset and what to do about them. Great for engineers.
         
         `Fix_DQ` has slightly more arguments:
+        <b>Caution:</b> X_train and y_train in Fix_DQ must be pandas Dataframes or pandas Series. I have not tested it on numpy arrays. You can try your luck.
+        
         - `quantile`: float (0.75): Define a threshold for IQR for outlier detection. Could be any float between 0 and 1. If quantile is set to `None`, then no outlier detection will take place.
         - `cat_fill_value`: string ("missing"): Define a fill value for missing categories in your object or categorical variables. This is a global default for your entire dataset. I will try to change it to a dictionary so that you can specify different values for different columns.
         - `num_fill_value`: integer or float (999): Define a fill value for missing numbers in your integer or float variables.  This is a global default for your entire dataset. I will try to change it to a dictionary so that you can specify different values for different columns.
         - `rare_threshold`: float (0.05):  Define a threshold for rare categories. If a certain category in a column is less 5% (say) of samples, then it will considered rare. All rare categories will be merged with a category value called "Rare". 
         - `correlation_threshold`: float (0.8): Define a correlation limit. Anything above this limit, the variable will be dropped. 
         <p>
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: pandas_dq Version: 1.3 Summary: Clean your data
+Metadata-Version: 2.1 Name: pandas_dq Version: 1.4 Summary: Clean your data
 using a scikit-learn transformer in a single line of code Home-page: https://
 github.com/AutoViML/pandas_dq Author: Ram Seshadri License: Apache License 2.0
 Description: # pandas_dq Analyze and clean your data in a single line of code
 with a Scikit-Learn compatible Transformer. # Table of Contents
     * What_is_pandas_dq
     * How_to_use_pandas_dq
     * How_to_install_pandas_dq
@@ -11,18 +11,18 @@
     * Maintainers
     * Contributing
     * License
 ## Introduction ### What is pandas_dq? `pandas_dq` is a new python library for
 automatically cleaning your dirty dataset using pandas scikit_learn functions.
 You can analyze your dataset and fix them - all in a single line of code! !
 [pandas_dq](./images/pandas_dq_logo.png) ## Uses `pandas_dq` has two important
-modules: `find_dq` and `Fix_DQ`. ### 1. find_dq function ![find_dq](./images/
-find_dq_screenshot.png)
-`find_dq` is a function that is probably the most popular way to use pandas_dq
-and it performs following data quality analysis steps:
+modules: `dq_report` and `Fix_DQ`. ### 1. dq_report function ![dq_report_code]
+(./images/find_dq_screenshot.png)
+`dq_report` is a function that is probably the most popular way to use
+pandas_dq and it performs following data quality analysis steps:
    1. It detects missing values and suggests to impute them with mean, median,
       mode, or a constant value.
    2. It identifies rare categories and suggests to group them into a single
       category or drop them.
    3. It finds infinite values and suggests to replace them with NaN or a large
       value.
    4. It detects mixed data types and suggests to convert them to a single type
@@ -41,15 +41,15 @@
   11. It detects feature leakage and suggests to avoid using features that are
       not available at prediction time.
 ### 2. Fix_DQ class: a scikit_learn transformer which can detect data quality
 issues and clean them all in one line of code ![fix_dq](./images/
 fix_dq_screenshot.png)
 `Fix_DQ` is a great way to clean an entire train data set and apply the same
 steps in an MLOps pipeline to a test dataset. `Fix_DQ` can be used to detect
-most issues in your data (similar to find_dq but without the target related
+most issues in your data (similar to dq_report but without the target related
 steps) in one step (during `fit` method). This transformer can then be saved
 (or "pickled") for applying the same steps on test data either at the same time
 or later.
 ### How can we use Fix_DQ in GridSearchCV to find the best model pipeline?
 This is another way to find the best data cleaning steps for your train data
 and then use the cleaned data in hyper parameter tuning using GridSearchCV or
 RandomizedSearchCV along with a LightGBM or an XGBoost or a scikit-learn model.
@@ -68,43 +68,46 @@
 See syntax below.
 ``` from pandas_dq import Fix_DQ # Call the transformer to print data quality
 issues # as well as clean your data - all in one step # Create an instance of
 the fix_data_quality transformer with default parameters fdq = Fix_DQ() # Fit
 the transformer on X_train and transform it X_train_transformed =
 fdq.fit_transform(X_train) # Transform X_test using the fitted transformer
 X_test_transformed = fdq.transform(X_test) ``` ### if you are not using the
-Transformer, you can simply call the function, find_dq ``` from pandas_dq
-import find_dq find_dq(df, target=target, verbose=0) ``` ## API
+Transformer, you can simply call the function, dq_report ``` from pandas_dq
+import dq_report dq_report(data, target=target, csv_engine="pandas", verbose=1)
+``` It prints out a data quality report like this: ![dq_report](./images/
+dq_report_screenshot.png) ## API
 pandas_dq has a very simple API with the following inputs. You need to create a
 sklearn-compatible transformer pipeline object by importing Fix_DQ from
 pandas_dq library.
 Once you import it, you can define the object by giving several options such
-as: **Arguments** Caution: X_train and y_train must be pandas Dataframes or
-pandas Series. I have not tested it on numpy arrays. You can try your luck.
-`find_dq` has only 3 arguments: - `data`: You can provide any kind of file
-format (string) or even a pandas DataFrame (df). It reads parquet, csv,
-feather, arrow, all kinds of file formats straight from disk. You just have to
-tell it the path to the file and the name of the file. - `target`: default:
-`None`. Otherwise, it should be a string name representing the name of a column
-in df. You can leave it as `None` if you don't want any target related issues.
-- `csv_engine`: default is `pandas`. If you want to load your file using any
-other backend engine such as `arrow` or `parquet` please specify it here. -
-`verbose`: This has 2 possible states: - `0` silent output. Great for running
-where it prints only high level data quality issues. - `1` more verbiage. Great
-for knowing details behind each issue and what the suggestions are. `Fix_DQ`
-has slightly more arguments: - `quantile`: float (0.75): Define a threshold for
-IQR for outlier detection. Could be any float between 0 and 1. If quantile is
-set to `None`, then no outlier detection will take place. - `cat_fill_value`:
-string ("missing"): Define a fill value for missing categories in your object
-or categorical variables. This is a global default for your entire dataset. I
-will try to change it to a dictionary so that you can specify different values
-for different columns. - `num_fill_value`: integer or float (999): Define a
-fill value for missing numbers in your integer or float variables. This is a
-global default for your entire dataset. I will try to change it to a dictionary
-so that you can specify different values for different columns. -
+as: **Arguments** `dq_report` has only 4 arguments: - `data`: You can provide
+any kind of file format (string) or even a pandas DataFrame (df). It reads
+parquet, csv, feather, arrow, all kinds of file formats straight from disk. You
+just have to tell it the path to the file and the name of the file. - `target`:
+default: `None`. Otherwise, it should be a string name representing the name of
+a column in df. You can leave it as `None` if you don't want any target related
+issues. - `csv_engine`: default is `pandas`. If you want to load your file
+using any other backend engine such as `arrow` or `parquet` please specify it
+here. - `verbose`: This has 2 possible states: - `0` summary report. Prints
+only the summary level data quality issues in the dataset. Great for managers.
+- `1` detailed report. Prints all the gory details behind each DQ issue in your
+dataset and what to do about them. Great for engineers. `Fix_DQ` has slightly
+more arguments: Caution: X_train and y_train in Fix_DQ must be pandas
+Dataframes or pandas Series. I have not tested it on numpy arrays. You can try
+your luck. - `quantile`: float (0.75): Define a threshold for IQR for outlier
+detection. Could be any float between 0 and 1. If quantile is set to `None`,
+then no outlier detection will take place. - `cat_fill_value`: string
+("missing"): Define a fill value for missing categories in your object or
+categorical variables. This is a global default for your entire dataset. I will
+try to change it to a dictionary so that you can specify different values for
+different columns. - `num_fill_value`: integer or float (999): Define a fill
+value for missing numbers in your integer or float variables. This is a global
+default for your entire dataset. I will try to change it to a dictionary so
+that you can specify different values for different columns. -
 `rare_threshold`: float (0.05): Define a threshold for rare categories. If a
 certain category in a column is less 5% (say) of samples, then it will
 considered rare. All rare categories will be merged with a category value
 called "Rare". - `correlation_threshold`: float (0.8): Define a correlation
 limit. Anything above this limit, the variable will be dropped.
 ## Maintainers * [@AutoViML](https://github.com/AutoViML) ## Contributing See
 [the contributing file](CONTRIBUTING.md)! PRs accepted. ## License Apache
```

### Comparing `pandas_dq-1.3/README.md` & `pandas_dq-1.4/README.md`

 * *Files 6% similar despite different names*

```diff
@@ -17,21 +17,21 @@
 ## Introduction
 ### What is pandas_dq?
 `pandas_dq` is a new python library for automatically cleaning your dirty dataset using pandas scikit_learn functions. You can analyze your dataset and fix them - all in a single line of code!
 
 ![pandas_dq](./images/pandas_dq_logo.png)
 
 ## Uses
-`pandas_dq` has two important modules: `find_dq` and `Fix_DQ`. 
+`pandas_dq` has two important modules: `dq_report` and `Fix_DQ`. 
 
-### 1.  find_dq function
+### 1.  dq_report function
 
-![find_dq](./images/find_dq_screenshot.png)
+![dq_report_code](./images/find_dq_screenshot.png)
 
-<p>`find_dq` is a function that is probably the most popular way to use pandas_dq and it performs following data quality analysis steps:
+<p>`dq_report` is a function that is probably the most popular way to use pandas_dq and it performs following data quality analysis steps:
 <ol>
 <li>It detects missing values and suggests to impute them with mean, median, mode, or a constant value.</li>
 <li>It identifies rare categories and suggests to group them into a single category or drop them.</li>
 <li>It finds infinite values and suggests to replace them with NaN or a large value.</li>
 <li>It detects mixed data types and suggests to convert them to a single type or split them into multiple columns.</li>
 <li>It detects outliers and suggests to remove them or use robust statistics.</li>
 <li>It detects high cardinality features and suggests to reduce them using encoding techniques or feature selection methods.</li>
@@ -43,22 +43,20 @@
 </ol>
 
 
 ### 2.  Fix_DQ class: a scikit_learn transformer which can detect data quality issues and clean them all in one line of code
 
 ![fix_dq](./images/fix_dq_screenshot.png)
 
-<p>`Fix_DQ` is a great way to clean an entire train data set and apply the same steps in an MLOps pipeline to a test dataset.  `Fix_DQ` can be used to detect most issues in your data (similar to find_dq but without the target related steps) in one step (during `fit` method). This transformer can then be saved (or "pickled") for applying the same steps on test data either at the same time or later.<br>
+<p>`Fix_DQ` is a great way to clean an entire train data set and apply the same steps in an MLOps pipeline to a test dataset.  `Fix_DQ` can be used to detect most issues in your data (similar to dq_report but without the target related steps) in one step (during `fit` method). This transformer can then be saved (or "pickled") for applying the same steps on test data either at the same time or later.<br>
 
 
 ###  How can we use Fix_DQ in GridSearchCV to find the best model pipeline?
 <p>This is another way to find the best data cleaning steps for your train data and then use the cleaned data in hyper parameter tuning using GridSearchCV or RandomizedSearchCV along with a LightGBM or an XGBoost or a scikit-learn model.<br>
 
-
-
 ## Install
 <p>
 
 **Prerequsites:**
 <ol>
 <li><b>pandas_dq is built using pandas, numpy and scikit-learn - that's all.</b> It should run on almost all Python3 Anaconda installations without additional installs. You won't have to import any special libraries.</li>
 </ol>
@@ -97,40 +95,44 @@
 # Fit the transformer on X_train and transform it
 X_train_transformed = fdq.fit_transform(X_train)
 
 # Transform X_test using the fitted transformer
 X_test_transformed = fdq.transform(X_test)
 ```
 
-### if you are not using the Transformer, you can simply call the function, find_dq
+### if you are not using the Transformer, you can simply call the function, dq_report
 
 ```
-from pandas_dq import find_dq
-find_dq(df, target=target, verbose=0)
+from pandas_dq import dq_report
+dq_report(data, target=target, csv_engine="pandas", verbose=1)
 ```
 
+It prints out a data quality report like this:
+
+![dq_report](./images/dq_report_screenshot.png)
+
 ## API
 
 <p>
 pandas_dq has a very simple API with the following inputs. You need to create a sklearn-compatible transformer pipeline object by importing Fix_DQ from pandas_dq library. <p>
 Once you import it, you can define the object by giving several options such as:
 
 **Arguments**
 
-<b>Caution:</b> X_train and y_train must be pandas Dataframes or pandas Series. I have not tested it on numpy arrays. You can try your luck.
-
-`find_dq` has only 3 arguments:
+`dq_report` has only 4 arguments:
 - `data`: You can provide any kind of file format (string) or even a pandas DataFrame (df). It reads parquet, csv, feather, arrow, all kinds of file formats straight from disk. You just have to tell it the path to the file and the name of the file.
 - `target`: default: `None`. Otherwise, it should be a string name representing the name of a column in df. You can leave it as `None` if you don't want any target related issues.
 - `csv_engine`: default is `pandas`. If you want to load your file using any other backend engine such as `arrow` or `parquet` please specify it here.
- - `verbose`: This has 2 possible states:
-  - `0` silent output. Great for running where it prints only high level data quality issues.
-  - `1` more verbiage. Great for knowing details behind each issue and what the suggestions are.
+- `verbose`: This has 2 possible states:
+  - `0` summary report. Prints only the summary level data quality issues in the dataset. Great for managers.
+  - `1` detailed report. Prints all the gory details behind each DQ issue in your dataset and what to do about them. Great for engineers.
 
 `Fix_DQ` has slightly more arguments:
+<b>Caution:</b> X_train and y_train in Fix_DQ must be pandas Dataframes or pandas Series. I have not tested it on numpy arrays. You can try your luck.
+
 - `quantile`: float (0.75): Define a threshold for IQR for outlier detection. Could be any float between 0 and 1. If quantile is set to `None`, then no outlier detection will take place.
 - `cat_fill_value`: string ("missing"): Define a fill value for missing categories in your object or categorical variables. This is a global default for your entire dataset. I will try to change it to a dictionary so that you can specify different values for different columns.
 - `num_fill_value`: integer or float (999): Define a fill value for missing numbers in your integer or float variables.  This is a global default for your entire dataset. I will try to change it to a dictionary so that you can specify different values for different columns.
 - `rare_threshold`: float (0.05):  Define a threshold for rare categories. If a certain category in a column is less 5% (say) of samples, then it will considered rare. All rare categories will be merged with a category value called "Rare". 
 - `correlation_threshold`: float (0.8): Define a correlation limit. Anything above this limit, the variable will be dropped. 
 <p>
```

#### html2text {}

```diff
@@ -8,18 +8,18 @@
     * Maintainers
     * Contributing
     * License
 ## Introduction ### What is pandas_dq? `pandas_dq` is a new python library for
 automatically cleaning your dirty dataset using pandas scikit_learn functions.
 You can analyze your dataset and fix them - all in a single line of code! !
 [pandas_dq](./images/pandas_dq_logo.png) ## Uses `pandas_dq` has two important
-modules: `find_dq` and `Fix_DQ`. ### 1. find_dq function ![find_dq](./images/
-find_dq_screenshot.png)
-`find_dq` is a function that is probably the most popular way to use pandas_dq
-and it performs following data quality analysis steps:
+modules: `dq_report` and `Fix_DQ`. ### 1. dq_report function ![dq_report_code]
+(./images/find_dq_screenshot.png)
+`dq_report` is a function that is probably the most popular way to use
+pandas_dq and it performs following data quality analysis steps:
    1. It detects missing values and suggests to impute them with mean, median,
       mode, or a constant value.
    2. It identifies rare categories and suggests to group them into a single
       category or drop them.
    3. It finds infinite values and suggests to replace them with NaN or a large
       value.
    4. It detects mixed data types and suggests to convert them to a single type
@@ -38,15 +38,15 @@
   11. It detects feature leakage and suggests to avoid using features that are
       not available at prediction time.
 ### 2. Fix_DQ class: a scikit_learn transformer which can detect data quality
 issues and clean them all in one line of code ![fix_dq](./images/
 fix_dq_screenshot.png)
 `Fix_DQ` is a great way to clean an entire train data set and apply the same
 steps in an MLOps pipeline to a test dataset. `Fix_DQ` can be used to detect
-most issues in your data (similar to find_dq but without the target related
+most issues in your data (similar to dq_report but without the target related
 steps) in one step (during `fit` method). This transformer can then be saved
 (or "pickled") for applying the same steps on test data either at the same time
 or later.
 ### How can we use Fix_DQ in GridSearchCV to find the best model pipeline?
 This is another way to find the best data cleaning steps for your train data
 and then use the cleaned data in hyper parameter tuning using GridSearchCV or
 RandomizedSearchCV along with a LightGBM or an XGBoost or a scikit-learn model.
@@ -65,43 +65,46 @@
 See syntax below.
 ``` from pandas_dq import Fix_DQ # Call the transformer to print data quality
 issues # as well as clean your data - all in one step # Create an instance of
 the fix_data_quality transformer with default parameters fdq = Fix_DQ() # Fit
 the transformer on X_train and transform it X_train_transformed =
 fdq.fit_transform(X_train) # Transform X_test using the fitted transformer
 X_test_transformed = fdq.transform(X_test) ``` ### if you are not using the
-Transformer, you can simply call the function, find_dq ``` from pandas_dq
-import find_dq find_dq(df, target=target, verbose=0) ``` ## API
+Transformer, you can simply call the function, dq_report ``` from pandas_dq
+import dq_report dq_report(data, target=target, csv_engine="pandas", verbose=1)
+``` It prints out a data quality report like this: ![dq_report](./images/
+dq_report_screenshot.png) ## API
 pandas_dq has a very simple API with the following inputs. You need to create a
 sklearn-compatible transformer pipeline object by importing Fix_DQ from
 pandas_dq library.
 Once you import it, you can define the object by giving several options such
-as: **Arguments** Caution: X_train and y_train must be pandas Dataframes or
-pandas Series. I have not tested it on numpy arrays. You can try your luck.
-`find_dq` has only 3 arguments: - `data`: You can provide any kind of file
-format (string) or even a pandas DataFrame (df). It reads parquet, csv,
-feather, arrow, all kinds of file formats straight from disk. You just have to
-tell it the path to the file and the name of the file. - `target`: default:
-`None`. Otherwise, it should be a string name representing the name of a column
-in df. You can leave it as `None` if you don't want any target related issues.
-- `csv_engine`: default is `pandas`. If you want to load your file using any
-other backend engine such as `arrow` or `parquet` please specify it here. -
-`verbose`: This has 2 possible states: - `0` silent output. Great for running
-where it prints only high level data quality issues. - `1` more verbiage. Great
-for knowing details behind each issue and what the suggestions are. `Fix_DQ`
-has slightly more arguments: - `quantile`: float (0.75): Define a threshold for
-IQR for outlier detection. Could be any float between 0 and 1. If quantile is
-set to `None`, then no outlier detection will take place. - `cat_fill_value`:
-string ("missing"): Define a fill value for missing categories in your object
-or categorical variables. This is a global default for your entire dataset. I
-will try to change it to a dictionary so that you can specify different values
-for different columns. - `num_fill_value`: integer or float (999): Define a
-fill value for missing numbers in your integer or float variables. This is a
-global default for your entire dataset. I will try to change it to a dictionary
-so that you can specify different values for different columns. -
+as: **Arguments** `dq_report` has only 4 arguments: - `data`: You can provide
+any kind of file format (string) or even a pandas DataFrame (df). It reads
+parquet, csv, feather, arrow, all kinds of file formats straight from disk. You
+just have to tell it the path to the file and the name of the file. - `target`:
+default: `None`. Otherwise, it should be a string name representing the name of
+a column in df. You can leave it as `None` if you don't want any target related
+issues. - `csv_engine`: default is `pandas`. If you want to load your file
+using any other backend engine such as `arrow` or `parquet` please specify it
+here. - `verbose`: This has 2 possible states: - `0` summary report. Prints
+only the summary level data quality issues in the dataset. Great for managers.
+- `1` detailed report. Prints all the gory details behind each DQ issue in your
+dataset and what to do about them. Great for engineers. `Fix_DQ` has slightly
+more arguments: Caution: X_train and y_train in Fix_DQ must be pandas
+Dataframes or pandas Series. I have not tested it on numpy arrays. You can try
+your luck. - `quantile`: float (0.75): Define a threshold for IQR for outlier
+detection. Could be any float between 0 and 1. If quantile is set to `None`,
+then no outlier detection will take place. - `cat_fill_value`: string
+("missing"): Define a fill value for missing categories in your object or
+categorical variables. This is a global default for your entire dataset. I will
+try to change it to a dictionary so that you can specify different values for
+different columns. - `num_fill_value`: integer or float (999): Define a fill
+value for missing numbers in your integer or float variables. This is a global
+default for your entire dataset. I will try to change it to a dictionary so
+that you can specify different values for different columns. -
 `rare_threshold`: float (0.05): Define a threshold for rare categories. If a
 certain category in a column is less 5% (say) of samples, then it will
 considered rare. All rare categories will be merged with a category value
 called "Rare". - `correlation_threshold`: float (0.8): Define a correlation
 limit. Anything above this limit, the variable will be dropped.
 ## Maintainers * [@AutoViML](https://github.com/AutoViML) ## Contributing See
 [the contributing file](CONTRIBUTING.md)! PRs accepted. ## License Apache
```

### Comparing `pandas_dq-1.3/pandas_dq.egg-info/PKG-INFO` & `pandas_dq-1.4/pandas_dq.egg-info/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pandas-dq
-Version: 1.3
+Version: 1.4
 Summary: Clean your data using a scikit-learn transformer in a single line of code
 Home-page: https://github.com/AutoViML/pandas_dq
 Author: Ram Seshadri
 License: Apache License 2.0
 Description: # pandas_dq
         Analyze and clean your data in a single line of code with a Scikit-Learn compatible Transformer.
         
@@ -24,21 +24,21 @@
         ## Introduction
         ### What is pandas_dq?
         `pandas_dq` is a new python library for automatically cleaning your dirty dataset using pandas scikit_learn functions. You can analyze your dataset and fix them - all in a single line of code!
         
         ![pandas_dq](./images/pandas_dq_logo.png)
         
         ## Uses
-        `pandas_dq` has two important modules: `find_dq` and `Fix_DQ`. 
+        `pandas_dq` has two important modules: `dq_report` and `Fix_DQ`. 
         
-        ### 1.  find_dq function
+        ### 1.  dq_report function
         
-        ![find_dq](./images/find_dq_screenshot.png)
+        ![dq_report_code](./images/find_dq_screenshot.png)
         
-        <p>`find_dq` is a function that is probably the most popular way to use pandas_dq and it performs following data quality analysis steps:
+        <p>`dq_report` is a function that is probably the most popular way to use pandas_dq and it performs following data quality analysis steps:
         <ol>
         <li>It detects missing values and suggests to impute them with mean, median, mode, or a constant value.</li>
         <li>It identifies rare categories and suggests to group them into a single category or drop them.</li>
         <li>It finds infinite values and suggests to replace them with NaN or a large value.</li>
         <li>It detects mixed data types and suggests to convert them to a single type or split them into multiple columns.</li>
         <li>It detects outliers and suggests to remove them or use robust statistics.</li>
         <li>It detects high cardinality features and suggests to reduce them using encoding techniques or feature selection methods.</li>
@@ -50,22 +50,20 @@
         </ol>
         
         
         ### 2.  Fix_DQ class: a scikit_learn transformer which can detect data quality issues and clean them all in one line of code
         
         ![fix_dq](./images/fix_dq_screenshot.png)
         
-        <p>`Fix_DQ` is a great way to clean an entire train data set and apply the same steps in an MLOps pipeline to a test dataset.  `Fix_DQ` can be used to detect most issues in your data (similar to find_dq but without the target related steps) in one step (during `fit` method). This transformer can then be saved (or "pickled") for applying the same steps on test data either at the same time or later.<br>
+        <p>`Fix_DQ` is a great way to clean an entire train data set and apply the same steps in an MLOps pipeline to a test dataset.  `Fix_DQ` can be used to detect most issues in your data (similar to dq_report but without the target related steps) in one step (during `fit` method). This transformer can then be saved (or "pickled") for applying the same steps on test data either at the same time or later.<br>
         
         
         ###  How can we use Fix_DQ in GridSearchCV to find the best model pipeline?
         <p>This is another way to find the best data cleaning steps for your train data and then use the cleaned data in hyper parameter tuning using GridSearchCV or RandomizedSearchCV along with a LightGBM or an XGBoost or a scikit-learn model.<br>
         
-        
-        
         ## Install
         <p>
         
         **Prerequsites:**
         <ol>
         <li><b>pandas_dq is built using pandas, numpy and scikit-learn - that's all.</b> It should run on almost all Python3 Anaconda installations without additional installs. You won't have to import any special libraries.</li>
         </ol>
@@ -104,40 +102,44 @@
         # Fit the transformer on X_train and transform it
         X_train_transformed = fdq.fit_transform(X_train)
         
         # Transform X_test using the fitted transformer
         X_test_transformed = fdq.transform(X_test)
         ```
         
-        ### if you are not using the Transformer, you can simply call the function, find_dq
+        ### if you are not using the Transformer, you can simply call the function, dq_report
         
         ```
-        from pandas_dq import find_dq
-        find_dq(df, target=target, verbose=0)
+        from pandas_dq import dq_report
+        dq_report(data, target=target, csv_engine="pandas", verbose=1)
         ```
         
+        It prints out a data quality report like this:
+        
+        ![dq_report](./images/dq_report_screenshot.png)
+        
         ## API
         
         <p>
         pandas_dq has a very simple API with the following inputs. You need to create a sklearn-compatible transformer pipeline object by importing Fix_DQ from pandas_dq library. <p>
         Once you import it, you can define the object by giving several options such as:
         
         **Arguments**
         
-        <b>Caution:</b> X_train and y_train must be pandas Dataframes or pandas Series. I have not tested it on numpy arrays. You can try your luck.
-        
-        `find_dq` has only 3 arguments:
+        `dq_report` has only 4 arguments:
         - `data`: You can provide any kind of file format (string) or even a pandas DataFrame (df). It reads parquet, csv, feather, arrow, all kinds of file formats straight from disk. You just have to tell it the path to the file and the name of the file.
         - `target`: default: `None`. Otherwise, it should be a string name representing the name of a column in df. You can leave it as `None` if you don't want any target related issues.
         - `csv_engine`: default is `pandas`. If you want to load your file using any other backend engine such as `arrow` or `parquet` please specify it here.
-         - `verbose`: This has 2 possible states:
-          - `0` silent output. Great for running where it prints only high level data quality issues.
-          - `1` more verbiage. Great for knowing details behind each issue and what the suggestions are.
+        - `verbose`: This has 2 possible states:
+          - `0` summary report. Prints only the summary level data quality issues in the dataset. Great for managers.
+          - `1` detailed report. Prints all the gory details behind each DQ issue in your dataset and what to do about them. Great for engineers.
         
         `Fix_DQ` has slightly more arguments:
+        <b>Caution:</b> X_train and y_train in Fix_DQ must be pandas Dataframes or pandas Series. I have not tested it on numpy arrays. You can try your luck.
+        
         - `quantile`: float (0.75): Define a threshold for IQR for outlier detection. Could be any float between 0 and 1. If quantile is set to `None`, then no outlier detection will take place.
         - `cat_fill_value`: string ("missing"): Define a fill value for missing categories in your object or categorical variables. This is a global default for your entire dataset. I will try to change it to a dictionary so that you can specify different values for different columns.
         - `num_fill_value`: integer or float (999): Define a fill value for missing numbers in your integer or float variables.  This is a global default for your entire dataset. I will try to change it to a dictionary so that you can specify different values for different columns.
         - `rare_threshold`: float (0.05):  Define a threshold for rare categories. If a certain category in a column is less 5% (say) of samples, then it will considered rare. All rare categories will be merged with a category value called "Rare". 
         - `correlation_threshold`: float (0.8): Define a correlation limit. Anything above this limit, the variable will be dropped. 
         <p>
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: pandas-dq Version: 1.3 Summary: Clean your data
+Metadata-Version: 2.1 Name: pandas-dq Version: 1.4 Summary: Clean your data
 using a scikit-learn transformer in a single line of code Home-page: https://
 github.com/AutoViML/pandas_dq Author: Ram Seshadri License: Apache License 2.0
 Description: # pandas_dq Analyze and clean your data in a single line of code
 with a Scikit-Learn compatible Transformer. # Table of Contents
     * What_is_pandas_dq
     * How_to_use_pandas_dq
     * How_to_install_pandas_dq
@@ -11,18 +11,18 @@
     * Maintainers
     * Contributing
     * License
 ## Introduction ### What is pandas_dq? `pandas_dq` is a new python library for
 automatically cleaning your dirty dataset using pandas scikit_learn functions.
 You can analyze your dataset and fix them - all in a single line of code! !
 [pandas_dq](./images/pandas_dq_logo.png) ## Uses `pandas_dq` has two important
-modules: `find_dq` and `Fix_DQ`. ### 1. find_dq function ![find_dq](./images/
-find_dq_screenshot.png)
-`find_dq` is a function that is probably the most popular way to use pandas_dq
-and it performs following data quality analysis steps:
+modules: `dq_report` and `Fix_DQ`. ### 1. dq_report function ![dq_report_code]
+(./images/find_dq_screenshot.png)
+`dq_report` is a function that is probably the most popular way to use
+pandas_dq and it performs following data quality analysis steps:
    1. It detects missing values and suggests to impute them with mean, median,
       mode, or a constant value.
    2. It identifies rare categories and suggests to group them into a single
       category or drop them.
    3. It finds infinite values and suggests to replace them with NaN or a large
       value.
    4. It detects mixed data types and suggests to convert them to a single type
@@ -41,15 +41,15 @@
   11. It detects feature leakage and suggests to avoid using features that are
       not available at prediction time.
 ### 2. Fix_DQ class: a scikit_learn transformer which can detect data quality
 issues and clean them all in one line of code ![fix_dq](./images/
 fix_dq_screenshot.png)
 `Fix_DQ` is a great way to clean an entire train data set and apply the same
 steps in an MLOps pipeline to a test dataset. `Fix_DQ` can be used to detect
-most issues in your data (similar to find_dq but without the target related
+most issues in your data (similar to dq_report but without the target related
 steps) in one step (during `fit` method). This transformer can then be saved
 (or "pickled") for applying the same steps on test data either at the same time
 or later.
 ### How can we use Fix_DQ in GridSearchCV to find the best model pipeline?
 This is another way to find the best data cleaning steps for your train data
 and then use the cleaned data in hyper parameter tuning using GridSearchCV or
 RandomizedSearchCV along with a LightGBM or an XGBoost or a scikit-learn model.
@@ -68,43 +68,46 @@
 See syntax below.
 ``` from pandas_dq import Fix_DQ # Call the transformer to print data quality
 issues # as well as clean your data - all in one step # Create an instance of
 the fix_data_quality transformer with default parameters fdq = Fix_DQ() # Fit
 the transformer on X_train and transform it X_train_transformed =
 fdq.fit_transform(X_train) # Transform X_test using the fitted transformer
 X_test_transformed = fdq.transform(X_test) ``` ### if you are not using the
-Transformer, you can simply call the function, find_dq ``` from pandas_dq
-import find_dq find_dq(df, target=target, verbose=0) ``` ## API
+Transformer, you can simply call the function, dq_report ``` from pandas_dq
+import dq_report dq_report(data, target=target, csv_engine="pandas", verbose=1)
+``` It prints out a data quality report like this: ![dq_report](./images/
+dq_report_screenshot.png) ## API
 pandas_dq has a very simple API with the following inputs. You need to create a
 sklearn-compatible transformer pipeline object by importing Fix_DQ from
 pandas_dq library.
 Once you import it, you can define the object by giving several options such
-as: **Arguments** Caution: X_train and y_train must be pandas Dataframes or
-pandas Series. I have not tested it on numpy arrays. You can try your luck.
-`find_dq` has only 3 arguments: - `data`: You can provide any kind of file
-format (string) or even a pandas DataFrame (df). It reads parquet, csv,
-feather, arrow, all kinds of file formats straight from disk. You just have to
-tell it the path to the file and the name of the file. - `target`: default:
-`None`. Otherwise, it should be a string name representing the name of a column
-in df. You can leave it as `None` if you don't want any target related issues.
-- `csv_engine`: default is `pandas`. If you want to load your file using any
-other backend engine such as `arrow` or `parquet` please specify it here. -
-`verbose`: This has 2 possible states: - `0` silent output. Great for running
-where it prints only high level data quality issues. - `1` more verbiage. Great
-for knowing details behind each issue and what the suggestions are. `Fix_DQ`
-has slightly more arguments: - `quantile`: float (0.75): Define a threshold for
-IQR for outlier detection. Could be any float between 0 and 1. If quantile is
-set to `None`, then no outlier detection will take place. - `cat_fill_value`:
-string ("missing"): Define a fill value for missing categories in your object
-or categorical variables. This is a global default for your entire dataset. I
-will try to change it to a dictionary so that you can specify different values
-for different columns. - `num_fill_value`: integer or float (999): Define a
-fill value for missing numbers in your integer or float variables. This is a
-global default for your entire dataset. I will try to change it to a dictionary
-so that you can specify different values for different columns. -
+as: **Arguments** `dq_report` has only 4 arguments: - `data`: You can provide
+any kind of file format (string) or even a pandas DataFrame (df). It reads
+parquet, csv, feather, arrow, all kinds of file formats straight from disk. You
+just have to tell it the path to the file and the name of the file. - `target`:
+default: `None`. Otherwise, it should be a string name representing the name of
+a column in df. You can leave it as `None` if you don't want any target related
+issues. - `csv_engine`: default is `pandas`. If you want to load your file
+using any other backend engine such as `arrow` or `parquet` please specify it
+here. - `verbose`: This has 2 possible states: - `0` summary report. Prints
+only the summary level data quality issues in the dataset. Great for managers.
+- `1` detailed report. Prints all the gory details behind each DQ issue in your
+dataset and what to do about them. Great for engineers. `Fix_DQ` has slightly
+more arguments: Caution: X_train and y_train in Fix_DQ must be pandas
+Dataframes or pandas Series. I have not tested it on numpy arrays. You can try
+your luck. - `quantile`: float (0.75): Define a threshold for IQR for outlier
+detection. Could be any float between 0 and 1. If quantile is set to `None`,
+then no outlier detection will take place. - `cat_fill_value`: string
+("missing"): Define a fill value for missing categories in your object or
+categorical variables. This is a global default for your entire dataset. I will
+try to change it to a dictionary so that you can specify different values for
+different columns. - `num_fill_value`: integer or float (999): Define a fill
+value for missing numbers in your integer or float variables. This is a global
+default for your entire dataset. I will try to change it to a dictionary so
+that you can specify different values for different columns. -
 `rare_threshold`: float (0.05): Define a threshold for rare categories. If a
 certain category in a column is less 5% (say) of samples, then it will
 considered rare. All rare categories will be merged with a category value
 called "Rare". - `correlation_threshold`: float (0.8): Define a correlation
 limit. Anything above this limit, the variable will be dropped.
 ## Maintainers * [@AutoViML](https://github.com/AutoViML) ## Contributing See
 [the contributing file](CONTRIBUTING.md)! PRs accepted. ## License Apache
```

### Comparing `pandas_dq-1.3/pandas_dq.py` & `pandas_dq-1.4/pandas_dq.py`

 * *Files 17% similar despite different names*

```diff
@@ -41,33 +41,34 @@
 # Import pandas and numpy libraries
 import pandas as pd
 import polars as pl
 import pyarrow as pa
 import numpy as np
 import copy
 import os
-# Define a function to print data cleaning suggestions
-def find_dq(data, target=None, csv_engine="pandas", verbose=0):
+# Define a function to print data quality report and suggestions to clean data
+def dq_report(data, target=None, csv_engine="pandas", verbose=0):
     """
-    This is a data quality check tool that accepts any kind of file format as a filename or as a pandas dataframe. 
-    It highlights potential data quality issues in the data. 
-    The function detects missing values and suggests to impute them with mean, median,
+    This is a data quality reporting tool that accepts any kind of file format as a filename or as a 
+    pandas dataframe as input and returns a report highlighting potential data quality issues in it. 
+    The function performs the following data quality checks. More will be added periodically.
+     It detects missing values and suggests to impute them with mean, median,
       mode, or a constant value. It also identifies rare categories and suggests to group them
        into a single category or to drop them. 
        The function finds infinite values and suggests to replace them with NaN or a
         large value. It detects mixed data types and suggests to convert them 
         to a single type or split them into multiple columns.
          The function detects duplicate rows and columns, outliers in numeric columns,
           high cardinality features only in categorical columns, and 
           highly correlated features. 
     Finally, the function identifies if the problem is a classification problem or
      a regression problem and checks if there is class imbalanced or target leakage in the dataset.
     """
     if not verbose:
-        print("Currently verbose set to 0. Change verbose to 1 to see more details on each DQ issue.")
+        print("This is a summary report. Change verbose to 1 to see more details on each DQ issue.")
     # Check if the input is a string or a dataframe
     if isinstance(data, str):
         # Get the file extension
         ext = os.path.splitext(data)[-1]
         # Load the file into a pandas dataframe based on the extension
         if ext == ".csv":
             if csv_engine == 'pandas':
@@ -95,134 +96,155 @@
 
     ### This is the column that lists our data quality issues
     new_col = 'DQ Issue'
     good_col = "The Good News"
     bad_col = "The Bad News"
 
     # Create an empty dataframe to store the data quality issues
-    dq_df1 = pd.DataFrame(columns=["Column", "first_comma", new_col])
-    dq_df1 = dq_df1.append({"Column": good_col, "first_comma":"", new_col: f""}, ignore_index=True)
-    dq_df1 = dq_df1.append({"Column": bad_col, "first_comma":"", new_col: f""}, ignore_index=True)
+    dq_df1 = pd.DataFrame(columns=[good_col, bad_col])
+    dq_df1 = dq_df1.T
+    dq_df1["first_comma"] = ""
+    dq_df1[new_col] = ""
 
     # Create an empty dataframe to store the data quality issues
-    dq_df2 = pd.DataFrame(columns=["Column", "first_comma", new_col])
-    for col in list(df):
-        dq_df2 = dq_df2.append({"Column": col, "first_comma":"", new_col: f""}, ignore_index=True)
-    
-    # Detect missing values and suggests to impute them with mean, median, mode, or a constant value123
+    data_types = pd.DataFrame(
+        df.dtypes,
+        columns=['Data Type']
+    )
     missing_values = df.isnull().sum()
     missing_cols = missing_values[missing_values > 0].index.tolist()
+    missing_data = pd.DataFrame(
+        missing_values,
+        columns=['Missing Values']
+    )
+    unique_values = pd.DataFrame(
+        columns=['Unique Values']
+    )
+    for row in list(df.columns.values):
+        unique_values.loc[row] = [df[row].nunique()]
+        
+    maximum_values = pd.DataFrame(
+        columns=['Maximum Value']
+    )
+    minimum_values = pd.DataFrame(
+        columns=['Minimum Value']
+    )
+    for row in list(df.columns.values):
+        if row not in missing_cols:
+            maximum_values.loc[row] = [df[row].max()]
+    for row in list(df.columns.values):
+        if row not in missing_cols:
+            minimum_values.loc[row] = [df[row].min()]
+
+    ### now generate the data quality report 
+    dq_df2 = data_types.join(missing_data).join(unique_values).join(minimum_values).join(maximum_values)
+
+    dq_df2["first_comma"] = ""
+    dq_df2[new_col] = f""
+    
+    # Detect missing values and suggests to impute them with mean, median, mode, or a constant value123
+    #missing_values = df.isnull().sum()
+    #missing_cols = missing_values[missing_values > 0].index.tolist()
     if len(missing_cols) > 0:
         for col in missing_cols:
             # Append a row to the dq_df1 with the column name and the issue only if the column has a missing value
             if missing_values[col] > 0:
-                mask0 = dq_df2['Column'] == col
-                new_string = f"{missing_values[col]} missing values. You may want to impute them with mean, median, mode, or a constant value such as 123."
-                dq_df2.loc[mask0,new_col] += dq_df2.loc[mask0,'first_comma'] + new_string
-                dq_df2.loc[mask0,'first_comma'] = ', '
+                new_string = f"{missing_values[col]} missing values. Impute them with mean, median, mode, or a constant value such as 123."
+                dq_df2.loc[col,new_col] += dq_df2.loc[col,'first_comma'] + new_string
+                dq_df2.loc[col,'first_comma'] = ', '
     else:
-        mask0 = dq_df1['Column'] == good_col
         new_string = f"There are no columns with missing values in the dataset"
-        dq_df1.loc[mask0,new_col] += dq_df1.loc[mask0,'first_comma'] + new_string
-        dq_df1.loc[mask0,'first_comma'] = ', '
+        dq_df1.loc[good_col,new_col] += dq_df1.loc[good_col,'first_comma'] + new_string
+        dq_df1.loc[good_col,'first_comma'] = ', '
     
 
     # Identify rare categories and suggests to group them into a single category or drop them123
     rare_threshold = 0.05 # Define a threshold for rare categories
     cat_cols = df.select_dtypes(include=["object", "category"]).columns.tolist() # Get categorical columns
     rare_cat_cols = []
     if len(cat_cols) > 0:
         for col in cat_cols:
             value_counts = df[col].value_counts(normalize=True)
             rare_values = value_counts[value_counts < rare_threshold].index.tolist()
             if len(rare_values) > 0:
                 rare_cat_cols.append(col)
                 # Append a row to the dq_df2 with the column name and the issue
-                mask0 = dq_df2['Column'] == col
-                new_string = f"{len(rare_values)} rare categories: {rare_values}. You may want to group them into a single category or drop the categories."
-                dq_df2.loc[mask0,new_col] += dq_df2.loc[mask0,'first_comma'] + new_string
-                dq_df2.loc[mask0,'first_comma'] = ', '
+                if len(rare_values) <= 10:
+                    new_string = f"{len(rare_values)} rare categories: {rare_values}. Group them into a single category or drop the categories."
+                else:
+                    new_string = f"{len(rare_values)} rare categories: Too many to list. Group them into a single category or drop the categories."
+                dq_df2.loc[col,new_col] += dq_df2.loc[col,'first_comma'] + new_string
+                dq_df2.loc[col,'first_comma'] = ', '
     else:
-        mask0 = dq_df1['Column'] == good_col
         new_string =  f"There are no categorical columns with rare categories (< {100*rare_threshold:.0f} percent) in this dataset"
-        dq_df1.loc[mask0,new_col] += dq_df1.loc[mask0,'first_comma'] + new_string
-        dq_df1.loc[mask0,'first_comma'] = ', '
+        dq_df1.loc[good_col,new_col] += dq_df1.loc[good_col,'first_comma'] + new_string
+        dq_df1.loc[good_col,'first_comma'] = ', '
 
 
     # Find infinite values and suggests to replace them with NaN or a large value123
     inf_values = df.replace([np.inf, -np.inf], np.nan).isnull().sum() - missing_values
     inf_cols = inf_values[inf_values > 0].index.tolist()
     if len(inf_cols) > 0:
-        mask0 = dq_df1['Column'] == bad_col
-        new_string =  f"There are {len(inf_cols)} columns with infinite values in the dataset. You may want to replace them with NaN or a large value."
-        dq_df1.loc[mask0,new_col] += dq_df1.loc[mask0,'first_comma'] + new_string
-        dq_df1.loc[mask0,'first_comma'] = ', '
+        new_string =  f"There are {len(inf_cols)} columns with infinite values in the dataset. Replace them with NaN or a finite value."
+        dq_df1.loc[bad_col,new_col] += dq_df1.loc[bad_col,'first_comma'] + new_string
+        dq_df1.loc[bad_col,'first_comma'] = ', '
         for col in inf_cols:
             if inf_values[col] > 0:
-                mask0 = dq_df2['Column'] == col
-                new_string = f"{inf_values[col]} infinite values. You may want to cap them with a maximum."
-                dq_df2.loc[mask0,new_col] += dq_df2.loc[mask0,'first_comma'] + new_string
-                dq_df2.loc[mask0,'first_comma'] = ', '
+                new_string = f"{inf_values[col]} infinite values. Replace them with a finite value."
+                dq_df2.loc[col,new_col] += dq_df2.loc[col,'first_comma'] + new_string
+                dq_df2.loc[col,'first_comma'] = ', '
     else:
-        mask0 = dq_df1['Column'] == good_col
         new_string =  f"There are no columns with infinite values in this dataset "
-        dq_df1.loc[mask0,new_col] += dq_df1.loc[mask0,'first_comma'] + new_string
-        dq_df1.loc[mask0,'first_comma'] = ', '
+        dq_df1.loc[good_col,new_col] += dq_df1.loc[good_col,'first_comma'] + new_string
+        dq_df1.loc[good_col,'first_comma'] = ', '
 
     # Detect mixed data types and suggests to convert them to a single type or split them into multiple columns123
     mixed_types = df.applymap(type).nunique() # Get the number of unique types in each column
     mixed_cols = mixed_types[mixed_types > 1].index.tolist() # Get the columns with more than one type
     if len(mixed_cols) > 0:
-        mask0 = dq_df1['Column'] == bad_col
-        new_string = f"There are {len(mixed_cols)} columns with mixed data types in the dataset. You may want to convert them to a single type or split them into multiple columns."
-        dq_df1.loc[mask0,new_col] += dq_df1.loc[mask0,'first_comma'] + new_string
-        dq_df1.loc[mask0,'first_comma'] = ', '
+        new_string = f"There are {len(mixed_cols)} columns with mixed data types in the dataset. Convert them to a single type or split them into multiple columns."
+        dq_df1.loc[bad_col,new_col] += dq_df1.loc[bad_col,'first_comma'] + new_string
+        dq_df1.loc[bad_col,'first_comma'] = ', '
         for col in mixed_cols:
             if mixed_types[col] > 1:
-                mask0 = dq_df2['Column'] == col
                 new_string = f"Mixed dtypes: has {mixed_types[col]} different data types: "
                 for each_class in df[col].apply(type).unique():
                     if each_class == str:
                         new_string +=  f" object,"
                     elif each_class == int:
                         new_string +=  f" integer,"
                     elif each_class == float:
                         new_string +=  f" float,"
-                dq_df2.loc[mask0,new_col] += dq_df2.loc[mask0,'first_comma'] + new_string
-                dq_df2.loc[mask0,'first_comma'] = ', '
+                dq_df2.loc[col,new_col] += dq_df2.loc[col,'first_comma'] + new_string
+                dq_df2.loc[col,'first_comma'] = ', '
     else:
-        mask0 = dq_df1['Column'] == good_col
         new_string =  f"There are no columns with mixed (more than one) dataypes in this dataset"
-        dq_df1.loc[mask0,new_col] += dq_df1.loc[mask0,'first_comma'] + new_string
-        dq_df1.loc[mask0,'first_comma'] = ', '
+        dq_df1.loc[good_col,new_col] += dq_df1.loc[good_col,'first_comma'] + new_string
+        dq_df1.loc[good_col,'first_comma'] = ', '
 
                 
     # Detect duplicate rows and columns
     dup_rows = df.duplicated().sum()
     dup_cols = df.T.duplicated().sum()
     if dup_rows > 0:
-        mask0 = dq_df1['Column'] == bad_col
-        new_string =  f"There are {len(dup_rows)} duplicate columns in the dataset. You may want to keep only one copy of {dup_rows}."
-        dq_df1.loc[mask0,new_col] += dq_df1.loc[mask0,'first_comma'] + new_string
-        dq_df1.loc[mask0,'first_comma'] = ', '
+        new_string =  f"There are {len(dup_rows)} duplicate columns in the dataset. Keep only one copy of {dup_rows}."
+        dq_df1.loc[bad_col,new_col] += dq_df1.loc[bad_col,'first_comma'] + new_string
+        dq_df1.loc[bad_col,'first_comma'] = ', '
     else:
-        mask0 = dq_df1['Column'] == good_col
         new_string =  f"There are no duplicate rows in this dataset"
-        dq_df1.loc[mask0,new_col] += dq_df1.loc[mask0,'first_comma'] + new_string
-        dq_df1.loc[mask0,'first_comma'] = ', '
+        dq_df1.loc[good_col,new_col] += dq_df1.loc[good_col,'first_comma'] + new_string
+        dq_df1.loc[good_col,'first_comma'] = ', '
     if dup_cols > 0:
-        mask0 = dq_df1['Column'] == bad_col
-        new_string =  f"There are {len(dup_cols)} duplicate columns in the dataset. You may want to keep only one copy of {dup_cols}."
-        dq_df1.loc[mask0,new_col] += dq_df1.loc[mask0,'first_comma'] + new_string
-        dq_df1.loc[mask0,'first_comma'] = ', '
+        new_string =  f"There are {len(dup_cols)} duplicate columns in the dataset. Keep only one copy of {dup_cols}."
+        dq_df1.loc[bad_col,new_col] += dq_df1.loc[bad_col,'first_comma'] + new_string
+        dq_df1.loc[bad_col,'first_comma'] = ', '
     else:
-        mask0 = dq_df1['Column'] == good_col
         new_string =  f"There are no duplicate columns in this datatset"
-        dq_df1.loc[mask0,new_col] += dq_df1.loc[mask0,'first_comma'] + new_string
-        dq_df1.loc[mask0,'first_comma'] = ', '
+        dq_df1.loc[good_col,new_col] += dq_df1.loc[good_col,'first_comma'] + new_string
+        dq_df1.loc[good_col,'first_comma'] = ', '
 
     # Detect outliers in numeric cols
     num_cols = df.select_dtypes(include=["int", "float"]).columns.tolist() # Get numerical columns
     if len(num_cols) > 0:
         first_time = True
         outlier_cols = []
         for col in num_cols:
@@ -231,70 +253,61 @@
             iqr = q3 - q1 # Get the interquartile range
             lower_bound = q1 - 1.5 * iqr # Get the lower bound
             upper_bound = q3 + 1.5 * iqr # Get the upper bound
             outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)][col] # Get the outliers
             if len(outliers) > 0:
                 outlier_cols.append(col)
                 if first_time:
-                    mask0 = dq_df1['Column'] == bad_col
                     new_string = f"There are {len(num_cols)} numerical columns, some with outliers. Remove them or use robust statistics."
-                    dq_df1.loc[mask0,new_col] += dq_df1.loc[mask0,'first_comma'] + new_string
-                    dq_df1.loc[mask0,'first_comma'] = ', '
+                    dq_df1.loc[bad_col,new_col] += dq_df1.loc[bad_col,'first_comma'] + new_string
+                    dq_df1.loc[bad_col,'first_comma'] = ', '
                     first_time =False
                 ### check if there are outlier columns and print them ##
-                mask0 = dq_df2['Column'] == col
-                new_string = f"has {len(outliers)} outliers starting at value: {min(outliers.values)}"
-                dq_df2.loc[mask0,new_col] += dq_df2.loc[mask0,'first_comma'] + new_string
-                dq_df2.loc[mask0,'first_comma'] = ', '
+                new_string = f"has {len(outliers)} outliers greater than upper bound or lower than lower bound: {min(outliers.values)}. Cap them or remove them."
+                dq_df2.loc[col,new_col] += dq_df2.loc[col,'first_comma'] + new_string
+                dq_df2.loc[col,'first_comma'] = ', '
         if len(outlier_cols) < 1:
-            mask0 = dq_df1['Column'] == good_col
             new_string =  f"There are no numeric columns with outliers in this dataset"
-            dq_df1.loc[mask0,new_col] += dq_df1.loc[mask0,'first_comma'] + new_string
-            dq_df1.loc[mask0,'first_comma'] = ', '
+            dq_df1.loc[good_col,new_col] += dq_df1.loc[good_col,'first_comma'] + new_string
+            dq_df1.loc[good_col,'first_comma'] = ', '
                 
     # Detect high cardinality features only in categorical columns
     cardinality_threshold = 100 # Define a threshold for high cardinality
     cardinality = df[cat_cols].nunique() # Get the number of unique values in each categorical column
     high_card_cols = cardinality[cardinality > cardinality_threshold].index.tolist() # Get the columns with high cardinality
     if len(high_card_cols) > 0:
-        mask0 = dq_df1['Column'] == bad_col
-        new_string = f"There are {len(high_card_cols)} columns with high cardinality (>{cardinality_threshold}) in the dataset. You may want to reduce them using encoding techniques or feature selection methods."
-        dq_df1.loc[mask0,new_col] += dq_df1.loc[mask0,'first_comma'] + new_string
-        dq_df1.loc[mask0,'first_comma'] = ', '
+        new_string = f"There are {len(high_card_cols)} columns with high cardinality (>{cardinality_threshold} categories) in the dataset. Reduce them using encoding techniques or feature selection methods."
+        dq_df1.loc[bad_col,new_col] += dq_df1.loc[bad_col,'first_comma'] + new_string
+        dq_df1.loc[bad_col,'first_comma'] = ', '
         for col in high_card_cols:
-            mask0 = dq_df2['Column'] == col
             new_string = f"high cardinality with {cardinality[col]} unique values."
-            dq_df2.loc[mask0,new_col] += dq_df2.loc[mask0,'first_comma'] + new_string
-            dq_df2.loc[mask0,'first_comma'] = ', '
+            dq_df2.loc[col,new_col] += dq_df2.loc[col,'first_comma'] + new_string
+            dq_df2.loc[col,'first_comma'] = ', '
     else:
-        mask0 = dq_df1['Column'] == good_col
         new_string =  f"There are no high cardinality columns in this dataset"
-        dq_df1.loc[mask0,new_col] += dq_df1.loc[mask0,'first_comma'] + new_string
-        dq_df1.loc[mask0,'first_comma'] = ', '
+        dq_df1.loc[good_col,new_col] += dq_df1.loc[good_col,'first_comma'] + new_string
+        dq_df1.loc[good_col,'first_comma'] = ', '
 
     # Detect highly correlated features
     correlation_threshold = 0.8 # Define a threshold for high correlation
     correlation_matrix = df.corr().abs() # Get the absolute correlation matrix of numerical columns
     upper_triangle = correlation_matrix.where(np.triu(np.ones(correlation_matrix.shape), k=1).astype(bool)) # Get the upper triangle of the matrix
     high_corr_cols = [column for column in upper_triangle.columns if any(upper_triangle[column] > correlation_threshold)] # Get the columns with high correlation
     if len(high_corr_cols) > 0:
-        mask0 = dq_df1['Column'] == bad_col
-        new_string = f"There are {len(high_corr_cols)} columns with higher than {correlation_threshold} correlation in the dataset. You may want to drop one of them or use dimensionality reduction techniques."
-        dq_df1.loc[mask0,new_col] += dq_df1.loc[mask0,'first_comma'] + new_string
-        dq_df1.loc[mask0,'first_comma'] = ', '
+        new_string = f"There are {len(high_corr_cols)} columns with >= {correlation_threshold} correlation in the dataset. Drop one of them or use dimensionality reduction techniques."
+        dq_df1.loc[bad_col,new_col] += dq_df1.loc[bad_col,'first_comma'] + new_string
+        dq_df1.loc[bad_col,'first_comma'] = ', '
         for col in high_corr_cols:
-            mask0 = dq_df2['Column'] == col
-            new_string = f"has a high correlation with {upper_triangle[col][upper_triangle[col] > correlation_threshold].index.tolist()}"
-            dq_df2.loc[mask0,new_col] += dq_df2.loc[mask0,'first_comma'] + new_string
-            dq_df2.loc[mask0,'first_comma'] = ', '
+            new_string = f"has a high correlation with {upper_triangle[col][upper_triangle[col] > correlation_threshold].index.tolist()}. Consider dropping one of them."
+            dq_df2.loc[col,new_col] += dq_df2.loc[col,'first_comma'] + new_string
+            dq_df2.loc[col,'first_comma'] = ', '
     else:
-        mask0 = dq_df1['Column'] == good_col
         new_string =  f"There are no highly correlated columns in the dataset."
-        dq_df1.loc[mask0,new_col] += dq_df1.loc[mask0,'first_comma'] + new_string
-        dq_df1.loc[mask0,'first_comma'] = ', '
+        dq_df1.loc[good_col,new_col] += dq_df1.loc[good_col,'first_comma'] + new_string
+        dq_df1.loc[good_col,'first_comma'] = ', '
 
     # First see if this is a classification problem 
     if target is not None:
         if isinstance(target, str):
             target_col = [target]
         else:
             target_col = copy.deepcopy(target) # Define the target column name
@@ -323,51 +336,54 @@
                 max_freq = value_counts.max()
                 # Define a threshold for imbalance
                 imbalance_threshold = 0.1
 
                 # Check if the class frequencies are imbalanced
                 if min_freq < imbalance_threshold or max_freq > 1 - imbalance_threshold:
                     # Print a message to suggest resampling techniques or class weights
-                    print(f"The classes are imbalanced in the {each_target_col} variable. You may want to use resampling techniques or class weights to address this issue.")
-                    # Print the class frequencies
-                    print(f"Class frequencies:\n{value_counts}")
+                    new_string =  f"Imbalanced classes in target variable ({each_target_col}). Use resampling or class weights to address."
+                    dq_df1.loc[bad_col,new_col] += dq_df1.loc[bad_col,'first_comma'] + new_string
+                    dq_df1.loc[bad_col,'first_comma'] = ', '
             
     # Detect target leakage in each feature
     if target is not None:
         target_col = copy.deepcopy(target) # Define the target column name
         if isinstance(target, str):
             preds = [x for x in list(df) if x not in [target_col]]
         else:
             preds = [x for x in list(df) if x not in target_col]
         leakage_threshold = 0.8 # Define a threshold for feature leakage
         leakage_matrix = df[preds].corrwith(df[target_col]).abs() # Get the absolute correlation matrix of each column with the target column
         leakage_cols = leakage_matrix[leakage_matrix > leakage_threshold].index.tolist() # Get the columns with feature leakage
         if len(leakage_cols) > 0:
-            print(f"There are {len(leakage_cols)} columns with feature leakage in the dataset. You may want to avoid using features that are not available at prediction time.")
+            new_string = f"There are {len(leakage_cols)} columns with data leakage. Double check whether you should use this variable."
+            dq_df1.loc[bad_col,new_col] += dq_df1.loc[bad_col,'first_comma'] + new_string
+            dq_df1.loc[bad_col,'first_comma'] = ', '
             for col in leakage_cols:
-                if verbose:
-                    print(f"    {col} has a correlation higher than {leakage_threshold} with {target_col}")
+                new_string = f"    {col} has a correlation >= {leakage_threshold} with {target_col}. Possible data leakage. Double check this variable."
+                dq_df2.loc[col,new_col] += dq_df2.loc[col,'first_comma'] + new_string
+                dq_df2.loc[col,'first_comma'] = ', '
         else:
-            mask0 = dq_df1['Column'] == good_col
             new_string =  f'There are no target leakage columns in the dataset'
-            dq_df1.loc[mask0,new_col] += dq_df1.loc[mask0,'first_comma'] + new_string
-            dq_df1.loc[mask0,'first_comma'] = ', '
+            dq_df1.loc[good_col,new_col] += dq_df1.loc[good_col,'first_comma'] + new_string
+            dq_df1.loc[good_col,'first_comma'] = ', '
     else:
-        print('There is no target given. Hence no target leakage columns detected in the dataset')
+        new_string = f'There is no target given. Hence no target leakage columns detected in the dataset'
+        dq_df1.loc[good_col,new_col] += dq_df1.loc[good_col,'first_comma'] + new_string
+        dq_df1.loc[good_col,'first_comma'] = ', '
 
     dq_df1.drop('first_comma', axis=1, inplace=True)
     dq_df2.drop('first_comma', axis=1, inplace=True)
     for col in list(df):
-        mask0 = dq_df2['Column'] == col
-        mask1 = dq_df2[new_col] == ""
-        dq_df2.loc[mask0&mask1,new_col] = "No issue"
+        if dq_df2.loc[col, new_col] == "":
+            dq_df2.loc[col,new_col] += "No issue"
 
     from IPython.display import display
 
-    if verbose >= 0:
+    if verbose == 0:
         all_rows = dq_df1.shape[0]
         ax = dq_df1.head(all_rows).style.background_gradient(cmap='Reds').set_properties(**{'font-family': 'Segoe UI'})
         display(ax);
 
     if verbose >= 1:
         all_rows = dq_df2.shape[0]
         ax = dq_df2.head(all_rows).style.background_gradient(cmap='Reds').set_properties(**{'font-family': 'Segoe UI'})
@@ -671,14 +687,14 @@
         imputed_X = self.impute_missing(power_X)
         
         # Return the transformed DataFrame
         return imputed_X
 
 ############################################################################################
 module_type = 'Running' if  __name__ == "__main__" else 'Imported'
-version_number =  '1.3'
+version_number =  '1.4'
 print(f"""{module_type} pandas_dq ({version_number}). Use fit and transform using:
 from pandas_dq import find_dq, Fix_DQ
 fdq = Fix_DQ(quantile=0.75, cat_fill_value="missing", num_fill_value=9999, 
                  rare_threshold=0.05, correlation_threshold=0.8)
 """)
 #################################################################################
```

