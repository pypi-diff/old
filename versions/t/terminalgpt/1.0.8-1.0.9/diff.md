# Comparing `tmp/terminalgpt-1.0.8.tar.gz` & `tmp/terminalgpt-1.0.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "terminalgpt-1.0.8.tar", max compression
+gzip compressed data, was "terminalgpt-1.0.9.tar", max compression
```

## Comparing `terminalgpt-1.0.8.tar` & `terminalgpt-1.0.9.tar`

### file list

```diff
@@ -1,12 +1,12 @@
--rw-r--r--   0        0        0     1070 2023-03-21 18:01:34.353070 terminalgpt-1.0.8/LICENSE
--rw-r--r--   0        0        0     3463 2023-03-22 18:34:32.484907 terminalgpt-1.0.8/README.md
--rw-r--r--   0        0        0      779 2023-03-29 18:54:20.197919 terminalgpt-1.0.8/pyproject.toml
--rw-r--r--   0        0        0       66 2023-03-11 15:11:43.240080 terminalgpt-1.0.8/terminalgpt/.gitattributes
--rw-r--r--   0        0        0        0 2023-03-11 15:11:43.240200 terminalgpt-1.0.8/terminalgpt/__init__.py
--rw-r--r--   0        0        0     6289 2023-03-29 18:51:24.391667 terminalgpt-1.0.8/terminalgpt/chat_utils.py
--rw-r--r--   0        0        0     2219 2023-03-29 18:46:16.438878 terminalgpt-1.0.8/terminalgpt/config.py
--rw-r--r--   0        0        0     2440 2023-03-29 18:46:16.439124 terminalgpt-1.0.8/terminalgpt/conversations.py
--rw-r--r--   0        0        0     1479 2023-03-21 17:20:53.535542 terminalgpt-1.0.8/terminalgpt/encryption.py
--rw-r--r--   0        0        0     7347 2023-03-29 18:49:00.146432 terminalgpt-1.0.8/terminalgpt/main.py
--rw-r--r--   0        0        0     3134 2023-03-27 10:43:57.761885 terminalgpt-1.0.8/terminalgpt/print_utils.py
--rw-r--r--   0        0        0     4321 1970-01-01 00:00:00.000000 terminalgpt-1.0.8/PKG-INFO
+-rw-r--r--   0        0        0     1070 2023-03-21 18:01:34.353070 terminalgpt-1.0.9/LICENSE
+-rw-r--r--   0        0        0     3395 2023-03-31 14:16:15.983658 terminalgpt-1.0.9/README.md
+-rw-r--r--   0        0        0      779 2023-03-31 14:16:15.984032 terminalgpt-1.0.9/pyproject.toml
+-rw-r--r--   0        0        0       66 2023-03-11 15:11:43.240080 terminalgpt-1.0.9/terminalgpt/.gitattributes
+-rw-r--r--   0        0        0        0 2023-03-11 15:11:43.240200 terminalgpt-1.0.9/terminalgpt/__init__.py
+-rw-r--r--   0        0        0     6878 2023-03-31 14:16:15.984259 terminalgpt-1.0.9/terminalgpt/chat_utils.py
+-rw-r--r--   0        0        0     2800 2023-03-31 14:16:15.984397 terminalgpt-1.0.9/terminalgpt/config.py
+-rw-r--r--   0        0        0     2440 2023-03-31 11:16:37.570616 terminalgpt-1.0.9/terminalgpt/conversations.py
+-rw-r--r--   0        0        0     1479 2023-03-21 17:20:53.535542 terminalgpt-1.0.9/terminalgpt/encryption.py
+-rw-r--r--   0        0        0     7057 2023-03-31 14:16:15.984537 terminalgpt-1.0.9/terminalgpt/main.py
+-rw-r--r--   0        0        0     3134 2023-03-31 11:16:37.571044 terminalgpt-1.0.9/terminalgpt/print_utils.py
+-rw-r--r--   0        0        0     4253 1970-01-01 00:00:00.000000 terminalgpt-1.0.9/PKG-INFO
```

### Comparing `terminalgpt-1.0.8/LICENSE` & `terminalgpt-1.0.9/LICENSE`

 * *Files identical despite different names*

### Comparing `terminalgpt-1.0.8/README.md` & `terminalgpt-1.0.9/README.md`

 * *Files 9% similar despite different names*

```diff
@@ -13,27 +13,29 @@
 
 ---
 
 ## Why?
 
 Some advantages of using TerminalGPT over the chatGPT browser-based app:
 
-1. It doesn't disconnect like the browser-based app, so you can leave it running in a terminal session on the side without losing context.
-2. It's highly available and can be used whenever you need it.
-3. It's faster with replies than the browser-based app.
-4. You can use TerminalGPT with your IDE terminal, which means you won't have to constantly switch between your browser and your IDE when you have questions.
-5. TerminalGPT's answers are tailored to your machine's operating system, distribution, and chip-set architecture.
-6. Doesn't use your conversation data for training the model (unlike the browser-based app).
-7. Your conversations are stored locally on your machine, so only you can access them.
+- It doesn't disconnect like the browser-based app, so you can leave it running in a terminal session on the side without losing context.
+- It's highly available and can be used whenever you need it.
+- It's faster with replies than the browser-based app.
+- You can use TerminalGPT with your IDE terminal, which means you won't have to constantly switch between your browser and your IDE when you have questions.
+- TerminalGPT's answers are tailored to your machine's operating system, distribution, and chip-set architecture
+- Doesn't use your conversation data for training the model (unlike the browser-based app).
+- Your conversations are stored locally on your machine, so only you can access them.
 
 ## Pre-requisites
 
-1. Python 3.6 or higher
-2. An OpenAI Account and API key (It's free for personal use).
-[How to create OpenAI API keys](https://elephas.app/blog/how-to-create-openai-api-keys-cl5c4f21d281431po7k8fgyol0)
+- Python 3.6 or higher
+- An OpenAI Account and API key (It's free for personal use).
+   1. Sign up at <https://beta.openai.com/signup> using email or Google/Microsoft account.
+   2. Go to <https://beta.openai.com/account/api-keys> or click on "View API keys" in the menu to get your API key.
+   For a more detailed guide on how to create an OpenAI API key, click [here](https://elephas.app/blog/how-to-create-openai-api-keys-cl5c4f21d281431po7k8fgyol0).
 
 ## Installation
 
 1. Install the latest TerminalGPT with pip install.
 
 ```sh
 pip install terminalgpt -U
@@ -53,16 +55,14 @@
 
 ## Usage
 
 ```sh
 Usage: terminalgpt [OPTIONS] COMMAND [ARGS]...
 
 Options:
-  --debug                Prints amounts of tokens used.
-  --token-limit INTEGER  Set the token limit between 1024 and 4096.
   --help                 Show this message and exit.
 
 Commands:
   new      Start a new conversation.
   load     Choose a previous conversation to load.
   delete   Choose a previous conversation to load.
   install  Creating a secret api key for the chatbot.
@@ -88,24 +88,14 @@
 
 Delete previous conversations:
 
 ```sh
 terminalgpt delete
 ```
 
-### Using flags
-
-Using flags, you can set the token limit and debug mode. the flags should be used before the command.
-
-For example:
-
-```sh
-terminalgpt --token-limit 2048 --debug new
-```
-
 ---
 
 ## Future Plans
 
 1. Support multiline input.
 2. Support optional vim input mode.
 3. Auto-completion for all commands.
```

### Comparing `terminalgpt-1.0.8/pyproject.toml` & `terminalgpt-1.0.9/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "terminalgpt"
-version = "1.0.8"
+version = "1.0.9"
 description = "AI chat asistent in your terminal powered by OpenAI GPT-3.5"
 authors = ["Adam Yodinsky <27074934+adamyodinsky@users.noreply.github.com>"]
 keywords=["ai", "chat", "terminal", "openai", "gpt3", "chatGPT", "assistant", "gpt3.5", "terminalGPT", "gpt-3.5-turbo"]
 readme = "README.md"
 
 [tool.poetry.dependencies]
 python = "^3.9"
```

### Comparing `terminalgpt-1.0.8/terminalgpt/chat_utils.py` & `terminalgpt-1.0.9/terminalgpt/chat_utils.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,9 +1,10 @@
 """"Chat utils module for terminalgpt."""
 
+import os
 import sys
 import time
 
 import openai
 import tiktoken
 from colorama import Back, Fore, Style
 from prompt_toolkit import PromptSession
@@ -16,15 +17,14 @@
 
 
 def chat_loop(
     conversation_name: str = None,
     **kwargs,
 ):
     """Main chat loop."""
-    debug: bool = kwargs["debug"]
     token_limit: int = kwargs["token_limit"]
     session: PromptSession = kwargs["session"]
     messages: list = kwargs["messages"]
 
     while True:
         # Get user input
 
@@ -67,15 +67,15 @@
             conversations.save_conversation(messages, conversation_name)
 
         # Print answer message
         print(Style.BRIGHT + "Assistant:" + Style.RESET_ALL)
         print_utils.print_slowly(Fore.YELLOW + message + Style.RESET_ALL)
 
         # Print usage
-        if debug:
+        if os.environ.get("LOG_LEVEL") == "DEBUG":
             print(
                 Fore.LIGHTBLUE_EX
                 + f"\nAPI Total Usage: {str(total_usage)} tokens"
                 + Style.RESET_ALL
             )
             print(
                 Fore.LIGHTCYAN_EX
@@ -110,46 +110,57 @@
             except openai.error.InvalidRequestError as error:
                 if "Please reduce the length of the messages" in str(error):
                     messages.pop(1)
                 else:
                     raise error
 
 
-# pylint: disable=unused-argument
-def validate_token_limit(ctx, param, limit: int):
-    """Validates the token limit."""
-
-    arr = [2**i for i in range(2, 13)]
-
-    if limit not in arr or limit < 1024:
-        raise ValueError("Token limit must be between 1024 and 4096 and a power of 2.")
-    return limit
-
-
 def exceeding_token_limit(total_usage: int, token_limit: int):
     """Returns True if the total_usage is greater than the token limit with some safe buffer."""
 
     return total_usage > token_limit
 
 
 def reduce_tokens(messages: list, token_limit: int, total_usage: int):
     """Reduce tokens in messages context."""
 
+    reduce_amount = total_usage - token_limit
     while exceeding_token_limit(total_usage, token_limit):
-        reduce_amount = total_usage - token_limit
         message = messages.pop(1)
         tokenized_message = TIKTOKEN_ENCODER.encode(message["content"])
 
         while reduce_amount > 0 and len(tokenized_message) > 0:
             total_usage -= 1
             reduce_amount -= 1
             tokenized_message.pop(0)
 
-    message["content"] = TIKTOKEN_ENCODER.decode(tokenized_message)
-    messages.insert(1, message)
+        if len(tokenized_message) == 0 and exceeding_token_limit(
+            total_usage, token_limit
+        ):
+            # every message follows <im_start>{role/name}\n{content}<im_end>\n
+            # thus we need to remove 4 tokens for every message that will be removed
+            # so if the message is empty
+            reduce_amount -= 4
+            total_usage -= 4
+
+            for key, _ in message.items():
+                if key == "name":  # if there's a name, the role is omitted
+                    # role is always required and always 1 token
+                    reduce_amount += 1
+                    total_usage += 1
+
+    if len(tokenized_message) > 0:
+        message["content"] = TIKTOKEN_ENCODER.decode(tokenized_message)
+        messages.insert(1, message)
+
+    if os.environ.get("LOG_LEVEL") == "DEBUG":
+        counted_tokens = num_tokens_from_messages(messages)
+        print(f"Counted usage: {total_usage}")
+        print(f"Real usage tokens: {counted_tokens}")
+
     return messages, total_usage
 
 
 def num_tokens_from_messages(messages) -> int:
     """Returns the number of tokens used by a list of messages."""
 
     encoding = tiktoken.get_encoding(config.ENCODING_MODEL)
@@ -158,15 +169,15 @@
         num_tokens += (
             4  # every message follows <im_start>{role/name}\n{content}<im_end>\n
         )
         for key, value in message.items():
             num_tokens += len(encoding.encode(value))
             if key == "name":  # if there's a name, the role is omitted
                 num_tokens += -1  # role is always required and always 1 token
-    num_tokens += 2  # every reply is primed with <im_start>assistant
+    num_tokens -= 2  # every reply is primed with <im_start>assistant
     return num_tokens
 
 
 def waiting_before_trying_again(wait_time: int = 10):
     """Waits for a given time before trying again."""
 
     with yaspin() as spinner:
```

### Comparing `terminalgpt-1.0.8/terminalgpt/config.py` & `terminalgpt-1.0.9/terminalgpt/config.py`

 * *Files 16% similar despite different names*

```diff
@@ -1,39 +1,63 @@
 """TerminalGPT configuration file."""
 
 import platform
 from os import path
 
+# def shell_version():
+#     """Get the current shell version."""
+
+#     shell = os.environ.get("SHELL")
+#     result = None
+
+#     if platform.system() == "Windows":
+#         result = subprocess.run(["ver"], stdout=subprocess.PIPE, check=True)
+#     else:
+#         result = subprocess.run(
+#             [shell, "--version"], stdout=subprocess.PIPE, check=False
+#         )
+#     return result.stdout.decode("utf-8").strip()
+
+
+def machine_info():
+    """Get the current machine info."""
+
+    return platform.platform()
+
+
 APP_NAME = "terminalgpt"
 API_TOKEN_LIMIT = 4096
+SAFETY_BUFFER = 1024
 
 BASE_PATH = f"~/.{APP_NAME}".replace("~", path.expanduser("~"))
 CONVERSATIONS_PATH = f"{BASE_PATH}/conversations"
 SECRET_PATH = f"{BASE_PATH}/{APP_NAME}.encrypted"
 KEY_PATH = f"{BASE_PATH}/{APP_NAME}.key"
 
 MODEL = "gpt-3.5-turbo-0301"
 ENCODING_MODEL = "cl100k_base"
 
 INIT_SYSTEM_MESSAGE = {
     "role": "system",
     "content": f"""
-You are a helpful personal assistant called "TerminalGPT" for a programer on a {platform.platform()} machine.
-Please note that your answers will be displayed on the terminal.
-So keep them short as possible (5 new lines max) and use a suitable format for printing on terminal.
+- Your name is "TerminalGPT".
+- You are a helpful personal assistant for programers.
+- You are running on {machine_info()} machine.
+- Please note that your answers will be displayed on the terminal.
+- So keep answers short as possible and use a suitable format for printing on a terminal.
 """,
 }
 
 
 INIT_WELCOME_MESSAGE = {
     "role": "system",
     "content": """
-Please start with a random and short greeting message starts with 'Welcome to terminalGPT'.
-Add a ton of self humor.
-Keep it short as possible, one line.
+- Please start the conversation with a random and short greeting message starts with 'Welcome to terminalGPT'.
+- Add a ton of self humor.
+- Keep it short as possible, one line.
 """,
 }
 
 INIT_WELCOME_BACK_MESSAGE = {
     "role": "system",
     "content": """
 The conversation you remember was a while ago, now we are continuing it.
```

### Comparing `terminalgpt-1.0.8/terminalgpt/conversations.py` & `terminalgpt-1.0.9/terminalgpt/conversations.py`

 * *Files identical despite different names*

### Comparing `terminalgpt-1.0.8/terminalgpt/encryption.py` & `terminalgpt-1.0.9/terminalgpt/encryption.py`

 * *Files identical despite different names*

### Comparing `terminalgpt-1.0.8/terminalgpt/main.py` & `terminalgpt-1.0.9/terminalgpt/main.py`

 * *Files 8% similar despite different names*

```diff
@@ -12,41 +12,24 @@
 
 from terminalgpt import chat_utils, config, print_utils
 from terminalgpt import conversations as conv
 from terminalgpt import encryption
 
 
 @click.group()
-@click.option(
-    "--debug",
-    is_flag=True,
-    help="Prints amounts of tokens used.",
-    type=bool,
-    default=False,
-)
-@click.option(
-    "--token-limit",
-    help="Set the token limit between 1024 and 4096.",
-    type=int,
-    default=config.API_TOKEN_LIMIT,
-    callback=chat_utils.validate_token_limit,
-)
 @click.pass_context
-def cli(ctx, debug, token_limit):
+def cli(ctx):
     """*~ TerminalGPT - Your Personal Terminal Assistant ~*"""
 
     ctx.ensure_object(dict)
-
-    ctx.obj["DEBUG"] = debug
-    ctx.obj["TOKEN_LIMIT"] = token_limit
-
     ctx.obj["SESSION"] = PromptSession(
         style=PromptStyle.from_dict({"prompt": "bold"}),
         message="\nUser: ",
     )
+    ctx.obj["TOKEN_LIMIT"] = config.API_TOKEN_LIMIT - config.SAFETY_BUFFER
 
     encryption.check_api_key()
     key = encryption.get_encryption_key(config.KEY_PATH)
     openai.api_key = encryption.decrypt(config.SECRET_PATH, key)
 
 
 @click.command(
@@ -89,18 +72,17 @@
 def new(ctx):
     """Start a new conversation."""
 
     messages = [
         config.INIT_SYSTEM_MESSAGE,
     ]
 
-    chat_utils.welcome_message(messages)
+    chat_utils.welcome_message(messages + [config.INIT_WELCOME_MESSAGE])
 
     chat_utils.chat_loop(
-        debug=ctx.obj["DEBUG"],
         token_limit=ctx.obj["TOKEN_LIMIT"],
         session=ctx.obj["SESSION"],
         messages=messages,
     )
 
 
 @cli.command(help="Choose a previous conversation to load.")
@@ -118,15 +100,15 @@
         + Style.RESET_ALL
     )
 
     if conv.is_conversations_empty(files=conversations, message=msg):
         return
 
     # setup file names auto-completion
-    completer = WordCompleter(conversations)
+    completer = WordCompleter(conversations, ignore_case=True)
     print_utils.print_slowly(print_utils.CONVERSATIONS_INIT_MESSAGE)
 
     # print conversations list
     for conversation in conversations:
         print_utils.print_slowly(Style.BRIGHT + "- " + conversation)
 
     # prompt user to choose a conversation and load it into messages
@@ -159,26 +141,27 @@
         + "- - - - - - - - - - - - - - - - - - - - - - - - -"
         + Style.RESET_ALL
     )
 
     messages.append(config.INIT_WELCOME_BACK_MESSAGE)
     total_usage = chat_utils.num_tokens_from_messages(messages)
 
-    if chat_utils.exceeding_token_limit(total_usage, config.API_TOKEN_LIMIT):
+    token_limit = ctx.obj["TOKEN_LIMIT"]
+
+    if chat_utils.exceeding_token_limit(total_usage, token_limit):
         messages, total_usage = chat_utils.reduce_tokens(
             messages=messages,
             total_usage=total_usage,
-            token_limit=config.API_TOKEN_LIMIT,
+            token_limit=token_limit,
         )
 
     chat_utils.welcome_message(messages=messages)
 
     chat_utils.chat_loop(
-        debug=ctx.obj["DEBUG"],
-        token_limit=ctx.obj["TOKEN_LIMIT"],
+        token_limit=token_limit,
         session=ctx.obj["SESSION"],
         messages=messages,
         conversation_name=conversation,
     )
 
 
 @click.command(help="Choose a previous conversation to load.")
@@ -195,15 +178,15 @@
         + Style.RESET_ALL
     )
 
     if conv.is_conversations_empty(files=conversations, message=msg):
         return
 
     # setup file names auto completion
-    completer = WordCompleter(conversations)
+    completer = WordCompleter(conversations, ignore_case=True)
     print_utils.print_slowly(print_utils.CONVERSATIONS_INIT_MESSAGE)
 
     # print conversations list
     for conversation in conversations:
         print_utils.print_slowly("- " + conversation)
 
     # prompt user to choose a conversation and delete it
@@ -225,17 +208,17 @@
                 + Fore.WHITE
                 + conversation
                 + Fore.LIGHTBLUE_EX
                 + " deleted! **"
                 + Style.RESET_ALL
             )
 
-            # update conversations list
-            conversations = conv.get_conversations()
-            completer = WordCompleter(conversations)
+            # delete conversation from conversations list
+            conversations.remove(conversation)
+            completer = WordCompleter(conversations, ignore_case=True)
         else:
             print_utils.print_slowly(
                 Style.BRIGHT
                 + Fore.RED
                 + "\n** Conversation not found! **"
                 + Style.RESET_ALL
             )
```

### Comparing `terminalgpt-1.0.8/terminalgpt/print_utils.py` & `terminalgpt-1.0.9/terminalgpt/print_utils.py`

 * *Files identical despite different names*

### Comparing `terminalgpt-1.0.8/PKG-INFO` & `terminalgpt-1.0.9/PKG-INFO`

 * *Files 8% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: terminalgpt
-Version: 1.0.8
+Version: 1.0.9
 Summary: AI chat asistent in your terminal powered by OpenAI GPT-3.5
 Keywords: ai,chat,terminal,openai,gpt3,chatGPT,assistant,gpt3.5,terminalGPT,gpt-3.5-turbo
 Author: Adam Yodinsky
 Author-email: 27074934+adamyodinsky@users.noreply.github.com
 Requires-Python: >=3.9,<4.0
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.9
@@ -34,27 +34,29 @@
 
 ---
 
 ## Why?
 
 Some advantages of using TerminalGPT over the chatGPT browser-based app:
 
-1. It doesn't disconnect like the browser-based app, so you can leave it running in a terminal session on the side without losing context.
-2. It's highly available and can be used whenever you need it.
-3. It's faster with replies than the browser-based app.
-4. You can use TerminalGPT with your IDE terminal, which means you won't have to constantly switch between your browser and your IDE when you have questions.
-5. TerminalGPT's answers are tailored to your machine's operating system, distribution, and chip-set architecture.
-6. Doesn't use your conversation data for training the model (unlike the browser-based app).
-7. Your conversations are stored locally on your machine, so only you can access them.
+- It doesn't disconnect like the browser-based app, so you can leave it running in a terminal session on the side without losing context.
+- It's highly available and can be used whenever you need it.
+- It's faster with replies than the browser-based app.
+- You can use TerminalGPT with your IDE terminal, which means you won't have to constantly switch between your browser and your IDE when you have questions.
+- TerminalGPT's answers are tailored to your machine's operating system, distribution, and chip-set architecture
+- Doesn't use your conversation data for training the model (unlike the browser-based app).
+- Your conversations are stored locally on your machine, so only you can access them.
 
 ## Pre-requisites
 
-1. Python 3.6 or higher
-2. An OpenAI Account and API key (It's free for personal use).
-[How to create OpenAI API keys](https://elephas.app/blog/how-to-create-openai-api-keys-cl5c4f21d281431po7k8fgyol0)
+- Python 3.6 or higher
+- An OpenAI Account and API key (It's free for personal use).
+   1. Sign up at <https://beta.openai.com/signup> using email or Google/Microsoft account.
+   2. Go to <https://beta.openai.com/account/api-keys> or click on "View API keys" in the menu to get your API key.
+   For a more detailed guide on how to create an OpenAI API key, click [here](https://elephas.app/blog/how-to-create-openai-api-keys-cl5c4f21d281431po7k8fgyol0).
 
 ## Installation
 
 1. Install the latest TerminalGPT with pip install.
 
 ```sh
 pip install terminalgpt -U
@@ -74,16 +76,14 @@
 
 ## Usage
 
 ```sh
 Usage: terminalgpt [OPTIONS] COMMAND [ARGS]...
 
 Options:
-  --debug                Prints amounts of tokens used.
-  --token-limit INTEGER  Set the token limit between 1024 and 4096.
   --help                 Show this message and exit.
 
 Commands:
   new      Start a new conversation.
   load     Choose a previous conversation to load.
   delete   Choose a previous conversation to load.
   install  Creating a secret api key for the chatbot.
@@ -109,24 +109,14 @@
 
 Delete previous conversations:
 
 ```sh
 terminalgpt delete
 ```
 
-### Using flags
-
-Using flags, you can set the token limit and debug mode. the flags should be used before the command.
-
-For example:
-
-```sh
-terminalgpt --token-limit 2048 --debug new
-```
-
 ---
 
 ## Future Plans
 
 1. Support multiline input.
 2. Support optional vim input mode.
 3. Auto-completion for all commands.
```

