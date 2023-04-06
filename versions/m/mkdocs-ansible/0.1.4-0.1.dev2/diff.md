# Comparing `tmp/mkdocs-ansible-0.1.4.tar.gz` & `tmp/mkdocs-ansible-0.1.dev2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "mkdocs-ansible-0.1.4.tar", last modified: Thu Apr  6 15:21:23 2023, max compression
+gzip compressed data, was "mkdocs-ansible-0.1.dev2.tar", last modified: Fri Mar 10 12:52:02 2023, max compression
```

## Comparing `mkdocs-ansible-0.1.4.tar` & `mkdocs-ansible-0.1.dev2.tar`

### file list

```diff
@@ -1,48 +1,48 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:21:23.168607 mkdocs-ansible-0.1.4/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:21:23.164607 mkdocs-ansible-0.1.4/.config/
--rw-r--r--   0 runner    (1001) docker     (123)      470 2023-04-06 15:21:07.000000 mkdocs-ansible-0.1.4/.config/dictionary.txt
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 15:21:07.000000 mkdocs-ansible-0.1.4/.config/requirements-test.txt
--rw-r--r--   0 runner    (1001) docker     (123)      355 2023-04-06 15:21:07.000000 mkdocs-ansible-0.1.4/.config/requirements.in
--rw-r--r--   0 runner    (1001) docker     (123)     1290 2023-04-06 15:21:07.000000 mkdocs-ansible-0.1.4/.config/requirements.txt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:21:23.164607 mkdocs-ansible-0.1.4/.github/
--rw-r--r--   0 runner    (1001) docker     (123)       26 2023-04-06 15:21:07.000000 mkdocs-ansible-0.1.4/.github/CODEOWNERS
--rw-r--r--   0 runner    (1001) docker     (123)      373 2023-04-06 15:21:07.000000 mkdocs-ansible-0.1.4/.github/dependabot.yml
--rw-r--r--   0 runner    (1001) docker     (123)       73 2023-04-06 15:21:07.000000 mkdocs-ansible-0.1.4/.github/release-drafter.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:21:23.164607 mkdocs-ansible-0.1.4/.github/workflows/
--rw-r--r--   0 runner    (1001) docker     (123)      244 2023-04-06 15:21:07.000000 mkdocs-ansible-0.1.4/.github/workflows/ack.yml
--rw-r--r--   0 runner    (1001) docker     (123)      248 2023-04-06 15:21:07.000000 mkdocs-ansible-0.1.4/.github/workflows/push.yml
--rw-r--r--   0 runner    (1001) docker     (123)      969 2023-04-06 15:21:07.000000 mkdocs-ansible-0.1.4/.github/workflows/release.yml
--rw-r--r--   0 runner    (1001) docker     (123)     4678 2023-04-06 15:21:07.000000 mkdocs-ansible-0.1.4/.github/workflows/tox.yml
--rw-r--r--   0 runner    (1001) docker     (123)       96 2023-04-06 15:21:07.000000 mkdocs-ansible-0.1.4/.gitignore
--rw-r--r--   0 runner    (1001) docker     (123)     4195 2023-04-06 15:21:07.000000 mkdocs-ansible-0.1.4/.pre-commit-config.yaml
--rw-r--r--   0 runner    (1001) docker     (123)      439 2023-04-06 15:21:07.000000 mkdocs-ansible-0.1.4/.readthedocs.yml
--rw-r--r--   0 runner    (1001) docker     (123)      281 2023-04-06 15:21:07.000000 mkdocs-ansible-0.1.4/.yamllint
--rw-r--r--   0 runner    (1001) docker     (123)     1704 2023-04-06 15:21:23.164607 mkdocs-ansible-0.1.4/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      475 2023-04-06 15:21:07.000000 mkdocs-ansible-0.1.4/cspell.config.yaml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:21:23.164607 mkdocs-ansible-0.1.4/docs/
--rw-r--r--   0 runner    (1001) docker     (123)      691 2023-04-06 15:21:07.000000 mkdocs-ansible-0.1.4/docs/README.md
--rw-r--r--   0 runner    (1001) docker     (123)     2374 2023-04-06 15:21:07.000000 mkdocs-ansible-0.1.4/mkdocs.yml
--rw-r--r--   0 runner    (1001) docker     (123)     1807 2023-04-06 15:21:07.000000 mkdocs-ansible-0.1.4/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 15:21:23.168607 mkdocs-ansible-0.1.4/setup.cfg
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:21:23.160607 mkdocs-ansible-0.1.4/src/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:21:23.164607 mkdocs-ansible-0.1.4/src/mkdocs_ansible/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:21:23.164607 mkdocs-ansible-0.1.4/src/mkdocs_ansible/.icons/
--rw-r--r--   0 runner    (1001) docker     (123)     1047 2023-04-06 15:21:07.000000 mkdocs-ansible-0.1.4/src/mkdocs_ansible/.icons/logo.svg
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:21:23.164607 mkdocs-ansible-0.1.4/src/mkdocs_ansible/.overrides/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 15:21:07.000000 mkdocs-ansible-0.1.4/src/mkdocs_ansible/.overrides/.gitignore
--rw-r--r--   0 runner    (1001) docker     (123)      195 2023-04-06 15:21:07.000000 mkdocs-ansible-0.1.4/src/mkdocs_ansible/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      160 2023-04-06 15:21:23.000000 mkdocs-ansible-0.1.4/src/mkdocs_ansible/_version.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:21:23.160607 mkdocs-ansible-0.1.4/src/mkdocs_ansible/assets/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:21:23.164607 mkdocs-ansible-0.1.4/src/mkdocs_ansible/assets/images/
--rw-r--r--   0 runner    (1001) docker     (123)    15406 2023-04-06 15:21:07.000000 mkdocs-ansible-0.1.4/src/mkdocs_ansible/assets/images/favicon.ico
--rw-r--r--   0 runner    (1001) docker     (123)    10993 2023-04-06 15:21:07.000000 mkdocs-ansible-0.1.4/src/mkdocs_ansible/assets/images/logo.png
--rw-r--r--   0 runner    (1001) docker     (123)     1047 2023-04-06 15:21:07.000000 mkdocs-ansible-0.1.4/src/mkdocs_ansible/assets/images/logo.svg
--rw-r--r--   0 runner    (1001) docker     (123)      770 2023-04-06 15:21:07.000000 mkdocs-ansible-0.1.4/src/mkdocs_ansible/mkdocs_theme.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:21:23.164607 mkdocs-ansible-0.1.4/src/mkdocs_ansible.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     1704 2023-04-06 15:21:23.000000 mkdocs-ansible-0.1.4/src/mkdocs_ansible.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      967 2023-04-06 15:21:23.000000 mkdocs-ansible-0.1.4/src/mkdocs_ansible.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 15:21:23.000000 mkdocs-ansible-0.1.4/src/mkdocs_ansible.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       41 2023-04-06 15:21:23.000000 mkdocs-ansible-0.1.4/src/mkdocs_ansible.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (123)     1401 2023-04-06 15:21:23.000000 mkdocs-ansible-0.1.4/src/mkdocs_ansible.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       15 2023-04-06 15:21:23.000000 mkdocs-ansible-0.1.4/src/mkdocs_ansible.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)     3242 2023-04-06 15:21:07.000000 mkdocs-ansible-0.1.4/tox.ini
+drwxr-xr-x   0 ssbarnea   (501) staff       (20)        0 2023-03-10 12:52:02.939027 mkdocs-ansible-0.1.dev2/
+drwxr-xr-x   0 ssbarnea   (501) staff       (20)        0 2023-03-10 12:52:02.932857 mkdocs-ansible-0.1.dev2/.config/
+-rw-r--r--   0 ssbarnea   (501) staff       (20)      470 2023-03-10 11:03:26.000000 mkdocs-ansible-0.1.dev2/.config/dictionary.txt
+-rw-r--r--   0 ssbarnea   (501) staff       (20)        0 2023-03-09 14:28:37.000000 mkdocs-ansible-0.1.dev2/.config/requirements-test.txt
+-rw-r--r--   0 ssbarnea   (501) staff       (20)      294 2023-03-09 14:52:07.000000 mkdocs-ansible-0.1.dev2/.config/requirements.in
+-rw-r--r--   0 ssbarnea   (501) staff       (20)     1195 2023-03-10 11:06:18.000000 mkdocs-ansible-0.1.dev2/.config/requirements.txt
+drwxr-xr-x   0 ssbarnea   (501) staff       (20)        0 2023-03-10 12:52:02.933802 mkdocs-ansible-0.1.dev2/.github/
+-rw-r--r--   0 ssbarnea   (501) staff       (20)       26 2023-03-09 12:05:03.000000 mkdocs-ansible-0.1.dev2/.github/CODEOWNERS
+-rw-r--r--   0 ssbarnea   (501) staff       (20)      392 2023-02-12 10:35:38.000000 mkdocs-ansible-0.1.dev2/.github/dependabot.yml
+-rw-r--r--   0 ssbarnea   (501) staff       (20)       73 2023-02-12 10:35:38.000000 mkdocs-ansible-0.1.dev2/.github/release-drafter.yml
+drwxr-xr-x   0 ssbarnea   (501) staff       (20)        0 2023-03-10 12:52:02.934760 mkdocs-ansible-0.1.dev2/.github/workflows/
+-rw-r--r--   0 ssbarnea   (501) staff       (20)      244 2023-02-12 10:35:38.000000 mkdocs-ansible-0.1.dev2/.github/workflows/ack.yml
+-rw-r--r--   0 ssbarnea   (501) staff       (20)      248 2023-02-12 10:35:38.000000 mkdocs-ansible-0.1.dev2/.github/workflows/push.yml
+-rw-r--r--   0 ssbarnea   (501) staff       (20)      969 2023-03-09 14:36:39.000000 mkdocs-ansible-0.1.dev2/.github/workflows/release.yml
+-rw-r--r--   0 ssbarnea   (501) staff       (20)     4678 2023-03-09 14:45:58.000000 mkdocs-ansible-0.1.dev2/.github/workflows/tox.yml
+-rw-r--r--   0 ssbarnea   (501) staff       (20)       89 2023-03-10 11:11:50.000000 mkdocs-ansible-0.1.dev2/.gitignore
+-rw-r--r--   0 ssbarnea   (501) staff       (20)     4815 2023-03-09 14:28:46.000000 mkdocs-ansible-0.1.dev2/.pre-commit-config.yaml
+-rw-r--r--   0 ssbarnea   (501) staff       (20)      439 2023-02-12 10:35:38.000000 mkdocs-ansible-0.1.dev2/.readthedocs.yml
+-rw-r--r--   0 ssbarnea   (501) staff       (20)      281 2023-03-09 12:14:58.000000 mkdocs-ansible-0.1.dev2/.yamllint
+-rw-r--r--   0 ssbarnea   (501) staff       (20)     1728 2023-03-10 12:52:02.938785 mkdocs-ansible-0.1.dev2/PKG-INFO
+-rw-r--r--   0 ssbarnea   (501) staff       (20)      475 2023-02-12 10:35:38.000000 mkdocs-ansible-0.1.dev2/cspell.config.yaml
+drwxr-xr-x   0 ssbarnea   (501) staff       (20)        0 2023-03-10 12:52:02.935078 mkdocs-ansible-0.1.dev2/docs/
+-rw-r--r--   0 ssbarnea   (501) staff       (20)      691 2023-03-10 11:01:16.000000 mkdocs-ansible-0.1.dev2/docs/README.md
+-rw-r--r--   0 ssbarnea   (501) staff       (20)     2400 2023-03-10 10:57:23.000000 mkdocs-ansible-0.1.dev2/mkdocs.yml
+-rw-r--r--   0 ssbarnea   (501) staff       (20)     1886 2023-03-10 12:49:37.000000 mkdocs-ansible-0.1.dev2/pyproject.toml
+-rw-r--r--   0 ssbarnea   (501) staff       (20)       38 2023-03-10 12:52:02.939127 mkdocs-ansible-0.1.dev2/setup.cfg
+drwxr-xr-x   0 ssbarnea   (501) staff       (20)        0 2023-03-10 12:52:02.929606 mkdocs-ansible-0.1.dev2/src/
+drwxr-xr-x   0 ssbarnea   (501) staff       (20)        0 2023-03-10 12:52:02.935729 mkdocs-ansible-0.1.dev2/src/mkdocs_ansible/
+drwxr-xr-x   0 ssbarnea   (501) staff       (20)        0 2023-03-10 12:52:02.937310 mkdocs-ansible-0.1.dev2/src/mkdocs_ansible/.icons/
+-rw-r--r--   0 ssbarnea   (501) staff       (20)     1047 2023-02-12 10:35:38.000000 mkdocs-ansible-0.1.dev2/src/mkdocs_ansible/.icons/logo.svg
+drwxr-xr-x   0 ssbarnea   (501) staff       (20)        0 2023-03-10 12:52:02.937635 mkdocs-ansible-0.1.dev2/src/mkdocs_ansible/.overrides/
+-rw-r--r--   0 ssbarnea   (501) staff       (20)        0 2023-03-10 10:24:35.000000 mkdocs-ansible-0.1.dev2/src/mkdocs_ansible/.overrides/.gitignore
+-rw-r--r--   0 ssbarnea   (501) staff       (20)      179 2023-03-09 14:28:37.000000 mkdocs-ansible-0.1.dev2/src/mkdocs_ansible/__init__.py
+-rw-r--r--   0 ssbarnea   (501) staff       (20)      168 2023-03-10 12:52:02.000000 mkdocs-ansible-0.1.dev2/src/mkdocs_ansible/_version.py
+drwxr-xr-x   0 ssbarnea   (501) staff       (20)        0 2023-03-10 12:52:02.929903 mkdocs-ansible-0.1.dev2/src/mkdocs_ansible/assets/
+drwxr-xr-x   0 ssbarnea   (501) staff       (20)        0 2023-03-10 12:52:02.938469 mkdocs-ansible-0.1.dev2/src/mkdocs_ansible/assets/images/
+-rw-r--r--   0 ssbarnea   (501) staff       (20)    15406 2023-02-12 10:35:38.000000 mkdocs-ansible-0.1.dev2/src/mkdocs_ansible/assets/images/favicon.ico
+-rw-r--r--   0 ssbarnea   (501) staff       (20)    10993 2023-02-12 10:35:38.000000 mkdocs-ansible-0.1.dev2/src/mkdocs_ansible/assets/images/logo.png
+-rw-r--r--   0 ssbarnea   (501) staff       (20)     1047 2023-02-12 10:35:38.000000 mkdocs-ansible-0.1.dev2/src/mkdocs_ansible/assets/images/logo.svg
+-rw-r--r--   0 ssbarnea   (501) staff       (20)      713 2023-03-10 11:03:33.000000 mkdocs-ansible-0.1.dev2/src/mkdocs_ansible/mkdocs_theme.yml
+drwxr-xr-x   0 ssbarnea   (501) staff       (20)        0 2023-03-10 12:52:02.937151 mkdocs-ansible-0.1.dev2/src/mkdocs_ansible.egg-info/
+-rw-r--r--   0 ssbarnea   (501) staff       (20)     1728 2023-03-10 12:52:02.000000 mkdocs-ansible-0.1.dev2/src/mkdocs_ansible.egg-info/PKG-INFO
+-rw-r--r--   0 ssbarnea   (501) staff       (20)      967 2023-03-10 12:52:02.000000 mkdocs-ansible-0.1.dev2/src/mkdocs_ansible.egg-info/SOURCES.txt
+-rw-r--r--   0 ssbarnea   (501) staff       (20)        1 2023-03-10 12:52:02.000000 mkdocs-ansible-0.1.dev2/src/mkdocs_ansible.egg-info/dependency_links.txt
+-rw-r--r--   0 ssbarnea   (501) staff       (20)       41 2023-03-10 12:52:02.000000 mkdocs-ansible-0.1.dev2/src/mkdocs_ansible.egg-info/entry_points.txt
+-rw-r--r--   0 ssbarnea   (501) staff       (20)      310 2023-03-10 12:52:02.000000 mkdocs-ansible-0.1.dev2/src/mkdocs_ansible.egg-info/requires.txt
+-rw-r--r--   0 ssbarnea   (501) staff       (20)       15 2023-03-10 12:52:02.000000 mkdocs-ansible-0.1.dev2/src/mkdocs_ansible.egg-info/top_level.txt
+-rw-r--r--   0 ssbarnea   (501) staff       (20)     3379 2023-03-09 14:39:35.000000 mkdocs-ansible-0.1.dev2/tox.ini
```

### Comparing `mkdocs-ansible-0.1.4/.config/requirements.txt` & `mkdocs-ansible-0.1.dev2/.config/requirements.txt`

 * *Files 8% similar despite different names*

```diff
@@ -1,60 +1,55 @@
 #
 # This file is autogenerated by pip-compile with Python 3.9
 # by the following command:
 #
-#    pip-compile --no-annotate --output-file=.config/requirements.txt --resolver=backtracking --strip-extras --unsafe-package=ruamel-yaml-clib pyproject.toml
+#    pip-compile --extra=docs --extra=test --no-annotate --output-file=.config/requirements.txt --resolver=backtracking --strip-extras --unsafe-package=ruamel-yaml-clib pyproject.toml
 #
-beautifulsoup4==4.12.1
-cairocffi==1.5.0
-cairosvg==2.7.0
+beautifulsoup4==4.11.2
+cairocffi==1.4.0
+cairosvg==2.6.0
 certifi==2022.12.7
 cffi==1.15.1
 charset-normalizer==3.1.0
 click==8.1.3
 colorama==0.4.6
 csscompressor==0.9.5
 cssselect2==0.7.0
 defusedxml==0.7.1
 ghp-import==2.1.0
-griffe==0.26.0
-htmlmin2==0.1.13
+griffe==0.25.5
+htmlmin==0.1.12
 idna==3.4
-importlib-metadata==6.1.0
+importlib-metadata==6.0.0
 jinja2==3.1.2
 jsmin==3.0.1
 markdown==3.3.7
-markdown-exec==1.4.0
-markdown-include==0.8.1
+markdown-exec==1.3.0
 markupsafe==2.1.2
 mergedeep==1.3.4
 mkdocs==1.4.2
 mkdocs-autorefs==0.4.1
 mkdocs-gen-files==0.4.0
-mkdocs-htmlproofer-plugin==0.11.0
-mkdocs-material==9.1.5
+mkdocs-htmlproofer-plugin==0.10.3
+mkdocs-material==9.1.1
 mkdocs-material-extensions==1.1.1
-mkdocs-minify-plugin==0.6.4
-mkdocs-monorepo-plugin==1.0.4
-mkdocstrings==0.21.2
-mkdocstrings-python==0.9.0
+mkdocs-minify-plugin==0.6.2
+mkdocstrings==0.20.0
+mkdocstrings-python==0.8.3
 packaging==23.0
-pillow==9.5.0
-pipdeptree==2.7.0
+pillow==9.4.0
+pipdeptree==2.5.2
 pycparser==2.21
 pygments==2.14.0
 pymdown-extensions==9.10
 python-dateutil==2.8.2
-python-slugify==8.0.1
 pyyaml==6.0
 pyyaml-env-tag==0.1
-regex==2023.3.23
+regex==2022.10.31
 requests==2.28.2
 six==1.16.0
 soupsieve==2.4
-text-unidecode==1.3
 tinycss2==1.2.1
-typing-extensions==4.5.0
-urllib3==1.26.15
-watchdog==3.0.0
+urllib3==1.26.14
+watchdog==2.3.1
 webencodings==0.5.1
 zipp==3.15.0
```

### Comparing `mkdocs-ansible-0.1.4/.github/workflows/release.yml` & `mkdocs-ansible-0.1.dev2/.github/workflows/release.yml`

 * *Files identical despite different names*

### Comparing `mkdocs-ansible-0.1.4/.github/workflows/tox.yml` & `mkdocs-ansible-0.1.dev2/.github/workflows/tox.yml`

 * *Files identical despite different names*

### Comparing `mkdocs-ansible-0.1.4/.pre-commit-config.yaml` & `mkdocs-ansible-0.1.dev2/.pre-commit-config.yaml`

 * *Files 20% similar despite different names*

```diff
@@ -6,15 +6,20 @@
   autofix_commit_msg: |
     chore: auto fixes from pre-commit.com hooks
 
     for more information, see https://pre-commit.ci
   skip:
     # https://github.com/pre-commit-ci/issues/issues/55
     - pip-compile
+    - schemas
   submodules: true
+exclude: >
+  (?x)^(
+    src/mkdocs_ansible/_version.py
+  )$
 repos:
   - repo: meta
     hooks:
       - id: check-useless-excludes
   - repo: https://github.com/pre-commit/mirrors-prettier
     # keep it before yamllint
     rev: v3.0.0-alpha.6
@@ -22,61 +27,61 @@
       - id: prettier
         always_run: true
         additional_dependencies:
           - prettier
           - prettier-plugin-toml
           - prettier-plugin-sort-json
   - repo: https://github.com/streetsidesoftware/cspell-cli
-    rev: v6.31.0
+    rev: v6.28.0
     hooks:
       - id: cspell
         # entry: codespell --relative
         args: [--relative, --no-progress, --no-summary]
         name: Spell check with cspell
   - repo: https://github.com/python-jsonschema/check-jsonschema
-    rev: 0.22.0
+    rev: 0.21.0
     hooks:
       - id: check-github-workflows
   - repo: https://github.com/pre-commit/pre-commit-hooks.git
     rev: v4.4.0
     hooks:
       - id: end-of-file-fixer
       - id: trailing-whitespace
       - id: mixed-line-ending
       - id: fix-byte-order-marker
       - id: check-executables-have-shebangs
       - id: check-merge-conflict
       - id: debug-statements
         language_version: python3
   - repo: https://github.com/codespell-project/codespell
-    rev: v2.2.4
+    rev: v2.2.2
     hooks:
       - id: codespell
         exclude: >
           (?x)^(
             .config/dictionary.txt
           )$
         additional_dependencies:
           - tomli
   - repo: https://github.com/adrienverge/yamllint.git
-    rev: v1.30.0
+    rev: v1.29.0
     hooks:
       - id: yamllint
         files: \.(yaml|yml)$
         types: [file, yaml]
         entry: yamllint --strict
   - repo: https://github.com/PyCQA/isort
     rev: 5.12.0
     hooks:
       - id: isort
         args:
           # https://github.com/pre-commit/mirrors-isort/issues/9#issuecomment-624404082
           - --filter-files
   - repo: https://github.com/psf/black
-    rev: 23.3.0
+    rev: 23.1.0
     hooks:
       - id: black
         language_version: python3
   - repo: https://github.com/pycqa/flake8.git
     rev: 6.0.0
     hooks:
       - id: flake8
@@ -91,46 +96,57 @@
   - repo: https://github.com/asottile/pyupgrade
     # keep it after flake8
     rev: v3.3.1
     hooks:
       - id: pyupgrade
         args: ["--py39-plus"]
   - repo: https://github.com/pre-commit/mirrors-mypy
-    rev: v1.1.1
+    rev: v1.0.1
     hooks:
       - id: mypy
         # empty args needed in order to match mypy cli behavior
         args: [--strict]
         additional_dependencies: []
   - repo: https://github.com/pycqa/pylint
-    rev: v3.0.0a6
+    rev: v2.16.4
     hooks:
       - id: pylint
         args:
           - --output-format=colorized
         additional_dependencies: []
   - repo: https://github.com/jazzband/pip-tools
     rev: 6.12.3
     hooks:
       - id: pip-compile
         name: lock
         alias: lock
         always_run: true
-        entry: pip-compile --upgrade --resolver=backtracking -q --no-annotate --output-file=.config/requirements.txt pyproject.toml --strip-extras --unsafe-package ruamel-yaml-clib
+        entry: pip-compile --upgrade --resolver=backtracking -q --no-annotate --output-file=.config/requirements-lock.txt pyproject.toml --strip-extras --unsafe-package ruamel-yaml-clib
         files: ^.config\/requirements.*$
         language: python
         language_version: "3.9" # minimal we support officially
         pass_filenames: false
         stages: [manual]
         additional_dependencies:
           - pip>=22.3.1
       - id: pip-compile
         name: deps
         alias: deps
         always_run: true
-        entry: pip-compile --resolver=backtracking -q --no-annotate --output-file=.config/requirements.txt pyproject.toml --strip-extras --unsafe-package ruamel-yaml-clib
+        entry: pip-compile --resolver=backtracking -q --no-annotate --output-file=.config/requirements.txt pyproject.toml --extra docs --extra test --strip-extras --unsafe-package ruamel-yaml-clib
         files: ^.config\/requirements.*$
         language: python
         language_version: "3.9" # minimal we support officially
         pass_filenames: false
         additional_dependencies:
           - pip>=22.3.1
+      - id: pip-compile
+        entry: pip-compile --resolver=backtracking -q --no-annotate --output-file=.config/requirements.txt pyproject.toml --extra docs --extra test --strip-extras --unsafe-package ruamel-yaml-clib --upgrade
+        language: python
+        always_run: true
+        pass_filenames: false
+        files: ^.config\/requirements.*$
+        alias: up
+        stages: [manual]
+        language_version: "3.9" # minimal we support officially
+        additional_dependencies:
+          - pip>=22.3.1
```

### Comparing `mkdocs-ansible-0.1.4/PKG-INFO` & `mkdocs-ansible-0.1.dev2/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: mkdocs-ansible
-Version: 0.1.4
+Version: 0.1.dev2
 Summary: Ansible MkDocs Theme based on mkdocs-material
 Author-email: Ansible by Red Hat <info@ansible.com>
 Maintainer-email: Ansible by Red Hat <info@ansible.com>
 License: MIT
 Project-URL: homepage, https://github.com/ansible/mkdocs-ansible
 Project-URL: documentation, https://mkdocs-ansible.readthedocs.io/
 Project-URL: repository, https://github.com/ansible/mkdocs-ansible
@@ -16,14 +16,15 @@
 Classifier: Programming Language :: JavaScript
 Classifier: Programming Language :: Python
 Classifier: Topic :: Documentation
 Classifier: Topic :: Software Development :: Documentation
 Classifier: Topic :: Text Processing :: Markup :: HTML
 Requires-Python: >=3.9
 Description-Content-Type: text/markdown
+Provides-Extra: test
 Provides-Extra: lock
 
 # mkdocs-ansible theme
 
 This [mkdocs](https://www.mkdocs.org/) theme is based on [mkdocs-material](https://squidfunk.github.io/mkdocs-material/) and aims to provide a consistent
 look and feel for any project related to [Ansible](https://docs.ansible.com/) ecosystem.
```

### Comparing `mkdocs-ansible-0.1.4/docs/README.md` & `mkdocs-ansible-0.1.dev2/docs/README.md`

 * *Files identical despite different names*

### Comparing `mkdocs-ansible-0.1.4/mkdocs.yml` & `mkdocs-ansible-0.1.dev2/mkdocs.yml`

 * *Files 2% similar despite different names*

```diff
@@ -37,19 +37,21 @@
     - navigation.top
     - navigation.tracking
     - search.highlight
     - search.share
     - search.suggest
     - toc.follow
     # - toc.integrate
+  # favicon: assets/favicon.png
+  icon:
+    logo: logo
 
 # Plugins
 plugins:
-  - material/social
-  - material/search:
+  - search:
       separator: '[\s\-,:!=\[\]()"`/]+|\.(?!\d)|&[lg]t;|(?!\b)(?=[A-Z][a-z])'
   - minify:
       minify_html: true
 
 # Customization
 extra:
   # analytics:
```

### Comparing `mkdocs-ansible-0.1.4/pyproject.toml` & `mkdocs-ansible-0.1.dev2/pyproject.toml`

 * *Files 6% similar despite different names*

```diff
@@ -39,15 +39,16 @@
 [[tool.mypy.overrides]]
 module = ["mkdocs_ansible._version"]
 
 [tool.pylint.MASTER]
 ignore-paths = "^src/.*/(_version|_vendor).*$"
 
 [tool.setuptools.dynamic]
-optional-dependencies.lock = { file = [".config/requirements.txt"] }
+optional-dependencies.test = { file = [".config/requirements-test.txt"] }
+optional-dependencies.lock = { file = [".config/requirements-lock.txt"] }
 dependencies = { file = [".config/requirements.in"] }
 
 [tool.setuptools]
 include-package-data = true
 
 [tool.setuptools.packages.find]
 where = ["src"]
```

### Comparing `mkdocs-ansible-0.1.4/src/mkdocs_ansible/.icons/logo.svg` & `mkdocs-ansible-0.1.dev2/src/mkdocs_ansible/.icons/logo.svg`

 * *Files identical despite different names*

### Comparing `mkdocs-ansible-0.1.4/src/mkdocs_ansible/assets/images/favicon.ico` & `mkdocs-ansible-0.1.dev2/src/mkdocs_ansible/assets/images/favicon.ico`

 * *Files identical despite different names*

### Comparing `mkdocs-ansible-0.1.4/src/mkdocs_ansible/assets/images/logo.png` & `mkdocs-ansible-0.1.dev2/src/mkdocs_ansible/assets/images/logo.png`

 * *Files identical despite different names*

### Comparing `mkdocs-ansible-0.1.4/src/mkdocs_ansible/assets/images/logo.svg` & `mkdocs-ansible-0.1.dev2/src/mkdocs_ansible/assets/images/logo.svg`

 * *Files identical despite different names*

### Comparing `mkdocs-ansible-0.1.4/src/mkdocs_ansible/mkdocs_theme.yml` & `mkdocs-ansible-0.1.dev2/src/mkdocs_ansible/mkdocs_theme.yml`

 * *Files 9% similar despite different names*

```diff
@@ -23,13 +23,11 @@
   # text: Roboto
   # code: Roboto Mono
   text: Red Hat Display
   code: Red Hat Mono
 # From Material 5.x on, icons are inlined into the HTML and CSS as SVGs. Some
 # icons that are part of the HTML can be configured and replaced
 icon:
-  # this look inside theme/.icons/<...>.svg
-  logo: logo
 
 favicon: assets/images/favicon.ico
 static_templates:
   - 404.html
```

### Comparing `mkdocs-ansible-0.1.4/src/mkdocs_ansible.egg-info/PKG-INFO` & `mkdocs-ansible-0.1.dev2/src/mkdocs_ansible.egg-info/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: mkdocs-ansible
-Version: 0.1.4
+Version: 0.1.dev2
 Summary: Ansible MkDocs Theme based on mkdocs-material
 Author-email: Ansible by Red Hat <info@ansible.com>
 Maintainer-email: Ansible by Red Hat <info@ansible.com>
 License: MIT
 Project-URL: homepage, https://github.com/ansible/mkdocs-ansible
 Project-URL: documentation, https://mkdocs-ansible.readthedocs.io/
 Project-URL: repository, https://github.com/ansible/mkdocs-ansible
@@ -16,14 +16,15 @@
 Classifier: Programming Language :: JavaScript
 Classifier: Programming Language :: Python
 Classifier: Topic :: Documentation
 Classifier: Topic :: Software Development :: Documentation
 Classifier: Topic :: Text Processing :: Markup :: HTML
 Requires-Python: >=3.9
 Description-Content-Type: text/markdown
+Provides-Extra: test
 Provides-Extra: lock
 
 # mkdocs-ansible theme
 
 This [mkdocs](https://www.mkdocs.org/) theme is based on [mkdocs-material](https://squidfunk.github.io/mkdocs-material/) and aims to provide a consistent
 look and feel for any project related to [Ansible](https://docs.ansible.com/) ecosystem.
```

### Comparing `mkdocs-ansible-0.1.4/src/mkdocs_ansible.egg-info/SOURCES.txt` & `mkdocs-ansible-0.1.dev2/src/mkdocs_ansible.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `mkdocs-ansible-0.1.4/tox.ini` & `mkdocs-ansible-0.1.dev2/tox.ini`

 * *Files 3% similar despite different names*

```diff
@@ -63,16 +63,19 @@
 deps =
   {[testenv:lint]deps}
 setenv =
   # without his upgrade would likely not do anything
   PIP_CONSTRAINT = /dev/null
 commands =
   pre-commit run --all-files --show-diff-on-failure --hook-stage manual lock
+  pre-commit run --all-files --show-diff-on-failure --hook-stage manual up
   # Update pre-commit hooks
   pre-commit autoupdate
+  # Update npm deps
+  sh -c "cd test/schemas && npm run deps"
   # We fail if files are modified at the end
   git diff --exit-code
 
 [testenv:docs]
 description = Builds docs
 extras =
   docs
```

