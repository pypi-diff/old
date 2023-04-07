# Comparing `tmp/HOBIT-0.0.4.tar.gz` & `tmp/HOBIT-0.0.5.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist\HOBIT-0.0.4.tar", last modified: Sat Aug 20 20:56:43 2022, max compression
+gzip compressed data, was "dist\HOBIT-0.0.5.tar", last modified: Fri Apr  7 08:14:11 2023, max compression
```

## Comparing `HOBIT-0.0.4.tar` & `HOBIT-0.0.5.tar`

### file list

```diff
@@ -1,15 +1,15 @@
-drwxrwxrwx   0        0        0        0 2022-08-20 20:56:43.925499 HOBIT-0.0.4/
-drwxrwxrwx   0        0        0        0 2022-08-20 20:56:43.899498 HOBIT-0.0.4/HOBIT/
--rw-rw-rw-   0        0        0     3477 2020-05-31 09:49:28.000000 HOBIT-0.0.4/HOBIT/HOBIT.py
--rw-rw-rw-   0        0        0       22 2020-05-30 22:14:41.000000 HOBIT-0.0.4/HOBIT/__init__.py
-drwxrwxrwx   0        0        0        0 2022-08-20 20:56:43.919502 HOBIT-0.0.4/HOBIT.egg-info/
--rw-rw-rw-   0        0        0     2189 2022-08-20 20:56:43.000000 HOBIT-0.0.4/HOBIT.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      223 2022-08-20 20:56:43.000000 HOBIT-0.0.4/HOBIT.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2022-08-20 20:56:43.000000 HOBIT-0.0.4/HOBIT.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0        2 2022-06-06 18:20:48.000000 HOBIT-0.0.4/HOBIT.egg-info/not-zip-safe
--rw-rw-rw-   0        0        0       60 2022-08-20 20:56:43.000000 HOBIT-0.0.4/HOBIT.egg-info/requires.txt
--rw-rw-rw-   0        0        0        6 2022-08-20 20:56:43.000000 HOBIT-0.0.4/HOBIT.egg-info/top_level.txt
--rw-rw-rw-   0        0        0     2189 2022-08-20 20:56:43.923496 HOBIT-0.0.4/PKG-INFO
--rw-rw-rw-   0        0        0     1375 2022-06-06 20:02:06.000000 HOBIT-0.0.4/README.md
--rw-rw-rw-   0        0        0       42 2022-08-20 20:56:43.926519 HOBIT-0.0.4/setup.cfg
--rw-rw-rw-   0        0        0      825 2022-08-20 20:56:29.000000 HOBIT-0.0.4/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-07 08:14:11.960057 HOBIT-0.0.5/
+drwxrwxrwx   0        0        0        0 2023-04-07 08:14:11.929057 HOBIT-0.0.5/HOBIT/
+-rw-rw-rw-   0        0        0     3477 2020-05-31 09:49:28.000000 HOBIT-0.0.5/HOBIT/HOBIT.py
+-rw-rw-rw-   0        0        0       22 2020-05-30 22:14:41.000000 HOBIT-0.0.5/HOBIT/__init__.py
+drwxrwxrwx   0        0        0        0 2023-04-07 08:14:11.955057 HOBIT-0.0.5/HOBIT.egg-info/
+-rw-rw-rw-   0        0        0     2108 2023-04-07 08:14:11.000000 HOBIT-0.0.5/HOBIT.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      223 2023-04-07 08:14:11.000000 HOBIT-0.0.5/HOBIT.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-07 08:14:11.000000 HOBIT-0.0.5/HOBIT.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0        2 2022-06-06 18:20:48.000000 HOBIT-0.0.5/HOBIT.egg-info/not-zip-safe
+-rw-rw-rw-   0        0        0       65 2023-04-07 08:14:11.000000 HOBIT-0.0.5/HOBIT.egg-info/requires.txt
+-rw-rw-rw-   0        0        0        6 2023-04-07 08:14:11.000000 HOBIT-0.0.5/HOBIT.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0     2108 2023-04-07 08:14:11.959057 HOBIT-0.0.5/PKG-INFO
+-rw-rw-rw-   0        0        0     1294 2022-08-20 21:28:26.000000 HOBIT-0.0.5/README.md
+-rw-rw-rw-   0        0        0       42 2023-04-07 08:14:11.961056 HOBIT-0.0.5/setup.cfg
+-rw-rw-rw-   0        0        0      825 2023-04-07 08:10:46.000000 HOBIT-0.0.5/setup.py
```

### Comparing `HOBIT-0.0.4/HOBIT/HOBIT.py` & `HOBIT-0.0.5/HOBIT/HOBIT.py`

 * *Files identical despite different names*

### Comparing `HOBIT-0.0.4/HOBIT.egg-info/PKG-INFO` & `HOBIT-0.0.5/HOBIT.egg-info/PKG-INFO`

 * *Files 20% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: HOBIT
-Version: 0.0.4
+Version: 0.0.5
 Summary: an installable package for Hybrid fitting of Sine and Cosine functions
 Home-page: https://github.com/Harmonic-Oscillator-hyBrid-fIT/HOBIT
 Author: Carmen Adriana Martinez Barbosa, Jose Arturo Celis Gil
 Author-email: anamabo3@gmail.com, solocelis@gmail.com
 License: UNKNOWN
 Description: <p align="center">
          <img src="https://github.com/anamabo/HOBIT/blob/master/images/logo.png?raw=true" alt="Sublime's custom image"/>
@@ -20,17 +20,17 @@
         f(x) = y_0 + y_1 * Sin(omega * x + phi)
         f(x) = y_0 + y_1 * Cos(omega * x + phi)
         ```
         
         whose are commonly used to describe harmonic oscillators.
         
         ## Install
-        Install HOBIT-0.0.3-py2.py3-none-any.whl that you can find in dist folder using 
+        Install HOBIT 0.0.4
         ```
-        pip install HOBIT-0.0.3-py2.py3-none-any.whl
+        pip install HOBIT==0.0.4
         ```
         ### Requirements
         Hobit will install/update the next python libraries
         
         * pandas>=1.1.3
         * numpy>=1.19.2
         * hyperopt>=0.2.7
```

### Comparing `HOBIT-0.0.4/PKG-INFO` & `HOBIT-0.0.5/PKG-INFO`

 * *Files 20% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: HOBIT
-Version: 0.0.4
+Version: 0.0.5
 Summary: an installable package for Hybrid fitting of Sine and Cosine functions
 Home-page: https://github.com/Harmonic-Oscillator-hyBrid-fIT/HOBIT
 Author: Carmen Adriana Martinez Barbosa, Jose Arturo Celis Gil
 Author-email: anamabo3@gmail.com, solocelis@gmail.com
 License: UNKNOWN
 Description: <p align="center">
          <img src="https://github.com/anamabo/HOBIT/blob/master/images/logo.png?raw=true" alt="Sublime's custom image"/>
@@ -20,17 +20,17 @@
         f(x) = y_0 + y_1 * Sin(omega * x + phi)
         f(x) = y_0 + y_1 * Cos(omega * x + phi)
         ```
         
         whose are commonly used to describe harmonic oscillators.
         
         ## Install
-        Install HOBIT-0.0.3-py2.py3-none-any.whl that you can find in dist folder using 
+        Install HOBIT 0.0.4
         ```
-        pip install HOBIT-0.0.3-py2.py3-none-any.whl
+        pip install HOBIT==0.0.4
         ```
         ### Requirements
         Hobit will install/update the next python libraries
         
         * pandas>=1.1.3
         * numpy>=1.19.2
         * hyperopt>=0.2.7
```

### Comparing `HOBIT-0.0.4/README.md` & `HOBIT-0.0.5/README.md`

 * *Files 8% similar despite different names*

```diff
@@ -12,17 +12,17 @@
 f(x) = y_0 + y_1 * Sin(omega * x + phi)
 f(x) = y_0 + y_1 * Cos(omega * x + phi)
 ```
 
 whose are commonly used to describe harmonic oscillators.
 
 ## Install
-Install HOBIT-0.0.3-py2.py3-none-any.whl that you can find in dist folder using 
+Install HOBIT 0.0.4
 ```
-pip install HOBIT-0.0.3-py2.py3-none-any.whl
+pip install HOBIT==0.0.4
 ```
 ### Requirements
 Hobit will install/update the next python libraries
 
 * pandas>=1.1.3
 * numpy>=1.19.2
 * hyperopt>=0.2.7
```

### Comparing `HOBIT-0.0.4/setup.py` & `HOBIT-0.0.5/setup.py`

 * *Files 11% similar despite different names*

```diff
@@ -4,15 +4,15 @@
 with open("requirements.txt") as f:
     requirements = f.read().splitlines()
 with open("README.md") as f:
     long_description = f.read()
 
 setup(
     name='HOBIT',
-    version='0.0.4',
+    version='0.0.5',
     description='an installable package for Hybrid fitting of Sine and Cosine functions',
     long_description=long_description,
     long_description_content_type='text/markdown',
     url='https://github.com/Harmonic-Oscillator-hyBrid-fIT/HOBIT',
     author='Carmen Adriana Martinez Barbosa, Jose Arturo Celis Gil',
     author_email='anamabo3@gmail.com, solocelis@gmail.com',
     packages=['HOBIT'],
```

