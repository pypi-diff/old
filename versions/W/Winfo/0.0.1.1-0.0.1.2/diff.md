# Comparing `tmp/Winfo-0.0.1.1.tar.gz` & `tmp/Winfo-0.0.1.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "Winfo-0.0.1.1.tar", last modified: Fri Apr  7 13:24:35 2023, max compression
+gzip compressed data, was "Winfo-0.0.1.2.tar", last modified: Fri Apr  7 13:57:37 2023, max compression
```

## Comparing `Winfo-0.0.1.1.tar` & `Winfo-0.0.1.2.tar`

### file list

```diff
@@ -1,18 +1,13 @@
-drwxrwxrwx   0        0        0        0 2023-04-07 13:24:35.823617 Winfo-0.0.1.1/
--rw-rw-rw-   0        0        0     1156 2023-04-07 10:35:15.000000 Winfo-0.0.1.1/LICENSE
--rw-rw-rw-   0        0        0     4296 2023-04-07 13:24:35.823617 Winfo-0.0.1.1/PKG-INFO
--rw-rw-rw-   0        0        0     3803 2023-04-07 09:58:38.000000 Winfo-0.0.1.1/README.md
-drwxrwxrwx   0        0        0        0 2023-04-07 13:24:35.801742 Winfo-0.0.1.1/Winfo/
--rw-rw-rw-   0        0        0     2515 2023-04-07 09:10:20.000000 Winfo-0.0.1.1/Winfo/__init__.py
--rw-rw-rw-   0        0        0     1106 2023-04-07 09:19:27.000000 Winfo-0.0.1.1/Winfo/cpu.py
--rw-rw-rw-   0        0        0      993 2023-04-07 09:26:01.000000 Winfo-0.0.1.1/Winfo/disk.py
--rw-rw-rw-   0        0        0      259 2023-04-06 22:15:29.000000 Winfo-0.0.1.1/Winfo/gpu.py
--rw-rw-rw-   0        0        0      951 2023-04-07 09:22:02.000000 Winfo-0.0.1.1/Winfo/memory.py
--rw-rw-rw-   0        0        0     1122 2023-04-06 22:14:47.000000 Winfo-0.0.1.1/Winfo/software.py
-drwxrwxrwx   0        0        0        0 2023-04-07 13:24:35.820033 Winfo-0.0.1.1/Winfo.egg-info/
--rw-rw-rw-   0        0        0     4296 2023-04-07 13:24:35.000000 Winfo-0.0.1.1/Winfo.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      234 2023-04-07 13:24:35.000000 Winfo-0.0.1.1/Winfo.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-07 13:24:35.000000 Winfo-0.0.1.1/Winfo.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0        6 2023-04-07 13:24:35.000000 Winfo-0.0.1.1/Winfo.egg-info/top_level.txt
--rw-rw-rw-   0        0        0       42 2023-04-07 13:24:35.824614 Winfo-0.0.1.1/setup.cfg
--rw-rw-rw-   0        0        0      728 2023-04-07 12:00:09.000000 Winfo-0.0.1.1/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-07 13:57:37.810587 Winfo-0.0.1.2/
+-rw-rw-rw-   0        0        0     1156 2023-04-07 10:35:15.000000 Winfo-0.0.1.2/LICENSE
+-rw-rw-rw-   0        0        0     4296 2023-04-07 13:57:37.809587 Winfo-0.0.1.2/PKG-INFO
+-rw-rw-rw-   0        0        0     3803 2023-04-07 09:58:38.000000 Winfo-0.0.1.2/README.md
+drwxrwxrwx   0        0        0        0 2023-04-07 13:57:37.790586 Winfo-0.0.1.2/Winfo/
+-rw-rw-rw-   0        0        0     6855 2023-04-07 13:49:40.000000 Winfo-0.0.1.2/Winfo/__init__.py
+drwxrwxrwx   0        0        0        0 2023-04-07 13:57:37.808585 Winfo-0.0.1.2/Winfo.egg-info/
+-rw-rw-rw-   0        0        0     4296 2023-04-07 13:57:37.000000 Winfo-0.0.1.2/Winfo.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      160 2023-04-07 13:57:37.000000 Winfo-0.0.1.2/Winfo.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-07 13:57:37.000000 Winfo-0.0.1.2/Winfo.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0        6 2023-04-07 13:57:37.000000 Winfo-0.0.1.2/Winfo.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0       42 2023-04-07 13:57:37.810587 Winfo-0.0.1.2/setup.cfg
+-rw-rw-rw-   0        0        0      728 2023-04-07 13:54:42.000000 Winfo-0.0.1.2/setup.py
```

### Comparing `Winfo-0.0.1.1/LICENSE` & `Winfo-0.0.1.2/LICENSE`

 * *Files identical despite different names*

### Comparing `Winfo-0.0.1.1/PKG-INFO` & `Winfo-0.0.1.2/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: Winfo
-Version: 0.0.1.1
+Version: 0.0.1.2
 Summary: Get information about your windows system
 Author: BLUEAMETHYST Studios
 Author-email: simon.schoeneberg@t-online.de
 Keywords: python,windows,util,information,system
 Classifier: Development Status :: 1 - Planning
 Classifier: Intended Audience :: Developers
 Classifier: Programming Language :: Python :: 3
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: Winfo Version: 0.0.1.1 Summary: Get information
+Metadata-Version: 2.1 Name: Winfo Version: 0.0.1.2 Summary: Get information
 about your windows system Author: BLUEAMETHYST Studios Author-email:
 simon.schoeneberg@t-online.de Keywords: python,windows,util,information,system
 Classifier: Development Status :: 1 - Planning Classifier: Intended Audience ::
 Developers Classifier: Programming Language :: Python :: 3 Classifier:
 Operating System :: Microsoft :: Windows Description-Content-Type: text/
 markdown License-File: LICENSE # Winfo Winfo is a Python Library for getting
 System Stats (Made for Windows) ## Features List of all features: ### Processor
```

### Comparing `Winfo-0.0.1.1/README.md` & `Winfo-0.0.1.2/README.md`

 * *Files identical despite different names*

### Comparing `Winfo-0.0.1.1/Winfo.egg-info/PKG-INFO` & `Winfo-0.0.1.2/Winfo.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: Winfo
-Version: 0.0.1.1
+Version: 0.0.1.2
 Summary: Get information about your windows system
 Author: BLUEAMETHYST Studios
 Author-email: simon.schoeneberg@t-online.de
 Keywords: python,windows,util,information,system
 Classifier: Development Status :: 1 - Planning
 Classifier: Intended Audience :: Developers
 Classifier: Programming Language :: Python :: 3
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: Winfo Version: 0.0.1.1 Summary: Get information
+Metadata-Version: 2.1 Name: Winfo Version: 0.0.1.2 Summary: Get information
 about your windows system Author: BLUEAMETHYST Studios Author-email:
 simon.schoeneberg@t-online.de Keywords: python,windows,util,information,system
 Classifier: Development Status :: 1 - Planning Classifier: Intended Audience ::
 Developers Classifier: Programming Language :: Python :: 3 Classifier:
 Operating System :: Microsoft :: Windows Description-Content-Type: text/
 markdown License-File: LICENSE # Winfo Winfo is a Python Library for getting
 System Stats (Made for Windows) ## Features List of all features: ### Processor
```

### Comparing `Winfo-0.0.1.1/setup.py` & `Winfo-0.0.1.2/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -2,15 +2,15 @@
 
 with open("README.md", "r") as f:
     readme = f.read()
     f.close()
     
 setup(
     name="Winfo",
-    version="0.0.1.1",
+    version="0.0.1.2",
     author="BLUEAMETHYST Studios",
     author_email="simon.schoeneberg@t-online.de",
     description="Get information about your windows system",
     long_description_content_type="text/markdown",
     long_description=readme,
     packages=find_packages(),
     keywords=['python', 'windows', 'util', 'information', 'system'],
```

