# Comparing `tmp/mkdocstrings-0.9.0.tar.gz` & `tmp/mkdocstrings-0.9.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "mkdocstrings-0.9.0.tar", last modified: Sat Mar 21 14:45:13 2020, max compression
+gzip compressed data, was "mkdocstrings-0.9.1.tar", last modified: Sat Mar 21 15:31:58 2020, max compression
```

## Comparing `mkdocstrings-0.9.0.tar` & `mkdocstrings-0.9.1.tar`

### file list

```diff
@@ -1,24 +1,24 @@
--rw-r--r--   0        0        0      754 2019-12-22 22:15:56.802859 mkdocstrings-0.9.0/LICENSE
--rw-r--r--   0        0        0     7018 2020-03-21 14:42:21.956404 mkdocstrings-0.9.0/README.md
--rw-r--r--   0        0        0     7018 2020-03-21 14:42:21.956404 mkdocstrings-0.9.0/README.md
--rw-r--r--   0        0        0     1811 2020-03-21 14:42:21.976404 mkdocstrings-0.9.0/pyproject.toml
--rw-r--r--   0        0        0     1811 2020-03-21 14:42:21.976404 mkdocstrings-0.9.0/pyproject.toml
--rw-r--r--   0        0        0      747 2020-03-21 14:42:21.976404 mkdocstrings-0.9.0/src/mkdocstrings/__init__.py
--rw-r--r--   0        0        0     8916 2020-03-21 14:42:21.976404 mkdocstrings-0.9.0/src/mkdocstrings/extension.py
--rw-r--r--   0        0        0     8219 2020-03-21 14:42:21.976404 mkdocstrings-0.9.0/src/mkdocstrings/handlers/__init__.py
--rw-r--r--   0        0        0    10421 2020-03-21 14:42:21.976404 mkdocstrings-0.9.0/src/mkdocstrings/handlers/python.py
--rw-r--r--   0        0        0    15278 2020-03-21 14:42:21.976404 mkdocstrings-0.9.0/src/mkdocstrings/plugin.py
--rw-r--r--   0        0        0     1510 2020-03-21 14:42:21.976404 mkdocstrings-0.9.0/src/mkdocstrings/templates/python/material/attribute.html
--rw-r--r--   0        0        0     3243 2020-03-21 14:42:21.999737 mkdocstrings-0.9.0/src/mkdocstrings/templates/python/material/children.html
--rw-r--r--   0        0        0     1806 2020-03-21 14:42:21.999737 mkdocstrings-0.9.0/src/mkdocstrings/templates/python/material/class.html
--rw-r--r--   0        0        0      658 2020-03-21 14:42:22.003071 mkdocstrings-0.9.0/src/mkdocstrings/templates/python/material/docstring.html
--rw-r--r--   0        0        0      358 2020-03-21 14:42:22.019737 mkdocstrings-0.9.0/src/mkdocstrings/templates/python/material/exceptions.html
--rw-r--r--   0        0        0     1934 2020-03-21 14:42:22.019737 mkdocstrings-0.9.0/src/mkdocstrings/templates/python/material/function.html
--rw-r--r--   0        0        0     1902 2020-03-21 14:42:22.019737 mkdocstrings-0.9.0/src/mkdocstrings/templates/python/material/method.html
--rw-r--r--   0        0        0     1510 2020-03-21 14:42:22.033071 mkdocstrings-0.9.0/src/mkdocstrings/templates/python/material/module.html
--rw-r--r--   0        0        0      570 2020-03-21 14:42:22.046404 mkdocstrings-0.9.0/src/mkdocstrings/templates/python/material/parameters.html
--rw-r--r--   0        0        0      234 2020-03-21 14:42:22.046404 mkdocstrings-0.9.0/src/mkdocstrings/templates/python/material/properties.html
--rw-r--r--   0        0        0      286 2020-03-21 14:42:22.046404 mkdocstrings-0.9.0/src/mkdocstrings/templates/python/material/return.html
--rw-r--r--   0        0        0      902 2020-03-21 14:42:22.046404 mkdocstrings-0.9.0/src/mkdocstrings/templates/python/material/signature.html
--rw-r--r--   0        0        0     8194 2020-03-21 14:45:13.393296 mkdocstrings-0.9.0/setup.py
--rw-r--r--   0        0        0     7812 2020-03-21 14:45:13.393701 mkdocstrings-0.9.0/PKG-INFO
+-rw-r--r--   0        0        0      754 2019-12-22 22:15:56.802859 mkdocstrings-0.9.1/LICENSE
+-rw-r--r--   0        0        0     7018 2020-03-21 14:42:21.956404 mkdocstrings-0.9.1/README.md
+-rw-r--r--   0        0        0     7018 2020-03-21 14:42:21.956404 mkdocstrings-0.9.1/README.md
+-rw-r--r--   0        0        0     1811 2020-03-21 15:30:30.066487 mkdocstrings-0.9.1/pyproject.toml
+-rw-r--r--   0        0        0     1811 2020-03-21 15:30:30.066487 mkdocstrings-0.9.1/pyproject.toml
+-rw-r--r--   0        0        0      747 2020-03-21 14:42:21.976404 mkdocstrings-0.9.1/src/mkdocstrings/__init__.py
+-rw-r--r--   0        0        0     8916 2020-03-21 14:42:21.976404 mkdocstrings-0.9.1/src/mkdocstrings/extension.py
+-rw-r--r--   0        0        0     8219 2020-03-21 14:42:21.976404 mkdocstrings-0.9.1/src/mkdocstrings/handlers/__init__.py
+-rw-r--r--   0        0        0    10421 2020-03-21 14:42:21.976404 mkdocstrings-0.9.1/src/mkdocstrings/handlers/python.py
+-rw-r--r--   0        0        0    15284 2020-03-21 15:28:24.299817 mkdocstrings-0.9.1/src/mkdocstrings/plugin.py
+-rw-r--r--   0        0        0     1510 2020-03-21 14:42:21.976404 mkdocstrings-0.9.1/src/mkdocstrings/templates/python/material/attribute.html
+-rw-r--r--   0        0        0     3243 2020-03-21 14:42:21.999737 mkdocstrings-0.9.1/src/mkdocstrings/templates/python/material/children.html
+-rw-r--r--   0        0        0     1806 2020-03-21 14:42:21.999737 mkdocstrings-0.9.1/src/mkdocstrings/templates/python/material/class.html
+-rw-r--r--   0        0        0      658 2020-03-21 14:42:22.003071 mkdocstrings-0.9.1/src/mkdocstrings/templates/python/material/docstring.html
+-rw-r--r--   0        0        0      358 2020-03-21 14:42:22.019737 mkdocstrings-0.9.1/src/mkdocstrings/templates/python/material/exceptions.html
+-rw-r--r--   0        0        0     1934 2020-03-21 14:42:22.019737 mkdocstrings-0.9.1/src/mkdocstrings/templates/python/material/function.html
+-rw-r--r--   0        0        0     1902 2020-03-21 14:42:22.019737 mkdocstrings-0.9.1/src/mkdocstrings/templates/python/material/method.html
+-rw-r--r--   0        0        0     1510 2020-03-21 14:42:22.033071 mkdocstrings-0.9.1/src/mkdocstrings/templates/python/material/module.html
+-rw-r--r--   0        0        0      570 2020-03-21 14:42:22.046404 mkdocstrings-0.9.1/src/mkdocstrings/templates/python/material/parameters.html
+-rw-r--r--   0        0        0      234 2020-03-21 14:42:22.046404 mkdocstrings-0.9.1/src/mkdocstrings/templates/python/material/properties.html
+-rw-r--r--   0        0        0      286 2020-03-21 14:42:22.046404 mkdocstrings-0.9.1/src/mkdocstrings/templates/python/material/return.html
+-rw-r--r--   0        0        0      902 2020-03-21 14:42:22.046404 mkdocstrings-0.9.1/src/mkdocstrings/templates/python/material/signature.html
+-rw-r--r--   0        0        0     8194 2020-03-21 15:31:58.954873 mkdocstrings-0.9.1/setup.py
+-rw-r--r--   0        0        0     7812 2020-03-21 15:31:58.955283 mkdocstrings-0.9.1/PKG-INFO
```

### Comparing `mkdocstrings-0.9.0/LICENSE` & `mkdocstrings-0.9.1/LICENSE`

 * *Files identical despite different names*

### Comparing `mkdocstrings-0.9.0/README.md` & `mkdocstrings-0.9.1/README.md`

 * *Files identical despite different names*

### Comparing `mkdocstrings-0.9.0/pyproject.toml` & `mkdocstrings-0.9.1/pyproject.toml`

 * *Files 0% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 [build-system]
 requires = ["poetry>=0.12"]
 build-backend = "poetry.masonry.api"
 
 [tool.poetry]
 name = "mkdocstrings"
-version = "0.9.0"
+version = "0.9.1"
 description = "Automatic documentation from sources, for mkdocs."
 authors = ["Timothée Mazzucotelli <pawamoy@pm.me>"]
 license = "ISC License"
 readme = "README.md"
 repository = "https://github.com/pawamoy/mkdocstrings"
 homepage = "https://github.com/pawamoy/mkdocstrings"
 keywords = ["mkdocs", "mkdocs-plugin", "docstrings", "autodoc", "documentation"]
```

### Comparing `mkdocstrings-0.9.0/src/mkdocstrings/__init__.py` & `mkdocstrings-0.9.1/src/mkdocstrings/__init__.py`

 * *Files identical despite different names*

### Comparing `mkdocstrings-0.9.0/src/mkdocstrings/extension.py` & `mkdocstrings-0.9.1/src/mkdocstrings/extension.py`

 * *Files identical despite different names*

### Comparing `mkdocstrings-0.9.0/src/mkdocstrings/handlers/__init__.py` & `mkdocstrings-0.9.1/src/mkdocstrings/handlers/__init__.py`

 * *Files identical despite different names*

### Comparing `mkdocstrings-0.9.0/src/mkdocstrings/handlers/python.py` & `mkdocstrings-0.9.1/src/mkdocstrings/handlers/python.py`

 * *Files identical despite different names*

### Comparing `mkdocstrings-0.9.0/src/mkdocstrings/plugin.py` & `mkdocstrings-0.9.1/src/mkdocstrings/plugin.py`

 * *Files 0% similar despite different names*

```diff
@@ -153,15 +153,15 @@
 
         In this hook, we map the IDs of every anchor found in the table of contents to the anchors absolute URLs.
         This mapping will be used later to fix unresolved reference of the form `[title][identifier]` or
         `[identifier][]`.
         """
         log.debug(f"mkdocstrings.plugin: Mapping identifiers to URLs for page {page.file.src_path}")
         for item in page.toc.items:
-            self.map_urls(page.abs_url, item)
+            self.map_urls(page.canonical_url, item)
         return html
 
     def map_urls(self, base_url: str, anchor: AnchorLink) -> None:
         """
         Recurse on every anchor to map its ID to its absolute URL.
 
         This method populates `self.url_map` by side-effect.
```

### Comparing `mkdocstrings-0.9.0/src/mkdocstrings/templates/python/material/attribute.html` & `mkdocstrings-0.9.1/src/mkdocstrings/templates/python/material/attribute.html`

 * *Files identical despite different names*

### Comparing `mkdocstrings-0.9.0/src/mkdocstrings/templates/python/material/children.html` & `mkdocstrings-0.9.1/src/mkdocstrings/templates/python/material/children.html`

 * *Files identical despite different names*

### Comparing `mkdocstrings-0.9.0/src/mkdocstrings/templates/python/material/class.html` & `mkdocstrings-0.9.1/src/mkdocstrings/templates/python/material/class.html`

 * *Files identical despite different names*

### Comparing `mkdocstrings-0.9.0/src/mkdocstrings/templates/python/material/docstring.html` & `mkdocstrings-0.9.1/src/mkdocstrings/templates/python/material/docstring.html`

 * *Files identical despite different names*

### Comparing `mkdocstrings-0.9.0/src/mkdocstrings/templates/python/material/function.html` & `mkdocstrings-0.9.1/src/mkdocstrings/templates/python/material/function.html`

 * *Files identical despite different names*

### Comparing `mkdocstrings-0.9.0/src/mkdocstrings/templates/python/material/method.html` & `mkdocstrings-0.9.1/src/mkdocstrings/templates/python/material/method.html`

 * *Files identical despite different names*

### Comparing `mkdocstrings-0.9.0/src/mkdocstrings/templates/python/material/module.html` & `mkdocstrings-0.9.1/src/mkdocstrings/templates/python/material/module.html`

 * *Files identical despite different names*

### Comparing `mkdocstrings-0.9.0/src/mkdocstrings/templates/python/material/parameters.html` & `mkdocstrings-0.9.1/src/mkdocstrings/templates/python/material/parameters.html`

 * *Files identical despite different names*

### Comparing `mkdocstrings-0.9.0/src/mkdocstrings/templates/python/material/signature.html` & `mkdocstrings-0.9.1/src/mkdocstrings/templates/python/material/signature.html`

 * *Files identical despite different names*

### Comparing `mkdocstrings-0.9.0/setup.py` & `mkdocstrings-0.9.1/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -14,15 +14,15 @@
 ['beautifulsoup4>=4.8.2,<5.0.0', 'mkdocs>=1.1,<2.0', 'pytkdocs>=0.1.1,<0.2.0']
 
 entry_points = \
 {'mkdocs.plugins': ['mkdocstrings = mkdocstrings.plugin:MkdocstringsPlugin']}
 
 setup_kwargs = {
     'name': 'mkdocstrings',
-    'version': '0.9.0',
+    'version': '0.9.1',
     'description': 'Automatic documentation from sources, for mkdocs.',
     'long_description': '# mkdocstrings\n[![pipeline status](https://gitlab.com/pawamoy/mkdocstrings/badges/master/pipeline.svg)](https://gitlab.com/pawamoy/mkdocstrings/pipelines)\n[![coverage report](https://gitlab.com/pawamoy/mkdocstrings/badges/master/coverage.svg)](https://gitlab.com/pawamoy/mkdocstrings/commits/master)\n[![documentation](https://img.shields.io/badge/docs-latest-green.svg?style=flat)](https://pawamoy.github.io/mkdocstrings)\n[![pypi version](https://img.shields.io/pypi/v/mkdocstrings.svg)](https://pypi.org/project/mkdocstrings/)\n\nAutomatic documentation from sources, for mkdocs.\n\n---\n\n![mkdocstrings_gif1](https://user-images.githubusercontent.com/3999221/77157604-fb807480-6aa1-11ea-99e0-d092371d4de0.gif)\n\n---\n\n- [Features](#features)\n    - [Python handler features](#python-handler-features)\n- [Requirements](#requirements)\n- [Installation](#installation)\n- [Usage](#usage)\n\n## Features\n\n- **Language agnostic:** just like `mkdocs`, `mkdocstrings` is written in Python but is language-agnostic. It means\n  you can use for any language, as long as you implement a [`handler`][mkdocstrings.handlers] for it. Currently, we\n  only have a [Python handler][mkdocstrings.handlers.python]. Maybe you\'d like to contribute another one :wink:?\n- **Multiple themes support:** each handler can offer multiple themes. Currently, we only offer the\n  :star: [Material theme](https://squidfunk.github.io/mkdocs-material/) :star: for the Python handler.\n- **Cross-references to other objects:** `mkdocstrings` makes it possible to reference other headings from your\n  Markdown files with the classic Markdown syntax: `[identifier][]` or `[title][identifier]`. This feature is language\n  agnostic as well: you can cross-reference any heading that appear in your Markdown pages.\n  If the handler for a particular language renders headings for documented objects, you\'ll be able to reference them!\n- **Inline injection in Markdown:** instead of generating Markdown files, `mkdocstrings` allows you to inject\n  documentation anywhere in your Markdown contents. The syntax is simple: `::: identifier` followed by a 4-spaces\n  indented YAML block. The identifier and YAML configuration will be passed to the appropriate handler\n  to collect and render documentation.\n- **Global and local configuration:** each handler can be configured globally in `mkdocs.yml`, and locally for each\n  "autodoc" instruction.\n- **Watch source code directories:** you can tell `mkdocstrings` to add directories to be watched by `mkdocs` when\n  serving the documentation, for auto-reload.\n- **Sane defaults:** you should be able to just drop the plugin in your configuration and enjoy your auto-generated docs.\n  \n### Python handler features\n\n- **Data collection from source code**: collection of the object-tree and the docstrings is done by\n  [`pytkdocs`](https://github.com/pawamoy/pytkdocs). The following features are possible thanks to it:\n    - **Support for type annotations:** `pytkdocs` collects your type annotations and `mkdocstrings` uses them\n      to display parameters types or return types. \n    - **Recursive documentation of Python objects:** just use the module dotted-path as identifier, and you get the full\n      module docs. You don\'t need to inject documentation for each class, function, etc.\n    - **Support for documented attribute:** attributes (variables) followed by a docstring (triple-quoted string) will\n      be recognized by `pytkdocs` in modules, classes and even in `__init__` methods.\n    - **Support for objects properties:** `pytkdocs` detects if a method is a `staticmethod`, a `classmethod`, etc.,\n      it also detects if a property is read-only or writable, and more! These properties will be displayed\n      next to the object signature by `mkdocstrings`.\n    - **Google-style sections support in docstrings:** `pytkdocs` understands `Arguments:`, `Raises:`\n      and `Returns:` sections, and returns structured data for `mkdocstrings` to render them.\n    - **Admonition support in docstrings:** blocks like `Note: ` or `Warning: ` will be transformed\n      to their [admonition](https://squidfunk.github.io/mkdocs-material/extensions/admonition/) equivalent.\n      *We do not support nested admonitions in docstrings!*\n- **Every object has a TOC entry:** we render a heading for each object, meaning `mkdocs` picks them into the Table\n  of Contents, which is nicely display by the Material theme. Thanks to `mkdocstrings` cross-reference ability,\n  you can even reference other objects within your docstrings, with the classic Markdown syntax:\n  `[this object][package.module.object]` or directly with `[package.module.object][]`\n- **Source code display:** `mkdocstrings` can add a collapsible div containing the highlighted source code\n  of the Python object.\n  \nTo get an example of what is possible, check `mkdocstrings`\'\nown [documentation](https://pawamoy.github.io/mkdocstrings), auto-generated from sources by itself of course,\nand the following GIF:\n\n![mkdocstrings_gif2](https://user-images.githubusercontent.com/3999221/77157838-7184db80-6aa2-11ea-9f9a-fe77405202de.gif)\n\n## Roadmap\n- [x] **January-March 2020:** Big refactor.\n- [ ] **March-April 2020:** Write. Tests. Because. It\'s important.\n  Gather feedback about Python handler configuration options.\n  Work the backlog.\n\n## Requirements\n`mkdocstrings` requires Python 3.6 or above.\n\n<details>\n<summary>To install Python 3.6, I recommend using <a href="https://github.com/pyenv/pyenv"><code>pyenv</code></a>.</summary>\n\n```bash\n# install pyenv\ngit clone https://github.com/pyenv/pyenv ~/.pyenv\n\n# setup pyenv (you should also put these three lines in .bashrc or similar)\nexport PATH="${HOME}/.pyenv/bin:${PATH}"\nexport PYENV_ROOT="${HOME}/.pyenv"\neval "$(pyenv init -)"\n\n# install Python 3.6\npyenv install 3.6.8\n\n# make it available globally\npyenv global system 3.6.8\n```\n</details>\n\n## Installation\nWith `pip`:\n```bash\npython3.6 -m pip install mkdocstrings\n```\n\n## Usage\n\n```yaml\n# mkdocs.yml\ntheme:\n  name: "material"\n\nplugins:\n  - search\n  - mkdocstrings:\n      default_handler: python\n      handlers:\n        python:\n          rendering:\n            show_source: true\n      watch:\n        - src/my_library\n```\n\nIn one of your markdown files:\n\n```yaml\n# Reference\n\n::: my_library.my_module.my_class\n    rendering:\n      show_source: false\n\n\n::: org.jpackage.BestOfTheBestFactoryInterface\n    handler: java  # we don\'t have a java handler yet, it\'s just an example\n```\n\nIn documentation strings (written in Markdown), you can reference objects from other places:\n\n```python\ndef some_function():\n    """\n    This is my function.\n\n    It references [another function][package.submodule.function].\n    It also references another object directly: [package.submodule.SuperClass][].\n    """\n    pass\n```\n\nAdd some style in `docs/custom.css`:\n\n```css\ndiv.doc-contents:not(.first) {\n  padding-left: 25px;\n  border-left: 4px solid rgba(230, 230, 230);\n  margin-bottom: 80px;\n}\n```\n\nAnd add it to your `mkdocs.yml`:\n\n```yaml\nextra_css:\n  - custom.css\n```\n',
     'author': 'Timothée Mazzucotelli',
     'author_email': 'pawamoy@pm.me',
     'maintainer': None,
     'maintainer_email': None,
     'url': 'https://github.com/pawamoy/mkdocstrings',
```

### Comparing `mkdocstrings-0.9.0/PKG-INFO` & `mkdocstrings-0.9.1/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: mkdocstrings
-Version: 0.9.0
+Version: 0.9.1
 Summary: Automatic documentation from sources, for mkdocs.
 Home-page: https://github.com/pawamoy/mkdocstrings
 License: ISC
 Keywords: mkdocs,mkdocs-plugin,docstrings,autodoc,documentation
 Author: Timothée Mazzucotelli
 Author-email: pawamoy@pm.me
 Requires-Python: >=3.6,<4.0
```

