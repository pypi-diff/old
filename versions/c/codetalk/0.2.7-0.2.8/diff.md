# Comparing `tmp/codetalk-0.2.7.tar.gz` & `tmp/codetalk-0.2.8.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "codetalk-0.2.7.tar", last modified: Mon Apr  3 07:05:47 2023, max compression
+gzip compressed data, was "codetalk-0.2.8.tar", last modified: Thu Apr  6 18:44:51 2023, max compression
```

## Comparing `codetalk-0.2.7.tar` & `codetalk-0.2.8.tar`

### file list

```diff
@@ -1,28 +1,28 @@
-drwxr-xr-x   0 albert     (501) staff       (20)        0 2023-04-03 07:05:47.020026 codetalk-0.2.7/
--rw-r--r--   0 albert     (501) staff       (20)      557 2023-03-29 20:07:15.000000 codetalk-0.2.7/LICENSE.txt
--rw-r--r--   0 albert     (501) staff       (20)      896 2023-04-03 07:05:47.019903 codetalk-0.2.7/PKG-INFO
--rw-r--r--   0 albert     (501) staff       (20)      749 2023-03-30 03:44:55.000000 codetalk-0.2.7/README.md
--rw-r--r--   0 albert     (501) staff       (20)       38 2023-04-03 07:05:47.020059 codetalk-0.2.7/setup.cfg
--rw-r--r--   0 albert     (501) staff       (20)      897 2023-04-03 05:54:29.000000 codetalk-0.2.7/setup.py
-drwxr-xr-x   0 albert     (501) staff       (20)        0 2023-04-03 07:05:47.017478 codetalk-0.2.7/src/
-drwxr-xr-x   0 albert     (501) staff       (20)        0 2023-04-03 07:05:47.018939 codetalk-0.2.7/src/codetalk/
--rw-r--r--   0 albert     (501) staff       (20)        0 2023-03-29 20:07:15.000000 codetalk-0.2.7/src/codetalk/__init__.py
-drwxr-xr-x   0 albert     (501) staff       (20)        0 2023-04-03 07:05:47.019768 codetalk-0.2.7/src/codetalk/assets/
--rw-r--r--   0 albert     (501) staff       (20)      571 2023-03-29 20:07:15.000000 codetalk-0.2.7/src/codetalk/assets/logo.txt
--rw-r--r--   0 albert     (501) staff       (20)        6 2023-04-03 07:02:45.000000 codetalk-0.2.7/src/codetalk/assets/version.txt
--rw-r--r--   0 albert     (501) staff       (20)     4556 2023-04-03 06:53:32.000000 codetalk-0.2.7/src/codetalk/backend.py
--rw-r--r--   0 albert     (501) staff       (20)      624 2023-03-29 20:07:15.000000 codetalk-0.2.7/src/codetalk/config.py
--rw-r--r--   0 albert     (501) staff       (20)     6365 2023-03-30 16:48:48.000000 codetalk-0.2.7/src/codetalk/filtration.py
--rw-r--r--   0 albert     (501) staff       (20)     6116 2023-04-03 05:28:16.000000 codetalk-0.2.7/src/codetalk/formatter.py
--rw-r--r--   0 albert     (501) staff       (20)     1677 2023-03-29 20:07:15.000000 codetalk-0.2.7/src/codetalk/index.py
--rw-r--r--   0 albert     (501) staff       (20)      744 2023-03-29 20:07:15.000000 codetalk-0.2.7/src/codetalk/logconf.py
--rw-r--r--   0 albert     (501) staff       (20)     4434 2023-04-03 06:58:29.000000 codetalk-0.2.7/src/codetalk/main.py
--rw-r--r--   0 albert     (501) staff       (20)     1462 2023-03-29 20:07:15.000000 codetalk-0.2.7/src/codetalk/spinner.py
--rw-r--r--   0 albert     (501) staff       (20)     2692 2023-04-03 05:28:16.000000 codetalk-0.2.7/src/codetalk/subcommand.py
-drwxr-xr-x   0 albert     (501) staff       (20)        0 2023-04-03 07:05:47.019559 codetalk-0.2.7/src/codetalk.egg-info/
--rw-r--r--   0 albert     (501) staff       (20)      896 2023-04-03 07:05:46.000000 codetalk-0.2.7/src/codetalk.egg-info/PKG-INFO
--rw-r--r--   0 albert     (501) staff       (20)      552 2023-04-03 07:05:46.000000 codetalk-0.2.7/src/codetalk.egg-info/SOURCES.txt
--rw-r--r--   0 albert     (501) staff       (20)        1 2023-04-03 07:05:46.000000 codetalk-0.2.7/src/codetalk.egg-info/dependency_links.txt
--rw-r--r--   0 albert     (501) staff       (20)       48 2023-04-03 07:05:46.000000 codetalk-0.2.7/src/codetalk.egg-info/entry_points.txt
--rw-r--r--   0 albert     (501) staff       (20)       65 2023-04-03 07:05:46.000000 codetalk-0.2.7/src/codetalk.egg-info/requires.txt
--rw-r--r--   0 albert     (501) staff       (20)        9 2023-04-03 07:05:46.000000 codetalk-0.2.7/src/codetalk.egg-info/top_level.txt
+drwxr-xr-x   0 albert     (501) staff       (20)        0 2023-04-06 18:44:51.215477 codetalk-0.2.8/
+-rw-r--r--   0 albert     (501) staff       (20)      557 2023-03-29 20:07:15.000000 codetalk-0.2.8/LICENSE.txt
+-rw-r--r--   0 albert     (501) staff       (20)      896 2023-04-06 18:44:51.215359 codetalk-0.2.8/PKG-INFO
+-rw-r--r--   0 albert     (501) staff       (20)      749 2023-03-30 03:44:55.000000 codetalk-0.2.8/README.md
+-rw-r--r--   0 albert     (501) staff       (20)       38 2023-04-06 18:44:51.215516 codetalk-0.2.8/setup.cfg
+-rw-r--r--   0 albert     (501) staff       (20)      897 2023-04-03 05:54:29.000000 codetalk-0.2.8/setup.py
+drwxr-xr-x   0 albert     (501) staff       (20)        0 2023-04-06 18:44:51.212449 codetalk-0.2.8/src/
+drwxr-xr-x   0 albert     (501) staff       (20)        0 2023-04-06 18:44:51.214268 codetalk-0.2.8/src/codetalk/
+-rw-r--r--   0 albert     (501) staff       (20)        0 2023-03-29 20:07:15.000000 codetalk-0.2.8/src/codetalk/__init__.py
+drwxr-xr-x   0 albert     (501) staff       (20)        0 2023-04-06 18:44:51.215220 codetalk-0.2.8/src/codetalk/assets/
+-rw-r--r--   0 albert     (501) staff       (20)      571 2023-03-29 20:07:15.000000 codetalk-0.2.8/src/codetalk/assets/logo.txt
+-rw-r--r--   0 albert     (501) staff       (20)        6 2023-04-06 18:42:50.000000 codetalk-0.2.8/src/codetalk/assets/version.txt
+-rw-r--r--   0 albert     (501) staff       (20)     4292 2023-04-06 18:41:57.000000 codetalk-0.2.8/src/codetalk/backend.py
+-rw-r--r--   0 albert     (501) staff       (20)      624 2023-03-29 20:07:15.000000 codetalk-0.2.8/src/codetalk/config.py
+-rw-r--r--   0 albert     (501) staff       (20)     6366 2023-04-05 19:00:00.000000 codetalk-0.2.8/src/codetalk/filtration.py
+-rw-r--r--   0 albert     (501) staff       (20)     6126 2023-04-04 06:09:21.000000 codetalk-0.2.8/src/codetalk/formatter.py
+-rw-r--r--   0 albert     (501) staff       (20)     1677 2023-03-29 20:07:15.000000 codetalk-0.2.8/src/codetalk/index.py
+-rw-r--r--   0 albert     (501) staff       (20)      744 2023-03-29 20:07:15.000000 codetalk-0.2.8/src/codetalk/logconf.py
+-rw-r--r--   0 albert     (501) staff       (20)     4434 2023-04-03 07:58:27.000000 codetalk-0.2.8/src/codetalk/main.py
+-rw-r--r--   0 albert     (501) staff       (20)     1462 2023-03-29 20:07:15.000000 codetalk-0.2.8/src/codetalk/spinner.py
+-rw-r--r--   0 albert     (501) staff       (20)     2692 2023-04-03 05:28:16.000000 codetalk-0.2.8/src/codetalk/subcommand.py
+drwxr-xr-x   0 albert     (501) staff       (20)        0 2023-04-06 18:44:51.215013 codetalk-0.2.8/src/codetalk.egg-info/
+-rw-r--r--   0 albert     (501) staff       (20)      896 2023-04-06 18:44:51.000000 codetalk-0.2.8/src/codetalk.egg-info/PKG-INFO
+-rw-r--r--   0 albert     (501) staff       (20)      552 2023-04-06 18:44:51.000000 codetalk-0.2.8/src/codetalk.egg-info/SOURCES.txt
+-rw-r--r--   0 albert     (501) staff       (20)        1 2023-04-06 18:44:51.000000 codetalk-0.2.8/src/codetalk.egg-info/dependency_links.txt
+-rw-r--r--   0 albert     (501) staff       (20)       48 2023-04-06 18:44:51.000000 codetalk-0.2.8/src/codetalk.egg-info/entry_points.txt
+-rw-r--r--   0 albert     (501) staff       (20)       65 2023-04-06 18:44:51.000000 codetalk-0.2.8/src/codetalk.egg-info/requires.txt
+-rw-r--r--   0 albert     (501) staff       (20)        9 2023-04-06 18:44:51.000000 codetalk-0.2.8/src/codetalk.egg-info/top_level.txt
```

### Comparing `codetalk-0.2.7/LICENSE.txt` & `codetalk-0.2.8/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `codetalk-0.2.7/PKG-INFO` & `codetalk-0.2.8/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: codetalk
-Version: 0.2.7
+Version: 0.2.8
 Summary: Talk to your code!
 Description-Content-Type: text/markdown
 License-File: LICENSE.txt
 
 # codetalk
 
 Talk to your code!
```

### Comparing `codetalk-0.2.7/README.md` & `codetalk-0.2.8/README.md`

 * *Files identical despite different names*

### Comparing `codetalk-0.2.7/setup.py` & `codetalk-0.2.8/setup.py`

 * *Files identical despite different names*

### Comparing `codetalk-0.2.7/src/codetalk/assets/logo.txt` & `codetalk-0.2.8/src/codetalk/assets/logo.txt`

 * *Files identical despite different names*

### Comparing `codetalk-0.2.7/src/codetalk/backend.py` & `codetalk-0.2.8/src/codetalk/backend.py`

 * *Files 10% similar despite different names*

```diff
@@ -7,16 +7,18 @@
 
 from . import logconf
 from . import index
 from .config import get_config
 from .formatter import TokenFormatter
 from .spinner import spinner
 
+SERVER_ADDRESS = "https://server.codetalk.ai:8000"
+
 def codetalk_api_call(route, payload={}, use_gzip=False):
-    server = 'http://127.0.0.1:8000' if get_config('use_local') else get_config('api_address')
+    server = get_config('override_ip') or SERVER_ADDRESS
     addr = server + route
     auth_token = get_config('user_token')
     headers = {
         "Authorization": f"Bearer {auth_token}",
         "Content-Type": "application/json",
     }
 
@@ -34,15 +36,15 @@
         logging.error(f"Error when calling codetalk API: {traceback.format_exc()}")
         print("Failed to reach the Codetalk API, quitting...")
         exit(-1)
 
     return response
 
 def validate_token(token):
-    server = 'http://127.0.0.1:8000' if get_config('use_local') else get_config('api_address')
+    server = get_config('override_ip') or SERVER_ADDRESS
     addr = server + '/validate'
     headers = {'Authorization': f'Bearer {token}'}
 
     try:
         response = requests.get(addr, headers=headers)
     except Exception as e:
         print(f"Error validating token: {e}")
@@ -89,36 +91,29 @@
 
 @spinner(text='Thinking...')
 def get_stream_client(addr, headers, data):
     response = requests.post(addr, headers=headers, json=data, stream=True)
     return sseclient.SSEClient(response)
 
 def get_response(query, messages):
-    server = 'http://127.0.0.1:8000' if get_config('use_local') else get_config('api_address')
+    server = get_config('override_ip') or SERVER_ADDRESS
     addr = server + '/respond'
 
     auth_token = get_config('user_token')
     headers = {
         "Authorization": f"Bearer {auth_token}",
         'Accept': 'text/event-stream',
     }
 
     data = {
         'messages': messages,
         'query': query,
         'project_id': get_config('current_project'),
     }
 
-    # TODO is this needed?
-    # if response.status_code != 200:
-    #     if len(messages) == 1:
-    #         raise
-    #     messages.pop(0)
-    #     return stream_chat_completion(messages, model)
-
     client = get_stream_client(addr, headers, data)
     if client == '__KEYBOARD_INTERRUPT':
         return client
 
     tokens = []
     try:
         _stream_message(client, tokens)
```

### Comparing `codetalk-0.2.7/src/codetalk/config.py` & `codetalk-0.2.8/src/codetalk/config.py`

 * *Files identical despite different names*

### Comparing `codetalk-0.2.7/src/codetalk/filtration.py` & `codetalk-0.2.8/src/codetalk/filtration.py`

 * *Files 1% similar despite different names*

```diff
@@ -42,15 +42,15 @@
             fp.readline()
     except UnicodeDecodeError:
         return True
     return False
 
 def is_ignored_dir(filepath):
     ignored_dirs = [re.compile(r) for r in [
-        r"(\/)?.git\/",
+        r"(\/)?\.git\/",
         r"(\/)?node_modules/",
         r"(\/)?venv(\d)?/",
     ]]
 
     return any(expr.search(filepath) for expr in ignored_dirs)
 
 def valid_mime(filepath):
```

### Comparing `codetalk-0.2.7/src/codetalk/formatter.py` & `codetalk-0.2.8/src/codetalk/formatter.py`

 * *Files 1% similar despite different names*

```diff
@@ -91,15 +91,15 @@
         sys.stdout.flush()
 
     def is_keyword(self, token):
         keywords = set(['if', 'else', 'for', 'while', 'return', 'class',
             'def', 'function', 'import', 'from', 'export', 'const',
             'let', 'var', 'switch', 'case', 'try', 'catch', 'finally',
             'break', 'continue', 'with', 'as', 'in', 'match', 'case',
-            'elif',
+            'elif', 'except',
         ])
 
         return token in keywords
 
     def is_typeval(self, token):
         types_and_values = set(['int', 'float', 'str', 'bool',
             'None', 'True', 'False','complex', 'tuple', 'list',
```

### Comparing `codetalk-0.2.7/src/codetalk/index.py` & `codetalk-0.2.8/src/codetalk/index.py`

 * *Files identical despite different names*

### Comparing `codetalk-0.2.7/src/codetalk/logconf.py` & `codetalk-0.2.8/src/codetalk/logconf.py`

 * *Files identical despite different names*

### Comparing `codetalk-0.2.7/src/codetalk/main.py` & `codetalk-0.2.8/src/codetalk/main.py`

 * *Files identical despite different names*

### Comparing `codetalk-0.2.7/src/codetalk/spinner.py` & `codetalk-0.2.8/src/codetalk/spinner.py`

 * *Files identical despite different names*

### Comparing `codetalk-0.2.7/src/codetalk/subcommand.py` & `codetalk-0.2.8/src/codetalk/subcommand.py`

 * *Files identical despite different names*

### Comparing `codetalk-0.2.7/src/codetalk.egg-info/PKG-INFO` & `codetalk-0.2.8/src/codetalk.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: codetalk
-Version: 0.2.7
+Version: 0.2.8
 Summary: Talk to your code!
 Description-Content-Type: text/markdown
 License-File: LICENSE.txt
 
 # codetalk
 
 Talk to your code!
```

### Comparing `codetalk-0.2.7/src/codetalk.egg-info/SOURCES.txt` & `codetalk-0.2.8/src/codetalk.egg-info/SOURCES.txt`

 * *Files identical despite different names*

