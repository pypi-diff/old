# Comparing `tmp/instld-0.0.2.tar.gz` & `tmp/instld-0.0.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "instld-0.0.2.tar", last modified: Mon Apr  3 13:56:34 2023, max compression
+gzip compressed data, was "instld-0.0.3.tar", last modified: Fri Apr  7 08:22:22 2023, max compression
```

## Comparing `instld-0.0.2.tar` & `instld-0.0.3.tar`

### file list

```diff
@@ -1,13 +1,13 @@
-drwxr-xr-x   0 pomponchik   (501) staff       (20)        0 2023-04-03 13:56:34.184563 instld-0.0.2/
--rw-r--r--   0 pomponchik   (501) staff       (20)     1067 2023-04-02 20:16:05.000000 instld-0.0.2/LICENSE
--rw-r--r--   0 pomponchik   (501) staff       (20)     1161 2023-04-03 13:56:34.184355 instld-0.0.2/PKG-INFO
--rw-r--r--   0 pomponchik   (501) staff       (20)      742 2023-04-03 13:55:48.000000 instld-0.0.2/README.md
-drwxr-xr-x   0 pomponchik   (501) staff       (20)        0 2023-04-03 13:56:34.183399 instld-0.0.2/installed/
--rw-r--r--   0 pomponchik   (501) staff       (20)     1551 2023-04-03 13:12:50.000000 instld-0.0.2/installed/__init__.py
-drwxr-xr-x   0 pomponchik   (501) staff       (20)        0 2023-04-03 13:56:34.184120 instld-0.0.2/instld.egg-info/
--rw-r--r--   0 pomponchik   (501) staff       (20)     1161 2023-04-03 13:56:34.000000 instld-0.0.2/instld.egg-info/PKG-INFO
--rw-r--r--   0 pomponchik   (501) staff       (20)      168 2023-04-03 13:56:34.000000 instld-0.0.2/instld.egg-info/SOURCES.txt
--rw-r--r--   0 pomponchik   (501) staff       (20)        1 2023-04-03 13:56:34.000000 instld-0.0.2/instld.egg-info/dependency_links.txt
--rw-r--r--   0 pomponchik   (501) staff       (20)       10 2023-04-03 13:56:34.000000 instld-0.0.2/instld.egg-info/top_level.txt
--rw-r--r--   0 pomponchik   (501) staff       (20)       38 2023-04-03 13:56:34.184626 instld-0.0.2/setup.cfg
--rw-r--r--   0 pomponchik   (501) staff       (20)      649 2023-04-03 13:53:16.000000 instld-0.0.2/setup.py
+drwxr-xr-x   0 pomponchik   (501) staff       (20)        0 2023-04-07 08:22:22.297668 instld-0.0.3/
+-rw-r--r--   0 pomponchik   (501) staff       (20)     1067 2023-04-02 20:16:05.000000 instld-0.0.3/LICENSE
+-rw-r--r--   0 pomponchik   (501) staff       (20)     1960 2023-04-07 08:22:22.297402 instld-0.0.3/PKG-INFO
+-rw-r--r--   0 pomponchik   (501) staff       (20)     1339 2023-04-07 06:53:17.000000 instld-0.0.3/README.md
+drwxr-xr-x   0 pomponchik   (501) staff       (20)        0 2023-04-07 08:22:22.296162 instld-0.0.3/installed/
+-rw-r--r--   0 pomponchik   (501) staff       (20)     1610 2023-04-07 07:00:54.000000 instld-0.0.3/installed/__init__.py
+drwxr-xr-x   0 pomponchik   (501) staff       (20)        0 2023-04-07 08:22:22.297127 instld-0.0.3/instld.egg-info/
+-rw-r--r--   0 pomponchik   (501) staff       (20)     1960 2023-04-07 08:22:22.000000 instld-0.0.3/instld.egg-info/PKG-INFO
+-rw-r--r--   0 pomponchik   (501) staff       (20)      168 2023-04-07 08:22:22.000000 instld-0.0.3/instld.egg-info/SOURCES.txt
+-rw-r--r--   0 pomponchik   (501) staff       (20)        1 2023-04-07 08:22:22.000000 instld-0.0.3/instld.egg-info/dependency_links.txt
+-rw-r--r--   0 pomponchik   (501) staff       (20)       10 2023-04-07 08:22:22.000000 instld-0.0.3/instld.egg-info/top_level.txt
+-rw-r--r--   0 pomponchik   (501) staff       (20)       38 2023-04-07 08:22:22.297766 instld-0.0.3/setup.cfg
+-rw-r--r--   0 pomponchik   (501) staff       (20)      864 2023-04-07 05:56:25.000000 instld-0.0.3/setup.py
```

### Comparing `instld-0.0.2/LICENSE` & `instld-0.0.3/LICENSE`

 * *Files identical despite different names*

### Comparing `instld-0.0.2/installed/__init__.py` & `instld-0.0.3/installed/__init__.py`

 * *Files 10% similar despite different names*

```diff
@@ -21,20 +21,23 @@
 
     subprocess.check_call([sys.executable, '-m', 'venv', path_to_venv], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
 
     for maybe_directory in os.listdir(path=sys_path):
         maybe_directory_full = os.path.join(sys_path, maybe_directory)
         if maybe_directory.startswith('python') and os.path.isdir(maybe_directory_full):
             sys_path = os.path.join(sys_path, maybe_directory, 'site-packages')
+            break
 
-    sys.path.append(sys_path)
+    with lock:
+        sys.path.insert(0, sys_path)
 
     yield sys_path
 
-    del sys.path[sys.path.index(sys_path)]
+    with lock:
+        del sys.path[sys.path.index(sys_path)]
 
 @contextmanager
 def pip_context(package_name):
     with tempfile.TemporaryDirectory() as directory:
         with search_path(directory) as where:
             try:
                 with lock:
```

