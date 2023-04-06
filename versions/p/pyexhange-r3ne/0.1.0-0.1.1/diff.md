# Comparing `tmp/pyexhange_r3ne-0.1.0.tar.gz` & `tmp/pyexhange_r3ne-0.1.1.tar.gz`

## Comparing `pyexhange_r3ne-0.1.0.tar` & `pyexhange_r3ne-0.1.1.tar`

### file list

```diff
@@ -1,20 +1,21 @@
--rw-r--r--   0        0        0       66 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.0/.gitattributes
--rwxr-xr-x   0        0        0       32 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.0/Run.bat
--rw-r--r--   0        0        0       39 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.0/config.json.example
--rw-r--r--   0        0        0     1896 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.0/pyexhange.py
--rw-r--r--   0        0        0      382 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.0/requirements.txt
--rw-r--r--   0        0        0      370 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.0/test.py
--rwxr-xr-x   0        0        0       71 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.0/upload.bat
--rw-r--r--   0        0        0        5 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.0/data/placeholder
--rw-r--r--   0        0        0     1505 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.0/modules/send.py
--rw-r--r--   0        0        0     2768 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.0/modules/trade.py
--rw-r--r--   0        0        0      934 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.0/modules/wallet.py
--rw-r--r--   0        0        0      824 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.0/modules/utils/coingecko.py
--rw-r--r--   0        0        0     2558 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.0/modules/utils/data.py
--rw-r--r--   0        0        0      802 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.0/modules/utils/exchanges.py
--rw-r--r--   0        0        0     1213 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.0/modules/utils/finhub.py
--rw-r--r--   0        0        0     3102 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.0/.gitignore
--rw-r--r--   0        0        0     1069 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.0/LICENCE.rst
--rw-r--r--   0        0        0      709 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.0/README.md
--rw-r--r--   0        0        0      693 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.0/pyproject.toml
--rw-r--r--   0        0        0     1284 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.0/PKG-INFO
+-rw-r--r--   0        0        0       66 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.1/.gitattributes
+-rwxr-xr-x   0        0        0       32 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.1/Run.bat
+-rw-r--r--   0        0        0       39 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.1/config.json.example
+-rw-r--r--   0        0        0     2077 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.1/pyexhange.py
+-rw-r--r--   0        0        0      382 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.1/requirements.txt
+-rw-r--r--   0        0        0      447 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.1/test.py
+-rwxr-xr-x   0        0        0       71 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.1/upload.bat
+-rw-r--r--   0        0        0        5 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.1/data/placeholder
+-rw-r--r--   0        0        0      900 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.1/modules/price.py
+-rw-r--r--   0        0        0     1505 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.1/modules/send.py
+-rw-r--r--   0        0        0     2803 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.1/modules/trade.py
+-rw-r--r--   0        0        0      934 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.1/modules/wallet.py
+-rw-r--r--   0        0        0      800 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.1/modules/utils/coingecko.py
+-rw-r--r--   0        0        0     2558 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.1/modules/utils/data.py
+-rw-r--r--   0        0        0      891 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.1/modules/utils/exchanges.py
+-rw-r--r--   0        0        0     1213 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.1/modules/utils/finhub.py
+-rw-r--r--   0        0        0     3102 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.1/.gitignore
+-rw-r--r--   0        0        0     1069 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.1/LICENCE.rst
+-rw-r--r--   0        0        0      709 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.1/README.md
+-rw-r--r--   0        0        0      693 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.1/pyproject.toml
+-rw-r--r--   0        0        0     1284 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.1/PKG-INFO
```

### Comparing `pyexhange_r3ne-0.1.0/pyexhange.py` & `pyexhange_r3ne-0.1.1/pyexhange.py`

 * *Files 16% similar despite different names*

```diff
@@ -5,29 +5,32 @@
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:
 '''
 
-from modules import trade
-from modules import send
-from modules import wallet
+import os
+import importlib
 from modules.utils.data import *
 
 try:
     data = jsonBase("./data")
 except FileNotFoundError:
     print("JSON file not found.")
 
-commands = {
-    "trade": trade.trade_function,
-    "send": send.send_function,
-    "wallet": wallet.wallet_function
-}
+commands = {}
+
+for filename in os.listdir("modules"):
+    if filename.endswith(".py"):
+        module_name = filename[:-3] # remove .py extension
+        module = importlib.import_module("modules." + module_name)
+        if hasattr(module, module_name + "_function"):
+            commands[module_name] = getattr(module, module_name + "_function")
+
 
 
 def handle_command(user_input):
     try:
         command_list = user_input.split()
         command = command_list[0]
         args = command_list[1:]
```

### Comparing `pyexhange_r3ne-0.1.0/modules/send.py` & `pyexhange_r3ne-0.1.1/modules/send.py`

 * *Files identical despite different names*

### Comparing `pyexhange_r3ne-0.1.0/modules/trade.py` & `pyexhange_r3ne-0.1.1/modules/trade.py`

 * *Files 9% similar despite different names*

```diff
@@ -22,18 +22,20 @@
     currency = currency.upper()
     try:
         if float(amount) < 0:
             # If amount is negative, we are selling, so check if user has enough of the currency
             walletBal = data.load(user, currency)
             if walletBal < abs(float(amount)):
                 return {"status": "failed", "error_code": "INSUFFICIENT_FUNDS", "error": f"Insufficient {currency} funds"}
-        cost = get_crypto_price(currency) * abs(float(amount))
+        cost = get_price(currency)
         usdBal = data.load(user, "USD")
-    except KeyError:
-        return {"status": "failed", "error_code": "NO_CURRENCY_FOUND", "error": f"{currency} could not be found from the database."}
+        if cost == None:
+            return {"status": "failed", "error_code": "NO_CURRENCY_FOUND", "error": f"{currency} could not be found from the database."}
+        else:
+            cost *= abs(float(amount))
     except TypeError:
         return {"status": "failed", "error_code": "INVALID_AMOUNT", "error": "Invalid input for amount"}
 
     if float(amount) > 0:
         # If amount is positive, we are buying
         if usdBal >= cost:
             usdBal -= cost
```

### Comparing `pyexhange_r3ne-0.1.0/modules/wallet.py` & `pyexhange_r3ne-0.1.1/modules/wallet.py`

 * *Files identical despite different names*

### Comparing `pyexhange_r3ne-0.1.0/modules/utils/coingecko.py` & `pyexhange_r3ne-0.1.1/modules/utils/coingecko.py`

 * *Files 16% similar despite different names*

```diff
@@ -5,16 +5,14 @@
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:
 '''
 
-import json
-import os
 from pycoingecko import CoinGeckoAPI
 
 cg = CoinGeckoAPI()
 
 def coingecko_get_crypto_price(crypto_name):
     crypto_name = crypto_name.lower()
     try:
```

### Comparing `pyexhange_r3ne-0.1.0/modules/utils/data.py` & `pyexhange_r3ne-0.1.1/modules/utils/data.py`

 * *Files identical despite different names*

### Comparing `pyexhange_r3ne-0.1.0/modules/utils/exchanges.py` & `pyexhange_r3ne-0.1.1/modules/utils/exchanges.py`

 * *Files 12% similar despite different names*

```diff
@@ -8,15 +8,18 @@
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:
 '''
 
 from modules.utils.finhub import *
 from modules.utils.coingecko import *
 
-def get_crypto_price(crypto):
+def get_price(crypto):
+    #Maybe stonks too?!?!
     finhub_price = finhub_get_crypto_price(crypto)
     coingecko_price = coingecko_get_crypto_price(crypto)
+    price = None
 
     if finhub_price == None:
-        return coingecko_price
-    else:
-        return finhub_price
+        price = coingecko_price
+    elif coingecko_price == None:
+        price = finhub_price
+    return float(price)
```

### Comparing `pyexhange_r3ne-0.1.0/modules/utils/finhub.py` & `pyexhange_r3ne-0.1.1/modules/utils/finhub.py`

 * *Files identical despite different names*

### Comparing `pyexhange_r3ne-0.1.0/.gitignore` & `pyexhange_r3ne-0.1.1/.gitignore`

 * *Files identical despite different names*

### Comparing `pyexhange_r3ne-0.1.0/LICENCE.rst` & `pyexhange_r3ne-0.1.1/LICENCE.rst`

 * *Files identical despite different names*

### Comparing `pyexhange_r3ne-0.1.0/README.md` & `pyexhange_r3ne-0.1.1/README.md`

 * *Files identical despite different names*

### Comparing `pyexhange_r3ne-0.1.0/pyproject.toml` & `pyexhange_r3ne-0.1.1/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 [build-system]
 requires = ["hatchling", "finnhub-python"]
 build-backend = "hatchling.build"
 
 [project]
 name = "pyexhange_r3ne"
-version = "0.1.0"
+version = "0.1.1"
 authors = [
   { name="R3ne.net", email="mail@r3ne.net" },
 ]
 description = "Python code that allows users to create and manage their own virtual wallets to get the trading experiense with out real money."
 readme = "README.md"
 requires-python = ">=3.7"
 classifiers = [
```

### Comparing `pyexhange_r3ne-0.1.0/PKG-INFO` & `pyexhange_r3ne-0.1.1/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pyexhange_r3ne
-Version: 0.1.0
+Version: 0.1.1
 Summary: Python code that allows users to create and manage their own virtual wallets to get the trading experiense with out real money.
 Project-URL: Homepage, https://github.com/JAAKKQ/pyexhange
 Project-URL: Bug Tracker, https://github.com/JAAKKQ/pyexhange/issues
 Author-email: "R3ne.net" <mail@r3ne.net>
 License-File: LICENCE.rst
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
```

