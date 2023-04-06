# Comparing `tmp/uasset_dump-0.0.2.tar.gz` & `tmp/uasset_dump-0.0.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "uasset_dump-0.0.2.tar", max compression
+gzip compressed data, was "uasset_dump-0.0.3.tar", max compression
```

## Comparing `uasset_dump-0.0.2.tar` & `uasset_dump-0.0.3.tar`

### file list

```diff
@@ -1,16 +1,16 @@
--rw-r--r--   0        0        0      306 2023-03-31 11:18:04.579115 uasset_dump-0.0.2/CHANGELOG.md
--rw-r--r--   0        0        0      761 2023-03-31 11:22:24.297536 uasset_dump-0.0.2/LICENSE.md
--rw-r--r--   0        0        0      979 2023-04-06 07:14:26.706705 uasset_dump-0.0.2/README.md
--rw-r--r--   0        0        0      859 2023-03-31 11:21:05.979756 uasset_dump-0.0.2/bootloader/__init__.py
--rw-r--r--   0        0        0      859 2023-03-31 11:21:05.979756 uasset_dump-0.0.2/bootloader/ue/__init__.py
--rw-r--r--   0        0        0      859 2023-03-31 11:21:05.979756 uasset_dump-0.0.2/bootloader/ue/cli/__init__.py
--rwxr-xr-x   0        0        0     2445 2023-04-06 03:55:38.985331 uasset_dump-0.0.2/bootloader/ue/cli/uassetdump.py
--rw-r--r--   0        0        0      859 2023-03-31 11:21:05.975392 uasset_dump-0.0.2/bootloader/ue/constant/__init__.py
--rw-r--r--   0        0        0     4797 2023-04-05 15:31:25.693554 uasset_dump-0.0.2/bootloader/ue/constant/uasset.py
--rw-r--r--   0        0        0      859 2023-03-31 11:21:05.975392 uasset_dump-0.0.2/bootloader/ue/model/__init__.py
--rw-r--r--   0        0        0     2915 2023-04-05 14:09:09.558252 uasset_dump-0.0.2/bootloader/ue/model/uasset.py
--rw-r--r--   0        0        0      859 2023-03-31 11:21:05.979756 uasset_dump-0.0.2/bootloader/ue/utils/__init__.py
--rw-r--r--   0        0        0     3825 2023-04-06 08:02:08.777383 uasset_dump-0.0.2/bootloader/ue/utils/uasset_dump.py
--rw-r--r--   0        0        0     1024 2023-04-06 08:02:50.774525 uasset_dump-0.0.2/pyproject.toml
--rw-r--r--   0        0        0     2040 1970-01-01 00:00:00.000000 uasset_dump-0.0.2/setup.py
--rw-r--r--   0        0        0     2051 1970-01-01 00:00:00.000000 uasset_dump-0.0.2/PKG-INFO
+-rw-r--r--   0        0        0      306 2023-03-31 11:18:04.579115 uasset_dump-0.0.3/CHANGELOG.md
+-rw-r--r--   0        0        0      761 2023-03-31 11:22:24.297536 uasset_dump-0.0.3/LICENSE.md
+-rw-r--r--   0        0        0      989 2023-04-06 08:39:51.410335 uasset_dump-0.0.3/README.md
+-rw-r--r--   0        0        0      859 2023-03-31 11:21:05.979756 uasset_dump-0.0.3/bootloader/__init__.py
+-rw-r--r--   0        0        0      859 2023-03-31 11:21:05.979756 uasset_dump-0.0.3/bootloader/ue/__init__.py
+-rw-r--r--   0        0        0      859 2023-03-31 11:21:05.979756 uasset_dump-0.0.3/bootloader/ue/cli/__init__.py
+-rwxr-xr-x   0        0        0     2445 2023-04-06 03:55:38.985331 uasset_dump-0.0.3/bootloader/ue/cli/uassetdump.py
+-rw-r--r--   0        0        0      859 2023-03-31 11:21:05.975392 uasset_dump-0.0.3/bootloader/ue/constant/__init__.py
+-rw-r--r--   0        0        0     4797 2023-04-05 15:31:25.693554 uasset_dump-0.0.3/bootloader/ue/constant/uasset.py
+-rw-r--r--   0        0        0      859 2023-03-31 11:21:05.975392 uasset_dump-0.0.3/bootloader/ue/model/__init__.py
+-rw-r--r--   0        0        0     2915 2023-04-05 14:09:09.558252 uasset_dump-0.0.3/bootloader/ue/model/uasset.py
+-rw-r--r--   0        0        0      859 2023-03-31 11:21:05.979756 uasset_dump-0.0.3/bootloader/ue/utils/__init__.py
+-rw-r--r--   0        0        0     3917 2023-04-06 08:45:02.183427 uasset_dump-0.0.3/bootloader/ue/utils/uasset_dump.py
+-rw-r--r--   0        0        0     1024 2023-04-06 08:45:15.951532 uasset_dump-0.0.3/pyproject.toml
+-rw-r--r--   0        0        0     2050 1970-01-01 00:00:00.000000 uasset_dump-0.0.3/setup.py
+-rw-r--r--   0        0        0     2061 1970-01-01 00:00:00.000000 uasset_dump-0.0.3/PKG-INFO
```

### Comparing `uasset_dump-0.0.2/LICENSE.md` & `uasset_dump-0.0.3/LICENSE.md`

 * *Files identical despite different names*

### Comparing `uasset_dump-0.0.2/README.md` & `uasset_dump-0.0.3/README.md`

 * *Files 12% similar despite different names*

```diff
@@ -27,9 +27,9 @@
 poetry update
 ```
 
 
 ## Installation
 
 ```shell
-/Users/Shared/Epic\ Games/UE_5.1/Engine/Binaries/ThirdParty/Python3/Mac/bin/python3 -m pip install uasset-dump
+/Users/Shared/Epic\ Games/UE_5.1/Engine/Binaries/ThirdParty/Python3/Mac/bin/python3 -m pip install --upgrade uasset-dump
 ```
```

### Comparing `uasset_dump-0.0.2/bootloader/__init__.py` & `uasset_dump-0.0.3/bootloader/__init__.py`

 * *Files identical despite different names*

### Comparing `uasset_dump-0.0.2/bootloader/ue/__init__.py` & `uasset_dump-0.0.3/bootloader/ue/__init__.py`

 * *Files identical despite different names*

### Comparing `uasset_dump-0.0.2/bootloader/ue/cli/__init__.py` & `uasset_dump-0.0.3/bootloader/ue/cli/__init__.py`

 * *Files identical despite different names*

### Comparing `uasset_dump-0.0.2/bootloader/ue/cli/uassetdump.py` & `uasset_dump-0.0.3/bootloader/ue/cli/uassetdump.py`

 * *Files identical despite different names*

### Comparing `uasset_dump-0.0.2/bootloader/ue/constant/__init__.py` & `uasset_dump-0.0.3/bootloader/ue/constant/__init__.py`

 * *Files identical despite different names*

### Comparing `uasset_dump-0.0.2/bootloader/ue/constant/uasset.py` & `uasset_dump-0.0.3/bootloader/ue/constant/uasset.py`

 * *Files identical despite different names*

### Comparing `uasset_dump-0.0.2/bootloader/ue/model/__init__.py` & `uasset_dump-0.0.3/bootloader/ue/model/__init__.py`

 * *Files identical despite different names*

### Comparing `uasset_dump-0.0.2/bootloader/ue/model/uasset.py` & `uasset_dump-0.0.3/bootloader/ue/model/uasset.py`

 * *Files identical despite different names*

### Comparing `uasset_dump-0.0.2/bootloader/ue/utils/__init__.py` & `uasset_dump-0.0.3/bootloader/ue/utils/__init__.py`

 * *Files identical despite different names*

### Comparing `uasset_dump-0.0.2/bootloader/ue/utils/uasset_dump.py` & `uasset_dump-0.0.3/bootloader/ue/utils/uasset_dump.py`

 * *Files 5% similar despite different names*

```diff
@@ -9,26 +9,28 @@
 # BOOTLOADER MAKES NO REPRESENTATIONS OR WARRANTIES ABOUT THE
 # SUITABILITY OF THE SOFTWARE, EITHER EXPRESS OR IMPLIED, INCLUDING BUT
 # NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR
 # A PARTICULAR PURPOSE, OR NON-INFRINGEMENT.  BOOTLOADER SHALL NOT BE
 # LIABLE FOR ANY LOSSES OR DAMAGES SUFFERED BY LICENSEE AS A RESULT OF
 # USING, MODIFYING OR DISTRIBUTING THIS SOFTWARE OR ITS DERIVATIVES.
 
+import json
 from pathlib import Path
 
 import unreal
 
 from bootloader.ue.model.uasset import UAsset
 
 
 UNREAL_ENGINE_PROJECT_CONTENT_PATH = '/Game/'
 
 
 def dump_assets(root_path: str or Path) -> None:
-    find_assets(root_path)
+    assets = find_assets(root_path)
+    print(json.dumps([asset.to_json() for asset in assets], indent=2))
 
 
 def find_assets(content_path: str) -> list[UAsset]:
     """
     Return the list of the assets found recursively in the specified path.
```

### Comparing `uasset_dump-0.0.2/pyproject.toml` & `uasset_dump-0.0.3/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -13,15 +13,15 @@
 ]
 keywords = ["cli", "tool", "utility", "unreal", "engine", "asset", "inventory", "dump", "json"]
 license = "SEE LICENSE IN <LICENSE.md>"
 name = "uasset-dump"
 packages = [{ include = "bootloader" }]
 readme = "README.md"
 repository = "https://github.com/bootloader-studio/cli-uasset-dump"
-version = "0.0.2"
+version = "0.0.3"
 
 [tool.poetry.dependencies]
 perseus-core-library = "^1.19.2"
 python = "^3.9"
 
 [tool.poetry.scripts]
 ueprjver = 'bootloader.ue.cli.uassetdump:run'
```

### Comparing `uasset_dump-0.0.2/setup.py` & `uasset_dump-0.0.3/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -16,17 +16,17 @@
 ['perseus-core-library>=1.19.2,<2.0.0']
 
 entry_points = \
 {'console_scripts': ['ueprjver = bootloader.ue.cli.uassetdump:run']}
 
 setup_kwargs = {
     'name': 'uasset-dump',
-    'version': '0.0.2',
+    'version': '0.0.3',
     'description': 'Command-line Interface (CLI) responsible for returning the list of the assets of an Unreal Engine project into a JSON structure',
-    'long_description': '# Unreal Engine Assets Dump\n\nCommand-line Interface (CLI) responsible for returning the list of the assets of an Unreal Engine project into a JSON structure.\n\n## Development\n\n### Poetry\n\nUnreal Engine Assets Dump used Poetry to declare all its dependencies.  [Poetry](https://python-poetry.org/) is a python dependency management tool to manage dependencies, packages, and libraries in your python project.\n\nWe need to install Poetry with Unreal Engine Python:\n\n```shell\ncurl -sSL https://install.python-poetry.org | python3 -\n```\n\nThen, we need to create the Python virtual environment using Poetry:\n\n```shell\npoetry env use /Users/Shared/Epic\\ Games/UE_5.1/Engine/Binaries/ThirdParty/Python3/Mac/bin/python3\n```\n\nWe can enter this virtual environment and install all the required dependencies:\n\n```shell\npoetry shell\npoetry update\n```\n\n\n## Installation\n\n```shell\n/Users/Shared/Epic\\ Games/UE_5.1/Engine/Binaries/ThirdParty/Python3/Mac/bin/python3 -m pip install uasset-dump\n```',
+    'long_description': '# Unreal Engine Assets Dump\n\nCommand-line Interface (CLI) responsible for returning the list of the assets of an Unreal Engine project into a JSON structure.\n\n## Development\n\n### Poetry\n\nUnreal Engine Assets Dump used Poetry to declare all its dependencies.  [Poetry](https://python-poetry.org/) is a python dependency management tool to manage dependencies, packages, and libraries in your python project.\n\nWe need to install Poetry with Unreal Engine Python:\n\n```shell\ncurl -sSL https://install.python-poetry.org | python3 -\n```\n\nThen, we need to create the Python virtual environment using Poetry:\n\n```shell\npoetry env use /Users/Shared/Epic\\ Games/UE_5.1/Engine/Binaries/ThirdParty/Python3/Mac/bin/python3\n```\n\nWe can enter this virtual environment and install all the required dependencies:\n\n```shell\npoetry shell\npoetry update\n```\n\n\n## Installation\n\n```shell\n/Users/Shared/Epic\\ Games/UE_5.1/Engine/Binaries/ThirdParty/Python3/Mac/bin/python3 -m pip install --upgrade uasset-dump\n```',
     'author': 'Daniel CAUNE',
     'author_email': 'daniel@bootloader.studio',
     'maintainer': 'None',
     'maintainer_email': 'None',
     'url': 'https://github.com/bootloader-studio/cli-uasset-dump',
     'packages': packages,
     'package_data': package_data,
```

### Comparing `uasset_dump-0.0.2/PKG-INFO` & `uasset_dump-0.0.3/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: uasset-dump
-Version: 0.0.2
+Version: 0.0.3
 Summary: Command-line Interface (CLI) responsible for returning the list of the assets of an Unreal Engine project into a JSON structure
 Home-page: https://github.com/bootloader-studio/cli-uasset-dump
 License: SEE LICENSE IN <LICENSE.md>
 Keywords: cli,tool,utility,unreal,engine,asset,inventory,dump,json
 Author: Daniel CAUNE
 Author-email: daniel@bootloader.studio
 Requires-Python: >=3.9,<4.0
@@ -50,9 +50,9 @@
 poetry update
 ```
 
 
 ## Installation
 
 ```shell
-/Users/Shared/Epic\ Games/UE_5.1/Engine/Binaries/ThirdParty/Python3/Mac/bin/python3 -m pip install uasset-dump
+/Users/Shared/Epic\ Games/UE_5.1/Engine/Binaries/ThirdParty/Python3/Mac/bin/python3 -m pip install --upgrade uasset-dump
 ```
```

