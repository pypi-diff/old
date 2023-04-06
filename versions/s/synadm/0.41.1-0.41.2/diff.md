# Comparing `tmp/synadm-0.41.1.tar.gz` & `tmp/synadm-0.41.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "synadm-0.41.1.tar", last modified: Sat Mar 25 17:24:03 2023, max compression
+gzip compressed data, was "synadm-0.41.2.tar", last modified: Thu Apr  6 17:28:00 2023, max compression
```

## Comparing `synadm-0.41.1.tar` & `synadm-0.41.2.tar`

### file list

```diff
@@ -1,56 +1,56 @@
-drwxr-xr-x   0 jackson    (501) staff       (20)        0 2023-03-25 17:24:03.987013 synadm-0.41.1/
--rw-r--r--   0 jackson    (501) staff       (20)      245 2023-03-25 16:56:01.000000 synadm-0.41.1/.bumpversion.cfg
-drwxr-xr-x   0 jackson    (501) staff       (20)        0 2023-03-25 17:24:03.976020 synadm-0.41.1/.github/
-drwxr-xr-x   0 jackson    (501) staff       (20)        0 2023-03-25 17:24:03.979511 synadm-0.41.1/.github/workflows/
--rw-r--r--   0 jackson    (501) staff       (20)      435 2023-03-15 12:29:09.000000 synadm-0.41.1/.github/workflows/lint.yaml
--rw-r--r--   0 jackson    (501) staff       (20)     2736 2023-02-24 10:57:22.000000 synadm-0.41.1/.github/workflows/release.yaml
--rw-r--r--   0 jackson    (501) staff       (20)       96 2023-03-25 16:54:14.000000 synadm-0.41.1/.gitignore
--rw-r--r--   0 jackson    (501) staff       (20)    35148 2023-02-24 10:57:22.000000 synadm-0.41.1/LICENSE
--rw-r--r--   0 jackson    (501) staff       (20)      646 2023-02-24 10:57:22.000000 synadm-0.41.1/Makefile
--rw-r--r--   0 jackson    (501) staff       (20)    14558 2023-03-25 17:24:03.986651 synadm-0.41.1/PKG-INFO
--rw-r--r--   0 jackson    (501) staff       (20)    13504 2023-03-25 16:54:14.000000 synadm-0.41.1/README.md
--rwxr-xr-x   0 jackson    (501) staff       (20)      814 2023-02-24 10:57:22.000000 synadm-0.41.1/bump.sh
-drwxr-xr-x   0 jackson    (501) staff       (20)        0 2023-03-25 17:24:03.976145 synadm-0.41.1/doc/
-drwxr-xr-x   0 jackson    (501) staff       (20)        0 2023-03-25 17:24:03.982787 synadm-0.41.1/doc/source/
--rw-r--r--   0 jackson    (501) staff       (20)     2554 2023-03-25 16:56:01.000000 synadm-0.41.1/doc/source/conf.py
--rw-r--r--   0 jackson    (501) staff       (20)      486 2023-03-25 16:54:14.000000 synadm-0.41.1/doc/source/index.rst
--rw-r--r--   0 jackson    (501) staff       (20)      303 2023-03-15 12:29:09.000000 synadm-0.41.1/doc/source/index_cli_reference.rst
--rw-r--r--   0 jackson    (501) staff       (20)      149 2023-02-24 10:57:22.000000 synadm-0.41.1/doc/source/index_modules.rst
--rw-r--r--   0 jackson    (501) staff       (20)      110 2023-02-24 10:57:22.000000 synadm-0.41.1/doc/source/synadm.cli.config.rst
--rw-r--r--   0 jackson    (501) staff       (20)       86 2023-02-24 10:57:22.000000 synadm-0.41.1/doc/source/synadm.cli.group.rst
--rw-r--r--   0 jackson    (501) staff       (20)       96 2023-02-24 10:57:22.000000 synadm-0.41.1/doc/source/synadm.cli.history.rst
--rw-r--r--   0 jackson    (501) staff       (20)       92 2023-02-24 10:57:22.000000 synadm-0.41.1/doc/source/synadm.cli.matrix.rst
--rw-r--r--   0 jackson    (501) staff       (20)       86 2023-02-24 10:57:22.000000 synadm-0.41.1/doc/source/synadm.cli.media.rst
--rw-r--r--   0 jackson    (501) staff       (20)       92 2023-03-15 12:29:09.000000 synadm-0.41.1/doc/source/synadm.cli.notice.rst
--rw-r--r--   0 jackson    (501) staff       (20)       92 2023-02-24 10:57:22.000000 synadm-0.41.1/doc/source/synadm.cli.regtok.rst
--rw-r--r--   0 jackson    (501) staff       (20)       81 2023-02-24 10:57:22.000000 synadm-0.41.1/doc/source/synadm.cli.room.rst
--rw-r--r--   0 jackson    (501) staff       (20)       88 2023-02-24 10:57:22.000000 synadm-0.41.1/doc/source/synadm.cli.root.rst
--rw-r--r--   0 jackson    (501) staff       (20)       81 2023-02-24 10:57:22.000000 synadm-0.41.1/doc/source/synadm.cli.user.rst
--rw-r--r--   0 jackson    (501) staff       (20)      948 2023-02-24 10:57:22.000000 synadm-0.41.1/doc/source/synadm.module.cli.rst
--rw-r--r--   0 jackson    (501) staff       (20)      427 2023-02-24 10:57:22.000000 synadm-0.41.1/doc/source/synadm.module.rst
--rwxr-xr-x   0 jackson    (501) staff       (20)      428 2023-03-25 17:08:27.000000 synadm-0.41.1/pypi.sh
--rw-r--r--   0 jackson    (501) staff       (20)       67 2023-02-24 10:57:22.000000 synadm-0.41.1/requirements.txt
--rwxr-xr-x   0 jackson    (501) staff       (20)      536 2023-02-24 10:57:22.000000 synadm-0.41.1/retag.sh
--rw-r--r--   0 jackson    (501) staff       (20)       38 2023-03-25 17:24:03.987129 synadm-0.41.1/setup.cfg
--rwxr-xr-x   0 jackson    (501) staff       (20)     2247 2023-03-25 16:56:01.000000 synadm-0.41.1/setup.py
--rw-r--r--   0 jackson    (501) staff       (20)       60 2023-02-24 10:57:22.000000 synadm-0.41.1/sphinx_requirements.txt
-drwxr-xr-x   0 jackson    (501) staff       (20)        0 2023-03-25 17:24:03.983073 synadm-0.41.1/synadm/
--rw-r--r--   0 jackson    (501) staff       (20)        0 2023-02-24 10:57:22.000000 synadm-0.41.1/synadm/__init__.py
--rw-r--r--   0 jackson    (501) staff       (20)    51147 2023-03-25 16:54:14.000000 synadm-0.41.1/synadm/api.py
-drwxr-xr-x   0 jackson    (501) staff       (20)        0 2023-03-25 17:24:03.986309 synadm-0.41.1/synadm/cli/
--rw-r--r--   0 jackson    (501) staff       (20)    20407 2023-03-25 16:54:14.000000 synadm-0.41.1/synadm/cli/__init__.py
--rw-r--r--   0 jackson    (501) staff       (20)     1458 2023-03-25 16:54:14.000000 synadm-0.41.1/synadm/cli/group.py
--rw-r--r--   0 jackson    (501) staff       (20)     4917 2023-03-25 16:54:14.000000 synadm-0.41.1/synadm/cli/history.py
--rw-r--r--   0 jackson    (501) staff       (20)     5328 2023-03-25 16:54:14.000000 synadm-0.41.1/synadm/cli/matrix.py
--rw-r--r--   0 jackson    (501) staff       (20)    10313 2023-03-25 16:54:14.000000 synadm-0.41.1/synadm/cli/media.py
--rw-r--r--   0 jackson    (501) staff       (20)     5832 2023-03-25 16:54:14.000000 synadm-0.41.1/synadm/cli/notice.py
--rw-r--r--   0 jackson    (501) staff       (20)     5438 2023-03-25 16:54:14.000000 synadm-0.41.1/synadm/cli/regtok.py
--rw-r--r--   0 jackson    (501) staff       (20)    12704 2023-03-25 16:54:14.000000 synadm-0.41.1/synadm/cli/room.py
--rw-r--r--   0 jackson    (501) staff       (20)    28397 2023-03-25 16:54:14.000000 synadm-0.41.1/synadm/cli/user.py
-drwxr-xr-x   0 jackson    (501) staff       (20)        0 2023-03-25 17:24:03.984507 synadm-0.41.1/synadm.egg-info/
--rw-r--r--   0 jackson    (501) staff       (20)    14558 2023-03-25 17:24:03.000000 synadm-0.41.1/synadm.egg-info/PKG-INFO
--rw-r--r--   0 jackson    (501) staff       (20)     1078 2023-03-25 17:24:03.000000 synadm-0.41.1/synadm.egg-info/SOURCES.txt
--rw-r--r--   0 jackson    (501) staff       (20)        1 2023-03-25 17:24:03.000000 synadm-0.41.1/synadm.egg-info/dependency_links.txt
--rw-r--r--   0 jackson    (501) staff       (20)       43 2023-03-25 17:24:03.000000 synadm-0.41.1/synadm.egg-info/entry_points.txt
--rw-r--r--   0 jackson    (501) staff       (20)       77 2023-03-25 17:24:03.000000 synadm-0.41.1/synadm.egg-info/requires.txt
--rw-r--r--   0 jackson    (501) staff       (20)        7 2023-03-25 17:24:03.000000 synadm-0.41.1/synadm.egg-info/top_level.txt
+drwxr-xr-x   0 jackson    (501) staff       (20)        0 2023-04-06 17:28:00.623012 synadm-0.41.2/
+-rw-r--r--   0 jackson    (501) staff       (20)      245 2023-04-06 17:26:21.000000 synadm-0.41.2/.bumpversion.cfg
+drwxr-xr-x   0 jackson    (501) staff       (20)        0 2023-04-06 17:28:00.612621 synadm-0.41.2/.github/
+drwxr-xr-x   0 jackson    (501) staff       (20)        0 2023-04-06 17:28:00.616376 synadm-0.41.2/.github/workflows/
+-rw-r--r--   0 jackson    (501) staff       (20)      435 2023-03-15 12:29:09.000000 synadm-0.41.2/.github/workflows/lint.yaml
+-rw-r--r--   0 jackson    (501) staff       (20)     2735 2023-03-28 18:08:19.000000 synadm-0.41.2/.github/workflows/release.yaml
+-rw-r--r--   0 jackson    (501) staff       (20)       96 2023-03-28 18:08:19.000000 synadm-0.41.2/.gitignore
+-rw-r--r--   0 jackson    (501) staff       (20)    35148 2023-02-24 10:57:22.000000 synadm-0.41.2/LICENSE
+-rw-r--r--   0 jackson    (501) staff       (20)      646 2023-02-24 10:57:22.000000 synadm-0.41.2/Makefile
+-rw-r--r--   0 jackson    (501) staff       (20)    14558 2023-04-06 17:28:00.622836 synadm-0.41.2/PKG-INFO
+-rw-r--r--   0 jackson    (501) staff       (20)    13504 2023-03-28 18:08:19.000000 synadm-0.41.2/README.md
+-rwxr-xr-x   0 jackson    (501) staff       (20)      814 2023-02-24 10:57:22.000000 synadm-0.41.2/bump.sh
+drwxr-xr-x   0 jackson    (501) staff       (20)        0 2023-04-06 17:28:00.612749 synadm-0.41.2/doc/
+drwxr-xr-x   0 jackson    (501) staff       (20)        0 2023-04-06 17:28:00.619104 synadm-0.41.2/doc/source/
+-rw-r--r--   0 jackson    (501) staff       (20)     2554 2023-04-06 17:26:21.000000 synadm-0.41.2/doc/source/conf.py
+-rw-r--r--   0 jackson    (501) staff       (20)      486 2023-03-25 16:54:14.000000 synadm-0.41.2/doc/source/index.rst
+-rw-r--r--   0 jackson    (501) staff       (20)      303 2023-03-15 12:29:09.000000 synadm-0.41.2/doc/source/index_cli_reference.rst
+-rw-r--r--   0 jackson    (501) staff       (20)      149 2023-02-24 10:57:22.000000 synadm-0.41.2/doc/source/index_modules.rst
+-rw-r--r--   0 jackson    (501) staff       (20)      110 2023-02-24 10:57:22.000000 synadm-0.41.2/doc/source/synadm.cli.config.rst
+-rw-r--r--   0 jackson    (501) staff       (20)       86 2023-02-24 10:57:22.000000 synadm-0.41.2/doc/source/synadm.cli.group.rst
+-rw-r--r--   0 jackson    (501) staff       (20)       96 2023-02-24 10:57:22.000000 synadm-0.41.2/doc/source/synadm.cli.history.rst
+-rw-r--r--   0 jackson    (501) staff       (20)       92 2023-02-24 10:57:22.000000 synadm-0.41.2/doc/source/synadm.cli.matrix.rst
+-rw-r--r--   0 jackson    (501) staff       (20)       86 2023-02-24 10:57:22.000000 synadm-0.41.2/doc/source/synadm.cli.media.rst
+-rw-r--r--   0 jackson    (501) staff       (20)       92 2023-03-15 12:29:09.000000 synadm-0.41.2/doc/source/synadm.cli.notice.rst
+-rw-r--r--   0 jackson    (501) staff       (20)       92 2023-02-24 10:57:22.000000 synadm-0.41.2/doc/source/synadm.cli.regtok.rst
+-rw-r--r--   0 jackson    (501) staff       (20)       81 2023-02-24 10:57:22.000000 synadm-0.41.2/doc/source/synadm.cli.room.rst
+-rw-r--r--   0 jackson    (501) staff       (20)       88 2023-02-24 10:57:22.000000 synadm-0.41.2/doc/source/synadm.cli.root.rst
+-rw-r--r--   0 jackson    (501) staff       (20)       81 2023-02-24 10:57:22.000000 synadm-0.41.2/doc/source/synadm.cli.user.rst
+-rw-r--r--   0 jackson    (501) staff       (20)      948 2023-02-24 10:57:22.000000 synadm-0.41.2/doc/source/synadm.module.cli.rst
+-rw-r--r--   0 jackson    (501) staff       (20)      427 2023-02-24 10:57:22.000000 synadm-0.41.2/doc/source/synadm.module.rst
+-rwxr-xr-x   0 jackson    (501) staff       (20)      424 2023-04-06 17:26:21.000000 synadm-0.41.2/pypi.sh
+-rw-r--r--   0 jackson    (501) staff       (20)       67 2023-02-24 10:57:22.000000 synadm-0.41.2/requirements.txt
+-rwxr-xr-x   0 jackson    (501) staff       (20)      536 2023-02-24 10:57:22.000000 synadm-0.41.2/retag.sh
+-rw-r--r--   0 jackson    (501) staff       (20)       38 2023-04-06 17:28:00.623052 synadm-0.41.2/setup.cfg
+-rwxr-xr-x   0 jackson    (501) staff       (20)     2247 2023-04-06 17:26:21.000000 synadm-0.41.2/setup.py
+-rw-r--r--   0 jackson    (501) staff       (20)       60 2023-02-24 10:57:22.000000 synadm-0.41.2/sphinx_requirements.txt
+drwxr-xr-x   0 jackson    (501) staff       (20)        0 2023-04-06 17:28:00.619338 synadm-0.41.2/synadm/
+-rw-r--r--   0 jackson    (501) staff       (20)        0 2023-02-24 10:57:22.000000 synadm-0.41.2/synadm/__init__.py
+-rw-r--r--   0 jackson    (501) staff       (20)    53122 2023-04-06 17:26:21.000000 synadm-0.41.2/synadm/api.py
+drwxr-xr-x   0 jackson    (501) staff       (20)        0 2023-04-06 17:28:00.622591 synadm-0.41.2/synadm/cli/
+-rw-r--r--   0 jackson    (501) staff       (20)    20407 2023-03-28 18:08:19.000000 synadm-0.41.2/synadm/cli/__init__.py
+-rw-r--r--   0 jackson    (501) staff       (20)     1458 2023-03-28 18:08:19.000000 synadm-0.41.2/synadm/cli/group.py
+-rw-r--r--   0 jackson    (501) staff       (20)     4917 2023-03-28 18:08:19.000000 synadm-0.41.2/synadm/cli/history.py
+-rw-r--r--   0 jackson    (501) staff       (20)     5328 2023-03-28 18:08:19.000000 synadm-0.41.2/synadm/cli/matrix.py
+-rw-r--r--   0 jackson    (501) staff       (20)    10313 2023-03-25 16:54:14.000000 synadm-0.41.2/synadm/cli/media.py
+-rw-r--r--   0 jackson    (501) staff       (20)     5832 2023-03-28 18:08:19.000000 synadm-0.41.2/synadm/cli/notice.py
+-rw-r--r--   0 jackson    (501) staff       (20)     5438 2023-03-25 16:54:14.000000 synadm-0.41.2/synadm/cli/regtok.py
+-rw-r--r--   0 jackson    (501) staff       (20)    12704 2023-03-28 18:08:19.000000 synadm-0.41.2/synadm/cli/room.py
+-rw-r--r--   0 jackson    (501) staff       (20)    28397 2023-03-28 18:08:19.000000 synadm-0.41.2/synadm/cli/user.py
+drwxr-xr-x   0 jackson    (501) staff       (20)        0 2023-04-06 17:28:00.620609 synadm-0.41.2/synadm.egg-info/
+-rw-r--r--   0 jackson    (501) staff       (20)    14558 2023-04-06 17:28:00.000000 synadm-0.41.2/synadm.egg-info/PKG-INFO
+-rw-r--r--   0 jackson    (501) staff       (20)     1078 2023-04-06 17:28:00.000000 synadm-0.41.2/synadm.egg-info/SOURCES.txt
+-rw-r--r--   0 jackson    (501) staff       (20)        1 2023-04-06 17:28:00.000000 synadm-0.41.2/synadm.egg-info/dependency_links.txt
+-rw-r--r--   0 jackson    (501) staff       (20)       43 2023-04-06 17:28:00.000000 synadm-0.41.2/synadm.egg-info/entry_points.txt
+-rw-r--r--   0 jackson    (501) staff       (20)       77 2023-04-06 17:28:00.000000 synadm-0.41.2/synadm.egg-info/requires.txt
+-rw-r--r--   0 jackson    (501) staff       (20)        7 2023-04-06 17:28:00.000000 synadm-0.41.2/synadm.egg-info/top_level.txt
```

### Comparing `synadm-0.41.1/.github/workflows/release.yaml` & `synadm-0.41.2/.github/workflows/release.yaml`

 * *Files 0% similar despite different names*

```diff
@@ -86,11 +86,11 @@
         body: |
           This is an autogenerated ${{ github.repository }} release.
           Release notes coming soon...
           ## Improved / Changed
           ## New
           ## Fixed
           ## Notes
-        draft: false
+        draft: true
         prerelease: false
       if: ${{ steps.check.outputs.release_existing == 'false' }}
```

### Comparing `synadm-0.41.1/LICENSE` & `synadm-0.41.2/LICENSE`

 * *Files identical despite different names*

### Comparing `synadm-0.41.1/Makefile` & `synadm-0.41.2/Makefile`

 * *Files identical despite different names*

### Comparing `synadm-0.41.1/PKG-INFO` & `synadm-0.41.2/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: synadm
-Version: 0.41.1
+Version: 0.41.2
 Summary: Command line admin tool for Synapse (Matrix reference homeserver)
 Home-page: https://github.com/joj0/synadm
 Author: Johannes Tiefenbacher
 Author-email: jt@peek-a-boo.at
 License: GPLv3+
 Project-URL: Bug Tracker, https://github.com/joj0/synadm/issues
 Project-URL: Documentation, https://github.com/joj0/synadm
```

### Comparing `synadm-0.41.1/README.md` & `synadm-0.41.2/README.md`

 * *Files identical despite different names*

### Comparing `synadm-0.41.1/bump.sh` & `synadm-0.41.2/bump.sh`

 * *Files identical despite different names*

### Comparing `synadm-0.41.1/doc/source/conf.py` & `synadm-0.41.2/doc/source/conf.py`

 * *Files 5% similar despite different names*

```diff
@@ -18,18 +18,18 @@
 # -- Project information -----------------------------------------------------
 
 project = 'synadm'
 copyright = '2020-2023, Johannes Tiefenbacher'
 author = 'Johannes Tiefenbacher'
 
 # The short X.Y version
-version = '0.41.1'
+version = '0.41.2'
 
 # The full version, including alpha/beta/rc tags
-release = '0.41.1'
+release = '0.41.2'
 
 
 # -- General configuration ---------------------------------------------------
 
 # Add any Sphinx extension module names here, as strings. They can be
 # extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
 # ones.
```

### Comparing `synadm-0.41.1/doc/source/synadm.module.cli.rst` & `synadm-0.41.2/doc/source/synadm.module.cli.rst`

 * *Files identical despite different names*

### Comparing `synadm-0.41.1/retag.sh` & `synadm-0.41.2/retag.sh`

 * *Files identical despite different names*

### Comparing `synadm-0.41.1/setup.py` & `synadm-0.41.2/setup.py`

 * *Files 5% similar despite different names*

```diff
@@ -17,15 +17,15 @@
 
 from setuptools import setup, find_packages
 with open('README.md') as f:
     long_description = f.read()
 
 setup(
     name="synadm",
-    version="0.41.1",
+    version="0.41.2",
     author="Johannes Tiefenbacher",
     author_email="jt@peek-a-boo.at",
     description="Command line admin tool for Synapse (Matrix reference homeserver)",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/joj0/synadm",
     project_urls={
```

### Comparing `synadm-0.41.1/synadm/api.py` & `synadm-0.41.2/synadm/api.py`

 * *Files 4% similar despite different names*

```diff
@@ -70,39 +70,53 @@
         }
         self.timeout = timeout
         if debug:
             HTTPConnection.debuglevel = 1
         self.verify = verify
 
     def query(self, method, urlpart, params=None, data=None, token=None,
-              base_url_override=None, verify=None):
+              base_url_override=None, verify=None, *args, **kwargs):
         """Generic wrapper around requests methods.
 
-        Handles requests methods, logging and exceptions.
+        Handles requests methods, logging and exceptions, and URL encoding.
 
         Args:
             urlpart (string): The path to the API endpoint, excluding
                 self.base_url and self.path (the part after
-                proto://fqdn:port/path).
+                proto://fqdn:port/path). It will be passed to Python's
+                str.format, so the string should not be already formatted
+                (as f-strings or with str.format) as to sanitize the URL.
             params (dict, optional): URL parameters (?param1&paarm2).  Defaults
                 to None.
             data (dict, optional): Request body used in POST, PUT, DELETE
                 requests.  Defaults to None.
             base_url_override (bool): The default setting of self.base_url set
                 on initialization can be overwritten using this argument.
             verify(bool): Mandatory SSL verification is turned on by default
                 and can be turned off using this method.
+            *args: Arguments that will be URL encoded and passed to Python's
+                str.format.
+            **kwargs: Keyword arguments that will be URL encoded (only the
+                values) and passed to Python's str.format.
 
         Returns:
             string or None: Usually a JSON string containing
                 the response of the API; responses that are not 200(OK) (usally
                 error messages returned by the API) will also be returned as
                 JSON strings. On exceptions the error type and description are
                 logged and None is returned.
         """
+        args = list(args)
+        kwargs = dict(kwargs)
+        for i in range(len(args)):
+            args[i] = urllib.parse.quote(args[i], safe="")
+        for i in kwargs.keys():
+            kwargs[i] = urllib.parse.quote(kwargs[i], safe="")
+        urlpart = urlpart.format(*args, **kwargs)
+
         if base_url_override:
             self.log.debug("base_url override!")
             url = f"{base_url_override}/{self.path}/{urlpart}"
             host_descr = urllib.parse.urlparse(base_url_override).netloc
         else:
             url = f"{self.base_url}/{self.path}/{urlpart}"
             host_descr = "Synapse"
@@ -305,15 +319,16 @@
 
         Returns:
             string, dict or None: A dict containing the room ID for the alias.
                 If room_id is missing in the response we return the whole
                 response as it might contain Synapse's error message.
         """
         room_directory = self.query(
-            "get", f"client/r0/directory/room/{urllib.parse.quote(room_alias)}"
+            "get", "client/r0/directory/room/{room_alias}",
+            room_alias=room_alias
         )
         if "room_id" in room_directory:
             return room_directory["room_id"]
         else:
             return room_directory  # might contain useful error message
 
     def room_get_aliases(self, room_id):
@@ -323,15 +338,16 @@
             room_id (string): A Matrix room ID (!abc123:example.org)
 
         Returns:
             dict or None: A dict containing a list of room aliases, Synapse's
                 error message or None on exceptions.
         """
         return self.query(
-            "get", f"client/r0/rooms/{urllib.parse.quote(room_id)}/aliases"
+            "get", "client/r0/rooms/{room_id}/aliases",
+            room_id=room_id
         )
 
     def raw_request(self, endpoint, method, data, token=None):
         data_dict = {}
         if method != "get":
             self.log.debug("The data we are trying to parse and submit:")
             self.log.debug(data)
@@ -462,15 +478,16 @@
                 passes as we need some Matrix API functionality here.
 
         Returns:
             string: JSON string containing the admin API's response or None if
                 an exception occured. See Synapse admin API docs for details.
         """
 
-        rooms = self.query("get", f"v1/users/{user_id}/joined_rooms")
+        rooms = self.query("get", "v1/users/{user_id}/joined_rooms",
+                           user_id=user_id)
         # Translate room ID's into aliases if requested.
         if return_aliases and rooms is not None and "joined_rooms" in rooms:
             for i, room_id in enumerate(rooms["joined_rooms"]):
                 aliases = matrix_api.room_get_aliases(room_id)
                 if aliases["aliases"] != []:
                     rooms["joined_rooms"][i] = " ".join(aliases["aliases"])
         return rooms
@@ -483,17 +500,17 @@
             gdpr_erase (bool): enable/disable gdpr-erasing the user, see
                 Synapse admin API docs for details.
 
         Returns:
             string: JSON string containing the admin API's response or None if
                 an exception occured. See Synapse admin API docs for details.
         """
-        return self.query("post", f"v1/deactivate/{user_id}", data={
+        return self.query("post", "v1/deactivate/{user_id}", data={
             "erase": gdpr_erase
-        })
+        }, user_id=user_id)
 
     def user_password(self, user_id, password, no_logout):
         """Set the user password, and log the user out if requested
 
         Args:
             user_id (string): fully qualified Matrix user ID
             password (string): new password that should be set
@@ -504,15 +521,16 @@
         Returns:
             string: JSON string containing the admin API's response or None if
             an exception occured. See Synapse admin API docs for details.
         """
         data = {"new_password": password}
         if no_logout:
             data.update({"logout_devices": False})
-        return self.query("post", f"v1/reset_password/{user_id}", data=data)
+        return self.query("post", "v1/reset_password/{user_id}", data=data,
+                          user_id=user_id)
 
     def user_details(self, user_id):
         """Get information about a given user
 
         Note that the admin API docs describe this function as "Query User
         Account".
 
@@ -520,15 +538,15 @@
             user_id (string): fully qualified Matrix user ID
 
         Returns:
             string: JSON string containing the admin API's response or None if
                 an exception occured. See Synapse admin API docs for details.
 
         """
-        return self.query("get", f"v2/users/{user_id}")
+        return self.query("get", "v2/users/{user_id}", user_id=user_id)
 
     def user_login(self, user_id, expire_days, expire, _expire_ts):
         """Get an access token that can be used to authenticate as that user.
 
         If one of the args expire_days, expire or _expire_ts is set, the
         valid_until_ms field will be sent to the API endpoint. If this is not
         the case the default of the API would be used. At the time of writing,
@@ -569,15 +587,16 @@
             self.log.info("Token expiry date set to timestamp: %d,",
                           expire_ts)
             self.log.info("which is the date/time: %s",
                           self._datetime_from_timestamp(expire_ts))
         else:
             self.log.info("Token will never expire.")
 
-        return self.query("post", f"v1/users/{user_id}/login", data=data)
+        return self.query("post", "v1/users/{user_id}/login", data=data,
+                          user_id=user_id)
 
     def user_modify(self, user_id, password, display_name, threepid,
                     avatar_url, admin, deactivation, user_type):
         """ Create or update information about a given user
 
         Threepid should be passed as a tuple in a tuple
         """
@@ -597,32 +616,34 @@
         if deactivation == "deactivate":
             data.update({"deactivated": True})
         if deactivation == "activate":
             data.update({"deactivated": False})
         if user_type:
             data.update({"user_type": None if user_type == 'null' else
                          user_type})
-        return self.query("put", f"v2/users/{user_id}", data=data)
+        return self.query("put", "v2/users/{user_id}", data=data,
+                          user_id=user_id)
 
     def user_whois(self, user_id):
         """ Return information about the active sessions for a specific user
         """
-        return self.query("get", f"v1/whois/{user_id}")
+        return self.query("get", "v1/whois/{user_id}", user_id=user_id)
 
     def user_devices(self, user_id):
         """ Return information about all devices for a specific user.
 
         Args:
             user_id (string): Fully qualified Matrix user ID.
 
         Returns:
             string: JSON string containing the admin API's response or None if
                 an exception occured. See Synapse admin API docs for details.
         """
-        return self.query("get", f"v2/users/{user_id}/devices")
+        return self.query("get", "v2/users/{user_id}/devices",
+                          user_id=user_id)
 
     def user_devices_get_todelete(self, devices_data, min_days, min_surviving,
                                   device_id, readable_seen):
         """ Gather a list of devices that possibly could be deleted.
 
         This method is used by the 'user prune-devices' command.
 
@@ -701,36 +722,39 @@
 
     def user_devices_delete(self, user_id, devices):
         """ Delete the specified devices for a specific user.
         Returns an empty JSON dict.
 
         devices is a list of device IDs
         """
-        return self.query("post", f"v2/users/{user_id}/delete_devices",
-                          data={"devices": devices})
+        return self.query("post", "v2/users/{user_id}/delete_devices",
+                          data={"devices": devices}, user_id=user_id)
 
     def user_auth_provider_search(self, provider, external_id):
         """ Finds a user based on their ID (external id) in auth provider
         represented by auth provider id (provider).
         """
         return self.query("get",
-                          f"v1/auth_providers/{provider}/users/{external_id}")
+                          "v1/auth_providers/{provider}/users/{external_id}",
+                          provider=provider, external_id=external_id)
 
     def user_3pid_search(self, medium, address):
         """ Finds a user based on their Third Party ID by specifying what kind
         of 3PID it is as medium.
         """
-        return self.query("get", f"v1/threepid/{medium}/users/{address}")
+        return self.query("get", "v1/threepid/{medium}/users/{address}",
+                          address=address)
 
     def room_join(self, room_id_or_alias, user_id):
         """ Allow an administrator to join an user account with a given user_id
         to a room with a given room_id_or_alias
         """
         data = {"user_id": user_id}
-        return self.query("post", f"v1/join/{room_id_or_alias}", data=data)
+        return self.query("post", "v1/join/{room_id_or_alias}", data=data,
+                          room_id_or_alias=room_id_or_alias)
 
     def room_list(self, _from, limit, name, order_by, reverse):
         """ List and search rooms
         """
         return self.query("get", "v1/rooms", params={
             "from": _from,
             "limit": limit,
@@ -738,32 +762,32 @@
             "order_by": order_by,
             "dir": "b" if reverse else None
         })
 
     def room_details(self, room_id):
         """ Get details about a room
         """
-        return self.query("get", f"v1/rooms/{room_id}")
+        return self.query("get", "v1/rooms/{room_id}", room_id=room_id)
 
     def room_members(self, room_id):
         """ Get a list of room members
         """
-        return self.query("get", f"v1/rooms/{room_id}/members")
+        return self.query("get", "v1/rooms/{room_id}/members", room_id=room_id)
 
     def room_state(self, room_id):
         """ Get a list of all state events in a room.
 
         Args:
             room_id (string)
 
         Returns:
             string: JSON string containing the admin API's response or None if
                 an exception occured. See Synapse admin API docs for details.
         """
-        return self.query("get", f"v1/rooms/{room_id}/state")
+        return self.query("get", "v1/rooms/{room_id}/state", room_id=room_id)
 
     def room_power_levels(self, from_, limit, name, order_by, reverse,
                           room_id=None, all_details=True,
                           output_format="json"):
         """ Get a list of configured power_levels in all rooms.
 
         or a single room.
@@ -822,15 +846,16 @@
         # everything else is optional and shouldn't even exist in post body
         if new_room_user_id:
             data.update({"new_room_user_id": new_room_user_id})
         if room_name:
             data.update({"room_name": room_name})
         if message:
             data.update({"message": message})
-        return self.query("delete", f"v1/rooms/{room_id}", data=data)
+        return self.query("delete", "v1/rooms/{room_id}", data=data,
+                          room_id=room_id)
 
     def block_room(self, room_id, block):
         """ Block or unblock a room.
 
         Args:
             room_id (string): Required.
             block (boolean): Whether to block or unblock a room.
@@ -839,81 +864,86 @@
             string: JSON string containing the admin API's response or None if
                 an exception occurred. See Synapse admin API docs for details.
         """
         # TODO prevent usage on versions before 1.48
         data = {
             "block": block
         }
-        return self.query("put", f"v1/rooms/{room_id}/block", data=data)
+        return self.query("put", "v1/rooms/{room_id}/block", data=data,
+                          room_id=room_id)
 
     def room_block_status(self, room_id):
         """ Returns if the room is blocked or not, and who blocked it.
 
         Args:
             room_id (string): Fully qualified Matrix room ID.
 
         Returns:
             string: JSON string containing the admin API's response or None if
                 an exception occured. See Synapse admin API docs for details.
         """
         # TODO prevent usage on versions before 1.48
-        return self.query("get", f"v1/rooms/{room_id}/block")
+        return self.query("get", "v1/rooms/{room_id}/block", room_id=room_id)
 
     def room_make_admin(self, room_id, user_id):
         """ Grant a user room admin permission. If the user is not in the room,
         and it is not publicly joinable, then invite the user.
         """
         data = {}
         if user_id:
             data.update({"user_id": user_id})
-        return self.query("post", f"v1/rooms/{room_id}/make_room_admin",
-                          data=data)
+        return self.query("post", "v1/rooms/{room_id}/make_room_admin",
+                          data=data, room_id=room_id)
 
     def room_media_list(self, room_id):
         """ Get a list of known media in an (unencrypted) room.
         """
-        return self.query("get", f"v1/room/{room_id}/media")
+        return self.query("get", "v1/room/{room_id}/media", room_id=room_id)
 
     def media_quarantine(self, server_name, media_id):
         """ Quarantine a single piece of local or remote media
         """
         return self.query(
-            "post", f"v1/media/quarantine/{server_name}/{media_id}", data={}
+            "post", "v1/media/quarantine/{server_name}/{media_id}", data={},
+            server_name=server_name, media_id=media_id
         )
 
     def media_unquarantine(self, server_name, media_id):
         """ Removes a single piece of local or remote media from quarantine.
         """
         return self.query(
-            "post", f"v1/media/unquarantine/{server_name}/{media_id}", data={}
+            "post", "v1/media/unquarantine/{server_name}/{media_id}", data={},
+            server_name=server_name, media_id=media_id
         )
 
     def room_media_quarantine(self, room_id):
         """ Quarantine all local and remote media in a room
         """
         return self.query(
-            "post", f"v1/room/{room_id}/media/quarantine", data={}
+            "post", "v1/room/{room_id}/media/quarantine", data={},
+            room_id=room_id
         )
 
     def user_media_quarantine(self, user_id):
         """ Quarantine all local and remote media of a user
         """
         return self.query(
-            "post", f"v1/user/{user_id}/media/quarantine", data={}
+            "post", "v1/user/{user_id}/media/quarantine", data={},
+            user_id=user_id
         )
 
     def user_media(self, user_id, _from, limit, order_by, reverse, readable):
         """ Get a user's uploaded media
         """
-        result = self.query("get", f"v1/users/{user_id}/media", params={
+        result = self.query("get", "v1/users/{user_id}/media", params={
             "from": _from,
             "limit": limit,
             "order_by": order_by,
             "dir": "b" if reverse else None
-        })
+        }, user_id=user_id)
         if (readable and result is not None and "media" in result):
             for i, media in enumerate(result["media"]):
                 created = media["created_ts"]
                 last_access = media["last_access_ts"]
                 if created is not None:
                     result["media"][i][
                         "created_ts"
@@ -924,15 +954,16 @@
                     ] = self._datetime_from_timestamp(last_access, as_str=True)
         return result
 
     def media_delete(self, server_name, media_id):
         """ Delete a specific (local) media_id
         """
         return self.query(
-            "delete", f"v1/media/{server_name}/{media_id}", data={}
+            "delete", "v1/media/{server_name}/{media_id}", data={},
+            server_name=server_name, media_id=media_id
         )
 
     def media_delete_by_date_or_size(self, server_name, before_days, before,
                                      _before_ts, _size_gt, delete_profiles):
         """ Delete local media by date and/or size FIXME and/or?
         """
         if before_days:
@@ -967,24 +998,25 @@
                 "size_gt": size_gt
             })
         if delete_profiles:
             params.update({
                 "keep_profiles": "false"
             })
         return self.query(
-            "post", f"v1/media/{server_name}/delete", data={}, params=params
+            "post", "v1/media/{server_name}/delete", data={}, params=params,
+            server_name=server_name
         )
 
     def media_protect(self, media_id):
         """ Protect a single piece of local or remote media
 
         from being quarantined
         """
         return self.query(
-            "post", f"v1/media/protect/{media_id}", data={}
+            "post", "v1/media/protect/{media_id}", data={}, media_id=media_id
         )
 
     def purge_media_cache(self, before_days, before, _before_ts):
         """ Purge old cached remote media
         """
         if before_days:
             self.log.debug("Received --before-days: %s", before_days)
@@ -1012,15 +1044,16 @@
         """ Get the server version
         """
         return self.query("get", "v1/server_version")
 
     def group_delete(self, group_id):
         """ Delete a local group (community)
         """
-        return self.query("post", f"v1/delete_group/{group_id}")
+        return self.query("post", "v1/delete_group/{group_id}",
+                          group_id=group_id)
 
     def purge_history(self, room_id, before_event_id, before_days, before,
                       _before_ts, delete_local):
         """ Purge room history
         """
         before_ts = None
         if before_days:
@@ -1052,22 +1085,24 @@
             })
 
         if delete_local:
             data.update({
                 "delete_local_events": True,
             })
 
-        return self.query("post", f"v1/purge_history/{room_id}", data=data)
+        return self.query("post", "v1/purge_history/{room_id}", data=data,
+                          room_id=room_id)
 
     def purge_history_status(self, purge_id):
         """ Get status of a recent history purge
 
         The status will be one of active, complete, or failed.
         """
-        return self.query("get", f"v1/purge_history_status/{purge_id}")
+        return self.query("get", "v1/purge_history_status/{purge_id}",
+                          purge_id=purge_id)
 
     def regtok_list(self, valid, readable_expiry):
         """ List registration tokens
 
         Args:
             valid (bool): List only valid (if True) or invalid (if False)
                 tokens. Default is to list all tokens regardless of validity.
@@ -1109,15 +1144,16 @@
                 timestamp.
 
         Returns:
             string: JSON string containing the admin API's response or None if
                 an exception occured. See Synapse admin API docs for details.
 
         """
-        result = self.query("get", f"v1/registration_tokens/{token}")
+        result = self.query("get", "v1/registration_tokens/{token}",
+                            token=token)
 
         # Change expiry_time to a human readable format if requested
         if (
             readable_expiry
             and result is not None
             and result.get("expiry_time") is not None
         ):
@@ -1204,41 +1240,44 @@
                 data["expiry_time"] = None
             else:
                 data["expiry_time"] = expiry_ts
         elif expire_at:
             self.log.debug(f"Received --expire-at: {expire_at}")
             data["expiry_time"] = self._timestamp_from_datetime(expire_at)
 
-        return self.query("put", f"v1/registration_tokens/{token}", data=data)
+        return self.query("put", "v1/registration_tokens/{token}", data=data,
+                          token=token)
 
     def regtok_delete(self, token):
         """ Delete a registration token
 
         Args:
             token (string): The registration token to delete
 
         Returns:
             string: JSON string containing the admin API's response or None if
                 an exception occured. See Synapse admin API docs for details.
 
         """
-        return self.query("delete", f"v1/registration_tokens/{token}")
+        return self.query("delete", "v1/registration_tokens/{token}",
+                          token=token)
 
     def user_shadow_ban(self, user_id, unban):
         """ Shadow-ban or unban a user.
 
         Args:
             user_id (string): The user to be banned/unbanned.
             unban (boolean): Unban the specified user.
         """
         if unban:
             method = "delete"
         else:
             method = "post"
-        return self.query(method, f"v1/users/{user_id}/shadow_ban")
+        return self.query(method, "v1/users/{user_id}/shadow_ban",
+                          user_id=user_id)
 
     def notice_send(self, receivers, content_plain, content_html, paginate,
                     regex):
         """ Send server notices.
 
         Args:
             receivers (string): Target(s) of the notice. Either localpart or
```

### Comparing `synadm-0.41.1/synadm/cli/__init__.py` & `synadm-0.41.2/synadm/cli/__init__.py`

 * *Files identical despite different names*

### Comparing `synadm-0.41.1/synadm/cli/group.py` & `synadm-0.41.2/synadm/cli/group.py`

 * *Files identical despite different names*

### Comparing `synadm-0.41.1/synadm/cli/history.py` & `synadm-0.41.2/synadm/cli/history.py`

 * *Files identical despite different names*

### Comparing `synadm-0.41.1/synadm/cli/matrix.py` & `synadm-0.41.2/synadm/cli/matrix.py`

 * *Files identical despite different names*

### Comparing `synadm-0.41.1/synadm/cli/media.py` & `synadm-0.41.2/synadm/cli/media.py`

 * *Files identical despite different names*

### Comparing `synadm-0.41.1/synadm/cli/notice.py` & `synadm-0.41.2/synadm/cli/notice.py`

 * *Files identical despite different names*

### Comparing `synadm-0.41.1/synadm/cli/regtok.py` & `synadm-0.41.2/synadm/cli/regtok.py`

 * *Files identical despite different names*

### Comparing `synadm-0.41.1/synadm/cli/room.py` & `synadm-0.41.2/synadm/cli/room.py`

 * *Files identical despite different names*

### Comparing `synadm-0.41.1/synadm/cli/user.py` & `synadm-0.41.2/synadm/cli/user.py`

 * *Files identical despite different names*

### Comparing `synadm-0.41.1/synadm.egg-info/PKG-INFO` & `synadm-0.41.2/synadm.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: synadm
-Version: 0.41.1
+Version: 0.41.2
 Summary: Command line admin tool for Synapse (Matrix reference homeserver)
 Home-page: https://github.com/joj0/synadm
 Author: Johannes Tiefenbacher
 Author-email: jt@peek-a-boo.at
 License: GPLv3+
 Project-URL: Bug Tracker, https://github.com/joj0/synadm/issues
 Project-URL: Documentation, https://github.com/joj0/synadm
```

### Comparing `synadm-0.41.1/synadm.egg-info/SOURCES.txt` & `synadm-0.41.2/synadm.egg-info/SOURCES.txt`

 * *Files identical despite different names*

