# Comparing `tmp/chatdbt-0.0.1.tar.gz` & `tmp/chatdbt-0.0.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "chatdbt-0.0.1.tar", max compression
+gzip compressed data, was "chatdbt-0.0.2.tar", max compression
```

## Comparing `chatdbt-0.0.1.tar` & `chatdbt-0.0.2.tar`

### file list

```diff
@@ -1,15 +1,16 @@
--rw-r--r--   0        0        0      245 2023-04-04 16:03:00.258531 chatdbt-0.0.1/chatdbt/__init__.py
--rw-r--r--   0        0        0    12855 2023-04-04 16:05:10.502257 chatdbt-0.0.1/chatdbt/chat.py
--rw-r--r--   0        0        0      413 2023-03-30 09:50:02.949353 chatdbt-0.0.1/chatdbt/dbt_doc_resolver/__init__.py
--rw-r--r--   0        0        0     1024 2023-04-04 10:53:56.113000 chatdbt-0.0.1/chatdbt/dbt_doc_resolver/localfs.py
--rw-r--r--   0        0        0     2456 2023-04-04 16:07:35.903312 chatdbt-0.0.1/chatdbt/i18n.py
--rw-r--r--   0        0        0     5348 2023-04-04 16:08:02.569721 chatdbt-0.0.1/chatdbt/model.py
--rw-r--r--   0        0        0     1567 2023-04-04 06:21:51.675856 chatdbt-0.0.1/chatdbt/openai.py
--rw-r--r--   0        0        0     4120 2023-04-04 16:03:59.431156 chatdbt-0.0.1/chatdbt/shortcut.py
--rw-r--r--   0        0        0      386 2023-04-04 15:55:49.091076 chatdbt-0.0.1/chatdbt/tiktoken_provider/__init__.py
--rw-r--r--   0        0        0      868 2023-04-04 15:55:44.322642 chatdbt-0.0.1/chatdbt/tiktoken_provider/tiktoken_http_server.py
--rw-r--r--   0        0        0      625 2023-04-04 14:37:03.059444 chatdbt-0.0.1/chatdbt/vector_storage/__init__.py
--rw-r--r--   0        0        0     1670 2023-03-30 11:35:03.665857 chatdbt-0.0.1/chatdbt/vector_storage/atlas.py
--rw-r--r--   0        0        0     2670 2023-04-04 14:42:21.851573 chatdbt-0.0.1/chatdbt/vector_storage/pgvector.py
--rw-r--r--   0        0        0     1929 2023-04-05 01:23:36.299530 chatdbt-0.0.1/pyproject.toml
--rw-r--r--   0        0        0      840 1970-01-01 00:00:00.000000 chatdbt-0.0.1/PKG-INFO
+-rw-r--r--   0        0        0     4293 2023-04-04 11:26:15.209241 chatdbt-0.0.2/README.md
+-rw-r--r--   0        0        0      245 2023-04-04 16:03:00.258531 chatdbt-0.0.2/chatdbt/__init__.py
+-rw-r--r--   0        0        0    12939 2023-04-06 14:59:42.982624 chatdbt-0.0.2/chatdbt/chat.py
+-rw-r--r--   0        0        0      413 2023-03-30 09:50:02.949353 chatdbt-0.0.2/chatdbt/dbt_doc_resolver/__init__.py
+-rw-r--r--   0        0        0     1024 2023-04-04 10:53:56.113000 chatdbt-0.0.2/chatdbt/dbt_doc_resolver/localfs.py
+-rw-r--r--   0        0        0     2456 2023-04-04 16:07:35.903312 chatdbt-0.0.2/chatdbt/i18n.py
+-rw-r--r--   0        0        0     5387 2023-04-06 15:19:40.954618 chatdbt-0.0.2/chatdbt/model.py
+-rw-r--r--   0        0        0     1627 2023-04-06 15:12:59.226924 chatdbt-0.0.2/chatdbt/openai.py
+-rw-r--r--   0        0        0     4471 2023-04-06 15:10:00.859901 chatdbt-0.0.2/chatdbt/shortcut.py
+-rw-r--r--   0        0        0      386 2023-04-04 15:55:49.091076 chatdbt-0.0.2/chatdbt/tiktoken_provider/__init__.py
+-rw-r--r--   0        0        0      868 2023-04-04 15:55:44.322642 chatdbt-0.0.2/chatdbt/tiktoken_provider/tiktoken_http_server.py
+-rw-r--r--   0        0        0      625 2023-04-04 14:37:03.059444 chatdbt-0.0.2/chatdbt/vector_storage/__init__.py
+-rw-r--r--   0        0        0     1670 2023-03-30 11:35:03.665857 chatdbt-0.0.2/chatdbt/vector_storage/atlas.py
+-rw-r--r--   0        0        0     2670 2023-04-04 14:42:21.851573 chatdbt-0.0.2/chatdbt/vector_storage/pgvector.py
+-rw-r--r--   0        0        0     2219 2023-04-06 15:40:30.572576 chatdbt-0.0.2/pyproject.toml
+-rw-r--r--   0        0        0     5385 1970-01-01 00:00:00.000000 chatdbt-0.0.2/PKG-INFO
```

### Comparing `chatdbt-0.0.1/chatdbt/chat.py` & `chatdbt-0.0.2/chatdbt/chat.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 import logging
-from typing import Optional, Set, List, Dict, cast
+from typing import Optional, Set, List, Dict, cast, Any
 import uuid
 import datetime
 from chatdbt.model import (
     ChatConversationDocument,
     ChatMessageMeta,
     Doc,
     DocMetaContainer,
@@ -141,20 +141,21 @@
     """Chatbot for dbt documentation"""
 
     def __init__(
         self,
         doc_resolver: DBTDocResolver,
         vector_storage: VectorStorage,
         tiktoken_provider: Optional[TikTokenProvider],
+        openai_config: Optional[Dict[str, Any]] = None,
         i18n: str = "en",
     ) -> None:
         self.doc_manager = DocManager(doc_resolver)
         self.vector_storage = vector_storage
         self.tiktoken_provider = tiktoken_provider
-        self.openai = Openai()
+        self.openai = Openai(**(openai_config or {}))
         self._i18n = i18n
         self._messages: List[ChatMessage] = []
 
     def index_dbt_docs(self):
         """Index all dbt docs"""
 
         if self.tiktoken_provider:
```

### Comparing `chatdbt-0.0.1/chatdbt/dbt_doc_resolver/localfs.py` & `chatdbt-0.0.2/chatdbt/dbt_doc_resolver/localfs.py`

 * *Files identical despite different names*

### Comparing `chatdbt-0.0.1/chatdbt/i18n.py` & `chatdbt-0.0.2/chatdbt/i18n.py`

 * *Files identical despite different names*

### Comparing `chatdbt-0.0.1/chatdbt/model.py` & `chatdbt-0.0.2/chatdbt/model.py`

 * *Files 2% similar despite different names*

```diff
@@ -73,30 +73,28 @@
 
 
 def _markdown_dbt_doc_li(name: str, content: str, indent: int = 4):
     _items = content.split("\n")
     items = []
     for item in _items:
         items.append(item)
-        items.append("")
-
-    body = "\n".join([" " * indent + item for item in ["```", *items, "```"]])
+    body = "\n\n".join([" " * indent + item for item in ["```", *items, "```"]])
     return f"""- {name}
 
 {body}
 
 """
 
 
 def _markdown_chat_doc_li(query: str, response: str, indent: int = 4):
     items = [
         " " * indent + item
         for item in ["```", f"query: {query}", f"response: {response}", "```"]
     ]
-    body = "\n".join(items)
+    body = "\n\n".join(items)
     return f"- {body}"
 
 
 class DBTDocResolver(ABC):
     """Base class for all DBT document resolvers"""
 
     @abstractmethod
@@ -141,15 +139,17 @@
     meta: DocMetaContainer
     name: str
     description: Optional[str]
     columns: List[CatalogColumn]
     depends_on: List[str]
 
     def get_content(self):
-        columns = [i.dict() for i in self.columns]
+        columns = [
+            str(i.dict()).replace(" ", "").replace("'", "") for i in self.columns
+        ]
         return f"""name: {self.name}
 description: {self.description or ''}
 columns: {columns}
 depends_on: {self.depends_on}
 """
 
     def get_metadata(self):
```

### Comparing `chatdbt-0.0.1/chatdbt/openai.py` & `chatdbt-0.0.2/chatdbt/openai.py`

 * *Files 11% similar despite different names*

```diff
@@ -26,26 +26,27 @@
 def price_for_embedding(n_tokens: int) -> float:
     return float(n_tokens) / 1000.0 * 0.0004
 
 
 class Openai(EmbeddingProvider):
     """OpenAI embedding"""
 
-    def __init__(self):
+    def __init__(self, temperature: float = 0.2):
         self.embedding_model = EMBEDDING_MODEL
+        self.temperature = float(temperature)
 
     def embed(self, content: str) -> List[float]:
         """Embed a piece of text into a vector"""
         return get_embedding(content, engine=self.embedding_model)
 
     def completion(self):
         openai.ChatCompletion.create()
 
-    def chat_completion(self, messages: List[Dict[str, str]], temperature=0.2) -> str:
-        res = chat_completion(messages, temperature=temperature)
+    def chat_completion(self, messages: List[Dict[str, str]]) -> str:
+        res = chat_completion(messages, temperature=self.temperature)
         usage = res["usage"]["total_tokens"]
         logging.info(
             "chat-completion total tokens: %s, cost %s$",
             usage,
             price_for_completion(usage),
         )
```

### Comparing `chatdbt-0.0.1/chatdbt/shortcut.py` & `chatdbt-0.0.2/chatdbt/shortcut.py`

 * *Files 10% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 import functools
 import logging
 import os
-from typing import Optional, cast
+from typing import Optional, cast, Any, Dict
 
 from chatdbt.chat import ChatBot
 from chatdbt.dbt_doc_resolver import get_dbt_doc_resolver
 from chatdbt.model import ChatMessage, DBTDocResolver, TikTokenProvider, VectorStorage
 from chatdbt.tiktoken_provider import get_tiktoken_provider
 from chatdbt.vector_storage import get_vector_storage
 
@@ -16,32 +16,36 @@
 ENV_VAR_DBT_DOC_RESOLVER_CONFIG_PREFIX = "CHATDBT_DBT_DOC_RESOLVER_CONFIG_"
 
 ENV_VAR_I18N = "CHATDBT_I18N"
 
 ENV_VAR_TIKTOKEN_PROVIDER_TYPE = "CHATDBT_TIKTOKEN_PROVIDER_TYPE"
 ENV_VAR_TIKTOKEN_PROVIDER_CONFIG_PREFIX = "CHATDBT_TIKTOKEN_PROVIDER_CONFIG_"
 
+ENV_VAR_OPENAI_CONFIG_PREFIX = "CHATDBT_OPENAI_CONFIG_"
+
 
 class _Global:
     chat_instance: Optional[ChatBot] = None
     chat_instance_init: bool = False
 
 
 def setup_shortcut(
     vector_storage: VectorStorage,
     dbt_doc_resolver: DBTDocResolver,
     tiktoken_provider: Optional[TikTokenProvider] = None,
+    openai_config: Optional[Dict[str, Any]] = None,
     i18n: str = "en-us",
 ):
     logging.basicConfig(level=logging.INFO)
 
     _Global.chat_instance = ChatBot(
         dbt_doc_resolver,
         vector_storage,
         tiktoken_provider,
+        openai_config,
         i18n,
     )
     _Global.chat_instance_init = True
 
 
 def setup_shortcut_via_env() -> None:
     """Setup chat instance via environment variables"""
@@ -77,18 +81,25 @@
     }
 
     if tiktoken_provider_type is not None:
         tiktoken_provider = get_tiktoken_provider(
             tiktoken_provider_type, tiktoken_provider_config
         )
 
+    openai_config = {
+        k.replace(ENV_VAR_OPENAI_CONFIG_PREFIX, "").lower(): v
+        for k, v in os.environ.items()
+        if k.startswith(ENV_VAR_OPENAI_CONFIG_PREFIX)
+    }
+
     setup_shortcut(
         get_vector_storage(vector_storage_type, vector_storage_config),
         get_dbt_doc_resolver(dbt_doc_resolver_type, dbt_doc_resolver_config),
         tiktoken_provider,
+        openai_config,
         i18n,
     )
 
 
 def ensure_chat_init(func):
     """Decorator to ensure chat instance is initialized before calling the function."""
```

### Comparing `chatdbt-0.0.1/chatdbt/tiktoken_provider/tiktoken_http_server.py` & `chatdbt-0.0.2/chatdbt/tiktoken_provider/tiktoken_http_server.py`

 * *Files identical despite different names*

### Comparing `chatdbt-0.0.1/chatdbt/vector_storage/__init__.py` & `chatdbt-0.0.2/chatdbt/vector_storage/__init__.py`

 * *Files identical despite different names*

### Comparing `chatdbt-0.0.1/chatdbt/vector_storage/atlas.py` & `chatdbt-0.0.2/chatdbt/vector_storage/atlas.py`

 * *Files identical despite different names*

### Comparing `chatdbt-0.0.1/chatdbt/vector_storage/pgvector.py` & `chatdbt-0.0.2/chatdbt/vector_storage/pgvector.py`

 * *Files identical despite different names*

### Comparing `chatdbt-0.0.1/pyproject.toml` & `chatdbt-0.0.2/pyproject.toml`

 * *Files 25% similar despite different names*

```diff
@@ -1,15 +1,16 @@
 [tool.poetry]
 name = "chatdbt"
-version = "0.0.1"
-description = ""
+version = "0.0.2"
+description = "chatdbt is an openai-based dbt documentation robot. You can use natural language to describe your data query requirements to the robot, and chatdbt will help you select the dbt model you need, or generate sql responses based on these dbt models to meet your need"
 authors = ["cadl <ctrlaltdeleteliu@gmail.com>"]
+readme = "README.md"
 
 [tool.poetry.dependencies]
-python = "^3.7.1"
+python = ">=3.7.1,<3.11"
 pydantic = "^1.9"
 openai = {version = "^0.27", extras = ["embeddings", "datalib"]}
 tenacity = "^8"
 requests = "^2.28"
 nomic = {version = "^1.0", optional = true}
 pgvector = {version = "^0.1", optional = true}
 sqlalchemy = {version = "^2", optional = true}
```

