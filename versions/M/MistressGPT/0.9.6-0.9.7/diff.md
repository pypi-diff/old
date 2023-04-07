# Comparing `tmp/MistressGPT-0.9.6.tar.gz` & `tmp/MistressGPT-0.9.7.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "MistressGPT-0.9.6.tar", last modified: Fri Apr  7 00:40:45 2023, max compression
+gzip compressed data, was "MistressGPT-0.9.7.tar", last modified: Fri Apr  7 00:59:50 2023, max compression
```

## Comparing `MistressGPT-0.9.6.tar` & `MistressGPT-0.9.7.tar`

### file list

```diff
@@ -1,30 +1,30 @@
-drwxr-xr-x   0 huzi       (501) staff       (20)        0 2023-04-07 00:40:45.532644 MistressGPT-0.9.6/
-drwxr-xr-x   0 huzi       (501) staff       (20)        0 2023-04-07 00:40:45.528035 MistressGPT-0.9.6/MistressGPT.egg-info/
--rw-r--r--   0 huzi       (501) staff       (20)     1410 2023-04-07 00:40:45.000000 MistressGPT-0.9.6/MistressGPT.egg-info/PKG-INFO
--rw-r--r--   0 huzi       (501) staff       (20)      648 2023-04-07 00:40:45.000000 MistressGPT-0.9.6/MistressGPT.egg-info/SOURCES.txt
--rw-r--r--   0 huzi       (501) staff       (20)        1 2023-04-07 00:40:45.000000 MistressGPT-0.9.6/MistressGPT.egg-info/dependency_links.txt
--rw-r--r--   0 huzi       (501) staff       (20)       63 2023-04-07 00:40:45.000000 MistressGPT-0.9.6/MistressGPT.egg-info/entry_points.txt
--rw-r--r--   0 huzi       (501) staff       (20)      102 2023-04-07 00:40:45.000000 MistressGPT-0.9.6/MistressGPT.egg-info/requires.txt
--rw-r--r--   0 huzi       (501) staff       (20)       13 2023-04-07 00:40:45.000000 MistressGPT-0.9.6/MistressGPT.egg-info/top_level.txt
--rw-r--r--   0 huzi       (501) staff       (20)     1410 2023-04-07 00:40:45.532498 MistressGPT-0.9.6/PKG-INFO
--rw-r--r--   0 huzi       (501) staff       (20)     1261 2023-04-06 00:01:40.000000 MistressGPT-0.9.6/README.md
-drwxr-xr-x   0 huzi       (501) staff       (20)        0 2023-04-07 00:40:45.529566 MistressGPT-0.9.6/chatmistress/
--rw-r--r--   0 huzi       (501) staff       (20)        0 2023-03-30 05:12:33.000000 MistressGPT-0.9.6/chatmistress/__init__.py
-drwxr-xr-x   0 huzi       (501) staff       (20)        0 2023-04-07 00:40:45.531156 MistressGPT-0.9.6/chatmistress/assets/
--rw-r--r--   0 huzi       (501) staff       (20)     2956 2023-04-02 06:57:10.000000 MistressGPT-0.9.6/chatmistress/assets/Kelpy-Codos.js
--rw-r--r--   0 huzi       (501) staff       (20)     8644 2023-04-02 06:57:10.000000 MistressGPT-0.9.6/chatmistress/assets/custom.css
--rw-r--r--   0 huzi       (501) staff       (20)       25 2023-04-02 06:57:10.000000 MistressGPT-0.9.6/chatmistress/assets/custom.js
--rw-r--r--   0 huzi       (501) staff       (20)    15406 2023-04-02 06:57:10.000000 MistressGPT-0.9.6/chatmistress/assets/favicon.ico
--rw-r--r--   0 huzi       (501) staff       (20)     4296 2023-04-06 00:11:42.000000 MistressGPT-0.9.6/chatmistress/chatmistress.py
--rw-r--r--   0 huzi       (501) staff       (20)     8871 2023-04-05 23:52:03.000000 MistressGPT-0.9.6/chatmistress/core.py
-drwxr-xr-x   0 huzi       (501) staff       (20)        0 2023-04-07 00:40:45.531630 MistressGPT-0.9.6/chatmistress/roles/
--rw-r--r--   0 huzi       (501) staff       (20)      758 2023-03-30 00:07:04.000000 MistressGPT-0.9.6/chatmistress/roles/landlady.yml
--rw-r--r--   0 huzi       (501) staff       (20)      964 2023-03-30 04:46:54.000000 MistressGPT-0.9.6/chatmistress/roles/wife.yml
-drwxr-xr-x   0 huzi       (501) staff       (20)        0 2023-04-07 00:40:45.532164 MistressGPT-0.9.6/chatmistress/templates/
--rw-r--r--   0 huzi       (501) staff       (20)     1104 2023-03-30 00:08:37.000000 MistressGPT-0.9.6/chatmistress/templates/role_play_summary.txt
--rw-r--r--   0 huzi       (501) staff       (20)     1113 2023-03-30 00:27:26.000000 MistressGPT-0.9.6/chatmistress/templates/role_play_sys.txt
--rw-r--r--   0 huzi       (501) staff       (20)     1239 2023-04-06 02:40:08.000000 MistressGPT-0.9.6/chatmistress/utils.py
--rw-r--r--   0 huzi       (501) staff       (20)     1876 2023-03-30 05:13:12.000000 MistressGPT-0.9.6/chatmistress/webbot.py
--rw-r--r--   0 huzi       (501) staff       (20)    20647 2023-04-06 00:30:48.000000 MistressGPT-0.9.6/chatmistress/webbot2.py
--rw-r--r--   0 huzi       (501) staff       (20)       38 2023-04-07 00:40:45.532689 MistressGPT-0.9.6/setup.cfg
--rw-r--r--   0 huzi       (501) staff       (20)      819 2023-04-07 00:40:32.000000 MistressGPT-0.9.6/setup.py
+drwxr-xr-x   0 huzi       (501) staff       (20)        0 2023-04-07 00:59:50.224013 MistressGPT-0.9.7/
+drwxr-xr-x   0 huzi       (501) staff       (20)        0 2023-04-07 00:59:50.219078 MistressGPT-0.9.7/MistressGPT.egg-info/
+-rw-r--r--   0 huzi       (501) staff       (20)     1410 2023-04-07 00:59:50.000000 MistressGPT-0.9.7/MistressGPT.egg-info/PKG-INFO
+-rw-r--r--   0 huzi       (501) staff       (20)      648 2023-04-07 00:59:50.000000 MistressGPT-0.9.7/MistressGPT.egg-info/SOURCES.txt
+-rw-r--r--   0 huzi       (501) staff       (20)        1 2023-04-07 00:59:50.000000 MistressGPT-0.9.7/MistressGPT.egg-info/dependency_links.txt
+-rw-r--r--   0 huzi       (501) staff       (20)       63 2023-04-07 00:59:50.000000 MistressGPT-0.9.7/MistressGPT.egg-info/entry_points.txt
+-rw-r--r--   0 huzi       (501) staff       (20)      102 2023-04-07 00:59:50.000000 MistressGPT-0.9.7/MistressGPT.egg-info/requires.txt
+-rw-r--r--   0 huzi       (501) staff       (20)       13 2023-04-07 00:59:50.000000 MistressGPT-0.9.7/MistressGPT.egg-info/top_level.txt
+-rw-r--r--   0 huzi       (501) staff       (20)     1410 2023-04-07 00:59:50.223850 MistressGPT-0.9.7/PKG-INFO
+-rw-r--r--   0 huzi       (501) staff       (20)     1261 2023-04-06 00:01:40.000000 MistressGPT-0.9.7/README.md
+drwxr-xr-x   0 huzi       (501) staff       (20)        0 2023-04-07 00:59:50.220623 MistressGPT-0.9.7/chatmistress/
+-rw-r--r--   0 huzi       (501) staff       (20)        0 2023-03-30 05:12:33.000000 MistressGPT-0.9.7/chatmistress/__init__.py
+drwxr-xr-x   0 huzi       (501) staff       (20)        0 2023-04-07 00:59:50.222474 MistressGPT-0.9.7/chatmistress/assets/
+-rw-r--r--   0 huzi       (501) staff       (20)     2956 2023-04-02 06:57:10.000000 MistressGPT-0.9.7/chatmistress/assets/Kelpy-Codos.js
+-rw-r--r--   0 huzi       (501) staff       (20)     8644 2023-04-02 06:57:10.000000 MistressGPT-0.9.7/chatmistress/assets/custom.css
+-rw-r--r--   0 huzi       (501) staff       (20)       25 2023-04-02 06:57:10.000000 MistressGPT-0.9.7/chatmistress/assets/custom.js
+-rw-r--r--   0 huzi       (501) staff       (20)    15406 2023-04-02 06:57:10.000000 MistressGPT-0.9.7/chatmistress/assets/favicon.ico
+-rw-r--r--   0 huzi       (501) staff       (20)     4508 2023-04-07 00:55:36.000000 MistressGPT-0.9.7/chatmistress/chatmistress.py
+-rw-r--r--   0 huzi       (501) staff       (20)     8871 2023-04-05 23:52:03.000000 MistressGPT-0.9.7/chatmistress/core.py
+drwxr-xr-x   0 huzi       (501) staff       (20)        0 2023-04-07 00:59:50.222952 MistressGPT-0.9.7/chatmistress/roles/
+-rw-r--r--   0 huzi       (501) staff       (20)      758 2023-03-30 00:07:04.000000 MistressGPT-0.9.7/chatmistress/roles/landlady.yml
+-rw-r--r--   0 huzi       (501) staff       (20)      964 2023-03-30 04:46:54.000000 MistressGPT-0.9.7/chatmistress/roles/wife.yml
+drwxr-xr-x   0 huzi       (501) staff       (20)        0 2023-04-07 00:59:50.223517 MistressGPT-0.9.7/chatmistress/templates/
+-rw-r--r--   0 huzi       (501) staff       (20)     1104 2023-03-30 00:08:37.000000 MistressGPT-0.9.7/chatmistress/templates/role_play_summary.txt
+-rw-r--r--   0 huzi       (501) staff       (20)     1113 2023-03-30 00:27:26.000000 MistressGPT-0.9.7/chatmistress/templates/role_play_sys.txt
+-rw-r--r--   0 huzi       (501) staff       (20)     1239 2023-04-06 02:40:08.000000 MistressGPT-0.9.7/chatmistress/utils.py
+-rw-r--r--   0 huzi       (501) staff       (20)     1876 2023-03-30 05:13:12.000000 MistressGPT-0.9.7/chatmistress/webbot.py
+-rw-r--r--   0 huzi       (501) staff       (20)    20647 2023-04-06 00:30:48.000000 MistressGPT-0.9.7/chatmistress/webbot2.py
+-rw-r--r--   0 huzi       (501) staff       (20)       38 2023-04-07 00:59:50.224056 MistressGPT-0.9.7/setup.cfg
+-rw-r--r--   0 huzi       (501) staff       (20)      819 2023-04-07 00:59:26.000000 MistressGPT-0.9.7/setup.py
```

### Comparing `MistressGPT-0.9.6/MistressGPT.egg-info/PKG-INFO` & `MistressGPT-0.9.7/MistressGPT.egg-info/PKG-INFO`

 * *Files 7% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: MistressGPT
-Version: 0.9.6
+Version: 0.9.7
 Summary: MistressGPT: 基于GPT3.5的女王聊天室
 Description-Content-Type: text/markdown
 
 # MistressGPT: 基于 GPT3.5 的女王聊天室
 
 ## 介绍
```

### Comparing `MistressGPT-0.9.6/MistressGPT.egg-info/SOURCES.txt` & `MistressGPT-0.9.7/MistressGPT.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `MistressGPT-0.9.6/PKG-INFO` & `MistressGPT-0.9.7/PKG-INFO`

 * *Files 7% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: MistressGPT
-Version: 0.9.6
+Version: 0.9.7
 Summary: MistressGPT: 基于GPT3.5的女王聊天室
 Description-Content-Type: text/markdown
 
 # MistressGPT: 基于 GPT3.5 的女王聊天室
 
 ## 介绍
```

### Comparing `MistressGPT-0.9.6/README.md` & `MistressGPT-0.9.7/README.md`

 * *Files identical despite different names*

### Comparing `MistressGPT-0.9.6/chatmistress/assets/Kelpy-Codos.js` & `MistressGPT-0.9.7/chatmistress/assets/Kelpy-Codos.js`

 * *Files identical despite different names*

### Comparing `MistressGPT-0.9.6/chatmistress/assets/custom.css` & `MistressGPT-0.9.7/chatmistress/assets/custom.css`

 * *Files identical despite different names*

### Comparing `MistressGPT-0.9.6/chatmistress/assets/favicon.ico` & `MistressGPT-0.9.7/chatmistress/assets/favicon.ico`

 * *Files identical despite different names*

### Comparing `MistressGPT-0.9.6/chatmistress/chatmistress.py` & `MistressGPT-0.9.7/chatmistress/chatmistress.py`

 * *Files 10% similar despite different names*

```diff
@@ -52,15 +52,17 @@
 
 @click.command()
 @click.argument('cmd', type=click.Choice(['cli', 'gui']))
 @click.option('--debug', default=False, help='Debug mode if True')
 @click.option('--max-token-limit', default=1000, help='temperature for openai')
 @click.option('--ext-url', default=None, help='外部模板URL')
 @click.option('--concurrency', default=20, help='外部模板URL')
-def main(cmd, debug, max_token_limit, ext_url, concurrency):
+@click.option('--inbrowser', default=True, help='是否开启浏览器')
+@click.option('--server-name', default=None, help='是否外网可用')
+def main(cmd, debug, max_token_limit, ext_url, concurrency, inbrowser, server_name):
     assert cmd in ('cli', 'gui')
 
     if 'OPENAI_API_KEY' not in os.environ:
         os.environ['OPENAI_API_KEY'] = input(
             'OPENAI_API_KEY 环境变量未设置, 请输入你的OPENAI_API_KEY: ')
 
     if ext_url is not None:
@@ -69,15 +71,16 @@
         roles: Dict[str, RoleInfo] = load_roles()
     if debug:
         max_token_limit = 200
 
     if cmd == 'gui':
         gui = creat_gui_chat(roles, debug=debug,
                              max_token_limit=max_token_limit)
-        gui.queue(concurrency_count=concurrency).launch(inbrowser=True)
+        gui.queue(concurrency_count=concurrency).launch(
+            server_name=server_name, inbrowser=inbrowser)
 
     elif cmd == 'cli':
         console = Console()
         session = PromptSession(history=FileHistory('./.role_play_history'))
         res_completer = WordCompleter([
             '!switch',
             '!exit',
```

### Comparing `MistressGPT-0.9.6/chatmistress/core.py` & `MistressGPT-0.9.7/chatmistress/core.py`

 * *Files identical despite different names*

### Comparing `MistressGPT-0.9.6/chatmistress/roles/landlady.yml` & `MistressGPT-0.9.7/chatmistress/roles/landlady.yml`

 * *Files identical despite different names*

### Comparing `MistressGPT-0.9.6/chatmistress/roles/wife.yml` & `MistressGPT-0.9.7/chatmistress/roles/wife.yml`

 * *Files identical despite different names*

### Comparing `MistressGPT-0.9.6/chatmistress/templates/role_play_summary.txt` & `MistressGPT-0.9.7/chatmistress/templates/role_play_summary.txt`

 * *Files identical despite different names*

### Comparing `MistressGPT-0.9.6/chatmistress/templates/role_play_sys.txt` & `MistressGPT-0.9.7/chatmistress/templates/role_play_sys.txt`

 * *Files identical despite different names*

### Comparing `MistressGPT-0.9.6/chatmistress/utils.py` & `MistressGPT-0.9.7/chatmistress/utils.py`

 * *Files identical despite different names*

### Comparing `MistressGPT-0.9.6/chatmistress/webbot.py` & `MistressGPT-0.9.7/chatmistress/webbot.py`

 * *Files identical despite different names*

### Comparing `MistressGPT-0.9.6/chatmistress/webbot2.py` & `MistressGPT-0.9.7/chatmistress/webbot2.py`

 * *Files identical despite different names*

### Comparing `MistressGPT-0.9.6/setup.py` & `MistressGPT-0.9.7/setup.py`

 * *Files 12% similar despite different names*

```diff
@@ -4,15 +4,15 @@
     long_description = fh.read()
 
 setup(
     name='MistressGPT',
     description='MistressGPT: 基于GPT3.5的女王聊天室',
     long_description=long_description,
     long_description_content_type='text/markdown',
-    version='0.9.6',
+    version='0.9.7',
     packages=find_packages(),
     entry_points={
         'console_scripts': [
             'mistressgpt=chatmistress.chatmistress:main'
         ]
     },
     package_data={
```

