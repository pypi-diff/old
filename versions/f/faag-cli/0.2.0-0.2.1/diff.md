# Comparing `tmp/faag_cli-0.2.0.tar.gz` & `tmp/faag_cli-0.2.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "faag_cli-0.2.0.tar", max compression
+gzip compressed data, was "faag_cli-0.2.1.tar", max compression
```

## Comparing `faag_cli-0.2.0.tar` & `faag_cli-0.2.1.tar`

### file list

```diff
@@ -1,46 +1,46 @@
--rw-r--r--   0        0        0     1070 2023-03-24 20:31:10.838587 faag_cli-0.2.0/LICENSE
--rw-r--r--   0        0        0     4531 2023-03-24 20:31:10.838587 faag_cli-0.2.0/README.md
--rw-r--r--   0        0        0      100 2023-03-24 20:31:10.838587 faag_cli-0.2.0/faag_cli/__init__.py
--rw-r--r--   0        0        0        0 2023-03-24 20:31:10.838587 faag_cli-0.2.0/faag_cli/constants/__init__.py
--rw-r--r--   0        0        0      430 2023-03-24 20:31:10.838587 faag_cli-0.2.0/faag_cli/constants/app_enums.py
--rw-r--r--   0        0        0     2598 2023-03-24 20:31:10.838587 faag_cli-0.2.0/faag_cli/constants/constants.py
--rw-r--r--   0        0        0      277 2023-03-24 20:31:10.838587 faag_cli-0.2.0/faag_cli/constants/formatter_config.py
--rw-r--r--   0        0        0     5909 2023-03-24 20:31:10.838587 faag_cli-0.2.0/faag_cli/constants/pylint_rules.py
--rw-r--r--   0        0        0      728 2023-03-24 20:31:10.838587 faag_cli-0.2.0/faag_cli/constants/ruff_rules.py
--rw-r--r--   0        0        0        0 2023-03-24 20:31:10.838587 faag_cli-0.2.0/faag_cli/core/__init__.py
--rw-r--r--   0        0        0     4906 2023-03-24 20:31:10.838587 faag_cli-0.2.0/faag_cli/core/app_generator.py
--rw-r--r--   0        0        0      166 2023-03-24 20:31:10.838587 faag_cli-0.2.0/faag_cli/core/feature_generator.py
--rw-r--r--   0        0        0     3232 2023-03-24 20:31:36.770909 faag_cli-0.2.0/faag_cli/faag.py
--rw-r--r--   0        0        0      114 2023-03-24 20:31:10.838587 faag_cli-0.2.0/faag_cli/templates/.env.jinja
--rw-r--r--   0        0        0       62 2023-03-24 20:31:10.838587 faag_cli-0.2.0/faag_cli/templates/.flaskenv.jinja
--rw-r--r--   0        0        0     1890 2023-03-24 20:31:10.838587 faag_cli-0.2.0/faag_cli/templates/.gitignore.jinja
--rw-r--r--   0        0        0      133 2023-03-24 20:31:10.838587 faag_cli-0.2.0/faag_cli/templates/base/__init__.jinja
--rw-r--r--   0        0        0     1380 2023-03-24 20:31:10.838587 faag_cli-0.2.0/faag_cli/templates/base/fast__init__.jinja
--rw-r--r--   0        0        0      937 2023-03-24 20:31:10.838587 faag_cli-0.2.0/faag_cli/templates/base/flask__init__.jinja
--rw-r--r--   0        0        0      983 2023-03-24 20:31:10.838587 faag_cli-0.2.0/faag_cli/templates/config/config.jinja
--rw-r--r--   0        0        0      114 2023-03-24 20:31:10.838587 faag_cli-0.2.0/faag_cli/templates/config/config__init__.jinja
--rw-r--r--   0        0        0       58 2023-03-24 20:31:10.838587 faag_cli-0.2.0/faag_cli/templates/config/constants.jinja
--rw-r--r--   0        0        0      633 2023-03-24 20:31:10.838587 faag_cli-0.2.0/faag_cli/templates/connection/connection__init__.jinja
--rw-r--r--   0        0        0      167 2023-03-24 20:31:10.838587 faag_cli-0.2.0/faag_cli/templates/controller/controller__init__.jinja
--rw-r--r--   0        0        0     1824 2023-03-24 20:31:10.838587 faag_cli-0.2.0/faag_cli/templates/controller/fast_controller.jinja
--rw-r--r--   0        0        0     1824 2023-03-24 20:31:10.838587 faag_cli-0.2.0/faag_cli/templates/controller/fast_controller__init__.jinja
--rw-r--r--   0        0        0     1551 2023-03-24 20:31:10.838587 faag_cli-0.2.0/faag_cli/templates/controller/flask_controller.jinja
--rw-r--r--   0        0        0       58 2023-03-24 20:31:10.838587 faag_cli-0.2.0/faag_cli/templates/controller/flask_controller__init__.jinja
--rw-r--r--   0        0        0      151 2023-03-24 20:31:10.838587 faag_cli-0.2.0/faag_cli/templates/controller/sample_controller.jinja
--rw-r--r--   0        0        0       40 2023-03-24 20:31:10.838587 faag_cli-0.2.0/faag_cli/templates/dao/dao__init__.jinja
--rw-r--r--   0        0        0      322 2023-03-24 20:31:10.838587 faag_cli-0.2.0/faag_cli/templates/dao/sample_dao.jinja
--rw-r--r--   0        0        0       33 2023-03-24 20:31:10.842587 faag_cli-0.2.0/faag_cli/templates/model/model__init__.jinja
--rw-r--r--   0        0        0        0 2023-03-24 20:31:10.842587 faag_cli-0.2.0/faag_cli/templates/model/sample_model.jinja
--rw-r--r--   0        0        0      281 2023-03-24 20:31:10.842587 faag_cli-0.2.0/faag_cli/templates/schemas/response/common_response_schema.jinja
--rw-r--r--   0        0        0      161 2023-03-24 20:31:10.842587 faag_cli-0.2.0/faag_cli/templates/schemas/response/user_response_schema.jinja
--rw-r--r--   0        0        0      190 2023-03-24 20:31:10.842587 faag_cli-0.2.0/faag_cli/templates/schemas/schemas__init__.jinja
--rw-r--r--   0        0        0      389 2023-03-24 20:31:10.842587 faag_cli-0.2.0/faag_cli/templates/service/sample_service.jinja
--rw-r--r--   0        0        0       52 2023-03-24 20:31:10.842587 faag_cli-0.2.0/faag_cli/templates/service/service__init__.jinja
--rw-r--r--   0        0        0     2558 2023-03-24 20:31:10.842587 faag_cli-0.2.0/faag_cli/templates/utils/logger.jinja
--rw-r--r--   0        0        0       36 2023-03-24 20:31:10.842587 faag_cli-0.2.0/faag_cli/templates/utils/utils__init__.jinja
--rw-r--r--   0        0        0        0 2023-03-24 20:31:10.842587 faag_cli-0.2.0/faag_cli/utils/__init__.py
--rw-r--r--   0        0        0     2567 2023-03-24 20:31:10.842587 faag_cli-0.2.0/faag_cli/utils/faag_utils.py
--rw-r--r--   0        0        0     2352 2023-03-24 20:31:10.842587 faag_cli-0.2.0/faag_cli/utils/poetry_template_generator.py
--rw-r--r--   0        0        0      258 2023-03-24 20:31:10.842587 faag_cli-0.2.0/faag_cli/utils/templates_loader.py
--rw-r--r--   0        0        0     2082 2023-03-24 20:31:36.770909 faag_cli-0.2.0/pyproject.toml
--rw-r--r--   0        0        0     5624 1970-01-01 00:00:00.000000 faag_cli-0.2.0/PKG-INFO
+-rw-r--r--   0        0        0     1070 2023-04-06 11:26:33.344315 faag_cli-0.2.1/LICENSE
+-rw-r--r--   0        0        0     4531 2023-04-06 11:26:33.344315 faag_cli-0.2.1/README.md
+-rw-r--r--   0        0        0      100 2023-04-06 11:26:33.344315 faag_cli-0.2.1/faag_cli/__init__.py
+-rw-r--r--   0        0        0        0 2023-04-06 11:26:33.344315 faag_cli-0.2.1/faag_cli/constants/__init__.py
+-rw-r--r--   0        0        0      430 2023-04-06 11:26:33.344315 faag_cli-0.2.1/faag_cli/constants/app_enums.py
+-rw-r--r--   0        0        0     2598 2023-04-06 11:26:33.344315 faag_cli-0.2.1/faag_cli/constants/constants.py
+-rw-r--r--   0        0        0      277 2023-04-06 11:26:33.344315 faag_cli-0.2.1/faag_cli/constants/formatter_config.py
+-rw-r--r--   0        0        0     5909 2023-04-06 11:26:33.344315 faag_cli-0.2.1/faag_cli/constants/pylint_rules.py
+-rw-r--r--   0        0        0      728 2023-04-06 11:26:33.344315 faag_cli-0.2.1/faag_cli/constants/ruff_rules.py
+-rw-r--r--   0        0        0        0 2023-04-06 11:26:33.344315 faag_cli-0.2.1/faag_cli/core/__init__.py
+-rw-r--r--   0        0        0     4906 2023-04-06 11:26:33.344315 faag_cli-0.2.1/faag_cli/core/app_generator.py
+-rw-r--r--   0        0        0      166 2023-04-06 11:26:33.344315 faag_cli-0.2.1/faag_cli/core/feature_generator.py
+-rw-r--r--   0        0        0     3232 2023-04-06 11:27:07.238901 faag_cli-0.2.1/faag_cli/faag.py
+-rw-r--r--   0        0        0      114 2023-04-06 11:26:33.344315 faag_cli-0.2.1/faag_cli/templates/.env.jinja
+-rw-r--r--   0        0        0       62 2023-04-06 11:26:33.344315 faag_cli-0.2.1/faag_cli/templates/.flaskenv.jinja
+-rw-r--r--   0        0        0     1890 2023-04-06 11:26:33.344315 faag_cli-0.2.1/faag_cli/templates/.gitignore.jinja
+-rw-r--r--   0        0        0      133 2023-04-06 11:26:33.344315 faag_cli-0.2.1/faag_cli/templates/base/__init__.jinja
+-rw-r--r--   0        0        0     1380 2023-04-06 11:26:33.344315 faag_cli-0.2.1/faag_cli/templates/base/fast__init__.jinja
+-rw-r--r--   0        0        0      937 2023-04-06 11:26:33.344315 faag_cli-0.2.1/faag_cli/templates/base/flask__init__.jinja
+-rw-r--r--   0        0        0      983 2023-04-06 11:26:33.344315 faag_cli-0.2.1/faag_cli/templates/config/config.jinja
+-rw-r--r--   0        0        0      114 2023-04-06 11:26:33.344315 faag_cli-0.2.1/faag_cli/templates/config/config__init__.jinja
+-rw-r--r--   0        0        0       58 2023-04-06 11:26:33.344315 faag_cli-0.2.1/faag_cli/templates/config/constants.jinja
+-rw-r--r--   0        0        0      633 2023-04-06 11:26:33.344315 faag_cli-0.2.1/faag_cli/templates/connection/connection__init__.jinja
+-rw-r--r--   0        0        0      167 2023-04-06 11:26:33.344315 faag_cli-0.2.1/faag_cli/templates/controller/controller__init__.jinja
+-rw-r--r--   0        0        0     1824 2023-04-06 11:26:33.344315 faag_cli-0.2.1/faag_cli/templates/controller/fast_controller.jinja
+-rw-r--r--   0        0        0     1824 2023-04-06 11:26:33.344315 faag_cli-0.2.1/faag_cli/templates/controller/fast_controller__init__.jinja
+-rw-r--r--   0        0        0     1551 2023-04-06 11:26:33.344315 faag_cli-0.2.1/faag_cli/templates/controller/flask_controller.jinja
+-rw-r--r--   0        0        0       58 2023-04-06 11:26:33.344315 faag_cli-0.2.1/faag_cli/templates/controller/flask_controller__init__.jinja
+-rw-r--r--   0        0        0      151 2023-04-06 11:26:33.344315 faag_cli-0.2.1/faag_cli/templates/controller/sample_controller.jinja
+-rw-r--r--   0        0        0       40 2023-04-06 11:26:33.344315 faag_cli-0.2.1/faag_cli/templates/dao/dao__init__.jinja
+-rw-r--r--   0        0        0      322 2023-04-06 11:26:33.344315 faag_cli-0.2.1/faag_cli/templates/dao/sample_dao.jinja
+-rw-r--r--   0        0        0       33 2023-04-06 11:26:33.344315 faag_cli-0.2.1/faag_cli/templates/model/model__init__.jinja
+-rw-r--r--   0        0        0        0 2023-04-06 11:26:33.344315 faag_cli-0.2.1/faag_cli/templates/model/sample_model.jinja
+-rw-r--r--   0        0        0      281 2023-04-06 11:26:33.344315 faag_cli-0.2.1/faag_cli/templates/schemas/response/common_response_schema.jinja
+-rw-r--r--   0        0        0      161 2023-04-06 11:26:33.344315 faag_cli-0.2.1/faag_cli/templates/schemas/response/user_response_schema.jinja
+-rw-r--r--   0        0        0      190 2023-04-06 11:26:33.344315 faag_cli-0.2.1/faag_cli/templates/schemas/schemas__init__.jinja
+-rw-r--r--   0        0        0      389 2023-04-06 11:26:33.344315 faag_cli-0.2.1/faag_cli/templates/service/sample_service.jinja
+-rw-r--r--   0        0        0       52 2023-04-06 11:26:33.344315 faag_cli-0.2.1/faag_cli/templates/service/service__init__.jinja
+-rw-r--r--   0        0        0     2558 2023-04-06 11:26:33.344315 faag_cli-0.2.1/faag_cli/templates/utils/logger.jinja
+-rw-r--r--   0        0        0       36 2023-04-06 11:26:33.344315 faag_cli-0.2.1/faag_cli/templates/utils/utils__init__.jinja
+-rw-r--r--   0        0        0        0 2023-04-06 11:26:33.344315 faag_cli-0.2.1/faag_cli/utils/__init__.py
+-rw-r--r--   0        0        0     2567 2023-04-06 11:26:33.344315 faag_cli-0.2.1/faag_cli/utils/faag_utils.py
+-rw-r--r--   0        0        0     2352 2023-04-06 11:26:33.344315 faag_cli-0.2.1/faag_cli/utils/poetry_template_generator.py
+-rw-r--r--   0        0        0      258 2023-04-06 11:26:33.344315 faag_cli-0.2.1/faag_cli/utils/templates_loader.py
+-rw-r--r--   0        0        0     2082 2023-04-06 11:27:07.238901 faag_cli-0.2.1/pyproject.toml
+-rw-r--r--   0        0        0     5624 1970-01-01 00:00:00.000000 faag_cli-0.2.1/PKG-INFO
```

### Comparing `faag_cli-0.2.0/LICENSE` & `faag_cli-0.2.1/LICENSE`

 * *Files identical despite different names*

### Comparing `faag_cli-0.2.0/README.md` & `faag_cli-0.2.1/README.md`

 * *Files identical despite different names*

### Comparing `faag_cli-0.2.0/faag_cli/constants/constants.py` & `faag_cli-0.2.1/faag_cli/constants/constants.py`

 * *Files identical despite different names*

### Comparing `faag_cli-0.2.0/faag_cli/constants/pylint_rules.py` & `faag_cli-0.2.1/faag_cli/constants/pylint_rules.py`

 * *Files identical despite different names*

### Comparing `faag_cli-0.2.0/faag_cli/constants/ruff_rules.py` & `faag_cli-0.2.1/faag_cli/constants/ruff_rules.py`

 * *Files identical despite different names*

### Comparing `faag_cli-0.2.0/faag_cli/core/app_generator.py` & `faag_cli-0.2.1/faag_cli/core/app_generator.py`

 * *Files identical despite different names*

### Comparing `faag_cli-0.2.0/faag_cli/faag.py` & `faag_cli-0.2.1/faag_cli/faag.py`

 * *Files 4% similar despite different names*

```diff
@@ -6,15 +6,15 @@
 from rich import print as rprint
 from typer import Option, Typer
 
 from faag_cli.constants.app_enums import AppTypes, FormatterTypes, LinterTypes
 from faag_cli.core.app_generator import AppGenerator
 from faag_cli.utils.faag_utils import FaagUtils
 
-__version__ = "0.2.0"
+__version__ = "0.2.1"
 
 typer_app = Typer(
     name="Faag CLI",
     help="FastAPI/Flask project generator with the best folder structure. Generate a new app using Faag CLI.",
 )  # Create a Typer instance
```

### Comparing `faag_cli-0.2.0/faag_cli/templates/.gitignore.jinja` & `faag_cli-0.2.1/faag_cli/templates/.gitignore.jinja`

 * *Files identical despite different names*

### Comparing `faag_cli-0.2.0/faag_cli/templates/base/fast__init__.jinja` & `faag_cli-0.2.1/faag_cli/templates/base/fast__init__.jinja`

 * *Files identical despite different names*

### Comparing `faag_cli-0.2.0/faag_cli/templates/base/flask__init__.jinja` & `faag_cli-0.2.1/faag_cli/templates/base/flask__init__.jinja`

 * *Files identical despite different names*

### Comparing `faag_cli-0.2.0/faag_cli/templates/config/config.jinja` & `faag_cli-0.2.1/faag_cli/templates/config/config.jinja`

 * *Files identical despite different names*

### Comparing `faag_cli-0.2.0/faag_cli/templates/connection/connection__init__.jinja` & `faag_cli-0.2.1/faag_cli/templates/connection/connection__init__.jinja`

 * *Files identical despite different names*

### Comparing `faag_cli-0.2.0/faag_cli/templates/controller/fast_controller.jinja` & `faag_cli-0.2.1/faag_cli/templates/controller/fast_controller.jinja`

 * *Files identical despite different names*

### Comparing `faag_cli-0.2.0/faag_cli/templates/controller/fast_controller__init__.jinja` & `faag_cli-0.2.1/faag_cli/templates/controller/fast_controller__init__.jinja`

 * *Files identical despite different names*

### Comparing `faag_cli-0.2.0/faag_cli/templates/controller/flask_controller.jinja` & `faag_cli-0.2.1/faag_cli/templates/controller/flask_controller.jinja`

 * *Files identical despite different names*

### Comparing `faag_cli-0.2.0/faag_cli/templates/utils/logger.jinja` & `faag_cli-0.2.1/faag_cli/templates/utils/logger.jinja`

 * *Files identical despite different names*

### Comparing `faag_cli-0.2.0/faag_cli/utils/faag_utils.py` & `faag_cli-0.2.1/faag_cli/utils/faag_utils.py`

 * *Files identical despite different names*

### Comparing `faag_cli-0.2.0/faag_cli/utils/poetry_template_generator.py` & `faag_cli-0.2.1/faag_cli/utils/poetry_template_generator.py`

 * *Files identical despite different names*

### Comparing `faag_cli-0.2.0/pyproject.toml` & `faag_cli-0.2.1/pyproject.toml`

 * *Files 12% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "faag_cli"
-version = "0.2.0"
+version = "0.2.1"
 description = "Flask/FastAPI Architecture Application Generator"
 authors = ["Vetrichelvan <pythonhubdev@gmail.com>", "Devzone <devzonehq@gmail.com>"]
 license = "MIT"
 readme = "README.md"
 keywords = ["FastAPI", "Flask", "SQLAlchemy", "Poetry", "Python", "CLI", "API", "Application", "Generator", "Architecture", "Faag"]
 packages = [{ include = "faag_cli" }]
 repository = "https://github.com/DevzoneCommunity/faag_cli"
@@ -24,20 +24,20 @@
 Jinja2 = "^3.1.2"
 typer = { extras = ["all"], version = ">=0.6.1,<0.8.0" }
 python-semantic-release = "^7.33.2"
 python-box = "^7.0.1"
 tomli-w = "^1.0.0"
 
 [tool.poetry.group.dev.dependencies]
-black = { extras = ["d"], version = "^23.1.0" }
-pre-commit = "^3.2.0"
+black = { extras = ["d"], version = "^23.3.0" }
+pre-commit = "^3.2.2"
 ruff = "^0.0.257"
 isort = "^5.12.0"
 mypy = "^1.1.1"
-types-setuptools = "^67.6.0.5"
+types-setuptools = "^67.6.0.7"
 
 [build-system]
 requires = [
     "poetry-core>=1.0.0",
 ]
 build-backend = "poetry.core.masonry.api"
```

### Comparing `faag_cli-0.2.0/PKG-INFO` & `faag_cli-0.2.1/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: faag-cli
-Version: 0.2.0
+Version: 0.2.1
 Summary: Flask/FastAPI Architecture Application Generator
 Home-page: https://github.com/DevzoneCommunity/faag_cli
 License: MIT
 Keywords: FastAPI,Flask,SQLAlchemy,Poetry,Python,CLI,API,Application,Generator,Architecture,Faag
 Author: Vetrichelvan
 Author-email: pythonhubdev@gmail.com
 Requires-Python: >=3.9,<4.0
```

