# Comparing `tmp/earthquakepy-0.2.5.tar.gz` & `tmp/earthquakepy-0.2.6.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "earthquakepy-0.2.5.tar", last modified: Mon Dec  5 18:53:49 2022, max compression
+gzip compressed data, was "earthquakepy-0.2.6.tar", last modified: Tue Dec  6 15:15:28 2022, max compression
```

## Comparing `earthquakepy-0.2.5.tar` & `earthquakepy-0.2.6.tar`

### file list

```diff
@@ -1,22 +1,22 @@
-drwxrwxr-x   0 digvijay  (1000) digvijay  (1000)        0 2022-12-05 18:53:49.462649 earthquakepy-0.2.5/
--rw-rw-r--   0 digvijay  (1000) digvijay  (1000)      803 2022-12-05 18:53:49.462649 earthquakepy-0.2.5/PKG-INFO
--rw-rw-r--   0 digvijay  (1000) digvijay  (1000)       90 2022-08-05 07:24:13.000000 earthquakepy-0.2.5/README.rst
-drwxrwxr-x   0 digvijay  (1000) digvijay  (1000)        0 2022-12-05 18:53:49.458649 earthquakepy-0.2.5/earthquakepy/
--rw-rw-r--   0 digvijay  (1000) digvijay  (1000)      192 2022-12-05 14:30:16.000000 earthquakepy-0.2.5/earthquakepy/__init__.py
--rw-rw-r--   0 digvijay  (1000) digvijay  (1000)     4334 2022-08-05 07:24:13.000000 earthquakepy-0.2.5/earthquakepy/ims.py
--rw-rw-r--   0 digvijay  (1000) digvijay  (1000)     3779 2022-08-05 07:24:13.000000 earthquakepy-0.2.5/earthquakepy/multidof.py
--rw-rw-r--   0 digvijay  (1000) digvijay  (1000)     2968 2022-08-05 07:24:13.000000 earthquakepy-0.2.5/earthquakepy/opensees_classes.py
--rw-rw-r--   0 digvijay  (1000) digvijay  (1000)     1591 2022-08-05 07:24:13.000000 earthquakepy-0.2.5/earthquakepy/opensees_helper.py
--rw-rw-r--   0 digvijay  (1000) digvijay  (1000)      322 2022-08-05 07:24:13.000000 earthquakepy-0.2.5/earthquakepy/responseMdof.py
--rw-rw-r--   0 digvijay  (1000) digvijay  (1000)     1295 2022-08-05 07:24:13.000000 earthquakepy-0.2.5/earthquakepy/responseSdof.py
--rw-rw-r--   0 digvijay  (1000) digvijay  (1000)     6882 2022-08-05 07:24:13.000000 earthquakepy-0.2.5/earthquakepy/singledof.py
--rw-rw-r--   0 digvijay  (1000) digvijay  (1000)    18203 2022-12-05 18:44:08.000000 earthquakepy-0.2.5/earthquakepy/timeseries.py
--rw-rw-r--   0 digvijay  (1000) digvijay  (1000)     5194 2022-12-05 18:44:08.000000 earthquakepy-0.2.5/earthquakepy/tsReaders.py
-drwxrwxr-x   0 digvijay  (1000) digvijay  (1000)        0 2022-12-05 18:53:49.458649 earthquakepy-0.2.5/earthquakepy.egg-info/
--rw-rw-r--   0 digvijay  (1000) digvijay  (1000)      803 2022-12-05 18:53:49.000000 earthquakepy-0.2.5/earthquakepy.egg-info/PKG-INFO
--rw-rw-r--   0 digvijay  (1000) digvijay  (1000)      470 2022-12-05 18:53:49.000000 earthquakepy-0.2.5/earthquakepy.egg-info/SOURCES.txt
--rw-rw-r--   0 digvijay  (1000) digvijay  (1000)        1 2022-12-05 18:53:49.000000 earthquakepy-0.2.5/earthquakepy.egg-info/dependency_links.txt
--rw-rw-r--   0 digvijay  (1000) digvijay  (1000)       23 2022-12-05 18:53:49.000000 earthquakepy-0.2.5/earthquakepy.egg-info/requires.txt
--rw-rw-r--   0 digvijay  (1000) digvijay  (1000)       13 2022-12-05 18:53:49.000000 earthquakepy-0.2.5/earthquakepy.egg-info/top_level.txt
--rw-rw-r--   0 digvijay  (1000) digvijay  (1000)       38 2022-12-05 18:53:49.462649 earthquakepy-0.2.5/setup.cfg
--rw-rw-r--   0 digvijay  (1000) digvijay  (1000)      984 2022-12-05 18:51:37.000000 earthquakepy-0.2.5/setup.py
+drwxrwxr-x   0 digvijay  (1000) digvijay  (1000)        0 2022-12-06 15:15:28.400995 earthquakepy-0.2.6/
+-rw-rw-r--   0 digvijay  (1000) digvijay  (1000)      803 2022-12-06 15:15:28.400995 earthquakepy-0.2.6/PKG-INFO
+-rw-rw-r--   0 digvijay  (1000) digvijay  (1000)       90 2022-12-06 07:40:28.000000 earthquakepy-0.2.6/README.rst
+drwxrwxr-x   0 digvijay  (1000) digvijay  (1000)        0 2022-12-06 15:15:28.396995 earthquakepy-0.2.6/earthquakepy/
+-rw-rw-r--   0 digvijay  (1000) digvijay  (1000)      192 2022-12-06 07:40:28.000000 earthquakepy-0.2.6/earthquakepy/__init__.py
+-rw-rw-r--   0 digvijay  (1000) digvijay  (1000)     4334 2022-12-06 07:40:28.000000 earthquakepy-0.2.6/earthquakepy/ims.py
+-rw-rw-r--   0 digvijay  (1000) digvijay  (1000)     3779 2022-12-06 07:40:28.000000 earthquakepy-0.2.6/earthquakepy/multidof.py
+-rw-rw-r--   0 digvijay  (1000) digvijay  (1000)     2968 2022-12-06 07:40:28.000000 earthquakepy-0.2.6/earthquakepy/opensees_classes.py
+-rw-rw-r--   0 digvijay  (1000) digvijay  (1000)     1591 2022-12-06 07:40:28.000000 earthquakepy-0.2.6/earthquakepy/opensees_helper.py
+-rw-rw-r--   0 digvijay  (1000) digvijay  (1000)      322 2022-12-06 07:40:28.000000 earthquakepy-0.2.6/earthquakepy/responseMdof.py
+-rw-rw-r--   0 digvijay  (1000) digvijay  (1000)     1295 2022-12-06 07:40:28.000000 earthquakepy-0.2.6/earthquakepy/responseSdof.py
+-rw-rw-r--   0 digvijay  (1000) digvijay  (1000)     6882 2022-12-06 07:40:28.000000 earthquakepy-0.2.6/earthquakepy/singledof.py
+-rw-rw-r--   0 digvijay  (1000) digvijay  (1000)    17897 2022-12-06 15:06:41.000000 earthquakepy-0.2.6/earthquakepy/timeseries.py
+-rw-rw-r--   0 digvijay  (1000) digvijay  (1000)     5194 2022-12-06 07:40:28.000000 earthquakepy-0.2.6/earthquakepy/tsReaders.py
+drwxrwxr-x   0 digvijay  (1000) digvijay  (1000)        0 2022-12-06 15:15:28.400995 earthquakepy-0.2.6/earthquakepy.egg-info/
+-rw-rw-r--   0 digvijay  (1000) digvijay  (1000)      803 2022-12-06 15:15:28.000000 earthquakepy-0.2.6/earthquakepy.egg-info/PKG-INFO
+-rw-rw-r--   0 digvijay  (1000) digvijay  (1000)      470 2022-12-06 15:15:28.000000 earthquakepy-0.2.6/earthquakepy.egg-info/SOURCES.txt
+-rw-rw-r--   0 digvijay  (1000) digvijay  (1000)        1 2022-12-06 15:15:28.000000 earthquakepy-0.2.6/earthquakepy.egg-info/dependency_links.txt
+-rw-rw-r--   0 digvijay  (1000) digvijay  (1000)       23 2022-12-06 15:15:28.000000 earthquakepy-0.2.6/earthquakepy.egg-info/requires.txt
+-rw-rw-r--   0 digvijay  (1000) digvijay  (1000)       13 2022-12-06 15:15:28.000000 earthquakepy-0.2.6/earthquakepy.egg-info/top_level.txt
+-rw-rw-r--   0 digvijay  (1000) digvijay  (1000)       38 2022-12-06 15:15:28.400995 earthquakepy-0.2.6/setup.cfg
+-rw-rw-r--   0 digvijay  (1000) digvijay  (1000)      984 2022-12-06 15:13:23.000000 earthquakepy-0.2.6/setup.py
```

### Comparing `earthquakepy-0.2.5/PKG-INFO` & `earthquakepy-0.2.6/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.2
 Name: earthquakepy
-Version: 0.2.5
+Version: 0.2.6
 Summary: python library for earthquake engineers.
 Home-page: https://github.com/gauthamrdy/earthquakepy
 Author: Gautham Reddy, Digvijay Patankar
 Author-email: pgrddy@gmail.com, dbpatankar@gmail.com
 License: GNU GPLv3
 Description: UNKNOWN
 Platform: UNKNOWN
```

### Comparing `earthquakepy-0.2.5/earthquakepy/ims.py` & `earthquakepy-0.2.6/earthquakepy/ims.py`

 * *Files identical despite different names*

### Comparing `earthquakepy-0.2.5/earthquakepy/multidof.py` & `earthquakepy-0.2.6/earthquakepy/multidof.py`

 * *Files identical despite different names*

### Comparing `earthquakepy-0.2.5/earthquakepy/opensees_classes.py` & `earthquakepy-0.2.6/earthquakepy/opensees_classes.py`

 * *Files identical despite different names*

### Comparing `earthquakepy-0.2.5/earthquakepy/opensees_helper.py` & `earthquakepy-0.2.6/earthquakepy/opensees_helper.py`

 * *Files identical despite different names*

### Comparing `earthquakepy-0.2.5/earthquakepy/responseSdof.py` & `earthquakepy-0.2.6/earthquakepy/responseSdof.py`

 * *Files identical despite different names*

### Comparing `earthquakepy-0.2.5/earthquakepy/singledof.py` & `earthquakepy-0.2.6/earthquakepy/singledof.py`

 * *Files identical despite different names*

### Comparing `earthquakepy-0.2.5/earthquakepy/timeseries.py` & `earthquakepy-0.2.6/earthquakepy/timeseries.py`

 * *Files 2% similar despite different names*

```diff
@@ -87,24 +87,24 @@
         Method plots time history of timeseries object. It accepts all the arguments that matplotlib.pyplot.subplots recognizes.
 
         Returns
         -------
         Matplotlib Figure Object
 
         """
-        mpl.pyplot.style.use('/home/kaushal/PhDwork/earthquakepy/mpl_stylesheet/style1.mplstyle')
         fig, ax = plt.subplots(**kwargs)
-        ax.plot(self.t, self.y)
+        ax.plot(self.t, self.y, color = 'k', label = str(self.eqName)+ '_' + str(self.component))
         if hasattr(self, "tunit"):
             ax.set_xlabel("t ({})".format(self.tunit))
         if hasattr(self, "yunit"):
             ax.set_ylabel(str(self.yunit))
         if log:
             ax.set_xscale("log")
         ax.set_xlim(left=0)
+        ax.legend()
         # plt.show()
         return fig
 
     def get_y(self, t):
         return np.interp(t, self.t, self.y)
 
     def get_response_spectra(self, T=np.arange(0.1, 20.01, 1.0), xi=0.05):
@@ -466,15 +466,14 @@
         Parameters
         ----------
         Returns
         -------
         Matplotlib Figure Object
 
         """
-        mpl.pyplot.style.use('/home/kaushal/PhDwork/earthquakepy/mpl_stylesheet/style1.mplstyle')
         fig, ax = plt.subplots(nrows=1, ncols=3, constrained_layout=True, **kwargs)
         ax[0].plot(self.T, self.Sd)
         ax[1].plot(self.T, self.Sv)
         ax[2].plot(self.T, self.Sa)
         ax[0].set_xlabel("Period (s)")
         ax[1].set_xlabel("Period (s)")
         ax[2].set_xlabel("Period (s)")
@@ -525,15 +524,14 @@
         Parameters
         ----------
         Returns
         -------
         Matplotlib Figure Object
 
         """
-        mpl.pyplot.style.use('/home/kaushal/PhDwork/earthquakepy/mpl_stylesheet/style1.mplstyle')
         defaultArgs = {"figsize" : (10,5)}
         kwargs = {**defaultArgs, **kwargs}
         fig = plt.figure(constrained_layout=True, **kwargs)
 
         gs = plt.GridSpec(2, 2, figure=fig)
         ax0 = fig.add_subplot(gs[0, :])
         ax1 = fig.add_subplot(gs[1, 0])
@@ -626,15 +624,14 @@
         Parameters
         ----------
         Returns
         -------
         Matplotlib Figure Object
 
         """
-        mpl.pyplot.style.use('/home/kaushal/PhDwork/earthquakepy/mpl_stylesheet/style1.mplstyle')
         fig, ax = plt.subplots()
         ax.plot(
             self.frequencies,
             2.0 / self.N * self.amplitude,
             )
         ax.set_xlabel("Frequency (Hz)")
         ax.set_ylabel("Power Amplitude")
```

### Comparing `earthquakepy-0.2.5/earthquakepy/tsReaders.py` & `earthquakepy-0.2.6/earthquakepy/tsReaders.py`

 * *Files identical despite different names*

### Comparing `earthquakepy-0.2.5/earthquakepy.egg-info/PKG-INFO` & `earthquakepy-0.2.6/earthquakepy.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.2
 Name: earthquakepy
-Version: 0.2.5
+Version: 0.2.6
 Summary: python library for earthquake engineers.
 Home-page: https://github.com/gauthamrdy/earthquakepy
 Author: Gautham Reddy, Digvijay Patankar
 Author-email: pgrddy@gmail.com, dbpatankar@gmail.com
 License: GNU GPLv3
 Description: UNKNOWN
 Platform: UNKNOWN
```

### Comparing `earthquakepy-0.2.5/setup.py` & `earthquakepy-0.2.6/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 #!/usr/bin/env python3
 
 from setuptools import setup
 
 setup(
     name="earthquakepy",
-    version="0.2.5",
+    version="0.2.6",
     description="python library for earthquake engineers.",
     url="https://github.com/gauthamrdy/earthquakepy",
     author="Gautham Reddy, Digvijay Patankar",
     author_email="pgrddy@gmail.com, dbpatankar@gmail.com",
     license="GNU GPLv3",
     packages=["earthquakepy"],
     install_requires=[
```

