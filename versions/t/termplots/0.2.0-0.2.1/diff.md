# Comparing `tmp/termplots-0.2.0.tar.gz` & `tmp/termplots-0.2.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "termplots-0.2.0.tar", last modified: Thu Apr  6 15:03:19 2023, max compression
+gzip compressed data, was "termplots-0.2.1.tar", last modified: Thu Apr  6 15:08:41 2023, max compression
```

## Comparing `termplots-0.2.0.tar` & `termplots-0.2.1.tar`

### file list

```diff
@@ -1,13 +1,13 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:03:19.789314 termplots-0.2.0/
--rw-r--r--   0 runner    (1001) docker     (123)     1073 2023-04-06 15:03:05.000000 termplots-0.2.0/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)     1995 2023-04-06 15:03:19.785314 termplots-0.2.0/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     1538 2023-04-06 15:03:05.000000 termplots-0.2.0/README.md
--rw-r--r--   0 runner    (1001) docker     (123)      450 2023-04-06 15:03:05.000000 termplots-0.2.0/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 15:03:19.789314 termplots-0.2.0/setup.cfg
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:03:19.785314 termplots-0.2.0/termplots/
--rw-r--r--   0 runner    (1001) docker     (123)     5936 2023-04-06 15:03:05.000000 termplots-0.2.0/termplots/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:03:19.785314 termplots-0.2.0/termplots.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     1995 2023-04-06 15:03:19.000000 termplots-0.2.0/termplots.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      186 2023-04-06 15:03:19.000000 termplots-0.2.0/termplots.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 15:03:19.000000 termplots-0.2.0/termplots.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       10 2023-04-06 15:03:19.000000 termplots-0.2.0/termplots.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:08:41.951132 termplots-0.2.1/
+-rw-r--r--   0 runner    (1001) docker     (123)     1073 2023-04-06 15:08:25.000000 termplots-0.2.1/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)     1995 2023-04-06 15:08:41.947132 termplots-0.2.1/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     1538 2023-04-06 15:08:25.000000 termplots-0.2.1/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)      450 2023-04-06 15:08:25.000000 termplots-0.2.1/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 15:08:41.951132 termplots-0.2.1/setup.cfg
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:08:41.947132 termplots-0.2.1/termplots/
+-rw-r--r--   0 runner    (1001) docker     (123)     5504 2023-04-06 15:08:25.000000 termplots-0.2.1/termplots/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:08:41.947132 termplots-0.2.1/termplots.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     1995 2023-04-06 15:08:41.000000 termplots-0.2.1/termplots.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      186 2023-04-06 15:08:41.000000 termplots-0.2.1/termplots.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 15:08:41.000000 termplots-0.2.1/termplots.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       10 2023-04-06 15:08:41.000000 termplots-0.2.1/termplots.egg-info/top_level.txt
```

### Comparing `termplots-0.2.0/LICENSE` & `termplots-0.2.1/LICENSE`

 * *Files identical despite different names*

### Comparing `termplots-0.2.0/PKG-INFO` & `termplots-0.2.1/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: termplots
-Version: 0.2.0
+Version: 0.2.1
 Summary: A lightweight plot library for your terminal!
 Author-email: Lorenzo Andreasi <lolloandreasi@gmail.com>
 Project-URL: Homepage, https://github.com/lollo03/termplots
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
 Requires-Python: >=3.7
```

### Comparing `termplots-0.2.0/README.md` & `termplots-0.2.1/README.md`

 * *Files identical despite different names*

### Comparing `termplots-0.2.0/termplots/__init__.py` & `termplots-0.2.1/termplots/__init__.py`

 * *Files 13% similar despite different names*

```diff
@@ -174,17 +174,7 @@
             pos = labels.index(label)
             color = colors[pos] if pos<len(colors) else colors[pos-len(colors)] 
             print(f'{color}{car[pos]}{reset}: {label}')
         pos += 1
         color = colors[pos] if pos<len(colors) else colors[pos-len(colors)] 
         print(f'{color}{car[-1]}{reset}: overlaps')
 
-# Tests...
-#plot([112, 132, 30], ystep=50)
-#plot([0,0.1,0.3], ystep=0.3)
-#plot([-32,-20,0,20,32], ystep=10)
-#mplot([[-32,-20,0],[32,20,0, 112]], ystep=50, labels=["1", "2"])
-#plot([[1,0,2], [-1,0,3,0,2,2]], car=['*', '$', '@'], labels=['List 1', 'List 2'])
-#plot([1,0,2,-1,0,3,0,2,2], car=['*', '$', '@'], labels=['List 1'])
-#print(getSteps([[32,20,0, 112],[-32,-20,0,20]]))
-cplot([[32,20,0, 112],[-32,-20,0,20]])
-cplot([-3,2,1,15])
```

### Comparing `termplots-0.2.0/termplots.egg-info/PKG-INFO` & `termplots-0.2.1/termplots.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: termplots
-Version: 0.2.0
+Version: 0.2.1
 Summary: A lightweight plot library for your terminal!
 Author-email: Lorenzo Andreasi <lolloandreasi@gmail.com>
 Project-URL: Homepage, https://github.com/lollo03/termplots
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
 Requires-Python: >=3.7
```

