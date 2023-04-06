# Comparing `tmp/datawrapper-0.4.7.tar.gz` & `tmp/datawrapper-0.4.8.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "datawrapper-0.4.7.tar", max compression
+gzip compressed data, was "datawrapper-0.4.8.tar", max compression
```

## Comparing `datawrapper-0.4.7.tar` & `datawrapper-0.4.8.tar`

### file list

```diff
@@ -1,8 +1,7 @@
--rw-r--r--   0        0        0     1093 2022-02-10 01:24:00.282810 datawrapper-0.4.7/LICENSE
--rw-r--r--   0        0        0    10084 2022-02-10 01:24:00.282810 datawrapper-0.4.7/README.md
--rw-r--r--   0        0        0      540 2022-02-10 01:24:00.282810 datawrapper-0.4.7/datawrapper/__init__.py
--rw-r--r--   0        0        0    21859 2022-02-10 01:24:00.282810 datawrapper-0.4.7/datawrapper/__main__.py
--rw-r--r--   0        0        0      362 2022-02-10 01:24:00.282810 datawrapper-0.4.7/datawrapper/example.py
--rw-r--r--   0        0        0     1990 2022-02-10 01:24:00.286810 datawrapper-0.4.7/pyproject.toml
--rw-r--r--   0        0        0    11459 2022-02-10 01:25:17.821341 datawrapper-0.4.7/setup.py
--rw-r--r--   0        0        0    11160 2022-02-10 01:25:17.822237 datawrapper-0.4.7/PKG-INFO
+-rw-r--r--   0        0        0     1093 2023-04-06 18:22:11.305264 datawrapper-0.4.8/LICENSE
+-rw-r--r--   0        0        0    10131 2023-04-06 18:22:11.309264 datawrapper-0.4.8/README.md
+-rw-r--r--   0        0        0      540 2023-04-06 18:22:11.309264 datawrapper-0.4.8/datawrapper/__init__.py
+-rw-r--r--   0        0        0    22985 2023-04-06 18:22:11.309264 datawrapper-0.4.8/datawrapper/__main__.py
+-rw-r--r--   0        0        0      362 2023-04-06 18:22:11.309264 datawrapper-0.4.8/datawrapper/example.py
+-rw-r--r--   0        0        0     3538 2023-04-06 18:22:11.313264 datawrapper-0.4.8/pyproject.toml
+-rw-r--r--   0        0        0    11309 1970-01-01 00:00:00.000000 datawrapper-0.4.8/PKG-INFO
```

### Comparing `datawrapper-0.4.7/LICENSE` & `datawrapper-0.4.8/LICENSE`

 * *Files identical despite different names*

### Comparing `datawrapper-0.4.7/README.md` & `datawrapper-0.4.8/README.md`

 * *Files 0% similar despite different names*

```diff
@@ -9,14 +9,15 @@
 [![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/chekos/datawrapper/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)
 
 [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
 [![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)
 [![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/chekos/datawrapper/blob/master/.pre-commit-config.yaml)
 [![Semantic Versions](https://img.shields.io/badge/%F0%9F%9A%80-semantic%20versions-informational.svg)](https://github.com/chekos/datawrapper/releases)
 [![License](https://img.shields.io/github/license/chekos/datawrapper)](https://github.com/chekos/datawrapper/blob/master/LICENSE)
+![Coverage Report](assets/images/coverage.svg)
 [![badge](https://img.shields.io/badge/try%20it%20on-mybinder.org-F5A252.svg?logo=data:image/png;base64,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)](https://mybinder.org/v2/gh/chekos/Datawrapper/master?urlpath=lab%2Ftree%2Fexamples%2Fdatawrapper.ipynb)
 
 A light-weight python wrapper for the Datawrapper API (v3). While it is not developed by Datawrapper officially, you can use it with your API credentials from datawrapper.de
 
 </div>
 
 ## 🚀 Features
```

### Comparing `datawrapper-0.4.7/datawrapper/__init__.py` & `datawrapper-0.4.8/datawrapper/__init__.py`

 * *Files identical despite different names*

### Comparing `datawrapper-0.4.7/datawrapper/__main__.py` & `datawrapper-0.4.8/datawrapper/__main__.py`

 * *Files 11% similar despite different names*

```diff
@@ -10,22 +10,25 @@
         dw = Datawrapper(access_token = <YOUR_ACCESS_TOKEN_HERE>)
 
         dw.account_info()
 """
 from typing import Any, Dict, Iterable, List, Optional, Union
 
 import json
+import logging
 import os
 from pathlib import Path
 
 import IPython
 import pandas as pd
 import requests as r
 from IPython.display import HTML, Image
 
+logger = logging.getLogger(__name__)
+
 
 class Datawrapper:
     """Handles connecting with Datawrapper's API.
 
     Handles access to your Datawrapper's account, create, delete and move charts, tables or maps.
     Will attempt to read environment variable DATAWRAPPER_ACCESS_TOKEN by default.
 
@@ -63,15 +66,15 @@
         """
         account_info_response = r.get(
             url=self._BASE_URL + "/v3/me", headers=self._auth_header
         )
         if account_info_response.status_code == 200:
             return account_info_response.json()
         else:
-            print(
+            logger.error(
                 "Couldn't find account. Make sure your credentials (access_code) are correct."
             )
             return None
 
     def add_data(self, chart_id: str, data: pd.DataFrame) -> r.Response:
         """Add data to a specified chart.
 
@@ -166,26 +169,26 @@
         )
 
         if (
             chart_type == "d3-maps-choropleth"
             or chart_type == "d3-maps-symbols"
             or chart_type == "locator-map"
         ):
-            print(
+            logger.debug(
                 "\nNOTE: Maps need a valid basemap, set in properties -> visualize"
             )
-            print(
+            logger.debug(
                 "Full list of valid maps can be retrieved with\n\ncurl --request GET --url https://api.datawrapper.de/plugin/basemap\n"
             )
 
         if new_chart_response.status_code <= 201:
             chart_info = new_chart_response.json()
-            print(f"New chart {chart_info['type']} created!")
+            logger.debug(f"New chart {chart_info['type']} created!")
         else:
-            print(
+            logger.error(
                 f"Chart could not be created, check your authorization credentials (access token){', and that the folder_id is valid (i.e exists, and your account has access to it)' if folder_id else ''}"
             )
 
         if data is not None:
             self.add_data(chart_id=chart_info["id"], data=data)
 
         return chart_info
@@ -193,14 +196,19 @@
     def update_description(
         self,
         chart_id: str,
         source_name: str = "",
         source_url: str = "",
         intro: str = "",
         byline: str = "",
+        aria_description: str = "",
+        number_prepend: str = "",
+        number_append: str = "",
+        number_format: str = "-",
+        number_divisor: int = 0,
     ) -> Union[Any, None]:
         """Update a chart's description.
 
         Parameters
         ----------
         chart_id : str
             ID of chart, table or map.
@@ -208,45 +216,58 @@
             Source of data, by default ""
         source_url : str, optional
             URL of source of data, by default ""
         intro : str, optional
             Introduction of your chart, table or map, by default ""
         byline : str, optional
             Who made this?, by default ""
+        aria_description : str, optional
+            Alt text description
+        number_prepend : str, optional
+            Something to put before the number
+        number_append : str, optional
+            Something to after before the number
+        number_format : str, optional
+            The format number
+        number_divisor : str, optional
+            A multiplier or divisor for the numbers
         """
 
         _header = self._auth_header
         _header["content-type"] = "application/json"
         _data = {
             "metadata": {
                 "describe": {
                     "source-name": source_name,
                     "source-url": source_url,
                     "intro": intro,
                     "byline": byline,
+                    "aria-description": aria_description,
+                    "number-prepend": number_prepend,
+                    "number-append": number_append,
+                    "number-format": number_format,
+                    "number-divisor": number_divisor,
                 }
             }
         }
         update_description_response = r.patch(
             url=self._CHARTS_URL + f"/{chart_id}",
             headers=_header,
             data=json.dumps(_data),
         )
         if update_description_response.status_code == 200:
-            print("Chart updated!")
+            logger.debug("Chart updated!")
         else:
-            print(
+            logger.error(
                 "Error. Status code: ", update_description_response.status_code
             )
-            print("Couldn't update chart.")
+            logger.error("Couldn't update chart.")
         return None
 
-    def publish_chart(
-        self, chart_id: str, display: bool = True
-    ) -> Union[Any, None]:
+    def publish_chart(self, chart_id: str, display: bool = True) -> Union[Any, None]:
         """Publishes a chart, table or map.
 
         Parameters
         ----------
         chart_id : str
             ID of chart, table or map.
         display : bool, optional
@@ -254,27 +275,27 @@
         """
 
         publish_chart_response = r.post(
             url=f"{self._PUBLISH_URL}/{chart_id}/publish",
             headers=self._auth_header,
         )
         if publish_chart_response.status_code <= 201:
-            # print(f"Chart published at {publish_chart_info[]}")
+            publish_chart_info = publish_chart_response.json()
+            logger.debug(f"Chart published at {publish_chart_info['url']}")
             if display:
-                publish_chart_info = publish_chart_response.json()
                 iframe_code = publish_chart_info["data"]["metadata"]["publish"][
                     "embed-codes"
                 ]["embed-method-iframe"]
                 # iframe_width = publish_chart_info['data']['metadata']['publish']['embed-width']
                 # iframe_height = publish_chart_info['data']['metadata']['publish']['embed-height']
                 return HTML(iframe_code)
             else:
                 return None
         else:
-            print("Chart couldn't be published at this time.")
+            logger.error("Chart couldn't be published at this time.")
             return None
 
     def chart_properties(
         self, chart_id: str
     ) -> Union[Dict[Any, Any], None, Any, Iterable[Any]]:
         """Retrieve information of a specific chart, table or map.
 
@@ -291,15 +312,15 @@
         chart_properties_response = r.get(
             url=self._CHARTS_URL + f"/{chart_id}",
             headers=self._auth_header,
         )
         if chart_properties_response.status_code == 200:
             return chart_properties_response.json()
         else:
-            print(
+            logger.error(
                 "Make sure you have the right id and authorization credentials (access_token)."
             )
             return None
 
     def update_metadata(
         self, chart_id: str, properties: Dict[Any, Any]
     ) -> Union[Any, None]:
@@ -319,24 +340,22 @@
 
         update_properties_response = r.patch(
             url=self._CHARTS_URL + f"/{chart_id}",
             headers=_header,
             data=json.dumps(_data),
         )
         if update_properties_response.status_code == 200:
-            print("Chart's metadata updated!")
+            logger.debug("Chart's metadata updated!")
             # return update_properties_response.json()
         else:
-            print(
-                "Error. Status code: ", update_properties_response.status_code
-            )
+            logger.error("Error. Status code: ", update_properties_response.status_code)
             x = update_properties_response.text
             y = json.loads(x)
-            print("Message: ", y["message"])
-            print("Chart could not be updated.")
+            logger.debug("Message: ", y["message"])
+            logger.debug("Chart could not be updated.")
         return None
 
     def update_chart(
         self,
         chart_id: str,
         title: str = "",
         theme: str = "",
@@ -383,18 +402,18 @@
 
         update_chart_response = r.patch(
             url=self._CHARTS_URL + f"/{chart_id}",
             headers=_header,
             data=json.dumps(_query),
         )
         if update_chart_response.status_code == 200:
-            print(f"Chart with id {chart_id} updated!")
+            logger.debug(f"Chart with id {chart_id} updated!")
             return self.publish_chart(chart_id)
         else:
-            print("Chart could not be updated at the time.")
+            logger.debug("Chart could not be updated at the time.")
             return None
 
     def display_chart(self, chart_id: str) -> IPython.display.HTML:
         """Displays a datawrapper chart.
 
         Parameters
         ----------
@@ -431,31 +450,27 @@
             iframe embed code.
         """
         _chart_properties = self.chart_properties(chart_id)
 
         if responsive:
             iframe_code = _chart_properties["metadata"]["publish"][  # type: ignore
                 "embed-codes"
-            ][
-                "embed-method-responsive"
-            ]
+            ]["embed-method-responsive"]
         else:
             iframe_code = _chart_properties["metadata"]["publish"][  # type: ignore
                 "embed-codes"
-            ][
-                "embed-method-iframe"
-            ]
+            ]["embed-method-iframe"]
         return iframe_code
 
     def export_chart(
         self,
         chart_id: str,
         unit: str = "px",
         mode: str = "rgb",
-        width: int = 100,
+        width: int = 400,
         plain: bool = False,
         zoom: int = 2,
         scale: int = 1,
         border_width: int = 20,
         output: str = "png",
         filepath: str = "./image.png",
         display: bool = False,
@@ -483,15 +498,15 @@
         output : str, optional
             One of png, pdf, or svg, by default "png"
         filepath : str, optional
             Name/filepath to save output in, by default "./image.png"
         display : bool, optional
             Whether to display the exported image as output in the notebook cell, by default False
 
-        Returns
+        Returns None
         -------
         IPython.display.Image
             If display is True, it returns an Image.
         """
         _export_url = f"{self._CHARTS_URL}/{chart_id}/export/{output}"
         _filepath = Path(filepath)
         _filepath = _filepath.with_suffix(f".{output}")
@@ -516,22 +531,27 @@
 
         if export_chart_response.status_code == 200:
             with open(_filepath, "wb") as response:
                 response.write(export_chart_response.content)
             if display:
                 return Image(_filepath)
             else:
-                print(f"File exported at {_filepath}")
+                logger.debug(f"File exported at {_filepath}")
         elif export_chart_response.status_code == 403:
-            print("You don't have access to the requested code.")
+            msg = "You don't have access to the requested chart."
+            logger.error(msg)
+            raise Exception(msg)
         elif export_chart_response.status_code == 401:
-            print("You couldn't be authenticated.")
-        else:
-            print("Couldn't export at this time.")
-        return None
+            msg = "You couldn't be authenticated."
+            logger.error(msg)
+            raise Exception(msg)
+        else:
+            msg = "Chart could not be exported."
+            logger.error(msg)
+            raise Exception(msg)
 
     def get_folders(self) -> Union[Dict[Any, Any], None, Any]:
         """Get a list of folders in your Datawrapper account.
 
         Returns
         -------
         dict
@@ -541,15 +561,15 @@
             url=self._FOLDERS_URL,
             headers=self._auth_header,
         )
 
         if get_folders_response.status_code == 200:
             return get_folders_response.json()
         else:
-            print(
+            logger.error(
                 "Couldn't retrieve folders in account. Make sure you have the rigth authorization credentials (access token)."
             )
             return None
 
     def move_chart(self, chart_id: str, folder_id: str) -> Union[Any, None]:
         """Moves a chart, table, or map to a specified folder.
 
@@ -569,17 +589,17 @@
         move_chart_response = r.patch(
             url=self._CHARTS_URL + f"/{chart_id}",
             headers=_header,
             data=json.dumps(_data),
         )
 
         if move_chart_response.status_code == 200:
-            print(f"Chart moved to folder {folder_id}")
+            logger.debug(f"Chart moved to folder {folder_id}")
         else:
-            print("Chart could not be moved at the moment.")
+            logger.error("Chart could not be moved at the moment.")
         return None
 
     def delete_chart(self, chart_id: str) -> r.Response.content:  # type: ignore
         """Deletes a specified chart, table or map.
 
 
         Parameters
@@ -595,15 +615,15 @@
 
         delete_chart_response = r.delete(
             url=self._CHARTS_URL + f"/{chart_id}", headers=self._auth_header
         )
         if delete_chart_response.content:
             return delete_chart_response.content
         else:
-            print(f"Successfully deleted chart with id {chart_id}")
+            logger.debug(f"Successfully deleted chart with id {chart_id}")
             return None
 
     def get_charts(
         self,
         user_id: str = "",
         published: str = "true",
         search: str = "",
@@ -657,9 +677,9 @@
             _query["limit"] = str(limit)
 
         get_charts_response = r.get(url=_url, headers=_header, params=_query)
 
         if get_charts_response.status_code == 200:
             return get_charts_response.json()["list"]  # type: ignore
         else:
-            print("Could not retrieve charts at this moment.")
+            logger.error("Could not retrieve charts at this moment.")
             return None
```

### Comparing `datawrapper-0.4.7/setup.py` & `datawrapper-0.4.8/PKG-INFO`

 * *Files 17% similar despite different names*

```diff
@@ -1,41 +1,286 @@
-# -*- coding: utf-8 -*-
-from setuptools import setup
+Metadata-Version: 2.1
+Name: datawrapper
+Version: 0.4.8
+Summary: A light-weight python wrapper for the Datawrapper API (v3). While it is not developed by Datawrapper officially, you can use it with your API credentials from datawrapper.de
+Home-page: https://github.com/chekos/datawrapper
+License: MIT
+Author: chekos
+Author-email: chekos@tacosdedatos.com
+Requires-Python: >=3.8.0,<3.11
+Classifier: Development Status :: 3 - Alpha
+Classifier: Intended Audience :: Developers
+Classifier: License :: OSI Approved :: MIT License
+Classifier: Operating System :: OS Independent
+Classifier: Programming Language :: Python :: 3
+Classifier: Programming Language :: Python :: 3.8
+Classifier: Programming Language :: Python :: 3.9
+Classifier: Programming Language :: Python :: 3.10
+Classifier: Topic :: Software Development :: Libraries :: Python Modules
+Requires-Dist: importlib_metadata (>=1.6,<4.0) ; python_version < "3.8"
+Requires-Dist: ipython (>=8.12.0,<9.0.0)
+Requires-Dist: pandas (>=1.5,<2.0.0)
+Requires-Dist: requests (>=2.28.2,<3.0.0)
+Requires-Dist: rich (>=13.3.3,<14.0.0)
+Project-URL: Repository, https://github.com/chekos/datawrapper
+Description-Content-Type: text/markdown
 
-packages = \
-['datawrapper']
+# datawrapper
 
-package_data = \
-{'': ['*']}
+<div align="center">
 
-install_requires = \
-['ipython>=7.22.0,<8.0.0',
- 'pandas>=1.3.0,<1.4.0',
- 'requests>=2.25.1,<3.0.0',
- 'rich>=9.8.2,<11.0.0']
-
-extras_require = \
-{':python_version < "3.8"': ['importlib_metadata>=1.6,<4.0']}
-
-entry_points = \
-{'console_scripts': ['datawrapper = datawrapper.__main__:app']}
-
-setup_kwargs = {
-    'name': 'datawrapper',
-    'version': '0.4.7',
-    'description': 'A light-weight python wrapper for the Datawrapper API (v3). While it is not developed by Datawrapper officially, you can use it with your API credentials from datawrapper.de',
-    'long_description': '# datawrapper\n\n<div align="center">\n\n[![PyPI Version](https://img.shields.io/pypi/v/datawrapper.svg)](https://pypi.python.org/pypi/datawrapper)\n[![Monthly downloads](https://img.shields.io/pypi/dm/datawrapper)](https://img.shields.io/pypi/dm/datawrappe)\n[![Build status](https://github.com/chekos/datawrapper/workflows/build/badge.svg?branch=master&event=push)](https://github.com/chekos/datawrapper/actions?query=workflow%3Abuild)\n[![Python Version](https://img.shields.io/pypi/pyversions/datawrapper.svg)](https://pypi.org/project/datawrapper/)\n[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/chekos/datawrapper/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)\n\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)\n[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/chekos/datawrapper/blob/master/.pre-commit-config.yaml)\n[![Semantic Versions](https://img.shields.io/badge/%F0%9F%9A%80-semantic%20versions-informational.svg)](https://github.com/chekos/datawrapper/releases)\n[![License](https://img.shields.io/github/license/chekos/datawrapper)](https://github.com/chekos/datawrapper/blob/master/LICENSE)\n[![badge](https://img.shields.io/badge/try%20it%20on-mybinder.org-F5A252.svg?logo=data:image/png;base64,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)](https://mybinder.org/v2/gh/chekos/Datawrapper/master?urlpath=lab%2Ftree%2Fexamples%2Fdatawrapper.ipynb)\n\nA light-weight python wrapper for the Datawrapper API (v3). While it is not developed by Datawrapper officially, you can use it with your API credentials from datawrapper.de\n\n</div>\n\n## 🚀 Features\n\n* Retrieve your account information (including folders).\n* Add data to charts, tables or maps.\n* Create charts, tables or maps - and add data from a `pandas.DataFrame` in one call!\n* Update chart descriptions.\n* Publish charts, tables or maps.\n* Retrieve chart properties, update its metadata, and other information.\n* Display a chart (as output of notebook cell - it gets weird because interactivity ¯\\\\_(ツ)_/¯ )\n* Retrieve a chart, table or map\'s iframe code to embed.\n* Export chart as png (still working on the svg and pdf parts).\n* Move charts across folders and organizations.\n* Delete charts.\n* Get a list of all your charts.\n\n## Installation\n\n```bash\npip install -U datawrapper\n```\n\nor install with `Poetry`\n\n```bash\npoetry add datawrapper\n```\n\n### Makefile usage\n\n[`Makefile`](https://github.com/chekos/datawrapper/blob/master/Makefile) contains many functions for fast assembling and convenient work.\n\n<details>\n<summary>1. Download Poetry</summary>\n<p>\n\n```bash\nmake download-poetry\n```\n\n</p>\n</details>\n\n<details>\n<summary>2. Install all dependencies and pre-commit hooks</summary>\n<p>\n\n```bash\nmake install\n```\n\nIf you do not want to install pre-commit hooks, run the command with the NO_PRE_COMMIT flag:\n\n```bash\nmake install NO_PRE_COMMIT=1\n```\n\n</p>\n</details>\n\n<details>\n<summary>3. Check the security of your code</summary>\n<p>\n\n```bash\nmake check-safety\n```\n\nThis command launches a `Poetry` and `Pip` integrity check as well as identifies security issues with `Safety` and `Bandit`. By default, the build will not crash if any of the items fail. But you can set `STRICT=1` for the entire build, or you can configure strictness for each item separately.\n\n```bash\nmake check-safety STRICT=1\n```\n\nor only for `safety`:\n\n```bash\nmake check-safety SAFETY_STRICT=1\n```\n\nmultiple\n\n```bash\nmake check-safety PIP_STRICT=1 SAFETY_STRICT=1\n```\n\n> List of flags for `check-safety` (can be set to `1` or `0`): `STRICT`, `POETRY_STRICT`, `PIP_STRICT`, `SAFETY_STRICT`, `BANDIT_STRICT`.\n\n</p>\n</details>\n\n<details>\n<summary>4. Check the codestyle</summary>\n<p>\n\nThe command is similar to `check-safety` but to check the code style, obviously. It uses `Black`, `Darglint`, `Isort`, and `Mypy` inside.\n\n```bash\nmake check-style\n```\n\nIt may also contain the `STRICT` flag.\n\n```bash\nmake check-style STRICT=1\n```\n\n> List of flags for `check-style` (can be set to `1` or `0`): `STRICT`, `BLACK_STRICT`, `DARGLINT_STRICT`, `ISORT_STRICT`, `MYPY_STRICT`.\n\n</p>\n</details>\n\n<details>\n<summary>5. Run all the codestyle formaters</summary>\n<p>\n\nCodestyle uses `pre-commit` hooks, so ensure you\'ve run `make install` before.\n\n```bash\nmake codestyle\n```\n\n</p>\n</details>\n\n<details>\n<summary>6. Run tests</summary>\n<p>\n\n```bash\nmake test\n```\n\n</p>\n</details>\n\n<details>\n<summary>7. Run all the linters</summary>\n<p>\n\n```bash\nmake lint\n```\n\nthe same as:\n\n```bash\nmake test && make check-safety && make check-style\n```\n\n> List of flags for `lint` (can be set to `1` or `0`): `STRICT`, `POETRY_STRICT`, `PIP_STRICT`, `SAFETY_STRICT`, `BANDIT_STRICT`, `BLACK_STRICT`, `DARGLINT_STRICT`, `ISORT_STRICT`, `MYPY_STRICT`.\n\n</p>\n</details>\n\n<details>\n<summary>8. Build docker</summary>\n<p>\n\n```bash\nmake docker\n```\n\nwhich is equivalent to:\n\n```bash\nmake docker VERSION=latest\n```\n\nMore information [here](https://github.com/chekos/datawrapper/tree/master/docker).\n\n</p>\n</details>\n\n<details>\n<summary>9. Cleanup docker</summary>\n<p>\n\n```bash\nmake clean_docker\n```\n\nor to remove all build\n\n```bash\nmake clean\n```\n\nMore information [here](https://github.com/chekos/datawrapper/tree/master/docker).\n\n</p>\n</details>\n\n## 📈 Releases\n\nYou can see the list of available releases on the [GitHub Releases](https://github.com/chekos/datawrapper/releases) page.\n\nWe follow [Semantic Versions](https://semver.org/) specification.\n\nWe use [`Release Drafter`](https://github.com/marketplace/actions/release-drafter). As pull requests are merged, a draft release is kept up-to-date listing the changes, ready to publish when you’re ready. With the categories option, you can categorize pull requests in release notes using labels.\n\nFor Pull Request this labels are configured, by default:\n\n|               **Label**               |  **Title in Releases**  |\n| :-----------------------------------: | :---------------------: |\n|       `enhancement`, `feature`        |       🚀 Features       |\n| `bug`, `refactoring`, `bugfix`, `fix` | 🔧 Fixes & Refactoring  |\n|       `build`, `ci`, `testing`        | 📦 Build System & CI/CD |\n|              `breaking`               |   💥 Breaking Changes   |\n|            `documentation`            |    📝 Documentation     |\n|            `dependencies`             | ⬆️ Dependencies updates |\n\nYou can update it in [`release-drafter.yml`](https://github.com/chekos/datawrapper/blob/master/.github/release-drafter.yml).\n\nGitHub creates the `bug`, `enhancement`, and `documentation` labels for you. Dependabot creates the `dependencies` label. Create the remaining labels on the Issues tab of your GitHub repository, when you need them.\n\n## 🛡 License\n\n[![License](https://img.shields.io/github/license/chekos/datawrapper)](https://github.com/chekos/datawrapper/blob/master/LICENSE)\n\nThis project is licensed under the terms of the `MIT` license. See [LICENSE](https://github.com/chekos/datawrapper/blob/master/LICENSE) for more details.\n\n## 📃 Citation\n\n```\n@misc{datawrapper,\n  author = {chekos},\n  title = {A light-weight python wrapper for the Datawrapper API (v3). While it is not developed by Datawrapper officially, you can use it with your API credentials from datawrapper.de},\n  year = {2021},\n  publisher = {GitHub},\n  journal = {GitHub repository},\n  howpublished = {\\url{https://github.com/chekos/datawrapper}}\n}\n```\n\n## Credits\n\nThis project was generated with [`python-package-template`](https://github.com/TezRomacH/python-package-template).\n',
-    'author': 'chekos',
-    'author_email': 'chekos@tacosdedatos.com',
-    'maintainer': None,
-    'maintainer_email': None,
-    'url': 'https://github.com/chekos/datawrapper',
-    'packages': packages,
-    'package_data': package_data,
-    'install_requires': install_requires,
-    'extras_require': extras_require,
-    'entry_points': entry_points,
-    'python_requires': '>=3.8.0,<3.9',
+[![PyPI Version](https://img.shields.io/pypi/v/datawrapper.svg)](https://pypi.python.org/pypi/datawrapper)
+[![Monthly downloads](https://img.shields.io/pypi/dm/datawrapper)](https://img.shields.io/pypi/dm/datawrappe)
+[![Build status](https://github.com/chekos/datawrapper/workflows/build/badge.svg?branch=master&event=push)](https://github.com/chekos/datawrapper/actions?query=workflow%3Abuild)
+[![Python Version](https://img.shields.io/pypi/pyversions/datawrapper.svg)](https://pypi.org/project/datawrapper/)
+[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/chekos/datawrapper/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)
+
+[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
+[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)
+[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/chekos/datawrapper/blob/master/.pre-commit-config.yaml)
+[![Semantic Versions](https://img.shields.io/badge/%F0%9F%9A%80-semantic%20versions-informational.svg)](https://github.com/chekos/datawrapper/releases)
+[![License](https://img.shields.io/github/license/chekos/datawrapper)](https://github.com/chekos/datawrapper/blob/master/LICENSE)
+![Coverage Report](assets/images/coverage.svg)
+[![badge](https://img.shields.io/badge/try%20it%20on-mybinder.org-F5A252.svg?logo=data:image/png;base64,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)](https://mybinder.org/v2/gh/chekos/Datawrapper/master?urlpath=lab%2Ftree%2Fexamples%2Fdatawrapper.ipynb)
+
+A light-weight python wrapper for the Datawrapper API (v3). While it is not developed by Datawrapper officially, you can use it with your API credentials from datawrapper.de
+
+</div>
+
+## 🚀 Features
+
+* Retrieve your account information (including folders).
+* Add data to charts, tables or maps.
+* Create charts, tables or maps - and add data from a `pandas.DataFrame` in one call!
+* Update chart descriptions.
+* Publish charts, tables or maps.
+* Retrieve chart properties, update its metadata, and other information.
+* Display a chart (as output of notebook cell - it gets weird because interactivity ¯\\_(ツ)_/¯ )
+* Retrieve a chart, table or map's iframe code to embed.
+* Export chart as png (still working on the svg and pdf parts).
+* Move charts across folders and organizations.
+* Delete charts.
+* Get a list of all your charts.
+
+## Installation
+
+```bash
+pip install -U datawrapper
+```
+
+or install with `Poetry`
+
+```bash
+poetry add datawrapper
+```
+
+### Makefile usage
+
+[`Makefile`](https://github.com/chekos/datawrapper/blob/master/Makefile) contains many functions for fast assembling and convenient work.
+
+<details>
+<summary>1. Download Poetry</summary>
+<p>
+
+```bash
+make download-poetry
+```
+
+</p>
+</details>
+
+<details>
+<summary>2. Install all dependencies and pre-commit hooks</summary>
+<p>
+
+```bash
+make install
+```
+
+If you do not want to install pre-commit hooks, run the command with the NO_PRE_COMMIT flag:
+
+```bash
+make install NO_PRE_COMMIT=1
+```
+
+</p>
+</details>
+
+<details>
+<summary>3. Check the security of your code</summary>
+<p>
+
+```bash
+make check-safety
+```
+
+This command launches a `Poetry` and `Pip` integrity check as well as identifies security issues with `Safety` and `Bandit`. By default, the build will not crash if any of the items fail. But you can set `STRICT=1` for the entire build, or you can configure strictness for each item separately.
+
+```bash
+make check-safety STRICT=1
+```
+
+or only for `safety`:
+
+```bash
+make check-safety SAFETY_STRICT=1
+```
+
+multiple
+
+```bash
+make check-safety PIP_STRICT=1 SAFETY_STRICT=1
+```
+
+> List of flags for `check-safety` (can be set to `1` or `0`): `STRICT`, `POETRY_STRICT`, `PIP_STRICT`, `SAFETY_STRICT`, `BANDIT_STRICT`.
+
+</p>
+</details>
+
+<details>
+<summary>4. Check the codestyle</summary>
+<p>
+
+The command is similar to `check-safety` but to check the code style, obviously. It uses `Black`, `Darglint`, `Isort`, and `Mypy` inside.
+
+```bash
+make check-style
+```
+
+It may also contain the `STRICT` flag.
+
+```bash
+make check-style STRICT=1
+```
+
+> List of flags for `check-style` (can be set to `1` or `0`): `STRICT`, `BLACK_STRICT`, `DARGLINT_STRICT`, `ISORT_STRICT`, `MYPY_STRICT`.
+
+</p>
+</details>
+
+<details>
+<summary>5. Run all the codestyle formaters</summary>
+<p>
+
+Codestyle uses `pre-commit` hooks, so ensure you've run `make install` before.
+
+```bash
+make codestyle
+```
+
+</p>
+</details>
+
+<details>
+<summary>6. Run tests</summary>
+<p>
+
+```bash
+make test
+```
+
+</p>
+</details>
+
+<details>
+<summary>7. Run all the linters</summary>
+<p>
+
+```bash
+make lint
+```
+
+the same as:
+
+```bash
+make test && make check-safety && make check-style
+```
+
+> List of flags for `lint` (can be set to `1` or `0`): `STRICT`, `POETRY_STRICT`, `PIP_STRICT`, `SAFETY_STRICT`, `BANDIT_STRICT`, `BLACK_STRICT`, `DARGLINT_STRICT`, `ISORT_STRICT`, `MYPY_STRICT`.
+
+</p>
+</details>
+
+<details>
+<summary>8. Build docker</summary>
+<p>
+
+```bash
+make docker
+```
+
+which is equivalent to:
+
+```bash
+make docker VERSION=latest
+```
+
+More information [here](https://github.com/chekos/datawrapper/tree/master/docker).
+
+</p>
+</details>
+
+<details>
+<summary>9. Cleanup docker</summary>
+<p>
+
+```bash
+make clean_docker
+```
+
+or to remove all build
+
+```bash
+make clean
+```
+
+More information [here](https://github.com/chekos/datawrapper/tree/master/docker).
+
+</p>
+</details>
+
+## 📈 Releases
+
+You can see the list of available releases on the [GitHub Releases](https://github.com/chekos/datawrapper/releases) page.
+
+We follow [Semantic Versions](https://semver.org/) specification.
+
+We use [`Release Drafter`](https://github.com/marketplace/actions/release-drafter). As pull requests are merged, a draft release is kept up-to-date listing the changes, ready to publish when you’re ready. With the categories option, you can categorize pull requests in release notes using labels.
+
+For Pull Request this labels are configured, by default:
+
+|               **Label**               |  **Title in Releases**  |
+| :-----------------------------------: | :---------------------: |
+|       `enhancement`, `feature`        |       🚀 Features       |
+| `bug`, `refactoring`, `bugfix`, `fix` | 🔧 Fixes & Refactoring  |
+|       `build`, `ci`, `testing`        | 📦 Build System & CI/CD |
+|              `breaking`               |   💥 Breaking Changes   |
+|            `documentation`            |    📝 Documentation     |
+|            `dependencies`             | ⬆️ Dependencies updates |
+
+You can update it in [`release-drafter.yml`](https://github.com/chekos/datawrapper/blob/master/.github/release-drafter.yml).
+
+GitHub creates the `bug`, `enhancement`, and `documentation` labels for you. Dependabot creates the `dependencies` label. Create the remaining labels on the Issues tab of your GitHub repository, when you need them.
+
+## 🛡 License
+
+[![License](https://img.shields.io/github/license/chekos/datawrapper)](https://github.com/chekos/datawrapper/blob/master/LICENSE)
+
+This project is licensed under the terms of the `MIT` license. See [LICENSE](https://github.com/chekos/datawrapper/blob/master/LICENSE) for more details.
+
+## 📃 Citation
+
+```
+@misc{datawrapper,
+  author = {chekos},
+  title = {A light-weight python wrapper for the Datawrapper API (v3). While it is not developed by Datawrapper officially, you can use it with your API credentials from datawrapper.de},
+  year = {2021},
+  publisher = {GitHub},
+  journal = {GitHub repository},
+  howpublished = {\url{https://github.com/chekos/datawrapper}}
 }
+```
+
+## Credits
 
+This project was generated with [`python-package-template`](https://github.com/TezRomacH/python-package-template).
 
-setup(**setup_kwargs)
```

