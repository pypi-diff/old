# Comparing `tmp/pyexhange_r3ne-0.1.1.tar.gz` & `tmp/pyexhange_r3ne-0.1.2.tar.gz`

## Comparing `pyexhange_r3ne-0.1.1.tar` & `pyexhange_r3ne-0.1.2.tar`

### file list

```diff
@@ -1,21 +1,21 @@
--rw-r--r--   0        0        0       66 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.1/.gitattributes
--rwxr-xr-x   0        0        0       32 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.1/Run.bat
--rw-r--r--   0        0        0       39 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.1/config.json.example
--rw-r--r--   0        0        0     2077 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.1/pyexhange.py
--rw-r--r--   0        0        0      382 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.1/requirements.txt
--rw-r--r--   0        0        0      447 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.1/test.py
--rwxr-xr-x   0        0        0       71 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.1/upload.bat
--rw-r--r--   0        0        0        5 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.1/data/placeholder
--rw-r--r--   0        0        0      900 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.1/modules/price.py
--rw-r--r--   0        0        0     1505 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.1/modules/send.py
--rw-r--r--   0        0        0     2803 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.1/modules/trade.py
--rw-r--r--   0        0        0      934 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.1/modules/wallet.py
--rw-r--r--   0        0        0      800 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.1/modules/utils/coingecko.py
--rw-r--r--   0        0        0     2558 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.1/modules/utils/data.py
--rw-r--r--   0        0        0      891 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.1/modules/utils/exchanges.py
--rw-r--r--   0        0        0     1213 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.1/modules/utils/finhub.py
--rw-r--r--   0        0        0     3102 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.1/.gitignore
--rw-r--r--   0        0        0     1069 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.1/LICENCE.rst
--rw-r--r--   0        0        0      709 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.1/README.md
--rw-r--r--   0        0        0      693 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.1/pyproject.toml
--rw-r--r--   0        0        0     1284 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.1/PKG-INFO
+-rw-r--r--   0        0        0       66 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.2/.gitattributes
+-rwxr-xr-x   0        0        0       32 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.2/Run.bat
+-rw-r--r--   0        0        0       39 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.2/config.json.example
+-rw-r--r--   0        0        0     2118 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.2/pyexhange.py
+-rw-r--r--   0        0        0      382 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.2/requirements.txt
+-rw-r--r--   0        0        0      447 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.2/test.py
+-rwxr-xr-x   0        0        0       71 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.2/upload.bat
+-rw-r--r--   0        0        0        5 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.2/data/placeholder
+-rw-r--r--   0        0        0      900 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.2/modules/price.py
+-rw-r--r--   0        0        0     1505 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.2/modules/send.py
+-rw-r--r--   0        0        0     2803 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.2/modules/trade.py
+-rw-r--r--   0        0        0      934 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.2/modules/wallet.py
+-rw-r--r--   0        0        0      800 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.2/modules/utils/coingecko.py
+-rw-r--r--   0        0        0     2558 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.2/modules/utils/data.py
+-rw-r--r--   0        0        0      891 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.2/modules/utils/exchanges.py
+-rw-r--r--   0        0        0     1213 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.2/modules/utils/finhub.py
+-rw-r--r--   0        0        0     3102 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.2/.gitignore
+-rw-r--r--   0        0        0     1069 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.2/LICENCE.rst
+-rw-r--r--   0        0        0      709 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.2/README.md
+-rw-r--r--   0        0        0      693 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.2/pyproject.toml
+-rw-r--r--   0        0        0     1284 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.2/PKG-INFO
```

### Comparing `pyexhange_r3ne-0.1.1/pyexhange.py` & `pyexhange_r3ne-0.1.2/pyexhange.py`

 * *Files 7% similar despite different names*

```diff
@@ -16,15 +16,15 @@
 try:
     data = jsonBase("./data")
 except FileNotFoundError:
     print("JSON file not found.")
 
 commands = {}
 
-for filename in os.listdir("modules"):
+for filename in os.listdir(os.path.join(os.path.dirname(__file__), "modules")):
     if filename.endswith(".py"):
         module_name = filename[:-3] # remove .py extension
         module = importlib.import_module("modules." + module_name)
         if hasattr(module, module_name + "_function"):
             commands[module_name] = getattr(module, module_name + "_function")
```

### Comparing `pyexhange_r3ne-0.1.1/modules/price.py` & `pyexhange_r3ne-0.1.2/modules/price.py`

 * *Files identical despite different names*

### Comparing `pyexhange_r3ne-0.1.1/modules/send.py` & `pyexhange_r3ne-0.1.2/modules/send.py`

 * *Files identical despite different names*

### Comparing `pyexhange_r3ne-0.1.1/modules/trade.py` & `pyexhange_r3ne-0.1.2/modules/trade.py`

 * *Files identical despite different names*

### Comparing `pyexhange_r3ne-0.1.1/modules/wallet.py` & `pyexhange_r3ne-0.1.2/modules/wallet.py`

 * *Files identical despite different names*

### Comparing `pyexhange_r3ne-0.1.1/modules/utils/coingecko.py` & `pyexhange_r3ne-0.1.2/modules/utils/coingecko.py`

 * *Files identical despite different names*

### Comparing `pyexhange_r3ne-0.1.1/modules/utils/data.py` & `pyexhange_r3ne-0.1.2/modules/utils/data.py`

 * *Files identical despite different names*

### Comparing `pyexhange_r3ne-0.1.1/modules/utils/exchanges.py` & `pyexhange_r3ne-0.1.2/modules/utils/exchanges.py`

 * *Files identical despite different names*

### Comparing `pyexhange_r3ne-0.1.1/modules/utils/finhub.py` & `pyexhange_r3ne-0.1.2/modules/utils/finhub.py`

 * *Files identical despite different names*

### Comparing `pyexhange_r3ne-0.1.1/.gitignore` & `pyexhange_r3ne-0.1.2/.gitignore`

 * *Files identical despite different names*

### Comparing `pyexhange_r3ne-0.1.1/LICENCE.rst` & `pyexhange_r3ne-0.1.2/LICENCE.rst`

 * *Files identical despite different names*

### Comparing `pyexhange_r3ne-0.1.1/README.md` & `pyexhange_r3ne-0.1.2/README.md`

 * *Files identical despite different names*

### Comparing `pyexhange_r3ne-0.1.1/pyproject.toml` & `pyexhange_r3ne-0.1.2/pyproject.toml`

 * *Files 2% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 [build-system]
 requires = ["hatchling", "finnhub-python"]
 build-backend = "hatchling.build"
 
 [project]
 name = "pyexhange_r3ne"
-version = "0.1.1"
+version = "0.1.2"
 authors = [
   { name="R3ne.net", email="mail@r3ne.net" },
 ]
 description = "Python code that allows users to create and manage their own virtual wallets to get the trading experiense with out real money."
 readme = "README.md"
 requires-python = ">=3.7"
 classifiers = [
```

### Comparing `pyexhange_r3ne-0.1.1/PKG-INFO` & `pyexhange_r3ne-0.1.2/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pyexhange_r3ne
-Version: 0.1.1
+Version: 0.1.2
 Summary: Python code that allows users to create and manage their own virtual wallets to get the trading experiense with out real money.
 Project-URL: Homepage, https://github.com/JAAKKQ/pyexhange
 Project-URL: Bug Tracker, https://github.com/JAAKKQ/pyexhange/issues
 Author-email: "R3ne.net" <mail@r3ne.net>
 License-File: LICENCE.rst
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
```

