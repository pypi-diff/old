# Comparing `tmp/gpt-chatbot-cli-0.3.1.tar.gz` & `tmp/gpt-chatbot-cli-0.3.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "gpt-chatbot-cli-0.3.1.tar", last modified: Fri Apr  7 01:57:30 2023, max compression
+gzip compressed data, was "gpt-chatbot-cli-0.3.2.tar", last modified: Fri Apr  7 04:39:49 2023, max compression
```

## Comparing `gpt-chatbot-cli-0.3.1.tar` & `gpt-chatbot-cli-0.3.2.tar`

### file list

```diff
@@ -1,25 +1,22 @@
-drwxr-xr-x   0 rukh      (1000) rukh      (1000)        0 2023-04-07 01:57:30.688983 gpt-chatbot-cli-0.3.1/
--rw-r--r--   0 rukh      (1000) rukh      (1000)     1051 2023-02-02 00:55:38.000000 gpt-chatbot-cli-0.3.1/LICENCE
--rw-r--r--   0 rukh      (1000) rukh      (1000)     2239 2023-04-07 01:57:30.685650 gpt-chatbot-cli-0.3.1/PKG-INFO
--rw-r--r--   0 rukh      (1000) rukh      (1000)     1571 2023-04-06 22:32:12.000000 gpt-chatbot-cli-0.3.1/README.md
--rw-r--r--   0 rukh      (1000) rukh      (1000)     1004 2023-04-07 01:55:53.000000 gpt-chatbot-cli-0.3.1/pyproject.toml
--rw-r--r--   0 rukh      (1000) rukh      (1000)       38 2023-04-07 01:57:30.688983 gpt-chatbot-cli-0.3.1/setup.cfg
-drwxr-xr-x   0 rukh      (1000) rukh      (1000)        0 2023-04-07 01:57:30.655650 gpt-chatbot-cli-0.3.1/src/
-drwxr-xr-x   0 rukh      (1000) rukh      (1000)        0 2023-04-07 01:57:30.665650 gpt-chatbot-cli-0.3.1/src/gpt_chatbot_cli.egg-info/
--rw-r--r--   0 rukh      (1000) rukh      (1000)     2239 2023-04-07 01:57:30.000000 gpt-chatbot-cli-0.3.1/src/gpt_chatbot_cli.egg-info/PKG-INFO
--rw-r--r--   0 rukh      (1000) rukh      (1000)      586 2023-04-07 01:57:30.000000 gpt-chatbot-cli-0.3.1/src/gpt_chatbot_cli.egg-info/SOURCES.txt
--rw-r--r--   0 rukh      (1000) rukh      (1000)        1 2023-04-07 01:57:30.000000 gpt-chatbot-cli-0.3.1/src/gpt_chatbot_cli.egg-info/dependency_links.txt
--rw-r--r--   0 rukh      (1000) rukh      (1000)       82 2023-04-07 01:57:30.000000 gpt-chatbot-cli-0.3.1/src/gpt_chatbot_cli.egg-info/requires.txt
--rw-r--r--   0 rukh      (1000) rukh      (1000)       14 2023-04-07 01:57:30.000000 gpt-chatbot-cli-0.3.1/src/gpt_chatbot_cli.egg-info/top_level.txt
-drwxr-xr-x   0 rukh      (1000) rukh      (1000)        0 2023-04-07 01:57:30.678983 gpt-chatbot-cli-0.3.1/src/gptchatbotcli/
--rw-r--r--   0 rukh      (1000) rukh      (1000)       54 2023-04-07 01:16:42.000000 gpt-chatbot-cli-0.3.1/src/gptchatbotcli/__init__.py
--rw-r--r--   0 rukh      (1000) rukh      (1000)       38 2023-04-07 00:47:06.000000 gpt-chatbot-cli-0.3.1/src/gptchatbotcli/__main__.py
--rw-r--r--   0 rukh      (1000) rukh      (1000)      579 2023-04-06 23:41:33.000000 gpt-chatbot-cli-0.3.1/src/gptchatbotcli/database.py
-drwxr-xr-x   0 rukh      (1000) rukh      (1000)        0 2023-04-07 01:57:30.682316 gpt-chatbot-cli-0.3.1/src/gptchatbotcli/db/
--rw-r--r--   0 rukh      (1000) rukh      (1000)       32 2023-04-07 00:32:42.000000 gpt-chatbot-cli-0.3.1/src/gptchatbotcli/db/__init__.py
--rw-r--r--   0 rukh      (1000) rukh      (1000)        0 2023-04-07 00:17:41.000000 gpt-chatbot-cli-0.3.1/src/gptchatbotcli/db/gpt_chatbot_chat_history.json
--rwxr-xr-x   0 rukh      (1000) rukh      (1000)     7331 2023-04-07 00:04:56.000000 gpt-chatbot-cli-0.3.1/src/gptchatbotcli/gpt-chatbot-cli.py
--rw-r--r--   0 rukh      (1000) rukh      (1000)      415 2023-04-06 23:41:16.000000 gpt-chatbot-cli-0.3.1/src/gptchatbotcli/history.py
--rw-r--r--   0 rukh      (1000) rukh      (1000)     1688 2023-04-06 23:41:21.000000 gpt-chatbot-cli-0.3.1/src/gptchatbotcli/openapi_controller.py
--rw-r--r--   0 rukh      (1000) rukh      (1000)     1242 2023-04-06 15:56:39.000000 gpt-chatbot-cli-0.3.1/src/gptchatbotcli/payloads.py
--rw-r--r--   0 rukh      (1000) rukh      (1000)      404 2023-04-06 23:41:42.000000 gpt-chatbot-cli-0.3.1/src/gptchatbotcli/services.py
+drwxr-xr-x   0 rukh      (1000) rukh      (1000)        0 2023-04-07 04:39:49.407603 gpt-chatbot-cli-0.3.2/
+-rw-r--r--   0 rukh      (1000) rukh      (1000)     1051 2023-02-02 00:55:38.000000 gpt-chatbot-cli-0.3.2/LICENCE
+-rw-r--r--   0 rukh      (1000) rukh      (1000)     2239 2023-04-07 04:39:49.407603 gpt-chatbot-cli-0.3.2/PKG-INFO
+-rw-r--r--   0 rukh      (1000) rukh      (1000)     1571 2023-04-06 22:32:12.000000 gpt-chatbot-cli-0.3.2/README.md
+-rw-r--r--   0 rukh      (1000) rukh      (1000)     1151 2023-04-07 04:37:46.000000 gpt-chatbot-cli-0.3.2/pyproject.toml
+-rw-r--r--   0 rukh      (1000) rukh      (1000)       38 2023-04-07 04:39:49.407603 gpt-chatbot-cli-0.3.2/setup.cfg
+drwxr-xr-x   0 rukh      (1000) rukh      (1000)        0 2023-04-07 04:39:49.400936 gpt-chatbot-cli-0.3.2/src/
+drwxr-xr-x   0 rukh      (1000) rukh      (1000)        0 2023-04-07 04:39:49.404269 gpt-chatbot-cli-0.3.2/src/gpt_chatbot_cli.egg-info/
+-rw-r--r--   0 rukh      (1000) rukh      (1000)     2239 2023-04-07 04:39:49.000000 gpt-chatbot-cli-0.3.2/src/gpt_chatbot_cli.egg-info/PKG-INFO
+-rw-r--r--   0 rukh      (1000) rukh      (1000)      508 2023-04-07 04:39:49.000000 gpt-chatbot-cli-0.3.2/src/gpt_chatbot_cli.egg-info/SOURCES.txt
+-rw-r--r--   0 rukh      (1000) rukh      (1000)        1 2023-04-07 04:39:49.000000 gpt-chatbot-cli-0.3.2/src/gpt_chatbot_cli.egg-info/dependency_links.txt
+-rw-r--r--   0 rukh      (1000) rukh      (1000)       61 2023-04-07 04:39:49.000000 gpt-chatbot-cli-0.3.2/src/gpt_chatbot_cli.egg-info/entry_points.txt
+-rw-r--r--   0 rukh      (1000) rukh      (1000)       82 2023-04-07 04:39:49.000000 gpt-chatbot-cli-0.3.2/src/gpt_chatbot_cli.egg-info/requires.txt
+-rw-r--r--   0 rukh      (1000) rukh      (1000)       14 2023-04-07 04:39:49.000000 gpt-chatbot-cli-0.3.2/src/gpt_chatbot_cli.egg-info/top_level.txt
+drwxr-xr-x   0 rukh      (1000) rukh      (1000)        0 2023-04-07 04:39:49.404269 gpt-chatbot-cli-0.3.2/src/gptchatbotcli/
+-rw-r--r--   0 rukh      (1000) rukh      (1000)       97 2023-04-07 04:37:55.000000 gpt-chatbot-cli-0.3.2/src/gptchatbotcli/__init__.py
+-rw-r--r--   0 rukh      (1000) rukh      (1000)     1085 2023-04-07 04:29:35.000000 gpt-chatbot-cli-0.3.2/src/gptchatbotcli/database.py
+-rw-r--r--   0 rukh      (1000) rukh      (1000)      429 2023-04-07 03:40:06.000000 gpt-chatbot-cli-0.3.2/src/gptchatbotcli/history.py
+-rwxr-xr-x   0 rukh      (1000) rukh      (1000)     7383 2023-04-07 04:31:12.000000 gpt-chatbot-cli-0.3.2/src/gptchatbotcli/index.py
+-rw-r--r--   0 rukh      (1000) rukh      (1000)     1702 2023-04-07 03:40:06.000000 gpt-chatbot-cli-0.3.2/src/gptchatbotcli/openapi_controller.py
+-rw-r--r--   0 rukh      (1000) rukh      (1000)     1242 2023-04-06 15:56:39.000000 gpt-chatbot-cli-0.3.2/src/gptchatbotcli/payloads.py
+-rw-r--r--   0 rukh      (1000) rukh      (1000)      404 2023-04-06 23:41:42.000000 gpt-chatbot-cli-0.3.2/src/gptchatbotcli/services.py
```

### Comparing `gpt-chatbot-cli-0.3.1/LICENCE` & `gpt-chatbot-cli-0.3.2/LICENCE`

 * *Files identical despite different names*

### Comparing `gpt-chatbot-cli-0.3.1/PKG-INFO` & `gpt-chatbot-cli-0.3.2/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: gpt-chatbot-cli
-Version: 0.3.1
+Version: 0.3.2
 Summary: A minimal chatgpt cli
 Author-email: Ruben Kharel <talkto@rubenk.com.np>
 Project-URL: Homepage, https://github.com/slithery0/gpt-chatbot-cli
 Project-URL: Bug Tracker, https://github.com/slithery0/gpt-chatbot-cli/issues
 Keywords: chatgpt,gpt-chatbot,chatgpt-cli
 Classifier: Development Status :: 4 - Beta
 Classifier: Intended Audience :: End Users/Desktop
```

### Comparing `gpt-chatbot-cli-0.3.1/README.md` & `gpt-chatbot-cli-0.3.2/README.md`

 * *Files identical despite different names*

### Comparing `gpt-chatbot-cli-0.3.1/src/gpt_chatbot_cli.egg-info/PKG-INFO` & `gpt-chatbot-cli-0.3.2/src/gpt_chatbot_cli.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: gpt-chatbot-cli
-Version: 0.3.1
+Version: 0.3.2
 Summary: A minimal chatgpt cli
 Author-email: Ruben Kharel <talkto@rubenk.com.np>
 Project-URL: Homepage, https://github.com/slithery0/gpt-chatbot-cli
 Project-URL: Bug Tracker, https://github.com/slithery0/gpt-chatbot-cli/issues
 Keywords: chatgpt,gpt-chatbot,chatgpt-cli
 Classifier: Development Status :: 4 - Beta
 Classifier: Intended Audience :: End Users/Desktop
```

### Comparing `gpt-chatbot-cli-0.3.1/src/gptchatbotcli/gpt-chatbot-cli.py` & `gpt-chatbot-cli-0.3.2/src/gptchatbotcli/index.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,28 +1,28 @@
 #!/usr/bin/env python3
 import os
 import termcolor
 from prompt_toolkit import prompt
 from prompt_toolkit.styles import Style
 import click
 
-from payloads import presets, chat_complitions_models
-from database import init_chat_history, update_chat_history, defind_chat_title
-from history import chat_history_picker
-from services import print_char_by_char, print_whole_but_color
-from openapi_controller import check_api_key_validity, chat_api_call, title_gen
+from gptchatbotcli.payloads import presets, chat_complitions_models
+from gptchatbotcli.database import init_chat_history, update_chat_history, defind_chat_title
+from gptchatbotcli.history import chat_history_picker
+from gptchatbotcli.services import print_char_by_char, print_whole_but_color
+from gptchatbotcli.openapi_controller import check_api_key_validity, chat_api_call, title_gen
 
 @click.command()
 @click.option('--api_key', '-k', help='Openai API key. If not provided, will prompt for it or use the environment variable OPENAI_API_KEY.')
 @click.option('--model', '-m', default='gpt-3.5-turbo', help='Model to use for text generation | (default: gpt-3.5-turbo)')
 @click.option('--temperature', '-t', default=0.9, type=click.FLOAT, help='Temperature for text generation | (default: 0.9)')
 @click.option('--preset', '-p', default='chat', help='Preset mode to use for text generation | (default: Chat) \nAvailable presets: Chat, Q&A, Grammar Correction, Eli5, Custom')
 @click.option('--history', '-hs', default=False, is_flag=True, help='Show chat history | (default: False)')
 @click.help_option('--help', '-h')
-def generate_text(api_key, model, temperature, preset, history):
+def main(api_key, model, temperature, preset, history):
     """
     A CLI for OpenAI's GPT-3 API.
     Chat with a bot, ask questions, correct grammar, summarize text, and more.
 
     \b
     Examples:
         gpt-chatbot-cli
@@ -167,8 +167,8 @@
         exit(1)
     except KeyboardInterrupt:
         print(termcolor.colored(f"Keyboard Interrupt, Exiting...", 'light_red'))
         exit(0)
 
 
 if __name__ == '__main__':
-    generate_text()
+    main()
```

### Comparing `gpt-chatbot-cli-0.3.1/src/gptchatbotcli/openapi_controller.py` & `gpt-chatbot-cli-0.3.2/src/gptchatbotcli/openapi_controller.py`

 * *Files 5% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 import openai
 import termcolor
 
-from payloads import chat_complitions_models
+from gptchatbotcli.payloads import chat_complitions_models
 
 
 def check_api_key_validity(api_key, where):
   if(where == "prompt"):
       print("Found env variable OPENAI_API_KEY")
   print("Checking for validity")
   try:
```

### Comparing `gpt-chatbot-cli-0.3.1/src/gptchatbotcli/payloads.py` & `gpt-chatbot-cli-0.3.2/src/gptchatbotcli/payloads.py`

 * *Files identical despite different names*

