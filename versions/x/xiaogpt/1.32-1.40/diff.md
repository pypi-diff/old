# Comparing `tmp/xiaogpt-1.32.tar.gz` & `tmp/xiaogpt-1.40.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "xiaogpt-1.32.tar", last modified: Wed Apr  5 13:37:11 2023, max compression
+gzip compressed data, was "xiaogpt-1.40.tar", last modified: Fri Apr  7 11:13:57 2023, max compression
```

## Comparing `xiaogpt-1.32.tar` & `xiaogpt-1.40.tar`

### file list

```diff
@@ -1,15 +1,15 @@
--rw-r--r--   0        0        0     1063 2023-04-05 13:37:01.031116 xiaogpt-1.32/LICENSE
--rw-r--r--   0        0        0    10532 2023-04-05 13:37:01.031116 xiaogpt-1.32/README.md
--rw-r--r--   0        0        0      911 2023-04-05 13:37:11.318990 xiaogpt-1.32/pyproject.toml
--rw-r--r--   0        0        0        0 2023-04-05 13:37:01.031116 xiaogpt-1.32/xiaogpt/__init__.py
--rw-r--r--   0        0        0       61 2023-04-05 13:37:01.031116 xiaogpt-1.32/xiaogpt/__main__.py
--rw-r--r--   0        0        0      189 2023-04-05 13:37:01.031116 xiaogpt-1.32/xiaogpt/bot/__init__.py
--rw-r--r--   0        0        0      218 2023-04-05 13:37:01.031116 xiaogpt-1.32/xiaogpt/bot/base_bot.py
--rw-r--r--   0        0        0     2325 2023-04-05 13:37:01.031116 xiaogpt-1.32/xiaogpt/bot/chatgptapi_bot.py
--rw-r--r--   0        0        0     1386 2023-04-05 13:37:01.031116 xiaogpt-1.32/xiaogpt/bot/gpt3_bot.py
--rw-r--r--   0        0        0     1732 2023-04-05 13:37:01.031116 xiaogpt-1.32/xiaogpt/bot/newbing_bot.py
--rw-r--r--   0        0        0     3000 2023-04-05 13:37:01.031116 xiaogpt-1.32/xiaogpt/cli.py
--rw-r--r--   0        0        0     4771 2023-04-05 13:37:01.031116 xiaogpt-1.32/xiaogpt/config.py
--rw-r--r--   0        0        0     1991 2023-04-05 13:37:01.031116 xiaogpt-1.32/xiaogpt/utils.py
--rw-r--r--   0        0        0    18717 2023-04-05 13:37:01.031116 xiaogpt-1.32/xiaogpt/xiaogpt.py
--rw-r--r--   0        0        0    11110 1970-01-01 00:00:00.000000 xiaogpt-1.32/PKG-INFO
+-rw-r--r--   0        0        0     1063 2023-04-07 11:13:49.171552 xiaogpt-1.40/LICENSE
+-rw-r--r--   0        0        0    10532 2023-04-07 11:13:49.171552 xiaogpt-1.40/README.md
+-rw-r--r--   0        0        0      911 2023-04-07 11:13:57.739975 xiaogpt-1.40/pyproject.toml
+-rw-r--r--   0        0        0        0 2023-04-07 11:13:49.171552 xiaogpt-1.40/xiaogpt/__init__.py
+-rw-r--r--   0        0        0       61 2023-04-07 11:13:49.171552 xiaogpt-1.40/xiaogpt/__main__.py
+-rw-r--r--   0        0        0      189 2023-04-07 11:13:49.171552 xiaogpt-1.40/xiaogpt/bot/__init__.py
+-rw-r--r--   0        0        0      218 2023-04-07 11:13:49.171552 xiaogpt-1.40/xiaogpt/bot/base_bot.py
+-rw-r--r--   0        0        0     2325 2023-04-07 11:13:49.171552 xiaogpt-1.40/xiaogpt/bot/chatgptapi_bot.py
+-rw-r--r--   0        0        0     1386 2023-04-07 11:13:49.171552 xiaogpt-1.40/xiaogpt/bot/gpt3_bot.py
+-rw-r--r--   0        0        0     1732 2023-04-07 11:13:49.171552 xiaogpt-1.40/xiaogpt/bot/newbing_bot.py
+-rw-r--r--   0        0        0     3000 2023-04-07 11:13:49.171552 xiaogpt-1.40/xiaogpt/cli.py
+-rw-r--r--   0        0        0     4771 2023-04-07 11:13:49.171552 xiaogpt-1.40/xiaogpt/config.py
+-rw-r--r--   0        0        0     1991 2023-04-07 11:13:49.171552 xiaogpt-1.40/xiaogpt/utils.py
+-rw-r--r--   0        0        0    18767 2023-04-07 11:13:49.171552 xiaogpt-1.40/xiaogpt/xiaogpt.py
+-rw-r--r--   0        0        0    11110 1970-01-01 00:00:00.000000 xiaogpt-1.40/PKG-INFO
```

### Comparing `xiaogpt-1.32/LICENSE` & `xiaogpt-1.40/LICENSE`

 * *Files identical despite different names*

### Comparing `xiaogpt-1.32/README.md` & `xiaogpt-1.40/README.md`

 * *Files identical despite different names*

### Comparing `xiaogpt-1.32/pyproject.toml` & `xiaogpt-1.40/pyproject.toml`

 * *Files 12% similar despite different names*

```diff
@@ -16,15 +16,15 @@
     "openai",
     "aiohttp",
     "rich",
     "edge-tts>=6.1.3",
     "EdgeGPT",
 ]
 dynamic = []
-version = "1.32"
+version = "1.40"
 
 [project.license]
 text = "MIT"
 
 [project.urls]
 Homepage = "https://github.com/yihong0618/xiaogpt"
```

### Comparing `xiaogpt-1.32/xiaogpt/bot/chatgptapi_bot.py` & `xiaogpt-1.40/xiaogpt/bot/chatgptapi_bot.py`

 * *Files identical despite different names*

### Comparing `xiaogpt-1.32/xiaogpt/bot/gpt3_bot.py` & `xiaogpt-1.40/xiaogpt/bot/gpt3_bot.py`

 * *Files identical despite different names*

### Comparing `xiaogpt-1.32/xiaogpt/bot/newbing_bot.py` & `xiaogpt-1.40/xiaogpt/bot/newbing_bot.py`

 * *Files identical despite different names*

### Comparing `xiaogpt-1.32/xiaogpt/cli.py` & `xiaogpt-1.40/xiaogpt/cli.py`

 * *Files identical despite different names*

### Comparing `xiaogpt-1.32/xiaogpt/config.py` & `xiaogpt-1.40/xiaogpt/config.py`

 * *Files identical despite different names*

### Comparing `xiaogpt-1.32/xiaogpt/utils.py` & `xiaogpt-1.40/xiaogpt/utils.py`

 * *Files identical despite different names*

### Comparing `xiaogpt-1.32/xiaogpt/xiaogpt.py` & `xiaogpt-1.40/xiaogpt/xiaogpt.py`

 * *Files 1% similar despite different names*

```diff
@@ -128,18 +128,20 @@
         # fix multi xiaoai problems we check did first
         # why we use this way to fix?
         # some videos and articles already in the Internet
         # we do not want to change old way, so we check if miotDID in `env` first
         # to set device id
 
         for h in hardware_data:
-            if did := os.getenv("MI_DID"):
+            if did := self.config.mi_did:
                 if h.get("miotDID", "") == str(did):
                     self.device_id = h.get("deviceID")
                     break
+                else:
+                    continue
             if h.get("hardware", "") == self.config.hardware:
                 self.device_id = h.get("deviceID")
                 break
         else:
             raise Exception(
                 f"we have no hardware: {self.config.hardware} please use `micli mina` to check"
             )
```

### Comparing `xiaogpt-1.32/PKG-INFO` & `xiaogpt-1.40/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: xiaogpt
-Version: 1.32
+Version: 1.40
 Summary: Play ChatGPT with xiaomi AI speaker
 Author-Email: yihong0618 <zouzou0208@gmail.com>
 License: MIT
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
 Classifier: Programming Language :: Python :: 3
 Project-URL: Homepage, https://github.com/yihong0618/xiaogpt
```

