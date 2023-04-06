# Comparing `tmp/wigli-0.1.8.tar.gz` & `tmp/wigli-0.1.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "wigli-0.1.8.tar", max compression
+gzip compressed data, was "wigli-0.1.9.tar", max compression
```

## Comparing `wigli-0.1.8.tar` & `wigli-0.1.9.tar`

### file list

```diff
@@ -1,14 +1,14 @@
--rw-r--r--   0        0        0     1088 2023-03-31 09:19:15.327979 wigli-0.1.8/LICENSE
--rw-r--r--   0        0        0      677 2023-04-06 23:15:50.311896 wigli-0.1.8/pyproject.toml
--rw-r--r--   0        0        0    16107 2023-04-05 13:06:16.855737 wigli-0.1.8/README.md
--rw-r--r--   0        0        0     1166 2023-04-06 03:11:51.370104 wigli-0.1.8/src/wigli/__init__.py
--rw-r--r--   0        0        0      160 2023-04-06 14:11:02.314376 wigli-0.1.8/src/wigli/__main__.py
--rw-r--r--   0        0        0     7195 2023-04-06 22:54:08.419627 wigli-0.1.8/src/wigli/_wigli_argparser.py
--rw-r--r--   0        0        0    21793 2023-04-06 23:15:39.439303 wigli-0.1.8/src/wigli/_wigli_bots.py
--rw-r--r--   0        0        0    10039 2023-04-06 23:05:45.868597 wigli-0.1.8/src/wigli/_wigli_cli.py
--rw-r--r--   0        0        0     9493 2023-04-06 23:07:05.928616 wigli-0.1.8/src/wigli/_wigli_data.py
--rw-r--r--   0        0        0    17816 2023-04-06 03:10:16.688390 wigli-0.1.8/src/wigli/_wigli_plugins.py
--rw-r--r--   0        0        0     2939 2023-04-06 14:11:02.321091 wigli-0.1.8/src/wigli/_wigli_testutils.py
--rw-r--r--   0        0        0     6947 2023-04-06 03:10:13.591799 wigli-0.1.8/src/wigli/_wigli_tools.py
--rw-r--r--   0        0        0       48 2023-04-06 23:15:50.313200 wigli-0.1.8/src/wigli/_wigli_version.py
--rw-r--r--   0        0        0    16651 1970-01-01 00:00:00.000000 wigli-0.1.8/PKG-INFO
+-rw-r--r--   0        0        0     1088 2023-03-31 09:19:15.327979 wigli-0.1.9/LICENSE
+-rw-r--r--   0        0        0      677 2023-04-06 23:22:54.158930 wigli-0.1.9/pyproject.toml
+-rw-r--r--   0        0        0    16107 2023-04-05 13:06:16.855737 wigli-0.1.9/README.md
+-rw-r--r--   0        0        0     1166 2023-04-06 03:11:51.370104 wigli-0.1.9/src/wigli/__init__.py
+-rw-r--r--   0        0        0      160 2023-04-06 14:11:02.314376 wigli-0.1.9/src/wigli/__main__.py
+-rw-r--r--   0        0        0     7195 2023-04-06 22:54:08.419627 wigli-0.1.9/src/wigli/_wigli_argparser.py
+-rw-r--r--   0        0        0    22056 2023-04-06 23:22:26.358715 wigli-0.1.9/src/wigli/_wigli_bots.py
+-rw-r--r--   0        0        0    10039 2023-04-06 23:05:45.868597 wigli-0.1.9/src/wigli/_wigli_cli.py
+-rw-r--r--   0        0        0     9493 2023-04-06 23:07:05.928616 wigli-0.1.9/src/wigli/_wigli_data.py
+-rw-r--r--   0        0        0    17816 2023-04-06 03:10:16.688390 wigli-0.1.9/src/wigli/_wigli_plugins.py
+-rw-r--r--   0        0        0     2939 2023-04-06 14:11:02.321091 wigli-0.1.9/src/wigli/_wigli_testutils.py
+-rw-r--r--   0        0        0     6947 2023-04-06 03:10:13.591799 wigli-0.1.9/src/wigli/_wigli_tools.py
+-rw-r--r--   0        0        0       48 2023-04-06 23:22:54.158930 wigli-0.1.9/src/wigli/_wigli_version.py
+-rw-r--r--   0        0        0    16651 1970-01-01 00:00:00.000000 wigli-0.1.9/PKG-INFO
```

### Comparing `wigli-0.1.8/LICENSE` & `wigli-0.1.9/LICENSE`

 * *Files identical despite different names*

### Comparing `wigli-0.1.8/pyproject.toml` & `wigli-0.1.9/pyproject.toml`

 * *Files 14% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 [build-system]
 requires = ["poetry-core"]
 build-backend = "poetry.core.masonry.api"
 
 [tool.poetry]
 name = "wigli"
-version = "0.1.8"
+version = "0.1.9"
 description = "Powerful ChatGPT wrapper adds extensible botswarms for web search, coding, and more."
 authors = ["Douglas Graham <doug.n.graham@gmail.com>"]
 license = "MIT"
 readme = "README.md"
 
 [tool.poetry.dependencies]
 python = "^3.7"
```

### Comparing `wigli-0.1.8/README.md` & `wigli-0.1.9/README.md`

 * *Files identical despite different names*

### Comparing `wigli-0.1.8/src/wigli/__init__.py` & `wigli-0.1.9/src/wigli/__init__.py`

 * *Files identical despite different names*

### Comparing `wigli-0.1.8/src/wigli/_wigli_argparser.py` & `wigli-0.1.9/src/wigli/_wigli_argparser.py`

 * *Files identical despite different names*

### Comparing `wigli-0.1.8/src/wigli/_wigli_bots.py` & `wigli-0.1.9/src/wigli/_wigli_bots.py`

 * *Files 1% similar despite different names*

```diff
@@ -240,19 +240,24 @@
         self.touchstamp = (
             self.birthstamp
             if touchstamp is None
             else touchstamp
         )
 
         if openai.api_key is None:
+            self.log("No openai.api_key found")
+            self.log("Attempting load_dotenv()")
             load_dotenv()
             openai.api_key = getenv("OPENAI_API_KEY")
 
         if openai.api_key is None:
-            load_dotenv(dotenv_path=join(self.data.data_dir, ".env"))
+            self.log("No openai.api_key found")
+            dotenv_path = join(self.data.data_dir, ".env")
+            self.log(f"Attempting load_dotenv(dotenv_path={dotenv_path})")
+            load_dotenv(dotenv_path=dotenv_path)
             openai.api_key = getenv("OPENAI_API_KEY")
 
         if messages is not None:
             self.Inject(messages)
         if prompt is not None:
             self.Inject(prompt)
```

### Comparing `wigli-0.1.8/src/wigli/_wigli_cli.py` & `wigli-0.1.9/src/wigli/_wigli_cli.py`

 * *Files identical despite different names*

### Comparing `wigli-0.1.8/src/wigli/_wigli_data.py` & `wigli-0.1.9/src/wigli/_wigli_data.py`

 * *Files identical despite different names*

### Comparing `wigli-0.1.8/src/wigli/_wigli_plugins.py` & `wigli-0.1.9/src/wigli/_wigli_plugins.py`

 * *Files identical despite different names*

### Comparing `wigli-0.1.8/src/wigli/_wigli_testutils.py` & `wigli-0.1.9/src/wigli/_wigli_testutils.py`

 * *Files identical despite different names*

### Comparing `wigli-0.1.8/src/wigli/_wigli_tools.py` & `wigli-0.1.9/src/wigli/_wigli_tools.py`

 * *Files identical despite different names*

### Comparing `wigli-0.1.8/PKG-INFO` & `wigli-0.1.9/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: wigli
-Version: 0.1.8
+Version: 0.1.9
 Summary: Powerful ChatGPT wrapper adds extensible botswarms for web search, coding, and more.
 License: MIT
 Author: Douglas Graham
 Author-email: doug.n.graham@gmail.com
 Requires-Python: >=3.7,<4.0
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Programming Language :: Python :: 3
```

