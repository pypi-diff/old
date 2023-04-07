# Comparing `tmp/meilisearch_tui-0.4.1.tar.gz` & `tmp/meilisearch_tui-0.5.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "meilisearch_tui-0.4.1.tar", max compression
+gzip compressed data, was "meilisearch_tui-0.5.0.tar", max compression
```

## Comparing `meilisearch_tui-0.4.1.tar` & `meilisearch_tui-0.5.0.tar`

### file list

```diff
@@ -1,23 +1,22 @@
--rw-r--r--   0        0        0     1069 2023-04-05 03:54:24.064611 meilisearch_tui-0.4.1/LICENSE
--rw-r--r--   0        0        0     2187 2023-04-05 03:54:24.068611 meilisearch_tui-0.4.1/README.md
--rw-r--r--   0        0        0        0 2023-04-05 03:54:24.068611 meilisearch_tui-0.4.1/meilisearch_tui/__init__.py
--rw-r--r--   0        0        0     2936 2023-04-05 03:54:24.068611 meilisearch_tui-0.4.1/meilisearch_tui/__main__.py
--rw-r--r--   0        0        0      608 2023-04-05 03:54:24.068611 meilisearch_tui-0.4.1/meilisearch_tui/client.py
--rw-r--r--   0        0        0     3226 2023-04-05 03:54:24.068611 meilisearch_tui-0.4.1/meilisearch_tui/config.py
--rw-r--r--   0        0        0       86 2023-04-05 03:54:24.068611 meilisearch_tui-0.4.1/meilisearch_tui/errors.py
--rw-r--r--   0        0        0     1855 2023-04-05 03:54:24.068611 meilisearch_tui-0.4.1/meilisearch_tui/meilisearch.css
--rw-r--r--   0        0        0        0 2023-04-05 03:54:24.068611 meilisearch_tui-0.4.1/meilisearch_tui/py.typed
--rw-r--r--   0        0        0        0 2023-04-05 03:54:24.068611 meilisearch_tui-0.4.1/meilisearch_tui/screens/__init__.py
--rw-r--r--   0        0        0     4548 2023-04-05 03:54:24.068611 meilisearch_tui-0.4.1/meilisearch_tui/screens/configuration.py
--rw-r--r--   0        0        0     6627 2023-04-05 03:54:24.068611 meilisearch_tui-0.4.1/meilisearch_tui/screens/data_load.py
--rw-r--r--   0        0        0     8991 2023-04-05 03:54:24.068611 meilisearch_tui-0.4.1/meilisearch_tui/screens/indexes.py
--rw-r--r--   0        0        0     3173 2023-04-05 03:54:24.068611 meilisearch_tui-0.4.1/meilisearch_tui/screens/meilisearch_settings.py
--rw-r--r--   0        0        0     6208 2023-04-05 03:54:24.068611 meilisearch_tui-0.4.1/meilisearch_tui/screens/search.py
--rw-r--r--   0        0        0      722 2023-04-05 03:54:24.072611 meilisearch_tui-0.4.1/meilisearch_tui/utils.py
--rw-r--r--   0        0        0        0 2023-04-05 03:54:24.072611 meilisearch_tui-0.4.1/meilisearch_tui/widgets/__init__.py
--rw-r--r--   0        0        0      844 2023-04-05 03:54:24.072611 meilisearch_tui-0.4.1/meilisearch_tui/widgets/index.py
--rw-r--r--   0        0        0     1543 2023-04-05 03:54:24.072611 meilisearch_tui-0.4.1/meilisearch_tui/widgets/index_sidebar.py
--rw-r--r--   0        0        0     1730 2023-04-05 03:54:24.072611 meilisearch_tui-0.4.1/meilisearch_tui/widgets/input.py
--rw-r--r--   0        0        0      709 2023-04-05 03:54:24.072611 meilisearch_tui-0.4.1/meilisearch_tui/widgets/messages.py
--rw-r--r--   0        0        0     2027 2023-04-05 03:54:24.072611 meilisearch_tui-0.4.1/pyproject.toml
--rw-r--r--   0        0        0     3454 1970-01-01 00:00:00.000000 meilisearch_tui-0.4.1/PKG-INFO
+-rw-r--r--   0        0        0     1069 2023-04-07 01:08:27.333700 meilisearch_tui-0.5.0/LICENSE
+-rw-r--r--   0        0        0     2187 2023-04-07 01:08:27.333700 meilisearch_tui-0.5.0/README.md
+-rw-r--r--   0        0        0        0 2023-04-07 01:08:27.337700 meilisearch_tui-0.5.0/meilisearch_tui/__init__.py
+-rw-r--r--   0        0        0     2780 2023-04-07 01:08:27.337700 meilisearch_tui-0.5.0/meilisearch_tui/__main__.py
+-rw-r--r--   0        0        0      608 2023-04-07 01:08:27.337700 meilisearch_tui-0.5.0/meilisearch_tui/client.py
+-rw-r--r--   0        0        0     3226 2023-04-07 01:08:27.337700 meilisearch_tui-0.5.0/meilisearch_tui/config.py
+-rw-r--r--   0        0        0       86 2023-04-07 01:08:27.337700 meilisearch_tui-0.5.0/meilisearch_tui/errors.py
+-rw-r--r--   0        0        0     1855 2023-04-07 01:08:27.337700 meilisearch_tui-0.5.0/meilisearch_tui/meilisearch.css
+-rw-r--r--   0        0        0        0 2023-04-07 01:08:27.337700 meilisearch_tui-0.5.0/meilisearch_tui/py.typed
+-rw-r--r--   0        0        0        0 2023-04-07 01:08:27.337700 meilisearch_tui-0.5.0/meilisearch_tui/screens/__init__.py
+-rw-r--r--   0        0        0     4548 2023-04-07 01:08:27.337700 meilisearch_tui-0.5.0/meilisearch_tui/screens/configuration.py
+-rw-r--r--   0        0        0    16537 2023-04-07 01:08:27.337700 meilisearch_tui-0.5.0/meilisearch_tui/screens/indexes.py
+-rw-r--r--   0        0        0     3173 2023-04-07 01:08:27.337700 meilisearch_tui-0.5.0/meilisearch_tui/screens/meilisearch_settings.py
+-rw-r--r--   0        0        0     6208 2023-04-07 01:08:27.337700 meilisearch_tui-0.5.0/meilisearch_tui/screens/search.py
+-rw-r--r--   0        0        0      722 2023-04-07 01:08:27.337700 meilisearch_tui-0.5.0/meilisearch_tui/utils.py
+-rw-r--r--   0        0        0        0 2023-04-07 01:08:27.337700 meilisearch_tui-0.5.0/meilisearch_tui/widgets/__init__.py
+-rw-r--r--   0        0        0      844 2023-04-07 01:08:27.337700 meilisearch_tui-0.5.0/meilisearch_tui/widgets/index.py
+-rw-r--r--   0        0        0     1543 2023-04-07 01:08:27.337700 meilisearch_tui-0.5.0/meilisearch_tui/widgets/index_sidebar.py
+-rw-r--r--   0        0        0     1730 2023-04-07 01:08:27.337700 meilisearch_tui-0.5.0/meilisearch_tui/widgets/input.py
+-rw-r--r--   0        0        0      709 2023-04-07 01:08:27.337700 meilisearch_tui-0.5.0/meilisearch_tui/widgets/messages.py
+-rw-r--r--   0        0        0     1985 2023-04-07 01:08:27.337700 meilisearch_tui-0.5.0/pyproject.toml
+-rw-r--r--   0        0        0     3404 1970-01-01 00:00:00.000000 meilisearch_tui-0.5.0/PKG-INFO
```

### Comparing `meilisearch_tui-0.4.1/LICENSE` & `meilisearch_tui-0.5.0/LICENSE`

 * *Files identical despite different names*

### Comparing `meilisearch_tui-0.4.1/README.md` & `meilisearch_tui-0.5.0/README.md`

 * *Files identical despite different names*

### Comparing `meilisearch_tui-0.4.1/meilisearch_tui/__main__.py` & `meilisearch_tui-0.5.0/meilisearch_tui/__main__.py`

 * *Files 11% similar despite different names*

```diff
@@ -7,15 +7,14 @@
 from textual.containers import Container
 from textual.widgets import Footer
 
 from meilisearch_tui.client import get_client
 from meilisearch_tui.config import Theme, load_config
 from meilisearch_tui.errors import NoMeilisearchUrlError
 from meilisearch_tui.screens.configuration import ConfigurationScreen
-from meilisearch_tui.screens.data_load import DataLoadScreen
 from meilisearch_tui.screens.indexes import IndexScreen
 from meilisearch_tui.screens.search import SearchScreen
 from meilisearch_tui.widgets.messages import ErrorMessage
 
 
 def _is_uvloop_platform() -> bool:  # pragma: no cover
     if platform != "win32":
@@ -23,24 +22,22 @@
     return False
 
 
 class MeilisearchApp(App):
     BINDINGS = [
         ("ctrl+c", "quit", "Quit"),
         ("s", "push_screen('search')", "Search"),
-        ("d", "push_screen('data_load')", "Load Data"),
         ("i", "push_screen('index')", "Index Management"),
         ("c", "push_screen('configuration')", "Configuration"),
     ]
     CSS_PATH = "meilisearch.css"
     TITLE = "Meilisearch"
     SCREENS = {
         "configuration": ConfigurationScreen(),
         "search": SearchScreen(),
-        "data_load": DataLoadScreen(),
         "index": IndexScreen(),
     }
 
     def compose(self) -> ComposeResult:
         with Container(id="body"):
             yield ErrorMessage("", classes="message-centered", id="generic-error")
         yield Footer()
```

### Comparing `meilisearch_tui-0.4.1/meilisearch_tui/client.py` & `meilisearch_tui-0.5.0/meilisearch_tui/client.py`

 * *Files identical despite different names*

### Comparing `meilisearch_tui-0.4.1/meilisearch_tui/config.py` & `meilisearch_tui-0.5.0/meilisearch_tui/config.py`

 * *Files identical despite different names*

### Comparing `meilisearch_tui-0.4.1/meilisearch_tui/meilisearch.css` & `meilisearch_tui-0.5.0/meilisearch_tui/meilisearch.css`

 * *Files identical despite different names*

### Comparing `meilisearch_tui-0.4.1/meilisearch_tui/screens/configuration.py` & `meilisearch_tui-0.5.0/meilisearch_tui/screens/configuration.py`

 * *Files identical despite different names*

### Comparing `meilisearch_tui-0.4.1/meilisearch_tui/screens/data_load.py` & `meilisearch_tui-0.5.0/meilisearch_tui/screens/search.py`

 * *Files 27% similar despite different names*

```diff
@@ -1,183 +1,163 @@
 from __future__ import annotations
 
 import asyncio
 from functools import cached_property
-from pathlib import Path
 
-from meilisearch_python_async.errors import (
-    MeilisearchApiError,
-    MeilisearchCommunicationError,
-    MeilisearchError,
-)
+from meilisearch_python_async.errors import MeilisearchCommunicationError
+from meilisearch_python_async.models.search import SearchResults
 from textual import events
 from textual.app import ComposeResult
-from textual.containers import Center, Container
+from textual.containers import Center, Container, Content
 from textual.screen import Screen
-from textual.widgets import Button, DirectoryTree, Footer, Input, Static
+from textual.widgets import Button, Footer, Input, Markdown, Static
 
 from meilisearch_tui.client import get_client
-from meilisearch_tui.widgets.index import CurrentIndexes
-from meilisearch_tui.widgets.input import InputWithLabel
-from meilisearch_tui.widgets.messages import ErrorMessage, SuccessMessage
+from meilisearch_tui.widgets.index_sidebar import IndexSidebar
+from meilisearch_tui.widgets.messages import ErrorMessage
 
 
-class DataLoadScreen(Screen):
+class SearchScreen(Screen):
+    def __init__(self) -> None:
+        super().__init__()
+        self.limit = 20
+        self.selected_index: str | None = None
+
     def compose(self) -> ComposeResult:
         yield ErrorMessage("", classes="message-centered", id="generic-error")
+        yield IndexSidebar(classes="sidebar")
         with Container(id="body"):
-            yield DirectoryTree(Path.home(), id="tree-view")
-            yield InputWithLabel(
-                label="Index",
-                input_id="index-name",
-                error_id="index-error",
-                error_message="An index is require",
-            )
-            yield InputWithLabel(
-                label="File Path",
-                input_id="data-file",
-                error_id="data-file-error",
-                error_message="A Path to a json, jsonl, or csv file is required",
-            )
+            yield Static("No index selected", id="index-name", classes="bottom-spacer")
+            yield Input(placeholder="Search", classes="bottom-spacer", id="search")
+            with Content(id="results-container"):
+                yield Markdown(id="results")
             with Center():
-                yield Button(label="Index File", id="index-button")
-            yield SuccessMessage(
-                "Data successfully sent for indexing",
-                classes="message-centered",
-                id="indexing-successful",
-            )
-            yield ErrorMessage("", classes="message-centered", id="indexing-error")
-            yield CurrentIndexes()
+                yield Button(label="Load More", classes="bottom-spacer", id="load-more-button")
         yield Footer()
 
     @cached_property
-    def body(self) -> Container:
+    def body_container(self) -> Container:
         return self.query_one("#body", Container)
 
     @cached_property
-    def current_indexes(self) -> CurrentIndexes:
-        return self.query_one(CurrentIndexes)
-
-    @cached_property
-    def data_file(self) -> Input:
-        return self.query_one("#data-file", Input)
-
-    @cached_property
-    def data_file_error(self) -> Static:
-        return self.query_one("#data-file-error", Static)
-
-    @cached_property
-    def directory_tree(self) -> DirectoryTree:
-        return self.query_one("#tree-view", DirectoryTree)
-
-    @cached_property
     def generic_error(self) -> ErrorMessage:
         return self.query_one("#generic-error", ErrorMessage)
 
     @cached_property
-    def index_button(self) -> Button:
-        return self.query_one("#index-button", Button)
+    def index_sidebar(self) -> IndexSidebar:
+        return self.query_one(IndexSidebar)
 
     @cached_property
-    def index_error(self) -> Static:
-        return self.query_one("#index-error", Static)
+    def index_name(self) -> Static:
+        return self.query_one("#index-name", Static)
 
     @cached_property
-    def index_name(self) -> Input:
-        return self.query_one("#index-name", Input)
+    def search_input(self) -> Input:
+        return self.query_one("#search", Input)
 
     @cached_property
-    def indexing_successful(self) -> Static:
-        return self.query_one("#indexing-successful", Static)
+    def results_container(self) -> Content:
+        return self.query_one("#results-container", Content)
 
     @cached_property
-    def indexing_error(self) -> Static:
-        return self.query_one("#indexing-error", Static)
+    def results(self) -> Markdown:
+        return self.query_one("#results", Markdown)
+
+    @cached_property
+    def load_more_button(self) -> Button:
+        return self.query_one("#load-more-button", Button)
 
     async def on_screen_resume(self, event: events.ScreenResume) -> None:
-        self.body.visible = True
+        self.body_container.visible = True
         self.generic_error.display = False
+        await self.index_sidebar.update()
+        self.search_input.value = ""
+        self.results.update("")
         try:
             async with get_client() as client:
                 indexes = await client.get_indexes()
         except MeilisearchCommunicationError as e:
-            self.body.visible = False
+            self.body_container.visible = False
             self.generic_error.display = True
             self.generic_error.renderable = f"An error occured: {e}.\nMake sure the Meilisearch server is running and accessable"  # type: ignore
             return
         except Exception as e:
-            self.body.visible = False
+            self.body_container.visible = False
             self.generic_error.display = True
             self.generic_error.renderable = f"An error occured: {e}."  # type: ignore
             return
 
         if indexes:
-            self.index_name.value = indexes[0].uid
-            self.directory_tree.focus()
+            self.index_name.update(f"Searching index: {indexes[0].uid}")
+            self.selected_index = self.index_sidebar.selected_index
         else:
-            self.index_name.focus()
+            self.selected_index = None
+            self.index_name.update("No index selected")
 
-        await self.current_indexes.update()
-        self.indexing_successful.visible = False
-        self.indexing_error.visible = False
-
-    def on_directory_tree_file_selected(self, event: DirectoryTree.FileSelected) -> None:
-        """Called when the user click a file in the directory tree."""
-        event.stop()
-        try:
-            self.data_file.value = event.path
-        except Exception:
-            raise
+        self.search_input.focus()
+        self.load_more_button.visible = False
+
+    async def on_list_item__child_clicked(self, message: IndexSidebar.Selected) -> None:  # type: ignore[name-defined]
+        self.selected_index = self.index_sidebar.selected_index
+        self.index_name.update(f"Searching index: {self.selected_index}")
+        self.search_input.value = ""
+        self.results.update("")
+
+    async def on_input_changed(self, message: Input.Changed) -> None:
+        self.limit = 20
+        if message.value:
+            asyncio.create_task(self.lookup_word(message.value))
+        else:
+            self.results.update("")
+            self.load_more_button.visible = False
 
     async def on_button_pressed(self, event: Button.Pressed) -> None:
         button_id = event.button.id
-        error = False
 
-        if button_id == "index-button":
-            if not self.data_file.value or Path(self.data_file.value).suffix not in (
-                ".csv",
-                ".json",
-                ".jsonl",
-            ):
-                self.data_file_error.visible = True
-                error = True
-            if not self.index_name.value:
-                self.index_error.visible = True
-                error = True
+        if button_id == "load-more-button":
+            self.limit += 20
+            asyncio.create_task(self.lookup_word(self.search_input.value))
+
+    async def lookup_word(self, search: str) -> None:
+        if not self.selected_index and search == self.search_input.value:
+            self.results.update("Error: No index provided")
+            return
 
-            if error:
-                return None
+        if not self.selected_index:
+            self.results.update("No index selected")
+            return
 
-            data_file_path = Path(self.data_file.value)
+        async with get_client() as client:
+            index = client.index(self.selected_index)
             try:
-                async with get_client() as client:
-                    index = client.index(self.index_name.value)
-                    if data_file_path.suffix == ".json":
-                        await index.add_documents_from_file_in_batches(data_file_path)
-                    else:
-                        await index.add_documents_from_raw_file(data_file_path)
-                asyncio.create_task(self._success_message())
-            except MeilisearchApiError as e:
-                asyncio.create_task(self._error_message(f"{e}"))
-            except MeilisearchCommunicationError as e:
-                asyncio.create_task(self._error_message(f"{e}"))
-            except MeilisearchError as e:
-                asyncio.create_task(self._error_message(f"{e}"))
+                results = await index.search(self.search_input.value, limit=self.limit)
             except Exception as e:
-                asyncio.create_task(self._error_message(f"An unknown error occured error: {e}"))
+                if search == self.search_input.value:
+                    self.results.update(f"Error: {e}")
+                return
+
+        # Make sure a new search hasn't started. This prevents race conditions with displaying
+        # the search results by only updating the display if the search is still relavent.
+        if search == self.search_input.value:
+            markdown = self.make_word_markdown(results)
+            self.results.update(markdown)
+
+    def make_word_markdown(self, results: SearchResults) -> str:
+        lines = []
+
+        if results.estimated_total_hits and results.estimated_total_hits > len(results.hits):
+            self.load_more_button.visible = True
+        else:
+            self.load_more_button.visible = False
 
-        await self.current_indexes.update()
+        lines.append(
+            f"## Hits: ~{results.estimated_total_hits} | Search time: {results.processing_time_ms} ms"
+        )
+
+        if results.hits:
+            for hit in results.hits:
+                for k, v in hit.items():
+                    lines.append(f"{k}: {v}\n")
+                lines.append("-------------------------------")
+            return "\n".join(lines)
 
-    def on_key(self, event: events.Key) -> None:
-        if event.key == "enter":
-            self.index_button.press()
-
-    async def _success_message(self) -> None:
-        self.indexing_successful.visible = True
-        await asyncio.sleep(5)
-        self.indexing_successful.visible = False
-
-    async def _error_message(self, message: str) -> None:
-        self.indexing_error.renderable = message
-        self.indexing_error.visible = True
-        await asyncio.sleep(5)
-        self.indexing_error.visible = False
+        return "No results found"
```

### Comparing `meilisearch_tui-0.4.1/meilisearch_tui/screens/meilisearch_settings.py` & `meilisearch_tui-0.5.0/meilisearch_tui/screens/meilisearch_settings.py`

 * *Files identical despite different names*

### Comparing `meilisearch_tui-0.4.1/meilisearch_tui/utils.py` & `meilisearch_tui-0.5.0/meilisearch_tui/utils.py`

 * *Files identical despite different names*

### Comparing `meilisearch_tui-0.4.1/meilisearch_tui/widgets/index.py` & `meilisearch_tui-0.5.0/meilisearch_tui/widgets/index.py`

 * *Files identical despite different names*

### Comparing `meilisearch_tui-0.4.1/meilisearch_tui/widgets/index_sidebar.py` & `meilisearch_tui-0.5.0/meilisearch_tui/widgets/index_sidebar.py`

 * *Files identical despite different names*

### Comparing `meilisearch_tui-0.4.1/meilisearch_tui/widgets/input.py` & `meilisearch_tui-0.5.0/meilisearch_tui/widgets/input.py`

 * *Files identical despite different names*

### Comparing `meilisearch_tui-0.4.1/meilisearch_tui/widgets/messages.py` & `meilisearch_tui-0.5.0/meilisearch_tui/widgets/messages.py`

 * *Files identical despite different names*

### Comparing `meilisearch_tui-0.4.1/pyproject.toml` & `meilisearch_tui-0.5.0/pyproject.toml`

 * *Files 9% similar despite different names*

```diff
@@ -1,21 +1,20 @@
 [tool.poetry]
 name = "meilisearch-tui"
-version = "0.4.1"
+version = "0.5.0"
 description = "A TUI for Managing and Searching with Meilisearch"
 authors = ["Paul Sanders <psanders1@gmail.com>"]
 license = "MIT"
 readme = "README.md"
 repository = "https://github.com/sanders41/meilisearch-tui"
 homepage = "https://github.com/sanders41/meilisearch-tui"
 documentation = "https://github.com/sanders41/meilisearch-tui"
 keywords = ["meilisearch", "tui"]
 classifiers=[
   "Development Status :: 4 - Beta",
-  "Programming Language :: Python :: 3.7",
   "Programming Language :: Python :: 3.8",
   "Programming Language :: Python :: 3.9",
   "Programming Language :: Python :: 3.10",
   "Programming Language :: Python :: 3.11",
   "License :: OSI Approved :: MIT License",
   "Operating System :: OS Independent",
 ]
@@ -32,16 +31,16 @@
 click = "8.1.3"
 msgpack = "1.0.5"
 mypy = "1.1.1"
 pre-commit = "3.2.2"
 pytest = "7.2.2"
 pytest-asyncio = "0.21.0"
 pytest-cov = "4.0.0"
-ruff = "0.0.260"
-tox = "4.4.8"
+ruff = "0.0.261"
+tox = "4.4.11"
 
 [build-system]
 requires = ["poetry-core>=1.0.0"]
 build-backend = "poetry.core.masonry.api"
 
 [tool.poetry.scripts]
 meilisearch = "meilisearch_tui.__main__:main"
```

### Comparing `meilisearch_tui-0.4.1/PKG-INFO` & `meilisearch_tui-0.5.0/PKG-INFO`

 * *Files 7% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: meilisearch-tui
-Version: 0.4.1
+Version: 0.5.0
 Summary: A TUI for Managing and Searching with Meilisearch
 Home-page: https://github.com/sanders41/meilisearch-tui
 License: MIT
 Keywords: meilisearch,tui
 Author: Paul Sanders
 Author-email: psanders1@gmail.com
 Requires-Python: >=3.8,<4.0
@@ -14,15 +14,14 @@
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10
 Classifier: Programming Language :: Python :: 3.11
 Classifier: Programming Language :: Python :: 3.10
 Classifier: Programming Language :: Python :: 3.11
-Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Requires-Dist: meilisearch-python-async (==1.1.0)
 Requires-Dist: textual (==0.18.0)
 Requires-Dist: uvloop (==0.17.0) ; sys_platform != "win32"
 Project-URL: Documentation, https://github.com/sanders41/meilisearch-tui
 Project-URL: Repository, https://github.com/sanders41/meilisearch-tui
```

