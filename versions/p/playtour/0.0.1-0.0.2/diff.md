# Comparing `tmp/playtour-0.0.1.tar.gz` & `tmp/playtour-0.0.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "playtour-0.0.1.tar", last modified: Thu Apr  6 15:38:07 2023, max compression
+gzip compressed data, was "playtour-0.0.2.tar", last modified: Thu Apr  6 15:57:42 2023, max compression
```

## Comparing `playtour-0.0.1.tar` & `playtour-0.0.2.tar`

### file list

```diff
@@ -1,15 +1,15 @@
-drwxr-xr-x   0 gitpod   (33333) gitpod   (33333)        0 2023-04-06 15:38:07.082080 playtour-0.0.1/
--rw-r--r--   0 gitpod   (33333) gitpod   (33333)     1073 2023-04-06 15:31:14.000000 playtour-0.0.1/LICENSE
--rw-r--r--   0 gitpod   (33333) gitpod   (33333)      499 2023-04-06 15:38:07.082080 playtour-0.0.1/PKG-INFO
--rw-r--r--   0 gitpod   (33333) gitpod   (33333)       10 2023-04-06 15:30:48.000000 playtour-0.0.1/README.md
--rw-r--r--   0 gitpod   (33333) gitpod   (33333)      561 2023-04-06 15:30:02.000000 playtour-0.0.1/pyproject.toml
--rw-r--r--   0 gitpod   (33333) gitpod   (33333)       38 2023-04-06 15:38:07.082080 playtour-0.0.1/setup.cfg
-drwxr-xr-x   0 gitpod   (33333) gitpod   (33333)        0 2023-04-06 15:38:07.082080 playtour-0.0.1/src/
-drwxr-xr-x   0 gitpod   (33333) gitpod   (33333)        0 2023-04-06 15:38:07.082080 playtour-0.0.1/src/playtour/
--rw-r--r--   0 gitpod   (33333) gitpod   (33333)        0 2023-04-06 14:51:08.000000 playtour-0.0.1/src/playtour/__init__.py
--rw-r--r--   0 gitpod   (33333) gitpod   (33333)      873 2023-04-06 14:22:16.000000 playtour-0.0.1/src/playtour/playtour.py
-drwxr-xr-x   0 gitpod   (33333) gitpod   (33333)        0 2023-04-06 15:38:07.082080 playtour-0.0.1/src/playtour.egg-info/
--rw-r--r--   0 gitpod   (33333) gitpod   (33333)      499 2023-04-06 15:38:07.000000 playtour-0.0.1/src/playtour.egg-info/PKG-INFO
--rw-r--r--   0 gitpod   (33333) gitpod   (33333)      226 2023-04-06 15:38:07.000000 playtour-0.0.1/src/playtour.egg-info/SOURCES.txt
--rw-r--r--   0 gitpod   (33333) gitpod   (33333)        1 2023-04-06 15:38:07.000000 playtour-0.0.1/src/playtour.egg-info/dependency_links.txt
--rw-r--r--   0 gitpod   (33333) gitpod   (33333)        9 2023-04-06 15:38:07.000000 playtour-0.0.1/src/playtour.egg-info/top_level.txt
+drwxr-xr-x   0 gitpod   (33333) gitpod   (33333)        0 2023-04-06 15:57:42.032910 playtour-0.0.2/
+-rw-r--r--   0 gitpod   (33333) gitpod   (33333)     1073 2023-04-06 15:31:14.000000 playtour-0.0.2/LICENSE
+-rw-r--r--   0 gitpod   (33333) gitpod   (33333)      499 2023-04-06 15:57:42.032910 playtour-0.0.2/PKG-INFO
+-rw-r--r--   0 gitpod   (33333) gitpod   (33333)       10 2023-04-06 15:30:48.000000 playtour-0.0.2/README.md
+-rw-r--r--   0 gitpod   (33333) gitpod   (33333)      596 2023-04-06 15:52:53.000000 playtour-0.0.2/pyproject.toml
+-rw-r--r--   0 gitpod   (33333) gitpod   (33333)       38 2023-04-06 15:57:42.032910 playtour-0.0.2/setup.cfg
+drwxr-xr-x   0 gitpod   (33333) gitpod   (33333)        0 2023-04-06 15:57:42.032910 playtour-0.0.2/src/
+-rw-r--r--   0 gitpod   (33333) gitpod   (33333)        0 2023-04-06 14:51:08.000000 playtour-0.0.2/src/__init__.py
+drwxr-xr-x   0 gitpod   (33333) gitpod   (33333)        0 2023-04-06 15:57:42.032910 playtour-0.0.2/src/playtour.egg-info/
+-rw-r--r--   0 gitpod   (33333) gitpod   (33333)      499 2023-04-06 15:57:42.000000 playtour-0.0.2/src/playtour.egg-info/PKG-INFO
+-rw-r--r--   0 gitpod   (33333) gitpod   (33333)      243 2023-04-06 15:57:42.000000 playtour-0.0.2/src/playtour.egg-info/SOURCES.txt
+-rw-r--r--   0 gitpod   (33333) gitpod   (33333)        1 2023-04-06 15:57:42.000000 playtour-0.0.2/src/playtour.egg-info/dependency_links.txt
+-rw-r--r--   0 gitpod   (33333) gitpod   (33333)       11 2023-04-06 15:57:42.000000 playtour-0.0.2/src/playtour.egg-info/requires.txt
+-rw-r--r--   0 gitpod   (33333) gitpod   (33333)       18 2023-04-06 15:57:42.000000 playtour-0.0.2/src/playtour.egg-info/top_level.txt
+-rw-r--r--   0 gitpod   (33333) gitpod   (33333)      891 2023-04-06 15:55:01.000000 playtour-0.0.2/src/playtour.py
```

### Comparing `playtour-0.0.1/LICENSE` & `playtour-0.0.2/LICENSE`

 * *Files identical despite different names*

### Comparing `playtour-0.0.1/pyproject.toml` & `playtour-0.0.2/pyproject.toml`

 * *Files 18% similar despite different names*

```diff
@@ -1,22 +1,25 @@
 [build-system]
 requires = ["setuptools>=61.0"]
 build-backend = "setuptools.build_meta"
 
 [project]
 name = "playtour"
-version = "0.0.1"
+version = "0.0.2"
 authors = [
   { name="ken", email="block24block@gmail.com" },
 ]
 description = "Loop page with playwright"
 readme = "README.md"
 requires-python = ">=3.7"
 classifiers = [
     "Programming Language :: Python :: 3",
     "License :: OSI Approved :: MIT License",
     "Operating System :: OS Independent",
 ]
+dependencies = [
+  "playwright",
+]
 
 [project.urls]
 "Homepage" = "https://github.com/turnon/playtour"
 "Bug Tracker" = "https://github.com/turnon/playtour/issues"
```

### Comparing `playtour-0.0.1/src/playtour/playtour.py` & `playtour-0.0.2/src/playtour.py`

 * *Files 16% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 from playwright.sync_api import sync_playwright
 
-def start(url=None, selector=None, wrapper=(lambda x: x), at=1, stop=None):
+def start(url=None, selector=None, wrapper=(lambda x: x), headless=True, at=1, stop=None):
     def page_nums():
         current = at
         while True:
             yield current
             if current == stop:
                 break
             current += 1
@@ -16,13 +16,13 @@
             if resp.status == 404:
                 break
             for selected in browser_page.query_selector_all(selector):
                 yield selected
 
     with (
         sync_playwright() as play,
-        play.chromium.launch(headless=False) as browser,
+        play.chromium.launch(headless=headless) as browser,
         browser.new_context() as ctx
         ):
         page = ctx.new_page()
         for element in fetch_elements(page):
             yield wrapper(element)
```

