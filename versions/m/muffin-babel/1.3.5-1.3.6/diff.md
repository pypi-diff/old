# Comparing `tmp/muffin_babel-1.3.5.tar.gz` & `tmp/muffin_babel-1.3.6.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "muffin_babel-1.3.5.tar", max compression
+gzip compressed data, was "muffin_babel-1.3.6.tar", max compression
```

## Comparing `muffin_babel-1.3.5.tar` & `muffin_babel-1.3.6.tar`

### file list

```diff
@@ -1,5 +1,5 @@
--rw-r--r--   0        0        0     4396 2023-04-06 16:36:52.600600 muffin_babel-1.3.5/README.rst
--rw-r--r--   0        0        0     9100 2023-04-06 16:36:52.600600 muffin_babel-1.3.5/muffin_babel/__init__.py
--rw-r--r--   0        0        0        0 2023-04-06 16:36:52.600600 muffin_babel-1.3.5/muffin_babel/py.typed
--rw-r--r--   0        0        0     2030 2023-04-06 16:36:52.600600 muffin_babel-1.3.5/pyproject.toml
--rw-r--r--   0        0        0     5691 1970-01-01 00:00:00.000000 muffin_babel-1.3.5/PKG-INFO
+-rw-r--r--   0        0        0     4396 2023-04-06 16:47:52.482546 muffin_babel-1.3.6/README.rst
+-rw-r--r--   0        0        0     9094 2023-04-06 16:47:52.482546 muffin_babel-1.3.6/muffin_babel/__init__.py
+-rw-r--r--   0        0        0        0 2023-04-06 16:47:52.482546 muffin_babel-1.3.6/muffin_babel/py.typed
+-rw-r--r--   0        0        0     2030 2023-04-06 16:47:52.482546 muffin_babel-1.3.6/pyproject.toml
+-rw-r--r--   0        0        0     5691 1970-01-01 00:00:00.000000 muffin_babel-1.3.6/PKG-INFO
```

### Comparing `muffin_babel-1.3.5/README.rst` & `muffin_babel-1.3.6/README.rst`

 * *Files identical despite different names*

### Comparing `muffin_babel-1.3.5/muffin_babel/__init__.py` & `muffin_babel-1.3.6/muffin_babel/__init__.py`

 * *Files 1% similar despite different names*

```diff
@@ -121,15 +121,15 @@
                 source = Path(locales_dir)
                 for locale in source.iterdir():
                     po_file = locale / "LC_MESSAGES" / f"{domain}.po"
                     if not po_file.exists():
                         continue
 
                     with po_file.open("rb") as po:
-                        catalog = read_po(po, locale.as_posix())
+                        catalog = read_po(po, locale.name)
 
                     mo_file = po_file.with_suffix(".mo")
 
                     with mo_file.open("wb") as mo:
                         logger.info("writing MO template file to %s", mo_file)
                         write_mo(mo, catalog, use_fuzzy=use_fuzzy)
```

### Comparing `muffin_babel-1.3.5/pyproject.toml` & `muffin_babel-1.3.6/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "muffin-babel"
-version = "1.3.5"
+version = "1.3.6"
 description = "Localization support for the Muffin Framework"
 readme = "README.rst"
 license = "MIT"
 authors = ["Kirill Klenov <horneds@gmail.com>"]
 keywords = ["localization", "internationalization", "muffin", "babel", "asyncio", "trio", "asgi"]
 classifiers = [
   "Development Status :: 5 - Production/Stable",
```

### Comparing `muffin_babel-1.3.5/PKG-INFO` & `muffin_babel-1.3.6/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: muffin-babel
-Version: 1.3.5
+Version: 1.3.6
 Summary: Localization support for the Muffin Framework
 Home-page: https://github.com/klen/muffin-babel
 License: MIT
 Keywords: localization,internationalization,muffin,babel,asyncio,trio,asgi
 Author: Kirill Klenov
 Author-email: horneds@gmail.com
 Requires-Python: >=3.8,<4.0
```

