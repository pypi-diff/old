# Comparing `tmp/deckz-9.4.0.tar.gz` & `tmp/deckz-9.5.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "deckz-9.4.0.tar", last modified: Wed Dec 30 00:21:51 2020, max compression
+gzip compressed data, was "deckz-9.5.0.tar", last modified: Thu Jan  7 15:15:19 2021, max compression
```

## Comparing `deckz-9.4.0.tar` & `deckz-9.5.0.tar`

### file list

```diff
@@ -1,24 +1,24 @@
--rw-r--r--   0        0        0    11358 2020-12-30 00:21:43.998245 deckz-9.4.0/LICENSE
--rw-r--r--   0        0        0     5236 2020-12-30 00:21:43.998245 deckz-9.4.0/README.md
--rw-r--r--   0        0        0       19 2020-12-30 00:21:43.998245 deckz-9.4.0/deckz/__init__.py
--rw-r--r--   0        0        0    13652 2020-12-30 00:21:43.998245 deckz-9.4.0/deckz/builder.py
--rw-r--r--   0        0        0     1157 2020-12-30 00:21:43.998245 deckz-9.4.0/deckz/cli/__init__.py
--rw-r--r--   0        0        0      470 2020-12-30 00:21:43.998245 deckz-9.4.0/deckz/cli/clean.py
--rw-r--r--   0        0        0     7753 2020-12-30 00:21:43.998245 deckz-9.4.0/deckz/cli/deps.py
--rw-r--r--   0        0        0     1292 2020-12-30 00:21:43.998245 deckz-9.4.0/deckz/cli/issue.py
--rw-r--r--   0        0        0     2665 2020-12-30 00:21:43.998245 deckz-9.4.0/deckz/cli/migrate_sections.py
--rw-r--r--   0        0        0      448 2020-12-30 00:21:43.998245 deckz-9.4.0/deckz/cli/print_config.py
--rw-r--r--   0        0        0      594 2020-12-30 00:21:43.998245 deckz-9.4.0/deckz/cli/run.py
--rw-r--r--   0        0        0      302 2020-12-30 00:21:43.998245 deckz-9.4.0/deckz/cli/upload.py
--rw-r--r--   0        0        0     3746 2020-12-30 00:21:43.998245 deckz-9.4.0/deckz/cli/watch.py
--rw-r--r--   0        0        0     1840 2020-12-30 00:21:43.998245 deckz-9.4.0/deckz/config.py
--rw-r--r--   0        0        0      160 2020-12-30 00:21:43.998245 deckz-9.4.0/deckz/exceptions.py
--rw-r--r--   0        0        0     2899 2020-12-30 00:21:43.998245 deckz-9.4.0/deckz/paths.py
--rw-r--r--   0        0        0      710 2020-12-30 00:21:43.998245 deckz-9.4.0/deckz/runner.py
--rw-r--r--   0        0        0      758 2020-12-30 00:21:43.998245 deckz-9.4.0/deckz/settings.py
--rw-r--r--   0        0        0    10730 2020-12-30 00:21:43.998245 deckz-9.4.0/deckz/targets.py
--rw-r--r--   0        0        0     8364 2020-12-30 00:21:43.998245 deckz-9.4.0/deckz/uploader.py
--rw-r--r--   0        0        0     1162 2020-12-30 00:21:43.998245 deckz-9.4.0/deckz/utils.py
--rw-r--r--   0        0        0     1027 2020-12-30 00:21:43.998245 deckz-9.4.0/pyproject.toml
--rw-r--r--   0        0        0     6619 2020-12-30 00:21:51.949508 deckz-9.4.0/setup.py
--rw-r--r--   0        0        0     6411 2020-12-30 00:21:51.950227 deckz-9.4.0/PKG-INFO
+-rw-r--r--   0        0        0    11358 2021-01-07 15:15:13.414607 deckz-9.5.0/LICENSE
+-rw-r--r--   0        0        0     5236 2021-01-07 15:15:13.414607 deckz-9.5.0/README.md
+-rw-r--r--   0        0        0       19 2021-01-07 15:15:13.414607 deckz-9.5.0/deckz/__init__.py
+-rw-r--r--   0        0        0    13652 2021-01-07 15:15:13.414607 deckz-9.5.0/deckz/builder.py
+-rw-r--r--   0        0        0     1174 2021-01-07 15:15:13.414607 deckz-9.5.0/deckz/cli/__init__.py
+-rw-r--r--   0        0        0      470 2021-01-07 15:15:13.414607 deckz-9.5.0/deckz/cli/clean.py
+-rw-r--r--   0        0        0     7753 2021-01-07 15:15:13.414607 deckz-9.5.0/deckz/cli/deps.py
+-rw-r--r--   0        0        0     1292 2021-01-07 15:15:13.414607 deckz-9.5.0/deckz/cli/issue.py
+-rw-r--r--   0        0        0     2665 2021-01-07 15:15:13.414607 deckz-9.5.0/deckz/cli/migrate_sections.py
+-rw-r--r--   0        0        0      448 2021-01-07 15:15:13.414607 deckz-9.5.0/deckz/cli/print_config.py
+-rw-r--r--   0        0        0      594 2021-01-07 15:15:13.414607 deckz-9.5.0/deckz/cli/run.py
+-rw-r--r--   0        0        0      302 2021-01-07 15:15:13.414607 deckz-9.5.0/deckz/cli/upload.py
+-rw-r--r--   0        0        0     3746 2021-01-07 15:15:13.414607 deckz-9.5.0/deckz/cli/watch.py
+-rw-r--r--   0        0        0     1840 2021-01-07 15:15:13.414607 deckz-9.5.0/deckz/config.py
+-rw-r--r--   0        0        0      160 2021-01-07 15:15:13.414607 deckz-9.5.0/deckz/exceptions.py
+-rw-r--r--   0        0        0     2899 2021-01-07 15:15:13.414607 deckz-9.5.0/deckz/paths.py
+-rw-r--r--   0        0        0      710 2021-01-07 15:15:13.414607 deckz-9.5.0/deckz/runner.py
+-rw-r--r--   0        0        0      758 2021-01-07 15:15:13.414607 deckz-9.5.0/deckz/settings.py
+-rw-r--r--   0        0        0    10730 2021-01-07 15:15:13.414607 deckz-9.5.0/deckz/targets.py
+-rw-r--r--   0        0        0     8364 2021-01-07 15:15:13.414607 deckz-9.5.0/deckz/uploader.py
+-rw-r--r--   0        0        0     1162 2021-01-07 15:15:13.414607 deckz-9.5.0/deckz/utils.py
+-rw-r--r--   0        0        0     1027 2021-01-07 15:15:13.418607 deckz-9.5.0/pyproject.toml
+-rw-r--r--   0        0        0     6619 2021-01-07 15:15:19.651425 deckz-9.5.0/setup.py
+-rw-r--r--   0        0        0     6411 2021-01-07 15:15:19.652115 deckz-9.5.0/PKG-INFO
```

### Comparing `deckz-9.4.0/LICENSE` & `deckz-9.5.0/LICENSE`

 * *Files identical despite different names*

### Comparing `deckz-9.4.0/README.md` & `deckz-9.5.0/README.md`

 * *Files identical despite different names*

### Comparing `deckz-9.4.0/deckz/builder.py` & `deckz-9.5.0/deckz/builder.py`

 * *Files identical despite different names*

### Comparing `deckz-9.4.0/deckz/cli/__init__.py` & `deckz-9.5.0/deckz/cli/__init__.py`

 * *Files 8% similar despite different names*

```diff
@@ -4,15 +4,16 @@
 
 from rich.logging import RichHandler
 from typer import Typer
 
 
 app = Typer(
     help="Tool to handle a large number of beamer decks, "
-    "used by several persons, with shared slides amongst the decks."
+    "used by several persons, with shared slides amongst the decks.",
+    chain=True,
 )
 
 
 def main() -> None:
     basicConfig(
         level=INFO,
         format="%(message)s",
```

### Comparing `deckz-9.4.0/deckz/cli/deps.py` & `deckz-9.5.0/deckz/cli/deps.py`

 * *Files identical despite different names*

### Comparing `deckz-9.4.0/deckz/cli/issue.py` & `deckz-9.5.0/deckz/cli/issue.py`

 * *Files identical despite different names*

### Comparing `deckz-9.4.0/deckz/cli/migrate_sections.py` & `deckz-9.5.0/deckz/cli/migrate_sections.py`

 * *Files identical despite different names*

### Comparing `deckz-9.4.0/deckz/cli/run.py` & `deckz-9.5.0/deckz/cli/run.py`

 * *Files identical despite different names*

### Comparing `deckz-9.4.0/deckz/cli/watch.py` & `deckz-9.5.0/deckz/cli/watch.py`

 * *Files identical despite different names*

### Comparing `deckz-9.4.0/deckz/config.py` & `deckz-9.5.0/deckz/config.py`

 * *Files identical despite different names*

### Comparing `deckz-9.4.0/deckz/paths.py` & `deckz-9.5.0/deckz/paths.py`

 * *Files identical despite different names*

### Comparing `deckz-9.4.0/deckz/runner.py` & `deckz-9.5.0/deckz/runner.py`

 * *Files identical despite different names*

### Comparing `deckz-9.4.0/deckz/settings.py` & `deckz-9.5.0/deckz/settings.py`

 * *Files identical despite different names*

### Comparing `deckz-9.4.0/deckz/targets.py` & `deckz-9.5.0/deckz/targets.py`

 * *Files identical despite different names*

### Comparing `deckz-9.4.0/deckz/uploader.py` & `deckz-9.5.0/deckz/uploader.py`

 * *Files identical despite different names*

### Comparing `deckz-9.4.0/deckz/utils.py` & `deckz-9.5.0/deckz/utils.py`

 * *Files identical despite different names*

### Comparing `deckz-9.4.0/pyproject.toml` & `deckz-9.5.0/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -2,15 +2,15 @@
 authors = ["m09 <142691+m09@users.noreply.github.com>"]
 classifiers = ["Topic :: Software Development :: Build Tools"]
 description = "Tool to handle multiple beamer decks."
 homepage = "https://github.com/m09/deckz"
 license = "Apache-2.0"
 name = "deckz"
 readme = "README.md"
-version = "9.4.0"
+version = "9.5.0"
 
 [tool.poetry.dependencies]
 GitPython = "^3.1.0"
 Jinja2 = "^2.11.1"
 PyYAML = "^5.3.1"
 appdirs = "^1.4.3"
 dulwich = "^0.20.11"
```

### Comparing `deckz-9.4.0/setup.py` & `deckz-9.5.0/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -22,15 +22,15 @@
  'watchdog>=0.10.2,<0.11.0']
 
 entry_points = \
 {'console_scripts': ['deckz = deckz.cli:main']}
 
 setup_kwargs = {
     'name': 'deckz',
-    'version': '9.4.0',
+    'version': '9.5.0',
     'description': 'Tool to handle multiple beamer decks.',
     'long_description': "# `deckz`\n\n[![CI Status](https://img.shields.io/github/workflow/status/m09/deckz/CI?label=CI&style=for-the-badge)](https://github.com/m09/deckz/actions?query=workflow%3ACI)\n[![CD Status](https://img.shields.io/github/workflow/status/m09/deckz/CD?label=CD&style=for-the-badge)](https://github.com/m09/deckz/actions?query=workflow%3ACD)\n[![Test Coverage](https://img.shields.io/codecov/c/github/m09/deckz?style=for-the-badge)](https://codecov.io/gh/m09/deckz)\n[![PyPI Project](https://img.shields.io/pypi/v/deckz?style=for-the-badge)](https://pypi.org/project/deckz/)\n\nTool to handle a large number of beamer decks, used by several persons, with shared slides amongst the decks. It is currently not meant to be usable directly by people finding about the package on GitHub. Please open an issue if you want more details or want to discuss this solution.\n\n## Installation\n\nWith `pip`:\n\n```shell\npip install deckz\n```\n\n### Shell completion installation\n\nDepending on your shell:\n\n- For Bash:\n\n    ```shell\n    _DECKZ_COMPLETE=source_bash deckz > deckz-complete.sh\n    ```\n\n- For Zsh:\n\n    ```shell\n    _DECKZ_COMPLETE=source_zsh deckz > deckz-complete.sh\n    ```\n\n- For Fish:\n\n    ```shell\n    _DECKZ_COMPLETE=source_fish deckz > deckz-complete.sh\n    ```\n\nAnd then source/activate the resulting file in your shell config.\n\n## Directory Structure\n\n`deckz` works with big assumptions on the directory structure of your presentation repository. Among those assumptions:\n\n- your directory should be a git repository\n- it should contain a `shared` folder for everything that will be shared by all decks during compilation (images, code snippets, etc)\n- it should contain jinja2 LaTeX templates in the `templates/jinja2` directory, with a specific name (listed below)\n- it should contain YAML templates in the `templates/yml` directory, with specific names (listed below)\n- your deck folders should be contained in an organization/company folder. This is meant to avoid repeating the company details all over the place\n- several configuration should be present to customize the decks efficiently (more on that later)\n\n```text\nroot (git repository)\n├── global-config.yml\n├── templates\n│\xa0\xa0 ├── jinja2\n│   │   ├── main.tex\n│   │   └── print.tex\n│\xa0\xa0 └── yml\n│       ├── company-config.yml\n│       ├── deck-config.yml\n│       ├── global-config.yml\n│       ├── targets.yml\n│       └── user-config.yml\n├── shared\n│\xa0\xa0 ├── img\n│\xa0\xa0 │\xa0\xa0 ├── image1.png\n│\xa0\xa0 │\xa0\xa0 └── image2.jpg\n│\xa0\xa0 ├── code\n│\xa0\xa0 │\xa0\xa0 ├── snippet1.py\n│\xa0\xa0 │\xa0\xa0 └── snippet2.js\n│\xa0\xa0 └── latex\n│\xa0\xa0  \xa0\xa0 ├── module1.tex\n│\xa0\xa0  \xa0\xa0 └── module2.tex\n├── company1\n│\xa0\xa0 ├── company-config.yml\n│\xa0\xa0 └── deck1\n│\xa0\xa0  \xa0\xa0 ├── session-config.yml\n│\xa0\xa0  \xa0\xa0 ├── deck-config.yml\n│\xa0\xa0  \xa0\xa0 └── targets.yml\n└── company2\n \xa0\xa0 ├── company-config.yml\n \xa0\xa0 └── deck2\n        ├── target1\n        │   └── custom-module.tex\n \xa0\xa0  \xa0\xa0 ├── deck-config.yml\n \xa0\xa0  \xa0\xa0 └── targets.yml\n```\n\n## Configuration\n\n`deckz` uses small configuration files in several places to avoid repetition.\n\n### Configuration merging\n\nThe configuration are merged in this order (a value from a configuration on the bottom overrides a value from a configuration on the top):\n\n- `global-config.yml`\n- `user-config.yml`\n- `company-config.yml`\n- `deck-config.yml`\n- `session-config.yml`\n\n### Using the configuration values in LaTeX files\n\nThe values obtained from the merged configurations can be used in LaTeX after a conversion from snake case to camel case: if the configuration contains the key `trainer_email`, it will be defined as the `\\TrainerEmail` command in LaTeX.\n\n### Details about specific configurations\n\n#### Global configuration\n\nThe global configuration contains the default values that don't fit at a more specific level.\n\nExample:\n\n```yml\npresentation_size: 10pt\n```\n\n#### User configuration\n\nThe user configuration contains the values that change when the speaker changes. It is located in the XDG compliant config location. It is `$HOME/.config/deckz/user-config.yml` on GNU/Linux for example.\n\nExample:\n\n```yml\ntrainer_activity: Data Scientist\ntrainer_email: john@doe.me\ntrainer_name: John Doe\ntrainer_specialization: NLP, NLU\ntrainer_training: MSc at UCL\n```\n\n#### Company configuration\n\nThe company configuration contains everything required to brand the presentations according to the represented company.\n\nExample:\n\n```yml\ncompany_logo: logo_company\ncompany_logo_height: 1cm\ncompany_name: Company\ncompany_website: https://www.company.com\n```\n\n#### Deck configuration\n\nThe deck configuration contains the title and acronym of the talk.\n\nExample:\n\n```yml\ndeck_acronym: COV19\ndeck_title: Machine Learning and COVID-19\n```\n\n#### Session configuration\n\nThe session configuration is optional and contains everything that will change from one session of a specific talk to another one.\n\nExample:\n\n```yml\nsession_end: 30/04/2020\nsession_start: 27/04/2020\n```\n\n## Usage\n\nSee the `--help` flag of the `deckz` command line tool.\n",
     'author': 'm09',
     'author_email': '142691+m09@users.noreply.github.com',
     'maintainer': None,
     'maintainer_email': None,
     'url': 'https://github.com/m09/deckz',
```

### Comparing `deckz-9.4.0/PKG-INFO` & `deckz-9.5.0/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: deckz
-Version: 9.4.0
+Version: 9.5.0
 Summary: Tool to handle multiple beamer decks.
 Home-page: https://github.com/m09/deckz
 License: Apache-2.0
 Author: m09
 Author-email: 142691+m09@users.noreply.github.com
 Requires-Python: >=3.6,<4.0
 Classifier: License :: OSI Approved :: Apache Software License
```

