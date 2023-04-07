# Comparing `tmp/tqsdk-sm-1.0.1.tar.gz` & `tmp/tqsdk-sm-1.0.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/tqsdk-sm-1.0.1.tar", last modified: Thu Mar 30 06:04:25 2023, max compression
+gzip compressed data, was "dist/tqsdk-sm-1.0.2.tar", last modified: Fri Apr  7 08:19:22 2023, max compression
```

## Comparing `tqsdk-sm-1.0.1.tar` & `tqsdk-sm-1.0.2.tar`

### file list

```diff
@@ -1,11 +1,11 @@
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-30 06:04:25.000000 tqsdk-sm-1.0.1/
--rw-r--r--   0 runner    (1001) docker     (122)      242 2023-03-30 06:04:25.000000 tqsdk-sm-1.0.1/PKG-INFO
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-30 06:04:25.000000 tqsdk-sm-1.0.1/tqsdk_sm/
--rw-r--r--   0 runner    (1001) docker     (122)      163 2023-03-30 06:04:18.000000 tqsdk-sm-1.0.1/tqsdk_sm/__init__.py
--rw-r--r--   0 runner    (1001) docker     (122)       38 2023-03-30 06:04:25.000000 tqsdk-sm-1.0.1/setup.cfg
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-30 06:04:25.000000 tqsdk-sm-1.0.1/tqsdk_sm.egg-info/
--rw-r--r--   0 runner    (1001) docker     (122)      242 2023-03-30 06:04:25.000000 tqsdk-sm-1.0.1/tqsdk_sm.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (122)      157 2023-03-30 06:04:25.000000 tqsdk-sm-1.0.1/tqsdk_sm.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (122)        9 2023-03-30 06:04:25.000000 tqsdk-sm-1.0.1/tqsdk_sm.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (122)        1 2023-03-30 06:04:25.000000 tqsdk-sm-1.0.1/tqsdk_sm.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (122)     1140 2023-03-30 06:04:18.000000 tqsdk-sm-1.0.1/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-07 08:19:22.000000 tqsdk-sm-1.0.2/
+-rw-r--r--   0 runner    (1001) docker     (122)      242 2023-04-07 08:19:22.000000 tqsdk-sm-1.0.2/PKG-INFO
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-07 08:19:22.000000 tqsdk-sm-1.0.2/tqsdk_sm/
+-rw-r--r--   0 runner    (1001) docker     (122)      163 2023-04-07 08:19:15.000000 tqsdk-sm-1.0.2/tqsdk_sm/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)       38 2023-04-07 08:19:22.000000 tqsdk-sm-1.0.2/setup.cfg
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-07 08:19:22.000000 tqsdk-sm-1.0.2/tqsdk_sm.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (122)      242 2023-04-07 08:19:22.000000 tqsdk-sm-1.0.2/tqsdk_sm.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (122)      157 2023-04-07 08:19:22.000000 tqsdk-sm-1.0.2/tqsdk_sm.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (122)        9 2023-04-07 08:19:22.000000 tqsdk-sm-1.0.2/tqsdk_sm.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (122)        1 2023-04-07 08:19:22.000000 tqsdk-sm-1.0.2/tqsdk_sm.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (122)     1140 2023-04-07 08:19:15.000000 tqsdk-sm-1.0.2/setup.py
```

### Comparing `tqsdk-sm-1.0.1/setup.py` & `tqsdk-sm-1.0.2/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -23,15 +23,15 @@
             python, abi = 'py3', 'none'
             return python, abi, plat
 except ImportError:
     bdist_wheel = None
 
 setuptools.setup(
     name='tqsdk-sm',
-    version="1.0.1",
+    version="1.0.2",
     description='TianQin SDK - sm lib',
     author='TianQin',
     author_email='tianqincn@gmail.com',
     url='https://www.shinnytech.com/tqsdk',
     packages=setuptools.find_packages(),
     python_requires='>=3',
     cmdclass={'bdist_wheel': bdist_wheel},
```

