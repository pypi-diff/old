# Comparing `tmp/meilisearch_tui-0.5.0.tar.gz` & `tmp/meilisearch_tui-0.5.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "meilisearch_tui-0.5.0.tar", max compression
+gzip compressed data, was "meilisearch_tui-0.5.1.tar", max compression
```

## Comparing `meilisearch_tui-0.5.0.tar` & `meilisearch_tui-0.5.1.tar`

### file list

```diff
@@ -1,22 +1,22 @@
--rw-r--r--   0        0        0     1069 2023-04-07 01:08:27.333700 meilisearch_tui-0.5.0/LICENSE
--rw-r--r--   0        0        0     2187 2023-04-07 01:08:27.333700 meilisearch_tui-0.5.0/README.md
--rw-r--r--   0        0        0        0 2023-04-07 01:08:27.337700 meilisearch_tui-0.5.0/meilisearch_tui/__init__.py
--rw-r--r--   0        0        0     2780 2023-04-07 01:08:27.337700 meilisearch_tui-0.5.0/meilisearch_tui/__main__.py
--rw-r--r--   0        0        0      608 2023-04-07 01:08:27.337700 meilisearch_tui-0.5.0/meilisearch_tui/client.py
--rw-r--r--   0        0        0     3226 2023-04-07 01:08:27.337700 meilisearch_tui-0.5.0/meilisearch_tui/config.py
--rw-r--r--   0        0        0       86 2023-04-07 01:08:27.337700 meilisearch_tui-0.5.0/meilisearch_tui/errors.py
--rw-r--r--   0        0        0     1855 2023-04-07 01:08:27.337700 meilisearch_tui-0.5.0/meilisearch_tui/meilisearch.css
--rw-r--r--   0        0        0        0 2023-04-07 01:08:27.337700 meilisearch_tui-0.5.0/meilisearch_tui/py.typed
--rw-r--r--   0        0        0        0 2023-04-07 01:08:27.337700 meilisearch_tui-0.5.0/meilisearch_tui/screens/__init__.py
--rw-r--r--   0        0        0     4548 2023-04-07 01:08:27.337700 meilisearch_tui-0.5.0/meilisearch_tui/screens/configuration.py
--rw-r--r--   0        0        0    16537 2023-04-07 01:08:27.337700 meilisearch_tui-0.5.0/meilisearch_tui/screens/indexes.py
--rw-r--r--   0        0        0     3173 2023-04-07 01:08:27.337700 meilisearch_tui-0.5.0/meilisearch_tui/screens/meilisearch_settings.py
--rw-r--r--   0        0        0     6208 2023-04-07 01:08:27.337700 meilisearch_tui-0.5.0/meilisearch_tui/screens/search.py
--rw-r--r--   0        0        0      722 2023-04-07 01:08:27.337700 meilisearch_tui-0.5.0/meilisearch_tui/utils.py
--rw-r--r--   0        0        0        0 2023-04-07 01:08:27.337700 meilisearch_tui-0.5.0/meilisearch_tui/widgets/__init__.py
--rw-r--r--   0        0        0      844 2023-04-07 01:08:27.337700 meilisearch_tui-0.5.0/meilisearch_tui/widgets/index.py
--rw-r--r--   0        0        0     1543 2023-04-07 01:08:27.337700 meilisearch_tui-0.5.0/meilisearch_tui/widgets/index_sidebar.py
--rw-r--r--   0        0        0     1730 2023-04-07 01:08:27.337700 meilisearch_tui-0.5.0/meilisearch_tui/widgets/input.py
--rw-r--r--   0        0        0      709 2023-04-07 01:08:27.337700 meilisearch_tui-0.5.0/meilisearch_tui/widgets/messages.py
--rw-r--r--   0        0        0     1985 2023-04-07 01:08:27.337700 meilisearch_tui-0.5.0/pyproject.toml
--rw-r--r--   0        0        0     3404 1970-01-01 00:00:00.000000 meilisearch_tui-0.5.0/PKG-INFO
+-rw-r--r--   0        0        0     1069 2023-04-07 01:16:51.895065 meilisearch_tui-0.5.1/LICENSE
+-rw-r--r--   0        0        0     2187 2023-04-07 01:16:51.895065 meilisearch_tui-0.5.1/README.md
+-rw-r--r--   0        0        0        0 2023-04-07 01:16:51.899065 meilisearch_tui-0.5.1/meilisearch_tui/__init__.py
+-rw-r--r--   0        0        0     2776 2023-04-07 01:16:51.899065 meilisearch_tui-0.5.1/meilisearch_tui/__main__.py
+-rw-r--r--   0        0        0      608 2023-04-07 01:16:51.899065 meilisearch_tui-0.5.1/meilisearch_tui/client.py
+-rw-r--r--   0        0        0     3226 2023-04-07 01:16:51.899065 meilisearch_tui-0.5.1/meilisearch_tui/config.py
+-rw-r--r--   0        0        0       86 2023-04-07 01:16:51.899065 meilisearch_tui-0.5.1/meilisearch_tui/errors.py
+-rw-r--r--   0        0        0     1855 2023-04-07 01:16:51.899065 meilisearch_tui-0.5.1/meilisearch_tui/meilisearch.css
+-rw-r--r--   0        0        0        0 2023-04-07 01:16:51.899065 meilisearch_tui-0.5.1/meilisearch_tui/py.typed
+-rw-r--r--   0        0        0        0 2023-04-07 01:16:51.899065 meilisearch_tui-0.5.1/meilisearch_tui/screens/__init__.py
+-rw-r--r--   0        0        0     4548 2023-04-07 01:16:51.899065 meilisearch_tui-0.5.1/meilisearch_tui/screens/configuration.py
+-rw-r--r--   0        0        0    16704 2023-04-07 01:16:51.899065 meilisearch_tui-0.5.1/meilisearch_tui/screens/indexes.py
+-rw-r--r--   0        0        0     3173 2023-04-07 01:16:51.899065 meilisearch_tui-0.5.1/meilisearch_tui/screens/meilisearch_settings.py
+-rw-r--r--   0        0        0     6208 2023-04-07 01:16:51.899065 meilisearch_tui-0.5.1/meilisearch_tui/screens/search.py
+-rw-r--r--   0        0        0      722 2023-04-07 01:16:51.899065 meilisearch_tui-0.5.1/meilisearch_tui/utils.py
+-rw-r--r--   0        0        0        0 2023-04-07 01:16:51.899065 meilisearch_tui-0.5.1/meilisearch_tui/widgets/__init__.py
+-rw-r--r--   0        0        0      844 2023-04-07 01:16:51.899065 meilisearch_tui-0.5.1/meilisearch_tui/widgets/index.py
+-rw-r--r--   0        0        0     1543 2023-04-07 01:16:51.899065 meilisearch_tui-0.5.1/meilisearch_tui/widgets/index_sidebar.py
+-rw-r--r--   0        0        0     1730 2023-04-07 01:16:51.899065 meilisearch_tui-0.5.1/meilisearch_tui/widgets/input.py
+-rw-r--r--   0        0        0      709 2023-04-07 01:16:51.899065 meilisearch_tui-0.5.1/meilisearch_tui/widgets/messages.py
+-rw-r--r--   0        0        0     1985 2023-04-07 01:16:51.899065 meilisearch_tui-0.5.1/pyproject.toml
+-rw-r--r--   0        0        0     3404 1970-01-01 00:00:00.000000 meilisearch_tui-0.5.1/PKG-INFO
```

### Comparing `meilisearch_tui-0.5.0/LICENSE` & `meilisearch_tui-0.5.1/LICENSE`

 * *Files identical despite different names*

### Comparing `meilisearch_tui-0.5.0/README.md` & `meilisearch_tui-0.5.1/README.md`

 * *Files identical despite different names*

### Comparing `meilisearch_tui-0.5.0/meilisearch_tui/__main__.py` & `meilisearch_tui-0.5.1/meilisearch_tui/__main__.py`

 * *Files 2% similar despite different names*

```diff
@@ -50,15 +50,15 @@
             self.set_theme()
             try:
                 async with get_client() as client:
                     indexes = await client.get_indexes()
                 if indexes:
                     self.push_screen("search")
                 else:
-                    self.push_screen("data_load")
+                    self.push_screen("index")
             except NoMeilisearchUrlError:
                 self.push_screen("configuration")
             except MeilisearchCommunicationError as e:
                 self.query_one(  # type: ignore
                     "#generic-error"
                 ).renderable = f"An error occured: {e}.\nMake sure the Meilisearch server is running and accessable"
             except Exception as e:
```

### Comparing `meilisearch_tui-0.5.0/meilisearch_tui/client.py` & `meilisearch_tui-0.5.1/meilisearch_tui/client.py`

 * *Files identical despite different names*

### Comparing `meilisearch_tui-0.5.0/meilisearch_tui/config.py` & `meilisearch_tui-0.5.1/meilisearch_tui/config.py`

 * *Files identical despite different names*

### Comparing `meilisearch_tui-0.5.0/meilisearch_tui/meilisearch.css` & `meilisearch_tui-0.5.1/meilisearch_tui/meilisearch.css`

 * *Files identical despite different names*

### Comparing `meilisearch_tui-0.5.0/meilisearch_tui/screens/configuration.py` & `meilisearch_tui-0.5.1/meilisearch_tui/screens/configuration.py`

 * *Files identical despite different names*

### Comparing `meilisearch_tui-0.5.0/meilisearch_tui/screens/indexes.py` & `meilisearch_tui-0.5.1/meilisearch_tui/screens/indexes.py`

 * *Files 2% similar despite different names*

```diff
@@ -437,14 +437,18 @@
     def index_sidebar(self) -> IndexSidebar:
         return self.query_one(IndexSidebar)
 
     @cached_property
     def meilisearch_settings(self) -> MeilisearchSettings:
         return self.query_one(MeilisearchSettings)
 
+    @cached_property
+    def tabbed_content(self) -> TabbedContent:
+        return self.query_one(TabbedContent)
+
     async def on_screen_resume(self, event: events.ScreenResume) -> None:
         self.body.visible = True
         self.generic_error.display = False
         await self.index_sidebar.update()
         try:
             async with get_client() as client:
                 indexes = await client.get_indexes()
@@ -465,14 +469,15 @@
             self.delete_index.selected_index = self.selected_index
             self.data_load.selected_index = self.selected_index
         else:
             self.selected_index = None
             self.meilisearch_settings.selected_index = None
             self.delete_index.selected_index = None
             self.data_load.selected_index = None
+            self.tabbed_content.active = "add-index"
 
     async def on_list_item__child_clicked(self, message: IndexSidebar.Selected) -> None:  # type: ignore[name-defined]
         self.selected_index = self.index_sidebar.selected_index
         self.meilisearch_settings.selected_index = self.index_sidebar.selected_index or ""
         self.delete_index.selected_index = self.index_sidebar.selected_index or None
         self.data_load.selected_index = self.index_sidebar.selected_index or None
```

### Comparing `meilisearch_tui-0.5.0/meilisearch_tui/screens/meilisearch_settings.py` & `meilisearch_tui-0.5.1/meilisearch_tui/screens/meilisearch_settings.py`

 * *Files identical despite different names*

### Comparing `meilisearch_tui-0.5.0/meilisearch_tui/screens/search.py` & `meilisearch_tui-0.5.1/meilisearch_tui/screens/search.py`

 * *Files identical despite different names*

### Comparing `meilisearch_tui-0.5.0/meilisearch_tui/utils.py` & `meilisearch_tui-0.5.1/meilisearch_tui/utils.py`

 * *Files identical despite different names*

### Comparing `meilisearch_tui-0.5.0/meilisearch_tui/widgets/index.py` & `meilisearch_tui-0.5.1/meilisearch_tui/widgets/index.py`

 * *Files identical despite different names*

### Comparing `meilisearch_tui-0.5.0/meilisearch_tui/widgets/index_sidebar.py` & `meilisearch_tui-0.5.1/meilisearch_tui/widgets/index_sidebar.py`

 * *Files identical despite different names*

### Comparing `meilisearch_tui-0.5.0/meilisearch_tui/widgets/input.py` & `meilisearch_tui-0.5.1/meilisearch_tui/widgets/input.py`

 * *Files identical despite different names*

### Comparing `meilisearch_tui-0.5.0/meilisearch_tui/widgets/messages.py` & `meilisearch_tui-0.5.1/meilisearch_tui/widgets/messages.py`

 * *Files identical despite different names*

### Comparing `meilisearch_tui-0.5.0/pyproject.toml` & `meilisearch_tui-0.5.1/pyproject.toml`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "meilisearch-tui"
-version = "0.5.0"
+version = "0.5.1"
 description = "A TUI for Managing and Searching with Meilisearch"
 authors = ["Paul Sanders <psanders1@gmail.com>"]
 license = "MIT"
 readme = "README.md"
 repository = "https://github.com/sanders41/meilisearch-tui"
 homepage = "https://github.com/sanders41/meilisearch-tui"
 documentation = "https://github.com/sanders41/meilisearch-tui"
```

### Comparing `meilisearch_tui-0.5.0/PKG-INFO` & `meilisearch_tui-0.5.1/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: meilisearch-tui
-Version: 0.5.0
+Version: 0.5.1
 Summary: A TUI for Managing and Searching with Meilisearch
 Home-page: https://github.com/sanders41/meilisearch-tui
 License: MIT
 Keywords: meilisearch,tui
 Author: Paul Sanders
 Author-email: psanders1@gmail.com
 Requires-Python: >=3.8,<4.0
```

