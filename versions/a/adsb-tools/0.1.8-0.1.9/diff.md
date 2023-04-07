# Comparing `tmp/adsb_tools-0.1.8.tar.gz` & `tmp/adsb_tools-0.1.9.tar.gz`

## Comparing `adsb_tools-0.1.8.tar` & `adsb_tools-0.1.9.tar`

### file list

```diff
@@ -1,12 +1,15 @@
--rw-r--r--   0        0        0       64 2020-02-02 00:00:00.000000 adsb_tools-0.1.8/requirements.txt
--rw-r--r--   0        0        0     2986 2020-02-02 00:00:00.000000 adsb_tools-0.1.8/docs/README.md
--rw-r--r--   0        0        0     7744 2020-02-02 00:00:00.000000 adsb_tools-0.1.8/docs/aircraft.md
--rw-r--r--   0        0        0      849 2020-02-02 00:00:00.000000 adsb_tools-0.1.8/src/setup.py
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 adsb_tools-0.1.8/src/adsb_tools/__init__.py
--rw-r--r--   0        0        0     3962 2020-02-02 00:00:00.000000 adsb_tools-0.1.8/src/adsb_tools/aircraft.py
--rw-r--r--   0        0        0      217 2020-02-02 00:00:00.000000 adsb_tools-0.1.8/src/adsb_tools/receiver.py
--rw-r--r--   0        0        0      273 2020-02-02 00:00:00.000000 adsb_tools-0.1.8/src/adsb_tools/timezone.py
--rw-r--r--   0        0        0     1237 2020-02-02 00:00:00.000000 adsb_tools-0.1.8/.gitignore
--rw-r--r--   0        0        0      129 2020-02-02 00:00:00.000000 adsb_tools-0.1.8/README.md
--rw-r--r--   0        0        0      699 2020-02-02 00:00:00.000000 adsb_tools-0.1.8/pyproject.toml
--rw-r--r--   0        0        0      744 2020-02-02 00:00:00.000000 adsb_tools-0.1.8/PKG-INFO
+-rw-r--r--   0        0        0       79 2020-02-02 00:00:00.000000 adsb_tools-0.1.9/requirements.txt
+-rw-r--r--   0        0        0     2986 2020-02-02 00:00:00.000000 adsb_tools-0.1.9/docs/README.md
+-rw-r--r--   0        0        0     7744 2020-02-02 00:00:00.000000 adsb_tools-0.1.9/docs/aircraft.md
+-rw-r--r--   0        0        0      875 2020-02-02 00:00:00.000000 adsb_tools-0.1.9/src/setup.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 adsb_tools-0.1.9/src/adsb_tools/__init__.py
+-rw-r--r--   0        0        0     3962 2020-02-02 00:00:00.000000 adsb_tools-0.1.9/src/adsb_tools/aircraft.py
+-rw-r--r--   0        0        0      217 2020-02-02 00:00:00.000000 adsb_tools-0.1.9/src/adsb_tools/receiver.py
+-rw-r--r--   0        0        0      273 2020-02-02 00:00:00.000000 adsb_tools-0.1.9/src/adsb_tools/timezone.py
+-rw-r--r--   0        0        0     3064 2020-02-02 00:00:00.000000 adsb_tools-0.1.9/src/adsb_tools/weather.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 adsb_tools-0.1.9/src/adsb_tools/utils/__init__.py
+-rw-r--r--   0        0        0      941 2020-02-02 00:00:00.000000 adsb_tools-0.1.9/src/adsb_tools/utils/requests_utils.py
+-rw-r--r--   0        0        0     1237 2020-02-02 00:00:00.000000 adsb_tools-0.1.9/.gitignore
+-rw-r--r--   0        0        0      129 2020-02-02 00:00:00.000000 adsb_tools-0.1.9/README.md
+-rw-r--r--   0        0        0      699 2020-02-02 00:00:00.000000 adsb_tools-0.1.9/pyproject.toml
+-rw-r--r--   0        0        0      744 2020-02-02 00:00:00.000000 adsb_tools-0.1.9/PKG-INFO
```

### Comparing `adsb_tools-0.1.8/docs/README.md` & `adsb_tools-0.1.9/docs/README.md`

 * *Files identical despite different names*

### Comparing `adsb_tools-0.1.8/docs/aircraft.md` & `adsb_tools-0.1.9/docs/aircraft.md`

 * *Files identical despite different names*

### Comparing `adsb_tools-0.1.8/src/setup.py` & `adsb_tools-0.1.9/src/setup.py`

 * *Files 12% similar despite different names*

```diff
@@ -3,20 +3,21 @@
 # read the contents of your README file
 from pathlib import Path
 this_directory = Path(__file__).parent
 long_description = (this_directory / "README.md").read_text()
 
 setup(
     name='adsb_tools',
-    version='0.1.8',
+    version='0.1.9',
     packages=['adsb_tools'],
     python_requires='>=3.7',
     install_requires=[
         'requests',
-        'pytz'
+        'pytz',
+        'timezonefinder'
     ],
     author='herereadthis',
     author_email='herereadthis.github@gmail.com',
     description='Various tools for handling ADS-B data coming from Dump1090 messages',
     long_description=long_description,
     long_description_content_type='text/markdown',
     url='https://github.com/herereadthis/adsb_tools',
```

### Comparing `adsb_tools-0.1.8/src/adsb_tools/aircraft.py` & `adsb_tools-0.1.9/src/adsb_tools/aircraft.py`

 * *Files identical despite different names*

### Comparing `adsb_tools-0.1.8/.gitignore` & `adsb_tools-0.1.9/.gitignore`

 * *Files identical despite different names*

### Comparing `adsb_tools-0.1.8/pyproject.toml` & `adsb_tools-0.1.9/pyproject.toml`

 * *Files 14% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 [build-system]
 requires = ["hatchling"]
 build-backend = "hatchling.build"
 
 [project]
 name = "adsb_tools"
-version = "0.1.8"
+version = "0.1.9"
 authors = [
     { name="herereadthis", email="herereadthis.github@gmail.com" },
 ]
 description = "ADS-B tools for reading Dump1090 messages"
 readme = "README.md"
 requires-python = ">=3.7"
 classifiers = [
```

### Comparing `adsb_tools-0.1.8/PKG-INFO` & `adsb_tools-0.1.9/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: adsb_tools
-Version: 0.1.8
+Version: 0.1.9
 Summary: ADS-B tools for reading Dump1090 messages
 Project-URL: Homepage, https://github.com/herereadthis/adsb_tools
 Project-URL: Bug Tracker, https://github.com/herereadthis/adsb_tools/issues
 Author-email: herereadthis <herereadthis.github@gmail.com>
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
 Classifier: Programming Language :: Python :: 3
```

