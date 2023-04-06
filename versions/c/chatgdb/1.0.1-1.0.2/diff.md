# Comparing `tmp/chatgdb-1.0.1.tar.gz` & `tmp/chatgdb-1.0.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "chatgdb-1.0.1.tar", max compression
+gzip compressed data, was "chatgdb-1.0.2.tar", max compression
```

## Comparing `chatgdb-1.0.1.tar` & `chatgdb-1.0.2.tar`

### file list

```diff
@@ -1,7 +1,7 @@
--rw-r--r--   0        0        0     1063 2023-03-31 21:54:58.877640 chatgdb-1.0.1/LICENSE
--rw-r--r--   0        0        0     1479 2023-04-05 04:54:04.756944 chatgdb-1.0.1/README.md
--rw-r--r--   0        0        0        0 2023-04-01 22:30:13.298149 chatgdb-1.0.1/chatgdb/__init__.py
--rw-r--r--   0        0        0      748 2023-04-05 01:57:44.066776 chatgdb-1.0.1/chatgdb/cli.py
--rw-r--r--   0        0        0     5325 2023-04-05 01:57:48.120098 chatgdb-1.0.1/chatgdb/core.py
--rw-r--r--   0        0        0      567 2023-04-05 04:54:12.540256 chatgdb-1.0.1/pyproject.toml
--rw-r--r--   0        0        0     2445 1970-01-01 00:00:00.000000 chatgdb-1.0.1/PKG-INFO
+-rw-r--r--   0        0        0     1063 2023-03-31 21:54:58.877640 chatgdb-1.0.2/LICENSE
+-rw-r--r--   0        0        0     1989 2023-04-06 18:48:13.916239 chatgdb-1.0.2/README.md
+-rw-r--r--   0        0        0        0 2023-04-01 22:30:13.298149 chatgdb-1.0.2/chatgdb/__init__.py
+-rw-r--r--   0        0        0      748 2023-04-05 01:57:44.066776 chatgdb-1.0.2/chatgdb/cli.py
+-rw-r--r--   0        0        0     5325 2023-04-06 18:48:11.972972 chatgdb-1.0.2/chatgdb/core.py
+-rw-r--r--   0        0        0      567 2023-04-06 18:48:51.188387 chatgdb-1.0.2/pyproject.toml
+-rw-r--r--   0        0        0     2955 1970-01-01 00:00:00.000000 chatgdb-1.0.2/PKG-INFO
```

### Comparing `chatgdb-1.0.1/LICENSE` & `chatgdb-1.0.2/LICENSE`

 * *Files identical despite different names*

### Comparing `chatgdb-1.0.1/chatgdb/cli.py` & `chatgdb-1.0.2/chatgdb/cli.py`

 * *Files identical despite different names*

### Comparing `chatgdb-1.0.1/chatgdb/core.py` & `chatgdb-1.0.2/chatgdb/core.py`

 * *Files identical despite different names*

### Comparing `chatgdb-1.0.1/pyproject.toml` & `chatgdb-1.0.2/pyproject.toml`

 * *Files 19% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "ChatGDB"
-version = "1.0.1"
+version = "1.0.2"
 authors = ["Pranay Gosar <gosarpranay@gmail.com>"]
 description = "Harness the power of ChatGPT directly inside the GDB debugger!"
 readme = "README.md"
 license = "MIT"
 repository = "https://github.com/pgosar/chatgdb"
 keywords = ["gdb", "debugger", "chatgpt"]
```

### Comparing `chatgdb-1.0.1/PKG-INFO` & `chatgdb-1.0.2/PKG-INFO`

 * *Files 23% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: chatgdb
-Version: 1.0.1
+Version: 1.0.2
 Summary: Harness the power of ChatGPT directly inside the GDB debugger!
 Home-page: https://github.com/pgosar/chatgdb
 License: MIT
 Keywords: gdb,debugger,chatgpt
 Author: Pranay Gosar
 Author-email: gosarpranay@gmail.com
 Requires-Python: >=3.3,<4.0
@@ -20,32 +20,39 @@
 Classifier: Programming Language :: Python :: 3.11
 Project-URL: Bug Tracker, https://github.com/pgosar/chatgdb/issues
 Project-URL: Repository, https://github.com/pgosar/chatgdb
 Description-Content-Type: text/markdown
 
 # ChatGDB
 Harness the power of ChatGPT inside the GDB debugger!
-![image](https://user-images.githubusercontent.com/55164602/229982475-9a9724fe-91d0-48a4-aa3b-85bfc38edafa.png)
-
+![Image](https://lh5.googleusercontent.com/xZMLwWWxavqYjC3fyCIZJ0m-s-f-XEoiOeWGbxRrw3dWoukUoWzJJ4iiBkVO2Vtiyr4K6o0WkTs7B40TapeBPIYwgVRVhDXGVjB4tFYoKH3_nK847nYXl3pISB6dEP6Wp_o0uPlfJOjCrLspm0_VNw)
 
 ### Installation instructions
+First, make sure you install [pip](https://pip.pypa.io/en/stable/installation/)
+
 To install, run the command ```pip3 install chatgdb```. It will create an executable called
 ```chatgdb``` that you will have to use to set your api key. To do that, run the command
 
 ```chatgdb -k <API KEY> ```
 
 Without the API key, you won't be able to make requests to OpenAI. The API key is stored in
 text in the same directory as the installed script, which is currently in your python site packages
-folder
+folder along with the main script. You can easily find this location by running the following in your terminal:
+
+``` python -m site --user-site```
 
 Optionally, you can also download the compressed files in the releases page to get the scripts directly.
 If you do this, you will need to instead invoke the cli tool with 
 
 ```python path/to/cli.py -k <API KEY>```.
 
 
 ### How to use
-While inside gdb, source the core.py file with ```source /path/to/core.py```. By default, this is pythonXXX/site-packages/chatgdb/core.py.  Then you can use the command chat appended by your query, for example ```chat list all breakpoints that I created```. There is also a command called ```explain``` that you can use with no arguments to explain the previously run command, and optionally, with a query to just ask GPT a question. Run chat help to print out a short tutorial on how to use the tool.
+I first recommend editing your ```$HOME/.gdbinit``` to source the main script automatically on startup. Run the following command:
+
+```echo "source $(python -m site --user-site)/chatgdb/core.py" > $HOME/.gdbinit```
+
+While inside GDB the command chat appended by your query, for example ```chat list all breakpoints that I created```. There is also a command called ```explain``` that you can use with no arguments to explain the previously run command, and optionally, with a query to just ask GPT a question. For example, running ```explain``` directly after running ```break 7``` would prompt the tool to explain how breakpoints work. Running ```explain how input formatting works in gdb``` would prompt it to explain input formatting (see the image at the top).
+
+Run chat help to print out a short tutorial on how to use the tool.
 
-You can also edit your ```$HOME/.gdbinit``` and source the file automatically on startup with
-```source /path/to/core.py```.
```

