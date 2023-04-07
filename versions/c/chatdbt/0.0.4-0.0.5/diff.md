# Comparing `tmp/chatdbt-0.0.4.tar.gz` & `tmp/chatdbt-0.0.5.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "chatdbt-0.0.4.tar", max compression
+gzip compressed data, was "chatdbt-0.0.5.tar", max compression
```

## Comparing `chatdbt-0.0.4.tar` & `chatdbt-0.0.5.tar`

### file list

```diff
@@ -1,16 +1,16 @@
--rw-r--r--   0        0        0     4293 2023-04-04 11:26:15.209241 chatdbt-0.0.4/README.md
--rw-r--r--   0        0        0      222 2023-04-06 16:00:42.469668 chatdbt-0.0.4/chatdbt/__init__.py
--rw-r--r--   0        0        0    12939 2023-04-06 14:59:42.982624 chatdbt-0.0.4/chatdbt/chat.py
--rw-r--r--   0        0        0      413 2023-03-30 09:50:02.949353 chatdbt-0.0.4/chatdbt/dbt_doc_resolver/__init__.py
--rw-r--r--   0        0        0     1024 2023-04-04 10:53:56.113000 chatdbt-0.0.4/chatdbt/dbt_doc_resolver/localfs.py
--rw-r--r--   0        0        0     2758 2023-04-06 16:00:46.107825 chatdbt-0.0.4/chatdbt/i18n.py
--rw-r--r--   0        0        0     5387 2023-04-06 15:19:40.954618 chatdbt-0.0.4/chatdbt/model.py
--rw-r--r--   0        0        0     1627 2023-04-06 15:12:59.226924 chatdbt-0.0.4/chatdbt/openai.py
--rw-r--r--   0        0        0     4471 2023-04-06 15:10:00.859901 chatdbt-0.0.4/chatdbt/shortcut.py
--rw-r--r--   0        0        0      386 2023-04-04 15:55:49.091076 chatdbt-0.0.4/chatdbt/tiktoken_provider/__init__.py
--rw-r--r--   0        0        0      868 2023-04-04 15:55:44.322642 chatdbt-0.0.4/chatdbt/tiktoken_provider/tiktoken_http_server.py
--rw-r--r--   0        0        0      625 2023-04-04 14:37:03.059444 chatdbt-0.0.4/chatdbt/vector_storage/__init__.py
--rw-r--r--   0        0        0     1670 2023-03-30 11:35:03.665857 chatdbt-0.0.4/chatdbt/vector_storage/atlas.py
--rw-r--r--   0        0        0     2670 2023-04-04 14:42:21.851573 chatdbt-0.0.4/chatdbt/vector_storage/pgvector.py
--rw-r--r--   0        0        0     2219 2023-04-06 16:01:49.751832 chatdbt-0.0.4/pyproject.toml
--rw-r--r--   0        0        0     5385 1970-01-01 00:00:00.000000 chatdbt-0.0.4/PKG-INFO
+-rw-r--r--   0        0        0     4293 2023-04-07 03:14:10.387224 chatdbt-0.0.5/README.md
+-rw-r--r--   0        0        0      222 2023-04-06 16:00:42.469668 chatdbt-0.0.5/chatdbt/__init__.py
+-rw-r--r--   0        0        0    12939 2023-04-06 16:51:14.112989 chatdbt-0.0.5/chatdbt/chat.py
+-rw-r--r--   0        0        0      413 2023-03-30 09:50:02.949353 chatdbt-0.0.5/chatdbt/dbt_doc_resolver/__init__.py
+-rw-r--r--   0        0        0     1024 2023-04-04 10:53:56.113000 chatdbt-0.0.5/chatdbt/dbt_doc_resolver/localfs.py
+-rw-r--r--   0        0        0     3149 2023-04-06 16:50:31.378054 chatdbt-0.0.5/chatdbt/i18n.py
+-rw-r--r--   0        0        0     5253 2023-04-07 03:13:59.840201 chatdbt-0.0.5/chatdbt/model.py
+-rw-r--r--   0        0        0     1627 2023-04-06 15:12:59.226924 chatdbt-0.0.5/chatdbt/openai.py
+-rw-r--r--   0        0        0     4471 2023-04-06 15:10:00.859901 chatdbt-0.0.5/chatdbt/shortcut.py
+-rw-r--r--   0        0        0      386 2023-04-04 15:55:49.091076 chatdbt-0.0.5/chatdbt/tiktoken_provider/__init__.py
+-rw-r--r--   0        0        0      868 2023-04-04 15:55:44.322642 chatdbt-0.0.5/chatdbt/tiktoken_provider/tiktoken_http_server.py
+-rw-r--r--   0        0        0      625 2023-04-04 14:37:03.059444 chatdbt-0.0.5/chatdbt/vector_storage/__init__.py
+-rw-r--r--   0        0        0     1670 2023-03-30 11:35:03.665857 chatdbt-0.0.5/chatdbt/vector_storage/atlas.py
+-rw-r--r--   0        0        0     2670 2023-04-04 14:42:21.851573 chatdbt-0.0.5/chatdbt/vector_storage/pgvector.py
+-rw-r--r--   0        0        0     2219 2023-04-07 03:15:22.271642 chatdbt-0.0.5/pyproject.toml
+-rw-r--r--   0        0        0     5385 1970-01-01 00:00:00.000000 chatdbt-0.0.5/PKG-INFO
```

### Comparing `chatdbt-0.0.4/README.md` & `chatdbt-0.0.5/README.md`

 * *Files identical despite different names*

### Comparing `chatdbt-0.0.4/chatdbt/chat.py` & `chatdbt-0.0.5/chatdbt/chat.py`

 * *Files 0% similar despite different names*

```diff
@@ -234,15 +234,15 @@
             )
 
         messages.append(
             {
                 "role": "user",
                 "content": get_i18n_text(
                     I18nKey.KEY_PROMPT_USER_ROLE_SUGGEST_TABLES
-                ).format(query, ",".join(dbt_model_names)),
+                ).format(",".join(dbt_model_names), query),
             }
         )
         response = self.openai.chat_completion(messages=messages)
         message = ChatMessage(
             uuid=uuid.uuid4().hex,
             created_at=datetime.datetime.now(),
             query=query,
@@ -303,15 +303,15 @@
             )
 
         messages.append(
             {
                 "role": "user",
                 "content": get_i18n_text(
                     I18nKey.KEY_PROMPT_USER_ROLE_SUGGEST_SQL
-                ).format(query, ",".join(dbt_model_names)),
+                ).format(",".join(dbt_model_names), query),
             }
         )
         logging.debug("messages: %s", messages)
         response = self.openai.chat_completion(messages=messages)
         message = ChatMessage(
             uuid=uuid.uuid4().hex,
             created_at=datetime.datetime.now(),
```

### Comparing `chatdbt-0.0.4/chatdbt/dbt_doc_resolver/localfs.py` & `chatdbt-0.0.5/chatdbt/dbt_doc_resolver/localfs.py`

 * *Files identical despite different names*

### Comparing `chatdbt-0.0.4/chatdbt/model.py` & `chatdbt-0.0.5/chatdbt/model.py`

 * *Files 8% similar despite different names*

```diff
@@ -82,20 +82,19 @@
 
 {body}
 
 """
 
 
 def _markdown_chat_doc_li(query: str, response: str, indent: int = 4):
-    items = [
-        " " * indent + item
-        for item in ["```", f"query: {query}", f"response: {response}", "```"]
-    ]
-    body = "\n\n".join(items)
-    return f"- {body}"
+    return f"""- {query}
+
+  > {response}
+
+"""
 
 
 class DBTDocResolver(ABC):
     """Base class for all DBT document resolvers"""
 
     @abstractmethod
     def get_manifest_by_unique_id(self, unique_id: str) -> Optional[Dict]:
```

### Comparing `chatdbt-0.0.4/chatdbt/openai.py` & `chatdbt-0.0.5/chatdbt/openai.py`

 * *Files identical despite different names*

### Comparing `chatdbt-0.0.4/chatdbt/shortcut.py` & `chatdbt-0.0.5/chatdbt/shortcut.py`

 * *Files identical despite different names*

### Comparing `chatdbt-0.0.4/chatdbt/tiktoken_provider/tiktoken_http_server.py` & `chatdbt-0.0.5/chatdbt/tiktoken_provider/tiktoken_http_server.py`

 * *Files identical despite different names*

### Comparing `chatdbt-0.0.4/chatdbt/vector_storage/__init__.py` & `chatdbt-0.0.5/chatdbt/vector_storage/__init__.py`

 * *Files identical despite different names*

### Comparing `chatdbt-0.0.4/chatdbt/vector_storage/atlas.py` & `chatdbt-0.0.5/chatdbt/vector_storage/atlas.py`

 * *Files identical despite different names*

### Comparing `chatdbt-0.0.4/chatdbt/vector_storage/pgvector.py` & `chatdbt-0.0.5/chatdbt/vector_storage/pgvector.py`

 * *Files identical despite different names*

### Comparing `chatdbt-0.0.4/pyproject.toml` & `chatdbt-0.0.5/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "chatdbt"
-version = "0.0.4"
+version = "0.0.5"
 description = "chatdbt is an openai-based dbt documentation robot. You can use natural language to describe your data query requirements to the robot, and chatdbt will help you select the dbt model you need, or generate sql responses based on these dbt models to meet your need"
 authors = ["cadl <ctrlaltdeleteliu@gmail.com>"]
 readme = "README.md"
 
 [tool.poetry.dependencies]
 python = ">=3.7.1,<3.11"
 pydantic = "^1.9"
```

### Comparing `chatdbt-0.0.4/PKG-INFO` & `chatdbt-0.0.5/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: chatdbt
-Version: 0.0.4
+Version: 0.0.5
 Summary: chatdbt is an openai-based dbt documentation robot. You can use natural language to describe your data query requirements to the robot, and chatdbt will help you select the dbt model you need, or generate sql responses based on these dbt models to meet your need
 Author: cadl
 Author-email: ctrlaltdeleteliu@gmail.com
 Requires-Python: >=3.7.1,<3.11
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
```

