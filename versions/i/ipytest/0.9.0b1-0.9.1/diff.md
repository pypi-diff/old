# Comparing `tmp/ipytest-0.9.0b1.tar.gz` & `tmp/ipytest-0.9.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/ipytest-0.9.0b1.tar", last modified: Wed Jun  3 20:28:45 2020, max compression
+gzip compressed data, was "dist/ipytest-0.9.1.tar", last modified: Sun Jul 12 22:57:29 2020, max compression
```

## Comparing `ipytest-0.9.0b1.tar` & `ipytest-0.9.1.tar`

### file list

```diff
@@ -1,18 +1,18 @@
-drwxrwxrwx   0 cmp       (1000) cmp       (1000)        0 2020-06-03 20:28:45.000000 ipytest-0.9.0b1/
-drwxrwxrwx   0 cmp       (1000) cmp       (1000)        0 2020-06-03 20:28:45.000000 ipytest-0.9.0b1/ipytest/
--rwxrwxrwx   0 cmp       (1000) cmp       (1000)     5733 2020-06-03 19:39:43.000000 ipytest-0.9.0b1/ipytest/_config.py
--rwxrwxrwx   0 cmp       (1000) cmp       (1000)     8239 2020-06-03 20:01:01.000000 ipytest-0.9.0b1/ipytest/_pytest_support.py
--rwxrwxrwx   0 cmp       (1000) cmp       (1000)     2488 2019-11-18 20:10:37.000000 ipytest-0.9.0b1/ipytest/_util.py
--rwxrwxrwx   0 cmp       (1000) cmp       (1000)      302 2020-05-20 19:56:15.000000 ipytest-0.9.0b1/ipytest/__init__.py
-drwxrwxrwx   0 cmp       (1000) cmp       (1000)        0 2020-06-03 20:28:45.000000 ipytest-0.9.0b1/ipytest.egg-info/
--rwxrwxrwx   0 cmp       (1000) cmp       (1000)        1 2020-06-03 20:28:45.000000 ipytest-0.9.0b1/ipytest.egg-info/dependency_links.txt
--rwxrwxrwx   0 cmp       (1000) cmp       (1000)    14878 2020-06-03 20:28:45.000000 ipytest-0.9.0b1/ipytest.egg-info/PKG-INFO
--rwxrwxrwx   0 cmp       (1000) cmp       (1000)       22 2020-06-03 20:28:45.000000 ipytest-0.9.0b1/ipytest.egg-info/requires.txt
--rwxrwxrwx   0 cmp       (1000) cmp       (1000)      288 2020-06-03 20:28:45.000000 ipytest-0.9.0b1/ipytest.egg-info/SOURCES.txt
--rwxrwxrwx   0 cmp       (1000) cmp       (1000)        8 2020-06-03 20:28:45.000000 ipytest-0.9.0b1/ipytest.egg-info/top_level.txt
--rwxrwxrwx   0 cmp       (1000) cmp       (1000)     1090 2020-05-20 20:29:08.000000 ipytest-0.9.0b1/LICENSE.md
--rwxrwxrwx   0 cmp       (1000) cmp       (1000)       37 2020-04-09 10:05:02.000000 ipytest-0.9.0b1/MANIFEST.in
--rwxrwxrwx   0 cmp       (1000) cmp       (1000)    14878 2020-06-03 20:28:45.000000 ipytest-0.9.0b1/PKG-INFO
--rwxrwxrwx   0 cmp       (1000) cmp       (1000)    11628 2020-06-03 20:05:24.000000 ipytest-0.9.0b1/Readme.md
--rwxrwxrwx   0 cmp       (1000) cmp       (1000)       77 2020-06-03 20:28:45.000000 ipytest-0.9.0b1/setup.cfg
--rwxrwxrwx   0 cmp       (1000) cmp       (1000)      805 2020-06-03 20:08:05.000000 ipytest-0.9.0b1/setup.py
+drwxrwxrwx   0 cmp       (1000) cmp       (1000)        0 2020-07-13 15:45:06.000000 ipytest-0.9.1/
+drwxrwxrwx   0 cmp       (1000) cmp       (1000)        0 2020-07-13 15:45:06.000000 ipytest-0.9.1/ipytest/
+-rwxrwxrwx   0 cmp       (1000) cmp       (1000)     5733 2020-07-12 13:50:49.000000 ipytest-0.9.1/ipytest/_config.py
+-rwxrwxrwx   0 cmp       (1000) cmp       (1000)     8239 2020-07-12 13:50:49.000000 ipytest-0.9.1/ipytest/_pytest_support.py
+-rwxrwxrwx   0 cmp       (1000) cmp       (1000)     2488 2019-11-18 20:10:37.000000 ipytest-0.9.1/ipytest/_util.py
+-rwxrwxrwx   0 cmp       (1000) cmp       (1000)      302 2020-07-12 13:50:49.000000 ipytest-0.9.1/ipytest/__init__.py
+drwxrwxrwx   0 cmp       (1000) cmp       (1000)        0 2020-07-13 15:45:06.000000 ipytest-0.9.1/ipytest.egg-info/
+-rwxrwxrwx   0 cmp       (1000) cmp       (1000)        1 2020-07-13 15:45:05.000000 ipytest-0.9.1/ipytest.egg-info/dependency_links.txt
+-rwxrwxrwx   0 cmp       (1000) cmp       (1000)    14943 2020-07-13 15:45:05.000000 ipytest-0.9.1/ipytest.egg-info/PKG-INFO
+-rwxrwxrwx   0 cmp       (1000) cmp       (1000)       30 2020-07-13 15:45:05.000000 ipytest-0.9.1/ipytest.egg-info/requires.txt
+-rwxrwxrwx   0 cmp       (1000) cmp       (1000)      288 2020-07-13 15:45:05.000000 ipytest-0.9.1/ipytest.egg-info/SOURCES.txt
+-rwxrwxrwx   0 cmp       (1000) cmp       (1000)        8 2020-07-13 15:45:05.000000 ipytest-0.9.1/ipytest.egg-info/top_level.txt
+-rwxrwxrwx   0 cmp       (1000) cmp       (1000)     1090 2020-07-12 13:50:49.000000 ipytest-0.9.1/LICENSE.md
+-rwxrwxrwx   0 cmp       (1000) cmp       (1000)       37 2020-04-09 10:05:02.000000 ipytest-0.9.1/MANIFEST.in
+-rwxrwxrwx   0 cmp       (1000) cmp       (1000)    14943 2020-07-13 15:45:06.000000 ipytest-0.9.1/PKG-INFO
+-rwxrwxrwx   0 cmp       (1000) cmp       (1000)    11679 2020-07-13 15:43:47.000000 ipytest-0.9.1/Readme.md
+-rwxrwxrwx   0 cmp       (1000) cmp       (1000)       77 2020-07-13 15:45:06.000000 ipytest-0.9.1/setup.cfg
+-rwxrwxrwx   0 cmp       (1000) cmp       (1000)      814 2020-07-13 15:43:39.000000 ipytest-0.9.1/setup.py
```

### Comparing `ipytest-0.9.0b1/ipytest/_config.py` & `ipytest-0.9.1/ipytest/_config.py`

 * *Files identical despite different names*

### Comparing `ipytest-0.9.0b1/ipytest/_pytest_support.py` & `ipytest-0.9.1/ipytest/_pytest_support.py`

 * *Files identical despite different names*

### Comparing `ipytest-0.9.0b1/ipytest/_util.py` & `ipytest-0.9.1/ipytest/_util.py`

 * *Files identical despite different names*

### Comparing `ipytest-0.9.0b1/ipytest.egg-info/PKG-INFO` & `ipytest-0.9.1/ipytest.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: ipytest
-Version: 0.9.0b1
+Version: 0.9.1
 Summary: Unit tests in IPython notebooks.
 Home-page: https://github.com/chmp/ipytest
 Author: Christopher Prohm
 Author-email: mail@cprohm.de
 License: MIT
 Description: # ipytest - Unit tests in IPython notebooks
         
@@ -73,15 +73,17 @@
            packages, it is advisable to install them as development packages, e.g.,
            `pip install -e .`.
         
         ## Changes
         
         Note: development is tracked on the `develop` branch.
         
-        - `development`:
+        - `0.9.1`:
+            - Add `ipython` as an explicit dependency
+        - `0.9.0`:
             - Add `Pytest>=5.4` to the requirements
             - Remove legacy functionality, mostly plain unittest integration
             - The `tempfile_fallback` also kicks in, if a filename was configured, but
               the file does not exist
             - Add `register_module` option to register the notebook with the module
               system of Python. This way `--doctest-modules` works as expected
         - `0.8.1`: release with sdist for conda-forge
```

### Comparing `ipytest-0.9.0b1/LICENSE.md` & `ipytest-0.9.1/LICENSE.md`

 * *Files identical despite different names*

### Comparing `ipytest-0.9.0b1/PKG-INFO` & `ipytest-0.9.1/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: ipytest
-Version: 0.9.0b1
+Version: 0.9.1
 Summary: Unit tests in IPython notebooks.
 Home-page: https://github.com/chmp/ipytest
 Author: Christopher Prohm
 Author-email: mail@cprohm.de
 License: MIT
 Description: # ipytest - Unit tests in IPython notebooks
         
@@ -73,15 +73,17 @@
            packages, it is advisable to install them as development packages, e.g.,
            `pip install -e .`.
         
         ## Changes
         
         Note: development is tracked on the `develop` branch.
         
-        - `development`:
+        - `0.9.1`:
+            - Add `ipython` as an explicit dependency
+        - `0.9.0`:
             - Add `Pytest>=5.4` to the requirements
             - Remove legacy functionality, mostly plain unittest integration
             - The `tempfile_fallback` also kicks in, if a filename was configured, but
               the file does not exist
             - Add `register_module` option to register the notebook with the module
               system of Python. This way `--doctest-modules` works as expected
         - `0.8.1`: release with sdist for conda-forge
```

### Comparing `ipytest-0.9.0b1/Readme.md` & `ipytest-0.9.1/Readme.md`

 * *Files 2% similar despite different names*

```diff
@@ -65,15 +65,17 @@
    packages, it is advisable to install them as development packages, e.g.,
    `pip install -e .`.
 
 ## Changes
 
 Note: development is tracked on the `develop` branch.
 
-- `development`:
+- `0.9.1`:
+    - Add `ipython` as an explicit dependency
+- `0.9.0`:
     - Add `Pytest>=5.4` to the requirements
     - Remove legacy functionality, mostly plain unittest integration
     - The `tempfile_fallback` also kicks in, if a filename was configured, but
       the file does not exist
     - Add `register_module` option to register the notebook with the module
       system of Python. This way `--doctest-modules` works as expected
 - `0.8.1`: release with sdist for conda-forge
```

### Comparing `ipytest-0.9.0b1/setup.py` & `ipytest-0.9.1/setup.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,24 +1,24 @@
 #!/usr/bin/env python
 import pathlib
 from setuptools import setup
 
 
 setup(
     name="ipytest",
-    version="0.9.0b1",
+    version="0.9.1",
     description="Unit tests in IPython notebooks.",
     long_description=pathlib.Path("Readme.md").read_text(),
     long_description_content_type="text/markdown",
     author="Christopher Prohm",
     url="https://github.com/chmp/ipytest",
     author_email="mail@cprohm.de",
     license="MIT",
     packages=["ipytest"],
-    install_requires=["packaging", "pytest>=5.4"],
+    install_requires=["packaging", "ipython", "pytest>=5.4"],
     tests_require=["pytest"],
     python_requires=">=3",
     classifiers=[
         "Development Status :: 4 - Beta",
         "Intended Audience :: Developers",
         "Topic :: Software Development :: Testing",
         "License :: OSI Approved :: MIT License",
```

