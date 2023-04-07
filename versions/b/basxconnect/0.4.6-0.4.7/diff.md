# Comparing `tmp/basxconnect-0.4.6.tar.gz` & `tmp/basxconnect-0.4.7.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "basxconnect-0.4.6.tar", last modified: Thu Jun 23 12:31:10 2022, max compression
+gzip compressed data, was "basxconnect-0.4.7.tar", last modified: Sun Jul 24 08:58:22 2022, max compression
```

## Comparing `basxconnect-0.4.6.tar` & `basxconnect-0.4.7.tar`

### file list

```diff
@@ -1,235 +1,237 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-23 12:31:10.594868 basxconnect-0.4.6/
--rw-r--r--   0 runner    (1001) docker     (121)       59 2022-06-23 12:30:55.000000 basxconnect-0.4.6/.bandit
--rw-r--r--   0 runner    (1001) docker     (121)      149 2022-06-23 12:30:55.000000 basxconnect-0.4.6/.flake8
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-23 12:31:10.570867 basxconnect-0.4.6/.github/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-23 12:31:10.574867 basxconnect-0.4.6/.github/ISSUE_TEMPLATE/
--rw-r--r--   0 runner    (1001) docker     (121)      841 2022-06-23 12:30:55.000000 basxconnect-0.4.6/.github/ISSUE_TEMPLATE/bug_report.md
--rw-r--r--   0 runner    (1001) docker     (121)      608 2022-06-23 12:30:55.000000 basxconnect-0.4.6/.github/ISSUE_TEMPLATE/feature_request.md
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-23 12:31:10.574867 basxconnect-0.4.6/.github/workflows/
--rw-r--r--   0 runner    (1001) docker     (121)      905 2022-06-23 12:30:55.000000 basxconnect-0.4.6/.github/workflows/automated_release.yml
--rw-r--r--   0 runner    (1001) docker     (121)     1692 2022-06-23 12:30:55.000000 basxconnect-0.4.6/.github/workflows/main.yml
--rw-r--r--   0 runner    (1001) docker     (121)      142 2022-06-23 12:30:55.000000 basxconnect-0.4.6/.gitignore
--rw-r--r--   0 runner    (1001) docker     (121)       31 2022-06-23 12:30:55.000000 basxconnect-0.4.6/.isort.cfg
--rw-r--r--   0 runner    (1001) docker     (121)     1527 2022-06-23 12:30:55.000000 basxconnect-0.4.6/LICENSE
--rw-r--r--   0 runner    (1001) docker     (121)      752 2022-06-23 12:30:55.000000 basxconnect-0.4.6/Makefile
--rw-r--r--   0 runner    (1001) docker     (121)     3421 2022-06-23 12:31:10.594868 basxconnect-0.4.6/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     2703 2022-06-23 12:30:55.000000 basxconnect-0.4.6/README.md
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-23 12:31:10.574867 basxconnect-0.4.6/basxconnect/
--rw-r--r--   0 runner    (1001) docker     (121)       22 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-23 12:31:10.578868 basxconnect-0.4.6/basxconnect/contributions/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/contributions/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      170 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/contributions/apps.py
--rw-r--r--   0 runner    (1001) docker     (121)      568 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/contributions/dynamic_preferences_registry.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-23 12:31:10.574867 basxconnect-0.4.6/basxconnect/contributions/locale/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-23 12:31:10.570867 basxconnect-0.4.6/basxconnect/contributions/locale/de/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-23 12:31:10.578868 basxconnect-0.4.6/basxconnect/contributions/locale/de/LC_MESSAGES/
--rw-r--r--   0 runner    (1001) docker     (121)     5968 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/contributions/locale/de/LC_MESSAGES/django.po
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-23 12:31:10.570867 basxconnect-0.4.6/basxconnect/contributions/locale/fr/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-23 12:31:10.578868 basxconnect-0.4.6/basxconnect/contributions/locale/fr/LC_MESSAGES/
--rw-r--r--   0 runner    (1001) docker     (121)     6137 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/contributions/locale/fr/LC_MESSAGES/django.po
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-23 12:31:10.570867 basxconnect-0.4.6/basxconnect/contributions/locale/nb_NO/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-23 12:31:10.578868 basxconnect-0.4.6/basxconnect/contributions/locale/nb_NO/LC_MESSAGES/
--rw-r--r--   0 runner    (1001) docker     (121)     5963 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/contributions/locale/nb_NO/LC_MESSAGES/django.po
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-23 12:31:10.574867 basxconnect-0.4.6/basxconnect/contributions/locale/pt/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-23 12:31:10.578868 basxconnect-0.4.6/basxconnect/contributions/locale/pt/LC_MESSAGES/
--rw-r--r--   0 runner    (1001) docker     (121)     6168 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/contributions/locale/pt/LC_MESSAGES/django.po
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-23 12:31:10.574867 basxconnect-0.4.6/basxconnect/contributions/locale/th/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-23 12:31:10.578868 basxconnect-0.4.6/basxconnect/contributions/locale/th/LC_MESSAGES/
--rw-r--r--   0 runner    (1001) docker     (121)     7308 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/contributions/locale/th/LC_MESSAGES/django.po
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-23 12:31:10.578868 basxconnect-0.4.6/basxconnect/contributions/migrations/
--rw-r--r--   0 runner    (1001) docker     (121)    14479 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/contributions/migrations/0001_initial.py
--rw-r--r--   0 runner    (1001) docker     (121)    16506 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/contributions/migrations/0002_alter_contribution_currency.py
--rw-r--r--   0 runner    (1001) docker     (121)      659 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/contributions/migrations/0003_alter_contribution__import.py
--rw-r--r--   0 runner    (1001) docker     (121)      745 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/contributions/migrations/0004_auto_20211030_0955.py
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/contributions/migrations/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2923 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/contributions/models.py
--rw-r--r--   0 runner    (1001) docker     (121)      437 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/contributions/settings.py
--rw-r--r--   0 runner    (1001) docker     (121)     1826 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/contributions/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-23 12:31:10.578868 basxconnect-0.4.6/basxconnect/contributions/wizards/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/contributions/wizards/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    12137 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/contributions/wizards/contributionsimport.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-23 12:31:10.578868 basxconnect-0.4.6/basxconnect/core/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1874 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/apps.py
--rw-r--r--   0 runner    (1001) docker     (121)      469 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/context_processors.py
--rw-r--r--   0 runner    (1001) docker     (121)     2007 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/dynamic_preferences_registry.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-23 12:31:10.578868 basxconnect-0.4.6/basxconnect/core/fixtures/
--rw-r--r--   0 runner    (1001) docker     (121)     6176 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/fixtures/base.de.json
--rw-r--r--   0 runner    (1001) docker     (121)     5718 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/fixtures/base.en.json
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-23 12:31:10.578868 basxconnect-0.4.6/basxconnect/core/layouts/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/layouts/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-23 12:31:10.578868 basxconnect-0.4.6/basxconnect/core/layouts/editperson/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/layouts/editperson/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-23 12:31:10.578868 basxconnect-0.4.6/basxconnect/core/layouts/editperson/common/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/layouts/editperson/common/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     9354 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/layouts/editperson/common/addresses.py
--rw-r--r--   0 runner    (1001) docker     (121)     1513 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/layouts/editperson/common/base_data.py
--rw-r--r--   0 runner    (1001) docker     (121)     1771 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/layouts/editperson/common/contributions_tab.py
--rw-r--r--   0 runner    (1001) docker     (121)     1832 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/layouts/editperson/common/head.py
--rw-r--r--   0 runner    (1001) docker     (121)     4805 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/layouts/editperson/common/relationships_tab.py
--rw-r--r--   0 runner    (1001) docker     (121)     4374 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/layouts/editperson/common/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-23 12:31:10.578868 basxconnect-0.4.6/basxconnect/core/layouts/editperson/legalperson/
--rw-r--r--   0 runner    (1001) docker     (121)       68 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/layouts/editperson/legalperson/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1117 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/layouts/editperson/legalperson/base_data_tab.py
--rw-r--r--   0 runner    (1001) docker     (121)     1178 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/layouts/editperson/legalperson/mailing.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-23 12:31:10.578868 basxconnect-0.4.6/basxconnect/core/layouts/editperson/naturalperson/
--rw-r--r--   0 runner    (1001) docker     (121)       68 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/layouts/editperson/naturalperson/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2063 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/layouts/editperson/naturalperson/base_data_tab.py
--rw-r--r--   0 runner    (1001) docker     (121)     1257 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/layouts/editperson/naturalperson/mailing.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-23 12:31:10.582867 basxconnect-0.4.6/basxconnect/core/layouts/editperson/personassociation/
--rw-r--r--   0 runner    (1001) docker     (121)       68 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/layouts/editperson/personassociation/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1016 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/layouts/editperson/personassociation/base_data_tab.py
--rw-r--r--   0 runner    (1001) docker     (121)      682 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/layouts/editperson/personassociation/mailing.py
--rw-r--r--   0 runner    (1001) docker     (121)     4998 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/layouts/settings_layout.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-23 12:31:10.574867 basxconnect-0.4.6/basxconnect/core/locale/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-23 12:31:10.574867 basxconnect-0.4.6/basxconnect/core/locale/de/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-23 12:31:10.582867 basxconnect-0.4.6/basxconnect/core/locale/de/LC_MESSAGES/
--rw-r--r--   0 runner    (1001) docker     (121)    22929 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/locale/de/LC_MESSAGES/django.po
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-23 12:31:10.574867 basxconnect-0.4.6/basxconnect/core/locale/fr/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-23 12:31:10.582867 basxconnect-0.4.6/basxconnect/core/locale/fr/LC_MESSAGES/
--rw-r--r--   0 runner    (1001) docker     (121)    25216 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/locale/fr/LC_MESSAGES/django.po
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-23 12:31:10.574867 basxconnect-0.4.6/basxconnect/core/locale/nb_NO/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-23 12:31:10.582867 basxconnect-0.4.6/basxconnect/core/locale/nb_NO/LC_MESSAGES/
--rw-r--r--   0 runner    (1001) docker     (121)    23756 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/locale/nb_NO/LC_MESSAGES/django.po
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-23 12:31:10.574867 basxconnect-0.4.6/basxconnect/core/locale/pt/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-23 12:31:10.582867 basxconnect-0.4.6/basxconnect/core/locale/pt/LC_MESSAGES/
--rw-r--r--   0 runner    (1001) docker     (121)    25314 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/locale/pt/LC_MESSAGES/django.po
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-23 12:31:10.574867 basxconnect-0.4.6/basxconnect/core/locale/th/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-23 12:31:10.582867 basxconnect-0.4.6/basxconnect/core/locale/th/LC_MESSAGES/
--rw-r--r--   0 runner    (1001) docker     (121)    31468 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/locale/th/LC_MESSAGES/django.po
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-23 12:31:10.586867 basxconnect-0.4.6/basxconnect/core/migrations/
--rw-r--r--   0 runner    (1001) docker     (121)  2061151 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/migrations/0001_initial.py
--rw-r--r--   0 runner    (1001) docker     (121)      507 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/migrations/0002_auto_20210309_1750.py
--rw-r--r--   0 runner    (1001) docker     (121)     2253 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/migrations/0003_auto_20210309_2221.py
--rw-r--r--   0 runner    (1001) docker     (121)     1734 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/migrations/0004_auto_20210311_1851.py
--rw-r--r--   0 runner    (1001) docker     (121)     1158 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/migrations/0005_auto_20210311_1851.py
--rw-r--r--   0 runner    (1001) docker     (121)     1094 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/migrations/0006_auto_20210312_0016.py
--rw-r--r--   0 runner    (1001) docker     (121)     2152 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/migrations/0007_auto_20210312_0054.py
--rw-r--r--   0 runner    (1001) docker     (121)     1398 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/migrations/0008_auto_20210323_1456.py
--rw-r--r--   0 runner    (1001) docker     (121)      877 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/migrations/0009_auto_20210522_1817.py
--rw-r--r--   0 runner    (1001) docker     (121)      682 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/migrations/0010_auto_20210523_1140.py
--rw-r--r--   0 runner    (1001) docker     (121)     2036 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/migrations/0011_auto_20210726_2047.py
--rw-r--r--   0 runner    (1001) docker     (121)      740 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/migrations/0012_auto_20210928_1158.py
--rw-r--r--   0 runner    (1001) docker     (121)      589 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/migrations/0013_auto_20210928_1445.py
--rw-r--r--   0 runner    (1001) docker     (121)    10895 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/migrations/0014_auto_20210928_1512.py
--rw-r--r--   0 runner    (1001) docker     (121)      862 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/migrations/0015_rename_category_to_tag.py
--rw-r--r--   0 runner    (1001) docker     (121)     1136 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/migrations/0016_auto_20210928_1534.py
--rw-r--r--   0 runner    (1001) docker     (121)      329 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/migrations/0017_remove_person_categories.py
--rw-r--r--   0 runner    (1001) docker     (121)      951 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/migrations/0018_term_slug.py
--rw-r--r--   0 runner    (1001) docker     (121)      447 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/migrations/0019_alter_term_slug.py
--rw-r--r--   0 runner    (1001) docker     (121)      603 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/migrations/0020_auto_20211005_1630.py
--rw-r--r--   0 runner    (1001) docker     (121)      527 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/migrations/0021_auto_20211007_0932.py
--rw-r--r--   0 runner    (1001) docker     (121)      729 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/migrations/0022_auto_20211018_1644.py
--rw-r--r--   0 runner    (1001) docker     (121)     3881 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/migrations/0023_auto_20211030_0955.py
--rw-r--r--   0 runner    (1001) docker     (121)      413 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/migrations/0024_alter_term_slug.py
--rw-r--r--   0 runner    (1001) docker     (121)      453 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/migrations/0025_alter_term_slug.py
--rw-r--r--   0 runner    (1001) docker     (121)     2129 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/migrations/0026_auto_20211216_0946.py
--rw-r--r--   0 runner    (1001) docker     (121)     4295 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/migrations/0027_auto_20211223_1948.py
--rw-r--r--   0 runner    (1001) docker     (121)      503 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/migrations/0028_auto_20220404_1058.py
--rw-r--r--   0 runner    (1001) docker     (121)     2244 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/migrations/0029_auto_20220429_1138.py
--rw-r--r--   0 runner    (1001) docker     (121)      721 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/migrations/0030_auto_20220602_1434.py
--rw-r--r--   0 runner    (1001) docker     (121)     3106 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/migrations/0031_alter_email_person_alter_email_type_alter_fax_person_and_more.py
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/migrations/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-23 12:31:10.586867 basxconnect-0.4.6/basxconnect/core/models/
--rw-r--r--   0 runner    (1001) docker     (121)      130 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/models/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     4333 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/models/addresses.py
--rw-r--r--   0 runner    (1001) docker     (121)    12894 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/models/persons.py
--rw-r--r--   0 runner    (1001) docker     (121)     1676 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/models/relationships.py
--rw-r--r--   0 runner    (1001) docker     (121)     2137 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/models/utils.py
--rw-r--r--   0 runner    (1001) docker     (121)      623 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/search_indexes.py
--rw-r--r--   0 runner    (1001) docker     (121)      483 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/settings.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-23 12:31:10.586867 basxconnect-0.4.6/basxconnect/core/static/
--rw-r--r--   0 runner    (1001) docker     (121)     3558 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/static/logo.png
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-23 12:31:10.586867 basxconnect-0.4.6/basxconnect/core/tests/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/tests/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1162 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/tests/settings.py
--rw-r--r--   0 runner    (1001) docker     (121)      644 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/tests/test_person.py
--rw-r--r--   0 runner    (1001) docker     (121)      160 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/tests/urls.py
--rw-r--r--   0 runner    (1001) docker     (121)     7506 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-23 12:31:10.586867 basxconnect-0.4.6/basxconnect/core/views/
--rw-r--r--   0 runner    (1001) docker     (121)      187 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/views/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1858 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/views/menu_views.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-23 12:31:10.586867 basxconnect-0.4.6/basxconnect/core/views/person/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/views/person/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    19636 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/views/person/person_browse_views.py
--rw-r--r--   0 runner    (1001) docker     (121)     7276 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/views/person/person_details_views.py
--rw-r--r--   0 runner    (1001) docker     (121)     8548 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/views/person/person_modals_views.py
--rw-r--r--   0 runner    (1001) docker     (121)     3064 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/views/person/search_person_view.py
--rw-r--r--   0 runner    (1001) docker     (121)     2216 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/views/relationship_views.py
--rw-r--r--   0 runner    (1001) docker     (121)     1449 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/views/settings_views.py
--rw-r--r--   0 runner    (1001) docker     (121)     4500 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/views/tag_views.py
--rw-r--r--   0 runner    (1001) docker     (121)     1281 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/views/term.py
--rw-r--r--   0 runner    (1001) docker     (121)      494 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/views/vocabulary.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-23 12:31:10.586867 basxconnect-0.4.6/basxconnect/core/wizards/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/wizards/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    13775 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/core/wizards/add_person.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-23 12:31:10.590868 basxconnect-0.4.6/basxconnect/mailer_integration/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/mailer_integration/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-23 12:31:10.590868 basxconnect-0.4.6/basxconnect/mailer_integration/abstract/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/mailer_integration/abstract/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2160 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/mailer_integration/abstract/mailer.py
--rw-r--r--   0 runner    (1001) docker     (121)      271 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/mailer_integration/apps.py
--rw-r--r--   0 runner    (1001) docker     (121)     1813 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/mailer_integration/dynamic_preferences_registry.py
--rw-r--r--   0 runner    (1001) docker     (121)     1518 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/mailer_integration/help.py
--rw-r--r--   0 runner    (1001) docker     (121)     5723 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/mailer_integration/layouts.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-23 12:31:10.574867 basxconnect-0.4.6/basxconnect/mailer_integration/locale/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-23 12:31:10.574867 basxconnect-0.4.6/basxconnect/mailer_integration/locale/de/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-23 12:31:10.590868 basxconnect-0.4.6/basxconnect/mailer_integration/locale/de/LC_MESSAGES/
--rw-r--r--   0 runner    (1001) docker     (121)     6658 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/mailer_integration/locale/de/LC_MESSAGES/django.po
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-23 12:31:10.574867 basxconnect-0.4.6/basxconnect/mailer_integration/locale/fr/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-23 12:31:10.590868 basxconnect-0.4.6/basxconnect/mailer_integration/locale/fr/LC_MESSAGES/
--rw-r--r--   0 runner    (1001) docker     (121)     5765 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/mailer_integration/locale/fr/LC_MESSAGES/django.po
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-23 12:31:10.574867 basxconnect-0.4.6/basxconnect/mailer_integration/locale/nb_NO/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-23 12:31:10.590868 basxconnect-0.4.6/basxconnect/mailer_integration/locale/nb_NO/LC_MESSAGES/
--rw-r--r--   0 runner    (1001) docker     (121)     5719 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/mailer_integration/locale/nb_NO/LC_MESSAGES/django.po
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-23 12:31:10.574867 basxconnect-0.4.6/basxconnect/mailer_integration/locale/pt/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-23 12:31:10.590868 basxconnect-0.4.6/basxconnect/mailer_integration/locale/pt/LC_MESSAGES/
--rw-r--r--   0 runner    (1001) docker     (121)     5766 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/mailer_integration/locale/pt/LC_MESSAGES/django.po
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-23 12:31:10.574867 basxconnect-0.4.6/basxconnect/mailer_integration/locale/th/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-23 12:31:10.590868 basxconnect-0.4.6/basxconnect/mailer_integration/locale/th/LC_MESSAGES/
--rw-r--r--   0 runner    (1001) docker     (121)     7328 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/mailer_integration/locale/th/LC_MESSAGES/django.po
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-23 12:31:10.590868 basxconnect-0.4.6/basxconnect/mailer_integration/mailchimp/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/mailer_integration/mailchimp/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     5344 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/mailer_integration/mailchimp/mailer.py
--rw-r--r--   0 runner    (1001) docker     (121)     3179 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/mailer_integration/mailchimp/parsing.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-23 12:31:10.594868 basxconnect-0.4.6/basxconnect/mailer_integration/migrations/
--rw-r--r--   0 runner    (1001) docker     (121)     1542 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/mailer_integration/migrations/0001_initial.py
--rw-r--r--   0 runner    (1001) docker     (121)      454 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/mailer_integration/migrations/0002_interest_external_id.py
--rw-r--r--   0 runner    (1001) docker     (121)      406 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/mailer_integration/migrations/0003_alter_interest_external_id.py
--rw-r--r--   0 runner    (1001) docker     (121)      772 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/mailer_integration/migrations/0004_auto_20210823_1424.py
--rw-r--r--   0 runner    (1001) docker     (121)      567 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/mailer_integration/migrations/0005_alter_mailingpreferences_email.py
--rw-r--r--   0 runner    (1001) docker     (121)      703 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/mailer_integration/migrations/0006_alter_mailingpreferences_status.py
--rw-r--r--   0 runner    (1001) docker     (121)      462 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/mailer_integration/migrations/0007_alter_mailingpreferences_interests.py
--rw-r--r--   0 runner    (1001) docker     (121)      595 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/mailer_integration/migrations/0008_alter_mailingpreferences_email.py
--rw-r--r--   0 runner    (1001) docker     (121)      579 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/mailer_integration/migrations/0009_alter_mailingpreferences_email.py
--rw-r--r--   0 runner    (1001) docker     (121)   338882 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/mailer_integration/migrations/0010_mailingpreferences_language.py
--rw-r--r--   0 runner    (1001) docker     (121)     2457 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/mailer_integration/migrations/0011_invalidperson_newperson_synchronizationresult.py
--rw-r--r--   0 runner    (1001) docker     (121)     2031 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/mailer_integration/migrations/0012_auto_20211119_0830.py
--rw-r--r--   0 runner    (1001) docker     (121)      656 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/mailer_integration/migrations/0013_mailingpreferences_latest_sync.py
--rw-r--r--   0 runner    (1001) docker     (121)      416 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/mailer_integration/migrations/0014_rename_mailingpreferences_subscription.py
--rw-r--r--   0 runner    (1001) docker     (121)      468 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/mailer_integration/migrations/0015_synchronizationperson_message.py
--rw-r--r--   0 runner    (1001) docker     (121)      377 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/mailer_integration/migrations/0016_remove_synchronizationperson_successfully_added.py
--rw-r--r--   0 runner    (1001) docker     (121)      933 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/mailer_integration/migrations/0017_auto_20211122_1219.py
--rw-r--r--   0 runner    (1001) docker     (121)      790 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/mailer_integration/migrations/0018_alter_synchronizationperson_sync_status.py
--rw-r--r--   0 runner    (1001) docker     (121)      753 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/mailer_integration/migrations/0019_auto_20211210_1602.py
--rw-r--r--   0 runner    (1001) docker     (121)      487 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/mailer_integration/migrations/0020_subscription_deleted.py
--rw-r--r--   0 runner    (1001) docker     (121)      597 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/mailer_integration/migrations/0021_auto_20220106_0917.py
--rw-r--r--   0 runner    (1001) docker     (121)     1323 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/mailer_integration/migrations/0022_auto_20220118_1308.py
--rw-r--r--   0 runner    (1001) docker     (121)     1406 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/mailer_integration/migrations/0023_auto_20220517_1700.py
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/mailer_integration/migrations/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     3148 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/mailer_integration/models.py
--rw-r--r--   0 runner    (1001) docker     (121)       92 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/mailer_integration/settings.py
--rw-r--r--   0 runner    (1001) docker     (121)     1398 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/mailer_integration/signal_handlers.py
--rw-r--r--   0 runner    (1001) docker     (121)     5704 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/mailer_integration/synchronize.py
--rw-r--r--   0 runner    (1001) docker     (121)      744 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/mailer_integration/urls.py
--rw-r--r--   0 runner    (1001) docker     (121)     6325 2022-06-23 12:30:55.000000 basxconnect-0.4.6/basxconnect/mailer_integration/views.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-23 12:31:10.574867 basxconnect-0.4.6/basxconnect.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)     3421 2022-06-23 12:31:10.000000 basxconnect-0.4.6/basxconnect.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     8678 2022-06-23 12:31:10.000000 basxconnect-0.4.6/basxconnect.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-06-23 12:31:10.000000 basxconnect-0.4.6/basxconnect.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-06-23 12:31:10.000000 basxconnect-0.4.6/basxconnect.egg-info/not-zip-safe
--rw-r--r--   0 runner    (1001) docker     (121)      147 2022-06-23 12:31:10.000000 basxconnect-0.4.6/basxconnect.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)       12 2022-06-23 12:31:10.000000 basxconnect-0.4.6/basxconnect.egg-info/top_level.txt
--rwxr-xr-x   0 runner    (1001) docker     (121)      964 2022-06-23 12:30:55.000000 basxconnect-0.4.6/manage.py
--rw-r--r--   0 runner    (1001) docker     (121)       38 2022-06-23 12:31:10.594868 basxconnect-0.4.6/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)     1449 2022-06-23 12:30:55.000000 basxconnect-0.4.6/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:22.488048 basxconnect-0.4.7/
+-rw-r--r--   0 runner    (1001) docker     (121)       59 2022-07-24 08:58:00.000000 basxconnect-0.4.7/.bandit
+-rw-r--r--   0 runner    (1001) docker     (121)      149 2022-07-24 08:58:00.000000 basxconnect-0.4.7/.flake8
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:22.452048 basxconnect-0.4.7/.github/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:22.456048 basxconnect-0.4.7/.github/ISSUE_TEMPLATE/
+-rw-r--r--   0 runner    (1001) docker     (121)      841 2022-07-24 08:58:00.000000 basxconnect-0.4.7/.github/ISSUE_TEMPLATE/bug_report.md
+-rw-r--r--   0 runner    (1001) docker     (121)      608 2022-07-24 08:58:00.000000 basxconnect-0.4.7/.github/ISSUE_TEMPLATE/feature_request.md
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:22.456048 basxconnect-0.4.7/.github/workflows/
+-rw-r--r--   0 runner    (1001) docker     (121)      905 2022-07-24 08:58:00.000000 basxconnect-0.4.7/.github/workflows/automated_release.yml
+-rw-r--r--   0 runner    (1001) docker     (121)     1692 2022-07-24 08:58:00.000000 basxconnect-0.4.7/.github/workflows/main.yml
+-rw-r--r--   0 runner    (1001) docker     (121)      142 2022-07-24 08:58:00.000000 basxconnect-0.4.7/.gitignore
+-rw-r--r--   0 runner    (1001) docker     (121)       31 2022-07-24 08:58:00.000000 basxconnect-0.4.7/.isort.cfg
+-rw-r--r--   0 runner    (1001) docker     (121)     1527 2022-07-24 08:58:00.000000 basxconnect-0.4.7/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (121)      752 2022-07-24 08:58:00.000000 basxconnect-0.4.7/Makefile
+-rw-r--r--   0 runner    (1001) docker     (121)     3421 2022-07-24 08:58:22.488048 basxconnect-0.4.7/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)     2703 2022-07-24 08:58:00.000000 basxconnect-0.4.7/README.md
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:22.456048 basxconnect-0.4.7/basxconnect/
+-rw-r--r--   0 runner    (1001) docker     (121)       22 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:22.456048 basxconnect-0.4.7/basxconnect/contributions/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/contributions/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      170 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/contributions/apps.py
+-rw-r--r--   0 runner    (1001) docker     (121)      568 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/contributions/dynamic_preferences_registry.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:22.452048 basxconnect-0.4.7/basxconnect/contributions/locale/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:22.452048 basxconnect-0.4.7/basxconnect/contributions/locale/de/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:22.456048 basxconnect-0.4.7/basxconnect/contributions/locale/de/LC_MESSAGES/
+-rw-r--r--   0 runner    (1001) docker     (121)     5968 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/contributions/locale/de/LC_MESSAGES/django.po
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:22.452048 basxconnect-0.4.7/basxconnect/contributions/locale/fr/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:22.456048 basxconnect-0.4.7/basxconnect/contributions/locale/fr/LC_MESSAGES/
+-rw-r--r--   0 runner    (1001) docker     (121)     6137 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/contributions/locale/fr/LC_MESSAGES/django.po
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:22.452048 basxconnect-0.4.7/basxconnect/contributions/locale/nb_NO/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:22.456048 basxconnect-0.4.7/basxconnect/contributions/locale/nb_NO/LC_MESSAGES/
+-rw-r--r--   0 runner    (1001) docker     (121)     5963 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/contributions/locale/nb_NO/LC_MESSAGES/django.po
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:22.452048 basxconnect-0.4.7/basxconnect/contributions/locale/pt/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:22.456048 basxconnect-0.4.7/basxconnect/contributions/locale/pt/LC_MESSAGES/
+-rw-r--r--   0 runner    (1001) docker     (121)     6168 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/contributions/locale/pt/LC_MESSAGES/django.po
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:22.452048 basxconnect-0.4.7/basxconnect/contributions/locale/th/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:22.460048 basxconnect-0.4.7/basxconnect/contributions/locale/th/LC_MESSAGES/
+-rw-r--r--   0 runner    (1001) docker     (121)     7308 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/contributions/locale/th/LC_MESSAGES/django.po
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:22.460048 basxconnect-0.4.7/basxconnect/contributions/migrations/
+-rw-r--r--   0 runner    (1001) docker     (121)    14479 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/contributions/migrations/0001_initial.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16506 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/contributions/migrations/0002_alter_contribution_currency.py
+-rw-r--r--   0 runner    (1001) docker     (121)      659 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/contributions/migrations/0003_alter_contribution__import.py
+-rw-r--r--   0 runner    (1001) docker     (121)      745 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/contributions/migrations/0004_auto_20211030_0955.py
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/contributions/migrations/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2923 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/contributions/models.py
+-rw-r--r--   0 runner    (1001) docker     (121)      437 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/contributions/settings.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1842 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/contributions/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:22.460048 basxconnect-0.4.7/basxconnect/contributions/wizards/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/contributions/wizards/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12132 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/contributions/wizards/contributionsimport.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:22.460048 basxconnect-0.4.7/basxconnect/core/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1878 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/apps.py
+-rw-r--r--   0 runner    (1001) docker     (121)      469 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/context_processors.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2007 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/dynamic_preferences_registry.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:22.460048 basxconnect-0.4.7/basxconnect/core/fixtures/
+-rw-r--r--   0 runner    (1001) docker     (121)     6176 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/fixtures/base.de.json
+-rw-r--r--   0 runner    (1001) docker     (121)     5718 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/fixtures/base.en.json
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:22.460048 basxconnect-0.4.7/basxconnect/core/layouts/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/layouts/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:22.460048 basxconnect-0.4.7/basxconnect/core/layouts/editperson/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/layouts/editperson/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:22.460048 basxconnect-0.4.7/basxconnect/core/layouts/editperson/common/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/layouts/editperson/common/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9361 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/layouts/editperson/common/addresses.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1529 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/layouts/editperson/common/base_data.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1762 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/layouts/editperson/common/contributions_tab.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1183 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/layouts/editperson/common/documenttemplates_tab.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1836 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/layouts/editperson/common/head.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4996 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/layouts/editperson/common/history_tab.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4817 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/layouts/editperson/common/relationships_tab.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4394 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/layouts/editperson/common/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:22.468048 basxconnect-0.4.7/basxconnect/core/layouts/editperson/legalperson/
+-rw-r--r--   0 runner    (1001) docker     (121)       68 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/layouts/editperson/legalperson/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1125 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/layouts/editperson/legalperson/base_data_tab.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1186 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/layouts/editperson/legalperson/mailing.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:22.472048 basxconnect-0.4.7/basxconnect/core/layouts/editperson/naturalperson/
+-rw-r--r--   0 runner    (1001) docker     (121)       68 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/layouts/editperson/naturalperson/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2075 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/layouts/editperson/naturalperson/base_data_tab.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1265 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/layouts/editperson/naturalperson/mailing.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:22.472048 basxconnect-0.4.7/basxconnect/core/layouts/editperson/personassociation/
+-rw-r--r--   0 runner    (1001) docker     (121)       68 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/layouts/editperson/personassociation/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1024 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/layouts/editperson/personassociation/base_data_tab.py
+-rw-r--r--   0 runner    (1001) docker     (121)      686 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/layouts/editperson/personassociation/mailing.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4994 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/layouts/settings_layout.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:22.452048 basxconnect-0.4.7/basxconnect/core/locale/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:22.452048 basxconnect-0.4.7/basxconnect/core/locale/de/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:22.472048 basxconnect-0.4.7/basxconnect/core/locale/de/LC_MESSAGES/
+-rw-r--r--   0 runner    (1001) docker     (121)    23605 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/locale/de/LC_MESSAGES/django.po
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:22.452048 basxconnect-0.4.7/basxconnect/core/locale/fr/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:22.472048 basxconnect-0.4.7/basxconnect/core/locale/fr/LC_MESSAGES/
+-rw-r--r--   0 runner    (1001) docker     (121)    25765 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/locale/fr/LC_MESSAGES/django.po
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:22.452048 basxconnect-0.4.7/basxconnect/core/locale/nb_NO/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:22.472048 basxconnect-0.4.7/basxconnect/core/locale/nb_NO/LC_MESSAGES/
+-rw-r--r--   0 runner    (1001) docker     (121)    24305 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/locale/nb_NO/LC_MESSAGES/django.po
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:22.452048 basxconnect-0.4.7/basxconnect/core/locale/pt/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:22.472048 basxconnect-0.4.7/basxconnect/core/locale/pt/LC_MESSAGES/
+-rw-r--r--   0 runner    (1001) docker     (121)    25863 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/locale/pt/LC_MESSAGES/django.po
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:22.452048 basxconnect-0.4.7/basxconnect/core/locale/th/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:22.472048 basxconnect-0.4.7/basxconnect/core/locale/th/LC_MESSAGES/
+-rw-r--r--   0 runner    (1001) docker     (121)    32017 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/locale/th/LC_MESSAGES/django.po
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:22.480048 basxconnect-0.4.7/basxconnect/core/migrations/
+-rw-r--r--   0 runner    (1001) docker     (121)  2061155 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/migrations/0001_initial.py
+-rw-r--r--   0 runner    (1001) docker     (121)      507 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/migrations/0002_auto_20210309_1750.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2253 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/migrations/0003_auto_20210309_2221.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1734 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/migrations/0004_auto_20210311_1851.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1158 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/migrations/0005_auto_20210311_1851.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1094 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/migrations/0006_auto_20210312_0016.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2152 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/migrations/0007_auto_20210312_0054.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1398 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/migrations/0008_auto_20210323_1456.py
+-rw-r--r--   0 runner    (1001) docker     (121)      877 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/migrations/0009_auto_20210522_1817.py
+-rw-r--r--   0 runner    (1001) docker     (121)      682 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/migrations/0010_auto_20210523_1140.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2036 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/migrations/0011_auto_20210726_2047.py
+-rw-r--r--   0 runner    (1001) docker     (121)      740 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/migrations/0012_auto_20210928_1158.py
+-rw-r--r--   0 runner    (1001) docker     (121)      589 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/migrations/0013_auto_20210928_1445.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10895 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/migrations/0014_auto_20210928_1512.py
+-rw-r--r--   0 runner    (1001) docker     (121)      862 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/migrations/0015_rename_category_to_tag.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1136 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/migrations/0016_auto_20210928_1534.py
+-rw-r--r--   0 runner    (1001) docker     (121)      329 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/migrations/0017_remove_person_categories.py
+-rw-r--r--   0 runner    (1001) docker     (121)      951 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/migrations/0018_term_slug.py
+-rw-r--r--   0 runner    (1001) docker     (121)      447 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/migrations/0019_alter_term_slug.py
+-rw-r--r--   0 runner    (1001) docker     (121)      603 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/migrations/0020_auto_20211005_1630.py
+-rw-r--r--   0 runner    (1001) docker     (121)      527 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/migrations/0021_auto_20211007_0932.py
+-rw-r--r--   0 runner    (1001) docker     (121)      729 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/migrations/0022_auto_20211018_1644.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3881 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/migrations/0023_auto_20211030_0955.py
+-rw-r--r--   0 runner    (1001) docker     (121)      413 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/migrations/0024_alter_term_slug.py
+-rw-r--r--   0 runner    (1001) docker     (121)      453 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/migrations/0025_alter_term_slug.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2129 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/migrations/0026_auto_20211216_0946.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4295 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/migrations/0027_auto_20211223_1948.py
+-rw-r--r--   0 runner    (1001) docker     (121)      503 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/migrations/0028_auto_20220404_1058.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2244 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/migrations/0029_auto_20220429_1138.py
+-rw-r--r--   0 runner    (1001) docker     (121)      721 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/migrations/0030_auto_20220602_1434.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3106 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/migrations/0031_alter_email_person_alter_email_type_alter_fax_person_and_more.py
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/migrations/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:22.480048 basxconnect-0.4.7/basxconnect/core/models/
+-rw-r--r--   0 runner    (1001) docker     (121)      130 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/models/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4337 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/models/addresses.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12893 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/models/persons.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1676 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/models/relationships.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2137 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/models/utils.py
+-rw-r--r--   0 runner    (1001) docker     (121)      623 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/search_indexes.py
+-rw-r--r--   0 runner    (1001) docker     (121)      487 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/settings.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:22.480048 basxconnect-0.4.7/basxconnect/core/static/
+-rw-r--r--   0 runner    (1001) docker     (121)     3558 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/static/logo.png
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:22.480048 basxconnect-0.4.7/basxconnect/core/tests/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/tests/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1174 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/tests/settings.py
+-rw-r--r--   0 runner    (1001) docker     (121)      676 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/tests/test_person.py
+-rw-r--r--   0 runner    (1001) docker     (121)      168 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/tests/urls.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7539 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:22.480048 basxconnect-0.4.7/basxconnect/core/views/
+-rw-r--r--   0 runner    (1001) docker     (121)      187 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/views/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1878 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/views/menu_views.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:22.480048 basxconnect-0.4.7/basxconnect/core/views/person/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/views/person/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19672 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/views/person/person_browse_views.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7446 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/views/person/person_details_views.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8560 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/views/person/person_modals_views.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3054 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/views/person/search_person_view.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2224 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/views/relationship_views.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1457 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/views/settings_views.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4532 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/views/tag_views.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1276 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/views/term.py
+-rw-r--r--   0 runner    (1001) docker     (121)      502 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/views/vocabulary.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:22.480048 basxconnect-0.4.7/basxconnect/core/wizards/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/wizards/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13732 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/core/wizards/add_person.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:22.484048 basxconnect-0.4.7/basxconnect/mailer_integration/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/mailer_integration/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:22.484048 basxconnect-0.4.7/basxconnect/mailer_integration/abstract/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/mailer_integration/abstract/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2160 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/mailer_integration/abstract/mailer.py
+-rw-r--r--   0 runner    (1001) docker     (121)      271 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/mailer_integration/apps.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1813 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/mailer_integration/dynamic_preferences_registry.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1526 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/mailer_integration/help.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5751 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/mailer_integration/layouts.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:22.452048 basxconnect-0.4.7/basxconnect/mailer_integration/locale/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:22.452048 basxconnect-0.4.7/basxconnect/mailer_integration/locale/de/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:22.484048 basxconnect-0.4.7/basxconnect/mailer_integration/locale/de/LC_MESSAGES/
+-rw-r--r--   0 runner    (1001) docker     (121)     6512 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/mailer_integration/locale/de/LC_MESSAGES/django.po
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:22.452048 basxconnect-0.4.7/basxconnect/mailer_integration/locale/fr/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:22.484048 basxconnect-0.4.7/basxconnect/mailer_integration/locale/fr/LC_MESSAGES/
+-rw-r--r--   0 runner    (1001) docker     (121)     5619 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/mailer_integration/locale/fr/LC_MESSAGES/django.po
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:22.452048 basxconnect-0.4.7/basxconnect/mailer_integration/locale/nb_NO/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:22.484048 basxconnect-0.4.7/basxconnect/mailer_integration/locale/nb_NO/LC_MESSAGES/
+-rw-r--r--   0 runner    (1001) docker     (121)     5573 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/mailer_integration/locale/nb_NO/LC_MESSAGES/django.po
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:22.452048 basxconnect-0.4.7/basxconnect/mailer_integration/locale/pt/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:22.484048 basxconnect-0.4.7/basxconnect/mailer_integration/locale/pt/LC_MESSAGES/
+-rw-r--r--   0 runner    (1001) docker     (121)     5620 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/mailer_integration/locale/pt/LC_MESSAGES/django.po
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:22.452048 basxconnect-0.4.7/basxconnect/mailer_integration/locale/th/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:22.484048 basxconnect-0.4.7/basxconnect/mailer_integration/locale/th/LC_MESSAGES/
+-rw-r--r--   0 runner    (1001) docker     (121)     7182 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/mailer_integration/locale/th/LC_MESSAGES/django.po
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:22.484048 basxconnect-0.4.7/basxconnect/mailer_integration/mailchimp/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/mailer_integration/mailchimp/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5344 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/mailer_integration/mailchimp/mailer.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3179 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/mailer_integration/mailchimp/parsing.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:22.488048 basxconnect-0.4.7/basxconnect/mailer_integration/migrations/
+-rw-r--r--   0 runner    (1001) docker     (121)     1542 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/mailer_integration/migrations/0001_initial.py
+-rw-r--r--   0 runner    (1001) docker     (121)      454 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/mailer_integration/migrations/0002_interest_external_id.py
+-rw-r--r--   0 runner    (1001) docker     (121)      406 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/mailer_integration/migrations/0003_alter_interest_external_id.py
+-rw-r--r--   0 runner    (1001) docker     (121)      772 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/mailer_integration/migrations/0004_auto_20210823_1424.py
+-rw-r--r--   0 runner    (1001) docker     (121)      567 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/mailer_integration/migrations/0005_alter_mailingpreferences_email.py
+-rw-r--r--   0 runner    (1001) docker     (121)      703 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/mailer_integration/migrations/0006_alter_mailingpreferences_status.py
+-rw-r--r--   0 runner    (1001) docker     (121)      462 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/mailer_integration/migrations/0007_alter_mailingpreferences_interests.py
+-rw-r--r--   0 runner    (1001) docker     (121)      595 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/mailer_integration/migrations/0008_alter_mailingpreferences_email.py
+-rw-r--r--   0 runner    (1001) docker     (121)      579 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/mailer_integration/migrations/0009_alter_mailingpreferences_email.py
+-rw-r--r--   0 runner    (1001) docker     (121)   338886 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/mailer_integration/migrations/0010_mailingpreferences_language.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2457 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/mailer_integration/migrations/0011_invalidperson_newperson_synchronizationresult.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2031 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/mailer_integration/migrations/0012_auto_20211119_0830.py
+-rw-r--r--   0 runner    (1001) docker     (121)      656 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/mailer_integration/migrations/0013_mailingpreferences_latest_sync.py
+-rw-r--r--   0 runner    (1001) docker     (121)      416 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/mailer_integration/migrations/0014_rename_mailingpreferences_subscription.py
+-rw-r--r--   0 runner    (1001) docker     (121)      468 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/mailer_integration/migrations/0015_synchronizationperson_message.py
+-rw-r--r--   0 runner    (1001) docker     (121)      377 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/mailer_integration/migrations/0016_remove_synchronizationperson_successfully_added.py
+-rw-r--r--   0 runner    (1001) docker     (121)      933 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/mailer_integration/migrations/0017_auto_20211122_1219.py
+-rw-r--r--   0 runner    (1001) docker     (121)      790 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/mailer_integration/migrations/0018_alter_synchronizationperson_sync_status.py
+-rw-r--r--   0 runner    (1001) docker     (121)      753 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/mailer_integration/migrations/0019_auto_20211210_1602.py
+-rw-r--r--   0 runner    (1001) docker     (121)      487 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/mailer_integration/migrations/0020_subscription_deleted.py
+-rw-r--r--   0 runner    (1001) docker     (121)      597 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/mailer_integration/migrations/0021_auto_20220106_0917.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1323 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/mailer_integration/migrations/0022_auto_20220118_1308.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1406 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/mailer_integration/migrations/0023_auto_20220517_1700.py
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/mailer_integration/migrations/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3152 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/mailer_integration/models.py
+-rw-r--r--   0 runner    (1001) docker     (121)       92 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/mailer_integration/settings.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1398 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/mailer_integration/signal_handlers.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5704 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/mailer_integration/synchronize.py
+-rw-r--r--   0 runner    (1001) docker     (121)      748 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/mailer_integration/urls.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6373 2022-07-24 08:58:00.000000 basxconnect-0.4.7/basxconnect/mailer_integration/views.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-24 08:58:22.456048 basxconnect-0.4.7/basxconnect.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (121)     3421 2022-07-24 08:58:22.000000 basxconnect-0.4.7/basxconnect.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)     8804 2022-07-24 08:58:22.000000 basxconnect-0.4.7/basxconnect.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-07-24 08:58:22.000000 basxconnect-0.4.7/basxconnect.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-07-24 08:58:22.000000 basxconnect-0.4.7/basxconnect.egg-info/not-zip-safe
+-rw-r--r--   0 runner    (1001) docker     (121)      147 2022-07-24 08:58:22.000000 basxconnect-0.4.7/basxconnect.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       12 2022-07-24 08:58:22.000000 basxconnect-0.4.7/basxconnect.egg-info/top_level.txt
+-rwxr-xr-x   0 runner    (1001) docker     (121)      968 2022-07-24 08:58:00.000000 basxconnect-0.4.7/manage.py
+-rw-r--r--   0 runner    (1001) docker     (121)       38 2022-07-24 08:58:22.488048 basxconnect-0.4.7/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (121)     1449 2022-07-24 08:58:00.000000 basxconnect-0.4.7/setup.py
```

### Comparing `basxconnect-0.4.6/.github/ISSUE_TEMPLATE/bug_report.md` & `basxconnect-0.4.7/.github/ISSUE_TEMPLATE/bug_report.md`

 * *Files identical despite different names*

### Comparing `basxconnect-0.4.6/.github/ISSUE_TEMPLATE/feature_request.md` & `basxconnect-0.4.7/.github/ISSUE_TEMPLATE/feature_request.md`

 * *Files identical despite different names*

### Comparing `basxconnect-0.4.6/.github/workflows/automated_release.yml` & `basxconnect-0.4.7/.github/workflows/automated_release.yml`

 * *Files identical despite different names*

### Comparing `basxconnect-0.4.6/.github/workflows/main.yml` & `basxconnect-0.4.7/.github/workflows/main.yml`

 * *Files identical despite different names*

### Comparing `basxconnect-0.4.6/LICENSE` & `basxconnect-0.4.7/LICENSE`

 * *Files identical despite different names*

### Comparing `basxconnect-0.4.6/Makefile` & `basxconnect-0.4.7/Makefile`

 * *Files identical despite different names*

### Comparing `basxconnect-0.4.6/PKG-INFO` & `basxconnect-0.4.7/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: basxconnect
-Version: 0.4.6
+Version: 0.4.7
 Summary: CRM application for non-profit organizations
 Home-page: https://github.com/basxsoftwareassociation/basxconnect
 Author: basx Software Association
 Author-email: sam@basx.dev
 License: New BSD License
 Platform: UNKNOWN
 Classifier: Development Status :: 4 - Beta
```

### Comparing `basxconnect-0.4.6/README.md` & `basxconnect-0.4.7/README.md`

 * *Files identical despite different names*

### Comparing `basxconnect-0.4.6/basxconnect/contributions/dynamic_preferences_registry.py` & `basxconnect-0.4.7/basxconnect/contributions/dynamic_preferences_registry.py`

 * *Files identical despite different names*

### Comparing `basxconnect-0.4.6/basxconnect/contributions/locale/de/LC_MESSAGES/django.po` & `basxconnect-0.4.7/basxconnect/contributions/locale/de/LC_MESSAGES/django.po`

 * *Files 1% similar despite different names*

```diff
@@ -4,15 +4,15 @@
 # FIRST AUTHOR <EMAIL@ADDRESS>, YEAR.
 #
 #, fuzzy
 msgid ""
 msgstr ""
 "Project-Id-Version: PACKAGE VERSION\n"
 "Report-Msgid-Bugs-To: \n"
-"POT-Creation-Date: 2022-06-02 14:49+0700\n"
+"POT-Creation-Date: 2022-07-24 15:47+0700\n"
 "PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE\n"
 "Last-Translator: FULL NAME <EMAIL@ADDRESS>\n"
 "Language-Team: LANGUAGE <LL@li.org>\n"
 "Language: \n"
 "MIME-Version: 1.0\n"
 "Content-Type: text/plain; charset=UTF-8\n"
 "Content-Transfer-Encoding: 8bit\n"
```

### Comparing `basxconnect-0.4.6/basxconnect/contributions/locale/fr/LC_MESSAGES/django.po` & `basxconnect-0.4.7/basxconnect/contributions/locale/fr/LC_MESSAGES/django.po`

 * *Files 1% similar despite different names*

```diff
@@ -3,15 +3,15 @@
 # This file is distributed under the same license as the PACKAGE package.
 # FIRST AUTHOR <EMAIL@ADDRESS>, YEAR.
 #
 msgid ""
 msgstr ""
 "Project-Id-Version: PACKAGE VERSION\n"
 "Report-Msgid-Bugs-To: \n"
-"POT-Creation-Date: 2022-06-02 14:49+0700\n"
+"POT-Creation-Date: 2022-07-24 15:47+0700\n"
 "PO-Revision-Date: 2021-03-25 02:49+0000\n"
 "Last-Translator: Nathan <bonnemainsnathan@gmail.com>\n"
 "Language-Team: French <https://hosted.weblate.org/projects/basxconnect/"
 "basxconnect-contributions/fr/>\n"
 "Language: fr\n"
 "MIME-Version: 1.0\n"
 "Content-Type: text/plain; charset=UTF-8\n"
```

### Comparing `basxconnect-0.4.6/basxconnect/contributions/locale/nb_NO/LC_MESSAGES/django.po` & `basxconnect-0.4.7/basxconnect/contributions/locale/nb_NO/LC_MESSAGES/django.po`

 * *Files 1% similar despite different names*

```diff
@@ -3,15 +3,15 @@
 # This file is distributed under the same license as the PACKAGE package.
 # FIRST AUTHOR <EMAIL@ADDRESS>, YEAR.
 #
 msgid ""
 msgstr ""
 "Project-Id-Version: PACKAGE VERSION\n"
 "Report-Msgid-Bugs-To: \n"
-"POT-Creation-Date: 2022-06-02 14:49+0700\n"
+"POT-Creation-Date: 2022-07-24 15:47+0700\n"
 "PO-Revision-Date: 2021-07-29 21:32+0000\n"
 "Last-Translator: Allan Nordhøy <epost@anotheragency.no>\n"
 "Language-Team: Norwegian Bokmål <https://hosted.weblate.org/projects/"
 "basxconnect/basxconnect-contributions/nb_NO/>\n"
 "Language: nb_NO\n"
 "MIME-Version: 1.0\n"
 "Content-Type: text/plain; charset=UTF-8\n"
```

### Comparing `basxconnect-0.4.6/basxconnect/contributions/locale/pt/LC_MESSAGES/django.po` & `basxconnect-0.4.7/basxconnect/contributions/locale/pt/LC_MESSAGES/django.po`

 * *Files 0% similar despite different names*

```diff
@@ -3,15 +3,15 @@
 # This file is distributed under the same license as the PACKAGE package.
 # FIRST AUTHOR <EMAIL@ADDRESS>, YEAR.
 #
 msgid ""
 msgstr ""
 "Project-Id-Version: PACKAGE VERSION\n"
 "Report-Msgid-Bugs-To: \n"
-"POT-Creation-Date: 2022-06-02 14:49+0700\n"
+"POT-Creation-Date: 2022-07-24 15:47+0700\n"
 "PO-Revision-Date: 2021-05-08 22:32+0000\n"
 "Last-Translator: ssantos <ssantos@web.de>\n"
 "Language-Team: Portuguese <https://hosted.weblate.org/projects/basxconnect/"
 "basxconnect-contributions/pt/>\n"
 "Language: pt\n"
 "MIME-Version: 1.0\n"
 "Content-Type: text/plain; charset=UTF-8\n"
```

### Comparing `basxconnect-0.4.6/basxconnect/contributions/locale/th/LC_MESSAGES/django.po` & `basxconnect-0.4.7/basxconnect/contributions/locale/th/LC_MESSAGES/django.po`

 * *Files 1% similar despite different names*

```diff
@@ -3,15 +3,15 @@
 # This file is distributed under the same license as the PACKAGE package.
 # FIRST AUTHOR <EMAIL@ADDRESS>, YEAR.
 #
 msgid ""
 msgstr ""
 "Project-Id-Version: PACKAGE VERSION\n"
 "Report-Msgid-Bugs-To: \n"
-"POT-Creation-Date: 2022-06-02 14:49+0700\n"
+"POT-Creation-Date: 2022-07-24 15:47+0700\n"
 "PO-Revision-Date: 2021-10-20 02:32+0000\n"
 "Last-Translator: Tidaphan <tida@basx.dev>\n"
 "Language-Team: Thai <https://hosted.weblate.org/projects/basxconnect/"
 "basxconnect-contributions/th/>\n"
 "Language: th\n"
 "MIME-Version: 1.0\n"
 "Content-Type: text/plain; charset=UTF-8\n"
```

### Comparing `basxconnect-0.4.6/basxconnect/contributions/migrations/0001_initial.py` & `basxconnect-0.4.7/basxconnect/contributions/migrations/0001_initial.py`

 * *Files identical despite different names*

### Comparing `basxconnect-0.4.6/basxconnect/contributions/migrations/0002_alter_contribution_currency.py` & `basxconnect-0.4.7/basxconnect/contributions/migrations/0002_alter_contribution_currency.py`

 * *Files identical despite different names*

### Comparing `basxconnect-0.4.6/basxconnect/contributions/migrations/0003_alter_contribution__import.py` & `basxconnect-0.4.7/basxconnect/contributions/migrations/0003_alter_contribution__import.py`

 * *Files identical despite different names*

### Comparing `basxconnect-0.4.6/basxconnect/contributions/migrations/0004_auto_20211030_0955.py` & `basxconnect-0.4.7/basxconnect/contributions/migrations/0004_auto_20211030_0955.py`

 * *Files identical despite different names*

### Comparing `basxconnect-0.4.6/basxconnect/contributions/models.py` & `basxconnect-0.4.7/basxconnect/contributions/models.py`

 * *Files identical despite different names*

### Comparing `basxconnect-0.4.6/basxconnect/contributions/urls.py` & `basxconnect-0.4.7/basxconnect/contributions/urls.py`

 * *Files 5% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 import htmlgenerator as hg
-from bread import layout, menu, views
-from bread.formatters import format_value
-from bread.utils.links import Link, ModelHref
-from bread.utils.urls import autopath, default_model_paths, model_urlname, reverse
+from basxbread import layout, menu, views
+from basxbread.formatters import format_value
+from basxbread.utils.links import Link, ModelHref
+from basxbread.utils.urls import autopath, default_model_paths, model_urlname, reverse
 from django.utils.translation import gettext_lazy as _
 from django.views.generic import RedirectView
 
 from . import models
 from .wizards.contributionsimport import ContributionsImportWizard
 
 urlpatterns = [
```

### Comparing `basxconnect-0.4.6/basxconnect/contributions/wizards/contributionsimport.py` & `basxconnect-0.4.7/basxconnect/contributions/wizards/contributionsimport.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,17 +1,17 @@
 import csv
 import os
 import traceback
 
 import chardet
 import dateparser
 import htmlgenerator as hg
-from bread import layout as _layout
-from bread.utils.urls import reverse_model
-from bread.views import BreadView, generate_wizard_form
+from basxbread import layout as _layout
+from basxbread.utils.urls import reverse_model
+from basxbread.views import BaseView, generate_wizard_form
 from django import forms
 from django.conf import settings
 from django.contrib import messages
 from django.contrib.auth.mixins import PermissionRequiredMixin
 from django.core.exceptions import ValidationError
 from django.core.files.storage import FileSystemStorage
 from django.shortcuts import redirect
@@ -238,28 +238,28 @@
     )
 
 
 # The WizardView contains mostly control-flow logic and some configuration
 
 
 class ContributionsImportWizard(
-    PermissionRequiredMixin, BreadView, NamedUrlSessionWizardView
+    PermissionRequiredMixin, BaseView, NamedUrlSessionWizardView
 ):
     initial_dict = {"upload_file": {"delimiter": ";"}}
     urlparams = (("step", str),)
     file_storage = FileSystemStorage(
         location=os.path.join(settings.MEDIA_ROOT, "wizards")
     )
     permission_required = "contributions.add_contributionimport"
 
     form_list = [
         ("upload_file", UploadForm),
         ("assignment", AssignmentForm),
     ]
-    template_name = "bread/base.html"
+    template_name = ""
 
     def get_context_data(self, *args, **kwargs):
         context = super().get_context_data(*args, **kwargs)
 
         upload_file = self.get_cleaned_data_for_step("upload_file")
         context["contributions"] = ()
         if upload_file:
```

### Comparing `basxconnect-0.4.6/basxconnect/core/apps.py` & `basxconnect-0.4.7/basxconnect/core/apps.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 from datetime import timedelta
 
-from bread.utils.celery import RepeatedTask
+from basxbread.utils.celery import RepeatedTask
 from celery import shared_task
 from django.apps import AppConfig
 from django.utils.timezone import now
 from django.utils.translation import gettext_lazy as _
 
 
 class CoreConfig(AppConfig):
```

### Comparing `basxconnect-0.4.6/basxconnect/core/dynamic_preferences_registry.py` & `basxconnect-0.4.7/basxconnect/core/dynamic_preferences_registry.py`

 * *Files identical despite different names*

### Comparing `basxconnect-0.4.6/basxconnect/core/fixtures/base.de.json` & `basxconnect-0.4.7/basxconnect/core/fixtures/base.de.json`

 * *Files identical despite different names*

### Comparing `basxconnect-0.4.6/basxconnect/core/fixtures/base.en.json` & `basxconnect-0.4.7/basxconnect/core/fixtures/base.en.json`

 * *Files identical despite different names*

### Comparing `basxconnect-0.4.6/basxconnect/core/layouts/editperson/common/addresses.py` & `basxconnect-0.4.7/basxconnect/core/layouts/editperson/common/addresses.py`

 * *Files 3% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import django.db.models
 import htmlgenerator as hg
-from bread import layout
-from bread.layout import ObjectFieldValue
-from bread.layout.components.datatable import DataTableColumn
-from bread.layout.components.icon import Icon
-from bread.layout.components.modal import modal_with_trigger
-from bread.utils import Link, ModelHref, pretty_modelname, reverse_model
+from basxbread import layout
+from basxbread.layout import ObjectFieldValue
+from basxbread.layout.components.datatable import DataTableColumn
+from basxbread.layout.components.icon import Icon
+from basxbread.layout.components.modal import modal_with_trigger
+from basxbread.utils import Link, ModelHref, reverse_model
 from django.utils import timezone
 from django.utils.translation import gettext_lazy as _
 from htmlgenerator import mark_safe
 
 from basxconnect.core import models
 from basxconnect.core.layouts.editperson.common.utils import tile_with_icon, tiling_col
 
@@ -113,15 +113,15 @@
         hg.F(lambda c: c["object"].core_web_list.all()),
         ["type", "url"],
         request,
     )
 
 
 def edit_heading(model: type):
-    return _("Edit %s") % pretty_modelname(model)
+    return _("Edit %s") % model._meta.verbose_name
 
 
 def display_postal():
     postal = hg.C("i")
     modal = layout.modal.Modal.with_ajax_content(
         heading=edit_heading(models.Postal),
         url=ModelHref(
```

### Comparing `basxconnect-0.4.6/basxconnect/core/layouts/editperson/common/base_data.py` & `basxconnect-0.4.7/basxconnect/core/layouts/editperson/common/base_data.py`

 * *Files 7% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 import htmlgenerator as hg
-from bread import layout
-from bread.layout import ObjectFieldLabel, ObjectFieldValue
-from bread.layout.components.icon import Icon
-from bread.layout.components.tag import Tag
+from basxbread import layout
+from basxbread.layout import ObjectFieldLabel, ObjectFieldValue
+from basxbread.layout.components.icon import Icon
+from basxbread.layout.components.tag import Tag
 from django.utils.translation import gettext_lazy as _
 
 from basxconnect.core.layouts.editperson.common import addresses, utils
 from basxconnect.core.layouts.editperson.common.utils import (
     open_modal_popup_button,
     tile_with_icon,
 )
```

### Comparing `basxconnect-0.4.6/basxconnect/core/layouts/editperson/common/contributions_tab.py` & `basxconnect-0.4.7/basxconnect/core/layouts/editperson/common/contributions_tab.py`

 * *Files 11% similar despite different names*

```diff
@@ -1,9 +1,9 @@
-from bread import layout
-from bread.utils import Link, ModelHref, pretty_modelname
+from basxbread import layout
+from basxbread.utils import Link, ModelHref
 from django.shortcuts import get_object_or_404
 from django.utils.translation import gettext_lazy as _
 
 from basxconnect.contributions.models import Contribution
 from basxconnect.core.layouts.editperson.common import utils
 from basxconnect.core.models import Person
 
@@ -30,15 +30,15 @@
                         ],
                         title="",
                         primary_button=layout.button.Button.from_link(
                             Link(
                                 href=ModelHref(
                                     Contribution, "add", query={"person": person.id}
                                 ),
-                                label=_("Add %s") % pretty_modelname(Contribution),
+                                label=_("Add %s") % Contribution._meta.verbose_name,
                             ),
                             icon=layout.icon.Icon("add", size=20),
                         ),
                         backurl=request.get_full_path(),
                         prevent_automatic_sortingnames=True,
                     )
                 )
```

### Comparing `basxconnect-0.4.6/basxconnect/core/layouts/editperson/common/head.py` & `basxconnect-0.4.7/basxconnect/core/layouts/editperson/common/head.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 import htmlgenerator as hg
-from bread import layout
+from basxbread import layout
 from django.utils.translation import gettext_lazy as _
 
 R = layout.grid.Row
 C = layout.grid.Col
 
 
 def editperson_toolbar(request):
```

### Comparing `basxconnect-0.4.6/basxconnect/core/layouts/editperson/common/relationships_tab.py` & `basxconnect-0.4.7/basxconnect/core/layouts/editperson/common/relationships_tab.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 from typing import Callable
 
 import htmlgenerator as hg
-from bread import layout
-from bread.layout.components.datatable import DataTableColumn
-from bread.utils import Link, ModelHref, reverse_model
+from basxbread import layout
+from basxbread.layout.components.datatable import DataTableColumn
+from basxbread.utils import Link, ModelHref, reverse_model
 from django.shortcuts import get_object_or_404
 from django.utils.translation import gettext_lazy as _
 
 from basxconnect.core.layouts.editperson.common import utils
 from basxconnect.core.models import Person, Relationship
 
 R = layout.grid.Row
```

### Comparing `basxconnect-0.4.6/basxconnect/core/layouts/editperson/common/utils.py` & `basxconnect-0.4.7/basxconnect/core/layouts/editperson/common/utils.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,16 +1,16 @@
 import collections
 from typing import List, Union
 
 import htmlgenerator as hg
-from bread import layout
-from bread.layout import ObjectFieldLabel, ObjectFieldValue
-from bread.layout.components.icon import Icon
-from bread.layout.components.modal import modal_with_trigger
-from bread.utils import ModelHref
+from basxbread import layout
+from basxbread.layout import ObjectFieldLabel, ObjectFieldValue
+from basxbread.layout.components.icon import Icon
+from basxbread.layout.components.modal import modal_with_trigger
+from basxbread.utils import ModelHref
 from django.urls import reverse_lazy
 from django.utils.translation import gettext_lazy as _
 from htmlgenerator import Lazy
 
 R = layout.grid.Row
 C = layout.grid.Col
 F = layout.forms.FormField
```

### Comparing `basxconnect-0.4.6/basxconnect/core/layouts/editperson/legalperson/base_data_tab.py` & `basxconnect-0.4.7/basxconnect/core/layouts/editperson/legalperson/base_data_tab.py`

 * *Files 12% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 import htmlgenerator as hg
-from bread import layout
-from bread.layout.components.icon import Icon
+from basxbread import layout
+from basxbread.layout.components.icon import Icon
 from django.utils.translation import gettext_lazy as _
 
 from basxconnect.core import models
 from basxconnect.core.layouts.editperson.common.base_data import common_tiles
 from basxconnect.core.layouts.editperson.common.utils import (
     grid_inside_tab,
     person_metadata,
```

### Comparing `basxconnect-0.4.6/basxconnect/core/layouts/editperson/legalperson/mailing.py` & `basxconnect-0.4.7/basxconnect/core/layouts/editperson/naturalperson/mailing.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,9 +1,9 @@
-from bread import layout
-from bread.layout.components.icon import Icon
+from basxbread import layout
+from basxbread.layout.components.icon import Icon
 from django.utils.translation import gettext_lazy as _
 
 from basxconnect.core import models
 from basxconnect.core.layouts.editperson.common.utils import (
     grid_inside_tab,
     tile_col_edit_modal,
     tiling_col,
@@ -25,20 +25,22 @@
 
     return layout.tabs.Tab(
         _("Mailings"),
         grid_inside_tab(
             R(
                 tile_col_edit_modal(
                     _("Settings"),
-                    models.LegalPerson,
+                    models.NaturalPerson,
                     "ajax_edit_mailings",
                     Icon("settings--adjust"),
                     [
                         "preferred_language",
                         "type",
                         "salutation_letter",
+                        "gender",
+                        "form_of_address",
                     ],
                 ),
                 mailer_tile,
             ),
         ),
     )
```

### Comparing `basxconnect-0.4.6/basxconnect/core/layouts/editperson/naturalperson/base_data_tab.py` & `basxconnect-0.4.7/basxconnect/core/layouts/editperson/naturalperson/base_data_tab.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 import htmlgenerator as hg
-from bread import layout
-from bread.layout import ObjectFieldLabel
-from bread.layout.components.icon import Icon
+from basxbread import layout
+from basxbread.layout import ObjectFieldLabel
+from basxbread.layout.components.icon import Icon
 from django.utils.translation import gettext_lazy as _
 
 from basxconnect.core import models
 from basxconnect.core.layouts.editperson.common import addresses, base_data, utils
 from basxconnect.core.layouts.editperson.common.utils import (
     display_label_and_value,
     person_metadata,
```

### Comparing `basxconnect-0.4.6/basxconnect/core/layouts/editperson/naturalperson/mailing.py` & `basxconnect-0.4.7/basxconnect/core/layouts/editperson/legalperson/mailing.py`

 * *Files 24% similar despite different names*

```diff
@@ -1,9 +1,9 @@
-from bread import layout
-from bread.layout.components.icon import Icon
+from basxbread import layout
+from basxbread.layout.components.icon import Icon
 from django.utils.translation import gettext_lazy as _
 
 from basxconnect.core import models
 from basxconnect.core.layouts.editperson.common.utils import (
     grid_inside_tab,
     tile_col_edit_modal,
     tiling_col,
@@ -25,22 +25,20 @@
 
     return layout.tabs.Tab(
         _("Mailings"),
         grid_inside_tab(
             R(
                 tile_col_edit_modal(
                     _("Settings"),
-                    models.NaturalPerson,
+                    models.LegalPerson,
                     "ajax_edit_mailings",
                     Icon("settings--adjust"),
                     [
                         "preferred_language",
                         "type",
                         "salutation_letter",
-                        "gender",
-                        "form_of_address",
                     ],
                 ),
                 mailer_tile,
             ),
         ),
     )
```

### Comparing `basxconnect-0.4.6/basxconnect/core/layouts/editperson/personassociation/base_data_tab.py` & `basxconnect-0.4.7/basxconnect/core/layouts/editperson/personassociation/base_data_tab.py`

 * *Files 14% similar despite different names*

```diff
@@ -1,9 +1,9 @@
-from bread import layout
-from bread.layout.components.icon import Icon
+from basxbread import layout
+from basxbread.layout.components.icon import Icon
 from django.utils.translation import gettext_lazy as _
 
 from basxconnect.core import models
 from basxconnect.core.layouts.editperson.common import base_data
 from basxconnect.core.layouts.editperson.common.utils import (
     grid_inside_tab,
     person_metadata,
```

### Comparing `basxconnect-0.4.6/basxconnect/core/layouts/editperson/personassociation/mailing.py` & `basxconnect-0.4.7/basxconnect/core/layouts/editperson/personassociation/mailing.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-from bread import layout
+from basxbread import layout
 from django.utils.translation import gettext_lazy as _
 
 from basxconnect.core.layouts.editperson.common.utils import grid_inside_tab, tiling_col
 
 R = layout.grid.Row
```

### Comparing `basxconnect-0.4.6/basxconnect/core/layouts/settings_layout.py` & `basxconnect-0.4.7/basxconnect/core/layouts/settings_layout.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 import htmlgenerator as hg
-from bread import layout
-from bread.utils import Link, ModelHref, pretty_modelname, reverse
-from bread.views import BrowseView
+from basxbread import layout
+from basxbread.utils import Link, ModelHref, reverse
+from basxbread.views import BrowseView
 from django.utils.translation import gettext_lazy as _
 
 from basxconnect.core.models import RelationshipType, Term, Vocabulary
 
 R = layout.grid.Row
 C = layout.grid.Col
 F = layout.forms.FormField
@@ -26,15 +26,15 @@
                                 "add",
                                 query={
                                     "next": reverse(
                                         "basxconnect.core.views.settings_views.relationshipssettings"
                                     )
                                 },
                             ),
-                            label=_("Add %s") % pretty_modelname(RelationshipType),
+                            label=_("Add %s") % RelationshipType._meta.verbose_name,
                         ),
                         icon=layout.icon.Icon("add", size=20),
                     ),
                     rowactions=[
                         Link(
                             label=_("Edit"),
                             href=ModelHref(
@@ -108,15 +108,15 @@
         columns=["term"],
         title=title,
         primary_button=layout.button.Button.from_link(
             Link(
                 href=ModelHref(
                     Term, "add", query={"vocabulary": cat.id}, return_to_current=True
                 ),
-                label=_("Add %s") % pretty_modelname(Term),
+                label=_("Add %s") % Term._meta.verbose_name,
             ),
             icon=layout.icon.Icon("add", size=20),
         ),
         prevent_automatic_sortingnames=True,
         rowclickaction=BrowseView.gen_rowclickaction("edit", return_to_current=True),
         rowactions=[
             Link(
```

### Comparing `basxconnect-0.4.6/basxconnect/core/locale/de/LC_MESSAGES/django.po` & `basxconnect-0.4.7/basxconnect/core/locale/de/LC_MESSAGES/django.po`

 * *Files 1% similar despite different names*

```diff
@@ -3,15 +3,15 @@
 # This file is distributed under the same license as the basxconnect package.
 # basx GmbH <info@basx.ch>, 2020.
 #
 msgid ""
 msgstr ""
 "Project-Id-Version: PACKAGE VERSION\n"
 "Report-Msgid-Bugs-To: \n"
-"POT-Creation-Date: 2022-06-02 14:49+0700\n"
+"POT-Creation-Date: 2022-07-24 15:47+0700\n"
 "PO-Revision-Date: 2021-04-08 02:26+0000\n"
 "Last-Translator: Frederik Bugglin <bugglin@basx.ch>\n"
 "Language-Team: German <https://hosted.weblate.org/projects/basxconnect/"
 "basxconnect/de/>\n"
 "Language: de\n"
 "MIME-Version: 1.0\n"
 "Content-Type: text/plain; charset=UTF-8\n"
@@ -192,28 +192,55 @@
 #: basxconnect/core/layouts/editperson/common/contributions_tab.py:17
 msgid "Contributions"
 msgstr "Zuwendungen"
 
 #: basxconnect/core/layouts/editperson/common/contributions_tab.py:37
 #: basxconnect/core/layouts/settings_layout.py:33
 #: basxconnect/core/layouts/settings_layout.py:115
-#: basxconnect/core/views/term.py:26 basxconnect/core/wizards/add_person.py:380
+#: basxconnect/core/views/term.py:26 basxconnect/core/wizards/add_person.py:379
 #, python-format
 msgid "Add %s"
 msgstr "%s hinzufügen"
 
+#: basxconnect/core/layouts/editperson/common/documenttemplates_tab.py:19
+msgid "Documents"
+msgstr ""
+
 #: basxconnect/core/layouts/editperson/common/head.py:20
 #: basxconnect/core/views/person/person_browse_views.py:193
 msgid "Restore"
 msgstr "Wiederherstellen"
 
 #: basxconnect/core/layouts/editperson/common/head.py:33
 msgid "Copy"
 msgstr "Kopieren"
 
+#: basxconnect/core/layouts/editperson/common/history_tab.py:68
+msgid "History"
+msgstr ""
+
+#: basxconnect/core/layouts/editperson/common/history_tab.py:78
+msgid "Date"
+msgstr ""
+
+#: basxconnect/core/layouts/editperson/common/history_tab.py:84
+msgid "Time"
+msgstr ""
+
+#: basxconnect/core/layouts/editperson/common/history_tab.py:90
+msgid "User"
+msgstr ""
+
+#: basxconnect/core/layouts/editperson/common/history_tab.py:94
+#: basxconnect/core/layouts/editperson/common/history_tab.py:126
+#, fuzzy
+#| msgid "Changed"
+msgid "Changes"
+msgstr "Zuletzt geändert"
+
 #: basxconnect/core/layouts/editperson/common/relationships_tab.py:22
 #: basxconnect/core/layouts/settings_layout.py:16
 #: basxconnect/core/models/relationships.py:55
 #: basxconnect/core/views/menu_views.py:75
 msgid "Relationships"
 msgstr "Verknüpfungen"
 
@@ -318,27 +345,27 @@
 #: basxconnect/core/models/persons.py:241
 msgid "Person"
 msgstr "Person"
 
 #: basxconnect/core/models/addresses.py:30
 #: basxconnect/core/models/addresses.py:54
 #: basxconnect/core/views/person/person_browse_views.py:158
-#: basxconnect/core/wizards/add_person.py:68
+#: basxconnect/core/wizards/add_person.py:67
 msgid "Email"
 msgstr "E-Mail"
 
 #: basxconnect/core/models/addresses.py:39
 #: basxconnect/core/models/addresses.py:74
 #: basxconnect/core/models/addresses.py:93
 #: basxconnect/core/models/addresses.py:114
 #: basxconnect/core/models/addresses.py:139
 #: basxconnect/core/models/persons.py:350
 #: basxconnect/core/models/persons.py:374
 #: basxconnect/core/models/relationships.py:36
-#: basxconnect/core/wizards/add_person.py:274
+#: basxconnect/core/wizards/add_person.py:273
 msgid "Type"
 msgstr "Typ"
 
 #: basxconnect/core/models/addresses.py:60
 msgid "Email address"
 msgstr "E-Mail-Adresse"
 
@@ -380,15 +407,15 @@
 msgstr "Faxnummern"
 
 #: basxconnect/core/models/addresses.py:127
 msgid "Country"
 msgstr "Land"
 
 #: basxconnect/core/models/addresses.py:128
-#: basxconnect/core/wizards/add_person.py:47
+#: basxconnect/core/wizards/add_person.py:46
 msgid "Address"
 msgstr "Adresse"
 
 #: basxconnect/core/models/addresses.py:129
 msgid "Post Code"
 msgstr "PLZ"
 
@@ -654,14 +681,15 @@
 
 #: basxconnect/core/views/person/person_details_views.py:161
 #, python-format
 msgid "%s is %s"
 msgstr "%s ist %s"
 
 #: basxconnect/core/views/person/person_details_views.py:178
+#, python-format
 msgid "Delete linked %s subscription as well"
 msgstr "Verknüpfte Email-Abonnemente %s auch löschen"
 
 #: basxconnect/core/views/person/person_details_views.py:224
 #, python-format
 msgid "Delete email %s"
 msgstr "Email %s löschen"
@@ -688,23 +716,23 @@
 msgstr "Email Adresse auch in %s ändern"
 
 #: basxconnect/core/views/person/person_modals_views.py:250
 msgid "Edit Email"
 msgstr "E-Mail bearbeiten"
 
 #: basxconnect/core/views/person/search_person_view.py:21
-#: basxconnect/core/wizards/add_person.py:148
+#: basxconnect/core/wizards/add_person.py:147
 msgid "Search person"
 msgstr "Suche"
 
-#: basxconnect/core/views/person/search_person_view.py:63
+#: basxconnect/core/views/person/search_person_view.py:62
 msgid "No results"
 msgstr "Keine Ergebnisse gefunden"
 
-#: basxconnect/core/views/person/search_person_view.py:96
+#: basxconnect/core/views/person/search_person_view.py:95
 #, python-format
 msgid "%s items found"
 msgstr "%s Einträge gefunden"
 
 #: basxconnect/core/views/relationship_views.py:40
 msgid "Edit Relationship"
 msgstr "Beziehung editieren"
@@ -740,89 +768,89 @@
 msgid "Submit"
 msgstr "Absenden"
 
 #: basxconnect/core/views/vocabulary.py:14
 msgid "Terms of vocabulary"
 msgstr "Begriffe von Vokabular"
 
-#: basxconnect/core/wizards/add_person.py:102
+#: basxconnect/core/wizards/add_person.py:101
 msgid "Back"
 msgstr "Zurück"
 
-#: basxconnect/core/wizards/add_person.py:113
+#: basxconnect/core/wizards/add_person.py:112
 msgid "Complete"
 msgstr "Fertigstellen"
 
-#: basxconnect/core/wizards/add_person.py:116
+#: basxconnect/core/wizards/add_person.py:115
 msgid "Continue"
 msgstr "Weiter"
 
-#: basxconnect/core/wizards/add_person.py:128
+#: basxconnect/core/wizards/add_person.py:127
 msgid "Check for existing people before continuing"
 msgstr "Auf existierende Einträge prüfen bevor es weitergehen kann"
 
-#: basxconnect/core/wizards/add_person.py:136
+#: basxconnect/core/wizards/add_person.py:135
 msgid "Start typing to search for a person..."
 msgstr "Tippen um nach Personen zu suchen..."
 
-#: basxconnect/core/wizards/add_person.py:152
+#: basxconnect/core/wizards/add_person.py:151
 msgid ""
 "Before a new person can be added it must be confirmed that the person does "
 "not exists yet."
 msgstr ""
 "Bevor eine neue Person hinzugefügt wird muss überprüft werden, ob die Person "
 "nicht bereits existiert"
 
-#: basxconnect/core/wizards/add_person.py:168
+#: basxconnect/core/wizards/add_person.py:167
 msgid "Type of person"
 msgstr "Personentyp"
 
-#: basxconnect/core/wizards/add_person.py:174
+#: basxconnect/core/wizards/add_person.py:173
 msgid "Choose person main type"
 msgstr "Hauptyp auswählen"
 
-#: basxconnect/core/wizards/add_person.py:177
+#: basxconnect/core/wizards/add_person.py:176
 msgid "Please choose what type of person you want to add:"
 msgstr "Bitte den Personentyp wählen"
 
-#: basxconnect/core/wizards/add_person.py:192
+#: basxconnect/core/wizards/add_person.py:191
 msgid "Subtype of person"
 msgstr "Art der Person"
 
-#: basxconnect/core/wizards/add_person.py:208
+#: basxconnect/core/wizards/add_person.py:207
 msgid "Choose person type"
 msgstr "Bitte den Personentyp wählen"
 
-#: basxconnect/core/wizards/add_person.py:216
+#: basxconnect/core/wizards/add_person.py:215
 msgid "Add person"
 msgstr "Person hinzufügen"
 
-#: basxconnect/core/wizards/add_person.py:224
+#: basxconnect/core/wizards/add_person.py:223
 msgid "Finish"
 msgstr "Beenden"
 
-#: basxconnect/core/wizards/add_person.py:273
+#: basxconnect/core/wizards/add_person.py:272
 msgid "Search"
 msgstr "Suche"
 
-#: basxconnect/core/wizards/add_person.py:275
+#: basxconnect/core/wizards/add_person.py:274
 msgid "Subtype"
 msgstr "Art"
 
-#: basxconnect/core/wizards/add_person.py:276
+#: basxconnect/core/wizards/add_person.py:275
 msgid "Information"
 msgstr "Informationen"
 
-#: basxconnect/core/wizards/add_person.py:277
+#: basxconnect/core/wizards/add_person.py:276
 msgid "Confirmation"
 msgstr "Bestätigung"
 
-#: basxconnect/core/wizards/add_person.py:301
+#: basxconnect/core/wizards/add_person.py:300
 msgid "Add new person"
 msgstr "Neue Person hinzufügen"
 
-#: basxconnect/core/wizards/add_person.py:372
+#: basxconnect/core/wizards/add_person.py:371
 msgid "Review and confirm the entered information"
 msgstr "Überprüfen und bestätigen Sie die eingetragenen Informationen"
 
 #~ msgid "Languages"
 #~ msgstr "Sprachen"
```

### Comparing `basxconnect-0.4.6/basxconnect/core/locale/fr/LC_MESSAGES/django.po` & `basxconnect-0.4.7/basxconnect/core/locale/fr/LC_MESSAGES/django.po`

 * *Files 2% similar despite different names*

```diff
@@ -3,15 +3,15 @@
 # This file is distributed under the same license as the PACKAGE package.
 # FIRST AUTHOR <EMAIL@ADDRESS>, YEAR.
 #
 msgid ""
 msgstr ""
 "Project-Id-Version: PACKAGE VERSION\n"
 "Report-Msgid-Bugs-To: \n"
-"POT-Creation-Date: 2022-06-02 14:49+0700\n"
+"POT-Creation-Date: 2022-07-24 15:47+0700\n"
 "PO-Revision-Date: 2022-02-12 10:55+0000\n"
 "Last-Translator: Nathan <bonnemainsnathan@gmail.com>\n"
 "Language-Team: French <https://hosted.weblate.org/projects/basxconnect/"
 "basxconnect/fr/>\n"
 "Language: fr\n"
 "MIME-Version: 1.0\n"
 "Content-Type: text/plain; charset=UTF-8\n"
@@ -192,28 +192,55 @@
 #: basxconnect/core/layouts/editperson/common/contributions_tab.py:17
 msgid "Contributions"
 msgstr "Contributions"
 
 #: basxconnect/core/layouts/editperson/common/contributions_tab.py:37
 #: basxconnect/core/layouts/settings_layout.py:33
 #: basxconnect/core/layouts/settings_layout.py:115
-#: basxconnect/core/views/term.py:26 basxconnect/core/wizards/add_person.py:380
+#: basxconnect/core/views/term.py:26 basxconnect/core/wizards/add_person.py:379
 #, python-format
 msgid "Add %s"
 msgstr "Ajouter %s"
 
+#: basxconnect/core/layouts/editperson/common/documenttemplates_tab.py:19
+msgid "Documents"
+msgstr ""
+
 #: basxconnect/core/layouts/editperson/common/head.py:20
 #: basxconnect/core/views/person/person_browse_views.py:193
 msgid "Restore"
 msgstr "Restaurer"
 
 #: basxconnect/core/layouts/editperson/common/head.py:33
 msgid "Copy"
 msgstr "Copier"
 
+#: basxconnect/core/layouts/editperson/common/history_tab.py:68
+msgid "History"
+msgstr ""
+
+#: basxconnect/core/layouts/editperson/common/history_tab.py:78
+msgid "Date"
+msgstr "Date"
+
+#: basxconnect/core/layouts/editperson/common/history_tab.py:84
+msgid "Time"
+msgstr ""
+
+#: basxconnect/core/layouts/editperson/common/history_tab.py:90
+msgid "User"
+msgstr "Utilisateur"
+
+#: basxconnect/core/layouts/editperson/common/history_tab.py:94
+#: basxconnect/core/layouts/editperson/common/history_tab.py:126
+#, fuzzy
+#| msgid "Change"
+msgid "Changes"
+msgstr "Modifier"
+
 #: basxconnect/core/layouts/editperson/common/relationships_tab.py:22
 #: basxconnect/core/layouts/settings_layout.py:16
 #: basxconnect/core/models/relationships.py:55
 #: basxconnect/core/views/menu_views.py:75
 msgid "Relationships"
 msgstr "Relations"
 
@@ -322,27 +349,27 @@
 #: basxconnect/core/models/persons.py:241
 msgid "Person"
 msgstr "Personne"
 
 #: basxconnect/core/models/addresses.py:30
 #: basxconnect/core/models/addresses.py:54
 #: basxconnect/core/views/person/person_browse_views.py:158
-#: basxconnect/core/wizards/add_person.py:68
+#: basxconnect/core/wizards/add_person.py:67
 msgid "Email"
 msgstr "E-mail"
 
 #: basxconnect/core/models/addresses.py:39
 #: basxconnect/core/models/addresses.py:74
 #: basxconnect/core/models/addresses.py:93
 #: basxconnect/core/models/addresses.py:114
 #: basxconnect/core/models/addresses.py:139
 #: basxconnect/core/models/persons.py:350
 #: basxconnect/core/models/persons.py:374
 #: basxconnect/core/models/relationships.py:36
-#: basxconnect/core/wizards/add_person.py:274
+#: basxconnect/core/wizards/add_person.py:273
 msgid "Type"
 msgstr "Type"
 
 #: basxconnect/core/models/addresses.py:60
 msgid "Email address"
 msgstr "Adresse e-mail"
 
@@ -384,15 +411,15 @@
 msgstr "Numéros de télécopie"
 
 #: basxconnect/core/models/addresses.py:127
 msgid "Country"
 msgstr "Pays"
 
 #: basxconnect/core/models/addresses.py:128
-#: basxconnect/core/wizards/add_person.py:47
+#: basxconnect/core/wizards/add_person.py:46
 msgid "Address"
 msgstr "Adresse"
 
 #: basxconnect/core/models/addresses.py:129
 msgid "Post Code"
 msgstr "Code postal"
 
@@ -700,23 +727,23 @@
 msgstr "Propager les modifications d'adresse e-mail vers %s"
 
 #: basxconnect/core/views/person/person_modals_views.py:250
 msgid "Edit Email"
 msgstr "Modifier e-mail"
 
 #: basxconnect/core/views/person/search_person_view.py:21
-#: basxconnect/core/wizards/add_person.py:148
+#: basxconnect/core/wizards/add_person.py:147
 msgid "Search person"
 msgstr "Rechercher une personne"
 
-#: basxconnect/core/views/person/search_person_view.py:63
+#: basxconnect/core/views/person/search_person_view.py:62
 msgid "No results"
 msgstr "Aucun résultat"
 
-#: basxconnect/core/views/person/search_person_view.py:96
+#: basxconnect/core/views/person/search_person_view.py:95
 #, python-format
 msgid "%s items found"
 msgstr "%s éléments trouvés"
 
 #: basxconnect/core/views/relationship_views.py:40
 msgid "Edit Relationship"
 msgstr "Modifier la relation"
@@ -755,109 +782,100 @@
 
 #: basxconnect/core/views/vocabulary.py:14
 #, fuzzy
 #| msgid "Vocabulary"
 msgid "Terms of vocabulary"
 msgstr "Vocabulaire"
 
-#: basxconnect/core/wizards/add_person.py:102
+#: basxconnect/core/wizards/add_person.py:101
 msgid "Back"
 msgstr "Retour"
 
-#: basxconnect/core/wizards/add_person.py:113
+#: basxconnect/core/wizards/add_person.py:112
 msgid "Complete"
 msgstr "Terminer"
 
-#: basxconnect/core/wizards/add_person.py:116
+#: basxconnect/core/wizards/add_person.py:115
 msgid "Continue"
 msgstr "Continuer"
 
-#: basxconnect/core/wizards/add_person.py:128
+#: basxconnect/core/wizards/add_person.py:127
 msgid "Check for existing people before continuing"
 msgstr "Vérifier s'il existe des personnes avant de continuer"
 
-#: basxconnect/core/wizards/add_person.py:136
+#: basxconnect/core/wizards/add_person.py:135
 msgid "Start typing to search for a person..."
 msgstr "Commencez à taper pour rechercher une personne…"
 
-#: basxconnect/core/wizards/add_person.py:152
+#: basxconnect/core/wizards/add_person.py:151
 msgid ""
 "Before a new person can be added it must be confirmed that the person does "
 "not exists yet."
 msgstr ""
 "Avant de pouvoir ajouter une nouvelle personne, il faut confirmer qu'elle "
 "n'existe pas encore."
 
-#: basxconnect/core/wizards/add_person.py:168
+#: basxconnect/core/wizards/add_person.py:167
 msgid "Type of person"
 msgstr "Type de personne"
 
-#: basxconnect/core/wizards/add_person.py:174
+#: basxconnect/core/wizards/add_person.py:173
 msgid "Choose person main type"
 msgstr "Sélectionnez le type principal de la personne"
 
-#: basxconnect/core/wizards/add_person.py:177
+#: basxconnect/core/wizards/add_person.py:176
 msgid "Please choose what type of person you want to add:"
 msgstr "Veuillez sélectionner le type de personne que vous souhaitez ajouter :"
 
-#: basxconnect/core/wizards/add_person.py:192
+#: basxconnect/core/wizards/add_person.py:191
 msgid "Subtype of person"
 msgstr "Sous-type de personne"
 
-#: basxconnect/core/wizards/add_person.py:208
+#: basxconnect/core/wizards/add_person.py:207
 msgid "Choose person type"
 msgstr "Sélectionnez le type de personne"
 
-#: basxconnect/core/wizards/add_person.py:216
+#: basxconnect/core/wizards/add_person.py:215
 msgid "Add person"
 msgstr "Ajouter une personne"
 
-#: basxconnect/core/wizards/add_person.py:224
+#: basxconnect/core/wizards/add_person.py:223
 msgid "Finish"
 msgstr "Terminer"
 
-#: basxconnect/core/wizards/add_person.py:273
+#: basxconnect/core/wizards/add_person.py:272
 msgid "Search"
 msgstr "Rechercher"
 
-#: basxconnect/core/wizards/add_person.py:275
+#: basxconnect/core/wizards/add_person.py:274
 msgid "Subtype"
 msgstr "Sous-type"
 
-#: basxconnect/core/wizards/add_person.py:276
+#: basxconnect/core/wizards/add_person.py:275
 msgid "Information"
 msgstr "Information"
 
-#: basxconnect/core/wizards/add_person.py:277
+#: basxconnect/core/wizards/add_person.py:276
 msgid "Confirmation"
 msgstr "Confirmation"
 
-#: basxconnect/core/wizards/add_person.py:301
+#: basxconnect/core/wizards/add_person.py:300
 msgid "Add new person"
 msgstr "Ajouter une nouvelle personne"
 
-#: basxconnect/core/wizards/add_person.py:372
+#: basxconnect/core/wizards/add_person.py:371
 msgid "Review and confirm the entered information"
 msgstr "Valider et confirmer les informations saisies"
 
 #~ msgid "Languages"
 #~ msgstr "Langues"
 
 #~ msgid "Revisions"
 #~ msgstr "Révisions"
 
-#~ msgid "Date"
-#~ msgstr "Date"
-
-#~ msgid "User"
-#~ msgstr "Utilisateur"
-
-#~ msgid "Change"
-#~ msgstr "Modifier"
-
 #, fuzzy
 #~| msgid "Person category"
 #~ msgid "Person Category"
 #~ msgstr "Catégorie de personne"
 
 #~ msgid "Categories"
 #~ msgstr "Catégories"
```

### Comparing `basxconnect-0.4.6/basxconnect/core/locale/nb_NO/LC_MESSAGES/django.po` & `basxconnect-0.4.7/basxconnect/core/locale/nb_NO/LC_MESSAGES/django.po`

 * *Files 0% similar despite different names*

```diff
@@ -3,15 +3,15 @@
 # This file is distributed under the same license as the PACKAGE package.
 # FIRST AUTHOR <EMAIL@ADDRESS>, YEAR.
 #
 msgid ""
 msgstr ""
 "Project-Id-Version: PACKAGE VERSION\n"
 "Report-Msgid-Bugs-To: \n"
-"POT-Creation-Date: 2022-06-02 14:49+0700\n"
+"POT-Creation-Date: 2022-07-24 15:47+0700\n"
 "PO-Revision-Date: 2021-11-05 02:35+0000\n"
 "Last-Translator: Allan Nordhøy <epost@anotheragency.no>\n"
 "Language-Team: Norwegian Bokmål <https://hosted.weblate.org/projects/"
 "basxconnect/basxconnect/nb_NO/>\n"
 "Language: nb_NO\n"
 "MIME-Version: 1.0\n"
 "Content-Type: text/plain; charset=UTF-8\n"
@@ -220,29 +220,56 @@
 #: basxconnect/core/layouts/editperson/common/contributions_tab.py:17
 msgid "Contributions"
 msgstr "Bidragsytere"
 
 #: basxconnect/core/layouts/editperson/common/contributions_tab.py:37
 #: basxconnect/core/layouts/settings_layout.py:33
 #: basxconnect/core/layouts/settings_layout.py:115
-#: basxconnect/core/views/term.py:26 basxconnect/core/wizards/add_person.py:380
+#: basxconnect/core/views/term.py:26 basxconnect/core/wizards/add_person.py:379
 #, python-format
 msgid "Add %s"
 msgstr "Legg til %s"
 
+#: basxconnect/core/layouts/editperson/common/documenttemplates_tab.py:19
+msgid "Documents"
+msgstr ""
+
 #: basxconnect/core/layouts/editperson/common/head.py:20
 #: basxconnect/core/views/person/person_browse_views.py:193
 msgid "Restore"
 msgstr "Gjenopprett"
 
 #: basxconnect/core/layouts/editperson/common/head.py:33
 #, fuzzy
 msgid "Copy"
 msgstr "Kopier"
 
+#: basxconnect/core/layouts/editperson/common/history_tab.py:68
+msgid "History"
+msgstr ""
+
+#: basxconnect/core/layouts/editperson/common/history_tab.py:78
+msgid "Date"
+msgstr "Dato"
+
+#: basxconnect/core/layouts/editperson/common/history_tab.py:84
+msgid "Time"
+msgstr ""
+
+#: basxconnect/core/layouts/editperson/common/history_tab.py:90
+msgid "User"
+msgstr "Bruker"
+
+#: basxconnect/core/layouts/editperson/common/history_tab.py:94
+#: basxconnect/core/layouts/editperson/common/history_tab.py:126
+#, fuzzy
+#| msgid "Change"
+msgid "Changes"
+msgstr "Endre"
+
 #: basxconnect/core/layouts/editperson/common/relationships_tab.py:22
 #: basxconnect/core/layouts/settings_layout.py:16
 #: basxconnect/core/models/relationships.py:55
 #: basxconnect/core/views/menu_views.py:75
 msgid "Relationships"
 msgstr "Relasjoner"
 
@@ -365,27 +392,27 @@
 #: basxconnect/core/models/persons.py:241
 msgid "Person"
 msgstr "Person"
 
 #: basxconnect/core/models/addresses.py:30
 #: basxconnect/core/models/addresses.py:54
 #: basxconnect/core/views/person/person_browse_views.py:158
-#: basxconnect/core/wizards/add_person.py:68
+#: basxconnect/core/wizards/add_person.py:67
 msgid "Email"
 msgstr "E-post"
 
 #: basxconnect/core/models/addresses.py:39
 #: basxconnect/core/models/addresses.py:74
 #: basxconnect/core/models/addresses.py:93
 #: basxconnect/core/models/addresses.py:114
 #: basxconnect/core/models/addresses.py:139
 #: basxconnect/core/models/persons.py:350
 #: basxconnect/core/models/persons.py:374
 #: basxconnect/core/models/relationships.py:36
-#: basxconnect/core/wizards/add_person.py:274
+#: basxconnect/core/wizards/add_person.py:273
 msgid "Type"
 msgstr "Type"
 
 #: basxconnect/core/models/addresses.py:60
 msgid "Email address"
 msgstr "E-postadresse"
 
@@ -428,15 +455,15 @@
 msgstr "Faks-nummer"
 
 #: basxconnect/core/models/addresses.py:127
 msgid "Country"
 msgstr "Land"
 
 #: basxconnect/core/models/addresses.py:128
-#: basxconnect/core/wizards/add_person.py:47
+#: basxconnect/core/wizards/add_person.py:46
 msgid "Address"
 msgstr "Adresse"
 
 #: basxconnect/core/models/addresses.py:129
 msgid "Post Code"
 msgstr "Postnummer"
 
@@ -758,24 +785,24 @@
 #: basxconnect/core/views/person/person_modals_views.py:250
 #, fuzzy
 #| msgid "Email"
 msgid "Edit Email"
 msgstr "E-post"
 
 #: basxconnect/core/views/person/search_person_view.py:21
-#: basxconnect/core/wizards/add_person.py:148
+#: basxconnect/core/wizards/add_person.py:147
 #, fuzzy
 msgid "Search person"
 msgstr "Søk"
 
-#: basxconnect/core/views/person/search_person_view.py:63
+#: basxconnect/core/views/person/search_person_view.py:62
 msgid "No results"
 msgstr "Resultatløst"
 
-#: basxconnect/core/views/person/search_person_view.py:96
+#: basxconnect/core/views/person/search_person_view.py:95
 #, python-format
 msgid "%s items found"
 msgstr ""
 
 #: basxconnect/core/views/relationship_views.py:40
 #, fuzzy
 #| msgid "Relationship"
@@ -817,109 +844,100 @@
 msgid "Submit"
 msgstr ""
 
 #: basxconnect/core/views/vocabulary.py:14
 msgid "Terms of vocabulary"
 msgstr ""
 
-#: basxconnect/core/wizards/add_person.py:102
+#: basxconnect/core/wizards/add_person.py:101
 msgid "Back"
 msgstr "Tilbake"
 
-#: basxconnect/core/wizards/add_person.py:113
+#: basxconnect/core/wizards/add_person.py:112
 #, fuzzy
 msgid "Complete"
 msgstr "Fullført"
 
-#: basxconnect/core/wizards/add_person.py:116
+#: basxconnect/core/wizards/add_person.py:115
 msgid "Continue"
 msgstr "Fortsett"
 
-#: basxconnect/core/wizards/add_person.py:128
+#: basxconnect/core/wizards/add_person.py:127
 msgid "Check for existing people before continuing"
 msgstr ""
 
-#: basxconnect/core/wizards/add_person.py:136
+#: basxconnect/core/wizards/add_person.py:135
 msgid "Start typing to search for a person..."
 msgstr ""
 
-#: basxconnect/core/wizards/add_person.py:152
+#: basxconnect/core/wizards/add_person.py:151
 msgid ""
 "Before a new person can be added it must be confirmed that the person does "
 "not exists yet."
 msgstr ""
 
-#: basxconnect/core/wizards/add_person.py:168
+#: basxconnect/core/wizards/add_person.py:167
 msgid "Type of person"
 msgstr ""
 
-#: basxconnect/core/wizards/add_person.py:174
+#: basxconnect/core/wizards/add_person.py:173
 msgid "Choose person main type"
 msgstr ""
 
-#: basxconnect/core/wizards/add_person.py:177
+#: basxconnect/core/wizards/add_person.py:176
 msgid "Please choose what type of person you want to add:"
 msgstr ""
 
-#: basxconnect/core/wizards/add_person.py:192
+#: basxconnect/core/wizards/add_person.py:191
 msgid "Subtype of person"
 msgstr ""
 
-#: basxconnect/core/wizards/add_person.py:208
+#: basxconnect/core/wizards/add_person.py:207
 msgid "Choose person type"
 msgstr ""
 
-#: basxconnect/core/wizards/add_person.py:216
+#: basxconnect/core/wizards/add_person.py:215
 msgid "Add person"
 msgstr "Legg til person"
 
-#: basxconnect/core/wizards/add_person.py:224
+#: basxconnect/core/wizards/add_person.py:223
 msgid "Finish"
 msgstr ""
 
-#: basxconnect/core/wizards/add_person.py:273
+#: basxconnect/core/wizards/add_person.py:272
 msgid "Search"
 msgstr "Søk"
 
-#: basxconnect/core/wizards/add_person.py:275
+#: basxconnect/core/wizards/add_person.py:274
 msgid "Subtype"
 msgstr ""
 
-#: basxconnect/core/wizards/add_person.py:276
+#: basxconnect/core/wizards/add_person.py:275
 msgid "Information"
 msgstr "Info"
 
-#: basxconnect/core/wizards/add_person.py:277
+#: basxconnect/core/wizards/add_person.py:276
 msgid "Confirmation"
 msgstr "Bekreftelse"
 
-#: basxconnect/core/wizards/add_person.py:301
+#: basxconnect/core/wizards/add_person.py:300
 msgid "Add new person"
 msgstr "Legg til ny person"
 
-#: basxconnect/core/wizards/add_person.py:372
+#: basxconnect/core/wizards/add_person.py:371
 #, fuzzy
 msgid "Review and confirm the entered information"
 msgstr "Gjennomse og bekreft innskrevet info"
 
 #~ msgid "Languages"
 #~ msgstr "Språk"
 
 #~ msgid "Revisions"
 #~ msgstr "Revisjoner"
 
-#~ msgid "Date"
-#~ msgstr "Dato"
-
-#~ msgid "User"
-#~ msgstr "Bruker"
-
-#~ msgid "Change"
-#~ msgstr "Endre"
-
 #, fuzzy
 #~| msgid "Person category"
 #~ msgid "Person Category"
 #~ msgstr "Personkateogri"
 
 #~ msgid "Categories"
 #~ msgstr "Kategorier"
```

### Comparing `basxconnect-0.4.6/basxconnect/core/locale/pt/LC_MESSAGES/django.po` & `basxconnect-0.4.7/basxconnect/core/locale/pt/LC_MESSAGES/django.po`

 * *Files 2% similar despite different names*

```diff
@@ -3,15 +3,15 @@
 # This file is distributed under the same license as the PACKAGE package.
 # FIRST AUTHOR <EMAIL@ADDRESS>, YEAR.
 #
 msgid ""
 msgstr ""
 "Project-Id-Version: PACKAGE VERSION\n"
 "Report-Msgid-Bugs-To: \n"
-"POT-Creation-Date: 2022-06-02 14:49+0700\n"
+"POT-Creation-Date: 2022-07-24 15:47+0700\n"
 "PO-Revision-Date: 2021-05-08 22:32+0000\n"
 "Last-Translator: ssantos <ssantos@web.de>\n"
 "Language-Team: Portuguese <https://hosted.weblate.org/projects/basxconnect/"
 "basxconnect/pt/>\n"
 "Language: pt\n"
 "MIME-Version: 1.0\n"
 "Content-Type: text/plain; charset=UTF-8\n"
@@ -235,28 +235,55 @@
 #| msgid "Confirmation"
 msgid "Contributions"
 msgstr "Confirmação"
 
 #: basxconnect/core/layouts/editperson/common/contributions_tab.py:37
 #: basxconnect/core/layouts/settings_layout.py:33
 #: basxconnect/core/layouts/settings_layout.py:115
-#: basxconnect/core/views/term.py:26 basxconnect/core/wizards/add_person.py:380
+#: basxconnect/core/views/term.py:26 basxconnect/core/wizards/add_person.py:379
 #, python-format
 msgid "Add %s"
 msgstr "Adicionar %s"
 
+#: basxconnect/core/layouts/editperson/common/documenttemplates_tab.py:19
+msgid "Documents"
+msgstr ""
+
 #: basxconnect/core/layouts/editperson/common/head.py:20
 #: basxconnect/core/views/person/person_browse_views.py:193
 msgid "Restore"
 msgstr ""
 
 #: basxconnect/core/layouts/editperson/common/head.py:33
 msgid "Copy"
 msgstr "Copiar"
 
+#: basxconnect/core/layouts/editperson/common/history_tab.py:68
+msgid "History"
+msgstr ""
+
+#: basxconnect/core/layouts/editperson/common/history_tab.py:78
+msgid "Date"
+msgstr "Data"
+
+#: basxconnect/core/layouts/editperson/common/history_tab.py:84
+msgid "Time"
+msgstr ""
+
+#: basxconnect/core/layouts/editperson/common/history_tab.py:90
+msgid "User"
+msgstr "Utilizador"
+
+#: basxconnect/core/layouts/editperson/common/history_tab.py:94
+#: basxconnect/core/layouts/editperson/common/history_tab.py:126
+#, fuzzy
+#| msgid "Change"
+msgid "Changes"
+msgstr "Alterar"
+
 #: basxconnect/core/layouts/editperson/common/relationships_tab.py:22
 #: basxconnect/core/layouts/settings_layout.py:16
 #: basxconnect/core/models/relationships.py:55
 #: basxconnect/core/views/menu_views.py:75
 msgid "Relationships"
 msgstr "Relações"
 
@@ -379,27 +406,27 @@
 #: basxconnect/core/models/persons.py:241
 msgid "Person"
 msgstr "Pessoa"
 
 #: basxconnect/core/models/addresses.py:30
 #: basxconnect/core/models/addresses.py:54
 #: basxconnect/core/views/person/person_browse_views.py:158
-#: basxconnect/core/wizards/add_person.py:68
+#: basxconnect/core/wizards/add_person.py:67
 msgid "Email"
 msgstr "E-mail"
 
 #: basxconnect/core/models/addresses.py:39
 #: basxconnect/core/models/addresses.py:74
 #: basxconnect/core/models/addresses.py:93
 #: basxconnect/core/models/addresses.py:114
 #: basxconnect/core/models/addresses.py:139
 #: basxconnect/core/models/persons.py:350
 #: basxconnect/core/models/persons.py:374
 #: basxconnect/core/models/relationships.py:36
-#: basxconnect/core/wizards/add_person.py:274
+#: basxconnect/core/wizards/add_person.py:273
 msgid "Type"
 msgstr "Escrever"
 
 #: basxconnect/core/models/addresses.py:60
 msgid "Email address"
 msgstr "Endereço do E-mail"
 
@@ -441,15 +468,15 @@
 msgstr "Números de Fax"
 
 #: basxconnect/core/models/addresses.py:127
 msgid "Country"
 msgstr "Pais"
 
 #: basxconnect/core/models/addresses.py:128
-#: basxconnect/core/wizards/add_person.py:47
+#: basxconnect/core/wizards/add_person.py:46
 msgid "Address"
 msgstr "Endereço"
 
 #: basxconnect/core/models/addresses.py:129
 msgid "Post Code"
 msgstr "Código-Postal"
 
@@ -768,23 +795,23 @@
 #: basxconnect/core/views/person/person_modals_views.py:250
 #, fuzzy
 #| msgid "Email"
 msgid "Edit Email"
 msgstr "E-mail"
 
 #: basxconnect/core/views/person/search_person_view.py:21
-#: basxconnect/core/wizards/add_person.py:148
+#: basxconnect/core/wizards/add_person.py:147
 msgid "Search person"
 msgstr "Procurar pessoa"
 
-#: basxconnect/core/views/person/search_person_view.py:63
+#: basxconnect/core/views/person/search_person_view.py:62
 msgid "No results"
 msgstr "Nenhum resultado"
 
-#: basxconnect/core/views/person/search_person_view.py:96
+#: basxconnect/core/views/person/search_person_view.py:95
 #, python-format
 msgid "%s items found"
 msgstr "%s itens encontrados"
 
 #: basxconnect/core/views/relationship_views.py:40
 #, fuzzy
 #| msgid "Relationship"
@@ -825,109 +852,100 @@
 msgid "Submit"
 msgstr ""
 
 #: basxconnect/core/views/vocabulary.py:14
 msgid "Terms of vocabulary"
 msgstr ""
 
-#: basxconnect/core/wizards/add_person.py:102
+#: basxconnect/core/wizards/add_person.py:101
 msgid "Back"
 msgstr "Voltar"
 
-#: basxconnect/core/wizards/add_person.py:113
+#: basxconnect/core/wizards/add_person.py:112
 msgid "Complete"
 msgstr "Completo"
 
-#: basxconnect/core/wizards/add_person.py:116
+#: basxconnect/core/wizards/add_person.py:115
 msgid "Continue"
 msgstr "Continuar"
 
-#: basxconnect/core/wizards/add_person.py:128
+#: basxconnect/core/wizards/add_person.py:127
 msgid "Check for existing people before continuing"
 msgstr "Verificar as pessoas existentes antes de continuar"
 
-#: basxconnect/core/wizards/add_person.py:136
+#: basxconnect/core/wizards/add_person.py:135
 msgid "Start typing to search for a person..."
 msgstr "Comece a digitar para procurar uma pessoa..."
 
-#: basxconnect/core/wizards/add_person.py:152
+#: basxconnect/core/wizards/add_person.py:151
 msgid ""
 "Before a new person can be added it must be confirmed that the person does "
 "not exists yet."
 msgstr ""
 "Antes que uma nova pessoa possa ser acrescentada, deve ser confirmado que a "
 "pessoa ainda não existe."
 
-#: basxconnect/core/wizards/add_person.py:168
+#: basxconnect/core/wizards/add_person.py:167
 msgid "Type of person"
 msgstr "Tipo de pessoa"
 
-#: basxconnect/core/wizards/add_person.py:174
+#: basxconnect/core/wizards/add_person.py:173
 msgid "Choose person main type"
 msgstr "Escolha o tipo de pessoa principal"
 
-#: basxconnect/core/wizards/add_person.py:177
+#: basxconnect/core/wizards/add_person.py:176
 msgid "Please choose what type of person you want to add:"
 msgstr "Por favor selecione o tipo de pessoa quer adicionar:"
 
-#: basxconnect/core/wizards/add_person.py:192
+#: basxconnect/core/wizards/add_person.py:191
 msgid "Subtype of person"
 msgstr "Subtipo de pessoa"
 
-#: basxconnect/core/wizards/add_person.py:208
+#: basxconnect/core/wizards/add_person.py:207
 msgid "Choose person type"
 msgstr "Escolher o tipo de pessoa"
 
-#: basxconnect/core/wizards/add_person.py:216
+#: basxconnect/core/wizards/add_person.py:215
 msgid "Add person"
 msgstr "Adicionar pessoa"
 
-#: basxconnect/core/wizards/add_person.py:224
+#: basxconnect/core/wizards/add_person.py:223
 msgid "Finish"
 msgstr "Concluir"
 
-#: basxconnect/core/wizards/add_person.py:273
+#: basxconnect/core/wizards/add_person.py:272
 msgid "Search"
 msgstr "Pesquisar"
 
-#: basxconnect/core/wizards/add_person.py:275
+#: basxconnect/core/wizards/add_person.py:274
 msgid "Subtype"
 msgstr "Subtipo"
 
-#: basxconnect/core/wizards/add_person.py:276
+#: basxconnect/core/wizards/add_person.py:275
 msgid "Information"
 msgstr "Informação"
 
-#: basxconnect/core/wizards/add_person.py:277
+#: basxconnect/core/wizards/add_person.py:276
 msgid "Confirmation"
 msgstr "Confirmação"
 
-#: basxconnect/core/wizards/add_person.py:301
+#: basxconnect/core/wizards/add_person.py:300
 msgid "Add new person"
 msgstr "Adicionar nova pessoa"
 
-#: basxconnect/core/wizards/add_person.py:372
+#: basxconnect/core/wizards/add_person.py:371
 msgid "Review and confirm the entered information"
 msgstr "Rever e confirmar informação introduzida"
 
 #~ msgid "Languages"
 #~ msgstr "Línguas"
 
 #~ msgid "Revisions"
 #~ msgstr "Revisões"
 
-#~ msgid "Date"
-#~ msgstr "Data"
-
-#~ msgid "User"
-#~ msgstr "Utilizador"
-
-#~ msgid "Change"
-#~ msgstr "Alterar"
-
 #, fuzzy
 #~| msgid "Person category"
 #~ msgid "Person Category"
 #~ msgstr "Categoria de pessoa"
 
 #~ msgid "Categories"
 #~ msgstr "Categorias"
```

### Comparing `basxconnect-0.4.6/basxconnect/core/locale/th/LC_MESSAGES/django.po` & `basxconnect-0.4.7/basxconnect/core/locale/th/LC_MESSAGES/django.po`

 * *Files 1% similar despite different names*

```diff
@@ -3,15 +3,15 @@
 # This file is distributed under the same license as the PACKAGE package.
 # FIRST AUTHOR <EMAIL@ADDRESS>, YEAR.
 #
 msgid ""
 msgstr ""
 "Project-Id-Version: \n"
 "Report-Msgid-Bugs-To: \n"
-"POT-Creation-Date: 2022-06-02 14:49+0700\n"
+"POT-Creation-Date: 2022-07-24 15:47+0700\n"
 "PO-Revision-Date: 2022-03-30 10:08+0000\n"
 "Last-Translator: Tidaphan <tida@basx.dev>\n"
 "Language-Team: Thai <https://hosted.weblate.org/projects/basxconnect/"
 "basxconnect/th/>\n"
 "Language: th\n"
 "MIME-Version: 1.0\n"
 "Content-Type: text/plain; charset=UTF-8\n"
@@ -192,28 +192,55 @@
 #: basxconnect/core/layouts/editperson/common/contributions_tab.py:17
 msgid "Contributions"
 msgstr "เงินบริจาค"
 
 #: basxconnect/core/layouts/editperson/common/contributions_tab.py:37
 #: basxconnect/core/layouts/settings_layout.py:33
 #: basxconnect/core/layouts/settings_layout.py:115
-#: basxconnect/core/views/term.py:26 basxconnect/core/wizards/add_person.py:380
+#: basxconnect/core/views/term.py:26 basxconnect/core/wizards/add_person.py:379
 #, python-format
 msgid "Add %s"
 msgstr "เพิ่ม %s"
 
+#: basxconnect/core/layouts/editperson/common/documenttemplates_tab.py:19
+msgid "Documents"
+msgstr ""
+
 #: basxconnect/core/layouts/editperson/common/head.py:20
 #: basxconnect/core/views/person/person_browse_views.py:193
 msgid "Restore"
 msgstr "เรียกคืนค่า"
 
 #: basxconnect/core/layouts/editperson/common/head.py:33
 msgid "Copy"
 msgstr "คัดลอก"
 
+#: basxconnect/core/layouts/editperson/common/history_tab.py:68
+msgid "History"
+msgstr ""
+
+#: basxconnect/core/layouts/editperson/common/history_tab.py:78
+msgid "Date"
+msgstr "วันที่"
+
+#: basxconnect/core/layouts/editperson/common/history_tab.py:84
+msgid "Time"
+msgstr ""
+
+#: basxconnect/core/layouts/editperson/common/history_tab.py:90
+msgid "User"
+msgstr "ชื่อผู้ใช้งาน"
+
+#: basxconnect/core/layouts/editperson/common/history_tab.py:94
+#: basxconnect/core/layouts/editperson/common/history_tab.py:126
+#, fuzzy
+#| msgid "Change"
+msgid "Changes"
+msgstr "เปลี่ยน"
+
 #: basxconnect/core/layouts/editperson/common/relationships_tab.py:22
 #: basxconnect/core/layouts/settings_layout.py:16
 #: basxconnect/core/models/relationships.py:55
 #: basxconnect/core/views/menu_views.py:75
 msgid "Relationships"
 msgstr "ความสัมพันธ์"
 
@@ -322,27 +349,27 @@
 #: basxconnect/core/models/persons.py:241
 msgid "Person"
 msgstr "บุคคล"
 
 #: basxconnect/core/models/addresses.py:30
 #: basxconnect/core/models/addresses.py:54
 #: basxconnect/core/views/person/person_browse_views.py:158
-#: basxconnect/core/wizards/add_person.py:68
+#: basxconnect/core/wizards/add_person.py:67
 msgid "Email"
 msgstr "อีเมล์"
 
 #: basxconnect/core/models/addresses.py:39
 #: basxconnect/core/models/addresses.py:74
 #: basxconnect/core/models/addresses.py:93
 #: basxconnect/core/models/addresses.py:114
 #: basxconnect/core/models/addresses.py:139
 #: basxconnect/core/models/persons.py:350
 #: basxconnect/core/models/persons.py:374
 #: basxconnect/core/models/relationships.py:36
-#: basxconnect/core/wizards/add_person.py:274
+#: basxconnect/core/wizards/add_person.py:273
 msgid "Type"
 msgstr "ประเภท"
 
 #: basxconnect/core/models/addresses.py:60
 msgid "Email address"
 msgstr "ที่อยู่อีเมล์"
 
@@ -384,15 +411,15 @@
 msgstr "แฟกซ์"
 
 #: basxconnect/core/models/addresses.py:127
 msgid "Country"
 msgstr "ประเทศ"
 
 #: basxconnect/core/models/addresses.py:128
-#: basxconnect/core/wizards/add_person.py:47
+#: basxconnect/core/wizards/add_person.py:46
 msgid "Address"
 msgstr "ที่อยู่"
 
 #: basxconnect/core/models/addresses.py:129
 msgid "Post Code"
 msgstr "รหัสไปรษณีย์"
 
@@ -700,23 +727,23 @@
 msgstr "เผยแพร่การเปลี่ยนแปลงที่อยู่อีเมลไปยัง %s"
 
 #: basxconnect/core/views/person/person_modals_views.py:250
 msgid "Edit Email"
 msgstr "แก้ไขอีเมล์"
 
 #: basxconnect/core/views/person/search_person_view.py:21
-#: basxconnect/core/wizards/add_person.py:148
+#: basxconnect/core/wizards/add_person.py:147
 msgid "Search person"
 msgstr "ค้นหาบุคคล"
 
-#: basxconnect/core/views/person/search_person_view.py:63
+#: basxconnect/core/views/person/search_person_view.py:62
 msgid "No results"
 msgstr "ไม่มีผลลัพท์"
 
-#: basxconnect/core/views/person/search_person_view.py:96
+#: basxconnect/core/views/person/search_person_view.py:95
 #, python-format
 msgid "%s items found"
 msgstr "%sรายการที่พบ"
 
 #: basxconnect/core/views/relationship_views.py:40
 msgid "Edit Relationship"
 msgstr "แก้ไขความสัมพันธ์"
@@ -753,89 +780,89 @@
 
 #: basxconnect/core/views/vocabulary.py:14
 #, fuzzy
 #| msgid "Vocabulary"
 msgid "Terms of vocabulary"
 msgstr "คำศัพท์"
 
-#: basxconnect/core/wizards/add_person.py:102
+#: basxconnect/core/wizards/add_person.py:101
 msgid "Back"
 msgstr "กลับ"
 
-#: basxconnect/core/wizards/add_person.py:113
+#: basxconnect/core/wizards/add_person.py:112
 msgid "Complete"
 msgstr "เรียบร้อย"
 
-#: basxconnect/core/wizards/add_person.py:116
+#: basxconnect/core/wizards/add_person.py:115
 msgid "Continue"
 msgstr "ต่อไป"
 
-#: basxconnect/core/wizards/add_person.py:128
+#: basxconnect/core/wizards/add_person.py:127
 msgid "Check for existing people before continuing"
 msgstr "ตรวจสอบข้อมูลก่อนดำเนินการต่อ"
 
-#: basxconnect/core/wizards/add_person.py:136
+#: basxconnect/core/wizards/add_person.py:135
 msgid "Start typing to search for a person..."
 msgstr "พิมพ์เพื่อค้นหาบุคคล"
 
-#: basxconnect/core/wizards/add_person.py:152
+#: basxconnect/core/wizards/add_person.py:151
 msgid ""
 "Before a new person can be added it must be confirmed that the person does "
 "not exists yet."
 msgstr "ก่อนที่จะเพิ่มบุคคลใหม่จะต้องได้รับการยืนยันว่าบุคคลนั้นยังไม่ปรากฏ"
 
-#: basxconnect/core/wizards/add_person.py:168
+#: basxconnect/core/wizards/add_person.py:167
 msgid "Type of person"
 msgstr "ประเภทบุคคล"
 
-#: basxconnect/core/wizards/add_person.py:174
+#: basxconnect/core/wizards/add_person.py:173
 msgid "Choose person main type"
 msgstr "เลือกประเภทบุคคลหลัก"
 
-#: basxconnect/core/wizards/add_person.py:177
+#: basxconnect/core/wizards/add_person.py:176
 msgid "Please choose what type of person you want to add:"
 msgstr "โปรดเลือกประเภทของบุคคลที่คุณต้องการเพิ่ม:"
 
-#: basxconnect/core/wizards/add_person.py:192
+#: basxconnect/core/wizards/add_person.py:191
 msgid "Subtype of person"
 msgstr "ประเภทบุคคลรายย่อย"
 
-#: basxconnect/core/wizards/add_person.py:208
+#: basxconnect/core/wizards/add_person.py:207
 msgid "Choose person type"
 msgstr "เลือกประเภทบุคคล"
 
-#: basxconnect/core/wizards/add_person.py:216
+#: basxconnect/core/wizards/add_person.py:215
 msgid "Add person"
 msgstr "เพิ่มบุคคล"
 
-#: basxconnect/core/wizards/add_person.py:224
+#: basxconnect/core/wizards/add_person.py:223
 msgid "Finish"
 msgstr "เสร็จเรียบร้อย"
 
-#: basxconnect/core/wizards/add_person.py:273
+#: basxconnect/core/wizards/add_person.py:272
 msgid "Search"
 msgstr "ค้นหา"
 
-#: basxconnect/core/wizards/add_person.py:275
+#: basxconnect/core/wizards/add_person.py:274
 msgid "Subtype"
 msgstr "ประเภทย่อย"
 
-#: basxconnect/core/wizards/add_person.py:276
+#: basxconnect/core/wizards/add_person.py:275
 msgid "Information"
 msgstr "ข้อมูลเบื้องต้น"
 
-#: basxconnect/core/wizards/add_person.py:277
+#: basxconnect/core/wizards/add_person.py:276
 msgid "Confirmation"
 msgstr "ยืนยัน"
 
-#: basxconnect/core/wizards/add_person.py:301
+#: basxconnect/core/wizards/add_person.py:300
 msgid "Add new person"
 msgstr "เพิ่มบุคคลใหม่"
 
-#: basxconnect/core/wizards/add_person.py:372
+#: basxconnect/core/wizards/add_person.py:371
 msgid "Review and confirm the entered information"
 msgstr "ตรวจสอบและยืนยันข้อมูล"
 
 #~ msgid "Administration"
 #~ msgstr "ผู้ดูแลระบบ"
 
 #~ msgid "System Information"
@@ -846,23 +873,14 @@
 
 #~ msgid "Languages"
 #~ msgstr "เลือกใช้ภาษา"
 
 #~ msgid "Revisions"
 #~ msgstr "การแก้ไข"
 
-#~ msgid "Date"
-#~ msgstr "วันที่"
-
-#~ msgid "User"
-#~ msgstr "ชื่อผู้ใช้งาน"
-
-#~ msgid "Change"
-#~ msgstr "เปลี่ยน"
-
 #~ msgid "Person Category"
 #~ msgstr "หมวดหมู่บุคคล"
 
 #~ msgid "Edit Categories"
 #~ msgstr "แก้ไขหมวดหมู่"
 
 #~ msgid "Unsaved changes"
```

### Comparing `basxconnect-0.4.6/basxconnect/core/migrations/0001_initial.py` & `basxconnect-0.4.7/basxconnect/core/migrations/0001_initial.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 # Generated by Django 3.1.5 on 2021-03-08 12:33
 
 import django.db.models.deletion
 import django_countries.fields
 import phonenumber_field.modelfields
 import simple_history.models
-from bread.contrib import languages
+from basxbread.contrib import languages
 from django.conf import settings
 from django.db import migrations, models
 
 
 class Migration(migrations.Migration):
 
     initial = True
```

### Comparing `basxconnect-0.4.6/basxconnect/core/migrations/0003_auto_20210309_2221.py` & `basxconnect-0.4.7/basxconnect/core/migrations/0003_auto_20210309_2221.py`

 * *Files identical despite different names*

### Comparing `basxconnect-0.4.6/basxconnect/core/migrations/0004_auto_20210311_1851.py` & `basxconnect-0.4.7/basxconnect/core/migrations/0004_auto_20210311_1851.py`

 * *Files identical despite different names*

### Comparing `basxconnect-0.4.6/basxconnect/core/migrations/0005_auto_20210311_1851.py` & `basxconnect-0.4.7/basxconnect/core/migrations/0005_auto_20210311_1851.py`

 * *Files identical despite different names*

### Comparing `basxconnect-0.4.6/basxconnect/core/migrations/0006_auto_20210312_0016.py` & `basxconnect-0.4.7/basxconnect/core/migrations/0006_auto_20210312_0016.py`

 * *Files identical despite different names*

### Comparing `basxconnect-0.4.6/basxconnect/core/migrations/0007_auto_20210312_0054.py` & `basxconnect-0.4.7/basxconnect/core/migrations/0007_auto_20210312_0054.py`

 * *Files identical despite different names*

### Comparing `basxconnect-0.4.6/basxconnect/core/migrations/0008_auto_20210323_1456.py` & `basxconnect-0.4.7/basxconnect/core/migrations/0008_auto_20210323_1456.py`

 * *Files identical despite different names*

### Comparing `basxconnect-0.4.6/basxconnect/core/migrations/0009_auto_20210522_1817.py` & `basxconnect-0.4.7/basxconnect/core/migrations/0009_auto_20210522_1817.py`

 * *Files identical despite different names*

### Comparing `basxconnect-0.4.6/basxconnect/core/migrations/0010_auto_20210523_1140.py` & `basxconnect-0.4.7/basxconnect/core/migrations/0010_auto_20210523_1140.py`

 * *Files identical despite different names*

### Comparing `basxconnect-0.4.6/basxconnect/core/migrations/0011_auto_20210726_2047.py` & `basxconnect-0.4.7/basxconnect/core/migrations/0011_auto_20210726_2047.py`

 * *Files identical despite different names*

### Comparing `basxconnect-0.4.6/basxconnect/core/migrations/0012_auto_20210928_1158.py` & `basxconnect-0.4.7/basxconnect/core/migrations/0012_auto_20210928_1158.py`

 * *Files identical despite different names*

### Comparing `basxconnect-0.4.6/basxconnect/core/migrations/0013_auto_20210928_1445.py` & `basxconnect-0.4.7/basxconnect/core/migrations/0013_auto_20210928_1445.py`

 * *Files identical despite different names*

### Comparing `basxconnect-0.4.6/basxconnect/core/migrations/0014_auto_20210928_1512.py` & `basxconnect-0.4.7/basxconnect/core/migrations/0014_auto_20210928_1512.py`

 * *Files identical despite different names*

### Comparing `basxconnect-0.4.6/basxconnect/core/migrations/0015_rename_category_to_tag.py` & `basxconnect-0.4.7/basxconnect/core/migrations/0015_rename_category_to_tag.py`

 * *Files identical despite different names*

### Comparing `basxconnect-0.4.6/basxconnect/core/migrations/0016_auto_20210928_1534.py` & `basxconnect-0.4.7/basxconnect/core/migrations/0016_auto_20210928_1534.py`

 * *Files identical despite different names*

### Comparing `basxconnect-0.4.6/basxconnect/core/migrations/0018_term_slug.py` & `basxconnect-0.4.7/basxconnect/core/migrations/0018_term_slug.py`

 * *Files identical despite different names*

### Comparing `basxconnect-0.4.6/basxconnect/core/migrations/0020_auto_20211005_1630.py` & `basxconnect-0.4.7/basxconnect/core/migrations/0020_auto_20211005_1630.py`

 * *Files identical despite different names*

### Comparing `basxconnect-0.4.6/basxconnect/core/migrations/0021_auto_20211007_0932.py` & `basxconnect-0.4.7/basxconnect/core/migrations/0021_auto_20211007_0932.py`

 * *Files identical despite different names*

### Comparing `basxconnect-0.4.6/basxconnect/core/migrations/0022_auto_20211018_1644.py` & `basxconnect-0.4.7/basxconnect/core/migrations/0022_auto_20211018_1644.py`

 * *Files identical despite different names*

### Comparing `basxconnect-0.4.6/basxconnect/core/migrations/0023_auto_20211030_0955.py` & `basxconnect-0.4.7/basxconnect/core/migrations/0023_auto_20211030_0955.py`

 * *Files identical despite different names*

### Comparing `basxconnect-0.4.6/basxconnect/core/migrations/0026_auto_20211216_0946.py` & `basxconnect-0.4.7/basxconnect/core/migrations/0026_auto_20211216_0946.py`

 * *Files identical despite different names*

### Comparing `basxconnect-0.4.6/basxconnect/core/migrations/0027_auto_20211223_1948.py` & `basxconnect-0.4.7/basxconnect/core/migrations/0027_auto_20211223_1948.py`

 * *Files identical despite different names*

### Comparing `basxconnect-0.4.6/basxconnect/core/migrations/0029_auto_20220429_1138.py` & `basxconnect-0.4.7/basxconnect/core/migrations/0029_auto_20220429_1138.py`

 * *Files identical despite different names*

### Comparing `basxconnect-0.4.6/basxconnect/core/migrations/0030_auto_20220602_1434.py` & `basxconnect-0.4.7/basxconnect/core/migrations/0030_auto_20220602_1434.py`

 * *Files identical despite different names*

### Comparing `basxconnect-0.4.6/basxconnect/core/migrations/0031_alter_email_person_alter_email_type_alter_fax_person_and_more.py` & `basxconnect-0.4.7/basxconnect/core/migrations/0031_alter_email_person_alter_email_type_alter_fax_person_and_more.py`

 * *Files identical despite different names*

### Comparing `basxconnect-0.4.6/basxconnect/core/models/addresses.py` & `basxconnect-0.4.7/basxconnect/core/models/addresses.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 import htmlgenerator as hg
-from bread.layout import button
+from basxbread.layout import button
 from django.db import models
 from django.utils.translation import gettext_lazy as _
 from django_countries.fields import CountryField
 from phonenumber_field.modelfields import PhoneNumberField
 
 from .persons import Person
 from .utils import Term
```

### Comparing `basxconnect-0.4.6/basxconnect/core/models/persons.py` & `basxconnect-0.4.7/basxconnect/core/models/persons.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 import datetime
 import random
 
-from bread import layout
-from bread.contrib.languages.fields import LanguageField
-from bread.utils import get_concrete_instance, pretty_modelname
-from bread.utils.inheritancemanager import InheritanceManager
+from basxbread import layout
+from basxbread.contrib.languages.fields import LanguageField
+from basxbread.utils import get_concrete_instance
+from basxbread.utils.inheritancemanager import InheritanceManager
 from django.contrib.contenttypes.fields import GenericRelation
 from django.db import models
 from django.utils import timezone
 from django.utils.translation import gettext_lazy as _
 from dynamic_preferences.registries import global_preferences_registry
 from simple_history.models import HistoricalRecords
 
@@ -133,15 +133,15 @@
 
     objects = PersonManager()
 
     def __str__(self):
         return self.name
 
     def maintype(self):
-        return pretty_modelname(get_concrete_instance(self))
+        return get_concrete_instance(self)._meta.verbose_name
 
     maintype.verbose_name = _("Main Type")
     maintype.sorting_name = "_maintype"
 
     def status(self):
         return (
             layout.tag.Tag(_("active"), tag_color="green")
```

### Comparing `basxconnect-0.4.6/basxconnect/core/models/relationships.py` & `basxconnect-0.4.7/basxconnect/core/models/relationships.py`

 * *Files identical despite different names*

### Comparing `basxconnect-0.4.6/basxconnect/core/models/utils.py` & `basxconnect-0.4.7/basxconnect/core/models/utils.py`

 * *Files identical despite different names*

### Comparing `basxconnect-0.4.6/basxconnect/core/search_indexes.py` & `basxconnect-0.4.7/basxconnect/core/search_indexes.py`

 * *Files identical despite different names*

### Comparing `basxconnect-0.4.6/basxconnect/core/static/logo.png` & `basxconnect-0.4.7/basxconnect/core/static/logo.png`

 * *Files identical despite different names*

### Comparing `basxconnect-0.4.6/basxconnect/core/tests/settings.py` & `basxconnect-0.4.7/basxconnect/core/tests/settings.py`

 * *Files 2% similar despite different names*

```diff
@@ -2,29 +2,29 @@
 """
 For the full list of settings and their values, see
 https://docs.djangoproject.com/en/3.1/ref/settings/
 """
 
 import os
 
-from bread.settings.required import *
+from basxbread.settings.required import *
 
 # the above will import a set of predefined settings to ensure required
 # settings are defined correctly and to reduce verbosity in this file
 
 # SECURITY WARNING: keep the secret key used in production secret!
 SECRET_KEY = "test"  # nosec # can ignore security check for testing key
 
 ALLOWED_HOSTS = ["*"]
 
-# BREAD_DEPENDENCIES are imported in the start import at the top
+# BASXBREAD_DEPENDENCIES are imported in the start import at the top
 INSTALLED_APPS = [
     "basxconnect.core.apps.CoreConfig",
     "basxconnect.contributions.apps.ContributionsConfig",
-] + BREAD_DEPENDENCIES
+] + BASXBREAD_DEPENDENCIES
 
 TEMPLATES[0]["OPTIONS"]["context_processors"].append(
     "basxconnect.core.context_processors.basxconnect_core"
 )
 
 ROOT_URLCONF = "basxconnect.core.tests.urls"
 DATABASES = {
```

### Comparing `basxconnect-0.4.6/basxconnect/core/tests/test_person.py` & `basxconnect-0.4.7/basxconnect/core/tests/test_person.py`

 * *Files 21% similar despite different names*

```diff
@@ -1,30 +1,30 @@
-from bread.tests.helper import generic_bread_testcase
+from basxbread.tests.helper import generic_basxbread_testcase
 from hypothesis.extra.django import from_model
 
 from basxconnect.core import models
 
 
-class VocabularyTest(generic_bread_testcase(models.Vocabulary)):
+class VocabularyTest(generic_basxbread_testcase(models.Vocabulary)):
     pass
 
 
 class TermTest(
-    generic_bread_testcase(models.Term, vocabulary=from_model(models.Vocabulary))
+    generic_basxbread_testcase(models.Term, vocabulary=from_model(models.Vocabulary))
 ):
     pass
 
 
-class PersonTest(generic_bread_testcase(models.Person)):
+class PersonTest(generic_basxbread_testcase(models.Person)):
     pass
 
 
-class NaturalPersonTest(generic_bread_testcase(models.NaturalPerson)):
+class NaturalPersonTest(generic_basxbread_testcase(models.NaturalPerson)):
     pass
 
 
-class LegalPersonTest(generic_bread_testcase(models.LegalPerson)):
+class LegalPersonTest(generic_basxbread_testcase(models.LegalPerson)):
     pass
 
 
-class PersonAssociationTest(generic_bread_testcase(models.PersonAssociation)):
+class PersonAssociationTest(generic_basxbread_testcase(models.PersonAssociation)):
     pass
```

### Comparing `basxconnect-0.4.6/basxconnect/core/urls.py` & `basxconnect-0.4.7/basxconnect/core/urls.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,15 @@
-from bread import views as breadviews
-from bread.utils.urls import autopath, default_model_paths, model_urlname, reverse_model
-from bread.views import AddView, BrowseView, EditView
+from basxbread import views as breadviews
+from basxbread.utils.urls import (
+    autopath,
+    default_model_paths,
+    model_urlname,
+    reverse_model,
+)
+from basxbread.views import AddView, BrowseView, EditView
 from django.views.generic import RedirectView
 
 import basxconnect.core.views.tag_views
 from basxconnect.core.views import settings_views
 from basxconnect.core.views.person import (
     person_browse_views,
     person_details_views,
```

### Comparing `basxconnect-0.4.6/basxconnect/core/views/menu_views.py` & `basxconnect-0.4.7/basxconnect/core/views/menu_views.py`

 * *Files 7% similar despite different names*

```diff
@@ -1,12 +1,12 @@
-from bread import layout as layout
-from bread import menu
-from bread.layout import DEVMODE_KEY
-from bread.utils.links import Link
-from bread.utils.urls import reverse, reverse_model
+from basxbread import layout as layout
+from basxbread import menu
+from basxbread.layout import DEVMODE_KEY
+from basxbread.utils.links import Link
+from basxbread.utils.urls import reverse, reverse_model
 from django.utils.translation import gettext_lazy as _
 
 import basxconnect.core.models
 
 from .. import models
```

### Comparing `basxconnect-0.4.6/basxconnect/core/views/person/person_browse_views.py` & `basxconnect-0.4.7/basxconnect/core/views/person/person_browse_views.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,17 +1,17 @@
 import htmlgenerator as hg
-from bread import layout as layout
-from bread.layout.components.datatable import DataTableColumn
-from bread.utils import get_concrete_instance
-from bread.utils.links import Link
-from bread.utils.urls import reverse, reverse_model
-from bread.views import BrowseView, BulkAction
-from bread.views.browse import delete as breaddelete
-from bread.views.browse import export as breadexport
-from bread.views.browse import restore as breadrestore
+from basxbread import layout as layout
+from basxbread.layout.components.datatable import DataTableColumn
+from basxbread.utils import get_concrete_instance
+from basxbread.utils.links import Link
+from basxbread.utils.urls import reverse, reverse_model
+from basxbread.views import BrowseView, BulkAction
+from basxbread.views.browse import delete as breaddelete
+from basxbread.views.browse import export as breadexport
+from basxbread.views.browse import restore as breadrestore
 from django import forms
 from django.db.models import Q
 from django.http import HttpResponseRedirect
 from django.utils.html import mark_safe
 from django.utils.translation import gettext_lazy as _
 from django.utils.translation import pgettext_lazy
```

### Comparing `basxconnect-0.4.6/basxconnect/core/views/person/person_details_views.py` & `basxconnect-0.4.7/basxconnect/core/views/person/person_details_views.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,28 +1,29 @@
 import logging
 
-import bread
+import basxbread
 import django
 import htmlgenerator as hg
-from bread import layout, menu
-from bread.layout.components.button import Button
-from bread.layout.components.forms import Form
-from bread.utils import Link, reverse_model
-from bread.views import EditView, ReadView, layoutasreadonly
+from basxbread import layout, menu
+from basxbread.layout.components.button import Button
+from basxbread.layout.components.forms import Form
+from basxbread.utils import Link, reverse_model
+from basxbread.views import EditView, ReadView, layoutasreadonly
 from django.apps import apps
 from django.conf import settings
 from django.forms import forms
 from django.http import HttpResponse, HttpResponseRedirect
 from django.shortcuts import get_object_or_404
 from django.utils.module_loading import import_string
 from django.utils.translation import gettext_lazy as _
 from django.views.decorators.csrf import csrf_exempt
 
 from ... import models
 from ...layouts.editperson import legalperson, naturalperson, personassociation
+from ...layouts.editperson.common import history_tab
 from ...layouts.editperson.common.head import editperson_head
 from ...layouts.editperson.common.relationships_tab import relationshipstab
 
 R = layout.grid.Row
 C = layout.grid.Col
 
 
@@ -128,32 +129,31 @@
                 gutter=False,
             ),
         ),
     )
 
 
 def editperson_tabs(base_data_tab, mailing_tab, request):
-
-    from django.apps import apps
-
-    if apps.is_installed("basxconnect.contributions"):
-        from ...layouts.editperson.common import contributions_tab
-
-        return [
-            base_data_tab(request),
-            relationshipstab(request),
-            mailing_tab(request),
-            contributions_tab.contributions_tab(request),
-        ]
-    return [
+    ret = [
         base_data_tab(request),
         relationshipstab(request),
         mailing_tab(request),
     ]
 
+    if apps.is_installed("basxconnect.contributions"):
+        from ...layouts.editperson.common import contributions_tab
+
+        ret.append(contributions_tab.contributions_tab(request))
+    if apps.is_installed("basxbread.contrib.publicurls"):
+        from ...layouts.editperson.common import documenttemplates_tab
+
+        ret.append(documenttemplates_tab.documenttemplates_tab())
+    ret.append(history_tab.history_tab())
+    return ret
+
 
 @csrf_exempt
 def togglepersonstatus(request, pk: int):
     if request.method == "POST":
         person = get_object_or_404(models.Person, pk=pk)
         person.active = not person.active
         person.save()
@@ -218,15 +218,15 @@
         request,
         import_string(settings.DEFAULT_PAGE_LAYOUT)(
             menu.main,
             Form(
                 form,
                 hg.BaseElement(
                     hg.H3(_("Delete email %s") % email.email),
-                    *(bread.layout.forms.FormField(field) for field in fields),
+                    *(basxbread.layout.forms.FormField(field) for field in fields),
                 ),
                 hg.DIV(
                     Button.from_link(
                         Link(
                             href=reverse_model(
                                 email.person, "read", kwargs={"pk": email.person.pk}
                             ),
```

### Comparing `basxconnect-0.4.6/basxconnect/core/views/person/person_modals_views.py` & `basxconnect-0.4.7/basxconnect/core/views/person/person_modals_views.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 import django.forms
 import htmlgenerator as hg
-from bread import layout
-from bread.layout.components.icon import Icon
-from bread.views import AddView, EditView
+from basxbread import layout
+from basxbread.layout.components.icon import Icon
+from basxbread.views import AddView, EditView
 from django.apps import apps
 from django.utils.translation import gettext_lazy as _
 
 from basxconnect.core import models
 
 
 class NaturalPersonEditMailingsView(EditView):
```

### Comparing `basxconnect-0.4.6/basxconnect/core/views/person/search_person_view.py` & `basxconnect-0.4.7/basxconnect/core/views/person/search_person_view.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 import htmlgenerator as hg
-from bread import layout as layout
-from bread.utils import reverse_model
+from basxbread import layout as layout
+from basxbread.utils import reverse_model
 from django.http import HttpResponse
 from django.urls import reverse_lazy
 from django.utils.translation import gettext_lazy as _
 from haystack.query import SearchQuerySet
 from haystack.utils import Highlighter
 from htmlgenerator import mark_safe
 
@@ -18,15 +18,14 @@
 ITEM_VALUE_CLASS = "search_result_value"
 
 searchbar = layout.search.Search(
     placeholder=_("Search person"),
     backend=layout.search.SearchBackendConfig(
         reverse_lazy("basxconnect.core.views.person.search_person_view.searchperson"),
     ),
-    width="140%",
 )
 
 
 def searchperson(request):
     query = request.GET.get("q")
 
     highlight = CustomHighlighter(query)
```

### Comparing `basxconnect-0.4.6/basxconnect/core/views/relationship_views.py` & `basxconnect-0.4.7/basxconnect/core/views/relationship_views.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 import htmlgenerator as hg
-from bread import layout
-from bread.views import AddView, EditView
+from basxbread import layout
+from basxbread.views import AddView, EditView
 from django.urls import reverse_lazy
 from django.utils.translation import gettext_lazy as _
 
 from basxconnect.core import models
 from basxconnect.core.views.person import search_person_view
```

### Comparing `basxconnect-0.4.6/basxconnect/core/views/settings_views.py` & `basxconnect-0.4.7/basxconnect/core/views/settings_views.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 import htmlgenerator as hg
-from bread import layout as layout
-from bread.utils.urls import aslayout
+from basxbread import layout as layout
+from basxbread.utils.urls import aslayout
 from django.utils.translation import gettext_lazy as _
 from dynamic_preferences.forms import global_preference_form_builder
 
 import basxconnect.core.layouts.settings_layout as settings_layout
 
 R = layout.grid.Row
 C = layout.grid.Col
```

### Comparing `basxconnect-0.4.6/basxconnect/core/views/tag_views.py` & `basxconnect-0.4.7/basxconnect/core/views/tag_views.py`

 * *Files 8% similar despite different names*

```diff
@@ -1,14 +1,14 @@
-import bread
+import basxbread
 import htmlgenerator as hg
-from bread import layout as layout
-from bread.layout.components.button import Button
-from bread.layout.components.modal import Modal, modal_with_trigger
-from bread.utils import aslayout, reverse_model
-from bread.views import AddView
+from basxbread import layout as layout
+from basxbread.layout.components.button import Button
+from basxbread.layout.components.modal import Modal, modal_with_trigger
+from basxbread.utils import aslayout, reverse_model
+from basxbread.views import AddView
 from django import forms
 from django.http import HttpResponseBadRequest, HttpResponseRedirect
 from django.utils.translation import gettext_lazy as _
 from django.utils.translation import ngettext_lazy
 from htmlgenerator import mark_safe
 
 from basxconnect.core import models
@@ -73,19 +73,19 @@
             "Remove tag from %(count)d person",
             "Remove tag from %(count)d persons",
             count,
         ) % {"count": count}
     tags_vocabulary_id = (
         getattr(Vocabulary.objects.filter(slug="tag").first(), "id", "") or ""
     )
-    return bread.layout.forms.Form(
+    return basxbread.layout.forms.Form(
         form,
         hg.H3(header),
         hg.DIV(
-            hg.DIV(bread.layout.forms.FormField("tag")),
+            hg.DIV(basxbread.layout.forms.FormField("tag")),
             hg.If(
                 operation == "add",
                 hg.DIV(
                     modal_with_trigger(
                         Modal.with_ajax_content(
                             heading=_("Create new tag"),
                             url=reverse_model(
```

### Comparing `basxconnect-0.4.6/basxconnect/core/views/term.py` & `basxconnect-0.4.7/basxconnect/core/views/term.py`

 * *Files 12% similar despite different names*

```diff
@@ -1,10 +1,10 @@
-from bread import layout
-from bread.utils import Link, ModelHref, pretty_modelname
-from bread.views import BrowseView
+from basxbread import layout
+from basxbread.utils import Link, ModelHref
+from basxbread.views import BrowseView
 from django.utils.translation import gettext_lazy as _
 
 from basxconnect.core.models import Term, Vocabulary
 
 
 class TermsBrowseView(BrowseView):
     def __init__(self, *args, **kwargs):
@@ -19,15 +19,15 @@
                 Link(
                     href=ModelHref(
                         Term,
                         "add",
                         query={"vocabulary": vocabulary.id},
                         return_to_current=True,
                     ),
-                    label=_("Add %s") % pretty_modelname(Term),
+                    label=_("Add %s") % Term._meta.verbose_name,
                 ),
                 icon=layout.icon.Icon("add", size=20),
             )
         return super().get(*args, **kwargs)
 
     def get_queryset(self):
         qs = super().get_queryset()
```

### Comparing `basxconnect-0.4.6/basxconnect/core/wizards/add_person.py` & `basxconnect-0.4.7/basxconnect/core/wizards/add_person.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,13 +1,12 @@
 import htmlgenerator as hg
-from bread import layout
-from bread.forms.forms import breadmodelform_factory
-from bread.utils import pretty_modelname
-from bread.utils.urls import reverse_model
-from bread.views import BreadView
+from basxbread import layout
+from basxbread.forms.forms import modelform_factory
+from basxbread.utils.urls import reverse_model
+from basxbread.views import BaseView
 from django import forms
 from django.apps import apps
 from django.contrib.auth.mixins import PermissionRequiredMixin
 from django.shortcuts import redirect
 from django.urls import reverse, reverse_lazy
 from django.utils.translation import gettext_lazy as _
 from dynamic_preferences.registries import global_preferences_registry
@@ -156,17 +155,17 @@
         searchelement,
         hg.DIV(id="search-results", style="margin-bottom: 2rem;"),
     )
 
 
 class ChooseType(forms.Form):
     PERSON_TYPES = {
-        "core.NaturalPerson": pretty_modelname(NaturalPerson),
-        "core.LegalPerson": pretty_modelname(LegalPerson),
-        "core.PersonAssociation": pretty_modelname(PersonAssociation),
+        "core.NaturalPerson": NaturalPerson._meta.verbose_name,
+        "core.LegalPerson": LegalPerson._meta.verbose_name,
+        "core.PersonAssociation": PersonAssociation._meta.verbose_name,
     }
     persontype = forms.TypedChoiceField(
         label=_("Type of person"),
         choices=tuple(PERSON_TYPES.items()),
         coerce=lambda a: apps.get_model(a),
         empty_value=None,
     )
@@ -222,24 +221,24 @@
         super().__init__(*args, **kwargs)
 
     title = _("Finish")
     _layout = hg.DIV("Please select a person type first")
 
 
 def generate_add_form_for(model, request, data, files, initial=None):
-    form = breadmodelform_factory(
+    form = modelform_factory(
         request=request, model=model, layout=ADD_FORM_LAYOUTS[model]()
     )(data, files, initial=initial)
 
-    for fieldname, field in breadmodelform_factory(
+    for fieldname, field in modelform_factory(
         request, Postal, ADD_ADDRESS_LAYOUT()
     )().fields.items():
         form.fields[fieldname] = field
 
-    for fieldname, field in breadmodelform_factory(
+    for fieldname, field in modelform_factory(
         request, Email, ADD_EMAIL_LAYOUT()
     )().fields.items():
         form.fields[fieldname] = field
 
     formlayout = hg.BaseElement(
         layout.grid.Grid(
             ADD_FORM_LAYOUTS[model](), style="margin-bottom: 2rem", gutter=False
@@ -253,15 +252,15 @@
         ),
     )
     form._layout = formlayout
     return form
 
 
 # The WizardView contains mostly control-flow logic and some configuration
-class AddPersonWizard(PermissionRequiredMixin, BreadView, NamedUrlSessionWizardView):
+class AddPersonWizard(PermissionRequiredMixin, BaseView, NamedUrlSessionWizardView):
     kwargs = {"url_name": "core:person:add_wizard", "urlparams": {"step": "str"}}
     urlparams = (("step", str),)
     permission_required = "core.add_person"
 
     form_list = [
         ("Search", SearchForm),
         ("Type", ChooseType),
@@ -373,15 +372,15 @@
                             lowcontrast=True,
                             hideclosebutton=True,
                         ),
                     )
                     for fieldname in form.fields:
                         form.fields[fieldname].disabled = True
                         form.fields[fieldname].widget.attrs["style"] = "color: #000"
-                form.title = _("Add %s") % pretty_modelname(persontype)
+                form.title = _("Add %s") % persontype._meta.verbose_name
         return form
 
     def done(self, form_list, **kwargs):
         personform = list(form_list)[-1]
         # in case the new person had a subtype set, we need to set the attribute here
         subtype = (self.get_cleaned_data_for_step("Subtype") or {}).get("subtype")
         if subtype:
```

### Comparing `basxconnect-0.4.6/basxconnect/mailer_integration/abstract/mailer.py` & `basxconnect-0.4.7/basxconnect/mailer_integration/abstract/mailer.py`

 * *Files identical despite different names*

### Comparing `basxconnect-0.4.6/basxconnect/mailer_integration/dynamic_preferences_registry.py` & `basxconnect-0.4.7/basxconnect/mailer_integration/dynamic_preferences_registry.py`

 * *Files identical despite different names*

### Comparing `basxconnect-0.4.6/basxconnect/mailer_integration/help.py` & `basxconnect-0.4.7/basxconnect/mailer_integration/help.py`

 * *Files 8% similar despite different names*

```diff
@@ -1,14 +1,14 @@
-import bread.layout
+import basxbread.layout
 import htmlgenerator as hg
 from django.utils.translation import gettext_lazy as _
 
 
 def sync_help_modal():
-    return bread.layout.modal.Modal(
+    return basxbread.layout.modal.Modal(
         _("Help"),
         _(
             "The button below is currently the only way of getting new subcribers from the mailer into our system. Is it also the only way of getting updates for subscribers that we already have in our system. This is what happens when the button is pressed:"
         ),
         hg.DIV(
             hg.UL(
                 hg.LI(
```

### Comparing `basxconnect-0.4.6/basxconnect/mailer_integration/layouts.py` & `basxconnect-0.4.7/basxconnect/mailer_integration/layouts.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,26 +1,26 @@
-import bread
+import basxbread
 import htmlgenerator as hg
-from bread import layout
-from bread.layout.components import tag
-from bread.layout.components.icon import Icon
-from bread.utils import ModelHref
+from basxbread import layout
+from basxbread.layout.components import tag
+from basxbread.layout.components.icon import Icon
+from basxbread.utils import ModelHref
 from django.conf import settings
 from django.shortcuts import get_object_or_404
 from django.utils.formats import localize
 from django.utils.timezone import localtime
 from django.utils.translation import gettext_lazy as _
 
 from basxconnect.core import models
 from basxconnect.core.layouts.editperson.common.utils import tile_with_icon
 from basxconnect.core.models import Person
 from basxconnect.mailer_integration.models import Interest, Subscription
 
-R = bread.layout.grid.Row
-C = bread.layout.grid.Col
+R = basxbread.layout.grid.Row
+C = basxbread.layout.grid.Col
 
 
 def mailer_integration_tile(request):
     person = get_object_or_404(Person, pk=request.resolver_match.kwargs["pk"])
     addresses = person.core_email_list.all()
     return tile_with_icon(
         Icon("email--new"),
```

### Comparing `basxconnect-0.4.6/basxconnect/mailer_integration/locale/de/LC_MESSAGES/django.po` & `basxconnect-0.4.7/basxconnect/mailer_integration/locale/de/LC_MESSAGES/django.po`

 * *Files 2% similar despite different names*

```diff
@@ -4,60 +4,56 @@
 # FIRST AUTHOR <EMAIL@ADDRESS>, YEAR.
 #
 #, fuzzy
 msgid ""
 msgstr ""
 "Project-Id-Version: PACKAGE VERSION\n"
 "Report-Msgid-Bugs-To: \n"
-"POT-Creation-Date: 2022-06-02 14:49+0700\n"
+"POT-Creation-Date: 2022-07-24 15:47+0700\n"
 "PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE\n"
 "Last-Translator: FULL NAME <EMAIL@ADDRESS>\n"
 "Language-Team: LANGUAGE <LL@li.org>\n"
 "Language: \n"
 "MIME-Version: 1.0\n"
 "Content-Type: text/plain; charset=UTF-8\n"
 "Content-Transfer-Encoding: 8bit\n"
 "Plural-Forms: nplurals=2; plural=(n != 1);\n"
 
-#: basxconnect/mailer_integration/dynamic_preferences_registry.py:10
+#: basxconnect/mailer_integration/dynamic_preferences_registry.py:6
 msgid "Mailchimp"
 msgstr ""
 
-#: basxconnect/mailer_integration/dynamic_preferences_registry.py:18
+#: basxconnect/mailer_integration/dynamic_preferences_registry.py:14
 msgid "Mailchimp server"
 msgstr ""
 
-#: basxconnect/mailer_integration/dynamic_preferences_registry.py:26
+#: basxconnect/mailer_integration/dynamic_preferences_registry.py:22
 msgid "Mailchimp list ID"
 msgstr ""
 
-#: basxconnect/mailer_integration/dynamic_preferences_registry.py:34
+#: basxconnect/mailer_integration/dynamic_preferences_registry.py:30
 msgid "Mailchimp segment ID"
 msgstr ""
 
-#: basxconnect/mailer_integration/dynamic_preferences_registry.py:42
+#: basxconnect/mailer_integration/dynamic_preferences_registry.py:38
 msgid "Mailchimp interests category ID"
 msgstr ""
 
-#: basxconnect/mailer_integration/dynamic_preferences_registry.py:50
+#: basxconnect/mailer_integration/dynamic_preferences_registry.py:46
 msgid "Mailchimp tag"
 msgstr ""
 
-#: basxconnect/mailer_integration/dynamic_preferences_registry.py:58
+#: basxconnect/mailer_integration/dynamic_preferences_registry.py:54
 msgid "BasxConnect Mailchimp tag"
 msgstr ""
 
-#: basxconnect/mailer_integration/dynamic_preferences_registry.py:66
+#: basxconnect/mailer_integration/dynamic_preferences_registry.py:62
 msgid "Mailchimp API key"
 msgstr ""
 
-#: basxconnect/mailer_integration/dynamic_preferences_registry.py:74
-msgid "synchronize preferred language of contact with Mailchimp"
-msgstr ""
-
 #: basxconnect/mailer_integration/help.py:8
 #: basxconnect/mailer_integration/views.py:69
 msgid "Help"
 msgstr ""
 
 #: basxconnect/mailer_integration/help.py:10
 msgid ""
```

### Comparing `basxconnect-0.4.6/basxconnect/mailer_integration/locale/fr/LC_MESSAGES/django.po` & `basxconnect-0.4.7/basxconnect/mailer_integration/locale/fr/LC_MESSAGES/django.po`

 * *Files 1% similar despite different names*

```diff
@@ -4,60 +4,56 @@
 # FIRST AUTHOR <EMAIL@ADDRESS>, YEAR.
 #
 #, fuzzy
 msgid ""
 msgstr ""
 "Project-Id-Version: PACKAGE VERSION\n"
 "Report-Msgid-Bugs-To: \n"
-"POT-Creation-Date: 2022-06-02 14:49+0700\n"
+"POT-Creation-Date: 2022-07-24 15:47+0700\n"
 "PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE\n"
 "Last-Translator: FULL NAME <EMAIL@ADDRESS>\n"
 "Language-Team: LANGUAGE <LL@li.org>\n"
 "Language: \n"
 "MIME-Version: 1.0\n"
 "Content-Type: text/plain; charset=UTF-8\n"
 "Content-Transfer-Encoding: 8bit\n"
 "Plural-Forms: nplurals=2; plural=(n > 1);\n"
 
-#: basxconnect/mailer_integration/dynamic_preferences_registry.py:10
+#: basxconnect/mailer_integration/dynamic_preferences_registry.py:6
 msgid "Mailchimp"
 msgstr ""
 
-#: basxconnect/mailer_integration/dynamic_preferences_registry.py:18
+#: basxconnect/mailer_integration/dynamic_preferences_registry.py:14
 msgid "Mailchimp server"
 msgstr ""
 
-#: basxconnect/mailer_integration/dynamic_preferences_registry.py:26
+#: basxconnect/mailer_integration/dynamic_preferences_registry.py:22
 msgid "Mailchimp list ID"
 msgstr ""
 
-#: basxconnect/mailer_integration/dynamic_preferences_registry.py:34
+#: basxconnect/mailer_integration/dynamic_preferences_registry.py:30
 msgid "Mailchimp segment ID"
 msgstr ""
 
-#: basxconnect/mailer_integration/dynamic_preferences_registry.py:42
+#: basxconnect/mailer_integration/dynamic_preferences_registry.py:38
 msgid "Mailchimp interests category ID"
 msgstr ""
 
-#: basxconnect/mailer_integration/dynamic_preferences_registry.py:50
+#: basxconnect/mailer_integration/dynamic_preferences_registry.py:46
 msgid "Mailchimp tag"
 msgstr ""
 
-#: basxconnect/mailer_integration/dynamic_preferences_registry.py:58
+#: basxconnect/mailer_integration/dynamic_preferences_registry.py:54
 msgid "BasxConnect Mailchimp tag"
 msgstr ""
 
-#: basxconnect/mailer_integration/dynamic_preferences_registry.py:66
+#: basxconnect/mailer_integration/dynamic_preferences_registry.py:62
 msgid "Mailchimp API key"
 msgstr ""
 
-#: basxconnect/mailer_integration/dynamic_preferences_registry.py:74
-msgid "synchronize preferred language of contact with Mailchimp"
-msgstr ""
-
 #: basxconnect/mailer_integration/help.py:8
 #: basxconnect/mailer_integration/views.py:69
 msgid "Help"
 msgstr ""
 
 #: basxconnect/mailer_integration/help.py:10
 msgid ""
```

### Comparing `basxconnect-0.4.6/basxconnect/mailer_integration/locale/nb_NO/LC_MESSAGES/django.po` & `basxconnect-0.4.7/basxconnect/mailer_integration/locale/nb_NO/LC_MESSAGES/django.po`

 * *Files 1% similar despite different names*

```diff
@@ -4,59 +4,55 @@
 # FIRST AUTHOR <EMAIL@ADDRESS>, YEAR.
 #
 #, fuzzy
 msgid ""
 msgstr ""
 "Project-Id-Version: PACKAGE VERSION\n"
 "Report-Msgid-Bugs-To: \n"
-"POT-Creation-Date: 2022-06-02 14:49+0700\n"
+"POT-Creation-Date: 2022-07-24 15:47+0700\n"
 "PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE\n"
 "Last-Translator: FULL NAME <EMAIL@ADDRESS>\n"
 "Language-Team: LANGUAGE <LL@li.org>\n"
 "Language: \n"
 "MIME-Version: 1.0\n"
 "Content-Type: text/plain; charset=UTF-8\n"
 "Content-Transfer-Encoding: 8bit\n"
 
-#: basxconnect/mailer_integration/dynamic_preferences_registry.py:10
+#: basxconnect/mailer_integration/dynamic_preferences_registry.py:6
 msgid "Mailchimp"
 msgstr ""
 
-#: basxconnect/mailer_integration/dynamic_preferences_registry.py:18
+#: basxconnect/mailer_integration/dynamic_preferences_registry.py:14
 msgid "Mailchimp server"
 msgstr ""
 
-#: basxconnect/mailer_integration/dynamic_preferences_registry.py:26
+#: basxconnect/mailer_integration/dynamic_preferences_registry.py:22
 msgid "Mailchimp list ID"
 msgstr ""
 
-#: basxconnect/mailer_integration/dynamic_preferences_registry.py:34
+#: basxconnect/mailer_integration/dynamic_preferences_registry.py:30
 msgid "Mailchimp segment ID"
 msgstr ""
 
-#: basxconnect/mailer_integration/dynamic_preferences_registry.py:42
+#: basxconnect/mailer_integration/dynamic_preferences_registry.py:38
 msgid "Mailchimp interests category ID"
 msgstr ""
 
-#: basxconnect/mailer_integration/dynamic_preferences_registry.py:50
+#: basxconnect/mailer_integration/dynamic_preferences_registry.py:46
 msgid "Mailchimp tag"
 msgstr ""
 
-#: basxconnect/mailer_integration/dynamic_preferences_registry.py:58
+#: basxconnect/mailer_integration/dynamic_preferences_registry.py:54
 msgid "BasxConnect Mailchimp tag"
 msgstr ""
 
-#: basxconnect/mailer_integration/dynamic_preferences_registry.py:66
+#: basxconnect/mailer_integration/dynamic_preferences_registry.py:62
 msgid "Mailchimp API key"
 msgstr ""
 
-#: basxconnect/mailer_integration/dynamic_preferences_registry.py:74
-msgid "synchronize preferred language of contact with Mailchimp"
-msgstr ""
-
 #: basxconnect/mailer_integration/help.py:8
 #: basxconnect/mailer_integration/views.py:69
 msgid "Help"
 msgstr ""
 
 #: basxconnect/mailer_integration/help.py:10
 msgid ""
```

### Comparing `basxconnect-0.4.6/basxconnect/mailer_integration/locale/pt/LC_MESSAGES/django.po` & `basxconnect-0.4.7/basxconnect/mailer_integration/locale/pt/LC_MESSAGES/django.po`

 * *Files 1% similar despite different names*

```diff
@@ -4,60 +4,56 @@
 # FIRST AUTHOR <EMAIL@ADDRESS>, YEAR.
 #
 #, fuzzy
 msgid ""
 msgstr ""
 "Project-Id-Version: PACKAGE VERSION\n"
 "Report-Msgid-Bugs-To: \n"
-"POT-Creation-Date: 2022-06-02 14:49+0700\n"
+"POT-Creation-Date: 2022-07-24 15:47+0700\n"
 "PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE\n"
 "Last-Translator: FULL NAME <EMAIL@ADDRESS>\n"
 "Language-Team: LANGUAGE <LL@li.org>\n"
 "Language: \n"
 "MIME-Version: 1.0\n"
 "Content-Type: text/plain; charset=UTF-8\n"
 "Content-Transfer-Encoding: 8bit\n"
 "Plural-Forms: nplurals=2; plural=(n != 1);\n"
 
-#: basxconnect/mailer_integration/dynamic_preferences_registry.py:10
+#: basxconnect/mailer_integration/dynamic_preferences_registry.py:6
 msgid "Mailchimp"
 msgstr ""
 
-#: basxconnect/mailer_integration/dynamic_preferences_registry.py:18
+#: basxconnect/mailer_integration/dynamic_preferences_registry.py:14
 msgid "Mailchimp server"
 msgstr ""
 
-#: basxconnect/mailer_integration/dynamic_preferences_registry.py:26
+#: basxconnect/mailer_integration/dynamic_preferences_registry.py:22
 msgid "Mailchimp list ID"
 msgstr ""
 
-#: basxconnect/mailer_integration/dynamic_preferences_registry.py:34
+#: basxconnect/mailer_integration/dynamic_preferences_registry.py:30
 msgid "Mailchimp segment ID"
 msgstr ""
 
-#: basxconnect/mailer_integration/dynamic_preferences_registry.py:42
+#: basxconnect/mailer_integration/dynamic_preferences_registry.py:38
 msgid "Mailchimp interests category ID"
 msgstr ""
 
-#: basxconnect/mailer_integration/dynamic_preferences_registry.py:50
+#: basxconnect/mailer_integration/dynamic_preferences_registry.py:46
 msgid "Mailchimp tag"
 msgstr ""
 
-#: basxconnect/mailer_integration/dynamic_preferences_registry.py:58
+#: basxconnect/mailer_integration/dynamic_preferences_registry.py:54
 msgid "BasxConnect Mailchimp tag"
 msgstr ""
 
-#: basxconnect/mailer_integration/dynamic_preferences_registry.py:66
+#: basxconnect/mailer_integration/dynamic_preferences_registry.py:62
 msgid "Mailchimp API key"
 msgstr ""
 
-#: basxconnect/mailer_integration/dynamic_preferences_registry.py:74
-msgid "synchronize preferred language of contact with Mailchimp"
-msgstr ""
-
 #: basxconnect/mailer_integration/help.py:8
 #: basxconnect/mailer_integration/views.py:69
 msgid "Help"
 msgstr ""
 
 #: basxconnect/mailer_integration/help.py:10
 msgid ""
```

### Comparing `basxconnect-0.4.6/basxconnect/mailer_integration/locale/th/LC_MESSAGES/django.po` & `basxconnect-0.4.7/basxconnect/mailer_integration/locale/th/LC_MESSAGES/django.po`

 * *Files 3% similar despite different names*

```diff
@@ -4,70 +4,66 @@
 # FIRST AUTHOR <EMAIL@ADDRESS>, YEAR.
 #
 #, fuzzy
 msgid ""
 msgstr ""
 "Project-Id-Version: PACKAGE VERSION\n"
 "Report-Msgid-Bugs-To: \n"
-"POT-Creation-Date: 2022-06-02 14:49+0700\n"
+"POT-Creation-Date: 2022-07-24 15:47+0700\n"
 "PO-Revision-Date: 2021-11-01 12:38+0700\n"
 "Last-Translator: Saksinkarn Petchkuljinda <dward.the.2nd@gmail.com>\n"
 "Language-Team: Thai <LL@li.org>\n"
 "Language: th\n"
 "MIME-Version: 1.0\n"
 "Content-Type: text/plain; charset=UTF-8\n"
 "Content-Transfer-Encoding: 8bit\n"
 "Plural-Forms: nplurals=1; plural=0;\n"
 
-#: basxconnect/mailer_integration/dynamic_preferences_registry.py:10
+#: basxconnect/mailer_integration/dynamic_preferences_registry.py:6
 msgid "Mailchimp"
 msgstr "Mailchimp"
 
-#: basxconnect/mailer_integration/dynamic_preferences_registry.py:18
+#: basxconnect/mailer_integration/dynamic_preferences_registry.py:14
 #, fuzzy
 #| msgid "Mailchimp"
 msgid "Mailchimp server"
 msgstr "Mailchimp"
 
-#: basxconnect/mailer_integration/dynamic_preferences_registry.py:26
+#: basxconnect/mailer_integration/dynamic_preferences_registry.py:22
 #, fuzzy
 #| msgid "Mailchimp"
 msgid "Mailchimp list ID"
 msgstr "Mailchimp"
 
-#: basxconnect/mailer_integration/dynamic_preferences_registry.py:34
+#: basxconnect/mailer_integration/dynamic_preferences_registry.py:30
 #, fuzzy
 #| msgid "Mailchimp"
 msgid "Mailchimp segment ID"
 msgstr "Mailchimp"
 
-#: basxconnect/mailer_integration/dynamic_preferences_registry.py:42
+#: basxconnect/mailer_integration/dynamic_preferences_registry.py:38
 msgid "Mailchimp interests category ID"
 msgstr ""
 
-#: basxconnect/mailer_integration/dynamic_preferences_registry.py:50
+#: basxconnect/mailer_integration/dynamic_preferences_registry.py:46
 #, fuzzy
 #| msgid "Mailchimp"
 msgid "Mailchimp tag"
 msgstr "Mailchimp"
 
-#: basxconnect/mailer_integration/dynamic_preferences_registry.py:58
+#: basxconnect/mailer_integration/dynamic_preferences_registry.py:54
 msgid "BasxConnect Mailchimp tag"
 msgstr ""
 
-#: basxconnect/mailer_integration/dynamic_preferences_registry.py:66
+#: basxconnect/mailer_integration/dynamic_preferences_registry.py:62
 #, fuzzy
 #| msgid "Mailchimp"
 msgid "Mailchimp API key"
 msgstr "Mailchimp"
 
-#: basxconnect/mailer_integration/dynamic_preferences_registry.py:74
-msgid "synchronize preferred language of contact with Mailchimp"
-msgstr ""
-
 #: basxconnect/mailer_integration/help.py:8
 #: basxconnect/mailer_integration/views.py:69
 msgid "Help"
 msgstr ""
 
 #: basxconnect/mailer_integration/help.py:10
 msgid ""
```

### Comparing `basxconnect-0.4.6/basxconnect/mailer_integration/mailchimp/mailer.py` & `basxconnect-0.4.7/basxconnect/mailer_integration/mailchimp/mailer.py`

 * *Files identical despite different names*

### Comparing `basxconnect-0.4.6/basxconnect/mailer_integration/mailchimp/parsing.py` & `basxconnect-0.4.7/basxconnect/mailer_integration/mailchimp/parsing.py`

 * *Files identical despite different names*

### Comparing `basxconnect-0.4.6/basxconnect/mailer_integration/migrations/0001_initial.py` & `basxconnect-0.4.7/basxconnect/mailer_integration/migrations/0001_initial.py`

 * *Files identical despite different names*

### Comparing `basxconnect-0.4.6/basxconnect/mailer_integration/migrations/0004_auto_20210823_1424.py` & `basxconnect-0.4.7/basxconnect/mailer_integration/migrations/0004_auto_20210823_1424.py`

 * *Files identical despite different names*

### Comparing `basxconnect-0.4.6/basxconnect/mailer_integration/migrations/0005_alter_mailingpreferences_email.py` & `basxconnect-0.4.7/basxconnect/mailer_integration/migrations/0005_alter_mailingpreferences_email.py`

 * *Files identical despite different names*

### Comparing `basxconnect-0.4.6/basxconnect/mailer_integration/migrations/0006_alter_mailingpreferences_status.py` & `basxconnect-0.4.7/basxconnect/mailer_integration/migrations/0006_alter_mailingpreferences_status.py`

 * *Files identical despite different names*

### Comparing `basxconnect-0.4.6/basxconnect/mailer_integration/migrations/0008_alter_mailingpreferences_email.py` & `basxconnect-0.4.7/basxconnect/mailer_integration/migrations/0008_alter_mailingpreferences_email.py`

 * *Files identical despite different names*

### Comparing `basxconnect-0.4.6/basxconnect/mailer_integration/migrations/0009_alter_mailingpreferences_email.py` & `basxconnect-0.4.7/basxconnect/mailer_integration/migrations/0009_alter_mailingpreferences_email.py`

 * *Files identical despite different names*

### Comparing `basxconnect-0.4.6/basxconnect/mailer_integration/migrations/0010_mailingpreferences_language.py` & `basxconnect-0.4.7/basxconnect/mailer_integration/migrations/0010_mailingpreferences_language.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 # Generated by Django 3.2.4 on 2021-11-02 07:33
 
-from bread.contrib import languages
+from basxbread.contrib import languages
 from django.db import migrations
 
 
 class Migration(migrations.Migration):
 
     dependencies = [
         ("mailer_integration", "0009_alter_mailingpreferences_email"),
```

### Comparing `basxconnect-0.4.6/basxconnect/mailer_integration/migrations/0011_invalidperson_newperson_synchronizationresult.py` & `basxconnect-0.4.7/basxconnect/mailer_integration/migrations/0011_invalidperson_newperson_synchronizationresult.py`

 * *Files identical despite different names*

### Comparing `basxconnect-0.4.6/basxconnect/mailer_integration/migrations/0012_auto_20211119_0830.py` & `basxconnect-0.4.7/basxconnect/mailer_integration/migrations/0012_auto_20211119_0830.py`

 * *Files identical despite different names*

### Comparing `basxconnect-0.4.6/basxconnect/mailer_integration/migrations/0013_mailingpreferences_latest_sync.py` & `basxconnect-0.4.7/basxconnect/mailer_integration/migrations/0013_mailingpreferences_latest_sync.py`

 * *Files identical despite different names*

### Comparing `basxconnect-0.4.6/basxconnect/mailer_integration/migrations/0017_auto_20211122_1219.py` & `basxconnect-0.4.7/basxconnect/mailer_integration/migrations/0017_auto_20211122_1219.py`

 * *Files identical despite different names*

### Comparing `basxconnect-0.4.6/basxconnect/mailer_integration/migrations/0018_alter_synchronizationperson_sync_status.py` & `basxconnect-0.4.7/basxconnect/mailer_integration/migrations/0018_alter_synchronizationperson_sync_status.py`

 * *Files identical despite different names*

### Comparing `basxconnect-0.4.6/basxconnect/mailer_integration/migrations/0019_auto_20211210_1602.py` & `basxconnect-0.4.7/basxconnect/mailer_integration/migrations/0019_auto_20211210_1602.py`

 * *Files identical despite different names*

### Comparing `basxconnect-0.4.6/basxconnect/mailer_integration/migrations/0021_auto_20220106_0917.py` & `basxconnect-0.4.7/basxconnect/mailer_integration/migrations/0021_auto_20220106_0917.py`

 * *Files identical despite different names*

### Comparing `basxconnect-0.4.6/basxconnect/mailer_integration/migrations/0022_auto_20220118_1308.py` & `basxconnect-0.4.7/basxconnect/mailer_integration/migrations/0022_auto_20220118_1308.py`

 * *Files identical despite different names*

### Comparing `basxconnect-0.4.6/basxconnect/mailer_integration/migrations/0023_auto_20220517_1700.py` & `basxconnect-0.4.7/basxconnect/mailer_integration/migrations/0023_auto_20220517_1700.py`

 * *Files identical despite different names*

### Comparing `basxconnect-0.4.6/basxconnect/mailer_integration/models.py` & `basxconnect-0.4.7/basxconnect/mailer_integration/models.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-from bread.contrib.languages.fields import LanguageField
+from basxbread.contrib.languages.fields import LanguageField
 from django.db import models
 from django.utils.translation import gettext_lazy as _
 
 from basxconnect.core.models import Email
 
 
 class Interest(models.Model):
```

### Comparing `basxconnect-0.4.6/basxconnect/mailer_integration/signal_handlers.py` & `basxconnect-0.4.7/basxconnect/mailer_integration/signal_handlers.py`

 * *Files identical despite different names*

### Comparing `basxconnect-0.4.6/basxconnect/mailer_integration/synchronize.py` & `basxconnect-0.4.7/basxconnect/mailer_integration/synchronize.py`

 * *Files identical despite different names*

### Comparing `basxconnect-0.4.6/basxconnect/mailer_integration/urls.py` & `basxconnect-0.4.7/basxconnect/mailer_integration/urls.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-from bread.utils.urls import autopath, default_model_paths, model_urlname
+from basxbread.utils.urls import autopath, default_model_paths, model_urlname
 
 import basxconnect.mailer_integration.views
 from basxconnect.mailer_integration import models
 
 urlpatterns = [
     autopath(basxconnect.mailer_integration.views.mailer_synchronization_view),
     autopath(
```

### Comparing `basxconnect-0.4.6/basxconnect/mailer_integration/views.py` & `basxconnect-0.4.7/basxconnect/mailer_integration/views.py`

 * *Files 8% similar despite different names*

```diff
@@ -1,66 +1,66 @@
 import traceback
 
-import bread.layout.components.notification
+import basxbread.layout.components.notification
 import htmlgenerator as hg
-from bread import layout, menu
-from bread.layout.components.datatable import DataTableColumn
-from bread.layout.components.forms import Form
-from bread.utils import aslayout, reverse_model
-from bread.utils.links import Link, ModelHref
-from bread.views import AddView, EditView
+from basxbread import layout, menu
+from basxbread.layout.components.datatable import DataTableColumn
+from basxbread.layout.components.forms import Form
+from basxbread.utils import aslayout, reverse_model
+from basxbread.utils.links import Link, ModelHref
+from basxbread.views import AddView, EditView
 from django import forms
 from django.urls import reverse_lazy
 from django.utils.translation import gettext_lazy as _
 
 from basxconnect.mailer_integration import settings
 from basxconnect.mailer_integration.abstract.mailer import MailerPerson
 from basxconnect.mailer_integration.help import sync_help_modal
 from basxconnect.mailer_integration.models import (
     SynchronizationPerson,
     SynchronizationResult,
 )
 from basxconnect.mailer_integration.synchronize import synchronize
 
-C = bread.layout.grid.Col
-R = bread.layout.grid.Row
+C = basxbread.layout.grid.Col
+R = basxbread.layout.grid.Row
 
 
 @aslayout
 def mailer_synchronization_view(request):
     if request.method == "POST":
         try:
             sync_result = synchronize(settings.MAILER)
-            notification = bread.layout.components.notification.InlineNotification(
+            notification = basxbread.layout.components.notification.InlineNotification(
                 _("Sychronization successful"),
                 _(
                     "Synchronized with mailer segment containing %s contacts. %s new persons were added to BasxConnect."
                 )
                 % (
                     sync_result.total_synchronized_persons,
                     sync_result.persons.filter(
                         sync_status=SynchronizationPerson.NEW
                     ).count(),
                 ),
                 kind="success",
             )
         except Exception:
-            notification = bread.layout.components.notification.InlineNotification(
+            notification = basxbread.layout.components.notification.InlineNotification(
                 "Error",
                 f"An error occured during synchronization. {traceback.format_exc()}",
                 kind="error",
             )
     else:
         notification = None
 
     help_modal = sync_help_modal()
     return hg.BaseElement(
         Form(
             forms.Form(),
-            bread.layout.grid.Grid(
+            basxbread.layout.grid.Grid(
                 hg.H3(_("Synchronization of Email Subcriptions")),
                 notification,
                 gutter=False,
             ),
             help_modal,
             layout.forms.helpers.Submit(
                 _("Download subscriptions"), style="display: inline-block;"
```

### Comparing `basxconnect-0.4.6/basxconnect.egg-info/PKG-INFO` & `basxconnect-0.4.7/basxconnect.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: basxconnect
-Version: 0.4.6
+Version: 0.4.7
 Summary: CRM application for non-profit organizations
 Home-page: https://github.com/basxsoftwareassociation/basxconnect
 Author: basx Software Association
 Author-email: sam@basx.dev
 License: New BSD License
 Platform: UNKNOWN
 Classifier: Development Status :: 4 - Beta
```

### Comparing `basxconnect-0.4.6/basxconnect.egg-info/SOURCES.txt` & `basxconnect-0.4.7/basxconnect.egg-info/SOURCES.txt`

 * *Files 1% similar despite different names*

```diff
@@ -48,15 +48,17 @@
 basxconnect/core/layouts/__init__.py
 basxconnect/core/layouts/settings_layout.py
 basxconnect/core/layouts/editperson/__init__.py
 basxconnect/core/layouts/editperson/common/__init__.py
 basxconnect/core/layouts/editperson/common/addresses.py
 basxconnect/core/layouts/editperson/common/base_data.py
 basxconnect/core/layouts/editperson/common/contributions_tab.py
+basxconnect/core/layouts/editperson/common/documenttemplates_tab.py
 basxconnect/core/layouts/editperson/common/head.py
+basxconnect/core/layouts/editperson/common/history_tab.py
 basxconnect/core/layouts/editperson/common/relationships_tab.py
 basxconnect/core/layouts/editperson/common/utils.py
 basxconnect/core/layouts/editperson/legalperson/__init__.py
 basxconnect/core/layouts/editperson/legalperson/base_data_tab.py
 basxconnect/core/layouts/editperson/legalperson/mailing.py
 basxconnect/core/layouts/editperson/naturalperson/__init__.py
 basxconnect/core/layouts/editperson/naturalperson/base_data_tab.py
```

### Comparing `basxconnect-0.4.6/manage.py` & `basxconnect-0.4.7/manage.py`

 * *Files 12% similar despite different names*

```diff
@@ -9,15 +9,15 @@
 if "test" in sys.argv:
     os.environ.setdefault("DJANGO_SETTINGS_MODULE", "basxconnect.core.tests.settings")
 else:
     INSTALLED_APPS = [
         "django.contrib.auth",
         "django.contrib.contenttypes",
         "django.contrib.sites",
-        "bread",
+        "basxbread",
         "djmoney",
         "basxconnect.core",
         "basxconnect.contributions",
         "basxconnect.mailer_integration",
     ]
     settings.configure(
         DEBUG=True,
```

### Comparing `basxconnect-0.4.6/setup.py` & `basxconnect-0.4.7/setup.py`

 * *Files identical despite different names*

