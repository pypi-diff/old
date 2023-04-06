# Comparing `tmp/muffin-babel-1.3.1.tar.gz` & `tmp/muffin-babel-1.3.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "muffin-babel-1.3.1.tar", last modified: Sat Mar  4 12:18:32 2023, max compression
+gzip compressed data, was "muffin-babel-1.3.3.tar", last modified: Thu Apr  6 11:06:36 2023, max compression
```

## Comparing `muffin-babel-1.3.1.tar` & `muffin-babel-1.3.3.tar`

### file list

```diff
@@ -1,16 +1,16 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-04 12:18:32.114260 muffin-babel-1.3.1/
--rw-r--r--   0 runner    (1001) docker     (123)      116 2023-03-04 12:18:23.000000 muffin-babel-1.3.1/Changelog
--rw-r--r--   0 runner    (1001) docker     (123)      220 2023-03-04 12:18:23.000000 muffin-babel-1.3.1/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     5542 2023-03-04 12:18:32.114260 muffin-babel-1.3.1/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     4396 2023-03-04 12:18:23.000000 muffin-babel-1.3.1/README.rst
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-04 12:18:32.110260 muffin-babel-1.3.1/muffin_babel/
--rw-r--r--   0 runner    (1001) docker     (123)     8740 2023-03-04 12:18:23.000000 muffin-babel-1.3.1/muffin_babel/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-04 12:18:23.000000 muffin-babel-1.3.1/muffin_babel/py.typed
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-04 12:18:32.114260 muffin-babel-1.3.1/muffin_babel.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     5542 2023-03-04 12:18:32.000000 muffin-babel-1.3.1/muffin_babel.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      273 2023-03-04 12:18:32.000000 muffin-babel-1.3.1/muffin_babel.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-04 12:18:32.000000 muffin-babel-1.3.1/muffin_babel.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      179 2023-03-04 12:18:32.000000 muffin-babel-1.3.1/muffin_babel.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       13 2023-03-04 12:18:32.000000 muffin-babel-1.3.1/muffin_babel.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)     2068 2023-03-04 12:18:23.000000 muffin-babel-1.3.1/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-04 12:18:32.114260 muffin-babel-1.3.1/setup.cfg
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:06:36.830515 muffin-babel-1.3.3/
+-rw-r--r--   0 runner    (1001) docker     (123)      116 2023-04-06 11:06:27.000000 muffin-babel-1.3.3/Changelog
+-rw-r--r--   0 runner    (1001) docker     (123)      220 2023-04-06 11:06:27.000000 muffin-babel-1.3.3/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     5542 2023-04-06 11:06:36.830515 muffin-babel-1.3.3/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     4396 2023-04-06 11:06:27.000000 muffin-babel-1.3.3/README.rst
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:06:36.830515 muffin-babel-1.3.3/muffin_babel/
+-rw-r--r--   0 runner    (1001) docker     (123)     8947 2023-04-06 11:06:27.000000 muffin-babel-1.3.3/muffin_babel/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 11:06:27.000000 muffin-babel-1.3.3/muffin_babel/py.typed
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:06:36.830515 muffin-babel-1.3.3/muffin_babel.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     5542 2023-04-06 11:06:36.000000 muffin-babel-1.3.3/muffin_babel.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      273 2023-04-06 11:06:36.000000 muffin-babel-1.3.3/muffin_babel.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 11:06:36.000000 muffin-babel-1.3.3/muffin_babel.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      179 2023-04-06 11:06:36.000000 muffin-babel-1.3.3/muffin_babel.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       13 2023-04-06 11:06:36.000000 muffin-babel-1.3.3/muffin_babel.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     2068 2023-04-06 11:06:27.000000 muffin-babel-1.3.3/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 11:06:36.830515 muffin-babel-1.3.3/setup.cfg
```

### Comparing `muffin-babel-1.3.1/PKG-INFO` & `muffin-babel-1.3.3/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: muffin-babel
-Version: 1.3.1
+Version: 1.3.3
 Summary: Localization support for the Muffin Framework
 Author-email: Kirill Klenov <horneds@gmail.com>
 License: MIT License
 Project-URL: homepage, https://github.com/klen/muffin-babel
 Project-URL: repository, https://github.com/klen/muffin-babel
 Project-URL: changelog, https://raw.githubusercontent.com/klen/muffin-babel/master/Changelog
 Keywords: localization,internationalization,muffin,babel,asyncio,trio,asgi
```

### Comparing `muffin-babel-1.3.1/README.rst` & `muffin-babel-1.3.3/README.rst`

 * *Files identical despite different names*

### Comparing `muffin-babel-1.3.1/muffin_babel/__init__.py` & `muffin-babel-1.3.3/muffin_babel/__init__.py`

 * *Files 3% similar despite different names*

```diff
@@ -1,11 +1,20 @@
 """Muffin-Babel -- I18n engine for Muffin framework."""
 import logging
 from pathlib import Path
-from typing import TYPE_CHECKING, Any, Awaitable, Callable, Dict, Optional, Tuple, TypeVar
+from typing import (
+    TYPE_CHECKING,
+    Any,
+    Awaitable,
+    Callable,
+    Dict,
+    Optional,
+    Tuple,
+    TypeVar,
+)
 
 from asgi_babel import current_locale, select_locale_by_request
 from babel import Locale, support
 from babel.messages.extract import extract_from_dir
 from babel.messages.frontend import Catalog
 from babel.messages.mofile import write_mo
 from babel.messages.pofile import read_po, write_po
@@ -39,20 +48,21 @@
         "sources_map": [
             ("**.py", "python"),
             ("**.html", "jinja2"),
         ],
         "options_map": {"**.html": {"encoding": "utf-8"}},
     }
 
-    def setup(self, app: Application, **options): # noqa: C901
+    def setup(self, app: Application, **options):  # noqa: C901
         """Setup the plugin's commands."""
         super(Plugin, self).setup(app, **options)
 
         self.__locale_selector: Callable[
-            [Request], Awaitable[Optional[str]],
+            [Request],
+            Awaitable[Optional[str]],
         ] = select_locale_by_request
 
         # Install a middleware for autodetection
         if self.cfg.auto_detect_locale:
             app.middleware(self.__middleware__, insert_first=True)
 
         @app.manage(lifespan=False)
@@ -82,18 +92,22 @@
                     method_map=self.cfg.sources_map,
                     options_map=self.cfg.options_map,
                 ):
 
                     lines = []
                     if locations:
                         filepath = dpath.absolute() / filename
-                        lines = [(filepath, lineno)]
+                        lines = [(filepath.as_posix(), lineno)]
 
                     catalog.add(
-                        message, None, lines, auto_comments=comments, context=context,
+                        message,
+                        None,
+                        lines,
+                        auto_comments=comments,
+                        context=context,
                     )
 
             locales_dir = Path(self.cfg.locale_folders[0])
             output = locales_dir / locale / "LC_MESSAGES" / f"{domain}.po"
 
             if output.exists():
                 with output.open("rb") as f:
@@ -106,29 +120,31 @@
 
             logger.info("writing PO template file to %s", output)
             with output.open("wb") as f:
                 write_po(f, catalog, sort_output=not locations, sort_by_file=locations)
 
         @app.manage(lifespan=False)
         def babel_compile_messages(
-            *, use_fuzzy=False, domain=self.cfg.domain,
+            *,
+            use_fuzzy=False,
+            domain=self.cfg.domain,
         ):
             """Compile messages for locales.
 
             :param domain:  set domain name for locales
             """
             for locales_dir in self.cfg.locale_folders:
                 source = Path(locales_dir)
                 for locale in source.iterdir():
                     po_file = locale / "LC_MESSAGES" / f"{domain}.po"
                     if not po_file.exists():
                         continue
 
                     with po_file.open("rb") as po:
-                        catalog = read_po(po, locale)
+                        catalog = read_po(po, locale.as_posix())
 
                     mo_file = po_file.with_suffix(".mo")
 
                     with mo_file.open("wb") as mo:
                         logger.info("writing MO template file to %s", mo_file)
                         write_mo(mo, catalog, use_fuzzy=use_fuzzy)
 
@@ -162,25 +178,26 @@
         return fn
 
     @property
     def current_locale(self) -> Locale:
         """Get current locale."""
         locale = current_locale.get()
         if locale is None:
-            self.current_locale = self.cfg.default_locale
-            locale = current_locale.get()
+            self.current_locale = locale = self.cfg.default_locale
         return locale
 
     @current_locale.setter
     def current_locale(self, lang: str):
         """Set current locale."""
         return current_locale.set(Locale.parse(lang, sep="-"))
 
     def get_translations(
-        self, domain: Optional[str] = None, locale: Optional[Locale] = None,
+        self,
+        domain: Optional[str] = None,
+        locale: Optional[Locale] = None,
     ) -> support.Translations:
         """Load and cache translations."""
         locale = locale or self.current_locale
         domain = domain or self.cfg.domain
         if (domain, locale.language) not in TRANSLATIONS:
             translations = None
             for path in reversed(self.cfg.locale_folders):
@@ -214,15 +231,19 @@
 
         """
         variables.setdefault("num", num)
         t = self.get_translations(domain)
         return t.ungettext(singular, plural, num) % variables
 
     def pgettext(
-        self, context: str, string: str, domain: Optional[str] = None, **variables,
+        self,
+        context: str,
+        string: str,
+        domain: Optional[str] = None,
+        **variables,
     ) -> str:
         """Like :meth:`gettext` but with a context."""
         t = self.get_translations(domain)
         return t.upgettext(context, string) % variables
 
     def npgettext(
         self,
```

### Comparing `muffin-babel-1.3.1/muffin_babel.egg-info/PKG-INFO` & `muffin-babel-1.3.3/muffin_babel.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: muffin-babel
-Version: 1.3.1
+Version: 1.3.3
 Summary: Localization support for the Muffin Framework
 Author-email: Kirill Klenov <horneds@gmail.com>
 License: MIT License
 Project-URL: homepage, https://github.com/klen/muffin-babel
 Project-URL: repository, https://github.com/klen/muffin-babel
 Project-URL: changelog, https://raw.githubusercontent.com/klen/muffin-babel/master/Changelog
 Keywords: localization,internationalization,muffin,babel,asyncio,trio,asgi
```

### Comparing `muffin-babel-1.3.1/pyproject.toml` & `muffin-babel-1.3.3/pyproject.toml`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [project]
 name = "muffin-babel"
-version = "1.3.1"
+version = "1.3.3"
 description = "Localization support for the Muffin Framework"
 readme = "README.rst"
 requires-python = ">=3.8"
 license = {"text" = "MIT License"}
 authors = [{ name = "Kirill Klenov", email = "horneds@gmail.com" }]
 keywords = ["localization", "internationalization", "muffin", "babel", "asyncio", "trio", "asgi"]
 classifiers = [
```

