# Comparing `tmp/calcipy-1.0.1.tar.gz` & `tmp/calcipy-1.1.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "calcipy-1.0.1.tar", max compression
+gzip compressed data, was "calcipy-1.1.1.tar", max compression
```

## Comparing `calcipy-1.0.1.tar` & `calcipy-1.1.1.tar`

### file list

```diff
@@ -1,33 +1,35 @@
--rw-r--r--   0        0        0     1066 2023-03-02 02:44:04.169254 calcipy-1.0.1/LICENSE
--rw-r--r--   0        0        0      167 2023-03-02 02:48:00.736355 calcipy-1.0.1/calcipy/__init__.py
--rw-r--r--   0        0        0     1259 2023-02-23 02:19:12.612069 calcipy-1.0.1/calcipy/can_skip.py
--rw-r--r--   0        0        0      175 2023-03-02 02:58:57.029784 calcipy-1.0.1/calcipy/check_for_stale_packages/__init__.py
--rw-r--r--   0        0        0     8214 2023-03-02 02:41:41.090176 calcipy-1.0.1/calcipy/check_for_stale_packages/_check_for_stale_packages.py
--rw-r--r--   0        0        0     5627 2023-02-25 23:57:25.000240 calcipy-1.0.1/calcipy/cli.py
--rw-r--r--   0        0        0      154 2023-03-02 02:58:57.946199 calcipy-1.0.1/calcipy/code_tag_collector/__init__.py
--rw-r--r--   0        0        0     9790 2023-02-26 00:17:08.509359 calcipy-1.0.1/calcipy/code_tag_collector/_collector.py
--rw-r--r--   0        0        0      140 2023-03-02 02:58:58.498973 calcipy-1.0.1/calcipy/dot_dict/__init__.py
--rw-r--r--   0        0        0      803 2023-02-25 23:58:05.004832 calcipy-1.0.1/calcipy/dot_dict/_dot_dict.py
--rw-r--r--   0        0        0     3271 2023-02-23 02:19:12.613926 calcipy-1.0.1/calcipy/file_search.py
--rw-r--r--   0        0        0     1814 2023-02-26 00:16:53.446873 calcipy-1.0.1/calcipy/invoke_helpers.py
--rw-r--r--   0        0        0      162 2023-03-02 02:58:58.973806 calcipy-1.0.1/calcipy/md_writer/__init__.py
--rw-r--r--   0        0        0     7815 2023-02-23 02:19:12.614596 calcipy-1.0.1/calcipy/md_writer/_writer.py
--rw-r--r--   0        0        0      162 2023-03-02 02:58:59.584964 calcipy-1.0.1/calcipy/noxfile/__init__.py
--rw-r--r--   0        0        0     6513 2023-02-23 13:23:19.364723 calcipy-1.0.1/calcipy/noxfile/_noxfile.py
--rw-r--r--   0        0        0     1193 2023-03-02 02:45:23.652620 calcipy-1.0.1/calcipy/scripts.py
--rw-r--r--   0        0        0        0 2023-02-21 03:18:10.928974 calcipy-1.0.1/calcipy/tasks/__init__.py
--rw-r--r--   0        0        0     3104 2023-02-25 23:52:16.858873 calcipy-1.0.1/calcipy/tasks/all_tasks.py
--rw-r--r--   0        0        0     1877 2023-02-25 23:55:28.029589 calcipy-1.0.1/calcipy/tasks/cl.py
--rw-r--r--   0        0        0     1132 2023-02-23 02:54:45.453854 calcipy-1.0.1/calcipy/tasks/defaults.py
--rw-r--r--   0        0        0     3434 2023-03-02 02:52:33.121247 calcipy-1.0.1/calcipy/tasks/doc.py
--rw-r--r--   0        0        0     3861 2023-02-26 00:22:17.320612 calcipy-1.0.1/calcipy/tasks/lint.py
--rw-r--r--   0        0        0      454 2023-02-23 02:19:12.617085 calcipy-1.0.1/calcipy/tasks/nox.py
--rw-r--r--   0        0        0     1275 2023-02-23 02:19:12.617365 calcipy-1.0.1/calcipy/tasks/pack.py
--rw-r--r--   0        0        0      557 2023-02-23 02:19:12.617596 calcipy-1.0.1/calcipy/tasks/stale.py
--rw-r--r--   0        0        0     1498 2023-02-23 02:19:12.617900 calcipy-1.0.1/calcipy/tasks/tags.py
--rw-r--r--   0        0        0     3182 2023-02-23 02:19:12.618169 calcipy-1.0.1/calcipy/tasks/test.py
--rw-r--r--   0        0        0      634 2023-02-23 02:19:12.618406 calcipy-1.0.1/calcipy/tasks/types.py
--rw-r--r--   0        0        0     6651 2023-03-02 03:08:30.087637 calcipy-1.0.1/docs/README.md
--rw-r--r--   0        0        0     6629 2023-03-02 02:48:00.775730 calcipy-1.0.1/pyproject.toml
--rw-r--r--   0        0        0    10046 1970-01-01 00:00:00.000000 calcipy-1.0.1/setup.py
--rw-r--r--   0        0        0    11501 1970-01-01 00:00:00.000000 calcipy-1.0.1/PKG-INFO
+-rw-r--r--   0        0        0     1066 2023-04-06 13:01:00.709942 calcipy-1.1.1/LICENSE
+-rw-r--r--   0        0        0      167 2023-04-06 14:09:09.042588 calcipy-1.1.1/calcipy/__init__.py
+-rw-r--r--   0        0        0     1259 2023-02-23 02:19:12.612069 calcipy-1.1.1/calcipy/can_skip.py
+-rw-r--r--   0        0        0      175 2023-03-02 02:58:57.029784 calcipy-1.1.1/calcipy/check_for_stale_packages/__init__.py
+-rw-r--r--   0        0        0     8214 2023-03-02 02:41:41.090176 calcipy-1.1.1/calcipy/check_for_stale_packages/_check_for_stale_packages.py
+-rw-r--r--   0        0        0     5641 2023-04-01 13:12:52.506798 calcipy-1.1.1/calcipy/cli.py
+-rw-r--r--   0        0        0      154 2023-03-02 02:58:57.946199 calcipy-1.1.1/calcipy/code_tag_collector/__init__.py
+-rw-r--r--   0        0        0     9790 2023-02-26 00:17:08.509359 calcipy-1.1.1/calcipy/code_tag_collector/_collector.py
+-rw-r--r--   0        0        0      140 2023-03-02 02:58:58.498973 calcipy-1.1.1/calcipy/dot_dict/__init__.py
+-rw-r--r--   0        0        0      803 2023-02-25 23:58:05.004832 calcipy-1.1.1/calcipy/dot_dict/_dot_dict.py
+-rw-r--r--   0        0        0        0 2023-04-05 02:28:27.975837 calcipy-1.1.1/calcipy/experiments/__init__.py
+-rw-r--r--   0        0        0     1861 2023-04-06 13:10:19.822580 calcipy-1.1.1/calcipy/experiments/check_duplicate_test_names.py
+-rw-r--r--   0        0        0     3271 2023-02-23 02:19:12.613926 calcipy-1.1.1/calcipy/file_search.py
+-rw-r--r--   0        0        0     1814 2023-02-26 00:16:53.446873 calcipy-1.1.1/calcipy/invoke_helpers.py
+-rw-r--r--   0        0        0      162 2023-03-02 02:58:58.973806 calcipy-1.1.1/calcipy/md_writer/__init__.py
+-rw-r--r--   0        0        0     7815 2023-02-23 02:19:12.614596 calcipy-1.1.1/calcipy/md_writer/_writer.py
+-rw-r--r--   0        0        0      162 2023-03-02 02:58:59.584964 calcipy-1.1.1/calcipy/noxfile/__init__.py
+-rw-r--r--   0        0        0     6513 2023-02-23 13:23:19.364723 calcipy-1.1.1/calcipy/noxfile/_noxfile.py
+-rw-r--r--   0        0        0     1193 2023-03-02 02:45:23.652620 calcipy-1.1.1/calcipy/scripts.py
+-rw-r--r--   0        0        0        0 2023-02-21 03:18:10.928974 calcipy-1.1.1/calcipy/tasks/__init__.py
+-rw-r--r--   0        0        0     3104 2023-04-05 22:06:13.047283 calcipy-1.1.1/calcipy/tasks/all_tasks.py
+-rw-r--r--   0        0        0     1876 2023-04-06 12:55:27.782578 calcipy-1.1.1/calcipy/tasks/cl.py
+-rw-r--r--   0        0        0     1132 2023-02-23 02:54:45.453854 calcipy-1.1.1/calcipy/tasks/defaults.py
+-rw-r--r--   0        0        0     3589 2023-04-06 12:54:31.902116 calcipy-1.1.1/calcipy/tasks/doc.py
+-rw-r--r--   0        0        0     3861 2023-02-26 00:22:17.320612 calcipy-1.1.1/calcipy/tasks/lint.py
+-rw-r--r--   0        0        0      454 2023-02-23 02:19:12.617085 calcipy-1.1.1/calcipy/tasks/nox.py
+-rw-r--r--   0        0        0     1275 2023-02-23 02:19:12.617365 calcipy-1.1.1/calcipy/tasks/pack.py
+-rw-r--r--   0        0        0      557 2023-02-23 02:19:12.617596 calcipy-1.1.1/calcipy/tasks/stale.py
+-rw-r--r--   0        0        0     1498 2023-02-23 02:19:12.617900 calcipy-1.1.1/calcipy/tasks/tags.py
+-rw-r--r--   0        0        0     3182 2023-02-23 02:19:12.618169 calcipy-1.1.1/calcipy/tasks/test.py
+-rw-r--r--   0        0        0      634 2023-02-23 02:19:12.618406 calcipy-1.1.1/calcipy/tasks/types.py
+-rw-r--r--   0        0        0     6651 2023-04-06 14:09:18.297359 calcipy-1.1.1/docs/README.md
+-rw-r--r--   0        0        0     6455 2023-04-06 14:09:09.080237 calcipy-1.1.1/pyproject.toml
+-rw-r--r--   0        0        0     9950 1970-01-01 00:00:00.000000 calcipy-1.1.1/setup.py
+-rw-r--r--   0        0        0    11358 1970-01-01 00:00:00.000000 calcipy-1.1.1/PKG-INFO
```

### Comparing `calcipy-1.0.1/LICENSE` & `calcipy-1.1.1/LICENSE`

 * *Files identical despite different names*

### Comparing `calcipy-1.0.1/calcipy/can_skip.py` & `calcipy-1.1.1/calcipy/can_skip.py`

 * *Files identical despite different names*

### Comparing `calcipy-1.0.1/calcipy/check_for_stale_packages/_check_for_stale_packages.py` & `calcipy-1.1.1/calcipy/check_for_stale_packages/_check_for_stale_packages.py`

 * *Files identical despite different names*

### Comparing `calcipy-1.0.1/calcipy/cli.py` & `calcipy-1.1.1/calcipy/cli.py`

 * *Files 4% similar despite different names*

```diff
@@ -148,15 +148,15 @@
         """Wraps the decorated task."""
         @invoke_task(*task_args, **task_kwargs)  # type: ignore[misc]
         @beartype
         @wraps(func)
         def inner(ctx: Context, *args: Any, **kwargs: Any) -> Task:
             """Wrap the task with settings configured in `gto` for working_dir and logging."""
             try:
-                ctx.config.gto
+                ctx.config.gto  # noqa: B018
             except AttributeError:
                 ctx.config.gto = GlobalTaskOptions()
 
             os.chdir(ctx.config.gto.working_dir)
             _configure_logger(ctx)
 
             return _run_task(func, ctx, *args, show_task_info=show_task_info, **kwargs)
```

### Comparing `calcipy-1.0.1/calcipy/code_tag_collector/_collector.py` & `calcipy-1.1.1/calcipy/code_tag_collector/_collector.py`

 * *Files identical despite different names*

### Comparing `calcipy-1.0.1/calcipy/dot_dict/_dot_dict.py` & `calcipy-1.1.1/calcipy/dot_dict/_dot_dict.py`

 * *Files identical despite different names*

### Comparing `calcipy-1.0.1/calcipy/file_search.py` & `calcipy-1.1.1/calcipy/file_search.py`

 * *Files identical despite different names*

### Comparing `calcipy-1.0.1/calcipy/invoke_helpers.py` & `calcipy-1.1.1/calcipy/invoke_helpers.py`

 * *Files identical despite different names*

### Comparing `calcipy-1.0.1/calcipy/md_writer/_writer.py` & `calcipy-1.1.1/calcipy/md_writer/_writer.py`

 * *Files identical despite different names*

### Comparing `calcipy-1.0.1/calcipy/noxfile/_noxfile.py` & `calcipy-1.1.1/calcipy/noxfile/_noxfile.py`

 * *Files identical despite different names*

### Comparing `calcipy-1.0.1/calcipy/scripts.py` & `calcipy-1.1.1/calcipy/scripts.py`

 * *Files identical despite different names*

### Comparing `calcipy-1.0.1/calcipy/tasks/all_tasks.py` & `calcipy-1.1.1/calcipy/tasks/all_tasks.py`

 * *Files identical despite different names*

### Comparing `calcipy-1.0.1/calcipy/tasks/cl.py` & `calcipy-1.1.1/calcipy/tasks/cl.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,9 @@
 """Changelog CLI."""
 
-
 from beartype import beartype
 from beartype.typing import Literal, Optional
 from invoke import Context
 
 from ..cli import task
 from ..invoke_helpers import get_doc_subdir, get_project_path, run
```

### Comparing `calcipy-1.0.1/calcipy/tasks/defaults.py` & `calcipy-1.1.1/calcipy/tasks/defaults.py`

 * *Files identical despite different names*

### Comparing `calcipy-1.0.1/calcipy/tasks/doc.py` & `calcipy-1.1.1/calcipy/tasks/doc.py`

 * *Files 8% similar despite different names*

```diff
@@ -1,23 +1,25 @@
 """Document CLI."""
 
 import webbrowser
+from contextlib import suppress
 from pathlib import Path
 
 from beartype import beartype
 from corallium.file_helpers import (
     MKDOCS_CONFIG,
     delete_dir,
     ensure_dir,
     open_in_browser,
     read_package_name,
     read_yaml_file,
     trim_trailing_whitespace,
 )
 from invoke import Context
+from invoke.exceptions import UnexpectedExit
 
 from ..cli import task
 from ..invoke_helpers import get_doc_subdir, get_project_path, run
 from ..md_writer import write_autoformatted_md_sections
 
 
 @beartype
@@ -106,10 +108,12 @@
 
 @task()
 def deploy(ctx: Context) -> None:
     """Deploy docs to the Github `gh-pages` branch."""
     if _is_mkdocs_local():  # pragma: no cover
         raise NotImplementedError('Not yet configured to deploy documentation without "use_directory_urls"')
 
-    run(ctx, 'pre-commit uninstall')  # To prevent pre-commit failures when mkdocs calls push
+    with suppress(UnexpectedExit):
+        run(ctx, 'pre-commit uninstall')  # To prevent pre-commit failures when mkdocs calls push
     run(ctx, 'poetry run mkdocs gh-deploy --force')
-    run(ctx, 'pre-commit install')  # Restore pre-commit
+    with suppress(UnexpectedExit):
+        run(ctx, 'pre-commit install')  # Restore pre-commit
```

### Comparing `calcipy-1.0.1/calcipy/tasks/lint.py` & `calcipy-1.1.1/calcipy/tasks/lint.py`

 * *Files identical despite different names*

### Comparing `calcipy-1.0.1/calcipy/tasks/pack.py` & `calcipy-1.1.1/calcipy/tasks/pack.py`

 * *Files identical despite different names*

### Comparing `calcipy-1.0.1/calcipy/tasks/stale.py` & `calcipy-1.1.1/calcipy/tasks/stale.py`

 * *Files identical despite different names*

### Comparing `calcipy-1.0.1/calcipy/tasks/tags.py` & `calcipy-1.1.1/calcipy/tasks/tags.py`

 * *Files identical despite different names*

### Comparing `calcipy-1.0.1/calcipy/tasks/test.py` & `calcipy-1.1.1/calcipy/tasks/test.py`

 * *Files identical despite different names*

### Comparing `calcipy-1.0.1/calcipy/tasks/types.py` & `calcipy-1.1.1/calcipy/tasks/types.py`

 * *Files identical despite different names*

### Comparing `calcipy-1.0.1/docs/README.md` & `calcipy-1.1.1/docs/README.md`

 * *Files identical despite different names*

### Comparing `calcipy-1.0.1/pyproject.toml` & `calcipy-1.1.1/pyproject.toml`

 * *Files 3% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 [build-system]
 build-backend = "poetry.core.masonry.api"
 requires = ["poetry-core"]
 
 [tool.commitizen]
-version = "1.0.1"
+version = "1.1.1"
 version_files = ["calcipy/__init__.py:^__version", "pyproject.toml:^version"]
 
 [tool.poetry]
 authors = ["Kyle King <dev.act.kyle@gmail.com>"]
 classifiers = [
   "Development Status :: 4 - Beta",
   "Framework :: Pytest",
@@ -17,24 +17,24 @@
   "Programming Language :: Python :: 3.10",
   "Programming Language :: Python :: 3.11",
   "Programming Language :: Python :: 3.8",
   "Programming Language :: Python :: 3.9",
   "Topic :: Software Development :: Libraries",
   "Topic :: Utilities",
 ] # https://pypi.org/classifiers/
-description = "Python package to simplify development. Includes functionality for task running, testing, linting, documenting, and more"
+description = "Python package to simplify development"
 documentation = "https://calcipy.kyleking.me"
 include = ["LICENSE"]
 keywords = ["nox", "python-poetry"]
 license = "MIT"
 maintainers = []
 name = "calcipy"
 readme = "docs/README.md"
 repository = "https://github.com/kyleking/calcipy"
-version = "1.0.1"
+version = "1.1.1"
 
 [tool.poetry.dependencies]
 python = "^3.8.12"
 arrow = {optional = true, version = ">=1.2.3"} # tags
 autopep8 = {optional = true, version = ">=2.0.1"} # flake8
 bandit = {optional = true, version = ">=1.7.4"} # lint
 beartype = ">=0.12.0"
@@ -57,15 +57,14 @@
 flake8-string-format = {optional = true, version = ">=0.3.0"} # flake8
 flake8-super = {optional = true, version = ">=0.1.3"} # flake8
 flake8-tuple = {optional = true, version = ">=0.4.1"} # flake8
 flake8-typing-imports = {optional = true, version = ">=1.14.0"} # flake8
 flake8-use-pathlib = {optional = true, version = ">=0.3.0"} # flake8
 flake8-variables-names = {optional = true, version = ">=0.0.5"} # flake8
 invoke = ">=2.0.0"
-mdx_truly_sane_lists = {optional = true, version = ">=1.2"} # doc
 mkdocs = {optional = true, version = ">=1.4.1"} # doc
 mkdocs-build-plantuml-plugin = {optional = true, version = ">=1.7.4"} # doc
 mkdocs-gen-files = {optional = true, version = ">=0.4.0"} # doc
 mkdocs-git-revision-date-localized-plugin = {optional = true, version = ">=1.0.1"} # doc
 mkdocs-include-markdown-plugin = {markers = "python_version < '3.12'", optional = true, version = ">=4.0.3"} # doc
 mkdocs-literate-nav = {optional = true, version = ">=0.5.0"} # doc
 mkdocs-material = {optional = true, version = ">=8.2.16"} # doc
@@ -90,15 +89,14 @@
 tabulate = {optional = true, version = ">=0.9.0"} # tags: Required for pandas to markdown
 transitions = {optional = true, version = ">=0.9.0"} # tags: docs
 
 [tool.poetry.extras]
 ddict = ["python-box"]
 doc = [
   "commitizen",
-  "mdx_truly_sane_lists",
   "mkdocs",
   "mkdocs-build-plantuml-plugin",
   "mkdocs-gen-files",
   "mkdocs-git-revision-date-localized-plugin",
   "mkdocs-include-markdown-plugin",
   "mkdocs-literate-nav",
   "mkdocs-material",
```

### Comparing `calcipy-1.0.1/setup.py` & `calcipy-1.1.1/setup.py`

 * *Files 2% similar despite different names*

```diff
@@ -2,28 +2,28 @@
 from setuptools import setup
 
 packages = \
 ['calcipy',
  'calcipy.check_for_stale_packages',
  'calcipy.code_tag_collector',
  'calcipy.dot_dict',
+ 'calcipy.experiments',
  'calcipy.md_writer',
  'calcipy.noxfile',
  'calcipy.tasks']
 
 package_data = \
 {'': ['*']}
 
 install_requires = \
 ['beartype>=0.12.0', 'corallium>=0.1.0', 'invoke>=2.0.0', 'pydantic>=1.10.5']
 
 extras_require = \
 {'ddict': ['python-box>=6.0.2'],
  'doc': ['commitizen>=2.42.0',
-         'mdx_truly_sane_lists>=1.2',
          'mkdocs>=1.4.1',
          'mkdocs-build-plantuml-plugin>=1.7.4',
          'mkdocs-gen-files>=0.4.0',
          'mkdocs-git-revision-date-localized-plugin>=1.0.1',
          'mkdocs-literate-nav>=0.5.0',
          'mkdocs-material>=8.2.16',
          'mkdocs-section-index>=0.3.4',
@@ -74,16 +74,16 @@
 {'console_scripts': ['calcipy = calcipy.scripts:start',
                      'calcipy_lint = calcipy.scripts:start_lint',
                      'calcipy_tags = calcipy.scripts:start_tags',
                      'calcipy_types = calcipy.scripts:start_types']}
 
 setup_kwargs = {
     'name': 'calcipy',
-    'version': '1.0.1',
-    'description': 'Python package to simplify development. Includes functionality for task running, testing, linting, documenting, and more',
+    'version': '1.1.1',
+    'description': 'Python package to simplify development',
     'long_description': '# calcipy\n\n![./calcipy-banner-wide.svg](https://raw.githubusercontent.com/KyleKing/calcipy/main/docs/calcipy-banner-wide.svg)\n\n`calcipy` is a Python package that implements best practices such as code style (linting, auto-fixes), documentation, CI/CD, and logging. Like the calcium carbonate in hard coral, packages can be built on the `calcipy` foundation.\n\n`calcipy` has some configurability, but is tailored for my particular use cases. If you want the same sort of functionality, there are a number of alternatives to consider:\n\n- [pyscaffold](https://github.com/pyscaffold/pyscaffold) is a much more mature project that aims for the same goals, but with a slightly different approach and tech stack (tox vs. nox, cookiecutter vs. copier, etc.)\n- [tidypy](https://github.com/jayclassless/tidypy#features), [pylama](https://github.com/klen/pylama), and [codecheck](https://pypi.org/project/codecheck/) offer similar functionality of bundling and running static checkers, but makes far fewer assumptions\n- [pytoil](https://github.com/FollowTheProcess/pytoil) is a general CLI tool for developer automation\n- And many more such as [pyta](https://github.com/pyta-uoft/pyta), [prospector](https://github.com/PyCQA/prospector), [wemake-python-styleguide](https://github.com/wemake-services/wemake-python-styleguide) / [cjolowicz/cookiecutter-hypermodern-python](https://github.com/cjolowicz/cookiecutter-hypermodern-python), [formate](https://github.com/python-formate/formate), [johnthagen/python-blueprint](https://github.com/johnthagen/python-blueprint), [oxsecurity/megalinter](https://github.com/oxsecurity/megalinter), etc.\n\n## Installation\n\nCalcipy needs a few static files managed using copier and a template project: [kyleking/calcipy_template](https://github.com/KyleKing/calcipy_template/)\n\nYou can quickly use the template to create a new project or add calcipy to an existing one:\n\n```sh\n# Install copier. pipx is recommended\npipx install copier\n\n# To create a new project\ncopier copy gh:KyleKing/calcipy_template new_project\ncd new_project\n\n# Or convert/update an existing one\ncd my_project\ncopier copy gh:KyleKing/calcipy_template .\ncopier update\n```\n\nSee [./Advanced_Configuration.md](./Advanced_Configuration.md) for documentation on the configurable aspects of `calcipy`\n\n### Calcipy CLI\n\nAdditionally, `calcipy` can be run as a CLI application without adding the package as a dependency.\n\nQuick Start:\n\n```sh\npipx install calcipy\n\n# Use \'tags\' to create a CODE_TAG_SUMMARY of the specified directory\ncalcipy tags --help\ncalcipy tags --base-dir=~/path/to/my_project\n\n# See additional documentation from the CLI help\n> calcipy\n\nSubcommands:\n\nmain                                     Main task pipeline.\nother                                    Run tasks that are otherwise not exercised in main.\nrelease                                  Release pipeline.\ncl.bump                                  Bumps project version based on commits & settings in pyproject.toml.\ncl.write                                 Write a Changelog file with the raw Git history.\ndoc.build                                Build documentation with mkdocs.\ndoc.deploy                               Deploy docs to the Github `gh-pages` branch.\ndoc.watch                                Serve local documentation for local editing.\nlint.autopep8                            Run autopep8.\nlint.check (lint)                        Run ruff as check-only.\nlint.fix                                 Run ruff and apply fixes.\nlint.flake8                              Run ruff and apply fixes.\nlint.pre-commit                          Run pre-commit.\nlint.pylint                              Run ruff and apply fixes.\nlint.security                            Attempt to identify possible security vulnerabilities.\nlint.watch                               Run ruff as check-only.\nnox.noxfile (nox)                        Run nox from the local noxfile.\npack.check-licenses                      Check licenses for compatibility with `licensecheck`.\npack.lock                                Ensure poetry.lock is  up-to-date.\npack.publish                             Build the distributed format(s) and publish.\nstale.check-for-stale-packages (stale)   Identify stale dependencies.\ntags.collect-code-tags (tags)            Create a `CODE_TAG_SUMMARY.md` with a table for TODO- and FIXME-style code comments.\ntest.coverage                            Generate useful coverage outputs after running pytest.\ntest.pytest (test)                       Run pytest with default arguments.\ntest.step                                Run pytest optimized to stop on first error.\ntest.watch                               Run pytest with polling and optimized to stop on first error.\ntypes.mypy                               Run mypy.\ntypes.pyright                            Run pyright.\n\nGlobal Task Options:\n\nworking_dir   Set the cwd for the program. Example: "../run --working-dir .. lint test"\n*file_args    List of Paths available globally to all tasks. Will resolve paths with working_dir\nverbose       Globally configure logger verbosity (-vvv for most verbose)\n```\n\n### Calcipy Pre-Commit\n\n`calcipy` can also be used as a `pre-commit` task by adding the below snippet to your `pre-commit` file:\n\n```yaml\nrepos:\n  - repo: https://github.com/KyleKing/calcipy\n    rev: main\n    hooks:\n      - id: tags\n      - id: lint-fix\n      - id: types\n```\n\n## Project Status\n\nSee the `Open Issues` and/or the [CODE_TAG_SUMMARY]. For release history, see the [CHANGELOG].\n\n## Contributing\n\nWe welcome pull requests! For your pull request to be accepted smoothly, we suggest that you first open a GitHub issue to discuss your idea. For resources on getting started with the code base, see the below documentation:\n\n- [DEVELOPER_GUIDE]\n- [STYLE_GUIDE]\n\n## Code of Conduct\n\nWe follow the [Contributor Covenant Code of Conduct][contributor-covenant].\n\n### Open Source Status\n\nWe try to reasonably meet most aspects of the "OpenSSF scorecard" from [Open Source Insights](https://deps.dev/pypi/calcipy)\n\n## Responsible Disclosure\n\nIf you have any security issue to report, please contact the project maintainers privately. You can reach us at [dev.act.kyle@gmail.com](mailto:dev.act.kyle@gmail.com).\n\n## License\n\n[LICENSE]\n\n[changelog]: https://calcipy.kyleking.me/docs/CHANGELOG\n[code_tag_summary]: https://calcipy.kyleking.me/docs/CODE_TAG_SUMMARY\n[contributor-covenant]: https://www.contributor-covenant.org\n[developer_guide]: https://calcipy.kyleking.me/docs/DEVELOPER_GUIDE\n[license]: https://github.com/kyleking/calcipy/blob/main/LICENSE\n[style_guide]: https://calcipy.kyleking.me/docs/STYLE_GUIDE\n',
     'author': 'Kyle King',
     'author_email': 'dev.act.kyle@gmail.com',
     'maintainer': 'None',
     'maintainer_email': 'None',
     'url': 'https://github.com/kyleking/calcipy',
     'packages': packages,
```

### Comparing `calcipy-1.0.1/PKG-INFO` & `calcipy-1.1.1/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 Metadata-Version: 2.1
 Name: calcipy
-Version: 1.0.1
-Summary: Python package to simplify development. Includes functionality for task running, testing, linting, documenting, and more
+Version: 1.1.1
+Summary: Python package to simplify development
 Home-page: https://github.com/kyleking/calcipy
 License: MIT
 Keywords: nox,python-poetry
 Author: Kyle King
 Author-email: dev.act.kyle@gmail.com
 Requires-Python: >=3.8.12,<4.0.0
 Classifier: Development Status :: 4 - Beta
@@ -56,15 +56,14 @@
 Requires-Dist: flake8-string-format (>=0.3.0) ; extra == "flake8"
 Requires-Dist: flake8-super (>=0.1.3) ; extra == "flake8"
 Requires-Dist: flake8-tuple (>=0.4.1) ; extra == "flake8"
 Requires-Dist: flake8-typing-imports (>=1.14.0) ; extra == "flake8"
 Requires-Dist: flake8-use-pathlib (>=0.3.0) ; extra == "flake8"
 Requires-Dist: flake8-variables-names (>=0.0.5) ; extra == "flake8"
 Requires-Dist: invoke (>=2.0.0)
-Requires-Dist: mdx_truly_sane_lists (>=1.2) ; extra == "doc"
 Requires-Dist: mkdocs (>=1.4.1) ; extra == "doc"
 Requires-Dist: mkdocs-build-plantuml-plugin (>=1.7.4) ; extra == "doc"
 Requires-Dist: mkdocs-gen-files (>=0.4.0) ; extra == "doc"
 Requires-Dist: mkdocs-git-revision-date-localized-plugin (>=1.0.1) ; extra == "doc"
 Requires-Dist: mkdocs-include-markdown-plugin (>=4.0.3) ; (python_version < "3.12") and (extra == "doc")
 Requires-Dist: mkdocs-literate-nav (>=0.5.0) ; extra == "doc"
 Requires-Dist: mkdocs-material (>=8.2.16) ; extra == "doc"
```

