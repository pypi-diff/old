# Comparing `tmp/hexo2notionnext-0.0.1.tar.gz` & `tmp/hexo2notionnext-0.0.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "hexo2notionnext-0.0.1.tar", last modified: Fri Apr  7 11:47:23 2023, max compression
+gzip compressed data, was "hexo2notionnext-0.0.2.tar", last modified: Fri Apr  7 12:13:26 2023, max compression
```

## Comparing `hexo2notionnext-0.0.1.tar` & `hexo2notionnext-0.0.2.tar`

### file list

```diff
@@ -1,15 +1,15 @@
-drwxr-xr-x   0 weizhang   (501) staff       (20)        0 2023-04-07 11:47:23.526822 hexo2notionnext-0.0.1/
--rw-r--r--   0 weizhang   (501) staff       (20)     1064 2023-04-06 11:20:35.000000 hexo2notionnext-0.0.1/LICENSE
--rw-r--r--   0 weizhang   (501) staff       (20)     3292 2023-04-07 11:47:23.526377 hexo2notionnext-0.0.1/PKG-INFO
-drwxr-xr-x   0 weizhang   (501) staff       (20)        0 2023-04-07 11:47:23.521140 hexo2notionnext-0.0.1/hexo2notionnext/
--rw-r--r--   0 weizhang   (501) staff       (20)        0 2023-04-07 11:40:01.000000 hexo2notionnext-0.0.1/hexo2notionnext/__init__.py
--rw-r--r--   0 weizhang   (501) staff       (20)       83 2023-04-07 11:43:26.000000 hexo2notionnext-0.0.1/hexo2notionnext/__main__.py
--rw-r--r--   0 weizhang   (501) staff       (20)     6187 2023-04-07 11:17:19.000000 hexo2notionnext-0.0.1/hexo2notionnext/hexo2notionnext.py
-drwxr-xr-x   0 weizhang   (501) staff       (20)        0 2023-04-07 11:47:23.525724 hexo2notionnext-0.0.1/hexo2notionnext.egg-info/
--rw-r--r--   0 weizhang   (501) staff       (20)     3292 2023-04-07 11:47:23.000000 hexo2notionnext-0.0.1/hexo2notionnext.egg-info/PKG-INFO
--rw-r--r--   0 weizhang   (501) staff       (20)      301 2023-04-07 11:47:23.000000 hexo2notionnext-0.0.1/hexo2notionnext.egg-info/SOURCES.txt
--rw-r--r--   0 weizhang   (501) staff       (20)        1 2023-04-07 11:47:23.000000 hexo2notionnext-0.0.1/hexo2notionnext.egg-info/dependency_links.txt
--rw-r--r--   0 weizhang   (501) staff       (20)       67 2023-04-07 11:47:23.000000 hexo2notionnext-0.0.1/hexo2notionnext.egg-info/requires.txt
--rw-r--r--   0 weizhang   (501) staff       (20)       16 2023-04-07 11:47:23.000000 hexo2notionnext-0.0.1/hexo2notionnext.egg-info/top_level.txt
--rw-r--r--   0 weizhang   (501) staff       (20)       38 2023-04-07 11:47:23.526984 hexo2notionnext-0.0.1/setup.cfg
--rw-r--r--   0 weizhang   (501) staff       (20)     1117 2023-04-07 11:39:18.000000 hexo2notionnext-0.0.1/setup.py
+drwxr-xr-x   0 weizhang   (501) staff       (20)        0 2023-04-07 12:13:26.879877 hexo2notionnext-0.0.2/
+-rw-r--r--   0 weizhang   (501) staff       (20)     1064 2023-04-06 11:20:35.000000 hexo2notionnext-0.0.2/LICENSE
+-rw-r--r--   0 weizhang   (501) staff       (20)     3296 2023-04-07 12:13:26.879313 hexo2notionnext-0.0.2/PKG-INFO
+drwxr-xr-x   0 weizhang   (501) staff       (20)        0 2023-04-07 12:13:26.872689 hexo2notionnext-0.0.2/hexo2notionnext/
+-rw-r--r--   0 weizhang   (501) staff       (20)        0 2023-04-07 11:40:01.000000 hexo2notionnext-0.0.2/hexo2notionnext/__init__.py
+-rw-r--r--   0 weizhang   (501) staff       (20)     6187 2023-04-07 11:17:19.000000 hexo2notionnext-0.0.2/hexo2notionnext/hexo2notionnext.py
+drwxr-xr-x   0 weizhang   (501) staff       (20)        0 2023-04-07 12:13:26.878460 hexo2notionnext-0.0.2/hexo2notionnext.egg-info/
+-rw-r--r--   0 weizhang   (501) staff       (20)     3296 2023-04-07 12:13:26.000000 hexo2notionnext-0.0.2/hexo2notionnext.egg-info/PKG-INFO
+-rw-r--r--   0 weizhang   (501) staff       (20)      315 2023-04-07 12:13:26.000000 hexo2notionnext-0.0.2/hexo2notionnext.egg-info/SOURCES.txt
+-rw-r--r--   0 weizhang   (501) staff       (20)        1 2023-04-07 12:13:26.000000 hexo2notionnext-0.0.2/hexo2notionnext.egg-info/dependency_links.txt
+-rw-r--r--   0 weizhang   (501) staff       (20)       73 2023-04-07 12:13:26.000000 hexo2notionnext-0.0.2/hexo2notionnext.egg-info/entry_points.txt
+-rw-r--r--   0 weizhang   (501) staff       (20)       67 2023-04-07 12:13:26.000000 hexo2notionnext-0.0.2/hexo2notionnext.egg-info/requires.txt
+-rw-r--r--   0 weizhang   (501) staff       (20)       16 2023-04-07 12:13:26.000000 hexo2notionnext-0.0.2/hexo2notionnext.egg-info/top_level.txt
+-rw-r--r--   0 weizhang   (501) staff       (20)       38 2023-04-07 12:13:26.880060 hexo2notionnext-0.0.2/setup.cfg
+-rw-r--r--   0 weizhang   (501) staff       (20)     1256 2023-04-07 12:13:21.000000 hexo2notionnext-0.0.2/setup.py
```

### Comparing `hexo2notionnext-0.0.1/LICENSE` & `hexo2notionnext-0.0.2/LICENSE`

 * *Files identical despite different names*

### Comparing `hexo2notionnext-0.0.1/PKG-INFO` & `hexo2notionnext-0.0.2/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 Metadata-Version: 2.1
 Name: hexo2notionnext
-Version: 0.0.1
+Version: 0.0.2
 Summary: Convert hexo  to notionnext
 Home-page: https://github.com/zhangweidev/hexo2notionnext
 Author: zhangwei
-Author-email: chxxiu@gmail.com
+Author-email: chxxiu+dev@gmail.com
 License: MIT
 Keywords: hexo notion notion.so notion-py markdown md converter
 Classifier: Development Status :: 5 - Production/Stable
 Classifier: Intended Audience :: Developers
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Programming Language :: Python :: 3.6
 Classifier: Programming Language :: Python :: 3.7
```

### Comparing `hexo2notionnext-0.0.1/hexo2notionnext/hexo2notionnext.py` & `hexo2notionnext-0.0.2/hexo2notionnext/hexo2notionnext.py`

 * *Files identical despite different names*

### Comparing `hexo2notionnext-0.0.1/hexo2notionnext.egg-info/PKG-INFO` & `hexo2notionnext-0.0.2/hexo2notionnext.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 Metadata-Version: 2.1
 Name: hexo2notionnext
-Version: 0.0.1
+Version: 0.0.2
 Summary: Convert hexo  to notionnext
 Home-page: https://github.com/zhangweidev/hexo2notionnext
 Author: zhangwei
-Author-email: chxxiu@gmail.com
+Author-email: chxxiu+dev@gmail.com
 License: MIT
 Keywords: hexo notion notion.so notion-py markdown md converter
 Classifier: Development Status :: 5 - Production/Stable
 Classifier: Intended Audience :: Developers
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Programming Language :: Python :: 3.6
 Classifier: Programming Language :: Python :: 3.7
```

### Comparing `hexo2notionnext-0.0.1/setup.py` & `hexo2notionnext-0.0.2/setup.py`

 * *Files 23% similar despite different names*

```diff
@@ -1,18 +1,18 @@
 from setuptools import setup
 
 setup(
     name='hexo2notionnext',
-    version='0.0.1',
+    version='0.0.2',
     description='Convert hexo  to notionnext',
     long_description=open('README.md', 'r').read(),
     long_description_content_type="text/markdown",
     url='https://github.com/zhangweidev/hexo2notionnext',
     author='zhangwei',
-    author_email='chxxiu@gmail.com',
+    author_email='chxxiu+dev@gmail.com',
     license='MIT',
     classifiers=[
         'Development Status :: 5 - Production/Stable',
         'Intended Audience :: Developers',
         'License :: OSI Approved :: MIT License',
         'Programming Language :: Python :: 3.6',
         'Programming Language :: Python :: 3.7',
@@ -25,9 +25,14 @@
     install_requires=[
         'md2notion>=2.4.1',
         'notion>=0.0.28',
         'python_dateutil>=2.8.2',
         'PyYAML>=6.0',
     ],
     keywords='hexo notion notion.so notion-py markdown md converter',
-    packages=['hexo2notionnext']
+    packages=['hexo2notionnext'],
+    entry_points = {
+        'console_scripts': [
+            'hexo2notionnext =hexo2notionnext.hexo2notionnext:main'
+        ]
+    }
 )
```

