# Comparing `tmp/gpt-chatbot-cli-0.3.2.tar.gz` & `tmp/gpt-chatbot-cli-0.3.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "gpt-chatbot-cli-0.3.2.tar", last modified: Fri Apr  7 04:39:49 2023, max compression
+gzip compressed data, was "gpt-chatbot-cli-0.3.3.tar", last modified: Fri Apr  7 05:10:29 2023, max compression
```

## Comparing `gpt-chatbot-cli-0.3.2.tar` & `gpt-chatbot-cli-0.3.3.tar`

### file list

```diff
@@ -1,22 +1,22 @@
-drwxr-xr-x   0 rukh      (1000) rukh      (1000)        0 2023-04-07 04:39:49.407603 gpt-chatbot-cli-0.3.2/
--rw-r--r--   0 rukh      (1000) rukh      (1000)     1051 2023-02-02 00:55:38.000000 gpt-chatbot-cli-0.3.2/LICENCE
--rw-r--r--   0 rukh      (1000) rukh      (1000)     2239 2023-04-07 04:39:49.407603 gpt-chatbot-cli-0.3.2/PKG-INFO
--rw-r--r--   0 rukh      (1000) rukh      (1000)     1571 2023-04-06 22:32:12.000000 gpt-chatbot-cli-0.3.2/README.md
--rw-r--r--   0 rukh      (1000) rukh      (1000)     1151 2023-04-07 04:37:46.000000 gpt-chatbot-cli-0.3.2/pyproject.toml
--rw-r--r--   0 rukh      (1000) rukh      (1000)       38 2023-04-07 04:39:49.407603 gpt-chatbot-cli-0.3.2/setup.cfg
-drwxr-xr-x   0 rukh      (1000) rukh      (1000)        0 2023-04-07 04:39:49.400936 gpt-chatbot-cli-0.3.2/src/
-drwxr-xr-x   0 rukh      (1000) rukh      (1000)        0 2023-04-07 04:39:49.404269 gpt-chatbot-cli-0.3.2/src/gpt_chatbot_cli.egg-info/
--rw-r--r--   0 rukh      (1000) rukh      (1000)     2239 2023-04-07 04:39:49.000000 gpt-chatbot-cli-0.3.2/src/gpt_chatbot_cli.egg-info/PKG-INFO
--rw-r--r--   0 rukh      (1000) rukh      (1000)      508 2023-04-07 04:39:49.000000 gpt-chatbot-cli-0.3.2/src/gpt_chatbot_cli.egg-info/SOURCES.txt
--rw-r--r--   0 rukh      (1000) rukh      (1000)        1 2023-04-07 04:39:49.000000 gpt-chatbot-cli-0.3.2/src/gpt_chatbot_cli.egg-info/dependency_links.txt
--rw-r--r--   0 rukh      (1000) rukh      (1000)       61 2023-04-07 04:39:49.000000 gpt-chatbot-cli-0.3.2/src/gpt_chatbot_cli.egg-info/entry_points.txt
--rw-r--r--   0 rukh      (1000) rukh      (1000)       82 2023-04-07 04:39:49.000000 gpt-chatbot-cli-0.3.2/src/gpt_chatbot_cli.egg-info/requires.txt
--rw-r--r--   0 rukh      (1000) rukh      (1000)       14 2023-04-07 04:39:49.000000 gpt-chatbot-cli-0.3.2/src/gpt_chatbot_cli.egg-info/top_level.txt
-drwxr-xr-x   0 rukh      (1000) rukh      (1000)        0 2023-04-07 04:39:49.404269 gpt-chatbot-cli-0.3.2/src/gptchatbotcli/
--rw-r--r--   0 rukh      (1000) rukh      (1000)       97 2023-04-07 04:37:55.000000 gpt-chatbot-cli-0.3.2/src/gptchatbotcli/__init__.py
--rw-r--r--   0 rukh      (1000) rukh      (1000)     1085 2023-04-07 04:29:35.000000 gpt-chatbot-cli-0.3.2/src/gptchatbotcli/database.py
--rw-r--r--   0 rukh      (1000) rukh      (1000)      429 2023-04-07 03:40:06.000000 gpt-chatbot-cli-0.3.2/src/gptchatbotcli/history.py
--rwxr-xr-x   0 rukh      (1000) rukh      (1000)     7383 2023-04-07 04:31:12.000000 gpt-chatbot-cli-0.3.2/src/gptchatbotcli/index.py
--rw-r--r--   0 rukh      (1000) rukh      (1000)     1702 2023-04-07 03:40:06.000000 gpt-chatbot-cli-0.3.2/src/gptchatbotcli/openapi_controller.py
--rw-r--r--   0 rukh      (1000) rukh      (1000)     1242 2023-04-06 15:56:39.000000 gpt-chatbot-cli-0.3.2/src/gptchatbotcli/payloads.py
--rw-r--r--   0 rukh      (1000) rukh      (1000)      404 2023-04-06 23:41:42.000000 gpt-chatbot-cli-0.3.2/src/gptchatbotcli/services.py
+drwxr-xr-x   0 rukh      (1000) rukh      (1000)        0 2023-04-07 05:10:29.505790 gpt-chatbot-cli-0.3.3/
+-rw-r--r--   0 rukh      (1000) rukh      (1000)     1051 2023-02-02 00:55:38.000000 gpt-chatbot-cli-0.3.3/LICENCE
+-rw-r--r--   0 rukh      (1000) rukh      (1000)     2313 2023-04-07 05:10:29.505790 gpt-chatbot-cli-0.3.3/PKG-INFO
+-rw-r--r--   0 rukh      (1000) rukh      (1000)     1645 2023-04-07 05:08:12.000000 gpt-chatbot-cli-0.3.3/README.md
+-rw-r--r--   0 rukh      (1000) rukh      (1000)      999 2023-04-07 05:08:12.000000 gpt-chatbot-cli-0.3.3/pyproject.toml
+-rw-r--r--   0 rukh      (1000) rukh      (1000)       38 2023-04-07 05:10:29.505790 gpt-chatbot-cli-0.3.3/setup.cfg
+drwxr-xr-x   0 rukh      (1000) rukh      (1000)        0 2023-04-07 05:10:29.502457 gpt-chatbot-cli-0.3.3/src/
+drwxr-xr-x   0 rukh      (1000) rukh      (1000)        0 2023-04-07 05:10:29.502457 gpt-chatbot-cli-0.3.3/src/gpt_chatbot_cli.egg-info/
+-rw-r--r--   0 rukh      (1000) rukh      (1000)     2313 2023-04-07 05:10:29.000000 gpt-chatbot-cli-0.3.3/src/gpt_chatbot_cli.egg-info/PKG-INFO
+-rw-r--r--   0 rukh      (1000) rukh      (1000)      508 2023-04-07 05:10:29.000000 gpt-chatbot-cli-0.3.3/src/gpt_chatbot_cli.egg-info/SOURCES.txt
+-rw-r--r--   0 rukh      (1000) rukh      (1000)        1 2023-04-07 05:10:29.000000 gpt-chatbot-cli-0.3.3/src/gpt_chatbot_cli.egg-info/dependency_links.txt
+-rw-r--r--   0 rukh      (1000) rukh      (1000)       61 2023-04-07 05:10:29.000000 gpt-chatbot-cli-0.3.3/src/gpt_chatbot_cli.egg-info/entry_points.txt
+-rw-r--r--   0 rukh      (1000) rukh      (1000)       82 2023-04-07 05:10:29.000000 gpt-chatbot-cli-0.3.3/src/gpt_chatbot_cli.egg-info/requires.txt
+-rw-r--r--   0 rukh      (1000) rukh      (1000)       14 2023-04-07 05:10:29.000000 gpt-chatbot-cli-0.3.3/src/gpt_chatbot_cli.egg-info/top_level.txt
+drwxr-xr-x   0 rukh      (1000) rukh      (1000)        0 2023-04-07 05:10:29.505790 gpt-chatbot-cli-0.3.3/src/gptchatbotcli/
+-rw-r--r--   0 rukh      (1000) rukh      (1000)       97 2023-04-07 05:08:12.000000 gpt-chatbot-cli-0.3.3/src/gptchatbotcli/__init__.py
+-rw-r--r--   0 rukh      (1000) rukh      (1000)      784 2023-04-07 05:08:12.000000 gpt-chatbot-cli-0.3.3/src/gptchatbotcli/database.py
+-rw-r--r--   0 rukh      (1000) rukh      (1000)      429 2023-04-07 05:08:12.000000 gpt-chatbot-cli-0.3.3/src/gptchatbotcli/history.py
+-rwxr-xr-x   0 rukh      (1000) rukh      (1000)     7383 2023-04-07 05:08:12.000000 gpt-chatbot-cli-0.3.3/src/gptchatbotcli/index.py
+-rw-r--r--   0 rukh      (1000) rukh      (1000)     1702 2023-04-07 05:08:12.000000 gpt-chatbot-cli-0.3.3/src/gptchatbotcli/openapi_controller.py
+-rw-r--r--   0 rukh      (1000) rukh      (1000)     1242 2023-04-07 05:08:12.000000 gpt-chatbot-cli-0.3.3/src/gptchatbotcli/payloads.py
+-rw-r--r--   0 rukh      (1000) rukh      (1000)      404 2023-04-07 05:08:12.000000 gpt-chatbot-cli-0.3.3/src/gptchatbotcli/services.py
```

### Comparing `gpt-chatbot-cli-0.3.2/LICENCE` & `gpt-chatbot-cli-0.3.3/LICENCE`

 * *Files identical despite different names*

### Comparing `gpt-chatbot-cli-0.3.2/PKG-INFO` & `gpt-chatbot-cli-0.3.3/PKG-INFO`

 * *Files 5% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: gpt-chatbot-cli
-Version: 0.3.2
+Version: 0.3.3
 Summary: A minimal chatgpt cli
 Author-email: Ruben Kharel <talkto@rubenk.com.np>
 Project-URL: Homepage, https://github.com/slithery0/gpt-chatbot-cli
 Project-URL: Bug Tracker, https://github.com/slithery0/gpt-chatbot-cli/issues
 Keywords: chatgpt,gpt-chatbot,chatgpt-cli
 Classifier: Development Status :: 4 - Beta
 Classifier: Intended Audience :: End Users/Desktop
@@ -17,17 +17,22 @@
 
 # Chatgpt-cli
 
 It's a very minimal cli prompt, where you can chat and keeping the conversation session memorable by chatgpt.
 
 ## Install
 
-Assuming you created a set env variable with key named `OPENAI_API_KEY`.
+Assuming you created a env variable with key named `OPENAI_API_KEY`.
 If you don't have a api key [visit here](https://platform.openai.com/account/api-keys) and generate one.
 
+```
+vim ~/.bashrc
+exports OPENAI_API_KEY=<YOUR OPENAI API KEY>
+```
+---
 
 ```
 $ pip3 install gpt-chatbot-cli
 ```
 
 ## Usage
 
@@ -50,15 +55,15 @@
                            or use the environment variable OPENAI_API_KEY.
   -m, --model TEXT         Model to use for text generation | (default:
                            gpt-3.5-turbo)
   -t, --temperature FLOAT  Temperature for text generation | (default: 0.9)
   -p, --preset TEXT        Preset mode to use for text generation | (default:
                            Chat)  Available presets: Chat, Q&A, Grammar
                            Correction, Eli5, Custom
-  -hs, --history           Show chat history | (default: False)
+  -hs, --history           Show chat history picker | (default: False)
   -h, --help               Show this message and exit.
 ```
 
 
 ## Demo
 
 [![asciicast](https://asciinema.org/a/uJSqTyzTX4QReLyHE3CMXRogM.svg)](https://asciinema.org/a/uJSqTyzTX4QReLyHE3CMXRogM)
```

### Comparing `gpt-chatbot-cli-0.3.2/README.md` & `gpt-chatbot-cli-0.3.3/README.md`

 * *Files 6% similar despite different names*

```diff
@@ -1,16 +1,21 @@
 # Chatgpt-cli
 
 It's a very minimal cli prompt, where you can chat and keeping the conversation session memorable by chatgpt.
 
 ## Install
 
-Assuming you created a set env variable with key named `OPENAI_API_KEY`.
+Assuming you created a env variable with key named `OPENAI_API_KEY`.
 If you don't have a api key [visit here](https://platform.openai.com/account/api-keys) and generate one.
 
+```
+vim ~/.bashrc
+exports OPENAI_API_KEY=<YOUR OPENAI API KEY>
+```
+---
 
 ```
 $ pip3 install gpt-chatbot-cli
 ```
 
 ## Usage
 
@@ -33,15 +38,15 @@
                            or use the environment variable OPENAI_API_KEY.
   -m, --model TEXT         Model to use for text generation | (default:
                            gpt-3.5-turbo)
   -t, --temperature FLOAT  Temperature for text generation | (default: 0.9)
   -p, --preset TEXT        Preset mode to use for text generation | (default:
                            Chat)  Available presets: Chat, Q&A, Grammar
                            Correction, Eli5, Custom
-  -hs, --history           Show chat history | (default: False)
+  -hs, --history           Show chat history picker | (default: False)
   -h, --help               Show this message and exit.
 ```
 
 
 ## Demo
 
 [![asciicast](https://asciinema.org/a/uJSqTyzTX4QReLyHE3CMXRogM.svg)](https://asciinema.org/a/uJSqTyzTX4QReLyHE3CMXRogM)
```

### Comparing `gpt-chatbot-cli-0.3.2/src/gpt_chatbot_cli.egg-info/PKG-INFO` & `gpt-chatbot-cli-0.3.3/src/gpt_chatbot_cli.egg-info/PKG-INFO`

 * *Files 5% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: gpt-chatbot-cli
-Version: 0.3.2
+Version: 0.3.3
 Summary: A minimal chatgpt cli
 Author-email: Ruben Kharel <talkto@rubenk.com.np>
 Project-URL: Homepage, https://github.com/slithery0/gpt-chatbot-cli
 Project-URL: Bug Tracker, https://github.com/slithery0/gpt-chatbot-cli/issues
 Keywords: chatgpt,gpt-chatbot,chatgpt-cli
 Classifier: Development Status :: 4 - Beta
 Classifier: Intended Audience :: End Users/Desktop
@@ -17,17 +17,22 @@
 
 # Chatgpt-cli
 
 It's a very minimal cli prompt, where you can chat and keeping the conversation session memorable by chatgpt.
 
 ## Install
 
-Assuming you created a set env variable with key named `OPENAI_API_KEY`.
+Assuming you created a env variable with key named `OPENAI_API_KEY`.
 If you don't have a api key [visit here](https://platform.openai.com/account/api-keys) and generate one.
 
+```
+vim ~/.bashrc
+exports OPENAI_API_KEY=<YOUR OPENAI API KEY>
+```
+---
 
 ```
 $ pip3 install gpt-chatbot-cli
 ```
 
 ## Usage
 
@@ -50,15 +55,15 @@
                            or use the environment variable OPENAI_API_KEY.
   -m, --model TEXT         Model to use for text generation | (default:
                            gpt-3.5-turbo)
   -t, --temperature FLOAT  Temperature for text generation | (default: 0.9)
   -p, --preset TEXT        Preset mode to use for text generation | (default:
                            Chat)  Available presets: Chat, Q&A, Grammar
                            Correction, Eli5, Custom
-  -hs, --history           Show chat history | (default: False)
+  -hs, --history           Show chat history picker | (default: False)
   -h, --help               Show this message and exit.
 ```
 
 
 ## Demo
 
 [![asciicast](https://asciinema.org/a/uJSqTyzTX4QReLyHE3CMXRogM.svg)](https://asciinema.org/a/uJSqTyzTX4QReLyHE3CMXRogM)
```

### Comparing `gpt-chatbot-cli-0.3.2/src/gptchatbotcli/database.py` & `gpt-chatbot-cli-0.3.3/src/gptchatbotcli/database.py`

 * *Files 20% similar despite different names*

```diff
@@ -1,16 +1,11 @@
 from tinydb import TinyDB, Query
 import time
 import os
-# from importlib.resources import files
-# print(__file__)
-# print("HI")
-# chat_history_path = os.path.join(os.path.dirname(__file__), 'db', "gpt_chatbot_chat_history.json")
-# print(chat_history_path)
-# chat_history_path = files("gptchatbotcli.db").joinpath("gpt_chatbot_chat_history.json").read_text()
+
 home_dir = os.path.expanduser("~")
 chat_history_path = os.path.join(home_dir, ".gpt_chatbot_chat_history.json")
 if not os.path.exists(chat_history_path):
   with open(chat_history_path, "x") as f:
     f.write("")
 db = TinyDB(chat_history_path)
```

### Comparing `gpt-chatbot-cli-0.3.2/src/gptchatbotcli/index.py` & `gpt-chatbot-cli-0.3.3/src/gptchatbotcli/index.py`

 * *Files identical despite different names*

### Comparing `gpt-chatbot-cli-0.3.2/src/gptchatbotcli/openapi_controller.py` & `gpt-chatbot-cli-0.3.3/src/gptchatbotcli/openapi_controller.py`

 * *Files identical despite different names*

### Comparing `gpt-chatbot-cli-0.3.2/src/gptchatbotcli/payloads.py` & `gpt-chatbot-cli-0.3.3/src/gptchatbotcli/payloads.py`

 * *Files identical despite different names*

