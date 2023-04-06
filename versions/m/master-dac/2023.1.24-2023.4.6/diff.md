# Comparing `tmp/master_dac-2023.1.24.tar.gz` & `tmp/master_dac-2023.4.6.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "master_dac-2023.1.24.tar", last modified: Tue Jan 24 18:50:37 2023, max compression
+gzip compressed data, was "master_dac-2023.4.6.tar", last modified: Thu Apr  6 09:57:41 2023, max compression
```

## Comparing `master_dac-2023.1.24.tar` & `master_dac-2023.4.6.tar`

### file list

```diff
@@ -1,26 +1,27 @@
-drwxrwxr-x   0 bpiwowar  (1000) bpiwowar  (1000)        0 2023-01-24 18:50:37.517677 master_dac-2023.1.24/
--rw-rw-r--   0 bpiwowar  (1000) bpiwowar  (1000)       46 2022-09-17 15:37:53.000000 master_dac-2023.1.24/.gitignore
--rw-rw-r--   0 bpiwowar  (1000) bpiwowar  (1000)       37 2022-09-17 12:55:51.000000 master_dac-2023.1.24/MANIFEST.in
--rw-rw-r--   0 bpiwowar  (1000) bpiwowar  (1000)      139 2023-01-24 18:50:37.517677 master_dac-2023.1.24/PKG-INFO
--rw-rw-r--   0 bpiwowar  (1000) bpiwowar  (1000)      127 2022-09-16 15:50:48.000000 master_dac-2023.1.24/README.md
-drwxrwxr-x   0 bpiwowar  (1000) bpiwowar  (1000)        0 2023-01-24 18:50:37.517677 master_dac-2023.1.24/master_dac/
--rw-rw-r--   0 bpiwowar  (1000) bpiwowar  (1000)        0 2022-09-16 09:57:44.000000 master_dac-2023.1.24/master_dac/__init__.py
--rw-rw-r--   0 bpiwowar  (1000) bpiwowar  (1000)     1662 2022-12-11 19:26:16.000000 master_dac-2023.1.24/master_dac/__main__.py
--rw-rw-r--   0 bpiwowar  (1000) bpiwowar  (1000)      838 2022-10-11 07:17:36.000000 master_dac-2023.1.24/master_dac/configuration.py
--rw-rw-r--   0 bpiwowar  (1000) bpiwowar  (1000)      801 2023-01-24 18:49:58.000000 master_dac-2023.1.24/master_dac/datasets.py
--rw-rw-r--   0 bpiwowar  (1000) bpiwowar  (1000)     2572 2022-10-11 11:53:13.000000 master_dac-2023.1.24/master_dac/install.py
-drwxrwxr-x   0 bpiwowar  (1000) bpiwowar  (1000)        0 2023-01-24 18:50:37.517677 master_dac-2023.1.24/master_dac/requirements/
--rw-rw-r--   0 bpiwowar  (1000) bpiwowar  (1000)      464 2023-01-16 15:28:40.000000 master_dac-2023.1.24/master_dac/requirements/amal.txt
--rw-rw-r--   0 bpiwowar  (1000) bpiwowar  (1000)      362 2022-12-11 19:26:16.000000 master_dac-2023.1.24/master_dac/requirements/deep.txt
--rw-rw-r--   0 bpiwowar  (1000) bpiwowar  (1000)       98 2023-01-24 18:50:34.000000 master_dac-2023.1.24/master_dac/requirements/rld.txt
--rw-rw-r--   0 bpiwowar  (1000) bpiwowar  (1000)     1325 2022-09-17 15:35:57.000000 master_dac-2023.1.24/master_dac/utils.py
-drwxrwxr-x   0 bpiwowar  (1000) bpiwowar  (1000)        0 2023-01-24 18:50:37.517677 master_dac-2023.1.24/master_dac.egg-info/
--rw-rw-r--   0 bpiwowar  (1000) bpiwowar  (1000)      139 2023-01-24 18:50:37.000000 master_dac-2023.1.24/master_dac.egg-info/PKG-INFO
--rw-rw-r--   0 bpiwowar  (1000) bpiwowar  (1000)      509 2023-01-24 18:50:37.000000 master_dac-2023.1.24/master_dac.egg-info/SOURCES.txt
--rw-rw-r--   0 bpiwowar  (1000) bpiwowar  (1000)        1 2023-01-24 18:50:37.000000 master_dac-2023.1.24/master_dac.egg-info/dependency_links.txt
--rw-rw-r--   0 bpiwowar  (1000) bpiwowar  (1000)       57 2023-01-24 18:50:37.000000 master_dac-2023.1.24/master_dac.egg-info/entry_points.txt
--rw-rw-r--   0 bpiwowar  (1000) bpiwowar  (1000)      140 2023-01-24 18:50:37.000000 master_dac-2023.1.24/master_dac.egg-info/requires.txt
--rw-rw-r--   0 bpiwowar  (1000) bpiwowar  (1000)       11 2023-01-24 18:50:37.000000 master_dac-2023.1.24/master_dac.egg-info/top_level.txt
--rw-rw-r--   0 bpiwowar  (1000) bpiwowar  (1000)       80 2022-09-16 09:56:30.000000 master_dac-2023.1.24/pyproject.toml
--rw-rw-r--   0 bpiwowar  (1000) bpiwowar  (1000)      390 2023-01-24 18:50:37.521677 master_dac-2023.1.24/setup.cfg
--rw-rw-r--   0 bpiwowar  (1000) bpiwowar  (1000)      485 2022-11-04 12:15:58.000000 master_dac-2023.1.24/setup.py
+drwxrwxr-x   0 bpiwowar  (1000) bpiwowar  (1000)        0 2023-04-06 09:57:41.815794 master_dac-2023.4.6/
+-rw-rw-r--   0 bpiwowar  (1000) bpiwowar  (1000)       46 2022-09-17 15:37:53.000000 master_dac-2023.4.6/.gitignore
+-rw-rw-r--   0 bpiwowar  (1000) bpiwowar  (1000)       37 2022-09-17 12:55:51.000000 master_dac-2023.4.6/MANIFEST.in
+-rw-rw-r--   0 bpiwowar  (1000) bpiwowar  (1000)       57 2023-04-06 09:57:41.815794 master_dac-2023.4.6/PKG-INFO
+-rw-rw-r--   0 bpiwowar  (1000) bpiwowar  (1000)      127 2022-09-16 15:50:48.000000 master_dac-2023.4.6/README.md
+drwxrwxr-x   0 bpiwowar  (1000) bpiwowar  (1000)        0 2023-04-06 09:57:41.811794 master_dac-2023.4.6/master_dac/
+-rw-rw-r--   0 bpiwowar  (1000) bpiwowar  (1000)        0 2022-09-16 09:57:44.000000 master_dac-2023.4.6/master_dac/__init__.py
+-rw-rw-r--   0 bpiwowar  (1000) bpiwowar  (1000)     1974 2023-04-06 09:38:42.000000 master_dac-2023.4.6/master_dac/__main__.py
+-rw-rw-r--   0 bpiwowar  (1000) bpiwowar  (1000)      838 2022-10-11 07:17:36.000000 master_dac-2023.4.6/master_dac/configuration.py
+-rw-rw-r--   0 bpiwowar  (1000) bpiwowar  (1000)      801 2023-01-24 18:49:58.000000 master_dac-2023.4.6/master_dac/datasets.py
+-rw-rw-r--   0 bpiwowar  (1000) bpiwowar  (1000)     2591 2023-04-06 09:40:44.000000 master_dac-2023.4.6/master_dac/install.py
+drwxrwxr-x   0 bpiwowar  (1000) bpiwowar  (1000)        0 2023-04-06 09:57:41.815794 master_dac-2023.4.6/master_dac/requirements/
+-rw-rw-r--   0 bpiwowar  (1000) bpiwowar  (1000)      464 2023-01-16 15:28:40.000000 master_dac-2023.4.6/master_dac/requirements/amal.txt
+-rw-rw-r--   0 bpiwowar  (1000) bpiwowar  (1000)      362 2022-12-11 19:26:16.000000 master_dac-2023.4.6/master_dac/requirements/deep.txt
+-rw-rw-r--   0 bpiwowar  (1000) bpiwowar  (1000)       32 2023-04-06 09:39:46.000000 master_dac-2023.4.6/master_dac/requirements/rital.txt
+-rw-rw-r--   0 bpiwowar  (1000) bpiwowar  (1000)       98 2023-01-24 18:50:34.000000 master_dac-2023.4.6/master_dac/requirements/rld.txt
+-rw-rw-r--   0 bpiwowar  (1000) bpiwowar  (1000)     1325 2022-09-17 15:35:57.000000 master_dac-2023.4.6/master_dac/utils.py
+drwxrwxr-x   0 bpiwowar  (1000) bpiwowar  (1000)        0 2023-04-06 09:57:41.811794 master_dac-2023.4.6/master_dac.egg-info/
+-rw-rw-r--   0 bpiwowar  (1000) bpiwowar  (1000)       57 2023-04-06 09:57:41.000000 master_dac-2023.4.6/master_dac.egg-info/PKG-INFO
+-rw-rw-r--   0 bpiwowar  (1000) bpiwowar  (1000)      543 2023-04-06 09:57:41.000000 master_dac-2023.4.6/master_dac.egg-info/SOURCES.txt
+-rw-rw-r--   0 bpiwowar  (1000) bpiwowar  (1000)        1 2023-04-06 09:57:41.000000 master_dac-2023.4.6/master_dac.egg-info/dependency_links.txt
+-rw-rw-r--   0 bpiwowar  (1000) bpiwowar  (1000)       56 2023-04-06 09:57:41.000000 master_dac-2023.4.6/master_dac.egg-info/entry_points.txt
+-rw-rw-r--   0 bpiwowar  (1000) bpiwowar  (1000)      140 2023-04-06 09:57:41.000000 master_dac-2023.4.6/master_dac.egg-info/requires.txt
+-rw-rw-r--   0 bpiwowar  (1000) bpiwowar  (1000)       11 2023-04-06 09:57:41.000000 master_dac-2023.4.6/master_dac.egg-info/top_level.txt
+-rw-rw-r--   0 bpiwowar  (1000) bpiwowar  (1000)       80 2022-09-16 09:56:30.000000 master_dac-2023.4.6/pyproject.toml
+-rw-rw-r--   0 bpiwowar  (1000) bpiwowar  (1000)      389 2023-04-06 09:57:41.815794 master_dac-2023.4.6/setup.cfg
+-rw-rw-r--   0 bpiwowar  (1000) bpiwowar  (1000)      485 2022-11-04 12:15:58.000000 master_dac-2023.4.6/setup.py
```

### Comparing `master_dac-2023.1.24/master_dac/__main__.py` & `master_dac-2023.4.6/master_dac/__main__.py`

 * *Files 7% similar despite different names*

```diff
@@ -15,22 +15,32 @@
 
 
 @main.group()
 def courses():
     """Permet de gérer la liste des cours suivis"""
     pass
 
-@click.argument("courses", type=click.Choice(["amal", "rld"]), nargs=-1)
+@click.argument("courses", type=click.Choice(["amal", "rld", "rital"]), nargs=-1)
 @courses.command("add")
 def courses_add(courses: List[str]):
     """Ajout de cours"""
     configuration = Configuration()
     configuration.courses.update(courses)
     configuration.save()
 
+@click.argument("courses", type=click.Choice(["amal", "rld", "rital"]), nargs=-1)
+@courses.command("rm")
+def courses_rm(courses: List[str]):
+    """Enlever un cours"""
+    configuration = Configuration()
+    for course in courses:
+        configuration.courses.remove(course)
+    configuration.save()
+
+
 @courses.command("list")
 def courses_list():
     """Liste des cours"""
     for course in Configuration().courses:
         print(course)
 
 @click.option("--no-self-update", is_flag=True)
```

### Comparing `master_dac-2023.1.24/master_dac/configuration.py` & `master_dac-2023.4.6/master_dac/configuration.py`

 * *Files identical despite different names*

### Comparing `master_dac-2023.1.24/master_dac/datasets.py` & `master_dac-2023.4.6/master_dac/datasets.py`

 * *Files identical despite different names*

### Comparing `master_dac-2023.1.24/master_dac/install.py` & `master_dac-2023.4.6/master_dac/install.py`

 * *Files 4% similar despite different names*

```diff
@@ -13,19 +13,14 @@
 import easypip
 
 try:
     from importlib.resources import files as resources_files
 except:
     from importlib_resources import files as resources_files
 
-REQUIREMENTS = {
-    "amal": ["deep", "amal"],
-    "rld": ["deep", "rld"]
-}
-
 @lru_cache()
 def cuda_version() -> Version:
     try:
         re_cuda = re.compile(br".*CUDA version: ([\d\.]+)", re.IGNORECASE)
         out = subprocess.check_output("nvidia-smi")
         for line in out.splitlines():
             m = re_cuda.match(line)
@@ -83,7 +78,11 @@
 
     install("deep", processed)
     install("rld", processed)
 
 def amal(processed: Set[str]):
     install("deep", processed)
     install("amal", processed)
+
+def rital(processed: Set[str]):
+    install("deep", processed)
+    install("rital", processed)
```

### Comparing `master_dac-2023.1.24/master_dac/utils.py` & `master_dac-2023.4.6/master_dac/utils.py`

 * *Files identical despite different names*

