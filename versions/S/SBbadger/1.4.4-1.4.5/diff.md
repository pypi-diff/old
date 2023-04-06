# Comparing `tmp/SBbadger-1.4.4.tar.gz` & `tmp/SBbadger-1.4.5.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/SBbadger-1.4.4.tar", last modified: Tue Apr  4 10:41:22 2023, max compression
+gzip compressed data, was "dist/SBbadger-1.4.5.tar", last modified: Thu Apr  6 22:13:52 2023, max compression
```

## Comparing `SBbadger-1.4.4.tar` & `SBbadger-1.4.5.tar`

### file list

```diff
@@ -1,20 +1,20 @@
-drwxrwxr-x   0 michael   (1000) michael   (1000)        0 2023-04-04 10:41:22.000000 SBbadger-1.4.4/
--rw-rw-r--   0 michael   (1000) michael   (1000)     1070 2023-03-01 06:54:41.000000 SBbadger-1.4.4/LICENSE
--rw-rw-r--   0 michael   (1000) michael   (1000)     5939 2023-04-04 10:41:22.000000 SBbadger-1.4.4/PKG-INFO
--rw-rw-r--   0 michael   (1000) michael   (1000)     5127 2023-03-01 06:54:41.000000 SBbadger-1.4.4/README.md
-drwxrwxr-x   0 michael   (1000) michael   (1000)        0 2023-04-04 10:41:22.000000 SBbadger-1.4.4/SBbadger/
--rw-rw-r--   0 michael   (1000) michael   (1000)      160 2023-03-01 06:54:41.000000 SBbadger-1.4.4/SBbadger/__init__.py
--rw-rw-r--   0 michael   (1000) michael   (1000)       21 2023-04-04 10:39:41.000000 SBbadger-1.4.4/SBbadger/_version.py
--rw-rw-r--   0 michael   (1000) michael   (1000)   571043 2023-04-04 10:35:11.000000 SBbadger-1.4.4/SBbadger/buildNetworks.py
--rw-rw-r--   0 michael   (1000) michael   (1000)   123113 2023-04-01 04:44:06.000000 SBbadger-1.4.4/SBbadger/generate.py
--rw-rw-r--   0 michael   (1000) michael   (1000)   120769 2023-04-01 04:44:06.000000 SBbadger-1.4.4/SBbadger/generate_serial.py
--rw-rw-r--   0 michael   (1000) michael   (1000)     2226 2023-04-04 10:35:50.000000 SBbadger-1.4.4/SBbadger/mass_action.py
-drwxrwxr-x   0 michael   (1000) michael   (1000)        0 2023-04-04 10:41:22.000000 SBbadger-1.4.4/SBbadger.egg-info/
--rw-rw-r--   0 michael   (1000) michael   (1000)     5939 2023-04-04 10:41:22.000000 SBbadger-1.4.4/SBbadger.egg-info/PKG-INFO
--rw-rw-r--   0 michael   (1000) michael   (1000)      351 2023-04-04 10:41:22.000000 SBbadger-1.4.4/SBbadger.egg-info/SOURCES.txt
--rw-rw-r--   0 michael   (1000) michael   (1000)        1 2023-04-04 10:41:22.000000 SBbadger-1.4.4/SBbadger.egg-info/dependency_links.txt
--rw-rw-r--   0 michael   (1000) michael   (1000)       38 2023-04-04 10:41:22.000000 SBbadger-1.4.4/SBbadger.egg-info/requires.txt
--rw-rw-r--   0 michael   (1000) michael   (1000)        9 2023-04-04 10:41:22.000000 SBbadger-1.4.4/SBbadger.egg-info/top_level.txt
--rw-rw-r--   0 michael   (1000) michael   (1000)      101 2023-03-01 06:54:41.000000 SBbadger-1.4.4/pyproject.toml
--rw-rw-r--   0 michael   (1000) michael   (1000)       79 2023-04-04 10:41:22.000000 SBbadger-1.4.4/setup.cfg
--rw-rw-r--   0 michael   (1000) michael   (1000)     1964 2023-04-04 10:39:41.000000 SBbadger-1.4.4/setup.py
+drwxrwxr-x   0 michael   (1000) michael   (1000)        0 2023-04-06 22:13:52.000000 SBbadger-1.4.5/
+-rw-rw-r--   0 michael   (1000) michael   (1000)     1070 2023-03-01 06:54:41.000000 SBbadger-1.4.5/LICENSE
+-rw-rw-r--   0 michael   (1000) michael   (1000)     5939 2023-04-06 22:13:52.000000 SBbadger-1.4.5/PKG-INFO
+-rw-rw-r--   0 michael   (1000) michael   (1000)     5127 2023-03-01 06:54:41.000000 SBbadger-1.4.5/README.md
+drwxrwxr-x   0 michael   (1000) michael   (1000)        0 2023-04-06 22:13:52.000000 SBbadger-1.4.5/SBbadger/
+-rw-rw-r--   0 michael   (1000) michael   (1000)      160 2023-03-01 06:54:41.000000 SBbadger-1.4.5/SBbadger/__init__.py
+-rw-rw-r--   0 michael   (1000) michael   (1000)       21 2023-04-06 22:07:36.000000 SBbadger-1.4.5/SBbadger/_version.py
+-rw-rw-r--   0 michael   (1000) michael   (1000)   572047 2023-04-06 22:07:37.000000 SBbadger-1.4.5/SBbadger/buildNetworks.py
+-rw-rw-r--   0 michael   (1000) michael   (1000)   123113 2023-04-01 04:44:06.000000 SBbadger-1.4.5/SBbadger/generate.py
+-rw-rw-r--   0 michael   (1000) michael   (1000)   120769 2023-04-01 04:44:06.000000 SBbadger-1.4.5/SBbadger/generate_serial.py
+-rw-rw-r--   0 michael   (1000) michael   (1000)     2226 2023-04-04 10:35:50.000000 SBbadger-1.4.5/SBbadger/mass_action.py
+drwxrwxr-x   0 michael   (1000) michael   (1000)        0 2023-04-06 22:13:52.000000 SBbadger-1.4.5/SBbadger.egg-info/
+-rw-rw-r--   0 michael   (1000) michael   (1000)     5939 2023-04-06 22:13:52.000000 SBbadger-1.4.5/SBbadger.egg-info/PKG-INFO
+-rw-rw-r--   0 michael   (1000) michael   (1000)      351 2023-04-06 22:13:52.000000 SBbadger-1.4.5/SBbadger.egg-info/SOURCES.txt
+-rw-rw-r--   0 michael   (1000) michael   (1000)        1 2023-04-06 22:13:52.000000 SBbadger-1.4.5/SBbadger.egg-info/dependency_links.txt
+-rw-rw-r--   0 michael   (1000) michael   (1000)       38 2023-04-06 22:13:52.000000 SBbadger-1.4.5/SBbadger.egg-info/requires.txt
+-rw-rw-r--   0 michael   (1000) michael   (1000)        9 2023-04-06 22:13:52.000000 SBbadger-1.4.5/SBbadger.egg-info/top_level.txt
+-rw-rw-r--   0 michael   (1000) michael   (1000)      101 2023-03-01 06:54:41.000000 SBbadger-1.4.5/pyproject.toml
+-rw-rw-r--   0 michael   (1000) michael   (1000)       79 2023-04-06 22:13:52.000000 SBbadger-1.4.5/setup.cfg
+-rw-rw-r--   0 michael   (1000) michael   (1000)     1964 2023-04-06 22:07:36.000000 SBbadger-1.4.5/setup.py
```

### Comparing `SBbadger-1.4.4/LICENSE` & `SBbadger-1.4.5/LICENSE`

 * *Files identical despite different names*

### Comparing `SBbadger-1.4.4/PKG-INFO` & `SBbadger-1.4.5/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 Metadata-Version: 2.1
 Name: SBbadger
-Version: 1.4.4
+Version: 1.4.5
 Summary: Synthetic biochemical reaction networks with definable degree distributions.
 Home-page: https://github.com/sys-bio/SBbadger
-Download-URL: https://github.com/sys-bio/SBbadger/archive/refs/tags/v1.4.4.tar.gz
+Download-URL: https://github.com/sys-bio/SBbadger/archive/refs/tags/v1.4.5.tar.gz
 Author: Michael Kochen
 Author-email: kochenma@uw.edu
 License: Apache
 Keywords: Systems biology,Benchmark Models
 Classifier: Development Status :: 5 - Production/Stable
 Classifier: Intended Audience :: Developers
 Classifier: Topic :: Software Development :: Build Tools
```

### Comparing `SBbadger-1.4.4/README.md` & `SBbadger-1.4.5/README.md`

 * *Files identical despite different names*

### Comparing `SBbadger-1.4.4/SBbadger/buildNetworks.py` & `SBbadger-1.4.5/SBbadger/buildNetworks.py`

 * *Files 0% similar despite different names*

```diff
@@ -11329,15 +11329,35 @@
             ic_str += each + ' = ' + str(ic) + '\n'
         if source is None:
             ic = uniform.rvs(loc=0, scale=10)
             ic_str += each + ' = ' + str(ic) + '\n'
 
     for each in b_sink:
         if each not in b_source:
-            ic_str += each + ' = 0\n'
+            if ic_params == 'trivial':
+                ic_str += each + ' = 1\n'
+            if isinstance(sink, list) and sink[1] == 'uniform':
+                ic = uniform.rvs(loc=sink[2], scale=sink[3]-sink[3])
+                ic_str += each + ' = ' + str(ic) + '\n'
+            if isinstance(sink, list) and sink[1] == 'loguniform':
+                ic = loguniform.rvs(sink[2], sink[3])
+                ic_str += each + ' = ' + str(ic) + '\n'
+            if isinstance(sink, list) and sink[1] == 'normal':
+                ic = norm.rvs(loc=sink[2], scale=sink[3])
+                ic_str += each + ' = ' + str(ic) + '\n'
+            if isinstance(sink, list) and sink[1] == 'lognormal':
+                ic = lognorm.rvs(scale=sink[2], s=sink[3])
+                ic_str += each + ' = ' + str(ic) + '\n'
+            if sink is None:
+                ic = uniform.rvs(loc=0, scale=10)
+                ic_str += each + ' = ' + str(ic) + '\n'
+
+    # for each in b_sink:
+    #     if each not in b_source:
+    #         ic_str += each + ' = 0\n'
 
     # for each in b_sink:
     #     if sink == 'trivial':
     #         ic_str += each + ' = 1\n'
     #     if isinstance(sink, list) and sink[1] == 'uniform':
     #         ic = uniform.rvs(loc=sink[2], scale=sink[3]-sink[2])
     #         ic_str += each + ' = ' + str(ic) + '\n'
```

### Comparing `SBbadger-1.4.4/SBbadger/generate.py` & `SBbadger-1.4.5/SBbadger/generate.py`

 * *Files identical despite different names*

### Comparing `SBbadger-1.4.4/SBbadger/generate_serial.py` & `SBbadger-1.4.5/SBbadger/generate_serial.py`

 * *Files identical despite different names*

### Comparing `SBbadger-1.4.4/SBbadger/mass_action.py` & `SBbadger-1.4.5/SBbadger/mass_action.py`

 * *Files identical despite different names*

### Comparing `SBbadger-1.4.4/SBbadger.egg-info/PKG-INFO` & `SBbadger-1.4.5/SBbadger.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 Metadata-Version: 2.1
 Name: SBbadger
-Version: 1.4.4
+Version: 1.4.5
 Summary: Synthetic biochemical reaction networks with definable degree distributions.
 Home-page: https://github.com/sys-bio/SBbadger
-Download-URL: https://github.com/sys-bio/SBbadger/archive/refs/tags/v1.4.4.tar.gz
+Download-URL: https://github.com/sys-bio/SBbadger/archive/refs/tags/v1.4.5.tar.gz
 Author: Michael Kochen
 Author-email: kochenma@uw.edu
 License: Apache
 Keywords: Systems biology,Benchmark Models
 Classifier: Development Status :: 5 - Production/Stable
 Classifier: Intended Audience :: Developers
 Classifier: Topic :: Software Development :: Build Tools
```

### Comparing `SBbadger-1.4.4/setup.py` & `SBbadger-1.4.5/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -32,15 +32,15 @@
     license='Apache',
     description='Synthetic biochemical reaction networks with definable degree distributions.',
     long_description=long_description,
     long_description_content_type='text/markdown',
     author='Michael Kochen',
     author_email='kochenma@uw.edu',
     url='https://github.com/sys-bio/SBbadger',
-    download_url='https://github.com/sys-bio/SBbadger/archive/refs/tags/v1.4.4.tar.gz',
+    download_url='https://github.com/sys-bio/SBbadger/archive/refs/tags/v1.4.5.tar.gz',
     keywords=['Systems biology', 'Benchmark Models'],
     install_requires=[
         'numpy',
         'scipy',
         'antimony',
         'matplotlib',
         'pydot',
```

