# Comparing `tmp/linuxp-plugin-1.0.1.tar.gz` & `tmp/linuxp-plugin-1.0.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "linuxp-plugin-1.0.1.tar", last modified: Sun Mar 19 01:26:45 2023, max compression
+gzip compressed data, was "linuxp-plugin-1.0.2.tar", last modified: Fri Apr  7 03:09:08 2023, max compression
```

## Comparing `linuxp-plugin-1.0.1.tar` & `linuxp-plugin-1.0.2.tar`

### file list

```diff
@@ -1,18 +1,18 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-19 01:26:45.394290 linuxp-plugin-1.0.1/
--rw-r--r--   0 runner    (1001) docker     (123)     1070 2023-03-19 01:26:27.000000 linuxp-plugin-1.0.1/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)     2850 2023-03-19 01:26:45.394290 linuxp-plugin-1.0.1/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     2067 2023-03-19 01:26:27.000000 linuxp-plugin-1.0.1/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-19 01:26:45.394290 linuxp-plugin-1.0.1/linux_profile_plugin/
--rw-r--r--   0 runner    (1001) docker     (123)     1297 2023-03-19 01:26:27.000000 linuxp-plugin-1.0.1/linux_profile_plugin/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      804 2023-03-19 01:26:27.000000 linuxp-plugin-1.0.1/linux_profile_plugin/commands.py
--rw-r--r--   0 runner    (1001) docker     (123)     1341 2023-03-19 01:26:27.000000 linuxp-plugin-1.0.1/linux_profile_plugin/main.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-19 01:26:45.394290 linuxp-plugin-1.0.1/linuxp_plugin.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     2850 2023-03-19 01:26:45.000000 linuxp-plugin-1.0.1/linuxp_plugin.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      377 2023-03-19 01:26:45.000000 linuxp-plugin-1.0.1/linuxp_plugin.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-19 01:26:45.000000 linuxp-plugin-1.0.1/linuxp_plugin.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       65 2023-03-19 01:26:45.000000 linuxp-plugin-1.0.1/linuxp_plugin.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (123)       15 2023-03-19 01:26:45.000000 linuxp-plugin-1.0.1/linuxp_plugin.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       21 2023-03-19 01:26:45.000000 linuxp-plugin-1.0.1/linuxp_plugin.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-19 01:26:45.000000 linuxp-plugin-1.0.1/linuxp_plugin.egg-info/zip-safe
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-19 01:26:45.394290 linuxp-plugin-1.0.1/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1499 2023-03-19 01:26:27.000000 linuxp-plugin-1.0.1/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 03:09:08.158911 linuxp-plugin-1.0.2/
+-rw-r--r--   0 runner    (1001) docker     (123)     1070 2023-04-07 03:08:47.000000 linuxp-plugin-1.0.2/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)     2872 2023-04-07 03:09:08.158911 linuxp-plugin-1.0.2/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     2090 2023-04-07 03:08:47.000000 linuxp-plugin-1.0.2/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 03:09:08.158911 linuxp-plugin-1.0.2/linux_profile_plugin/
+-rw-r--r--   0 runner    (1001) docker     (123)     1296 2023-04-07 03:08:47.000000 linuxp-plugin-1.0.2/linux_profile_plugin/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      804 2023-04-07 03:08:47.000000 linuxp-plugin-1.0.2/linux_profile_plugin/commands.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1341 2023-04-07 03:08:47.000000 linuxp-plugin-1.0.2/linux_profile_plugin/main.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 03:09:08.158911 linuxp-plugin-1.0.2/linuxp_plugin.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     2872 2023-04-07 03:09:08.000000 linuxp-plugin-1.0.2/linuxp_plugin.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      377 2023-04-07 03:09:08.000000 linuxp-plugin-1.0.2/linuxp_plugin.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 03:09:08.000000 linuxp-plugin-1.0.2/linuxp_plugin.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       65 2023-04-07 03:09:08.000000 linuxp-plugin-1.0.2/linuxp_plugin.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       15 2023-04-07 03:09:08.000000 linuxp-plugin-1.0.2/linuxp_plugin.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       21 2023-04-07 03:09:08.000000 linuxp-plugin-1.0.2/linuxp_plugin.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 03:09:07.000000 linuxp-plugin-1.0.2/linuxp_plugin.egg-info/zip-safe
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-07 03:09:08.158911 linuxp-plugin-1.0.2/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1498 2023-04-07 03:08:47.000000 linuxp-plugin-1.0.2/setup.py
```

### Comparing `linuxp-plugin-1.0.1/LICENSE` & `linuxp-plugin-1.0.2/LICENSE`

 * *Files identical despite different names*

### Comparing `linuxp-plugin-1.0.1/PKG-INFO` & `linuxp-plugin-1.0.2/PKG-INFO`

 * *Files 17% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 Metadata-Version: 2.1
 Name: linuxp-plugin
-Version: 1.0.1
+Version: 1.0.2
 Summary: 🐧 Plugin Linux Profile
-Home-page: https://github.com/MyLinuxProfile/linux-profile-plugin
+Home-page: https://github.com/linux-profile/linux-profile-plugin
 Author: Fernando Celmer
 Author-email: email@fernandocelmer.com
 Classifier: Development Status :: 4 - Beta
 Classifier: Operating System :: OS Independent
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Intended Audience :: Developers
 Classifier: Natural Language :: English
@@ -15,28 +15,28 @@
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10
 Requires-Python: >=3.6
 Description-Content-Type: text/markdown
 License-File: LICENSE
 
-<img src="https://github.com/MyLinuxProfile/linux-profile-plugin/blob/master/docs/linuxp.png?raw=true">
+<img src="https://github.com/linux-profile/linux-profile-plugin/blob/master/docs/linuxp.png?raw=true">
 
-![GitHub Org's stars](https://img.shields.io/github/stars/MyLinuxProfile?label=LinuxProfile&style=flat-square)
-![GitHub last commit](https://img.shields.io/github/last-commit/MyLinuxProfile/linux-profile-plugin?style=flat-square)
+![GitHub Org's stars](https://img.shields.io/github/stars/linux-profile?label=LinuxProfile&style=flat-square)
+![GitHub last commit](https://img.shields.io/github/last-commit/linux-profile/linux-profile-plugin?style=flat-square)
 ![PyPI](https://img.shields.io/pypi/v/linuxp-plugin)
 
-[![check](https://github.com/MyLinuxProfile/linux-profile-plugin/actions/workflows/python-publish-pypi.yml/badge.svg)](https://github.com/MyLinuxProfile/linux-profile-plugin/actions/workflows/python-publish-pypi.yml)
-[![check](https://github.com/MyLinuxProfile/linux-profile-plugin/actions/workflows/python-publish-pypi-test.yml/badge.svg)](https://github.com/MyLinuxProfile/linux-profile-plugin/actions/workflows/python-publish-pypi-test.yml)
-[![check](https://github.com/MyLinuxProfile/linux-profile-plugin/actions/workflows/python-app-code.yml/badge.svg)](https://github.com/MyLinuxProfile/linux-profile-plugin/actions/workflows/python-app-code.yml)
+[![check](https://github.com/linux-profile/linux-profile-plugin/actions/workflows/python-publish-pypi.yml/badge.svg)](https://github.com/linux-profile/linux-profile-plugin/actions/workflows/python-publish-pypi.yml)
+[![check](https://github.com/linux-profile/linux-profile-plugin/actions/workflows/python-publish-pypi-test.yml/badge.svg)](https://github.com/linux-profile/linux-profile-plugin/actions/workflows/python-publish-pypi-test.yml)
+[![check](https://github.com/linux-profile/linux-profile-plugin/actions/workflows/python-app-code.yml/badge.svg)](https://github.com/linux-profile/linux-profile-plugin/actions/workflows/python-app-code.yml)
 
 ---
 
 - **Documentation**: [https://docs.linuxprofile.com](https://docs.linuxprofile.com)
-- **Source Code**: [https://github.com/MyLinuxProfile/linux-profile-plugin](https://github.com/MyLinuxProfile/linux-profile-plugin)
+- **Source Code**: [https://github.com/linux-profile/linux-profile-plugin](https://github.com/linux-profile/linux-profile-plugin)
 
 ---
 
 ## Installation
 
 - **Install - Pypi/PIP**
 
@@ -47,18 +47,21 @@
 | Command               | Description                                                                           | Docs      |
 |:--------------------- |:------------------------------------------------------------------------------------- | :-------: | 
 | ``linuxp_plugin hello``      | My custom command.                                                                    | [Link](#) |
 | ``linuxp_plugin explore``    | This command shows some settings.                                                     | [Link](#) |
 
 
 ## Commit Style
-- ⚙️ NO-TASK
+
+- ⚙️ FEATURE
 - 📝 PEP8
 - 📌 ISSUE
 - 🪲 BUG
 - 📘 DOCS
 - 📦 PyPI
 - ❤️️ TEST
+- ⬆️ CI/CD
+- ⚠️ SECURITY
 
 ## License
 
 This project is licensed under the terms of the MIT license.
```

### Comparing `linuxp-plugin-1.0.1/linux_profile_plugin/__init__.py` & `linuxp-plugin-1.0.2/linux_profile_plugin/__init__.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-__version__ = "1.0.1"
+__version__ = "1.0.2"
 
 __author__ = 'Fernando Celmer <email@fernandocelmer.com>'
 __copyright__ = """MIT License
 
 Copyright (c) 2023 Linux Profile
 
 Permission is hereby granted, free of charge, to any person obtaining a copy
@@ -21,12 +21,11 @@
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 SOFTWARE."""
 
 
 __info__ = """
-
-Help: linuxp-plugin --help
+Help: linuxp_plugin --help
 Docs: https://docs.linuxprofile.com/
 =====================================
 """
```

### Comparing `linuxp-plugin-1.0.1/linux_profile_plugin/commands.py` & `linuxp-plugin-1.0.2/linux_profile_plugin/commands.py`

 * *Files identical despite different names*

### Comparing `linuxp-plugin-1.0.1/linux_profile_plugin/main.py` & `linuxp-plugin-1.0.2/linux_profile_plugin/main.py`

 * *Files identical despite different names*

### Comparing `linuxp-plugin-1.0.1/linuxp_plugin.egg-info/PKG-INFO` & `linuxp-plugin-1.0.2/linuxp_plugin.egg-info/PKG-INFO`

 * *Files 17% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 Metadata-Version: 2.1
 Name: linuxp-plugin
-Version: 1.0.1
+Version: 1.0.2
 Summary: 🐧 Plugin Linux Profile
-Home-page: https://github.com/MyLinuxProfile/linux-profile-plugin
+Home-page: https://github.com/linux-profile/linux-profile-plugin
 Author: Fernando Celmer
 Author-email: email@fernandocelmer.com
 Classifier: Development Status :: 4 - Beta
 Classifier: Operating System :: OS Independent
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Intended Audience :: Developers
 Classifier: Natural Language :: English
@@ -15,28 +15,28 @@
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10
 Requires-Python: >=3.6
 Description-Content-Type: text/markdown
 License-File: LICENSE
 
-<img src="https://github.com/MyLinuxProfile/linux-profile-plugin/blob/master/docs/linuxp.png?raw=true">
+<img src="https://github.com/linux-profile/linux-profile-plugin/blob/master/docs/linuxp.png?raw=true">
 
-![GitHub Org's stars](https://img.shields.io/github/stars/MyLinuxProfile?label=LinuxProfile&style=flat-square)
-![GitHub last commit](https://img.shields.io/github/last-commit/MyLinuxProfile/linux-profile-plugin?style=flat-square)
+![GitHub Org's stars](https://img.shields.io/github/stars/linux-profile?label=LinuxProfile&style=flat-square)
+![GitHub last commit](https://img.shields.io/github/last-commit/linux-profile/linux-profile-plugin?style=flat-square)
 ![PyPI](https://img.shields.io/pypi/v/linuxp-plugin)
 
-[![check](https://github.com/MyLinuxProfile/linux-profile-plugin/actions/workflows/python-publish-pypi.yml/badge.svg)](https://github.com/MyLinuxProfile/linux-profile-plugin/actions/workflows/python-publish-pypi.yml)
-[![check](https://github.com/MyLinuxProfile/linux-profile-plugin/actions/workflows/python-publish-pypi-test.yml/badge.svg)](https://github.com/MyLinuxProfile/linux-profile-plugin/actions/workflows/python-publish-pypi-test.yml)
-[![check](https://github.com/MyLinuxProfile/linux-profile-plugin/actions/workflows/python-app-code.yml/badge.svg)](https://github.com/MyLinuxProfile/linux-profile-plugin/actions/workflows/python-app-code.yml)
+[![check](https://github.com/linux-profile/linux-profile-plugin/actions/workflows/python-publish-pypi.yml/badge.svg)](https://github.com/linux-profile/linux-profile-plugin/actions/workflows/python-publish-pypi.yml)
+[![check](https://github.com/linux-profile/linux-profile-plugin/actions/workflows/python-publish-pypi-test.yml/badge.svg)](https://github.com/linux-profile/linux-profile-plugin/actions/workflows/python-publish-pypi-test.yml)
+[![check](https://github.com/linux-profile/linux-profile-plugin/actions/workflows/python-app-code.yml/badge.svg)](https://github.com/linux-profile/linux-profile-plugin/actions/workflows/python-app-code.yml)
 
 ---
 
 - **Documentation**: [https://docs.linuxprofile.com](https://docs.linuxprofile.com)
-- **Source Code**: [https://github.com/MyLinuxProfile/linux-profile-plugin](https://github.com/MyLinuxProfile/linux-profile-plugin)
+- **Source Code**: [https://github.com/linux-profile/linux-profile-plugin](https://github.com/linux-profile/linux-profile-plugin)
 
 ---
 
 ## Installation
 
 - **Install - Pypi/PIP**
 
@@ -47,18 +47,21 @@
 | Command               | Description                                                                           | Docs      |
 |:--------------------- |:------------------------------------------------------------------------------------- | :-------: | 
 | ``linuxp_plugin hello``      | My custom command.                                                                    | [Link](#) |
 | ``linuxp_plugin explore``    | This command shows some settings.                                                     | [Link](#) |
 
 
 ## Commit Style
-- ⚙️ NO-TASK
+
+- ⚙️ FEATURE
 - 📝 PEP8
 - 📌 ISSUE
 - 🪲 BUG
 - 📘 DOCS
 - 📦 PyPI
 - ❤️️ TEST
+- ⬆️ CI/CD
+- ⚠️ SECURITY
 
 ## License
 
 This project is licensed under the terms of the MIT license.
```

### Comparing `linuxp-plugin-1.0.1/setup.py` & `linuxp-plugin-1.0.2/setup.py`

 * *Files 16% similar despite different names*

```diff
@@ -19,15 +19,15 @@
     name="linuxp-plugin",
     version=__version__,
     author="Fernando Celmer",
     author_email="email@fernandocelmer.com",
     description="🐧 Plugin Linux Profile",
     long_description=long_description,
     long_description_content_type="text/markdown",
-    url="https://github.com/MyLinuxProfile/linux-profile-plugin",
+    url="https://github.com/linux-profile/linux-profile-plugin",
     cmdclass={
         'install': CustomInstallCommand,
     },
     install_requires=[
         'linuxp>=1.0.16'
     ],
     classifiers=[
```

