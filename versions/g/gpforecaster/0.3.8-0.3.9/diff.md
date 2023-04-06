# Comparing `tmp/gpforecaster-0.3.8.tar.gz` & `tmp/gpforecaster-0.3.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "gpforecaster-0.3.8.tar", last modified: Wed Dec 21 17:16:24 2022, max compression
+gzip compressed data, was "gpforecaster-0.3.9.tar", last modified: Thu Dec 22 10:07:29 2022, max compression
```

## Comparing `gpforecaster-0.3.8.tar` & `gpforecaster-0.3.9.tar`

### file list

```diff
@@ -1,31 +1,31 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-21 17:16:24.489130 gpforecaster-0.3.8/
--rw-r--r--   0 runner    (1001) docker     (123)      698 2022-12-21 17:16:24.489130 gpforecaster-0.3.8/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)       28 2022-12-21 17:16:16.000000 gpforecaster-0.3.8/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-21 17:16:24.489130 gpforecaster-0.3.8/gpforecaster/
--rw-r--r--   0 runner    (1001) docker     (123)      347 2022-12-21 17:16:16.000000 gpforecaster-0.3.8/gpforecaster/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-21 17:16:24.489130 gpforecaster-0.3.8/gpforecaster/model/
--rw-r--r--   0 runner    (1001) docker     (123)       67 2022-12-21 17:16:16.000000 gpforecaster-0.3.8/gpforecaster/model/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      508 2022-12-21 17:16:16.000000 gpforecaster-0.3.8/gpforecaster/model/gp.py
--rw-r--r--   0 runner    (1001) docker     (123)    12143 2022-12-21 17:16:16.000000 gpforecaster-0.3.8/gpforecaster/model/gpf.py
--rw-r--r--   0 runner    (1001) docker     (123)     1593 2022-12-21 17:16:16.000000 gpforecaster-0.3.8/gpforecaster/model/mean_functions.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-21 17:16:24.489130 gpforecaster-0.3.8/gpforecaster/results/
--rw-r--r--   0 runner    (1001) docker     (123)       33 2022-12-21 17:16:16.000000 gpforecaster-0.3.8/gpforecaster/results/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    12169 2022-12-21 17:16:16.000000 gpforecaster-0.3.8/gpforecaster/results/calculate_metrics.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-21 17:16:24.489130 gpforecaster-0.3.8/gpforecaster/tests/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2022-12-21 17:16:16.000000 gpforecaster-0.3.8/gpforecaster/tests/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      663 2022-12-21 17:16:16.000000 gpforecaster-0.3.8/gpforecaster/tests/test_calculate_results.py
--rw-r--r--   0 runner    (1001) docker     (123)     1586 2022-12-21 17:16:16.000000 gpforecaster-0.3.8/gpforecaster/tests/test_early_stopping.py
--rw-r--r--   0 runner    (1001) docker     (123)      772 2022-12-21 17:16:16.000000 gpforecaster-0.3.8/gpforecaster/tests/test_model_results_police.py
--rw-r--r--   0 runner    (1001) docker     (123)     1222 2022-12-21 17:16:16.000000 gpforecaster-0.3.8/gpforecaster/tests/test_model_results_prison.py
--rw-r--r--   0 runner    (1001) docker     (123)     2516 2022-12-21 17:16:16.000000 gpforecaster-0.3.8/gpforecaster/tests/test_tourism_gpf_with_local_file.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-21 17:16:24.489130 gpforecaster-0.3.8/gpforecaster/utils/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2022-12-21 17:16:16.000000 gpforecaster-0.3.8/gpforecaster/utils/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      919 2022-12-21 17:16:16.000000 gpforecaster-0.3.8/gpforecaster/utils/logger.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-21 17:16:24.489130 gpforecaster-0.3.8/gpforecaster.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)      698 2022-12-21 17:16:24.000000 gpforecaster-0.3.8/gpforecaster.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      745 2022-12-21 17:16:24.000000 gpforecaster-0.3.8/gpforecaster.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2022-12-21 17:16:24.000000 gpforecaster-0.3.8/gpforecaster.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      172 2022-12-21 17:16:24.000000 gpforecaster-0.3.8/gpforecaster.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       13 2022-12-21 17:16:24.000000 gpforecaster-0.3.8/gpforecaster.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)       38 2022-12-21 17:16:24.489130 gpforecaster-0.3.8/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1630 2022-12-21 17:16:16.000000 gpforecaster-0.3.8/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-22 10:07:29.678177 gpforecaster-0.3.9/
+-rw-r--r--   0 runner    (1001) docker     (123)      698 2022-12-22 10:07:29.678177 gpforecaster-0.3.9/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)       28 2022-12-22 10:07:18.000000 gpforecaster-0.3.9/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-22 10:07:29.674177 gpforecaster-0.3.9/gpforecaster/
+-rw-r--r--   0 runner    (1001) docker     (123)      347 2022-12-22 10:07:18.000000 gpforecaster-0.3.9/gpforecaster/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-22 10:07:29.674177 gpforecaster-0.3.9/gpforecaster/model/
+-rw-r--r--   0 runner    (1001) docker     (123)       67 2022-12-22 10:07:18.000000 gpforecaster-0.3.9/gpforecaster/model/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      508 2022-12-22 10:07:18.000000 gpforecaster-0.3.9/gpforecaster/model/gp.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12339 2022-12-22 10:07:18.000000 gpforecaster-0.3.9/gpforecaster/model/gpf.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1593 2022-12-22 10:07:18.000000 gpforecaster-0.3.9/gpforecaster/model/mean_functions.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-22 10:07:29.678177 gpforecaster-0.3.9/gpforecaster/results/
+-rw-r--r--   0 runner    (1001) docker     (123)       33 2022-12-22 10:07:18.000000 gpforecaster-0.3.9/gpforecaster/results/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12169 2022-12-22 10:07:18.000000 gpforecaster-0.3.9/gpforecaster/results/calculate_metrics.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-22 10:07:29.678177 gpforecaster-0.3.9/gpforecaster/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2022-12-22 10:07:18.000000 gpforecaster-0.3.9/gpforecaster/tests/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      663 2022-12-22 10:07:18.000000 gpforecaster-0.3.9/gpforecaster/tests/test_calculate_results.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1586 2022-12-22 10:07:18.000000 gpforecaster-0.3.9/gpforecaster/tests/test_early_stopping.py
+-rw-r--r--   0 runner    (1001) docker     (123)      772 2022-12-22 10:07:18.000000 gpforecaster-0.3.9/gpforecaster/tests/test_model_results_police.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1222 2022-12-22 10:07:18.000000 gpforecaster-0.3.9/gpforecaster/tests/test_model_results_prison.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2516 2022-12-22 10:07:18.000000 gpforecaster-0.3.9/gpforecaster/tests/test_tourism_gpf_with_local_file.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-22 10:07:29.678177 gpforecaster-0.3.9/gpforecaster/utils/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2022-12-22 10:07:18.000000 gpforecaster-0.3.9/gpforecaster/utils/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      919 2022-12-22 10:07:18.000000 gpforecaster-0.3.9/gpforecaster/utils/logger.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-22 10:07:29.674177 gpforecaster-0.3.9/gpforecaster.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)      698 2022-12-22 10:07:29.000000 gpforecaster-0.3.9/gpforecaster.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      745 2022-12-22 10:07:29.000000 gpforecaster-0.3.9/gpforecaster.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2022-12-22 10:07:29.000000 gpforecaster-0.3.9/gpforecaster.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      172 2022-12-22 10:07:29.000000 gpforecaster-0.3.9/gpforecaster.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       13 2022-12-22 10:07:29.000000 gpforecaster-0.3.9/gpforecaster.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2022-12-22 10:07:29.678177 gpforecaster-0.3.9/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1630 2022-12-22 10:07:18.000000 gpforecaster-0.3.9/setup.py
```

### Comparing `gpforecaster-0.3.8/PKG-INFO` & `gpforecaster-0.3.9/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: gpforecaster
-Version: 0.3.8
+Version: 0.3.9
 Summary: Hierarchical time series forecasting model using Gaussian Processes
 Author: Luis Roque
 Author-email: <roque0luis@gmail.com>
 Keywords: python,time series,hierarchical,forecasting,gaussian process,machine learning
 Classifier: Development Status :: 2 - Pre-Alpha
 Classifier: Intended Audience :: Science/Research
 Classifier: Topic :: Scientific/Engineering
```

### Comparing `gpforecaster-0.3.8/gpforecaster/model/gpf.py` & `gpforecaster-0.3.9/gpforecaster/model/gpf.py`

 * *Files 0% similar despite different names*

```diff
@@ -253,14 +253,15 @@
         )
         td = timedelta(seconds=int(time.time() - self.timer_start))
         self.logger.info(f"Num epochs {i}")
         self.logger.info(f"wall time train {str(td)}")
 
         self.logger.info(f"Val Loss {np.round(loss.item(), 2)}")
         self.logger.info(f"Loss {np.round(val_loss, 2)}")
+
         return model, likelihood
 
     def validate(self, model, mll):
         with torch.no_grad(), gpytorch.settings.fast_pred_var():
             likelihood_list_val, model_list_val = self._build_model(
                 x=self.test_x, y=self.test_y
             )
@@ -270,14 +271,18 @@
             self.val_losses.append(float(val_loss.item()))
         return val_loss.item()
 
     def plot_losses(self):
         n_iterations = np.arange(len(self.losses))
         plt.plot(n_iterations, self.losses)
         plt.plot(n_iterations, self.val_losses, marker="*")
+        timestamp = time.strftime("%Y%m%d-%H%M%S", time.gmtime())
+        plt.savefig(
+            f"./plots/gpf_loss_{self.dataset}_{timestamp}.pdf", format="pdf", bbox_inches="tight"
+        )
         plt.show()
 
     def predict(self, model, likelihood, clip=True):
         model.eval()
         likelihood.eval()
 
         with torch.no_grad(), gpytorch.settings.fast_pred_var():
```

### Comparing `gpforecaster-0.3.8/gpforecaster/model/mean_functions.py` & `gpforecaster-0.3.9/gpforecaster/model/mean_functions.py`

 * *Files identical despite different names*

### Comparing `gpforecaster-0.3.8/gpforecaster/results/calculate_metrics.py` & `gpforecaster-0.3.9/gpforecaster/results/calculate_metrics.py`

 * *Files identical despite different names*

### Comparing `gpforecaster-0.3.8/gpforecaster/tests/test_calculate_results.py` & `gpforecaster-0.3.9/gpforecaster/tests/test_calculate_results.py`

 * *Files identical despite different names*

### Comparing `gpforecaster-0.3.8/gpforecaster/tests/test_early_stopping.py` & `gpforecaster-0.3.9/gpforecaster/tests/test_early_stopping.py`

 * *Files identical despite different names*

### Comparing `gpforecaster-0.3.8/gpforecaster/tests/test_model_results_police.py` & `gpforecaster-0.3.9/gpforecaster/tests/test_model_results_police.py`

 * *Files identical despite different names*

### Comparing `gpforecaster-0.3.8/gpforecaster/tests/test_model_results_prison.py` & `gpforecaster-0.3.9/gpforecaster/tests/test_model_results_prison.py`

 * *Files identical despite different names*

### Comparing `gpforecaster-0.3.8/gpforecaster/tests/test_tourism_gpf_with_local_file.py` & `gpforecaster-0.3.9/gpforecaster/tests/test_tourism_gpf_with_local_file.py`

 * *Files identical despite different names*

### Comparing `gpforecaster-0.3.8/gpforecaster/utils/logger.py` & `gpforecaster-0.3.9/gpforecaster/utils/logger.py`

 * *Files identical despite different names*

### Comparing `gpforecaster-0.3.8/gpforecaster.egg-info/PKG-INFO` & `gpforecaster-0.3.9/gpforecaster.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: gpforecaster
-Version: 0.3.8
+Version: 0.3.9
 Summary: Hierarchical time series forecasting model using Gaussian Processes
 Author: Luis Roque
 Author-email: <roque0luis@gmail.com>
 Keywords: python,time series,hierarchical,forecasting,gaussian process,machine learning
 Classifier: Development Status :: 2 - Pre-Alpha
 Classifier: Intended Audience :: Science/Research
 Classifier: Topic :: Scientific/Engineering
```

### Comparing `gpforecaster-0.3.8/gpforecaster.egg-info/SOURCES.txt` & `gpforecaster-0.3.9/gpforecaster.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `gpforecaster-0.3.8/setup.py` & `gpforecaster-0.3.9/setup.py`

 * *Files identical despite different names*

