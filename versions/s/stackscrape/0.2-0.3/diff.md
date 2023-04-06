# Comparing `tmp/stackscrape-0.2.tar.gz` & `tmp/stackscrape-0.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "stackscrape-0.2.tar", last modified: Thu Apr  6 18:45:55 2023, max compression
+gzip compressed data, was "stackscrape-0.3.tar", last modified: Thu Apr  6 18:50:22 2023, max compression
```

## Comparing `stackscrape-0.2.tar` & `stackscrape-0.3.tar`

### file list

```diff
@@ -1,10 +1,10 @@
--rw-r--r--   0        0        0       35 2022-03-14 22:35:08.000000 stackscrape-0.2/.gitignore
--rw-r--r--   0        0        0      495 2023-04-06 17:43:23.602669 stackscrape-0.2/.vscode/launch.json
--rw-r--r--   0        0        0     1072 2023-04-06 16:29:58.964435 stackscrape-0.2/LICENSE
--rw-r--r--   0        0        0       96 2023-04-06 16:29:00.321330 stackscrape-0.2/README.md
--rw-r--r--   0        0        0      775 2023-04-06 16:45:33.674630 stackscrape-0.2/pyproject.toml
--rw-r--r--   0        0        0     1140 2023-04-06 18:44:50.942835 stackscrape-0.2/stackscrape/__init__.py
--rw-r--r--   0        0        0       69 2022-03-14 22:05:33.000000 stackscrape-0.2/stackscrape/__main__.py
--rw-r--r--   0        0        0     3022 2023-04-06 18:44:43.364676 stackscrape-0.2/stackscrape/stackscrape.py
--rw-r--r--   0        0        0       81 2023-04-06 17:56:08.582292 stackscrape-0.2/test.py
--rw-r--r--   0        0        0      625 1970-01-01 00:00:00.000000 stackscrape-0.2/PKG-INFO
+-rw-r--r--   0        0        0       35 2022-03-14 22:35:08.000000 stackscrape-0.3/.gitignore
+-rw-r--r--   0        0        0      495 2023-04-06 17:43:23.602669 stackscrape-0.3/.vscode/launch.json
+-rw-r--r--   0        0        0     1072 2023-04-06 16:29:58.964435 stackscrape-0.3/LICENSE
+-rw-r--r--   0        0        0      825 2023-04-06 18:47:23.240664 stackscrape-0.3/README.md
+-rw-r--r--   0        0        0      775 2023-04-06 16:45:33.674630 stackscrape-0.3/pyproject.toml
+-rw-r--r--   0        0        0     1142 2023-04-06 18:48:44.919323 stackscrape-0.3/stackscrape/__init__.py
+-rw-r--r--   0        0        0       69 2022-03-14 22:05:33.000000 stackscrape-0.3/stackscrape/__main__.py
+-rw-r--r--   0        0        0     3022 2023-04-06 18:44:43.364676 stackscrape-0.3/stackscrape/stackscrape.py
+-rw-r--r--   0        0        0       81 2023-04-06 17:56:08.582292 stackscrape-0.3/test.py
+-rw-r--r--   0        0        0     1354 1970-01-01 00:00:00.000000 stackscrape-0.3/PKG-INFO
```

### Comparing `stackscrape-0.2/LICENSE` & `stackscrape-0.3/LICENSE`

 * *Files identical despite different names*

### Comparing `stackscrape-0.2/pyproject.toml` & `stackscrape-0.3/pyproject.toml`

 * *Files identical despite different names*

### Comparing `stackscrape-0.2/stackscrape/__init__.py` & `stackscrape-0.3/stackscrape/__init__.py`

 * *Files 2% similar despite different names*

```diff
@@ -16,23 +16,23 @@
   -n NUM --num=NUM        Max number of items to fetch. [default: 1000]
   -o OUT --out=OUT        Save results to file OUT.
   -h --help               Show this screen.
   --version               Show version.
 
 """
 
-__version__ = '0.2'
+__version__ = '0.3'
 
 from docopt import docopt, DocoptExit
 from .stackscrape import get_qa
 
 
 def main():
     arguments = docopt(__doc__, version=__version__)
     site = arguments['--site']
     tag = arguments['--tag']
-    text = arguments['--text']
+    text = arguments['--filter']
     days = int(arguments['--days'])
     num = int(arguments['--num'])
     out = arguments['--out']
     get_qa(site, tag, text, days, num, out)
```

### Comparing `stackscrape-0.2/stackscrape/stackscrape.py` & `stackscrape-0.3/stackscrape/stackscrape.py`

 * *Files identical despite different names*

