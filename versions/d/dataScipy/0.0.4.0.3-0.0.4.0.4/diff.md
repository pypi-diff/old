# Comparing `tmp/dataScipy-0.0.4.0.3.tar.gz` & `tmp/dataScipy-0.0.4.0.4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dataScipy-0.0.4.0.3.tar", last modified: Sun Apr  2 17:59:47 2023, max compression
+gzip compressed data, was "dataScipy-0.0.4.0.4.tar", last modified: Fri Apr  7 12:31:20 2023, max compression
```

## Comparing `dataScipy-0.0.4.0.3.tar` & `dataScipy-0.0.4.0.4.tar`

### file list

```diff
@@ -1,17 +1,17 @@
-drwxr-xr-x   0 bora       (501) staff       (20)        0 2023-04-02 17:59:47.252209 dataScipy-0.0.4.0.3/
--rw-r--r--   0 bora       (501) staff       (20)       66 2023-03-24 16:14:24.000000 dataScipy-0.0.4.0.3/AUTHORS.md
--rw-r--r--   0 bora       (501) staff       (20)     1066 2023-03-24 16:14:37.000000 dataScipy-0.0.4.0.3/LICENCE
--rw-r--r--   0 bora       (501) staff       (20)     1141 2023-04-02 17:59:47.252090 dataScipy-0.0.4.0.3/PKG-INFO
--rw-r--r--   0 bora       (501) staff       (20)      252 2023-03-24 16:14:44.000000 dataScipy-0.0.4.0.3/README.md
--rw-r--r--   0 bora       (501) staff       (20)     1030 2023-04-02 17:59:40.000000 dataScipy-0.0.4.0.3/pyproject.toml
--rw-r--r--   0 bora       (501) staff       (20)       38 2023-04-02 17:59:47.252244 dataScipy-0.0.4.0.3/setup.cfg
-drwxr-xr-x   0 bora       (501) staff       (20)        0 2023-04-02 17:59:47.249713 dataScipy-0.0.4.0.3/src/
-drwxr-xr-x   0 bora       (501) staff       (20)        0 2023-04-02 17:59:47.251115 dataScipy-0.0.4.0.3/src/dataScipy/
--rw-r--r--   0 bora       (501) staff       (20)    28651 2023-04-02 17:58:12.000000 dataScipy-0.0.4.0.3/src/dataScipy/DataScience.py
--rw-r--r--   0 bora       (501) staff       (20)      127 2023-04-02 17:58:15.000000 dataScipy-0.0.4.0.3/src/dataScipy/__init__.py
-drwxr-xr-x   0 bora       (501) staff       (20)        0 2023-04-02 17:59:47.251915 dataScipy-0.0.4.0.3/src/dataScipy.egg-info/
--rw-r--r--   0 bora       (501) staff       (20)     1141 2023-04-02 17:59:47.000000 dataScipy-0.0.4.0.3/src/dataScipy.egg-info/PKG-INFO
--rw-r--r--   0 bora       (501) staff       (20)      282 2023-04-02 17:59:47.000000 dataScipy-0.0.4.0.3/src/dataScipy.egg-info/SOURCES.txt
--rw-r--r--   0 bora       (501) staff       (20)        1 2023-04-02 17:59:47.000000 dataScipy-0.0.4.0.3/src/dataScipy.egg-info/dependency_links.txt
--rw-r--r--   0 bora       (501) staff       (20)       50 2023-04-02 17:59:47.000000 dataScipy-0.0.4.0.3/src/dataScipy.egg-info/requires.txt
--rw-r--r--   0 bora       (501) staff       (20)       10 2023-04-02 17:59:47.000000 dataScipy-0.0.4.0.3/src/dataScipy.egg-info/top_level.txt
+drwxr-xr-x   0 bora       (501) staff       (20)        0 2023-04-07 12:31:20.562195 dataScipy-0.0.4.0.4/
+-rw-r--r--   0 bora       (501) staff       (20)       66 2023-03-24 16:14:24.000000 dataScipy-0.0.4.0.4/AUTHORS.md
+-rw-r--r--   0 bora       (501) staff       (20)     1066 2023-03-24 16:14:37.000000 dataScipy-0.0.4.0.4/LICENCE
+-rw-r--r--   0 bora       (501) staff       (20)     1141 2023-04-07 12:31:20.562092 dataScipy-0.0.4.0.4/PKG-INFO
+-rw-r--r--   0 bora       (501) staff       (20)      252 2023-03-24 16:14:44.000000 dataScipy-0.0.4.0.4/README.md
+-rw-r--r--   0 bora       (501) staff       (20)     1030 2023-04-07 12:30:15.000000 dataScipy-0.0.4.0.4/pyproject.toml
+-rw-r--r--   0 bora       (501) staff       (20)       38 2023-04-07 12:31:20.562224 dataScipy-0.0.4.0.4/setup.cfg
+drwxr-xr-x   0 bora       (501) staff       (20)        0 2023-04-07 12:31:20.560053 dataScipy-0.0.4.0.4/src/
+drwxr-xr-x   0 bora       (501) staff       (20)        0 2023-04-07 12:31:20.561196 dataScipy-0.0.4.0.4/src/dataScipy/
+-rw-r--r--   0 bora       (501) staff       (20)    29031 2023-04-07 12:29:05.000000 dataScipy-0.0.4.0.4/src/dataScipy/DataScience.py
+-rw-r--r--   0 bora       (501) staff       (20)      127 2023-04-07 12:28:23.000000 dataScipy-0.0.4.0.4/src/dataScipy/__init__.py
+drwxr-xr-x   0 bora       (501) staff       (20)        0 2023-04-07 12:31:20.561962 dataScipy-0.0.4.0.4/src/dataScipy.egg-info/
+-rw-r--r--   0 bora       (501) staff       (20)     1141 2023-04-07 12:31:20.000000 dataScipy-0.0.4.0.4/src/dataScipy.egg-info/PKG-INFO
+-rw-r--r--   0 bora       (501) staff       (20)      282 2023-04-07 12:31:20.000000 dataScipy-0.0.4.0.4/src/dataScipy.egg-info/SOURCES.txt
+-rw-r--r--   0 bora       (501) staff       (20)        1 2023-04-07 12:31:20.000000 dataScipy-0.0.4.0.4/src/dataScipy.egg-info/dependency_links.txt
+-rw-r--r--   0 bora       (501) staff       (20)       50 2023-04-07 12:31:20.000000 dataScipy-0.0.4.0.4/src/dataScipy.egg-info/requires.txt
+-rw-r--r--   0 bora       (501) staff       (20)       10 2023-04-07 12:31:20.000000 dataScipy-0.0.4.0.4/src/dataScipy.egg-info/top_level.txt
```

### Comparing `dataScipy-0.0.4.0.3/LICENCE` & `dataScipy-0.0.4.0.4/LICENCE`

 * *Files identical despite different names*

### Comparing `dataScipy-0.0.4.0.3/PKG-INFO` & `dataScipy-0.0.4.0.4/PKG-INFO`

 * *Files 9% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: dataScipy
-Version: 0.0.4.0.3
+Version: 0.0.4.0.4
 Summary: Python Library for some data-science tasks
 Author-email: Bora Aktas <baktas19@ku.edu.tr>
 Project-URL: Homepage, https://github.com/boraaktas/dataScipy
 Project-URL: Bug Tracker, https://github.com/boraaktas/dataScipy/issues
 Classifier: Development Status :: 1 - Planning
 Classifier: Intended Audience :: Science/Research
 Classifier: Natural Language :: English
```

### Comparing `dataScipy-0.0.4.0.3/pyproject.toml` & `dataScipy-0.0.4.0.4/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 [build-system]
 requires = ["setuptools>=61.0"]
 build-backend = "setuptools.build_meta"
 
 [project]
 name = "dataScipy"
-version = "0.0.4.0.3"
+version = "0.0.4.0.4"
 authors = [
   { name="Bora Aktas", email="baktas19@ku.edu.tr" },
 ]
 description = "Python Library for some data-science tasks"
 readme = "README.md"
 requires-python = ">=3.5"
 classifiers = [
```

### Comparing `dataScipy-0.0.4.0.3/src/dataScipy/DataScience.py` & `dataScipy-0.0.4.0.4/src/dataScipy/DataScience.py`

 * *Files 2% similar despite different names*

```diff
@@ -211,95 +211,95 @@
 
 
 ##########################################################################################
 ################################ PLOTTING RESIDUALS (ERRORS) #############################
 ##########################################################################################
 
 
-def plot_resids(residuals):
+def plot_resids(residuals, figsize=(8, 4), x_label='Time', y_label='Residuals', title='Residuals for the Forecast'):
     """
     Plot the residuals.
     :param residuals: the residuals (list)
     """
 
     residuals_mean = np.mean(residuals)
     no_residuals = len(residuals)
     mean_array = [residuals_mean] * no_residuals
 
-    plt.figure(figsize=(8, 4))
+    plt.figure(figsize=figsize)
     plt.plot(residuals, label='Residual', color='b')
     plt.plot(mean_array, label='Mean', linestyle='--', color='r')
-    plt.title("Residuals for the Forecast", loc = 'center')
-    plt.xlabel("Time")
-    plt.ylabel("Residuals")
+    plt.title(title, loc = 'center')
+    plt.xlabel(x_label)
+    plt.ylabel(y_label)
     plt.legend()
     plt.show()
 
 
 
-def plot_normalized_resids(residuals):
+def plot_normalized_resids(residuals, figsize=(6, 4)):
     """
     Plot the normalized residuals.
     :param residuals: the residuals (list)
     """
 
     residual_array = np.array(residuals)
 
     mean = residual_array.mean()
     std = residual_array.std()
 
     normalized_resids = DataFrame((residual_array - np.array(mean)) / std)
 
-    plt.figure(figsize=(6, 4))
+    plt.figure(figsize=figsize)
     plt.plot(normalized_resids, label='Normalized Residual', color='b')
     plt.title("Normalized Residuals for the Forecast", loc = 'center')
     plt.xlabel("Time")
     plt.ylabel("Normalized Residuals")
     plt.legend()
     plt.show()
 
 
 
-def plot_histogram_of_normalized_resids(residuals):
+def plot_histogram_of_normalized_resids(residuals, figsize=(6, 4)):
     """
     Plot the histogram of the normalized residuals.
     :param residuals: the residuals (list)
     """
 
     residual_array = np.array(residuals)
     
     mean = residual_array.mean()
     std = residual_array.std()
 
     normalized_resids = DataFrame((residual_array - np.array(mean)) / std)
 
-    fig = plt.figure(figsize=(6, 4))
+    fig = plt.figure(figsize=figsize)
     normalized_resids.plot(kind='hist', density=True, color='b', ec='w', ax=fig.gca(), legend=False)
     normalized_resids.plot(kind='kde', color='r', ax=fig.gca(), legend=False)
     plt.title("Histogram Plus Estimated Density", loc = 'center')
     plt.ylabel("Density")
     plt.xlabel("Residuals")
     plt.show()
 
 
 
-def plot_normal_of_normalized_resids(residuals):
+def plot_normal_of_normalized_resids(residuals, figsize=(6, 4)):
     """
     Plot the normal Q-Q plot of the normalized residuals.
     :param residuals: the residuals (list)
     """
 
     residual_array = np.array(residuals)
 
     rng = (0, 1)
     scaler = preprocessing.MinMaxScaler(feature_range=(rng[0], rng[1]))
     normed = scaler.fit_transform(residual_array.reshape(-1, 1)) 
     residuals_norm = [round(i[0], 2) for i in normed]
 
-    plt.figure(figsize=(6, 4))
+    plt.figure(figsize=figsize)
     stats.probplot(residuals_norm, dist="norm", plot=plt)
     plt.ylabel("Residuals")
     plt.title("Normal Q-Q plot", loc='center')
     plt.show()
 
 
 
@@ -591,15 +591,16 @@
 
 ##########################################################################################
 #################################### FORECAST PLOTTING ###################################
 ##########################################################################################
 
 
 
-def plot_forecasts(data, horizon, forecasts, time_step=1):
+def plot_forecasts(data, horizon, forecasts, time_step=1,
+                    figsize=(12, 5), title='Forecast and Data', xlabel=None, ylabel=None):
     """
     Plot the forecasts for the time series.
     :param data: the time series (list)
     :param horizon: the time horizon (list)
     :param forecasts: the forecasts (list)
     :param time_step: the step size for the time axis (integer)
 
@@ -609,27 +610,29 @@
     >>> forecasts = list of forecast values
     >>> plot_forecasts(data, horizon, forecasts)
     >>> plot_forecasts(data, horizon, forecasts, time_step=2)
     """
     
     number_of_dots = len(horizon)
 
-    plt.figure(figsize=(12, 5))
+    plt.figure(figsize=figsize)
     plt.xticks(np.arange(min(horizon), max(horizon)+1, time_step))
     plt.grid()
     plt.plot(horizon, data[:number_of_dots], label='data')
     plt.plot(horizon, forecasts[:number_of_dots], label='forecast')
-    plt.xlabel('Time')
-    plt.title('Forecast and Data')
+    plt.xlabel(xlabel)
+    plt.ylabel(ylabel)
+    plt.title(title)
     plt.legend()
     plt.show()
 
 
 
-def plot_forecasts_predictIntervals(data, horizon, forecasts, error_value, percent=0.90, time_step=1):
+def plot_forecasts_predictIntervals(data, horizon, forecasts, error_value, percent=0.90, time_step=1, 
+                                    figsize=(12, 5), title='Forecast and Data with Prediction Intervals', xlabel=None, ylabel=None):
     """
     Plot the forecasts for the time series.
     :param data: the time series (list)
     :param horizon: the time horizon (list)
     :param forecasts: the forecasts (list)
     :param error_function: the error function to calculate the error of the forecasts (function)
     :param percent: the percentage of the prediction interval (float)
@@ -648,28 +651,29 @@
     no_values = len(horizon)
 
     a = (1 - percent) / 2
     zval = abs(stats.norm.ppf(a))
     forecasts_upper_bounds = forecasts + zval * error_value
     forecasts_lower_bounds = forecasts - zval * error_value
 
-    plt.figure(figsize=(12, 5))
+    plt.figure(figsize=figsize)
     plt.xticks(np.arange(min(horizon), max(horizon)+1, time_step))
     plt.grid()
     plt.plot(horizon, data[:no_values], label='data')
     plt.plot(horizon, forecasts[:no_values], label='forecast')
     plt.fill_between(horizon, forecasts_lower_bounds[:no_values], forecasts_upper_bounds[:no_values], color='b', alpha=.1, label='confidence interval')
-    plt.xlabel('Time')
-    plt.title('Forecast and Data with Confidence Interval')
+    plt.xlabel(xlabel)
+    plt.ylabel(ylabel)
+    plt.title(title)
     plt.legend()
     plt.show()
 
 
 
-def plot_autocorrelation(values, no_lags=30):
+def plot_autocorrelation(values, no_lags=30, figsize=(6, 4)):
     """
     Plot the autocorrelation of the values.
     :param values: the values (list)
     :param no_lags: the number of lags to plot (int)
 
     :Example:
     >>> data = list of data values
@@ -684,24 +688,24 @@
     max_lag = len(values)
     if max_lag > 30:
         max_lag = 31
 
     if no_lags < max_lag:
         max_lag = no_lags + 1
 
-    plt.figure(figsize=(6, 4)) 
+    plt.figure(figsize=figsize)
     sm.graphics.tsa.plot_acf(normalized_values, color='b', ax=plt.gca(), lags=np.arange(1, max_lag))
     plt.title("Autocorrelation", loc='center')
     plt.ylabel("Correlations")
     plt.xlabel("Lags")
     plt.show()
 
 
 
-def plot_partial_autocorrelation(values, no_lags=30):
+def plot_partial_autocorrelation(values, no_lags=30, figsize=(6, 4)):
     """
     Plot the autocorrelation of the values.
     :param values: the values to plot (list)
     :param no_lags: the number of lags to plot (int)
 
     :Example:
     >>> data = list of data values
@@ -716,24 +720,24 @@
     max_lag = len(values)
     if max_lag > 30:
         max_lag = 31
 
     if no_lags < max_lag:
         max_lag = no_lags + 1
 
-    plt.figure(figsize=(6, 4)) 
+    plt.figure(figsize=figsize)
     sm.graphics.tsa.plot_pacf(normalized_values, color='b', ax=plt.gca(), lags=np.arange(1, max_lag), method='ywm')
     plt.title("Partial-Autocorrelation", loc='center')
     plt.ylabel("Correlations")
     plt.xlabel("Lags")
     plt.show()
 
 
 
-def plot_PACF_ACF_together(values, no_lags=30):
+def plot_PACF_ACF_together(values, no_lags=30, figsize=(13, 4)):
     """
     Plot the autocorrelation and partial autocorrelation of the values.
     :param values: the values to plot (list)
     :param no_lags: the number of lags to plot (int)
 
     :Example:
     >>> data = list of data values
@@ -748,15 +752,15 @@
     max_lag = len(values)
     if max_lag > 30:
         max_lag = 31
 
     if no_lags < max_lag:
         max_lag = no_lags + 1
 
-    plt.figure(figsize=(13, 4)) 
+    plt.figure(figsize=figsize) 
     plt.subplot(1, 2, 1)
     sm.graphics.tsa.plot_acf(normalized_values, color='b', ax=plt.gca(), lags=np.arange(1, max_lag))
     plt.title("Autocorrelation", loc='center')
     plt.ylabel("Correlations")
     plt.xlabel("Lags")
 
     plt.subplot(1, 2, 2)
```

### Comparing `dataScipy-0.0.4.0.3/src/dataScipy.egg-info/PKG-INFO` & `dataScipy-0.0.4.0.4/src/dataScipy.egg-info/PKG-INFO`

 * *Files 9% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: dataScipy
-Version: 0.0.4.0.3
+Version: 0.0.4.0.4
 Summary: Python Library for some data-science tasks
 Author-email: Bora Aktas <baktas19@ku.edu.tr>
 Project-URL: Homepage, https://github.com/boraaktas/dataScipy
 Project-URL: Bug Tracker, https://github.com/boraaktas/dataScipy/issues
 Classifier: Development Status :: 1 - Planning
 Classifier: Intended Audience :: Science/Research
 Classifier: Natural Language :: English
```

