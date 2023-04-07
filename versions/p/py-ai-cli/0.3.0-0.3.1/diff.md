# Comparing `tmp/py-ai-cli-0.3.0.tar.gz` & `tmp/py-ai-cli-0.3.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "py-ai-cli-0.3.0.tar", last modified: Fri Apr  7 14:07:16 2023, max compression
+gzip compressed data, was "py-ai-cli-0.3.1.tar", last modified: Fri Apr  7 14:11:51 2023, max compression
```

## Comparing `py-ai-cli-0.3.0.tar` & `py-ai-cli-0.3.1.tar`

### file list

```diff
@@ -1,12 +1,12 @@
--rw-r--r--   0        0        0     1663 2023-04-07 14:06:57.329149 py-ai-cli-0.3.0/CHANGELOG.md
--rw-r--r--   0        0        0     3155 2023-04-07 14:06:57.329149 py-ai-cli-0.3.0/README.md
--rw-r--r--   0        0        0     3940 2023-04-07 14:06:57.329149 py-ai-cli-0.3.0/README_ja.md
--rw-r--r--   0        0        0     2922 2023-04-07 14:06:57.329149 py-ai-cli-0.3.0/README_zh.md
--rw-r--r--   0        0        0     2021 2023-04-07 14:06:57.705180 py-ai-cli-0.3.0/pyproject.toml
--rw-r--r--   0        0        0      690 2023-04-07 14:06:57.705180 py-ai-cli-0.3.0/src/ai_cli/__init__.py
--rw-r--r--   0        0        0     8143 2023-04-07 14:06:57.705180 py-ai-cli-0.3.0/src/ai_cli/bot/__init__.py
--rw-r--r--   0        0        0      195 2023-04-07 14:06:57.705180 py-ai-cli-0.3.0/src/ai_cli/bot/token.py
--rwxr-xr-x   0        0        0    13579 2023-04-07 14:06:57.705180 py-ai-cli-0.3.0/src/ai_cli/cli.py
--rw-r--r--   0        0        0     4468 2023-04-07 14:06:57.705180 py-ai-cli-0.3.0/src/ai_cli/git.py
--rw-r--r--   0        0        0     2822 2023-04-07 14:06:57.705180 py-ai-cli-0.3.0/src/ai_cli/setting.py
--rw-r--r--   0        0        0     3631 1970-01-01 00:00:00.000000 py-ai-cli-0.3.0/PKG-INFO
+-rw-r--r--   0        0        0     1663 2023-04-07 14:11:32.585311 py-ai-cli-0.3.1/CHANGELOG.md
+-rw-r--r--   0        0        0     3155 2023-04-07 14:11:32.585311 py-ai-cli-0.3.1/README.md
+-rw-r--r--   0        0        0     3940 2023-04-07 14:11:32.585311 py-ai-cli-0.3.1/README_ja.md
+-rw-r--r--   0        0        0     2922 2023-04-07 14:11:32.585311 py-ai-cli-0.3.1/README_zh.md
+-rw-r--r--   0        0        0     2021 2023-04-07 14:11:32.953309 py-ai-cli-0.3.1/pyproject.toml
+-rw-r--r--   0        0        0      690 2023-04-07 14:11:32.953309 py-ai-cli-0.3.1/src/ai_cli/__init__.py
+-rw-r--r--   0        0        0     8231 2023-04-07 14:11:32.953309 py-ai-cli-0.3.1/src/ai_cli/bot/__init__.py
+-rw-r--r--   0        0        0      195 2023-04-07 14:11:32.953309 py-ai-cli-0.3.1/src/ai_cli/bot/token.py
+-rwxr-xr-x   0        0        0    13579 2023-04-07 14:11:32.953309 py-ai-cli-0.3.1/src/ai_cli/cli.py
+-rw-r--r--   0        0        0     4468 2023-04-07 14:11:32.953309 py-ai-cli-0.3.1/src/ai_cli/git.py
+-rw-r--r--   0        0        0     2822 2023-04-07 14:11:32.953309 py-ai-cli-0.3.1/src/ai_cli/setting.py
+-rw-r--r--   0        0        0     3631 1970-01-01 00:00:00.000000 py-ai-cli-0.3.1/PKG-INFO
```

### Comparing `py-ai-cli-0.3.0/CHANGELOG.md` & `py-ai-cli-0.3.1/CHANGELOG.md`

 * *Files identical despite different names*

### Comparing `py-ai-cli-0.3.0/README.md` & `py-ai-cli-0.3.1/README.md`

 * *Files identical despite different names*

### Comparing `py-ai-cli-0.3.0/README_ja.md` & `py-ai-cli-0.3.1/README_ja.md`

 * *Files identical despite different names*

### Comparing `py-ai-cli-0.3.0/README_zh.md` & `py-ai-cli-0.3.1/README_zh.md`

 * *Files identical despite different names*

### Comparing `py-ai-cli-0.3.0/pyproject.toml` & `py-ai-cli-0.3.1/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -100,15 +100,15 @@
     "pysocks>=1.7.1",
     "pyperclip>=1.8.2",
     "EdgeGPT>=0.1.22.1",
     "tiktoken>=0.3.3",
 ]
 requires-python = ">=3.8"
 readme = "README.md"
-version = "0.3.0"
+version = "0.3.1"
 
 [project.license]
 text = "MIT"
 
 [project.urls]
 Repository = "https://github.com/yufeikang/ai-cli"
 Documentation = "https://github.com/yufeikang/ai-cli/blob/main/README.md"
```

### Comparing `py-ai-cli-0.3.0/src/ai_cli/__init__.py` & `py-ai-cli-0.3.1/src/ai_cli/__init__.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-__version__ = "0.3.0"
+__version__ = "0.3.1"
 
 import logging
 import os
 from logging.handlers import RotatingFileHandler
 from pathlib import Path
 
 HOME = Path.home()
```

### Comparing `py-ai-cli-0.3.0/src/ai_cli/bot/__init__.py` & `py-ai-cli-0.3.1/src/ai_cli/bot/__init__.py`

 * *Files 2% similar despite different names*

```diff
@@ -174,14 +174,16 @@
     def update_conversation(self, response: dict):
         throttling = response.get("item").get("throttling")
         if throttling:
             self.max_conversation = throttling.get("maxNumUserMessagesInConversation")
             self.current_conversation = throttling.get("numUserMessagesInConversation")
 
     def should_summarize(self) -> bool:
+        if self.max_conversation is None:
+            return super().should_summarize()
         if self.current_conversation + 1 >= self.max_conversation:
             logger.info(
                 f"Conversation count: {self.current_conversation + 1} >= {self.max_conversation}, should summarize"
             )
             return True
         return super().should_summarize()
```

### Comparing `py-ai-cli-0.3.0/src/ai_cli/cli.py` & `py-ai-cli-0.3.1/src/ai_cli/cli.py`

 * *Files identical despite different names*

### Comparing `py-ai-cli-0.3.0/src/ai_cli/git.py` & `py-ai-cli-0.3.1/src/ai_cli/git.py`

 * *Files identical despite different names*

### Comparing `py-ai-cli-0.3.0/src/ai_cli/setting.py` & `py-ai-cli-0.3.1/src/ai_cli/setting.py`

 * *Files identical despite different names*

### Comparing `py-ai-cli-0.3.0/PKG-INFO` & `py-ai-cli-0.3.1/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: py_ai_cli
-Version: 0.3.0
+Version: 0.3.1
 Summary: This CLI tool allows you to easily chat with chatGPT in the command line. You can chat with it, ask questions, and even translate text. It also
 License: MIT
 Author-email: Yufei Kang <kou.uhi.x@gmail.com>
 Requires-Python: >=3.8
 Project-URL: Documentation, https://github.com/yufeikang/ai-cli/blob/main/README.md
 Project-URL: Repository, https://github.com/yufeikang/ai-cli
 Description-Content-Type: text/markdown
```

