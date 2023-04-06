# Comparing `tmp/multicaller-0.0.0a8.tar.gz` & `tmp/multicaller-0.0.0a9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "multicaller-0.0.0a8.tar", last modified: Sat Mar 19 19:27:55 2022, max compression
+gzip compressed data, was "multicaller-0.0.0a9.tar", last modified: Sat Apr 23 23:20:16 2022, max compression
```

## Comparing `multicaller-0.0.0a8.tar` & `multicaller-0.0.0a9.tar`

### file list

```diff
@@ -1,17 +1,17 @@
-drwxr-xr-x   0 gerg       (502) staff       (20)        0 2022-03-19 19:27:55.462107 multicaller-0.0.0a8/
--rw-r--r--   0 gerg       (502) staff       (20)       60 2021-10-07 19:48:42.000000 multicaller-0.0.0a8/MANIFEST.in
--rw-r--r--   0 gerg       (502) staff       (20)      668 2022-03-19 19:27:55.462162 multicaller-0.0.0a8/PKG-INFO
--rw-r--r--   0 gerg       (502) staff       (20)       98 2021-10-07 19:18:46.000000 multicaller-0.0.0a8/README.md
-drwxr-xr-x   0 gerg       (502) staff       (20)        0 2022-03-19 19:27:55.461031 multicaller-0.0.0a8/multicaller/
--rw-r--r--   0 gerg       (502) staff       (20)        0 2021-10-07 14:30:30.000000 multicaller-0.0.0a8/multicaller/__init__.py
-drwxr-xr-x   0 gerg       (502) staff       (20)        0 2022-03-19 19:27:55.461946 multicaller-0.0.0a8/multicaller/abi/
--rw-r--r--   0 gerg       (502) staff       (20)     3279 2021-10-07 14:08:19.000000 multicaller-0.0.0a8/multicaller/abi/multiCall.json
--rw-r--r--   0 gerg       (502) staff       (20)     5323 2022-03-19 16:33:48.000000 multicaller-0.0.0a8/multicaller/multicaller.py
-drwxr-xr-x   0 gerg       (502) staff       (20)        0 2022-03-19 19:27:55.461819 multicaller-0.0.0a8/multicaller.egg-info/
--rw-r--r--   0 gerg       (502) staff       (20)      668 2022-03-19 19:27:55.000000 multicaller-0.0.0a8/multicaller.egg-info/PKG-INFO
--rw-r--r--   0 gerg       (502) staff       (20)      302 2022-03-19 19:27:55.000000 multicaller-0.0.0a8/multicaller.egg-info/SOURCES.txt
--rw-r--r--   0 gerg       (502) staff       (20)        1 2022-03-19 19:27:55.000000 multicaller-0.0.0a8/multicaller.egg-info/dependency_links.txt
--rw-r--r--   0 gerg       (502) staff       (20)       13 2022-03-19 19:27:55.000000 multicaller-0.0.0a8/multicaller.egg-info/requires.txt
--rw-r--r--   0 gerg       (502) staff       (20)       12 2022-03-19 19:27:55.000000 multicaller-0.0.0a8/multicaller.egg-info/top_level.txt
--rw-r--r--   0 gerg       (502) staff       (20)      103 2021-10-07 19:16:42.000000 multicaller-0.0.0a8/pyproject.toml
--rw-r--r--   0 gerg       (502) staff       (20)      671 2022-03-19 19:27:55.462396 multicaller-0.0.0a8/setup.cfg
+drwxr-xr-x   0 gerg       (502) staff       (20)        0 2022-04-23 23:20:16.199128 multicaller-0.0.0a9/
+-rw-r--r--   0 gerg       (502) staff       (20)       60 2021-10-07 19:48:42.000000 multicaller-0.0.0a9/MANIFEST.in
+-rw-r--r--   0 gerg       (502) staff       (20)      668 2022-04-23 23:20:16.199209 multicaller-0.0.0a9/PKG-INFO
+-rw-r--r--   0 gerg       (502) staff       (20)       98 2021-10-07 19:18:46.000000 multicaller-0.0.0a9/README.md
+drwxr-xr-x   0 gerg       (502) staff       (20)        0 2022-04-23 23:20:16.197921 multicaller-0.0.0a9/multicaller/
+-rw-r--r--   0 gerg       (502) staff       (20)        0 2021-10-07 14:30:30.000000 multicaller-0.0.0a9/multicaller/__init__.py
+drwxr-xr-x   0 gerg       (502) staff       (20)        0 2022-04-23 23:20:16.198882 multicaller-0.0.0a9/multicaller/abi/
+-rw-r--r--   0 gerg       (502) staff       (20)     3279 2021-10-07 14:08:19.000000 multicaller-0.0.0a9/multicaller/abi/multiCall.json
+-rw-r--r--   0 gerg       (502) staff       (20)     5433 2022-04-23 23:18:47.000000 multicaller-0.0.0a9/multicaller/multicaller.py
+drwxr-xr-x   0 gerg       (502) staff       (20)        0 2022-04-23 23:20:16.198765 multicaller-0.0.0a9/multicaller.egg-info/
+-rw-r--r--   0 gerg       (502) staff       (20)      668 2022-04-23 23:20:16.000000 multicaller-0.0.0a9/multicaller.egg-info/PKG-INFO
+-rw-r--r--   0 gerg       (502) staff       (20)      302 2022-04-23 23:20:16.000000 multicaller-0.0.0a9/multicaller.egg-info/SOURCES.txt
+-rw-r--r--   0 gerg       (502) staff       (20)        1 2022-04-23 23:20:16.000000 multicaller-0.0.0a9/multicaller.egg-info/dependency_links.txt
+-rw-r--r--   0 gerg       (502) staff       (20)       13 2022-04-23 23:20:16.000000 multicaller-0.0.0a9/multicaller.egg-info/requires.txt
+-rw-r--r--   0 gerg       (502) staff       (20)       12 2022-04-23 23:20:16.000000 multicaller-0.0.0a9/multicaller.egg-info/top_level.txt
+-rw-r--r--   0 gerg       (502) staff       (20)      103 2021-10-07 19:16:42.000000 multicaller-0.0.0a9/pyproject.toml
+-rw-r--r--   0 gerg       (502) staff       (20)      671 2022-04-23 23:20:16.199458 multicaller-0.0.0a9/setup.cfg
```

### Comparing `multicaller-0.0.0a8/PKG-INFO` & `multicaller-0.0.0a9/PKG-INFO`

 * *Files 19% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: multicaller
-Version: 0.0.0a8
+Version: 0.0.0a9
 Summary: web3py multicaller simplified interface
 Home-page: https://github.com/gerrrg/multicaller
 Author: gerrrg
 Author-email: gerrrrrrrg@gmail.com
 License: UNKNOWN
 Project-URL: Bug Tracker, https://github.com/gerrrg/multicaller/issues
 Platform: UNKNOWN
```

### Comparing `multicaller-0.0.0a8/multicaller/abi/multiCall.json` & `multicaller-0.0.0a9/multicaller/abi/multiCall.json`

 * *Files identical despite different names*

### Comparing `multicaller-0.0.0a8/multicaller/multicaller.py` & `multicaller-0.0.0a9/multicaller/multicaller.py`

 * *Files 6% similar despite different names*

```diff
@@ -16,15 +16,17 @@
 		5:	'0x3b2A02F22fCbc872AF77674ceD303eb269a46ce3',
 		42:	'0x2cc8688C5f75E365aaEEb4ea8D6a480405A48D2A',
 		56:	'0x1Ee38d535d541c55C9dae27B12edf090C608E6Fb',
 		100:	'0xb5b692a88BDFc81ca69dcB1d924f59f0413A602a',
 		128:	'0xc9a9F768ebD123A00B52e7A0E590df2e9E998707',
 		137:	'0xa1B2b503959aedD81512C37e9dce48164ec6a94d',
 		250:	'0xb828C456600857abd4ed6C32FAcc607bD0464F4F',
-		42161:	'0x269ff446d9892c9e19082564df3f5e8741e190a1'
+		42161:	'0x269ff446d9892c9e19082564df3f5e8741e190a1',
+		42220:	'0x75F59534dd892c1f8a7B172D639FA854D529ada3',
+		43114:	'0x82979a6f8D628270B29F5687bEA2F73D5D0eC77d'
 	};
 
 	def __init__(self, _chainId, _web3=None, _rpcEndpoint=None, _batches=1, _maxRetries=20, _verbose=False):
 		if _web3 is None and _rpcEndpoint is None:
 			print("[ERROR] You must provide a Web3 instance or an RPC Endpoint.");
 			print();
 			quit();
@@ -156,15 +158,15 @@
 
 				break;
 			except OverflowError:
 				self.batches += 1;
 				print("Too many requests in one batch. Reattempting with", self.batches, "batches...");
 			except Exception as e:
 				print("Attempt", retries, "of", self.maxRetries, "failed. Retrying...");
-				print(e.message, e.args);
-
+				self.reset();
+				raise e;
 		self.reset();
 		return(outputData);
 
 	def reset(self):
 		self.payload = [];
 		self.decoders = [];
```

### Comparing `multicaller-0.0.0a8/multicaller.egg-info/PKG-INFO` & `multicaller-0.0.0a9/multicaller.egg-info/PKG-INFO`

 * *Files 19% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: multicaller
-Version: 0.0.0a8
+Version: 0.0.0a9
 Summary: web3py multicaller simplified interface
 Home-page: https://github.com/gerrrg/multicaller
 Author: gerrrg
 Author-email: gerrrrrrrg@gmail.com
 License: UNKNOWN
 Project-URL: Bug Tracker, https://github.com/gerrrg/multicaller/issues
 Platform: UNKNOWN
```

### Comparing `multicaller-0.0.0a8/setup.cfg` & `multicaller-0.0.0a9/setup.cfg`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [metadata]
 name = multicaller
-version = 0.0.0a8
+version = 0.0.0a9
 author = gerrrg
 author_email = gerrrrrrrg@gmail.com
 description = web3py multicaller simplified interface
 long_description = file: README.md
 long_description_content_type = text/markdown
 url = https://github.com/gerrrg/multicaller
 project_urls =
```

