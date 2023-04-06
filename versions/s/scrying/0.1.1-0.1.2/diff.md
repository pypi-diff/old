# Comparing `tmp/scrying-0.1.1.tar.gz` & `tmp/scrying-0.1.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "scrying-0.1.1.tar", last modified: Thu Apr  6 14:35:59 2023, max compression
+gzip compressed data, was "scrying-0.1.2.tar", last modified: Thu Apr  6 14:43:00 2023, max compression
```

## Comparing `scrying-0.1.1.tar` & `scrying-0.1.2.tar`

### file list

```diff
@@ -1,15 +1,15 @@
-drwxrwxr-x   0 matteo    (1000) matteo    (1000)        0 2023-04-06 14:35:59.086115 scrying-0.1.1/
--rw-rw-r--   0 matteo    (1000) matteo    (1000)        0 2023-04-06 13:34:40.000000 scrying-0.1.1/LICENSE
--rw-rw-r--   0 matteo    (1000) matteo    (1000)      704 2023-04-06 14:35:59.086115 scrying-0.1.1/PKG-INFO
--rw-rw-r--   0 matteo    (1000) matteo    (1000)      476 2023-04-06 14:32:55.000000 scrying-0.1.1/README.md
-drwxrwxr-x   0 matteo    (1000) matteo    (1000)        0 2023-04-06 14:35:59.086115 scrying-0.1.1/scrying/
--rw-rw-r--   0 matteo    (1000) matteo    (1000)      134 2023-04-06 14:35:52.000000 scrying-0.1.1/scrying/__init__.py
--rw-rw-r--   0 matteo    (1000) matteo    (1000)     1225 2023-04-06 14:15:48.000000 scrying-0.1.1/scrying/main.py
-drwxrwxr-x   0 matteo    (1000) matteo    (1000)        0 2023-04-06 14:35:59.086115 scrying-0.1.1/scrying.egg-info/
--rw-rw-r--   0 matteo    (1000) matteo    (1000)      704 2023-04-06 14:35:59.000000 scrying-0.1.1/scrying.egg-info/PKG-INFO
--rw-rw-r--   0 matteo    (1000) matteo    (1000)      216 2023-04-06 14:35:59.000000 scrying-0.1.1/scrying.egg-info/SOURCES.txt
--rw-rw-r--   0 matteo    (1000) matteo    (1000)        1 2023-04-06 14:35:59.000000 scrying-0.1.1/scrying.egg-info/dependency_links.txt
--rw-rw-r--   0 matteo    (1000) matteo    (1000)       21 2023-04-06 14:35:59.000000 scrying-0.1.1/scrying.egg-info/requires.txt
--rw-rw-r--   0 matteo    (1000) matteo    (1000)        8 2023-04-06 14:35:59.000000 scrying-0.1.1/scrying.egg-info/top_level.txt
--rw-rw-r--   0 matteo    (1000) matteo    (1000)       38 2023-04-06 14:35:59.086115 scrying-0.1.1/setup.cfg
--rw-rw-r--   0 matteo    (1000) matteo    (1000)      902 2023-04-06 14:35:52.000000 scrying-0.1.1/setup.py
+drwxrwxr-x   0 matteo    (1000) matteo    (1000)        0 2023-04-06 14:43:00.568504 scrying-0.1.2/
+-rw-rw-r--   0 matteo    (1000) matteo    (1000)        0 2023-04-06 13:34:40.000000 scrying-0.1.2/LICENSE
+-rw-rw-r--   0 matteo    (1000) matteo    (1000)     1212 2023-04-06 14:43:00.568504 scrying-0.1.2/PKG-INFO
+-rw-rw-r--   0 matteo    (1000) matteo    (1000)      466 2023-04-06 14:37:25.000000 scrying-0.1.2/README.md
+drwxrwxr-x   0 matteo    (1000) matteo    (1000)        0 2023-04-06 14:43:00.568504 scrying-0.1.2/scrying/
+-rw-rw-r--   0 matteo    (1000) matteo    (1000)      134 2023-04-06 14:42:48.000000 scrying-0.1.2/scrying/__init__.py
+-rw-rw-r--   0 matteo    (1000) matteo    (1000)     1225 2023-04-06 14:15:48.000000 scrying-0.1.2/scrying/main.py
+drwxrwxr-x   0 matteo    (1000) matteo    (1000)        0 2023-04-06 14:43:00.568504 scrying-0.1.2/scrying.egg-info/
+-rw-rw-r--   0 matteo    (1000) matteo    (1000)     1212 2023-04-06 14:43:00.000000 scrying-0.1.2/scrying.egg-info/PKG-INFO
+-rw-rw-r--   0 matteo    (1000) matteo    (1000)      216 2023-04-06 14:43:00.000000 scrying-0.1.2/scrying.egg-info/SOURCES.txt
+-rw-rw-r--   0 matteo    (1000) matteo    (1000)        1 2023-04-06 14:43:00.000000 scrying-0.1.2/scrying.egg-info/dependency_links.txt
+-rw-rw-r--   0 matteo    (1000) matteo    (1000)       21 2023-04-06 14:43:00.000000 scrying-0.1.2/scrying.egg-info/requires.txt
+-rw-rw-r--   0 matteo    (1000) matteo    (1000)        8 2023-04-06 14:43:00.000000 scrying-0.1.2/scrying.egg-info/top_level.txt
+-rw-rw-r--   0 matteo    (1000) matteo    (1000)       38 2023-04-06 14:43:00.568504 scrying-0.1.2/setup.cfg
+-rw-rw-r--   0 matteo    (1000) matteo    (1000)     1083 2023-04-06 14:42:52.000000 scrying-0.1.2/setup.py
```

### Comparing `scrying-0.1.1/scrying/main.py` & `scrying-0.1.2/scrying/main.py`

 * *Files identical despite different names*

### Comparing `scrying-0.1.1/setup.py` & `scrying-0.1.2/setup.py`

 * *Files 19% similar despite different names*

```diff
@@ -1,23 +1,28 @@
+from pathlib import Path
+
 from setuptools import setup
 
+this_directory = Path(__file__).parent
+
 setup(
     name='scrying',
-    version='0.1.1',
+    version='0.1.2',
     description='A ScryfallAPI port written in Python',
     url='https://github.com/chumpblocckami/scrying',
     author='Matteo Mazzola',
     author_email='contact.matteomazzola@gmail.com',
     license='BSD 2-clause',
     packages=["scrying"],
     install_requires=['requests',
                       'pillow',
                       'tqdm'
                       ],
-
+    long_description=(this_directory / "README.md").read_text(),
+    long_description_content_type='text/markdown',
     classifiers=[
         'Development Status :: 1 - Planning',
         'Intended Audience :: Science/Research',
         'License :: OSI Approved :: BSD License',
         'Operating System :: POSIX :: Linux',
         'Programming Language :: Python :: 2',
         'Programming Language :: Python :: 2.7',
```

