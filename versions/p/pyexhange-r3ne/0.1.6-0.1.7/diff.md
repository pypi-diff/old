# Comparing `tmp/pyexhange_r3ne-0.1.6.tar.gz` & `tmp/pyexhange_r3ne-0.1.7.tar.gz`

## Comparing `pyexhange_r3ne-0.1.6.tar` & `pyexhange_r3ne-0.1.7.tar`

### file list

```diff
@@ -1,21 +1,21 @@
--rw-r--r--   0        0        0       66 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.6/.gitattributes
--rwxr-xr-x   0        0        0       32 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.6/Run.bat
--rw-r--r--   0        0        0       39 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.6/config.json.example
--rw-r--r--   0        0        0     2094 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.6/pyexhange.py
--rw-r--r--   0        0        0      382 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.6/requirements.txt
--rw-r--r--   0        0        0      454 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.6/test.py
--rwxr-xr-x   0        0        0       71 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.6/upload.bat
--rw-r--r--   0        0        0        5 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.6/data/placeholder
--rw-r--r--   0        0        0     1113 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.6/modules/price.py
--rw-r--r--   0        0        0     1505 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.6/modules/send.py
--rw-r--r--   0        0        0     2842 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.6/modules/trade.py
--rw-r--r--   0        0        0     1051 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.6/modules/wallet.py
--rw-r--r--   0        0        0      893 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.6/modules/utils/coingecko.py
--rw-r--r--   0        0        0     2558 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.6/modules/utils/data.py
--rw-r--r--   0        0        0      865 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.6/modules/utils/exchanges.py
--rw-r--r--   0        0        0     1149 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.6/modules/utils/finhub.py
--rw-r--r--   0        0        0     3102 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.6/.gitignore
--rw-r--r--   0        0        0     1069 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.6/LICENCE.rst
--rw-r--r--   0        0        0      709 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.6/README.md
--rw-r--r--   0        0        0      693 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.6/pyproject.toml
--rw-r--r--   0        0        0     1284 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.6/PKG-INFO
+-rw-r--r--   0        0        0       66 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.7/.gitattributes
+-rwxr-xr-x   0        0        0       32 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.7/Run.bat
+-rw-r--r--   0        0        0       39 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.7/config.json.example
+-rw-r--r--   0        0        0     2094 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.7/pyexhange.py
+-rw-r--r--   0        0        0      382 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.7/requirements.txt
+-rw-r--r--   0        0        0      454 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.7/test.py
+-rwxr-xr-x   0        0        0       71 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.7/upload.bat
+-rw-r--r--   0        0        0        5 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.7/data/placeholder
+-rw-r--r--   0        0        0     1113 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.7/modules/price.py
+-rw-r--r--   0        0        0     1505 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.7/modules/send.py
+-rw-r--r--   0        0        0     2854 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.7/modules/trade.py
+-rw-r--r--   0        0        0     1138 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.7/modules/wallet.py
+-rw-r--r--   0        0        0      893 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.7/modules/utils/coingecko.py
+-rw-r--r--   0        0        0     2558 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.7/modules/utils/data.py
+-rw-r--r--   0        0        0      936 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.7/modules/utils/exchanges.py
+-rw-r--r--   0        0        0     1149 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.7/modules/utils/finhub.py
+-rw-r--r--   0        0        0     3102 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.7/.gitignore
+-rw-r--r--   0        0        0     1069 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.7/LICENCE.rst
+-rw-r--r--   0        0        0      709 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.7/README.md
+-rw-r--r--   0        0        0      693 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.7/pyproject.toml
+-rw-r--r--   0        0        0     1284 2020-02-02 00:00:00.000000 pyexhange_r3ne-0.1.7/PKG-INFO
```

### Comparing `pyexhange_r3ne-0.1.6/pyexhange.py` & `pyexhange_r3ne-0.1.7/pyexhange.py`

 * *Files identical despite different names*

### Comparing `pyexhange_r3ne-0.1.6/modules/price.py` & `pyexhange_r3ne-0.1.7/modules/price.py`

 * *Files identical despite different names*

### Comparing `pyexhange_r3ne-0.1.6/modules/send.py` & `pyexhange_r3ne-0.1.7/modules/send.py`

 * *Files identical despite different names*

### Comparing `pyexhange_r3ne-0.1.6/modules/trade.py` & `pyexhange_r3ne-0.1.7/modules/trade.py`

 * *Files 6% similar despite different names*

```diff
@@ -16,27 +16,29 @@
 
 def trade_function(*args):
     if len(args) != 3:
         return {"status": "failed", "error_code": "INVALID_ARGUMENTS", "error": "Invalid arguments. Usage: trade [user] [amount] [currency]"}
     
     user, amount, currency = args
     currency = currency.upper()
-    symbol = get_data(currency)['symbol']
+    curdata = get_data(currency)
     try:
+        if curdata == None:
+            return {"status": "failed", "error_code": "NO_CURRENCY_FOUND", "error": f"{currency} could not be found from the database."}
+        
+        symbol = curdata['symbol']
+        cost = curdata['price']
+        cost *= abs(float(amount))
         if float(amount) < 0:
             # If amount is negative, we are selling, so check if user has enough of the currency
             walletBal = data.load(user, symbol)
             if walletBal < abs(float(amount)):
                 return {"status": "failed", "error_code": "INSUFFICIENT_FUNDS", "error": f"Insufficient {currency} funds"}
-        cost = get_data(currency)['price']
         usdBal = data.load(user, "USD")
-        if cost == None:
-            return {"status": "failed", "error_code": "NO_CURRENCY_FOUND", "error": f"{currency} could not be found from the database."}
-        else:
-            cost *= abs(float(amount))
+
     except TypeError:
         return {"status": "failed", "error_code": "INVALID_AMOUNT", "error": "Invalid input for amount"}
 
     if float(amount) > 0:
         # If amount is positive, we are buying
         if usdBal >= cost:
             usdBal -= cost
```

### Comparing `pyexhange_r3ne-0.1.6/modules/wallet.py` & `pyexhange_r3ne-0.1.7/modules/wallet.py`

 * *Files 20% similar despite different names*

```diff
@@ -17,11 +17,14 @@
 def wallet_function(*args):
     if len(args) != 2:
         return {"status": "failed", "error_code": "INVALID_ARGUMENTS", "error": "Invalid arguments. Usage: wallet [user] [currency]"}
 
     user, currency = args
     currency = currency.upper()
     curdata = get_data(currency)
+
+    if curdata == None:
+        curdata = {"price": 0, "symbol":"CRYPTO"}
     amount = data.load(user, curdata['symbol'])
 
-    output = {"status": "success", "amount": amount,"price": curdata['price'] * amount, "currency": currency}
+    output = {"status": "success", "amount": amount,"price": curdata['price'] * amount, "currency": curdata['symbol']}
     return output
```

### Comparing `pyexhange_r3ne-0.1.6/modules/utils/coingecko.py` & `pyexhange_r3ne-0.1.7/modules/utils/coingecko.py`

 * *Files identical despite different names*

### Comparing `pyexhange_r3ne-0.1.6/modules/utils/data.py` & `pyexhange_r3ne-0.1.7/modules/utils/data.py`

 * *Files identical despite different names*

### Comparing `pyexhange_r3ne-0.1.6/modules/utils/exchanges.py` & `pyexhange_r3ne-0.1.7/modules/utils/exchanges.py`

 * *Files 8% similar despite different names*

```diff
@@ -15,11 +15,13 @@
 def get_data(crypto):
     #Maybe stonks too?!?!
     finhub_price = finhub_get_data(crypto)
     coingecko_price = coingecko_get_data(crypto)
     price = None
 
     if finhub_price == None:
+        print("Used CoinGecko API")
         price = coingecko_price
     if coingecko_price == None:
+        print("Used Finhub API")
         price = finhub_price
     return price
```

### Comparing `pyexhange_r3ne-0.1.6/modules/utils/finhub.py` & `pyexhange_r3ne-0.1.7/modules/utils/finhub.py`

 * *Files identical despite different names*

### Comparing `pyexhange_r3ne-0.1.6/.gitignore` & `pyexhange_r3ne-0.1.7/.gitignore`

 * *Files identical despite different names*

### Comparing `pyexhange_r3ne-0.1.6/LICENCE.rst` & `pyexhange_r3ne-0.1.7/LICENCE.rst`

 * *Files identical despite different names*

### Comparing `pyexhange_r3ne-0.1.6/README.md` & `pyexhange_r3ne-0.1.7/README.md`

 * *Files identical despite different names*

### Comparing `pyexhange_r3ne-0.1.6/pyproject.toml` & `pyexhange_r3ne-0.1.7/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 [build-system]
 requires = ["hatchling", "finnhub-python"]
 build-backend = "hatchling.build"
 
 [project]
 name = "pyexhange_r3ne"
-version = "0.1.6"
+version = "0.1.7"
 authors = [
   { name="R3ne.net", email="mail@r3ne.net" },
 ]
 description = "Python code that allows users to create and manage their own virtual wallets to get the trading experiense with out real money."
 readme = "README.md"
 requires-python = ">=3.7"
 classifiers = [
```

### Comparing `pyexhange_r3ne-0.1.6/PKG-INFO` & `pyexhange_r3ne-0.1.7/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pyexhange_r3ne
-Version: 0.1.6
+Version: 0.1.7
 Summary: Python code that allows users to create and manage their own virtual wallets to get the trading experiense with out real money.
 Project-URL: Homepage, https://github.com/JAAKKQ/pyexhange
 Project-URL: Bug Tracker, https://github.com/JAAKKQ/pyexhange/issues
 Author-email: "R3ne.net" <mail@r3ne.net>
 License-File: LICENCE.rst
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
```

