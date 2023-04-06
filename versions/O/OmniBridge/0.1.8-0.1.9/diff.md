# Comparing `tmp/OmniBridge-0.1.8.tar.gz` & `tmp/OmniBridge-0.1.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "OmniBridge-0.1.8.tar", last modified: Thu Apr  6 15:44:17 2023, max compression
+gzip compressed data, was "OmniBridge-0.1.9.tar", last modified: Thu Apr  6 15:54:40 2023, max compression
```

## Comparing `OmniBridge-0.1.8.tar` & `OmniBridge-0.1.9.tar`

### file list

```diff
@@ -1,17 +1,37 @@
-drwxrwxrwx   0        0        0        0 2023-04-06 15:44:17.919069 OmniBridge-0.1.8/
--rw-rw-rw-   0        0        0    11558 2023-04-06 06:04:35.000000 OmniBridge-0.1.8/LICENSE
-drwxrwxrwx   0        0        0        0 2023-04-06 15:44:17.914040 OmniBridge-0.1.8/OmniBridge.egg-info/
--rw-rw-rw-   0        0        0      951 2023-04-06 15:44:17.000000 OmniBridge-0.1.8/OmniBridge.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      274 2023-04-06 15:44:17.000000 OmniBridge-0.1.8/OmniBridge.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-06 15:44:17.000000 OmniBridge-0.1.8/OmniBridge.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       23 2023-04-06 15:44:17.000000 OmniBridge-0.1.8/OmniBridge.egg-info/requires.txt
--rw-rw-rw-   0        0        0       11 2023-04-06 15:44:17.000000 OmniBridge-0.1.8/OmniBridge.egg-info/top_level.txt
--rw-rw-rw-   0        0        0      951 2023-04-06 15:44:17.918069 OmniBridge-0.1.8/PKG-INFO
--rw-rw-rw-   0        0        0      659 2023-04-06 05:36:51.000000 OmniBridge-0.1.8/README.md
-drwxrwxrwx   0        0        0        0 2023-04-06 15:44:17.917040 OmniBridge-0.1.8/omnibridge/
--rw-rw-rw-   0        0        0        0 2023-04-06 08:39:45.000000 OmniBridge-0.1.8/omnibridge/__init__.py
--rw-rw-rw-   0        0        0     1598 2023-04-06 08:26:29.000000 OmniBridge-0.1.8/omnibridge/main.py
--rw-rw-rw-   0        0        0       17 2023-04-06 15:25:16.000000 OmniBridge-0.1.8/omnibridge/version.py
--rw-rw-rw-   0        0        0     1151 2023-04-05 09:41:50.000000 OmniBridge-0.1.8/pyproject.toml
--rw-rw-rw-   0        0        0       42 2023-04-06 15:44:17.919069 OmniBridge-0.1.8/setup.cfg
--rw-rw-rw-   0        0        0      924 2023-04-06 15:42:54.000000 OmniBridge-0.1.8/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-06 15:54:40.083122 OmniBridge-0.1.9/
+-rw-rw-rw-   0        0        0    11558 2023-04-06 06:04:35.000000 OmniBridge-0.1.9/LICENSE
+drwxrwxrwx   0        0        0        0 2023-04-06 15:54:40.058001 OmniBridge-0.1.9/OmniBridge.egg-info/
+-rw-rw-rw-   0        0        0      951 2023-04-06 15:54:39.000000 OmniBridge-0.1.9/OmniBridge.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0     1083 2023-04-06 15:54:40.000000 OmniBridge-0.1.9/OmniBridge.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-06 15:54:39.000000 OmniBridge-0.1.9/OmniBridge.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       23 2023-04-06 15:54:39.000000 OmniBridge-0.1.9/OmniBridge.egg-info/requires.txt
+-rw-rw-rw-   0        0        0       11 2023-04-06 15:54:39.000000 OmniBridge-0.1.9/OmniBridge.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0      951 2023-04-06 15:54:40.082123 OmniBridge-0.1.9/PKG-INFO
+-rw-rw-rw-   0        0        0      659 2023-04-06 05:36:51.000000 OmniBridge-0.1.9/README.md
+drwxrwxrwx   0        0        0        0 2023-04-06 15:54:40.062005 OmniBridge-0.1.9/omnibridge/
+-rw-rw-rw-   0        0        0        0 2023-04-06 08:39:45.000000 OmniBridge-0.1.9/omnibridge/__init__.py
+drwxrwxrwx   0        0        0        0 2023-04-06 15:54:40.064005 OmniBridge-0.1.9/omnibridge/cli/
+-rw-rw-rw-   0        0        0        0 2023-04-06 15:06:12.000000 OmniBridge-0.1.9/omnibridge/cli/__init__.py
+-rw-rw-rw-   0        0        0      493 2023-04-06 15:36:31.000000 OmniBridge-0.1.9/omnibridge/cli/banner.py
+-rw-rw-rw-   0        0        0     1598 2023-04-06 08:26:29.000000 OmniBridge-0.1.9/omnibridge/main.py
+-rw-rw-rw-   0        0        0       17 2023-04-06 15:54:35.000000 OmniBridge-0.1.9/omnibridge/version.py
+drwxrwxrwx   0        0        0        0 2023-04-06 15:54:40.066051 OmniBridge-0.1.9/omnibridge/wrappers/
+-rw-rw-rw-   0        0        0        0 2023-04-06 15:06:24.000000 OmniBridge-0.1.9/omnibridge/wrappers/__init__.py
+drwxrwxrwx   0        0        0        0 2023-04-06 15:54:40.071612 OmniBridge-0.1.9/omnibridge/wrappers/api_based_wrappers/
+-rw-rw-rw-   0        0        0        0 2023-04-06 15:06:46.000000 OmniBridge-0.1.9/omnibridge/wrappers/api_based_wrappers/__init__.py
+-rw-rw-rw-   0        0        0     1389 2023-04-06 08:29:58.000000 OmniBridge-0.1.9/omnibridge/wrappers/api_based_wrappers/base_api_wrapper.py
+-rw-rw-rw-   0        0        0     1247 2023-04-06 08:29:58.000000 OmniBridge-0.1.9/omnibridge/wrappers/api_based_wrappers/dalle_wrapper.py
+-rw-rw-rw-   0        0        0     1702 2023-04-06 08:29:58.000000 OmniBridge-0.1.9/omnibridge/wrappers/api_based_wrappers/gpt_wrapper.py
+-rw-rw-rw-   0        0        0      973 2023-04-06 08:29:58.000000 OmniBridge-0.1.9/omnibridge/wrappers/api_based_wrappers/hugging_face_wrapper.py
+drwxrwxrwx   0        0        0        0 2023-04-06 15:54:40.081122 OmniBridge-0.1.9/omnibridge/wrappers/models_configurations/
+-rw-rw-rw-   0        0        0        0 2023-04-06 08:29:58.000000 OmniBridge-0.1.9/omnibridge/wrappers/models_configurations/__init__.py
+-rw-rw-rw-   0        0        0      634 2023-04-06 08:29:58.000000 OmniBridge-0.1.9/omnibridge/wrappers/models_configurations/base_config.py
+-rw-rw-rw-   0        0        0      639 2023-04-06 08:29:58.000000 OmniBridge-0.1.9/omnibridge/wrappers/models_configurations/chatgpt_config.py
+-rw-rw-rw-   0        0        0     1871 2023-04-06 08:29:58.000000 OmniBridge-0.1.9/omnibridge/wrappers/models_configurations/config_loader.py
+-rw-rw-rw-   0        0        0      136 2023-04-06 08:29:58.000000 OmniBridge-0.1.9/omnibridge/wrappers/models_configurations/config_types.py
+-rw-rw-rw-   0        0        0      410 2023-04-06 08:29:58.000000 OmniBridge-0.1.9/omnibridge/wrappers/models_configurations/dalle_config.py
+-rw-rw-rw-   0        0        0      352 2023-04-06 08:29:58.000000 OmniBridge-0.1.9/omnibridge/wrappers/models_configurations/hugging_face_config.py
+-rw-rw-rw-   0        0        0     1559 2023-04-06 08:29:58.000000 OmniBridge-0.1.9/omnibridge/wrappers/runners.py
+-rw-rw-rw-   0        0        0     1151 2023-04-05 09:41:50.000000 OmniBridge-0.1.9/pyproject.toml
+-rw-rw-rw-   0        0        0       42 2023-04-06 15:54:40.083122 OmniBridge-0.1.9/setup.cfg
+-rw-rw-rw-   0        0        0      959 2023-04-06 15:54:36.000000 OmniBridge-0.1.9/setup.py
```

### Comparing `OmniBridge-0.1.8/LICENSE` & `OmniBridge-0.1.9/LICENSE`

 * *Files identical despite different names*

### Comparing `OmniBridge-0.1.8/OmniBridge.egg-info/PKG-INFO` & `OmniBridge-0.1.9/OmniBridge.egg-info/PKG-INFO`

 * *Files 12% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: OmniBridge
-Version: 0.1.8
+Version: 0.1.9
 Summary: Bridging AI models
 Home-page: https://github.com/tmpOrgName/OmniBridge
 Author: OmniSpective
 Author-email: eliran9692@gmail.com
 License: Apache License 2.0
 Description-Content-Type: text/markdown
 License-File: LICENSE
```

### Comparing `OmniBridge-0.1.8/PKG-INFO` & `OmniBridge-0.1.9/PKG-INFO`

 * *Files 12% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: OmniBridge
-Version: 0.1.8
+Version: 0.1.9
 Summary: Bridging AI models
 Home-page: https://github.com/tmpOrgName/OmniBridge
 Author: OmniSpective
 Author-email: eliran9692@gmail.com
 License: Apache License 2.0
 Description-Content-Type: text/markdown
 License-File: LICENSE
```

### Comparing `OmniBridge-0.1.8/README.md` & `OmniBridge-0.1.9/README.md`

 * *Files identical despite different names*

### Comparing `OmniBridge-0.1.8/omnibridge/main.py` & `OmniBridge-0.1.9/omnibridge/main.py`

 * *Files identical despite different names*

### Comparing `OmniBridge-0.1.8/pyproject.toml` & `OmniBridge-0.1.9/pyproject.toml`

 * *Files identical despite different names*

### Comparing `OmniBridge-0.1.8/setup.py` & `OmniBridge-0.1.9/setup.py`

 * *Files 9% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-from setuptools import setup
+from setuptools import setup, find_packages
 from importlib import util
 from os import path
 import os
 
 this_directory = path.abspath(path.dirname(__file__))
 with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
     long_description = f.read()
@@ -14,21 +14,21 @@
 spec.loader.exec_module(mod)
 version = mod.version
 
 
 setup(
     name='OmniBridge',
     license="Apache License 2.0",
-    version="0.1.8",
+    version=version,
     author='OmniSpective',
     author_email='eliran9692@gmail.com',
     description='Bridging AI models',
     long_description=long_description,
     long_description_content_type="text/markdown",
     url='https://github.com/tmpOrgName/OmniBridge',
-    packages=['omnibridge'],
+    packages=find_packages(exclude=["version"]),
     install_requires=[
         'requests',
         'ruff',
         'argparse'
     ],
 )
```

