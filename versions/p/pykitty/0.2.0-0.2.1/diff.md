# Comparing `tmp/pykitty-0.2.0.tar.gz` & `tmp/pykitty-0.2.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pykitty-0.2.0.tar", max compression
+gzip compressed data, was "pykitty-0.2.1.tar", max compression
```

## Comparing `pykitty-0.2.0.tar` & `pykitty-0.2.1.tar`

### file list

```diff
@@ -1,7 +1,7 @@
--rw-r--r--   0        0        0     2151 2023-04-06 19:00:49.233258 pykitty-0.2.0/README.md
--rw-r--r--   0        0        0       35 2023-03-27 19:20:21.848084 pykitty-0.2.0/pykitty/__init__.py
--rw-r--r--   0        0        0     2943 2023-04-06 19:00:01.649008 pykitty-0.2.0/pykitty/cli.py
--rw-r--r--   0        0        0     5543 2023-04-06 18:58:39.794979 pykitty-0.2.0/pykitty/client.py
--rw-r--r--   0        0        0     1806 2023-03-27 06:19:00.880708 pykitty-0.2.0/pykitty/kitty_parser.py
--rw-r--r--   0        0        0      504 2023-04-06 19:18:33.307163 pykitty-0.2.0/pyproject.toml
--rw-r--r--   0        0        0     2746 1970-01-01 00:00:00.000000 pykitty-0.2.0/PKG-INFO
+-rw-r--r--   0        0        0     2202 2023-04-07 10:29:06.231169 pykitty-0.2.1/README.md
+-rw-r--r--   0        0        0       21 2023-04-06 19:26:41.689694 pykitty-0.2.1/pykitty/__init__.py
+-rw-r--r--   0        0        0     2943 2023-04-06 19:00:01.649008 pykitty-0.2.1/pykitty/cli.py
+-rw-r--r--   0        0        0     6071 2023-04-07 10:29:06.231436 pykitty-0.2.1/pykitty/client.py
+-rw-r--r--   0        0        0     3016 2023-04-07 10:29:06.231718 pykitty-0.2.1/pykitty/kitty_parser.py
+-rw-r--r--   0        0        0      531 2023-04-07 10:29:06.231984 pykitty-0.2.1/pyproject.toml
+-rw-r--r--   0        0        0     2845 1970-01-01 00:00:00.000000 pykitty-0.2.1/PKG-INFO
```

### Comparing `pykitty-0.2.0/README.md` & `pykitty-0.2.1/README.md`

 * *Files 9% similar despite different names*

```diff
@@ -76,18 +76,23 @@
 api.add_expense(
     amount="10.00",
     description="Lunch",
     weight_mapping={"username1": 0.6, "username2": 0.4},
 )
 ```
 
+### Get Expenses
+```python
+api.get_expenses()
+```
+
 ## License
 
 This project is licensed under the MIT License.
 
 ## Next Steps (TODO)
 
 - [x] Parse Kitty URL parser to extract `kitty_id` 
-- [ ] Implement `get_expenses` method to retrieve all expenses.
+- [x] Implement `get_expenses` method to retrieve all expenses.
 - [ ] Add support for updating and deleting expenses.
 - [ ] Document CLI usage.
 - [ ] Support for Kittysplit in other languages.
```

### Comparing `pykitty-0.2.0/pykitty/cli.py` & `pykitty-0.2.1/pykitty/cli.py`

 * *Files identical despite different names*

### Comparing `pykitty-0.2.0/pykitty/client.py` & `pykitty-0.2.1/pykitty/client.py`

 * *Files 8% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 from datetime import datetime
-from typing import Dict, Union
+from typing import Dict, List, Union
 from urllib.parse import urlparse
 
 import requests
 
 from pykitty import kitty_parser
 
 
@@ -27,17 +27,25 @@
 ) -> Union[str, None]:
     response = session.get(base_url + path)
     csrf_parser = kitty_parser.CSRFHTMLParser()
     csrf_parser.feed(response.text)
     return csrf_parser.csrf_token
 
 
-def kitty_endpoint(path, method: str = "GET", csrf_protected: bool = False):
+def kitty_endpoint(
+    path,
+    method: str = "GET",
+    csrf_protected: bool = False,
+    user_needs_to_be_selected: bool = False,
+):
     def decorator(func):
         def wrapper(self, *args, **kwargs):
+            if user_needs_to_be_selected and self.selected_viewing_party_id is None:
+                raise ValueError("No user selected!")
+
             kwargs.update(
                 {
                     "path": path,
                     "method": method,
                 }
             )
             if csrf_protected:
@@ -100,15 +108,25 @@
         self._request(
             kwargs.pop("method"),
             kwargs.pop("path"),
             csrf_token=kwargs.pop("csrf_token"),
             data=form_data,
         )
 
-    @kitty_endpoint("/entries/new/expense/", method="POST", csrf_protected=True)
+    @kitty_endpoint("/entries/", user_needs_to_be_selected=True)
+    def get_expenses(self, **kwargs) -> List[dict]:
+        response = self._request(kwargs.pop("method"), kwargs.pop("path"))
+        return kitty_parser.parse_expenses(response.text)
+
+    @kitty_endpoint(
+        "/entries/new/expense/",
+        method="POST",
+        csrf_protected=True,
+        user_needs_to_be_selected=True,
+    )
     def add_expense(
         self,
         amount: str,
         description: str,
         entry_date: Union[str, None] = None,
         weight_mapping: Union[Dict[str, float], None] = None,
         **kwargs,
```

### Comparing `pykitty-0.2.0/PKG-INFO` & `pykitty-0.2.1/PKG-INFO`

 * *Files 3% similar despite different names*

```diff
@@ -1,20 +1,21 @@
 Metadata-Version: 2.1
 Name: pykitty
-Version: 0.2.0
+Version: 0.2.1
 Summary: The unofficial Kittysplit wrapper for Python.
 License: MIT
 Author: Lars Heinen
 Requires-Python: >=3.8,<4.0
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10
 Classifier: Programming Language :: Python :: 3.11
+Requires-Dist: beautifulsoup4 (>=4.12.1,<5.0.0)
 Requires-Dist: requests (>=2.28.2,<3.0.0)
 Requires-Dist: typer[all] (>=0.7.0,<0.8.0)
 Description-Content-Type: text/markdown
 
 # PyKitty
 
 This Python SDK allows you to interact with [KittySplit](https://kittysplit.de/) to manage expenses in a group. You can fetch a list of users, select a user and add expenses.
@@ -93,19 +94,24 @@
 api.add_expense(
     amount="10.00",
     description="Lunch",
     weight_mapping={"username1": 0.6, "username2": 0.4},
 )
 ```
 
+### Get Expenses
+```python
+api.get_expenses()
+```
+
 ## License
 
 This project is licensed under the MIT License.
 
 ## Next Steps (TODO)
 
 - [x] Parse Kitty URL parser to extract `kitty_id` 
-- [ ] Implement `get_expenses` method to retrieve all expenses.
+- [x] Implement `get_expenses` method to retrieve all expenses.
 - [ ] Add support for updating and deleting expenses.
 - [ ] Document CLI usage.
 - [ ] Support for Kittysplit in other languages.
```

