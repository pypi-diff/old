# Comparing `tmp/mbox-to-json-0.0.2.tar.gz` & `tmp/mbox-to-json-1.0.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "mbox-to-json-0.0.2.tar", last modified: Thu Apr  6 14:57:29 2023, max compression
+gzip compressed data, was "mbox-to-json-1.0.0.tar", last modified: Sat Apr  1 12:58:00 2023, max compression
```

## Comparing `mbox-to-json-0.0.2.tar` & `mbox-to-json-1.0.0.tar`

### file list

```diff
@@ -1,20 +1,20 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:57:29.221975 mbox-to-json-0.0.2/
--rw-r--r--   0 runner    (1001) docker     (123)     1073 2023-04-06 14:57:19.000000 mbox-to-json-0.0.2/LICENSE.txt
--rw-r--r--   0 runner    (1001) docker     (123)       24 2023-04-06 14:57:19.000000 mbox-to-json-0.0.2/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)      564 2023-04-06 14:57:29.221975 mbox-to-json-0.0.2/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     6169 2023-04-06 14:57:19.000000 mbox-to-json-0.0.2/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:57:29.221975 mbox-to-json-0.0.2/mbox_to_json.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)      564 2023-04-06 14:57:29.000000 mbox-to-json-0.0.2/mbox_to_json.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      355 2023-04-06 14:57:29.000000 mbox-to-json-0.0.2/mbox_to_json.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 14:57:29.000000 mbox-to-json-0.0.2/mbox_to_json.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       47 2023-04-06 14:57:29.000000 mbox-to-json-0.0.2/mbox_to_json.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 14:57:29.000000 mbox-to-json-0.0.2/mbox_to_json.egg-info/not-zip-safe
--rw-r--r--   0 runner    (1001) docker     (123)       55 2023-04-06 14:57:29.000000 mbox-to-json-0.0.2/mbox_to_json.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        4 2023-04-06 14:57:29.000000 mbox-to-json-0.0.2/mbox_to_json.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)       55 2023-04-06 14:57:19.000000 mbox-to-json-0.0.2/requirements.txt
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 14:57:29.221975 mbox-to-json-0.0.2/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)      919 2023-04-06 14:57:19.000000 mbox-to-json-0.0.2/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:57:29.221975 mbox-to-json-0.0.2/src/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 14:57:19.000000 mbox-to-json-0.0.2/src/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     7618 2023-04-06 14:57:19.000000 mbox-to-json-0.0.2/src/extract.py
--rw-r--r--   0 runner    (1001) docker     (123)     2150 2023-04-06 14:57:19.000000 mbox-to-json-0.0.2/src/main.py
+drwxr-xr-x   0 prakharsharma   (501) staff       (20)        0 2023-04-01 12:58:00.864587 mbox-to-json-1.0.0/
+-rw-r--r--   0 prakharsharma   (501) staff       (20)     1073 2023-01-11 13:15:21.000000 mbox-to-json-1.0.0/LICENSE.txt
+-rw-r--r--   0 prakharsharma   (501) staff       (20)       24 2023-01-11 13:56:10.000000 mbox-to-json-1.0.0/MANIFEST.in
+-rw-r--r--   0 prakharsharma   (501) staff       (20)      573 2023-04-01 12:58:00.864425 mbox-to-json-1.0.0/PKG-INFO
+-rw-r--r--   0 prakharsharma   (501) staff       (20)     6169 2023-02-06 09:47:59.000000 mbox-to-json-1.0.0/README.md
+drwxr-xr-x   0 prakharsharma   (501) staff       (20)        0 2023-04-01 12:58:00.863568 mbox-to-json-1.0.0/mbox_to_json.egg-info/
+-rw-r--r--   0 prakharsharma   (501) staff       (20)      573 2023-04-01 12:58:00.000000 mbox-to-json-1.0.0/mbox_to_json.egg-info/PKG-INFO
+-rw-r--r--   0 prakharsharma   (501) staff       (20)      355 2023-04-01 12:58:00.000000 mbox-to-json-1.0.0/mbox_to_json.egg-info/SOURCES.txt
+-rw-r--r--   0 prakharsharma   (501) staff       (20)        1 2023-04-01 12:58:00.000000 mbox-to-json-1.0.0/mbox_to_json.egg-info/dependency_links.txt
+-rw-r--r--   0 prakharsharma   (501) staff       (20)       47 2023-04-01 12:58:00.000000 mbox-to-json-1.0.0/mbox_to_json.egg-info/entry_points.txt
+-rw-r--r--   0 prakharsharma   (501) staff       (20)        1 2023-04-01 12:58:00.000000 mbox-to-json-1.0.0/mbox_to_json.egg-info/not-zip-safe
+-rw-r--r--   0 prakharsharma   (501) staff       (20)       55 2023-04-01 12:58:00.000000 mbox-to-json-1.0.0/mbox_to_json.egg-info/requires.txt
+-rw-r--r--   0 prakharsharma   (501) staff       (20)        4 2023-04-01 12:58:00.000000 mbox-to-json-1.0.0/mbox_to_json.egg-info/top_level.txt
+-rw-r--r--   0 prakharsharma   (501) staff       (20)       55 2023-02-04 14:13:50.000000 mbox-to-json-1.0.0/requirements.txt
+-rw-r--r--   0 prakharsharma   (501) staff       (20)       38 2023-04-01 12:58:00.864639 mbox-to-json-1.0.0/setup.cfg
+-rw-r--r--   0 prakharsharma   (501) staff       (20)      928 2023-04-01 12:57:23.000000 mbox-to-json-1.0.0/setup.py
+drwxr-xr-x   0 prakharsharma   (501) staff       (20)        0 2023-04-01 12:58:00.864107 mbox-to-json-1.0.0/src/
+-rw-r--r--   0 prakharsharma   (501) staff       (20)        0 2023-01-11 13:15:20.000000 mbox-to-json-1.0.0/src/__init__.py
+-rw-r--r--   0 prakharsharma   (501) staff       (20)     7618 2023-02-05 06:54:59.000000 mbox-to-json-1.0.0/src/extract.py
+-rw-r--r--   0 prakharsharma   (501) staff       (20)     2150 2023-04-01 11:11:21.000000 mbox-to-json-1.0.0/src/main.py
```

### Comparing `mbox-to-json-0.0.2/LICENSE.txt` & `mbox-to-json-1.0.0/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `mbox-to-json-0.0.2/PKG-INFO` & `mbox-to-json-1.0.0/PKG-INFO`

 * *Files 8% similar despite different names*

```diff
@@ -1,16 +1,16 @@
 Metadata-Version: 2.1
 Name: mbox-to-json
-Version: 0.0.2
+Version: 1.0.0
 Summary: MBOX to JSON Converter
 Home-page: https://github.com/PS1607/mbox-to-json
 Author: Prakhar Sharma
 Author-email: prakharsharma1607@gmail.com
 License: MIT
-Keywords: MBOX to JSON Converter
+Keywords: mbox json csv converter
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
 Description-Content-Type: text/markdown
 License-File: LICENSE.txt
 
-A small package that converts MBOX files to JSON. Also includes functionality to extract attachments.
+A small package that converts MBOX files to JSON(or CSV). Also includes functionality to extract attachments.
```

### Comparing `mbox-to-json-0.0.2/README.md` & `mbox-to-json-1.0.0/README.md`

 * *Files identical despite different names*

### Comparing `mbox-to-json-0.0.2/mbox_to_json.egg-info/PKG-INFO` & `mbox-to-json-1.0.0/mbox_to_json.egg-info/PKG-INFO`

 * *Files 8% similar despite different names*

```diff
@@ -1,16 +1,16 @@
 Metadata-Version: 2.1
 Name: mbox-to-json
-Version: 0.0.2
+Version: 1.0.0
 Summary: MBOX to JSON Converter
 Home-page: https://github.com/PS1607/mbox-to-json
 Author: Prakhar Sharma
 Author-email: prakharsharma1607@gmail.com
 License: MIT
-Keywords: MBOX to JSON Converter
+Keywords: mbox json csv converter
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
 Description-Content-Type: text/markdown
 License-File: LICENSE.txt
 
-A small package that converts MBOX files to JSON. Also includes functionality to extract attachments.
+A small package that converts MBOX files to JSON(or CSV). Also includes functionality to extract attachments.
```

### Comparing `mbox-to-json-0.0.2/setup.py` & `mbox-to-json-1.0.0/setup.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,17 +1,17 @@
 from setuptools import setup, find_packages
 
 with open('requirements.txt') as f:
 	requirements = f.readlines()
 
-long_description = 'A small package that converts MBOX files to JSON. Also includes functionality to extract attachments.'
+long_description = 'A small package that converts MBOX files to JSON(or CSV). Also includes functionality to extract attachments.'
 
 setup(
 		name ='mbox-to-json',
-		version ='0.0.2',
+		version ='1.0.0',
 		author ='Prakhar Sharma',
 		author_email ='prakharsharma1607@gmail.com',
 		url ='https://github.com/PS1607/mbox-to-json',
 		description ='MBOX to JSON Converter',
 		long_description = long_description,
 		long_description_content_type ="text/markdown",
 		license ='MIT',
@@ -22,11 +22,11 @@
 			]
 		},
 		classifiers =(
 			"Programming Language :: Python :: 3",
 			"License :: OSI Approved :: MIT License",
 			"Operating System :: OS Independent",
 		),
-		keywords ='MBOX to JSON Converter',
+		keywords ='mbox json csv converter',
 		install_requires = requirements,
 		zip_safe = False
 )
```

### Comparing `mbox-to-json-0.0.2/src/extract.py` & `mbox-to-json-1.0.0/src/extract.py`

 * *Files identical despite different names*

### Comparing `mbox-to-json-0.0.2/src/main.py` & `mbox-to-json-1.0.0/src/main.py`

 * *Files identical despite different names*

