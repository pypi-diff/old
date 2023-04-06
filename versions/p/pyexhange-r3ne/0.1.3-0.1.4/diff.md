# Comparing `tmp/pyexhange_r3ne-0.1.3.tar.gz` & `tmp/pyexhange_r3ne-0.1.4.tar.gz`

## Comparing `pyexhange_r3ne-0.1.3.tar` & `pyexhange_r3ne-0.1.4.tar`

### file list

```diff
@@ -1,21 +1,21 @@
--rw-r--r--   0        0        0       66 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.3/.gitattributes
--rwxr-xr-x   0        0        0       32 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.3/Run.bat
--rw-r--r--   0        0        0       39 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.3/config.json.example
--rw-r--r--   0        0        0     2118 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.3/pyexhange.py
--rw-r--r--   0        0        0      382 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.3/requirements.txt
--rw-r--r--   0        0        0      447 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.3/test.py
--rwxr-xr-x   0        0        0       71 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.3/upload.bat
--rw-r--r--   0        0        0        5 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.3/data/placeholder
--rw-r--r--   0        0        0      935 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.3/modules/price.py
--rw-r--r--   0        0        0     1505 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.3/modules/send.py
--rw-r--r--   0        0        0     2803 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.3/modules/trade.py
--rw-r--r--   0        0        0      934 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.3/modules/wallet.py
--rw-r--r--   0        0        0      800 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.3/modules/utils/coingecko.py
--rw-r--r--   0        0        0     2558 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.3/modules/utils/data.py
--rw-r--r--   0        0        0      891 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.3/modules/utils/exchanges.py
--rw-r--r--   0        0        0     1213 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.3/modules/utils/finhub.py
--rw-r--r--   0        0        0     3102 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.3/.gitignore
--rw-r--r--   0        0        0     1069 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.3/LICENCE.rst
--rw-r--r--   0        0        0      709 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.3/README.md
--rw-r--r--   0        0        0      693 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.3/pyproject.toml
--rw-r--r--   0        0        0     1284 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.3/PKG-INFO
+-rw-r--r--   0        0        0       66 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.4/.gitattributes
+-rwxr-xr-x   0        0        0       32 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.4/Run.bat
+-rw-r--r--   0        0        0       39 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.4/config.json.example
+-rw-r--r--   0        0        0     2094 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.4/pyexhange.py
+-rw-r--r--   0        0        0      382 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.4/requirements.txt
+-rw-r--r--   0        0        0      447 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.4/test.py
+-rwxr-xr-x   0        0        0       71 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.4/upload.bat
+-rw-r--r--   0        0        0        5 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.4/data/placeholder
+-rw-r--r--   0        0        0     1105 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.4/modules/price.py
+-rw-r--r--   0        0        0     1505 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.4/modules/send.py
+-rw-r--r--   0        0        0     2803 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.4/modules/trade.py
+-rw-r--r--   0        0        0      934 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.4/modules/wallet.py
+-rw-r--r--   0        0        0      800 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.4/modules/utils/coingecko.py
+-rw-r--r--   0        0        0     2558 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.4/modules/utils/data.py
+-rw-r--r--   0        0        0      891 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.4/modules/utils/exchanges.py
+-rw-r--r--   0        0        0     1213 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.4/modules/utils/finhub.py
+-rw-r--r--   0        0        0     3102 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.4/.gitignore
+-rw-r--r--   0        0        0     1069 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.4/LICENCE.rst
+-rw-r--r--   0        0        0      709 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.4/README.md
+-rw-r--r--   0        0        0      693 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.4/pyproject.toml
+-rw-r--r--   0        0        0     1284 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.4/PKG-INFO
```

### Comparing `pyexhange_r3ne-0.1.3/pyexhange.py` & `pyexhange_r3ne-0.1.4/pyexhange.py`

 * *Files 12% similar despite different names*

```diff
@@ -31,28 +31,28 @@
 
 def handle_command(user_input):
     try:
         command_list = user_input.split()
         command = command_list[0]
         args = command_list[1:]
     except:
-        return {"status": "error", "error_code": "FIELD_EMPTY", "error_message": "Field is empty"}
+        return {"status": "error", "error_code": "FIELD_EMPTY", "error": "Field is empty"}
 
     if command in commands:
         try:
             money_redeemed = data.load(args[0], "redeemed?") or False
             if not money_redeemed:
                 usdBal = data.load(args[0], "usd")
                 data.save(args[0], "usd", usdBal + 2000)
                 data.save(args[0], "redeemed?", True)
             return commands[command](*args)
         except Exception as e:
-            return {"status": "error", "error_code": "UNKNOWN_ERROR", "error_message": str(e)}
+            return {"status": "error", "error_code": "UNKNOWN_ERROR", "error": str(e)}
     else:
-        return {"status": "error", "error_code": "INVALID_COMMAND", "error_message": "Invalid command"}
+        return {"status": "error", "error_code": "INVALID_COMMAND", "error": "Invalid command"}
 
 
 def main():
     while True:
         user_input = input("Enter a command: ")
         output = handle_command(user_input)
         print(output)
```

### Comparing `pyexhange_r3ne-0.1.3/modules/price.py` & `pyexhange_r3ne-0.1.4/modules/price.py`

 * *Files 9% similar despite different names*

```diff
@@ -8,20 +8,22 @@
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:
 '''
 
 from modules.utils.data import *
 from modules.utils.exchanges import *
 
+
 def price_function(*args):
-    if len(args) != 1:
+    if len(args) != 2:
         return {"status": "failed", "error_code": "INVALID_ARGUMENTS", "error": "Invalid arguments. Usage: price system [currency]"}
     user, currency = args
     currency = currency.upper()
 
-    output = {
-    "status": "success",
-    "price": get_price(currency),
-    "currency": currency,
-    }
-
-    return output
+    try:
+        return {
+            "status": "success",
+            "price": get_price(currency),
+            "currency": currency,
+        }
+    except:
+        return {"status": "failed", "error_code": "NO_CURRENCY_FOUND", "error": f"{currency} could not be found from the database."}
```

### Comparing `pyexhange_r3ne-0.1.3/modules/send.py` & `pyexhange_r3ne-0.1.4/modules/send.py`

 * *Files identical despite different names*

### Comparing `pyexhange_r3ne-0.1.3/modules/trade.py` & `pyexhange_r3ne-0.1.4/modules/trade.py`

 * *Files identical despite different names*

### Comparing `pyexhange_r3ne-0.1.3/modules/wallet.py` & `pyexhange_r3ne-0.1.4/modules/wallet.py`

 * *Files identical despite different names*

### Comparing `pyexhange_r3ne-0.1.3/modules/utils/coingecko.py` & `pyexhange_r3ne-0.1.4/modules/utils/coingecko.py`

 * *Files identical despite different names*

### Comparing `pyexhange_r3ne-0.1.3/modules/utils/data.py` & `pyexhange_r3ne-0.1.4/modules/utils/data.py`

 * *Files identical despite different names*

### Comparing `pyexhange_r3ne-0.1.3/modules/utils/exchanges.py` & `pyexhange_r3ne-0.1.4/modules/utils/exchanges.py`

 * *Files identical despite different names*

### Comparing `pyexhange_r3ne-0.1.3/modules/utils/finhub.py` & `pyexhange_r3ne-0.1.4/modules/utils/finhub.py`

 * *Files identical despite different names*

### Comparing `pyexhange_r3ne-0.1.3/.gitignore` & `pyexhange_r3ne-0.1.4/.gitignore`

 * *Files identical despite different names*

### Comparing `pyexhange_r3ne-0.1.3/LICENCE.rst` & `pyexhange_r3ne-0.1.4/LICENCE.rst`

 * *Files identical despite different names*

### Comparing `pyexhange_r3ne-0.1.3/README.md` & `pyexhange_r3ne-0.1.4/README.md`

 * *Files identical despite different names*

### Comparing `pyexhange_r3ne-0.1.3/pyproject.toml` & `pyexhange_r3ne-0.1.4/pyproject.toml`

 * *Files 2% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 [build-system]
 requires = ["hatchling", "finnhub-python"]
 build-backend = "hatchling.build"
 
 [project]
 name = "pyexhange_r3ne"
-version = "0.1.3"
+version = "0.1.4"
 authors = [
   { name="R3ne.net", email="mail@r3ne.net" },
 ]
 description = "Python code that allows users to create and manage their own virtual wallets to get the trading experiense with out real money."
 readme = "README.md"
 requires-python = ">=3.7"
 classifiers = [
```

### Comparing `pyexhange_r3ne-0.1.3/PKG-INFO` & `pyexhange_r3ne-0.1.4/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pyexhange_r3ne
-Version: 0.1.3
+Version: 0.1.4
 Summary: Python code that allows users to create and manage their own virtual wallets to get the trading experiense with out real money.
 Project-URL: Homepage, https://github.com/JAAKKQ/pyexhange
 Project-URL: Bug Tracker, https://github.com/JAAKKQ/pyexhange/issues
 Author-email: "R3ne.net" <mail@r3ne.net>
 License-File: LICENCE.rst
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
```

