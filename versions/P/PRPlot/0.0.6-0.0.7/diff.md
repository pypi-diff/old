# Comparing `tmp/PRPlot-0.0.6.tar.gz` & `tmp/PRPlot-0.0.7.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "PRPlot-0.0.6.tar", last modified: Fri Apr  7 02:05:02 2023, max compression
+gzip compressed data, was "PRPlot-0.0.7.tar", last modified: Fri Apr  7 02:17:14 2023, max compression
```

## Comparing `PRPlot-0.0.6.tar` & `PRPlot-0.0.7.tar`

### file list

```diff
@@ -1,14 +1,14 @@
-drwxrwxr-x   0 ferubko   (1000) ferubko   (1000)        0 2023-04-07 02:05:02.683098 PRPlot-0.0.6/
--rw-rw-r--   0 ferubko   (1000) ferubko   (1000)    35149 2023-04-06 20:40:07.000000 PRPlot-0.0.6/LICENSE
--rw-rw-r--   0 ferubko   (1000) ferubko   (1000)     1188 2023-04-07 02:05:02.687098 PRPlot-0.0.6/PKG-INFO
-drwxrwxr-x   0 ferubko   (1000) ferubko   (1000)        0 2023-04-07 02:05:02.659098 PRPlot-0.0.6/PRPlot/
--rw-rw-r--   0 ferubko   (1000) ferubko   (1000)     2437 2023-04-07 02:04:14.000000 PRPlot-0.0.6/PRPlot/PRPlot.py
--rw-rw-r--   0 ferubko   (1000) ferubko   (1000)      115 2023-04-07 02:04:35.000000 PRPlot-0.0.6/PRPlot/__init__.py
-drwxrwxr-x   0 ferubko   (1000) ferubko   (1000)        0 2023-04-07 02:05:02.679098 PRPlot-0.0.6/PRPlot.egg-info/
--rw-rw-r--   0 ferubko   (1000) ferubko   (1000)     1188 2023-04-07 02:05:02.000000 PRPlot-0.0.6/PRPlot.egg-info/PKG-INFO
--rw-rw-r--   0 ferubko   (1000) ferubko   (1000)      192 2023-04-07 02:05:02.000000 PRPlot-0.0.6/PRPlot.egg-info/SOURCES.txt
--rw-rw-r--   0 ferubko   (1000) ferubko   (1000)        1 2023-04-07 02:05:02.000000 PRPlot-0.0.6/PRPlot.egg-info/dependency_links.txt
--rw-rw-r--   0 ferubko   (1000) ferubko   (1000)        7 2023-04-07 02:05:02.000000 PRPlot-0.0.6/PRPlot.egg-info/top_level.txt
--rw-rw-r--   0 ferubko   (1000) ferubko   (1000)        8 2023-04-06 20:40:07.000000 PRPlot-0.0.6/README.md
--rw-rw-r--   0 ferubko   (1000) ferubko   (1000)       38 2023-04-07 02:05:02.699098 PRPlot-0.0.6/setup.cfg
--rw-rw-r--   0 ferubko   (1000) ferubko   (1000)     1557 2023-04-07 02:04:28.000000 PRPlot-0.0.6/setup.py
+drwxrwxr-x   0 ferubko   (1000) ferubko   (1000)        0 2023-04-07 02:17:14.629146 PRPlot-0.0.7/
+-rw-rw-r--   0 ferubko   (1000) ferubko   (1000)    35149 2023-04-06 20:40:07.000000 PRPlot-0.0.7/LICENSE
+-rw-rw-r--   0 ferubko   (1000) ferubko   (1000)     1188 2023-04-07 02:17:14.629146 PRPlot-0.0.7/PKG-INFO
+drwxrwxr-x   0 ferubko   (1000) ferubko   (1000)        0 2023-04-07 02:17:14.529144 PRPlot-0.0.7/PRPlot/
+-rw-rw-r--   0 ferubko   (1000) ferubko   (1000)     2464 2023-04-07 02:16:21.000000 PRPlot-0.0.7/PRPlot/PRPlot.py
+-rw-rw-r--   0 ferubko   (1000) ferubko   (1000)      115 2023-04-07 02:16:31.000000 PRPlot-0.0.7/PRPlot/__init__.py
+drwxrwxr-x   0 ferubko   (1000) ferubko   (1000)        0 2023-04-07 02:17:14.629146 PRPlot-0.0.7/PRPlot.egg-info/
+-rw-rw-r--   0 ferubko   (1000) ferubko   (1000)     1188 2023-04-07 02:17:14.000000 PRPlot-0.0.7/PRPlot.egg-info/PKG-INFO
+-rw-rw-r--   0 ferubko   (1000) ferubko   (1000)      192 2023-04-07 02:17:14.000000 PRPlot-0.0.7/PRPlot.egg-info/SOURCES.txt
+-rw-rw-r--   0 ferubko   (1000) ferubko   (1000)        1 2023-04-07 02:17:14.000000 PRPlot-0.0.7/PRPlot.egg-info/dependency_links.txt
+-rw-rw-r--   0 ferubko   (1000) ferubko   (1000)        7 2023-04-07 02:17:14.000000 PRPlot-0.0.7/PRPlot.egg-info/top_level.txt
+-rw-rw-r--   0 ferubko   (1000) ferubko   (1000)        8 2023-04-06 20:40:07.000000 PRPlot-0.0.7/README.md
+-rw-rw-r--   0 ferubko   (1000) ferubko   (1000)       38 2023-04-07 02:17:14.641146 PRPlot-0.0.7/setup.cfg
+-rw-rw-r--   0 ferubko   (1000) ferubko   (1000)     1557 2023-04-07 02:16:39.000000 PRPlot-0.0.7/setup.py
```

### Comparing `PRPlot-0.0.6/LICENSE` & `PRPlot-0.0.7/LICENSE`

 * *Files identical despite different names*

### Comparing `PRPlot-0.0.6/PKG-INFO` & `PRPlot-0.0.7/PKG-INFO`

 * *Files 15% similar despite different names*

```diff
@@ -1,16 +1,16 @@
 Metadata-Version: 2.1
 Name: PRPlot
-Version: 0.0.6
+Version: 0.0.7
 Summary: It is a Python library for build a very nice predict-reference plots. It is an extension of the matplotlib library
 Home-page: https://github.com/89605502155/PRPlot
 Author: Andrey Ferubko
 Author-email: ferubko1999@yandex.ru
 License: GNU General Public License v3.0
-Download-URL: https://github.com/89605502155/N-PLS/archive/v0.0.6.zip
+Download-URL: https://github.com/89605502155/N-PLS/archive/v0.0.7.zip
 Platform: UNKNOWN
 Classifier: License :: OSI Approved :: GNU General Public License v3 (GPLv3)
 Classifier: Operating System :: OS Independent
 Classifier: Intended Audience :: End Users/Desktop
 Classifier: Intended Audience :: Developers
 Classifier: Programming Language :: Python
 Classifier: Programming Language :: Python :: 3
```

### Comparing `PRPlot-0.0.6/PRPlot/PRPlot.py` & `PRPlot-0.0.7/PRPlot/PRPlot.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 import matplotlib.pyplot as plt
 import matplotlib as mpl
 import math
 from decimal import Decimal
 
 
-class PRPlot(plt,mpl):
+class PRPlot():
     def __int__(self, ms=30, lw=3, name_plot=None, x_name="X", y_name="Y",save_name="Plot"):
         self.ms = ms
         self.lw = lw
         self.name_plot = name_plot
         self.x_name = x_name
         self.y_name = y_name
         self.save_name = save_name
@@ -42,37 +42,37 @@
         lis=list()
         for i in arr1:
             lis.append(i)
         for i in arr2:
             lis.append(i)
         return lis
 
-    def main(self, ref, predict, save):
+    def main(self, ref, predict, save,ms=30, lw=3, name_plot=None, x_name="X", y_name="Y",save_name="Plot"):
         mpl.rc('font', family='Times New Roman')
         fig, axs = plt.subplots(figsize=(12, 7))
-        axs.plot(ref, predict, ".", color="red", ms=self.ms)
-        axs.plot(ref, ref, color="blue", lw=self.lw)
+        axs.plot(ref, predict, ".", color="red", ms=ms)
+        axs.plot(ref, ref, color="blue", lw=lw)
 
         lis_x, lis_x_num = self.ax(ref)
         lis_y, lis_y_num = self.ax(self.n_dat(ref,predict))
 
         axs.set_xticks(lis_x_num)
         axs.set_yticks(lis_y_num)
 
-        axs.set_ylabel(self.y_name, fontsize=25, labelpad=8)
+        axs.set_ylabel(y_name, fontsize=25, labelpad=8)
         axs.grid(color="black", linewidth=0.7)
-        axs.set_xlabel(self.x_name, fontsize=25, labelpad=15)
-        axs.set_title(self.name_plot, fontsize=28, loc="center", pad=15)
+        axs.set_xlabel(x_name, fontsize=25, labelpad=15)
+        axs.set_title(name_plot, fontsize=28, loc="center", pad=15)
         axs.tick_params(which='major', length=10, width=2)
 
         axs.set_xticklabels(lis_x, fontsize=20)
         axs.set_yticklabels(lis_y, fontsize=20)
 
         axs.get_xaxis().set_tick_params(direction='in')
         axs.get_yaxis().set_tick_params(direction='in')
 
         if save:
-            plt.savefig(self.save_name+'.png', format='png', dpi=300)
-            plt.savefig(self.save_name+".svg", format="svg")
+            plt.savefig(save_name+'.png', format='png', dpi=300)
+            plt.savefig(save_name+".svg", format="svg")
         plt.show()
         return 0
```

### Comparing `PRPlot-0.0.6/PRPlot.egg-info/PKG-INFO` & `PRPlot-0.0.7/PRPlot.egg-info/PKG-INFO`

 * *Files 15% similar despite different names*

```diff
@@ -1,16 +1,16 @@
 Metadata-Version: 2.1
 Name: PRPlot
-Version: 0.0.6
+Version: 0.0.7
 Summary: It is a Python library for build a very nice predict-reference plots. It is an extension of the matplotlib library
 Home-page: https://github.com/89605502155/PRPlot
 Author: Andrey Ferubko
 Author-email: ferubko1999@yandex.ru
 License: GNU General Public License v3.0
-Download-URL: https://github.com/89605502155/N-PLS/archive/v0.0.6.zip
+Download-URL: https://github.com/89605502155/N-PLS/archive/v0.0.7.zip
 Platform: UNKNOWN
 Classifier: License :: OSI Approved :: GNU General Public License v3 (GPLv3)
 Classifier: Operating System :: OS Independent
 Classifier: Intended Audience :: End Users/Desktop
 Classifier: Intended Audience :: Developers
 Classifier: Programming Language :: Python
 Classifier: Programming Language :: Python :: 3
```

### Comparing `PRPlot-0.0.6/setup.py` & `PRPlot-0.0.7/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 from io import open
 from setuptools import setup
 
 
-version = '0.0.6'
+version = '0.0.7'
 
 with open('README.md', encoding='utf-8') as f:
     long_description = f.read()
 
 setup(
     name='PRPlot',
     version=version,
```

