# Comparing `tmp/fava-1.8.tar.gz` & `tmp/fava-1.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/fava-1.8.tar", last modified: Wed Jul 25 18:38:10 2018, max compression
+gzip compressed data, was "dist/fava-1.9.tar", last modified: Mon Oct  8 19:16:40 2018, max compression
```

## Comparing `fava-1.8.tar` & `fava-1.9.tar`

### file list

```diff
@@ -1,167 +1,167 @@
-drwxr-xr-x   0 jakob     (1000) users      (100)        0 2018-07-25 18:38:10.000000 fava-1.8/
-drwxr-xr-x   0 jakob     (1000) users      (100)        0 2018-07-25 18:38:10.000000 fava-1.8/fava/
-drwxr-xr-x   0 jakob     (1000) users      (100)        0 2018-07-25 18:38:10.000000 fava-1.8/fava/core/
--rw-r--r--   0 jakob     (1000) users      (100)    17681 2018-07-23 15:21:43.000000 fava-1.8/fava/core/__init__.py
--rw-r--r--   0 jakob     (1000) users      (100)     2387 2018-06-24 14:50:46.000000 fava-1.8/fava/core/attributes.py
--rw-r--r--   0 jakob     (1000) users      (100)     4898 2018-06-24 13:58:43.000000 fava-1.8/fava/core/budgets.py
--rw-r--r--   0 jakob     (1000) users      (100)     6386 2018-07-23 15:21:43.000000 fava-1.8/fava/core/charts.py
--rw-r--r--   0 jakob     (1000) users      (100)     3639 2018-07-23 15:20:15.000000 fava-1.8/fava/core/fava_options.py
--rw-r--r--   0 jakob     (1000) users      (100)     9979 2018-07-23 15:20:15.000000 fava-1.8/fava/core/file.py
--rw-r--r--   0 jakob     (1000) users      (100)    10148 2018-07-23 15:21:43.000000 fava-1.8/fava/core/filters.py
--rw-r--r--   0 jakob     (1000) users      (100)      742 2018-07-23 15:21:43.000000 fava-1.8/fava/core/helpers.py
--rw-r--r--   0 jakob     (1000) users      (100)     3740 2018-07-23 15:21:43.000000 fava-1.8/fava/core/ingest.py
--rw-r--r--   0 jakob     (1000) users      (100)     2139 2018-06-24 13:58:43.000000 fava-1.8/fava/core/inventory.py
--rw-r--r--   0 jakob     (1000) users      (100)     2766 2018-06-24 13:58:43.000000 fava-1.8/fava/core/misc.py
--rw-r--r--   0 jakob     (1000) users      (100)     2256 2018-07-23 15:20:15.000000 fava-1.8/fava/core/number.py
--rw-r--r--   0 jakob     (1000) users      (100)     6589 2018-06-24 13:58:43.000000 fava-1.8/fava/core/query_shell.py
--rw-r--r--   0 jakob     (1000) users      (100)     4230 2018-07-23 15:21:43.000000 fava-1.8/fava/core/tree.py
--rw-r--r--   0 jakob     (1000) users      (100)     1460 2018-07-23 15:21:43.000000 fava-1.8/fava/core/watcher.py
-drwxr-xr-x   0 jakob     (1000) users      (100)        0 2018-07-25 18:38:10.000000 fava-1.8/fava/ext/
--rw-r--r--   0 jakob     (1000) users      (100)     1675 2018-07-23 15:21:43.000000 fava-1.8/fava/ext/__init__.py
--rw-r--r--   0 jakob     (1000) users      (100)      947 2018-06-24 13:58:43.000000 fava-1.8/fava/ext/auto_commit.py
-drwxr-xr-x   0 jakob     (1000) users      (100)        0 2018-07-25 18:38:10.000000 fava-1.8/fava/help/
--rw-r--r--   0 jakob     (1000) users      (100)      306 2018-06-24 13:58:43.000000 fava-1.8/fava/help/__init__.py
--rw-r--r--   0 jakob     (1000) users      (100)     1710 2018-06-24 13:58:43.000000 fava-1.8/fava/help/_index.md
--rw-r--r--   0 jakob     (1000) users      (100)     5048 2018-06-24 13:58:43.000000 fava-1.8/fava/help/beancount_syntax.md
--rw-r--r--   0 jakob     (1000) users      (100)     1513 2018-07-23 15:21:43.000000 fava-1.8/fava/help/budgets.md
--rw-r--r--   0 jakob     (1000) users      (100)      935 2018-06-24 13:58:43.000000 fava-1.8/fava/help/extensions.md
--rw-r--r--   0 jakob     (1000) users      (100)     6364 2018-06-24 13:58:43.000000 fava-1.8/fava/help/features.md
--rw-r--r--   0 jakob     (1000) users      (100)     3038 2018-07-23 15:20:15.000000 fava-1.8/fava/help/filters.md
--rw-r--r--   0 jakob     (1000) users      (100)      689 2018-06-24 13:58:43.000000 fava-1.8/fava/help/import.md
--rw-r--r--   0 jakob     (1000) users      (100)     5759 2018-07-23 15:21:43.000000 fava-1.8/fava/help/options.md
-drwxr-xr-x   0 jakob     (1000) users      (100)        0 2018-07-25 18:38:10.000000 fava-1.8/fava/plugins/
--rw-r--r--   0 jakob     (1000) users      (100)     2485 2018-06-24 13:58:43.000000 fava-1.8/fava/plugins/link_statements.py
--rw-r--r--   0 jakob     (1000) users      (100)      760 2018-06-24 13:58:43.000000 fava-1.8/fava/plugins/tag_discovered_documents.py
-drwxr-xr-x   0 jakob     (1000) users      (100)        0 2018-07-25 18:38:10.000000 fava-1.8/fava/static/
-drwxr-xr-x   0 jakob     (1000) users      (100)        0 2018-07-25 18:38:10.000000 fava-1.8/fava/static/css/
--rw-r--r--   0 jakob     (1000) users      (100)    10786 2018-07-23 15:21:43.000000 fava-1.8/fava/static/css/base.css
--rw-r--r--   0 jakob     (1000) users      (100)     3283 2018-07-23 15:20:15.000000 fava-1.8/fava/static/css/charts.css
--rw-r--r--   0 jakob     (1000) users      (100)      878 2018-06-24 13:58:43.000000 fava-1.8/fava/static/css/components.css
--rw-r--r--   0 jakob     (1000) users      (100)     2980 2018-06-24 14:50:46.000000 fava-1.8/fava/static/css/editor.css
--rw-r--r--   0 jakob     (1000) users      (100)     1355 2018-07-25 18:28:46.000000 fava-1.8/fava/static/css/entry-forms.css
--rw-r--r--   0 jakob     (1000) users      (100)     1283 2018-06-24 13:58:43.000000 fava-1.8/fava/static/css/fonts.css
--rw-r--r--   0 jakob     (1000) users      (100)     3327 2018-06-24 13:58:43.000000 fava-1.8/fava/static/css/header.css
--rw-r--r--   0 jakob     (1000) users      (100)      965 2018-06-24 13:58:43.000000 fava-1.8/fava/static/css/help.css
--rw-r--r--   0 jakob     (1000) users      (100)     1155 2018-06-24 13:58:43.000000 fava-1.8/fava/static/css/ingest.css
--rw-r--r--   0 jakob     (1000) users      (100)     4350 2018-06-24 13:58:43.000000 fava-1.8/fava/static/css/journal-table.css
--rw-r--r--   0 jakob     (1000) users      (100)     1232 2018-06-24 13:58:43.000000 fava-1.8/fava/static/css/media-mobile.css
--rw-r--r--   0 jakob     (1000) users      (100)      283 2018-06-24 13:58:43.000000 fava-1.8/fava/static/css/media-print.css
--rw-r--r--   0 jakob     (1000) users      (100)     1892 2018-06-24 13:58:43.000000 fava-1.8/fava/static/css/overlay.css
--rw-r--r--   0 jakob     (1000) users      (100)      803 2018-06-24 13:58:43.000000 fava-1.8/fava/static/css/query.css
--rw-r--r--   0 jakob     (1000) users      (100)     3736 2018-06-24 13:58:43.000000 fava-1.8/fava/static/css/style.css
--rw-r--r--   0 jakob     (1000) users      (100)     2833 2018-06-24 13:58:43.000000 fava-1.8/fava/static/css/tree-table.css
-drwxr-xr-x   0 jakob     (1000) users      (100)        0 2018-07-25 18:38:10.000000 fava-1.8/fava/static/gen/
-drwxr-xr-x   0 jakob     (1000) users      (100)        0 2018-07-25 18:38:10.000000 fava-1.8/fava/static/gen/codemirror/
--rw-r--r--   0 jakob     (1000) users      (100)      507 2018-07-25 18:38:10.000000 fava-1.8/fava/static/gen/codemirror/addon-dialog-dialog.css
--rw-r--r--   0 jakob     (1000) users      (100)      435 2018-07-25 18:38:10.000000 fava-1.8/fava/static/gen/codemirror/addon-fold-foldgutter.css
--rw-r--r--   0 jakob     (1000) users      (100)      623 2018-07-25 18:38:10.000000 fava-1.8/fava/static/gen/codemirror/addon-hint-show-hint.css
--rw-r--r--   0 jakob     (1000) users      (100)     8542 2018-07-25 18:38:10.000000 fava-1.8/fava/static/gen/codemirror/lib-codemirror.css
--rw-r--r--   0 jakob     (1000) users      (100)    19348 2018-07-25 18:38:10.000000 fava-1.8/fava/static/gen/FiraMono-Medium.woff
--rw-r--r--   0 jakob     (1000) users      (100)    19320 2018-07-25 18:38:10.000000 fava-1.8/fava/static/gen/FiraMono-Regular.woff
--rw-r--r--   0 jakob     (1000) users      (100)    34928 2018-07-25 18:38:10.000000 fava-1.8/fava/static/gen/FiraSans-Medium.woff
--rw-r--r--   0 jakob     (1000) users      (100)    34764 2018-07-25 18:38:10.000000 fava-1.8/fava/static/gen/FiraSans-Regular.woff
--rw-r--r--   0 jakob     (1000) users      (100)    19652 2018-07-25 18:38:10.000000 fava-1.8/fava/static/gen/SourceCodePro-Regular.woff
--rw-r--r--   0 jakob     (1000) users      (100)    19852 2018-07-25 18:38:10.000000 fava-1.8/fava/static/gen/SourceCodePro-Semibold.woff
--rw-r--r--   0 jakob     (1000) users      (100)    31888 2018-07-25 18:38:10.000000 fava-1.8/fava/static/gen/SourceSerifPro-Regular.woff
--rw-r--r--   0 jakob     (1000) users      (100)    35128 2018-07-25 18:38:10.000000 fava-1.8/fava/static/gen/SourceSerifPro-Semibold.woff
--rw-r--r--   0 jakob     (1000) users      (100)   825935 2018-07-25 18:38:10.000000 fava-1.8/fava/static/gen/app.js
-drwxr-xr-x   0 jakob     (1000) users      (100)        0 2018-07-25 18:38:10.000000 fava-1.8/fava/static/images/
--rw-r--r--   0 jakob     (1000) users      (100)     2802 2018-06-24 13:58:43.000000 fava-1.8/fava/static/images/favicon.ico
-drwxr-xr-x   0 jakob     (1000) users      (100)        0 2018-07-25 18:38:10.000000 fava-1.8/fava/templates/
-drwxr-xr-x   0 jakob     (1000) users      (100)        0 2018-07-25 18:38:10.000000 fava-1.8/fava/templates/macros/
--rw-r--r--   0 jakob     (1000) users      (100)     2566 2018-07-23 15:20:15.000000 fava-1.8/fava/templates/macros/_account_macros.html
--rw-r--r--   0 jakob     (1000) users      (100)     1732 2018-07-23 15:21:43.000000 fava-1.8/fava/templates/_aside.html
--rw-r--r--   0 jakob     (1000) users      (100)     4150 2018-07-23 15:20:15.000000 fava-1.8/fava/templates/_charts.html
--rw-r--r--   0 jakob     (1000) users      (100)     2380 2018-06-24 13:58:43.000000 fava-1.8/fava/templates/_context.html
--rw-r--r--   0 jakob     (1000) users      (100)     1156 2018-06-24 13:58:43.000000 fava-1.8/fava/templates/_entry_filters.html
--rw-r--r--   0 jakob     (1000) users      (100)     3948 2018-07-25 18:28:46.000000 fava-1.8/fava/templates/_entry_forms.html
--rw-r--r--   0 jakob     (1000) users      (100)      147 2018-06-24 13:58:43.000000 fava-1.8/fava/templates/_error.html
--rw-r--r--   0 jakob     (1000) users      (100)      966 2018-07-23 15:21:43.000000 fava-1.8/fava/templates/_globals.html
--rw-r--r--   0 jakob     (1000) users      (100)     9663 2018-06-24 14:50:46.000000 fava-1.8/fava/templates/_journal_table.html
--rw-r--r--   0 jakob     (1000) users      (100)     6538 2018-06-24 14:50:46.000000 fava-1.8/fava/templates/_layout.html
--rw-r--r--   0 jakob     (1000) users      (100)     2341 2018-06-24 13:58:43.000000 fava-1.8/fava/templates/_overlays.html
--rw-r--r--   0 jakob     (1000) users      (100)     2663 2018-06-24 13:58:43.000000 fava-1.8/fava/templates/_query_table.html
--rw-r--r--   0 jakob     (1000) users      (100)     8367 2018-06-24 13:58:43.000000 fava-1.8/fava/templates/_tree_table.html
--rw-r--r--   0 jakob     (1000) users      (100)     2294 2018-06-24 13:58:43.000000 fava-1.8/fava/templates/account.html
--rw-r--r--   0 jakob     (1000) users      (100)     1032 2018-06-28 16:08:16.000000 fava-1.8/fava/templates/balance_sheet.html
--rw-r--r--   0 jakob     (1000) users      (100)      666 2018-06-24 13:58:43.000000 fava-1.8/fava/templates/beancount_file
--rw-r--r--   0 jakob     (1000) users      (100)      821 2018-06-24 13:58:43.000000 fava-1.8/fava/templates/commodities.html
--rw-r--r--   0 jakob     (1000) users      (100)     2094 2018-07-23 15:21:43.000000 fava-1.8/fava/templates/editor.html
--rw-r--r--   0 jakob     (1000) users      (100)     1319 2018-06-24 13:58:43.000000 fava-1.8/fava/templates/errors.html
--rw-r--r--   0 jakob     (1000) users      (100)      890 2018-07-23 15:20:15.000000 fava-1.8/fava/templates/events.html
--rw-r--r--   0 jakob     (1000) users      (100)     1989 2018-06-29 10:37:55.000000 fava-1.8/fava/templates/extract.html
--rw-r--r--   0 jakob     (1000) users      (100)      573 2018-06-24 13:58:43.000000 fava-1.8/fava/templates/help.html
--rw-r--r--   0 jakob     (1000) users      (100)     2678 2018-06-24 14:50:46.000000 fava-1.8/fava/templates/holdings.html
--rw-r--r--   0 jakob     (1000) users      (100)     1402 2018-07-23 15:20:15.000000 fava-1.8/fava/templates/import.html
--rw-r--r--   0 jakob     (1000) users      (100)     1057 2018-06-24 13:58:43.000000 fava-1.8/fava/templates/income_statement.html
--rw-r--r--   0 jakob     (1000) users      (100)      214 2018-06-24 13:58:43.000000 fava-1.8/fava/templates/journal.html
--rw-r--r--   0 jakob     (1000) users      (100)     1101 2018-06-24 13:58:43.000000 fava-1.8/fava/templates/options.html
--rw-r--r--   0 jakob     (1000) users      (100)     1691 2018-06-24 13:58:43.000000 fava-1.8/fava/templates/query.html
--rw-r--r--   0 jakob     (1000) users      (100)     4525 2018-07-23 15:20:15.000000 fava-1.8/fava/templates/statistics.html
--rw-r--r--   0 jakob     (1000) users      (100)      469 2018-06-24 13:58:43.000000 fava-1.8/fava/templates/trial_balance.html
-drwxr-xr-x   0 jakob     (1000) users      (100)        0 2018-07-25 18:38:10.000000 fava-1.8/fava/translations/
-drwxr-xr-x   0 jakob     (1000) users      (100)        0 2018-07-25 18:38:10.000000 fava-1.8/fava/translations/de/
-drwxr-xr-x   0 jakob     (1000) users      (100)        0 2018-07-25 18:38:10.000000 fava-1.8/fava/translations/de/LC_MESSAGES/
--rw-r--r--   0 jakob     (1000) users      (100)     3864 2018-07-25 18:29:12.000000 fava-1.8/fava/translations/de/LC_MESSAGES/messages.mo
--rw-r--r--   0 jakob     (1000) users      (100)    10889 2018-07-25 18:29:10.000000 fava-1.8/fava/translations/de/LC_MESSAGES/messages.po
-drwxr-xr-x   0 jakob     (1000) users      (100)        0 2018-07-25 18:38:10.000000 fava-1.8/fava/translations/es/
-drwxr-xr-x   0 jakob     (1000) users      (100)        0 2018-07-25 18:38:10.000000 fava-1.8/fava/translations/es/LC_MESSAGES/
--rw-r--r--   0 jakob     (1000) users      (100)     3259 2018-07-25 18:29:17.000000 fava-1.8/fava/translations/es/LC_MESSAGES/messages.mo
--rw-r--r--   0 jakob     (1000) users      (100)    10746 2018-07-25 18:29:15.000000 fava-1.8/fava/translations/es/LC_MESSAGES/messages.po
-drwxr-xr-x   0 jakob     (1000) users      (100)        0 2018-07-25 18:38:10.000000 fava-1.8/fava/translations/fr/
-drwxr-xr-x   0 jakob     (1000) users      (100)        0 2018-07-25 18:38:10.000000 fava-1.8/fava/translations/fr/LC_MESSAGES/
--rw-r--r--   0 jakob     (1000) users      (100)     3282 2018-07-25 18:29:22.000000 fava-1.8/fava/translations/fr/LC_MESSAGES/messages.mo
--rw-r--r--   0 jakob     (1000) users      (100)    10751 2018-07-25 18:29:19.000000 fava-1.8/fava/translations/fr/LC_MESSAGES/messages.po
-drwxr-xr-x   0 jakob     (1000) users      (100)        0 2018-07-25 18:38:10.000000 fava-1.8/fava/translations/nl/
-drwxr-xr-x   0 jakob     (1000) users      (100)        0 2018-07-25 18:38:10.000000 fava-1.8/fava/translations/nl/LC_MESSAGES/
--rw-r--r--   0 jakob     (1000) users      (100)     3219 2018-07-25 18:29:29.000000 fava-1.8/fava/translations/nl/LC_MESSAGES/messages.mo
--rw-r--r--   0 jakob     (1000) users      (100)    10731 2018-07-25 18:29:25.000000 fava-1.8/fava/translations/nl/LC_MESSAGES/messages.po
-drwxr-xr-x   0 jakob     (1000) users      (100)        0 2018-07-25 18:38:10.000000 fava-1.8/fava/translations/pt/
-drwxr-xr-x   0 jakob     (1000) users      (100)        0 2018-07-25 18:38:10.000000 fava-1.8/fava/translations/pt/LC_MESSAGES/
--rw-r--r--   0 jakob     (1000) users      (100)     3160 2018-07-25 18:29:34.000000 fava-1.8/fava/translations/pt/LC_MESSAGES/messages.mo
--rw-r--r--   0 jakob     (1000) users      (100)    10810 2018-07-25 18:29:31.000000 fava-1.8/fava/translations/pt/LC_MESSAGES/messages.po
-drwxr-xr-x   0 jakob     (1000) users      (100)        0 2018-07-25 18:38:10.000000 fava-1.8/fava/translations/ru/
-drwxr-xr-x   0 jakob     (1000) users      (100)        0 2018-07-25 18:38:10.000000 fava-1.8/fava/translations/ru/LC_MESSAGES/
--rw-r--r--   0 jakob     (1000) users      (100)     3928 2018-07-25 18:29:39.000000 fava-1.8/fava/translations/ru/LC_MESSAGES/messages.mo
--rw-r--r--   0 jakob     (1000) users      (100)    11397 2018-07-25 18:29:37.000000 fava-1.8/fava/translations/ru/LC_MESSAGES/messages.po
-drwxr-xr-x   0 jakob     (1000) users      (100)        0 2018-07-25 18:38:10.000000 fava-1.8/fava/translations/sk/
-drwxr-xr-x   0 jakob     (1000) users      (100)        0 2018-07-25 18:38:10.000000 fava-1.8/fava/translations/sk/LC_MESSAGES/
--rw-r--r--   0 jakob     (1000) users      (100)     5515 2018-07-25 18:29:47.000000 fava-1.8/fava/translations/sk/LC_MESSAGES/messages.mo
--rw-r--r--   0 jakob     (1000) users      (100)    11587 2018-07-25 18:29:45.000000 fava-1.8/fava/translations/sk/LC_MESSAGES/messages.po
-drwxr-xr-x   0 jakob     (1000) users      (100)        0 2018-07-25 18:38:10.000000 fava-1.8/fava/translations/uk/
-drwxr-xr-x   0 jakob     (1000) users      (100)        0 2018-07-25 18:38:10.000000 fava-1.8/fava/translations/uk/LC_MESSAGES/
--rw-r--r--   0 jakob     (1000) users      (100)     6799 2018-07-25 18:29:51.000000 fava-1.8/fava/translations/uk/LC_MESSAGES/messages.mo
--rw-r--r--   0 jakob     (1000) users      (100)    12830 2018-07-25 18:29:50.000000 fava-1.8/fava/translations/uk/LC_MESSAGES/messages.po
-drwxr-xr-x   0 jakob     (1000) users      (100)        0 2018-07-25 18:38:10.000000 fava-1.8/fava/translations/zh/
-drwxr-xr-x   0 jakob     (1000) users      (100)        0 2018-07-25 18:38:10.000000 fava-1.8/fava/translations/zh/LC_MESSAGES/
--rw-r--r--   0 jakob     (1000) users      (100)     3193 2018-07-25 18:29:43.000000 fava-1.8/fava/translations/zh/LC_MESSAGES/messages.mo
--rw-r--r--   0 jakob     (1000) users      (100)    10534 2018-07-25 18:29:40.000000 fava-1.8/fava/translations/zh/LC_MESSAGES/messages.po
--rw-r--r--   0 jakob     (1000) users      (100)       97 2018-06-24 13:58:43.000000 fava-1.8/fava/translations/babel.conf
--rw-r--r--   0 jakob     (1000) users      (100)    10174 2018-07-25 18:29:00.000000 fava-1.8/fava/translations/messages.pot
-drwxr-xr-x   0 jakob     (1000) users      (100)        0 2018-07-25 18:38:10.000000 fava-1.8/fava/util/
--rw-r--r--   0 jakob     (1000) users      (100)     2619 2018-07-23 15:21:07.000000 fava-1.8/fava/util/__init__.py
--rw-r--r--   0 jakob     (1000) users      (100)     8169 2018-06-24 13:58:43.000000 fava-1.8/fava/util/date.py
--rw-r--r--   0 jakob     (1000) users      (100)     2096 2018-06-24 13:58:43.000000 fava-1.8/fava/util/excel.py
--rw-r--r--   0 jakob     (1000) users      (100)     2286 2018-07-23 15:21:43.000000 fava-1.8/fava/util/ranking.py
--rw-r--r--   0 jakob     (1000) users      (100)      594 2018-07-25 18:34:14.000000 fava-1.8/fava/__init__.py
--rw-r--r--   0 jakob     (1000) users      (100)    10538 2018-06-24 14:50:46.000000 fava-1.8/fava/application.py
--rw-r--r--   0 jakob     (1000) users      (100)     3052 2018-06-24 14:50:46.000000 fava-1.8/fava/cli.py
--rw-r--r--   0 jakob     (1000) users      (100)     4967 2018-06-24 13:58:43.000000 fava-1.8/fava/json_api.py
--rw-r--r--   0 jakob     (1000) users      (100)     3332 2018-07-25 18:28:46.000000 fava-1.8/fava/serialisation.py
--rw-r--r--   0 jakob     (1000) users      (100)     5374 2018-07-23 15:20:15.000000 fava-1.8/fava/template_filters.py
-drwxr-xr-x   0 jakob     (1000) users      (100)        0 2018-07-25 18:38:10.000000 fava-1.8/fava.egg-info/
--rw-r--r--   0 jakob     (1000) users      (100)     2901 2018-07-25 18:38:10.000000 fava-1.8/fava.egg-info/PKG-INFO
--rw-r--r--   0 jakob     (1000) users      (100)     3898 2018-07-25 18:38:10.000000 fava-1.8/fava.egg-info/SOURCES.txt
--rw-r--r--   0 jakob     (1000) users      (100)        1 2018-07-25 18:38:10.000000 fava-1.8/fava.egg-info/dependency_links.txt
--rw-r--r--   0 jakob     (1000) users      (100)       40 2018-07-25 18:38:10.000000 fava-1.8/fava.egg-info/entry_points.txt
--rw-r--r--   0 jakob     (1000) users      (100)        1 2018-06-24 14:02:22.000000 fava-1.8/fava.egg-info/not-zip-safe
--rw-r--r--   0 jakob     (1000) users      (100)      252 2018-07-25 18:38:10.000000 fava-1.8/fava.egg-info/requires.txt
--rw-r--r--   0 jakob     (1000) users      (100)        5 2018-07-25 18:38:10.000000 fava-1.8/fava.egg-info/top_level.txt
--rw-r--r--   0 jakob     (1000) users      (100)      475 2018-06-24 13:58:43.000000 fava-1.8/AUTHORS
--rw-r--r--   0 jakob     (1000) users      (100)    16700 2018-07-25 18:34:28.000000 fava-1.8/CHANGES
--rw-r--r--   0 jakob     (1000) users      (100)     1108 2018-06-24 13:58:43.000000 fava-1.8/LICENSE
--rw-r--r--   0 jakob     (1000) users      (100)      196 2018-06-24 13:58:43.000000 fava-1.8/MANIFEST.in
--rw-r--r--   0 jakob     (1000) users      (100)     1475 2018-06-24 13:58:43.000000 fava-1.8/README.rst
--rw-r--r--   0 jakob     (1000) users      (100)     2305 2018-07-23 15:20:15.000000 fava-1.8/setup.py
--rw-r--r--   0 jakob     (1000) users      (100)     2901 2018-07-25 18:38:10.000000 fava-1.8/PKG-INFO
--rw-r--r--   0 jakob     (1000) users      (100)       38 2018-07-25 18:38:10.000000 fava-1.8/setup.cfg
+drwxr-xr-x   0 jakob     (1000) users      (100)        0 2018-10-08 19:16:40.000000 fava-1.9/
+-rw-r--r--   0 jakob     (1000) users      (100)      475 2018-07-25 18:39:36.000000 fava-1.9/AUTHORS
+-rw-r--r--   0 jakob     (1000) users      (100)    16931 2018-10-08 19:13:34.000000 fava-1.9/CHANGES
+-rw-r--r--   0 jakob     (1000) users      (100)     1108 2018-07-25 18:39:36.000000 fava-1.9/LICENSE
+-rw-r--r--   0 jakob     (1000) users      (100)      196 2018-07-25 18:39:36.000000 fava-1.9/MANIFEST.in
+-rw-r--r--   0 jakob     (1000) users      (100)     2901 2018-10-08 19:16:40.000000 fava-1.9/PKG-INFO
+-rw-r--r--   0 jakob     (1000) users      (100)     1475 2018-07-25 18:39:36.000000 fava-1.9/README.rst
+drwxr-xr-x   0 jakob     (1000) users      (100)        0 2018-10-08 19:16:40.000000 fava-1.9/fava/
+-rw-r--r--   0 jakob     (1000) users      (100)      594 2018-10-08 19:14:08.000000 fava-1.9/fava/__init__.py
+-rw-r--r--   0 jakob     (1000) users      (100)    10784 2018-10-04 13:57:57.000000 fava-1.9/fava/application.py
+-rw-r--r--   0 jakob     (1000) users      (100)     3092 2018-09-18 09:58:42.000000 fava-1.9/fava/cli.py
+drwxr-xr-x   0 jakob     (1000) users      (100)        0 2018-10-08 19:16:40.000000 fava-1.9/fava/core/
+-rw-r--r--   0 jakob     (1000) users      (100)    17788 2018-10-02 12:33:28.000000 fava-1.9/fava/core/__init__.py
+-rw-r--r--   0 jakob     (1000) users      (100)     2387 2018-09-18 09:58:42.000000 fava-1.9/fava/core/attributes.py
+-rw-r--r--   0 jakob     (1000) users      (100)     4898 2018-09-18 09:58:42.000000 fava-1.9/fava/core/budgets.py
+-rw-r--r--   0 jakob     (1000) users      (100)     6386 2018-09-18 09:58:42.000000 fava-1.9/fava/core/charts.py
+-rw-r--r--   0 jakob     (1000) users      (100)     3694 2018-09-18 09:58:42.000000 fava-1.9/fava/core/fava_options.py
+-rw-r--r--   0 jakob     (1000) users      (100)     9979 2018-09-18 09:58:42.000000 fava-1.9/fava/core/file.py
+-rw-r--r--   0 jakob     (1000) users      (100)    10326 2018-10-02 12:33:28.000000 fava-1.9/fava/core/filters.py
+-rw-r--r--   0 jakob     (1000) users      (100)      742 2018-09-18 09:58:42.000000 fava-1.9/fava/core/helpers.py
+-rw-r--r--   0 jakob     (1000) users      (100)     3822 2018-10-04 14:04:02.000000 fava-1.9/fava/core/ingest.py
+-rw-r--r--   0 jakob     (1000) users      (100)     2139 2018-07-25 18:39:36.000000 fava-1.9/fava/core/inventory.py
+-rw-r--r--   0 jakob     (1000) users      (100)     2766 2018-09-18 09:58:42.000000 fava-1.9/fava/core/misc.py
+-rw-r--r--   0 jakob     (1000) users      (100)     2256 2018-09-18 09:58:42.000000 fava-1.9/fava/core/number.py
+-rw-r--r--   0 jakob     (1000) users      (100)     6589 2018-09-18 09:58:42.000000 fava-1.9/fava/core/query_shell.py
+-rw-r--r--   0 jakob     (1000) users      (100)     4230 2018-09-18 09:58:42.000000 fava-1.9/fava/core/tree.py
+-rw-r--r--   0 jakob     (1000) users      (100)     1460 2018-10-04 13:57:54.000000 fava-1.9/fava/core/watcher.py
+drwxr-xr-x   0 jakob     (1000) users      (100)        0 2018-10-08 19:16:40.000000 fava-1.9/fava/ext/
+-rw-r--r--   0 jakob     (1000) users      (100)     1675 2018-09-18 09:58:42.000000 fava-1.9/fava/ext/__init__.py
+-rw-r--r--   0 jakob     (1000) users      (100)      947 2018-09-18 09:58:42.000000 fava-1.9/fava/ext/auto_commit.py
+drwxr-xr-x   0 jakob     (1000) users      (100)        0 2018-10-08 19:16:40.000000 fava-1.9/fava/help/
+-rw-r--r--   0 jakob     (1000) users      (100)      306 2018-09-18 09:58:42.000000 fava-1.9/fava/help/__init__.py
+-rw-r--r--   0 jakob     (1000) users      (100)     1710 2018-07-25 18:39:36.000000 fava-1.9/fava/help/_index.md
+-rw-r--r--   0 jakob     (1000) users      (100)     5048 2018-07-25 18:39:36.000000 fava-1.9/fava/help/beancount_syntax.md
+-rw-r--r--   0 jakob     (1000) users      (100)     1513 2018-07-25 18:39:36.000000 fava-1.9/fava/help/budgets.md
+-rw-r--r--   0 jakob     (1000) users      (100)      935 2018-07-25 18:39:36.000000 fava-1.9/fava/help/extensions.md
+-rw-r--r--   0 jakob     (1000) users      (100)     6364 2018-07-25 18:39:36.000000 fava-1.9/fava/help/features.md
+-rw-r--r--   0 jakob     (1000) users      (100)     3038 2018-07-25 18:39:36.000000 fava-1.9/fava/help/filters.md
+-rw-r--r--   0 jakob     (1000) users      (100)      779 2018-10-04 13:57:57.000000 fava-1.9/fava/help/import.md
+-rw-r--r--   0 jakob     (1000) users      (100)     6395 2018-09-03 13:22:32.000000 fava-1.9/fava/help/options.md
+-rw-r--r--   0 jakob     (1000) users      (100)     4967 2018-09-18 09:58:42.000000 fava-1.9/fava/json_api.py
+drwxr-xr-x   0 jakob     (1000) users      (100)        0 2018-10-08 19:16:40.000000 fava-1.9/fava/plugins/
+-rw-r--r--   0 jakob     (1000) users      (100)     2409 2018-09-18 09:58:42.000000 fava-1.9/fava/plugins/link_documents.py
+-rw-r--r--   0 jakob     (1000) users      (100)      760 2018-09-18 09:58:42.000000 fava-1.9/fava/plugins/tag_discovered_documents.py
+-rw-r--r--   0 jakob     (1000) users      (100)     4232 2018-10-02 12:33:24.000000 fava-1.9/fava/serialisation.py
+drwxr-xr-x   0 jakob     (1000) users      (100)        0 2018-10-08 19:16:40.000000 fava-1.9/fava/static/
+drwxr-xr-x   0 jakob     (1000) users      (100)        0 2018-10-08 19:16:40.000000 fava-1.9/fava/static/css/
+-rw-r--r--   0 jakob     (1000) users      (100)    10801 2018-09-05 15:14:33.000000 fava-1.9/fava/static/css/base.css
+-rw-r--r--   0 jakob     (1000) users      (100)     3283 2018-07-25 18:39:36.000000 fava-1.9/fava/static/css/charts.css
+-rw-r--r--   0 jakob     (1000) users      (100)      878 2018-07-25 18:39:36.000000 fava-1.9/fava/static/css/components.css
+-rw-r--r--   0 jakob     (1000) users      (100)     2980 2018-09-05 15:46:26.000000 fava-1.9/fava/static/css/editor.css
+-rw-r--r--   0 jakob     (1000) users      (100)     1412 2018-10-04 13:57:57.000000 fava-1.9/fava/static/css/entry-forms.css
+-rw-r--r--   0 jakob     (1000) users      (100)     1283 2018-07-25 18:39:36.000000 fava-1.9/fava/static/css/fonts.css
+-rw-r--r--   0 jakob     (1000) users      (100)     3327 2018-07-25 18:39:36.000000 fava-1.9/fava/static/css/header.css
+-rw-r--r--   0 jakob     (1000) users      (100)      965 2018-07-25 18:39:36.000000 fava-1.9/fava/static/css/help.css
+-rw-r--r--   0 jakob     (1000) users      (100)     1258 2018-10-04 13:57:57.000000 fava-1.9/fava/static/css/ingest.css
+-rw-r--r--   0 jakob     (1000) users      (100)     4411 2018-09-05 15:14:33.000000 fava-1.9/fava/static/css/journal-table.css
+-rw-r--r--   0 jakob     (1000) users      (100)     1232 2018-07-25 18:39:36.000000 fava-1.9/fava/static/css/media-mobile.css
+-rw-r--r--   0 jakob     (1000) users      (100)      283 2018-07-25 18:39:36.000000 fava-1.9/fava/static/css/media-print.css
+-rw-r--r--   0 jakob     (1000) users      (100)     1892 2018-07-25 18:39:36.000000 fava-1.9/fava/static/css/overlay.css
+-rw-r--r--   0 jakob     (1000) users      (100)      803 2018-07-25 18:39:36.000000 fava-1.9/fava/static/css/query.css
+-rw-r--r--   0 jakob     (1000) users      (100)     3736 2018-07-25 18:39:36.000000 fava-1.9/fava/static/css/style.css
+-rw-r--r--   0 jakob     (1000) users      (100)     2833 2018-07-25 18:39:36.000000 fava-1.9/fava/static/css/tree-table.css
+drwxr-xr-x   0 jakob     (1000) users      (100)        0 2018-10-08 19:16:40.000000 fava-1.9/fava/static/gen/
+-rw-r--r--   0 jakob     (1000) users      (100)    19348 2018-10-08 16:23:56.000000 fava-1.9/fava/static/gen/FiraMono-Medium.woff
+-rw-r--r--   0 jakob     (1000) users      (100)    19320 2018-10-08 16:23:56.000000 fava-1.9/fava/static/gen/FiraMono-Regular.woff
+-rw-r--r--   0 jakob     (1000) users      (100)    34928 2018-10-08 16:23:56.000000 fava-1.9/fava/static/gen/FiraSans-Medium.woff
+-rw-r--r--   0 jakob     (1000) users      (100)    34764 2018-10-08 16:23:56.000000 fava-1.9/fava/static/gen/FiraSans-Regular.woff
+-rw-r--r--   0 jakob     (1000) users      (100)    19652 2018-10-08 16:23:56.000000 fava-1.9/fava/static/gen/SourceCodePro-Regular.woff
+-rw-r--r--   0 jakob     (1000) users      (100)    19852 2018-10-08 16:23:56.000000 fava-1.9/fava/static/gen/SourceCodePro-Semibold.woff
+-rw-r--r--   0 jakob     (1000) users      (100)    31888 2018-10-08 16:23:56.000000 fava-1.9/fava/static/gen/SourceSerifPro-Regular.woff
+-rw-r--r--   0 jakob     (1000) users      (100)    35128 2018-10-08 16:23:56.000000 fava-1.9/fava/static/gen/SourceSerifPro-Semibold.woff
+-rw-r--r--   0 jakob     (1000) users      (100)   840625 2018-10-08 16:23:56.000000 fava-1.9/fava/static/gen/app.js
+drwxr-xr-x   0 jakob     (1000) users      (100)        0 2018-10-08 19:16:40.000000 fava-1.9/fava/static/gen/codemirror/
+-rw-r--r--   0 jakob     (1000) users      (100)      507 2018-10-08 16:23:56.000000 fava-1.9/fava/static/gen/codemirror/addon-dialog-dialog.css
+-rw-r--r--   0 jakob     (1000) users      (100)      435 2018-10-08 16:23:56.000000 fava-1.9/fava/static/gen/codemirror/addon-fold-foldgutter.css
+-rw-r--r--   0 jakob     (1000) users      (100)      623 2018-10-08 16:23:56.000000 fava-1.9/fava/static/gen/codemirror/addon-hint-show-hint.css
+-rw-r--r--   0 jakob     (1000) users      (100)     8542 2018-10-08 16:23:56.000000 fava-1.9/fava/static/gen/codemirror/lib-codemirror.css
+drwxr-xr-x   0 jakob     (1000) users      (100)        0 2018-10-08 19:16:40.000000 fava-1.9/fava/static/images/
+-rw-r--r--   0 jakob     (1000) users      (100)     2802 2018-07-25 18:39:36.000000 fava-1.9/fava/static/images/favicon.ico
+-rw-r--r--   0 jakob     (1000) users      (100)     5374 2018-09-18 09:58:42.000000 fava-1.9/fava/template_filters.py
+drwxr-xr-x   0 jakob     (1000) users      (100)        0 2018-10-08 19:16:40.000000 fava-1.9/fava/templates/
+-rw-r--r--   0 jakob     (1000) users      (100)     1732 2018-07-25 18:39:36.000000 fava-1.9/fava/templates/_aside.html
+-rw-r--r--   0 jakob     (1000) users      (100)     4150 2018-07-25 18:39:36.000000 fava-1.9/fava/templates/_charts.html
+-rw-r--r--   0 jakob     (1000) users      (100)     2380 2018-07-25 18:39:36.000000 fava-1.9/fava/templates/_context.html
+-rw-r--r--   0 jakob     (1000) users      (100)     1156 2018-07-25 18:39:36.000000 fava-1.9/fava/templates/_entry_filters.html
+-rw-r--r--   0 jakob     (1000) users      (100)     3830 2018-10-04 13:57:57.000000 fava-1.9/fava/templates/_entry_forms.html
+-rw-r--r--   0 jakob     (1000) users      (100)      147 2018-07-25 18:39:36.000000 fava-1.9/fava/templates/_error.html
+-rw-r--r--   0 jakob     (1000) users      (100)      966 2018-07-25 18:39:36.000000 fava-1.9/fava/templates/_globals.html
+-rw-r--r--   0 jakob     (1000) users      (100)     9660 2018-09-05 15:14:33.000000 fava-1.9/fava/templates/_journal_table.html
+-rw-r--r--   0 jakob     (1000) users      (100)     6538 2018-07-25 18:39:36.000000 fava-1.9/fava/templates/_layout.html
+-rw-r--r--   0 jakob     (1000) users      (100)     2341 2018-07-25 18:39:36.000000 fava-1.9/fava/templates/_overlays.html
+-rw-r--r--   0 jakob     (1000) users      (100)     2663 2018-07-25 18:39:36.000000 fava-1.9/fava/templates/_query_table.html
+-rw-r--r--   0 jakob     (1000) users      (100)     8367 2018-07-25 18:39:36.000000 fava-1.9/fava/templates/_tree_table.html
+-rw-r--r--   0 jakob     (1000) users      (100)     2294 2018-07-25 18:39:36.000000 fava-1.9/fava/templates/account.html
+-rw-r--r--   0 jakob     (1000) users      (100)     1032 2018-07-25 18:39:36.000000 fava-1.9/fava/templates/balance_sheet.html
+-rw-r--r--   0 jakob     (1000) users      (100)      666 2018-07-25 18:39:36.000000 fava-1.9/fava/templates/beancount_file
+-rw-r--r--   0 jakob     (1000) users      (100)      821 2018-07-25 18:39:36.000000 fava-1.9/fava/templates/commodities.html
+-rw-r--r--   0 jakob     (1000) users      (100)     2094 2018-09-05 15:46:26.000000 fava-1.9/fava/templates/editor.html
+-rw-r--r--   0 jakob     (1000) users      (100)     1319 2018-07-25 18:39:36.000000 fava-1.9/fava/templates/errors.html
+-rw-r--r--   0 jakob     (1000) users      (100)      890 2018-07-25 18:39:36.000000 fava-1.9/fava/templates/events.html
+-rw-r--r--   0 jakob     (1000) users      (100)     1999 2018-10-02 12:33:24.000000 fava-1.9/fava/templates/extract.html
+-rw-r--r--   0 jakob     (1000) users      (100)      573 2018-07-25 18:39:36.000000 fava-1.9/fava/templates/help.html
+-rw-r--r--   0 jakob     (1000) users      (100)     2678 2018-07-25 18:39:36.000000 fava-1.9/fava/templates/holdings.html
+-rw-r--r--   0 jakob     (1000) users      (100)     1402 2018-10-04 14:04:02.000000 fava-1.9/fava/templates/import.html
+-rw-r--r--   0 jakob     (1000) users      (100)     1057 2018-07-25 18:39:36.000000 fava-1.9/fava/templates/income_statement.html
+-rw-r--r--   0 jakob     (1000) users      (100)      214 2018-07-25 18:39:36.000000 fava-1.9/fava/templates/journal.html
+drwxr-xr-x   0 jakob     (1000) users      (100)        0 2018-10-08 19:16:40.000000 fava-1.9/fava/templates/macros/
+-rw-r--r--   0 jakob     (1000) users      (100)     2566 2018-07-25 18:39:36.000000 fava-1.9/fava/templates/macros/_account_macros.html
+-rw-r--r--   0 jakob     (1000) users      (100)     1101 2018-07-25 18:39:36.000000 fava-1.9/fava/templates/options.html
+-rw-r--r--   0 jakob     (1000) users      (100)     1691 2018-07-25 18:39:36.000000 fava-1.9/fava/templates/query.html
+-rw-r--r--   0 jakob     (1000) users      (100)     4525 2018-07-25 18:39:36.000000 fava-1.9/fava/templates/statistics.html
+-rw-r--r--   0 jakob     (1000) users      (100)      469 2018-07-25 18:39:36.000000 fava-1.9/fava/templates/trial_balance.html
+drwxr-xr-x   0 jakob     (1000) users      (100)        0 2018-10-08 19:16:40.000000 fava-1.9/fava/translations/
+-rw-r--r--   0 jakob     (1000) users      (100)       97 2018-07-25 18:39:36.000000 fava-1.9/fava/translations/babel.conf
+drwxr-xr-x   0 jakob     (1000) users      (100)        0 2018-10-08 19:16:40.000000 fava-1.9/fava/translations/de/
+drwxr-xr-x   0 jakob     (1000) users      (100)        0 2018-10-08 19:16:40.000000 fava-1.9/fava/translations/de/LC_MESSAGES/
+-rw-r--r--   0 jakob     (1000) users      (100)     3864 2018-10-08 19:10:02.000000 fava-1.9/fava/translations/de/LC_MESSAGES/messages.mo
+-rw-r--r--   0 jakob     (1000) users      (100)    10875 2018-10-08 19:09:55.000000 fava-1.9/fava/translations/de/LC_MESSAGES/messages.po
+drwxr-xr-x   0 jakob     (1000) users      (100)        0 2018-10-08 19:16:40.000000 fava-1.9/fava/translations/es/
+drwxr-xr-x   0 jakob     (1000) users      (100)        0 2018-10-08 19:16:40.000000 fava-1.9/fava/translations/es/LC_MESSAGES/
+-rw-r--r--   0 jakob     (1000) users      (100)     3259 2018-10-08 19:10:08.000000 fava-1.9/fava/translations/es/LC_MESSAGES/messages.mo
+-rw-r--r--   0 jakob     (1000) users      (100)    10732 2018-10-08 19:10:06.000000 fava-1.9/fava/translations/es/LC_MESSAGES/messages.po
+drwxr-xr-x   0 jakob     (1000) users      (100)        0 2018-10-08 19:16:40.000000 fava-1.9/fava/translations/fr/
+drwxr-xr-x   0 jakob     (1000) users      (100)        0 2018-10-08 19:16:40.000000 fava-1.9/fava/translations/fr/LC_MESSAGES/
+-rw-r--r--   0 jakob     (1000) users      (100)     3282 2018-10-08 19:10:15.000000 fava-1.9/fava/translations/fr/LC_MESSAGES/messages.mo
+-rw-r--r--   0 jakob     (1000) users      (100)    10737 2018-10-08 19:10:10.000000 fava-1.9/fava/translations/fr/LC_MESSAGES/messages.po
+-rw-r--r--   0 jakob     (1000) users      (100)    10160 2018-10-08 19:09:32.000000 fava-1.9/fava/translations/messages.pot
+drwxr-xr-x   0 jakob     (1000) users      (100)        0 2018-10-08 19:16:40.000000 fava-1.9/fava/translations/nl/
+drwxr-xr-x   0 jakob     (1000) users      (100)        0 2018-10-08 19:16:40.000000 fava-1.9/fava/translations/nl/LC_MESSAGES/
+-rw-r--r--   0 jakob     (1000) users      (100)     3219 2018-10-08 19:10:21.000000 fava-1.9/fava/translations/nl/LC_MESSAGES/messages.mo
+-rw-r--r--   0 jakob     (1000) users      (100)    10717 2018-10-08 19:10:18.000000 fava-1.9/fava/translations/nl/LC_MESSAGES/messages.po
+drwxr-xr-x   0 jakob     (1000) users      (100)        0 2018-10-08 19:16:40.000000 fava-1.9/fava/translations/pt/
+drwxr-xr-x   0 jakob     (1000) users      (100)        0 2018-10-08 19:16:40.000000 fava-1.9/fava/translations/pt/LC_MESSAGES/
+-rw-r--r--   0 jakob     (1000) users      (100)     3160 2018-10-08 19:10:25.000000 fava-1.9/fava/translations/pt/LC_MESSAGES/messages.mo
+-rw-r--r--   0 jakob     (1000) users      (100)    10796 2018-10-08 19:10:23.000000 fava-1.9/fava/translations/pt/LC_MESSAGES/messages.po
+drwxr-xr-x   0 jakob     (1000) users      (100)        0 2018-10-08 19:16:40.000000 fava-1.9/fava/translations/ru/
+drwxr-xr-x   0 jakob     (1000) users      (100)        0 2018-10-08 19:16:40.000000 fava-1.9/fava/translations/ru/LC_MESSAGES/
+-rw-r--r--   0 jakob     (1000) users      (100)     3928 2018-10-08 19:10:29.000000 fava-1.9/fava/translations/ru/LC_MESSAGES/messages.mo
+-rw-r--r--   0 jakob     (1000) users      (100)    11383 2018-10-08 19:10:27.000000 fava-1.9/fava/translations/ru/LC_MESSAGES/messages.po
+drwxr-xr-x   0 jakob     (1000) users      (100)        0 2018-10-08 19:16:40.000000 fava-1.9/fava/translations/sk/
+drwxr-xr-x   0 jakob     (1000) users      (100)        0 2018-10-08 19:16:40.000000 fava-1.9/fava/translations/sk/LC_MESSAGES/
+-rw-r--r--   0 jakob     (1000) users      (100)     5426 2018-10-08 19:10:49.000000 fava-1.9/fava/translations/sk/LC_MESSAGES/messages.mo
+-rw-r--r--   0 jakob     (1000) users      (100)    11533 2018-10-08 19:10:46.000000 fava-1.9/fava/translations/sk/LC_MESSAGES/messages.po
+drwxr-xr-x   0 jakob     (1000) users      (100)        0 2018-10-08 19:16:40.000000 fava-1.9/fava/translations/uk/
+drwxr-xr-x   0 jakob     (1000) users      (100)        0 2018-10-08 19:16:40.000000 fava-1.9/fava/translations/uk/LC_MESSAGES/
+-rw-r--r--   0 jakob     (1000) users      (100)     6707 2018-10-08 19:10:52.000000 fava-1.9/fava/translations/uk/LC_MESSAGES/messages.mo
+-rw-r--r--   0 jakob     (1000) users      (100)    12773 2018-10-08 19:10:51.000000 fava-1.9/fava/translations/uk/LC_MESSAGES/messages.po
+drwxr-xr-x   0 jakob     (1000) users      (100)        0 2018-10-08 19:16:40.000000 fava-1.9/fava/translations/zh/
+drwxr-xr-x   0 jakob     (1000) users      (100)        0 2018-10-08 19:16:40.000000 fava-1.9/fava/translations/zh/LC_MESSAGES/
+-rw-r--r--   0 jakob     (1000) users      (100)     3193 2018-10-08 19:10:35.000000 fava-1.9/fava/translations/zh/LC_MESSAGES/messages.mo
+-rw-r--r--   0 jakob     (1000) users      (100)    10520 2018-10-08 19:10:31.000000 fava-1.9/fava/translations/zh/LC_MESSAGES/messages.po
+drwxr-xr-x   0 jakob     (1000) users      (100)        0 2018-10-08 19:16:40.000000 fava-1.9/fava/util/
+-rw-r--r--   0 jakob     (1000) users      (100)     2619 2018-10-02 12:33:28.000000 fava-1.9/fava/util/__init__.py
+-rw-r--r--   0 jakob     (1000) users      (100)    11305 2018-09-18 09:58:42.000000 fava-1.9/fava/util/date.py
+-rw-r--r--   0 jakob     (1000) users      (100)     2096 2018-09-18 09:58:42.000000 fava-1.9/fava/util/excel.py
+-rw-r--r--   0 jakob     (1000) users      (100)     2286 2018-09-18 09:58:42.000000 fava-1.9/fava/util/ranking.py
+drwxr-xr-x   0 jakob     (1000) users      (100)        0 2018-10-08 19:16:40.000000 fava-1.9/fava.egg-info/
+-rw-r--r--   0 jakob     (1000) users      (100)     2901 2018-10-08 19:16:40.000000 fava-1.9/fava.egg-info/PKG-INFO
+-rw-r--r--   0 jakob     (1000) users      (100)     3897 2018-10-08 19:16:40.000000 fava-1.9/fava.egg-info/SOURCES.txt
+-rw-r--r--   0 jakob     (1000) users      (100)        1 2018-10-08 19:16:40.000000 fava-1.9/fava.egg-info/dependency_links.txt
+-rw-r--r--   0 jakob     (1000) users      (100)       40 2018-10-08 19:16:40.000000 fava-1.9/fava.egg-info/entry_points.txt
+-rw-r--r--   0 jakob     (1000) users      (100)        1 2018-07-25 18:40:48.000000 fava-1.9/fava.egg-info/not-zip-safe
+-rw-r--r--   0 jakob     (1000) users      (100)      252 2018-10-08 19:16:40.000000 fava-1.9/fava.egg-info/requires.txt
+-rw-r--r--   0 jakob     (1000) users      (100)        5 2018-10-08 19:16:40.000000 fava-1.9/fava.egg-info/top_level.txt
+-rw-r--r--   0 jakob     (1000) users      (100)       38 2018-10-08 19:16:40.000000 fava-1.9/setup.cfg
+-rw-r--r--   0 jakob     (1000) users      (100)     2305 2018-07-25 18:39:36.000000 fava-1.9/setup.py
```

### Comparing `fava-1.8/fava/core/__init__.py` & `fava-1.9/fava/core/__init__.py`

 * *Files 2% similar despite different names*

```diff
@@ -108,19 +108,15 @@
         'fava_options', '_filters', '_is_encrypted', 'options', 'price_map',
         'root_account', 'root_tree', '_watcher'] + MODULES
 
     def __init__(self, path):
         #: The path to the main Beancount file.
         self.beancount_file_path = path
         self._is_encrypted = is_encrypted_file(path)
-        self._filters = {
-            'account': AccountFilter(),
-            'filter': AdvancedFilter(),
-            'time': TimeFilter(),
-        }
+        self._filters = {}
 
         #: An :class:`AttributesModule` instance.
         self.attributes = AttributesModule(self)
 
         #: A :class:`.BudgetModule` instance.
         self.budgets = BudgetModule(self)
 
@@ -201,14 +197,20 @@
 
         self.fava_options, errors = parse_options(entries_by_type[Custom])
         self.errors.extend(errors)
 
         for mod in MODULES:
             getattr(self, mod).load_file()
 
+        self._filters = {
+            'account': AccountFilter(self.options, self.fava_options),
+            'filter': AdvancedFilter(self.options, self.fava_options),
+            'time': TimeFilter(self.options, self.fava_options),
+        }
+
         self.filter(True)
 
     # pylint: disable=attribute-defined-outside-init
     def filter(self, force=False, **kwargs):
         """Set and apply (if necessary) filters."""
         changed = False
         for filter_name, value in kwargs.items():
@@ -217,15 +219,15 @@
 
         if not (changed or force):
             return
 
         self.entries = self.all_entries
 
         for filter_class in self._filters.values():
-            self.entries = filter_class.apply(self.entries, self.options)
+            self.entries = filter_class.apply(self.entries)
 
         self.root_account = realization.realize(self.entries,
                                                 self.account_types)
         self.root_tree = Tree(self.entries)
 
         self._date_first, self._date_last = \
             getters.get_min_max_dates(self.entries, (Transaction))
```

### Comparing `fava-1.8/fava/core/attributes.py` & `fava-1.9/fava/core/attributes.py`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/core/budgets.py` & `fava-1.9/fava/core/budgets.py`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/core/charts.py` & `fava-1.9/fava/core/charts.py`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/core/fava_options.py` & `fava-1.9/fava/core/fava_options.py`

 * *Files 6% similar despite different names*

```diff
@@ -15,14 +15,15 @@
 
 DEFAULTS = {
     'account-journal-include-children': True,
     'currency-column': 61,
     'auto-reload': False,
     'default-file': None,
     'extensions': [],
+    'fiscal-year-end': '12-31',
     'import-config': None,
     'import-dirs': [],
     'insert-entry': [],
     'interval': 'month',
     'journal-show': ['transaction', 'balance', 'note', 'document', 'custom',
                      'budget', 'query'],
     'journal-show-document': ['discovered', 'statement'],
@@ -65,14 +66,15 @@
 
 STR_OPTS = [
     'import-config',
     'interval',
     'language',
     'locale',
     'unrealized',
+    'fiscal-year-end',
 ]
 
 
 def parse_options(custom_entries):
     """Parse custom entries for Fava options.
 
     The format for option entries is the following:
```

### Comparing `fava-1.8/fava/core/file.py` & `fava-1.9/fava/core/file.py`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/core/filters.py` & `fava-1.9/fava/core/filters.py`

 * *Files 3% similar despite different names*

```diff
@@ -265,15 +265,17 @@
 
         p[0] = _key
 
 
 class EntryFilter():
     """Filters a list of entries. """
 
-    def __init__(self):
+    def __init__(self, options, fava_options):
+        self.options = options
+        self.fava_options = fava_options
         self.value = None
 
     def set(self, value):
         """Set the filter.
 
         Subclasses should check for validity of the value in this method.
         """
@@ -281,77 +283,80 @@
             return False
         self.value = value
         return True
 
     def _include_entry(self, entry):
         raise NotImplementedError
 
-    def _filter(self, entries, _):
+    def _filter(self, entries):
         return [entry for entry in entries if self._include_entry(entry)]
 
-    def apply(self, entries, options):
+    def apply(self, entries):
         """Apply filter.
 
         Args:
             entries: a list of entries.
             options: an options_map.
 
         Returns:
             A list of filtered entries.
 
         """
         if self.value:
-            return self._filter(entries, options)
+            return self._filter(entries)
         return entries
 
     def __bool__(self):
         return bool(self.value)
 
 
 class TimeFilter(EntryFilter):  # pylint: disable=abstract-method
     """Filter by dates."""
 
-    def __init__(self):
-        super().__init__()
+    def __init__(self, *args):
+        super().__init__(*args)
         self.begin_date = None
         self.end_date = None
 
     def set(self, value):
         if value == self.value:
             return False
         self.value = value
         if not self.value:
             return True
 
-        self.begin_date, self.end_date = parse_date(self.value)
+        self.begin_date, self.end_date = parse_date(
+            self.value,
+            self.fava_options['fiscal-year-end']
+        )
         if not self.begin_date:
             self.value = None
             raise FilterException('time',
                                   'Failed to parse date: {}'.format(value))
         return True
 
-    def _filter(self, entries, options):
+    def _filter(self, entries):
         entries, _ = summarize.clamp_opt(entries, self.begin_date,
-                                         self.end_date, options)
+                                         self.end_date, self.options)
         return entries
 
 
 LEXER = FilterSyntaxLexer()
 PARSE = ply.yacc.yacc(
     errorlog=ply.yacc.NullLogger(),
     write_tables=False,
     debug=False,
     module=FilterSyntaxParser()).parse
 
 
 class AdvancedFilter(EntryFilter):
     """Filter by tags and links and keys."""
 
-    def __init__(self):
-        super().__init__()
+    def __init__(self, *args):
+        super().__init__(*args)
         self._include = None
 
     def set(self, value):
         if value == self.value:
             return False
         self.value = value
         if value and value.strip():
@@ -396,16 +401,16 @@
 
 class AccountFilter(EntryFilter):
     """Filter by account.
 
     The filter string can either a regular expression or a parent account.
     """
 
-    def __init__(self):
-        super().__init__()
+    def __init__(self, *args):
+        super().__init__(*args)
         self.match = None
 
     def set(self, value):
         if value == self.value:
             return False
         self.value = value
         self.match = Match(value or '')
```

### Comparing `fava-1.8/fava/core/helpers.py` & `fava-1.9/fava/core/helpers.py`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/core/ingest.py` & `fava-1.9/fava/core/ingest.py`

 * *Files 2% similar despite different names*

```diff
@@ -76,19 +76,22 @@
         """
         if not filename or not importer_name:
             return []
 
         if os.stat(self.module_path).st_mtime_ns > self.mtime:
             self.load_file()
 
-        new_entries, _ = extract.extract_from_file(
+        new_entries = extract.extract_from_file(
             filename,
             self.importers.get(importer_name),
             existing_entries=self.ledger.all_entries)
 
+        if isinstance(new_entries, tuple):
+            new_entries, _ = new_entries
+
         return new_entries
 
     @staticmethod
     def file_account(filename, importer):
         """Account for the given file.
 
         Args:
```

### Comparing `fava-1.8/fava/core/inventory.py` & `fava-1.9/fava/core/inventory.py`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/core/misc.py` & `fava-1.9/fava/core/misc.py`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/core/number.py` & `fava-1.9/fava/core/number.py`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/core/query_shell.py` & `fava-1.9/fava/core/query_shell.py`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/core/tree.py` & `fava-1.9/fava/core/tree.py`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/core/watcher.py` & `fava-1.9/fava/core/watcher.py`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/ext/__init__.py` & `fava-1.9/fava/ext/__init__.py`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/ext/auto_commit.py` & `fava-1.9/fava/ext/auto_commit.py`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/help/_index.md` & `fava-1.9/fava/help/_index.md`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/help/beancount_syntax.md` & `fava-1.9/fava/help/beancount_syntax.md`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/help/budgets.md` & `fava-1.9/fava/help/budgets.md`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/help/extensions.md` & `fava-1.9/fava/help/extensions.md`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/help/features.md` & `fava-1.9/fava/help/features.md`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/help/filters.md` & `fava-1.9/fava/help/filters.md`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/help/import.md` & `fava-1.9/fava/help/import.md`

 * *Files 21% similar despite different names*

```diff
@@ -1,13 +1,14 @@
 Fava can use Beancount's import system to semi-automatically import entries
 into your Beancount ledger. See [Importing External Data in
 Beancount](http://furius.ca/beancount/doc/ingest) for more information on how
 to write importers.
 
 Set the `import-config` option to point to your import config and set
 `import-dirs` to the directories that contain the files that you want to
-import.
+import. And if you wish to save new entries elsewhere than main file - use
+`insert-entry` option.
 
 Fava currently only supports entries of type `Transaction` and `Balance`. Set
 the special metadata key `__source__` to display the corresponding text
 (CSV-row, XML-fragment, etc.) for the entry in the list of entries to import.
 Note that this metadata will be stripped before saving the entry to file.
```

### Comparing `fava-1.8/fava/help/options.md` & `fava-1.9/fava/help/options.md`

 * *Files 5% similar despite different names*

```diff
@@ -56,14 +56,33 @@
 Default: `month`
 
 The default interval that charts and the account reports by interval use.
 The possible options are `day`, `week`, `month`, `quarter`, and `year`.
 
 ---
 
+## `fiscal-year-end`
+
+Default: `12-31`
+
+The last day of the fiscal (financial or tax) period for accounting purposes in 
+`%m-%d` format.  Allows for the use of `FY2018`, `FY2018-Q3`, `fiscal_year` and 
+`fiscal_quarter` in the time filter.
+
+Examples are:
+
+* `09-30` - US federal government
+* `06-30` - Australia / NZ
+* `04-05` - UK
+
+See [Fiscal Year on WikiPedia](https://en.wikipedia.org/wiki/Fiscal_year) for 
+more examples.
+
+---
+
 ## `extensions`
 
 Default: Not set.
 
 A space-separated list of Python modules to load as extensions. The directory
 of the main Beancount file is searched too, so for example a `my_extension.py`
 right next to it could be used by giving `my_extension`. Note that Python has a
@@ -111,16 +130,20 @@
 
 ---
 
 ## `journal-show`
 
 Default: `transaction balance note document custom budget query`
 
-The entry types given in this list will be shown in the Journal report.
-All other types will be hidden and can be toggled using the buttons.
+The entry types and other elements given in this list will be shown in the
+Journal report. Supported values are entry type names, as well as well as
+the special values "metadata" and "postings" that determine the default
+visibility of the corresponding transaction parts.
+
+All other elements will be hidden and can be toggled using the buttons.
 
 ---
 
 ## `journal-show-transaction`
 
 Default: `cleared pending`
```

### Comparing `fava-1.8/fava/plugins/link_statements.py` & `fava-1.9/fava/plugins/link_documents.py`

 * *Files 17% similar despite different names*

```diff
@@ -1,61 +1,62 @@
-"""Beancount plugin to link statements to documents.
+"""Beancount plugin to link transactions to documents.
+
+It goes through all transactions with a `document` metadata-key, and tries to
+associate them to Document entries. It then adds a link from transactions to
+documents, as well as the "#linked" tag.
 
-It goes through all transactions with a `statement` metadata-key, and tries to
-match them to Document entries. It then adds a link to the transaction and the
-document, and the tag "#statement" to the document.
 """
 
 import collections
 from os.path import join, dirname, normpath, basename
 
 from beancount.core import data
 from beancount.core.compare import hash_entry
 
-StatementDocumentError = collections.namedtuple('StatementDocumentError',
-                                                'source message entry')
+DocumentError = collections.namedtuple('DocumentError',
+                                       'source message entry')
 
-__plugins__ = ['link_statements']
+__plugins__ = ['link_documents']
 
 
-def link_statements(entries, _):
+def link_documents(entries, _):
     errors = []
 
     all_documents = [(index, entry) for index, entry in enumerate(entries)
                      if isinstance(entry, data.Document)]
 
     transactions = [(index, entry) for index, entry in enumerate(entries)
                     if isinstance(entry, data.Transaction)]
 
     for index, entry in transactions:
-        statements = [value for key, value in entry.meta.items()
-                      if key.startswith('statement')]
+        disk_docs = [value for key, value in entry.meta.items()
+                     if key.startswith('document')]
 
         _hash = hash_entry(entry)[:8]
-        for statement in statements:
-            statement_path = normpath(join(dirname(entry.meta['filename']),
-                                           statement))
+        for disk_doc in disk_docs:
+            disk_doc_path = normpath(join(dirname(entry.meta['filename']),
+                                          disk_doc))
             documents = [(j, document) for j, document in all_documents
-                         if (document.filename == statement_path) or
+                         if (document.filename == disk_doc_path) or
                          (document.account in
                           [pos.account for pos in entry.postings] and
-                          basename(document.filename) == statement)]
+                          basename(document.filename) == disk_doc)]
 
             if not documents:
                 errors.append(
-                    StatementDocumentError(
+                    DocumentError(
                         entry.meta,
-                        "Statement Document not found: {}".format(statement),
+                        "Document not found: {}".format(disk_doc),
                         entry))
                 continue
 
             for j, document in documents:
                 tags = set(document.tags).union(
-                    ['statement']).difference(['discovered']) \
-                    if document.tags else set(['statement'])
+                    ['linked']).difference(['discovered']) \
+                    if document.tags else set(['linked'])
                 links = set(document.links).union([_hash]) \
                     if document.links else set([_hash])
                 entries[j] = document._replace(links=links, tags=tags)
 
             links = set(entry.links).union([_hash]) \
                 if entry.links else set([_hash])
             entries[index] = entry._replace(links=links)
```

### Comparing `fava-1.8/fava/plugins/tag_discovered_documents.py` & `fava-1.9/fava/plugins/tag_discovered_documents.py`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/static/css/base.css` & `fava-1.9/fava/static/css/base.css`

 * *Files 1% similar despite different names*

```diff
@@ -181,16 +181,16 @@
 }
 
 select {
   font-size: inherit;
   margin: 0 .5em 0 0;
 }
 
-input {
-  /* remove dropdown triangle */
+input:invalid {
+  border: 1px solid var(--color-error);
 }
 
 input[type='text']::-webkit-calendar-picker-indicator {
   display: none;
 }
 
 input[type='date']::-webkit-inner-spin-button,
```

### Comparing `fava-1.8/fava/static/css/charts.css` & `fava-1.9/fava/static/css/charts.css`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/static/css/components.css` & `fava-1.9/fava/static/css/components.css`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/static/css/editor.css` & `fava-1.9/fava/static/css/editor.css`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/static/css/entry-forms.css` & `fava-1.9/fava/static/css/entry-forms.css`

 * *Files 4% similar despite different names*

```diff
@@ -5,31 +5,36 @@
   width: 100%;
 }
 
 .entry-form label {
   display: none;
 }
 
-.entry-form .number,
-.entry-form .currency {
-  width: 100px;
+.entry-form .amount {
+  width: 220px;
 }
 
 .entry-form input[name='flag'] {
   padding-left: 2px;
   padding-right: 2px;
   text-align: center;
   width: 1.5em;
 }
 
 .entry-form input.account,
-.entry-form input[name='narration'],
+.entry-form input[name='narration'] {
+  flex-basis: 200px;
+  flex-grow: 1;
+  min-width: 20em;
+}
+
 .entry-form input[name='payee'] {
+  flex-basis: 100px;
   flex-grow: 1;
-  min-width: 15em;
+  min-width: 10em;
 }
 
 .entry-form input.metadata-value {
   flex-grow: 1;
   max-width: 15em;
 }
 
@@ -55,16 +60,16 @@
   display: initial;
 }
 
 .entry-form .posting {
   padding-left: 50px;
 }
 
-.entry-form .posting:last-child .currency {
-  width: 72px;
+.entry-form .posting:last-child .amount {
+  width: 192px;
 }
 
 .entry-form .metadata {
   font-size: .8em;
   padding-left: 56px;
 }
```

### Comparing `fava-1.8/fava/static/css/fonts.css` & `fava-1.9/fava/static/css/fonts.css`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/static/css/header.css` & `fava-1.9/fava/static/css/header.css`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/static/css/help.css` & `fava-1.9/fava/static/css/help.css`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/static/css/ingest.css` & `fava-1.9/fava/static/css/ingest.css`

 * *Files 16% similar despite different names*

```diff
@@ -14,35 +14,41 @@
   flex-grow: 1;
   margin-right: .5em;
   overflow: auto;
 }
 
 .ingest-row .source pre {
   font-size: .9em;
+  white-space: pre-wrap;
 }
 
 .ingest-row .entry-form {
   flex-shrink: 0;
+  max-width: 1000px;
   min-width: 600px;
 }
 
+.ingest-row .source.hidden + .entry-form {
+  flex: 1;
+}
+
 .ingest-row input[name='payee'] {
   width: 140px;
 }
 
 .ingest-row .actions {
   font-size: .8em;
   width: 60px;
 }
 
 .ingest-row .actions .inner {
   min-width: 100px;
   text-align: left;
   transform: rotate(90deg);
-  transform-origin: 30% 50%;
+  transform-origin: 28% 50%;
 }
 
 .ingest-row .actions label {
   display: inline-block;
   margin: 0;
 }
```

### Comparing `fava-1.8/fava/static/css/journal-table.css` & `fava-1.9/fava/static/css/journal-table.css`

 * *Files 6% similar despite different names*

```diff
@@ -54,15 +54,15 @@
   background-color: var(--color-table-header-background);
   color: var(--color-table-header-text);
 }
 
 .journal > li,
 .journal.show-custom .custom.budget,
 .journal.show-document .document.discovered,
-.journal.show-document .document.statement,
+.journal.show-document .document.linked,
 .journal .metadata,
 .journal .postings {
   display: none;
 }
 
 .journal .head,
 .journal.show-balance .balance,
@@ -71,47 +71,48 @@
 .journal.show-document .document,
 .journal.show-note .note,
 .journal.show-open .open,
 .journal.show-pad .pad,
 .journal.show-query .query,
 .journal.show-metadata .metadata,
 .journal.show-postings .postings,
-.transaction.show-postings .postings {
+.transaction.show-postings .postings,
+.transaction.show-postings .metadata {
   display: block;
 }
 
 .journal.show-transaction.show-cleared .transaction.cleared,
 .journal.show-transaction.show-pending .transaction.pending,
 .journal.show-transaction.show-other .transaction.other,
 .journal.show-document.show-discovered .document.discovered,
-.journal.show-document.show-statement .document.statement,
+.journal.show-document.show-linked .document.linked,
 .journal.show-custom.show-budget .custom.budget {
   display: block;
 }
 
 .journal p,
 .journal dl {
   border-bottom: thin solid var(--color-table-border);
 }
 
+.journal .payee {
+  cursor: pointer;
+}
+
 .journal .postings {
   background-color: var(--color-journal-postings);
   font-size: .9em;
   opacity: .8;
 }
 
 .journal .postings .num {
   line-height: 16px;
   overflow: hidden;
 }
 
-.journal .transaction {
-  cursor: pointer;
-}
-
 /* Metadata */
 .journal dl {
   font-size: .9em;
   margin: 0;
   padding: 2px 0;
 }
 
@@ -121,14 +122,15 @@
   float: left;
   margin-left: 9rem;
   min-width: 4rem;
   width: auto;
 }
 
 .journal dd {
+  cursor: pointer;
   margin-left: 15rem;
 }
 
 .journal p > .num {
   border-left: 1px solid var(--color-table-border);
   width: 9rem;
 }
@@ -205,14 +207,15 @@
 
 .journal .document .filename {
   margin-left: 1em;
 }
 
 .journal .indicators {
   align-items: center;
+  cursor: pointer;
   display: flex;
   flex-shrink: 3;
   flex-wrap: wrap;
   justify-content: flex-end;
 }
 
 .journal .indicators span {
```

### Comparing `fava-1.8/fava/static/css/media-mobile.css` & `fava-1.9/fava/static/css/media-mobile.css`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/static/css/overlay.css` & `fava-1.9/fava/static/css/overlay.css`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/static/css/query.css` & `fava-1.9/fava/static/css/query.css`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/static/css/style.css` & `fava-1.9/fava/static/css/style.css`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/static/css/tree-table.css` & `fava-1.9/fava/static/css/tree-table.css`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/static/gen/codemirror/addon-hint-show-hint.css` & `fava-1.9/fava/static/gen/codemirror/addon-hint-show-hint.css`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/static/gen/codemirror/lib-codemirror.css` & `fava-1.9/fava/static/gen/codemirror/lib-codemirror.css`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/static/gen/FiraMono-Medium.woff` & `fava-1.9/fava/static/gen/FiraMono-Medium.woff`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/static/gen/FiraMono-Regular.woff` & `fava-1.9/fava/static/gen/FiraMono-Regular.woff`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/static/gen/FiraSans-Medium.woff` & `fava-1.9/fava/static/gen/FiraSans-Medium.woff`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/static/gen/FiraSans-Regular.woff` & `fava-1.9/fava/static/gen/FiraSans-Regular.woff`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/static/gen/SourceCodePro-Regular.woff` & `fava-1.9/fava/static/gen/SourceCodePro-Regular.woff`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/static/gen/SourceCodePro-Semibold.woff` & `fava-1.9/fava/static/gen/SourceCodePro-Semibold.woff`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/static/gen/SourceSerifPro-Regular.woff` & `fava-1.9/fava/static/gen/SourceSerifPro-Regular.woff`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/static/gen/SourceSerifPro-Semibold.woff` & `fava-1.9/fava/static/gen/SourceSerifPro-Semibold.woff`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/static/gen/app.js` & `fava-1.9/fava/static/gen/app.js`

 * *Files 17% similar despite different names*

#### js-beautify {}

```diff
@@ -1,320 +1,10 @@
 (function() {
     'use strict';
 
-    var commonjsGlobal = typeof window !== 'undefined' ? window : typeof global !== 'undefined' ? global : typeof self !== 'undefined' ? self : {};
-
-    function createCommonjsModule(fn, module) {
-        return module = {
-            exports: {}
-        }, fn(module, module.exports), module.exports;
-    }
-
-    var urlSearchParams_node = createCommonjsModule(function(module) {
-
-        function URLSearchParams(query) {
-            var
-                index, key, value,
-                pairs, i, length,
-                dict = Object.create(null);
-            this[secret] = dict;
-            if (!query) {
-                return;
-            }
-            if (typeof query === 'string') {
-                if (query.charAt(0) === '?') {
-                    query = query.slice(1);
-                }
-                for (
-                    pairs = query.split('&'),
-                    i = 0,
-                    length = pairs.length; i < length; i++
-                ) {
-                    value = pairs[i];
-                    index = value.indexOf('=');
-                    if (-1 < index) {
-                        appendTo(
-                            dict,
-                            decode(value.slice(0, index)),
-                            decode(value.slice(index + 1))
-                        );
-                    } else if (value.length) {
-                        appendTo(
-                            dict,
-                            decode(value),
-                            ''
-                        );
-                    }
-                }
-            } else {
-                if (isArray(query)) {
-                    for (
-                        i = 0,
-                        length = query.length; i < length; i++
-                    ) {
-                        value = query[i];
-                        appendTo(dict, value[0], value[1]);
-                    }
-                } else {
-                    for (key in query) {
-                        appendTo(dict, key, query[key]);
-                    }
-                }
-            }
-        }
-
-        var
-            isArray = Array.isArray,
-            URLSearchParamsProto = URLSearchParams.prototype,
-            find = /[!'\(\)~]|%20|%00/g,
-            plus = /\+/g,
-            replace = {
-                '!': '%21',
-                "'": '%27',
-                '(': '%28',
-                ')': '%29',
-                '~': '%7E',
-                '%20': '+',
-                '%00': '\x00'
-            },
-            replacer = function(match) {
-                return replace[match];
-            },
-            secret = '__URLSearchParams__:' + Math.random();
-
-        function appendTo(dict, name, value) {
-            if (name in dict) {
-                dict[name].push('' + value);
-            } else {
-                dict[name] = isArray(value) ? value : ['' + value];
-            }
-        }
-
-        function decode(str) {
-            return decodeURIComponent(str.replace(plus, ' '));
-        }
-
-        function encode(str) {
-            return encodeURIComponent(str).replace(find, replacer);
-        }
-
-        URLSearchParamsProto.append = function append(name, value) {
-            appendTo(this[secret], name, value);
-        };
-
-        URLSearchParamsProto.delete = function del(name) {
-            delete this[secret][name];
-        };
-
-        URLSearchParamsProto.get = function get(name) {
-            var dict = this[secret];
-            return name in dict ? dict[name][0] : null;
-        };
-
-        URLSearchParamsProto.getAll = function getAll(name) {
-            var dict = this[secret];
-            return name in dict ? dict[name].slice(0) : [];
-        };
-
-        URLSearchParamsProto.has = function has(name) {
-            return name in this[secret];
-        };
-
-        URLSearchParamsProto.set = function set(name, value) {
-            this[secret][name] = ['' + value];
-        };
-
-        URLSearchParamsProto.forEach = function forEach(callback, thisArg) {
-            var dict = this[secret];
-            Object.getOwnPropertyNames(dict).forEach(function(name) {
-                dict[name].forEach(function(value) {
-                    callback.call(thisArg, value, name, this);
-                }, this);
-            }, this);
-        };
-
-        /*
-        URLSearchParamsProto.toBody = function() {
-          return new Blob(
-            [this.toString()],
-            {type: 'application/x-www-form-urlencoded'}
-          );
-        };
-        */
-
-        URLSearchParamsProto.toJSON = function toJSON() {
-            return {};
-        };
-
-        URLSearchParamsProto.toString = function toString() {
-            var dict = this[secret],
-                query = [],
-                i, key, name, value;
-            for (key in dict) {
-                name = encode(key);
-                for (
-                    i = 0,
-                    value = dict[key]; i < value.length; i++
-                ) {
-                    query.push(name + '=' + encode(value[i]));
-                }
-            }
-            return query.join('&');
-        };
-
-        URLSearchParams = (module.exports = commonjsGlobal.URLSearchParams || URLSearchParams);
-
-        (function(URLSearchParamsProto) {
-
-            var iterable = (function() {
-                try {
-                    return !!Symbol.iterator;
-                } catch (error) {
-                    return false;
-                }
-            }());
-
-            // mostly related to issue #24
-            if (!('forEach' in URLSearchParamsProto)) {
-                URLSearchParamsProto.forEach = function forEach(callback, thisArg) {
-                    var names = Object.create(null);
-                    this.toString()
-                        .replace(/=[\s\S]*?(?:&|$)/g, '=')
-                        .split('=')
-                        .forEach(function(name) {
-                            if (!name.length || name in names) {
-                                return;
-                            }
-                            (names[name] = this.getAll(name)).forEach(function(value) {
-                                callback.call(thisArg, value, name, this);
-                            }, this);
-                        }, this);
-                };
-            }
-
-            if (!('keys' in URLSearchParamsProto)) {
-                URLSearchParamsProto.keys = function keys() {
-                    var items = [];
-                    this.forEach(function(value, name) {
-                        items.push(name);
-                    });
-                    var iterator = {
-                        next: function() {
-                            var value = items.shift();
-                            return {
-                                done: value === undefined,
-                                value: value
-                            };
-                        }
-                    };
-
-                    if (iterable) {
-                        iterator[Symbol.iterator] = function() {
-                            return iterator;
-                        };
-                    }
-
-                    return iterator;
-                };
-            }
-
-            if (!('values' in URLSearchParamsProto)) {
-                URLSearchParamsProto.values = function values() {
-                    var items = [];
-                    this.forEach(function(value) {
-                        items.push(value);
-                    });
-                    var iterator = {
-                        next: function() {
-                            var value = items.shift();
-                            return {
-                                done: value === undefined,
-                                value: value
-                            };
-                        }
-                    };
-
-                    if (iterable) {
-                        iterator[Symbol.iterator] = function() {
-                            return iterator;
-                        };
-                    }
-
-                    return iterator;
-                };
-            }
-
-            if (!('entries' in URLSearchParamsProto)) {
-                URLSearchParamsProto.entries = function entries() {
-                    var items = [];
-                    this.forEach(function(value, name) {
-                        items.push([name, value]);
-                    });
-                    var iterator = {
-                        next: function() {
-                            var value = items.shift();
-                            return {
-                                done: value === undefined,
-                                value: value
-                            };
-                        }
-                    };
-
-                    if (iterable) {
-                        iterator[Symbol.iterator] = function() {
-                            return iterator;
-                        };
-                    }
-
-                    return iterator;
-                };
-            }
-
-            if (iterable && !(Symbol.iterator in URLSearchParamsProto)) {
-                URLSearchParamsProto[Symbol.iterator] = URLSearchParamsProto.entries;
-            }
-
-            if (!('sort' in URLSearchParamsProto)) {
-                URLSearchParamsProto.sort = function sort() {
-                    var this$1 = this;
-
-                    var
-                        entries = this.entries(),
-                        entry = entries.next(),
-                        done = entry.done,
-                        keys = [],
-                        values = Object.create(null),
-                        i, key, value;
-                    while (!done) {
-                        value = entry.value;
-                        key = value[0];
-                        keys.push(key);
-                        if (!(key in values)) {
-                            values[key] = [];
-                        }
-                        values[key].push(value[1]);
-                        entry = entries.next();
-                        done = entry.done;
-                    }
-                    // not the champion in efficiency
-                    // but these two bits just do the job
-                    keys.sort();
-                    for (i = 0; i < keys.length; i++) {
-                        this$1.delete(keys[i]);
-                    }
-                    for (i = 0; i < keys.length; i++) {
-                        key = keys[i];
-                        this$1.append(key, values[key].shift());
-                    }
-                };
-            }
-
-        }(URLSearchParams.prototype));
-    });
-
     // Select a single element.
     function $(expr, con) {
         if (con === void 0) con = document;
 
         return con.querySelector(expr);
     }
 
@@ -586,19 +276,27 @@
         });
     }
 
     e.on('page-loaded', function() {
         initSort();
     });
 
+    var commonjsGlobal = typeof window !== 'undefined' ? window : typeof global !== 'undefined' ? global : typeof self !== 'undefined' ? self : {};
+
+    function createCommonjsModule(fn, module) {
+        return module = {
+            exports: {}
+        }, fn(module, module.exports), module.exports;
+    }
+
     var codemirror = createCommonjsModule(function(module, exports) {
         // CodeMirror, copyright (c) by Marijn Haverbeke and others
-        // Distributed under an MIT license: http://codemirror.net/LICENSE
+        // Distributed under an MIT license: https://codemirror.net/LICENSE
 
-        // This is CodeMirror (http://codemirror.net), a code editor
+        // This is CodeMirror (https://codemirror.net), a code editor
         // implemented in JavaScript on top of the browser's DOM.
         //
         // You can find some technical background for some of the code below
         // at http://marijnhaverbeke.nl/blog/#cm-internals .
 
         (function(global, factory) {
             module.exports = factory();
@@ -3023,15 +2721,15 @@
                 var builder = {
                     pre: eltP("pre", [content], "CodeMirror-line"),
                     content: content,
                     col: 0,
                     pos: 0,
                     cm: cm,
                     trailingSpace: false,
-                    splitSpaces: (ie || webkit) && cm.getOption("lineWrapping")
+                    splitSpaces: cm.getOption("lineWrapping")
                 };
                 lineView.measure = {};
 
                 // Iterate over the logical lines that make up this visual line.
                 for (var i = 0; i <= (lineView.rest ? lineView.rest.length : 0); i++) {
                     var line = i ? lineView.rest[i - 1] : lineView.line,
                         order = (void 0);
@@ -3172,14 +2870,16 @@
                         token.title = title;
                     }
                     return builder.content.appendChild(token)
                 }
                 builder.content.appendChild(content);
             }
 
+            // Change some spaces to NBSP to prevent the browser from collapsing
+            // trailing spaces at the end of a line when rendering text (issue #1362).
             function splitSpaces(text, trailingBefore) {
                 if (text.length > 1 && !/  /.test(text)) {
                     return text
                 }
                 var spaceBefore = trailingBefore,
                     result = "";
                 for (var i = 0; i < text.length; i++) {
@@ -10364,19 +10064,19 @@
                         display.scroller.draggable = false;
                         setTimeout(function() {
                             return display.scroller.draggable = true;
                         }, 100);
                     }
                     return
                 }
-                if (clickInGutter(cm, e)) {
+                var button = e_button(e);
+                if (button == 3 && captureRightClick ? contextMenuInGutter(cm, e) : clickInGutter(cm, e)) {
                     return
                 }
                 var pos = posFromMouse(cm, e),
-                    button = e_button(e),
                     repeat = pos ? clickRepeat(pos, button) : "single";
                 window.focus();
 
                 // #3261: make sure, that we're not starting a second selection
                 if (button == 1 && cm.state.selectingText) {
                     cm.state.selectingText(e);
                 }
@@ -11011,14 +10711,15 @@
                 option("tabindex", null, function(cm, val) {
                     return cm.display.input.getField().tabIndex = val || "";
                 });
                 option("autofocus", null);
                 option("direction", "ltr", function(cm, val) {
                     return cm.doc.setDirection(val);
                 }, true);
+                option("phrases", null);
             }
 
             function guttersChanged(cm) {
                 updateGutters(cm);
                 regChange(cm);
                 alignHorizontally(cm);
             }
@@ -12178,14 +11879,19 @@
                         this.display.input.reset();
                         scrollToCoords(this, doc.scrollLeft, doc.scrollTop);
                         this.curOp.forceScroll = true;
                         signalLater(this, "swapDoc", this, old);
                         return old
                     }),
 
+                    phrase: function(phraseText) {
+                        var phrases = this.options.phrases;
+                        return phrases && Object.prototype.hasOwnProperty.call(phrases, phraseText) ? phrases[phraseText] : phraseText
+                    },
+
                     getInputField: function() {
                         return this.display.input.getField()
                     },
                     getWrapperElement: function() {
                         return this.display.wrapper
                     },
                     getScrollerElement: function() {
@@ -13645,15 +13351,15 @@
                 Doc.prototype[name] = func;
             };
 
             CodeMirror$1.fromTextArea = fromTextArea;
 
             addLegacyProps(CodeMirror$1);
 
-            CodeMirror$1.version = "5.39.2";
+            CodeMirror$1.version = "5.40.2";
 
             return CodeMirror$1;
 
         })));
     });
 
     var mousetrap = createCommonjsModule(function(module) {
@@ -14703,15 +14409,15 @@
                 });
             }
         })(typeof window !== 'undefined' ? window : null, typeof window !== 'undefined' ? document : null);
     });
 
     var simple = createCommonjsModule(function(module, exports) {
         // CodeMirror, copyright (c) by Marijn Haverbeke and others
-        // Distributed under an MIT license: http://codemirror.net/LICENSE
+        // Distributed under an MIT license: https://codemirror.net/LICENSE
 
         (function(mod) {
             {
                 mod(codemirror);
             }
         })(function(CodeMirror) {
 
@@ -15010,15 +14716,15 @@
                 };
             }
         });
     });
 
     var dialog = createCommonjsModule(function(module, exports) {
         // CodeMirror, copyright (c) by Marijn Haverbeke and others
-        // Distributed under an MIT license: http://codemirror.net/LICENSE
+        // Distributed under an MIT license: https://codemirror.net/LICENSE
 
         // Open simple dialogs on top of an editor. Relies on dialog.css.
 
         (function(mod) {
             {
                 mod(codemirror);
             }
@@ -15213,15 +14919,15 @@
                 return close;
             });
         });
     });
 
     var searchcursor = createCommonjsModule(function(module, exports) {
         // CodeMirror, copyright (c) by Marijn Haverbeke and others
-        // Distributed under an MIT license: http://codemirror.net/LICENSE
+        // Distributed under an MIT license: https://codemirror.net/LICENSE
 
         (function(mod) {
             {
                 mod(codemirror);
             }
         })(function(CodeMirror) {
             var Pos = CodeMirror.Pos;
@@ -15628,15 +15334,15 @@
                 }
             });
         });
     });
 
     var search$1 = createCommonjsModule(function(module, exports) {
         // CodeMirror, copyright (c) by Marijn Haverbeke and others
-        // Distributed under an MIT license: http://codemirror.net/LICENSE
+        // Distributed under an MIT license: https://codemirror.net/LICENSE
 
         // Define search commands. Depends on dialog.js or another
         // implementation of the openDialog method.
 
         // Replace works a little oddly -- it will do the replace on the next
         // Ctrl-G (or whatever is bound to findNext) press. You prevent a
         // replace by making sure the match is no longer selected when hitting
@@ -15746,17 +15452,14 @@
                 }
                 if (typeof query == "string" ? query == "" : query.test("")) {
                     query = /x^/;
                 }
                 return query;
             }
 
-            var queryDialog =
-                '<span class="CodeMirror-search-label">Search:</span> <input type="text" style="width: 10em" class="CodeMirror-search-field"/> <span style="color: #888" class="CodeMirror-search-hint">(Use /re/ syntax for regexp search)</span>';
-
             function startSearch(cm, state, query) {
                 state.queryText = query;
                 state.query = parseQuery(query);
                 cm.removeOverlay(state.overlay, queryCaseInsensitive(state.query));
                 state.overlay = searchOverlay(state.query, queryCaseInsensitive(state.query));
                 cm.addOverlay(state.overlay);
                 if (cm.showMatchesOnScrollbar) {
@@ -15796,15 +15499,15 @@
                             if (to.line < 3 && document.querySelector &&
                                 (dialog$$1 = cm.display.wrapper.querySelector(".CodeMirror-dialog")) &&
                                 dialog$$1.getBoundingClientRect().bottom - 4 > cm.cursorCoords(to, "window").top) {
                                 (hiding = dialog$$1).style.opacity = .4;
                             }
                         });
                     };
-                    persistentDialog(cm, queryDialog, q, searchNext, function(event, query) {
+                    persistentDialog(cm, getQueryDialog(cm), q, searchNext, function(event, query) {
                         var keyName = CodeMirror.keyName(event);
                         var extra = cm.getOption('extraKeys'),
                             cmd = (extra && extra[keyName]) || CodeMirror.keyMap[cm.getOption("keyMap")][keyName];
                         if (cmd == "findNext" || cmd == "findPrev" ||
                             cmd == "findPersistentNext" || cmd == "findPersistentPrev") {
                             CodeMirror.e_stop(event);
                             startSearch(cm, getSearchState(cm), query);
@@ -15815,15 +15518,15 @@
                         }
                     });
                     if (immediate && q) {
                         startSearch(cm, state, q);
                         findNext(cm, rev);
                     }
                 } else {
-                    dialog$$1(cm, queryDialog, "Search for:", q, function(query) {
+                    dialog$$1(cm, getQueryDialog(cm), "Search for:", q, function(query) {
                         if (query && !state.query) {
                             cm.operation(function() {
                                 startSearch(cm, state, query);
                                 state.posFrom = state.posTo = cm.getCursor();
                                 findNext(cm, rev);
                             });
                         }
@@ -15866,18 +15569,30 @@
                     if (state.annotate) {
                         state.annotate.clear();
                         state.annotate = null;
                     }
                 });
             }
 
-            var replaceQueryDialog =
-                ' <input type="text" style="width: 10em" class="CodeMirror-search-field"/> <span style="color: #888" class="CodeMirror-search-hint">(Use /re/ syntax for regexp search)</span>';
-            var replacementQueryDialog = '<span class="CodeMirror-search-label">With:</span> <input type="text" style="width: 10em" class="CodeMirror-search-field"/>';
-            var doReplaceConfirm = '<span class="CodeMirror-search-label">Replace?</span> <button>Yes</button> <button>No</button> <button>All</button> <button>Stop</button>';
+
+            function getQueryDialog(cm) {
+                return '<span class="CodeMirror-search-label">' + cm.phrase("Search:") + '</span> <input type="text" style="width: 10em" class="CodeMirror-search-field"/> <span style="color: #888" class="CodeMirror-search-hint">' + cm.phrase("(Use /re/ syntax for regexp search)") + '</span>';
+            }
+
+            function getReplaceQueryDialog(cm) {
+                return ' <input type="text" style="width: 10em" class="CodeMirror-search-field"/> <span style="color: #888" class="CodeMirror-search-hint">' + cm.phrase("(Use /re/ syntax for regexp search)") + '</span>';
+            }
+
+            function getReplacementQueryDialog(cm) {
+                return '<span class="CodeMirror-search-label">' + cm.phrase("With:") + '</span> <input type="text" style="width: 10em" class="CodeMirror-search-field"/>';
+            }
+
+            function getDoReplaceConfirm(cm) {
+                return '<span class="CodeMirror-search-label">' + cm.phrase("Replace?") + '</span> <button>' + cm.phrase("Yes") + '</button> <button>' + cm.phrase("No") + '</button> <button>' + cm.phrase("All") + '</button> <button>' + cm.phrase("Stop") + '</button> ';
+            }
 
             function replaceAll(cm, query, text) {
                 cm.operation(function() {
                     for (var cursor = getSearchCursor(cm, query); cursor.findNext();) {
                         if (typeof query != "string") {
                             var match = cm.getRange(cursor.from(), cursor.to()).match(query);
                             cursor.replace(text.replace(/\$(\d)/g, function(_, i) {
@@ -15891,21 +15606,21 @@
             }
 
             function replace(cm, all) {
                 if (cm.getOption("readOnly")) {
                     return;
                 }
                 var query = cm.getSelection() || getSearchState(cm).lastQuery;
-                var dialogText = '<span class="CodeMirror-search-label">' + (all ? 'Replace all:' : 'Replace:') + '</span>';
-                dialog$$1(cm, dialogText + replaceQueryDialog, dialogText, query, function(query) {
+                var dialogText = '<span class="CodeMirror-search-label">' + (all ? cm.phrase("Replace all:") : cm.phrase("Replace:")) + '</span>';
+                dialog$$1(cm, dialogText + getReplaceQueryDialog(cm), dialogText, query, function(query) {
                     if (!query) {
                         return;
                     }
                     query = parseQuery(query);
-                    dialog$$1(cm, replacementQueryDialog, "Replace with:", "", function(text) {
+                    dialog$$1(cm, getReplacementQueryDialog(cm), cm.phrase("Replace with:"), "", function(text) {
                         text = parseString(text);
                         if (all) {
                             replaceAll(cm, query, text);
                         } else {
                             clearSearch(cm);
                             var cursor = getSearchCursor(cm, query, cm.getCursor("from"));
                             var advance = function() {
@@ -15919,15 +15634,15 @@
                                     }
                                 }
                                 cm.setSelection(cursor.from(), cursor.to());
                                 cm.scrollIntoView({
                                     from: cursor.from(),
                                     to: cursor.to()
                                 });
-                                confirmDialog(cm, doReplaceConfirm, "Replace?",
+                                confirmDialog(cm, getDoReplaceConfirm(cm), cm.phrase("Replace?"),
                                     [function() {
                                             doReplace(match);
                                         }, advance,
                                         function() {
                                             replaceAll(cm, query, text);
                                         }
                                     ]);
@@ -15969,15 +15684,15 @@
                 replace(cm, true);
             };
         });
     });
 
     var rulers = createCommonjsModule(function(module, exports) {
         // CodeMirror, copyright (c) by Marijn Haverbeke and others
-        // Distributed under an MIT license: http://codemirror.net/LICENSE
+        // Distributed under an MIT license: https://codemirror.net/LICENSE
 
         (function(mod) {
             {
                 mod(codemirror);
             }
         })(function(CodeMirror) {
 
@@ -16027,15 +15742,15 @@
                 }
             }
         });
     });
 
     var trailingspace = createCommonjsModule(function(module, exports) {
         // CodeMirror, copyright (c) by Marijn Haverbeke and others
-        // Distributed under an MIT license: http://codemirror.net/LICENSE
+        // Distributed under an MIT license: https://codemirror.net/LICENSE
 
         (function(mod) {
             {
                 mod(codemirror);
             }
         })(function(CodeMirror) {
             CodeMirror.defineOption("showTrailingSpace", false, function(cm, val, prev) {
@@ -16060,15 +15775,15 @@
                 }
             });
         });
     });
 
     var foldcode = createCommonjsModule(function(module, exports) {
         // CodeMirror, copyright (c) by Marijn Haverbeke and others
-        // Distributed under an MIT license: http://codemirror.net/LICENSE
+        // Distributed under an MIT license: https://codemirror.net/LICENSE
 
         (function(mod) {
             {
                 mod(codemirror);
             }
         })(function(CodeMirror) {
 
@@ -16237,15 +15952,15 @@
                 return getOption(this, options, name);
             });
         });
     });
 
     var foldgutter = createCommonjsModule(function(module, exports) {
         // CodeMirror, copyright (c) by Marijn Haverbeke and others
-        // Distributed under an MIT license: http://codemirror.net/LICENSE
+        // Distributed under an MIT license: https://codemirror.net/LICENSE
 
         (function(mod) {
             {
                 mod(codemirror, foldcode);
             }
         })(function(CodeMirror) {
 
@@ -16415,15 +16130,15 @@
                 }
             }
         });
     });
 
     var showHint = createCommonjsModule(function(module, exports) {
         // CodeMirror, copyright (c) by Marijn Haverbeke and others
-        // Distributed under an MIT license: http://codemirror.net/LICENSE
+        // Distributed under an MIT license: https://codemirror.net/LICENSE
 
         (function(mod) {
             {
                 mod(codemirror);
             }
         })(function(CodeMirror) {
 
@@ -17024,15 +16739,15 @@
 
             CodeMirror.defineOption("hintOptions", null);
         });
     });
 
     var comment = createCommonjsModule(function(module, exports) {
         // CodeMirror, copyright (c) by Marijn Haverbeke and others
-        // Distributed under an MIT license: http://codemirror.net/LICENSE
+        // Distributed under an MIT license: https://codemirror.net/LICENSE
 
         (function(mod) {
             {
                 mod(codemirror);
             }
         })(function(CodeMirror) {
 
@@ -17311,15 +17026,15 @@
                 return true;
             });
         });
     });
 
     var placeholder = createCommonjsModule(function(module, exports) {
         // CodeMirror, copyright (c) by Marijn Haverbeke and others
-        // Distributed under an MIT license: http://codemirror.net/LICENSE
+        // Distributed under an MIT license: https://codemirror.net/LICENSE
 
         (function(mod) {
             {
                 mod(codemirror);
             }
         })(function(CodeMirror) {
             CodeMirror.defineOption("placeholder", "", function(cm, val, old) {
@@ -17386,15 +17101,15 @@
                 return (cm.lineCount() === 1) && (cm.getLine(0) === "");
             }
         });
     });
 
     var activeLine = createCommonjsModule(function(module, exports) {
         // CodeMirror, copyright (c) by Marijn Haverbeke and others
-        // Distributed under an MIT license: http://codemirror.net/LICENSE
+        // Distributed under an MIT license: https://codemirror.net/LICENSE
 
         (function(mod) {
             {
                 mod(codemirror);
             }
         })(function(CodeMirror) {
             var WRAP_CLASS = "CodeMirror-activeline";
@@ -18294,22 +18009,21 @@
                         }
                         if (historyState) {
                             window.history.pushState(null, null, url);
                             window.scroll(0, 0);
                         }
                         this$1.updateState();
                         $('article').innerHTML = data;
+                        svg.classList.remove('loading');
                         e.trigger('page-loaded');
                         handleHash();
                     });
             }, function() {
-                e.trigger('error', ("Loading " + url + " failed."));
-            })
-            .finally(function() {
                 svg.classList.remove('loading');
+                e.trigger('error', ("Loading " + url + " failed."));
             });
     };
 
     // Update the routers state object. The state object is used to distinguish
     // between the user navigating the browser history or the hash changing.
     Router.prototype.updateState = function updateState() {
         this.state = {
@@ -18915,15 +18629,15 @@
         return x;
     }
 
     var top = 1,
         right = 2,
         bottom = 3,
         left = 4,
-        epsilon$1 = 1e-6;
+        epsilon = 1e-6;
 
     function translateX(x) {
         return "translate(" + (x + 0.5) + ",0)";
     }
 
     function translateY(y) {
         return "translate(0," + (y + 0.5) + ")";
@@ -18974,53 +18688,53 @@
                 tickExit = tick.exit(),
                 tickEnter = tick.enter().append("g").attr("class", "tick"),
                 line = tick.select("line"),
                 text = tick.select("text");
 
             path = path.merge(path.enter().insert("path", ".tick")
                 .attr("class", "domain")
-                .attr("stroke", "#000"));
+                .attr("stroke", "currentColor"));
 
             tick = tick.merge(tickEnter);
 
             line = line.merge(tickEnter.append("line")
-                .attr("stroke", "#000")
+                .attr("stroke", "currentColor")
                 .attr(x + "2", k * tickSizeInner));
 
             text = text.merge(tickEnter.append("text")
-                .attr("fill", "#000")
+                .attr("fill", "currentColor")
                 .attr(x, k * spacing)
                 .attr("dy", orient === top ? "0em" : orient === bottom ? "0.71em" : "0.32em"));
 
             if (context !== selection) {
                 path = path.transition(context);
                 tick = tick.transition(context);
                 line = line.transition(context);
                 text = text.transition(context);
 
                 tickExit = tickExit.transition(context)
-                    .attr("opacity", epsilon$1)
+                    .attr("opacity", epsilon)
                     .attr("transform", function(d) {
                         return isFinite(d = position(d)) ? transform(d) : this.getAttribute("transform");
                     });
 
                 tickEnter
-                    .attr("opacity", epsilon$1)
+                    .attr("opacity", epsilon)
                     .attr("transform", function(d) {
                         var p = this.parentNode.__axis;
                         return transform(p && isFinite(p = p(d)) ? p : position(d));
                     });
             }
 
             tickExit.remove();
 
             path
                 .attr("d", orient === left || orient == right ?
-                    "M" + k * tickSizeOuter + "," + range0 + "H0.5V" + range1 + "H" + k * tickSizeOuter :
-                    "M" + range0 + "," + k * tickSizeOuter + "V0.5H" + range1 + "V" + k * tickSizeOuter);
+                    (tickSizeOuter ? "M" + k * tickSizeOuter + "," + range0 + "H0.5V" + range1 + "H" + k * tickSizeOuter : "M0.5," + range0 + "V" + range1) :
+                    (tickSizeOuter ? "M" + range0 + "," + k * tickSizeOuter + "V0.5H" + range1 + "V" + k * tickSizeOuter : "M" + range0 + ",0.5H" + range1));
 
             tick
                 .attr("opacity", 1)
                 .attr("transform", function(d) {
                     return transform(position(d));
                 });
 
@@ -21174,15 +20888,15 @@
             return value.replace(/[0-9]/g, function(i) {
                 return numerals[+i];
             });
         };
     }
 
     // [[fill]align][sign][symbol][0][width][,][.precision][~][type]
-    var re = /^(?:(.)?([<>=^]))?([+\-\( ])?([$#])?(0)?(\d+)?(,)?(\.\d+)?(~)?([a-z%])?$/i;
+    var re = /^(?:(.)?([<>=^]))?([+\-( ])?([$#])?(0)?(\d+)?(,)?(\.\d+)?(~)?([a-z%])?$/i;
 
     function formatSpecifier(specifier) {
         return new FormatSpecifier(specifier);
     }
 
     formatSpecifier.prototype = FormatSpecifier.prototype; // instanceof
 
@@ -23821,16 +23535,16 @@
             new Selection([
                 [selector]
             ], root);
     }
 
     var pi = Math.PI,
         tau = 2 * pi,
-        epsilon$2 = 1e-6,
-        tauEpsilon = tau - epsilon$2;
+        epsilon$1 = 1e-6,
+        tauEpsilon = tau - epsilon$1;
 
     function Path() {
         this._x0 = this._y0 = // start of current subpath
             this._x1 = this._y1 = null; // end of current subpath
         this._ = "";
     }
 
@@ -23875,20 +23589,20 @@
 
             // Is this path empty? Move to (x1,y1).
             if (this._x1 === null) {
                 this._ += "M" + (this._x1 = x1) + "," + (this._y1 = y1);
             }
 
             // Or, is (x1,y1) coincident with (x0,y0)? Do nothing.
-            else if (!(l01_2 > epsilon$2));
+            else if (!(l01_2 > epsilon$1));
 
             // Or, are (x0,y0), (x1,y1) and (x2,y2) collinear?
             // Equivalently, is (x1,y1) coincident with (x2,y2)?
             // Or, is the radius zero? Line to (x1,y1).
-            else if (!(Math.abs(y01 * x21 - y21 * x01) > epsilon$2) || !r) {
+            else if (!(Math.abs(y01 * x21 - y21 * x01) > epsilon$1) || !r) {
                 this._ += "L" + (this._x1 = x1) + "," + (this._y1 = y1);
             }
 
             // Otherwise, draw an arc!
             else {
                 var x20 = x2 - x0,
                     y20 = y2 - y0,
@@ -23897,15 +23611,15 @@
                     l21 = Math.sqrt(l21_2),
                     l01 = Math.sqrt(l01_2),
                     l = r * Math.tan((pi - Math.acos((l21_2 + l01_2 - l20_2) / (2 * l21 * l01))) / 2),
                     t01 = l / l01,
                     t21 = l / l21;
 
                 // If the start tangent is not coincident with (x0,y0), line to.
-                if (Math.abs(t01 - 1) > epsilon$2) {
+                if (Math.abs(t01 - 1) > epsilon$1) {
                     this._ += "L" + (x1 + t01 * x01) + "," + (y1 + t01 * y01);
                 }
 
                 this._ += "A" + r + "," + r + ",0,0," + (+(y01 * x20 > x01 * y20)) + "," + (this._x1 = x1 + t21 * x21) + "," + (this._y1 = y1 + t21 * y21);
             }
         },
         arc: function(x, y, r, a0, a1, ccw) {
@@ -23924,15 +23638,15 @@
 
             // Is this path empty? Move to (x0,y0).
             if (this._x1 === null) {
                 this._ += "M" + x0 + "," + y0;
             }
 
             // Or, is (x0,y0) not coincident with the previous point? Line to (x0,y0).
-            else if (Math.abs(this._x1 - x0) > epsilon$2 || Math.abs(this._y1 - y0) > epsilon$2) {
+            else if (Math.abs(this._x1 - x0) > epsilon$1 || Math.abs(this._y1 - y0) > epsilon$1) {
                 this._ += "L" + x0 + "," + y0;
             }
 
             // Is this arc empty? We’re done.
             if (!r) {
                 return;
             }
@@ -23944,15 +23658,15 @@
 
             // Is this a complete circle? Draw two arcs to complete the circle.
             if (da > tauEpsilon) {
                 this._ += "A" + r + "," + r + ",0,1," + cw + "," + (x - dx) + "," + (y - dy) + "A" + r + "," + r + ",0,1," + cw + "," + (this._x1 = x0) + "," + (this._y1 = y0);
             }
 
             // Is this arc non-empty? Draw an arc!
-            else if (da > epsilon$2) {
+            else if (da > epsilon$1) {
                 this._ += "A" + r + "," + r + ",0," + (+(da >= pi)) + "," + cw + "," + (this._x1 = x + r * Math.cos(a1)) + "," + (this._y1 = y + r * Math.sin(a1));
             }
         },
         rect: function(x, y, w, h) {
             this._ += "M" + (this._x0 = this._x1 = +x) + "," + (this._y0 = this._y1 = +y) + "h" + (+w) + "v" + (+h) + "h" + (-w) + "Z";
         },
         toString: function() {
@@ -23970,15 +23684,15 @@
     var atan2 = Math.atan2;
     var cos = Math.cos;
     var max$1 = Math.max;
     var min$1 = Math.min;
     var sin = Math.sin;
     var sqrt$1 = Math.sqrt;
 
-    var epsilon$3 = 1e-12;
+    var epsilon$2 = 1e-12;
     var pi$1 = Math.PI;
     var halfPi = pi$1 / 2;
     var tau$1 = 2 * pi$1;
 
     function acos(x) {
         return x > 1 ? 0 : x < -1 ? pi$1 : Math.acos(x);
     }
@@ -24087,93 +23801,93 @@
 
             // Ensure that the outer radius is always larger than the inner radius.
             if (r1 < r0) {
                 r = r1, r1 = r0, r0 = r;
             }
 
             // Is it a point?
-            if (!(r1 > epsilon$3)) {
+            if (!(r1 > epsilon$2)) {
                 context.moveTo(0, 0);
             }
 
             // Or is it a circle or annulus?
-            else if (da > tau$1 - epsilon$3) {
+            else if (da > tau$1 - epsilon$2) {
                 context.moveTo(r1 * cos(a0), r1 * sin(a0));
                 context.arc(0, 0, r1, a0, a1, !cw);
-                if (r0 > epsilon$3) {
+                if (r0 > epsilon$2) {
                     context.moveTo(r0 * cos(a1), r0 * sin(a1));
                     context.arc(0, 0, r0, a1, a0, cw);
                 }
             }
 
             // Or is it a circular or annular sector?
             else {
                 var a01 = a0,
                     a11 = a1,
                     a00 = a0,
                     a10 = a1,
                     da0 = da,
                     da1 = da,
                     ap = padAngle.apply(this, arguments) / 2,
-                    rp = (ap > epsilon$3) && (padRadius ? +padRadius.apply(this, arguments) : sqrt$1(r0 * r0 + r1 * r1)),
+                    rp = (ap > epsilon$2) && (padRadius ? +padRadius.apply(this, arguments) : sqrt$1(r0 * r0 + r1 * r1)),
                     rc = min$1(abs(r1 - r0) / 2, +cornerRadius.apply(this, arguments)),
                     rc0 = rc,
                     rc1 = rc,
                     t0,
                     t1;
 
                 // Apply padding? Note that since r1 ≥ r0, da1 ≥ da0.
-                if (rp > epsilon$3) {
+                if (rp > epsilon$2) {
                     var p0 = asin(rp / r0 * sin(ap)),
                         p1 = asin(rp / r1 * sin(ap));
-                    if ((da0 -= p0 * 2) > epsilon$3) {
+                    if ((da0 -= p0 * 2) > epsilon$2) {
                         p0 *= (cw ? 1 : -1), a00 += p0, a10 -= p0;
                     } else {
                         da0 = 0, a00 = a10 = (a0 + a1) / 2;
                     }
-                    if ((da1 -= p1 * 2) > epsilon$3) {
+                    if ((da1 -= p1 * 2) > epsilon$2) {
                         p1 *= (cw ? 1 : -1), a01 += p1, a11 -= p1;
                     } else {
                         da1 = 0, a01 = a11 = (a0 + a1) / 2;
                     }
                 }
 
                 var x01 = r1 * cos(a01),
                     y01 = r1 * sin(a01),
                     x10 = r0 * cos(a10),
                     y10 = r0 * sin(a10);
 
                 // Apply rounded corners?
-                if (rc > epsilon$3) {
+                if (rc > epsilon$2) {
                     var x11 = r1 * cos(a11),
                         y11 = r1 * sin(a11),
                         x00 = r0 * cos(a00),
                         y00 = r0 * sin(a00);
 
                     // Restrict the corner radius according to the sector angle.
                     if (da < pi$1) {
-                        var oc = da0 > epsilon$3 ? intersect(x01, y01, x00, y00, x11, y11, x10, y10) : [x10, y10],
+                        var oc = da0 > epsilon$2 ? intersect(x01, y01, x00, y00, x11, y11, x10, y10) : [x10, y10],
                             ax = x01 - oc[0],
                             ay = y01 - oc[1],
                             bx = x11 - oc[0],
                             by = y11 - oc[1],
                             kc = 1 / sin(acos((ax * bx + ay * by) / (sqrt$1(ax * ax + ay * ay) * sqrt$1(bx * bx + by * by))) / 2),
                             lc = sqrt$1(oc[0] * oc[0] + oc[1] * oc[1]);
                         rc0 = min$1(rc, (r0 - lc) / (kc - 1));
                         rc1 = min$1(rc, (r1 - lc) / (kc + 1));
                     }
                 }
 
                 // Is the sector collapsed to a line?
-                if (!(da1 > epsilon$3)) {
+                if (!(da1 > epsilon$2)) {
                     context.moveTo(x01, y01);
                 }
 
                 // Does the sector’s outer ring have rounded corners?
-                else if (rc1 > epsilon$3) {
+                else if (rc1 > epsilon$2) {
                     t0 = cornerTangents(x00, y00, x01, y01, r1, rc1, cw);
                     t1 = cornerTangents(x11, y11, x10, y10, r1, rc1, cw);
 
                     context.moveTo(t0.cx + t0.x01, t0.cy + t0.y01);
 
                     // Have the corners merged?
                     if (rc1 < rc) {
@@ -24191,20 +23905,20 @@
                 // Or is the outer ring just a circular arc?
                 else {
                     context.moveTo(x01, y01), context.arc(0, 0, r1, a01, a11, !cw);
                 }
 
                 // Is there no inner ring, and it’s a circular sector?
                 // Or perhaps it’s an annular sector collapsed due to padding?
-                if (!(r0 > epsilon$3) || !(da0 > epsilon$3)) {
+                if (!(r0 > epsilon$2) || !(da0 > epsilon$2)) {
                     context.lineTo(x10, y10);
                 }
 
                 // Does the sector’s inner ring (or point) have rounded corners?
-                else if (rc0 > epsilon$3) {
+                else if (rc0 > epsilon$2) {
                     t0 = cornerTangents(x10, y10, x11, y11, r0, -rc0, cw);
                     t1 = cornerTangents(x01, y01, x00, y00, r0, -rc0, cw);
 
                     context.lineTo(t0.cx + t0.x01, t0.cy + t0.y01);
 
                     // Have the corners merged?
                     if (rc0 < rc) {
@@ -24901,49 +24615,31 @@
 
     var magma = ramp$1(colors("00000401000501010601010802010902020b02020d03030f03031204041405041606051806051a07061c08071e0907200a08220b09240c09260d0a290e0b2b100b2d110c2f120d31130d34140e36150e38160f3b180f3d19103f1a10421c10441d11471e114920114b21114e22115024125325125527125829115a2a115c2c115f2d11612f116331116533106734106936106b38106c390f6e3b0f703d0f713f0f72400f74420f75440f764510774710784910784a10794c117a4e117b4f127b51127c52137c54137d56147d57157e59157e5a167e5c167f5d177f5f187f601880621980641a80651a80671b80681c816a1c816b1d816d1d816e1e81701f81721f817320817521817621817822817922827b23827c23827e24828025828125818326818426818627818827818928818b29818c29818e2a81902a81912b81932b80942c80962c80982d80992d809b2e7f9c2e7f9e2f7fa02f7fa1307ea3307ea5317ea6317da8327daa337dab337cad347cae347bb0357bb2357bb3367ab5367ab73779b83779ba3878bc3978bd3977bf3a77c03a76c23b75c43c75c53c74c73d73c83e73ca3e72cc3f71cd4071cf4070d0416fd2426fd3436ed5446dd6456cd8456cd9466bdb476adc4869de4968df4a68e04c67e24d66e34e65e44f64e55064e75263e85362e95462ea5661eb5760ec5860ed5a5fee5b5eef5d5ef05f5ef1605df2625df2645cf3655cf4675cf4695cf56b5cf66c5cf66e5cf7705cf7725cf8745cf8765cf9785df9795df97b5dfa7d5efa7f5efa815ffb835ffb8560fb8761fc8961fc8a62fc8c63fc8e64fc9065fd9266fd9467fd9668fd9869fd9a6afd9b6bfe9d6cfe9f6dfea16efea36ffea571fea772fea973feaa74feac76feae77feb078feb27afeb47bfeb67cfeb77efeb97ffebb81febd82febf84fec185fec287fec488fec68afec88cfeca8dfecc8ffecd90fecf92fed194fed395fed597fed799fed89afdda9cfddc9efddea0fde0a1fde2a3fde3a5fde5a7fde7a9fde9aafdebacfcecaefceeb0fcf0b2fcf2b4fcf4b6fcf6b8fcf7b9fcf9bbfcfbbdfcfdbf"));
 
     var inferno = ramp$1(colors("00000401000501010601010802010a02020c02020e03021004031204031405041706041907051b08051d09061f0a07220b07240c08260d08290e092b10092d110a30120a32140b34150b37160b39180c3c190c3e1b0c411c0c431e0c451f0c48210c4a230c4c240c4f260c51280b53290b552b0b572d0b592f0a5b310a5c320a5e340a5f3609613809623909633b09643d09653e0966400a67420a68440a68450a69470b6a490b6a4a0c6b4c0c6b4d0d6c4f0d6c510e6c520e6d540f6d550f6d57106e59106e5a116e5c126e5d126e5f136e61136e62146e64156e65156e67166e69166e6a176e6c186e6d186e6f196e71196e721a6e741a6e751b6e771c6d781c6d7a1d6d7c1d6d7d1e6d7f1e6c801f6c82206c84206b85216b87216b88226a8a226a8c23698d23698f24699025689225689326679526679727669827669a28659b29649d29649f2a63a02a63a22b62a32c61a52c60a62d60a82e5fa92e5eab2f5ead305dae305cb0315bb1325ab3325ab43359b63458b73557b93556ba3655bc3754bd3853bf3952c03a51c13a50c33b4fc43c4ec63d4dc73e4cc83f4bca404acb4149cc4248ce4347cf4446d04545d24644d34743d44842d54a41d74b3fd84c3ed94d3dda4e3cdb503bdd513ade5238df5337e05536e15635e25734e35933e45a31e55c30e65d2fe75e2ee8602de9612bea632aeb6429eb6628ec6726ed6925ee6a24ef6c23ef6e21f06f20f1711ff1731df2741cf3761bf37819f47918f57b17f57d15f67e14f68013f78212f78410f8850ff8870ef8890cf98b0bf98c0af98e09fa9008fa9207fa9407fb9606fb9706fb9906fb9b06fb9d07fc9f07fca108fca309fca50afca60cfca80dfcaa0ffcac11fcae12fcb014fcb216fcb418fbb61afbb81dfbba1ffbbc21fbbe23fac026fac228fac42afac62df9c72ff9c932f9cb35f8cd37f8cf3af7d13df7d340f6d543f6d746f5d949f5db4cf4dd4ff4df53f4e156f3e35af3e55df2e661f2e865f2ea69f1ec6df1ed71f1ef75f1f179f2f27df2f482f3f586f3f68af4f88ef5f992f6fa96f8fb9af9fc9dfafda1fcffa4"));
 
     var plasma = ramp$1(colors("0d088710078813078916078a19068c1b068d1d068e20068f2206902406912605912805922a05932c05942e05952f059631059733059735049837049938049a3a049a3c049b3e049c3f049c41049d43039e44039e46039f48039f4903a04b03a14c02a14e02a25002a25102a35302a35502a45601a45801a45901a55b01a55c01a65e01a66001a66100a76300a76400a76600a76700a86900a86a00a86c00a86e00a86f00a87100a87201a87401a87501a87701a87801a87a02a87b02a87d03a87e03a88004a88104a78305a78405a78606a68707a68808a68a09a58b0aa58d0ba58e0ca48f0da4910ea3920fa39410a29511a19613a19814a099159f9a169f9c179e9d189d9e199da01a9ca11b9ba21d9aa31e9aa51f99a62098a72197a82296aa2395ab2494ac2694ad2793ae2892b02991b12a90b22b8fb32c8eb42e8db52f8cb6308bb7318ab83289ba3388bb3488bc3587bd3786be3885bf3984c03a83c13b82c23c81c33d80c43e7fc5407ec6417dc7427cc8437bc9447aca457acb4679cc4778cc4977cd4a76ce4b75cf4c74d04d73d14e72d24f71d35171d45270d5536fd5546ed6556dd7566cd8576bd9586ada5a6ada5b69db5c68dc5d67dd5e66de5f65de6164df6263e06363e16462e26561e26660e3685fe4695ee56a5de56b5de66c5ce76e5be76f5ae87059e97158e97257ea7457eb7556eb7655ec7754ed7953ed7a52ee7b51ef7c51ef7e50f07f4ff0804ef1814df1834cf2844bf3854bf3874af48849f48948f58b47f58c46f68d45f68f44f79044f79143f79342f89441f89540f9973ff9983ef99a3efa9b3dfa9c3cfa9e3bfb9f3afba139fba238fca338fca537fca636fca835fca934fdab33fdac33fdae32fdaf31fdb130fdb22ffdb42ffdb52efeb72dfeb82cfeba2cfebb2bfebd2afebe2afec029fdc229fdc328fdc527fdc627fdc827fdca26fdcb26fccd25fcce25fcd025fcd225fbd324fbd524fbd724fad824fada24f9dc24f9dd25f8df25f8e125f7e225f7e425f6e626f6e826f5e926f5eb27f4ed27f3ee27f3f027f2f227f1f426f1f525f0f724f0f921"));
 
-    Delaunator.from = function(points, getX, getY) {
-        if (!getX) {
-            getX = defaultGetX;
-        }
-        if (!getY) {
-            getY = defaultGetY;
-        }
+    var EPSILON = Math.pow(2, -52);
 
-        var n = points.length;
-        var coords = new Float64Array(n * 2);
-
-        for (var i = 0; i < n; i++) {
-            var p = points[i];
-            coords[2 * i] = getX(p);
-            coords[2 * i + 1] = getY(p);
-        }
-
-        return new Delaunator(coords);
-    };
-
-    function Delaunator(coords) {
+    var Delaunator = function Delaunator(coords) {
         var this$1 = this;
 
-        if (!ArrayBuffer.isView(coords)) {
-            throw new Error('Expected coords to be a typed array.');
-        }
-
         var minX = Infinity;
         var minY = Infinity;
         var maxX = -Infinity;
         var maxY = -Infinity;
 
         var n = coords.length >> 1;
         var ids = this.ids = new Uint32Array(n);
 
+        if (n > 0 && typeof coords[0] !== 'number') {
+            throw new Error('Expected coords to contain numbers.');
+        }
+
         this.coords = coords;
 
         for (var i = 0; i < n; i++) {
             var x = coords[2 * i];
             var y = coords[2 * i + 1];
             if (x < minX) {
                 minX = x;
@@ -24963,89 +24659,83 @@
         var cx = (minX + maxX) / 2;
         var cy = (minY + maxY) / 2;
 
         var minDist = Infinity;
         var i0, i1, i2;
 
         // pick a seed point close to the centroid
-        for (i = 0; i < n; i++) {
-            var d = dist(cx, cy, coords[2 * i], coords[2 * i + 1]);
+        for (var i$1 = 0; i$1 < n; i$1++) {
+            var d = dist(cx, cy, coords[2 * i$1], coords[2 * i$1 + 1]);
             if (d < minDist) {
-                i0 = i;
+                i0 = i$1;
                 minDist = d;
             }
         }
+        var i0x = coords[2 * i0];
+        var i0y = coords[2 * i0 + 1];
 
         minDist = Infinity;
 
         // find the point closest to the seed
-        for (i = 0; i < n; i++) {
-            if (i === i0) {
+        for (var i$2 = 0; i$2 < n; i$2++) {
+            if (i$2 === i0) {
                 continue;
             }
-            d = dist(coords[2 * i0], coords[2 * i0 + 1], coords[2 * i], coords[2 * i + 1]);
-            if (d < minDist && d > 0) {
-                i1 = i;
-                minDist = d;
+            var d$1 = dist(i0x, i0y, coords[2 * i$2], coords[2 * i$2 + 1]);
+            if (d$1 < minDist && d$1 > 0) {
+                i1 = i$2;
+                minDist = d$1;
             }
         }
+        var i1x = coords[2 * i1];
+        var i1y = coords[2 * i1 + 1];
 
         var minRadius = Infinity;
 
         // find the third point which forms the smallest circumcircle with the first two
-        for (i = 0; i < n; i++) {
-            if (i === i0 || i === i1) {
+        for (var i$3 = 0; i$3 < n; i$3++) {
+            if (i$3 === i0 || i$3 === i1) {
                 continue;
             }
-
-            var r = circumradius(
-                coords[2 * i0], coords[2 * i0 + 1],
-                coords[2 * i1], coords[2 * i1 + 1],
-                coords[2 * i], coords[2 * i + 1]);
-
+            var r = circumradius(i0x, i0y, i1x, i1y, coords[2 * i$3], coords[2 * i$3 + 1]);
             if (r < minRadius) {
-                i2 = i;
+                i2 = i$3;
                 minRadius = r;
             }
         }
+        var i2x = coords[2 * i2];
+        var i2y = coords[2 * i2 + 1];
 
         if (minRadius === Infinity) {
             throw new Error('No Delaunay triangulation exists for this input.');
         }
 
         // swap the order of the seed points for counter-clockwise orientation
-        if (area$1(coords[2 * i0], coords[2 * i0 + 1],
-                coords[2 * i1], coords[2 * i1 + 1],
-                coords[2 * i2], coords[2 * i2 + 1]) < 0) {
-
-            var tmp = i1;
+        if (orient(i0x, i0y, i1x, i1y, i2x, i2y)) {
+            var i$4 = i1;
+            var x$1 = i1x;
+            var y$1 = i1y;
             i1 = i2;
-            i2 = tmp;
+            i1x = i2x;
+            i1y = i2y;
+            i2 = i$4;
+            i2x = x$1;
+            i2y = y$1;
         }
 
-        var i0x = coords[2 * i0];
-        var i0y = coords[2 * i0 + 1];
-        var i1x = coords[2 * i1];
-        var i1y = coords[2 * i1 + 1];
-        var i2x = coords[2 * i2];
-        var i2y = coords[2 * i2 + 1];
-
         var center = circumcenter(i0x, i0y, i1x, i1y, i2x, i2y);
         this._cx = center.x;
         this._cy = center.y;
 
         // sort the points by distance from the seed triangle circumcenter
         quicksort(ids, coords, 0, ids.length - 1, center.x, center.y);
 
         // initialize a hash table for storing edges of the advancing convex hull
         this._hashSize = Math.ceil(Math.sqrt(n));
-        this._hash = [];
-        for (i = 0; i < this._hashSize; i++) {
-            this$1._hash[i] = null;
-        }
+        this._hash = new Array(this._hashSize);
 
         // initialize a circular doubly-linked list that will hold an advancing convex hull
         var e = this.hull = insertNode(coords, i0);
         this._hashEdge(e);
         e.t = 0;
         e = insertNode(coords, i1, e);
         this._hashEdge(e);
@@ -25058,79 +24748,79 @@
         var triangles = this.triangles = new Uint32Array(maxTriangles * 3);
         var halfedges = this.halfedges = new Int32Array(maxTriangles * 3);
 
         this.trianglesLen = 0;
 
         this._addTriangle(i0, i1, i2, -1, -1, -1);
 
-        var xp, yp;
-        for (var k = 0; k < ids.length; k++) {
-            i = ids[k];
-            x = coords[2 * i];
-            y = coords[2 * i + 1];
+        for (var k = 0, xp = (void 0), yp = (void 0); k < ids.length; k++) {
+            var i$5 = ids[k];
+            var x$2 = coords[2 * i$5];
+            var y$2 = coords[2 * i$5 + 1];
 
-            // skip duplicate points
-            if (x === xp && y === yp) {
+            // skip near-duplicate points
+            if (k > 0 && Math.abs(x$2 - xp) <= EPSILON && Math.abs(y$2 - yp) <= EPSILON) {
                 continue;
             }
-            xp = x;
-            yp = y;
+            xp = x$2;
+            yp = y$2;
 
             // skip seed triangle points
-            if ((x === i0x && y === i0y) ||
-                (x === i1x && y === i1y) ||
-                (x === i2x && y === i2y)) {
+            if (i$5 === i0 || i$5 === i1 || i$5 === i2) {
                 continue;
             }
 
             // find a visible edge on the convex hull using edge hash
-            var startKey = this$1._hashKey(x, y);
+            var startKey = this$1._hashKey(x$2, y$2);
             var key = startKey;
-            var start;
+            var start = (void 0);
             do {
                 start = this$1._hash[key];
                 key = (key + 1) % this$1._hashSize;
             } while ((!start || start.removed) && key !== startKey);
 
+            start = start.prev;
             e = start;
-            while (area$1(x, y, e.x, e.y, e.next.x, e.next.y) >= 0) {
+            while (!orient(x$2, y$2, e.x, e.y, e.next.x, e.next.y)) {
                 e = e.next;
                 if (e === start) {
-                    throw new Error('Something is wrong with the input points.');
+                    e = null;
+                    break;
                 }
             }
+            // likely a near-duplicate point; skip it
+            if (!e) {
+                continue;
+            }
 
             var walkBack = e === start;
 
             // add the first triangle from the point
-            var t = this$1._addTriangle(e.i, i, e.next.i, -1, -1, e.t);
+            var t = this$1._addTriangle(e.i, i$5, e.next.i, -1, -1, e.t);
 
             e.t = t; // keep track of boundary triangles on the hull
-            e = insertNode(coords, i, e);
+            e = insertNode(coords, i$5, e);
 
             // recursively flip triangles from the point until they satisfy the Delaunay condition
             e.t = this$1._legalize(t + 2);
-            if (e.prev.prev.t === halfedges[t + 1]) {
-                e.prev.prev.t = t + 2;
-            }
 
             // walk forward through the hull, adding more triangles and flipping recursively
             var q = e.next;
-            while (area$1(x, y, q.x, q.y, q.next.x, q.next.y) < 0) {
-                t = this$1._addTriangle(q.i, i, q.next.i, q.prev.t, -1, q.t);
+            while (orient(x$2, y$2, q.x, q.y, q.next.x, q.next.y)) {
+                t = this$1._addTriangle(q.i, i$5, q.next.i, q.prev.t, -1, q.t);
                 q.prev.t = this$1._legalize(t + 2);
                 this$1.hull = removeNode(q);
                 q = q.next;
             }
 
             if (walkBack) {
                 // walk backward from the other side, adding more triangles and flipping
                 q = e.prev;
-                while (area$1(x, y, q.prev.x, q.prev.y, q.x, q.y) < 0) {
-                    t = this$1._addTriangle(q.prev.i, i, q.i, -1, q.t, q.prev.t);
+                while (orient(x$2, y$2, q.prev.x, q.prev.y, q.x, q.y)) {
+                    t = this$1._addTriangle(q.prev.i, i$5, q.i, -1, q.t, q.prev.t);
                     this$1._legalize(t + 2);
                     q.prev.t = t;
                     this$1.hull = removeNode(q);
                     q = q.prev;
                 }
             }
 
@@ -25138,166 +24828,208 @@
             this$1._hashEdge(e);
             this$1._hashEdge(e.prev);
         }
 
         // trim typed triangle mesh arrays
         this.triangles = triangles.subarray(0, this.trianglesLen);
         this.halfedges = halfedges.subarray(0, this.trianglesLen);
-    }
+    };
 
-    Delaunator.prototype = {
+    Delaunator.from = function from(points, getX, getY) {
+        if (!getX) {
+            getX = defaultGetX;
+        }
+        if (!getY) {
+            getY = defaultGetY;
+        }
 
-        _hashEdge: function(e) {
-            this._hash[this._hashKey(e.x, e.y)] = e;
-        },
+        var n = points.length;
+        var coords = new Float64Array(n * 2);
 
-        _hashKey: function(x, y) {
-            var dx = x - this._cx;
-            var dy = y - this._cy;
-            // use pseudo-angle: a measure that monotonically increases
-            // with real angle, but doesn't require expensive trigonometry
-            var p = 1 - dx / (Math.abs(dx) + Math.abs(dy));
-            return Math.floor((2 + (dy < 0 ? -p : p)) / 4 * this._hashSize);
-        },
+        for (var i = 0; i < n; i++) {
+            var p = points[i];
+            coords[2 * i] = getX(p);
+            coords[2 * i + 1] = getY(p);
+        }
 
-        _legalize: function(a) {
-            var triangles = this.triangles;
-            var coords = this.coords;
-            var halfedges = this.halfedges;
-
-            var b = halfedges[a];
-
-            var a0 = a - a % 3;
-            var b0 = b - b % 3;
-
-            var al = a0 + (a + 1) % 3;
-            var ar = a0 + (a + 2) % 3;
-            var bl = b0 + (b + 2) % 3;
-
-            var p0 = triangles[ar];
-            var pr = triangles[a];
-            var pl = triangles[al];
-            var p1 = triangles[bl];
-
-            var illegal = inCircle(
-                coords[2 * p0], coords[2 * p0 + 1],
-                coords[2 * pr], coords[2 * pr + 1],
-                coords[2 * pl], coords[2 * pl + 1],
-                coords[2 * p1], coords[2 * p1 + 1]);
-
-            if (illegal) {
-                triangles[a] = p1;
-                triangles[b] = p0;
-
-                this._link(a, halfedges[bl]);
-                this._link(b, halfedges[ar]);
-                this._link(ar, bl);
+        return new Delaunator(coords);
+    };
 
-                var br = b0 + (b + 1) % 3;
+    Delaunator.prototype._hashEdge = function _hashEdge(e) {
+        this._hash[this._hashKey(e.x, e.y)] = e;
+    };
 
-                this._legalize(a);
-                return this._legalize(br);
-            }
+    Delaunator.prototype._hashKey = function _hashKey(x, y) {
+        return Math.floor(pseudoAngle(x - this._cx, y - this._cy) * this._hashSize) % this._hashSize;
+    };
 
+    Delaunator.prototype._legalize = function _legalize(a) {
+        var ref = this;
+        var triangles = ref.triangles;
+        var coords = ref.coords;
+        var halfedges = ref.halfedges;
+
+        var b = halfedges[a];
+
+        /* if the pair of triangles doesn't satisfy the Delaunay condition
+         * (p1 is inside the circumcircle of [p0, pl, pr]), flip them,
+         * then do the same check/flip recursively for the new pair of triangles
+         *
+         *       pl                pl
+         *      /||\              /  \
+         *   al/ || \bl        al/\a
+         *    /  ||  \          /  \
+         *   /  a||b  \flip/___ar___\
+         * p0\   ||   /p1   =>   p0\---bl---/p1
+         *    \  ||  /          \  /
+         *   ar\ || /br         b\/br
+         *      \||/              \  /
+         *       pr                pr
+         */
+        var a0 = a - a % 3;
+        var b0 = b - b % 3;
+
+        var al = a0 + (a + 1) % 3;
+        var ar = a0 + (a + 2) % 3;
+        var bl = b0 + (b + 2) % 3;
+
+        if (b === -1) {
             return ar;
-        },
+        }
 
-        _link: function(a, b) {
-            this.halfedges[a] = b;
-            if (b !== -1) {
-                this.halfedges[b] = a;
+        var p0 = triangles[ar];
+        var pr = triangles[a];
+        var pl = triangles[al];
+        var p1 = triangles[bl];
+
+        var illegal = inCircle(
+            coords[2 * p0], coords[2 * p0 + 1],
+            coords[2 * pr], coords[2 * pr + 1],
+            coords[2 * pl], coords[2 * pl + 1],
+            coords[2 * p1], coords[2 * p1 + 1]);
+
+        if (illegal) {
+            triangles[a] = p1;
+            triangles[b] = p0;
+
+            var hbl = halfedges[bl];
+
+            // edge swapped on the other side of the hull (rare); fix the halfedge reference
+            if (hbl === -1) {
+                var e = this.hull;
+                do {
+                    if (e.t === bl) {
+                        e.t = a;
+                        break;
+                    }
+                    e = e.next;
+                } while (e !== this.hull);
             }
-        },
+            this._link(a, hbl);
+            this._link(b, halfedges[ar]);
+            this._link(ar, bl);
 
-        // add a new triangle given vertex indices and adjacent half-edge ids
-        _addTriangle: function(i0, i1, i2, a, b, c) {
-            var t = this.trianglesLen;
+            var br = b0 + (b + 1) % 3;
 
-            this.triangles[t] = i0;
-            this.triangles[t + 1] = i1;
-            this.triangles[t + 2] = i2;
-
-            this._link(t, a);
-            this._link(t + 1, b);
-            this._link(t + 2, c);
+            this._legalize(a);
+            return this._legalize(br);
+        }
 
-            this.trianglesLen += 3;
+        return ar;
+    };
 
-            return t;
+    Delaunator.prototype._link = function _link(a, b) {
+        this.halfedges[a] = b;
+        if (b !== -1) {
+            this.halfedges[b] = a;
         }
     };
 
+    // add a new triangle given vertex indices and adjacent half-edge ids
+    Delaunator.prototype._addTriangle = function _addTriangle(i0, i1, i2, a, b, c) {
+        var t = this.trianglesLen;
+
+        this.triangles[t] = i0;
+        this.triangles[t + 1] = i1;
+        this.triangles[t + 2] = i2;
+
+        this._link(t, a);
+        this._link(t + 1, b);
+        this._link(t + 2, c);
+
+        this.trianglesLen += 3;
+
+        return t;
+    };
+
+    // monotonically increases with real angle, but doesn't need expensive trigonometry
+    function pseudoAngle(dx, dy) {
+        var p = dx / (Math.abs(dx) + Math.abs(dy));
+        return (dy > 0 ? 3 - p : 1 + p) / 4; // [0..1]
+    }
+
     function dist(ax, ay, bx, by) {
         var dx = ax - bx;
         var dy = ay - by;
         return dx * dx + dy * dy;
     }
 
-    function area$1(px, py, qx, qy, rx, ry) {
-        return (qy - py) * (rx - qx) - (qx - px) * (ry - qy);
+    function orient(px, py, qx, qy, rx, ry) {
+        return (qy - py) * (rx - qx) - (qx - px) * (ry - qy) < 0;
     }
 
     function inCircle(ax, ay, bx, by, cx, cy, px, py) {
-        ax -= px;
-        ay -= py;
-        bx -= px;
-        by -= py;
-        cx -= px;
-        cy -= py;
-
-        var ap = ax * ax + ay * ay;
-        var bp = bx * bx + by * by;
-        var cp = cx * cx + cy * cy;
-
-        return ax * (by * cp - bp * cy) -
-            ay * (bx * cp - bp * cx) +
-            ap * (bx * cy - by * cx) < 0;
+        var dx = ax - px;
+        var dy = ay - py;
+        var ex = bx - px;
+        var ey = by - py;
+        var fx = cx - px;
+        var fy = cy - py;
+
+        var ap = dx * dx + dy * dy;
+        var bp = ex * ex + ey * ey;
+        var cp = fx * fx + fy * fy;
+
+        return dx * (ey * cp - bp * fy) -
+            dy * (ex * cp - bp * fx) +
+            ap * (ex * fy - ey * fx) < 0;
     }
 
     function circumradius(ax, ay, bx, by, cx, cy) {
-        bx -= ax;
-        by -= ay;
-        cx -= ax;
-        cy -= ay;
-
-        var bl = bx * bx + by * by;
-        var cl = cx * cx + cy * cy;
+        var dx = bx - ax;
+        var dy = by - ay;
+        var ex = cx - ax;
+        var ey = cy - ay;
+
+        var bl = dx * dx + dy * dy;
+        var cl = ex * ex + ey * ey;
+        var d = dx * ey - dy * ex;
 
-        if (bl === 0 || cl === 0) {
-            return Infinity;
-        }
-
-        var d = bx * cy - by * cx;
-        if (d === 0) {
-            return Infinity;
-        }
+        var x = (ey * bl - dy * cl) * 0.5 / d;
+        var y = (dx * cl - ex * bl) * 0.5 / d;
 
-        var x = (cy * bl - by * cl) * 0.5 / d;
-        var y = (bx * cl - cx * bl) * 0.5 / d;
-
-        return x * x + y * y;
+        return bl && cl && d && (x * x + y * y) || Infinity;
     }
 
     function circumcenter(ax, ay, bx, by, cx, cy) {
-        bx -= ax;
-        by -= ay;
-        cx -= ax;
-        cy -= ay;
-
-        var bl = bx * bx + by * by;
-        var cl = cx * cx + cy * cy;
+        var dx = bx - ax;
+        var dy = by - ay;
+        var ex = cx - ax;
+        var ey = cy - ay;
+
+        var bl = dx * dx + dy * dy;
+        var cl = ex * ex + ey * ey;
+        var d = dx * ey - dy * ex;
 
-        var d = bx * cy - by * cx;
-
-        var x = (cy * bl - by * cl) * 0.5 / d;
-        var y = (bx * cl - cx * bl) * 0.5 / d;
+        var x = ax + (ey * bl - dy * cl) * 0.5 / d;
+        var y = ay + (dx * cl - ex * bl) * 0.5 / d;
 
         return {
-            x: ax + x,
-            y: ay + y
+            x: x,
+            y: y
         };
     }
 
     // create a new node in a doubly linked list
     function insertNode(coords, i, prev) {
         var node = {
             i: i,
@@ -25398,14 +25130,16 @@
         return p[0];
     }
 
     function defaultGetY(p) {
         return p[1];
     }
 
+    var epsilon$3 = 1e-6;
+
     var Path$1 = function Path() {
         this._x0 = this._y0 = // start of current subpath
             this._x1 = this._y1 = null; // end of current subpath
         this._ = "";
     };
     Path$1.prototype.moveTo = function moveTo(x, y) {
         this._ += "M" + (this._x0 = this._x1 = +x) + "," + (this._y0 = this._y1 = +y);
@@ -25424,15 +25158,15 @@
         var x0 = x + r;
         var y0 = y;
         if (r < 0) {
             throw new Error("negative radius");
         }
         if (this._x1 === null) {
             this._ += "M" + x0 + "," + y0;
-        } else if (Math.abs(this._x1 - x0) > epsilon || Math.abs(this._y1 - y0) > epsilon) {
+        } else if (Math.abs(this._x1 - x0) > epsilon$3 || Math.abs(this._y1 - y0) > epsilon$3) {
             this._ += "L" + x0 + "," + y0;
         }
         if (!r) {
             return;
         }
         this._ += "A" + r + "," + r + ",0,1,1," + (x - r) + "," + y + "A" + r + "," + r + ",0,1,1," + (this._x1 = x0) + "," + (this._y1 = y0);
     };
@@ -25467,100 +25201,63 @@
         var ymax = ref[3];
 
         if (!((xmax = +xmax) >= (xmin = +xmin)) || !((ymax = +ymax) >= (ymin = +ymin))) {
             throw new Error("invalid bounds");
         }
         var ref$1 = this.delaunay = delaunay;
         var points = ref$1.points;
-        var halfedges = ref$1.halfedges;
         var hull = ref$1.hull;
         var triangles = ref$1.triangles;
         var circumcenters = this.circumcenters = new Float64Array(triangles.length / 3 * 2);
-        var edges = this.edges = new Uint32Array(halfedges.length);
-        var index = this.index = new Uint32Array(points.length);
         var vectors = this.vectors = new Float64Array(points.length * 2);
         this.xmax = xmax, this.xmin = xmin;
         this.ymax = ymax, this.ymin = ymin;
 
-        // Compute cell topology.
-        for (var i = 0, e = 0, m = halfedges.length; i < m; ++i) {
-            var t = triangles[i]; // Cell vertex.
-            if (index[t * 2] !== index[t * 2 + 1]) {
-                continue;
-            } // Already connected.
-            var e0 = index[t * 2] = e;
-            var j = i;
-
-            do { // Walk forward.
-                edges[e++] = Math.floor(j / 3);
-                j = halfedges[j];
-                if (j === -1) { // Went off the convex hull; walk backward.
-                    var e1 = e;
-                    j = i;
-                    do {
-                        j = halfedges[j % 3 === 0 ? j + 2 : j - 1];
-                        if (j === -1 || triangles[j] !== t) {
-                            break;
-                        }
-                        edges[e++] = Math.floor(j / 3);
-                    } while (j !== i);
-                    if (e1 < e) {
-                        edges.subarray(e0, e1).reverse();
-                        edges.subarray(e0, e).reverse();
-                    }
-                    break;
-                }
-                j = j % 3 === 2 ? j - 2 : j + 1;
-                if (triangles[j] !== t) {
-                    break;
-                } // Bad triangulation; break early.
-            } while (j !== i);
-
-            index[t * 2 + 1] = e;
-        }
-
         // Compute circumcenters.
-        for (var i$1 = 0, j$1 = 0, n = triangles.length; i$1 < n; i$1 += 3, j$1 += 2) {
-            var t1 = triangles[i$1] * 2;
-            var t2 = triangles[i$1 + 1] * 2;
-            var t3 = triangles[i$1 + 2] * 2;
-            var x1 = points[t1];
-            var y1 = points[t1 + 1];
+        for (var i = 0, j = 0, n = triangles.length; i < n; i += 3, j += 2) {
+            var t1 = triangles[i] * 2;
+            var t2 = triangles[i + 1] * 2;
+            var t3 = triangles[i + 2] * 2;
+            var x1$1 = points[t1];
+            var y1$1 = points[t1 + 1];
             var x2 = points[t2];
             var y2 = points[t2 + 1];
             var x3 = points[t3];
             var y3 = points[t3 + 1];
-            var a2 = x1 - x2;
-            var a3 = x1 - x3;
-            var b2 = y1 - y2;
-            var b3 = y1 - y3;
-            var d1 = x1 * x1 + y1 * y1;
+            var a2 = x1$1 - x2;
+            var a3 = x1$1 - x3;
+            var b2 = y1$1 - y2;
+            var b3 = y1$1 - y3;
+            var d1 = x1$1 * x1$1 + y1$1 * y1$1;
             var d2 = d1 - x2 * x2 - y2 * y2;
             var d3 = d1 - x3 * x3 - y3 * y3;
             var ab = (a3 * b2 - a2 * b3) * 2;
-            circumcenters[j$1] = (b2 * d3 - b3 * d2) / ab;
-            circumcenters[j$1 + 1] = (a3 * d2 - a2 * d3) / ab;
+            circumcenters[j] = (b2 * d3 - b3 * d2) / ab;
+            circumcenters[j + 1] = (a3 * d2 - a2 * d3) / ab;
         }
 
         // Compute exterior cell rays.
-        for (var n$1 = hull.length, p0 = (void 0), x0 = (void 0), y0 = (void 0), p1 = triangles[hull[n$1 - 1]] * 2, x1$1 = points[p1], y1$1 = points[p1 + 1], i$2 = 0; i$2 < n$1; ++i$2) {
-            p0 = p1, x0 = x1$1, y0 = y1$1, p1 = triangles[hull[i$2]] * 2, x1$1 = points[p1], y1$1 = points[p1 + 1];
-            vectors[p0 * 2 + 2] = vectors[p1 * 2] = y0 - y1$1;
-            vectors[p0 * 2 + 3] = vectors[p1 * 2 + 1] = x1$1 - x0;
-        }
+        var node = hull;
+        var p0, p1 = node.i * 4;
+        var x0, x1 = node.x;
+        var y0, y1 = node.y;
+        do {
+            node = node.next, p0 = p1, x0 = x1, y0 = y1, p1 = node.i * 4, x1 = node.x, y1 = node.y;
+            vectors[p0 + 2] = vectors[p1] = y0 - y1;
+            vectors[p0 + 3] = vectors[p1 + 1] = x1 - x0;
+        } while (node !== hull);
     };
     Voronoi.prototype.render = function render(context) {
         var this$1 = this;
 
         var buffer = context == null ? context = new Path$1 : undefined;
         var ref = this;
         var ref_delaunay = ref.delaunay;
         var halfedges = ref_delaunay.halfedges;
         var hull = ref_delaunay.hull;
-        var triangles = ref_delaunay.triangles;
         var circumcenters = ref.circumcenters;
         var vectors = ref.vectors;
         for (var i = 0, n = halfedges.length; i < n; ++i) {
             var j = halfedges[i];
             if (j < i) {
                 continue;
             }
@@ -25568,24 +25265,26 @@
             var tj = Math.floor(j / 3) * 2;
             var xi = circumcenters[ti];
             var yi = circumcenters[ti + 1];
             var xj = circumcenters[tj];
             var yj = circumcenters[tj + 1];
             this$1._renderSegment(xi, yi, xj, yj, context);
         }
-        for (var i$1 = 0, n$1 = hull.length; i$1 < n$1; ++i$1) {
-            var t = Math.floor(hull[i$1] / 3) * 2;
+        var node = hull;
+        do {
+            node = node.next;
+            var t = Math.floor(node.t / 3) * 2;
             var x = circumcenters[t];
             var y = circumcenters[t + 1];
-            var v = triangles[hull[i$1]] * 4;
+            var v = node.i * 4;
             var p = this$1._project(x, y, vectors[v + 2], vectors[v + 3]);
             if (p) {
                 this$1._renderSegment(x, y, p[0], p[1], context);
             }
-        }
+        } while (node !== hull);
         return buffer && buffer.value();
     };
     Voronoi.prototype.renderBounds = function renderBounds(context) {
         var buffer = context == null ? context = new Path$1 : undefined;
         context.rect(this.xmin, this.ymin, this.xmax - this.xmin, this.ymax - this.ymin);
         return buffer && buffer.value();
     };
@@ -25631,97 +25330,38 @@
             context.lineTo(S[2], S[3]);
         }
     };
     Voronoi.prototype.contains = function contains(i, x, y) {
         if ((x = +x, x !== x) || (y = +y, y !== y)) {
             return false;
         }
-        return this._step(i, x, y) === i;
-    };
-    Voronoi.prototype.find = function find(x, y, i) {
-        if (i === void 0) i = 0;
-
-        if ((x = +x, x !== x) || (y = +y, y !== y)) {
-            return -1;
-        }
-        var c;
-        while ((c = this._step(i, x, y)) >= 0 && c !== i) {
-            i = c;
-        }
-        return c;
-    };
-    Voronoi.prototype._step = function _step(i, x, y) {
-        var ref = this;
-        var ref_delaunay = ref.delaunay;
-        var points = ref_delaunay.points;
-        var triangles = ref_delaunay.triangles;
-        var edges = ref.edges;
-        var index = ref.index;
-        if (points.length === 0) {
-            return -1;
-        } // Empty triangulation.
-        var j0 = index[i * 2];
-        var j1 = index[i * 2 + 1];
-        if (j0 === j1) {
-            return -1;
-        } // Coincident point.
-        var c = i,
-            k = edges[j0] * 3;
-        var dc = Math.pow((x - points[c * 2]), 2) + Math.pow((y - points[c * 2 + 1]), 2);
-        switch (i) { // Test previous point on triangle (for hull).
-            case triangles[k]:
-                k = triangles[k + 2];
-                break;
-            case triangles[k + 1]:
-                k = triangles[k];
-                break;
-            case triangles[k + 2]:
-                k = triangles[k + 1];
-                break;
-        }
-        var dk = Math.pow((x - points[k * 2]), 2) + Math.pow((y - points[k * 2 + 1]), 2);
-        if (dk < dc) {
-            dc = dk, c = k;
-        }
-        for (var j = j0; j < j1; ++j) {
-            k = edges[j] * 3;
-            switch (i) { // Test next point on triangle.
-                case triangles[k]:
-                    k = triangles[k + 1];
-                    break;
-                case triangles[k + 1]:
-                    k = triangles[k + 2];
-                    break;
-                case triangles[k + 2]:
-                    k = triangles[k];
-                    break;
-            }
-            dk = Math.pow((x - points[k * 2]), 2) + Math.pow((y - points[k * 2 + 1]), 2);
-            if (dk < dc) {
-                dc = dk, c = k;
-            }
-        }
-        return c;
+        return this.delaunay._step(i, x, y) === i;
     };
     Voronoi.prototype._cell = function _cell(i) {
         var ref = this;
-        var index = ref.index;
-        var edges = ref.edges;
         var circumcenters = ref.circumcenters;
-        var t0 = index[i * 2];
-        var t1 = index[i * 2 + 1];
-        if (t0 === t1) {
+        var ref_delaunay = ref.delaunay;
+        var inedges = ref_delaunay.inedges;
+        var halfedges = ref_delaunay.halfedges;
+        var triangles = ref_delaunay.triangles;
+        var e0 = inedges[i];
+        if (e0 === -1) {
             return null;
-        }
-        var points = new Float64Array((t1 - t0) * 2);
-        for (var t = t0, j = 0; t < t1; ++t, j += 2) {
-            var ti = edges[t] * 2;
-            points[j] = circumcenters[ti];
-            points[j + 1] = circumcenters[ti + 1];
-        }
+        } // coincident point
+        var points = [];
+        var e = e0;
+        do {
+            var t = Math.floor(e / 3);
+            points.push(circumcenters[t * 2], circumcenters[t * 2 + 1]);
+            e = e % 3 === 2 ? e - 2 : e + 1;
+            if (triangles[e] !== i) {
+                break;
+            } // bad triangulation
+            e = halfedges[e];
+        } while (e !== e0 && e !== -1);
         return points;
     };
     Voronoi.prototype._clip = function _clip(i) {
         var points = this._cell(i);
         if (points === null) {
             return null;
         }
@@ -25950,20 +25590,89 @@
     var Delaunay = function Delaunay(points) {
         var ref = new Delaunator(points);
         var halfedges = ref.halfedges;
         var hull = ref.hull;
         var triangles = ref.triangles;
         this.points = points;
         this.halfedges = halfedges;
-        this.hull = Uint32Array.from(hullIterable(hull));
+        this.hull = hull;
         this.triangles = triangles;
+        var inedges = this.inedges = new Int32Array(points.length / 2).fill(-1);
+        var outedges = this.outedges = new Int32Array(points.length / 2).fill(-1);
+
+        // Compute an index from each point to an (arbitrary) incoming halfedge.
+        for (var e = 0, n = halfedges.length; e < n; ++e) {
+            inedges[triangles[e % 3 === 2 ? e - 2 : e + 1]] = e;
+        }
+
+        // For points on the hull, index both the incoming and outgoing halfedges.
+        var node0, node1 = hull;
+        do {
+            node0 = node1, node1 = node1.next;
+            inedges[node1.i] = node0.t;
+            outedges[node0.i] = node1.t;
+        } while (node1 !== hull);
     };
     Delaunay.prototype.voronoi = function voronoi(bounds) {
         return new Voronoi(this, bounds);
     };
+    Delaunay.prototype.neighbors = function* neighbors(i) {
+        var ref = this;
+        var inedges = ref.inedges;
+        var outedges = ref.outedges;
+        var halfedges = ref.halfedges;
+        var triangles = ref.triangles;
+        var e0 = inedges[i];
+        if (e0 === -1) {
+            return;
+        } // coincident point
+        var e = e0;
+        do {
+            yield triangles[e];
+            e = e % 3 === 2 ? e - 2 : e + 1;
+            if (triangles[e] !== i) {
+                return;
+            } // bad triangulation
+            e = halfedges[e];
+            if (e === -1) {
+                return yield triangles[outedges[i]];
+            }
+        } while (e !== e0);
+    };
+    Delaunay.prototype.find = function find(x, y, i) {
+        if (i === void 0) i = 0;
+
+        if ((x = +x, x !== x) || (y = +y, y !== y)) {
+            return -1;
+        }
+        var c;
+        while ((c = this._step(i, x, y)) >= 0 && c !== i) {
+            i = c;
+        }
+        return c;
+    };
+    Delaunay.prototype._step = function _step(i, x, y) {
+        var this$1 = this;
+
+        var ref = this;
+        var inedges = ref.inedges;
+        var points = ref.points;
+        if (inedges[i] === -1) {
+            return -1;
+        } // coincident point
+        var c = i;
+        var dc = Math.pow((x - points[i * 2]), 2) + Math.pow((y - points[i * 2 + 1]), 2);
+        for (var t of this$1.neighbors(i)) {
+            var dt = Math.pow((x - points[t * 2]), 2) + Math.pow((y - points[t * 2 + 1]), 2);
+            if (dt < dc) {
+                dc = dt, c = t;
+            }
+        }
+        return c;
+    };
     Delaunay.prototype.render = function render(context) {
         var buffer = context == null ? context = new Path$1 : undefined;
         var ref = this;
         var points = ref.points;
         var halfedges = ref.halfedges;
         var triangles = ref.triangles;
         for (var i = 0, n = halfedges.length; i < n; ++i) {
@@ -25992,24 +25701,21 @@
             context.arc(x, y, r, 0, tau$2);
         }
         return buffer && buffer.value();
     };
     Delaunay.prototype.renderHull = function renderHull(context) {
         var buffer = context == null ? context = new Path$1 : undefined;
         var ref = this;
-        var points = ref.points;
         var hull = ref.hull;
-        var triangles = ref.triangles;
-        var n = hull.length;
-        var i0, i1 = triangles[hull[n - 1]] * 2;
-        for (var i = 0; i < n; ++i) {
-            i0 = i1, i1 = triangles[hull[i]] * 2;
-            context.moveTo(points[i0], points[i0 + 1]);
-            context.lineTo(points[i1], points[i1 + 1]);
+        var node = hull;
+        context.moveTo(node.x, node.y);
+        while (node = node.next, node !== hull) {
+            context.lineTo(node.x, node.y);
         }
+        context.closePath();
         return buffer && buffer.value();
     };
     Delaunay.prototype.hullPolygon = function hullPolygon() {
         var polygon = new Polygon;
         this.renderHull(polygon);
         return polygon.value();
     };
@@ -26067,22 +25773,14 @@
         for (var p of points) {
             yield fx.call(that, p, i, points);
             yield fy.call(that, p, i, points);
             ++i;
         }
     }
 
-    function* hullIterable(hull) {
-        var node = hull;
-        do {
-            yield node.t;
-        }
-        while ((node = node.next) !== hull);
-    }
-
     var noop$1 = {
         value: function() {}
     };
 
     function dispatch() {
         var arguments$1 = arguments;
 
@@ -28687,16 +28385,15 @@
         });
 
         if (this.type === 'Transaction') {
             entryData.postings = [];
             $$('.posting', this.form).forEach(function(posting) {
                 entryData.postings.push({
                     account: posting.querySelector('.account').value,
-                    number: posting.querySelector('.number').value,
-                    currency: posting.querySelector('.currency').value,
+                    amount: posting.querySelector('.amount').value,
                 });
             });
         }
 
         if (this.type === 'Balance') {
             entryData.account = this.form.querySelector('.account').value;
         }
@@ -28727,20 +28424,19 @@
         }
         $('[name=narration]', this.form).value = entry.narration;
         $$('.posting', this.form).forEach(function(el) {
             el.remove();
         });
         entry.postings.forEach(function(posting) {
             var account = posting.account;
-            var units = posting.units;
+            var amount = posting.amount;
             var row = this$1.addPosting();
             $('.account', row).value = account;
-            if (units) {
-                $('.number', row).value = formatCurrency(units.number);
-                $('.currency', row).value = units.currency;
+            if (amount) {
+                $('.amount', row).value = amount;
             }
         });
     };
 
     // Submit an Array of forms (do nothing if one of them is invalid).
     EntryForm.submit = function submit(forms, successCallback) {
         var jsonData = {
@@ -28848,41 +28544,47 @@
 
         $.delegate(ingest, 'click', '.actions input', function(event) {
             var input = event.target;
             input.closest('.ingest-row').className = "ingest-row " + (input.value);
         });
     });
 
+    function addFilter(value) {
+        var filter = $('#filter-filter');
+        if (filter.value) {
+            filter.value += " " + value;
+        } else {
+            filter.value = value;
+        }
+        e.trigger('form-submit-filters', filter.form);
+    }
+
     e.on('page-loaded', function() {
         var journal = $('#journal-table');
         if (!journal) {
             return;
         }
 
         $.delegate(journal, 'click', 'li', function(event) {
             if (event.target.tagName === 'A') {
                 return;
             }
-            // Filter for tags and links when clicking on them.
+
             if (event.target.className === 'tag' || event.target.className === 'link') {
-                var filter = $('#filter-filter');
-                filter.value += " " + (event.target.innerText);
-                e.trigger('form-submit-filters', filter.form);
-                return;
-            }
-            // Filter for metadata when clicking on the value.
-            if (event.target.tagName === 'DD') {
-                var filter$1 = $('#filter-filter');
-                filter$1.value += " " + (event.target.previousElementSibling.innerText) + "\"" + (event.target.innerText) + "\"";
-                e.trigger('form-submit-filters', filter$1.form);
-                return;
-            }
-            // Toggle postings by clicking on transaction row.
-            var transaction = event.target.closest('.transaction');
-            if (transaction) {
+                // Filter for tags and links when clicking on them.
+                addFilter(event.target.innerText);
+            } else if (event.target.className === 'payee') {
+                // Filter for payees when clicking on them.
+                addFilter(("payee:\"" + (event.target.innerText) + "\""));
+            } else if (event.target.tagName === 'DD') {
+                // Filter for metadata when clicking on the value.
+                addFilter((" " + (event.target.previousElementSibling.innerText) + "\"" + (event.target.innerText) + "\""));
+            } else if (event.target.closest('.indicators')) {
+                // Toggle postings and metadata by clicking on indicators.
+                var transaction = event.target.closest('.transaction');
                 transaction.classList.toggle('show-postings');
             }
         });
 
         // Toggle entries with buttons.
         $$('#entry-filters button').forEach(function(button) {
             button.addEventListener('click', function() {
```

### Comparing `fava-1.8/fava/static/images/favicon.ico` & `fava-1.9/fava/static/images/favicon.ico`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/templates/macros/_account_macros.html` & `fava-1.9/fava/templates/macros/_account_macros.html`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/templates/_aside.html` & `fava-1.9/fava/templates/_aside.html`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/templates/_charts.html` & `fava-1.9/fava/templates/_charts.html`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/templates/_context.html` & `fava-1.9/fava/templates/_context.html`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/templates/_entry_filters.html` & `fava-1.9/fava/templates/_entry_filters.html`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/templates/_entry_forms.html` & `fava-1.9/fava/templates/_entry_forms.html`

 * *Files 6% similar despite different names*

```diff
@@ -1,20 +1,22 @@
 {% macro input_account(account) %}
-<input type="text" class="account" placeholder="{{ _('Account') }}" list="accounts" value="{{ account or '' }}" required pattern="(?:[\p{Lu}][\p{L}\p{Nd}\-]*)(?::[\p{Lu}\p{Nd}][\p{L}\p{Nd}\-]*)+">
+<input type="text" class="account" placeholder="{{ _('Account') }}" list="accounts" value="{{ account or '' }}" pattern="{{ config.ACCOUNT_RE }}">
 {% endmacro %}
-{% macro input_date(date) %}
+{% macro input_date(date) -%}
 <input type="date" name="date" value="{{ date or today() }}" required>
-{% endmacro %}
+{%- endmacro %}
+{% macro input_number(number) -%}
+<input type="tel" class="number" pattern="[0-9.,]*" placeholder="{{ _('Number') }}" value="{{ number }}">
+{%- endmacro %}
 
 {% macro posting(posting=None) %}
 <div class="fieldset posting">
   <button class="muted round remove-fieldset" data-event="remove-fieldset" type="button" tabindex="-1">×</button>
   {{ input_account(posting.account) }}
-  <input type="tel" class="number" placeholder="{{ _('Number') }}" value="{{ posting.units.number if posting else '' }}">
-  <input type="text" class="currency" placeholder="{{ _('Currency') }}" list="currencies" value="{{ posting.units.currency if posting else '' }}">
+  <input type="text" class="amount" placeholder="{{ _('Amount') }}" value="{{ posting.amount if posting else '' }}">
   <button class="muted round add-row" type="button" data-event="add-posting" title="{{ _('Add posting') }}">+</button>
 </div>
 {% endmacro %}
 
 {% macro metadata(key=None, value=None) %}
 <div class="fieldset metadata-row">
   <button class="muted round remove-fieldset" data-event="remove-fieldset" type="button" tabindex="-1">×</button>
@@ -55,15 +57,15 @@
 
 {% macro Balance(entry=None) %}
 <div class="entry-form balance" data-type="Balance">
   <div class="fieldset">
     {{ input_date(entry.date) }}
     <h4>{{ _('Balance') }}</h4>
     {{ input_account(entry.account) }}
-    <input type="tel" class="number" name="number" placeholder="{{ _('Number') }}" value="{{ entry.amount.number if entry.amount else '' }}">
+    {{ input_number(entry.amount.number if entry.amount else '') }}
     <input type="text" class="currency" name="currency" placeholder="{{ _('Currency') }}" list="currencies" value="{{ entry.amount.currency if entry.amount else '' }}">
     <button class="muted round" type="button" data-event="add-metadata" title="{{ _('Add metadata') }}">m</button>
   </div>
   {{ entry_meta(entry.meta) }}
 </div>
 {% endmacro %}
```

### Comparing `fava-1.8/fava/templates/_globals.html` & `fava-1.9/fava/templates/_globals.html`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/templates/_journal_table.html` & `fava-1.9/fava/templates/_journal_table.html`

 * *Files 3% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 {% set entry_types = ['open', 'close', 'transaction', 'balance', 'note', 'document', 'pad', 'query', 'custom'] %}
 {% set sub_types = {
   'custom': (
     ('budget', 'B', _('Budget entries')),
   ),
   'document': (
     ('discovered', 'D', _('Documents with a #discovered tag')),
-    ('statement', 'S', _('Documents with a #statement tag')),
+    ('linked', 'L', _('Documents with a #linked tag')),
   ),
   'transaction': (
     ('cleared', '*', _('Cleared transactions')),
     ('pending', '!', _('Pending transactions')),
     ('other', 'x', _('Other transactions')),
   ),
 } %}
@@ -26,15 +26,15 @@
   'transaction': 's t',
   'cleared': 't c',
   'pending': 't p',
   'other': 't o',
 
   'document': 's d',
   'discovered': 'd d',
-  'statement': 'd s',
+  'linked': 'd l',
 } %}
 {% set short_type = {
    'balance': 'Bal',
    'close': 'Close',
    'document': 'Doc',
    'note': 'Note',
    'open': 'Open',
@@ -48,17 +48,17 @@
 {% macro account_link(name) %}<a class="account-link" href="{{ url_for('account', name=name) }}">{{ name }}</a>{% endmacro %}
 {% macro render_metadata(metadata, entry_hash=None) -%}
 {% if metadata %}
 <dl class="metadata">
   {% for key, value in metadata.items() %}
   <dt>{{ key }}:</dt>
   <dd>
-  {%- if key.startswith('statement') %}<a class="filename" data-remote target=_blank href="{{ url_for('statement', entry_hash=entry_hash, key=key) }}">{% endif -%}
+  {%- if key.startswith('document') %}<a class="filename" data-remote target=_blank href="{{ url_for('statement', entry_hash=entry_hash, key=key) }}">{% endif -%}
     {{ value }}
-    {%- if key.startswith('statement') %}</a>{% endif -%}
+    {%- if key.startswith('document') %}</a>{% endif -%}
   </dd>
   {% endfor %}
 </dl>
 {% endif %}
 {%- endmacro %}
 {% macro render_tags_links(entry) -%}
 {% for tag in entry.tags|sort %}<span class="tag">#{{ tag }}</span>{% endfor %}
@@ -98,15 +98,15 @@
 {% for entry in entries|reverse %}
     {% if show_change_and_balance %}
         {% set entry, _, change, balance = entry %}
     {% endif %}
     {% set type = entry.__class__.__name__.lower() %}
     {% set entry_hash = entry|hash_entry %}
     {% set metadata = entry.meta|remove_keys(['__tolerances__', '__automatic__', 'filename', 'lineno']) %}
-    <li class="{{ type }} {{ entry.type or '' }} {{ entry.flag|flag_to_type if entry.flag else '' }}{{ ' statement' if entry.tags and 'statement' in entry.tags else '' }}{{ ' discovered' if entry.tags and 'discovered' in entry.tags else '' }}">
+    <li class="{{ type }} {{ entry.type or '' }} {{ entry.flag|flag_to_type if entry.flag else '' }}{{ ' linked' if entry.tags and 'linked' in entry.tags else '' }}{{ ' discovered' if entry.tags and 'discovered' in entry.tags else '' }}">
         <p>
         <span class="datecell" data-sort-value=-{{ loop.index }}><a href="#context-{{ entry_hash }}">{{ entry.date }}</a></span>
         <span class="flag">{% if type == 'transaction' %}{{ entry.flag }}{% else %}{{ short_type.get(type, type[:3]) }}{% endif %}</span>
         <span class="description{% if type != 'transaction' %}"{% else %} droptarget" data-entry="{{ entry_hash }}" data-entry-date="{{ entry.date }}" data-account-name="{{ entry.postings[0].account if entry.postings else "" }}"{% endif %}>
         {% if type == 'open' or type == 'close' %}
             {{ account_link(entry.account) }}
         {% elif type == 'note' %}
@@ -131,15 +131,15 @@
         {% elif type == 'balance' %}
             {{ account_link(entry.account) }}
             {% if entry.diff_amount %}
             <span class="spacer"></span>
             accumulated <span class="num">{{ (entry.amount.number + entry.diff_amount.number)|format_currency(entry.amount.currency, show_if_zero=True) }} {{ entry.amount.currency }}</span>
             {% endif %}
         {% elif type == 'transaction' %}
-            <strong>{{ entry.payee or '' }}</strong>{% if entry.payee and entry.narration %}<span class="separator"></span> {% endif %}{{ entry.narration or '' }}
+            <strong class="payee">{{ entry.payee or '' }}</strong>{% if entry.payee and entry.narration %}<span class="separator"></span> {% endif %}{{ entry.narration or '' }}
             {{ render_tags_links(entry) }}
         {% endif %}
         </span>
         <span class="indicators">
           {% for key, value in metadata.items() %}
           <span class="metadata-indicator" title="{{ key }}: {{ value }}">{{ key[:2] }}</span>
           {% endfor %}
```

### Comparing `fava-1.8/fava/templates/_layout.html` & `fava-1.9/fava/templates/_layout.html`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/templates/_overlays.html` & `fava-1.9/fava/templates/_overlays.html`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/templates/_query_table.html` & `fava-1.9/fava/templates/_query_table.html`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/templates/_tree_table.html` & `fava-1.9/fava/templates/_tree_table.html`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/templates/account.html` & `fava-1.9/fava/templates/account.html`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/templates/balance_sheet.html` & `fava-1.9/fava/templates/balance_sheet.html`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/templates/beancount_file` & `fava-1.9/fava/templates/beancount_file`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/templates/commodities.html` & `fava-1.9/fava/templates/commodities.html`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/templates/editor.html` & `fava-1.9/fava/templates/editor.html`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/templates/errors.html` & `fava-1.9/fava/templates/errors.html`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/templates/events.html` & `fava-1.9/fava/templates/events.html`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/templates/extract.html` & `fava-1.9/fava/templates/extract.html`

 * *Files 1% similar despite different names*

```diff
@@ -22,15 +22,15 @@
   <div class="ingest-row{{ ' duplicate' if duplicate else ' import' }}">
     <div class="line">{% if entry.meta.lineno > 0 %}{{ entry.meta.lineno }}{% endif %}</div>
     <div class="source">
       {% if entry.meta['__source__'] %}
       <pre>{{ entry.meta['__source__'] }}</pre>
       {% endif %}
     </div>
-    {{ entry_forms[type](entry) if type in ['Balance', 'Note', 'Transaction'] else '' }}
+    {{ entry_forms[type](entry|serialise) if type in ['Balance', 'Note', 'Transaction'] else '' }}
     <div class="actions">
       <div class="inner">
         <label><input name="action-{{ loop.index }}" type="radio" value="ignore">{{ _('Ignore') }}</label>
         <label><input name="action-{{ loop.index }}" type="radio" value="duplicate"{{ ' checked' if duplicate else '' }}>{{ _('Duplicate') }}</label>
         <label><input name="action-{{ loop.index }}" type="radio" value="import"{{ ' checked' if not duplicate else '' }}>{{ _('Import') }}</label>
       </div>
     </div>
```

### Comparing `fava-1.8/fava/templates/help.html` & `fava-1.9/fava/templates/help.html`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/templates/holdings.html` & `fava-1.9/fava/templates/holdings.html`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/templates/import.html` & `fava-1.9/fava/templates/import.html`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/templates/income_statement.html` & `fava-1.9/fava/templates/income_statement.html`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/templates/options.html` & `fava-1.9/fava/templates/options.html`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/templates/query.html` & `fava-1.9/fava/templates/query.html`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/templates/statistics.html` & `fava-1.9/fava/templates/statistics.html`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/translations/de/LC_MESSAGES/messages.mo` & `fava-1.9/fava/translations/de/LC_MESSAGES/messages.mo`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/translations/de/LC_MESSAGES/messages.po` & `fava-1.9/fava/translations/de/LC_MESSAGES/messages.po`

 * *Files 1% similar despite different names*

```diff
@@ -22,15 +22,15 @@
 #: fava/templates/_entry_filters.html:3 fava/templates/_entry_forms.html:2
 #: fava/templates/_overlays.html:18 fava/templates/_tree_table.html:24
 #: fava/templates/_tree_table.html:105 fava/templates/holdings.html:48
 #: fava/templates/import.html:19 fava/templates/statistics.html:36
 msgid "Account"
 msgstr "Konto"
 
-#: fava/templates/_entry_forms.html:40 fava/templates/_entry_forms.html:41
+#: fava/templates/_entry_forms.html:42 fava/templates/_entry_forms.html:43
 msgid "Payee"
 msgstr "Empfänger"
 
 #: fava/templates/_globals.html:2
 msgid "Income Statement"
 msgstr "Gewinn- und Verlustrechnung"
 
@@ -103,15 +103,15 @@
 msgid "Cost"
 msgstr "Kosten"
 
 #: fava/templates/_journal_table.html:93
 msgid "Change"
 msgstr "Änderung"
 
-#: fava/templates/_entry_forms.html:60 fava/templates/_journal_table.html:94
+#: fava/templates/_entry_forms.html:62 fava/templates/_journal_table.html:94
 #: fava/templates/statistics.html:40
 msgid "Balance"
 msgstr "Saldo"
 
 #: fava/templates/_context.html:57 fava/templates/_overlays.html:33
 #: fava/templates/editor.html:41
 msgid "Save"
@@ -191,16 +191,15 @@
 msgid "Help - %(title)s"
 msgstr "Hilfe - %(title)s"
 
 #: fava/templates/help.html:9
 msgid "Help pages"
 msgstr "Hilfeseiten"
 
-#: fava/templates/_entry_forms.html:13 fava/templates/_entry_forms.html:63
-#: fava/templates/holdings.html:48
+#: fava/templates/_entry_forms.html:65 fava/templates/holdings.html:48
 msgid "Currency"
 msgstr "Währung"
 
 #: fava/templates/holdings.html:48
 msgid "Cost currency"
 msgstr "Kostenwährung"
 
@@ -216,20 +215,20 @@
 msgid "Income"
 msgstr "Einkommen"
 
 #: fava/templates/income_statement.html:10
 msgid "Expenses"
 msgstr "Ausgaben"
 
-#: fava/templates/_entry_forms.html:21 fava/templates/options.html:9
+#: fava/templates/_entry_forms.html:23 fava/templates/options.html:9
 #: fava/templates/options.html:26
 msgid "Key"
 msgstr "Schlüssel"
 
-#: fava/templates/_entry_forms.html:22 fava/templates/options.html:10
+#: fava/templates/_entry_forms.html:24 fava/templates/options.html:10
 #: fava/templates/options.html:27
 msgid "Value"
 msgstr "Wert"
 
 #: fava/templates/_query_table.html:69
 msgid "Download as"
 msgstr "Herunterladen als"
@@ -275,27 +274,27 @@
 msgid "close"
 msgstr "Schließen"
 
 #: fava/templates/_overlays.html:30
 msgid "New transaction"
 msgstr "Neue Transaktion"
 
-#: fava/templates/_entry_forms.html:42 fava/templates/_entry_forms.html:43
+#: fava/templates/_entry_forms.html:44 fava/templates/_entry_forms.html:45
 msgid "Narration"
 msgstr "Beschreibung"
 
 #: fava/templates/_overlays.html:34
 msgid "Save and add new"
 msgstr "Speichern und hinzufügen"
 
-#: fava/templates/_entry_forms.html:12 fava/templates/_entry_forms.html:62
+#: fava/templates/_entry_forms.html:8
 msgid "Number"
 msgstr "Zahl"
 
-#: fava/templates/_entry_forms.html:14 fava/templates/_entry_forms.html:45
+#: fava/templates/_entry_forms.html:16 fava/templates/_entry_forms.html:47
 msgid "Add posting"
 msgstr "Eintrag hinzufügen"
 
 #: fava/templates/_globals.html:11 fava/templates/extract.html:7
 #: fava/templates/extract.html:34
 msgid "Import"
 msgstr "Import"
@@ -344,20 +343,20 @@
 msgid "...enter a BQL query. 'help' to list available commands."
 msgstr "… BQL-Abfrage eingeben. 'help', um alle Befehle aufzulisten."
 
 #: fava/templates/_journal_table.html:80
 msgid "Metadata"
 msgstr "Metadaten"
 
-#: fava/templates/_entry_forms.html:23 fava/templates/_entry_forms.html:44
-#: fava/templates/_entry_forms.html:64 fava/templates/_entry_forms.html:76
+#: fava/templates/_entry_forms.html:25 fava/templates/_entry_forms.html:46
+#: fava/templates/_entry_forms.html:66 fava/templates/_entry_forms.html:78
 msgid "Add metadata"
 msgstr "Metadaten hinzufügen"
 
-#: fava/templates/_entry_forms.html:74
+#: fava/templates/_entry_forms.html:76
 msgid "Note"
 msgstr "Notiz"
 
 #: fava/templates/_context.html:4
 msgid "Location"
 msgstr ""
 
@@ -385,18 +384,14 @@
 msgid "Other transactions"
 msgstr ""
 
 #: fava/templates/_journal_table.html:7
 msgid "Documents with a #discovered tag"
 msgstr ""
 
-#: fava/templates/_journal_table.html:8
-msgid "Documents with a #statement tag"
-msgstr ""
-
 #: fava/templates/_journal_table.html:81
 msgid "Postings"
 msgstr ""
 
 #: fava/templates/_overlays.html:7
 msgid "Upload file(s)"
 msgstr ""
@@ -458,31 +453,39 @@
 msgid "Download currently filtered entries as a Beancount file"
 msgstr ""
 
 #: fava/templates/extract.html:40
 msgid "Import entries"
 msgstr ""
 
-#: fava/util/date.py:44
+#: fava/util/date.py:50
 msgid "Yearly"
 msgstr ""
 
-#: fava/util/date.py:45
+#: fava/util/date.py:51
 msgid "Quarterly"
 msgstr ""
 
-#: fava/util/date.py:46
+#: fava/util/date.py:52
 msgid "Monthly"
 msgstr ""
 
-#: fava/util/date.py:47
+#: fava/util/date.py:53
 msgid "Weekly"
 msgstr ""
 
-#: fava/util/date.py:48
+#: fava/util/date.py:54
 msgid "Daily"
 msgstr ""
 
 #: fava/templates/editor.html:18
 msgid "Edit"
 msgstr ""
 
+#: fava/templates/_entry_forms.html:15
+msgid "Amount"
+msgstr ""
+
+#: fava/templates/_journal_table.html:8
+msgid "Documents with a #linked tag"
+msgstr ""
+
```

### Comparing `fava-1.8/fava/translations/es/LC_MESSAGES/messages.mo` & `fava-1.9/fava/translations/es/LC_MESSAGES/messages.mo`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/translations/es/LC_MESSAGES/messages.po` & `fava-1.9/fava/translations/es/LC_MESSAGES/messages.po`

 * *Files 1% similar despite different names*

```diff
@@ -22,15 +22,15 @@
 #: fava/templates/_entry_filters.html:3 fava/templates/_entry_forms.html:2
 #: fava/templates/_overlays.html:18 fava/templates/_tree_table.html:24
 #: fava/templates/_tree_table.html:105 fava/templates/holdings.html:48
 #: fava/templates/import.html:19 fava/templates/statistics.html:36
 msgid "Account"
 msgstr "Cuenta"
 
-#: fava/templates/_entry_forms.html:40 fava/templates/_entry_forms.html:41
+#: fava/templates/_entry_forms.html:42 fava/templates/_entry_forms.html:43
 msgid "Payee"
 msgstr "Beneficiario"
 
 #: fava/templates/_globals.html:2
 msgid "Income Statement"
 msgstr "Cuenta de resultados"
 
@@ -105,15 +105,15 @@
 msgstr "Costo"
 
 #: fava/templates/_journal_table.html:93
 #, fuzzy
 msgid "Change"
 msgstr "Cambio"
 
-#: fava/templates/_entry_forms.html:60 fava/templates/_journal_table.html:94
+#: fava/templates/_entry_forms.html:62 fava/templates/_journal_table.html:94
 #: fava/templates/statistics.html:40
 msgid "Balance"
 msgstr "Saldo"
 
 #: fava/templates/_context.html:57 fava/templates/_overlays.html:33
 #: fava/templates/editor.html:41
 msgid "Save"
@@ -193,16 +193,15 @@
 msgid "Help - %(title)s"
 msgstr "Ayuda - %(title)s"
 
 #: fava/templates/help.html:9
 msgid "Help pages"
 msgstr "Páginas de ayuda"
 
-#: fava/templates/_entry_forms.html:13 fava/templates/_entry_forms.html:63
-#: fava/templates/holdings.html:48
+#: fava/templates/_entry_forms.html:65 fava/templates/holdings.html:48
 msgid "Currency"
 msgstr "Moneda"
 
 #: fava/templates/holdings.html:48
 msgid "Cost currency"
 msgstr "Divisa de costo"
 
@@ -218,20 +217,20 @@
 msgid "Income"
 msgstr "Ingresos"
 
 #: fava/templates/income_statement.html:10
 msgid "Expenses"
 msgstr "Gastos"
 
-#: fava/templates/_entry_forms.html:21 fava/templates/options.html:9
+#: fava/templates/_entry_forms.html:23 fava/templates/options.html:9
 #: fava/templates/options.html:26
 msgid "Key"
 msgstr "Clave"
 
-#: fava/templates/_entry_forms.html:22 fava/templates/options.html:10
+#: fava/templates/_entry_forms.html:24 fava/templates/options.html:10
 #: fava/templates/options.html:27
 msgid "Value"
 msgstr "Valor"
 
 #: fava/templates/_query_table.html:69
 msgid "Download as"
 msgstr "Descargar como"
@@ -277,27 +276,27 @@
 msgid "close"
 msgstr "cerrar"
 
 #: fava/templates/_overlays.html:30
 msgid "New transaction"
 msgstr "Nueva transacción"
 
-#: fava/templates/_entry_forms.html:42 fava/templates/_entry_forms.html:43
+#: fava/templates/_entry_forms.html:44 fava/templates/_entry_forms.html:45
 msgid "Narration"
 msgstr "Narración"
 
 #: fava/templates/_overlays.html:34
 msgid "Save and add new"
 msgstr "Guardar y añadir nueva"
 
-#: fava/templates/_entry_forms.html:12 fava/templates/_entry_forms.html:62
+#: fava/templates/_entry_forms.html:8
 msgid "Number"
 msgstr "Número"
 
-#: fava/templates/_entry_forms.html:14 fava/templates/_entry_forms.html:45
+#: fava/templates/_entry_forms.html:16 fava/templates/_entry_forms.html:47
 msgid "Add posting"
 msgstr "Añadir asiento"
 
 #: fava/templates/_globals.html:11 fava/templates/extract.html:7
 #: fava/templates/extract.html:34
 msgid "Import"
 msgstr ""
@@ -346,20 +345,20 @@
 msgid "...enter a BQL query. 'help' to list available commands."
 msgstr ""
 
 #: fava/templates/_journal_table.html:80
 msgid "Metadata"
 msgstr ""
 
-#: fava/templates/_entry_forms.html:23 fava/templates/_entry_forms.html:44
-#: fava/templates/_entry_forms.html:64 fava/templates/_entry_forms.html:76
+#: fava/templates/_entry_forms.html:25 fava/templates/_entry_forms.html:46
+#: fava/templates/_entry_forms.html:66 fava/templates/_entry_forms.html:78
 msgid "Add metadata"
 msgstr ""
 
-#: fava/templates/_entry_forms.html:74
+#: fava/templates/_entry_forms.html:76
 msgid "Note"
 msgstr ""
 
 #: fava/templates/_context.html:4
 msgid "Location"
 msgstr ""
 
@@ -387,18 +386,14 @@
 msgid "Other transactions"
 msgstr ""
 
 #: fava/templates/_journal_table.html:7
 msgid "Documents with a #discovered tag"
 msgstr ""
 
-#: fava/templates/_journal_table.html:8
-msgid "Documents with a #statement tag"
-msgstr ""
-
 #: fava/templates/_journal_table.html:81
 msgid "Postings"
 msgstr ""
 
 #: fava/templates/_overlays.html:7
 msgid "Upload file(s)"
 msgstr ""
@@ -460,31 +455,39 @@
 msgid "Download currently filtered entries as a Beancount file"
 msgstr ""
 
 #: fava/templates/extract.html:40
 msgid "Import entries"
 msgstr ""
 
-#: fava/util/date.py:44
+#: fava/util/date.py:50
 msgid "Yearly"
 msgstr ""
 
-#: fava/util/date.py:45
+#: fava/util/date.py:51
 msgid "Quarterly"
 msgstr ""
 
-#: fava/util/date.py:46
+#: fava/util/date.py:52
 msgid "Monthly"
 msgstr ""
 
-#: fava/util/date.py:47
+#: fava/util/date.py:53
 msgid "Weekly"
 msgstr ""
 
-#: fava/util/date.py:48
+#: fava/util/date.py:54
 msgid "Daily"
 msgstr ""
 
 #: fava/templates/editor.html:18
 msgid "Edit"
 msgstr ""
 
+#: fava/templates/_entry_forms.html:15
+msgid "Amount"
+msgstr ""
+
+#: fava/templates/_journal_table.html:8
+msgid "Documents with a #linked tag"
+msgstr ""
+
```

### Comparing `fava-1.8/fava/translations/fr/LC_MESSAGES/messages.mo` & `fava-1.9/fava/translations/fr/LC_MESSAGES/messages.mo`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/translations/fr/LC_MESSAGES/messages.po` & `fava-1.9/fava/translations/fr/LC_MESSAGES/messages.po`

 * *Files 2% similar despite different names*

```diff
@@ -22,15 +22,15 @@
 #: fava/templates/_entry_filters.html:3 fava/templates/_entry_forms.html:2
 #: fava/templates/_overlays.html:18 fava/templates/_tree_table.html:24
 #: fava/templates/_tree_table.html:105 fava/templates/holdings.html:48
 #: fava/templates/import.html:19 fava/templates/statistics.html:36
 msgid "Account"
 msgstr "Compte"
 
-#: fava/templates/_entry_forms.html:40 fava/templates/_entry_forms.html:41
+#: fava/templates/_entry_forms.html:42 fava/templates/_entry_forms.html:43
 msgid "Payee"
 msgstr "Bénéficiaire"
 
 #: fava/templates/_globals.html:2
 msgid "Income Statement"
 msgstr "Compte de résultat"
 
@@ -103,15 +103,15 @@
 msgid "Cost"
 msgstr "Coût"
 
 #: fava/templates/_journal_table.html:93
 msgid "Change"
 msgstr "Opération"
 
-#: fava/templates/_entry_forms.html:60 fava/templates/_journal_table.html:94
+#: fava/templates/_entry_forms.html:62 fava/templates/_journal_table.html:94
 #: fava/templates/statistics.html:40
 msgid "Balance"
 msgstr "Solde"
 
 #: fava/templates/_context.html:57 fava/templates/_overlays.html:33
 #: fava/templates/editor.html:41
 msgid "Save"
@@ -191,16 +191,15 @@
 msgid "Help - %(title)s"
 msgstr "Aide - %(title)s"
 
 #: fava/templates/help.html:9
 msgid "Help pages"
 msgstr "pages d'Aide"
 
-#: fava/templates/_entry_forms.html:13 fava/templates/_entry_forms.html:63
-#: fava/templates/holdings.html:48
+#: fava/templates/_entry_forms.html:65 fava/templates/holdings.html:48
 msgid "Currency"
 msgstr "Devise"
 
 #: fava/templates/holdings.html:48
 msgid "Cost currency"
 msgstr "Devise pour les coûts"
 
@@ -216,20 +215,20 @@
 msgid "Income"
 msgstr "Revenu"
 
 #: fava/templates/income_statement.html:10
 msgid "Expenses"
 msgstr "Dépenses"
 
-#: fava/templates/_entry_forms.html:21 fava/templates/options.html:9
+#: fava/templates/_entry_forms.html:23 fava/templates/options.html:9
 #: fava/templates/options.html:26
 msgid "Key"
 msgstr "Clé"
 
-#: fava/templates/_entry_forms.html:22 fava/templates/options.html:10
+#: fava/templates/_entry_forms.html:24 fava/templates/options.html:10
 #: fava/templates/options.html:27
 msgid "Value"
 msgstr "Valeur"
 
 #: fava/templates/_query_table.html:69
 msgid "Download as"
 msgstr "Télécharger en tant que"
@@ -275,27 +274,27 @@
 msgid "close"
 msgstr "Fermer"
 
 #: fava/templates/_overlays.html:30
 msgid "New transaction"
 msgstr "Nouvelle transaction"
 
-#: fava/templates/_entry_forms.html:42 fava/templates/_entry_forms.html:43
+#: fava/templates/_entry_forms.html:44 fava/templates/_entry_forms.html:45
 msgid "Narration"
 msgstr "Narration"
 
 #: fava/templates/_overlays.html:34
 msgid "Save and add new"
 msgstr "Enregistrer et ajouter 1 nouvelle"
 
-#: fava/templates/_entry_forms.html:12 fava/templates/_entry_forms.html:62
+#: fava/templates/_entry_forms.html:8
 msgid "Number"
 msgstr "Nombre"
 
-#: fava/templates/_entry_forms.html:14 fava/templates/_entry_forms.html:45
+#: fava/templates/_entry_forms.html:16 fava/templates/_entry_forms.html:47
 msgid "Add posting"
 msgstr "Ajouter Enregistrement"
 
 #: fava/templates/_globals.html:11 fava/templates/extract.html:7
 #: fava/templates/extract.html:34
 msgid "Import"
 msgstr ""
@@ -344,20 +343,20 @@
 msgid "...enter a BQL query. 'help' to list available commands."
 msgstr ""
 
 #: fava/templates/_journal_table.html:80
 msgid "Metadata"
 msgstr ""
 
-#: fava/templates/_entry_forms.html:23 fava/templates/_entry_forms.html:44
-#: fava/templates/_entry_forms.html:64 fava/templates/_entry_forms.html:76
+#: fava/templates/_entry_forms.html:25 fava/templates/_entry_forms.html:46
+#: fava/templates/_entry_forms.html:66 fava/templates/_entry_forms.html:78
 msgid "Add metadata"
 msgstr ""
 
-#: fava/templates/_entry_forms.html:74
+#: fava/templates/_entry_forms.html:76
 msgid "Note"
 msgstr ""
 
 #: fava/templates/_context.html:4
 msgid "Location"
 msgstr ""
 
@@ -385,18 +384,14 @@
 msgid "Other transactions"
 msgstr ""
 
 #: fava/templates/_journal_table.html:7
 msgid "Documents with a #discovered tag"
 msgstr ""
 
-#: fava/templates/_journal_table.html:8
-msgid "Documents with a #statement tag"
-msgstr ""
-
 #: fava/templates/_journal_table.html:81
 msgid "Postings"
 msgstr ""
 
 #: fava/templates/_overlays.html:7
 msgid "Upload file(s)"
 msgstr ""
@@ -458,31 +453,39 @@
 msgid "Download currently filtered entries as a Beancount file"
 msgstr ""
 
 #: fava/templates/extract.html:40
 msgid "Import entries"
 msgstr ""
 
-#: fava/util/date.py:44
+#: fava/util/date.py:50
 msgid "Yearly"
 msgstr ""
 
-#: fava/util/date.py:45
+#: fava/util/date.py:51
 msgid "Quarterly"
 msgstr ""
 
-#: fava/util/date.py:46
+#: fava/util/date.py:52
 msgid "Monthly"
 msgstr ""
 
-#: fava/util/date.py:47
+#: fava/util/date.py:53
 msgid "Weekly"
 msgstr ""
 
-#: fava/util/date.py:48
+#: fava/util/date.py:54
 msgid "Daily"
 msgstr ""
 
 #: fava/templates/editor.html:18
 msgid "Edit"
 msgstr ""
 
+#: fava/templates/_entry_forms.html:15
+msgid "Amount"
+msgstr ""
+
+#: fava/templates/_journal_table.html:8
+msgid "Documents with a #linked tag"
+msgstr ""
+
```

### Comparing `fava-1.8/fava/translations/nl/LC_MESSAGES/messages.mo` & `fava-1.9/fava/translations/nl/LC_MESSAGES/messages.mo`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/translations/nl/LC_MESSAGES/messages.po` & `fava-1.9/fava/translations/nl/LC_MESSAGES/messages.po`

 * *Files 0% similar despite different names*

```diff
@@ -22,15 +22,15 @@
 #: fava/templates/_entry_filters.html:3 fava/templates/_entry_forms.html:2
 #: fava/templates/_overlays.html:18 fava/templates/_tree_table.html:24
 #: fava/templates/_tree_table.html:105 fava/templates/holdings.html:48
 #: fava/templates/import.html:19 fava/templates/statistics.html:36
 msgid "Account"
 msgstr "Rekening"
 
-#: fava/templates/_entry_forms.html:40 fava/templates/_entry_forms.html:41
+#: fava/templates/_entry_forms.html:42 fava/templates/_entry_forms.html:43
 msgid "Payee"
 msgstr "Begunstigde"
 
 #: fava/templates/_globals.html:2
 msgid "Income Statement"
 msgstr "Winst- en Verliesrekening"
 
@@ -104,15 +104,15 @@
 msgid "Cost"
 msgstr "Kosten"
 
 #: fava/templates/_journal_table.html:93
 msgid "Change"
 msgstr "Verschil"
 
-#: fava/templates/_entry_forms.html:60 fava/templates/_journal_table.html:94
+#: fava/templates/_entry_forms.html:62 fava/templates/_journal_table.html:94
 #: fava/templates/statistics.html:40
 msgid "Balance"
 msgstr "Balans"
 
 #: fava/templates/_context.html:57 fava/templates/_overlays.html:33
 #: fava/templates/editor.html:41
 msgid "Save"
@@ -192,16 +192,15 @@
 msgid "Help - %(title)s"
 msgstr "Hulp - %(title)s"
 
 #: fava/templates/help.html:9
 msgid "Help pages"
 msgstr "Hulp pagina's"
 
-#: fava/templates/_entry_forms.html:13 fava/templates/_entry_forms.html:63
-#: fava/templates/holdings.html:48
+#: fava/templates/_entry_forms.html:65 fava/templates/holdings.html:48
 msgid "Currency"
 msgstr "Valuta"
 
 #: fava/templates/holdings.html:48
 msgid "Cost currency"
 msgstr "Kosten Valuta"
 
@@ -217,20 +216,20 @@
 msgid "Income"
 msgstr "Inkomsten"
 
 #: fava/templates/income_statement.html:10
 msgid "Expenses"
 msgstr "Uitgaven"
 
-#: fava/templates/_entry_forms.html:21 fava/templates/options.html:9
+#: fava/templates/_entry_forms.html:23 fava/templates/options.html:9
 #: fava/templates/options.html:26
 msgid "Key"
 msgstr "Sleutel"
 
-#: fava/templates/_entry_forms.html:22 fava/templates/options.html:10
+#: fava/templates/_entry_forms.html:24 fava/templates/options.html:10
 #: fava/templates/options.html:27
 msgid "Value"
 msgstr "Waarde"
 
 #: fava/templates/_query_table.html:69
 msgid "Download as"
 msgstr "Downloaded als"
@@ -276,27 +275,27 @@
 msgid "close"
 msgstr "sluiten"
 
 #: fava/templates/_overlays.html:30
 msgid "New transaction"
 msgstr "Nieuwe transactie"
 
-#: fava/templates/_entry_forms.html:42 fava/templates/_entry_forms.html:43
+#: fava/templates/_entry_forms.html:44 fava/templates/_entry_forms.html:45
 msgid "Narration"
 msgstr "Omschrijving"
 
 #: fava/templates/_overlays.html:34
 msgid "Save and add new"
 msgstr "Opslaan en nieuw"
 
-#: fava/templates/_entry_forms.html:12 fava/templates/_entry_forms.html:62
+#: fava/templates/_entry_forms.html:8
 msgid "Number"
 msgstr "Nummer"
 
-#: fava/templates/_entry_forms.html:14 fava/templates/_entry_forms.html:45
+#: fava/templates/_entry_forms.html:16 fava/templates/_entry_forms.html:47
 msgid "Add posting"
 msgstr "Boeking toevoegen"
 
 #: fava/templates/_globals.html:11 fava/templates/extract.html:7
 #: fava/templates/extract.html:34
 msgid "Import"
 msgstr ""
@@ -345,20 +344,20 @@
 msgid "...enter a BQL query. 'help' to list available commands."
 msgstr ""
 
 #: fava/templates/_journal_table.html:80
 msgid "Metadata"
 msgstr ""
 
-#: fava/templates/_entry_forms.html:23 fava/templates/_entry_forms.html:44
-#: fava/templates/_entry_forms.html:64 fava/templates/_entry_forms.html:76
+#: fava/templates/_entry_forms.html:25 fava/templates/_entry_forms.html:46
+#: fava/templates/_entry_forms.html:66 fava/templates/_entry_forms.html:78
 msgid "Add metadata"
 msgstr ""
 
-#: fava/templates/_entry_forms.html:74
+#: fava/templates/_entry_forms.html:76
 msgid "Note"
 msgstr ""
 
 #: fava/templates/_context.html:4
 msgid "Location"
 msgstr ""
 
@@ -386,18 +385,14 @@
 msgid "Other transactions"
 msgstr ""
 
 #: fava/templates/_journal_table.html:7
 msgid "Documents with a #discovered tag"
 msgstr ""
 
-#: fava/templates/_journal_table.html:8
-msgid "Documents with a #statement tag"
-msgstr ""
-
 #: fava/templates/_journal_table.html:81
 msgid "Postings"
 msgstr ""
 
 #: fava/templates/_overlays.html:7
 msgid "Upload file(s)"
 msgstr ""
@@ -459,31 +454,39 @@
 msgid "Download currently filtered entries as a Beancount file"
 msgstr ""
 
 #: fava/templates/extract.html:40
 msgid "Import entries"
 msgstr ""
 
-#: fava/util/date.py:44
+#: fava/util/date.py:50
 msgid "Yearly"
 msgstr ""
 
-#: fava/util/date.py:45
+#: fava/util/date.py:51
 msgid "Quarterly"
 msgstr ""
 
-#: fava/util/date.py:46
+#: fava/util/date.py:52
 msgid "Monthly"
 msgstr ""
 
-#: fava/util/date.py:47
+#: fava/util/date.py:53
 msgid "Weekly"
 msgstr ""
 
-#: fava/util/date.py:48
+#: fava/util/date.py:54
 msgid "Daily"
 msgstr ""
 
 #: fava/templates/editor.html:18
 msgid "Edit"
 msgstr ""
 
+#: fava/templates/_entry_forms.html:15
+msgid "Amount"
+msgstr ""
+
+#: fava/templates/_journal_table.html:8
+msgid "Documents with a #linked tag"
+msgstr ""
+
```

### Comparing `fava-1.8/fava/translations/pt/LC_MESSAGES/messages.mo` & `fava-1.9/fava/translations/pt/LC_MESSAGES/messages.mo`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/translations/pt/LC_MESSAGES/messages.po` & `fava-1.9/fava/translations/pt/LC_MESSAGES/messages.po`

 * *Files 2% similar despite different names*

```diff
@@ -22,15 +22,15 @@
 #: fava/templates/_entry_filters.html:3 fava/templates/_entry_forms.html:2
 #: fava/templates/_overlays.html:18 fava/templates/_tree_table.html:24
 #: fava/templates/_tree_table.html:105 fava/templates/holdings.html:48
 #: fava/templates/import.html:19 fava/templates/statistics.html:36
 msgid "Account"
 msgstr "Conta"
 
-#: fava/templates/_entry_forms.html:40 fava/templates/_entry_forms.html:41
+#: fava/templates/_entry_forms.html:42 fava/templates/_entry_forms.html:43
 msgid "Payee"
 msgstr "Beneficiário"
 
 #: fava/templates/_globals.html:2
 msgid "Income Statement"
 msgstr "Declaração de Rendimentos"
 
@@ -104,15 +104,15 @@
 msgid "Cost"
 msgstr "Custo"
 
 #: fava/templates/_journal_table.html:93
 msgid "Change"
 msgstr "Alterar"
 
-#: fava/templates/_entry_forms.html:60 fava/templates/_journal_table.html:94
+#: fava/templates/_entry_forms.html:62 fava/templates/_journal_table.html:94
 #: fava/templates/statistics.html:40
 msgid "Balance"
 msgstr "Saldo"
 
 #: fava/templates/_context.html:57 fava/templates/_overlays.html:33
 #: fava/templates/editor.html:41
 msgid "Save"
@@ -195,16 +195,15 @@
 msgid "Help - %(title)s"
 msgstr "Ajuda - %(title)s"
 
 #: fava/templates/help.html:9
 msgid "Help pages"
 msgstr "Páginas de ajuda"
 
-#: fava/templates/_entry_forms.html:13 fava/templates/_entry_forms.html:63
-#: fava/templates/holdings.html:48
+#: fava/templates/_entry_forms.html:65 fava/templates/holdings.html:48
 msgid "Currency"
 msgstr "Moeda"
 
 #: fava/templates/holdings.html:48
 msgid "Cost currency"
 msgstr "Moeda de custo"
 
@@ -220,20 +219,20 @@
 msgid "Income"
 msgstr "Rendimento"
 
 #: fava/templates/income_statement.html:10
 msgid "Expenses"
 msgstr "Despesas"
 
-#: fava/templates/_entry_forms.html:21 fava/templates/options.html:9
+#: fava/templates/_entry_forms.html:23 fava/templates/options.html:9
 #: fava/templates/options.html:26
 msgid "Key"
 msgstr "Chave"
 
-#: fava/templates/_entry_forms.html:22 fava/templates/options.html:10
+#: fava/templates/_entry_forms.html:24 fava/templates/options.html:10
 #: fava/templates/options.html:27
 msgid "Value"
 msgstr "Valor"
 
 #: fava/templates/_query_table.html:69
 msgid "Download as"
 msgstr "Guardar como"
@@ -279,27 +278,27 @@
 msgid "close"
 msgstr "fechar"
 
 #: fava/templates/_overlays.html:30
 msgid "New transaction"
 msgstr "Nova transação"
 
-#: fava/templates/_entry_forms.html:42 fava/templates/_entry_forms.html:43
+#: fava/templates/_entry_forms.html:44 fava/templates/_entry_forms.html:45
 msgid "Narration"
 msgstr "Descrição"
 
 #: fava/templates/_overlays.html:34
 msgid "Save and add new"
 msgstr "Salvar e adicionar novo"
 
-#: fava/templates/_entry_forms.html:12 fava/templates/_entry_forms.html:62
+#: fava/templates/_entry_forms.html:8
 msgid "Number"
 msgstr "Número"
 
-#: fava/templates/_entry_forms.html:14 fava/templates/_entry_forms.html:45
+#: fava/templates/_entry_forms.html:16 fava/templates/_entry_forms.html:47
 msgid "Add posting"
 msgstr "Inserir movimento"
 
 #: fava/templates/_globals.html:11 fava/templates/extract.html:7
 #: fava/templates/extract.html:34
 msgid "Import"
 msgstr ""
@@ -348,20 +347,20 @@
 msgid "...enter a BQL query. 'help' to list available commands."
 msgstr ""
 
 #: fava/templates/_journal_table.html:80
 msgid "Metadata"
 msgstr ""
 
-#: fava/templates/_entry_forms.html:23 fava/templates/_entry_forms.html:44
-#: fava/templates/_entry_forms.html:64 fava/templates/_entry_forms.html:76
+#: fava/templates/_entry_forms.html:25 fava/templates/_entry_forms.html:46
+#: fava/templates/_entry_forms.html:66 fava/templates/_entry_forms.html:78
 msgid "Add metadata"
 msgstr ""
 
-#: fava/templates/_entry_forms.html:74
+#: fava/templates/_entry_forms.html:76
 msgid "Note"
 msgstr ""
 
 #: fava/templates/_context.html:4
 msgid "Location"
 msgstr ""
 
@@ -389,18 +388,14 @@
 msgid "Other transactions"
 msgstr ""
 
 #: fava/templates/_journal_table.html:7
 msgid "Documents with a #discovered tag"
 msgstr ""
 
-#: fava/templates/_journal_table.html:8
-msgid "Documents with a #statement tag"
-msgstr ""
-
 #: fava/templates/_journal_table.html:81
 msgid "Postings"
 msgstr ""
 
 #: fava/templates/_overlays.html:7
 msgid "Upload file(s)"
 msgstr ""
@@ -462,31 +457,39 @@
 msgid "Download currently filtered entries as a Beancount file"
 msgstr ""
 
 #: fava/templates/extract.html:40
 msgid "Import entries"
 msgstr ""
 
-#: fava/util/date.py:44
+#: fava/util/date.py:50
 msgid "Yearly"
 msgstr ""
 
-#: fava/util/date.py:45
+#: fava/util/date.py:51
 msgid "Quarterly"
 msgstr ""
 
-#: fava/util/date.py:46
+#: fava/util/date.py:52
 msgid "Monthly"
 msgstr ""
 
-#: fava/util/date.py:47
+#: fava/util/date.py:53
 msgid "Weekly"
 msgstr ""
 
-#: fava/util/date.py:48
+#: fava/util/date.py:54
 msgid "Daily"
 msgstr ""
 
 #: fava/templates/editor.html:18
 msgid "Edit"
 msgstr ""
 
+#: fava/templates/_entry_forms.html:15
+msgid "Amount"
+msgstr ""
+
+#: fava/templates/_journal_table.html:8
+msgid "Documents with a #linked tag"
+msgstr ""
+
```

### Comparing `fava-1.8/fava/translations/ru/LC_MESSAGES/messages.mo` & `fava-1.9/fava/translations/ru/LC_MESSAGES/messages.mo`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/translations/ru/LC_MESSAGES/messages.po` & `fava-1.9/fava/translations/ru/LC_MESSAGES/messages.po`

 * *Files 1% similar despite different names*

```diff
@@ -22,15 +22,15 @@
 #: fava/templates/_entry_filters.html:3 fava/templates/_entry_forms.html:2
 #: fava/templates/_overlays.html:18 fava/templates/_tree_table.html:24
 #: fava/templates/_tree_table.html:105 fava/templates/holdings.html:48
 #: fava/templates/import.html:19 fava/templates/statistics.html:36
 msgid "Account"
 msgstr "Счёт"
 
-#: fava/templates/_entry_forms.html:40 fava/templates/_entry_forms.html:41
+#: fava/templates/_entry_forms.html:42 fava/templates/_entry_forms.html:43
 msgid "Payee"
 msgstr "Контрагент"
 
 #: fava/templates/_globals.html:2
 msgid "Income Statement"
 msgstr "Справка о доходах"
 
@@ -103,15 +103,15 @@
 msgid "Cost"
 msgstr "Стоимость"
 
 #: fava/templates/_journal_table.html:93
 msgid "Change"
 msgstr "Изменение"
 
-#: fava/templates/_entry_forms.html:60 fava/templates/_journal_table.html:94
+#: fava/templates/_entry_forms.html:62 fava/templates/_journal_table.html:94
 #: fava/templates/statistics.html:40
 msgid "Balance"
 msgstr "Баланс"
 
 #: fava/templates/_context.html:57 fava/templates/_overlays.html:33
 #: fava/templates/editor.html:41
 msgid "Save"
@@ -191,16 +191,15 @@
 msgid "Help - %(title)s"
 msgstr "Помощь - %(title)s"
 
 #: fava/templates/help.html:9
 msgid "Help pages"
 msgstr "Страницы помощи"
 
-#: fava/templates/_entry_forms.html:13 fava/templates/_entry_forms.html:63
-#: fava/templates/holdings.html:48
+#: fava/templates/_entry_forms.html:65 fava/templates/holdings.html:48
 msgid "Currency"
 msgstr "Валюта"
 
 #: fava/templates/holdings.html:48
 msgid "Cost currency"
 msgstr "Валюта (стоим.)"
 
@@ -216,20 +215,20 @@
 msgid "Income"
 msgstr "Доход"
 
 #: fava/templates/income_statement.html:10
 msgid "Expenses"
 msgstr "Расходы"
 
-#: fava/templates/_entry_forms.html:21 fava/templates/options.html:9
+#: fava/templates/_entry_forms.html:23 fava/templates/options.html:9
 #: fava/templates/options.html:26
 msgid "Key"
 msgstr "Ключ"
 
-#: fava/templates/_entry_forms.html:22 fava/templates/options.html:10
+#: fava/templates/_entry_forms.html:24 fava/templates/options.html:10
 #: fava/templates/options.html:27
 msgid "Value"
 msgstr "Значение"
 
 #: fava/templates/_query_table.html:69
 msgid "Download as"
 msgstr "Скачать как"
@@ -275,27 +274,27 @@
 msgid "close"
 msgstr "закрыть"
 
 #: fava/templates/_overlays.html:30
 msgid "New transaction"
 msgstr "Новая транзакция"
 
-#: fava/templates/_entry_forms.html:42 fava/templates/_entry_forms.html:43
+#: fava/templates/_entry_forms.html:44 fava/templates/_entry_forms.html:45
 msgid "Narration"
 msgstr "Описание"
 
 #: fava/templates/_overlays.html:34
 msgid "Save and add new"
 msgstr "Записать и добавить новую"
 
-#: fava/templates/_entry_forms.html:12 fava/templates/_entry_forms.html:62
+#: fava/templates/_entry_forms.html:8
 msgid "Number"
 msgstr "Количество"
 
-#: fava/templates/_entry_forms.html:14 fava/templates/_entry_forms.html:45
+#: fava/templates/_entry_forms.html:16 fava/templates/_entry_forms.html:47
 msgid "Add posting"
 msgstr "Добавить проводку"
 
 #: fava/templates/_globals.html:11 fava/templates/extract.html:7
 #: fava/templates/extract.html:34
 msgid "Import"
 msgstr ""
@@ -344,20 +343,20 @@
 msgid "...enter a BQL query. 'help' to list available commands."
 msgstr ""
 
 #: fava/templates/_journal_table.html:80
 msgid "Metadata"
 msgstr ""
 
-#: fava/templates/_entry_forms.html:23 fava/templates/_entry_forms.html:44
-#: fava/templates/_entry_forms.html:64 fava/templates/_entry_forms.html:76
+#: fava/templates/_entry_forms.html:25 fava/templates/_entry_forms.html:46
+#: fava/templates/_entry_forms.html:66 fava/templates/_entry_forms.html:78
 msgid "Add metadata"
 msgstr ""
 
-#: fava/templates/_entry_forms.html:74
+#: fava/templates/_entry_forms.html:76
 msgid "Note"
 msgstr ""
 
 #: fava/templates/_context.html:4
 msgid "Location"
 msgstr ""
 
@@ -385,18 +384,14 @@
 msgid "Other transactions"
 msgstr ""
 
 #: fava/templates/_journal_table.html:7
 msgid "Documents with a #discovered tag"
 msgstr ""
 
-#: fava/templates/_journal_table.html:8
-msgid "Documents with a #statement tag"
-msgstr ""
-
 #: fava/templates/_journal_table.html:81
 msgid "Postings"
 msgstr ""
 
 #: fava/templates/_overlays.html:7
 msgid "Upload file(s)"
 msgstr ""
@@ -458,31 +453,39 @@
 msgid "Download currently filtered entries as a Beancount file"
 msgstr ""
 
 #: fava/templates/extract.html:40
 msgid "Import entries"
 msgstr ""
 
-#: fava/util/date.py:44
+#: fava/util/date.py:50
 msgid "Yearly"
 msgstr ""
 
-#: fava/util/date.py:45
+#: fava/util/date.py:51
 msgid "Quarterly"
 msgstr ""
 
-#: fava/util/date.py:46
+#: fava/util/date.py:52
 msgid "Monthly"
 msgstr ""
 
-#: fava/util/date.py:47
+#: fava/util/date.py:53
 msgid "Weekly"
 msgstr ""
 
-#: fava/util/date.py:48
+#: fava/util/date.py:54
 msgid "Daily"
 msgstr ""
 
 #: fava/templates/editor.html:18
 msgid "Edit"
 msgstr ""
 
+#: fava/templates/_entry_forms.html:15
+msgid "Amount"
+msgstr ""
+
+#: fava/templates/_journal_table.html:8
+msgid "Documents with a #linked tag"
+msgstr ""
+
```

### Comparing `fava-1.8/fava/translations/sk/LC_MESSAGES/messages.mo` & `fava-1.9/fava/translations/sk/LC_MESSAGES/messages.mo`

 * *Files 18% similar despite different names*

#### msgunfmt {}

```diff
@@ -100,17 +100,14 @@
 
 msgid "Documents folder"
 msgstr "Priečinok s dokumentmi"
 
 msgid "Documents with a #discovered tag"
 msgstr "Dokumenty označené #discovered (objavené)"
 
-msgid "Documents with a #statement tag"
-msgstr "Dokumenty označené #statement (výpis)"
-
 msgid "Download as"
 msgstr "Stiahnuť ako"
 
 msgid "Download currently filtered entries as a Beancount file"
 msgstr "Stiahnuť aktuálne filtrované zápisy ako Beancount súbor"
 
 msgid "Duplicate"
```

### Comparing `fava-1.8/fava/translations/sk/LC_MESSAGES/messages.po` & `fava-1.9/fava/translations/sk/LC_MESSAGES/messages.po`

 * *Files 1% similar despite different names*

```diff
@@ -22,15 +22,15 @@
 #: fava/templates/_entry_filters.html:3 fava/templates/_entry_forms.html:2
 #: fava/templates/_overlays.html:18 fava/templates/_tree_table.html:24
 #: fava/templates/_tree_table.html:105 fava/templates/holdings.html:48
 #: fava/templates/import.html:19 fava/templates/statistics.html:36
 msgid "Account"
 msgstr "Účet"
 
-#: fava/templates/_entry_forms.html:40 fava/templates/_entry_forms.html:41
+#: fava/templates/_entry_forms.html:42 fava/templates/_entry_forms.html:43
 msgid "Payee"
 msgstr "Príjemca"
 
 #: fava/templates/_globals.html:2
 msgid "Income Statement"
 msgstr "Výkaz ziskov a strát"
 
@@ -106,15 +106,15 @@
 msgid "Cost"
 msgstr "Výdavok"
 
 #: fava/templates/_journal_table.html:93
 msgid "Change"
 msgstr "Zmena"
 
-#: fava/templates/_entry_forms.html:60 fava/templates/_journal_table.html:94
+#: fava/templates/_entry_forms.html:62 fava/templates/_journal_table.html:94
 #: fava/templates/statistics.html:40
 msgid "Balance"
 msgstr "Zostatok"
 
 #: fava/templates/_context.html:57 fava/templates/_overlays.html:33
 #: fava/templates/editor.html:41
 msgid "Save"
@@ -196,16 +196,15 @@
 msgstr "Pomoc - %(title)"
 
 #: fava/templates/help.html:9
 #, fuzzy
 msgid "Help pages"
 msgstr "Pomocné stránky"
 
-#: fava/templates/_entry_forms.html:13 fava/templates/_entry_forms.html:63
-#: fava/templates/holdings.html:48
+#: fava/templates/_entry_forms.html:65 fava/templates/holdings.html:48
 msgid "Currency"
 msgstr "Mena"
 
 #: fava/templates/holdings.html:48
 msgid "Cost currency"
 msgstr "Mena výdavku"
 
@@ -221,20 +220,20 @@
 msgid "Income"
 msgstr "Príjem"
 
 #: fava/templates/income_statement.html:10
 msgid "Expenses"
 msgstr "Výdavky"
 
-#: fava/templates/_entry_forms.html:21 fava/templates/options.html:9
+#: fava/templates/_entry_forms.html:23 fava/templates/options.html:9
 #: fava/templates/options.html:26
 msgid "Key"
 msgstr "Kľúč"
 
-#: fava/templates/_entry_forms.html:22 fava/templates/options.html:10
+#: fava/templates/_entry_forms.html:24 fava/templates/options.html:10
 #: fava/templates/options.html:27
 msgid "Value"
 msgstr "Hodnota"
 
 #: fava/templates/_query_table.html:69
 msgid "Download as"
 msgstr "Stiahnuť ako"
@@ -280,27 +279,27 @@
 msgid "close"
 msgstr "zavrieť"
 
 #: fava/templates/_overlays.html:30
 msgid "New transaction"
 msgstr "Nová transakcia"
 
-#: fava/templates/_entry_forms.html:42 fava/templates/_entry_forms.html:43
+#: fava/templates/_entry_forms.html:44 fava/templates/_entry_forms.html:45
 msgid "Narration"
 msgstr "Popis"
 
 #: fava/templates/_overlays.html:34
 msgid "Save and add new"
 msgstr "Uložit a pridať novú transakciu"
 
-#: fava/templates/_entry_forms.html:12 fava/templates/_entry_forms.html:62
+#: fava/templates/_entry_forms.html:8
 msgid "Number"
 msgstr "Číslo"
 
-#: fava/templates/_entry_forms.html:14 fava/templates/_entry_forms.html:45
+#: fava/templates/_entry_forms.html:16 fava/templates/_entry_forms.html:47
 msgid "Add posting"
 msgstr "Pridať položku"
 
 #: fava/templates/_globals.html:11 fava/templates/extract.html:7
 #: fava/templates/extract.html:34
 msgid "Import"
 msgstr "Importovať"
@@ -349,20 +348,20 @@
 msgid "...enter a BQL query. 'help' to list available commands."
 msgstr "...zadajte BQL dotaz. 'help' zobrazí všetky dostupné príkazy."
 
 #: fava/templates/_journal_table.html:80
 msgid "Metadata"
 msgstr "Metadáta"
 
-#: fava/templates/_entry_forms.html:23 fava/templates/_entry_forms.html:44
-#: fava/templates/_entry_forms.html:64 fava/templates/_entry_forms.html:76
+#: fava/templates/_entry_forms.html:25 fava/templates/_entry_forms.html:46
+#: fava/templates/_entry_forms.html:66 fava/templates/_entry_forms.html:78
 msgid "Add metadata"
 msgstr "Pridať metadáta"
 
-#: fava/templates/_entry_forms.html:74
+#: fava/templates/_entry_forms.html:76
 msgid "Note"
 msgstr "Poznámka"
 
 #: fava/templates/_context.html:4
 msgid "Location"
 msgstr "Poloha"
 
@@ -390,18 +389,14 @@
 msgid "Other transactions"
 msgstr "Ostatné transakcie"
 
 #: fava/templates/_journal_table.html:7
 msgid "Documents with a #discovered tag"
 msgstr "Dokumenty označené #discovered (objavené)"
 
-#: fava/templates/_journal_table.html:8
-msgid "Documents with a #statement tag"
-msgstr "Dokumenty označené #statement (výpis)"
-
 #: fava/templates/_journal_table.html:81
 msgid "Postings"
 msgstr "Položky"
 
 #: fava/templates/_overlays.html:7
 msgid "Upload file(s)"
 msgstr "Nahrať súbor-y"
@@ -463,31 +458,39 @@
 msgid "Download currently filtered entries as a Beancount file"
 msgstr "Stiahnuť aktuálne filtrované zápisy ako Beancount súbor"
 
 #: fava/templates/extract.html:40
 msgid "Import entries"
 msgstr "Importovať zápisy"
 
-#: fava/util/date.py:44
+#: fava/util/date.py:50
 msgid "Yearly"
 msgstr ""
 
-#: fava/util/date.py:45
+#: fava/util/date.py:51
 msgid "Quarterly"
 msgstr ""
 
-#: fava/util/date.py:46
+#: fava/util/date.py:52
 msgid "Monthly"
 msgstr ""
 
-#: fava/util/date.py:47
+#: fava/util/date.py:53
 msgid "Weekly"
 msgstr ""
 
-#: fava/util/date.py:48
+#: fava/util/date.py:54
 msgid "Daily"
 msgstr ""
 
 #: fava/templates/editor.html:18
 msgid "Edit"
 msgstr ""
 
+#: fava/templates/_entry_forms.html:15
+msgid "Amount"
+msgstr ""
+
+#: fava/templates/_journal_table.html:8
+msgid "Documents with a #linked tag"
+msgstr ""
+
```

### Comparing `fava-1.8/fava/translations/uk/LC_MESSAGES/messages.mo` & `fava-1.9/fava/translations/uk/LC_MESSAGES/messages.mo`

 * *Files 4% similar despite different names*

#### msgunfmt {}

```diff
@@ -100,17 +100,14 @@
 
 msgid "Documents folder"
 msgstr "Директорія документів"
 
 msgid "Documents with a #discovered tag"
 msgstr "Документи з #discovered тегом"
 
-msgid "Documents with a #statement tag"
-msgstr "Документи з #statement тегом"
-
 msgid "Download as"
 msgstr "Скачати як"
 
 msgid "Download currently filtered entries as a Beancount file"
 msgstr "Завантажити поточно відфільтровані записи як файл Beancount"
 
 msgid "Duplicate"
```

### Comparing `fava-1.8/fava/translations/uk/LC_MESSAGES/messages.po` & `fava-1.9/fava/translations/uk/LC_MESSAGES/messages.po`

 * *Files 2% similar despite different names*

```diff
@@ -22,15 +22,15 @@
 #: fava/templates/_entry_filters.html:3 fava/templates/_entry_forms.html:2
 #: fava/templates/_overlays.html:18 fava/templates/_tree_table.html:24
 #: fava/templates/_tree_table.html:105 fava/templates/holdings.html:48
 #: fava/templates/import.html:19 fava/templates/statistics.html:36
 msgid "Account"
 msgstr "Рахунок"
 
-#: fava/templates/_entry_forms.html:40 fava/templates/_entry_forms.html:41
+#: fava/templates/_entry_forms.html:42 fava/templates/_entry_forms.html:43
 msgid "Payee"
 msgstr "Отримувач"
 
 #: fava/templates/_globals.html:2
 msgid "Income Statement"
 msgstr "Доходний звіт"
 
@@ -103,15 +103,15 @@
 msgid "Cost"
 msgstr "Вартість"
 
 #: fava/templates/_journal_table.html:93
 msgid "Change"
 msgstr "Зміна"
 
-#: fava/templates/_entry_forms.html:60 fava/templates/_journal_table.html:94
+#: fava/templates/_entry_forms.html:62 fava/templates/_journal_table.html:94
 #: fava/templates/statistics.html:40
 msgid "Balance"
 msgstr "Баланс"
 
 #: fava/templates/_context.html:57 fava/templates/_overlays.html:33
 #: fava/templates/editor.html:41
 msgid "Save"
@@ -191,16 +191,15 @@
 msgid "Help - %(title)s"
 msgstr "Допомога - %(title)s"
 
 #: fava/templates/help.html:9
 msgid "Help pages"
 msgstr "Сторінки допомоги"
 
-#: fava/templates/_entry_forms.html:13 fava/templates/_entry_forms.html:63
-#: fava/templates/holdings.html:48
+#: fava/templates/_entry_forms.html:65 fava/templates/holdings.html:48
 msgid "Currency"
 msgstr "Валюта"
 
 #: fava/templates/holdings.html:48
 msgid "Cost currency"
 msgstr "Курс валюти"
 
@@ -216,20 +215,20 @@
 msgid "Income"
 msgstr "Дохід"
 
 #: fava/templates/income_statement.html:10
 msgid "Expenses"
 msgstr "Витрати"
 
-#: fava/templates/_entry_forms.html:21 fava/templates/options.html:9
+#: fava/templates/_entry_forms.html:23 fava/templates/options.html:9
 #: fava/templates/options.html:26
 msgid "Key"
 msgstr "Ключ"
 
-#: fava/templates/_entry_forms.html:22 fava/templates/options.html:10
+#: fava/templates/_entry_forms.html:24 fava/templates/options.html:10
 #: fava/templates/options.html:27
 msgid "Value"
 msgstr "Значення"
 
 #: fava/templates/_query_table.html:69
 msgid "Download as"
 msgstr "Скачати як"
@@ -275,27 +274,27 @@
 msgid "close"
 msgstr "закрити"
 
 #: fava/templates/_overlays.html:30
 msgid "New transaction"
 msgstr "Нова транзакція"
 
-#: fava/templates/_entry_forms.html:42 fava/templates/_entry_forms.html:43
+#: fava/templates/_entry_forms.html:44 fava/templates/_entry_forms.html:45
 msgid "Narration"
 msgstr "Опис"
 
 #: fava/templates/_overlays.html:34
 msgid "Save and add new"
 msgstr "Записати й додати нову"
 
-#: fava/templates/_entry_forms.html:12 fava/templates/_entry_forms.html:62
+#: fava/templates/_entry_forms.html:8
 msgid "Number"
 msgstr "Кількість"
 
-#: fava/templates/_entry_forms.html:14 fava/templates/_entry_forms.html:45
+#: fava/templates/_entry_forms.html:16 fava/templates/_entry_forms.html:47
 msgid "Add posting"
 msgstr "Додати проведення"
 
 #: fava/templates/_globals.html:11 fava/templates/extract.html:7
 #: fava/templates/extract.html:34
 msgid "Import"
 msgstr "Імпортувати"
@@ -344,20 +343,20 @@
 msgid "...enter a BQL query. 'help' to list available commands."
 msgstr "...введіть BQL запрос. 'help' щоб отримати список доступних команд."
 
 #: fava/templates/_journal_table.html:80
 msgid "Metadata"
 msgstr "Метадані"
 
-#: fava/templates/_entry_forms.html:23 fava/templates/_entry_forms.html:44
-#: fava/templates/_entry_forms.html:64 fava/templates/_entry_forms.html:76
+#: fava/templates/_entry_forms.html:25 fava/templates/_entry_forms.html:46
+#: fava/templates/_entry_forms.html:66 fava/templates/_entry_forms.html:78
 msgid "Add metadata"
 msgstr "Додати метадані"
 
-#: fava/templates/_entry_forms.html:74
+#: fava/templates/_entry_forms.html:76
 msgid "Note"
 msgstr "Примітка"
 
 #: fava/templates/_context.html:4
 msgid "Location"
 msgstr "Розташування"
 
@@ -385,18 +384,14 @@
 msgid "Other transactions"
 msgstr "Інші транзакції"
 
 #: fava/templates/_journal_table.html:7
 msgid "Documents with a #discovered tag"
 msgstr "Документи з #discovered тегом"
 
-#: fava/templates/_journal_table.html:8
-msgid "Documents with a #statement tag"
-msgstr "Документи з #statement тегом"
-
 #: fava/templates/_journal_table.html:81
 msgid "Postings"
 msgstr "Записи"
 
 #: fava/templates/_overlays.html:7
 msgid "Upload file(s)"
 msgstr "Завантажити файл(и)"
@@ -459,31 +454,39 @@
 msgid "Download currently filtered entries as a Beancount file"
 msgstr "Завантажити поточно відфільтровані записи як файл Beancount"
 
 #: fava/templates/extract.html:40
 msgid "Import entries"
 msgstr "Імпортувати записи"
 
-#: fava/util/date.py:44
+#: fava/util/date.py:50
 msgid "Yearly"
 msgstr ""
 
-#: fava/util/date.py:45
+#: fava/util/date.py:51
 msgid "Quarterly"
 msgstr ""
 
-#: fava/util/date.py:46
+#: fava/util/date.py:52
 msgid "Monthly"
 msgstr ""
 
-#: fava/util/date.py:47
+#: fava/util/date.py:53
 msgid "Weekly"
 msgstr ""
 
-#: fava/util/date.py:48
+#: fava/util/date.py:54
 msgid "Daily"
 msgstr ""
 
 #: fava/templates/editor.html:18
 msgid "Edit"
 msgstr ""
 
+#: fava/templates/_entry_forms.html:15
+msgid "Amount"
+msgstr ""
+
+#: fava/templates/_journal_table.html:8
+msgid "Documents with a #linked tag"
+msgstr ""
+
```

### Comparing `fava-1.8/fava/translations/zh/LC_MESSAGES/messages.mo` & `fava-1.9/fava/translations/zh/LC_MESSAGES/messages.mo`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/translations/zh/LC_MESSAGES/messages.po` & `fava-1.9/fava/translations/zh/LC_MESSAGES/messages.po`

 * *Files 1% similar despite different names*

```diff
@@ -22,15 +22,15 @@
 #: fava/templates/_entry_filters.html:3 fava/templates/_entry_forms.html:2
 #: fava/templates/_overlays.html:18 fava/templates/_tree_table.html:24
 #: fava/templates/_tree_table.html:105 fava/templates/holdings.html:48
 #: fava/templates/import.html:19 fava/templates/statistics.html:36
 msgid "Account"
 msgstr "帐户"
 
-#: fava/templates/_entry_forms.html:40 fava/templates/_entry_forms.html:41
+#: fava/templates/_entry_forms.html:42 fava/templates/_entry_forms.html:43
 msgid "Payee"
 msgstr "收款人"
 
 #: fava/templates/_globals.html:2
 msgid "Income Statement"
 msgstr "损益表"
 
@@ -103,15 +103,15 @@
 msgid "Cost"
 msgstr "成本"
 
 #: fava/templates/_journal_table.html:93
 msgid "Change"
 msgstr "变动"
 
-#: fava/templates/_entry_forms.html:60 fava/templates/_journal_table.html:94
+#: fava/templates/_entry_forms.html:62 fava/templates/_journal_table.html:94
 #: fava/templates/statistics.html:40
 msgid "Balance"
 msgstr "余额"
 
 #: fava/templates/_context.html:57 fava/templates/_overlays.html:33
 #: fava/templates/editor.html:41
 msgid "Save"
@@ -191,16 +191,15 @@
 msgid "Help - %(title)s"
 msgstr "帮助 - %(title)s"
 
 #: fava/templates/help.html:9
 msgid "Help pages"
 msgstr "帮助页"
 
-#: fava/templates/_entry_forms.html:13 fava/templates/_entry_forms.html:63
-#: fava/templates/holdings.html:48
+#: fava/templates/_entry_forms.html:65 fava/templates/holdings.html:48
 msgid "Currency"
 msgstr "货币"
 
 #: fava/templates/holdings.html:48
 msgid "Cost currency"
 msgstr "成本货币"
 
@@ -216,20 +215,20 @@
 msgid "Income"
 msgstr "收入"
 
 #: fava/templates/income_statement.html:10
 msgid "Expenses"
 msgstr "支出"
 
-#: fava/templates/_entry_forms.html:21 fava/templates/options.html:9
+#: fava/templates/_entry_forms.html:23 fava/templates/options.html:9
 #: fava/templates/options.html:26
 msgid "Key"
 msgstr "键"
 
-#: fava/templates/_entry_forms.html:22 fava/templates/options.html:10
+#: fava/templates/_entry_forms.html:24 fava/templates/options.html:10
 #: fava/templates/options.html:27
 msgid "Value"
 msgstr "值"
 
 #: fava/templates/_query_table.html:69
 msgid "Download as"
 msgstr "下载为"
@@ -275,27 +274,27 @@
 msgid "close"
 msgstr "关闭"
 
 #: fava/templates/_overlays.html:30
 msgid "New transaction"
 msgstr "新交易"
 
-#: fava/templates/_entry_forms.html:42 fava/templates/_entry_forms.html:43
+#: fava/templates/_entry_forms.html:44 fava/templates/_entry_forms.html:45
 msgid "Narration"
 msgstr "摘要"
 
 #: fava/templates/_overlays.html:34
 msgid "Save and add new"
 msgstr "保存并添加下一条"
 
-#: fava/templates/_entry_forms.html:12 fava/templates/_entry_forms.html:62
+#: fava/templates/_entry_forms.html:8
 msgid "Number"
 msgstr "数额"
 
-#: fava/templates/_entry_forms.html:14 fava/templates/_entry_forms.html:45
+#: fava/templates/_entry_forms.html:16 fava/templates/_entry_forms.html:47
 msgid "Add posting"
 msgstr "添加记录"
 
 #: fava/templates/_globals.html:11 fava/templates/extract.html:7
 #: fava/templates/extract.html:34
 msgid "Import"
 msgstr "导入"
@@ -344,20 +343,20 @@
 msgid "...enter a BQL query. 'help' to list available commands."
 msgstr ""
 
 #: fava/templates/_journal_table.html:80
 msgid "Metadata"
 msgstr "元数据"
 
-#: fava/templates/_entry_forms.html:23 fava/templates/_entry_forms.html:44
-#: fava/templates/_entry_forms.html:64 fava/templates/_entry_forms.html:76
+#: fava/templates/_entry_forms.html:25 fava/templates/_entry_forms.html:46
+#: fava/templates/_entry_forms.html:66 fava/templates/_entry_forms.html:78
 msgid "Add metadata"
 msgstr "添加元数据"
 
-#: fava/templates/_entry_forms.html:74
+#: fava/templates/_entry_forms.html:76
 msgid "Note"
 msgstr "备注"
 
 #: fava/templates/_context.html:4
 msgid "Location"
 msgstr "位置"
 
@@ -385,18 +384,14 @@
 msgid "Other transactions"
 msgstr ""
 
 #: fava/templates/_journal_table.html:7
 msgid "Documents with a #discovered tag"
 msgstr ""
 
-#: fava/templates/_journal_table.html:8
-msgid "Documents with a #statement tag"
-msgstr ""
-
 #: fava/templates/_journal_table.html:81
 msgid "Postings"
 msgstr ""
 
 #: fava/templates/_overlays.html:7
 msgid "Upload file(s)"
 msgstr ""
@@ -458,31 +453,39 @@
 msgid "Download currently filtered entries as a Beancount file"
 msgstr ""
 
 #: fava/templates/extract.html:40
 msgid "Import entries"
 msgstr ""
 
-#: fava/util/date.py:44
+#: fava/util/date.py:50
 msgid "Yearly"
 msgstr ""
 
-#: fava/util/date.py:45
+#: fava/util/date.py:51
 msgid "Quarterly"
 msgstr ""
 
-#: fava/util/date.py:46
+#: fava/util/date.py:52
 msgid "Monthly"
 msgstr ""
 
-#: fava/util/date.py:47
+#: fava/util/date.py:53
 msgid "Weekly"
 msgstr ""
 
-#: fava/util/date.py:48
+#: fava/util/date.py:54
 msgid "Daily"
 msgstr ""
 
 #: fava/templates/editor.html:18
 msgid "Edit"
 msgstr ""
 
+#: fava/templates/_entry_forms.html:15
+msgid "Amount"
+msgstr ""
+
+#: fava/templates/_journal_table.html:8
+msgid "Documents with a #linked tag"
+msgstr ""
+
```

### Comparing `fava-1.8/fava/translations/messages.pot` & `fava-1.9/fava/translations/messages.pot`

 * *Files 1% similar despite different names*

```diff
@@ -4,15 +4,15 @@
 # FIRST AUTHOR <EMAIL@ADDRESS>, 2018.
 #
 #, fuzzy
 msgid ""
 msgstr ""
 "Project-Id-Version: PROJECT VERSION\n"
 "Report-Msgid-Bugs-To: EMAIL@ADDRESS\n"
-"POT-Creation-Date: 2018-07-25 20:28+0200\n"
+"POT-Creation-Date: 2018-10-08 21:09+0200\n"
 "PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE\n"
 "Last-Translator: FULL NAME <EMAIL@ADDRESS>\n"
 "Language-Team: LANGUAGE <LL@li.org>\n"
 "MIME-Version: 1.0\n"
 "Content-Type: text/plain; charset=utf-8\n"
 "Content-Transfer-Encoding: 8bit\n"
 "Generated-By: Babel 2.6.0\n"
@@ -71,56 +71,59 @@
 msgid "Account"
 msgstr ""
 
 #: fava/templates/_entry_filters.html:4
 msgid "Filter by tag, payee, ..."
 msgstr ""
 
-#: fava/templates/_entry_forms.html:12 fava/templates/_entry_forms.html:62
+#: fava/templates/_entry_forms.html:8
 msgid "Number"
 msgstr ""
 
-#: fava/templates/_entry_forms.html:13 fava/templates/_entry_forms.html:63
-#: fava/templates/holdings.html:48
-msgid "Currency"
+#: fava/templates/_entry_forms.html:15
+msgid "Amount"
 msgstr ""
 
-#: fava/templates/_entry_forms.html:14 fava/templates/_entry_forms.html:45
+#: fava/templates/_entry_forms.html:16 fava/templates/_entry_forms.html:47
 msgid "Add posting"
 msgstr ""
 
-#: fava/templates/_entry_forms.html:21 fava/templates/options.html:9
+#: fava/templates/_entry_forms.html:23 fava/templates/options.html:9
 #: fava/templates/options.html:26
 msgid "Key"
 msgstr ""
 
-#: fava/templates/_entry_forms.html:22 fava/templates/options.html:10
+#: fava/templates/_entry_forms.html:24 fava/templates/options.html:10
 #: fava/templates/options.html:27
 msgid "Value"
 msgstr ""
 
-#: fava/templates/_entry_forms.html:23 fava/templates/_entry_forms.html:44
-#: fava/templates/_entry_forms.html:64 fava/templates/_entry_forms.html:76
+#: fava/templates/_entry_forms.html:25 fava/templates/_entry_forms.html:46
+#: fava/templates/_entry_forms.html:66 fava/templates/_entry_forms.html:78
 msgid "Add metadata"
 msgstr ""
 
-#: fava/templates/_entry_forms.html:40 fava/templates/_entry_forms.html:41
+#: fava/templates/_entry_forms.html:42 fava/templates/_entry_forms.html:43
 msgid "Payee"
 msgstr ""
 
-#: fava/templates/_entry_forms.html:42 fava/templates/_entry_forms.html:43
+#: fava/templates/_entry_forms.html:44 fava/templates/_entry_forms.html:45
 msgid "Narration"
 msgstr ""
 
-#: fava/templates/_entry_forms.html:60 fava/templates/_journal_table.html:94
+#: fava/templates/_entry_forms.html:62 fava/templates/_journal_table.html:94
 #: fava/templates/statistics.html:40
 msgid "Balance"
 msgstr ""
 
-#: fava/templates/_entry_forms.html:74
+#: fava/templates/_entry_forms.html:65 fava/templates/holdings.html:48
+msgid "Currency"
+msgstr ""
+
+#: fava/templates/_entry_forms.html:76
 msgid "Note"
 msgstr ""
 
 #: fava/templates/_globals.html:2
 msgid "Income Statement"
 msgstr ""
 
@@ -178,15 +181,15 @@
 msgstr ""
 
 #: fava/templates/_journal_table.html:7
 msgid "Documents with a #discovered tag"
 msgstr ""
 
 #: fava/templates/_journal_table.html:8
-msgid "Documents with a #statement tag"
+msgid "Documents with a #linked tag"
 msgstr ""
 
 #: fava/templates/_journal_table.html:11
 msgid "Cleared transactions"
 msgstr ""
 
 #: fava/templates/_journal_table.html:12
@@ -478,27 +481,27 @@
 msgid "# Entries"
 msgstr ""
 
 #: fava/templates/statistics.html:90
 msgid "Total"
 msgstr ""
 
-#: fava/util/date.py:44
+#: fava/util/date.py:50
 msgid "Yearly"
 msgstr ""
 
-#: fava/util/date.py:45
+#: fava/util/date.py:51
 msgid "Quarterly"
 msgstr ""
 
-#: fava/util/date.py:46
+#: fava/util/date.py:52
 msgid "Monthly"
 msgstr ""
 
-#: fava/util/date.py:47
+#: fava/util/date.py:53
 msgid "Weekly"
 msgstr ""
 
-#: fava/util/date.py:48
+#: fava/util/date.py:54
 msgid "Daily"
 msgstr ""
```

### Comparing `fava-1.8/fava/util/__init__.py` & `fava-1.9/fava/util/__init__.py`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/util/excel.py` & `fava-1.9/fava/util/excel.py`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/util/ranking.py` & `fava-1.9/fava/util/ranking.py`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/__init__.py` & `fava-1.9/fava/__init__.py`

 * *Files 0% similar despite different names*

```diff
@@ -8,8 +8,8 @@
     Unless required by applicable law or agreed to in writing, software
     distributed under the License is distributed on an "AS IS" BASIS,
     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
     See the License for the specific language governing permissions and
     limitations under the License.
 """
 
-__version__ = '1.8'
+__version__ = '1.9'
```

### Comparing `fava-1.8/fava/application.py` & `fava-1.9/fava/application.py`

 * *Files 2% similar despite different names*

```diff
@@ -10,34 +10,37 @@
 Attributes:
     app: An instance of :class:`flask.Flask`, this is Fava's WSGI application.
 
 """
 import datetime
 import functools
 import inspect
+import threading
 import os
 import os.path
 from io import BytesIO
 
 from flask import (abort, Flask, render_template, request,
                    redirect, g, send_file, render_template_string)
 import flask
 from flask_babel import Babel
 import markdown2
 import werkzeug.urls
 from werkzeug.utils import secure_filename
 from beancount.utils.text_utils import replace_numbers
 from beancount.core.data import Document
+from beancount.core.account import ACCOUNT_RE
 
 from fava import template_filters
 from fava.core import FavaLedger
 from fava.core.charts import FavaJSONEncoder
 from fava.core.helpers import FavaAPIException
 from fava.help import HELP_PAGES
 from fava.json_api import json_api
+from fava.serialisation import serialise
 from fava.util import slugify, resource_path, setup_logging, send_file_inline
 from fava.util.date import Interval
 from fava.util.excel import HAVE_EXCEL
 
 
 setup_logging()
 app = Flask(  # pylint: disable=invalid-name
@@ -49,14 +52,15 @@
 app.json_encoder = FavaJSONEncoder
 app.jinja_options['extensions'].append('jinja2.ext.do')
 app.jinja_env.trim_blocks = True
 app.jinja_env.lstrip_blocks = True
 
 app.config['HAVE_EXCEL'] = HAVE_EXCEL
 app.config['HELP_PAGES'] = HELP_PAGES
+app.config['ACCOUNT_RE'] = ACCOUNT_RE
 
 REPORTS = [
     '_context',
     'balance_sheet',
     'commodities',
     'events',
     'editor',
@@ -69,14 +73,17 @@
     'options',
     'query',
     'statistics',
     'trial_balance',
 ]
 
 
+LOAD_FILE_LOCK = threading.Lock()
+
+
 def _load_file():
     """Load Beancount files.
 
     This is run automatically on the first request.
     """
     app.config['LEDGERS'] = {}
     for filepath in app.config['BEANCOUNT_FILES']:
@@ -103,14 +110,15 @@
         return g.ledger.fava_options['language']
     return request.accept_languages.best_match(
         ['de', 'en', 'es', 'zh', 'nl', 'fr', 'pt', 'sk', 'uk'])
 
 
 for _, function in inspect.getmembers(template_filters, inspect.isfunction):
     app.add_template_filter(function)
+app.add_template_filter(serialise)
 
 
 @app.url_defaults
 def _inject_filters(endpoint, values):
     if ('bfile' not in values
             and app.url_map.is_endpoint_expecting(endpoint, 'bfile')):
         values['bfile'] = g.beancount_file_slug
@@ -201,16 +209,17 @@
             response.set_data(replace_numbers(original_text))
     return response
 
 
 @app.url_value_preprocessor
 def _pull_beancount_file(_, values):
     g.beancount_file_slug = values.pop('bfile', None) if values else None
-    if not app.config.get('LEDGERS'):
-        _load_file()
+    with LOAD_FILE_LOCK:
+        if not app.config.get('LEDGERS'):
+            _load_file()
     if not g.beancount_file_slug:
         g.beancount_file_slug = app.config['FILE_SLUGS'][0]
     if g.beancount_file_slug not in app.config['FILE_SLUGS']:
         abort(404)
     g.ledger = app.config['LEDGERS'][g.beancount_file_slug]
     g.conversion = request.args.get('conversion')
     g.partial = request.args.get('partial', False)
```

### Comparing `fava-1.8/fava/cli.py` & `fava-1.9/fava/cli.py`

 * *Files 6% similar despite different names*

```diff
@@ -10,16 +10,17 @@
 from fava.application import app
 from fava.util import simple_wsgi
 from fava import __version__
 
 
 # pylint: disable=too-many-arguments
 @click.command()
-@click.argument('filenames', nargs=-1,
-                type=click.Path(exists=True, resolve_path=True))
+@click.argument(
+    'filenames',
+    nargs=-1, type=click.Path(exists=True, dir_okay=False, resolve_path=True))
 @click.option('-p', '--port', type=int, default=5000, metavar='<port>',
               help='The port to listen on. (default: 5000)')
 @click.option('-H', '--host', type=str, default='localhost', metavar='<host>',
               help='The host to listen on. (default: localhost)')
 @click.option('--prefix', type=str,
               help='Set an URL prefix. (for reverse proxy)')
 @click.option('--incognito', is_flag=True,
@@ -31,24 +32,24 @@
 @click.option('--profile-dir', type=click.Path(),
               help='Output directory for profiling data.')
 @click.version_option(version=__version__, prog_name='fava')
 def main(filenames, port, host, prefix, incognito, debug, profile,
          profile_dir):
     """Start Fava for FILENAMES on http://<host>:<port>.
 
-    If the `BEANCOUNT_FILE` environment variable is set, Fava will use the file
-    specified there in addition to FILENAMES.
+    If the `BEANCOUNT_FILE` environment variable is set, Fava will use the
+    files (space-delimited) specified there in addition to FILENAMES.
     """
 
     if profile:  # pragma: no cover
         debug = True
 
     env_filename = os.environ.get('BEANCOUNT_FILE')
     if env_filename:
-        filenames = filenames + (env_filename,)
+        filenames = filenames + tuple(env_filename.split())
 
     if not filenames:
         raise click.UsageError('No file specified')
 
     app.config['BEANCOUNT_FILES'] = filenames
     app.config['INCOGNITO'] = incognito
```

### Comparing `fava-1.8/fava/json_api.py` & `fava-1.9/fava/json_api.py`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava/serialisation.py` & `fava-1.9/fava/serialisation.py`

 * *Files 26% similar despite different names*

```diff
@@ -4,18 +4,19 @@
 of this module to obtain the appropriate data structures from
 `beancount.core.data`. Similarly, for the full entry completion, a JSON
 representation of the entry is provided.
 
 This is not intended to work well enough for full roundtrips yet.
 """
 
+import functools
 import re
 
-from beancount.core import data
-from beancount.core.amount import Amount
+from beancount.core import data, position
+from beancount.core.amount import A, Amount
 from beancount.core.number import D
 
 from fava import util
 from fava.core.helpers import FavaAPIException
 
 
 def extract_tags_links(string):
@@ -43,50 +44,80 @@
         return None
     if '/' in num:
         left, right = num.split('/')
         return D(left) / D(right)
     return D(num)
 
 
+@functools.singledispatch
 def serialise(entry):
     """Serialise an entry."""
     if not entry:
         return None
     ret = entry._asdict()
     ret['type'] = entry.__class__.__name__
     if ret['type'] == 'Transaction':
         if entry.tags:
             ret['narration'] += ' ' + ' '.join(['#' + t for t in entry.tags])
         if entry.links:
             ret['narration'] += ' ' + ' '.join(['^' + l for l in entry.links])
+        del ret['links']
+        del ret['tags']
+        ret['postings'] = [serialise(pos) for pos in entry.postings]
     return ret
 
 
+@serialise.register(data.Posting)
+def _serialise_posting(posting):
+    """Serialise a posting."""
+    if isinstance(posting.units, Amount):
+        position_str = position.to_string(posting)
+    else:
+        position_str = ''
+
+    if posting.price is not None:
+        position_str += ' @ {}'.format(posting.price.to_string())
+    return {
+        'account': posting.account,
+        'amount': position_str,
+    }
+
+
+def deserialise_posting(posting):
+    """Parse JSON to a Beancount Posting."""
+    amount = posting.get('amount')
+    price = None
+    if amount:
+        if '@' in amount:
+            amount, raw_price = amount.split('@')
+            price = A(raw_price)
+        pos = position.from_string(amount)
+        units, cost = pos.units, pos.cost
+    else:
+        units, cost = None, None
+    return data.Posting(posting['account'], units, cost, price, None, None)
+
+
 def deserialise(json_entry):
     """Parse JSON to a Beancount entry.
 
     Args:
         json_entry: The entry.
 
     Raises:
         KeyError: if one of the required entry fields is missing.
         FavaAPIException: if the type of the given entry is not supported.
     """
     if json_entry['type'] == 'Transaction':
         date = util.date.parse_date(json_entry['date'])[0]
         narration, tags, links = extract_tags_links(json_entry['narration'])
-        txn = data.Transaction(json_entry['meta'], date, json_entry['flag'],
-                               json_entry['payee'], narration, tags, links, [])
-
-        for posting in json_entry['postings']:
-            data.create_simple_posting(txn, posting['account'],
-                                       parse_number(posting.get('number')),
-                                       posting.get('currency'))
-
-        return txn
+        postings = [deserialise_posting(pos) for pos in json_entry['postings']]
+        return data.Transaction(json_entry['meta'], date, json_entry['flag'],
+                                json_entry['payee'], narration, tags, links,
+                                postings)
     if json_entry['type'] == 'Balance':
         date = util.date.parse_date(json_entry['date'])[0]
         number = parse_number(json_entry['number'])
         amount = Amount(number, json_entry['currency'])
 
         return data.Balance(json_entry['meta'], date, json_entry['account'],
                             amount, None, None)
```

### Comparing `fava-1.8/fava/template_filters.py` & `fava-1.9/fava/template_filters.py`

 * *Files identical despite different names*

### Comparing `fava-1.8/fava.egg-info/PKG-INFO` & `fava-1.9/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: fava
-Version: 1.8
+Version: 1.9
 Summary: Web interface for the accounting tool Beancount.
 Home-page: https://beancount.github.io/fava/
 Author: Dominik Aumayr
 Author-email: dominik@aumayr.name
 License: MIT
 Description: .. image:: https://badges.gitter.im/beancount/fava.svg
            :alt: Join the chat at https://gitter.im/beancount/fava
```

### Comparing `fava-1.8/fava.egg-info/SOURCES.txt` & `fava-1.9/fava.egg-info/SOURCES.txt`

 * *Files 4% similar despite different names*

```diff
@@ -39,15 +39,15 @@
 fava/help/beancount_syntax.md
 fava/help/budgets.md
 fava/help/extensions.md
 fava/help/features.md
 fava/help/filters.md
 fava/help/import.md
 fava/help/options.md
-fava/plugins/link_statements.py
+fava/plugins/link_documents.py
 fava/plugins/tag_discovered_documents.py
 fava/static/css/base.css
 fava/static/css/charts.css
 fava/static/css/components.css
 fava/static/css/editor.css
 fava/static/css/entry-forms.css
 fava/static/css/fonts.css
```

### Comparing `fava-1.8/CHANGES` & `fava-1.9/CHANGES`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,17 @@
 Changelog
 =========
 
+v1.9 (October 8th, 2018)
+------------------------
+
+In this release, the click behaviour has been updated to allow filtering for
+payees. The entry input forms now allow inputting prices and costs.  As
+always, bugs have been fixed.
+
 v1.8 (July 25th, 2018)
 ----------------------
 
 The journal design has been updated and should now have a clearer structure.
 Starting with this version, there will not be any more GUI releases of Fava.
 The GUI broke frequently and does not seem to worth the maintenance burden.
```

### Comparing `fava-1.8/LICENSE` & `fava-1.9/LICENSE`

 * *Files identical despite different names*

### Comparing `fava-1.8/README.rst` & `fava-1.9/README.rst`

 * *Files identical despite different names*

### Comparing `fava-1.8/setup.py` & `fava-1.9/setup.py`

 * *Files identical despite different names*

### Comparing `fava-1.8/PKG-INFO` & `fava-1.9/fava.egg-info/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: fava
-Version: 1.8
+Version: 1.9
 Summary: Web interface for the accounting tool Beancount.
 Home-page: https://beancount.github.io/fava/
 Author: Dominik Aumayr
 Author-email: dominik@aumayr.name
 License: MIT
 Description: .. image:: https://badges.gitter.im/beancount/fava.svg
            :alt: Join the chat at https://gitter.im/beancount/fava
```

