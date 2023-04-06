# Comparing `tmp/hshshshs-0.0.6.tar.gz` & `tmp/hshshshs-0.0.7.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "hshshshs-0.0.6.tar", last modified: Wed Apr  5 10:37:43 2023, max compression
+gzip compressed data, was "hshshshs-0.0.7.tar", last modified: Thu Apr  6 09:44:56 2023, max compression
```

## Comparing `hshshshs-0.0.6.tar` & `hshshshs-0.0.7.tar`

### file list

```diff
@@ -1,13 +1,13 @@
-drwxrwxrwx   0        0        0        0 2023-04-05 10:37:43.895204 hshshshs-0.0.6/
--rw-rw-rw-   0        0        0      261 2023-04-05 10:37:43.895204 hshshshs-0.0.6/PKG-INFO
-drwxrwxrwx   0        0        0        0 2023-04-05 10:37:43.882597 hshshshs-0.0.6/hshshshs/
--rw-rw-rw-   0        0        0        0 2023-03-17 08:41:46.000000 hshshshs-0.0.6/hshshshs/__init__.py
--rw-rw-rw-   0        0        0     1935 2023-03-29 12:36:59.000000 hshshshs-0.0.6/hshshshs/cFunction.py
-drwxrwxrwx   0        0        0        0 2023-04-05 10:37:43.893206 hshshshs-0.0.6/hshshshs.egg-info/
--rw-rw-rw-   0        0        0      261 2023-04-05 10:37:43.000000 hshshshs-0.0.6/hshshshs.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      210 2023-04-05 10:37:43.000000 hshshshs-0.0.6/hshshshs.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-05 10:37:43.000000 hshshshs-0.0.6/hshshshs.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0        8 2023-04-05 10:37:43.000000 hshshshs-0.0.6/hshshshs.egg-info/requires.txt
--rw-rw-rw-   0        0        0        9 2023-04-05 10:37:43.000000 hshshshs-0.0.6/hshshshs.egg-info/top_level.txt
--rw-rw-rw-   0        0        0       42 2023-04-05 10:37:43.896204 hshshshs-0.0.6/setup.cfg
--rw-rw-rw-   0        0        0      978 2023-04-05 10:36:21.000000 hshshshs-0.0.6/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-06 09:44:56.004462 hshshshs-0.0.7/
+-rw-rw-rw-   0        0        0      261 2023-04-06 09:44:56.004462 hshshshs-0.0.7/PKG-INFO
+drwxrwxrwx   0        0        0        0 2023-04-06 09:44:56.004462 hshshshs-0.0.7/hshshshs/
+-rw-rw-rw-   0        0        0        0 2023-03-17 08:41:46.000000 hshshshs-0.0.7/hshshshs/__init__.py
+-rw-rw-rw-   0        0        0     1935 2023-03-29 12:36:59.000000 hshshshs-0.0.7/hshshshs/cFunction.py
+drwxrwxrwx   0        0        0        0 2023-04-06 09:44:56.004462 hshshshs-0.0.7/hshshshs.egg-info/
+-rw-rw-rw-   0        0        0      261 2023-04-06 09:44:55.000000 hshshshs-0.0.7/hshshshs.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      210 2023-04-06 09:44:55.000000 hshshshs-0.0.7/hshshshs.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-06 09:44:55.000000 hshshshs-0.0.7/hshshshs.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0        8 2023-04-06 09:44:55.000000 hshshshs-0.0.7/hshshshs.egg-info/requires.txt
+-rw-rw-rw-   0        0        0        9 2023-04-06 09:44:55.000000 hshshshs-0.0.7/hshshshs.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0       42 2023-04-06 09:44:56.004462 hshshshs-0.0.7/setup.cfg
+-rw-rw-rw-   0        0        0      978 2023-04-06 09:44:20.000000 hshshshs-0.0.7/setup.py
```

### Comparing `hshshshs-0.0.6/hshshshs/cFunction.py` & `hshshshs-0.0.7/hshshshs/cFunction.py`

 * *Files identical despite different names*

### Comparing `hshshshs-0.0.6/setup.py` & `hshshshs-0.0.7/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -15,15 +15,15 @@
                 module_name = "%(base)s.%(item)s" % vars()
             else:
                 module_name = item
             packages[module_name] = dir
             packages.update(find_packages(dir, module_name))
     return packages
 setup(  name="hshshshs",
-        version="0.0.6",
+        version="0.0.7",
         url="http://github.com/kimhansu/hshshshs",
         license="MIT",
         author="kimhansu",
         author_email="gimhansu@naver.com",
         keywords=["calendar","isoweek","listsum"],
         description="math function",
         packages=find_packages("."),
```

