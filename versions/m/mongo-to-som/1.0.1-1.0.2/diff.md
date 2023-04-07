# Comparing `tmp/mongo_to_som-1.0.1.tar.gz` & `tmp/mongo_to_som-1.0.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "mongo_to_som-1.0.1.tar", last modified: Fri Apr  7 14:00:22 2023, max compression
+gzip compressed data, was "mongo_to_som-1.0.2.tar", last modified: Fri Apr  7 14:04:14 2023, max compression
```

## Comparing `mongo_to_som-1.0.1.tar` & `mongo_to_som-1.0.2.tar`

### file list

```diff
@@ -1,14 +1,14 @@
-drwxrwxrwx   0        0        0        0 2023-04-07 14:00:22.811814 mongo_to_som-1.0.1/
--rw-rw-rw-   0        0        0     1143 2023-04-07 14:00:22.811814 mongo_to_som-1.0.1/PKG-INFO
--rw-rw-rw-   0        0        0      395 2023-04-07 12:24:07.000000 mongo_to_som-1.0.1/README.md
-drwxrwxrwx   0        0        0        0 2023-04-07 14:00:22.805814 mongo_to_som-1.0.1/mongo_to_som/
--rw-rw-rw-   0        0        0       48 2023-04-07 11:54:33.000000 mongo_to_som-1.0.1/mongo_to_som/__init__.py
--rw-rw-rw-   0        0        0     7405 2023-04-07 12:10:25.000000 mongo_to_som-1.0.1/mongo_to_som/mongotosom.py
-drwxrwxrwx   0        0        0        0 2023-04-07 14:00:22.810814 mongo_to_som-1.0.1/mongo_to_som.egg-info/
--rw-rw-rw-   0        0        0     1143 2023-04-07 14:00:22.000000 mongo_to_som-1.0.1/mongo_to_som.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      249 2023-04-07 14:00:22.000000 mongo_to_som-1.0.1/mongo_to_som.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-07 14:00:22.000000 mongo_to_som-1.0.1/mongo_to_som.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       51 2023-04-07 14:00:22.000000 mongo_to_som-1.0.1/mongo_to_som.egg-info/requires.txt
--rw-rw-rw-   0        0        0       13 2023-04-07 14:00:22.000000 mongo_to_som-1.0.1/mongo_to_som.egg-info/top_level.txt
--rw-rw-rw-   0        0        0       42 2023-04-07 14:00:22.811814 mongo_to_som-1.0.1/setup.cfg
--rw-rw-rw-   0        0        0     1451 2023-04-07 13:59:20.000000 mongo_to_som-1.0.1/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-07 14:04:14.290702 mongo_to_som-1.0.2/
+-rw-rw-rw-   0        0        0     1143 2023-04-07 14:04:14.290702 mongo_to_som-1.0.2/PKG-INFO
+-rw-rw-rw-   0        0        0      395 2023-04-07 12:24:07.000000 mongo_to_som-1.0.2/README.md
+drwxrwxrwx   0        0        0        0 2023-04-07 14:04:14.282703 mongo_to_som-1.0.2/mongo_to_som/
+-rw-rw-rw-   0        0        0       48 2023-04-07 11:54:33.000000 mongo_to_som-1.0.2/mongo_to_som/__init__.py
+-rw-rw-rw-   0        0        0     7405 2023-04-07 12:10:25.000000 mongo_to_som-1.0.2/mongo_to_som/mongotosom.py
+drwxrwxrwx   0        0        0        0 2023-04-07 14:04:14.288700 mongo_to_som-1.0.2/mongo_to_som.egg-info/
+-rw-rw-rw-   0        0        0     1143 2023-04-07 14:04:14.000000 mongo_to_som-1.0.2/mongo_to_som.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      249 2023-04-07 14:04:14.000000 mongo_to_som-1.0.2/mongo_to_som.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-07 14:04:14.000000 mongo_to_som-1.0.2/mongo_to_som.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       51 2023-04-07 14:04:14.000000 mongo_to_som-1.0.2/mongo_to_som.egg-info/requires.txt
+-rw-rw-rw-   0        0        0       13 2023-04-07 14:04:14.000000 mongo_to_som-1.0.2/mongo_to_som.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0       42 2023-04-07 14:04:14.290702 mongo_to_som-1.0.2/setup.cfg
+-rw-rw-rw-   0        0        0     1428 2023-04-07 14:04:12.000000 mongo_to_som-1.0.2/setup.py
```

### Comparing `mongo_to_som-1.0.1/PKG-INFO` & `mongo_to_som-1.0.2/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: mongo_to_som
-Version: 1.0.1
+Version: 1.0.2
 Summary: Library to create Self-Organizing Map from MongoDB collection
 Home-page: UNKNOWN
 Author: Tomáš Peregrín
 Author-email: djtoso@gmail.com
 License: MIT
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

### Comparing `mongo_to_som-1.0.1/mongo_to_som/mongotosom.py` & `mongo_to_som-1.0.2/mongo_to_som/mongotosom.py`

 * *Files identical despite different names*

### Comparing `mongo_to_som-1.0.1/mongo_to_som.egg-info/PKG-INFO` & `mongo_to_som-1.0.2/mongo_to_som.egg-info/PKG-INFO`

 * *Files 11% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: mongo-to-som
-Version: 1.0.1
+Version: 1.0.2
 Summary: Library to create Self-Organizing Map from MongoDB collection
 Home-page: UNKNOWN
 Author: Tomáš Peregrín
 Author-email: djtoso@gmail.com
 License: MIT
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

### Comparing `mongo_to_som-1.0.1/setup.py` & `mongo_to_som-1.0.2/setup.py`

 * *Files 10% similar despite different names*

```diff
@@ -6,18 +6,18 @@
 HERE = path.abspath(path.dirname(__file__))
 
 # Get the long description from the README file
 with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
     long_description = f.read()
 
 setup(
-    name='mongo_to_som',
-    packages=find_packages(include=['mongo_to_som']),
+    name="mongo_to_som",
+    packages=["mongo_to_som"],
     include_package_data=True,
-    version='1.0.1',
+    version='1.0.2',
     description='Library to create Self-Organizing Map from MongoDB collection',
     long_description=long_description,
     long_description_content_type="text/markdown",
     author='Tomáš Peregrín',
     author_email="djtoso@gmail.com",
     license='MIT',
     classifiers=[
```

