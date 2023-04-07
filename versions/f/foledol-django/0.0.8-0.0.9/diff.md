# Comparing `tmp/foledol-django-0.0.8.tar.gz` & `tmp/foledol-django-0.0.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "/Users/lde/foledol/django/dist/tmp3ouyykwd/foledol-django-0.0.8.tar", last modified: Wed Feb  9 13:57:48 2022, max compression
+gzip compressed data, was "/Users/lde/foledol/django/dist/tmp6a857d0g/foledol-django-0.0.9.tar", last modified: Fri Feb 11 12:46:32 2022, max compression
```

## Comparing `foledol-django-0.0.8.tar` & `foledol-django-0.0.9.tar`

### file list

```diff
@@ -1,89 +1,104 @@
-drwxr-xr-x   0 lde        (502) staff       (20)        0 2022-02-09 13:57:48.000000 foledol-django-0.0.8/
--rw-r--r--   0 lde        (502) staff       (20)     1073 2022-02-04 10:23:15.000000 foledol-django-0.0.8/LICENSE
--rw-r--r--   0 lde        (502) staff       (20)      129 2022-02-07 21:01:06.000000 foledol-django-0.0.8/MANIFEST.in
--rw-r--r--   0 lde        (502) staff       (20)      472 2022-02-09 13:57:48.000000 foledol-django-0.0.8/PKG-INFO
--rw-r--r--   0 lde        (502) staff       (20)       59 2022-02-06 15:03:04.000000 foledol-django-0.0.8/README.md
--rw-r--r--   0 lde        (502) staff       (20)      136 2022-02-04 21:46:36.000000 foledol-django-0.0.8/pyproject.toml
--rw-r--r--   0 lde        (502) staff       (20)      501 2022-02-09 13:57:48.000000 foledol-django-0.0.8/setup.cfg
--rw-r--r--   0 lde        (502) staff       (20)      211 2022-02-04 22:20:16.000000 foledol-django-0.0.8/setup.py
-drwxr-xr-x   0 lde        (502) staff       (20)        0 2022-02-09 13:57:48.000000 foledol-django-0.0.8/src/
-drwxr-xr-x   0 lde        (502) staff       (20)        0 2022-02-09 13:57:48.000000 foledol-django-0.0.8/src/foledol/
--rw-r--r--   0 lde        (502) staff       (20)        0 2022-02-09 13:56:15.000000 foledol-django-0.0.8/src/foledol/__init__.py
-drwxr-xr-x   0 lde        (502) staff       (20)        0 2022-02-09 13:57:48.000000 foledol-django-0.0.8/src/foledol/django/
--rw-r--r--   0 lde        (502) staff       (20)        0 2022-02-09 13:56:15.000000 foledol-django-0.0.8/src/foledol/django/__init__.py
--rw-r--r--   0 lde        (502) staff       (20)       87 2022-02-09 13:56:15.000000 foledol-django-0.0.8/src/foledol/django/apps.py
--rw-r--r--   0 lde        (502) staff       (20)      868 2022-02-09 13:56:15.000000 foledol-django-0.0.8/src/foledol/django/logger.py
--rw-r--r--   0 lde        (502) staff       (20)     4869 2022-02-09 13:56:16.000000 foledol-django-0.0.8/src/foledol/django/meta.py
-drwxr-xr-x   0 lde        (502) staff       (20)        0 2022-02-09 13:57:48.000000 foledol-django-0.0.8/src/foledol/django/migrations/
--rw-r--r--   0 lde        (502) staff       (20)     1724 2022-02-09 13:56:15.000000 foledol-django-0.0.8/src/foledol/django/migrations/0001_initial.py
--rw-r--r--   0 lde        (502) staff       (20)        0 2022-02-09 13:56:15.000000 foledol-django-0.0.8/src/foledol/django/migrations/__init__.py
--rw-r--r--   0 lde        (502) staff       (20)     1138 2022-02-09 13:56:15.000000 foledol-django-0.0.8/src/foledol/django/models.py
-drwxr-xr-x   0 lde        (502) staff       (20)        0 2022-02-09 13:57:48.000000 foledol-django-0.0.8/src/foledol/django/templates/
--rw-r--r--   0 lde        (502) staff       (20)     6148 2022-02-09 13:56:15.000000 foledol-django-0.0.8/src/foledol/django/templates/.DS_Store
-drwxr-xr-x   0 lde        (502) staff       (20)        0 2022-02-09 13:57:48.000000 foledol-django-0.0.8/src/foledol/django/templates/common/
--rw-r--r--   0 lde        (502) staff       (20)      852 2022-02-09 13:56:16.000000 foledol-django-0.0.8/src/foledol/django/templates/common/archive.html
--rw-r--r--   0 lde        (502) staff       (20)      911 2022-02-09 13:56:16.000000 foledol-django-0.0.8/src/foledol/django/templates/common/delete.html
--rw-r--r--   0 lde        (502) staff       (20)      127 2022-02-09 13:56:16.000000 foledol-django-0.0.8/src/foledol/django/templates/common/error.html
--rw-r--r--   0 lde        (502) staff       (20)     1121 2022-02-09 13:56:16.000000 foledol-django-0.0.8/src/foledol/django/templates/common/print.html
-drwxr-xr-x   0 lde        (502) staff       (20)        0 2022-02-09 13:57:48.000000 foledol-django-0.0.8/src/foledol/django/templates/components/
--rw-r--r--   0 lde        (502) staff       (20)      341 2022-02-09 13:56:15.000000 foledol-django-0.0.8/src/foledol/django/templates/components/banners.html
--rw-r--r--   0 lde        (502) staff       (20)      395 2022-02-09 13:56:15.000000 foledol-django-0.0.8/src/foledol/django/templates/components/field_check.html
--rw-r--r--   0 lde        (502) staff       (20)      284 2022-02-09 13:56:15.000000 foledol-django-0.0.8/src/foledol/django/templates/components/field_check_new.html
--rw-r--r--   0 lde        (502) staff       (20)      414 2022-02-09 13:56:15.000000 foledol-django-0.0.8/src/foledol/django/templates/components/field_check_short.html
--rw-r--r--   0 lde        (502) staff       (20)     1191 2022-02-09 13:56:15.000000 foledol-django-0.0.8/src/foledol/django/templates/components/field_city.html
--rw-r--r--   0 lde        (502) staff       (20)     1661 2022-02-09 13:56:15.000000 foledol-django-0.0.8/src/foledol/django/templates/components/field_country.html
--rw-r--r--   0 lde        (502) staff       (20)      541 2022-02-09 13:56:15.000000 foledol-django-0.0.8/src/foledol/django/templates/components/field_date.html
--rw-r--r--   0 lde        (502) staff       (20)      441 2022-02-09 13:56:15.000000 foledol-django-0.0.8/src/foledol/django/templates/components/field_date_short.html
--rw-r--r--   0 lde        (502) staff       (20)      652 2022-02-09 13:56:15.000000 foledol-django-0.0.8/src/foledol/django/templates/components/field_select.html
--rw-r--r--   0 lde        (502) staff       (20)      835 2022-02-09 13:56:15.000000 foledol-django-0.0.8/src/foledol/django/templates/components/field_select_short.html
--rw-r--r--   0 lde        (502) staff       (20)      632 2022-02-09 13:56:15.000000 foledol-django-0.0.8/src/foledol/django/templates/components/field_text.html
--rw-r--r--   0 lde        (502) staff       (20)      547 2022-02-09 13:56:15.000000 foledol-django-0.0.8/src/foledol/django/templates/components/field_text_area.html
--rw-r--r--   0 lde        (502) staff       (20)      586 2022-02-09 13:56:15.000000 foledol-django-0.0.8/src/foledol/django/templates/components/field_text_area_short.html
--rw-r--r--   0 lde        (502) staff       (20)     2519 2022-02-09 13:56:15.000000 foledol-django-0.0.8/src/foledol/django/templates/components/field_text_short.html
--rw-r--r--   0 lde        (502) staff       (20)     1192 2022-02-09 13:56:15.000000 foledol-django-0.0.8/src/foledol/django/templates/components/field_zip.html
--rw-r--r--   0 lde        (502) staff       (20)     2716 2022-02-09 13:56:15.000000 foledol-django-0.0.8/src/foledol/django/templates/components/grid.html
--rw-r--r--   0 lde        (502) staff       (20)     1090 2022-02-09 13:56:15.000000 foledol-django-0.0.8/src/foledol/django/templates/components/grid_column.html
--rw-r--r--   0 lde        (502) staff       (20)      779 2022-02-09 13:56:15.000000 foledol-django-0.0.8/src/foledol/django/templates/components/grid_row.html
--rw-r--r--   0 lde        (502) staff       (20)      258 2022-02-09 13:56:15.000000 foledol-django-0.0.8/src/foledol/django/templates/components/list.html
--rw-r--r--   0 lde        (502) staff       (20)      700 2022-02-09 13:56:15.000000 foledol-django-0.0.8/src/foledol/django/templates/components/logs.html
--rw-r--r--   0 lde        (502) staff       (20)      466 2022-02-09 13:56:15.000000 foledol-django-0.0.8/src/foledol/django/templates/components/meta.html
--rw-r--r--   0 lde        (502) staff       (20)     1235 2022-02-09 13:56:15.000000 foledol-django-0.0.8/src/foledol/django/templates/components/navigator.html
--rw-r--r--   0 lde        (502) staff       (20)      450 2022-02-09 13:56:15.000000 foledol-django-0.0.8/src/foledol/django/templates/components/navigator_inputs.html
--rw-r--r--   0 lde        (502) staff       (20)     2869 2022-02-09 13:56:15.000000 foledol-django-0.0.8/src/foledol/django/templates/components/paginator.html
--rw-r--r--   0 lde        (502) staff       (20)      260 2022-02-09 13:56:15.000000 foledol-django-0.0.8/src/foledol/django/templates/components/report.html
--rw-r--r--   0 lde        (502) staff       (20)     6617 2022-02-09 13:56:15.000000 foledol-django-0.0.8/src/foledol/django/templates/components/table.html
--rw-r--r--   0 lde        (502) staff       (20)      135 2022-02-09 13:56:15.000000 foledol-django-0.0.8/src/foledol/django/templates/components/table_column.html
--rw-r--r--   0 lde        (502) staff       (20)      497 2022-02-09 13:56:15.000000 foledol-django-0.0.8/src/foledol/django/templates/components/table_header.html
--rw-r--r--   0 lde        (502) staff       (20)     1912 2022-02-09 13:56:15.000000 foledol-django-0.0.8/src/foledol/django/templates/components/upload.html
--rw-r--r--   0 lde        (502) staff       (20)     2379 2022-02-09 13:56:16.000000 foledol-django-0.0.8/src/foledol/django/templates/log.html
--rw-r--r--   0 lde        (502) staff       (20)      509 2022-02-09 13:56:16.000000 foledol-django-0.0.8/src/foledol/django/templates/log_events.html
--rw-r--r--   0 lde        (502) staff       (20)      681 2022-02-09 13:56:16.000000 foledol-django-0.0.8/src/foledol/django/templates/logs.html
-drwxr-xr-x   0 lde        (502) staff       (20)        0 2022-02-09 13:57:48.000000 foledol-django-0.0.8/src/foledol/django/templatetags/
--rw-r--r--   0 lde        (502) staff       (20)        0 2022-02-09 13:56:15.000000 foledol-django-0.0.8/src/foledol/django/templatetags/__init__.py
--rw-r--r--   0 lde        (502) staff       (20)      703 2022-02-09 13:56:15.000000 foledol-django-0.0.8/src/foledol/django/templatetags/custom.py
--rw-r--r--   0 lde        (502) staff       (20)      564 2022-02-09 13:56:15.000000 foledol-django-0.0.8/src/foledol/django/templatetags/date_extras.py
--rw-r--r--   0 lde        (502) staff       (20)     1780 2022-02-09 13:56:15.000000 foledol-django-0.0.8/src/foledol/django/templatetags/form_extras.py
--rw-r--r--   0 lde        (502) staff       (20)     3986 2022-02-09 13:56:15.000000 foledol-django-0.0.8/src/foledol/django/test.py
-drwxr-xr-x   0 lde        (502) staff       (20)        0 2022-02-09 13:57:48.000000 foledol-django-0.0.8/src/foledol/django/tools/
--rw-r--r--   0 lde        (502) staff       (20)        0 2022-02-09 13:56:15.000000 foledol-django-0.0.8/src/foledol/django/tools/__init__.py
--rw-r--r--   0 lde        (502) staff       (20)      960 2022-02-09 13:56:15.000000 foledol-django-0.0.8/src/foledol/django/tools/barcode.py
--rw-r--r--   0 lde        (502) staff       (20)     1632 2022-02-09 13:56:15.000000 foledol-django-0.0.8/src/foledol/django/tools/canvas.py
--rw-r--r--   0 lde        (502) staff       (20)     1317 2022-02-09 13:56:15.000000 foledol-django-0.0.8/src/foledol/django/tools/chart.py
--rw-r--r--   0 lde        (502) staff       (20)     6834 2022-02-09 13:56:15.000000 foledol-django-0.0.8/src/foledol/django/tools/field.py
--rw-r--r--   0 lde        (502) staff       (20)      293 2022-02-09 13:56:15.000000 foledol-django-0.0.8/src/foledol/django/tools/filter.py
--rw-r--r--   0 lde        (502) staff       (20)     1970 2022-02-09 13:56:15.000000 foledol-django-0.0.8/src/foledol/django/tools/form.py
--rw-r--r--   0 lde        (502) staff       (20)      942 2022-02-09 13:56:15.000000 foledol-django-0.0.8/src/foledol/django/tools/handlers.py
--rw-r--r--   0 lde        (502) staff       (20)     1056 2022-02-09 13:56:15.000000 foledol-django-0.0.8/src/foledol/django/tools/readers.py
--rw-r--r--   0 lde        (502) staff       (20)     4077 2022-02-09 13:56:15.000000 foledol-django-0.0.8/src/foledol/django/tools/report.py
--rw-r--r--   0 lde        (502) staff       (20)     1166 2022-02-09 13:56:15.000000 foledol-django-0.0.8/src/foledol/django/tools/table.py
--rw-r--r--   0 lde        (502) staff       (20)     2414 2022-02-09 13:56:15.000000 foledol-django-0.0.8/src/foledol/django/tools/writer.py
--rw-r--r--   0 lde        (502) staff       (20)      417 2022-02-09 13:56:16.000000 foledol-django-0.0.8/src/foledol/django/urls.py
--rw-r--r--   0 lde        (502) staff       (20)    12112 2022-02-09 13:56:15.000000 foledol-django-0.0.8/src/foledol/django/utils.py
-drwxr-xr-x   0 lde        (502) staff       (20)        0 2022-02-09 13:57:48.000000 foledol-django-0.0.8/src/foledol/django/views/
--rw-r--r--   0 lde        (502) staff       (20)        0 2022-02-09 13:56:16.000000 foledol-django-0.0.8/src/foledol/django/views/__init__.py
--rw-r--r--   0 lde        (502) staff       (20)     5260 2022-02-09 13:56:16.000000 foledol-django-0.0.8/src/foledol/django/views/logs.py
-drwxr-xr-x   0 lde        (502) staff       (20)        0 2022-02-09 13:57:48.000000 foledol-django-0.0.8/src/foledol_django.egg-info/
--rw-r--r--   0 lde        (502) staff       (20)      472 2022-02-09 13:57:48.000000 foledol-django-0.0.8/src/foledol_django.egg-info/PKG-INFO
--rw-r--r--   0 lde        (502) staff       (20)     3235 2022-02-09 13:57:48.000000 foledol-django-0.0.8/src/foledol_django.egg-info/SOURCES.txt
--rw-r--r--   0 lde        (502) staff       (20)        1 2022-02-09 13:57:48.000000 foledol-django-0.0.8/src/foledol_django.egg-info/dependency_links.txt
--rw-r--r--   0 lde        (502) staff       (20)        8 2022-02-09 13:57:48.000000 foledol-django-0.0.8/src/foledol_django.egg-info/top_level.txt
+drwxr-xr-x   0 lde        (502) staff       (20)        0 2022-02-11 12:46:32.000000 foledol-django-0.0.9/
+-rw-r--r--   0 lde        (502) staff       (20)     1073 2022-02-04 10:23:15.000000 foledol-django-0.0.9/LICENSE
+-rw-r--r--   0 lde        (502) staff       (20)      129 2022-02-07 21:01:06.000000 foledol-django-0.0.9/MANIFEST.in
+-rw-r--r--   0 lde        (502) staff       (20)      472 2022-02-11 12:46:32.000000 foledol-django-0.0.9/PKG-INFO
+-rw-r--r--   0 lde        (502) staff       (20)       59 2022-02-06 15:03:04.000000 foledol-django-0.0.9/README.md
+-rw-r--r--   0 lde        (502) staff       (20)      136 2022-02-04 21:46:36.000000 foledol-django-0.0.9/pyproject.toml
+-rw-r--r--   0 lde        (502) staff       (20)      501 2022-02-11 12:46:32.000000 foledol-django-0.0.9/setup.cfg
+-rw-r--r--   0 lde        (502) staff       (20)      211 2022-02-04 22:20:16.000000 foledol-django-0.0.9/setup.py
+drwxr-xr-x   0 lde        (502) staff       (20)        0 2022-02-11 12:46:32.000000 foledol-django-0.0.9/src/
+drwxr-xr-x   0 lde        (502) staff       (20)        0 2022-02-11 12:46:32.000000 foledol-django-0.0.9/src/foledol/
+-rw-r--r--   0 lde        (502) staff       (20)        0 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/__init__.py
+drwxr-xr-x   0 lde        (502) staff       (20)        0 2022-02-11 12:46:32.000000 foledol-django-0.0.9/src/foledol/django/
+-rw-r--r--   0 lde        (502) staff       (20)        0 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/__init__.py
+-rw-r--r--   0 lde        (502) staff       (20)       87 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/apps.py
+-rw-r--r--   0 lde        (502) staff       (20)     1269 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/auth.py
+-rw-r--r--   0 lde        (502) staff       (20)      868 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/logger.py
+-rw-r--r--   0 lde        (502) staff       (20)     4869 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/meta.py
+drwxr-xr-x   0 lde        (502) staff       (20)        0 2022-02-11 12:46:32.000000 foledol-django-0.0.9/src/foledol/django/migrations/
+-rw-r--r--   0 lde        (502) staff       (20)     1724 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/migrations/0001_initial.py
+-rw-r--r--   0 lde        (502) staff       (20)     2142 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/migrations/0002_auto_20220211_0730.py
+-rw-r--r--   0 lde        (502) staff       (20)        0 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/migrations/__init__.py
+-rw-r--r--   0 lde        (502) staff       (20)     7438 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/models.py
+drwxr-xr-x   0 lde        (502) staff       (20)        0 2022-02-11 12:46:32.000000 foledol-django-0.0.9/src/foledol/django/reports/
+-rw-r--r--   0 lde        (502) staff       (20)        0 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/reports/__init__.py
+-rw-r--r--   0 lde        (502) staff       (20)     2937 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/reports/grid.py
+drwxr-xr-x   0 lde        (502) staff       (20)        0 2022-02-11 12:46:32.000000 foledol-django-0.0.9/src/foledol/django/templates/
+-rw-r--r--   0 lde        (502) staff       (20)     6148 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/templates/.DS_Store
+-rw-r--r--   0 lde        (502) staff       (20)     2601 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/templates/column.html
+-rw-r--r--   0 lde        (502) staff       (20)      374 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/templates/columns.html
+drwxr-xr-x   0 lde        (502) staff       (20)        0 2022-02-11 12:46:32.000000 foledol-django-0.0.9/src/foledol/django/templates/common/
+-rw-r--r--   0 lde        (502) staff       (20)      852 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/templates/common/archive.html
+-rw-r--r--   0 lde        (502) staff       (20)      911 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/templates/common/delete.html
+-rw-r--r--   0 lde        (502) staff       (20)      127 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/templates/common/error.html
+-rw-r--r--   0 lde        (502) staff       (20)     1121 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/templates/common/print.html
+drwxr-xr-x   0 lde        (502) staff       (20)        0 2022-02-11 12:46:32.000000 foledol-django-0.0.9/src/foledol/django/templates/components/
+-rw-r--r--   0 lde        (502) staff       (20)      341 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/templates/components/banners.html
+-rw-r--r--   0 lde        (502) staff       (20)      395 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/templates/components/field_check.html
+-rw-r--r--   0 lde        (502) staff       (20)      284 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/templates/components/field_check_new.html
+-rw-r--r--   0 lde        (502) staff       (20)      414 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/templates/components/field_check_short.html
+-rw-r--r--   0 lde        (502) staff       (20)     1191 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/templates/components/field_city.html
+-rw-r--r--   0 lde        (502) staff       (20)     1661 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/templates/components/field_country.html
+-rw-r--r--   0 lde        (502) staff       (20)      541 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/templates/components/field_date.html
+-rw-r--r--   0 lde        (502) staff       (20)      441 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/templates/components/field_date_short.html
+-rw-r--r--   0 lde        (502) staff       (20)      652 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/templates/components/field_select.html
+-rw-r--r--   0 lde        (502) staff       (20)      835 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/templates/components/field_select_short.html
+-rw-r--r--   0 lde        (502) staff       (20)      632 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/templates/components/field_text.html
+-rw-r--r--   0 lde        (502) staff       (20)      547 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/templates/components/field_text_area.html
+-rw-r--r--   0 lde        (502) staff       (20)      586 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/templates/components/field_text_area_short.html
+-rw-r--r--   0 lde        (502) staff       (20)     2519 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/templates/components/field_text_short.html
+-rw-r--r--   0 lde        (502) staff       (20)     1192 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/templates/components/field_zip.html
+-rw-r--r--   0 lde        (502) staff       (20)     2716 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/templates/components/grid.html
+-rw-r--r--   0 lde        (502) staff       (20)     1090 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/templates/components/grid_column.html
+-rw-r--r--   0 lde        (502) staff       (20)      779 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/templates/components/grid_row.html
+-rw-r--r--   0 lde        (502) staff       (20)      258 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/templates/components/list.html
+-rw-r--r--   0 lde        (502) staff       (20)      700 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/templates/components/logs.html
+-rw-r--r--   0 lde        (502) staff       (20)      466 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/templates/components/meta.html
+-rw-r--r--   0 lde        (502) staff       (20)     1235 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/templates/components/navigator.html
+-rw-r--r--   0 lde        (502) staff       (20)      450 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/templates/components/navigator_inputs.html
+-rw-r--r--   0 lde        (502) staff       (20)     2869 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/templates/components/paginator.html
+-rw-r--r--   0 lde        (502) staff       (20)      260 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/templates/components/report.html
+-rw-r--r--   0 lde        (502) staff       (20)     6617 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/templates/components/table.html
+-rw-r--r--   0 lde        (502) staff       (20)      135 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/templates/components/table_column.html
+-rw-r--r--   0 lde        (502) staff       (20)      497 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/templates/components/table_header.html
+-rw-r--r--   0 lde        (502) staff       (20)     1912 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/templates/components/upload.html
+-rw-r--r--   0 lde        (502) staff       (20)     4625 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/templates/grid.html
+-rw-r--r--   0 lde        (502) staff       (20)      372 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/templates/grids.html
+-rw-r--r--   0 lde        (502) staff       (20)     2379 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/templates/log.html
+-rw-r--r--   0 lde        (502) staff       (20)      509 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/templates/log_events.html
+-rw-r--r--   0 lde        (502) staff       (20)      681 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/templates/logs.html
+-rw-r--r--   0 lde        (502) staff       (20)      716 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/templates/user_login.html
+-rw-r--r--   0 lde        (502) staff       (20)       63 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/templates/user_logout.html
+drwxr-xr-x   0 lde        (502) staff       (20)        0 2022-02-11 12:46:32.000000 foledol-django-0.0.9/src/foledol/django/templatetags/
+-rw-r--r--   0 lde        (502) staff       (20)        0 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/templatetags/__init__.py
+-rw-r--r--   0 lde        (502) staff       (20)      703 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/templatetags/custom.py
+-rw-r--r--   0 lde        (502) staff       (20)      564 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/templatetags/date_extras.py
+-rw-r--r--   0 lde        (502) staff       (20)     1780 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/templatetags/form_extras.py
+-rw-r--r--   0 lde        (502) staff       (20)     4418 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/test.py
+drwxr-xr-x   0 lde        (502) staff       (20)        0 2022-02-11 12:46:32.000000 foledol-django-0.0.9/src/foledol/django/tools/
+-rw-r--r--   0 lde        (502) staff       (20)        0 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/tools/__init__.py
+-rw-r--r--   0 lde        (502) staff       (20)      960 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/tools/barcode.py
+-rw-r--r--   0 lde        (502) staff       (20)     1632 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/tools/canvas.py
+-rw-r--r--   0 lde        (502) staff       (20)     1317 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/tools/chart.py
+-rw-r--r--   0 lde        (502) staff       (20)     6834 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/tools/field.py
+-rw-r--r--   0 lde        (502) staff       (20)      293 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/tools/filter.py
+-rw-r--r--   0 lde        (502) staff       (20)     1970 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/tools/form.py
+-rw-r--r--   0 lde        (502) staff       (20)      942 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/tools/handlers.py
+-rw-r--r--   0 lde        (502) staff       (20)     1056 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/tools/readers.py
+-rw-r--r--   0 lde        (502) staff       (20)     4119 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/tools/report.py
+-rw-r--r--   0 lde        (502) staff       (20)     1166 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/tools/table.py
+-rw-r--r--   0 lde        (502) staff       (20)     2414 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/tools/writer.py
+-rw-r--r--   0 lde        (502) staff       (20)     1237 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/urls.py
+-rw-r--r--   0 lde        (502) staff       (20)    12733 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/utils.py
+drwxr-xr-x   0 lde        (502) staff       (20)        0 2022-02-11 12:46:32.000000 foledol-django-0.0.9/src/foledol/django/views/
+-rw-r--r--   0 lde        (502) staff       (20)        0 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/views/__init__.py
+-rw-r--r--   0 lde        (502) staff       (20)     4575 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/views/column.py
+-rw-r--r--   0 lde        (502) staff       (20)     1179 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/views/columns.py
+-rw-r--r--   0 lde        (502) staff       (20)    12811 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/views/grid.py
+-rw-r--r--   0 lde        (502) staff       (20)     1374 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/views/grids.py
+-rw-r--r--   0 lde        (502) staff       (20)     5260 2022-02-11 12:45:12.000000 foledol-django-0.0.9/src/foledol/django/views/logs.py
+drwxr-xr-x   0 lde        (502) staff       (20)        0 2022-02-11 12:46:32.000000 foledol-django-0.0.9/src/foledol_django.egg-info/
+-rw-r--r--   0 lde        (502) staff       (20)      472 2022-02-11 12:46:32.000000 foledol-django-0.0.9/src/foledol_django.egg-info/PKG-INFO
+-rw-r--r--   0 lde        (502) staff       (20)     3784 2022-02-11 12:46:32.000000 foledol-django-0.0.9/src/foledol_django.egg-info/SOURCES.txt
+-rw-r--r--   0 lde        (502) staff       (20)        1 2022-02-11 12:46:32.000000 foledol-django-0.0.9/src/foledol_django.egg-info/dependency_links.txt
+-rw-r--r--   0 lde        (502) staff       (20)        8 2022-02-11 12:46:32.000000 foledol-django-0.0.9/src/foledol_django.egg-info/top_level.txt
```

### Comparing `foledol-django-0.0.8/LICENSE` & `foledol-django-0.0.9/LICENSE`

 * *Files identical despite different names*

### Comparing `foledol-django-0.0.8/src/foledol/django/logger.py` & `foledol-django-0.0.9/src/foledol/django/logger.py`

 * *Files identical despite different names*

### Comparing `foledol-django-0.0.8/src/foledol/django/meta.py` & `foledol-django-0.0.9/src/foledol/django/meta.py`

 * *Files identical despite different names*

### Comparing `foledol-django-0.0.8/src/foledol/django/migrations/0001_initial.py` & `foledol-django-0.0.9/src/foledol/django/migrations/0001_initial.py`

 * *Files identical despite different names*

### Comparing `foledol-django-0.0.8/src/foledol/django/templates/.DS_Store` & `foledol-django-0.0.9/src/foledol/django/templates/.DS_Store`

 * *Files identical despite different names*

### Comparing `foledol-django-0.0.8/src/foledol/django/templates/common/archive.html` & `foledol-django-0.0.9/src/foledol/django/templates/common/archive.html`

 * *Files identical despite different names*

### Comparing `foledol-django-0.0.8/src/foledol/django/templates/common/delete.html` & `foledol-django-0.0.9/src/foledol/django/templates/common/delete.html`

 * *Files identical despite different names*

### Comparing `foledol-django-0.0.8/src/foledol/django/templates/common/print.html` & `foledol-django-0.0.9/src/foledol/django/templates/common/print.html`

 * *Files identical despite different names*

### Comparing `foledol-django-0.0.8/src/foledol/django/templates/components/field_city.html` & `foledol-django-0.0.9/src/foledol/django/templates/components/field_city.html`

 * *Files identical despite different names*

### Comparing `foledol-django-0.0.8/src/foledol/django/templates/components/field_country.html` & `foledol-django-0.0.9/src/foledol/django/templates/components/field_country.html`

 * *Files identical despite different names*

### Comparing `foledol-django-0.0.8/src/foledol/django/templates/components/field_date.html` & `foledol-django-0.0.9/src/foledol/django/templates/components/field_date.html`

 * *Files identical despite different names*

### Comparing `foledol-django-0.0.8/src/foledol/django/templates/components/field_select.html` & `foledol-django-0.0.9/src/foledol/django/templates/components/field_select.html`

 * *Files identical despite different names*

### Comparing `foledol-django-0.0.8/src/foledol/django/templates/components/field_select_short.html` & `foledol-django-0.0.9/src/foledol/django/templates/components/field_select_short.html`

 * *Files identical despite different names*

### Comparing `foledol-django-0.0.8/src/foledol/django/templates/components/field_text.html` & `foledol-django-0.0.9/src/foledol/django/templates/components/field_text.html`

 * *Files identical despite different names*

### Comparing `foledol-django-0.0.8/src/foledol/django/templates/components/field_text_area.html` & `foledol-django-0.0.9/src/foledol/django/templates/components/field_text_area.html`

 * *Files identical despite different names*

### Comparing `foledol-django-0.0.8/src/foledol/django/templates/components/field_text_area_short.html` & `foledol-django-0.0.9/src/foledol/django/templates/components/field_text_area_short.html`

 * *Files identical despite different names*

### Comparing `foledol-django-0.0.8/src/foledol/django/templates/components/field_text_short.html` & `foledol-django-0.0.9/src/foledol/django/templates/components/field_text_short.html`

 * *Files identical despite different names*

### Comparing `foledol-django-0.0.8/src/foledol/django/templates/components/field_zip.html` & `foledol-django-0.0.9/src/foledol/django/templates/components/field_zip.html`

 * *Files identical despite different names*

### Comparing `foledol-django-0.0.8/src/foledol/django/templates/components/grid.html` & `foledol-django-0.0.9/src/foledol/django/templates/components/grid.html`

 * *Files identical despite different names*

### Comparing `foledol-django-0.0.8/src/foledol/django/templates/components/grid_column.html` & `foledol-django-0.0.9/src/foledol/django/templates/components/grid_column.html`

 * *Files identical despite different names*

### Comparing `foledol-django-0.0.8/src/foledol/django/templates/components/grid_row.html` & `foledol-django-0.0.9/src/foledol/django/templates/components/grid_row.html`

 * *Files identical despite different names*

### Comparing `foledol-django-0.0.8/src/foledol/django/templates/components/logs.html` & `foledol-django-0.0.9/src/foledol/django/templates/components/logs.html`

 * *Files identical despite different names*

### Comparing `foledol-django-0.0.8/src/foledol/django/templates/components/navigator.html` & `foledol-django-0.0.9/src/foledol/django/templates/components/navigator.html`

 * *Files identical despite different names*

### Comparing `foledol-django-0.0.8/src/foledol/django/templates/components/paginator.html` & `foledol-django-0.0.9/src/foledol/django/templates/components/paginator.html`

 * *Files identical despite different names*

### Comparing `foledol-django-0.0.8/src/foledol/django/templates/components/table.html` & `foledol-django-0.0.9/src/foledol/django/templates/components/table.html`

 * *Files identical despite different names*

### Comparing `foledol-django-0.0.8/src/foledol/django/templates/components/upload.html` & `foledol-django-0.0.9/src/foledol/django/templates/components/upload.html`

 * *Files identical despite different names*

### Comparing `foledol-django-0.0.8/src/foledol/django/templates/log.html` & `foledol-django-0.0.9/src/foledol/django/templates/log.html`

 * *Files identical despite different names*

### Comparing `foledol-django-0.0.8/src/foledol/django/templates/logs.html` & `foledol-django-0.0.9/src/foledol/django/templates/logs.html`

 * *Files identical despite different names*

### Comparing `foledol-django-0.0.8/src/foledol/django/templatetags/custom.py` & `foledol-django-0.0.9/src/foledol/django/templatetags/custom.py`

 * *Files identical despite different names*

### Comparing `foledol-django-0.0.8/src/foledol/django/templatetags/date_extras.py` & `foledol-django-0.0.9/src/foledol/django/templatetags/date_extras.py`

 * *Files identical despite different names*

### Comparing `foledol-django-0.0.8/src/foledol/django/templatetags/form_extras.py` & `foledol-django-0.0.9/src/foledol/django/templatetags/form_extras.py`

 * *Files identical despite different names*

### Comparing `foledol-django-0.0.8/src/foledol/django/test.py` & `foledol-django-0.0.9/src/foledol/django/test.py`

 * *Files 10% similar despite different names*

```diff
@@ -30,34 +30,34 @@
 
 
 def create_object(test, context, ref, obj=None, path=None, space=settings.DEFAULT_SPACE):
     if obj:
         set_default(obj, context)
     context.update({
         'action': 'create',
-        'path': ':' + get_default_path(test, path)
+        'path': ':' + get_default_path(test, path, space)
     })
     response = get_and_post(test, reverse(space + ':' + test.prefix + '_create'), context)
     test.assertContains(response, ref)
 
 
 def update_object(test, pk, context, ref, path=None, space=settings.DEFAULT_SPACE):
     context.update({
         'action': 'update',
-        'path': ':' + get_default_path(test, path)
+        'path': ':' + get_default_path(test, path, space)
     })
     response = get_and_post(test, reverse(space + ':' + test.prefix + '_update', kwargs={'pk': pk}), context)
     test.assertContains(response, ref)
 
 
 def delete_object(test, pk, ref, path=None, space=settings.DEFAULT_SPACE):
     context = {
         'action': 'delete',
         'delete': '',
-        'path': ':' + get_default_path(test, path)
+        'path': ':' + get_default_path(test, path, space)
     }
     response = test.client.get(reverse(space + ':' + test.prefix + '_delete', kwargs={'pk': pk}), context, follow=True)
     test.assertEqual(response.status_code, 200)
     response = test.client.post(reverse(space + ':' + test.prefix + '_delete', kwargs={'pk': pk}), context, follow=True)
     test.assertEqual(response.status_code, 200)
     test.assertNotContains(response, ref)
 
@@ -101,14 +101,28 @@
     return download(test, action, url, 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
 
 
 def export_object_as_txt(test, action, url):
     return download(test, action, url, 'text/plain')
 
 
+def import_object(test, action, url, path, access='rb'):
+    with open(path, access) as file:
+        response = test.client.post(url, {
+            'action': action,
+            'path': ':' + url,
+            'upload': file
+        }, follow=True)
+        test.assertEqual(response.status_code, 200)
+
+
+def import_object_as_txt(test, action, url, path):
+    import_object(test, action, url, path, access='r')
+
+
 def run_object_module(test, action, url):
     response = test.client.post(url, {
         'action': action,
         'path': ':' + url,
     }, follow=True)
     test.assertEqual(response.status_code, 200)
     return response
```

### Comparing `foledol-django-0.0.8/src/foledol/django/tools/barcode.py` & `foledol-django-0.0.9/src/foledol/django/tools/barcode.py`

 * *Files identical despite different names*

### Comparing `foledol-django-0.0.8/src/foledol/django/tools/canvas.py` & `foledol-django-0.0.9/src/foledol/django/tools/canvas.py`

 * *Files identical despite different names*

### Comparing `foledol-django-0.0.8/src/foledol/django/tools/chart.py` & `foledol-django-0.0.9/src/foledol/django/tools/chart.py`

 * *Files identical despite different names*

### Comparing `foledol-django-0.0.8/src/foledol/django/tools/field.py` & `foledol-django-0.0.9/src/foledol/django/tools/field.py`

 * *Files identical despite different names*

### Comparing `foledol-django-0.0.8/src/foledol/django/tools/form.py` & `foledol-django-0.0.9/src/foledol/django/tools/form.py`

 * *Files identical despite different names*

### Comparing `foledol-django-0.0.8/src/foledol/django/tools/handlers.py` & `foledol-django-0.0.9/src/foledol/django/tools/handlers.py`

 * *Files identical despite different names*

### Comparing `foledol-django-0.0.8/src/foledol/django/tools/readers.py` & `foledol-django-0.0.9/src/foledol/django/tools/readers.py`

 * *Files identical despite different names*

### Comparing `foledol-django-0.0.8/src/foledol/django/tools/report.py` & `foledol-django-0.0.9/src/foledol/django/tools/report.py`

 * *Files 4% similar despite different names*

```diff
@@ -12,19 +12,20 @@
 class ReportColumn:
     def __init__(self, width, label):
         self.width = width
         self.label = label
 
 
 class ReportItem:
-    def __init__(self, key, label, route=None, confirm=False):
+    def __init__(self, key, label, route=None, confirm=False, report=None):
         self.key = key
         self.label = label
         self.route = route
         self.confirm = confirm
+        self.report = report
 
 
 def build_report(builder):
     buffer = BytesIO()
     page = canvas.Canvas(buffer)
     builder(page)
```

### Comparing `foledol-django-0.0.8/src/foledol/django/tools/table.py` & `foledol-django-0.0.9/src/foledol/django/tools/table.py`

 * *Files identical despite different names*

### Comparing `foledol-django-0.0.8/src/foledol/django/tools/writer.py` & `foledol-django-0.0.9/src/foledol/django/tools/writer.py`

 * *Files identical despite different names*

### Comparing `foledol-django-0.0.8/src/foledol/django/utils.py` & `foledol-django-0.0.9/src/foledol/django/utils.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 # -*- coding: utf-8 -*-
-
+import io
 import os
 import re
 import shutil
 import smtplib
 import sys
 from datetime import datetime
 from email.mime.multipart import MIMEMultipart
@@ -464,7 +464,26 @@
             row.append(item)
         else:
             row = [item]
             rows.append(row)
     return rows
 
 
+def response_as_txt(output, title):
+    response = HttpResponse(
+        output.getvalue().encode("cp1252"),
+        #output.getvalue().encode("iso-8859-1"),
+        content_type='text/plain'
+    )
+    response['Content-Disposition'] = 'attachment; filename="' + title + '.txt"'
+    return response
+
+
+def to_file(output, path):
+    if isinstance(output, io.StringIO):
+        with open(path, mode='w') as file:
+            output.seek(0)
+            file.write(output.getvalue())
+        return
+    with open(path, mode='wb') as file:
+        output.seek(0)
+        shutil.copyfileobj(output, file, length=4096)
```

### Comparing `foledol-django-0.0.8/src/foledol/django/views/logs.py` & `foledol-django-0.0.9/src/foledol/django/views/logs.py`

 * *Files identical despite different names*

### Comparing `foledol-django-0.0.8/src/foledol_django.egg-info/SOURCES.txt` & `foledol-django-0.0.9/src/foledol_django.egg-info/SOURCES.txt`

 * *Files 9% similar despite different names*

```diff
@@ -3,26 +3,36 @@
 README.md
 pyproject.toml
 setup.cfg
 setup.py
 src/foledol/__init__.py
 src/foledol/django/__init__.py
 src/foledol/django/apps.py
+src/foledol/django/auth.py
 src/foledol/django/logger.py
 src/foledol/django/meta.py
 src/foledol/django/models.py
 src/foledol/django/test.py
 src/foledol/django/urls.py
 src/foledol/django/utils.py
 src/foledol/django/migrations/0001_initial.py
+src/foledol/django/migrations/0002_auto_20220211_0730.py
 src/foledol/django/migrations/__init__.py
+src/foledol/django/reports/__init__.py
+src/foledol/django/reports/grid.py
 src/foledol/django/templates/.DS_Store
+src/foledol/django/templates/column.html
+src/foledol/django/templates/columns.html
+src/foledol/django/templates/grid.html
+src/foledol/django/templates/grids.html
 src/foledol/django/templates/log.html
 src/foledol/django/templates/log_events.html
 src/foledol/django/templates/logs.html
+src/foledol/django/templates/user_login.html
+src/foledol/django/templates/user_logout.html
 src/foledol/django/templates/common/archive.html
 src/foledol/django/templates/common/delete.html
 src/foledol/django/templates/common/error.html
 src/foledol/django/templates/common/print.html
 src/foledol/django/templates/components/banners.html
 src/foledol/django/templates/components/field_check.html
 src/foledol/django/templates/components/field_check_new.html
@@ -65,12 +75,16 @@
 src/foledol/django/tools/form.py
 src/foledol/django/tools/handlers.py
 src/foledol/django/tools/readers.py
 src/foledol/django/tools/report.py
 src/foledol/django/tools/table.py
 src/foledol/django/tools/writer.py
 src/foledol/django/views/__init__.py
+src/foledol/django/views/column.py
+src/foledol/django/views/columns.py
+src/foledol/django/views/grid.py
+src/foledol/django/views/grids.py
 src/foledol/django/views/logs.py
 src/foledol_django.egg-info/PKG-INFO
 src/foledol_django.egg-info/SOURCES.txt
 src/foledol_django.egg-info/dependency_links.txt
 src/foledol_django.egg-info/top_level.txt
```

