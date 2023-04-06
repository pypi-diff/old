# Comparing `tmp/types-beautifulsoup4-4.9.3.tar.gz` & `tmp/types-beautifulsoup4-4.9.4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "types-beautifulsoup4-4.9.3.tar", last modified: Wed Aug 11 03:18:55 2021, max compression
+gzip compressed data, was "types-beautifulsoup4-4.9.4.tar", last modified: Sun Aug 15 15:18:00 2021, max compression
```

## Comparing `types-beautifulsoup4-4.9.3.tar` & `types-beautifulsoup4-4.9.4.tar`

### file list

```diff
@@ -1,21 +1,21 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-08-11 03:18:55.241023 types-beautifulsoup4-4.9.3/
--rw-r--r--   0 runner    (1001) docker     (121)      987 2021-08-11 03:18:55.241023 types-beautifulsoup4-4.9.3/PKG-INFO
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-08-11 03:18:55.237023 types-beautifulsoup4-4.9.3/bs4-stubs/
--rw-r--r--   0 runner    (1001) docker     (121)       16 2021-08-11 03:18:54.000000 types-beautifulsoup4-4.9.3/bs4-stubs/METADATA.toml
--rw-r--r--   0 runner    (1001) docker     (121)     2560 2021-08-11 03:18:45.000000 types-beautifulsoup4-4.9.3/bs4-stubs/__init__.pyi
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-08-11 03:18:55.237023 types-beautifulsoup4-4.9.3/bs4-stubs/builder/
--rw-r--r--   0 runner    (1001) docker     (121)     2246 2021-08-11 03:18:45.000000 types-beautifulsoup4-4.9.3/bs4-stubs/builder/__init__.pyi
--rw-r--r--   0 runner    (1001) docker     (121)     2397 2021-08-11 03:18:45.000000 types-beautifulsoup4-4.9.3/bs4-stubs/builder/_html5lib.pyi
--rw-r--r--   0 runner    (1001) docker     (121)     1470 2021-08-11 03:18:45.000000 types-beautifulsoup4-4.9.3/bs4-stubs/builder/_htmlparser.pyi
--rw-r--r--   0 runner    (1001) docker     (121)     1677 2021-08-11 03:18:45.000000 types-beautifulsoup4-4.9.3/bs4-stubs/builder/_lxml.pyi
--rw-r--r--   0 runner    (1001) docker     (121)     2049 2021-08-11 03:18:45.000000 types-beautifulsoup4-4.9.3/bs4-stubs/dammit.pyi
--rw-r--r--   0 runner    (1001) docker     (121)      876 2021-08-11 03:18:45.000000 types-beautifulsoup4-4.9.3/bs4-stubs/diagnose.pyi
--rw-r--r--   0 runner    (1001) docker     (121)    13838 2021-08-11 03:18:45.000000 types-beautifulsoup4-4.9.3/bs4-stubs/element.pyi
--rw-r--r--   0 runner    (1001) docker     (121)     1338 2021-08-11 03:18:45.000000 types-beautifulsoup4-4.9.3/bs4-stubs/formatter.pyi
--rw-r--r--   0 runner    (1001) docker     (121)       38 2021-08-11 03:18:55.241023 types-beautifulsoup4-4.9.3/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)     1367 2021-08-11 03:18:54.000000 types-beautifulsoup4-4.9.3/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-08-11 03:18:55.241023 types-beautifulsoup4-4.9.3/types_beautifulsoup4.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)      987 2021-08-11 03:18:55.000000 types-beautifulsoup4-4.9.3/types_beautifulsoup4.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)      446 2021-08-11 03:18:55.000000 types-beautifulsoup4-4.9.3/types_beautifulsoup4.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2021-08-11 03:18:55.000000 types-beautifulsoup4-4.9.3/types_beautifulsoup4.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)       10 2021-08-11 03:18:55.000000 types-beautifulsoup4-4.9.3/types_beautifulsoup4.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-08-15 15:18:00.534419 types-beautifulsoup4-4.9.4/
+-rw-r--r--   0 runner    (1001) docker     (121)      987 2021-08-15 15:18:00.534419 types-beautifulsoup4-4.9.4/PKG-INFO
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-08-15 15:18:00.534419 types-beautifulsoup4-4.9.4/bs4-stubs/
+-rw-r--r--   0 runner    (1001) docker     (121)       16 2021-08-15 15:17:59.000000 types-beautifulsoup4-4.9.4/bs4-stubs/METADATA.toml
+-rw-r--r--   0 runner    (1001) docker     (121)     2560 2021-08-15 15:17:49.000000 types-beautifulsoup4-4.9.4/bs4-stubs/__init__.pyi
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-08-15 15:18:00.534419 types-beautifulsoup4-4.9.4/bs4-stubs/builder/
+-rw-r--r--   0 runner    (1001) docker     (121)     2246 2021-08-15 15:17:49.000000 types-beautifulsoup4-4.9.4/bs4-stubs/builder/__init__.pyi
+-rw-r--r--   0 runner    (1001) docker     (121)     2397 2021-08-15 15:17:49.000000 types-beautifulsoup4-4.9.4/bs4-stubs/builder/_html5lib.pyi
+-rw-r--r--   0 runner    (1001) docker     (121)     1470 2021-08-15 15:17:49.000000 types-beautifulsoup4-4.9.4/bs4-stubs/builder/_htmlparser.pyi
+-rw-r--r--   0 runner    (1001) docker     (121)     1677 2021-08-15 15:17:49.000000 types-beautifulsoup4-4.9.4/bs4-stubs/builder/_lxml.pyi
+-rw-r--r--   0 runner    (1001) docker     (121)     2049 2021-08-15 15:17:49.000000 types-beautifulsoup4-4.9.4/bs4-stubs/dammit.pyi
+-rw-r--r--   0 runner    (1001) docker     (121)      876 2021-08-15 15:17:49.000000 types-beautifulsoup4-4.9.4/bs4-stubs/diagnose.pyi
+-rw-r--r--   0 runner    (1001) docker     (121)    13833 2021-08-15 15:17:49.000000 types-beautifulsoup4-4.9.4/bs4-stubs/element.pyi
+-rw-r--r--   0 runner    (1001) docker     (121)     1338 2021-08-15 15:17:49.000000 types-beautifulsoup4-4.9.4/bs4-stubs/formatter.pyi
+-rw-r--r--   0 runner    (1001) docker     (121)       38 2021-08-15 15:18:00.534419 types-beautifulsoup4-4.9.4/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (121)     1367 2021-08-15 15:17:59.000000 types-beautifulsoup4-4.9.4/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-08-15 15:18:00.534419 types-beautifulsoup4-4.9.4/types_beautifulsoup4.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (121)      987 2021-08-15 15:18:00.000000 types-beautifulsoup4-4.9.4/types_beautifulsoup4.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)      446 2021-08-15 15:18:00.000000 types-beautifulsoup4-4.9.4/types_beautifulsoup4.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2021-08-15 15:18:00.000000 types-beautifulsoup4-4.9.4/types_beautifulsoup4.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       10 2021-08-15 15:18:00.000000 types-beautifulsoup4-4.9.4/types_beautifulsoup4.egg-info/top_level.txt
```

### Comparing `types-beautifulsoup4-4.9.3/PKG-INFO` & `types-beautifulsoup4-4.9.4/PKG-INFO`

 * *Files 18% similar despite different names*

```diff
@@ -1,21 +1,21 @@
 Metadata-Version: 2.1
 Name: types-beautifulsoup4
-Version: 4.9.3
+Version: 4.9.4
 Summary: Typing stubs for beautifulsoup4
 Home-page: https://github.com/python/typeshed
 License: Apache-2.0 license
 Description: ## Typing stubs for beautifulsoup4
         
         This is a PEP 561 type stub package for the `beautifulsoup4` package.
         It can be used by type-checking tools like mypy, PyCharm, pytype etc. to check code
         that uses `beautifulsoup4`. The source for this package can be found at
         https://github.com/python/typeshed/tree/master/stubs/beautifulsoup4. All fixes for
         types and metadata should be contributed there.
         
         See https://github.com/python/typeshed/blob/master/README.md for more details.
-        This package was generated from typeshed commit `96358fd944b6b413f49c85085f3c2b44ba2fe954`.
+        This package was generated from typeshed commit `3ce5502675d3c23394b592f00234fbdfc743a7d5`.
         
 Platform: UNKNOWN
 Classifier: License :: OSI Approved :: Apache Software License
 Classifier: Typing :: Typed
 Description-Content-Type: text/markdown
```

### Comparing `types-beautifulsoup4-4.9.3/bs4-stubs/__init__.pyi` & `types-beautifulsoup4-4.9.4/bs4-stubs/__init__.pyi`

 * *Files identical despite different names*

### Comparing `types-beautifulsoup4-4.9.3/bs4-stubs/builder/__init__.pyi` & `types-beautifulsoup4-4.9.4/bs4-stubs/builder/__init__.pyi`

 * *Files identical despite different names*

### Comparing `types-beautifulsoup4-4.9.3/bs4-stubs/builder/_html5lib.pyi` & `types-beautifulsoup4-4.9.4/bs4-stubs/builder/_html5lib.pyi`

 * *Files identical despite different names*

### Comparing `types-beautifulsoup4-4.9.3/bs4-stubs/builder/_htmlparser.pyi` & `types-beautifulsoup4-4.9.4/bs4-stubs/builder/_htmlparser.pyi`

 * *Files identical despite different names*

### Comparing `types-beautifulsoup4-4.9.3/bs4-stubs/builder/_lxml.pyi` & `types-beautifulsoup4-4.9.4/bs4-stubs/builder/_lxml.pyi`

 * *Files identical despite different names*

### Comparing `types-beautifulsoup4-4.9.3/bs4-stubs/dammit.pyi` & `types-beautifulsoup4-4.9.4/bs4-stubs/dammit.pyi`

 * *Files identical despite different names*

### Comparing `types-beautifulsoup4-4.9.3/bs4-stubs/diagnose.pyi` & `types-beautifulsoup4-4.9.4/bs4-stubs/diagnose.pyi`

 * *Files identical despite different names*

### Comparing `types-beautifulsoup4-4.9.3/bs4-stubs/element.pyi` & `types-beautifulsoup4-4.9.4/bs4-stubs/element.pyi`

 * *Files 1% similar despite different names*

```diff
@@ -46,26 +46,26 @@
         previous_sibling: PageElement | None = ...,
         next_sibling: PageElement | None = ...,
     ) -> None: ...
     def format_string(self, s: str, formatter: Formatter | str | None) -> str: ...
     def formatter_for_name(self, formatter: Formatter | str | _EntitySubstitution): ...
     nextSibling: PageElement | None
     previousSibling: PageElement | None
-    def replace_with(self: Self, replace_with: PageElement) -> Self: ...
-    def replaceWith(self: Self, replace_with: PageElement) -> Self: ...
+    def replace_with(self: Self, replace_with: PageElement | str) -> Self: ...
+    replaceWith = replace_with
     def unwrap(self: Self) -> Self: ...
     replace_with_children = unwrap
     replaceWithChildren = unwrap
     def wrap(self, wrap_inside: _PageElementT) -> _PageElementT: ...
     def extract(self: Self, _self_index: int | None = ...) -> Self: ...
-    def insert(self, position: int, new_child: PageElement) -> None: ...
-    def append(self, tag: PageElement) -> None: ...
-    def extend(self, tags: Iterable[PageElement]) -> None: ...
-    def insert_before(self, *args: PageElement) -> None: ...
-    def insert_after(self, *args: PageElement) -> None: ...
+    def insert(self, position: int, new_child: PageElement | str) -> None: ...
+    def append(self, tag: PageElement | str) -> None: ...
+    def extend(self, tags: Iterable[PageElement | str]) -> None: ...
+    def insert_before(self, *args: PageElement | str) -> None: ...
+    def insert_after(self, *args: PageElement | str) -> None: ...
     def find_next(
         self,
         name: _Strainable | SoupStrainer | None = ...,
         attrs: dict[str, _Strainable] | _Strainable = ...,
         text: _Strainable | None = ...,
         **kwargs: _Strainable,
     ) -> Tag | NavigableString | None: ...
```

### Comparing `types-beautifulsoup4-4.9.3/bs4-stubs/formatter.pyi` & `types-beautifulsoup4-4.9.4/bs4-stubs/formatter.pyi`

 * *Files identical despite different names*

### Comparing `types-beautifulsoup4-4.9.3/setup.py` & `types-beautifulsoup4-4.9.4/setup.py`

 * *Files 16% similar despite different names*

```diff
@@ -8,19 +8,19 @@
 This is a PEP 561 type stub package for the `beautifulsoup4` package.
 It can be used by type-checking tools like mypy, PyCharm, pytype etc. to check code
 that uses `beautifulsoup4`. The source for this package can be found at
 https://github.com/python/typeshed/tree/master/stubs/beautifulsoup4. All fixes for
 types and metadata should be contributed there.
 
 See https://github.com/python/typeshed/blob/master/README.md for more details.
-This package was generated from typeshed commit `96358fd944b6b413f49c85085f3c2b44ba2fe954`.
+This package was generated from typeshed commit `3ce5502675d3c23394b592f00234fbdfc743a7d5`.
 '''.lstrip()
 
 setup(name=name,
-      version="4.9.3",
+      version="4.9.4",
       description=description,
       long_description=long_description,
       long_description_content_type="text/markdown",
       url="https://github.com/python/typeshed",
       install_requires=[],
       packages=['bs4-stubs'],
       package_data={'bs4-stubs': ['__init__.pyi', 'diagnose.pyi', 'dammit.pyi', 'element.pyi', 'formatter.pyi', 'builder/__init__.pyi', 'builder/_htmlparser.pyi', 'builder/_html5lib.pyi', 'builder/_lxml.pyi', 'METADATA.toml']},
```

### Comparing `types-beautifulsoup4-4.9.3/types_beautifulsoup4.egg-info/PKG-INFO` & `types-beautifulsoup4-4.9.4/types_beautifulsoup4.egg-info/PKG-INFO`

 * *Files 18% similar despite different names*

```diff
@@ -1,21 +1,21 @@
 Metadata-Version: 2.1
 Name: types-beautifulsoup4
-Version: 4.9.3
+Version: 4.9.4
 Summary: Typing stubs for beautifulsoup4
 Home-page: https://github.com/python/typeshed
 License: Apache-2.0 license
 Description: ## Typing stubs for beautifulsoup4
         
         This is a PEP 561 type stub package for the `beautifulsoup4` package.
         It can be used by type-checking tools like mypy, PyCharm, pytype etc. to check code
         that uses `beautifulsoup4`. The source for this package can be found at
         https://github.com/python/typeshed/tree/master/stubs/beautifulsoup4. All fixes for
         types and metadata should be contributed there.
         
         See https://github.com/python/typeshed/blob/master/README.md for more details.
-        This package was generated from typeshed commit `96358fd944b6b413f49c85085f3c2b44ba2fe954`.
+        This package was generated from typeshed commit `3ce5502675d3c23394b592f00234fbdfc743a7d5`.
         
 Platform: UNKNOWN
 Classifier: License :: OSI Approved :: Apache Software License
 Classifier: Typing :: Typed
 Description-Content-Type: text/markdown
```

