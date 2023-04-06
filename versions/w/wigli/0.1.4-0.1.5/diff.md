# Comparing `tmp/wigli-0.1.4.tar.gz` & `tmp/wigli-0.1.5.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "wigli-0.1.4.tar", max compression
+gzip compressed data, was "wigli-0.1.5.tar", max compression
```

## Comparing `wigli-0.1.4.tar` & `wigli-0.1.5.tar`

### file list

```diff
@@ -1,14 +1,14 @@
--rw-r--r--   0        0        0     1088 2023-03-31 09:19:15.327979 wigli-0.1.4/LICENSE
--rw-r--r--   0        0        0      677 2023-04-06 22:30:47.088256 wigli-0.1.4/pyproject.toml
--rw-r--r--   0        0        0    16107 2023-04-05 13:06:16.855737 wigli-0.1.4/README.md
--rw-r--r--   0        0        0     1166 2023-04-06 03:11:51.370104 wigli-0.1.4/src/wigli/__init__.py
--rw-r--r--   0        0        0      160 2023-04-06 14:11:02.314376 wigli-0.1.4/src/wigli/__main__.py
--rw-r--r--   0        0        0     7145 2023-04-06 22:25:44.286604 wigli-0.1.4/src/wigli/_wigli_argparser.py
--rw-r--r--   0        0        0    21703 2023-04-06 22:28:26.093790 wigli-0.1.4/src/wigli/_wigli_bots.py
--rw-r--r--   0        0        0     9971 2023-04-06 22:26:29.255478 wigli-0.1.4/src/wigli/_wigli_cli.py
--rw-r--r--   0        0        0     9493 2023-04-06 03:10:14.371028 wigli-0.1.4/src/wigli/_wigli_data.py
--rw-r--r--   0        0        0    17816 2023-04-06 03:10:16.688390 wigli-0.1.4/src/wigli/_wigli_plugins.py
--rw-r--r--   0        0        0     2939 2023-04-06 14:11:02.321091 wigli-0.1.4/src/wigli/_wigli_testutils.py
--rw-r--r--   0        0        0     6947 2023-04-06 03:10:13.591799 wigli-0.1.4/src/wigli/_wigli_tools.py
--rw-r--r--   0        0        0       48 2023-04-06 22:30:47.089278 wigli-0.1.4/src/wigli/_wigli_version.py
--rw-r--r--   0        0        0    16651 1970-01-01 00:00:00.000000 wigli-0.1.4/PKG-INFO
+-rw-r--r--   0        0        0     1088 2023-03-31 09:19:15.327979 wigli-0.1.5/LICENSE
+-rw-r--r--   0        0        0      677 2023-04-06 22:54:25.249875 wigli-0.1.5/pyproject.toml
+-rw-r--r--   0        0        0    16107 2023-04-05 13:06:16.855737 wigli-0.1.5/README.md
+-rw-r--r--   0        0        0     1166 2023-04-06 03:11:51.370104 wigli-0.1.5/src/wigli/__init__.py
+-rw-r--r--   0        0        0      160 2023-04-06 14:11:02.314376 wigli-0.1.5/src/wigli/__main__.py
+-rw-r--r--   0        0        0     7195 2023-04-06 22:54:08.419627 wigli-0.1.5/src/wigli/_wigli_argparser.py
+-rw-r--r--   0        0        0    21743 2023-04-06 22:52:50.212151 wigli-0.1.5/src/wigli/_wigli_bots.py
+-rw-r--r--   0        0        0    10054 2023-04-06 22:49:04.260547 wigli-0.1.5/src/wigli/_wigli_cli.py
+-rw-r--r--   0        0        0     9493 2023-04-06 03:10:14.371028 wigli-0.1.5/src/wigli/_wigli_data.py
+-rw-r--r--   0        0        0    17816 2023-04-06 03:10:16.688390 wigli-0.1.5/src/wigli/_wigli_plugins.py
+-rw-r--r--   0        0        0     2939 2023-04-06 14:11:02.321091 wigli-0.1.5/src/wigli/_wigli_testutils.py
+-rw-r--r--   0        0        0     6947 2023-04-06 03:10:13.591799 wigli-0.1.5/src/wigli/_wigli_tools.py
+-rw-r--r--   0        0        0       48 2023-04-06 22:54:25.249875 wigli-0.1.5/src/wigli/_wigli_version.py
+-rw-r--r--   0        0        0    16651 1970-01-01 00:00:00.000000 wigli-0.1.5/PKG-INFO
```

### Comparing `wigli-0.1.4/LICENSE` & `wigli-0.1.5/LICENSE`

 * *Files identical despite different names*

### Comparing `wigli-0.1.4/pyproject.toml` & `wigli-0.1.5/pyproject.toml`

 * *Files 14% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 [build-system]
 requires = ["poetry-core"]
 build-backend = "poetry.core.masonry.api"
 
 [tool.poetry]
 name = "wigli"
-version = "0.1.4"
+version = "0.1.5"
 description = "Powerful ChatGPT wrapper adds extensible botswarms for web search, coding, and more."
 authors = ["Douglas Graham <doug.n.graham@gmail.com>"]
 license = "MIT"
 readme = "README.md"
 
 [tool.poetry.dependencies]
 python = "^3.7"
```

### Comparing `wigli-0.1.4/README.md` & `wigli-0.1.5/README.md`

 * *Files identical despite different names*

### Comparing `wigli-0.1.4/src/wigli/__init__.py` & `wigli-0.1.5/src/wigli/__init__.py`

 * *Files identical despite different names*

### Comparing `wigli-0.1.4/src/wigli/_wigli_argparser.py` & `wigli-0.1.5/src/wigli/_wigli_argparser.py`

 * *Files 1% similar despite different names*

```diff
@@ -81,14 +81,34 @@
             default="",
             help="the prompt to submit",
         )
     else:
         parser.set_defaults(prompt="")
 
     parser.add_argument(
+        "-v",
+        "--verbosity",
+        action="count",
+        default=0,
+        help=f"verbosity with which to print logs, cumulative up to {MAX_VERBOSITY}",
+    )
+    parser.add_argument(
+        "-V",
+        "--version",
+        action="store_true",
+        help=f"print version number",
+    )
+    parser.add_argument(
+        "-K",
+        "--set-api-key",
+        metavar="API_KEY",
+        type=str,
+        help="Create a .env file with your OpenAI API Key to enable ChatGPT access",
+    )
+    parser.add_argument(
         "-l",
         "--list",
         action="store_true",
         help="list past conversations",
     )
     # parser.add_argument(
     #     "-n",
@@ -213,39 +233,20 @@
     #     help="prompt will be transcribed from audio",
     # )
     parser.add_argument(
         "--doctest",
         action="store_true",
         help=f"interpret prompt as a Python function and invoke the headless DocTest bot",
     )
-    parser.add_argument(
-        "-v",
-        "--verbosity",
-        action="count",
-        default=0,
-        help=f"verbosity with which to print logs, cumulative up to {MAX_VERBOSITY}",
-    )
-    parser.add_argument(
-        "-V",
-        "--version",
-        action="store_true",
-        help=f"print version number",
-    )
-    parser.add_argument(
-        "-L",
-        "--list-installed-plugins",
-        action="store_true",
-        help=f"list installed plugins",
-    )
-    parser.add_argument(
-        "--list-plugins",
-        action="store_true",
-        help=f"list available plugins on PyPI",
-    )
-    parser.add_argument(
-        "-K",
-        "--set-api-key",
-        type=str,
-        help="Create a .env file with your OpenAI API Key to enable ChatGPT access",
-    )
+    # parser.add_argument(
+    #     "-L",
+    #     "--list-installed-plugins",
+    #     action="store_true",
+    #     help=f"list installed plugins",
+    # )
+    # parser.add_argument(
+    #     "--list-plugins",
+    #     action="store_true",
+    #     help=f"list available plugins on PyPI",
+    # )
 
     return parser.parse_args(argv)
```

### Comparing `wigli-0.1.4/src/wigli/_wigli_bots.py` & `wigli-0.1.5/src/wigli/_wigli_bots.py`

 * *Files 0% similar despite different names*

```diff
@@ -2,14 +2,15 @@
 
 import openai
 
 from copy import deepcopy
 from dotenv import load_dotenv
 from json import load
 from os import getenv
+from os.path import join
 from slugify import slugify
 from time import time
 from typing import Any, Callable, Iterable, List, TYPE_CHECKING
 
 from wigli._wigli_tools import (
     clamp,
     count_tokens,
@@ -239,15 +240,15 @@
         self.touchstamp = (
             self.birthstamp
             if touchstamp is None
             else touchstamp
         )
 
         if openai.api_key == "":
-            load_dotenv(dotenv_path=self.wiglidata.data_dir)
+            load_dotenv(dotenv_path=join(self.wiglidata.data_dir, ".env"))
             load_dotenv()
             openai.api_key = getenv("OPENAI_API_KEY")
 
         if messages is not None:
             self.Inject(messages)
         if prompt is not None:
             self.Inject(prompt)
```

### Comparing `wigli-0.1.4/src/wigli/_wigli_cli.py` & `wigli-0.1.5/src/wigli/_wigli_cli.py`

 * *Files 0% similar despite different names*

```diff
@@ -119,14 +119,15 @@
             with open(join(self.data.data_dir, ".env"), "w") as f:
                 f.write(
                     f"""\
 # Once you add your API key below, make sure to not share it with anyone! The API key should remain private.
 OPENAI_API_KEY={self.args.set_api_key}
 """
                 )
+            self.log(f"Saved API key at {join(self.data.data_dir, '.env')}", v=0)
             return
         
         # if self.args.list_installed_plugins:
         #     discovered_plugins = entry_points(group='wigli._wigli_plugins')
         #     for discovered_plugin in discovered_plugins:
         #         print(f"    {discovered_plugin}")
         #     return
```

### Comparing `wigli-0.1.4/src/wigli/_wigli_data.py` & `wigli-0.1.5/src/wigli/_wigli_data.py`

 * *Files identical despite different names*

### Comparing `wigli-0.1.4/src/wigli/_wigli_plugins.py` & `wigli-0.1.5/src/wigli/_wigli_plugins.py`

 * *Files identical despite different names*

### Comparing `wigli-0.1.4/src/wigli/_wigli_testutils.py` & `wigli-0.1.5/src/wigli/_wigli_testutils.py`

 * *Files identical despite different names*

### Comparing `wigli-0.1.4/src/wigli/_wigli_tools.py` & `wigli-0.1.5/src/wigli/_wigli_tools.py`

 * *Files identical despite different names*

### Comparing `wigli-0.1.4/PKG-INFO` & `wigli-0.1.5/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: wigli
-Version: 0.1.4
+Version: 0.1.5
 Summary: Powerful ChatGPT wrapper adds extensible botswarms for web search, coding, and more.
 License: MIT
 Author: Douglas Graham
 Author-email: doug.n.graham@gmail.com
 Requires-Python: >=3.7,<4.0
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Programming Language :: Python :: 3
```

