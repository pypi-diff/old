# Comparing `tmp/muffin-babel-1.3.3.tar.gz` & `tmp/muffin_babel-1.3.5.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "muffin-babel-1.3.3.tar", last modified: Thu Apr  6 11:06:36 2023, max compression
+gzip compressed data, was "muffin_babel-1.3.5.tar", max compression
```

## Comparing `muffin-babel-1.3.3.tar` & `muffin_babel-1.3.5.tar`

### file list

```diff
@@ -1,16 +1,5 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:06:36.830515 muffin-babel-1.3.3/
--rw-r--r--   0 runner    (1001) docker     (123)      116 2023-04-06 11:06:27.000000 muffin-babel-1.3.3/Changelog
--rw-r--r--   0 runner    (1001) docker     (123)      220 2023-04-06 11:06:27.000000 muffin-babel-1.3.3/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     5542 2023-04-06 11:06:36.830515 muffin-babel-1.3.3/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     4396 2023-04-06 11:06:27.000000 muffin-babel-1.3.3/README.rst
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:06:36.830515 muffin-babel-1.3.3/muffin_babel/
--rw-r--r--   0 runner    (1001) docker     (123)     8947 2023-04-06 11:06:27.000000 muffin-babel-1.3.3/muffin_babel/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 11:06:27.000000 muffin-babel-1.3.3/muffin_babel/py.typed
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:06:36.830515 muffin-babel-1.3.3/muffin_babel.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     5542 2023-04-06 11:06:36.000000 muffin-babel-1.3.3/muffin_babel.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      273 2023-04-06 11:06:36.000000 muffin-babel-1.3.3/muffin_babel.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 11:06:36.000000 muffin-babel-1.3.3/muffin_babel.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      179 2023-04-06 11:06:36.000000 muffin-babel-1.3.3/muffin_babel.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       13 2023-04-06 11:06:36.000000 muffin-babel-1.3.3/muffin_babel.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)     2068 2023-04-06 11:06:27.000000 muffin-babel-1.3.3/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 11:06:36.830515 muffin-babel-1.3.3/setup.cfg
+-rw-r--r--   0        0        0     4396 2023-04-06 16:36:52.600600 muffin_babel-1.3.5/README.rst
+-rw-r--r--   0        0        0     9100 2023-04-06 16:36:52.600600 muffin_babel-1.3.5/muffin_babel/__init__.py
+-rw-r--r--   0        0        0        0 2023-04-06 16:36:52.600600 muffin_babel-1.3.5/muffin_babel/py.typed
+-rw-r--r--   0        0        0     2030 2023-04-06 16:36:52.600600 muffin_babel-1.3.5/pyproject.toml
+-rw-r--r--   0        0        0     5691 1970-01-01 00:00:00.000000 muffin_babel-1.3.5/PKG-INFO
```

### Comparing `muffin-babel-1.3.3/PKG-INFO` & `muffin_babel-1.3.5/PKG-INFO`

 * *Files 7% similar despite different names*

```diff
@@ -1,34 +1,38 @@
 Metadata-Version: 2.1
 Name: muffin-babel
-Version: 1.3.3
+Version: 1.3.5
 Summary: Localization support for the Muffin Framework
-Author-email: Kirill Klenov <horneds@gmail.com>
-License: MIT License
-Project-URL: homepage, https://github.com/klen/muffin-babel
-Project-URL: repository, https://github.com/klen/muffin-babel
-Project-URL: changelog, https://raw.githubusercontent.com/klen/muffin-babel/master/Changelog
+Home-page: https://github.com/klen/muffin-babel
+License: MIT
 Keywords: localization,internationalization,muffin,babel,asyncio,trio,asgi
+Author: Kirill Klenov
+Author-email: horneds@gmail.com
+Requires-Python: >=3.8,<4.0
 Classifier: Development Status :: 5 - Production/Stable
+Classifier: Framework :: AsyncIO
+Classifier: Framework :: Trio
 Classifier: Intended Audience :: Developers
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Programming Language :: Python
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10
 Classifier: Programming Language :: Python :: 3.11
+Classifier: Programming Language :: Python :: 3
+Classifier: Programming Language :: Python :: 3.10
+Classifier: Programming Language :: Python :: 3.11
+Classifier: Programming Language :: Python :: 3.8
+Classifier: Programming Language :: Python :: 3.9
 Classifier: Topic :: Internet :: WWW/HTTP
-Classifier: Framework :: AsyncIO
-Classifier: Framework :: Trio
-Requires-Python: >=3.8
+Requires-Dist: asgi-babel (>=0,<1)
+Requires-Dist: muffin (>=0,<1)
+Project-URL: Repository, https://github.com/klen/muffin-babel
 Description-Content-Type: text/x-rst
-Provides-Extra: tests
-Provides-Extra: dev
-Provides-Extra: example
 
 Muffin-Babel
 ############
 
 .. _description:
 
 **Muffin-Babel** -- an extension to Muffin_ that adds localization support with help of Babel_.
@@ -206,7 +210,8 @@
 
 .. _klen: https://github.com/klen
 .. _Muffin: https://github.com/klen/muffin
 .. _Muffin-Jinja2: https://github.com/klen/muffin-jinja2
 .. _Babel: http://babel.edgewall.org/
 
 .. _MIT license: http://opensource.org/licenses/MIT
+
```

### Comparing `muffin-babel-1.3.3/README.rst` & `muffin_babel-1.3.5/README.rst`

 * *Files identical despite different names*

### Comparing `muffin-babel-1.3.3/muffin_babel/__init__.py` & `muffin_babel-1.3.5/muffin_babel/__init__.py`

 * *Files 10% similar despite different names*

```diff
@@ -1,36 +1,26 @@
 """Muffin-Babel -- I18n engine for Muffin framework."""
 import logging
+from contextlib import contextmanager
 from pathlib import Path
-from typing import (
-    TYPE_CHECKING,
-    Any,
-    Awaitable,
-    Callable,
-    Dict,
-    Optional,
-    Tuple,
-    TypeVar,
-)
+from typing import TYPE_CHECKING, Any, Awaitable, Callable, Dict, Optional, Tuple, TypeVar
 
 from asgi_babel import current_locale, select_locale_by_request
 from babel import Locale, support
+from babel.messages.catalog import Catalog
 from babel.messages.extract import extract_from_dir
-from babel.messages.frontend import Catalog
 from babel.messages.mofile import write_mo
 from babel.messages.pofile import read_po, write_po
 from muffin import Application, Request
 from muffin.plugins import BasePlugin
 
 logger = logging.getLogger(__name__)
 logger.addHandler(logging.NullHandler())
 
 if TYPE_CHECKING:
-    from numbers import Number
-
     from asgi_tools.types import TASGIReceive, TASGISend
 
 TLocaleSelector = Callable[[Request], Awaitable[Optional[str]]]
 TVLocaleSelector = TypeVar("TVLocaleSelector", bound=TLocaleSelector)
 
 TRANSLATIONS: Dict[Tuple[str, str], support.Translations] = {}
 
@@ -88,15 +78,14 @@
             catalog = Catalog(locale=locale, project=project, charset=charset)
             for dpath in dirs:
                 for filename, lineno, message, comments, context in extract_from_dir(
                     dpath,
                     method_map=self.cfg.sources_map,
                     options_map=self.cfg.options_map,
                 ):
-
                     lines = []
                     if locations:
                         filepath = dpath.absolute() / filename
                         lines = [(filepath.as_posix(), lineno)]
 
                     catalog.add(
                         message,
@@ -119,19 +108,15 @@
                 output.parent.mkdir(parents=True)
 
             logger.info("writing PO template file to %s", output)
             with output.open("wb") as f:
                 write_po(f, catalog, sort_output=not locations, sort_by_file=locations)
 
         @app.manage(lifespan=False)
-        def babel_compile_messages(
-            *,
-            use_fuzzy=False,
-            domain=self.cfg.domain,
-        ):
+        def babel_compile_messages(*, use_fuzzy=False, domain=self.cfg.domain):
             """Compile messages for locales.
 
             :param domain:  set domain name for locales
             """
             for locales_dir in self.cfg.locale_folders:
                 source = Path(locales_dir)
                 for locale in source.iterdir():
@@ -145,24 +130,19 @@
                     mo_file = po_file.with_suffix(".mo")
 
                     with mo_file.open("wb") as mo:
                         logger.info("writing MO template file to %s", mo_file)
                         write_mo(mo, catalog, use_fuzzy=use_fuzzy)
 
     async def __middleware__(
-        self,
-        handler: Callable,
-        request: Request,
-        receive: "TASGIReceive",
-        send: "TASGISend",
+        self, handler: Callable, request: Request, receive: "TASGIReceive", send: "TASGISend"
     ) -> Any:
         """Auto detect a locale by the given request."""
         lang = await self.__locale_selector(request)
-        self.current_locale = lang or self.cfg.default_locale
-
+        self.current_locale = lang or self.cfg.default_locale  # type: ignore[assignment]
         return await handler(request, receive, send)
 
     async def startup(self):
         """Tune Jinja2 if the plugin is installed."""
         if self.cfg.configure_jinja2 and "jinja2" in self.app.plugins:
             jinja2 = self.app.plugins["jinja2"]
             jinja2.env.add_extension("jinja2.ext.i18n")
@@ -178,83 +158,79 @@
         return fn
 
     @property
     def current_locale(self) -> Locale:
         """Get current locale."""
         locale = current_locale.get()
         if locale is None:
-            self.current_locale = locale = self.cfg.default_locale
+            locale = Locale.parse(self.cfg.default_locale, sep="-")
+            current_locale.set(locale)
         return locale
 
     @current_locale.setter
     def current_locale(self, lang: str):
         """Set current locale."""
         return current_locale.set(Locale.parse(lang, sep="-"))
 
+    @contextmanager
+    def locale_ctx(self, lang: str):
+        """Update current locale as context manager."""
+        old_locale = current_locale.get()
+        self.current_locale = lang  # type: ignore[assignment]
+        yield self
+        current_locale.set(old_locale)
+
     def get_translations(
-        self,
-        domain: Optional[str] = None,
-        locale: Optional[Locale] = None,
+        self, domain: Optional[str] = None, locale: Optional[Locale] = None
     ) -> support.Translations:
         """Load and cache translations."""
         locale = locale or self.current_locale
         domain = domain or self.cfg.domain
         if (domain, locale.language) not in TRANSLATIONS:
             translations = None
             for path in reversed(self.cfg.locale_folders):
-                trans = support.Translations.load(path, locales=locale, domain=domain)
+                trans = support.Translations.load(path, locales=locale.language, domain=domain)
                 if translations:
                     translations._catalog.update(trans._catalog)
                 else:
                     translations = trans
 
-            TRANSLATIONS[(domain, locale.language)] = translations
+            TRANSLATIONS[(domain, locale.language)] = translations  # type: ignore[assignment]
 
         return TRANSLATIONS[(domain, locale.language)]
 
     def gettext(self, string: str, domain: Optional[str] = None, **variables) -> str:
         """Translate a string with the current locale."""
         t = self.get_translations(domain)
         return t.ugettext(string) % variables
 
     def ngettext(
-        self,
-        singular: str,
-        plural: str,
-        num: "Number",
-        domain: Optional[str] = None,
-        **variables,
+        self, singular: str, plural: str, num: int, domain: Optional[str] = None, **variables
     ) -> str:
         """Translate a string wity the current locale.
 
         The `num` parameter is used to dispatch between singular and various plural forms of the
         message.
 
         """
         variables.setdefault("num", num)
         t = self.get_translations(domain)
         return t.ungettext(singular, plural, num) % variables
 
-    def pgettext(
-        self,
-        context: str,
-        string: str,
-        domain: Optional[str] = None,
-        **variables,
-    ) -> str:
+    def pgettext(self, context: str, string: str, domain: Optional[str] = None, **variables) -> str:
         """Like :meth:`gettext` but with a context."""
         t = self.get_translations(domain)
         return t.upgettext(context, string) % variables
 
     def npgettext(
         self,
         context: str,
         singular: str,
         plural: str,
-        num: "Number",
+        num: int,
         domain: Optional[str] = None,
         **variables,
     ) -> str:
         """Like :meth:`ngettext` but with a context."""
         variables.setdefault("num", num)
         t = self.get_translations(domain)
         return t.unpgettext(context, singular, plural, num) % variables
```

### Comparing `muffin-babel-1.3.3/pyproject.toml` & `muffin_babel-1.3.5/pyproject.toml`

 * *Files 19% similar despite different names*

```diff
@@ -1,15 +1,14 @@
-[project]
+[tool.poetry]
 name = "muffin-babel"
-version = "1.3.3"
+version = "1.3.5"
 description = "Localization support for the Muffin Framework"
 readme = "README.rst"
-requires-python = ">=3.8"
-license = {"text" = "MIT License"}
-authors = [{ name = "Kirill Klenov", email = "horneds@gmail.com" }]
+license = "MIT"
+authors = ["Kirill Klenov <horneds@gmail.com>"]
 keywords = ["localization", "internationalization", "muffin", "babel", "asyncio", "trio", "asgi"]
 classifiers = [
   "Development Status :: 5 - Production/Stable",
   "Intended Audience :: Developers",
   "License :: OSI Approved :: MIT License",
   "Programming Language :: Python",
   "Programming Language :: Python :: 3",
@@ -17,40 +16,34 @@
   "Programming Language :: Python :: 3.9",
   "Programming Language :: Python :: 3.10",
   "Programming Language :: Python :: 3.11",
   "Topic :: Internet :: WWW/HTTP",
   "Framework :: AsyncIO",
   "Framework :: Trio",
 ]
-dependencies = [
-  "asgi-babel >= 0.8.9",
-  "muffin >= 0.92",
-]
-
-[project.urls]
 homepage = "https://github.com/klen/muffin-babel"
 repository = "https://github.com/klen/muffin-babel"
-changelog = "https://raw.githubusercontent.com/klen/muffin-babel/master/Changelog"
-
-[project.optional-dependencies]
-tests = [
-  "muffin-jinja2 >= 1.7.0",
-  "pytest",
-  "pytest-aio[curio,trio]",
-  "pytest-mypy",
-  "ruff",
+packages = [
+  { include = "muffin_babel" },
 ]
-dev = ["pre-commit", "refurb", "bump2version"]
-example = ["uvicorn", "muffin-jinja2"]
-
-[tool.setuptools]
-packages = ['muffin_babel']
 
-[tool.setuptools.package-data]
-muffin_babel = ["py.typed"]
+[tool.poetry.dependencies]
+python = "^3.8"
+asgi-babel = "^0"
+muffin = "^0"
+
+[tool.poetry.group.dev.dependencies]
+ruff = "*"
+black = "*"
+pre-commit = "*"
+pytest = "*"
+pytest-mypy = "*"
+pytest-aio = { version = "*", extras = ["curio", "trio"] }
+uvicorn = "*"
+muffin-jinja2 = "*"
 
 [tool.pytest.ini_options]
 addopts = "-xsv"
 log_cli = true
 
 [tool.mypy]
 packages = ["muffin_babel"]
@@ -71,13 +64,24 @@
 [testenv:pypy39]
 deps = -e .[tests]
 commands =
 	pytest tests.py
 """
 
 [tool.ruff]
-fix = true
 line-length = 100
 target-version = "py38"
 exclude = [".venv", "docs", "examples"]
 select = ["ALL"]
-ignore = ["D", "UP", "ANN", "DJ", "EM", "RSE", "SLF", "RET", "S101", "PLR2004", "PLR0912", "N804", "A003", "TRY003"]
+ignore = [
+  "ANN", "ARG", "UP", "D", "DJ", "COM", "EM", "RSE", "SLF", "RET", "S101", "PLR2004",
+  "PLR0912", "N804", "A003", "TRY003", "RUF001"
+]
+
+[tool.black]
+line-length = 100
+target-version = ["py310", "py311"]
+preview = true
+
+[build-system]
+requires = ["poetry-core>=1.0.0"]
+build-backend = "poetry.core.masonry.api"
```

