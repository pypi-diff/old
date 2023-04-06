# Comparing `tmp/pyexhange_r3ne-0.1.7.tar.gz` & `tmp/pyexhange_r3ne-0.1.8.tar.gz`

## Comparing `pyexhange_r3ne-0.1.7.tar` & `pyexhange_r3ne-0.1.8.tar`

### file list

```diff
@@ -1,21 +1,21 @@
--rw-r--r--   0        0        0       66 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.7/.gitattributes
--rwxr-xr-x   0        0        0       32 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.7/Run.bat
--rw-r--r--   0        0        0       39 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.7/config.json.example
--rw-r--r--   0        0        0     2094 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.7/pyexhange.py
--rw-r--r--   0        0        0      382 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.7/requirements.txt
--rw-r--r--   0        0        0      454 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.7/test.py
--rwxr-xr-x   0        0        0       71 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.7/upload.bat
--rw-r--r--   0        0        0        5 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.7/data/placeholder
--rw-r--r--   0        0        0     1113 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.7/modules/price.py
--rw-r--r--   0        0        0     1505 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.7/modules/send.py
--rw-r--r--   0        0        0     2854 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.7/modules/trade.py
--rw-r--r--   0        0        0     1138 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.7/modules/wallet.py
--rw-r--r--   0        0        0      893 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.7/modules/utils/coingecko.py
--rw-r--r--   0        0        0     2558 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.7/modules/utils/data.py
--rw-r--r--   0        0        0      936 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.7/modules/utils/exchanges.py
--rw-r--r--   0        0        0     1149 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.7/modules/utils/finhub.py
--rw-r--r--   0        0        0     3102 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.7/.gitignore
--rw-r--r--   0        0        0     1069 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.7/LICENCE.rst
--rw-r--r--   0        0        0      709 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.7/README.md
--rw-r--r--   0        0        0      693 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.7/pyproject.toml
--rw-r--r--   0        0        0     1284 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.7/PKG-INFO
+-rw-r--r--   0        0        0       66 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.8/.gitattributes
+-rwxr-xr-x   0        0        0       32 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.8/Run.bat
+-rw-r--r--   0        0        0       39 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.8/config.json.example
+-rw-r--r--   0        0        0     1653 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.8/pyexhange.py
+-rw-r--r--   0        0        0      382 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.8/requirements.txt
+-rw-r--r--   0        0        0      454 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.8/test.py
+-rwxr-xr-x   0        0        0       71 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.8/upload.bat
+-rw-r--r--   0        0        0        5 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.8/data/placeholder
+-rw-r--r--   0        0        0      672 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.8/modules/price.py
+-rw-r--r--   0        0        0     1064 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.8/modules/send.py
+-rw-r--r--   0        0        0     2413 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.8/modules/trade.py
+-rw-r--r--   0        0        0      697 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.8/modules/wallet.py
+-rw-r--r--   0        0        0      452 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.8/modules/utils/coingecko.py
+-rw-r--r--   0        0        0     2117 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.8/modules/utils/data.py
+-rw-r--r--   0        0        0      424 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.8/modules/utils/exchanges.py
+-rw-r--r--   0        0        0      708 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.8/modules/utils/finhub.py
+-rw-r--r--   0        0        0     3102 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.8/.gitignore
+-rw-r--r--   0        0        0     1069 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.8/LICENCE.rst
+-rw-r--r--   0        0        0      709 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.8/README.md
+-rw-r--r--   0        0        0      693 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.8/pyproject.toml
+-rw-r--r--   0        0        0     1284 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.8/PKG-INFO
```

### Comparing `pyexhange_r3ne-0.1.7/modules/send.py` & `pyexhange_r3ne-0.1.8/modules/trade.py`

 * *Files 26% similar despite different names*

```diff
@@ -1,40 +1,69 @@
 '''
 Copyright (c) 2023 R3ne.net
-
-Permission is hereby granted, free of charge, to any person obtaining a copy
-of this software and associated documentation files (the "Software"), to deal
-in the Software without restriction, including without limitation the rights
-to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
-copies of the Software, and to permit persons to whom the Software is
-furnished to do so, subject to the following conditions:
 '''
 
+from modules.utils.exchanges import *
 from modules.utils.data import *
 
 data = jsonBase("./data")
 
-def send_function(*args):
-    # Check if number of arguments is correct
-    if len(args) != 5:
-        return {"status": "failed", "error_code": "INVALID_ARGUMENTS", "error": "Invalid arguments. Usage: send [user] [user_to] [amount] [currency] [message]"}
-
-    user, userTo, amount, currency, message = args
+def trade_function(*args):
+    if len(args) != 3:
+        return {"status": "failed", "error_code": "INVALID_ARGUMENTS", "error": "Invalid arguments. Usage: trade [user] [amount] [currency]"}
+    
+    user, amount, currency = args
     currency = currency.upper()
-    amount = abs(float(amount))
-    myBal = data.load(user, currency)
-    if myBal >= amount:
-        myBal -= amount
-        toBal = data.load(userTo, currency)
-        toBal += amount
-        data.save(user, currency, myBal)
-        data.save(userTo, currency, toBal)
+    curdata = get_data(currency)
+    try:
+        if curdata == None:
+            return {"status": "failed", "error_code": "NO_CURRENCY_FOUND", "error": f"{currency} could not be found from the database."}
+        
+        symbol = curdata['symbol']
+        cost = curdata['price']
+        cost *= abs(float(amount))
+        if float(amount) < 0:
+            # If amount is negative, we are selling, so check if user has enough of the currency
+            walletBal = data.load(user, symbol)
+            if walletBal < abs(float(amount)):
+                return {"status": "failed", "error_code": "INSUFFICIENT_FUNDS", "error": f"Insufficient {currency} funds"}
+        usdBal = data.load(user, "USD")
+
+    except TypeError:
+        return {"status": "failed", "error_code": "INVALID_AMOUNT", "error": "Invalid input for amount"}
+
+    if float(amount) > 0:
+        # If amount is positive, we are buying
+        if usdBal >= cost:
+            usdBal -= cost
+            walletBal = data.load(user, symbol)
+            walletBal += float(amount)
+            data.save(user, "USD", usdBal)
+            data.save(user, symbol, walletBal, "CRYPTO")
+            output = {
+                "status": "success",
+                "amount": amount,
+                "currency": symbol,
+                "cost": cost
+            }
+            return output
+        else:
+            output = {
+                "status": "failed",
+                "error_code": "INSUFFICIENT_FUNDS",
+                "error": "Insufficient USD funds"
+            }
+            return output
+    else:
+        # If amount is negative, we are selling
+        usdBal += cost
+        walletBal -= abs(float(amount))
+        data.save(user, "USD", usdBal)
+        data.save(user, symbol, walletBal, "CRYPTO")
         output = {
             "status": "success",
             "amount": amount,
-            "userTo": userTo,
-            "currency": currency,
-            "message": message
+            "currency": symbol,
+            "cost": cost
         }
         return output
-    else:
-        return {"status": "failed", "error_code": "INSUFFICIENT_FUNDS", "error": "Insufficient funds."}
+
```

### Comparing `pyexhange_r3ne-0.1.7/.gitignore` & `pyexhange_r3ne-0.1.8/.gitignore`

 * *Files identical despite different names*

### Comparing `pyexhange_r3ne-0.1.7/LICENCE.rst` & `pyexhange_r3ne-0.1.8/LICENCE.rst`

 * *Files identical despite different names*

### Comparing `pyexhange_r3ne-0.1.7/README.md` & `pyexhange_r3ne-0.1.8/README.md`

 * *Files identical despite different names*

### Comparing `pyexhange_r3ne-0.1.7/pyproject.toml` & `pyexhange_r3ne-0.1.8/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 [build-system]
 requires = ["hatchling", "finnhub-python"]
 build-backend = "hatchling.build"
 
 [project]
 name = "pyexhange_r3ne"
-version = "0.1.7"
+version = "0.1.8"
 authors = [
   { name="R3ne.net", email="mail@r3ne.net" },
 ]
 description = "Python code that allows users to create and manage their own virtual wallets to get the trading experiense with out real money."
 readme = "README.md"
 requires-python = ">=3.7"
 classifiers = [
```

### Comparing `pyexhange_r3ne-0.1.7/PKG-INFO` & `pyexhange_r3ne-0.1.8/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pyexhange_r3ne
-Version: 0.1.7
+Version: 0.1.8
 Summary: Python code that allows users to create and manage their own virtual wallets to get the trading experiense with out real money.
 Project-URL: Homepage, https://github.com/JAAKKQ/pyexhange
 Project-URL: Bug Tracker, https://github.com/JAAKKQ/pyexhange/issues
 Author-email: "R3ne.net" <mail@r3ne.net>
 License-File: LICENCE.rst
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
```

