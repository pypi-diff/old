# Comparing `tmp/azure-core-experimental-1.0.0b1.zip` & `tmp/azure-core-experimental-1.0.0b2.zip`

## zipinfo {}

```diff
@@ -1,34 +1,43 @@
-Zip file size: 20049 bytes, number of entries: 32
-drwxrwxr-x  2.0 unx        0 b- stor 22-Oct-05 20:29 azure-core-experimental-1.0.0b1/
-drwxrwxr-x  2.0 unx        0 b- stor 22-Oct-05 20:29 azure-core-experimental-1.0.0b1/azure_core_experimental.egg-info/
-drwxrwxr-x  2.0 unx        0 b- stor 22-Oct-05 20:29 azure-core-experimental-1.0.0b1/tests/
-drwxrwxr-x  2.0 unx        0 b- stor 22-Oct-05 20:29 azure-core-experimental-1.0.0b1/azure/
-drwxrwxr-x  2.0 unx        0 b- stor 22-Oct-05 20:29 azure-core-experimental-1.0.0b1/samples/
--rw-rw-r--  2.0 unx       38 b- defN 22-Oct-05 20:29 azure-core-experimental-1.0.0b1/setup.cfg
--rw-rw-r--  2.0 unx     1073 b- defN 22-Oct-05 20:27 azure-core-experimental-1.0.0b1/LICENSE
--rw-rw-r--  2.0 unx     2333 b- defN 22-Oct-05 20:27 azure-core-experimental-1.0.0b1/setup.py
--rw-rw-r--  2.0 unx      139 b- defN 22-Oct-05 20:27 azure-core-experimental-1.0.0b1/CHANGELOG.md
--rw-rw-r--  2.0 unx     1567 b- defN 22-Oct-05 20:27 azure-core-experimental-1.0.0b1/README.md
--rw-rw-r--  2.0 unx      278 b- defN 22-Oct-05 20:27 azure-core-experimental-1.0.0b1/MANIFEST.in
--rw-rw-r--  2.0 unx     2609 b- defN 22-Oct-05 20:29 azure-core-experimental-1.0.0b1/PKG-INFO
--rw-rw-r--  2.0 unx        6 b- defN 22-Oct-05 20:29 azure-core-experimental-1.0.0b1/azure_core_experimental.egg-info/top_level.txt
--rw-rw-r--  2.0 unx        1 b- defN 22-Oct-05 20:29 azure-core-experimental-1.0.0b1/azure_core_experimental.egg-info/dependency_links.txt
--rw-rw-r--  2.0 unx      685 b- defN 22-Oct-05 20:29 azure-core-experimental-1.0.0b1/azure_core_experimental.egg-info/SOURCES.txt
--rw-rw-r--  2.0 unx       26 b- defN 22-Oct-05 20:29 azure-core-experimental-1.0.0b1/azure_core_experimental.egg-info/requires.txt
--rw-rw-r--  2.0 unx        1 b- defN 22-Oct-05 20:29 azure-core-experimental-1.0.0b1/azure_core_experimental.egg-info/not-zip-safe
--rw-rw-r--  2.0 unx     2609 b- defN 22-Oct-05 20:29 azure-core-experimental-1.0.0b1/azure_core_experimental.egg-info/PKG-INFO
--rw-rw-r--  2.0 unx     7127 b- defN 22-Oct-05 20:27 azure-core-experimental-1.0.0b1/tests/test_pyodide_transport.py
-drwxrwxr-x  2.0 unx        0 b- stor 22-Oct-05 20:29 azure-core-experimental-1.0.0b1/azure/core/
--rw-rw-r--  2.0 unx       81 b- defN 22-Oct-05 20:27 azure-core-experimental-1.0.0b1/azure/__init__.py
-drwxrwxr-x  2.0 unx        0 b- stor 22-Oct-05 20:29 azure-core-experimental-1.0.0b1/azure/core/experimental/
--rw-rw-r--  2.0 unx       81 b- defN 22-Oct-05 20:27 azure-core-experimental-1.0.0b1/azure/core/__init__.py
-drwxrwxr-x  2.0 unx        0 b- stor 22-Oct-05 20:29 azure-core-experimental-1.0.0b1/azure/core/experimental/transport/
--rw-rw-r--  2.0 unx      172 b- defN 22-Oct-05 20:27 azure-core-experimental-1.0.0b1/azure/core/experimental/_version.py
--rw-rw-r--  2.0 unx     1356 b- defN 22-Oct-05 20:27 azure-core-experimental-1.0.0b1/azure/core/experimental/__init__.py
--rw-rw-r--  2.0 unx        0 b- defN 22-Oct-05 20:27 azure-core-experimental-1.0.0b1/azure/core/experimental/py.typed
--rw-rw-r--  2.0 unx     6431 b- defN 22-Oct-05 20:27 azure-core-experimental-1.0.0b1/azure/core/experimental/transport/_pyodide.py
--rw-rw-r--  2.0 unx     1862 b- defN 22-Oct-05 20:27 azure-core-experimental-1.0.0b1/azure/core/experimental/transport/__init__.py
-drwxrwxr-x  2.0 unx        0 b- stor 22-Oct-05 20:29 azure-core-experimental-1.0.0b1/samples/pyodide_integration/
--rw-rw-r--  2.0 unx     5354 b- defN 22-Oct-05 20:27 azure-core-experimental-1.0.0b1/samples/pyodide_integration/browser.py
--rw-rw-r--  2.0 unx      855 b- defN 22-Oct-05 20:27 azure-core-experimental-1.0.0b1/samples/pyodide_integration/async_testing.py
-32 files, 34684 bytes uncompressed, 13883 bytes compressed:  60.0%
+Zip file size: 28438 bytes, number of entries: 41
+drwxrwxr-x  2.0 unx        0 b- stor 23-Apr-06 18:54 azure-core-experimental-1.0.0b2/
+drwxrwxr-x  2.0 unx        0 b- stor 23-Apr-06 18:54 azure-core-experimental-1.0.0b2/samples/
+drwxrwxr-x  2.0 unx        0 b- stor 23-Apr-06 18:54 azure-core-experimental-1.0.0b2/azure/
+drwxrwxr-x  2.0 unx        0 b- stor 23-Apr-06 18:54 azure-core-experimental-1.0.0b2/azure_core_experimental.egg-info/
+drwxrwxr-x  2.0 unx        0 b- stor 23-Apr-06 18:54 azure-core-experimental-1.0.0b2/tests/
+-rw-rw-r--  2.0 unx      278 b- defN 23-Apr-06 18:52 azure-core-experimental-1.0.0b2/MANIFEST.in
+-rw-rw-r--  2.0 unx     2729 b- defN 23-Apr-06 18:54 azure-core-experimental-1.0.0b2/PKG-INFO
+-rw-rw-r--  2.0 unx     1585 b- defN 23-Apr-06 18:52 azure-core-experimental-1.0.0b2/README.md
+-rw-rw-r--  2.0 unx     1073 b- defN 23-Apr-06 18:52 azure-core-experimental-1.0.0b2/LICENSE
+-rw-rw-r--  2.0 unx     2311 b- defN 23-Apr-06 18:52 azure-core-experimental-1.0.0b2/setup.py
+-rw-rw-r--  2.0 unx       38 b- defN 23-Apr-06 18:54 azure-core-experimental-1.0.0b2/setup.cfg
+-rw-rw-r--  2.0 unx      241 b- defN 23-Apr-06 18:52 azure-core-experimental-1.0.0b2/CHANGELOG.md
+-rw-rw-r--  2.0 unx       98 b- defN 23-Apr-06 18:52 azure-core-experimental-1.0.0b2/pyproject.toml
+drwxrwxr-x  2.0 unx        0 b- stor 23-Apr-06 18:54 azure-core-experimental-1.0.0b2/samples/httpx_integration/
+drwxrwxr-x  2.0 unx        0 b- stor 23-Apr-06 18:54 azure-core-experimental-1.0.0b2/samples/pyodide_integration/
+-rw-rw-r--  2.0 unx     1824 b- defN 23-Apr-06 18:52 azure-core-experimental-1.0.0b2/samples/httpx_integration/httpx_transport_sample_async.py
+-rw-rw-r--  2.0 unx     1043 b- defN 23-Apr-06 18:52 azure-core-experimental-1.0.0b2/samples/httpx_integration/httpx_transport_sample.py
+-rw-rw-r--  2.0 unx     5331 b- defN 23-Apr-06 18:52 azure-core-experimental-1.0.0b2/samples/pyodide_integration/browser.py
+-rw-rw-r--  2.0 unx      855 b- defN 23-Apr-06 18:52 azure-core-experimental-1.0.0b2/samples/pyodide_integration/async_testing.py
+drwxrwxr-x  2.0 unx        0 b- stor 23-Apr-06 18:54 azure-core-experimental-1.0.0b2/azure/core/
+-rw-rw-r--  2.0 unx       81 b- defN 23-Apr-06 18:52 azure-core-experimental-1.0.0b2/azure/__init__.py
+drwxrwxr-x  2.0 unx        0 b- stor 23-Apr-06 18:54 azure-core-experimental-1.0.0b2/azure/core/experimental/
+-rw-rw-r--  2.0 unx       81 b- defN 23-Apr-06 18:52 azure-core-experimental-1.0.0b2/azure/core/__init__.py
+drwxrwxr-x  2.0 unx        0 b- stor 23-Apr-06 18:54 azure-core-experimental-1.0.0b2/azure/core/experimental/transport/
+-rw-rw-r--  2.0 unx     1357 b- defN 23-Apr-06 18:52 azure-core-experimental-1.0.0b2/azure/core/experimental/__init__.py
+-rw-rw-r--  2.0 unx      172 b- defN 23-Apr-06 18:52 azure-core-experimental-1.0.0b2/azure/core/experimental/_version.py
+-rw-rw-r--  2.0 unx        0 b- defN 23-Apr-06 18:52 azure-core-experimental-1.0.0b2/azure/core/experimental/py.typed
+-rw-rw-r--  2.0 unx     2430 b- defN 23-Apr-06 18:52 azure-core-experimental-1.0.0b2/azure/core/experimental/transport/__init__.py
+-rw-rw-r--  2.0 unx     5621 b- defN 23-Apr-06 18:52 azure-core-experimental-1.0.0b2/azure/core/experimental/transport/_httpx_async.py
+-rw-rw-r--  2.0 unx     5223 b- defN 23-Apr-06 18:52 azure-core-experimental-1.0.0b2/azure/core/experimental/transport/_httpx.py
+-rw-rw-r--  2.0 unx     6433 b- defN 23-Apr-06 18:52 azure-core-experimental-1.0.0b2/azure/core/experimental/transport/_pyodide.py
+-rw-rw-r--  2.0 unx     2729 b- defN 23-Apr-06 18:54 azure-core-experimental-1.0.0b2/azure_core_experimental.egg-info/PKG-INFO
+-rw-rw-r--  2.0 unx      982 b- defN 23-Apr-06 18:54 azure-core-experimental-1.0.0b2/azure_core_experimental.egg-info/SOURCES.txt
+-rw-rw-r--  2.0 unx       26 b- defN 23-Apr-06 18:54 azure-core-experimental-1.0.0b2/azure_core_experimental.egg-info/requires.txt
+-rw-rw-r--  2.0 unx        1 b- defN 23-Apr-06 18:54 azure-core-experimental-1.0.0b2/azure_core_experimental.egg-info/not-zip-safe
+-rw-rw-r--  2.0 unx        1 b- defN 23-Apr-06 18:54 azure-core-experimental-1.0.0b2/azure_core_experimental.egg-info/dependency_links.txt
+-rw-rw-r--  2.0 unx        6 b- defN 23-Apr-06 18:54 azure-core-experimental-1.0.0b2/azure_core_experimental.egg-info/top_level.txt
+drwxrwxr-x  2.0 unx        0 b- stor 23-Apr-06 18:54 azure-core-experimental-1.0.0b2/tests/async_tests/
+-rw-rw-r--  2.0 unx     1907 b- defN 23-Apr-06 18:52 azure-core-experimental-1.0.0b2/tests/test_httpx_transport.py
+-rw-rw-r--  2.0 unx     7088 b- defN 23-Apr-06 18:52 azure-core-experimental-1.0.0b2/tests/test_pyodide_transport.py
+-rw-rw-r--  2.0 unx     2061 b- defN 23-Apr-06 18:52 azure-core-experimental-1.0.0b2/tests/async_tests/test_httpx_transport_async.py
+41 files, 53605 bytes uncompressed, 20344 bytes compressed:  62.0%
```

## zipnote {}

```diff
@@ -1,97 +1,124 @@
-Filename: azure-core-experimental-1.0.0b1/
+Filename: azure-core-experimental-1.0.0b2/
 Comment: 
 
-Filename: azure-core-experimental-1.0.0b1/azure_core_experimental.egg-info/
+Filename: azure-core-experimental-1.0.0b2/samples/
 Comment: 
 
-Filename: azure-core-experimental-1.0.0b1/tests/
+Filename: azure-core-experimental-1.0.0b2/azure/
 Comment: 
 
-Filename: azure-core-experimental-1.0.0b1/azure/
+Filename: azure-core-experimental-1.0.0b2/azure_core_experimental.egg-info/
 Comment: 
 
-Filename: azure-core-experimental-1.0.0b1/samples/
+Filename: azure-core-experimental-1.0.0b2/tests/
 Comment: 
 
-Filename: azure-core-experimental-1.0.0b1/setup.cfg
+Filename: azure-core-experimental-1.0.0b2/MANIFEST.in
 Comment: 
 
-Filename: azure-core-experimental-1.0.0b1/LICENSE
+Filename: azure-core-experimental-1.0.0b2/PKG-INFO
 Comment: 
 
-Filename: azure-core-experimental-1.0.0b1/setup.py
+Filename: azure-core-experimental-1.0.0b2/README.md
 Comment: 
 
-Filename: azure-core-experimental-1.0.0b1/CHANGELOG.md
+Filename: azure-core-experimental-1.0.0b2/LICENSE
 Comment: 
 
-Filename: azure-core-experimental-1.0.0b1/README.md
+Filename: azure-core-experimental-1.0.0b2/setup.py
 Comment: 
 
-Filename: azure-core-experimental-1.0.0b1/MANIFEST.in
+Filename: azure-core-experimental-1.0.0b2/setup.cfg
 Comment: 
 
-Filename: azure-core-experimental-1.0.0b1/PKG-INFO
+Filename: azure-core-experimental-1.0.0b2/CHANGELOG.md
 Comment: 
 
-Filename: azure-core-experimental-1.0.0b1/azure_core_experimental.egg-info/top_level.txt
+Filename: azure-core-experimental-1.0.0b2/pyproject.toml
 Comment: 
 
-Filename: azure-core-experimental-1.0.0b1/azure_core_experimental.egg-info/dependency_links.txt
+Filename: azure-core-experimental-1.0.0b2/samples/httpx_integration/
 Comment: 
 
-Filename: azure-core-experimental-1.0.0b1/azure_core_experimental.egg-info/SOURCES.txt
+Filename: azure-core-experimental-1.0.0b2/samples/pyodide_integration/
 Comment: 
 
-Filename: azure-core-experimental-1.0.0b1/azure_core_experimental.egg-info/requires.txt
+Filename: azure-core-experimental-1.0.0b2/samples/httpx_integration/httpx_transport_sample_async.py
 Comment: 
 
-Filename: azure-core-experimental-1.0.0b1/azure_core_experimental.egg-info/not-zip-safe
+Filename: azure-core-experimental-1.0.0b2/samples/httpx_integration/httpx_transport_sample.py
 Comment: 
 
-Filename: azure-core-experimental-1.0.0b1/azure_core_experimental.egg-info/PKG-INFO
+Filename: azure-core-experimental-1.0.0b2/samples/pyodide_integration/browser.py
 Comment: 
 
-Filename: azure-core-experimental-1.0.0b1/tests/test_pyodide_transport.py
+Filename: azure-core-experimental-1.0.0b2/samples/pyodide_integration/async_testing.py
 Comment: 
 
-Filename: azure-core-experimental-1.0.0b1/azure/core/
+Filename: azure-core-experimental-1.0.0b2/azure/core/
 Comment: 
 
-Filename: azure-core-experimental-1.0.0b1/azure/__init__.py
+Filename: azure-core-experimental-1.0.0b2/azure/__init__.py
 Comment: 
 
-Filename: azure-core-experimental-1.0.0b1/azure/core/experimental/
+Filename: azure-core-experimental-1.0.0b2/azure/core/experimental/
 Comment: 
 
-Filename: azure-core-experimental-1.0.0b1/azure/core/__init__.py
+Filename: azure-core-experimental-1.0.0b2/azure/core/__init__.py
 Comment: 
 
-Filename: azure-core-experimental-1.0.0b1/azure/core/experimental/transport/
+Filename: azure-core-experimental-1.0.0b2/azure/core/experimental/transport/
 Comment: 
 
-Filename: azure-core-experimental-1.0.0b1/azure/core/experimental/_version.py
+Filename: azure-core-experimental-1.0.0b2/azure/core/experimental/__init__.py
 Comment: 
 
-Filename: azure-core-experimental-1.0.0b1/azure/core/experimental/__init__.py
+Filename: azure-core-experimental-1.0.0b2/azure/core/experimental/_version.py
 Comment: 
 
-Filename: azure-core-experimental-1.0.0b1/azure/core/experimental/py.typed
+Filename: azure-core-experimental-1.0.0b2/azure/core/experimental/py.typed
 Comment: 
 
-Filename: azure-core-experimental-1.0.0b1/azure/core/experimental/transport/_pyodide.py
+Filename: azure-core-experimental-1.0.0b2/azure/core/experimental/transport/__init__.py
 Comment: 
 
-Filename: azure-core-experimental-1.0.0b1/azure/core/experimental/transport/__init__.py
+Filename: azure-core-experimental-1.0.0b2/azure/core/experimental/transport/_httpx_async.py
 Comment: 
 
-Filename: azure-core-experimental-1.0.0b1/samples/pyodide_integration/
+Filename: azure-core-experimental-1.0.0b2/azure/core/experimental/transport/_httpx.py
 Comment: 
 
-Filename: azure-core-experimental-1.0.0b1/samples/pyodide_integration/browser.py
+Filename: azure-core-experimental-1.0.0b2/azure/core/experimental/transport/_pyodide.py
 Comment: 
 
-Filename: azure-core-experimental-1.0.0b1/samples/pyodide_integration/async_testing.py
+Filename: azure-core-experimental-1.0.0b2/azure_core_experimental.egg-info/PKG-INFO
+Comment: 
+
+Filename: azure-core-experimental-1.0.0b2/azure_core_experimental.egg-info/SOURCES.txt
+Comment: 
+
+Filename: azure-core-experimental-1.0.0b2/azure_core_experimental.egg-info/requires.txt
+Comment: 
+
+Filename: azure-core-experimental-1.0.0b2/azure_core_experimental.egg-info/not-zip-safe
+Comment: 
+
+Filename: azure-core-experimental-1.0.0b2/azure_core_experimental.egg-info/dependency_links.txt
+Comment: 
+
+Filename: azure-core-experimental-1.0.0b2/azure_core_experimental.egg-info/top_level.txt
+Comment: 
+
+Filename: azure-core-experimental-1.0.0b2/tests/async_tests/
+Comment: 
+
+Filename: azure-core-experimental-1.0.0b2/tests/test_httpx_transport.py
+Comment: 
+
+Filename: azure-core-experimental-1.0.0b2/tests/test_pyodide_transport.py
+Comment: 
+
+Filename: azure-core-experimental-1.0.0b2/tests/async_tests/test_httpx_transport_async.py
 Comment: 
 
 Zip file comment:
```

## Comparing `azure-core-experimental-1.0.0b1/LICENSE` & `azure-core-experimental-1.0.0b2/LICENSE`

 * *Files identical despite different names*

## Comparing `azure-core-experimental-1.0.0b1/setup.py` & `azure-core-experimental-1.0.0b2/setup.py`

 * *Files 19% similar despite different names*

```diff
@@ -1,67 +1,66 @@
 #!/usr/bin/env python
 
-#-------------------------------------------------------------------------
+# -------------------------------------------------------------------------
 # Copyright (c) Microsoft Corporation. All rights reserved.
 # Licensed under the MIT License. See License.txt in the project root for
 # license information.
-#--------------------------------------------------------------------------
+# --------------------------------------------------------------------------
 
 import re
 import os.path
 from io import open
 from setuptools import find_packages, setup  # type: ignore
 
 # Change the PACKAGE_NAME only to change folder and different name
 PACKAGE_NAME = "azure-core-experimental"
 PACKAGE_PPRINT_NAME = "Core Experimental"
 
 package_folder_path = "azure/core/experimental"
 
 # Version extraction inspired from 'requests'
-with open(os.path.join(package_folder_path, '_version.py'), 'r') as fd:
-    version = re.search(r'^VERSION\s*=\s*[\'"]([^\'"]*)[\'"]',  # type: ignore
-                        fd.read(), re.MULTILINE).group(1)
+with open(os.path.join(package_folder_path, "_version.py"), "r") as fd:
+    version = re.search(r'^VERSION\s*=\s*[\'"]([^\'"]*)[\'"]', fd.read(), re.MULTILINE).group(1)  # type: ignore
 
 if not version:
-    raise RuntimeError('Cannot find version information')
+    raise RuntimeError("Cannot find version information")
 
-with open('README.md', encoding='utf-8') as f:
+with open("README.md", encoding="utf-8") as f:
     readme = f.read()
-with open('CHANGELOG.md', encoding='utf-8') as f:
+with open("CHANGELOG.md", encoding="utf-8") as f:
     changelog = f.read()
 
 setup(
     name=PACKAGE_NAME,
     version=version,
-    description='Microsoft Azure {} Library for Python'.format(PACKAGE_PPRINT_NAME),
-    long_description=readme + '\n\n' + changelog,
-    long_description_content_type='text/markdown',
-    license='MIT License',
-    author='Microsoft Corporation',
-    author_email='azpysdkhelp@microsoft.com',
-    url='https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/core/azure-core-experimental',
+    description="Microsoft Azure {} Library for Python".format(PACKAGE_PPRINT_NAME),
+    long_description=readme + "\n\n" + changelog,
+    long_description_content_type="text/markdown",
+    license="MIT License",
+    author="Microsoft Corporation",
+    author_email="azpysdkhelp@microsoft.com",
+    url="https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/core/azure-core-experimental",
     classifiers=[
         "Development Status :: 4 - Beta",
-        'Programming Language :: Python',
-        'Programming Language :: Python :: 3 :: Only',
-        'Programming Language :: Python :: 3',
-        'Programming Language :: Python :: 3.7',
-        'Programming Language :: Python :: 3.8',
-        'Programming Language :: Python :: 3.9',
-        'Programming Language :: Python :: 3.10',
-        'Programming Language :: Python :: 3.11',
-        'License :: OSI Approved :: MIT License',
+        "Programming Language :: Python",
+        "Programming Language :: Python :: 3 :: Only",
+        "Programming Language :: Python :: 3",
+        "Programming Language :: Python :: 3.7",
+        "Programming Language :: Python :: 3.8",
+        "Programming Language :: Python :: 3.9",
+        "Programming Language :: Python :: 3.10",
+        "Programming Language :: Python :: 3.11",
+        "License :: OSI Approved :: MIT License",
     ],
     zip_safe=False,
     packages=[
-        'azure.core.experimental',
+        "azure.core.experimental",
     ],
     include_package_data=True,
     package_data={
-        'pytyped': ['py.typed'],
+        "pytyped": ["py.typed"],
     },
     python_requires=">=3.7",
     install_requires=[
-        'azure-core<2.0.0,>=1.25.0',
+        "azure-core<2.0.0,>=1.25.0",
     ],
 )
```

## Comparing `azure-core-experimental-1.0.0b1/README.md` & `azure-core-experimental-1.0.0b2/README.md`

 * *Files 8% similar despite different names*

```diff
@@ -10,14 +10,15 @@
 ```bash
 pip install azure-core-experimental
 ```
 
 ## Features list
 
 - pyodide transport
+- httpx transport
 
 ## Contributing
 
 This project welcomes contributions and suggestions.  Most contributions require you to agree to a Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us the rights to use your contribution. For details, visit https://cla.microsoft.com.
 
 When you submit a pull request, a CLA-bot will automatically determine whether you need to provide a CLA and decorate the PR appropriately (e.g., label, comment). Simply follow the instructions provided by the bot. You will only need to do this once across all repos using our CLA.
```

## Comparing `azure-core-experimental-1.0.0b1/PKG-INFO` & `azure-core-experimental-1.0.0b2/PKG-INFO`

 * *Files 3% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: azure-core-experimental
-Version: 1.0.0b1
+Version: 1.0.0b2
 Summary: Microsoft Azure Core Experimental Library for Python
 Home-page: https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/core/azure-core-experimental
 Author: Microsoft Corporation
 Author-email: azpysdkhelp@microsoft.com
 License: MIT License
 Classifier: Development Status :: 4 - Beta
 Classifier: Programming Language :: Python
@@ -32,26 +32,33 @@
 ```bash
 pip install azure-core-experimental
 ```
 
 ## Features list
 
 - pyodide transport
+- httpx transport
 
 ## Contributing
 
 This project welcomes contributions and suggestions.  Most contributions require you to agree to a Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us the rights to use your contribution. For details, visit https://cla.microsoft.com.
 
 When you submit a pull request, a CLA-bot will automatically determine whether you need to provide a CLA and decorate the PR appropriately (e.g., label, comment). Simply follow the instructions provided by the bot. You will only need to do this once across all repos using our CLA.
 
 This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.
 
 
 # Release History
 
+## 1.0.0b2 (2023-04-06)
+
+### Features Added
+
+- httpx implementation of azure-core transport protocol
+
 ## 1.0.0b1 (2022-10-06)
 
 Initial release
 
 ### Features Added
 
 - pyodide implementation of azure-core transport protocol
```

## Comparing `azure-core-experimental-1.0.0b1/azure_core_experimental.egg-info/PKG-INFO` & `azure-core-experimental-1.0.0b2/azure_core_experimental.egg-info/PKG-INFO`

 * *Files 3% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: azure-core-experimental
-Version: 1.0.0b1
+Version: 1.0.0b2
 Summary: Microsoft Azure Core Experimental Library for Python
 Home-page: https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/core/azure-core-experimental
 Author: Microsoft Corporation
 Author-email: azpysdkhelp@microsoft.com
 License: MIT License
 Classifier: Development Status :: 4 - Beta
 Classifier: Programming Language :: Python
@@ -32,26 +32,33 @@
 ```bash
 pip install azure-core-experimental
 ```
 
 ## Features list
 
 - pyodide transport
+- httpx transport
 
 ## Contributing
 
 This project welcomes contributions and suggestions.  Most contributions require you to agree to a Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us the rights to use your contribution. For details, visit https://cla.microsoft.com.
 
 When you submit a pull request, a CLA-bot will automatically determine whether you need to provide a CLA and decorate the PR appropriately (e.g., label, comment). Simply follow the instructions provided by the bot. You will only need to do this once across all repos using our CLA.
 
 This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.
 
 
 # Release History
 
+## 1.0.0b2 (2023-04-06)
+
+### Features Added
+
+- httpx implementation of azure-core transport protocol
+
 ## 1.0.0b1 (2022-10-06)
 
 Initial release
 
 ### Features Added
 
 - pyodide implementation of azure-core transport protocol
```

## Comparing `azure-core-experimental-1.0.0b1/tests/test_pyodide_transport.py` & `azure-core-experimental-1.0.0b2/tests/test_pyodide_transport.py`

 * *Files 1% similar despite different names*

```diff
@@ -74,17 +74,15 @@
         return AsyncPipeline(transport.PyodideTransport(), [AsyncRetryPolicy()])
 
     @pytest.fixture()
     def mock_pyfetch(self, mock_pyodide_module):
         """Utility fixture for less typing."""
         return mock_pyodide_module.http.pyfetch
 
-    def create_mock_response(
-            self, body: bytes, headers: dict, status: int, status_text: str
-    ) -> mock.Mock:
+    def create_mock_response(self, body: bytes, headers: dict, status: int, status_text: str) -> mock.Mock:
         """Create a mock response object that mimics `pyodide.http.FetchResponse`"""
         mock_response = mock.Mock()
         mock_response.body = body
         mock_response.js_response.headers = headers
         mock_response.status = status
         mock_response.status_text = status_text
         bytes_promise = asyncio.Future()
@@ -102,17 +100,15 @@
     async def test_successful_send(self, mock_pyfetch, mock_pyodide_module, pipeline):
         """Test that a successful send returns the correct values."""
         # setup data
         mock_pyfetch.reset_mock()
         method = "POST"
         headers = {"key": "value"}
         data = b"data"
-        request = HttpRequest(
-            method=method, url=PLACEHOLDER_ENDPOINT, headers=headers, data=data
-        )
+        request = HttpRequest(method=method, url=PLACEHOLDER_ENDPOINT, headers=headers, data=data)
         response_body = b"0123"
         response_headers = {"header": "value"}
         response_status = 200
         response_text = "OK"
         mock_response = self.create_mock_response(
             body=response_body,
             headers=response_headers,
@@ -163,8 +159,9 @@
     @pytest.mark.skipif(sys.version_info < (3, 8), reason="pyodide needs py 3.8+")
     def test_valid_import(self, transport):
         """Test that we can import Pyodide classes from `azure.core.pipeline.transport`
         Adding the transport fixture will mock the Pyodide modules in `sys.modules`.
         """
         # Use patch so we don't clutter up the `sys.modules` namespace.
         import azure.core.experimental.transport as transport
+
         assert transport.PyodideTransport
```

## Comparing `azure-core-experimental-1.0.0b1/azure/core/experimental/__init__.py` & `azure-core-experimental-1.0.0b2/azure/core/experimental/__init__.py`

 * *Files 14% similar despite different names*

```diff
@@ -21,8 +21,9 @@
 # LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
 # FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
 # IN THE SOFTWARE.
 #
 # --------------------------------------------------------------------------
 
 from ._version import VERSION
+
 __version__ = VERSION
```

## Comparing `azure-core-experimental-1.0.0b1/azure/core/experimental/transport/_pyodide.py` & `azure-core-experimental-1.0.0b2/azure/core/experimental/transport/_pyodide.py`

 * *Files 0% similar despite different names*

```diff
@@ -23,30 +23,29 @@
 # IN THE SOFTWARE.
 #
 # --------------------------------------------------------------------------
 
 from collections.abc import AsyncIterator
 from io import BytesIO
 
-import js # pylint: disable=import-error
+import js  # pylint: disable=import-error
 from pyodide import JsException  # pylint: disable=import-error
 from pyodide.http import pyfetch  # pylint: disable=import-error
 
 from azure.core.exceptions import HttpResponseError
 from azure.core.pipeline import Pipeline
 from azure.core.utils import CaseInsensitiveDict
 
 from azure.core.rest._http_response_impl_async import AsyncHttpResponseImpl
 from azure.core.pipeline.transport import HttpRequest, AsyncioRequestsTransport
 
 
 class PyodideTransportResponse(AsyncHttpResponseImpl):
     """Async response object for the `PyodideTransport`."""
 
-
     def _js_stream(self):
         """So we get a fresh stream every time."""
         return self._internal_response.clone().js_response.body
 
     async def close(self) -> None:
         """We don't actually have control over closing connections in the browser, so we just pretend
         to close.
@@ -58,14 +57,15 @@
         return self.content
 
     async def load_body(self) -> None:
         """Backcompat"""
         if self._content is None:
             self._content = await self._internal_response.clone().bytes()
 
+
 class PyodideStreamDownloadGenerator(AsyncIterator):
     """Simple stream download generator that returns the contents of
     a request.
     """
 
     # pylint: disable=unused-argument
     def __init__(self, pipeline: Pipeline, response: PyodideTransportResponse, *_, **kwargs):
@@ -102,14 +102,15 @@
             self._buffer_left += self._stream.write(bytes(read.value))
 
         # move the stream position back to where we started
         self._stream.seek(start_pos)
         self._buffer_left -= self._block_size
         return self._stream.read(self._block_size)
 
+
 class PyodideTransport(AsyncioRequestsTransport):
     """**This object is experimental**, meaning it may be changed in a future release
     or might break with a future Pyodide release. This transport was built with Pyodide
     version 0.20.0.
 
     Implements a basic HTTP sender using the Pyodide Javascript Fetch API.
     """
```

## Comparing `azure-core-experimental-1.0.0b1/samples/pyodide_integration/browser.py` & `azure-core-experimental-1.0.0b2/samples/pyodide_integration/browser.py`

 * *Files 1% similar despite different names*

```diff
@@ -77,20 +77,17 @@
         assert data != b"hello world\n"
 
         response = await transport.send(request, stream_response=True)
         response.headers["enc"] = "deflate"
         data = b"".join([x async for x in response.iter_bytes()])
         assert data == b"hello world\n"
 
-
     async def test_sentiment_analysis(self):
         """Test that sentiment analysis works."""
-        results = await self.text_analytics_client.analyze_sentiment(
-            ["good great amazing"]
-        )
+        results = await self.text_analytics_client.analyze_sentiment(["good great amazing"])
         assert len(results) == 1
         result = results[0]
         assert result.sentiment == "positive"
         assert result.confidence_scores.positive > 0.98
         assert result.confidence_scores.neutral < 0.02
         assert result.confidence_scores.negative < 0.02
```

## Comparing `azure-core-experimental-1.0.0b1/samples/pyodide_integration/async_testing.py` & `azure-core-experimental-1.0.0b2/samples/pyodide_integration/async_testing.py`

 * *Files identical despite different names*

