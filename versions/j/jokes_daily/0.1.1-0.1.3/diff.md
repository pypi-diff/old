# Comparing `tmp/jokes_daily-0.1.1.tar.gz` & `tmp/jokes_daily-0.1.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "jokes_daily-0.1.1.tar", last modified: Thu Apr  6 18:01:37 2023, max compression
+gzip compressed data, was "jokes_daily-0.1.3.tar", last modified: Fri Apr  7 04:58:53 2023, max compression
```

## Comparing `jokes_daily-0.1.1.tar` & `jokes_daily-0.1.3.tar`

### file list

```diff
@@ -1,14 +1,16 @@
--rw-r--r--   0        0        0     1078 2023-04-02 11:19:30.759600 jokes_daily-0.1.1/LICENSE
--rw-r--r--   0        0        0      634 2023-04-02 13:36:03.447449 jokes_daily-0.1.1/docs/Makefile
--rw-r--r--   0        0        0       32 2023-04-02 13:53:22.369921 jokes_daily-0.1.1/docs/cli.rst
--rw-r--r--   0        0        0     1252 2023-04-02 13:52:56.663718 jokes_daily-0.1.1/docs/conf.py
--rw-r--r--   0        0        0       33 2023-04-02 13:53:26.860605 jokes_daily-0.1.1/docs/core.rst
--rw-r--r--   0        0        0      470 2023-04-02 14:02:07.259560 jokes_daily-0.1.1/docs/index.rst
--rw-r--r--   0        0        0      800 2023-04-02 13:36:03.449124 jokes_daily-0.1.1/docs/make.bat
--rw-r--r--   0        0        0      596 2023-04-02 14:18:20.616636 jokes_daily-0.1.1/docs/quickstart.rst
--rw-r--r--   0        0        0      160 2023-04-06 17:58:48.805269 jokes_daily-0.1.1/jokes_daily/__init__.py
--rw-r--r--   0        0        0      552 2023-04-02 11:30:44.960506 jokes_daily-0.1.1/jokes_daily/cli.py
--rw-r--r--   0        0        0     1305 2023-04-02 11:03:10.492725 jokes_daily-0.1.1/jokes_daily/core.py
--rw-r--r--   0        0        0      497 2023-04-06 17:58:55.190287 jokes_daily-0.1.1/pyproject.toml
--rw-r--r--   0        0        0      689 2023-04-06 18:00:33.730243 jokes_daily-0.1.1/readme.md
--rw-r--r--   0        0        0     1071 1970-01-01 00:00:00.000000 jokes_daily-0.1.1/PKG-INFO
+-rw-r--r--   0        0        0      192 2023-04-07 04:57:17.938831 jokes_daily-0.1.3/.bumpversion.cfg
+-rw-r--r--   0        0        0     1078 2023-04-02 11:19:30.759600 jokes_daily-0.1.3/LICENSE
+-rw-r--r--   0        0        0      634 2023-04-02 13:36:03.447449 jokes_daily-0.1.3/docs/Makefile
+-rw-r--r--   0        0        0       32 2023-04-02 13:53:22.369921 jokes_daily-0.1.3/docs/cli.rst
+-rw-r--r--   0        0        0     1252 2023-04-02 13:52:56.663718 jokes_daily-0.1.3/docs/conf.py
+-rw-r--r--   0        0        0       33 2023-04-02 13:53:26.860605 jokes_daily-0.1.3/docs/core.rst
+-rw-r--r--   0        0        0      470 2023-04-02 14:02:07.259560 jokes_daily-0.1.3/docs/index.rst
+-rw-r--r--   0        0        0      800 2023-04-02 13:36:03.449124 jokes_daily-0.1.3/docs/make.bat
+-rw-r--r--   0        0        0      596 2023-04-02 14:18:20.616636 jokes_daily-0.1.3/docs/quickstart.rst
+-rw-r--r--   0        0        0      160 2023-04-07 04:57:17.938445 jokes_daily-0.1.3/jokes_daily/__init__.py
+-rw-r--r--   0        0        0      552 2023-04-02 11:30:44.960506 jokes_daily-0.1.3/jokes_daily/cli.py
+-rw-r--r--   0        0        0     1305 2023-04-02 11:03:10.492725 jokes_daily-0.1.3/jokes_daily/core.py
+-rw-r--r--   0        0        0      499 2023-04-07 04:55:53.554547 jokes_daily-0.1.3/pyproject.toml
+-rw-r--r--   0        0        0      689 2023-04-06 18:00:33.730243 jokes_daily-0.1.3/readme.md
+-rw-r--r--   0        0        0      517 2023-04-07 04:37:09.889334 jokes_daily-0.1.3/requirements.dev.txt
+-rw-r--r--   0        0        0     1071 1970-01-01 00:00:00.000000 jokes_daily-0.1.3/PKG-INFO
```

### Comparing `jokes_daily-0.1.1/LICENSE` & `jokes_daily-0.1.3/LICENSE`

 * *Files identical despite different names*

### Comparing `jokes_daily-0.1.1/docs/Makefile` & `jokes_daily-0.1.3/docs/Makefile`

 * *Files identical despite different names*

### Comparing `jokes_daily-0.1.1/docs/conf.py` & `jokes_daily-0.1.3/docs/conf.py`

 * *Files identical despite different names*

### Comparing `jokes_daily-0.1.1/docs/make.bat` & `jokes_daily-0.1.3/docs/make.bat`

 * *Files identical despite different names*

### Comparing `jokes_daily-0.1.1/docs/quickstart.rst` & `jokes_daily-0.1.3/docs/quickstart.rst`

 * *Files identical despite different names*

### Comparing `jokes_daily-0.1.1/jokes_daily/cli.py` & `jokes_daily-0.1.3/jokes_daily/cli.py`

 * *Files identical despite different names*

### Comparing `jokes_daily-0.1.1/jokes_daily/core.py` & `jokes_daily-0.1.3/jokes_daily/core.py`

 * *Files identical despite different names*

### Comparing `jokes_daily-0.1.1/readme.md` & `jokes_daily-0.1.3/readme.md`

 * *Files identical despite different names*

### Comparing `jokes_daily-0.1.1/PKG-INFO` & `jokes_daily-0.1.3/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: jokes_daily
-Version: 0.1.1
+Version: 0.1.3
 Summary: jokes_daily is a python cli app to generate jokes from your terminal
 Author-email: Nikhil Akki <nikhil.akki@outlook.com>
 Description-Content-Type: text/markdown
 Classifier: License :: OSI Approved :: MIT License
 Project-URL: Home, https://github.com/nikhilakki/nikhilakki.in-blog-code-examples/tree/main/jokes_daily
 
 # Jokes Daily is a simple CLI app
```

