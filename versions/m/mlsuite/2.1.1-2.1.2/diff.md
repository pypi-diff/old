# Comparing `tmp/mlsuite-2.1.1.tar.gz` & `tmp/mlsuite-2.1.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "mlsuite-2.1.1.tar", last modified: Thu Apr  6 08:32:58 2023, max compression
+gzip compressed data, was "mlsuite-2.1.2.tar", last modified: Thu Apr  6 09:31:17 2023, max compression
```

## Comparing `mlsuite-2.1.1.tar` & `mlsuite-2.1.2.tar`

### file list

```diff
@@ -1,24 +1,24 @@
-drwxr-xr-x   0 li.suxing (31799) basic_bioinfo  (2003)        0 2023-04-06 08:32:58.968888 mlsuite-2.1.1/
--rw-r--r--   0 li.suxing (31799) basic_bioinfo  (2003)     1067 2022-08-30 02:42:20.000000 mlsuite-2.1.1/LICENSE
-drwxr-xr-x   0 li.suxing (31799) basic_bioinfo  (2003)        0 2023-04-06 08:32:58.953911 mlsuite-2.1.1/MLsuite/
--rwxr-xr-x   0 li.suxing (31799) basic_bioinfo  (2003)     7701 2023-04-06 08:32:39.000000 mlsuite-2.1.1/MLsuite/MLArguments.py
--rwxr-xr-x   0 li.suxing (31799) basic_bioinfo  (2003)    26629 2023-02-15 07:37:37.000000 mlsuite-2.1.1/MLsuite/MLEstimators.py
--rwxr-xr-x   0 li.suxing (31799) basic_bioinfo  (2003)     1931 2022-07-07 10:04:52.000000 mlsuite-2.1.1/MLsuite/MLLogging.py
--rwxr-xr-x   0 li.suxing (31799) basic_bioinfo  (2003)     2219 2022-07-07 10:04:52.000000 mlsuite-2.1.1/MLsuite/MLOpenWrite.py
--rwxr-xr-x   0 li.suxing (31799) basic_bioinfo  (2003)      836 2022-09-06 09:45:06.000000 mlsuite-2.1.1/MLsuite/MLPipeline.py
--rwxr-xr-x   0 li.suxing (31799) basic_bioinfo  (2003)     4438 2022-09-13 08:33:47.000000 mlsuite-2.1.1/MLsuite/MLPredicting.py
--rwxr-xr-x   0 li.suxing (31799) basic_bioinfo  (2003)    26637 2022-11-07 04:09:30.000000 mlsuite-2.1.1/MLsuite/MLSupervising.py
--rwxr-xr-x   0 li.suxing (31799) basic_bioinfo  (2003)     3424 2022-07-07 10:04:52.000000 mlsuite-2.1.1/MLsuite/MLUtilities.py
--rw-r--r--   0 li.suxing (31799) basic_bioinfo  (2003)       17 2022-09-06 06:29:23.000000 mlsuite-2.1.1/MLsuite/__init__.py
--rwxr-xr-x   0 li.suxing (31799) basic_bioinfo  (2003)     2118 2022-12-14 01:57:48.000000 mlsuite-2.1.1/MLsuite/main.py
--rw-r--r--   0 li.suxing (31799) basic_bioinfo  (2003)     1285 2023-04-06 08:32:58.967486 mlsuite-2.1.1/PKG-INFO
--rw-r--r--   0 li.suxing (31799) basic_bioinfo  (2003)     2405 2023-04-06 08:32:11.000000 mlsuite-2.1.1/README.md
-drwxr-xr-x   0 li.suxing (31799) basic_bioinfo  (2003)        0 2023-04-06 08:32:58.964473 mlsuite-2.1.1/mlsuite.egg-info/
--rw-r--r--   0 li.suxing (31799) basic_bioinfo  (2003)     1285 2023-04-06 08:32:58.000000 mlsuite-2.1.1/mlsuite.egg-info/PKG-INFO
--rw-r--r--   0 li.suxing (31799) basic_bioinfo  (2003)      414 2023-04-06 08:32:58.000000 mlsuite-2.1.1/mlsuite.egg-info/SOURCES.txt
--rw-r--r--   0 li.suxing (31799) basic_bioinfo  (2003)        1 2023-04-06 08:32:58.000000 mlsuite-2.1.1/mlsuite.egg-info/dependency_links.txt
--rw-r--r--   0 li.suxing (31799) basic_bioinfo  (2003)      115 2023-04-06 08:32:58.000000 mlsuite-2.1.1/mlsuite.egg-info/requires.txt
--rw-r--r--   0 li.suxing (31799) basic_bioinfo  (2003)        8 2023-04-06 08:32:58.000000 mlsuite-2.1.1/mlsuite.egg-info/top_level.txt
--rwxr-xr-x   0 li.suxing (31799) basic_bioinfo  (2003)      455 2022-09-06 10:51:20.000000 mlsuite-2.1.1/mlsuite.py
--rw-r--r--   0 li.suxing (31799) basic_bioinfo  (2003)       38 2023-04-06 08:32:58.969429 mlsuite-2.1.1/setup.cfg
--rwxr-xr-x   0 li.suxing (31799) basic_bioinfo  (2003)     1823 2023-04-06 08:29:42.000000 mlsuite-2.1.1/setup.py
+drwxr-xr-x   0 li.suxing (31799) basic_bioinfo  (2003)        0 2023-04-06 09:31:17.275000 mlsuite-2.1.2/
+-rw-r--r--   0 li.suxing (31799) basic_bioinfo  (2003)     1067 2022-08-30 02:42:20.000000 mlsuite-2.1.2/LICENSE
+drwxr-xr-x   0 li.suxing (31799) basic_bioinfo  (2003)        0 2023-04-06 09:31:17.261844 mlsuite-2.1.2/MLsuite/
+-rwxr-xr-x   0 li.suxing (31799) basic_bioinfo  (2003)     7701 2023-04-06 09:30:26.000000 mlsuite-2.1.2/MLsuite/MLArguments.py
+-rwxr-xr-x   0 li.suxing (31799) basic_bioinfo  (2003)    26629 2023-02-15 07:37:37.000000 mlsuite-2.1.2/MLsuite/MLEstimators.py
+-rwxr-xr-x   0 li.suxing (31799) basic_bioinfo  (2003)     1931 2022-07-07 10:04:52.000000 mlsuite-2.1.2/MLsuite/MLLogging.py
+-rwxr-xr-x   0 li.suxing (31799) basic_bioinfo  (2003)     2219 2022-07-07 10:04:52.000000 mlsuite-2.1.2/MLsuite/MLOpenWrite.py
+-rwxr-xr-x   0 li.suxing (31799) basic_bioinfo  (2003)      836 2022-09-06 09:45:06.000000 mlsuite-2.1.2/MLsuite/MLPipeline.py
+-rwxr-xr-x   0 li.suxing (31799) basic_bioinfo  (2003)     4438 2022-09-13 08:33:47.000000 mlsuite-2.1.2/MLsuite/MLPredicting.py
+-rwxr-xr-x   0 li.suxing (31799) basic_bioinfo  (2003)    26637 2022-11-07 04:09:30.000000 mlsuite-2.1.2/MLsuite/MLSupervising.py
+-rwxr-xr-x   0 li.suxing (31799) basic_bioinfo  (2003)     3424 2022-07-07 10:04:52.000000 mlsuite-2.1.2/MLsuite/MLUtilities.py
+-rw-r--r--   0 li.suxing (31799) basic_bioinfo  (2003)       17 2022-09-06 06:29:23.000000 mlsuite-2.1.2/MLsuite/__init__.py
+-rwxr-xr-x   0 li.suxing (31799) basic_bioinfo  (2003)     2118 2022-12-14 01:57:48.000000 mlsuite-2.1.2/MLsuite/main.py
+-rw-r--r--   0 li.suxing (31799) basic_bioinfo  (2003)     1285 2023-04-06 09:31:17.273361 mlsuite-2.1.2/PKG-INFO
+-rw-r--r--   0 li.suxing (31799) basic_bioinfo  (2003)     2614 2023-04-06 09:30:13.000000 mlsuite-2.1.2/README.md
+drwxr-xr-x   0 li.suxing (31799) basic_bioinfo  (2003)        0 2023-04-06 09:31:17.270954 mlsuite-2.1.2/mlsuite.egg-info/
+-rw-r--r--   0 li.suxing (31799) basic_bioinfo  (2003)     1285 2023-04-06 09:31:17.000000 mlsuite-2.1.2/mlsuite.egg-info/PKG-INFO
+-rw-r--r--   0 li.suxing (31799) basic_bioinfo  (2003)      414 2023-04-06 09:31:17.000000 mlsuite-2.1.2/mlsuite.egg-info/SOURCES.txt
+-rw-r--r--   0 li.suxing (31799) basic_bioinfo  (2003)        1 2023-04-06 09:31:17.000000 mlsuite-2.1.2/mlsuite.egg-info/dependency_links.txt
+-rw-r--r--   0 li.suxing (31799) basic_bioinfo  (2003)      116 2023-04-06 09:31:17.000000 mlsuite-2.1.2/mlsuite.egg-info/requires.txt
+-rw-r--r--   0 li.suxing (31799) basic_bioinfo  (2003)        8 2023-04-06 09:31:17.000000 mlsuite-2.1.2/mlsuite.egg-info/top_level.txt
+-rwxr-xr-x   0 li.suxing (31799) basic_bioinfo  (2003)      455 2022-09-06 10:51:20.000000 mlsuite-2.1.2/mlsuite.py
+-rw-r--r--   0 li.suxing (31799) basic_bioinfo  (2003)       38 2023-04-06 09:31:17.275535 mlsuite-2.1.2/setup.cfg
+-rwxr-xr-x   0 li.suxing (31799) basic_bioinfo  (2003)     1824 2023-04-06 09:28:55.000000 mlsuite-2.1.2/setup.py
```

### Comparing `mlsuite-2.1.1/LICENSE` & `mlsuite-2.1.2/LICENSE`

 * *Files identical despite different names*

### Comparing `mlsuite-2.1.1/MLsuite/MLArguments.py` & `mlsuite-2.1.2/MLsuite/MLArguments.py`

 * *Files 1% similar despite different names*

```diff
@@ -22,15 +22,15 @@
 Example:
 1. python mlsuite.py Auto    -i data.traintest.txt -g group.new.txt -p data.predict.txt -o testdt/ -m DT
 2. python mlsuite.py Auto    -i data.traintest.txt -g group.new.txt -o testdt/ -m DT
 3. python mlsuite.py Fitting -i data.traintest.txt -g group.new.txt -o testdt/ -m DT
 4. python mlsuite.py Predict -p data.predict.txt   -g group.new.txt -x modelpath/ -y predictdt/ -m DT.''')
 
     parser.add_argument('-V','--version',action ='version',
-                version='mlsuite version 2.1.1')
+                version='mlsuite version 2.1.2')
     subparsers = parser.add_subparsers(dest="commands",
                     help='machine learning models help.')
     ### Fitting module
     P_fitting  = subparsers.add_parser('Fitting',conflict_handler='resolve', add_help=False)
     P_fitting.add_argument("-i", "--input",type=str,
                     help='''the input train and test data file with dataframe format  by row(samples) x columns (features and Y). the sample column name must be Sample.
 ''')
```

### Comparing `mlsuite-2.1.1/MLsuite/MLEstimators.py` & `mlsuite-2.1.2/MLsuite/MLEstimators.py`

 * *Files identical despite different names*

### Comparing `mlsuite-2.1.1/MLsuite/MLLogging.py` & `mlsuite-2.1.2/MLsuite/MLLogging.py`

 * *Files identical despite different names*

### Comparing `mlsuite-2.1.1/MLsuite/MLOpenWrite.py` & `mlsuite-2.1.2/MLsuite/MLOpenWrite.py`

 * *Files identical despite different names*

### Comparing `mlsuite-2.1.1/MLsuite/MLPipeline.py` & `mlsuite-2.1.2/MLsuite/MLPipeline.py`

 * *Files identical despite different names*

### Comparing `mlsuite-2.1.1/MLsuite/MLPredicting.py` & `mlsuite-2.1.2/MLsuite/MLPredicting.py`

 * *Files identical despite different names*

### Comparing `mlsuite-2.1.1/MLsuite/MLSupervising.py` & `mlsuite-2.1.2/MLsuite/MLSupervising.py`

 * *Files identical despite different names*

### Comparing `mlsuite-2.1.1/MLsuite/MLUtilities.py` & `mlsuite-2.1.2/MLsuite/MLUtilities.py`

 * *Files identical despite different names*

### Comparing `mlsuite-2.1.1/MLsuite/main.py` & `mlsuite-2.1.2/MLsuite/main.py`

 * *Files identical despite different names*

### Comparing `mlsuite-2.1.1/PKG-INFO` & `mlsuite-2.1.2/PKG-INFO`

 * *Files 10% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: mlsuite
-Version: 2.1.1
+Version: 2.1.2
 Summary: The traditional machine learning analysis based on sklearn package
 Home-page: https://git.genecast.com.cn/narwhal/mlsuite
 Author: suxing li
 Author-email: li.suxing@genecast.com.cn
 Maintainer: suxing li
 Maintainer-email: li.suxing@genecast.com.cn
 Platform: all
```

### Comparing `mlsuite-2.1.1/README.md` & `mlsuite-2.1.2/README.md`

 * *Files 6% similar despite different names*

```diff
@@ -1,13 +1,13 @@
-# MLkit
+# mlsuite
 
 ## Install
 
 ```
-pip install mlsuite==2.1.1
+pip install mlsuite==2.1.2
 pip install https://github.com/JamesRitchie/scikit-rvm/archive/master.zip
 ```
 
 ## Usage
 
 Notice: used pyhton3, not python2
 
@@ -30,26 +30,37 @@
 
 1. python mlsuite.py Auto    -i data.traintest.txt -g group.new.txt -p data.predict.txt -o testdt/ -m DT
 2. python mlsuite.py Auto    -i data.traintest.txt -g group.new.txt -o testdt/ -m DT
 3. python mlsuite.py Fitting -i data.traintest.txt -g group.new.txt -o testdt/ -m DT
 4. python mlsuite.py Predict -p data.predict.txt   -g group.new.txt -x modelpath/ -y predictdt/ -m DT.
 
 ## Update log
+### v2.1.2
+1. revised same packages' version:
+```
+    lightgbm == 3.3.3,
+    joblib == 1.2.0,
+    numpy >= 1.16.4,
+    pandas >= 0.24.2,
+    scikit-learn == 1.2.0,
+    sklearn_pandas == 2.2.0,
+    xgboost == 1.7.2
+```
+
 ### v2.1.1
-    1. fixed same packages' version:
-    ```
+ 1. fixed same packages' version:
+```
     lightgbm == 3.3.3,
     joblib == 1.2.0,
     numpy == 1.23.5,
     pandas == 1.5.2,
     scikit-learn == 1.2.0,
     sklearn_pandas == 2.2.0,
     xgboost == 1.7.2
-    ```
-
+```
 
 ### v2.1.0
     1. LinearSVM parameter: LinearSVC(dual=False) report error: "unsupported set of arguments:  The combination of penalty='l2' and loss='hinge' are not supported when dual=False, Parameters: penalty='l2', loss='hinge', dual=False". So go back LinearSVC(dual=True).
     2. modified version information in MLArguments.py.
 
 ### v2.0.9
```

### Comparing `mlsuite-2.1.1/mlsuite.egg-info/PKG-INFO` & `mlsuite-2.1.2/mlsuite.egg-info/PKG-INFO`

 * *Files 10% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: mlsuite
-Version: 2.1.1
+Version: 2.1.2
 Summary: The traditional machine learning analysis based on sklearn package
 Home-page: https://git.genecast.com.cn/narwhal/mlsuite
 Author: suxing li
 Author-email: li.suxing@genecast.com.cn
 Maintainer: suxing li
 Maintainer-email: li.suxing@genecast.com.cn
 Platform: all
```

### Comparing `mlsuite-2.1.1/setup.py` & `mlsuite-2.1.2/setup.py`

 * *Files 6% similar despite different names*

```diff
@@ -4,30 +4,30 @@
 from setuptools import find_packages, setup
 from glob import glob
 from os.path import dirname, join
 import os
 
 setup(
     name='mlsuite',
-    version='2.1.1',
+    version='2.1.2',
     description='The traditional machine learning analysis based on sklearn package',
     author='suxing li',
     author_email='li.suxing@genecast.com.cn',
     maintainer='suxing li',
     maintainer_email='li.suxing@genecast.com.cn',
     packages=find_packages(where='.', exclude=(), include=('*',)),
     include_package_data=True,
     platforms=['all'],
     url='https://git.genecast.com.cn/narwhal/mlsuite',
     scripts=['./mlsuite.py'],
     install_requires=[
         'lightgbm == 3.3.3',
         'joblib == 1.2.0',
-        'numpy == 1.23.5',
-        'pandas == 1.5.2',
+        'numpy >= 1.16.4',
+        'pandas >= 0.24.2',
         'scikit-learn == 1.2.0',
         'sklearn_pandas == 2.2.0',
         'xgboost == 1.7.2'
     ],
     classifiers=[
         "Development Status :: 4 - Beta",
         "Environment :: Console",
```

