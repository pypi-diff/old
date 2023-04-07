# Comparing `tmp/ChatGPTWeb-0.0.1.tar.gz` & `tmp/ChatGPTWeb-0.0.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "ChatGPTWeb-0.0.1.tar", last modified: Fri Apr  7 13:42:24 2023, max compression
+gzip compressed data, was "ChatGPTWeb-0.0.2.tar", last modified: Fri Apr  7 14:01:11 2023, max compression
```

## Comparing `ChatGPTWeb-0.0.1.tar` & `ChatGPTWeb-0.0.2.tar`

### file list

```diff
@@ -1,17 +1,17 @@
-drwxrwxrwx   0        0        0        0 2023-04-07 13:42:24.652016 ChatGPTWeb-0.0.1/
-drwxrwxrwx   0        0        0        0 2023-04-07 13:42:24.647016 ChatGPTWeb-0.0.1/ChatGPTWeb/
--rw-rw-rw-   0        0        0    11588 2023-04-07 13:42:01.000000 ChatGPTWeb-0.0.1/ChatGPTWeb/GPT.py
--rw-rw-rw-   0        0        0       48 2023-04-07 13:23:59.000000 ChatGPTWeb-0.0.1/ChatGPTWeb/__init__.py
--rw-rw-rw-   0        0        0     1117 2023-04-07 13:22:56.000000 ChatGPTWeb-0.0.1/ChatGPTWeb/__main__.py
--rw-rw-rw-   0        0        0     4692 2023-04-07 13:14:27.000000 ChatGPTWeb-0.0.1/ChatGPTWeb/config.py
-drwxrwxrwx   0        0        0        0 2023-04-07 13:42:24.650016 ChatGPTWeb-0.0.1/ChatGPTWeb.egg-info/
--rw-rw-rw-   0        0        0      620 2023-04-07 13:42:24.000000 ChatGPTWeb-0.0.1/ChatGPTWeb.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      280 2023-04-07 13:42:24.000000 ChatGPTWeb-0.0.1/ChatGPTWeb.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-07 13:42:24.000000 ChatGPTWeb-0.0.1/ChatGPTWeb.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       22 2023-04-07 13:42:24.000000 ChatGPTWeb-0.0.1/ChatGPTWeb.egg-info/requires.txt
--rw-rw-rw-   0        0        0       11 2023-04-07 13:42:24.000000 ChatGPTWeb-0.0.1/ChatGPTWeb.egg-info/top_level.txt
--rw-rw-rw-   0        0        0    35823 2023-04-07 06:03:43.000000 ChatGPTWeb-0.0.1/LICENSE
--rw-rw-rw-   0        0        0      620 2023-04-07 13:42:24.651017 ChatGPTWeb-0.0.1/PKG-INFO
--rw-rw-rw-   0        0        0      263 2023-04-07 13:40:59.000000 ChatGPTWeb-0.0.1/README.md
--rw-rw-rw-   0        0        0       42 2023-04-07 13:42:24.652016 ChatGPTWeb-0.0.1/setup.cfg
--rw-rw-rw-   0        0        0      748 2023-04-07 13:42:22.000000 ChatGPTWeb-0.0.1/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-07 14:01:11.651036 ChatGPTWeb-0.0.2/
+drwxrwxrwx   0        0        0        0 2023-04-07 14:01:11.646659 ChatGPTWeb-0.0.2/ChatGPTWeb/
+-rw-rw-rw-   0        0        0    11588 2023-04-07 13:42:01.000000 ChatGPTWeb-0.0.2/ChatGPTWeb/ChatGPTWeb.py
+-rw-rw-rw-   0        0        0       55 2023-04-07 14:00:21.000000 ChatGPTWeb-0.0.2/ChatGPTWeb/__init__.py
+-rw-rw-rw-   0        0        0     1135 2023-04-07 14:00:31.000000 ChatGPTWeb-0.0.2/ChatGPTWeb/__main__.py
+-rw-rw-rw-   0        0        0     4692 2023-04-07 13:14:27.000000 ChatGPTWeb-0.0.2/ChatGPTWeb/config.py
+drwxrwxrwx   0        0        0        0 2023-04-07 14:01:11.648659 ChatGPTWeb-0.0.2/ChatGPTWeb.egg-info/
+-rw-rw-rw-   0        0        0      620 2023-04-07 14:01:11.000000 ChatGPTWeb-0.0.2/ChatGPTWeb.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      287 2023-04-07 14:01:11.000000 ChatGPTWeb-0.0.2/ChatGPTWeb.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-07 14:01:11.000000 ChatGPTWeb-0.0.2/ChatGPTWeb.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       22 2023-04-07 14:01:11.000000 ChatGPTWeb-0.0.2/ChatGPTWeb.egg-info/requires.txt
+-rw-rw-rw-   0        0        0       11 2023-04-07 14:01:11.000000 ChatGPTWeb-0.0.2/ChatGPTWeb.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0    35823 2023-04-07 06:03:43.000000 ChatGPTWeb-0.0.2/LICENSE
+-rw-rw-rw-   0        0        0      620 2023-04-07 14:01:11.649659 ChatGPTWeb-0.0.2/PKG-INFO
+-rw-rw-rw-   0        0        0      263 2023-04-07 13:40:59.000000 ChatGPTWeb-0.0.2/README.md
+-rw-rw-rw-   0        0        0       42 2023-04-07 14:01:11.651036 ChatGPTWeb-0.0.2/setup.cfg
+-rw-rw-rw-   0        0        0      748 2023-04-07 14:01:02.000000 ChatGPTWeb-0.0.2/setup.py
```

### Comparing `ChatGPTWeb-0.0.1/ChatGPTWeb/GPT.py` & `ChatGPTWeb-0.0.2/ChatGPTWeb/ChatGPTWeb.py`

 * *Files identical despite different names*

### Comparing `ChatGPTWeb-0.0.1/ChatGPTWeb/__main__.py` & `ChatGPTWeb-0.0.2/ChatGPTWeb/__main__.py`

 * *Files 10% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 from contextlib import asynccontextmanager,contextmanager
-from GPT import chatgpt
+from ChatGPTWeb.ChatGPTWeb import chatgpt
 from config import MsgData
 import asyncio
 import aioconsole
 
 session_token=""
 
 a = chatgpt(session_token=session_token)
```

### Comparing `ChatGPTWeb-0.0.1/ChatGPTWeb/config.py` & `ChatGPTWeb-0.0.2/ChatGPTWeb/config.py`

 * *Files identical despite different names*

### Comparing `ChatGPTWeb-0.0.1/ChatGPTWeb.egg-info/PKG-INFO` & `ChatGPTWeb-0.0.2/ChatGPTWeb.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: ChatGPTWeb
-Version: 0.0.1
+Version: 0.0.2
 Summary: a ChatGPT API,no web ui
 Home-page: https://github.com/nek0us/ChatGPT
 Author: nek0us
 Author-email: nekouss@gmail.com
 Classifier: Programming Language :: Python :: 3.9
 Classifier: License :: OSI Approved :: MIT License
 Description-Content-Type: text/markdown
```

### Comparing `ChatGPTWeb-0.0.1/LICENSE` & `ChatGPTWeb-0.0.2/LICENSE`

 * *Files identical despite different names*

### Comparing `ChatGPTWeb-0.0.1/PKG-INFO` & `ChatGPTWeb-0.0.2/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: ChatGPTWeb
-Version: 0.0.1
+Version: 0.0.2
 Summary: a ChatGPT API,no web ui
 Home-page: https://github.com/nek0us/ChatGPT
 Author: nek0us
 Author-email: nekouss@gmail.com
 Classifier: Programming Language :: Python :: 3.9
 Classifier: License :: OSI Approved :: MIT License
 Description-Content-Type: text/markdown
```

### Comparing `ChatGPTWeb-0.0.1/setup.py` & `ChatGPTWeb-0.0.2/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -3,15 +3,15 @@
 with open("README.md", "r",encoding="utf8") as readme_file:
     readme = readme_file.read()
 
 requirements = ["playwright","aioconsole"] # 这里填依赖包信息
 
 setup(
     name="ChatGPTWeb",
-    version="0.0.1",
+    version="0.0.2",
     author="nek0us",
     author_email="nekouss@gmail.com",
     description="a ChatGPT API,no web ui",
     long_description=readme,
     long_description_content_type="text/markdown",
     url="https://github.com/nek0us/ChatGPT",
     packages=find_packages(),
```

