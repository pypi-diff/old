# Comparing `tmp/gto-0.3.0rc1.tar.gz` & `tmp/gto-0.3.0rc2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "gto-0.3.0rc1.tar", last modified: Thu Apr  6 15:16:22 2023, max compression
+gzip compressed data, was "gto-0.3.0rc2.tar", last modified: Thu Apr  6 16:35:45 2023, max compression
```

## Comparing `gto-0.3.0rc1.tar` & `gto-0.3.0rc2.tar`

### file list

```diff
@@ -1,66 +1,66 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:16:22.886763 gto-0.3.0rc1/
--rw-r--r--   0 runner    (1001) docker     (123)      164 2023-04-06 15:16:11.000000 gto-0.3.0rc1/.coveragerc
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:16:22.874763 gto-0.3.0rc1/.github/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:16:22.878763 gto-0.3.0rc1/.github/ISSUE_TEMPLATE/
--rw-r--r--   0 runner    (1001) docker     (123)     1358 2023-04-06 15:16:11.000000 gto-0.3.0rc1/.github/ISSUE_TEMPLATE/epic-or-story.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:16:22.878763 gto-0.3.0rc1/.github/workflows/
--rw-r--r--   0 runner    (1001) docker     (123)     3442 2023-04-06 15:16:11.000000 gto-0.3.0rc1/.github/workflows/check-test-release.yml
--rw-r--r--   0 runner    (1001) docker     (123)     2071 2023-04-06 15:16:11.000000 gto-0.3.0rc1/.gitignore
--rw-r--r--   0 runner    (1001) docker     (123)     1457 2023-04-06 15:16:11.000000 gto-0.3.0rc1/.pre-commit-config.yaml
--rw-r--r--   0 runner    (1001) docker     (123)    20057 2023-04-06 15:16:11.000000 gto-0.3.0rc1/.pylintrc
--rw-r--r--   0 runner    (1001) docker     (123)    11345 2023-04-06 15:16:11.000000 gto-0.3.0rc1/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)     3502 2023-04-06 15:16:22.886763 gto-0.3.0rc1/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     2765 2023-04-06 15:16:11.000000 gto-0.3.0rc1/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:16:22.882763 gto-0.3.0rc1/gto/
--rw-r--r--   0 runner    (1001) docker     (123)      265 2023-04-06 15:16:11.000000 gto-0.3.0rc1/gto/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      163 2023-04-06 15:16:22.000000 gto-0.3.0rc1/gto/_gto_version.py
--rw-r--r--   0 runner    (1001) docker     (123)      404 2023-04-06 15:16:11.000000 gto-0.3.0rc1/gto/_version.py
--rw-r--r--   0 runner    (1001) docker     (123)    17289 2023-04-06 15:16:11.000000 gto-0.3.0rc1/gto/api.py
--rw-r--r--   0 runner    (1001) docker     (123)    19695 2023-04-06 15:16:11.000000 gto-0.3.0rc1/gto/base.py
--rw-r--r--   0 runner    (1001) docker     (123)    29313 2023-04-06 15:16:11.000000 gto-0.3.0rc1/gto/cli.py
--rw-r--r--   0 runner    (1001) docker     (123)      501 2023-04-06 15:16:11.000000 gto-0.3.0rc1/gto/commit_message_generator.py
--rw-r--r--   0 runner    (1001) docker     (123)     4102 2023-04-06 15:16:11.000000 gto-0.3.0rc1/gto/config.py
--rw-r--r--   0 runner    (1001) docker     (123)     3724 2023-04-06 15:16:11.000000 gto-0.3.0rc1/gto/constants.py
--rw-r--r--   0 runner    (1001) docker     (123)     5762 2023-04-06 15:16:11.000000 gto-0.3.0rc1/gto/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)     3266 2023-04-06 15:16:11.000000 gto-0.3.0rc1/gto/ext.py
--rw-r--r--   0 runner    (1001) docker     (123)      833 2023-04-06 15:16:11.000000 gto-0.3.0rc1/gto/ext_dvc.py
--rw-r--r--   0 runner    (1001) docker     (123)     1368 2023-04-06 15:16:11.000000 gto-0.3.0rc1/gto/ext_mlem.py
--rw-r--r--   0 runner    (1001) docker     (123)     7367 2023-04-06 15:16:11.000000 gto-0.3.0rc1/gto/git_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)    18038 2023-04-06 15:16:11.000000 gto-0.3.0rc1/gto/index.py
--rw-r--r--   0 runner    (1001) docker     (123)      763 2023-04-06 15:16:11.000000 gto-0.3.0rc1/gto/log.py
--rw-r--r--   0 runner    (1001) docker     (123)    20840 2023-04-06 15:16:11.000000 gto-0.3.0rc1/gto/registry.py
--rw-r--r--   0 runner    (1001) docker     (123)    11166 2023-04-06 15:16:11.000000 gto-0.3.0rc1/gto/tag.py
--rw-r--r--   0 runner    (1001) docker     (123)     1720 2023-04-06 15:16:11.000000 gto-0.3.0rc1/gto/ui.py
--rw-r--r--   0 runner    (1001) docker     (123)     2990 2023-04-06 15:16:11.000000 gto-0.3.0rc1/gto/utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     3123 2023-04-06 15:16:11.000000 gto-0.3.0rc1/gto/versions.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:16:22.882763 gto-0.3.0rc1/gto.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     3502 2023-04-06 15:16:22.000000 gto-0.3.0rc1/gto.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     1143 2023-04-06 15:16:22.000000 gto-0.3.0rc1/gto.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 15:16:22.000000 gto-0.3.0rc1/gto.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       84 2023-04-06 15:16:22.000000 gto-0.3.0rc1/gto.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 15:16:22.000000 gto-0.3.0rc1/gto.egg-info/not-zip-safe
--rw-r--r--   0 runner    (1001) docker     (123)      236 2023-04-06 15:16:22.000000 gto-0.3.0rc1/gto.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       10 2023-04-06 15:16:22.000000 gto-0.3.0rc1/gto.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)      207 2023-04-06 15:16:11.000000 gto-0.3.0rc1/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)       41 2023-04-06 15:16:11.000000 gto-0.3.0rc1/renovate.json
--rw-r--r--   0 runner    (1001) docker     (123)     1152 2023-04-06 15:16:22.886763 gto-0.3.0rc1/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     2137 2023-04-06 15:16:11.000000 gto-0.3.0rc1/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:16:22.882763 gto-0.3.0rc1/tests/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 15:16:11.000000 gto-0.3.0rc1/tests/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3220 2023-04-06 15:16:11.000000 gto-0.3.0rc1/tests/conftest.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:16:22.886763 gto-0.3.0rc1/tests/resources/
--rw-r--r--   0 runner    (1001) docker     (123)      759 2023-04-06 15:16:11.000000 gto-0.3.0rc1/tests/resources/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2782 2023-04-06 15:16:11.000000 gto-0.3.0rc1/tests/resources/sample_remote_repo_expected_history_churn.json
--rw-r--r--   0 runner    (1001) docker     (123)      703 2023-04-06 15:16:11.000000 gto-0.3.0rc1/tests/resources/sample_remote_repo_expected_registry.json
--rw-r--r--   0 runner    (1001) docker     (123)      563 2023-04-06 15:16:11.000000 gto-0.3.0rc1/tests/skip_presets.py
--rw-r--r--   0 runner    (1001) docker     (123)    28593 2023-04-06 15:16:11.000000 gto-0.3.0rc1/tests/test_api.py
--rw-r--r--   0 runner    (1001) docker     (123)    12554 2023-04-06 15:16:11.000000 gto-0.3.0rc1/tests/test_cli.py
--rw-r--r--   0 runner    (1001) docker     (123)     3874 2023-04-06 15:16:11.000000 gto-0.3.0rc1/tests/test_config.py
--rw-r--r--   0 runner    (1001) docker     (123)     1202 2023-04-06 15:16:11.000000 gto-0.3.0rc1/tests/test_constants.py
--rw-r--r--   0 runner    (1001) docker     (123)    13338 2023-04-06 15:16:11.000000 gto-0.3.0rc1/tests/test_git_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     3241 2023-04-06 15:16:11.000000 gto-0.3.0rc1/tests/test_index.py
--rw-r--r--   0 runner    (1001) docker     (123)    19732 2023-04-06 15:16:11.000000 gto-0.3.0rc1/tests/test_registry.py
--rw-r--r--   0 runner    (1001) docker     (123)     5427 2023-04-06 15:16:11.000000 gto-0.3.0rc1/tests/test_showcase.py
--rw-r--r--   0 runner    (1001) docker     (123)     3965 2023-04-06 15:16:11.000000 gto-0.3.0rc1/tests/test_tag.py
--rw-r--r--   0 runner    (1001) docker     (123)      816 2023-04-06 15:16:11.000000 gto-0.3.0rc1/tests/test_versions.py
--rw-r--r--   0 runner    (1001) docker     (123)     1605 2023-04-06 15:16:11.000000 gto-0.3.0rc1/tests/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:35:45.196151 gto-0.3.0rc2/
+-rw-r--r--   0 runner    (1001) docker     (123)      164 2023-04-06 16:35:27.000000 gto-0.3.0rc2/.coveragerc
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:35:45.184150 gto-0.3.0rc2/.github/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:35:45.188151 gto-0.3.0rc2/.github/ISSUE_TEMPLATE/
+-rw-r--r--   0 runner    (1001) docker     (123)     1358 2023-04-06 16:35:27.000000 gto-0.3.0rc2/.github/ISSUE_TEMPLATE/epic-or-story.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:35:45.188151 gto-0.3.0rc2/.github/workflows/
+-rw-r--r--   0 runner    (1001) docker     (123)     3442 2023-04-06 16:35:27.000000 gto-0.3.0rc2/.github/workflows/check-test-release.yml
+-rw-r--r--   0 runner    (1001) docker     (123)     2071 2023-04-06 16:35:27.000000 gto-0.3.0rc2/.gitignore
+-rw-r--r--   0 runner    (1001) docker     (123)     1457 2023-04-06 16:35:27.000000 gto-0.3.0rc2/.pre-commit-config.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)    20057 2023-04-06 16:35:27.000000 gto-0.3.0rc2/.pylintrc
+-rw-r--r--   0 runner    (1001) docker     (123)    11345 2023-04-06 16:35:27.000000 gto-0.3.0rc2/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)     3502 2023-04-06 16:35:45.196151 gto-0.3.0rc2/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     2765 2023-04-06 16:35:27.000000 gto-0.3.0rc2/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:35:45.192151 gto-0.3.0rc2/gto/
+-rw-r--r--   0 runner    (1001) docker     (123)      265 2023-04-06 16:35:27.000000 gto-0.3.0rc2/gto/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      163 2023-04-06 16:35:44.000000 gto-0.3.0rc2/gto/_gto_version.py
+-rw-r--r--   0 runner    (1001) docker     (123)      404 2023-04-06 16:35:27.000000 gto-0.3.0rc2/gto/_version.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17289 2023-04-06 16:35:27.000000 gto-0.3.0rc2/gto/api.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19695 2023-04-06 16:35:27.000000 gto-0.3.0rc2/gto/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)    29313 2023-04-06 16:35:27.000000 gto-0.3.0rc2/gto/cli.py
+-rw-r--r--   0 runner    (1001) docker     (123)      501 2023-04-06 16:35:27.000000 gto-0.3.0rc2/gto/commit_message_generator.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4102 2023-04-06 16:35:27.000000 gto-0.3.0rc2/gto/config.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3724 2023-04-06 16:35:27.000000 gto-0.3.0rc2/gto/constants.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5762 2023-04-06 16:35:27.000000 gto-0.3.0rc2/gto/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3266 2023-04-06 16:35:27.000000 gto-0.3.0rc2/gto/ext.py
+-rw-r--r--   0 runner    (1001) docker     (123)      833 2023-04-06 16:35:27.000000 gto-0.3.0rc2/gto/ext_dvc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1368 2023-04-06 16:35:27.000000 gto-0.3.0rc2/gto/ext_mlem.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7367 2023-04-06 16:35:27.000000 gto-0.3.0rc2/gto/git_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)    18038 2023-04-06 16:35:27.000000 gto-0.3.0rc2/gto/index.py
+-rw-r--r--   0 runner    (1001) docker     (123)      763 2023-04-06 16:35:27.000000 gto-0.3.0rc2/gto/log.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20840 2023-04-06 16:35:27.000000 gto-0.3.0rc2/gto/registry.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11221 2023-04-06 16:35:27.000000 gto-0.3.0rc2/gto/tag.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1720 2023-04-06 16:35:27.000000 gto-0.3.0rc2/gto/ui.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2990 2023-04-06 16:35:27.000000 gto-0.3.0rc2/gto/utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3123 2023-04-06 16:35:27.000000 gto-0.3.0rc2/gto/versions.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:35:45.192151 gto-0.3.0rc2/gto.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     3502 2023-04-06 16:35:45.000000 gto-0.3.0rc2/gto.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     1143 2023-04-06 16:35:45.000000 gto-0.3.0rc2/gto.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 16:35:45.000000 gto-0.3.0rc2/gto.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       84 2023-04-06 16:35:45.000000 gto-0.3.0rc2/gto.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 16:35:45.000000 gto-0.3.0rc2/gto.egg-info/not-zip-safe
+-rw-r--r--   0 runner    (1001) docker     (123)      236 2023-04-06 16:35:45.000000 gto-0.3.0rc2/gto.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       10 2023-04-06 16:35:45.000000 gto-0.3.0rc2/gto.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      207 2023-04-06 16:35:27.000000 gto-0.3.0rc2/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)       41 2023-04-06 16:35:27.000000 gto-0.3.0rc2/renovate.json
+-rw-r--r--   0 runner    (1001) docker     (123)     1152 2023-04-06 16:35:45.196151 gto-0.3.0rc2/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     2137 2023-04-06 16:35:27.000000 gto-0.3.0rc2/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:35:45.196151 gto-0.3.0rc2/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 16:35:27.000000 gto-0.3.0rc2/tests/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3220 2023-04-06 16:35:27.000000 gto-0.3.0rc2/tests/conftest.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:35:45.196151 gto-0.3.0rc2/tests/resources/
+-rw-r--r--   0 runner    (1001) docker     (123)      759 2023-04-06 16:35:27.000000 gto-0.3.0rc2/tests/resources/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2782 2023-04-06 16:35:27.000000 gto-0.3.0rc2/tests/resources/sample_remote_repo_expected_history_churn.json
+-rw-r--r--   0 runner    (1001) docker     (123)      703 2023-04-06 16:35:27.000000 gto-0.3.0rc2/tests/resources/sample_remote_repo_expected_registry.json
+-rw-r--r--   0 runner    (1001) docker     (123)      563 2023-04-06 16:35:27.000000 gto-0.3.0rc2/tests/skip_presets.py
+-rw-r--r--   0 runner    (1001) docker     (123)    28593 2023-04-06 16:35:27.000000 gto-0.3.0rc2/tests/test_api.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12773 2023-04-06 16:35:27.000000 gto-0.3.0rc2/tests/test_cli.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3874 2023-04-06 16:35:27.000000 gto-0.3.0rc2/tests/test_config.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1202 2023-04-06 16:35:27.000000 gto-0.3.0rc2/tests/test_constants.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13338 2023-04-06 16:35:27.000000 gto-0.3.0rc2/tests/test_git_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3241 2023-04-06 16:35:27.000000 gto-0.3.0rc2/tests/test_index.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19732 2023-04-06 16:35:27.000000 gto-0.3.0rc2/tests/test_registry.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5427 2023-04-06 16:35:27.000000 gto-0.3.0rc2/tests/test_showcase.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3965 2023-04-06 16:35:27.000000 gto-0.3.0rc2/tests/test_tag.py
+-rw-r--r--   0 runner    (1001) docker     (123)      816 2023-04-06 16:35:27.000000 gto-0.3.0rc2/tests/test_versions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1605 2023-04-06 16:35:27.000000 gto-0.3.0rc2/tests/utils.py
```

### Comparing `gto-0.3.0rc1/.github/ISSUE_TEMPLATE/epic-or-story.md` & `gto-0.3.0rc2/.github/ISSUE_TEMPLATE/epic-or-story.md`

 * *Files identical despite different names*

### Comparing `gto-0.3.0rc1/.github/workflows/check-test-release.yml` & `gto-0.3.0rc2/.github/workflows/check-test-release.yml`

 * *Files identical despite different names*

### Comparing `gto-0.3.0rc1/.gitignore` & `gto-0.3.0rc2/.gitignore`

 * *Files identical despite different names*

### Comparing `gto-0.3.0rc1/.pre-commit-config.yaml` & `gto-0.3.0rc2/.pre-commit-config.yaml`

 * *Files identical despite different names*

### Comparing `gto-0.3.0rc1/.pylintrc` & `gto-0.3.0rc2/.pylintrc`

 * *Files identical despite different names*

### Comparing `gto-0.3.0rc1/LICENSE` & `gto-0.3.0rc2/LICENSE`

 * *Files identical despite different names*

### Comparing `gto-0.3.0rc1/PKG-INFO` & `gto-0.3.0rc2/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: gto
-Version: 0.3.0rc1
+Version: 0.3.0rc2
 Summary: Version and deploy your models following GitOps principles
 Download-URL: https://github.com/iterative/gto
 Author: Alexander Guschin
 Author-email: aguschin@iterative.ai
 License: Apache License 2.0
 Keywords: git repo repository artifact registry developer-tools collaboration
 Classifier: Development Status :: 2 - Pre-Alpha
```

### Comparing `gto-0.3.0rc1/README.md` & `gto-0.3.0rc2/README.md`

 * *Files identical despite different names*

### Comparing `gto-0.3.0rc1/gto/api.py` & `gto-0.3.0rc2/gto/api.py`

 * *Files identical despite different names*

### Comparing `gto-0.3.0rc1/gto/base.py` & `gto-0.3.0rc2/gto/base.py`

 * *Files identical despite different names*

### Comparing `gto-0.3.0rc1/gto/cli.py` & `gto-0.3.0rc2/gto/cli.py`

 * *Files identical despite different names*

### Comparing `gto-0.3.0rc1/gto/config.py` & `gto-0.3.0rc2/gto/config.py`

 * *Files identical despite different names*

### Comparing `gto-0.3.0rc1/gto/constants.py` & `gto-0.3.0rc2/gto/constants.py`

 * *Files identical despite different names*

### Comparing `gto-0.3.0rc1/gto/exceptions.py` & `gto-0.3.0rc2/gto/exceptions.py`

 * *Files identical despite different names*

### Comparing `gto-0.3.0rc1/gto/ext.py` & `gto-0.3.0rc2/gto/ext.py`

 * *Files identical despite different names*

### Comparing `gto-0.3.0rc1/gto/ext_dvc.py` & `gto-0.3.0rc2/gto/ext_dvc.py`

 * *Files identical despite different names*

### Comparing `gto-0.3.0rc1/gto/ext_mlem.py` & `gto-0.3.0rc2/gto/ext_mlem.py`

 * *Files identical despite different names*

### Comparing `gto-0.3.0rc1/gto/git_utils.py` & `gto-0.3.0rc2/gto/git_utils.py`

 * *Files identical despite different names*

### Comparing `gto-0.3.0rc1/gto/index.py` & `gto-0.3.0rc2/gto/index.py`

 * *Files identical despite different names*

### Comparing `gto-0.3.0rc1/gto/log.py` & `gto-0.3.0rc2/gto/log.py`

 * *Files identical despite different names*

### Comparing `gto-0.3.0rc1/gto/registry.py` & `gto-0.3.0rc2/gto/registry.py`

 * *Files identical despite different names*

### Comparing `gto-0.3.0rc1/gto/tag.py` & `gto-0.3.0rc2/gto/tag.py`

 * *Files 1% similar despite different names*

```diff
@@ -20,14 +20,15 @@
     ACTION,
     COUNTER,
     NAME,
     STAGE,
     TAG,
     VERSION,
     Action,
+    name_to_tag,
     tag_re,
     tag_to_name,
 )
 from .exceptions import (
     InvalidTagName,
     MissingArg,
     NotImplementedInGTO,
@@ -56,14 +57,16 @@
     stage: Optional[str] = None,
     repo: Optional[git.Repo] = None,
     simple: bool = False,
 ):
     if action not in TagTemplates:
         raise UnknownAction(action=action)
 
+    artifact = name_to_tag(artifact)
+
     tag = TagTemplates[action].format(artifact=artifact, version=version, stage=stage)
     if simple:
         return tag
     if repo is None:
         raise MissingArg(arg="repo")
     counter = 0
     for t in repo.tags:
```

### Comparing `gto-0.3.0rc1/gto/ui.py` & `gto-0.3.0rc2/gto/ui.py`

 * *Files identical despite different names*

### Comparing `gto-0.3.0rc1/gto/utils.py` & `gto-0.3.0rc2/gto/utils.py`

 * *Files identical despite different names*

### Comparing `gto-0.3.0rc1/gto/versions.py` & `gto-0.3.0rc2/gto/versions.py`

 * *Files identical despite different names*

### Comparing `gto-0.3.0rc1/gto.egg-info/PKG-INFO` & `gto-0.3.0rc2/gto.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: gto
-Version: 0.3.0rc1
+Version: 0.3.0rc2
 Summary: Version and deploy your models following GitOps principles
 Download-URL: https://github.com/iterative/gto
 Author: Alexander Guschin
 Author-email: aguschin@iterative.ai
 License: Apache License 2.0
 Keywords: git repo repository artifact registry developer-tools collaboration
 Classifier: Development Status :: 2 - Pre-Alpha
```

### Comparing `gto-0.3.0rc1/gto.egg-info/SOURCES.txt` & `gto-0.3.0rc2/gto.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `gto-0.3.0rc1/setup.cfg` & `gto-0.3.0rc2/setup.cfg`

 * *Files identical despite different names*

### Comparing `gto-0.3.0rc1/setup.py` & `gto-0.3.0rc2/setup.py`

 * *Files identical despite different names*

### Comparing `gto-0.3.0rc1/tests/conftest.py` & `gto-0.3.0rc2/tests/conftest.py`

 * *Files identical despite different names*

### Comparing `gto-0.3.0rc1/tests/resources/__init__.py` & `gto-0.3.0rc2/tests/resources/__init__.py`

 * *Files identical despite different names*

### Comparing `gto-0.3.0rc1/tests/resources/sample_remote_repo_expected_history_churn.json` & `gto-0.3.0rc2/tests/resources/sample_remote_repo_expected_history_churn.json`

 * *Files identical despite different names*

### Comparing `gto-0.3.0rc1/tests/resources/sample_remote_repo_expected_registry.json` & `gto-0.3.0rc2/tests/resources/sample_remote_repo_expected_registry.json`

 * *Files identical despite different names*

### Comparing `gto-0.3.0rc1/tests/skip_presets.py` & `gto-0.3.0rc2/tests/skip_presets.py`

 * *Files identical despite different names*

### Comparing `gto-0.3.0rc1/tests/test_api.py` & `gto-0.3.0rc2/tests/test_api.py`

 * *Files identical despite different names*

### Comparing `gto-0.3.0rc1/tests/test_cli.py` & `gto-0.3.0rc2/tests/test_cli.py`

 * *Files 1% similar despite different names*

```diff
@@ -351,14 +351,21 @@
 
     _check_failing_cmd(
         "register",
         ["-r", repo.working_dir, "a3", "--version", "1.2.3"],
         "❌ Supplied version '1.2.3' cannot be parsed\n",
     )
 
+    _check_successful_cmd(
+        "register",
+        ["-r", repo.working_dir, "classification/dvclive:models/nn"],
+        "classification/dvclive=models/nn@v0.0.1",
+        search_func=_check_output_contains,
+    )
+
 
 def test_assign(repo_with_commit: Tuple[git.Repo, Callable]):
     repo, write_file = repo_with_commit
 
     _check_successful_cmd(
         "register",
         ["-r", repo.working_dir, "nn1"],
```

### Comparing `gto-0.3.0rc1/tests/test_config.py` & `gto-0.3.0rc2/tests/test_config.py`

 * *Files identical despite different names*

### Comparing `gto-0.3.0rc1/tests/test_constants.py` & `gto-0.3.0rc2/tests/test_constants.py`

 * *Files identical despite different names*

### Comparing `gto-0.3.0rc1/tests/test_git_utils.py` & `gto-0.3.0rc2/tests/test_git_utils.py`

 * *Files identical despite different names*

### Comparing `gto-0.3.0rc1/tests/test_index.py` & `gto-0.3.0rc2/tests/test_index.py`

 * *Files identical despite different names*

### Comparing `gto-0.3.0rc1/tests/test_registry.py` & `gto-0.3.0rc2/tests/test_registry.py`

 * *Files identical despite different names*

### Comparing `gto-0.3.0rc1/tests/test_showcase.py` & `gto-0.3.0rc2/tests/test_showcase.py`

 * *Files identical despite different names*

### Comparing `gto-0.3.0rc1/tests/test_tag.py` & `gto-0.3.0rc2/tests/test_tag.py`

 * *Files identical despite different names*

### Comparing `gto-0.3.0rc1/tests/test_versions.py` & `gto-0.3.0rc2/tests/test_versions.py`

 * *Files identical despite different names*

### Comparing `gto-0.3.0rc1/tests/utils.py` & `gto-0.3.0rc2/tests/utils.py`

 * *Files identical despite different names*

