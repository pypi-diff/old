# Comparing `tmp/invenio-search-2.1.0.tar.gz` & `tmp/invenio-search-2.2.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/invenio-search-2.1.0.tar", last modified: Mon Oct  3 12:49:40 2022, max compression
+gzip compressed data, was "dist/invenio-search-2.2.0.tar", last modified: Thu Apr  6 12:06:32 2023, max compression
```

## Comparing `invenio-search-2.1.0.tar` & `invenio-search-2.2.0.tar`

### file list

```diff
@@ -1,150 +1,150 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-03 12:49:40.000000 invenio-search-2.1.0/
--rw-r--r--   0 runner    (1001) docker     (121)      124 2022-10-03 12:49:34.000000 invenio-search-2.1.0/.dockerignore
--rw-r--r--   0 runner    (1001) docker     (121)      667 2022-10-03 12:49:34.000000 invenio-search-2.1.0/.editorconfig
--rw-r--r--   0 runner    (1001) docker     (121)       41 2022-10-03 12:49:34.000000 invenio-search-2.1.0/.git-blame-ignore-revs
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-03 12:49:40.000000 invenio-search-2.1.0/.github/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-03 12:49:40.000000 invenio-search-2.1.0/.github/workflows/
--rw-r--r--   0 runner    (1001) docker     (121)      891 2022-10-03 12:49:34.000000 invenio-search-2.1.0/.github/workflows/pypi-publish.yml
--rw-r--r--   0 runner    (1001) docker     (121)     2403 2022-10-03 12:49:34.000000 invenio-search-2.1.0/.github/workflows/tests.yml
--rw-r--r--   0 runner    (1001) docker     (121)      605 2022-10-03 12:49:34.000000 invenio-search-2.1.0/AUTHORS.rst
--rw-r--r--   0 runner    (1001) docker     (121)     2847 2022-10-03 12:49:34.000000 invenio-search-2.1.0/CHANGES.rst
--rw-r--r--   0 runner    (1001) docker     (121)     3725 2022-10-03 12:49:34.000000 invenio-search-2.1.0/CONTRIBUTING.rst
--rw-r--r--   0 runner    (1001) docker     (121)      762 2022-10-03 12:49:34.000000 invenio-search-2.1.0/INSTALL.rst
--rw-r--r--   0 runner    (1001) docker     (121)     1067 2022-10-03 12:49:34.000000 invenio-search-2.1.0/LICENSE
--rw-r--r--   0 runner    (1001) docker     (121)      786 2022-10-03 12:49:34.000000 invenio-search-2.1.0/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (121)     5769 2022-10-03 12:49:40.000000 invenio-search-2.1.0/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     1379 2022-10-03 12:49:34.000000 invenio-search-2.1.0/README.rst
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-03 12:49:40.000000 invenio-search-2.1.0/docs/
--rw-r--r--   0 runner    (1001) docker     (121)     7441 2022-10-03 12:49:34.000000 invenio-search-2.1.0/docs/Makefile
--rw-r--r--   0 runner    (1001) docker     (121)      358 2022-10-03 12:49:34.000000 invenio-search-2.1.0/docs/api.rst
--rw-r--r--   0 runner    (1001) docker     (121)      247 2022-10-03 12:49:34.000000 invenio-search-2.1.0/docs/authors.rst
--rw-r--r--   0 runner    (1001) docker     (121)      247 2022-10-03 12:49:34.000000 invenio-search-2.1.0/docs/changes.rst
--rw-r--r--   0 runner    (1001) docker     (121)    10144 2022-10-03 12:49:34.000000 invenio-search-2.1.0/docs/conf.py
--rw-r--r--   0 runner    (1001) docker     (121)     7743 2022-10-03 12:49:34.000000 invenio-search-2.1.0/docs/configuration.rst
--rw-r--r--   0 runner    (1001) docker     (121)      252 2022-10-03 12:49:34.000000 invenio-search-2.1.0/docs/contributing.rst
--rw-r--r--   0 runner    (1001) docker     (121)      827 2022-10-03 12:49:34.000000 invenio-search-2.1.0/docs/index.rst
--rw-r--r--   0 runner    (1001) docker     (121)      247 2022-10-03 12:49:34.000000 invenio-search-2.1.0/docs/installation.rst
--rw-r--r--   0 runner    (1001) docker     (121)      253 2022-10-03 12:49:34.000000 invenio-search-2.1.0/docs/license.rst
--rw-r--r--   0 runner    (1001) docker     (121)     6997 2022-10-03 12:49:34.000000 invenio-search-2.1.0/docs/make.bat
--rw-r--r--   0 runner    (1001) docker     (121)       32 2022-10-03 12:49:34.000000 invenio-search-2.1.0/docs/requirements.txt
--rw-r--r--   0 runner    (1001) docker     (121)      263 2022-10-03 12:49:34.000000 invenio-search-2.1.0/docs/usage.rst
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-03 12:49:40.000000 invenio-search-2.1.0/examples/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-03 12:49:40.000000 invenio-search-2.1.0/examples/data/
--rw-r--r--   0 runner    (1001) docker     (121)      234 2022-10-03 12:49:34.000000 invenio-search-2.1.0/examples/data/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-03 12:49:40.000000 invenio-search-2.1.0/examples/data/demo/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-03 12:49:40.000000 invenio-search-2.1.0/examples/data/demo/authorities/
--rw-r--r--   0 runner    (1001) docker     (121)      286 2022-10-03 12:49:34.000000 invenio-search-2.1.0/examples/data/demo/authorities/authority-v1.0.0.json
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-03 12:49:40.000000 invenio-search-2.1.0/examples/data/demo/bibliographic/
--rw-r--r--   0 runner    (1001) docker     (121)      286 2022-10-03 12:49:34.000000 invenio-search-2.1.0/examples/data/demo/bibliographic/bibliographic-v1.0.0.json
--rw-r--r--   0 runner    (1001) docker     (121)      286 2022-10-03 12:49:34.000000 invenio-search-2.1.0/examples/data/demo/default-v1.0.0.json
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-03 12:49:40.000000 invenio-search-2.1.0/examples/data/os-v1/
--rw-r--r--   0 runner    (1001) docker     (121)      229 2022-10-03 12:49:34.000000 invenio-search-2.1.0/examples/data/os-v1/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-03 12:49:40.000000 invenio-search-2.1.0/examples/data/os-v1/demo/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-03 12:49:40.000000 invenio-search-2.1.0/examples/data/os-v1/demo/authorities/
--rw-r--r--   0 runner    (1001) docker     (121)      125 2022-10-03 12:49:34.000000 invenio-search-2.1.0/examples/data/os-v1/demo/authorities/authority-v1.0.0.json
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-03 12:49:40.000000 invenio-search-2.1.0/examples/data/os-v1/demo/bibliographic/
--rw-r--r--   0 runner    (1001) docker     (121)      125 2022-10-03 12:49:34.000000 invenio-search-2.1.0/examples/data/os-v1/demo/bibliographic/bibliographic-v1.0.0.json
--rw-r--r--   0 runner    (1001) docker     (121)      125 2022-10-03 12:49:34.000000 invenio-search-2.1.0/examples/data/os-v1/demo/default-v1.0.0.json
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-03 12:49:40.000000 invenio-search-2.1.0/examples/data/os-v2/
--rw-r--r--   0 runner    (1001) docker     (121)      229 2022-10-03 12:49:34.000000 invenio-search-2.1.0/examples/data/os-v2/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-03 12:49:40.000000 invenio-search-2.1.0/examples/data/os-v2/demo/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-03 12:49:40.000000 invenio-search-2.1.0/examples/data/os-v2/demo/authorities/
--rw-r--r--   0 runner    (1001) docker     (121)      125 2022-10-03 12:49:34.000000 invenio-search-2.1.0/examples/data/os-v2/demo/authorities/authority-v1.0.0.json
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-03 12:49:40.000000 invenio-search-2.1.0/examples/data/os-v2/demo/bibliographic/
--rw-r--r--   0 runner    (1001) docker     (121)      125 2022-10-03 12:49:34.000000 invenio-search-2.1.0/examples/data/os-v2/demo/bibliographic/bibliographic-v1.0.0.json
--rw-r--r--   0 runner    (1001) docker     (121)      125 2022-10-03 12:49:34.000000 invenio-search-2.1.0/examples/data/os-v2/demo/default-v1.0.0.json
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-03 12:49:40.000000 invenio-search-2.1.0/examples/data/v7/
--rw-r--r--   0 runner    (1001) docker     (121)      234 2022-10-03 12:49:34.000000 invenio-search-2.1.0/examples/data/v7/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-03 12:49:40.000000 invenio-search-2.1.0/examples/data/v7/demo/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-03 12:49:40.000000 invenio-search-2.1.0/examples/data/v7/demo/authorities/
--rw-r--r--   0 runner    (1001) docker     (121)      125 2022-10-03 12:49:34.000000 invenio-search-2.1.0/examples/data/v7/demo/authorities/authority-v1.0.0.json
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-03 12:49:40.000000 invenio-search-2.1.0/examples/data/v7/demo/bibliographic/
--rw-r--r--   0 runner    (1001) docker     (121)      125 2022-10-03 12:49:34.000000 invenio-search-2.1.0/examples/data/v7/demo/bibliographic/bibliographic-v1.0.0.json
--rw-r--r--   0 runner    (1001) docker     (121)      125 2022-10-03 12:49:34.000000 invenio-search-2.1.0/examples/data/v7/demo/default-v1.0.0.json
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-03 12:49:40.000000 invenio-search-2.1.0/invenio_search/
--rw-r--r--   0 runner    (1001) docker     (121)    13171 2022-10-03 12:49:34.000000 invenio-search-2.1.0/invenio_search/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    10375 2022-10-03 12:49:34.000000 invenio-search-2.1.0/invenio_search/api.py
--rw-r--r--   0 runner    (1001) docker     (121)     7070 2022-10-03 12:49:34.000000 invenio-search-2.1.0/invenio_search/cli.py
--rw-r--r--   0 runner    (1001) docker     (121)     3947 2022-10-03 12:49:34.000000 invenio-search-2.1.0/invenio_search/config.py
--rw-r--r--   0 runner    (1001) docker     (121)     3051 2022-10-03 12:49:34.000000 invenio-search-2.1.0/invenio_search/engine.py
--rw-r--r--   0 runner    (1001) docker     (121)      381 2022-10-03 12:49:34.000000 invenio-search-2.1.0/invenio_search/errors.py
--rw-r--r--   0 runner    (1001) docker     (121)    19431 2022-10-03 12:49:34.000000 invenio-search-2.1.0/invenio_search/ext.py
--rw-r--r--   0 runner    (1001) docker     (121)      733 2022-10-03 12:49:34.000000 invenio-search-2.1.0/invenio_search/proxies.py
--rw-r--r--   0 runner    (1001) docker     (121)     2512 2022-10-03 12:49:34.000000 invenio-search-2.1.0/invenio_search/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-03 12:49:40.000000 invenio-search-2.1.0/invenio_search.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)     5769 2022-10-03 12:49:40.000000 invenio-search-2.1.0/invenio_search.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     3757 2022-10-03 12:49:40.000000 invenio-search-2.1.0/invenio_search.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-10-03 12:49:40.000000 invenio-search-2.1.0/invenio_search.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)      138 2022-10-03 12:49:40.000000 invenio-search-2.1.0/invenio_search.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-10-03 12:49:40.000000 invenio-search-2.1.0/invenio_search.egg-info/not-zip-safe
--rw-r--r--   0 runner    (1001) docker     (121)      396 2022-10-03 12:49:40.000000 invenio-search-2.1.0/invenio_search.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)       15 2022-10-03 12:49:40.000000 invenio-search-2.1.0/invenio_search.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (121)       91 2022-10-03 12:49:34.000000 invenio-search-2.1.0/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (121)      467 2022-10-03 12:49:34.000000 invenio-search-2.1.0/requirements-devel.txt
--rwxr-xr-x   0 runner    (1001) docker     (121)      733 2022-10-03 12:49:34.000000 invenio-search-2.1.0/run-tests.sh
--rw-r--r--   0 runner    (1001) docker     (121)     1608 2022-10-03 12:49:40.000000 invenio-search-2.1.0/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)      322 2022-10-03 12:49:34.000000 invenio-search-2.1.0/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-03 12:49:40.000000 invenio-search-2.1.0/tests/
--rw-r--r--   0 runner    (1001) docker     (121)     1938 2022-10-03 12:49:34.000000 invenio-search-2.1.0/tests/conftest.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-03 12:49:40.000000 invenio-search-2.1.0/tests/mock_module/
--rw-r--r--   0 runner    (1001) docker     (121)      291 2022-10-03 12:49:34.000000 invenio-search-2.1.0/tests/mock_module/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-03 12:49:40.000000 invenio-search-2.1.0/tests/mock_module/mappings/
--rw-r--r--   0 runner    (1001) docker     (121)      295 2022-10-03 12:49:34.000000 invenio-search-2.1.0/tests/mock_module/mappings/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-03 12:49:40.000000 invenio-search-2.1.0/tests/mock_module/mappings/authors/
--rw-r--r--   0 runner    (1001) docker     (121)       17 2022-10-03 12:49:34.000000 invenio-search-2.1.0/tests/mock_module/mappings/authors/authors-v1.0.0.json
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-03 12:49:40.000000 invenio-search-2.1.0/tests/mock_module/mappings/os-v1/
--rw-r--r--   0 runner    (1001) docker     (121)      248 2022-10-03 12:49:34.000000 invenio-search-2.1.0/tests/mock_module/mappings/os-v1/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-03 12:49:40.000000 invenio-search-2.1.0/tests/mock_module/mappings/os-v1/authors/
--rw-r--r--   0 runner    (1001) docker     (121)       17 2022-10-03 12:49:34.000000 invenio-search-2.1.0/tests/mock_module/mappings/os-v1/authors/authors-v1.0.0.json
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-03 12:49:40.000000 invenio-search-2.1.0/tests/mock_module/mappings/os-v1/records/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-03 12:49:40.000000 invenio-search-2.1.0/tests/mock_module/mappings/os-v1/records/authorities/
--rw-r--r--   0 runner    (1001) docker     (121)       17 2022-10-03 12:49:34.000000 invenio-search-2.1.0/tests/mock_module/mappings/os-v1/records/authorities/authority-v1.0.0.json
--rw-r--r--   0 runner    (1001) docker     (121)        9 2022-10-03 12:49:34.000000 invenio-search-2.1.0/tests/mock_module/mappings/os-v1/records/authorities/notajson
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-03 12:49:40.000000 invenio-search-2.1.0/tests/mock_module/mappings/os-v1/records/bibliographic/
--rw-r--r--   0 runner    (1001) docker     (121)       17 2022-10-03 12:49:34.000000 invenio-search-2.1.0/tests/mock_module/mappings/os-v1/records/bibliographic/bibliographic-v1.0.0.json
--rw-r--r--   0 runner    (1001) docker     (121)       17 2022-10-03 12:49:34.000000 invenio-search-2.1.0/tests/mock_module/mappings/os-v1/records/default-v1.0.0.json
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-03 12:49:40.000000 invenio-search-2.1.0/tests/mock_module/mappings/os-v2/
--rw-r--r--   0 runner    (1001) docker     (121)      248 2022-10-03 12:49:34.000000 invenio-search-2.1.0/tests/mock_module/mappings/os-v2/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-03 12:49:40.000000 invenio-search-2.1.0/tests/mock_module/mappings/os-v2/authors/
--rw-r--r--   0 runner    (1001) docker     (121)       17 2022-10-03 12:49:34.000000 invenio-search-2.1.0/tests/mock_module/mappings/os-v2/authors/authors-v1.0.0.json
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-03 12:49:40.000000 invenio-search-2.1.0/tests/mock_module/mappings/os-v2/records/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-03 12:49:40.000000 invenio-search-2.1.0/tests/mock_module/mappings/os-v2/records/authorities/
--rw-r--r--   0 runner    (1001) docker     (121)       17 2022-10-03 12:49:34.000000 invenio-search-2.1.0/tests/mock_module/mappings/os-v2/records/authorities/authority-v1.0.0.json
--rw-r--r--   0 runner    (1001) docker     (121)        9 2022-10-03 12:49:34.000000 invenio-search-2.1.0/tests/mock_module/mappings/os-v2/records/authorities/notajson
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-03 12:49:40.000000 invenio-search-2.1.0/tests/mock_module/mappings/os-v2/records/bibliographic/
--rw-r--r--   0 runner    (1001) docker     (121)       17 2022-10-03 12:49:34.000000 invenio-search-2.1.0/tests/mock_module/mappings/os-v2/records/bibliographic/bibliographic-v1.0.0.json
--rw-r--r--   0 runner    (1001) docker     (121)       17 2022-10-03 12:49:34.000000 invenio-search-2.1.0/tests/mock_module/mappings/os-v2/records/default-v1.0.0.json
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-03 12:49:40.000000 invenio-search-2.1.0/tests/mock_module/mappings/records/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-03 12:49:40.000000 invenio-search-2.1.0/tests/mock_module/mappings/records/authorities/
--rw-r--r--   0 runner    (1001) docker     (121)       17 2022-10-03 12:49:34.000000 invenio-search-2.1.0/tests/mock_module/mappings/records/authorities/authority-v1.0.0.json
--rw-r--r--   0 runner    (1001) docker     (121)        9 2022-10-03 12:49:34.000000 invenio-search-2.1.0/tests/mock_module/mappings/records/authorities/notajson
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-03 12:49:40.000000 invenio-search-2.1.0/tests/mock_module/mappings/records/bibliographic/
--rw-r--r--   0 runner    (1001) docker     (121)       17 2022-10-03 12:49:34.000000 invenio-search-2.1.0/tests/mock_module/mappings/records/bibliographic/bibliographic-v1.0.0.json
--rw-r--r--   0 runner    (1001) docker     (121)       17 2022-10-03 12:49:34.000000 invenio-search-2.1.0/tests/mock_module/mappings/records/default-v1.0.0.json
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-03 12:49:40.000000 invenio-search-2.1.0/tests/mock_module/mappings/v7/
--rw-r--r--   0 runner    (1001) docker     (121)      248 2022-10-03 12:49:34.000000 invenio-search-2.1.0/tests/mock_module/mappings/v7/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-03 12:49:40.000000 invenio-search-2.1.0/tests/mock_module/mappings/v7/authors/
--rw-r--r--   0 runner    (1001) docker     (121)       17 2022-10-03 12:49:34.000000 invenio-search-2.1.0/tests/mock_module/mappings/v7/authors/authors-v1.0.0.json
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-03 12:49:40.000000 invenio-search-2.1.0/tests/mock_module/mappings/v7/records/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-03 12:49:40.000000 invenio-search-2.1.0/tests/mock_module/mappings/v7/records/authorities/
--rw-r--r--   0 runner    (1001) docker     (121)       17 2022-10-03 12:49:34.000000 invenio-search-2.1.0/tests/mock_module/mappings/v7/records/authorities/authority-v1.0.0.json
--rw-r--r--   0 runner    (1001) docker     (121)        9 2022-10-03 12:49:34.000000 invenio-search-2.1.0/tests/mock_module/mappings/v7/records/authorities/notajson
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-03 12:49:40.000000 invenio-search-2.1.0/tests/mock_module/mappings/v7/records/bibliographic/
--rw-r--r--   0 runner    (1001) docker     (121)       17 2022-10-03 12:49:34.000000 invenio-search-2.1.0/tests/mock_module/mappings/v7/records/bibliographic/bibliographic-v1.0.0.json
--rw-r--r--   0 runner    (1001) docker     (121)       17 2022-10-03 12:49:34.000000 invenio-search-2.1.0/tests/mock_module/mappings/v7/records/default-v1.0.0.json
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-03 12:49:40.000000 invenio-search-2.1.0/tests/mock_module/templates/
--rw-r--r--   0 runner    (1001) docker     (121)      295 2022-10-03 12:49:34.000000 invenio-search-2.1.0/tests/mock_module/templates/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-03 12:49:40.000000 invenio-search-2.1.0/tests/mock_module/templates/os-v1/
--rw-r--r--   0 runner    (1001) docker     (121)      294 2022-10-03 12:49:34.000000 invenio-search-2.1.0/tests/mock_module/templates/os-v1/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      872 2022-10-03 12:49:34.000000 invenio-search-2.1.0/tests/mock_module/templates/os-v1/record-view-os-v1.json
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-03 12:49:40.000000 invenio-search-2.1.0/tests/mock_module/templates/os-v2/
--rw-r--r--   0 runner    (1001) docker     (121)      294 2022-10-03 12:49:34.000000 invenio-search-2.1.0/tests/mock_module/templates/os-v2/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      872 2022-10-03 12:49:34.000000 invenio-search-2.1.0/tests/mock_module/templates/os-v2/record-view-os-v2.json
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-10-03 12:49:34.000000 invenio-search-2.1.0/tests/mock_module/templates/should_not_register.txt
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-03 12:49:40.000000 invenio-search-2.1.0/tests/mock_module/templates/v7/
--rw-r--r--   0 runner    (1001) docker     (121)      286 2022-10-03 12:49:34.000000 invenio-search-2.1.0/tests/mock_module/templates/v7/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      872 2022-10-03 12:49:34.000000 invenio-search-2.1.0/tests/mock_module/templates/v7/record-view-v7.json
--rw-r--r--   0 runner    (1001) docker     (121)     6238 2022-10-03 12:49:34.000000 invenio-search-2.1.0/tests/test_cli.py
--rw-r--r--   0 runner    (1001) docker     (121)    15764 2022-10-03 12:49:34.000000 invenio-search-2.1.0/tests/test_invenio_search.py
--rw-r--r--   0 runner    (1001) docker     (121)     9087 2022-10-03 12:49:34.000000 invenio-search-2.1.0/tests/test_query.py
--rw-r--r--   0 runner    (1001) docker     (121)      920 2022-10-03 12:49:34.000000 invenio-search-2.1.0/tests/test_utils.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 12:06:32.000000 invenio-search-2.2.0/
+-rw-r--r--   0 runner    (1001) docker     (122)      124 2023-04-06 12:06:28.000000 invenio-search-2.2.0/.dockerignore
+-rw-r--r--   0 runner    (1001) docker     (122)      667 2023-04-06 12:06:28.000000 invenio-search-2.2.0/.editorconfig
+-rw-r--r--   0 runner    (1001) docker     (122)       41 2023-04-06 12:06:28.000000 invenio-search-2.2.0/.git-blame-ignore-revs
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 12:06:32.000000 invenio-search-2.2.0/.github/
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 12:06:32.000000 invenio-search-2.2.0/.github/workflows/
+-rw-r--r--   0 runner    (1001) docker     (122)      891 2023-04-06 12:06:28.000000 invenio-search-2.2.0/.github/workflows/pypi-publish.yml
+-rw-r--r--   0 runner    (1001) docker     (122)     2403 2023-04-06 12:06:28.000000 invenio-search-2.2.0/.github/workflows/tests.yml
+-rw-r--r--   0 runner    (1001) docker     (122)      605 2023-04-06 12:06:28.000000 invenio-search-2.2.0/AUTHORS.rst
+-rw-r--r--   0 runner    (1001) docker     (122)     2929 2023-04-06 12:06:28.000000 invenio-search-2.2.0/CHANGES.rst
+-rw-r--r--   0 runner    (1001) docker     (122)     3725 2023-04-06 12:06:28.000000 invenio-search-2.2.0/CONTRIBUTING.rst
+-rw-r--r--   0 runner    (1001) docker     (122)      762 2023-04-06 12:06:28.000000 invenio-search-2.2.0/INSTALL.rst
+-rw-r--r--   0 runner    (1001) docker     (122)     1067 2023-04-06 12:06:28.000000 invenio-search-2.2.0/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (122)      786 2023-04-06 12:06:28.000000 invenio-search-2.2.0/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (122)     5883 2023-04-06 12:06:32.000000 invenio-search-2.2.0/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (122)     1379 2023-04-06 12:06:28.000000 invenio-search-2.2.0/README.rst
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 12:06:32.000000 invenio-search-2.2.0/docs/
+-rw-r--r--   0 runner    (1001) docker     (122)     7441 2023-04-06 12:06:28.000000 invenio-search-2.2.0/docs/Makefile
+-rw-r--r--   0 runner    (1001) docker     (122)      358 2023-04-06 12:06:28.000000 invenio-search-2.2.0/docs/api.rst
+-rw-r--r--   0 runner    (1001) docker     (122)      247 2023-04-06 12:06:28.000000 invenio-search-2.2.0/docs/authors.rst
+-rw-r--r--   0 runner    (1001) docker     (122)      247 2023-04-06 12:06:28.000000 invenio-search-2.2.0/docs/changes.rst
+-rw-r--r--   0 runner    (1001) docker     (122)    10144 2023-04-06 12:06:28.000000 invenio-search-2.2.0/docs/conf.py
+-rw-r--r--   0 runner    (1001) docker     (122)     7743 2023-04-06 12:06:28.000000 invenio-search-2.2.0/docs/configuration.rst
+-rw-r--r--   0 runner    (1001) docker     (122)      252 2023-04-06 12:06:28.000000 invenio-search-2.2.0/docs/contributing.rst
+-rw-r--r--   0 runner    (1001) docker     (122)      827 2023-04-06 12:06:28.000000 invenio-search-2.2.0/docs/index.rst
+-rw-r--r--   0 runner    (1001) docker     (122)      247 2023-04-06 12:06:28.000000 invenio-search-2.2.0/docs/installation.rst
+-rw-r--r--   0 runner    (1001) docker     (122)      253 2023-04-06 12:06:28.000000 invenio-search-2.2.0/docs/license.rst
+-rw-r--r--   0 runner    (1001) docker     (122)     6997 2023-04-06 12:06:28.000000 invenio-search-2.2.0/docs/make.bat
+-rw-r--r--   0 runner    (1001) docker     (122)       32 2023-04-06 12:06:28.000000 invenio-search-2.2.0/docs/requirements.txt
+-rw-r--r--   0 runner    (1001) docker     (122)      263 2023-04-06 12:06:28.000000 invenio-search-2.2.0/docs/usage.rst
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 12:06:32.000000 invenio-search-2.2.0/examples/
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 12:06:32.000000 invenio-search-2.2.0/examples/data/
+-rw-r--r--   0 runner    (1001) docker     (122)      234 2023-04-06 12:06:28.000000 invenio-search-2.2.0/examples/data/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 12:06:32.000000 invenio-search-2.2.0/examples/data/demo/
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 12:06:32.000000 invenio-search-2.2.0/examples/data/demo/authorities/
+-rw-r--r--   0 runner    (1001) docker     (122)      286 2023-04-06 12:06:28.000000 invenio-search-2.2.0/examples/data/demo/authorities/authority-v1.0.0.json
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 12:06:32.000000 invenio-search-2.2.0/examples/data/demo/bibliographic/
+-rw-r--r--   0 runner    (1001) docker     (122)      286 2023-04-06 12:06:28.000000 invenio-search-2.2.0/examples/data/demo/bibliographic/bibliographic-v1.0.0.json
+-rw-r--r--   0 runner    (1001) docker     (122)      286 2023-04-06 12:06:28.000000 invenio-search-2.2.0/examples/data/demo/default-v1.0.0.json
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 12:06:32.000000 invenio-search-2.2.0/examples/data/os-v1/
+-rw-r--r--   0 runner    (1001) docker     (122)      229 2023-04-06 12:06:28.000000 invenio-search-2.2.0/examples/data/os-v1/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 12:06:32.000000 invenio-search-2.2.0/examples/data/os-v1/demo/
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 12:06:32.000000 invenio-search-2.2.0/examples/data/os-v1/demo/authorities/
+-rw-r--r--   0 runner    (1001) docker     (122)      125 2023-04-06 12:06:28.000000 invenio-search-2.2.0/examples/data/os-v1/demo/authorities/authority-v1.0.0.json
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 12:06:32.000000 invenio-search-2.2.0/examples/data/os-v1/demo/bibliographic/
+-rw-r--r--   0 runner    (1001) docker     (122)      125 2023-04-06 12:06:28.000000 invenio-search-2.2.0/examples/data/os-v1/demo/bibliographic/bibliographic-v1.0.0.json
+-rw-r--r--   0 runner    (1001) docker     (122)      125 2023-04-06 12:06:28.000000 invenio-search-2.2.0/examples/data/os-v1/demo/default-v1.0.0.json
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 12:06:32.000000 invenio-search-2.2.0/examples/data/os-v2/
+-rw-r--r--   0 runner    (1001) docker     (122)      229 2023-04-06 12:06:28.000000 invenio-search-2.2.0/examples/data/os-v2/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 12:06:32.000000 invenio-search-2.2.0/examples/data/os-v2/demo/
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 12:06:32.000000 invenio-search-2.2.0/examples/data/os-v2/demo/authorities/
+-rw-r--r--   0 runner    (1001) docker     (122)      125 2023-04-06 12:06:28.000000 invenio-search-2.2.0/examples/data/os-v2/demo/authorities/authority-v1.0.0.json
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 12:06:32.000000 invenio-search-2.2.0/examples/data/os-v2/demo/bibliographic/
+-rw-r--r--   0 runner    (1001) docker     (122)      125 2023-04-06 12:06:28.000000 invenio-search-2.2.0/examples/data/os-v2/demo/bibliographic/bibliographic-v1.0.0.json
+-rw-r--r--   0 runner    (1001) docker     (122)      125 2023-04-06 12:06:28.000000 invenio-search-2.2.0/examples/data/os-v2/demo/default-v1.0.0.json
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 12:06:32.000000 invenio-search-2.2.0/examples/data/v7/
+-rw-r--r--   0 runner    (1001) docker     (122)      234 2023-04-06 12:06:28.000000 invenio-search-2.2.0/examples/data/v7/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 12:06:32.000000 invenio-search-2.2.0/examples/data/v7/demo/
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 12:06:32.000000 invenio-search-2.2.0/examples/data/v7/demo/authorities/
+-rw-r--r--   0 runner    (1001) docker     (122)      125 2023-04-06 12:06:28.000000 invenio-search-2.2.0/examples/data/v7/demo/authorities/authority-v1.0.0.json
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 12:06:32.000000 invenio-search-2.2.0/examples/data/v7/demo/bibliographic/
+-rw-r--r--   0 runner    (1001) docker     (122)      125 2023-04-06 12:06:28.000000 invenio-search-2.2.0/examples/data/v7/demo/bibliographic/bibliographic-v1.0.0.json
+-rw-r--r--   0 runner    (1001) docker     (122)      125 2023-04-06 12:06:28.000000 invenio-search-2.2.0/examples/data/v7/demo/default-v1.0.0.json
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 12:06:32.000000 invenio-search-2.2.0/invenio_search/
+-rw-r--r--   0 runner    (1001) docker     (122)    13171 2023-04-06 12:06:28.000000 invenio-search-2.2.0/invenio_search/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    10375 2023-04-06 12:06:28.000000 invenio-search-2.2.0/invenio_search/api.py
+-rw-r--r--   0 runner    (1001) docker     (122)     7357 2023-04-06 12:06:28.000000 invenio-search-2.2.0/invenio_search/cli.py
+-rw-r--r--   0 runner    (1001) docker     (122)     3947 2023-04-06 12:06:28.000000 invenio-search-2.2.0/invenio_search/config.py
+-rw-r--r--   0 runner    (1001) docker     (122)     3051 2023-04-06 12:06:28.000000 invenio-search-2.2.0/invenio_search/engine.py
+-rw-r--r--   0 runner    (1001) docker     (122)      488 2023-04-06 12:06:28.000000 invenio-search-2.2.0/invenio_search/errors.py
+-rw-r--r--   0 runner    (1001) docker     (122)    20716 2023-04-06 12:06:28.000000 invenio-search-2.2.0/invenio_search/ext.py
+-rw-r--r--   0 runner    (1001) docker     (122)      733 2023-04-06 12:06:28.000000 invenio-search-2.2.0/invenio_search/proxies.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2512 2023-04-06 12:06:28.000000 invenio-search-2.2.0/invenio_search/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 12:06:32.000000 invenio-search-2.2.0/invenio_search.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (122)     5883 2023-04-06 12:06:32.000000 invenio-search-2.2.0/invenio_search.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (122)     3757 2023-04-06 12:06:32.000000 invenio-search-2.2.0/invenio_search.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (122)        1 2023-04-06 12:06:32.000000 invenio-search-2.2.0/invenio_search.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (122)      138 2023-04-06 12:06:32.000000 invenio-search-2.2.0/invenio_search.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (122)        1 2023-04-06 12:06:32.000000 invenio-search-2.2.0/invenio_search.egg-info/not-zip-safe
+-rw-r--r--   0 runner    (1001) docker     (122)      414 2023-04-06 12:06:32.000000 invenio-search-2.2.0/invenio_search.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (122)       15 2023-04-06 12:06:32.000000 invenio-search-2.2.0/invenio_search.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (122)       91 2023-04-06 12:06:28.000000 invenio-search-2.2.0/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (122)      467 2023-04-06 12:06:28.000000 invenio-search-2.2.0/requirements-devel.txt
+-rwxr-xr-x   0 runner    (1001) docker     (122)      733 2023-04-06 12:06:28.000000 invenio-search-2.2.0/run-tests.sh
+-rw-r--r--   0 runner    (1001) docker     (122)     1627 2023-04-06 12:06:32.000000 invenio-search-2.2.0/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (122)      322 2023-04-06 12:06:28.000000 invenio-search-2.2.0/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 12:06:32.000000 invenio-search-2.2.0/tests/
+-rw-r--r--   0 runner    (1001) docker     (122)     1938 2023-04-06 12:06:28.000000 invenio-search-2.2.0/tests/conftest.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 12:06:32.000000 invenio-search-2.2.0/tests/mock_module/
+-rw-r--r--   0 runner    (1001) docker     (122)      291 2023-04-06 12:06:28.000000 invenio-search-2.2.0/tests/mock_module/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 12:06:32.000000 invenio-search-2.2.0/tests/mock_module/mappings/
+-rw-r--r--   0 runner    (1001) docker     (122)      295 2023-04-06 12:06:28.000000 invenio-search-2.2.0/tests/mock_module/mappings/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 12:06:32.000000 invenio-search-2.2.0/tests/mock_module/mappings/authors/
+-rw-r--r--   0 runner    (1001) docker     (122)       17 2023-04-06 12:06:28.000000 invenio-search-2.2.0/tests/mock_module/mappings/authors/authors-v1.0.0.json
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 12:06:32.000000 invenio-search-2.2.0/tests/mock_module/mappings/os-v1/
+-rw-r--r--   0 runner    (1001) docker     (122)      248 2023-04-06 12:06:28.000000 invenio-search-2.2.0/tests/mock_module/mappings/os-v1/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 12:06:32.000000 invenio-search-2.2.0/tests/mock_module/mappings/os-v1/authors/
+-rw-r--r--   0 runner    (1001) docker     (122)       17 2023-04-06 12:06:28.000000 invenio-search-2.2.0/tests/mock_module/mappings/os-v1/authors/authors-v1.0.0.json
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 12:06:32.000000 invenio-search-2.2.0/tests/mock_module/mappings/os-v1/records/
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 12:06:32.000000 invenio-search-2.2.0/tests/mock_module/mappings/os-v1/records/authorities/
+-rw-r--r--   0 runner    (1001) docker     (122)       17 2023-04-06 12:06:28.000000 invenio-search-2.2.0/tests/mock_module/mappings/os-v1/records/authorities/authority-v1.0.0.json
+-rw-r--r--   0 runner    (1001) docker     (122)        9 2023-04-06 12:06:28.000000 invenio-search-2.2.0/tests/mock_module/mappings/os-v1/records/authorities/notajson
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 12:06:32.000000 invenio-search-2.2.0/tests/mock_module/mappings/os-v1/records/bibliographic/
+-rw-r--r--   0 runner    (1001) docker     (122)       17 2023-04-06 12:06:28.000000 invenio-search-2.2.0/tests/mock_module/mappings/os-v1/records/bibliographic/bibliographic-v1.0.0.json
+-rw-r--r--   0 runner    (1001) docker     (122)       17 2023-04-06 12:06:28.000000 invenio-search-2.2.0/tests/mock_module/mappings/os-v1/records/default-v1.0.0.json
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 12:06:32.000000 invenio-search-2.2.0/tests/mock_module/mappings/os-v2/
+-rw-r--r--   0 runner    (1001) docker     (122)      248 2023-04-06 12:06:28.000000 invenio-search-2.2.0/tests/mock_module/mappings/os-v2/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 12:06:32.000000 invenio-search-2.2.0/tests/mock_module/mappings/os-v2/authors/
+-rw-r--r--   0 runner    (1001) docker     (122)       17 2023-04-06 12:06:28.000000 invenio-search-2.2.0/tests/mock_module/mappings/os-v2/authors/authors-v1.0.0.json
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 12:06:32.000000 invenio-search-2.2.0/tests/mock_module/mappings/os-v2/records/
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 12:06:32.000000 invenio-search-2.2.0/tests/mock_module/mappings/os-v2/records/authorities/
+-rw-r--r--   0 runner    (1001) docker     (122)       17 2023-04-06 12:06:28.000000 invenio-search-2.2.0/tests/mock_module/mappings/os-v2/records/authorities/authority-v1.0.0.json
+-rw-r--r--   0 runner    (1001) docker     (122)        9 2023-04-06 12:06:28.000000 invenio-search-2.2.0/tests/mock_module/mappings/os-v2/records/authorities/notajson
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 12:06:32.000000 invenio-search-2.2.0/tests/mock_module/mappings/os-v2/records/bibliographic/
+-rw-r--r--   0 runner    (1001) docker     (122)       17 2023-04-06 12:06:28.000000 invenio-search-2.2.0/tests/mock_module/mappings/os-v2/records/bibliographic/bibliographic-v1.0.0.json
+-rw-r--r--   0 runner    (1001) docker     (122)       17 2023-04-06 12:06:28.000000 invenio-search-2.2.0/tests/mock_module/mappings/os-v2/records/default-v1.0.0.json
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 12:06:32.000000 invenio-search-2.2.0/tests/mock_module/mappings/records/
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 12:06:32.000000 invenio-search-2.2.0/tests/mock_module/mappings/records/authorities/
+-rw-r--r--   0 runner    (1001) docker     (122)       17 2023-04-06 12:06:28.000000 invenio-search-2.2.0/tests/mock_module/mappings/records/authorities/authority-v1.0.0.json
+-rw-r--r--   0 runner    (1001) docker     (122)        9 2023-04-06 12:06:28.000000 invenio-search-2.2.0/tests/mock_module/mappings/records/authorities/notajson
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 12:06:32.000000 invenio-search-2.2.0/tests/mock_module/mappings/records/bibliographic/
+-rw-r--r--   0 runner    (1001) docker     (122)       17 2023-04-06 12:06:28.000000 invenio-search-2.2.0/tests/mock_module/mappings/records/bibliographic/bibliographic-v1.0.0.json
+-rw-r--r--   0 runner    (1001) docker     (122)       17 2023-04-06 12:06:28.000000 invenio-search-2.2.0/tests/mock_module/mappings/records/default-v1.0.0.json
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 12:06:32.000000 invenio-search-2.2.0/tests/mock_module/mappings/v7/
+-rw-r--r--   0 runner    (1001) docker     (122)      248 2023-04-06 12:06:28.000000 invenio-search-2.2.0/tests/mock_module/mappings/v7/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 12:06:32.000000 invenio-search-2.2.0/tests/mock_module/mappings/v7/authors/
+-rw-r--r--   0 runner    (1001) docker     (122)       17 2023-04-06 12:06:28.000000 invenio-search-2.2.0/tests/mock_module/mappings/v7/authors/authors-v1.0.0.json
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 12:06:32.000000 invenio-search-2.2.0/tests/mock_module/mappings/v7/records/
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 12:06:32.000000 invenio-search-2.2.0/tests/mock_module/mappings/v7/records/authorities/
+-rw-r--r--   0 runner    (1001) docker     (122)       17 2023-04-06 12:06:28.000000 invenio-search-2.2.0/tests/mock_module/mappings/v7/records/authorities/authority-v1.0.0.json
+-rw-r--r--   0 runner    (1001) docker     (122)        9 2023-04-06 12:06:28.000000 invenio-search-2.2.0/tests/mock_module/mappings/v7/records/authorities/notajson
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 12:06:32.000000 invenio-search-2.2.0/tests/mock_module/mappings/v7/records/bibliographic/
+-rw-r--r--   0 runner    (1001) docker     (122)       17 2023-04-06 12:06:28.000000 invenio-search-2.2.0/tests/mock_module/mappings/v7/records/bibliographic/bibliographic-v1.0.0.json
+-rw-r--r--   0 runner    (1001) docker     (122)       17 2023-04-06 12:06:28.000000 invenio-search-2.2.0/tests/mock_module/mappings/v7/records/default-v1.0.0.json
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 12:06:32.000000 invenio-search-2.2.0/tests/mock_module/templates/
+-rw-r--r--   0 runner    (1001) docker     (122)      295 2023-04-06 12:06:28.000000 invenio-search-2.2.0/tests/mock_module/templates/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 12:06:32.000000 invenio-search-2.2.0/tests/mock_module/templates/os-v1/
+-rw-r--r--   0 runner    (1001) docker     (122)      294 2023-04-06 12:06:28.000000 invenio-search-2.2.0/tests/mock_module/templates/os-v1/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)      872 2023-04-06 12:06:28.000000 invenio-search-2.2.0/tests/mock_module/templates/os-v1/record-view-os-v1.json
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 12:06:32.000000 invenio-search-2.2.0/tests/mock_module/templates/os-v2/
+-rw-r--r--   0 runner    (1001) docker     (122)      294 2023-04-06 12:06:28.000000 invenio-search-2.2.0/tests/mock_module/templates/os-v2/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)      872 2023-04-06 12:06:28.000000 invenio-search-2.2.0/tests/mock_module/templates/os-v2/record-view-os-v2.json
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 12:06:28.000000 invenio-search-2.2.0/tests/mock_module/templates/should_not_register.txt
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 12:06:32.000000 invenio-search-2.2.0/tests/mock_module/templates/v7/
+-rw-r--r--   0 runner    (1001) docker     (122)      286 2023-04-06 12:06:28.000000 invenio-search-2.2.0/tests/mock_module/templates/v7/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)      872 2023-04-06 12:06:28.000000 invenio-search-2.2.0/tests/mock_module/templates/v7/record-view-v7.json
+-rw-r--r--   0 runner    (1001) docker     (122)     6238 2023-04-06 12:06:28.000000 invenio-search-2.2.0/tests/test_cli.py
+-rw-r--r--   0 runner    (1001) docker     (122)    17382 2023-04-06 12:06:28.000000 invenio-search-2.2.0/tests/test_invenio_search.py
+-rw-r--r--   0 runner    (1001) docker     (122)     9087 2023-04-06 12:06:28.000000 invenio-search-2.2.0/tests/test_query.py
+-rw-r--r--   0 runner    (1001) docker     (122)      920 2023-04-06 12:06:28.000000 invenio-search-2.2.0/tests/test_utils.py
```

### Comparing `invenio-search-2.1.0/.editorconfig` & `invenio-search-2.2.0/.editorconfig`

 * *Files identical despite different names*

### Comparing `invenio-search-2.1.0/.github/workflows/pypi-publish.yml` & `invenio-search-2.2.0/.github/workflows/pypi-publish.yml`

 * *Files identical despite different names*

### Comparing `invenio-search-2.1.0/.github/workflows/tests.yml` & `invenio-search-2.2.0/.github/workflows/tests.yml`

 * *Files identical despite different names*

### Comparing `invenio-search-2.1.0/AUTHORS.rst` & `invenio-search-2.2.0/AUTHORS.rst`

 * *Files identical despite different names*

### Comparing `invenio-search-2.1.0/CHANGES.rst` & `invenio-search-2.2.0/CHANGES.rst`

 * *Files 1% similar despite different names*

```diff
@@ -4,14 +4,18 @@
 
     Invenio is free software; you can redistribute it and/or modify it
     under the terms of the MIT License; see LICENSE file for more details.
 
 Changes
 =======
 
+Version 2.2.0 (released 2023-04-06)
+
+- cli: adds interface for updating mappings
+
 Version 2.1.0 (released 2022-10-03)
 
 - Adds support for OpenSearch v2
 
 Version 2.0.0 (released 2022-09-22)
 
 - Removes Elasticsearch < v7
```

### Comparing `invenio-search-2.1.0/CONTRIBUTING.rst` & `invenio-search-2.2.0/CONTRIBUTING.rst`

 * *Files identical despite different names*

### Comparing `invenio-search-2.1.0/INSTALL.rst` & `invenio-search-2.2.0/INSTALL.rst`

 * *Files identical despite different names*

### Comparing `invenio-search-2.1.0/LICENSE` & `invenio-search-2.2.0/LICENSE`

 * *Files identical despite different names*

### Comparing `invenio-search-2.1.0/MANIFEST.in` & `invenio-search-2.2.0/MANIFEST.in`

 * *Files identical despite different names*

### Comparing `invenio-search-2.1.0/PKG-INFO` & `invenio-search-2.2.0/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: invenio-search
-Version: 2.1.0
+Version: 2.2.0
 Summary: "Invenio module for information retrieval."
 Home-page: https://github.com/inveniosoftware/invenio-search
 Author: CERN
 Author-email: info@inveniosoftware.org
 License: MIT
 Description: ..
             This file is part of Invenio.
@@ -48,14 +48,18 @@
         
             Invenio is free software; you can redistribute it and/or modify it
             under the terms of the MIT License; see LICENSE file for more details.
         
         Changes
         =======
         
+        Version 2.2.0 (released 2023-04-06)
+        
+        - cli: adds interface for updating mappings
+        
         Version 2.1.0 (released 2022-10-03)
         
         - Adds support for OpenSearch v2
         
         Version 2.0.0 (released 2022-09-22)
         
         - Removes Elasticsearch < v7
```

### Comparing `invenio-search-2.1.0/README.rst` & `invenio-search-2.2.0/README.rst`

 * *Files identical despite different names*

### Comparing `invenio-search-2.1.0/docs/Makefile` & `invenio-search-2.2.0/docs/Makefile`

 * *Files identical despite different names*

### Comparing `invenio-search-2.1.0/docs/conf.py` & `invenio-search-2.2.0/docs/conf.py`

 * *Files identical despite different names*

### Comparing `invenio-search-2.1.0/docs/configuration.rst` & `invenio-search-2.2.0/docs/configuration.rst`

 * *Files identical despite different names*

### Comparing `invenio-search-2.1.0/docs/index.rst` & `invenio-search-2.2.0/docs/index.rst`

 * *Files identical despite different names*

### Comparing `invenio-search-2.1.0/docs/make.bat` & `invenio-search-2.2.0/docs/make.bat`

 * *Files identical despite different names*

### Comparing `invenio-search-2.1.0/invenio_search/__init__.py` & `invenio-search-2.2.0/invenio_search/__init__.py`

 * *Files 0% similar despite different names*

```diff
@@ -411,15 +411,15 @@
     RecordsSearchV2,
     UnPrefixedRecordsSearch,
     UnPrefixedRecordsSearchV2,
 )
 from .ext import InvenioSearch
 from .proxies import current_search, current_search_client
 
-__version__ = "2.1.0"
+__version__ = "2.2.0"
 
 
 __all__ = (
     "__version__",
     "InvenioSearch",
     "RecordsSearch",
     "RecordsSearchV2",
```

### Comparing `invenio-search-2.1.0/invenio_search/api.py` & `invenio-search-2.2.0/invenio_search/api.py`

 * *Files identical despite different names*

### Comparing `invenio-search-2.1.0/invenio_search/cli.py` & `invenio-search-2.2.0/invenio_search/cli.py`

 * *Files 2% similar despite different names*

```diff
@@ -134,14 +134,24 @@
         body=json.load(body),
         ignore=[400] if force else None,
     )
     if verbose:
         click.echo(json.dumps(result))
 
 
+@index.command()
+@click.argument("index_name")
+@with_appcontext
+@search_version_check
+def update(index_name):
+    """Update mappings of existing index."""
+    current_search.update_mapping(index_name)
+    click.secho(f"Mapping of index {index_name} updated successfully.", fg="green")
+
+
 @index.command("list")
 @click.option("-a", "--only-active", is_flag=True, default=False)
 @click.option("--only-aliases", is_flag=True, default=False)
 @click.option("--verbose", is_flag=True, default=False)
 @with_appcontext
 def list_cmd(only_active, only_aliases, verbose):
     """List indices."""
```

### Comparing `invenio-search-2.1.0/invenio_search/config.py` & `invenio-search-2.2.0/invenio_search/config.py`

 * *Files identical despite different names*

### Comparing `invenio-search-2.1.0/invenio_search/engine.py` & `invenio-search-2.2.0/invenio_search/engine.py`

 * *Files identical despite different names*

### Comparing `invenio-search-2.1.0/invenio_search/ext.py` & `invenio-search-2.2.0/invenio_search/ext.py`

 * *Files 2% similar despite different names*

```diff
@@ -9,26 +9,27 @@
 
 """Invenio module for information retrieval."""
 
 import json
 import os
 import warnings
 
+import dictdiffer
 from pkg_resources import (
     iter_entry_points,
     resource_filename,
     resource_isdir,
     resource_listdir,
 )
 from werkzeug.utils import cached_property
 
 from . import config
 from .cli import index as index_cmd
-from .engine import ES, OS, SEARCH_DISTRIBUTION, SearchEngine, search
-from .errors import IndexAlreadyExistsError
+from .engine import ES, OS, SEARCH_DISTRIBUTION, SearchEngine, dsl, search
+from .errors import IndexAlreadyExistsError, NotAllowedMappingUpdate
 from .utils import (
     build_alias_name,
     build_index_from_parts,
     build_index_name,
     timestamp_suffix,
 )
 
@@ -402,14 +403,45 @@
             elif action["type"] == "create_alias":
                 yield action["alias"], self.client.indices.put_alias(
                     index=action["index"],
                     name=action["alias"],
                     ignore=ignore,
                 )
 
+    def update_mapping(self, index):
+        """Update mapping of the existing index."""
+        mapping_path = self.mappings[index]
+        index_alias_name = build_alias_name(index)
+
+        # get api returns only dicts
+        index_dict = self.client.indices.get(index_alias_name)
+        index_keys = list(index_dict.keys())
+
+        # make sure only one index exists
+        assert len(index_keys) == 1
+
+        full_index_name = index_keys[0]
+
+        old_mapping = index_dict[full_index_name]["mappings"]
+
+        # need to initialise Index class to use the .put_mapping API wrapper method
+        index_ = dsl.Index(full_index_name, using=self.client)
+
+        with open(mapping_path, "r") as body:
+            mapping = json.load(body)["mappings"]
+            changes = dictdiffer.diff(old_mapping, mapping)
+
+            # allow only additions to mappings (backwards compatibility is kept)
+            if all([change == "add" for change in changes]):
+                # raises 400 if the mapping cannot be updated
+                # (f.e. type changes or index needs to be closed)
+                index_.put_mapping(using=self.client, body=mapping)
+            else:
+                raise NotAllowedMappingUpdate(list(changes))
+
     def put_templates(self, ignore=None):
         """Yield tuple with registered template and response from client."""
         ignore = ignore or []
 
         def _replace_prefix(template_path, body):
             """Replace index prefix in template request body."""
             pattern = "__SEARCH_INDEX_PREFIX__"
```

### Comparing `invenio-search-2.1.0/invenio_search/proxies.py` & `invenio-search-2.2.0/invenio_search/proxies.py`

 * *Files identical despite different names*

### Comparing `invenio-search-2.1.0/invenio_search/utils.py` & `invenio-search-2.2.0/invenio_search/utils.py`

 * *Files identical despite different names*

### Comparing `invenio-search-2.1.0/invenio_search.egg-info/PKG-INFO` & `invenio-search-2.2.0/invenio_search.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: invenio-search
-Version: 2.1.0
+Version: 2.2.0
 Summary: "Invenio module for information retrieval."
 Home-page: https://github.com/inveniosoftware/invenio-search
 Author: CERN
 Author-email: info@inveniosoftware.org
 License: MIT
 Description: ..
             This file is part of Invenio.
@@ -48,14 +48,18 @@
         
             Invenio is free software; you can redistribute it and/or modify it
             under the terms of the MIT License; see LICENSE file for more details.
         
         Changes
         =======
         
+        Version 2.2.0 (released 2023-04-06)
+        
+        - cli: adds interface for updating mappings
+        
         Version 2.1.0 (released 2022-10-03)
         
         - Adds support for OpenSearch v2
         
         Version 2.0.0 (released 2022-09-22)
         
         - Removes Elasticsearch < v7
```

### Comparing `invenio-search-2.1.0/invenio_search.egg-info/SOURCES.txt` & `invenio-search-2.2.0/invenio_search.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `invenio-search-2.1.0/run-tests.sh` & `invenio-search-2.2.0/run-tests.sh`

 * *Files identical despite different names*

### Comparing `invenio-search-2.1.0/setup.cfg` & `invenio-search-2.2.0/setup.cfg`

 * *Files 4% similar despite different names*

```diff
@@ -15,14 +15,15 @@
 [options]
 include_package_data = True
 packages = find:
 python_requires = >=3.7
 zip_safe = False
 install_requires = 
 	invenio-base>=1.2.3,<2.0.0
+	dictdiffer>=0.9.0
 
 [options.extras_require]
 tests = 
 	pytest-black>=0.3.0
 	invenio-db[versioning]>=1.0.0,<2.0.0
 	mock>=1.3.0
 	pytest-invenio>=2.0.0,<3.0.0
```

### Comparing `invenio-search-2.1.0/tests/conftest.py` & `invenio-search-2.2.0/tests/conftest.py`

 * *Files identical despite different names*

### Comparing `invenio-search-2.1.0/tests/mock_module/templates/os-v1/record-view-os-v1.json` & `invenio-search-2.2.0/tests/mock_module/templates/os-v1/record-view-os-v1.json`

 * *Files identical despite different names*

### Comparing `invenio-search-2.1.0/tests/mock_module/templates/os-v2/record-view-os-v2.json` & `invenio-search-2.2.0/tests/mock_module/templates/os-v2/record-view-os-v2.json`

 * *Files identical despite different names*

### Comparing `invenio-search-2.1.0/tests/mock_module/templates/v7/record-view-v7.json` & `invenio-search-2.2.0/tests/mock_module/templates/v7/record-view-v7.json`

 * *Files identical despite different names*

### Comparing `invenio-search-2.1.0/tests/test_cli.py` & `invenio-search-2.2.0/tests/test_cli.py`

 * *Files identical despite different names*

### Comparing `invenio-search-2.1.0/tests/test_invenio_search.py` & `invenio-search-2.2.0/tests/test_invenio_search.py`

 * *Files 2% similar despite different names*

```diff
@@ -5,24 +5,24 @@
 # Copyright (C)      2022 TU Wien.
 #
 # Invenio is free software; you can redistribute it and/or modify it
 # under the terms of the MIT License; see LICENSE file for more details.
 
 
 """Module tests."""
-
+import json
 from collections import defaultdict
 
 import pytest
 from flask import Flask
 from mock import patch
 
 from invenio_search import InvenioSearch, current_search, current_search_client
 from invenio_search.engine import ES, SEARCH_DISTRIBUTION, search
-from invenio_search.errors import IndexAlreadyExistsError
+from invenio_search.errors import IndexAlreadyExistsError, NotAllowedMappingUpdate
 
 
 def _get_version():
     """Get filename postfix with current ES/OS version."""
     search_major_version = search.VERSION[0]
     version = "v{}" if SEARCH_DISTRIBUTION == ES else "os-v{}"
     return version.format(search_major_version)
@@ -103,15 +103,14 @@
     ext = InvenioSearch(app)
     ep_group = "test"
 
     def mock_entry_points_mappings(group=None):
         assert group == ep_group
 
         class ep(object):
-
             name = "records"
             module_name = "mock_module.mappings"
 
         yield ep
 
     assert len(ext.mappings) == 0
     with patch("invenio_search.ext.iter_entry_points", mock_entry_points_mappings):
@@ -444,7 +443,50 @@
     search.register_mappings("records", "mock_module.mappings")
     list(search.create(index_list=["authors-authors-v1.0.0", "records-default-v1.0.0"]))
     list(search.create(ignore_existing=True))
     assert (
         search.client.indices.exists("records-bibliographic-bibliographic-v1.0.0")
         is True
     )
+
+
+def test_update_mappings(app):
+    """Test if mapping gets correctly updated."""
+
+    mapping_path = "tests/mock_module/mappings/os-v2/records/default-v1.0.0.json"
+    current_search_client.indices.delete("*")
+
+    with open(mapping_path, "r") as body:
+        initial_mapping = json.load(body)
+
+    current_search_client.indices.create(
+        index="records-default-v1.0.0", body=initial_mapping
+    )
+    current_search.register_mappings("records", "mock_module.mappings")
+    assert current_search_client.indices.exists("records-default-v1.0.0") is True
+
+    try:
+        # change mapping
+        with open(mapping_path, "w") as mapping_file:
+            # test addition
+            new_mapping = {"mappings": {"properties": {"title": {"type": "keyword"}}}}
+            json_mapping = json.dumps(new_mapping)
+            mapping_file.write(json_mapping)
+
+        current_search.update_mapping("records-default-v1.0.0")
+
+        with open(mapping_path, "w") as mapping_file:
+            # test change
+            new_mapping = {"mappings": {"properties": {"abstract": {"type": "text"}}}}
+            json_mapping = json.dumps(new_mapping)
+            mapping_file.write(json_mapping)
+
+    except NotAllowedMappingUpdate:
+        with pytest.raises(NotAllowedMappingUpdate):
+            current_search.update_mapping("records-default-v1.0.0")
+
+    finally:
+        # recover initial state of the file
+        with open(mapping_path, "w") as mapping_file:
+            # reset test files
+            json_obj = json.dumps(initial_mapping)
+            mapping_file.write(json_obj)
```

### Comparing `invenio-search-2.1.0/tests/test_query.py` & `invenio-search-2.2.0/tests/test_query.py`

 * *Files identical despite different names*

### Comparing `invenio-search-2.1.0/tests/test_utils.py` & `invenio-search-2.2.0/tests/test_utils.py`

 * *Files identical despite different names*

