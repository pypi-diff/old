# Comparing `tmp/bcligpt-0.1.5.tar.gz` & `tmp/bcligpt-0.2.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "bcligpt-0.1.5.tar", last modified: Thu Apr  6 10:14:18 2023, max compression
+gzip compressed data, was "bcligpt-0.2.0.tar", last modified: Thu Apr  6 10:26:55 2023, max compression
```

## Comparing `bcligpt-0.1.5.tar` & `bcligpt-0.2.0.tar`

### file list

```diff
@@ -1,16 +1,16 @@
-drwxr-xr-x   0 marco     (1000) marco     (1000)        0 2023-04-06 10:14:18.396748 bcligpt-0.1.5/
--rw-r--r--   0 marco     (1000) marco     (1000)      319 2023-04-06 10:14:18.396748 bcligpt-0.1.5/PKG-INFO
--rw-r--r--   0 marco     (1000) marco     (1000)      133 2023-04-03 14:53:27.000000 bcligpt-0.1.5/README.md
--rw-r--r--   0 marco     (1000) marco     (1000)      374 2023-04-06 10:14:14.000000 bcligpt-0.1.5/pyproject.toml
--rw-r--r--   0 marco     (1000) marco     (1000)       38 2023-04-06 10:14:18.396748 bcligpt-0.1.5/setup.cfg
-drwxr-xr-x   0 marco     (1000) marco     (1000)        0 2023-04-06 10:14:18.392748 bcligpt-0.1.5/src/
-drwxr-xr-x   0 marco     (1000) marco     (1000)        0 2023-04-06 10:14:18.396748 bcligpt-0.1.5/src/bcligpt/
--rw-r--r--   0 marco     (1000) marco     (1000)       48 2023-04-03 15:22:45.000000 bcligpt-0.1.5/src/bcligpt/__init__.py
--rw-r--r--   0 marco     (1000) marco     (1000)     2943 2023-04-06 10:02:30.000000 bcligpt-0.1.5/src/bcligpt/app.py
-drwxr-xr-x   0 marco     (1000) marco     (1000)        0 2023-04-06 10:14:18.396748 bcligpt-0.1.5/src/bcligpt.egg-info/
--rw-r--r--   0 marco     (1000) marco     (1000)      319 2023-04-06 10:14:18.000000 bcligpt-0.1.5/src/bcligpt.egg-info/PKG-INFO
--rw-r--r--   0 marco     (1000) marco     (1000)      279 2023-04-06 10:14:18.000000 bcligpt-0.1.5/src/bcligpt.egg-info/SOURCES.txt
--rw-r--r--   0 marco     (1000) marco     (1000)        1 2023-04-06 10:14:18.000000 bcligpt-0.1.5/src/bcligpt.egg-info/dependency_links.txt
--rw-r--r--   0 marco     (1000) marco     (1000)       42 2023-04-06 10:14:18.000000 bcligpt-0.1.5/src/bcligpt.egg-info/entry_points.txt
--rw-r--r--   0 marco     (1000) marco     (1000)       21 2023-04-06 10:14:18.000000 bcligpt-0.1.5/src/bcligpt.egg-info/requires.txt
--rw-r--r--   0 marco     (1000) marco     (1000)        8 2023-04-06 10:14:18.000000 bcligpt-0.1.5/src/bcligpt.egg-info/top_level.txt
+drwxr-xr-x   0 marco     (1000) marco     (1000)        0 2023-04-06 10:26:55.717548 bcligpt-0.2.0/
+-rw-r--r--   0 marco     (1000) marco     (1000)      319 2023-04-06 10:26:55.717548 bcligpt-0.2.0/PKG-INFO
+-rw-r--r--   0 marco     (1000) marco     (1000)      133 2023-04-03 14:53:27.000000 bcligpt-0.2.0/README.md
+-rw-r--r--   0 marco     (1000) marco     (1000)      374 2023-04-06 10:26:52.000000 bcligpt-0.2.0/pyproject.toml
+-rw-r--r--   0 marco     (1000) marco     (1000)       38 2023-04-06 10:26:55.717548 bcligpt-0.2.0/setup.cfg
+drwxr-xr-x   0 marco     (1000) marco     (1000)        0 2023-04-06 10:26:55.717548 bcligpt-0.2.0/src/
+drwxr-xr-x   0 marco     (1000) marco     (1000)        0 2023-04-06 10:26:55.717548 bcligpt-0.2.0/src/bcligpt/
+-rw-r--r--   0 marco     (1000) marco     (1000)       48 2023-04-03 15:22:45.000000 bcligpt-0.2.0/src/bcligpt/__init__.py
+-rw-r--r--   0 marco     (1000) marco     (1000)     3034 2023-04-06 10:22:59.000000 bcligpt-0.2.0/src/bcligpt/app.py
+drwxr-xr-x   0 marco     (1000) marco     (1000)        0 2023-04-06 10:26:55.717548 bcligpt-0.2.0/src/bcligpt.egg-info/
+-rw-r--r--   0 marco     (1000) marco     (1000)      319 2023-04-06 10:26:55.000000 bcligpt-0.2.0/src/bcligpt.egg-info/PKG-INFO
+-rw-r--r--   0 marco     (1000) marco     (1000)      279 2023-04-06 10:26:55.000000 bcligpt-0.2.0/src/bcligpt.egg-info/SOURCES.txt
+-rw-r--r--   0 marco     (1000) marco     (1000)        1 2023-04-06 10:26:55.000000 bcligpt-0.2.0/src/bcligpt.egg-info/dependency_links.txt
+-rw-r--r--   0 marco     (1000) marco     (1000)       42 2023-04-06 10:26:55.000000 bcligpt-0.2.0/src/bcligpt.egg-info/entry_points.txt
+-rw-r--r--   0 marco     (1000) marco     (1000)       21 2023-04-06 10:26:55.000000 bcligpt-0.2.0/src/bcligpt.egg-info/requires.txt
+-rw-r--r--   0 marco     (1000) marco     (1000)        8 2023-04-06 10:26:55.000000 bcligpt-0.2.0/src/bcligpt.egg-info/top_level.txt
```

### Comparing `bcligpt-0.1.5/src/bcligpt/app.py` & `bcligpt-0.2.0/src/bcligpt/app.py`

 * *Files 8% similar despite different names*

```diff
@@ -20,16 +20,17 @@
     encoding = tiktoken.encoding_for_model(model)
     result = openai.ChatCompletion.create(
       model=model,
       messages=messages,)
 
     tokens = 0
     console = Console()
+    cost = 0.00
     while True:
-        message = input(f"(Tokens: {tokens}) - You: ")
+        message = input(f"(Spent: ${'{:.2f}'.format(cost)}) (Tokens: {tokens}) - You: ")
         message_token_count = len(encoding.encode(message))
         tokens += message_token_count
         while tokens > 3500:
             popped_message = messages.pop(1)
             tokens -= len(encoding.encode(popped_message["content"]))
         messages.append({"role": "user", "content": message})
 
@@ -59,12 +60,13 @@
                             print("\033[F", end="")
                 if finish_reason == "stop":
                     for i in range(new_lines):
                         print("\n", end="")
             message_token_count = len(encoding.encode(full_content))
             tokens += message_token_count
             messages.append({"role": "assistant", "content": full_content})
+            cost = tokens * 0.002 / 1000
         except InvalidRequestError as e:
             print("Error: ", e)
             while tokens > 3500:
                 popped_message = messages.pop(1)
                 tokens -= len(encoding.encode(popped_message["content"]))
```

