# Comparing `tmp/dcmetro-0.1.2.tar.gz` & `tmp/dcmetro-0.1.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dcmetro-0.1.2.tar", last modified: Fri Apr  7 00:40:02 2023, max compression
+gzip compressed data, was "dcmetro-0.1.3.tar", last modified: Fri Apr  7 00:47:13 2023, max compression
```

## Comparing `dcmetro-0.1.2.tar` & `dcmetro-0.1.3.tar`

### file list

```diff
@@ -1,24 +1,24 @@
-drwxr-xr-x   0 harunferaidon   (501) staff       (20)        0 2023-04-07 00:40:02.225430 dcmetro-0.1.2/
--rw-r--r--   0 harunferaidon   (501) staff       (20)     1061 2023-04-06 04:00:36.000000 dcmetro-0.1.2/LICENSE.txt
--rw-r--r--   0 harunferaidon   (501) staff       (20)     2619 2023-04-07 00:40:02.225589 dcmetro-0.1.2/PKG-INFO
--rw-r--r--   0 harunferaidon   (501) staff       (20)     2383 2023-04-07 00:39:35.000000 dcmetro-0.1.2/README.md
-drwxr-xr-x   0 harunferaidon   (501) staff       (20)        0 2023-04-07 00:40:02.221249 dcmetro-0.1.2/dcmetro.egg-info/
--rw-r--r--   0 harunferaidon   (501) staff       (20)     2619 2023-04-07 00:40:02.000000 dcmetro-0.1.2/dcmetro.egg-info/PKG-INFO
--rw-r--r--   0 harunferaidon   (501) staff       (20)      438 2023-04-07 00:40:02.000000 dcmetro-0.1.2/dcmetro.egg-info/SOURCES.txt
--rw-r--r--   0 harunferaidon   (501) staff       (20)        1 2023-04-07 00:40:02.000000 dcmetro-0.1.2/dcmetro.egg-info/dependency_links.txt
--rw-r--r--   0 harunferaidon   (501) staff       (20)       60 2023-04-07 00:40:02.000000 dcmetro-0.1.2/dcmetro.egg-info/entry_points.txt
--rw-r--r--   0 harunferaidon   (501) staff       (20)       27 2023-04-07 00:40:02.000000 dcmetro-0.1.2/dcmetro.egg-info/requires.txt
--rw-r--r--   0 harunferaidon   (501) staff       (20)        4 2023-04-07 00:40:02.000000 dcmetro-0.1.2/dcmetro.egg-info/top_level.txt
--rw-r--r--   0 harunferaidon   (501) staff       (20)       79 2023-04-07 00:40:02.226165 dcmetro-0.1.2/setup.cfg
--rw-r--r--   0 harunferaidon   (501) staff       (20)      707 2023-04-07 00:38:40.000000 dcmetro-0.1.2/setup.py
-drwxr-xr-x   0 harunferaidon   (501) staff       (20)        0 2023-04-07 00:40:02.221652 dcmetro-0.1.2/src/
--rw-r--r--   0 harunferaidon   (501) staff       (20)        0 2023-04-04 00:34:40.000000 dcmetro-0.1.2/src/__init__.py
-drwxr-xr-x   0 harunferaidon   (501) staff       (20)        0 2023-04-07 00:40:02.225022 dcmetro-0.1.2/src/main/
--rw-r--r--   0 harunferaidon   (501) staff       (20)        0 2023-03-28 20:16:32.000000 dcmetro-0.1.2/src/main/__init__.py
--rw-r--r--   0 harunferaidon   (501) staff       (20)     2260 2023-04-07 00:36:46.000000 dcmetro-0.1.2/src/main/app.py
--rw-r--r--   0 harunferaidon   (501) staff       (20)     1930 2023-04-06 04:00:36.000000 dcmetro-0.1.2/src/main/build_graph.py
--rw-r--r--   0 harunferaidon   (501) staff       (20)     6689 2023-04-07 00:33:34.000000 dcmetro-0.1.2/src/main/commands.py
--rw-r--r--   0 harunferaidon   (501) staff       (20)    11170 2023-04-04 05:08:25.000000 dcmetro-0.1.2/src/main/constants.py
--rw-r--r--   0 harunferaidon   (501) staff       (20)     1843 2023-04-04 00:34:40.000000 dcmetro-0.1.2/src/main/dijkstra.py
--rw-r--r--   0 harunferaidon   (501) staff       (20)      574 2023-04-04 05:08:25.000000 dcmetro-0.1.2/src/main/generate_station_codes.py
--rw-r--r--   0 harunferaidon   (501) staff       (20)     1098 2023-04-04 05:08:25.000000 dcmetro-0.1.2/src/main/get_station_distances.py
+drwxr-xr-x   0 harunferaidon   (501) staff       (20)        0 2023-04-07 00:47:13.442307 dcmetro-0.1.3/
+-rw-r--r--   0 harunferaidon   (501) staff       (20)     1061 2023-04-06 04:00:36.000000 dcmetro-0.1.3/LICENSE.txt
+-rw-r--r--   0 harunferaidon   (501) staff       (20)     2546 2023-04-07 00:47:13.442483 dcmetro-0.1.3/PKG-INFO
+-rw-r--r--   0 harunferaidon   (501) staff       (20)     2310 2023-04-07 00:46:51.000000 dcmetro-0.1.3/README.md
+drwxr-xr-x   0 harunferaidon   (501) staff       (20)        0 2023-04-07 00:47:13.422749 dcmetro-0.1.3/dcmetro.egg-info/
+-rw-r--r--   0 harunferaidon   (501) staff       (20)     2546 2023-04-07 00:47:13.000000 dcmetro-0.1.3/dcmetro.egg-info/PKG-INFO
+-rw-r--r--   0 harunferaidon   (501) staff       (20)      438 2023-04-07 00:47:13.000000 dcmetro-0.1.3/dcmetro.egg-info/SOURCES.txt
+-rw-r--r--   0 harunferaidon   (501) staff       (20)        1 2023-04-07 00:47:13.000000 dcmetro-0.1.3/dcmetro.egg-info/dependency_links.txt
+-rw-r--r--   0 harunferaidon   (501) staff       (20)       60 2023-04-07 00:47:13.000000 dcmetro-0.1.3/dcmetro.egg-info/entry_points.txt
+-rw-r--r--   0 harunferaidon   (501) staff       (20)       27 2023-04-07 00:47:13.000000 dcmetro-0.1.3/dcmetro.egg-info/requires.txt
+-rw-r--r--   0 harunferaidon   (501) staff       (20)        4 2023-04-07 00:47:13.000000 dcmetro-0.1.3/dcmetro.egg-info/top_level.txt
+-rw-r--r--   0 harunferaidon   (501) staff       (20)       79 2023-04-07 00:47:13.443096 dcmetro-0.1.3/setup.cfg
+-rw-r--r--   0 harunferaidon   (501) staff       (20)      707 2023-04-07 00:47:06.000000 dcmetro-0.1.3/setup.py
+drwxr-xr-x   0 harunferaidon   (501) staff       (20)        0 2023-04-07 00:47:13.423316 dcmetro-0.1.3/src/
+-rw-r--r--   0 harunferaidon   (501) staff       (20)        0 2023-04-04 00:34:40.000000 dcmetro-0.1.3/src/__init__.py
+drwxr-xr-x   0 harunferaidon   (501) staff       (20)        0 2023-04-07 00:47:13.441477 dcmetro-0.1.3/src/main/
+-rw-r--r--   0 harunferaidon   (501) staff       (20)        0 2023-03-28 20:16:32.000000 dcmetro-0.1.3/src/main/__init__.py
+-rw-r--r--   0 harunferaidon   (501) staff       (20)     2260 2023-04-07 00:36:46.000000 dcmetro-0.1.3/src/main/app.py
+-rw-r--r--   0 harunferaidon   (501) staff       (20)     1930 2023-04-06 04:00:36.000000 dcmetro-0.1.3/src/main/build_graph.py
+-rw-r--r--   0 harunferaidon   (501) staff       (20)     6689 2023-04-07 00:33:34.000000 dcmetro-0.1.3/src/main/commands.py
+-rw-r--r--   0 harunferaidon   (501) staff       (20)    11170 2023-04-04 05:08:25.000000 dcmetro-0.1.3/src/main/constants.py
+-rw-r--r--   0 harunferaidon   (501) staff       (20)     1843 2023-04-04 00:34:40.000000 dcmetro-0.1.3/src/main/dijkstra.py
+-rw-r--r--   0 harunferaidon   (501) staff       (20)      574 2023-04-04 05:08:25.000000 dcmetro-0.1.3/src/main/generate_station_codes.py
+-rw-r--r--   0 harunferaidon   (501) staff       (20)     1098 2023-04-04 05:08:25.000000 dcmetro-0.1.3/src/main/get_station_distances.py
```

### Comparing `dcmetro-0.1.2/LICENSE.txt` & `dcmetro-0.1.3/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `dcmetro-0.1.2/PKG-INFO` & `dcmetro-0.1.3/PKG-INFO`

 * *Files 11% similar despite different names*

```diff
@@ -1,22 +1,21 @@
 Metadata-Version: 2.1
 Name: dcmetro
-Version: 0.1.2
+Version: 0.1.3
 Summary: Console app for sending commands to get live information on the DC Metro
 Author: Harun Feraidon
 License: MIT
 Description-Content-Type: text/markdown
 License-File: LICENSE.txt
 
 # DC Metro Command Line Tool
-![gif not found, check images/demo.gif](images/demo.gif)
+![Imgur](https://i.imgur.com/rE4AKgU.gif)
 
 ## What is it
 With this application, you can submit concise commands via your terminal to request and then receive information.
-[PyPi page here](https://pypi.org/project/dcmetro/0.1.1/)
 
 ## Setup
 1. Setup a python virtual environment. `python3 -m venv venv`
 2. Activate your python virtual environment. `source venv/bin/activate`
 3. Install with `pip install dcmetro`.
 4. (OPTIONAL, BUT RECOMMENDED) Skipping this step means you will be using a community API key. Creating your own API token will be more reliable. Setup a WMATA API token [here](https://developer.wmata.com). Run `echo 'API_KEY = "<YOUR TOKEN HERE>"' > .env`
 5. Run `dcmetro` to start.
```

### Comparing `dcmetro-0.1.2/README.md` & `dcmetro-0.1.3/README.md`

 * *Files 3% similar despite different names*

```diff
@@ -1,13 +1,12 @@
 # DC Metro Command Line Tool
-![gif not found, check images/demo.gif](images/demo.gif)
+![Imgur](https://i.imgur.com/rE4AKgU.gif)
 
 ## What is it
 With this application, you can submit concise commands via your terminal to request and then receive information.
-[PyPi page here](https://pypi.org/project/dcmetro/0.1.1/)
 
 ## Setup
 1. Setup a python virtual environment. `python3 -m venv venv`
 2. Activate your python virtual environment. `source venv/bin/activate`
 3. Install with `pip install dcmetro`.
 4. (OPTIONAL, BUT RECOMMENDED) Skipping this step means you will be using a community API key. Creating your own API token will be more reliable. Setup a WMATA API token [here](https://developer.wmata.com). Run `echo 'API_KEY = "<YOUR TOKEN HERE>"' > .env`
 5. Run `dcmetro` to start.
```

### Comparing `dcmetro-0.1.2/dcmetro.egg-info/PKG-INFO` & `dcmetro-0.1.3/dcmetro.egg-info/PKG-INFO`

 * *Files 11% similar despite different names*

```diff
@@ -1,22 +1,21 @@
 Metadata-Version: 2.1
 Name: dcmetro
-Version: 0.1.2
+Version: 0.1.3
 Summary: Console app for sending commands to get live information on the DC Metro
 Author: Harun Feraidon
 License: MIT
 Description-Content-Type: text/markdown
 License-File: LICENSE.txt
 
 # DC Metro Command Line Tool
-![gif not found, check images/demo.gif](images/demo.gif)
+![Imgur](https://i.imgur.com/rE4AKgU.gif)
 
 ## What is it
 With this application, you can submit concise commands via your terminal to request and then receive information.
-[PyPi page here](https://pypi.org/project/dcmetro/0.1.1/)
 
 ## Setup
 1. Setup a python virtual environment. `python3 -m venv venv`
 2. Activate your python virtual environment. `source venv/bin/activate`
 3. Install with `pip install dcmetro`.
 4. (OPTIONAL, BUT RECOMMENDED) Skipping this step means you will be using a community API key. Creating your own API token will be more reliable. Setup a WMATA API token [here](https://developer.wmata.com). Run `echo 'API_KEY = "<YOUR TOKEN HERE>"' > .env`
 5. Run `dcmetro` to start.
```

### Comparing `dcmetro-0.1.2/setup.py` & `dcmetro-0.1.3/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -3,15 +3,15 @@
 
 with open(os.path.join(os.path.dirname(__file__), "README.md"), "r") as f:
     long_description = f.read()
 
 setup(
     name='dcmetro',
     packages=find_packages(include=["src", "src.main"]),
-    version='0.1.2',
+    version='0.1.3',
     description='Console app for sending commands to get live information on the DC Metro',
     long_description=long_description,
     long_description_content_type="text/markdown",
     author='Harun Feraidon',
     license='MIT',
     entry_points={
         "console_scripts": [
```

### Comparing `dcmetro-0.1.2/src/main/app.py` & `dcmetro-0.1.3/src/main/app.py`

 * *Files identical despite different names*

### Comparing `dcmetro-0.1.2/src/main/build_graph.py` & `dcmetro-0.1.3/src/main/build_graph.py`

 * *Files identical despite different names*

### Comparing `dcmetro-0.1.2/src/main/commands.py` & `dcmetro-0.1.3/src/main/commands.py`

 * *Files identical despite different names*

### Comparing `dcmetro-0.1.2/src/main/constants.py` & `dcmetro-0.1.3/src/main/constants.py`

 * *Files identical despite different names*

### Comparing `dcmetro-0.1.2/src/main/dijkstra.py` & `dcmetro-0.1.3/src/main/dijkstra.py`

 * *Files identical despite different names*

### Comparing `dcmetro-0.1.2/src/main/generate_station_codes.py` & `dcmetro-0.1.3/src/main/generate_station_codes.py`

 * *Files identical despite different names*

### Comparing `dcmetro-0.1.2/src/main/get_station_distances.py` & `dcmetro-0.1.3/src/main/get_station_distances.py`

 * *Files identical despite different names*

