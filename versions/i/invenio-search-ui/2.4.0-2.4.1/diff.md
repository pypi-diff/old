# Comparing `tmp/invenio-search-ui-2.4.0.tar.gz` & `tmp/invenio-search-ui-2.4.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/invenio-search-ui-2.4.0.tar", last modified: Thu Mar  2 16:53:44 2023, max compression
+gzip compressed data, was "dist/invenio-search-ui-2.4.1.tar", last modified: Thu Apr  6 15:14:18 2023, max compression
```

## Comparing `invenio-search-ui-2.4.0.tar` & `invenio-search-ui-2.4.1.tar`

### file list

```diff
@@ -1,384 +1,384 @@
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/
--rw-r--r--   0 runner    (1001) docker     (122)      124 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/.dockerignore
--rw-r--r--   0 runner    (1001) docker     (122)      667 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/.editorconfig
--rw-r--r--   0 runner    (1001) docker     (122)       41 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/.git-blame-ignore-revs
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/.github/
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/.github/workflows/
--rw-r--r--   0 runner    (1001) docker     (122)      683 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/.github/workflows/pypi-publish.yml
--rw-r--r--   0 runner    (1001) docker     (122)     1839 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/.github/workflows/tests.yml
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/.tx/
--rw-r--r--   0 runner    (1001) docker     (122)     2385 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/.tx/config
--rw-r--r--   0 runner    (1001) docker     (122)      484 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/AUTHORS.rst
--rw-r--r--   0 runner    (1001) docker     (122)     3792 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/CHANGES.rst
--rw-r--r--   0 runner    (1001) docker     (122)     3734 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/CONTRIBUTING.rst
--rw-r--r--   0 runner    (1001) docker     (122)      356 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/INSTALL.rst
--rw-r--r--   0 runner    (1001) docker     (122)     1067 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/LICENSE
--rw-r--r--   0 runner    (1001) docker     (122)     1619 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (122)     6618 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (122)     1006 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/README.rst
--rw-r--r--   0 runner    (1001) docker     (122)      285 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/babel-js.ini
--rw-r--r--   0 runner    (1001) docker     (122)      499 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/babel.ini
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/docs/
--rw-r--r--   0 runner    (1001) docker     (122)     7453 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/docs/Makefile
--rw-r--r--   0 runner    (1001) docker     (122)      357 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/docs/api.rst
--rw-r--r--   0 runner    (1001) docker     (122)      247 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/docs/authors.rst
--rw-r--r--   0 runner    (1001) docker     (122)      247 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/docs/changes.rst
--rw-r--r--   0 runner    (1001) docker     (122)    10160 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/docs/conf.py
--rw-r--r--   0 runner    (1001) docker     (122)      302 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/docs/configuration.rst
--rw-r--r--   0 runner    (1001) docker     (122)      252 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/docs/contributing.rst
--rw-r--r--   0 runner    (1001) docker     (122)     6587 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/docs/customizing.rst
--rw-r--r--   0 runner    (1001) docker     (122)      844 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/docs/index.rst
--rw-r--r--   0 runner    (1001) docker     (122)      247 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/docs/installation.rst
--rw-r--r--   0 runner    (1001) docker     (122)      253 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/docs/license.rst
--rw-r--r--   0 runner    (1001) docker     (122)     7003 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/docs/make.bat
--rw-r--r--   0 runner    (1001) docker     (122)       17 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/docs/requirements.txt
--rw-r--r--   0 runner    (1001) docker     (122)      266 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/docs/usage.rst
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/
--rw-r--r--   0 runner    (1001) docker     (122)    12610 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/bootstrap3/
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/bootstrap3/js/
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/bootstrap3/js/invenio_search_ui/
--rw-r--r--   0 runner    (1001) docker     (122)      573 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/bootstrap3/js/invenio_search_ui/app.js
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/bootstrap3/scss/
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/bootstrap3/scss/invenio_search_ui/
--rw-r--r--   0 runner    (1001) docker     (122)      887 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/bootstrap3/scss/invenio_search_ui/search.scss
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/js/
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/js/invenio_search_ui/
--rw-r--r--   0 runner    (1001) docker     (122)      400 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/js/invenio_search_ui/app.js
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/js/invenio_search_ui/components/
--rw-r--r--   0 runner    (1001) docker     (122)     1637 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/js/invenio_search_ui/components/InvenioSearchPagination.js
--rw-r--r--   0 runner    (1001) docker     (122)     4925 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/js/invenio_search_ui/components/MultipleOptionsSearchBar.js
--rw-r--r--   0 runner    (1001) docker     (122)     3495 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/js/invenio_search_ui/components/Results.js
--rw-r--r--   0 runner    (1001) docker     (122)     1057 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/js/invenio_search_ui/components/ResultsGridItem.js
--rw-r--r--   0 runner    (1001) docker     (122)     1053 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/js/invenio_search_ui/components/ResultsListItem.js
--rw-r--r--   0 runner    (1001) docker     (122)     6957 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/js/invenio_search_ui/components/SearchApp.js
--rw-r--r--   0 runner    (1001) docker     (122)      790 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/js/invenio_search_ui/components/SearchAppFacets.js
--rw-r--r--   0 runner    (1001) docker     (122)      887 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/js/invenio_search_ui/components/SearchAppResultsPane.js
--rw-r--r--   0 runner    (1001) docker     (122)      947 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/js/invenio_search_ui/components/SearchBar.js
--rw-r--r--   0 runner    (1001) docker     (122)     3640 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/js/invenio_search_ui/components/SearchDropdowns.js
--rw-r--r--   0 runner    (1001) docker     (122)     1487 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/js/invenio_search_ui/components/SearchFilters.js
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/js/invenio_search_ui/components/common/
--rw-r--r--   0 runner    (1001) docker     (122)     6688 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/js/invenio_search_ui/components/common/facets.js
--rw-r--r--   0 runner    (1001) docker     (122)      311 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/js/invenio_search_ui/components/context.js
--rw-r--r--   0 runner    (1001) docker     (122)     1039 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/js/invenio_search_ui/components/index.js
--rw-r--r--   0 runner    (1001) docker     (122)      380 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/js/invenio_search_ui/defaultComponents.js
--rw-r--r--   0 runner    (1001) docker     (122)      367 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/js/invenio_search_ui/index.js
--rw-r--r--   0 runner    (1001) docker     (122)     2042 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/js/invenio_search_ui/util.js
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/
--rw-r--r--   0 runner    (1001) docker     (122)     1830 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/i18next-scanner.config.js
--rw-r--r--   0 runner    (1001) docker     (122)     1039 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/i18next.js
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/af/
--rw-r--r--   0 runner    (1001) docker     (122)      827 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/af/messages.po
--rw-r--r--   0 runner    (1001) docker     (122)      302 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/af/translations.json
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/ar/
--rw-r--r--   0 runner    (1001) docker     (122)     1293 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/ar/messages.po
--rw-r--r--   0 runner    (1001) docker     (122)      577 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/ar/translations.json
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/bg/
--rw-r--r--   0 runner    (1001) docker     (122)      837 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/bg/messages.po
--rw-r--r--   0 runner    (1001) docker     (122)      312 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/bg/translations.json
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/ca/
--rw-r--r--   0 runner    (1001) docker     (122)      937 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/ca/messages.po
--rw-r--r--   0 runner    (1001) docker     (122)      307 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/ca/translations.json
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/cs/
--rw-r--r--   0 runner    (1001) docker     (122)     1026 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/cs/messages.po
--rw-r--r--   0 runner    (1001) docker     (122)      312 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/cs/translations.json
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/da/
--rw-r--r--   0 runner    (1001) docker     (122)      824 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/da/messages.po
--rw-r--r--   0 runner    (1001) docker     (122)      302 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/da/translations.json
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/de/
--rw-r--r--   0 runner    (1001) docker     (122)     1090 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/de/messages.po
--rw-r--r--   0 runner    (1001) docker     (122)      441 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/de/translations.json
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/el/
--rw-r--r--   0 runner    (1001) docker     (122)      837 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/el/messages.po
--rw-r--r--   0 runner    (1001) docker     (122)      316 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/el/translations.json
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/en/
--rw-r--r--   0 runner    (1001) docker     (122)      316 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/en/messages.po
--rw-r--r--   0 runner    (1001) docker     (122)        2 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/en/translations.json
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/es/
--rw-r--r--   0 runner    (1001) docker     (122)     1180 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/es/messages.po
--rw-r--r--   0 runner    (1001) docker     (122)      493 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/es/translations.json
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/et/
--rw-r--r--   0 runner    (1001) docker     (122)     1101 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/et/messages.po
--rw-r--r--   0 runner    (1001) docker     (122)      465 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/et/translations.json
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/et_EE/
--rw-r--r--   0 runner    (1001) docker     (122)      842 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/et_EE/messages.po
--rw-r--r--   0 runner    (1001) docker     (122)      302 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/et_EE/translations.json
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/fa/
--rw-r--r--   0 runner    (1001) docker     (122)      836 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/fa/messages.po
--rw-r--r--   0 runner    (1001) docker     (122)      314 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/fa/translations.json
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/fr/
--rw-r--r--   0 runner    (1001) docker     (122)     1004 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/fr/messages.po
--rw-r--r--   0 runner    (1001) docker     (122)      306 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/fr/translations.json
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/gl/
--rw-r--r--   0 runner    (1001) docker     (122)      826 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/gl/messages.po
--rw-r--r--   0 runner    (1001) docker     (122)      302 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/gl/translations.json
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/hr/
--rw-r--r--   0 runner    (1001) docker     (122)      904 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/hr/messages.po
--rw-r--r--   0 runner    (1001) docker     (122)      308 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/hr/translations.json
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/hu/
--rw-r--r--   0 runner    (1001) docker     (122)     1105 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/hu/messages.po
--rw-r--r--   0 runner    (1001) docker     (122)      509 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/hu/translations.json
--rw-r--r--   0 runner    (1001) docker     (122)     2974 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/index.js
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/it/
--rw-r--r--   0 runner    (1001) docker     (122)      869 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/it/messages.po
--rw-r--r--   0 runner    (1001) docker     (122)      307 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/it/translations.json
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/ja/
--rw-r--r--   0 runner    (1001) docker     (122)      828 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/ja/messages.po
--rw-r--r--   0 runner    (1001) docker     (122)      311 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/ja/translations.json
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/ka/
--rw-r--r--   0 runner    (1001) docker     (122)      851 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/ka/messages.po
--rw-r--r--   0 runner    (1001) docker     (122)      329 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/ka/translations.json
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/lt/
--rw-r--r--   0 runner    (1001) docker     (122)      966 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/lt/messages.po
--rw-r--r--   0 runner    (1001) docker     (122)      309 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/lt/translations.json
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/no/
--rw-r--r--   0 runner    (1001) docker     (122)      832 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/no/messages.po
--rw-r--r--   0 runner    (1001) docker     (122)      307 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/no/translations.json
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/pl/
--rw-r--r--   0 runner    (1001) docker     (122)      975 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/pl/messages.po
--rw-r--r--   0 runner    (1001) docker     (122)      307 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/pl/translations.json
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/pt/
--rw-r--r--   0 runner    (1001) docker     (122)      884 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/pt/messages.po
--rw-r--r--   0 runner    (1001) docker     (122)      307 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/pt/translations.json
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/ro/
--rw-r--r--   0 runner    (1001) docker     (122)      867 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/ro/messages.po
--rw-r--r--   0 runner    (1001) docker     (122)      302 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/ro/translations.json
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/ru/
--rw-r--r--   0 runner    (1001) docker     (122)      975 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/ru/messages.po
--rw-r--r--   0 runner    (1001) docker     (122)      314 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/ru/translations.json
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/rw/
--rw-r--r--   0 runner    (1001) docker     (122)      829 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/rw/messages.po
--rw-r--r--   0 runner    (1001) docker     (122)      302 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/rw/translations.json
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/sk/
--rw-r--r--   0 runner    (1001) docker     (122)     1005 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/sk/messages.po
--rw-r--r--   0 runner    (1001) docker     (122)      307 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/sk/translations.json
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/sv/
--rw-r--r--   0 runner    (1001) docker     (122)     1037 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/sv/messages.po
--rw-r--r--   0 runner    (1001) docker     (122)      459 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/sv/translations.json
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/tr/
--rw-r--r--   0 runner    (1001) docker     (122)     1055 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/tr/messages.po
--rw-r--r--   0 runner    (1001) docker     (122)      370 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/tr/translations.json
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/uk/
--rw-r--r--   0 runner    (1001) docker     (122)     1065 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/uk/messages.po
--rw-r--r--   0 runner    (1001) docker     (122)      318 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/uk/translations.json
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/zh_CN/
--rw-r--r--   0 runner    (1001) docker     (122)     1006 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/zh_CN/messages.po
--rw-r--r--   0 runner    (1001) docker     (122)      413 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/zh_CN/translations.json
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/zh_TW/
--rw-r--r--   0 runner    (1001) docker     (122)      839 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/zh_TW/messages.po
--rw-r--r--   0 runner    (1001) docker     (122)      308 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/zh_TW/translations.json
--rw-r--r--   0 runner    (1001) docker     (122)   124321 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/package-lock.json
--rw-r--r--   0 runner    (1001) docker     (122)      944 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/package.json
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/scripts/
--rw-r--r--   0 runner    (1001) docker     (122)     1215 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/scripts/compileCatalog.js
--rw-r--r--   0 runner    (1001) docker     (122)      728 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/scripts/initCatalog.js
--rw-r--r--   0 runner    (1001) docker     (122)      863 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/translations.pot
--rw-r--r--   0 runner    (1001) docker     (122)     2110 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/config.py
--rw-r--r--   0 runner    (1001) docker     (122)     1263 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/ext.py
--rw-r--r--   0 runner    (1001) docker     (122)     8020 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/searchconfig.py
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/static/
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/static/templates/
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/static/templates/invenio_search_ui/
--rw-r--r--   0 runner    (1001) docker     (122)      521 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/static/templates/invenio_search_ui/count.html
--rw-r--r--   0 runner    (1001) docker     (122)      418 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/static/templates/invenio_search_ui/error.html
--rw-r--r--   0 runner    (1001) docker     (122)     2362 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/static/templates/invenio_search_ui/facets.html
--rw-r--r--   0 runner    (1001) docker     (122)      332 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/static/templates/invenio_search_ui/loading.html
--rw-r--r--   0 runner    (1001) docker     (122)     1386 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/static/templates/invenio_search_ui/pagination.html
--rw-r--r--   0 runner    (1001) docker     (122)      595 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/static/templates/invenio_search_ui/range.html
--rw-r--r--   0 runner    (1001) docker     (122)     1285 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/static/templates/invenio_search_ui/results.html
--rw-r--r--   0 runner    (1001) docker     (122)      788 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/static/templates/invenio_search_ui/searchbar.html
--rw-r--r--   0 runner    (1001) docker     (122)      499 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/static/templates/invenio_search_ui/selectbox.html
--rw-r--r--   0 runner    (1001) docker     (122)      471 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/static/templates/invenio_search_ui/togglebutton.html
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/templates/
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/templates/invenio_search_ui/
--rw-r--r--   0 runner    (1001) docker     (122)      543 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/templates/invenio_search_ui/header.html
--rw-r--r--   0 runner    (1001) docker     (122)     4885 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/templates/invenio_search_ui/search.html
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/templates/semantic-ui/
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/templates/semantic-ui/invenio_search_ui/
--rw-r--r--   0 runner    (1001) docker     (122)      691 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/templates/semantic-ui/invenio_search_ui/header.html
--rw-r--r--   0 runner    (1001) docker     (122)      744 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/templates/semantic-ui/invenio_search_ui/search.html
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/af/
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/af/LC_MESSAGES/
--rw-r--r--   0 runner    (1001) docker     (122)      799 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/af/LC_MESSAGES/messages-js.po
--rw-r--r--   0 runner    (1001) docker     (122)      519 2023-03-02 16:53:43.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/af/LC_MESSAGES/messages.mo
--rw-r--r--   0 runner    (1001) docker     (122)     1060 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/af/LC_MESSAGES/messages.po
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/ar/
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/ar/LC_MESSAGES/
--rw-r--r--   0 runner    (1001) docker     (122)      749 2023-03-02 16:53:43.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/ar/LC_MESSAGES/messages.mo
--rw-r--r--   0 runner    (1001) docker     (122)     1359 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/ar/LC_MESSAGES/messages.po
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/bg/
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/bg/LC_MESSAGES/
--rw-r--r--   0 runner    (1001) docker     (122)      799 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/bg/LC_MESSAGES/messages-js.po
--rw-r--r--   0 runner    (1001) docker     (122)      571 2023-03-02 16:53:43.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/bg/LC_MESSAGES/messages.mo
--rw-r--r--   0 runner    (1001) docker     (122)     1195 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/bg/LC_MESSAGES/messages.po
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/ca/
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/ca/LC_MESSAGES/
--rw-r--r--   0 runner    (1001) docker     (122)      797 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/ca/LC_MESSAGES/messages-js.po
--rw-r--r--   0 runner    (1001) docker     (122)      560 2023-03-02 16:53:43.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/ca/LC_MESSAGES/messages.mo
--rw-r--r--   0 runner    (1001) docker     (122)     1184 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/ca/LC_MESSAGES/messages.po
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/cs/
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/cs/LC_MESSAGES/
--rw-r--r--   0 runner    (1001) docker     (122)      822 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/cs/LC_MESSAGES/messages-js.po
--rw-r--r--   0 runner    (1001) docker     (122)      688 2023-03-02 16:53:43.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/cs/LC_MESSAGES/messages.mo
--rw-r--r--   0 runner    (1001) docker     (122)     1330 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/cs/LC_MESSAGES/messages.po
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/da/
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/da/LC_MESSAGES/
--rw-r--r--   0 runner    (1001) docker     (122)      796 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/da/LC_MESSAGES/messages-js.po
--rw-r--r--   0 runner    (1001) docker     (122)      516 2023-03-02 16:53:43.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/da/LC_MESSAGES/messages.mo
--rw-r--r--   0 runner    (1001) docker     (122)     1057 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/da/LC_MESSAGES/messages.po
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/de/
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/de/LC_MESSAGES/
--rw-r--r--   0 runner    (1001) docker     (122)      886 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/de/LC_MESSAGES/messages-js.po
--rw-r--r--   0 runner    (1001) docker     (122)      669 2023-03-02 16:53:43.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/de/LC_MESSAGES/messages.mo
--rw-r--r--   0 runner    (1001) docker     (122)     1295 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/de/LC_MESSAGES/messages.po
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/el/
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/el/LC_MESSAGES/
--rw-r--r--   0 runner    (1001) docker     (122)      795 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/el/LC_MESSAGES/messages-js.po
--rw-r--r--   0 runner    (1001) docker     (122)      607 2023-03-02 16:53:43.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/el/LC_MESSAGES/messages.mo
--rw-r--r--   0 runner    (1001) docker     (122)     1236 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/el/LC_MESSAGES/messages.po
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/es/
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/es/LC_MESSAGES/
--rw-r--r--   0 runner    (1001) docker     (122)      797 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/es/LC_MESSAGES/messages-js.po
--rw-r--r--   0 runner    (1001) docker     (122)      695 2023-03-02 16:53:43.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/es/LC_MESSAGES/messages.mo
--rw-r--r--   0 runner    (1001) docker     (122)     1307 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/es/LC_MESSAGES/messages.po
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/et/
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/et/LC_MESSAGES/
--rw-r--r--   0 runner    (1001) docker     (122)      656 2023-03-02 16:53:43.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/et/LC_MESSAGES/messages.mo
--rw-r--r--   0 runner    (1001) docker     (122)     1229 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/et/LC_MESSAGES/messages.po
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/et_EE/
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/et_EE/LC_MESSAGES/
--rw-r--r--   0 runner    (1001) docker     (122)      534 2023-03-02 16:53:43.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/et_EE/LC_MESSAGES/messages.mo
--rw-r--r--   0 runner    (1001) docker     (122)     1075 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/et_EE/LC_MESSAGES/messages.po
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/fa/
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/fa/LC_MESSAGES/
--rw-r--r--   0 runner    (1001) docker     (122)      564 2023-03-02 16:53:43.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/fa/LC_MESSAGES/messages.mo
--rw-r--r--   0 runner    (1001) docker     (122)     1188 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/fa/LC_MESSAGES/messages.po
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/fr/
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/fr/LC_MESSAGES/
--rw-r--r--   0 runner    (1001) docker     (122)      795 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/fr/LC_MESSAGES/messages-js.po
--rw-r--r--   0 runner    (1001) docker     (122)      656 2023-03-02 16:53:43.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/fr/LC_MESSAGES/messages.mo
--rw-r--r--   0 runner    (1001) docker     (122)     1254 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/fr/LC_MESSAGES/messages.po
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/gl/
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/gl/LC_MESSAGES/
--rw-r--r--   0 runner    (1001) docker     (122)      798 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/gl/LC_MESSAGES/messages-js.po
--rw-r--r--   0 runner    (1001) docker     (122)      518 2023-03-02 16:53:43.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/gl/LC_MESSAGES/messages.mo
--rw-r--r--   0 runner    (1001) docker     (122)     1059 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/gl/LC_MESSAGES/messages.po
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/hr/
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/hr/LC_MESSAGES/
--rw-r--r--   0 runner    (1001) docker     (122)      870 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/hr/LC_MESSAGES/messages-js.po
--rw-r--r--   0 runner    (1001) docker     (122)      637 2023-03-02 16:53:43.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/hr/LC_MESSAGES/messages.mo
--rw-r--r--   0 runner    (1001) docker     (122)     1261 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/hr/LC_MESSAGES/messages.po
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/hu/
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/hu/LC_MESSAGES/
--rw-r--r--   0 runner    (1001) docker     (122)      799 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/hu/LC_MESSAGES/messages-js.po
--rw-r--r--   0 runner    (1001) docker     (122)      644 2023-03-02 16:53:43.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/hu/LC_MESSAGES/messages.mo
--rw-r--r--   0 runner    (1001) docker     (122)     1234 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/hu/LC_MESSAGES/messages.po
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/it/
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/it/LC_MESSAGES/
--rw-r--r--   0 runner    (1001) docker     (122)      797 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/it/LC_MESSAGES/messages-js.po
--rw-r--r--   0 runner    (1001) docker     (122)      645 2023-03-02 16:53:43.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/it/LC_MESSAGES/messages.mo
--rw-r--r--   0 runner    (1001) docker     (122)     1243 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/it/LC_MESSAGES/messages.po
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/ja/
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/ja/LC_MESSAGES/
--rw-r--r--   0 runner    (1001) docker     (122)      791 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/ja/LC_MESSAGES/messages-js.po
--rw-r--r--   0 runner    (1001) docker     (122)      555 2023-03-02 16:53:43.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/ja/LC_MESSAGES/messages.mo
--rw-r--r--   0 runner    (1001) docker     (122)     1179 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/ja/LC_MESSAGES/messages.po
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/ka/
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/ka/LC_MESSAGES/
--rw-r--r--   0 runner    (1001) docker     (122)      791 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/ka/LC_MESSAGES/messages-js.po
--rw-r--r--   0 runner    (1001) docker     (122)      569 2023-03-02 16:53:43.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/ka/LC_MESSAGES/messages.mo
--rw-r--r--   0 runner    (1001) docker     (122)     1193 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/ka/LC_MESSAGES/messages.po
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/lt/
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/lt/LC_MESSAGES/
--rw-r--r--   0 runner    (1001) docker     (122)      697 2023-03-02 16:53:43.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/lt/LC_MESSAGES/messages.mo
--rw-r--r--   0 runner    (1001) docker     (122)     1321 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/lt/LC_MESSAGES/messages.po
--rw-r--r--   0 runner    (1001) docker     (122)      744 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/messages-js.pot
--rw-r--r--   0 runner    (1001) docker     (122)      994 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/messages.pot
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/no/
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/no/LC_MESSAGES/
--rw-r--r--   0 runner    (1001) docker     (122)      799 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/no/LC_MESSAGES/messages-js.po
--rw-r--r--   0 runner    (1001) docker     (122)      561 2023-03-02 16:53:43.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/no/LC_MESSAGES/messages.mo
--rw-r--r--   0 runner    (1001) docker     (122)     1185 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/no/LC_MESSAGES/messages.po
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/pl/
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/pl/LC_MESSAGES/
--rw-r--r--   0 runner    (1001) docker     (122)      854 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/pl/LC_MESSAGES/messages-js.po
--rw-r--r--   0 runner    (1001) docker     (122)      706 2023-03-02 16:53:43.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/pl/LC_MESSAGES/messages.mo
--rw-r--r--   0 runner    (1001) docker     (122)     1330 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/pl/LC_MESSAGES/messages.po
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/pt/
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/pt/LC_MESSAGES/
--rw-r--r--   0 runner    (1001) docker     (122)      800 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/pt/LC_MESSAGES/messages-js.po
--rw-r--r--   0 runner    (1001) docker     (122)      618 2023-03-02 16:53:43.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/pt/LC_MESSAGES/messages.mo
--rw-r--r--   0 runner    (1001) docker     (122)     1242 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/pt/LC_MESSAGES/messages.po
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/ro/
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/ro/LC_MESSAGES/
--rw-r--r--   0 runner    (1001) docker     (122)      839 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/ro/LC_MESSAGES/messages-js.po
--rw-r--r--   0 runner    (1001) docker     (122)      603 2023-03-02 16:53:43.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/ro/LC_MESSAGES/messages.mo
--rw-r--r--   0 runner    (1001) docker     (122)     1227 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/ro/LC_MESSAGES/messages.po
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/ru/
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/ru/LC_MESSAGES/
--rw-r--r--   0 runner    (1001) docker     (122)      935 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/ru/LC_MESSAGES/messages-js.po
--rw-r--r--   0 runner    (1001) docker     (122)      705 2023-03-02 16:53:43.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/ru/LC_MESSAGES/messages.mo
--rw-r--r--   0 runner    (1001) docker     (122)     1329 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/ru/LC_MESSAGES/messages.po
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/rw/
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/rw/LC_MESSAGES/
--rw-r--r--   0 runner    (1001) docker     (122)      801 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/rw/LC_MESSAGES/messages-js.po
--rw-r--r--   0 runner    (1001) docker     (122)      521 2023-03-02 16:53:43.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/rw/LC_MESSAGES/messages.mo
--rw-r--r--   0 runner    (1001) docker     (122)     1062 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/rw/LC_MESSAGES/messages.po
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/sk/
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/sk/LC_MESSAGES/
--rw-r--r--   0 runner    (1001) docker     (122)      823 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/sk/LC_MESSAGES/messages-js.po
--rw-r--r--   0 runner    (1001) docker     (122)      680 2023-03-02 16:53:43.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/sk/LC_MESSAGES/messages.mo
--rw-r--r--   0 runner    (1001) docker     (122)     1275 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/sk/LC_MESSAGES/messages.po
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/sv/
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/sv/LC_MESSAGES/
--rw-r--r--   0 runner    (1001) docker     (122)      797 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/sv/LC_MESSAGES/messages-js.po
--rw-r--r--   0 runner    (1001) docker     (122)      631 2023-03-02 16:53:43.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/sv/LC_MESSAGES/messages.mo
--rw-r--r--   0 runner    (1001) docker     (122)     1213 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/sv/LC_MESSAGES/messages.po
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/tr/
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/tr/LC_MESSAGES/
--rw-r--r--   0 runner    (1001) docker     (122)      629 2023-03-02 16:53:43.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/tr/LC_MESSAGES/messages.mo
--rw-r--r--   0 runner    (1001) docker     (122)     1302 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/tr/LC_MESSAGES/messages.po
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/uk/
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/uk/LC_MESSAGES/
--rw-r--r--   0 runner    (1001) docker     (122)      873 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/uk/LC_MESSAGES/messages-js.po
--rw-r--r--   0 runner    (1001) docker     (122)      789 2023-03-02 16:53:43.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/uk/LC_MESSAGES/messages.mo
--rw-r--r--   0 runner    (1001) docker     (122)     1413 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/uk/LC_MESSAGES/messages.po
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/zh_CN/
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/zh_CN/LC_MESSAGES/
--rw-r--r--   0 runner    (1001) docker     (122)      804 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/zh_CN/LC_MESSAGES/messages-js.po
--rw-r--r--   0 runner    (1001) docker     (122)      635 2023-03-02 16:53:43.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/zh_CN/LC_MESSAGES/messages.mo
--rw-r--r--   0 runner    (1001) docker     (122)     1179 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/zh_CN/LC_MESSAGES/messages.po
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/zh_TW/
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/zh_TW/LC_MESSAGES/
--rw-r--r--   0 runner    (1001) docker     (122)      805 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/zh_TW/LC_MESSAGES/messages-js.po
--rw-r--r--   0 runner    (1001) docker     (122)      569 2023-03-02 16:53:43.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/zh_TW/LC_MESSAGES/messages.mo
--rw-r--r--   0 runner    (1001) docker     (122)     1193 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/translations/zh_TW/LC_MESSAGES/messages.po
--rw-r--r--   0 runner    (1001) docker     (122)     8353 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/views.py
--rw-r--r--   0 runner    (1001) docker     (122)     2248 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/invenio_search_ui/webpack.py
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui.egg-info/
--rw-r--r--   0 runner    (1001) docker     (122)     6618 2023-03-02 16:53:43.000000 invenio-search-ui-2.4.0/invenio_search_ui.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (122)    16135 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/invenio_search_ui.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (122)        1 2023-03-02 16:53:43.000000 invenio-search-ui-2.4.0/invenio_search_ui.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (122)      301 2023-03-02 16:53:43.000000 invenio-search-ui-2.4.0/invenio_search_ui.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (122)        1 2023-03-02 16:53:43.000000 invenio-search-ui-2.4.0/invenio_search_ui.egg-info/not-zip-safe
--rw-r--r--   0 runner    (1001) docker     (122)      194 2023-03-02 16:53:43.000000 invenio-search-ui-2.4.0/invenio_search_ui.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (122)       18 2023-03-02 16:53:43.000000 invenio-search-ui-2.4.0/invenio_search_ui.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (122)      103 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (122)      721 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/requirements-devel.txt
--rwxr-xr-x   0 runner    (1001) docker     (122)      522 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/run-tests.sh
--rw-r--r--   0 runner    (1001) docker     (122)     2070 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (122)      273 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/tests/
--rw-r--r--   0 runner    (1001) docker     (122)     2537 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/tests/conftest.py
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/tests/templates/
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-02 16:53:44.000000 invenio-search-ui-2.4.0/tests/templates/invenio_search_ui/
--rw-r--r--   0 runner    (1001) docker     (122)      606 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/tests/templates/invenio_search_ui/base.html
--rw-r--r--   0 runner    (1001) docker     (122)      707 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/tests/templates/invenio_search_ui/base_header.html
--rw-r--r--   0 runner    (1001) docker     (122)      792 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/tests/test_app.py
--rw-r--r--   0 runner    (1001) docker     (122)     1637 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/tests/test_ng_templates.py
--rw-r--r--   0 runner    (1001) docker     (122)     2685 2023-03-02 16:53:34.000000 invenio-search-ui-2.4.0/tests/test_rsk_templates.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/
+-rw-r--r--   0 runner    (1001) docker     (122)      124 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/.dockerignore
+-rw-r--r--   0 runner    (1001) docker     (122)      667 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/.editorconfig
+-rw-r--r--   0 runner    (1001) docker     (122)       41 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/.git-blame-ignore-revs
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/.github/
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/.github/workflows/
+-rw-r--r--   0 runner    (1001) docker     (122)      683 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/.github/workflows/pypi-publish.yml
+-rw-r--r--   0 runner    (1001) docker     (122)     1839 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/.github/workflows/tests.yml
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/.tx/
+-rw-r--r--   0 runner    (1001) docker     (122)     2385 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/.tx/config
+-rw-r--r--   0 runner    (1001) docker     (122)      484 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/AUTHORS.rst
+-rw-r--r--   0 runner    (1001) docker     (122)     3863 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/CHANGES.rst
+-rw-r--r--   0 runner    (1001) docker     (122)     3734 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/CONTRIBUTING.rst
+-rw-r--r--   0 runner    (1001) docker     (122)      356 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/INSTALL.rst
+-rw-r--r--   0 runner    (1001) docker     (122)     1067 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (122)     1619 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (122)     6721 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (122)     1006 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/README.rst
+-rw-r--r--   0 runner    (1001) docker     (122)      285 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/babel-js.ini
+-rw-r--r--   0 runner    (1001) docker     (122)      499 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/babel.ini
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/docs/
+-rw-r--r--   0 runner    (1001) docker     (122)     7453 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/docs/Makefile
+-rw-r--r--   0 runner    (1001) docker     (122)      357 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/docs/api.rst
+-rw-r--r--   0 runner    (1001) docker     (122)      247 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/docs/authors.rst
+-rw-r--r--   0 runner    (1001) docker     (122)      247 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/docs/changes.rst
+-rw-r--r--   0 runner    (1001) docker     (122)    10160 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/docs/conf.py
+-rw-r--r--   0 runner    (1001) docker     (122)      302 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/docs/configuration.rst
+-rw-r--r--   0 runner    (1001) docker     (122)      252 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/docs/contributing.rst
+-rw-r--r--   0 runner    (1001) docker     (122)     6587 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/docs/customizing.rst
+-rw-r--r--   0 runner    (1001) docker     (122)      844 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/docs/index.rst
+-rw-r--r--   0 runner    (1001) docker     (122)      247 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/docs/installation.rst
+-rw-r--r--   0 runner    (1001) docker     (122)      253 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/docs/license.rst
+-rw-r--r--   0 runner    (1001) docker     (122)     7003 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/docs/make.bat
+-rw-r--r--   0 runner    (1001) docker     (122)       17 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/docs/requirements.txt
+-rw-r--r--   0 runner    (1001) docker     (122)      266 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/docs/usage.rst
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/
+-rw-r--r--   0 runner    (1001) docker     (122)    12610 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/bootstrap3/
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/bootstrap3/js/
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/bootstrap3/js/invenio_search_ui/
+-rw-r--r--   0 runner    (1001) docker     (122)      573 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/bootstrap3/js/invenio_search_ui/app.js
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/bootstrap3/scss/
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/bootstrap3/scss/invenio_search_ui/
+-rw-r--r--   0 runner    (1001) docker     (122)      887 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/bootstrap3/scss/invenio_search_ui/search.scss
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/js/
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/js/invenio_search_ui/
+-rw-r--r--   0 runner    (1001) docker     (122)      400 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/js/invenio_search_ui/app.js
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/js/invenio_search_ui/components/
+-rw-r--r--   0 runner    (1001) docker     (122)     1724 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/js/invenio_search_ui/components/InvenioSearchPagination.js
+-rw-r--r--   0 runner    (1001) docker     (122)     4925 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/js/invenio_search_ui/components/MultipleOptionsSearchBar.js
+-rw-r--r--   0 runner    (1001) docker     (122)     3495 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/js/invenio_search_ui/components/Results.js
+-rw-r--r--   0 runner    (1001) docker     (122)     1057 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/js/invenio_search_ui/components/ResultsGridItem.js
+-rw-r--r--   0 runner    (1001) docker     (122)     1053 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/js/invenio_search_ui/components/ResultsListItem.js
+-rw-r--r--   0 runner    (1001) docker     (122)     6957 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/js/invenio_search_ui/components/SearchApp.js
+-rw-r--r--   0 runner    (1001) docker     (122)      790 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/js/invenio_search_ui/components/SearchAppFacets.js
+-rw-r--r--   0 runner    (1001) docker     (122)      887 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/js/invenio_search_ui/components/SearchAppResultsPane.js
+-rw-r--r--   0 runner    (1001) docker     (122)      947 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/js/invenio_search_ui/components/SearchBar.js
+-rw-r--r--   0 runner    (1001) docker     (122)     3640 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/js/invenio_search_ui/components/SearchDropdowns.js
+-rw-r--r--   0 runner    (1001) docker     (122)     1487 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/js/invenio_search_ui/components/SearchFilters.js
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/js/invenio_search_ui/components/common/
+-rw-r--r--   0 runner    (1001) docker     (122)     6688 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/js/invenio_search_ui/components/common/facets.js
+-rw-r--r--   0 runner    (1001) docker     (122)      311 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/js/invenio_search_ui/components/context.js
+-rw-r--r--   0 runner    (1001) docker     (122)     1039 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/js/invenio_search_ui/components/index.js
+-rw-r--r--   0 runner    (1001) docker     (122)      380 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/js/invenio_search_ui/defaultComponents.js
+-rw-r--r--   0 runner    (1001) docker     (122)      367 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/js/invenio_search_ui/index.js
+-rw-r--r--   0 runner    (1001) docker     (122)     2042 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/js/invenio_search_ui/util.js
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/
+-rw-r--r--   0 runner    (1001) docker     (122)     1830 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/i18next-scanner.config.js
+-rw-r--r--   0 runner    (1001) docker     (122)     1039 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/i18next.js
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/af/
+-rw-r--r--   0 runner    (1001) docker     (122)      827 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/af/messages.po
+-rw-r--r--   0 runner    (1001) docker     (122)      302 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/af/translations.json
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/ar/
+-rw-r--r--   0 runner    (1001) docker     (122)     1293 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/ar/messages.po
+-rw-r--r--   0 runner    (1001) docker     (122)      577 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/ar/translations.json
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/bg/
+-rw-r--r--   0 runner    (1001) docker     (122)      837 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/bg/messages.po
+-rw-r--r--   0 runner    (1001) docker     (122)      312 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/bg/translations.json
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/ca/
+-rw-r--r--   0 runner    (1001) docker     (122)      937 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/ca/messages.po
+-rw-r--r--   0 runner    (1001) docker     (122)      307 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/ca/translations.json
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/cs/
+-rw-r--r--   0 runner    (1001) docker     (122)     1026 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/cs/messages.po
+-rw-r--r--   0 runner    (1001) docker     (122)      312 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/cs/translations.json
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/da/
+-rw-r--r--   0 runner    (1001) docker     (122)      824 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/da/messages.po
+-rw-r--r--   0 runner    (1001) docker     (122)      302 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/da/translations.json
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/de/
+-rw-r--r--   0 runner    (1001) docker     (122)     1090 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/de/messages.po
+-rw-r--r--   0 runner    (1001) docker     (122)      441 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/de/translations.json
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/el/
+-rw-r--r--   0 runner    (1001) docker     (122)      837 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/el/messages.po
+-rw-r--r--   0 runner    (1001) docker     (122)      316 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/el/translations.json
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/en/
+-rw-r--r--   0 runner    (1001) docker     (122)      316 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/en/messages.po
+-rw-r--r--   0 runner    (1001) docker     (122)        2 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/en/translations.json
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/es/
+-rw-r--r--   0 runner    (1001) docker     (122)     1180 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/es/messages.po
+-rw-r--r--   0 runner    (1001) docker     (122)      493 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/es/translations.json
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/et/
+-rw-r--r--   0 runner    (1001) docker     (122)     1101 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/et/messages.po
+-rw-r--r--   0 runner    (1001) docker     (122)      465 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/et/translations.json
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/et_EE/
+-rw-r--r--   0 runner    (1001) docker     (122)      842 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/et_EE/messages.po
+-rw-r--r--   0 runner    (1001) docker     (122)      302 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/et_EE/translations.json
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/fa/
+-rw-r--r--   0 runner    (1001) docker     (122)      836 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/fa/messages.po
+-rw-r--r--   0 runner    (1001) docker     (122)      314 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/fa/translations.json
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/fr/
+-rw-r--r--   0 runner    (1001) docker     (122)     1004 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/fr/messages.po
+-rw-r--r--   0 runner    (1001) docker     (122)      306 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/fr/translations.json
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/gl/
+-rw-r--r--   0 runner    (1001) docker     (122)      826 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/gl/messages.po
+-rw-r--r--   0 runner    (1001) docker     (122)      302 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/gl/translations.json
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/hr/
+-rw-r--r--   0 runner    (1001) docker     (122)      904 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/hr/messages.po
+-rw-r--r--   0 runner    (1001) docker     (122)      308 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/hr/translations.json
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/hu/
+-rw-r--r--   0 runner    (1001) docker     (122)     1105 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/hu/messages.po
+-rw-r--r--   0 runner    (1001) docker     (122)      509 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/hu/translations.json
+-rw-r--r--   0 runner    (1001) docker     (122)     2974 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/index.js
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/it/
+-rw-r--r--   0 runner    (1001) docker     (122)      869 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/it/messages.po
+-rw-r--r--   0 runner    (1001) docker     (122)      307 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/it/translations.json
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/ja/
+-rw-r--r--   0 runner    (1001) docker     (122)      828 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/ja/messages.po
+-rw-r--r--   0 runner    (1001) docker     (122)      311 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/ja/translations.json
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/ka/
+-rw-r--r--   0 runner    (1001) docker     (122)      851 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/ka/messages.po
+-rw-r--r--   0 runner    (1001) docker     (122)      329 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/ka/translations.json
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/lt/
+-rw-r--r--   0 runner    (1001) docker     (122)      966 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/lt/messages.po
+-rw-r--r--   0 runner    (1001) docker     (122)      309 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/lt/translations.json
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/no/
+-rw-r--r--   0 runner    (1001) docker     (122)      832 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/no/messages.po
+-rw-r--r--   0 runner    (1001) docker     (122)      307 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/no/translations.json
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/pl/
+-rw-r--r--   0 runner    (1001) docker     (122)      975 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/pl/messages.po
+-rw-r--r--   0 runner    (1001) docker     (122)      307 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/pl/translations.json
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/pt/
+-rw-r--r--   0 runner    (1001) docker     (122)      884 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/pt/messages.po
+-rw-r--r--   0 runner    (1001) docker     (122)      307 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/pt/translations.json
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/ro/
+-rw-r--r--   0 runner    (1001) docker     (122)      867 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/ro/messages.po
+-rw-r--r--   0 runner    (1001) docker     (122)      302 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/ro/translations.json
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/ru/
+-rw-r--r--   0 runner    (1001) docker     (122)      975 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/ru/messages.po
+-rw-r--r--   0 runner    (1001) docker     (122)      314 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/ru/translations.json
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/rw/
+-rw-r--r--   0 runner    (1001) docker     (122)      829 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/rw/messages.po
+-rw-r--r--   0 runner    (1001) docker     (122)      302 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/rw/translations.json
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/sk/
+-rw-r--r--   0 runner    (1001) docker     (122)     1005 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/sk/messages.po
+-rw-r--r--   0 runner    (1001) docker     (122)      307 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/sk/translations.json
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/sv/
+-rw-r--r--   0 runner    (1001) docker     (122)     1037 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/sv/messages.po
+-rw-r--r--   0 runner    (1001) docker     (122)      459 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/sv/translations.json
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/tr/
+-rw-r--r--   0 runner    (1001) docker     (122)     1055 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/tr/messages.po
+-rw-r--r--   0 runner    (1001) docker     (122)      370 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/tr/translations.json
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/uk/
+-rw-r--r--   0 runner    (1001) docker     (122)     1065 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/uk/messages.po
+-rw-r--r--   0 runner    (1001) docker     (122)      318 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/uk/translations.json
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/zh_CN/
+-rw-r--r--   0 runner    (1001) docker     (122)     1006 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/zh_CN/messages.po
+-rw-r--r--   0 runner    (1001) docker     (122)      413 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/zh_CN/translations.json
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/zh_TW/
+-rw-r--r--   0 runner    (1001) docker     (122)      839 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/zh_TW/messages.po
+-rw-r--r--   0 runner    (1001) docker     (122)      308 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/zh_TW/translations.json
+-rw-r--r--   0 runner    (1001) docker     (122)   124321 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/package-lock.json
+-rw-r--r--   0 runner    (1001) docker     (122)      944 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/package.json
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/scripts/
+-rw-r--r--   0 runner    (1001) docker     (122)     1215 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/scripts/compileCatalog.js
+-rw-r--r--   0 runner    (1001) docker     (122)      728 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/scripts/initCatalog.js
+-rw-r--r--   0 runner    (1001) docker     (122)      863 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/translations.pot
+-rw-r--r--   0 runner    (1001) docker     (122)     2110 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/config.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1263 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/ext.py
+-rw-r--r--   0 runner    (1001) docker     (122)     8202 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/searchconfig.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/static/
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/static/templates/
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/static/templates/invenio_search_ui/
+-rw-r--r--   0 runner    (1001) docker     (122)      521 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/static/templates/invenio_search_ui/count.html
+-rw-r--r--   0 runner    (1001) docker     (122)      418 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/static/templates/invenio_search_ui/error.html
+-rw-r--r--   0 runner    (1001) docker     (122)     2362 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/static/templates/invenio_search_ui/facets.html
+-rw-r--r--   0 runner    (1001) docker     (122)      332 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/static/templates/invenio_search_ui/loading.html
+-rw-r--r--   0 runner    (1001) docker     (122)     1386 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/static/templates/invenio_search_ui/pagination.html
+-rw-r--r--   0 runner    (1001) docker     (122)      595 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/static/templates/invenio_search_ui/range.html
+-rw-r--r--   0 runner    (1001) docker     (122)     1285 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/static/templates/invenio_search_ui/results.html
+-rw-r--r--   0 runner    (1001) docker     (122)      788 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/static/templates/invenio_search_ui/searchbar.html
+-rw-r--r--   0 runner    (1001) docker     (122)      499 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/static/templates/invenio_search_ui/selectbox.html
+-rw-r--r--   0 runner    (1001) docker     (122)      471 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/static/templates/invenio_search_ui/togglebutton.html
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/templates/
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/templates/invenio_search_ui/
+-rw-r--r--   0 runner    (1001) docker     (122)      543 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/templates/invenio_search_ui/header.html
+-rw-r--r--   0 runner    (1001) docker     (122)     4885 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/templates/invenio_search_ui/search.html
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/templates/semantic-ui/
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/templates/semantic-ui/invenio_search_ui/
+-rw-r--r--   0 runner    (1001) docker     (122)      691 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/templates/semantic-ui/invenio_search_ui/header.html
+-rw-r--r--   0 runner    (1001) docker     (122)      744 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/templates/semantic-ui/invenio_search_ui/search.html
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/af/
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/af/LC_MESSAGES/
+-rw-r--r--   0 runner    (1001) docker     (122)      799 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/af/LC_MESSAGES/messages-js.po
+-rw-r--r--   0 runner    (1001) docker     (122)      519 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/af/LC_MESSAGES/messages.mo
+-rw-r--r--   0 runner    (1001) docker     (122)     1060 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/af/LC_MESSAGES/messages.po
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/ar/
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/ar/LC_MESSAGES/
+-rw-r--r--   0 runner    (1001) docker     (122)      749 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/ar/LC_MESSAGES/messages.mo
+-rw-r--r--   0 runner    (1001) docker     (122)     1359 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/ar/LC_MESSAGES/messages.po
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/bg/
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/bg/LC_MESSAGES/
+-rw-r--r--   0 runner    (1001) docker     (122)      799 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/bg/LC_MESSAGES/messages-js.po
+-rw-r--r--   0 runner    (1001) docker     (122)      571 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/bg/LC_MESSAGES/messages.mo
+-rw-r--r--   0 runner    (1001) docker     (122)     1195 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/bg/LC_MESSAGES/messages.po
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/ca/
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/ca/LC_MESSAGES/
+-rw-r--r--   0 runner    (1001) docker     (122)      797 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/ca/LC_MESSAGES/messages-js.po
+-rw-r--r--   0 runner    (1001) docker     (122)      560 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/ca/LC_MESSAGES/messages.mo
+-rw-r--r--   0 runner    (1001) docker     (122)     1184 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/ca/LC_MESSAGES/messages.po
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/cs/
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/cs/LC_MESSAGES/
+-rw-r--r--   0 runner    (1001) docker     (122)      822 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/cs/LC_MESSAGES/messages-js.po
+-rw-r--r--   0 runner    (1001) docker     (122)      688 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/cs/LC_MESSAGES/messages.mo
+-rw-r--r--   0 runner    (1001) docker     (122)     1330 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/cs/LC_MESSAGES/messages.po
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/da/
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/da/LC_MESSAGES/
+-rw-r--r--   0 runner    (1001) docker     (122)      796 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/da/LC_MESSAGES/messages-js.po
+-rw-r--r--   0 runner    (1001) docker     (122)      516 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/da/LC_MESSAGES/messages.mo
+-rw-r--r--   0 runner    (1001) docker     (122)     1057 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/da/LC_MESSAGES/messages.po
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/de/
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/de/LC_MESSAGES/
+-rw-r--r--   0 runner    (1001) docker     (122)      886 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/de/LC_MESSAGES/messages-js.po
+-rw-r--r--   0 runner    (1001) docker     (122)      669 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/de/LC_MESSAGES/messages.mo
+-rw-r--r--   0 runner    (1001) docker     (122)     1295 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/de/LC_MESSAGES/messages.po
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/el/
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/el/LC_MESSAGES/
+-rw-r--r--   0 runner    (1001) docker     (122)      795 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/el/LC_MESSAGES/messages-js.po
+-rw-r--r--   0 runner    (1001) docker     (122)      607 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/el/LC_MESSAGES/messages.mo
+-rw-r--r--   0 runner    (1001) docker     (122)     1236 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/el/LC_MESSAGES/messages.po
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/es/
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/es/LC_MESSAGES/
+-rw-r--r--   0 runner    (1001) docker     (122)      797 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/es/LC_MESSAGES/messages-js.po
+-rw-r--r--   0 runner    (1001) docker     (122)      695 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/es/LC_MESSAGES/messages.mo
+-rw-r--r--   0 runner    (1001) docker     (122)     1307 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/es/LC_MESSAGES/messages.po
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/et/
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/et/LC_MESSAGES/
+-rw-r--r--   0 runner    (1001) docker     (122)      656 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/et/LC_MESSAGES/messages.mo
+-rw-r--r--   0 runner    (1001) docker     (122)     1229 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/et/LC_MESSAGES/messages.po
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/et_EE/
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/et_EE/LC_MESSAGES/
+-rw-r--r--   0 runner    (1001) docker     (122)      534 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/et_EE/LC_MESSAGES/messages.mo
+-rw-r--r--   0 runner    (1001) docker     (122)     1075 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/et_EE/LC_MESSAGES/messages.po
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/fa/
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/fa/LC_MESSAGES/
+-rw-r--r--   0 runner    (1001) docker     (122)      564 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/fa/LC_MESSAGES/messages.mo
+-rw-r--r--   0 runner    (1001) docker     (122)     1188 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/fa/LC_MESSAGES/messages.po
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/fr/
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/fr/LC_MESSAGES/
+-rw-r--r--   0 runner    (1001) docker     (122)      795 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/fr/LC_MESSAGES/messages-js.po
+-rw-r--r--   0 runner    (1001) docker     (122)      656 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/fr/LC_MESSAGES/messages.mo
+-rw-r--r--   0 runner    (1001) docker     (122)     1254 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/fr/LC_MESSAGES/messages.po
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/gl/
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/gl/LC_MESSAGES/
+-rw-r--r--   0 runner    (1001) docker     (122)      798 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/gl/LC_MESSAGES/messages-js.po
+-rw-r--r--   0 runner    (1001) docker     (122)      518 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/gl/LC_MESSAGES/messages.mo
+-rw-r--r--   0 runner    (1001) docker     (122)     1059 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/gl/LC_MESSAGES/messages.po
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/hr/
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/hr/LC_MESSAGES/
+-rw-r--r--   0 runner    (1001) docker     (122)      870 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/hr/LC_MESSAGES/messages-js.po
+-rw-r--r--   0 runner    (1001) docker     (122)      637 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/hr/LC_MESSAGES/messages.mo
+-rw-r--r--   0 runner    (1001) docker     (122)     1261 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/hr/LC_MESSAGES/messages.po
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/hu/
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/hu/LC_MESSAGES/
+-rw-r--r--   0 runner    (1001) docker     (122)      799 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/hu/LC_MESSAGES/messages-js.po
+-rw-r--r--   0 runner    (1001) docker     (122)      644 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/hu/LC_MESSAGES/messages.mo
+-rw-r--r--   0 runner    (1001) docker     (122)     1234 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/hu/LC_MESSAGES/messages.po
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/it/
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/it/LC_MESSAGES/
+-rw-r--r--   0 runner    (1001) docker     (122)      797 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/it/LC_MESSAGES/messages-js.po
+-rw-r--r--   0 runner    (1001) docker     (122)      645 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/it/LC_MESSAGES/messages.mo
+-rw-r--r--   0 runner    (1001) docker     (122)     1243 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/it/LC_MESSAGES/messages.po
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/ja/
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/ja/LC_MESSAGES/
+-rw-r--r--   0 runner    (1001) docker     (122)      791 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/ja/LC_MESSAGES/messages-js.po
+-rw-r--r--   0 runner    (1001) docker     (122)      555 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/ja/LC_MESSAGES/messages.mo
+-rw-r--r--   0 runner    (1001) docker     (122)     1179 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/ja/LC_MESSAGES/messages.po
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/ka/
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/ka/LC_MESSAGES/
+-rw-r--r--   0 runner    (1001) docker     (122)      791 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/ka/LC_MESSAGES/messages-js.po
+-rw-r--r--   0 runner    (1001) docker     (122)      569 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/ka/LC_MESSAGES/messages.mo
+-rw-r--r--   0 runner    (1001) docker     (122)     1193 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/ka/LC_MESSAGES/messages.po
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/lt/
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/lt/LC_MESSAGES/
+-rw-r--r--   0 runner    (1001) docker     (122)      697 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/lt/LC_MESSAGES/messages.mo
+-rw-r--r--   0 runner    (1001) docker     (122)     1321 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/lt/LC_MESSAGES/messages.po
+-rw-r--r--   0 runner    (1001) docker     (122)      744 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/messages-js.pot
+-rw-r--r--   0 runner    (1001) docker     (122)      994 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/messages.pot
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/no/
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/no/LC_MESSAGES/
+-rw-r--r--   0 runner    (1001) docker     (122)      799 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/no/LC_MESSAGES/messages-js.po
+-rw-r--r--   0 runner    (1001) docker     (122)      561 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/no/LC_MESSAGES/messages.mo
+-rw-r--r--   0 runner    (1001) docker     (122)     1185 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/no/LC_MESSAGES/messages.po
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/pl/
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/pl/LC_MESSAGES/
+-rw-r--r--   0 runner    (1001) docker     (122)      854 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/pl/LC_MESSAGES/messages-js.po
+-rw-r--r--   0 runner    (1001) docker     (122)      706 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/pl/LC_MESSAGES/messages.mo
+-rw-r--r--   0 runner    (1001) docker     (122)     1330 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/pl/LC_MESSAGES/messages.po
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/pt/
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/pt/LC_MESSAGES/
+-rw-r--r--   0 runner    (1001) docker     (122)      800 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/pt/LC_MESSAGES/messages-js.po
+-rw-r--r--   0 runner    (1001) docker     (122)      618 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/pt/LC_MESSAGES/messages.mo
+-rw-r--r--   0 runner    (1001) docker     (122)     1242 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/pt/LC_MESSAGES/messages.po
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/ro/
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/ro/LC_MESSAGES/
+-rw-r--r--   0 runner    (1001) docker     (122)      839 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/ro/LC_MESSAGES/messages-js.po
+-rw-r--r--   0 runner    (1001) docker     (122)      603 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/ro/LC_MESSAGES/messages.mo
+-rw-r--r--   0 runner    (1001) docker     (122)     1227 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/ro/LC_MESSAGES/messages.po
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/ru/
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/ru/LC_MESSAGES/
+-rw-r--r--   0 runner    (1001) docker     (122)      935 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/ru/LC_MESSAGES/messages-js.po
+-rw-r--r--   0 runner    (1001) docker     (122)      705 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/ru/LC_MESSAGES/messages.mo
+-rw-r--r--   0 runner    (1001) docker     (122)     1329 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/ru/LC_MESSAGES/messages.po
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/rw/
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/rw/LC_MESSAGES/
+-rw-r--r--   0 runner    (1001) docker     (122)      801 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/rw/LC_MESSAGES/messages-js.po
+-rw-r--r--   0 runner    (1001) docker     (122)      521 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/rw/LC_MESSAGES/messages.mo
+-rw-r--r--   0 runner    (1001) docker     (122)     1062 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/rw/LC_MESSAGES/messages.po
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/sk/
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/sk/LC_MESSAGES/
+-rw-r--r--   0 runner    (1001) docker     (122)      823 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/sk/LC_MESSAGES/messages-js.po
+-rw-r--r--   0 runner    (1001) docker     (122)      680 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/sk/LC_MESSAGES/messages.mo
+-rw-r--r--   0 runner    (1001) docker     (122)     1275 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/sk/LC_MESSAGES/messages.po
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/sv/
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/sv/LC_MESSAGES/
+-rw-r--r--   0 runner    (1001) docker     (122)      797 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/sv/LC_MESSAGES/messages-js.po
+-rw-r--r--   0 runner    (1001) docker     (122)      631 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/sv/LC_MESSAGES/messages.mo
+-rw-r--r--   0 runner    (1001) docker     (122)     1213 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/sv/LC_MESSAGES/messages.po
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/tr/
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/tr/LC_MESSAGES/
+-rw-r--r--   0 runner    (1001) docker     (122)      629 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/tr/LC_MESSAGES/messages.mo
+-rw-r--r--   0 runner    (1001) docker     (122)     1302 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/tr/LC_MESSAGES/messages.po
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/uk/
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/uk/LC_MESSAGES/
+-rw-r--r--   0 runner    (1001) docker     (122)      873 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/uk/LC_MESSAGES/messages-js.po
+-rw-r--r--   0 runner    (1001) docker     (122)      789 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/uk/LC_MESSAGES/messages.mo
+-rw-r--r--   0 runner    (1001) docker     (122)     1413 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/uk/LC_MESSAGES/messages.po
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/zh_CN/
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/zh_CN/LC_MESSAGES/
+-rw-r--r--   0 runner    (1001) docker     (122)      804 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/zh_CN/LC_MESSAGES/messages-js.po
+-rw-r--r--   0 runner    (1001) docker     (122)      635 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/zh_CN/LC_MESSAGES/messages.mo
+-rw-r--r--   0 runner    (1001) docker     (122)     1179 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/zh_CN/LC_MESSAGES/messages.po
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/zh_TW/
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/zh_TW/LC_MESSAGES/
+-rw-r--r--   0 runner    (1001) docker     (122)      805 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/zh_TW/LC_MESSAGES/messages-js.po
+-rw-r--r--   0 runner    (1001) docker     (122)      569 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/zh_TW/LC_MESSAGES/messages.mo
+-rw-r--r--   0 runner    (1001) docker     (122)     1193 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/translations/zh_TW/LC_MESSAGES/messages.po
+-rw-r--r--   0 runner    (1001) docker     (122)     8353 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/views.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2248 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/invenio_search_ui/webpack.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (122)     6721 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (122)    16135 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (122)        1 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (122)      301 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (122)        1 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui.egg-info/not-zip-safe
+-rw-r--r--   0 runner    (1001) docker     (122)      194 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (122)       18 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/invenio_search_ui.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (122)      103 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (122)      721 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/requirements-devel.txt
+-rwxr-xr-x   0 runner    (1001) docker     (122)      522 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/run-tests.sh
+-rw-r--r--   0 runner    (1001) docker     (122)     2070 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (122)      273 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/tests/
+-rw-r--r--   0 runner    (1001) docker     (122)     2537 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/tests/conftest.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/tests/templates/
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:14:18.000000 invenio-search-ui-2.4.1/tests/templates/invenio_search_ui/
+-rw-r--r--   0 runner    (1001) docker     (122)      606 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/tests/templates/invenio_search_ui/base.html
+-rw-r--r--   0 runner    (1001) docker     (122)      707 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/tests/templates/invenio_search_ui/base_header.html
+-rw-r--r--   0 runner    (1001) docker     (122)      792 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/tests/test_app.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1637 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/tests/test_ng_templates.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2685 2023-04-06 15:14:13.000000 invenio-search-ui-2.4.1/tests/test_rsk_templates.py
```

### Comparing `invenio-search-ui-2.4.0/.editorconfig` & `invenio-search-ui-2.4.1/.editorconfig`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/.github/workflows/pypi-publish.yml` & `invenio-search-ui-2.4.1/.github/workflows/pypi-publish.yml`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/.github/workflows/tests.yml` & `invenio-search-ui-2.4.1/.github/workflows/tests.yml`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/.tx/config` & `invenio-search-ui-2.4.1/.tx/config`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/CHANGES.rst` & `invenio-search-ui-2.4.1/CHANGES.rst`

 * *Files 2% similar despite different names*

```diff
@@ -4,14 +4,18 @@
 
     Invenio is free software; you can redistribute it and/or modify it
     under the terms of the MIT License; see LICENSE file for more details.
 
 Changes
 =======
 
+Version 2.4.1 (released 2023-04-06)
+
+- control maximum search results
+
 Version 2.4.0 (released 2023-03-02)
 
 - remove deprecated flask-babelex dependency and imports
 
 Version 2.3.0 (released 2023-01-26)
 
 - assets: normalize overridable ids
```

### Comparing `invenio-search-ui-2.4.0/CONTRIBUTING.rst` & `invenio-search-ui-2.4.1/CONTRIBUTING.rst`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/LICENSE` & `invenio-search-ui-2.4.1/LICENSE`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/MANIFEST.in` & `invenio-search-ui-2.4.1/MANIFEST.in`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/PKG-INFO` & `invenio-search-ui-2.4.1/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: invenio-search-ui
-Version: 2.4.0
+Version: 2.4.1
 Summary: UI for Invenio-Search.
 Home-page: https://github.com/inveniosoftware/invenio-search-ui
 Author: CERN
 Author-email: info@inveniosoftware.org
 License: MIT
 Description: ..
             This file is part of Invenio.
@@ -41,14 +41,18 @@
         
             Invenio is free software; you can redistribute it and/or modify it
             under the terms of the MIT License; see LICENSE file for more details.
         
         Changes
         =======
         
+        Version 2.4.1 (released 2023-04-06)
+        
+        - control maximum search results
+        
         Version 2.4.0 (released 2023-03-02)
         
         - remove deprecated flask-babelex dependency and imports
         
         Version 2.3.0 (released 2023-01-26)
         
         - assets: normalize overridable ids
```

### Comparing `invenio-search-ui-2.4.0/README.rst` & `invenio-search-ui-2.4.1/README.rst`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/docs/Makefile` & `invenio-search-ui-2.4.1/docs/Makefile`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/docs/conf.py` & `invenio-search-ui-2.4.1/docs/conf.py`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/docs/customizing.rst` & `invenio-search-ui-2.4.1/docs/customizing.rst`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/docs/index.rst` & `invenio-search-ui-2.4.1/docs/index.rst`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/docs/make.bat` & `invenio-search-ui-2.4.1/docs/make.bat`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/__init__.py` & `invenio-search-ui-2.4.1/invenio_search_ui/__init__.py`

 * *Files 0% similar despite different names*

```diff
@@ -323,10 +323,10 @@
         <p>{{ record.metadata.description }}</p>
       </li>
     </ul>
 """
 
 from .ext import InvenioSearchUI
 
-__version__ = "2.4.0"
+__version__ = "2.4.1"
 
 __all__ = ("__version__", "InvenioSearchUI")
```

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/assets/bootstrap3/js/invenio_search_ui/app.js` & `invenio-search-ui-2.4.1/invenio_search_ui/assets/bootstrap3/js/invenio_search_ui/app.js`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/assets/bootstrap3/scss/invenio_search_ui/search.scss` & `invenio-search-ui-2.4.1/invenio_search_ui/assets/bootstrap3/scss/invenio_search_ui/search.scss`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/js/invenio_search_ui/components/InvenioSearchPagination.js` & `invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/js/invenio_search_ui/components/InvenioSearchPagination.js`

 * *Files 24% similar despite different names*

#### js-beautify {}

```diff
@@ -12,14 +12,18 @@
 import {
     Grid
 } from "semantic-ui-react";
 
 export const InvenioSearchPagination = ({
         paginationOptions
     }) => {
+        const {
+            maxTotalResults,
+            resultsPerPage
+        } = paginationOptions;
         return ( <
                 Grid.Row verticalAlign = "middle" >
                 <
                 Grid.Column className = "computer tablet only"
                 width = {
                     4
                 } > < /Grid.Column> <
@@ -30,14 +34,15 @@
                 textAlign = "center" >
                 <
                 Pagination options = {
                     {
                         size: "mini",
                         showFirst: false,
                         showLast: false,
+                        maxTotalResults,
                     }
                 }
                 /> <
                 /Grid.Column> <
                 Grid.Column className = "mobile only"
                 width = {
                     16
@@ -45,26 +50,27 @@
                 textAlign = "center" >
                 <
                 Pagination options = {
                     {
                         boundaryRangeCount: 0,
                         showFirst: false,
                         showLast: false,
+                        maxTotalResults,
                     }
                 }
                 /> <
                 /Grid.Column> <
                 Grid.Column className = "computer tablet only "
                 textAlign = "right"
                 width = {
                     4
                 } >
                 <
                 ResultsPerPage values = {
-                    paginationOptions.resultsPerPage
+                    resultsPerPage
                 }
                 label = {
                     (cmp) => < > {
                         cmp
                     }
                     results per page < />} /
                     >
@@ -74,15 +80,15 @@
                     textAlign = "center"
                     width = {
                         16
                     } >
                     <
                     ResultsPerPage
                     values = {
-                        paginationOptions.resultsPerPage
+                        resultsPerPage
                     }
                     label = {
                         (cmp) => < > {
                             cmp
                         }
                         results per page < />} /
                         >
```

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/js/invenio_search_ui/components/MultipleOptionsSearchBar.js` & `invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/js/invenio_search_ui/components/MultipleOptionsSearchBar.js`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/js/invenio_search_ui/components/Results.js` & `invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/js/invenio_search_ui/components/Results.js`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/js/invenio_search_ui/components/ResultsGridItem.js` & `invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/js/invenio_search_ui/components/ResultsGridItem.js`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/js/invenio_search_ui/components/ResultsListItem.js` & `invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/js/invenio_search_ui/components/ResultsListItem.js`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/js/invenio_search_ui/components/SearchApp.js` & `invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/js/invenio_search_ui/components/SearchApp.js`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/js/invenio_search_ui/components/SearchAppFacets.js` & `invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/js/invenio_search_ui/components/SearchAppFacets.js`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/js/invenio_search_ui/components/SearchAppResultsPane.js` & `invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/js/invenio_search_ui/components/SearchAppResultsPane.js`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/js/invenio_search_ui/components/SearchBar.js` & `invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/js/invenio_search_ui/components/SearchBar.js`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/js/invenio_search_ui/components/SearchDropdowns.js` & `invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/js/invenio_search_ui/components/SearchDropdowns.js`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/js/invenio_search_ui/components/SearchFilters.js` & `invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/js/invenio_search_ui/components/SearchFilters.js`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/js/invenio_search_ui/components/common/facets.js` & `invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/js/invenio_search_ui/components/common/facets.js`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/js/invenio_search_ui/components/index.js` & `invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/js/invenio_search_ui/components/index.js`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/js/invenio_search_ui/util.js` & `invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/js/invenio_search_ui/util.js`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/i18next-scanner.config.js` & `invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/i18next-scanner.config.js`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/i18next.js` & `invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/i18next.js`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/af/messages.po` & `invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/af/messages.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/ar/messages.po` & `invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/ar/messages.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/ar/translations.json` & `invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/ar/translations.json`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/bg/messages.po` & `invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/bg/messages.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/ca/messages.po` & `invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/ca/messages.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/cs/messages.po` & `invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/cs/messages.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/da/messages.po` & `invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/da/messages.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/de/messages.po` & `invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/de/messages.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/el/messages.po` & `invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/el/messages.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/es/messages.po` & `invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/es/messages.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/et/messages.po` & `invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/et/messages.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/et_EE/messages.po` & `invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/et_EE/messages.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/fa/messages.po` & `invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/fa/messages.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/fr/messages.po` & `invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/fr/messages.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/gl/messages.po` & `invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/gl/messages.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/hr/messages.po` & `invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/hr/messages.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/hu/messages.po` & `invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/hu/messages.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/index.js` & `invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/index.js`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/it/messages.po` & `invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/it/messages.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/ja/messages.po` & `invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/ja/messages.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/ka/messages.po` & `invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/ka/messages.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/lt/messages.po` & `invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/lt/messages.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/no/messages.po` & `invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/no/messages.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/pl/messages.po` & `invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/pl/messages.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/pt/messages.po` & `invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/pt/messages.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/ro/messages.po` & `invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/ro/messages.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/ru/messages.po` & `invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/ru/messages.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/rw/messages.po` & `invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/rw/messages.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/sk/messages.po` & `invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/sk/messages.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/sv/messages.po` & `invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/sv/messages.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/tr/messages.po` & `invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/tr/messages.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/uk/messages.po` & `invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/uk/messages.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/zh_CN/messages.po` & `invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/zh_CN/messages.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/zh_TW/messages.po` & `invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/messages/zh_TW/messages.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/package-lock.json` & `invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/package-lock.json`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/package.json` & `invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/package.json`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/scripts/compileCatalog.js` & `invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/scripts/compileCatalog.js`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/scripts/initCatalog.js` & `invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/scripts/initCatalog.js`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/translations.pot` & `invenio-search-ui-2.4.1/invenio_search_ui/assets/semantic-ui/translations/invenio_search_ui/translations.pot`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/config.py` & `invenio-search-ui-2.4.1/invenio_search_ui/config.py`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/ext.py` & `invenio-search-ui-2.4.1/invenio_search_ui/ext.py`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/searchconfig.py` & `invenio-search-ui-2.4.1/invenio_search_ui/searchconfig.py`

 * *Files 2% similar despite different names*

```diff
@@ -81,14 +81,15 @@
         app_id="search",
         headers=None,
         list_view=True,
         grid_view=False,
         pagination_options=(10, 20, 50),
         default_size=10,
         default_page=1,
+        default_max_results=10000,
         facets=None,
         sort=None,
         initial_filters=[],
     )
 
     def __init__(self, configuration_options):
         """Initialize the search configuration.
@@ -102,14 +103,15 @@
         :param list_view: Boolean enabling the list view of the results.
         :param grid_view: Boolean enabling the grid view of the results.
         :param pagination_options: An integer array providing the results per
             page options.
         :param default_size: An integer setting the default number of results
             per page.
         :param default_page: An integer setting the default page.
+        :param default_max_results: An integer setting the default maximum total results.
         """
         options = deepcopy(self.default_options)
         options.update(configuration_options)
         for key, value in options.items():
             setattr(self, key, value)
 
     @property
@@ -179,14 +181,15 @@
             )
         return {
             "resultsPerPage": [
                 {"text": str(option), "value": option}
                 for option in self.pagination_options
             ],
             "defaultValue": self.default_size,
+            "maxTotalResults": self.default_max_results,
         }
 
     @property
     def defaultSortingOnEmptyQueryString(self):
         """Defines the default sorting options when there is no query."""
         return {
             "sortBy": self.sort.default_no_query,
```

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/static/templates/invenio_search_ui/count.html` & `invenio-search-ui-2.4.1/invenio_search_ui/static/templates/invenio_search_ui/count.html`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/static/templates/invenio_search_ui/facets.html` & `invenio-search-ui-2.4.1/invenio_search_ui/static/templates/invenio_search_ui/facets.html`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/static/templates/invenio_search_ui/pagination.html` & `invenio-search-ui-2.4.1/invenio_search_ui/static/templates/invenio_search_ui/pagination.html`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/static/templates/invenio_search_ui/range.html` & `invenio-search-ui-2.4.1/invenio_search_ui/static/templates/invenio_search_ui/range.html`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/static/templates/invenio_search_ui/results.html` & `invenio-search-ui-2.4.1/invenio_search_ui/static/templates/invenio_search_ui/results.html`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/static/templates/invenio_search_ui/searchbar.html` & `invenio-search-ui-2.4.1/invenio_search_ui/static/templates/invenio_search_ui/searchbar.html`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/templates/invenio_search_ui/header.html` & `invenio-search-ui-2.4.1/invenio_search_ui/templates/invenio_search_ui/header.html`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/templates/invenio_search_ui/search.html` & `invenio-search-ui-2.4.1/invenio_search_ui/templates/invenio_search_ui/search.html`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/templates/semantic-ui/invenio_search_ui/header.html` & `invenio-search-ui-2.4.1/invenio_search_ui/templates/semantic-ui/invenio_search_ui/header.html`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/templates/semantic-ui/invenio_search_ui/search.html` & `invenio-search-ui-2.4.1/invenio_search_ui/templates/semantic-ui/invenio_search_ui/search.html`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/af/LC_MESSAGES/messages-js.po` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/af/LC_MESSAGES/messages-js.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/af/LC_MESSAGES/messages.mo` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/af/LC_MESSAGES/messages.mo`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/af/LC_MESSAGES/messages.po` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/af/LC_MESSAGES/messages.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/ar/LC_MESSAGES/messages.mo` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/ar/LC_MESSAGES/messages.mo`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/ar/LC_MESSAGES/messages.po` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/ar/LC_MESSAGES/messages.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/bg/LC_MESSAGES/messages-js.po` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/bg/LC_MESSAGES/messages-js.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/bg/LC_MESSAGES/messages.mo` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/bg/LC_MESSAGES/messages.mo`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/bg/LC_MESSAGES/messages.po` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/bg/LC_MESSAGES/messages.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/ca/LC_MESSAGES/messages-js.po` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/ca/LC_MESSAGES/messages-js.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/ca/LC_MESSAGES/messages.mo` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/ca/LC_MESSAGES/messages.mo`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/ca/LC_MESSAGES/messages.po` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/ca/LC_MESSAGES/messages.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/cs/LC_MESSAGES/messages-js.po` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/cs/LC_MESSAGES/messages-js.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/cs/LC_MESSAGES/messages.mo` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/cs/LC_MESSAGES/messages.mo`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/cs/LC_MESSAGES/messages.po` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/cs/LC_MESSAGES/messages.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/da/LC_MESSAGES/messages-js.po` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/da/LC_MESSAGES/messages-js.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/da/LC_MESSAGES/messages.mo` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/da/LC_MESSAGES/messages.mo`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/da/LC_MESSAGES/messages.po` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/da/LC_MESSAGES/messages.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/de/LC_MESSAGES/messages-js.po` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/de/LC_MESSAGES/messages-js.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/de/LC_MESSAGES/messages.mo` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/de/LC_MESSAGES/messages.mo`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/de/LC_MESSAGES/messages.po` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/de/LC_MESSAGES/messages.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/el/LC_MESSAGES/messages-js.po` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/el/LC_MESSAGES/messages-js.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/el/LC_MESSAGES/messages.mo` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/el/LC_MESSAGES/messages.mo`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/el/LC_MESSAGES/messages.po` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/el/LC_MESSAGES/messages.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/es/LC_MESSAGES/messages-js.po` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/es/LC_MESSAGES/messages-js.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/es/LC_MESSAGES/messages.mo` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/es/LC_MESSAGES/messages.mo`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/es/LC_MESSAGES/messages.po` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/es/LC_MESSAGES/messages.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/et/LC_MESSAGES/messages.mo` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/et/LC_MESSAGES/messages.mo`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/et/LC_MESSAGES/messages.po` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/et/LC_MESSAGES/messages.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/et_EE/LC_MESSAGES/messages.mo` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/et_EE/LC_MESSAGES/messages.mo`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/et_EE/LC_MESSAGES/messages.po` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/et_EE/LC_MESSAGES/messages.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/fa/LC_MESSAGES/messages.mo` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/fa/LC_MESSAGES/messages.mo`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/fa/LC_MESSAGES/messages.po` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/fa/LC_MESSAGES/messages.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/fr/LC_MESSAGES/messages-js.po` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/fr/LC_MESSAGES/messages-js.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/fr/LC_MESSAGES/messages.mo` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/fr/LC_MESSAGES/messages.mo`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/fr/LC_MESSAGES/messages.po` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/fr/LC_MESSAGES/messages.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/gl/LC_MESSAGES/messages-js.po` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/gl/LC_MESSAGES/messages-js.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/gl/LC_MESSAGES/messages.mo` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/gl/LC_MESSAGES/messages.mo`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/gl/LC_MESSAGES/messages.po` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/gl/LC_MESSAGES/messages.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/hr/LC_MESSAGES/messages-js.po` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/hr/LC_MESSAGES/messages-js.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/hr/LC_MESSAGES/messages.mo` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/hr/LC_MESSAGES/messages.mo`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/hr/LC_MESSAGES/messages.po` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/hr/LC_MESSAGES/messages.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/hu/LC_MESSAGES/messages-js.po` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/hu/LC_MESSAGES/messages-js.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/hu/LC_MESSAGES/messages.mo` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/hu/LC_MESSAGES/messages.mo`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/hu/LC_MESSAGES/messages.po` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/hu/LC_MESSAGES/messages.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/it/LC_MESSAGES/messages-js.po` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/it/LC_MESSAGES/messages-js.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/it/LC_MESSAGES/messages.mo` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/it/LC_MESSAGES/messages.mo`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/it/LC_MESSAGES/messages.po` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/it/LC_MESSAGES/messages.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/ja/LC_MESSAGES/messages-js.po` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/ja/LC_MESSAGES/messages-js.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/ja/LC_MESSAGES/messages.mo` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/ja/LC_MESSAGES/messages.mo`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/ja/LC_MESSAGES/messages.po` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/ja/LC_MESSAGES/messages.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/ka/LC_MESSAGES/messages-js.po` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/ka/LC_MESSAGES/messages-js.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/ka/LC_MESSAGES/messages.mo` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/ka/LC_MESSAGES/messages.mo`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/ka/LC_MESSAGES/messages.po` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/ka/LC_MESSAGES/messages.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/lt/LC_MESSAGES/messages.mo` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/lt/LC_MESSAGES/messages.mo`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/lt/LC_MESSAGES/messages.po` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/lt/LC_MESSAGES/messages.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/messages-js.pot` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/messages-js.pot`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/messages.pot` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/messages.pot`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/no/LC_MESSAGES/messages-js.po` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/no/LC_MESSAGES/messages-js.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/no/LC_MESSAGES/messages.mo` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/no/LC_MESSAGES/messages.mo`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/no/LC_MESSAGES/messages.po` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/no/LC_MESSAGES/messages.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/pl/LC_MESSAGES/messages-js.po` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/pl/LC_MESSAGES/messages-js.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/pl/LC_MESSAGES/messages.mo` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/pl/LC_MESSAGES/messages.mo`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/pl/LC_MESSAGES/messages.po` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/pl/LC_MESSAGES/messages.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/pt/LC_MESSAGES/messages-js.po` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/pt/LC_MESSAGES/messages-js.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/pt/LC_MESSAGES/messages.mo` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/pt/LC_MESSAGES/messages.mo`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/pt/LC_MESSAGES/messages.po` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/pt/LC_MESSAGES/messages.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/ro/LC_MESSAGES/messages-js.po` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/ro/LC_MESSAGES/messages-js.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/ro/LC_MESSAGES/messages.mo` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/ro/LC_MESSAGES/messages.mo`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/ro/LC_MESSAGES/messages.po` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/ro/LC_MESSAGES/messages.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/ru/LC_MESSAGES/messages-js.po` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/ru/LC_MESSAGES/messages-js.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/ru/LC_MESSAGES/messages.mo` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/ru/LC_MESSAGES/messages.mo`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/ru/LC_MESSAGES/messages.po` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/ru/LC_MESSAGES/messages.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/rw/LC_MESSAGES/messages-js.po` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/rw/LC_MESSAGES/messages-js.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/rw/LC_MESSAGES/messages.mo` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/rw/LC_MESSAGES/messages.mo`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/rw/LC_MESSAGES/messages.po` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/rw/LC_MESSAGES/messages.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/sk/LC_MESSAGES/messages-js.po` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/sk/LC_MESSAGES/messages-js.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/sk/LC_MESSAGES/messages.mo` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/sk/LC_MESSAGES/messages.mo`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/sk/LC_MESSAGES/messages.po` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/sk/LC_MESSAGES/messages.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/sv/LC_MESSAGES/messages-js.po` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/sv/LC_MESSAGES/messages-js.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/sv/LC_MESSAGES/messages.mo` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/sv/LC_MESSAGES/messages.mo`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/sv/LC_MESSAGES/messages.po` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/sv/LC_MESSAGES/messages.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/tr/LC_MESSAGES/messages.mo` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/tr/LC_MESSAGES/messages.mo`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/tr/LC_MESSAGES/messages.po` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/tr/LC_MESSAGES/messages.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/uk/LC_MESSAGES/messages-js.po` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/uk/LC_MESSAGES/messages-js.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/uk/LC_MESSAGES/messages.mo` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/uk/LC_MESSAGES/messages.mo`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/uk/LC_MESSAGES/messages.po` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/uk/LC_MESSAGES/messages.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/zh_CN/LC_MESSAGES/messages-js.po` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/zh_CN/LC_MESSAGES/messages-js.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/zh_CN/LC_MESSAGES/messages.mo` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/zh_CN/LC_MESSAGES/messages.mo`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/zh_CN/LC_MESSAGES/messages.po` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/zh_CN/LC_MESSAGES/messages.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/zh_TW/LC_MESSAGES/messages-js.po` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/zh_TW/LC_MESSAGES/messages-js.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/zh_TW/LC_MESSAGES/messages.mo` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/zh_TW/LC_MESSAGES/messages.mo`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/translations/zh_TW/LC_MESSAGES/messages.po` & `invenio-search-ui-2.4.1/invenio_search_ui/translations/zh_TW/LC_MESSAGES/messages.po`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/views.py` & `invenio-search-ui-2.4.1/invenio_search_ui/views.py`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui/webpack.py` & `invenio-search-ui-2.4.1/invenio_search_ui/webpack.py`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui.egg-info/PKG-INFO` & `invenio-search-ui-2.4.1/invenio_search_ui.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: invenio-search-ui
-Version: 2.4.0
+Version: 2.4.1
 Summary: UI for Invenio-Search.
 Home-page: https://github.com/inveniosoftware/invenio-search-ui
 Author: CERN
 Author-email: info@inveniosoftware.org
 License: MIT
 Description: ..
             This file is part of Invenio.
@@ -41,14 +41,18 @@
         
             Invenio is free software; you can redistribute it and/or modify it
             under the terms of the MIT License; see LICENSE file for more details.
         
         Changes
         =======
         
+        Version 2.4.1 (released 2023-04-06)
+        
+        - control maximum search results
+        
         Version 2.4.0 (released 2023-03-02)
         
         - remove deprecated flask-babelex dependency and imports
         
         Version 2.3.0 (released 2023-01-26)
         
         - assets: normalize overridable ids
```

### Comparing `invenio-search-ui-2.4.0/invenio_search_ui.egg-info/SOURCES.txt` & `invenio-search-ui-2.4.1/invenio_search_ui.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/requirements-devel.txt` & `invenio-search-ui-2.4.1/requirements-devel.txt`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/run-tests.sh` & `invenio-search-ui-2.4.1/run-tests.sh`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/setup.cfg` & `invenio-search-ui-2.4.1/setup.cfg`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/tests/conftest.py` & `invenio-search-ui-2.4.1/tests/conftest.py`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/tests/templates/invenio_search_ui/base.html` & `invenio-search-ui-2.4.1/tests/templates/invenio_search_ui/base.html`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/tests/templates/invenio_search_ui/base_header.html` & `invenio-search-ui-2.4.1/tests/templates/invenio_search_ui/base_header.html`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/tests/test_app.py` & `invenio-search-ui-2.4.1/tests/test_app.py`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/tests/test_ng_templates.py` & `invenio-search-ui-2.4.1/tests/test_ng_templates.py`

 * *Files identical despite different names*

### Comparing `invenio-search-ui-2.4.0/tests/test_rsk_templates.py` & `invenio-search-ui-2.4.1/tests/test_rsk_templates.py`

 * *Files identical despite different names*

