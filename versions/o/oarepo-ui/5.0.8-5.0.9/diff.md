# Comparing `tmp/oarepo-ui-5.0.8.tar.gz` & `tmp/oarepo-ui-5.0.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "oarepo-ui-5.0.8.tar", last modified: Sun Mar 26 10:48:19 2023, max compression
+gzip compressed data, was "oarepo-ui-5.0.9.tar", last modified: Mon Mar 27 14:31:48 2023, max compression
```

## Comparing `oarepo-ui-5.0.8.tar` & `oarepo-ui-5.0.9.tar`

### file list

```diff
@@ -1,98 +1,98 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-26 10:48:19.084761 oarepo-ui-5.0.8/
--rw-r--r--   0 runner    (1001) docker     (123)      917 2023-03-26 10:45:21.000000 oarepo-ui-5.0.8/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     4079 2023-03-26 10:48:19.084761 oarepo-ui-5.0.8/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     3696 2023-03-26 10:45:21.000000 oarepo-ui-5.0.8/README.md
--rw-r--r--   0 runner    (1001) docker     (123)      552 2023-03-26 10:45:21.000000 oarepo-ui-5.0.8/babel.ini
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-26 10:48:19.064761 oarepo-ui-5.0.8/oarepo_ui/
--rw-r--r--   0 runner    (1001) docker     (123)      194 2023-03-26 10:45:21.000000 oarepo-ui-5.0.8/oarepo_ui/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1322 2023-03-26 10:45:21.000000 oarepo-ui-5.0.8/oarepo_ui/cli.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-26 10:48:19.064761 oarepo-ui-5.0.8/oarepo_ui/css/
--rw-r--r--   0 runner    (1001) docker     (123)      514 2023-03-26 10:45:21.000000 oarepo-ui-5.0.8/oarepo_ui/css/builtin.css
--rw-r--r--   0 runner    (1001) docker     (123)     1509 2023-03-26 10:45:21.000000 oarepo-ui-5.0.8/oarepo_ui/ext.py
--rw-r--r--   0 runner    (1001) docker     (123)      181 2023-03-26 10:45:21.000000 oarepo-ui-5.0.8/oarepo_ui/proxies.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-26 10:48:19.064761 oarepo-ui-5.0.8/oarepo_ui/resources/
--rw-r--r--   0 runner    (1001) docker     (123)      114 2023-03-26 10:45:21.000000 oarepo-ui-5.0.8/oarepo_ui/resources/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2359 2023-03-26 10:45:21.000000 oarepo-ui-5.0.8/oarepo_ui/resources/config.py
--rw-r--r--   0 runner    (1001) docker     (123)     5467 2023-03-26 10:45:21.000000 oarepo-ui-5.0.8/oarepo_ui/resources/resource.py
--rw-r--r--   0 runner    (1001) docker     (123)     7563 2023-03-26 10:45:21.000000 oarepo-ui-5.0.8/oarepo_ui/resources/templating.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-26 10:48:19.060761 oarepo-ui-5.0.8/oarepo_ui/templates/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-26 10:48:19.060761 oarepo-ui-5.0.8/oarepo_ui/templates/oarepo_ui/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-26 10:48:19.068760 oarepo-ui-5.0.8/oarepo_ui/templates/oarepo_ui/components/
--rw-r--r--   0 runner    (1001) docker     (123)      169 2023-03-26 10:45:21.000000 oarepo-ui-5.0.8/oarepo_ui/templates/oarepo_ui/components/000-array.jinja2
--rw-r--r--   0 runner    (1001) docker     (123)      423 2023-03-26 10:45:21.000000 oarepo-ui-5.0.8/oarepo_ui/templates/oarepo_ui/components/000-date.jinja2
--rw-r--r--   0 runner    (1001) docker     (123)      420 2023-03-26 10:45:21.000000 oarepo-ui-5.0.8/oarepo_ui/templates/oarepo_ui/components/000-field.jinja2
--rw-r--r--   0 runner    (1001) docker     (123)      456 2023-03-26 10:45:21.000000 oarepo-ui-5.0.8/oarepo_ui/templates/oarepo_ui/components/000-primitive.jinja2
--rw-r--r--   0 runner    (1001) docker     (123)      443 2023-03-26 10:45:21.000000 oarepo-ui-5.0.8/oarepo_ui/templates/oarepo_ui/components/000-strings.jinja2
--rw-r--r--   0 runner    (1001) docker     (123)      107 2023-03-26 10:45:21.000000 oarepo-ui-5.0.8/oarepo_ui/templates/oarepo_ui/components/000-value.jinja2
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-26 10:48:19.068760 oarepo-ui-5.0.8/oarepo_ui/theme/
--rw-r--r--   0 runner    (1001) docker     (123)      148 2023-03-26 10:45:21.000000 oarepo-ui-5.0.8/oarepo_ui/theme/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-26 10:48:19.060761 oarepo-ui-5.0.8/oarepo_ui/theme/assets/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-26 10:48:19.064761 oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-26 10:48:19.064761 oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/js/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-26 10:48:19.068760 oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/js/custom_fields/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-26 10:45:21.000000 oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/js/custom_fields/.gitkeep
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-26 10:48:19.072760 oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/
--rw-r--r--   0 runner    (1001) docker     (123)      625 2023-03-26 10:45:21.000000 oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/context.js
--rw-r--r--   0 runner    (1001) docker     (123)     4249 2023-03-26 10:45:21.000000 oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/hooks.jsx
--rw-r--r--   0 runner    (1001) docker     (123)      368 2023-03-26 10:45:21.000000 oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/index.js
--rw-r--r--   0 runner    (1001) docker     (123)      761 2023-03-26 10:45:21.000000 oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/layouts.jsx
--rw-r--r--   0 runner    (1001) docker     (123)      550 2023-03-26 10:45:21.000000 oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/search.js
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-26 10:48:19.080760 oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/
--rw-r--r--   0 runner    (1001) docker     (123)     1143 2023-03-26 10:45:21.000000 oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/Button.jsx
--rw-r--r--   0 runner    (1001) docker     (123)     1433 2023-03-26 10:45:21.000000 oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/Column.jsx
--rw-r--r--   0 runner    (1001) docker     (123)     1686 2023-03-26 10:45:21.000000 oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/ColumnWrapper.jsx
--rw-r--r--   0 runner    (1001) docker     (123)     1131 2023-03-26 10:45:21.000000 oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/Container.jsx
--rw-r--r--   0 runner    (1001) docker     (123)     2005 2023-03-26 10:45:21.000000 oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/DividedRow.jsx
--rw-r--r--   0 runner    (1001) docker     (123)     1406 2023-03-26 10:45:21.000000 oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/ErrorMessage.jsx
--rw-r--r--   0 runner    (1001) docker     (123)     2358 2023-03-26 10:45:21.000000 oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/Grid.jsx
--rw-r--r--   0 runner    (1001) docker     (123)     1458 2023-03-26 10:45:21.000000 oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/Header.jsx
--rw-r--r--   0 runner    (1001) docker     (123)     2690 2023-03-26 10:45:21.000000 oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/Icon.jsx
--rw-r--r--   0 runner    (1001) docker     (123)     1130 2023-03-26 10:45:21.000000 oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/Label.jsx
--rw-r--r--   0 runner    (1001) docker     (123)     1084 2023-03-26 10:45:21.000000 oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/Link.jsx
--rw-r--r--   0 runner    (1001) docker     (123)     2098 2023-03-26 10:45:21.000000 oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/List.jsx
--rw-r--r--   0 runner    (1001) docker     (123)     2188 2023-03-26 10:45:21.000000 oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/Placeholder.jsx
--rw-r--r--   0 runner    (1001) docker     (123)      796 2023-03-26 10:45:21.000000 oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/Raw.jsx
--rw-r--r--   0 runner    (1001) docker     (123)     1545 2023-03-26 10:45:21.000000 oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/Row.jsx
--rw-r--r--   0 runner    (1001) docker     (123)     1935 2023-03-26 10:45:21.000000 oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/RowWrapper.jsx
--rw-r--r--   0 runner    (1001) docker     (123)     1131 2023-03-26 10:45:21.000000 oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/Segment.jsx
--rw-r--r--   0 runner    (1001) docker     (123)     1043 2023-03-26 10:45:21.000000 oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/Separator.jsx
--rw-r--r--   0 runner    (1001) docker     (123)      498 2023-03-26 10:45:21.000000 oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/ShouldRender.jsx
--rw-r--r--   0 runner    (1001) docker     (123)     1307 2023-03-26 10:45:21.000000 oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/Span.jsx
--rw-r--r--   0 runner    (1001) docker     (123)     2531 2023-03-26 10:45:21.000000 oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/TruncatedText.jsx
--rw-r--r--   0 runner    (1001) docker     (123)      984 2023-03-26 10:45:21.000000 oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/index.js
--rw-r--r--   0 runner    (1001) docker     (123)      835 2023-03-26 10:45:21.000000 oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/util.js
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-26 10:48:19.084761 oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/translations/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-26 10:48:19.084761 oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/translations/oarepo_ui/
--rw-r--r--   0 runner    (1001) docker     (123)     1854 2023-03-26 10:45:21.000000 oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/translations/oarepo_ui/i18next-scanner.config.js
--rw-r--r--   0 runner    (1001) docker     (123)     1070 2023-03-26 10:45:21.000000 oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/translations/oarepo_ui/i18next.js
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-26 10:48:19.084761 oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/translations/oarepo_ui/messages/
--rw-r--r--   0 runner    (1001) docker     (123)       31 2023-03-26 10:45:21.000000 oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/translations/oarepo_ui/messages/index.js
--rw-r--r--   0 runner    (1001) docker     (123)      698 2023-03-26 10:45:21.000000 oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/translations/oarepo_ui/package.json
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-26 10:48:19.084761 oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/translations/oarepo_ui/scripts/
--rw-r--r--   0 runner    (1001) docker     (123)     1215 2023-03-26 10:45:21.000000 oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/translations/oarepo_ui/scripts/compileCatalog.js
--rw-r--r--   0 runner    (1001) docker     (123)      728 2023-03-26 10:45:21.000000 oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/translations/oarepo_ui/scripts/initCatalog.js
--rw-r--r--   0 runner    (1001) docker     (123)     3983 2023-03-26 10:45:21.000000 oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/translations/oarepo_ui/translations.pot
--rw-r--r--   0 runner    (1001) docker     (123)       86 2023-03-26 10:45:21.000000 oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/translations/yarn.lock
--rw-r--r--   0 runner    (1001) docker     (123)     2427 2023-03-26 10:45:21.000000 oarepo-ui-5.0.8/oarepo_ui/theme/webpack.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-26 10:48:19.084761 oarepo-ui-5.0.8/oarepo_ui/translations/
--rw-r--r--   0 runner    (1001) docker     (123)      133 2023-03-26 10:45:21.000000 oarepo-ui-5.0.8/oarepo_ui/translations/.gitkeep
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-26 10:48:19.064761 oarepo-ui-5.0.8/oarepo_ui/translations/cs/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-26 10:48:19.084761 oarepo-ui-5.0.8/oarepo_ui/translations/cs/LC_MESSAGES/
--rw-r--r--   0 runner    (1001) docker     (123)      676 2023-03-26 10:45:21.000000 oarepo-ui-5.0.8/oarepo_ui/translations/cs/LC_MESSAGES/messages.po
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-26 10:48:19.064761 oarepo-ui-5.0.8/oarepo_ui/translations/en/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-26 10:48:19.084761 oarepo-ui-5.0.8/oarepo_ui/translations/en/LC_MESSAGES/
--rw-r--r--   0 runner    (1001) docker     (123)      649 2023-03-26 10:45:21.000000 oarepo-ui-5.0.8/oarepo_ui/translations/en/LC_MESSAGES/messages.po
--rw-r--r--   0 runner    (1001) docker     (123)      602 2023-03-26 10:45:21.000000 oarepo-ui-5.0.8/oarepo_ui/translations/messages.pot
--rw-r--r--   0 runner    (1001) docker     (123)      696 2023-03-26 10:45:21.000000 oarepo-ui-5.0.8/oarepo_ui/utils.py
--rw-r--r--   0 runner    (1001) docker     (123)      103 2023-03-26 10:45:21.000000 oarepo-ui-5.0.8/oarepo_ui/views.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-26 10:48:19.064761 oarepo-ui-5.0.8/oarepo_ui.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     4079 2023-03-26 10:48:18.000000 oarepo-ui-5.0.8/oarepo_ui.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     3782 2023-03-26 10:48:19.000000 oarepo-ui-5.0.8/oarepo_ui.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-26 10:48:18.000000 oarepo-ui-5.0.8/oarepo_ui.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      344 2023-03-26 10:48:18.000000 oarepo-ui-5.0.8/oarepo_ui.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-26 10:46:06.000000 oarepo-ui-5.0.8/oarepo_ui.egg-info/not-zip-safe
--rw-r--r--   0 runner    (1001) docker     (123)      382 2023-03-26 10:48:18.000000 oarepo-ui-5.0.8/oarepo_ui.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       16 2023-03-26 10:48:18.000000 oarepo-ui-5.0.8/oarepo_ui.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)      103 2023-03-26 10:45:21.000000 oarepo-ui-5.0.8/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)     1895 2023-03-26 10:48:19.084761 oarepo-ui-5.0.8/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-26 10:45:21.000000 oarepo-ui-5.0.8/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 14:31:48.522540 oarepo-ui-5.0.9/
+-rw-r--r--   0 runner    (1001) docker     (123)      917 2023-03-27 14:29:18.000000 oarepo-ui-5.0.9/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     4079 2023-03-27 14:31:48.522540 oarepo-ui-5.0.9/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     3696 2023-03-27 14:29:18.000000 oarepo-ui-5.0.9/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)      552 2023-03-27 14:29:18.000000 oarepo-ui-5.0.9/babel.ini
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 14:31:48.514540 oarepo-ui-5.0.9/oarepo_ui/
+-rw-r--r--   0 runner    (1001) docker     (123)      194 2023-03-27 14:29:18.000000 oarepo-ui-5.0.9/oarepo_ui/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1322 2023-03-27 14:29:18.000000 oarepo-ui-5.0.9/oarepo_ui/cli.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 14:31:48.518540 oarepo-ui-5.0.9/oarepo_ui/css/
+-rw-r--r--   0 runner    (1001) docker     (123)      514 2023-03-27 14:29:18.000000 oarepo-ui-5.0.9/oarepo_ui/css/builtin.css
+-rw-r--r--   0 runner    (1001) docker     (123)     1509 2023-03-27 14:29:18.000000 oarepo-ui-5.0.9/oarepo_ui/ext.py
+-rw-r--r--   0 runner    (1001) docker     (123)      181 2023-03-27 14:29:18.000000 oarepo-ui-5.0.9/oarepo_ui/proxies.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 14:31:48.518540 oarepo-ui-5.0.9/oarepo_ui/resources/
+-rw-r--r--   0 runner    (1001) docker     (123)      114 2023-03-27 14:29:18.000000 oarepo-ui-5.0.9/oarepo_ui/resources/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2359 2023-03-27 14:29:18.000000 oarepo-ui-5.0.9/oarepo_ui/resources/config.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5602 2023-03-27 14:29:18.000000 oarepo-ui-5.0.9/oarepo_ui/resources/resource.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7563 2023-03-27 14:29:18.000000 oarepo-ui-5.0.9/oarepo_ui/resources/templating.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 14:31:48.514540 oarepo-ui-5.0.9/oarepo_ui/templates/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 14:31:48.514540 oarepo-ui-5.0.9/oarepo_ui/templates/oarepo_ui/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 14:31:48.518540 oarepo-ui-5.0.9/oarepo_ui/templates/oarepo_ui/components/
+-rw-r--r--   0 runner    (1001) docker     (123)      169 2023-03-27 14:29:18.000000 oarepo-ui-5.0.9/oarepo_ui/templates/oarepo_ui/components/000-array.jinja2
+-rw-r--r--   0 runner    (1001) docker     (123)      423 2023-03-27 14:29:18.000000 oarepo-ui-5.0.9/oarepo_ui/templates/oarepo_ui/components/000-date.jinja2
+-rw-r--r--   0 runner    (1001) docker     (123)      420 2023-03-27 14:29:18.000000 oarepo-ui-5.0.9/oarepo_ui/templates/oarepo_ui/components/000-field.jinja2
+-rw-r--r--   0 runner    (1001) docker     (123)      456 2023-03-27 14:29:18.000000 oarepo-ui-5.0.9/oarepo_ui/templates/oarepo_ui/components/000-primitive.jinja2
+-rw-r--r--   0 runner    (1001) docker     (123)      443 2023-03-27 14:29:18.000000 oarepo-ui-5.0.9/oarepo_ui/templates/oarepo_ui/components/000-strings.jinja2
+-rw-r--r--   0 runner    (1001) docker     (123)      107 2023-03-27 14:29:18.000000 oarepo-ui-5.0.9/oarepo_ui/templates/oarepo_ui/components/000-value.jinja2
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 14:31:48.518540 oarepo-ui-5.0.9/oarepo_ui/theme/
+-rw-r--r--   0 runner    (1001) docker     (123)      148 2023-03-27 14:29:18.000000 oarepo-ui-5.0.9/oarepo_ui/theme/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 14:31:48.514540 oarepo-ui-5.0.9/oarepo_ui/theme/assets/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 14:31:48.514540 oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 14:31:48.514540 oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/js/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 14:31:48.518540 oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/js/custom_fields/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-27 14:29:18.000000 oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/js/custom_fields/.gitkeep
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 14:31:48.518540 oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/
+-rw-r--r--   0 runner    (1001) docker     (123)      625 2023-03-27 14:29:18.000000 oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/context.js
+-rw-r--r--   0 runner    (1001) docker     (123)     4249 2023-03-27 14:29:18.000000 oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/hooks.jsx
+-rw-r--r--   0 runner    (1001) docker     (123)      368 2023-03-27 14:29:18.000000 oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/index.js
+-rw-r--r--   0 runner    (1001) docker     (123)      761 2023-03-27 14:29:18.000000 oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/layouts.jsx
+-rw-r--r--   0 runner    (1001) docker     (123)      550 2023-03-27 14:29:18.000000 oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/search.js
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 14:31:48.522540 oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/
+-rw-r--r--   0 runner    (1001) docker     (123)     1143 2023-03-27 14:29:18.000000 oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/Button.jsx
+-rw-r--r--   0 runner    (1001) docker     (123)     1433 2023-03-27 14:29:18.000000 oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/Column.jsx
+-rw-r--r--   0 runner    (1001) docker     (123)     1686 2023-03-27 14:29:18.000000 oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/ColumnWrapper.jsx
+-rw-r--r--   0 runner    (1001) docker     (123)     1131 2023-03-27 14:29:18.000000 oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/Container.jsx
+-rw-r--r--   0 runner    (1001) docker     (123)     2005 2023-03-27 14:29:18.000000 oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/DividedRow.jsx
+-rw-r--r--   0 runner    (1001) docker     (123)     1406 2023-03-27 14:29:18.000000 oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/ErrorMessage.jsx
+-rw-r--r--   0 runner    (1001) docker     (123)     2358 2023-03-27 14:29:18.000000 oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/Grid.jsx
+-rw-r--r--   0 runner    (1001) docker     (123)     1458 2023-03-27 14:29:18.000000 oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/Header.jsx
+-rw-r--r--   0 runner    (1001) docker     (123)     2690 2023-03-27 14:29:18.000000 oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/Icon.jsx
+-rw-r--r--   0 runner    (1001) docker     (123)     1130 2023-03-27 14:29:18.000000 oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/Label.jsx
+-rw-r--r--   0 runner    (1001) docker     (123)     1084 2023-03-27 14:29:18.000000 oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/Link.jsx
+-rw-r--r--   0 runner    (1001) docker     (123)     2098 2023-03-27 14:29:18.000000 oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/List.jsx
+-rw-r--r--   0 runner    (1001) docker     (123)     2188 2023-03-27 14:29:18.000000 oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/Placeholder.jsx
+-rw-r--r--   0 runner    (1001) docker     (123)      796 2023-03-27 14:29:18.000000 oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/Raw.jsx
+-rw-r--r--   0 runner    (1001) docker     (123)     1545 2023-03-27 14:29:18.000000 oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/Row.jsx
+-rw-r--r--   0 runner    (1001) docker     (123)     1935 2023-03-27 14:29:18.000000 oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/RowWrapper.jsx
+-rw-r--r--   0 runner    (1001) docker     (123)     1131 2023-03-27 14:29:18.000000 oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/Segment.jsx
+-rw-r--r--   0 runner    (1001) docker     (123)     1043 2023-03-27 14:29:18.000000 oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/Separator.jsx
+-rw-r--r--   0 runner    (1001) docker     (123)      498 2023-03-27 14:29:18.000000 oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/ShouldRender.jsx
+-rw-r--r--   0 runner    (1001) docker     (123)     1307 2023-03-27 14:29:18.000000 oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/Span.jsx
+-rw-r--r--   0 runner    (1001) docker     (123)     2531 2023-03-27 14:29:18.000000 oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/TruncatedText.jsx
+-rw-r--r--   0 runner    (1001) docker     (123)      984 2023-03-27 14:29:18.000000 oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/index.js
+-rw-r--r--   0 runner    (1001) docker     (123)      835 2023-03-27 14:29:18.000000 oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/util.js
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 14:31:48.522540 oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/translations/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 14:31:48.522540 oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/translations/oarepo_ui/
+-rw-r--r--   0 runner    (1001) docker     (123)     1854 2023-03-27 14:29:18.000000 oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/translations/oarepo_ui/i18next-scanner.config.js
+-rw-r--r--   0 runner    (1001) docker     (123)     1070 2023-03-27 14:29:18.000000 oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/translations/oarepo_ui/i18next.js
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 14:31:48.522540 oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/translations/oarepo_ui/messages/
+-rw-r--r--   0 runner    (1001) docker     (123)       31 2023-03-27 14:29:18.000000 oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/translations/oarepo_ui/messages/index.js
+-rw-r--r--   0 runner    (1001) docker     (123)      698 2023-03-27 14:29:18.000000 oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/translations/oarepo_ui/package.json
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 14:31:48.522540 oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/translations/oarepo_ui/scripts/
+-rw-r--r--   0 runner    (1001) docker     (123)     1215 2023-03-27 14:29:18.000000 oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/translations/oarepo_ui/scripts/compileCatalog.js
+-rw-r--r--   0 runner    (1001) docker     (123)      728 2023-03-27 14:29:18.000000 oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/translations/oarepo_ui/scripts/initCatalog.js
+-rw-r--r--   0 runner    (1001) docker     (123)     3983 2023-03-27 14:29:18.000000 oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/translations/oarepo_ui/translations.pot
+-rw-r--r--   0 runner    (1001) docker     (123)       86 2023-03-27 14:29:18.000000 oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/translations/yarn.lock
+-rw-r--r--   0 runner    (1001) docker     (123)     2427 2023-03-27 14:29:18.000000 oarepo-ui-5.0.9/oarepo_ui/theme/webpack.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 14:31:48.522540 oarepo-ui-5.0.9/oarepo_ui/translations/
+-rw-r--r--   0 runner    (1001) docker     (123)      133 2023-03-27 14:29:18.000000 oarepo-ui-5.0.9/oarepo_ui/translations/.gitkeep
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 14:31:48.514540 oarepo-ui-5.0.9/oarepo_ui/translations/cs/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 14:31:48.522540 oarepo-ui-5.0.9/oarepo_ui/translations/cs/LC_MESSAGES/
+-rw-r--r--   0 runner    (1001) docker     (123)      676 2023-03-27 14:29:18.000000 oarepo-ui-5.0.9/oarepo_ui/translations/cs/LC_MESSAGES/messages.po
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 14:31:48.514540 oarepo-ui-5.0.9/oarepo_ui/translations/en/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 14:31:48.522540 oarepo-ui-5.0.9/oarepo_ui/translations/en/LC_MESSAGES/
+-rw-r--r--   0 runner    (1001) docker     (123)      649 2023-03-27 14:29:18.000000 oarepo-ui-5.0.9/oarepo_ui/translations/en/LC_MESSAGES/messages.po
+-rw-r--r--   0 runner    (1001) docker     (123)      602 2023-03-27 14:29:18.000000 oarepo-ui-5.0.9/oarepo_ui/translations/messages.pot
+-rw-r--r--   0 runner    (1001) docker     (123)      696 2023-03-27 14:29:18.000000 oarepo-ui-5.0.9/oarepo_ui/utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)      103 2023-03-27 14:29:18.000000 oarepo-ui-5.0.9/oarepo_ui/views.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-27 14:31:48.518540 oarepo-ui-5.0.9/oarepo_ui.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     4079 2023-03-27 14:31:48.000000 oarepo-ui-5.0.9/oarepo_ui.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     3782 2023-03-27 14:31:48.000000 oarepo-ui-5.0.9/oarepo_ui.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-27 14:31:48.000000 oarepo-ui-5.0.9/oarepo_ui.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      344 2023-03-27 14:31:48.000000 oarepo-ui-5.0.9/oarepo_ui.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-27 14:29:54.000000 oarepo-ui-5.0.9/oarepo_ui.egg-info/not-zip-safe
+-rw-r--r--   0 runner    (1001) docker     (123)      382 2023-03-27 14:31:48.000000 oarepo-ui-5.0.9/oarepo_ui.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       16 2023-03-27 14:31:48.000000 oarepo-ui-5.0.9/oarepo_ui.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      103 2023-03-27 14:29:18.000000 oarepo-ui-5.0.9/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)     1895 2023-03-27 14:31:48.526540 oarepo-ui-5.0.9/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-27 14:29:18.000000 oarepo-ui-5.0.9/setup.py
```

### Comparing `oarepo-ui-5.0.8/MANIFEST.in` & `oarepo-ui-5.0.9/MANIFEST.in`

 * *Files identical despite different names*

### Comparing `oarepo-ui-5.0.8/PKG-INFO` & `oarepo-ui-5.0.9/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: oarepo-ui
-Version: 5.0.8
+Version: 5.0.9
 Summary: UI module for invenio 3.5+
 Home-page: https://github.com/oarepo/oarepo-ui
 Author: Mirek Simek
 Author-email: miroslav.simek@vscht.cz
 License: MIT
 Keywords: oarepo ui
 Platform: any
```

### Comparing `oarepo-ui-5.0.8/README.md` & `oarepo-ui-5.0.9/README.md`

 * *Files identical despite different names*

### Comparing `oarepo-ui-5.0.8/babel.ini` & `oarepo-ui-5.0.9/babel.ini`

 * *Files identical despite different names*

### Comparing `oarepo-ui-5.0.8/oarepo_ui/cli.py` & `oarepo-ui-5.0.9/oarepo_ui/cli.py`

 * *Files identical despite different names*

### Comparing `oarepo-ui-5.0.8/oarepo_ui/css/builtin.css` & `oarepo-ui-5.0.9/oarepo_ui/css/builtin.css`

 * *Files identical despite different names*

### Comparing `oarepo-ui-5.0.8/oarepo_ui/ext.py` & `oarepo-ui-5.0.9/oarepo_ui/ext.py`

 * *Files identical despite different names*

### Comparing `oarepo-ui-5.0.8/oarepo_ui/resources/config.py` & `oarepo-ui-5.0.9/oarepo_ui/resources/config.py`

 * *Files identical despite different names*

### Comparing `oarepo-ui-5.0.8/oarepo_ui/resources/resource.py` & `oarepo-ui-5.0.9/oarepo_ui/resources/resource.py`

 * *Files 6% similar despite different names*

```diff
@@ -89,25 +89,23 @@
         self.run_components("register_context_processor", context_processors=ret)
         return ret
 
     @request_read_args
     @request_view_args
     def detail(self):
         """Returns item detail page."""
-        record = self._api_service.read(
-            g.identity, resource_requestctx.view_args["pid_value"]
-        )
+        record = self._get_record(resource_requestctx)
         # TODO: handle permissions UI way - better response than generic error
         serialized_record = self.config.ui_serializer.dump_obj(record.to_dict())
         # make links absolute
         if "links" in serialized_record:
             for k, v in list(serialized_record["links"].items()):
                 if not isinstance(v, str):
                     continue
-                if not v.startswith("/"):
+                if not v.startswith("/") and not v.startswith("https://"):
                     v = f"/api{self._api_service.config.url_prefix}{v}"
                     serialized_record["links"][k] = v
         layout = current_oarepo_ui.get_layout(self.get_layout_name())
         self.run_components(
             "before_ui_detail",
             layout=layout,
             resource=self,
@@ -125,14 +123,19 @@
             data=serialized_record,
             metadata=serialized_record.get("metadata", serialized_record),
             ui=serialized_record.get("ui", serialized_record),
             layout=layout,
             component_key="detail",
         )
 
+    def _get_record(self, resource_requestctx):
+        return self._api_service.read(
+            g.identity, resource_requestctx.view_args["pid_value"]
+        )
+
     @request_read_args
     @request_view_args
     def export(self):
         pid_value = resource_requestctx.view_args["pid_value"]
         export_format = resource_requestctx.view_args["export_format"]
 
         record = self._api_service.read(g.identity, pid_value)
```

### Comparing `oarepo-ui-5.0.8/oarepo_ui/resources/templating.py` & `oarepo-ui-5.0.9/oarepo_ui/resources/templating.py`

 * *Files identical despite different names*

### Comparing `oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/context.js` & `oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/context.js`

 * *Files identical despite different names*

### Comparing `oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/hooks.jsx` & `oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/hooks.jsx`

 * *Files identical despite different names*

### Comparing `oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/layouts.jsx` & `oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/layouts.jsx`

 * *Files identical despite different names*

### Comparing `oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/search.js` & `oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/search.js`

 * *Files identical despite different names*

### Comparing `oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/Button.jsx` & `oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/Button.jsx`

 * *Files identical despite different names*

### Comparing `oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/Column.jsx` & `oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/Column.jsx`

 * *Files identical despite different names*

### Comparing `oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/ColumnWrapper.jsx` & `oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/ColumnWrapper.jsx`

 * *Files identical despite different names*

### Comparing `oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/Container.jsx` & `oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/Container.jsx`

 * *Files identical despite different names*

### Comparing `oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/DividedRow.jsx` & `oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/DividedRow.jsx`

 * *Files identical despite different names*

### Comparing `oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/ErrorMessage.jsx` & `oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/ErrorMessage.jsx`

 * *Files identical despite different names*

### Comparing `oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/Grid.jsx` & `oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/Grid.jsx`

 * *Files identical despite different names*

### Comparing `oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/Header.jsx` & `oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/Header.jsx`

 * *Files identical despite different names*

### Comparing `oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/Icon.jsx` & `oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/Icon.jsx`

 * *Files identical despite different names*

### Comparing `oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/Label.jsx` & `oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/Label.jsx`

 * *Files identical despite different names*

### Comparing `oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/Link.jsx` & `oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/Link.jsx`

 * *Files identical despite different names*

### Comparing `oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/List.jsx` & `oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/List.jsx`

 * *Files identical despite different names*

### Comparing `oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/Placeholder.jsx` & `oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/Placeholder.jsx`

 * *Files identical despite different names*

### Comparing `oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/Raw.jsx` & `oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/Raw.jsx`

 * *Files identical despite different names*

### Comparing `oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/Row.jsx` & `oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/Row.jsx`

 * *Files identical despite different names*

### Comparing `oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/RowWrapper.jsx` & `oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/RowWrapper.jsx`

 * *Files identical despite different names*

### Comparing `oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/Segment.jsx` & `oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/Segment.jsx`

 * *Files identical despite different names*

### Comparing `oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/Separator.jsx` & `oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/Separator.jsx`

 * *Files identical despite different names*

### Comparing `oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/Span.jsx` & `oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/Span.jsx`

 * *Files identical despite different names*

### Comparing `oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/TruncatedText.jsx` & `oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/TruncatedText.jsx`

 * *Files identical despite different names*

### Comparing `oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/index.js` & `oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/ui_components/index.js`

 * *Files identical despite different names*

### Comparing `oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/util.js` & `oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/js/oarepo_ui/util.js`

 * *Files identical despite different names*

### Comparing `oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/translations/oarepo_ui/i18next-scanner.config.js` & `oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/translations/oarepo_ui/i18next-scanner.config.js`

 * *Files identical despite different names*

### Comparing `oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/translations/oarepo_ui/i18next.js` & `oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/translations/oarepo_ui/i18next.js`

 * *Files identical despite different names*

### Comparing `oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/translations/oarepo_ui/package.json` & `oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/translations/oarepo_ui/package.json`

 * *Files identical despite different names*

### Comparing `oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/translations/oarepo_ui/scripts/compileCatalog.js` & `oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/translations/oarepo_ui/scripts/compileCatalog.js`

 * *Files identical despite different names*

### Comparing `oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/translations/oarepo_ui/scripts/initCatalog.js` & `oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/translations/oarepo_ui/scripts/initCatalog.js`

 * *Files identical despite different names*

### Comparing `oarepo-ui-5.0.8/oarepo_ui/theme/assets/semantic-ui/translations/oarepo_ui/translations.pot` & `oarepo-ui-5.0.9/oarepo_ui/theme/assets/semantic-ui/translations/oarepo_ui/translations.pot`

 * *Files identical despite different names*

### Comparing `oarepo-ui-5.0.8/oarepo_ui/theme/webpack.py` & `oarepo-ui-5.0.9/oarepo_ui/theme/webpack.py`

 * *Files identical despite different names*

### Comparing `oarepo-ui-5.0.8/oarepo_ui/translations/cs/LC_MESSAGES/messages.po` & `oarepo-ui-5.0.9/oarepo_ui/translations/cs/LC_MESSAGES/messages.po`

 * *Files identical despite different names*

### Comparing `oarepo-ui-5.0.8/oarepo_ui/translations/en/LC_MESSAGES/messages.po` & `oarepo-ui-5.0.9/oarepo_ui/translations/en/LC_MESSAGES/messages.po`

 * *Files identical despite different names*

### Comparing `oarepo-ui-5.0.8/oarepo_ui/translations/messages.pot` & `oarepo-ui-5.0.9/oarepo_ui/translations/messages.pot`

 * *Files identical despite different names*

### Comparing `oarepo-ui-5.0.8/oarepo_ui/utils.py` & `oarepo-ui-5.0.9/oarepo_ui/utils.py`

 * *Files identical despite different names*

### Comparing `oarepo-ui-5.0.8/oarepo_ui.egg-info/PKG-INFO` & `oarepo-ui-5.0.9/oarepo_ui.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: oarepo-ui
-Version: 5.0.8
+Version: 5.0.9
 Summary: UI module for invenio 3.5+
 Home-page: https://github.com/oarepo/oarepo-ui
 Author: Mirek Simek
 Author-email: miroslav.simek@vscht.cz
 License: MIT
 Keywords: oarepo ui
 Platform: any
```

### Comparing `oarepo-ui-5.0.8/oarepo_ui.egg-info/SOURCES.txt` & `oarepo-ui-5.0.9/oarepo_ui.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `oarepo-ui-5.0.8/setup.cfg` & `oarepo-ui-5.0.9/setup.cfg`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [metadata]
 name = oarepo-ui
-version = 5.0.8
+version = 5.0.9
 description = UI module for invenio 3.5+
 long_description = file: README.md
 long_description_content_type = text/markdown
 keywords = oarepo ui
 license = MIT
 author = Mirek Simek
 author_email = miroslav.simek@vscht.cz
```

