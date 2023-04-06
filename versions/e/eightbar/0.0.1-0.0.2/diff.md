# Comparing `tmp/eightbar-0.0.1.tar.gz` & `tmp/eightbar-0.0.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "eightbar-0.0.1.tar", last modified: Thu Apr  6 20:46:41 2023, max compression
+gzip compressed data, was "eightbar-0.0.2.tar", last modified: Thu Apr  6 20:49:16 2023, max compression
```

## Comparing `eightbar-0.0.1.tar` & `eightbar-0.0.2.tar`

### file list

```diff
@@ -1,49 +1,49 @@
-drwxr-xr-x   0 mtm        (501) staff       (20)        0 2023-04-06 20:46:41.690733 eightbar-0.0.1/
--rw-r--r--   0 mtm        (501) staff       (20)      591 2023-04-05 19:59:49.000000 eightbar-0.0.1/.coveragerc
--rw-r--r--   0 mtm        (501) staff       (20)      566 2023-04-05 19:59:49.000000 eightbar-0.0.1/.gitignore
--rw-r--r--   0 mtm        (501) staff       (20)       56 2023-04-05 19:59:49.000000 eightbar-0.0.1/.isort.cfg
--rw-r--r--   0 mtm        (501) staff       (20)     1670 2023-04-06 05:27:11.000000 eightbar-0.0.1/.pre-commit-config.yaml
--rw-r--r--   0 mtm        (501) staff       (20)      530 2023-04-05 19:59:49.000000 eightbar-0.0.1/.readthedocs.yml
--rw-r--r--   0 mtm        (501) staff       (20)       87 2023-04-05 19:59:49.000000 eightbar-0.0.1/AUTHORS.rst
--rw-r--r--   0 mtm        (501) staff       (20)      128 2023-04-05 19:59:49.000000 eightbar-0.0.1/CHANGELOG.rst
--rw-r--r--   0 mtm        (501) staff       (20)    13827 2023-04-05 19:59:49.000000 eightbar-0.0.1/CONTRIBUTING.rst
--rw-r--r--   0 mtm        (501) staff       (20)     1083 2023-04-05 19:59:49.000000 eightbar-0.0.1/LICENSE.txt
--rw-r--r--   0 mtm        (501) staff       (20)     2544 2023-04-06 20:46:41.690981 eightbar-0.0.1/PKG-INFO
--rw-r--r--   0 mtm        (501) staff       (20)     2067 2023-04-05 19:59:49.000000 eightbar-0.0.1/README.rst
-drwxr-xr-x   0 mtm        (501) staff       (20)        0 2023-04-06 20:46:41.674939 eightbar-0.0.1/docs/
--rw-r--r--   0 mtm        (501) staff       (20)     1154 2023-04-05 19:59:49.000000 eightbar-0.0.1/docs/Makefile
-drwxr-xr-x   0 mtm        (501) staff       (20)        0 2023-04-06 20:46:41.676017 eightbar-0.0.1/docs/_static/
--rw-r--r--   0 mtm        (501) staff       (20)       18 2023-04-05 19:59:49.000000 eightbar-0.0.1/docs/_static/.gitignore
--rw-r--r--   0 mtm        (501) staff       (20)       41 2023-04-05 19:59:49.000000 eightbar-0.0.1/docs/authors.rst
--rw-r--r--   0 mtm        (501) staff       (20)       43 2023-04-05 19:59:49.000000 eightbar-0.0.1/docs/changelog.rst
--rw-r--r--   0 mtm        (501) staff       (20)     9737 2023-04-05 20:18:10.000000 eightbar-0.0.1/docs/conf.py
--rw-r--r--   0 mtm        (501) staff       (20)       33 2023-04-05 19:59:49.000000 eightbar-0.0.1/docs/contributing.rst
--rw-r--r--   0 mtm        (501) staff       (20)     2317 2023-04-05 19:59:49.000000 eightbar-0.0.1/docs/index.rst
--rw-r--r--   0 mtm        (501) staff       (20)       67 2023-04-05 19:59:49.000000 eightbar-0.0.1/docs/license.rst
--rw-r--r--   0 mtm        (501) staff       (20)       39 2023-04-05 19:59:49.000000 eightbar-0.0.1/docs/readme.rst
--rw-r--r--   0 mtm        (501) staff       (20)      233 2023-04-05 19:59:49.000000 eightbar-0.0.1/docs/requirements.txt
--rw-r--r--   0 mtm        (501) staff       (20)      346 2023-04-05 19:59:49.000000 eightbar-0.0.1/pyproject.toml
--rw-r--r--   0 mtm        (501) staff       (20)     1258 2023-04-06 20:46:41.692506 eightbar-0.0.1/setup.cfg
--rw-r--r--   0 mtm        (501) staff       (20)      703 2023-04-05 19:59:49.000000 eightbar-0.0.1/setup.py
-drwxr-xr-x   0 mtm        (501) staff       (20)        0 2023-04-06 20:46:41.659175 eightbar-0.0.1/src/
-drwxr-xr-x   0 mtm        (501) staff       (20)        0 2023-04-06 20:46:41.683548 eightbar-0.0.1/src/eightbar/
--rw-r--r--   0 mtm        (501) staff       (20)      577 2023-04-05 19:59:49.000000 eightbar-0.0.1/src/eightbar/__init__.py
--rw-r--r--   0 mtm        (501) staff       (20)     2109 2023-04-06 19:20:29.000000 eightbar-0.0.1/src/eightbar/component.py
--rw-r--r--   0 mtm        (501) staff       (20)     9822 2023-04-06 19:23:46.000000 eightbar-0.0.1/src/eightbar/lib.py
--rw-r--r--   0 mtm        (501) staff       (20)     2672 2023-04-06 13:34:33.000000 eightbar-0.0.1/src/eightbar/main.py
--rw-r--r--   0 mtm        (501) staff       (20)       99 2023-04-06 19:11:25.000000 eightbar-0.0.1/src/eightbar/product.py
-drwxr-xr-x   0 mtm        (501) staff       (20)        0 2023-04-06 20:46:41.688903 eightbar-0.0.1/src/eightbar/templates/
--rw-r--r--   0 mtm        (501) staff       (20)      153 2023-04-06 04:51:15.000000 eightbar-0.0.1/src/eightbar/templates/view1.j2
--rw-r--r--   0 mtm        (501) staff       (20)     3836 2023-04-06 17:40:03.000000 eightbar-0.0.1/src/eightbar/versions.py
-drwxr-xr-x   0 mtm        (501) staff       (20)        0 2023-04-06 20:46:41.688365 eightbar-0.0.1/src/eightbar.egg-info/
--rw-r--r--   0 mtm        (501) staff       (20)     2544 2023-04-06 20:46:41.000000 eightbar-0.0.1/src/eightbar.egg-info/PKG-INFO
--rw-r--r--   0 mtm        (501) staff       (20)      828 2023-04-06 20:46:41.000000 eightbar-0.0.1/src/eightbar.egg-info/SOURCES.txt
--rw-r--r--   0 mtm        (501) staff       (20)        1 2023-04-06 20:46:41.000000 eightbar-0.0.1/src/eightbar.egg-info/dependency_links.txt
--rw-r--r--   0 mtm        (501) staff       (20)       47 2023-04-06 20:46:41.000000 eightbar-0.0.1/src/eightbar.egg-info/entry_points.txt
--rw-r--r--   0 mtm        (501) staff       (20)        1 2023-04-06 20:46:41.000000 eightbar-0.0.1/src/eightbar.egg-info/not-zip-safe
--rw-r--r--   0 mtm        (501) staff       (20)      102 2023-04-06 20:46:41.000000 eightbar-0.0.1/src/eightbar.egg-info/requires.txt
--rw-r--r--   0 mtm        (501) staff       (20)        9 2023-04-06 20:46:41.000000 eightbar-0.0.1/src/eightbar.egg-info/top_level.txt
-drwxr-xr-x   0 mtm        (501) staff       (20)        0 2023-04-06 20:46:41.690240 eightbar-0.0.1/tests/
--rw-r--r--   0 mtm        (501) staff       (20)      276 2023-04-05 19:59:49.000000 eightbar-0.0.1/tests/conftest.py
--rw-r--r--   0 mtm        (501) staff       (20)      593 2023-04-05 19:59:49.000000 eightbar-0.0.1/tests/test_skeleton.py
--rw-r--r--   0 mtm        (501) staff       (20)     2851 2023-04-05 19:59:49.000000 eightbar-0.0.1/tox.ini
+drwxr-xr-x   0 mtm        (501) staff       (20)        0 2023-04-06 20:49:16.937993 eightbar-0.0.2/
+-rw-r--r--   0 mtm        (501) staff       (20)      591 2023-04-05 19:59:49.000000 eightbar-0.0.2/.coveragerc
+-rw-r--r--   0 mtm        (501) staff       (20)      566 2023-04-05 19:59:49.000000 eightbar-0.0.2/.gitignore
+-rw-r--r--   0 mtm        (501) staff       (20)       56 2023-04-05 19:59:49.000000 eightbar-0.0.2/.isort.cfg
+-rw-r--r--   0 mtm        (501) staff       (20)     1670 2023-04-06 05:27:11.000000 eightbar-0.0.2/.pre-commit-config.yaml
+-rw-r--r--   0 mtm        (501) staff       (20)      530 2023-04-05 19:59:49.000000 eightbar-0.0.2/.readthedocs.yml
+-rw-r--r--   0 mtm        (501) staff       (20)       87 2023-04-05 19:59:49.000000 eightbar-0.0.2/AUTHORS.rst
+-rw-r--r--   0 mtm        (501) staff       (20)      128 2023-04-05 19:59:49.000000 eightbar-0.0.2/CHANGELOG.rst
+-rw-r--r--   0 mtm        (501) staff       (20)    13827 2023-04-05 19:59:49.000000 eightbar-0.0.2/CONTRIBUTING.rst
+-rw-r--r--   0 mtm        (501) staff       (20)     1083 2023-04-05 19:59:49.000000 eightbar-0.0.2/LICENSE.txt
+-rw-r--r--   0 mtm        (501) staff       (20)     2544 2023-04-06 20:49:16.938250 eightbar-0.0.2/PKG-INFO
+-rw-r--r--   0 mtm        (501) staff       (20)     2067 2023-04-05 19:59:49.000000 eightbar-0.0.2/README.rst
+drwxr-xr-x   0 mtm        (501) staff       (20)        0 2023-04-06 20:49:16.926962 eightbar-0.0.2/docs/
+-rw-r--r--   0 mtm        (501) staff       (20)     1154 2023-04-05 19:59:49.000000 eightbar-0.0.2/docs/Makefile
+drwxr-xr-x   0 mtm        (501) staff       (20)        0 2023-04-06 20:49:16.927657 eightbar-0.0.2/docs/_static/
+-rw-r--r--   0 mtm        (501) staff       (20)       18 2023-04-05 19:59:49.000000 eightbar-0.0.2/docs/_static/.gitignore
+-rw-r--r--   0 mtm        (501) staff       (20)       41 2023-04-05 19:59:49.000000 eightbar-0.0.2/docs/authors.rst
+-rw-r--r--   0 mtm        (501) staff       (20)       43 2023-04-05 19:59:49.000000 eightbar-0.0.2/docs/changelog.rst
+-rw-r--r--   0 mtm        (501) staff       (20)     9737 2023-04-05 20:18:10.000000 eightbar-0.0.2/docs/conf.py
+-rw-r--r--   0 mtm        (501) staff       (20)       33 2023-04-05 19:59:49.000000 eightbar-0.0.2/docs/contributing.rst
+-rw-r--r--   0 mtm        (501) staff       (20)     2317 2023-04-05 19:59:49.000000 eightbar-0.0.2/docs/index.rst
+-rw-r--r--   0 mtm        (501) staff       (20)       67 2023-04-05 19:59:49.000000 eightbar-0.0.2/docs/license.rst
+-rw-r--r--   0 mtm        (501) staff       (20)       39 2023-04-05 19:59:49.000000 eightbar-0.0.2/docs/readme.rst
+-rw-r--r--   0 mtm        (501) staff       (20)      233 2023-04-05 19:59:49.000000 eightbar-0.0.2/docs/requirements.txt
+-rw-r--r--   0 mtm        (501) staff       (20)      346 2023-04-05 19:59:49.000000 eightbar-0.0.2/pyproject.toml
+-rw-r--r--   0 mtm        (501) staff       (20)     1269 2023-04-06 20:49:16.939833 eightbar-0.0.2/setup.cfg
+-rw-r--r--   0 mtm        (501) staff       (20)      703 2023-04-05 19:59:49.000000 eightbar-0.0.2/setup.py
+drwxr-xr-x   0 mtm        (501) staff       (20)        0 2023-04-06 20:49:16.913228 eightbar-0.0.2/src/
+drwxr-xr-x   0 mtm        (501) staff       (20)        0 2023-04-06 20:49:16.931751 eightbar-0.0.2/src/eightbar/
+-rw-r--r--   0 mtm        (501) staff       (20)      577 2023-04-05 19:59:49.000000 eightbar-0.0.2/src/eightbar/__init__.py
+-rw-r--r--   0 mtm        (501) staff       (20)     2109 2023-04-06 19:20:29.000000 eightbar-0.0.2/src/eightbar/component.py
+-rw-r--r--   0 mtm        (501) staff       (20)     9822 2023-04-06 19:23:46.000000 eightbar-0.0.2/src/eightbar/lib.py
+-rw-r--r--   0 mtm        (501) staff       (20)     2672 2023-04-06 13:34:33.000000 eightbar-0.0.2/src/eightbar/main.py
+-rw-r--r--   0 mtm        (501) staff       (20)       99 2023-04-06 19:11:25.000000 eightbar-0.0.2/src/eightbar/product.py
+drwxr-xr-x   0 mtm        (501) staff       (20)        0 2023-04-06 20:49:16.936254 eightbar-0.0.2/src/eightbar/templates/
+-rw-r--r--   0 mtm        (501) staff       (20)      153 2023-04-06 04:51:15.000000 eightbar-0.0.2/src/eightbar/templates/view1.j2
+-rw-r--r--   0 mtm        (501) staff       (20)     3836 2023-04-06 17:40:03.000000 eightbar-0.0.2/src/eightbar/versions.py
+drwxr-xr-x   0 mtm        (501) staff       (20)        0 2023-04-06 20:49:16.935781 eightbar-0.0.2/src/eightbar.egg-info/
+-rw-r--r--   0 mtm        (501) staff       (20)     2544 2023-04-06 20:49:16.000000 eightbar-0.0.2/src/eightbar.egg-info/PKG-INFO
+-rw-r--r--   0 mtm        (501) staff       (20)      828 2023-04-06 20:49:16.000000 eightbar-0.0.2/src/eightbar.egg-info/SOURCES.txt
+-rw-r--r--   0 mtm        (501) staff       (20)        1 2023-04-06 20:49:16.000000 eightbar-0.0.2/src/eightbar.egg-info/dependency_links.txt
+-rw-r--r--   0 mtm        (501) staff       (20)       47 2023-04-06 20:49:16.000000 eightbar-0.0.2/src/eightbar.egg-info/entry_points.txt
+-rw-r--r--   0 mtm        (501) staff       (20)        1 2023-04-06 20:49:16.000000 eightbar-0.0.2/src/eightbar.egg-info/not-zip-safe
+-rw-r--r--   0 mtm        (501) staff       (20)      112 2023-04-06 20:49:16.000000 eightbar-0.0.2/src/eightbar.egg-info/requires.txt
+-rw-r--r--   0 mtm        (501) staff       (20)        9 2023-04-06 20:49:16.000000 eightbar-0.0.2/src/eightbar.egg-info/top_level.txt
+drwxr-xr-x   0 mtm        (501) staff       (20)        0 2023-04-06 20:49:16.937470 eightbar-0.0.2/tests/
+-rw-r--r--   0 mtm        (501) staff       (20)      276 2023-04-05 19:59:49.000000 eightbar-0.0.2/tests/conftest.py
+-rw-r--r--   0 mtm        (501) staff       (20)      593 2023-04-05 19:59:49.000000 eightbar-0.0.2/tests/test_skeleton.py
+-rw-r--r--   0 mtm        (501) staff       (20)     2851 2023-04-05 19:59:49.000000 eightbar-0.0.2/tox.ini
```

### Comparing `eightbar-0.0.1/.coveragerc` & `eightbar-0.0.2/.coveragerc`

 * *Files identical despite different names*

### Comparing `eightbar-0.0.1/.gitignore` & `eightbar-0.0.2/.gitignore`

 * *Files identical despite different names*

### Comparing `eightbar-0.0.1/.pre-commit-config.yaml` & `eightbar-0.0.2/.pre-commit-config.yaml`

 * *Files identical despite different names*

### Comparing `eightbar-0.0.1/.readthedocs.yml` & `eightbar-0.0.2/.readthedocs.yml`

 * *Files identical despite different names*

### Comparing `eightbar-0.0.1/CONTRIBUTING.rst` & `eightbar-0.0.2/CONTRIBUTING.rst`

 * *Files identical despite different names*

### Comparing `eightbar-0.0.1/LICENSE.txt` & `eightbar-0.0.2/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `eightbar-0.0.1/PKG-INFO` & `eightbar-0.0.2/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: eightbar
-Version: 0.0.1
+Version: 0.0.2
 Summary: Add a short description here!
 Home-page: https://github.com/pyscaffold/pyscaffold/
 Author: Taylor Monacelli
 Author-email: taylormonacelli@gmail.com
 License: MIT
 Project-URL: Documentation, https://pyscaffold.org/
 Platform: any
```

### Comparing `eightbar-0.0.1/README.rst` & `eightbar-0.0.2/README.rst`

 * *Files identical despite different names*

### Comparing `eightbar-0.0.1/docs/Makefile` & `eightbar-0.0.2/docs/Makefile`

 * *Files identical despite different names*

### Comparing `eightbar-0.0.1/docs/conf.py` & `eightbar-0.0.2/docs/conf.py`

 * *Files identical despite different names*

### Comparing `eightbar-0.0.1/docs/index.rst` & `eightbar-0.0.2/docs/index.rst`

 * *Files identical despite different names*

### Comparing `eightbar-0.0.1/setup.cfg` & `eightbar-0.0.2/setup.cfg`

 * *Files 1% similar despite different names*

```diff
@@ -21,14 +21,15 @@
 include_package_data = True
 package_dir = 
 	=src
 install_requires = 
 	importlib-metadata; python_version<"3.8"
 	requests
 	jinja2
+	packaging
 
 [options.packages.find]
 where = src
 exclude = 
 	tests
 
 [options.extras_require]
```

### Comparing `eightbar-0.0.1/setup.py` & `eightbar-0.0.2/setup.py`

 * *Files identical despite different names*

### Comparing `eightbar-0.0.1/src/eightbar/__init__.py` & `eightbar-0.0.2/src/eightbar/__init__.py`

 * *Files identical despite different names*

### Comparing `eightbar-0.0.1/src/eightbar/component.py` & `eightbar-0.0.2/src/eightbar/component.py`

 * *Files identical despite different names*

### Comparing `eightbar-0.0.1/src/eightbar/lib.py` & `eightbar-0.0.2/src/eightbar/lib.py`

 * *Files identical despite different names*

### Comparing `eightbar-0.0.1/src/eightbar/main.py` & `eightbar-0.0.2/src/eightbar/main.py`

 * *Files identical despite different names*

### Comparing `eightbar-0.0.1/src/eightbar/versions.py` & `eightbar-0.0.2/src/eightbar/versions.py`

 * *Files identical despite different names*

### Comparing `eightbar-0.0.1/src/eightbar.egg-info/PKG-INFO` & `eightbar-0.0.2/src/eightbar.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: eightbar
-Version: 0.0.1
+Version: 0.0.2
 Summary: Add a short description here!
 Home-page: https://github.com/pyscaffold/pyscaffold/
 Author: Taylor Monacelli
 Author-email: taylormonacelli@gmail.com
 License: MIT
 Project-URL: Documentation, https://pyscaffold.org/
 Platform: any
```

### Comparing `eightbar-0.0.1/src/eightbar.egg-info/SOURCES.txt` & `eightbar-0.0.2/src/eightbar.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `eightbar-0.0.1/tests/test_skeleton.py` & `eightbar-0.0.2/tests/test_skeleton.py`

 * *Files identical despite different names*

### Comparing `eightbar-0.0.1/tox.ini` & `eightbar-0.0.2/tox.ini`

 * *Files identical despite different names*

