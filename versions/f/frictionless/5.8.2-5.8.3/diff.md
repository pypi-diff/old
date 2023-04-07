# Comparing `tmp/frictionless-5.8.2.tar.gz` & `tmp/frictionless-5.8.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "frictionless-5.8.2.tar", last modified: Tue Mar  7 11:42:01 2023, max compression
+gzip compressed data, was "frictionless-5.8.3.tar", last modified: Tue Mar  7 12:42:04 2023, max compression
```

## Comparing `frictionless-5.8.2.tar` & `frictionless-5.8.3.tar`

### file list

```diff
@@ -1,763 +1,763 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.705770 frictionless-5.8.2/
--rw-r--r--   0 runner    (1001) docker     (123)     2404 2023-03-07 11:41:54.000000 frictionless-5.8.2/AUTHORS.md
--rw-r--r--   0 runner    (1001) docker     (123)     1097 2023-03-07 11:41:54.000000 frictionless-5.8.2/LICENSE.md
--rw-r--r--   0 runner    (1001) docker     (123)      125 2023-03-07 11:41:54.000000 frictionless-5.8.2/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     1306 2023-03-07 11:41:54.000000 frictionless-5.8.2/Makefile
--rw-r--r--   0 runner    (1001) docker     (123)     5538 2023-03-07 11:42:01.705770 frictionless-5.8.2/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     3565 2023-03-07 11:41:54.000000 frictionless-5.8.2/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.649769 frictionless-5.8.2/frictionless/
--rw-r--r--   0 runner    (1001) docker     (123)      772 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)       96 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/__main__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.649769 frictionless-5.8.2/frictionless/actions/
--rw-r--r--   0 runner    (1001) docker     (123)      124 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/actions/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1392 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/actions/describe.py
--rw-r--r--   0 runner    (1001) docker     (123)     3477 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/actions/extract.py
--rw-r--r--   0 runner    (1001) docker     (123)     2111 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/actions/transform.py
--rw-r--r--   0 runner    (1001) docker     (123)     4410 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/actions/validate.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.649769 frictionless-5.8.2/frictionless/assets/
--rw-r--r--   0 runner    (1001) docker     (123)        6 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/assets/VERSION
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.649769 frictionless-5.8.2/frictionless/assets/profiles/
--rw-r--r--   0 runner    (1001) docker     (123)     8260 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/assets/profiles/geojson.json
--rw-r--r--   0 runner    (1001) docker     (123)    10245 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/assets/profiles/topojson.json
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.653769 frictionless-5.8.2/frictionless/assets/templates/
--rw-r--r--   0 runner    (1001) docker     (123)      228 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/assets/templates/checklist.md
--rw-r--r--   0 runner    (1001) docker     (123)      115 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/assets/templates/detector.md
--rw-r--r--   0 runner    (1001) docker     (123)      184 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/assets/templates/dialect.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.653769 frictionless-5.8.2/frictionless/assets/templates/erd/
--rw-r--r--   0 runner    (1001) docker     (123)      133 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/assets/templates/erd/field.html
--rw-r--r--   0 runner    (1001) docker     (123)       50 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/assets/templates/erd/graph.html
--rw-r--r--   0 runner    (1001) docker     (123)      147 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/assets/templates/erd/primary_key_field.html
--rw-r--r--   0 runner    (1001) docker     (123)      228 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/assets/templates/erd/table.html
--rw-r--r--   0 runner    (1001) docker     (123)      499 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/assets/templates/field-table.md
--rw-r--r--   0 runner    (1001) docker     (123)      489 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/assets/templates/field.md
--rw-r--r--   0 runner    (1001) docker     (123)      353 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/assets/templates/inquiry.md
--rw-r--r--   0 runner    (1001) docker     (123)      268 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/assets/templates/package-table.md
--rw-r--r--   0 runner    (1001) docker     (123)      262 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/assets/templates/package.md
--rw-r--r--   0 runner    (1001) docker     (123)      242 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/assets/templates/pipeline.md
--rw-r--r--   0 runner    (1001) docker     (123)      172 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/assets/templates/report-task.md
--rw-r--r--   0 runner    (1001) docker     (123)      239 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/assets/templates/report.md
--rw-r--r--   0 runner    (1001) docker     (123)      434 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/assets/templates/resource-table.md
--rw-r--r--   0 runner    (1001) docker     (123)      473 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/assets/templates/resource.md
--rw-r--r--   0 runner    (1001) docker     (123)       45 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/assets/templates/schema-table.md
--rw-r--r--   0 runner    (1001) docker     (123)       85 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/assets/templates/schema.md
--rw-r--r--   0 runner    (1001) docker     (123)       97 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/assets/templates/step.md
--rw-r--r--   0 runner    (1001) docker     (123)      222 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/assets/templates/task.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.653769 frictionless-5.8.2/frictionless/catalog/
--rw-r--r--   0 runner    (1001) docker     (123)       58 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/catalog/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     6449 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/catalog/catalog.py
--rw-r--r--   0 runner    (1001) docker     (123)     3037 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/catalog/dataset.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.653769 frictionless-5.8.2/frictionless/checklist/
--rw-r--r--   0 runner    (1001) docker     (123)       58 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/checklist/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3610 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/checklist/check.py
--rw-r--r--   0 runner    (1001) docker     (123)     4848 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/checklist/checklist.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.653769 frictionless-5.8.2/frictionless/checks/
--rw-r--r--   0 runner    (1001) docker     (123)       91 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/checks/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2996 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/checks/baseline.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.653769 frictionless-5.8.2/frictionless/checks/cell/
--rw-r--r--   0 runner    (1001) docker     (123)      301 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/checks/cell/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      975 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/checks/cell/ascii_value.py
--rw-r--r--   0 runner    (1001) docker     (123)     2879 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/checks/cell/deviated_cell.py
--rw-r--r--   0 runner    (1001) docker     (123)     3361 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/checks/cell/deviated_value.py
--rw-r--r--   0 runner    (1001) docker     (123)     1351 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/checks/cell/forbidden_value.py
--rw-r--r--   0 runner    (1001) docker     (123)     2104 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/checks/cell/required_value.py
--rw-r--r--   0 runner    (1001) docker     (123)     1523 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/checks/cell/sequential_value.py
--rw-r--r--   0 runner    (1001) docker     (123)     1368 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/checks/cell/truncated_value.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.653769 frictionless-5.8.2/frictionless/checks/row/
--rw-r--r--   0 runner    (1001) docker     (123)       84 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/checks/row/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      882 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/checks/row/duplicate_row.py
--rw-r--r--   0 runner    (1001) docker     (123)     1190 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/checks/row/row_constraint.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.653769 frictionless-5.8.2/frictionless/checks/table/
--rw-r--r--   0 runner    (1001) docker     (123)       47 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/checks/table/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3886 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/checks/table/table_dimensions.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.653769 frictionless-5.8.2/frictionless/detector/
--rw-r--r--   0 runner    (1001) docker     (123)       31 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/detector/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    15886 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/detector/detector.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.653769 frictionless-5.8.2/frictionless/dialect/
--rw-r--r--   0 runner    (1001) docker     (123)       58 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/dialect/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1998 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/dialect/control.py
--rw-r--r--   0 runner    (1001) docker     (123)     9212 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/dialect/dialect.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.653769 frictionless-5.8.2/frictionless/error/
--rw-r--r--   0 runner    (1001) docker     (123)       25 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/error/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2989 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/error/error.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.657769 frictionless-5.8.2/frictionless/errors/
--rw-r--r--   0 runner    (1001) docker     (123)      191 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/errors/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4792 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/errors/cell.py
--rw-r--r--   0 runner    (1001) docker     (123)      215 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/errors/data.py
--rw-r--r--   0 runner    (1001) docker     (123)      726 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/errors/file.py
--rw-r--r--   0 runner    (1001) docker     (123)     1038 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/errors/header.py
--rw-r--r--   0 runner    (1001) docker     (123)     2387 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/errors/label.py
--rw-r--r--   0 runner    (1001) docker     (123)     3485 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/errors/metadata.py
--rw-r--r--   0 runner    (1001) docker     (123)     1505 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/errors/resource.py
--rw-r--r--   0 runner    (1001) docker     (123)     3754 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/errors/row.py
--rw-r--r--   0 runner    (1001) docker     (123)     1628 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/errors/table.py
--rw-r--r--   0 runner    (1001) docker     (123)     1050 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/exception.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.657769 frictionless-5.8.2/frictionless/fields/
--rw-r--r--   0 runner    (1001) docker     (123)      484 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/fields/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      236 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/fields/any.py
--rw-r--r--   0 runner    (1001) docker     (123)     2500 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/fields/array.py
--rw-r--r--   0 runner    (1001) docker     (123)     1695 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/fields/boolean.py
--rw-r--r--   0 runner    (1001) docker     (123)     1868 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/fields/date.py
--rw-r--r--   0 runner    (1001) docker     (123)     1715 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/fields/datetime.py
--rw-r--r--   0 runner    (1001) docker     (123)      962 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/fields/duration.py
--rw-r--r--   0 runner    (1001) docker     (123)     1675 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/fields/geojson.py
--rw-r--r--   0 runner    (1001) docker     (123)     2142 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/fields/geopoint.py
--rw-r--r--   0 runner    (1001) docker     (123)     1858 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/fields/integer.py
--rw-r--r--   0 runner    (1001) docker     (123)     3619 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/fields/number.py
--rw-r--r--   0 runner    (1001) docker     (123)      954 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/fields/object.py
--rw-r--r--   0 runner    (1001) docker     (123)     2941 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/fields/string.py
--rw-r--r--   0 runner    (1001) docker     (123)     1800 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/fields/time.py
--rw-r--r--   0 runner    (1001) docker     (123)      975 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/fields/year.py
--rw-r--r--   0 runner    (1001) docker     (123)     1330 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/fields/yearmonth.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.657769 frictionless-5.8.2/frictionless/formats/
--rw-r--r--   0 runner    (1001) docker     (123)      355 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.657769 frictionless-5.8.2/frictionless/formats/csv/
--rw-r--r--   0 runner    (1001) docker     (123)       92 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/csv/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2742 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/csv/control.py
--rw-r--r--   0 runner    (1001) docker     (123)     3144 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/csv/parser.py
--rw-r--r--   0 runner    (1001) docker     (123)      786 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/csv/plugin.py
--rw-r--r--   0 runner    (1001) docker     (123)      187 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/csv/settings.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.657769 frictionless-5.8.2/frictionless/formats/erd/
--rw-r--r--   0 runner    (1001) docker     (123)       30 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/erd/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2051 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/erd/mapper.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.657769 frictionless-5.8.2/frictionless/formats/excel/
--rw-r--r--   0 runner    (1001) docker     (123)      175 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/excel/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1213 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/excel/adapter.py
--rw-r--r--   0 runner    (1001) docker     (123)     1669 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/excel/control.py
--rw-r--r--   0 runner    (1001) docker     (123)      416 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/excel/mapper.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.657769 frictionless-5.8.2/frictionless/formats/excel/parsers/
--rw-r--r--   0 runner    (1001) docker     (123)       56 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/excel/parsers/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3939 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/excel/parsers/xls.py
--rw-r--r--   0 runner    (1001) docker     (123)    14420 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/excel/parsers/xlsx.py
--rw-r--r--   0 runner    (1001) docker     (123)     1129 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/excel/plugin.py
--rw-r--r--   0 runner    (1001) docker     (123)      885 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/excel/settings.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.657769 frictionless-5.8.2/frictionless/formats/gsheets/
--rw-r--r--   0 runner    (1001) docker     (123)      104 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/gsheets/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      516 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/gsheets/control.py
--rw-r--r--   0 runner    (1001) docker     (123)     1977 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/gsheets/parser.py
--rw-r--r--   0 runner    (1001) docker     (123)     1135 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/gsheets/plugin.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.661769 frictionless-5.8.2/frictionless/formats/html/
--rw-r--r--   0 runner    (1001) docker     (123)       95 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/html/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      581 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/html/control.py
--rw-r--r--   0 runner    (1001) docker     (123)     2212 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/html/parser.py
--rw-r--r--   0 runner    (1001) docker     (123)      723 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/html/plugin.py
--rw-r--r--   0 runner    (1001) docker     (123)       74 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/html/settings.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.661769 frictionless-5.8.2/frictionless/formats/inline/
--rw-r--r--   0 runner    (1001) docker     (123)      101 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/inline/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      746 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/inline/control.py
--rw-r--r--   0 runner    (1001) docker     (123)     2619 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/inline/parser.py
--rw-r--r--   0 runner    (1001) docker     (123)     1028 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/inline/plugin.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.661769 frictionless-5.8.2/frictionless/formats/json/
--rw-r--r--   0 runner    (1001) docker     (123)      109 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/json/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      965 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/json/control.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.661769 frictionless-5.8.2/frictionless/formats/json/parsers/
--rw-r--r--   0 runner    (1001) docker     (123)       60 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/json/parsers/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2147 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/json/parsers/json.py
--rw-r--r--   0 runner    (1001) docker     (123)     1771 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/json/parsers/jsonl.py
--rw-r--r--   0 runner    (1001) docker     (123)     1194 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/json/plugin.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.661769 frictionless-5.8.2/frictionless/formats/jsonschema/
--rw-r--r--   0 runner    (1001) docker     (123)       37 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/jsonschema/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1273 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/jsonschema/mapper.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.661769 frictionless-5.8.2/frictionless/formats/markdown/
--rw-r--r--   0 runner    (1001) docker     (123)       70 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/markdown/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4217 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/markdown/mapper.py
--rw-r--r--   0 runner    (1001) docker     (123)      450 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/markdown/plugin.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.661769 frictionless-5.8.2/frictionless/formats/ods/
--rw-r--r--   0 runner    (1001) docker     (123)      124 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/ods/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1234 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/ods/adapter.py
--rw-r--r--   0 runner    (1001) docker     (123)      559 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/ods/control.py
--rw-r--r--   0 runner    (1001) docker     (123)     3167 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/ods/parser.py
--rw-r--r--   0 runner    (1001) docker     (123)     1063 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/ods/plugin.py
--rw-r--r--   0 runner    (1001) docker     (123)       65 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/ods/settings.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.661769 frictionless-5.8.2/frictionless/formats/pandas/
--rw-r--r--   0 runner    (1001) docker     (123)      101 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/pandas/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      200 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/pandas/control.py
--rw-r--r--   0 runner    (1001) docker     (123)     7756 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/pandas/parser.py
--rw-r--r--   0 runner    (1001) docker     (123)     1232 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/pandas/plugin.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.661769 frictionless-5.8.2/frictionless/formats/parquet/
--rw-r--r--   0 runner    (1001) docker     (123)      104 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/parquet/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1456 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/parquet/control.py
--rw-r--r--   0 runner    (1001) docker     (123)     1423 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/parquet/parser.py
--rw-r--r--   0 runner    (1001) docker     (123)      796 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/parquet/plugin.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.661769 frictionless-5.8.2/frictionless/formats/qsv/
--rw-r--r--   0 runner    (1001) docker     (123)       62 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/qsv/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1096 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/qsv/adapter.py
--rw-r--r--   0 runner    (1001) docker     (123)      805 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/qsv/mapper.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.661769 frictionless-5.8.2/frictionless/formats/spss/
--rw-r--r--   0 runner    (1001) docker     (123)       95 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/spss/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      194 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/spss/control.py
--rw-r--r--   0 runner    (1001) docker     (123)     6463 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/spss/parser.py
--rw-r--r--   0 runner    (1001) docker     (123)      672 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/spss/plugin.py
--rw-r--r--   0 runner    (1001) docker     (123)      261 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/spss/settings.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.665769 frictionless-5.8.2/frictionless/formats/sql/
--rw-r--r--   0 runner    (1001) docker     (123)      230 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/sql/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5052 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/sql/adapter.py
--rw-r--r--   0 runner    (1001) docker     (123)     1557 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/sql/control.py
--rw-r--r--   0 runner    (1001) docker     (123)     3986 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/sql/indexer.py
--rw-r--r--   0 runner    (1001) docker     (123)      121 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/sql/interfaces.py
--rw-r--r--   0 runner    (1001) docker     (123)    11452 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/sql/mapper.py
--rw-r--r--   0 runner    (1001) docker     (123)     1901 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/sql/parser.py
--rw-r--r--   0 runner    (1001) docker     (123)     1308 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/sql/plugin.py
--rw-r--r--   0 runner    (1001) docker     (123)      425 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/sql/settings.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.665769 frictionless-5.8.2/frictionless/formats/yaml/
--rw-r--r--   0 runner    (1001) docker     (123)       95 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/yaml/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      896 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/yaml/control.py
--rw-r--r--   0 runner    (1001) docker     (123)     2088 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/yaml/parser.py
--rw-r--r--   0 runner    (1001) docker     (123)      869 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/yaml/plugin.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.665769 frictionless-5.8.2/frictionless/formats/zip/
--rw-r--r--   0 runner    (1001) docker     (123)       94 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/zip/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5018 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/zip/adapter.py
--rw-r--r--   0 runner    (1001) docker     (123)      728 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/zip/control.py
--rw-r--r--   0 runner    (1001) docker     (123)      539 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/formats/zip/plugin.py
--rw-r--r--   0 runner    (1001) docker     (123)    11108 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/helpers.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.665769 frictionless-5.8.2/frictionless/inquiry/
--rw-r--r--   0 runner    (1001) docker     (123)       59 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/inquiry/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3079 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/inquiry/inquiry.py
--rw-r--r--   0 runner    (1001) docker     (123)     7664 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/inquiry/task.py
--rw-r--r--   0 runner    (1001) docker     (123)     1233 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/interfaces.py
--rw-r--r--   0 runner    (1001) docker     (123)    17201 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/metadata.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.665769 frictionless-5.8.2/frictionless/package/
--rw-r--r--   0 runner    (1001) docker     (123)       29 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/package/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.665769 frictionless-5.8.2/frictionless/package/methods/
--rw-r--r--   0 runner    (1001) docker     (123)       64 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/package/methods/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      597 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/package/methods/transform.py
--rw-r--r--   0 runner    (1001) docker     (123)     2551 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/package/methods/validate.py
--rw-r--r--   0 runner    (1001) docker     (123)    22444 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/package/package.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.665769 frictionless-5.8.2/frictionless/pipeline/
--rw-r--r--   0 runner    (1001) docker     (123)       58 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/pipeline/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3490 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/pipeline/pipeline.py
--rw-r--r--   0 runner    (1001) docker     (123)     3029 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/pipeline/step.py
--rw-r--r--   0 runner    (1001) docker     (123)     8044 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/platform.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.665769 frictionless-5.8.2/frictionless/portals/
--rw-r--r--   0 runner    (1001) docker     (123)       64 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/portals/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.665769 frictionless-5.8.2/frictionless/portals/ckan/
--rw-r--r--   0 runner    (1001) docker     (123)       97 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/portals/ckan/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     9075 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/portals/ckan/adapter.py
--rw-r--r--   0 runner    (1001) docker     (123)     2226 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/portals/ckan/control.py
--rw-r--r--   0 runner    (1001) docker     (123)     1268 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/portals/ckan/plugin.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.665769 frictionless-5.8.2/frictionless/portals/github/
--rw-r--r--   0 runner    (1001) docker     (123)      103 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/portals/github/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     9461 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/portals/github/adapter.py
--rw-r--r--   0 runner    (1001) docker     (123)     3165 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/portals/github/control.py
--rw-r--r--   0 runner    (1001) docker     (123)     1300 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/portals/github/plugin.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.665769 frictionless-5.8.2/frictionless/portals/zenodo/
--rw-r--r--   0 runner    (1001) docker     (123)      103 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/portals/zenodo/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    10570 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/portals/zenodo/adapter.py
--rw-r--r--   0 runner    (1001) docker     (123)     4676 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/portals/zenodo/control.py
--rw-r--r--   0 runner    (1001) docker     (123)     1116 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/portals/zenodo/plugin.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.669769 frictionless-5.8.2/frictionless/program/
--rw-r--r--   0 runner    (1001) docker     (123)      223 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/program/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      570 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/program/api.py
--rw-r--r--   0 runner    (1001) docker     (123)     6785 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/program/common.py
--rw-r--r--   0 runner    (1001) docker     (123)     3370 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/program/convert.py
--rw-r--r--   0 runner    (1001) docker     (123)     4934 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/program/describe.py
--rw-r--r--   0 runner    (1001) docker     (123)     7559 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/program/extract.py
--rw-r--r--   0 runner    (1001) docker     (123)     2169 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/program/index.py
--rw-r--r--   0 runner    (1001) docker     (123)      909 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/program/program.py
--rw-r--r--   0 runner    (1001) docker     (123)     1798 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/program/summary.py
--rw-r--r--   0 runner    (1001) docker     (123)     2607 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/program/transform.py
--rw-r--r--   0 runner    (1001) docker     (123)     7178 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/program/validate.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.669769 frictionless-5.8.2/frictionless/project/
--rw-r--r--   0 runner    (1001) docker     (123)      121 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/project/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)       60 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/project/config.py
--rw-r--r--   0 runner    (1001) docker     (123)    10588 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/project/database.py
--rw-r--r--   0 runner    (1001) docker     (123)     7694 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/project/filesystem.py
--rw-r--r--   0 runner    (1001) docker     (123)     1008 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/project/interfaces.py
--rw-r--r--   0 runner    (1001) docker     (123)     7140 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/project/project.py
--rw-r--r--   0 runner    (1001) docker     (123)       94 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/project/settings.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.669769 frictionless-5.8.2/frictionless/report/
--rw-r--r--   0 runner    (1001) docker     (123)       56 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/report/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      429 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/report/interfaces.py
--rw-r--r--   0 runner    (1001) docker     (123)     8783 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/report/report.py
--rw-r--r--   0 runner    (1001) docker     (123)     4717 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/report/task.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.669769 frictionless-5.8.2/frictionless/resource/
--rw-r--r--   0 runner    (1001) docker     (123)       31 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/resource/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.669769 frictionless-5.8.2/frictionless/resource/methods/
--rw-r--r--   0 runner    (1001) docker     (123)       93 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/resource/methods/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    10168 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/resource/methods/analyze.py
--rw-r--r--   0 runner    (1001) docker     (123)     2223 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/resource/methods/transform.py
--rw-r--r--   0 runner    (1001) docker     (123)     3951 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/resource/methods/validate.py
--rw-r--r--   0 runner    (1001) docker     (123)    45922 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/resource/resource.py
--rw-r--r--   0 runner    (1001) docker     (123)      608 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/resource/stats.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.669769 frictionless-5.8.2/frictionless/resources/
--rw-r--r--   0 runner    (1001) docker     (123)      169 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/resources/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)       91 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/resources/chart.py
--rw-r--r--   0 runner    (1001) docker     (123)      104 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/resources/file.py
--rw-r--r--   0 runner    (1001) docker     (123)      104 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/resources/json.py
--rw-r--r--   0 runner    (1001) docker     (123)      702 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/resources/metadata.py
--rw-r--r--   0 runner    (1001) docker     (123)       95 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/resources/package.py
--rw-r--r--   0 runner    (1001) docker     (123)      107 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/resources/table.py
--rw-r--r--   0 runner    (1001) docker     (123)      168 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/resources/text.py
--rw-r--r--   0 runner    (1001) docker     (123)      107 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/resources/view.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.669769 frictionless-5.8.2/frictionless/schema/
--rw-r--r--   0 runner    (1001) docker     (123)       52 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/schema/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     9608 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/schema/field.py
--rw-r--r--   0 runner    (1001) docker     (123)    12063 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/schema/schema.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.669769 frictionless-5.8.2/frictionless/schemes/
--rw-r--r--   0 runner    (1001) docker     (123)      131 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/schemes/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.673770 frictionless-5.8.2/frictionless/schemes/aws/
--rw-r--r--   0 runner    (1001) docker     (123)       92 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/schemes/aws/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      476 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/schemes/aws/control.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.673770 frictionless-5.8.2/frictionless/schemes/aws/loaders/
--rw-r--r--   0 runner    (1001) docker     (123)       25 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/schemes/aws/loaders/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2905 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/schemes/aws/loaders/s3.py
--rw-r--r--   0 runner    (1001) docker     (123)      404 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/schemes/aws/plugin.py
--rw-r--r--   0 runner    (1001) docker     (123)      100 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/schemes/aws/settings.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.673770 frictionless-5.8.2/frictionless/schemes/buffer/
--rw-r--r--   0 runner    (1001) docker     (123)      101 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/schemes/buffer/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      200 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/schemes/buffer/control.py
--rw-r--r--   0 runner    (1001) docker     (123)      496 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/schemes/buffer/loader.py
--rw-r--r--   0 runner    (1001) docker     (123)      780 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/schemes/buffer/plugin.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.673770 frictionless-5.8.2/frictionless/schemes/local/
--rw-r--r--   0 runner    (1001) docker     (123)       98 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/schemes/local/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      197 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/schemes/local/control.py
--rw-r--r--   0 runner    (1001) docker     (123)      620 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/schemes/local/loader.py
--rw-r--r--   0 runner    (1001) docker     (123)      522 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/schemes/local/plugin.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.673770 frictionless-5.8.2/frictionless/schemes/multipart/
--rw-r--r--   0 runner    (1001) docker     (123)      110 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/schemes/multipart/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      483 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/schemes/multipart/control.py
--rw-r--r--   0 runner    (1001) docker     (123)     2844 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/schemes/multipart/loader.py
--rw-r--r--   0 runner    (1001) docker     (123)      674 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/schemes/multipart/plugin.py
--rw-r--r--   0 runner    (1001) docker     (123)       78 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/schemes/multipart/settings.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.673770 frictionless-5.8.2/frictionless/schemes/remote/
--rw-r--r--   0 runner    (1001) docker     (123)      101 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/schemes/remote/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      553 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/schemes/remote/control.py
--rw-r--r--   0 runner    (1001) docker     (123)     2531 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/schemes/remote/loader.py
--rw-r--r--   0 runner    (1001) docker     (123)      600 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/schemes/remote/plugin.py
--rw-r--r--   0 runner    (1001) docker     (123)      124 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/schemes/remote/settings.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.673770 frictionless-5.8.2/frictionless/schemes/stream/
--rw-r--r--   0 runner    (1001) docker     (123)      101 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/schemes/stream/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      200 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/schemes/stream/control.py
--rw-r--r--   0 runner    (1001) docker     (123)     1607 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/schemes/stream/loader.py
--rw-r--r--   0 runner    (1001) docker     (123)      832 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/schemes/stream/plugin.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.673770 frictionless-5.8.2/frictionless/server/
--rw-r--r--   0 runner    (1001) docker     (123)      256 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/server/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.673770 frictionless-5.8.2/frictionless/server/bytes/
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/server/bytes/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      527 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/server/bytes/read.py
--rw-r--r--   0 runner    (1001) docker     (123)      610 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/server/config.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.673770 frictionless-5.8.2/frictionless/server/data/
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/server/data/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      488 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/server/data/read.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.673770 frictionless-5.8.2/frictionless/server/field/
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/server/field/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      494 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/server/field/list.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.677770 frictionless-5.8.2/frictionless/server/file/
--rw-r--r--   0 runner    (1001) docker     (123)      240 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/server/file/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      581 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/server/file/copy.py
--rw-r--r--   0 runner    (1001) docker     (123)      463 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/server/file/count.py
--rw-r--r--   0 runner    (1001) docker     (123)      781 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/server/file/create.py
--rw-r--r--   0 runner    (1001) docker     (123)      484 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/server/file/delete.py
--rw-r--r--   0 runner    (1001) docker     (123)      501 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/server/file/index.py
--rw-r--r--   0 runner    (1001) docker     (123)      489 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/server/file/list.py
--rw-r--r--   0 runner    (1001) docker     (123)      526 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/server/file/move.py
--rw-r--r--   0 runner    (1001) docker     (123)      498 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/server/file/read.py
--rw-r--r--   0 runner    (1001) docker     (123)      516 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/server/file/rename.py
--rw-r--r--   0 runner    (1001) docker     (123)      464 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/server/file/update.py
--rw-r--r--   0 runner    (1001) docker     (123)      689 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/server/file/upload.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.677770 frictionless-5.8.2/frictionless/server/folder/
--rw-r--r--   0 runner    (1001) docker     (123)       40 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/server/folder/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      538 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/server/folder/create.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.677770 frictionless-5.8.2/frictionless/server/package/
--rw-r--r--   0 runner    (1001) docker     (123)       62 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/server/package/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      470 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/server/package/create.py
--rw-r--r--   0 runner    (1001) docker     (123)      578 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/server/package/publish.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.677770 frictionless-5.8.2/frictionless/server/project/
--rw-r--r--   0 runner    (1001) docker     (123)       81 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/server/project/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      588 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/server/project/connect.py
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/server/project/index.py
--rw-r--r--   0 runner    (1001) docker     (123)      512 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/server/project/query.py
--rw-r--r--   0 runner    (1001) docker     (123)       53 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/server/router.py
--rw-r--r--   0 runner    (1001) docker     (123)     1092 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/server/server.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.677770 frictionless-5.8.2/frictionless/server/table/
--rw-r--r--   0 runner    (1001) docker     (123)       58 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/server/table/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      502 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/server/table/query.py
--rw-r--r--   0 runner    (1001) docker     (123)      672 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/server/table/read.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.677770 frictionless-5.8.2/frictionless/server/text/
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/server/text/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      479 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/server/text/read.py
--rw-r--r--   0 runner    (1001) docker     (123)     3640 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/settings.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.677770 frictionless-5.8.2/frictionless/standards/
--rw-r--r--   0 runner    (1001) docker     (123)       71 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/standards/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.677770 frictionless-5.8.2/frictionless/standards/core/
--rw-r--r--   0 runner    (1001) docker     (123)       92 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/standards/core/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1031 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/standards/core/dialect.py
--rw-r--r--   0 runner    (1001) docker     (123)      288 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/standards/core/package.py
--rw-r--r--   0 runner    (1001) docker     (123)      880 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/standards/core/resource.py
--rw-r--r--   0 runner    (1001) docker     (123)     2078 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/standards/core/schema.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.677770 frictionless-5.8.2/frictionless/standards/labs/
--rw-r--r--   0 runner    (1001) docker     (123)      138 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/standards/labs/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      449 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/standards/labs/catalog.py
--rw-r--r--   0 runner    (1001) docker     (123)      408 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/standards/labs/checklist.py
--rw-r--r--   0 runner    (1001) docker     (123)      199 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/standards/labs/error.py
--rw-r--r--   0 runner    (1001) docker     (123)      365 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/standards/labs/inquiry.py
--rw-r--r--   0 runner    (1001) docker     (123)      362 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/standards/labs/pipeline.py
--rw-r--r--   0 runner    (1001) docker     (123)      495 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/standards/labs/report.py
--rw-r--r--   0 runner    (1001) docker     (123)      445 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/standards/standard.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.677770 frictionless-5.8.2/frictionless/steps/
--rw-r--r--   0 runner    (1001) docker     (123)      105 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/steps/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.677770 frictionless-5.8.2/frictionless/steps/cell/
--rw-r--r--   0 runner    (1001) docker     (123)      226 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/steps/cell/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1513 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/steps/cell/cell_convert.py
--rw-r--r--   0 runner    (1001) docker     (123)     1541 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/steps/cell/cell_fill.py
--rw-r--r--   0 runner    (1001) docker     (123)      972 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/steps/cell/cell_format.py
--rw-r--r--   0 runner    (1001) docker     (123)     1004 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/steps/cell/cell_interpolate.py
--rw-r--r--   0 runner    (1001) docker     (123)     1382 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/steps/cell/cell_replace.py
--rw-r--r--   0 runner    (1001) docker     (123)      710 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/steps/cell/cell_set.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.681770 frictionless-5.8.2/frictionless/steps/field/
--rw-r--r--   0 runner    (1001) docker     (123)      333 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/steps/field/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2775 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/steps/field/field_add.py
--rw-r--r--   0 runner    (1001) docker     (123)      909 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/steps/field/field_filter.py
--rw-r--r--   0 runner    (1001) docker     (123)     2613 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/steps/field/field_merge.py
--rw-r--r--   0 runner    (1001) docker     (123)      956 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/steps/field/field_move.py
--rw-r--r--   0 runner    (1001) docker     (123)     3638 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/steps/field/field_pack.py
--rw-r--r--   0 runner    (1001) docker     (123)      916 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/steps/field/field_remove.py
--rw-r--r--   0 runner    (1001) docker     (123)     1728 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/steps/field/field_split.py
--rw-r--r--   0 runner    (1001) docker     (123)     1497 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/steps/field/field_unpack.py
--rw-r--r--   0 runner    (1001) docker     (123)     2021 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/steps/field/field_update.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.681770 frictionless-5.8.2/frictionless/steps/resource/
--rw-r--r--   0 runner    (1001) docker     (123)      180 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/steps/resource/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      945 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/steps/resource/resource_add.py
--rw-r--r--   0 runner    (1001) docker     (123)      893 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/steps/resource/resource_remove.py
--rw-r--r--   0 runner    (1001) docker     (123)     1201 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/steps/resource/resource_transform.py
--rw-r--r--   0 runner    (1001) docker     (123)     1562 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/steps/resource/resource_update.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.681770 frictionless-5.8.2/frictionless/steps/row/
--rw-r--r--   0 runner    (1001) docker     (123)      239 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/steps/row/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1223 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/steps/row/row_filter.py
--rw-r--r--   0 runner    (1001) docker     (123)     1353 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/steps/row/row_search.py
--rw-r--r--   0 runner    (1001) docker     (123)     1446 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/steps/row/row_slice.py
--rw-r--r--   0 runner    (1001) docker     (123)      939 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/steps/row/row_sort.py
--rw-r--r--   0 runner    (1001) docker     (123)      847 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/steps/row/row_split.py
--rw-r--r--   0 runner    (1001) docker     (123)     1451 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/steps/row/row_subset.py
--rw-r--r--   0 runner    (1001) docker     (123)     1596 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/steps/row/row_ungroup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.681770 frictionless-5.8.2/frictionless/steps/table/
--rw-r--r--   0 runner    (1001) docker     (123)      591 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/steps/table/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1219 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/steps/table/table_aggregate.py
--rw-r--r--   0 runner    (1001) docker     (123)     1274 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/steps/table/table_attach.py
--rw-r--r--   0 runner    (1001) docker     (123)      886 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/steps/table/table_debug.py
--rw-r--r--   0 runner    (1001) docker     (123)     2045 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/steps/table/table_diff.py
--rw-r--r--   0 runner    (1001) docker     (123)     1650 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/steps/table/table_intersect.py
--rw-r--r--   0 runner    (1001) docker     (123)     3457 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/steps/table/table_join.py
--rw-r--r--   0 runner    (1001) docker     (123)     1705 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/steps/table/table_melt.py
--rw-r--r--   0 runner    (1001) docker     (123)     2635 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/steps/table/table_merge.py
--rw-r--r--   0 runner    (1001) docker     (123)      661 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/steps/table/table_normalize.py
--rw-r--r--   0 runner    (1001) docker     (123)     1210 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/steps/table/table_pivot.py
--rw-r--r--   0 runner    (1001) docker     (123)      443 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/steps/table/table_print.py
--rw-r--r--   0 runner    (1001) docker     (123)     1165 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/steps/table/table_recast.py
--rw-r--r--   0 runner    (1001) docker     (123)      533 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/steps/table/table_transpose.py
--rw-r--r--   0 runner    (1001) docker     (123)      953 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/steps/table/table_validate.py
--rw-r--r--   0 runner    (1001) docker     (123)      899 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/steps/table/table_write.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.685770 frictionless-5.8.2/frictionless/system/
--rw-r--r--   0 runner    (1001) docker     (123)      172 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/system/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      783 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/system/adapter.py
--rw-r--r--   0 runner    (1001) docker     (123)    10607 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/system/loader.py
--rw-r--r--   0 runner    (1001) docker     (123)      353 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/system/mapper.py
--rw-r--r--   0 runner    (1001) docker     (123)     5403 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/system/parser.py
--rw-r--r--   0 runner    (1001) docker     (123)     2575 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/system/plugin.py
--rw-r--r--   0 runner    (1001) docker     (123)    12034 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/system/system.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.685770 frictionless-5.8.2/frictionless/table/
--rw-r--r--   0 runner    (1001) docker     (123)      101 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/table/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     6615 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/table/header.py
--rw-r--r--   0 runner    (1001) docker     (123)       77 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/table/interfaces.py
--rw-r--r--   0 runner    (1001) docker     (123)       29 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/table/lookup.py
--rw-r--r--   0 runner    (1001) docker     (123)    11228 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/table/row.py
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/table/table.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.685770 frictionless-5.8.2/frictionless/vendor/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/vendor/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.685770 frictionless-5.8.2/frictionless/vendor/wkt/
--rw-r--r--   0 runner    (1001) docker     (123)       30 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/vendor/wkt/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4297 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/vendor/wkt/grammar.txt
--rw-r--r--   0 runner    (1001) docker     (123)    20691 2023-03-07 11:41:55.000000 frictionless-5.8.2/frictionless/vendor/wkt/parser.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.649769 frictionless-5.8.2/frictionless.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     5538 2023-03-07 11:42:01.000000 frictionless-5.8.2/frictionless.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)    21428 2023-03-07 11:42:01.000000 frictionless-5.8.2/frictionless.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-07 11:42:01.000000 frictionless-5.8.2/frictionless.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       64 2023-03-07 11:42:01.000000 frictionless-5.8.2/frictionless.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-07 11:42:01.000000 frictionless-5.8.2/frictionless.egg-info/not-zip-safe
--rw-r--r--   0 runner    (1001) docker     (123)     1103 2023-03-07 11:42:01.000000 frictionless-5.8.2/frictionless.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       19 2023-03-07 11:42:01.000000 frictionless-5.8.2/frictionless.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)      157 2023-03-07 11:41:55.000000 frictionless-5.8.2/pylama.ini
--rw-r--r--   0 runner    (1001) docker     (123)       30 2023-03-07 11:41:55.000000 frictionless-5.8.2/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)      282 2023-03-07 11:41:55.000000 frictionless-5.8.2/pytest.ini
--rw-r--r--   0 runner    (1001) docker     (123)       67 2023-03-07 11:42:01.705770 frictionless-5.8.2/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     3671 2023-03-07 11:41:55.000000 frictionless-5.8.2/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.645769 frictionless-5.8.2/tests/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.685770 frictionless-5.8.2/tests/actions/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/actions/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      559 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/actions/test_describe.py
--rw-r--r--   0 runner    (1001) docker     (123)      874 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/actions/test_extract.py
--rw-r--r--   0 runner    (1001) docker     (123)     1951 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/actions/test_transform.py
--rw-r--r--   0 runner    (1001) docker     (123)     3007 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/actions/test_validate.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.685770 frictionless-5.8.2/tests/assets/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/assets/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.685770 frictionless-5.8.2/tests/catalog/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/catalog/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      771 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/catalog/test_dereference.py
--rw-r--r--   0 runner    (1001) docker     (123)      363 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/catalog/test_general.py
--rw-r--r--   0 runner    (1001) docker     (123)     1238 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/catalog/test_infer.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.685770 frictionless-5.8.2/tests/checklist/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/checklist/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.685770 frictionless-5.8.2/tests/checklist/check/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/checklist/check/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      284 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/checklist/check/test_convert.py
--rw-r--r--   0 runner    (1001) docker     (123)      161 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/checklist/check/test_general.py
--rw-r--r--   0 runner    (1001) docker     (123)     1050 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/checklist/test_convert.py
--rw-r--r--   0 runner    (1001) docker     (123)     2662 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/checklist/test_general.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.685770 frictionless-5.8.2/tests/detector/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/detector/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     7028 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/detector/test_general.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.685770 frictionless-5.8.2/tests/dialect/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/dialect/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.685770 frictionless-5.8.2/tests/dialect/control/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/dialect/control/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      155 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/dialect/control/test_general.py
--rw-r--r--   0 runner    (1001) docker     (123)      680 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/dialect/test_convert.py
--rw-r--r--   0 runner    (1001) docker     (123)      195 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/dialect/test_describe.py
--rw-r--r--   0 runner    (1001) docker     (123)     1171 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/dialect/test_general.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.685770 frictionless-5.8.2/tests/errors/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/errors/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.685770 frictionless-5.8.2/tests/formats/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/formats/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.685770 frictionless-5.8.2/tests/formats/csv/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/formats/csv/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    11834 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/formats/csv/test_parser.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.685770 frictionless-5.8.2/tests/formats/erd/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/formats/erd/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1620 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/formats/erd/test_mapper.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.689770 frictionless-5.8.2/tests/formats/excel/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/formats/excel/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1174 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/formats/excel/test_adapter.py
--rw-r--r--   0 runner    (1001) docker     (123)      220 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/formats/excel/test_control.py
--rw-r--r--   0 runner    (1001) docker     (123)     1844 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/formats/excel/test_mapper.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.689770 frictionless-5.8.2/tests/formats/gsheets/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/formats/gsheets/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2005 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/formats/gsheets/test_parser.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.689770 frictionless-5.8.2/tests/formats/html/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/formats/html/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1879 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/formats/html/test_parser.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.689770 frictionless-5.8.2/tests/formats/inline/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/formats/inline/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3692 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/formats/inline/test_parser.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.689770 frictionless-5.8.2/tests/formats/json/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/formats/json/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.689770 frictionless-5.8.2/tests/formats/json/parsers/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/formats/json/parsers/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4278 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/formats/json/parsers/test_json.py
--rw-r--r--   0 runner    (1001) docker     (123)     1341 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/formats/json/parsers/test_jsonl.py
--rw-r--r--   0 runner    (1001) docker     (123)      238 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/formats/json/test_control.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.689770 frictionless-5.8.2/tests/formats/jsonschema/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/formats/jsonschema/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3175 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/formats/jsonschema/test_mapper.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.689770 frictionless-5.8.2/tests/formats/markdown/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/formats/markdown/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     7045 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/formats/markdown/test_mapper.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.689770 frictionless-5.8.2/tests/formats/ods/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/formats/ods/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      543 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/formats/ods/test_adapter.py
--rw-r--r--   0 runner    (1001) docker     (123)     3495 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/formats/ods/test_parser.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.689770 frictionless-5.8.2/tests/formats/pandas/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/formats/pandas/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    11094 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/formats/pandas/test_parser.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.689770 frictionless-5.8.2/tests/formats/parquet/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/formats/parquet/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1649 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/formats/parquet/test_parser.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.689770 frictionless-5.8.2/tests/formats/spss/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/formats/spss/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4667 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/formats/spss/test_parser.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.689770 frictionless-5.8.2/tests/formats/sql/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/formats/sql/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      733 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/formats/sql/conftest.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.689770 frictionless-5.8.2/tests/formats/sql/databases/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/formats/sql/databases/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.689770 frictionless-5.8.2/tests/formats/sql/databases/mysql/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/formats/sql/databases/mysql/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     8962 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/formats/sql/databases/mysql/test_adapter.py
--rw-r--r--   0 runner    (1001) docker     (123)     1827 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/formats/sql/databases/mysql/test_parser.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.689770 frictionless-5.8.2/tests/formats/sql/databases/postgres/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/formats/sql/databases/postgres/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     9373 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/formats/sql/databases/postgres/test_adapter.py
--rw-r--r--   0 runner    (1001) docker     (123)     1789 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/formats/sql/databases/postgres/test_parser.py
--rw-r--r--   0 runner    (1001) docker     (123)     9998 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/formats/sql/test_adapter.py
--rw-r--r--   0 runner    (1001) docker     (123)     1368 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/formats/sql/test_mapper.py
--rw-r--r--   0 runner    (1001) docker     (123)     4968 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/formats/sql/test_parser.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.689770 frictionless-5.8.2/tests/formats/yaml/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/formats/yaml/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1055 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/formats/yaml/test_parser.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.689770 frictionless-5.8.2/tests/formats/zip/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/formats/zip/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     6347 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/formats/zip/test_adapter.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.693770 frictionless-5.8.2/tests/inquiry/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/inquiry/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.693770 frictionless-5.8.2/tests/inquiry/task/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/inquiry/task/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      734 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/inquiry/task/test_convert.py
--rw-r--r--   0 runner    (1001) docker     (123)      468 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/inquiry/task/test_general.py
--rw-r--r--   0 runner    (1001) docker     (123)      445 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/inquiry/task/test_validate.py
--rw-r--r--   0 runner    (1001) docker     (123)      981 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/inquiry/test_convert.py
--rw-r--r--   0 runner    (1001) docker     (123)     1210 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/inquiry/test_general.py
--rw-r--r--   0 runner    (1001) docker     (123)     5005 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/inquiry/test_validate.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.693770 frictionless-5.8.2/tests/package/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/package/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     7421 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/package/test_analyze.py
--rw-r--r--   0 runner    (1001) docker     (123)     1248 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/package/test_compression.py
--rw-r--r--   0 runner    (1001) docker     (123)     1964 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/package/test_convert.py
--rw-r--r--   0 runner    (1001) docker     (123)      352 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/package/test_dereference.py
--rw-r--r--   0 runner    (1001) docker     (123)     5825 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/package/test_describe.py
--rw-r--r--   0 runner    (1001) docker     (123)     1403 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/package/test_extract.py
--rw-r--r--   0 runner    (1001) docker     (123)     9379 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/package/test_general.py
--rw-r--r--   0 runner    (1001) docker     (123)     3275 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/package/test_infer.py
--rw-r--r--   0 runner    (1001) docker     (123)     1912 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/package/test_onerror.py
--rw-r--r--   0 runner    (1001) docker     (123)     3348 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/package/test_profile.py
--rw-r--r--   0 runner    (1001) docker     (123)     3288 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/package/test_resources.py
--rw-r--r--   0 runner    (1001) docker     (123)     4357 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/package/test_schema.py
--rw-r--r--   0 runner    (1001) docker     (123)     2093 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/package/test_security.py
--rw-r--r--   0 runner    (1001) docker     (123)     1053 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/package/test_transform.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.693770 frictionless-5.8.2/tests/package/validate/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/package/validate/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    11041 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/package/validate/test_general.py
--rw-r--r--   0 runner    (1001) docker     (123)     1158 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/package/validate/test_parallel.py
--rw-r--r--   0 runner    (1001) docker     (123)     5657 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/package/validate/test_schema.py
--rw-r--r--   0 runner    (1001) docker     (123)     2216 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/package/validate/test_stats.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.693770 frictionless-5.8.2/tests/pipeline/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/pipeline/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.693770 frictionless-5.8.2/tests/pipeline/step/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/pipeline/step/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      269 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/pipeline/step/test_convert.py
--rw-r--r--   0 runner    (1001) docker     (123)      156 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/pipeline/step/test_general.py
--rw-r--r--   0 runner    (1001) docker     (123)     1123 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/pipeline/test_convert.py
--rw-r--r--   0 runner    (1001) docker     (123)      878 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/pipeline/test_general.py
--rw-r--r--   0 runner    (1001) docker     (123)      288 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/pipeline/test_validate.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.693770 frictionless-5.8.2/tests/portals/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/portals/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.693770 frictionless-5.8.2/tests/portals/ckan/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/portals/ckan/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      905 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/portals/ckan/conftest.py
--rw-r--r--   0 runner    (1001) docker     (123)    16583 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/portals/ckan/test_adapter.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.693770 frictionless-5.8.2/tests/portals/github/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/portals/github/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3423 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/portals/github/conftest.py
--rw-r--r--   0 runner    (1001) docker     (123)    29355 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/portals/github/test_adapter.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.693770 frictionless-5.8.2/tests/portals/zenodo/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/portals/zenodo/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1604 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/portals/zenodo/conftest.py
--rw-r--r--   0 runner    (1001) docker     (123)    29559 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/portals/zenodo/test_adapter.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.697770 frictionless-5.8.2/tests/project/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/project/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      740 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/project/test_bytes.py
--rw-r--r--   0 runner    (1001) docker     (123)      767 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/project/test_data.py
--rw-r--r--   0 runner    (1001) docker     (123)    11427 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/project/test_file.py
--rw-r--r--   0 runner    (1001) docker     (123)      864 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/project/test_folder.py
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/project/test_package.py
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/project/test_project.py
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/project/test_table.py
--rw-r--r--   0 runner    (1001) docker     (123)      769 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/project/test_text.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.697770 frictionless-5.8.2/tests/report/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/report/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.697770 frictionless-5.8.2/tests/report/task/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/report/task/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2657 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/report/task/test_convert.py
--rw-r--r--   0 runner    (1001) docker     (123)      521 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/report/task/test_general.py
--rw-r--r--   0 runner    (1001) docker     (123)     2446 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/report/test_convert.py
--rw-r--r--   0 runner    (1001) docker     (123)     1394 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/report/test_general.py
--rw-r--r--   0 runner    (1001) docker     (123)      185 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/report/test_validate.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.697770 frictionless-5.8.2/tests/resource/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/resource/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     8617 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/resource/test_analyze.py
--rw-r--r--   0 runner    (1001) docker     (123)     5099 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/resource/test_compression.py
--rw-r--r--   0 runner    (1001) docker     (123)     3468 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/resource/test_convert.py
--rw-r--r--   0 runner    (1001) docker     (123)     2876 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/resource/test_dereference.py
--rw-r--r--   0 runner    (1001) docker     (123)     8229 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/resource/test_describe.py
--rw-r--r--   0 runner    (1001) docker     (123)     6826 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/resource/test_detector.py
--rw-r--r--   0 runner    (1001) docker     (123)    10533 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/resource/test_dialect.py
--rw-r--r--   0 runner    (1001) docker     (123)     2288 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/resource/test_encoding.py
--rw-r--r--   0 runner    (1001) docker     (123)     3640 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/resource/test_extract.py
--rw-r--r--   0 runner    (1001) docker     (123)      485 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/resource/test_extrapaths.py
--rw-r--r--   0 runner    (1001) docker     (123)     1040 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/resource/test_format.py
--rw-r--r--   0 runner    (1001) docker     (123)    18365 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/resource/test_general.py
--rw-r--r--   0 runner    (1001) docker     (123)     2256 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/resource/test_index.py
--rw-r--r--   0 runner    (1001) docker     (123)     1688 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/resource/test_infer.py
--rw-r--r--   0 runner    (1001) docker     (123)     1523 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/resource/test_innerpath.py
--rw-r--r--   0 runner    (1001) docker     (123)     1583 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/resource/test_onerror.py
--rw-r--r--   0 runner    (1001) docker     (123)     8505 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/resource/test_open.py
--rw-r--r--   0 runner    (1001) docker     (123)     1544 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/resource/test_profile.py
--rw-r--r--   0 runner    (1001) docker     (123)     1518 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/resource/test_read.py
--rw-r--r--   0 runner    (1001) docker     (123)     6663 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/resource/test_schema.py
--rw-r--r--   0 runner    (1001) docker     (123)     2747 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/resource/test_scheme.py
--rw-r--r--   0 runner    (1001) docker     (123)     5597 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/resource/test_security.py
--rw-r--r--   0 runner    (1001) docker     (123)     3125 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/resource/test_stats.py
--rw-r--r--   0 runner    (1001) docker     (123)     1308 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/resource/test_write.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.697770 frictionless-5.8.2/tests/resource/transform/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/resource/transform/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5295 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/resource/transform/test_general.py
--rw-r--r--   0 runner    (1001) docker     (123)      720 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/resource/transform/test_pipeline.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.701770 frictionless-5.8.2/tests/resource/validate/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/resource/validate/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      400 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/resource/validate/test_checklist.py
--rw-r--r--   0 runner    (1001) docker     (123)      642 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/resource/validate/test_compression.py
--rw-r--r--   0 runner    (1001) docker     (123)     4244 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/resource/validate/test_detector.py
--rw-r--r--   0 runner    (1001) docker     (123)     2414 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/resource/validate/test_dialect.py
--rw-r--r--   0 runner    (1001) docker     (123)      665 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/resource/validate/test_encoding.py
--rw-r--r--   0 runner    (1001) docker     (123)      348 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/resource/validate/test_format.py
--rw-r--r--   0 runner    (1001) docker     (123)    14518 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/resource/validate/test_general.py
--rw-r--r--   0 runner    (1001) docker     (123)     9924 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/resource/validate/test_schema.py
--rw-r--r--   0 runner    (1001) docker     (123)      441 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/resource/validate/test_scheme.py
--rw-r--r--   0 runner    (1001) docker     (123)     2588 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/resource/validate/test_stats.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.701770 frictionless-5.8.2/tests/schema/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/schema/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.701770 frictionless-5.8.2/tests/schema/field/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/schema/field/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     8723 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/schema/field/test_constraints.py
--rw-r--r--   0 runner    (1001) docker     (123)      614 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/schema/field/test_convert.py
--rw-r--r--   0 runner    (1001) docker     (123)     1490 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/schema/field/test_custom.py
--rw-r--r--   0 runner    (1001) docker     (123)     3498 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/schema/field/test_general.py
--rw-r--r--   0 runner    (1001) docker     (123)     1221 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/schema/field/test_read.py
--rw-r--r--   0 runner    (1001) docker     (123)     4154 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/schema/test_convert.py
--rw-r--r--   0 runner    (1001) docker     (123)      309 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/schema/test_describe.py
--rw-r--r--   0 runner    (1001) docker     (123)    14453 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/schema/test_general.py
--rw-r--r--   0 runner    (1001) docker     (123)      687 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/schema/test_validate.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.701770 frictionless-5.8.2/tests/schemes/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/schemes/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.701770 frictionless-5.8.2/tests/schemes/aws/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/schemes/aws/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.701770 frictionless-5.8.2/tests/schemes/aws/loaders/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/schemes/aws/loaders/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4178 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/schemes/aws/loaders/test_s3.py
--rw-r--r--   0 runner    (1001) docker     (123)      101 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/schemes/aws/test_control.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.701770 frictionless-5.8.2/tests/schemes/buffer/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/schemes/buffer/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      994 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/schemes/buffer/test_loader.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.701770 frictionless-5.8.2/tests/schemes/local/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/schemes/local/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      669 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/schemes/local/test_loader.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.701770 frictionless-5.8.2/tests/schemes/multipart/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/schemes/multipart/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5279 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/schemes/multipart/test_loader.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.701770 frictionless-5.8.2/tests/schemes/remote/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/schemes/remote/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2552 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/schemes/remote/test_loader.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.701770 frictionless-5.8.2/tests/schemes/stream/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/schemes/stream/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1828 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/schemes/stream/test_loader.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.701770 frictionless-5.8.2/tests/server/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/server/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      494 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/server/conftest.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.705770 frictionless-5.8.2/tests/server/project/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/server/project/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      230 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/server/project/test_connect.py
--rw-r--r--   0 runner    (1001) docker     (123)      393 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/server/project/test_create_directory.py
--rw-r--r--   0 runner    (1001) docker     (123)      686 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/server/project/test_create_file.py
--rw-r--r--   0 runner    (1001) docker     (123)     1079 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/server/project/test_delete_file.py
--rw-r--r--   0 runner    (1001) docker     (123)      685 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/server/project/test_list_files.py
--rw-r--r--   0 runner    (1001) docker     (123)      492 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/server/project/test_list_folders.py
--rw-r--r--   0 runner    (1001) docker     (123)      754 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/server/project/test_move_file.py
--rw-r--r--   0 runner    (1001) docker     (123)      285 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/server/project/test_read_file.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.705770 frictionless-5.8.2/tests/server/resource/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/server/resource/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/server/test_server.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.705770 frictionless-5.8.2/tests/system/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/system/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/system/test_plugin.py
--rw-r--r--   0 runner    (1001) docker     (123)      662 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/system/test_system.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 11:42:01.705770 frictionless-5.8.2/tests/table/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/table/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1239 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/table/test_header.py
--rw-r--r--   0 runner    (1001) docker     (123)     2135 2023-03-07 11:41:55.000000 frictionless-5.8.2/tests/table/test_row.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.528933 frictionless-5.8.3/
+-rw-r--r--   0 runner    (1001) docker     (123)     2404 2023-03-07 12:42:00.000000 frictionless-5.8.3/AUTHORS.md
+-rw-r--r--   0 runner    (1001) docker     (123)     1097 2023-03-07 12:42:00.000000 frictionless-5.8.3/LICENSE.md
+-rw-r--r--   0 runner    (1001) docker     (123)      125 2023-03-07 12:42:00.000000 frictionless-5.8.3/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     1306 2023-03-07 12:42:00.000000 frictionless-5.8.3/Makefile
+-rw-r--r--   0 runner    (1001) docker     (123)     5538 2023-03-07 12:42:04.528933 frictionless-5.8.3/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     3565 2023-03-07 12:42:00.000000 frictionless-5.8.3/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.464933 frictionless-5.8.3/frictionless/
+-rw-r--r--   0 runner    (1001) docker     (123)      772 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)       96 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/__main__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.468933 frictionless-5.8.3/frictionless/actions/
+-rw-r--r--   0 runner    (1001) docker     (123)      124 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/actions/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1392 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/actions/describe.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3477 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/actions/extract.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2111 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/actions/transform.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4410 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/actions/validate.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.468933 frictionless-5.8.3/frictionless/assets/
+-rw-r--r--   0 runner    (1001) docker     (123)        6 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/assets/VERSION
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.468933 frictionless-5.8.3/frictionless/assets/profiles/
+-rw-r--r--   0 runner    (1001) docker     (123)     8260 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/assets/profiles/geojson.json
+-rw-r--r--   0 runner    (1001) docker     (123)    10245 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/assets/profiles/topojson.json
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.468933 frictionless-5.8.3/frictionless/assets/templates/
+-rw-r--r--   0 runner    (1001) docker     (123)      228 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/assets/templates/checklist.md
+-rw-r--r--   0 runner    (1001) docker     (123)      115 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/assets/templates/detector.md
+-rw-r--r--   0 runner    (1001) docker     (123)      184 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/assets/templates/dialect.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.468933 frictionless-5.8.3/frictionless/assets/templates/erd/
+-rw-r--r--   0 runner    (1001) docker     (123)      133 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/assets/templates/erd/field.html
+-rw-r--r--   0 runner    (1001) docker     (123)       50 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/assets/templates/erd/graph.html
+-rw-r--r--   0 runner    (1001) docker     (123)      147 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/assets/templates/erd/primary_key_field.html
+-rw-r--r--   0 runner    (1001) docker     (123)      228 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/assets/templates/erd/table.html
+-rw-r--r--   0 runner    (1001) docker     (123)      499 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/assets/templates/field-table.md
+-rw-r--r--   0 runner    (1001) docker     (123)      489 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/assets/templates/field.md
+-rw-r--r--   0 runner    (1001) docker     (123)      353 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/assets/templates/inquiry.md
+-rw-r--r--   0 runner    (1001) docker     (123)      268 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/assets/templates/package-table.md
+-rw-r--r--   0 runner    (1001) docker     (123)      262 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/assets/templates/package.md
+-rw-r--r--   0 runner    (1001) docker     (123)      242 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/assets/templates/pipeline.md
+-rw-r--r--   0 runner    (1001) docker     (123)      172 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/assets/templates/report-task.md
+-rw-r--r--   0 runner    (1001) docker     (123)      239 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/assets/templates/report.md
+-rw-r--r--   0 runner    (1001) docker     (123)      434 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/assets/templates/resource-table.md
+-rw-r--r--   0 runner    (1001) docker     (123)      473 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/assets/templates/resource.md
+-rw-r--r--   0 runner    (1001) docker     (123)       45 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/assets/templates/schema-table.md
+-rw-r--r--   0 runner    (1001) docker     (123)       85 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/assets/templates/schema.md
+-rw-r--r--   0 runner    (1001) docker     (123)       97 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/assets/templates/step.md
+-rw-r--r--   0 runner    (1001) docker     (123)      222 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/assets/templates/task.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.472933 frictionless-5.8.3/frictionless/catalog/
+-rw-r--r--   0 runner    (1001) docker     (123)       58 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/catalog/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6449 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/catalog/catalog.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3037 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/catalog/dataset.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.472933 frictionless-5.8.3/frictionless/checklist/
+-rw-r--r--   0 runner    (1001) docker     (123)       58 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/checklist/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3610 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/checklist/check.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4848 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/checklist/checklist.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.472933 frictionless-5.8.3/frictionless/checks/
+-rw-r--r--   0 runner    (1001) docker     (123)       91 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/checks/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2996 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/checks/baseline.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.472933 frictionless-5.8.3/frictionless/checks/cell/
+-rw-r--r--   0 runner    (1001) docker     (123)      301 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/checks/cell/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      975 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/checks/cell/ascii_value.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2879 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/checks/cell/deviated_cell.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3361 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/checks/cell/deviated_value.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1351 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/checks/cell/forbidden_value.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2104 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/checks/cell/required_value.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1523 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/checks/cell/sequential_value.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1368 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/checks/cell/truncated_value.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.472933 frictionless-5.8.3/frictionless/checks/row/
+-rw-r--r--   0 runner    (1001) docker     (123)       84 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/checks/row/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      882 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/checks/row/duplicate_row.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1190 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/checks/row/row_constraint.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.472933 frictionless-5.8.3/frictionless/checks/table/
+-rw-r--r--   0 runner    (1001) docker     (123)       47 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/checks/table/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3886 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/checks/table/table_dimensions.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.472933 frictionless-5.8.3/frictionless/detector/
+-rw-r--r--   0 runner    (1001) docker     (123)       31 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/detector/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15886 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/detector/detector.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.472933 frictionless-5.8.3/frictionless/dialect/
+-rw-r--r--   0 runner    (1001) docker     (123)       58 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/dialect/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1998 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/dialect/control.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9212 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/dialect/dialect.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.472933 frictionless-5.8.3/frictionless/error/
+-rw-r--r--   0 runner    (1001) docker     (123)       25 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/error/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2989 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/error/error.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.472933 frictionless-5.8.3/frictionless/errors/
+-rw-r--r--   0 runner    (1001) docker     (123)      191 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/errors/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4792 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/errors/cell.py
+-rw-r--r--   0 runner    (1001) docker     (123)      215 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/errors/data.py
+-rw-r--r--   0 runner    (1001) docker     (123)      726 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/errors/file.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1038 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/errors/header.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2387 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/errors/label.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3485 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/errors/metadata.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1505 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/errors/resource.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3754 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/errors/row.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1628 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/errors/table.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1050 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/exception.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.476933 frictionless-5.8.3/frictionless/fields/
+-rw-r--r--   0 runner    (1001) docker     (123)      484 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/fields/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      236 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/fields/any.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2500 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/fields/array.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1695 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/fields/boolean.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1868 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/fields/date.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1715 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/fields/datetime.py
+-rw-r--r--   0 runner    (1001) docker     (123)      962 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/fields/duration.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1675 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/fields/geojson.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2142 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/fields/geopoint.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1858 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/fields/integer.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3619 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/fields/number.py
+-rw-r--r--   0 runner    (1001) docker     (123)      954 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/fields/object.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2941 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/fields/string.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1800 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/fields/time.py
+-rw-r--r--   0 runner    (1001) docker     (123)      975 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/fields/year.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1330 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/fields/yearmonth.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.476933 frictionless-5.8.3/frictionless/formats/
+-rw-r--r--   0 runner    (1001) docker     (123)      355 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.476933 frictionless-5.8.3/frictionless/formats/csv/
+-rw-r--r--   0 runner    (1001) docker     (123)       92 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/csv/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2742 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/csv/control.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3144 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/csv/parser.py
+-rw-r--r--   0 runner    (1001) docker     (123)      786 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/csv/plugin.py
+-rw-r--r--   0 runner    (1001) docker     (123)      187 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/csv/settings.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.476933 frictionless-5.8.3/frictionless/formats/erd/
+-rw-r--r--   0 runner    (1001) docker     (123)       30 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/erd/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2051 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/erd/mapper.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.476933 frictionless-5.8.3/frictionless/formats/excel/
+-rw-r--r--   0 runner    (1001) docker     (123)      175 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/excel/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1213 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/excel/adapter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1669 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/excel/control.py
+-rw-r--r--   0 runner    (1001) docker     (123)      416 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/excel/mapper.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.476933 frictionless-5.8.3/frictionless/formats/excel/parsers/
+-rw-r--r--   0 runner    (1001) docker     (123)       56 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/excel/parsers/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3939 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/excel/parsers/xls.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14420 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/excel/parsers/xlsx.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1129 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/excel/plugin.py
+-rw-r--r--   0 runner    (1001) docker     (123)      885 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/excel/settings.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.476933 frictionless-5.8.3/frictionless/formats/gsheets/
+-rw-r--r--   0 runner    (1001) docker     (123)      104 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/gsheets/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      516 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/gsheets/control.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1977 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/gsheets/parser.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1135 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/gsheets/plugin.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.476933 frictionless-5.8.3/frictionless/formats/html/
+-rw-r--r--   0 runner    (1001) docker     (123)       95 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/html/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      581 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/html/control.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2212 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/html/parser.py
+-rw-r--r--   0 runner    (1001) docker     (123)      723 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/html/plugin.py
+-rw-r--r--   0 runner    (1001) docker     (123)       74 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/html/settings.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.480933 frictionless-5.8.3/frictionless/formats/inline/
+-rw-r--r--   0 runner    (1001) docker     (123)      101 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/inline/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      746 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/inline/control.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2619 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/inline/parser.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1028 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/inline/plugin.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.480933 frictionless-5.8.3/frictionless/formats/json/
+-rw-r--r--   0 runner    (1001) docker     (123)      109 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/json/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      965 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/json/control.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.480933 frictionless-5.8.3/frictionless/formats/json/parsers/
+-rw-r--r--   0 runner    (1001) docker     (123)       60 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/json/parsers/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2147 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/json/parsers/json.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1771 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/json/parsers/jsonl.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1194 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/json/plugin.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.480933 frictionless-5.8.3/frictionless/formats/jsonschema/
+-rw-r--r--   0 runner    (1001) docker     (123)       37 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/jsonschema/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1273 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/jsonschema/mapper.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.480933 frictionless-5.8.3/frictionless/formats/markdown/
+-rw-r--r--   0 runner    (1001) docker     (123)       70 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/markdown/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4217 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/markdown/mapper.py
+-rw-r--r--   0 runner    (1001) docker     (123)      450 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/markdown/plugin.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.480933 frictionless-5.8.3/frictionless/formats/ods/
+-rw-r--r--   0 runner    (1001) docker     (123)      124 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/ods/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1234 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/ods/adapter.py
+-rw-r--r--   0 runner    (1001) docker     (123)      559 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/ods/control.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3167 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/ods/parser.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1063 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/ods/plugin.py
+-rw-r--r--   0 runner    (1001) docker     (123)       65 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/ods/settings.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.480933 frictionless-5.8.3/frictionless/formats/pandas/
+-rw-r--r--   0 runner    (1001) docker     (123)      101 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/pandas/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      200 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/pandas/control.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7756 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/pandas/parser.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1232 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/pandas/plugin.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.480933 frictionless-5.8.3/frictionless/formats/parquet/
+-rw-r--r--   0 runner    (1001) docker     (123)      104 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/parquet/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1456 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/parquet/control.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1423 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/parquet/parser.py
+-rw-r--r--   0 runner    (1001) docker     (123)      796 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/parquet/plugin.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.480933 frictionless-5.8.3/frictionless/formats/qsv/
+-rw-r--r--   0 runner    (1001) docker     (123)       62 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/qsv/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1096 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/qsv/adapter.py
+-rw-r--r--   0 runner    (1001) docker     (123)      805 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/qsv/mapper.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.480933 frictionless-5.8.3/frictionless/formats/spss/
+-rw-r--r--   0 runner    (1001) docker     (123)       95 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/spss/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      194 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/spss/control.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6463 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/spss/parser.py
+-rw-r--r--   0 runner    (1001) docker     (123)      672 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/spss/plugin.py
+-rw-r--r--   0 runner    (1001) docker     (123)      261 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/spss/settings.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.484933 frictionless-5.8.3/frictionless/formats/sql/
+-rw-r--r--   0 runner    (1001) docker     (123)      230 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/sql/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5052 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/sql/adapter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1557 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/sql/control.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3986 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/sql/indexer.py
+-rw-r--r--   0 runner    (1001) docker     (123)      121 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/sql/interfaces.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11452 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/sql/mapper.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1901 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/sql/parser.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1308 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/sql/plugin.py
+-rw-r--r--   0 runner    (1001) docker     (123)      425 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/sql/settings.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.484933 frictionless-5.8.3/frictionless/formats/yaml/
+-rw-r--r--   0 runner    (1001) docker     (123)       95 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/yaml/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      896 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/yaml/control.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2088 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/yaml/parser.py
+-rw-r--r--   0 runner    (1001) docker     (123)      869 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/yaml/plugin.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.484933 frictionless-5.8.3/frictionless/formats/zip/
+-rw-r--r--   0 runner    (1001) docker     (123)       94 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/zip/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5018 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/zip/adapter.py
+-rw-r--r--   0 runner    (1001) docker     (123)      728 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/zip/control.py
+-rw-r--r--   0 runner    (1001) docker     (123)      539 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/formats/zip/plugin.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11108 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/helpers.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.484933 frictionless-5.8.3/frictionless/inquiry/
+-rw-r--r--   0 runner    (1001) docker     (123)       59 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/inquiry/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3079 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/inquiry/inquiry.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7664 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/inquiry/task.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1233 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/interfaces.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17201 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/metadata.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.484933 frictionless-5.8.3/frictionless/package/
+-rw-r--r--   0 runner    (1001) docker     (123)       29 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/package/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.484933 frictionless-5.8.3/frictionless/package/methods/
+-rw-r--r--   0 runner    (1001) docker     (123)       64 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/package/methods/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      597 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/package/methods/transform.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2551 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/package/methods/validate.py
+-rw-r--r--   0 runner    (1001) docker     (123)    22444 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/package/package.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.484933 frictionless-5.8.3/frictionless/pipeline/
+-rw-r--r--   0 runner    (1001) docker     (123)       58 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/pipeline/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3490 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/pipeline/pipeline.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3029 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/pipeline/step.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8275 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/platform.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.484933 frictionless-5.8.3/frictionless/portals/
+-rw-r--r--   0 runner    (1001) docker     (123)       64 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/portals/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.484933 frictionless-5.8.3/frictionless/portals/ckan/
+-rw-r--r--   0 runner    (1001) docker     (123)       97 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/portals/ckan/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9075 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/portals/ckan/adapter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2226 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/portals/ckan/control.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1268 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/portals/ckan/plugin.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.484933 frictionless-5.8.3/frictionless/portals/github/
+-rw-r--r--   0 runner    (1001) docker     (123)      103 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/portals/github/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9461 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/portals/github/adapter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3165 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/portals/github/control.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1300 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/portals/github/plugin.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.488933 frictionless-5.8.3/frictionless/portals/zenodo/
+-rw-r--r--   0 runner    (1001) docker     (123)      103 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/portals/zenodo/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10570 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/portals/zenodo/adapter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4676 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/portals/zenodo/control.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1116 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/portals/zenodo/plugin.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.488933 frictionless-5.8.3/frictionless/program/
+-rw-r--r--   0 runner    (1001) docker     (123)      223 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/program/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      570 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/program/api.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6785 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/program/common.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3370 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/program/convert.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4934 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/program/describe.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7559 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/program/extract.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2169 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/program/index.py
+-rw-r--r--   0 runner    (1001) docker     (123)      909 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/program/program.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1798 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/program/summary.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2607 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/program/transform.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7178 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/program/validate.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.488933 frictionless-5.8.3/frictionless/project/
+-rw-r--r--   0 runner    (1001) docker     (123)      121 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/project/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)       60 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/project/config.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10588 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/project/database.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7694 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/project/filesystem.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1008 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/project/interfaces.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7140 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/project/project.py
+-rw-r--r--   0 runner    (1001) docker     (123)       94 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/project/settings.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.488933 frictionless-5.8.3/frictionless/report/
+-rw-r--r--   0 runner    (1001) docker     (123)       56 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/report/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      429 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/report/interfaces.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8783 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/report/report.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4717 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/report/task.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.488933 frictionless-5.8.3/frictionless/resource/
+-rw-r--r--   0 runner    (1001) docker     (123)       31 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/resource/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.488933 frictionless-5.8.3/frictionless/resource/methods/
+-rw-r--r--   0 runner    (1001) docker     (123)       93 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/resource/methods/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10168 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/resource/methods/analyze.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2223 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/resource/methods/transform.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3951 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/resource/methods/validate.py
+-rw-r--r--   0 runner    (1001) docker     (123)    45922 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/resource/resource.py
+-rw-r--r--   0 runner    (1001) docker     (123)      608 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/resource/stats.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.492933 frictionless-5.8.3/frictionless/resources/
+-rw-r--r--   0 runner    (1001) docker     (123)      169 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/resources/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)       91 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/resources/chart.py
+-rw-r--r--   0 runner    (1001) docker     (123)      104 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/resources/file.py
+-rw-r--r--   0 runner    (1001) docker     (123)      104 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/resources/json.py
+-rw-r--r--   0 runner    (1001) docker     (123)      702 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/resources/metadata.py
+-rw-r--r--   0 runner    (1001) docker     (123)       95 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/resources/package.py
+-rw-r--r--   0 runner    (1001) docker     (123)      107 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/resources/table.py
+-rw-r--r--   0 runner    (1001) docker     (123)      168 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/resources/text.py
+-rw-r--r--   0 runner    (1001) docker     (123)      107 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/resources/view.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.492933 frictionless-5.8.3/frictionless/schema/
+-rw-r--r--   0 runner    (1001) docker     (123)       52 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/schema/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9608 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/schema/field.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12063 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/schema/schema.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.492933 frictionless-5.8.3/frictionless/schemes/
+-rw-r--r--   0 runner    (1001) docker     (123)      131 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/schemes/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.492933 frictionless-5.8.3/frictionless/schemes/aws/
+-rw-r--r--   0 runner    (1001) docker     (123)       92 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/schemes/aws/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      476 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/schemes/aws/control.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.492933 frictionless-5.8.3/frictionless/schemes/aws/loaders/
+-rw-r--r--   0 runner    (1001) docker     (123)       25 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/schemes/aws/loaders/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2905 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/schemes/aws/loaders/s3.py
+-rw-r--r--   0 runner    (1001) docker     (123)      404 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/schemes/aws/plugin.py
+-rw-r--r--   0 runner    (1001) docker     (123)      100 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/schemes/aws/settings.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.492933 frictionless-5.8.3/frictionless/schemes/buffer/
+-rw-r--r--   0 runner    (1001) docker     (123)      101 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/schemes/buffer/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      200 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/schemes/buffer/control.py
+-rw-r--r--   0 runner    (1001) docker     (123)      496 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/schemes/buffer/loader.py
+-rw-r--r--   0 runner    (1001) docker     (123)      780 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/schemes/buffer/plugin.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.492933 frictionless-5.8.3/frictionless/schemes/local/
+-rw-r--r--   0 runner    (1001) docker     (123)       98 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/schemes/local/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      197 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/schemes/local/control.py
+-rw-r--r--   0 runner    (1001) docker     (123)      620 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/schemes/local/loader.py
+-rw-r--r--   0 runner    (1001) docker     (123)      522 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/schemes/local/plugin.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.492933 frictionless-5.8.3/frictionless/schemes/multipart/
+-rw-r--r--   0 runner    (1001) docker     (123)      110 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/schemes/multipart/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      483 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/schemes/multipart/control.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2844 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/schemes/multipart/loader.py
+-rw-r--r--   0 runner    (1001) docker     (123)      674 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/schemes/multipart/plugin.py
+-rw-r--r--   0 runner    (1001) docker     (123)       78 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/schemes/multipart/settings.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.492933 frictionless-5.8.3/frictionless/schemes/remote/
+-rw-r--r--   0 runner    (1001) docker     (123)      101 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/schemes/remote/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      553 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/schemes/remote/control.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2531 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/schemes/remote/loader.py
+-rw-r--r--   0 runner    (1001) docker     (123)      600 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/schemes/remote/plugin.py
+-rw-r--r--   0 runner    (1001) docker     (123)      124 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/schemes/remote/settings.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.492933 frictionless-5.8.3/frictionless/schemes/stream/
+-rw-r--r--   0 runner    (1001) docker     (123)      101 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/schemes/stream/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      200 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/schemes/stream/control.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1607 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/schemes/stream/loader.py
+-rw-r--r--   0 runner    (1001) docker     (123)      832 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/schemes/stream/plugin.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.492933 frictionless-5.8.3/frictionless/server/
+-rw-r--r--   0 runner    (1001) docker     (123)      256 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/server/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.496933 frictionless-5.8.3/frictionless/server/bytes/
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/server/bytes/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      527 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/server/bytes/read.py
+-rw-r--r--   0 runner    (1001) docker     (123)      610 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/server/config.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.496933 frictionless-5.8.3/frictionless/server/data/
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/server/data/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      488 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/server/data/read.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.496933 frictionless-5.8.3/frictionless/server/field/
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/server/field/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      494 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/server/field/list.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.496933 frictionless-5.8.3/frictionless/server/file/
+-rw-r--r--   0 runner    (1001) docker     (123)      240 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/server/file/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      581 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/server/file/copy.py
+-rw-r--r--   0 runner    (1001) docker     (123)      463 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/server/file/count.py
+-rw-r--r--   0 runner    (1001) docker     (123)      781 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/server/file/create.py
+-rw-r--r--   0 runner    (1001) docker     (123)      484 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/server/file/delete.py
+-rw-r--r--   0 runner    (1001) docker     (123)      501 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/server/file/index.py
+-rw-r--r--   0 runner    (1001) docker     (123)      489 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/server/file/list.py
+-rw-r--r--   0 runner    (1001) docker     (123)      526 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/server/file/move.py
+-rw-r--r--   0 runner    (1001) docker     (123)      498 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/server/file/read.py
+-rw-r--r--   0 runner    (1001) docker     (123)      516 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/server/file/rename.py
+-rw-r--r--   0 runner    (1001) docker     (123)      464 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/server/file/update.py
+-rw-r--r--   0 runner    (1001) docker     (123)      689 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/server/file/upload.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.496933 frictionless-5.8.3/frictionless/server/folder/
+-rw-r--r--   0 runner    (1001) docker     (123)       40 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/server/folder/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      538 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/server/folder/create.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.496933 frictionless-5.8.3/frictionless/server/package/
+-rw-r--r--   0 runner    (1001) docker     (123)       62 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/server/package/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      470 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/server/package/create.py
+-rw-r--r--   0 runner    (1001) docker     (123)      578 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/server/package/publish.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.496933 frictionless-5.8.3/frictionless/server/project/
+-rw-r--r--   0 runner    (1001) docker     (123)       81 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/server/project/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      588 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/server/project/connect.py
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/server/project/index.py
+-rw-r--r--   0 runner    (1001) docker     (123)      512 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/server/project/query.py
+-rw-r--r--   0 runner    (1001) docker     (123)       53 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/server/router.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1092 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/server/server.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.496933 frictionless-5.8.3/frictionless/server/table/
+-rw-r--r--   0 runner    (1001) docker     (123)       58 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/server/table/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      502 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/server/table/query.py
+-rw-r--r--   0 runner    (1001) docker     (123)      672 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/server/table/read.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.496933 frictionless-5.8.3/frictionless/server/text/
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/server/text/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      479 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/server/text/read.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3640 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/settings.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.496933 frictionless-5.8.3/frictionless/standards/
+-rw-r--r--   0 runner    (1001) docker     (123)       71 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/standards/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.496933 frictionless-5.8.3/frictionless/standards/core/
+-rw-r--r--   0 runner    (1001) docker     (123)       92 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/standards/core/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1031 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/standards/core/dialect.py
+-rw-r--r--   0 runner    (1001) docker     (123)      288 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/standards/core/package.py
+-rw-r--r--   0 runner    (1001) docker     (123)      880 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/standards/core/resource.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2078 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/standards/core/schema.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.500933 frictionless-5.8.3/frictionless/standards/labs/
+-rw-r--r--   0 runner    (1001) docker     (123)      138 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/standards/labs/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      449 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/standards/labs/catalog.py
+-rw-r--r--   0 runner    (1001) docker     (123)      408 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/standards/labs/checklist.py
+-rw-r--r--   0 runner    (1001) docker     (123)      199 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/standards/labs/error.py
+-rw-r--r--   0 runner    (1001) docker     (123)      365 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/standards/labs/inquiry.py
+-rw-r--r--   0 runner    (1001) docker     (123)      362 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/standards/labs/pipeline.py
+-rw-r--r--   0 runner    (1001) docker     (123)      495 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/standards/labs/report.py
+-rw-r--r--   0 runner    (1001) docker     (123)      445 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/standards/standard.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.500933 frictionless-5.8.3/frictionless/steps/
+-rw-r--r--   0 runner    (1001) docker     (123)      105 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/steps/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.500933 frictionless-5.8.3/frictionless/steps/cell/
+-rw-r--r--   0 runner    (1001) docker     (123)      226 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/steps/cell/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1513 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/steps/cell/cell_convert.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1541 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/steps/cell/cell_fill.py
+-rw-r--r--   0 runner    (1001) docker     (123)      972 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/steps/cell/cell_format.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1004 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/steps/cell/cell_interpolate.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1382 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/steps/cell/cell_replace.py
+-rw-r--r--   0 runner    (1001) docker     (123)      710 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/steps/cell/cell_set.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.500933 frictionless-5.8.3/frictionless/steps/field/
+-rw-r--r--   0 runner    (1001) docker     (123)      333 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/steps/field/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2775 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/steps/field/field_add.py
+-rw-r--r--   0 runner    (1001) docker     (123)      909 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/steps/field/field_filter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2613 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/steps/field/field_merge.py
+-rw-r--r--   0 runner    (1001) docker     (123)      956 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/steps/field/field_move.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3638 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/steps/field/field_pack.py
+-rw-r--r--   0 runner    (1001) docker     (123)      916 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/steps/field/field_remove.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1728 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/steps/field/field_split.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1497 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/steps/field/field_unpack.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2021 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/steps/field/field_update.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.500933 frictionless-5.8.3/frictionless/steps/resource/
+-rw-r--r--   0 runner    (1001) docker     (123)      180 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/steps/resource/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      945 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/steps/resource/resource_add.py
+-rw-r--r--   0 runner    (1001) docker     (123)      893 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/steps/resource/resource_remove.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1201 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/steps/resource/resource_transform.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1562 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/steps/resource/resource_update.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.500933 frictionless-5.8.3/frictionless/steps/row/
+-rw-r--r--   0 runner    (1001) docker     (123)      239 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/steps/row/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1223 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/steps/row/row_filter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1353 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/steps/row/row_search.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1446 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/steps/row/row_slice.py
+-rw-r--r--   0 runner    (1001) docker     (123)      939 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/steps/row/row_sort.py
+-rw-r--r--   0 runner    (1001) docker     (123)      847 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/steps/row/row_split.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1451 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/steps/row/row_subset.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1596 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/steps/row/row_ungroup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.504933 frictionless-5.8.3/frictionless/steps/table/
+-rw-r--r--   0 runner    (1001) docker     (123)      591 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/steps/table/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1219 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/steps/table/table_aggregate.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1274 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/steps/table/table_attach.py
+-rw-r--r--   0 runner    (1001) docker     (123)      886 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/steps/table/table_debug.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2045 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/steps/table/table_diff.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1650 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/steps/table/table_intersect.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3457 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/steps/table/table_join.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1705 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/steps/table/table_melt.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2635 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/steps/table/table_merge.py
+-rw-r--r--   0 runner    (1001) docker     (123)      661 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/steps/table/table_normalize.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1210 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/steps/table/table_pivot.py
+-rw-r--r--   0 runner    (1001) docker     (123)      443 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/steps/table/table_print.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1165 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/steps/table/table_recast.py
+-rw-r--r--   0 runner    (1001) docker     (123)      533 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/steps/table/table_transpose.py
+-rw-r--r--   0 runner    (1001) docker     (123)      953 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/steps/table/table_validate.py
+-rw-r--r--   0 runner    (1001) docker     (123)      899 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/steps/table/table_write.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.504933 frictionless-5.8.3/frictionless/system/
+-rw-r--r--   0 runner    (1001) docker     (123)      172 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/system/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      783 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/system/adapter.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10607 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/system/loader.py
+-rw-r--r--   0 runner    (1001) docker     (123)      353 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/system/mapper.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5403 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/system/parser.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2575 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/system/plugin.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12034 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/system/system.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.504933 frictionless-5.8.3/frictionless/table/
+-rw-r--r--   0 runner    (1001) docker     (123)      101 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/table/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6615 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/table/header.py
+-rw-r--r--   0 runner    (1001) docker     (123)       77 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/table/interfaces.py
+-rw-r--r--   0 runner    (1001) docker     (123)       29 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/table/lookup.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11228 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/table/row.py
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/table/table.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.504933 frictionless-5.8.3/frictionless/vendor/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/vendor/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.504933 frictionless-5.8.3/frictionless/vendor/wkt/
+-rw-r--r--   0 runner    (1001) docker     (123)       30 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/vendor/wkt/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4297 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/vendor/wkt/grammar.txt
+-rw-r--r--   0 runner    (1001) docker     (123)    20691 2023-03-07 12:42:01.000000 frictionless-5.8.3/frictionless/vendor/wkt/parser.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.468933 frictionless-5.8.3/frictionless.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     5538 2023-03-07 12:42:04.000000 frictionless-5.8.3/frictionless.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)    21428 2023-03-07 12:42:04.000000 frictionless-5.8.3/frictionless.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-07 12:42:04.000000 frictionless-5.8.3/frictionless.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       64 2023-03-07 12:42:04.000000 frictionless-5.8.3/frictionless.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-07 12:42:04.000000 frictionless-5.8.3/frictionless.egg-info/not-zip-safe
+-rw-r--r--   0 runner    (1001) docker     (123)     1103 2023-03-07 12:42:04.000000 frictionless-5.8.3/frictionless.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       19 2023-03-07 12:42:04.000000 frictionless-5.8.3/frictionless.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      157 2023-03-07 12:42:01.000000 frictionless-5.8.3/pylama.ini
+-rw-r--r--   0 runner    (1001) docker     (123)       30 2023-03-07 12:42:01.000000 frictionless-5.8.3/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)      282 2023-03-07 12:42:01.000000 frictionless-5.8.3/pytest.ini
+-rw-r--r--   0 runner    (1001) docker     (123)       67 2023-03-07 12:42:04.528933 frictionless-5.8.3/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     3671 2023-03-07 12:42:01.000000 frictionless-5.8.3/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.464933 frictionless-5.8.3/tests/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.504933 frictionless-5.8.3/tests/actions/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/actions/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      559 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/actions/test_describe.py
+-rw-r--r--   0 runner    (1001) docker     (123)      874 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/actions/test_extract.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1951 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/actions/test_transform.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3007 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/actions/test_validate.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.504933 frictionless-5.8.3/tests/assets/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/assets/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.508933 frictionless-5.8.3/tests/catalog/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/catalog/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      771 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/catalog/test_dereference.py
+-rw-r--r--   0 runner    (1001) docker     (123)      363 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/catalog/test_general.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1238 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/catalog/test_infer.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.508933 frictionless-5.8.3/tests/checklist/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/checklist/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.508933 frictionless-5.8.3/tests/checklist/check/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/checklist/check/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      284 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/checklist/check/test_convert.py
+-rw-r--r--   0 runner    (1001) docker     (123)      161 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/checklist/check/test_general.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1050 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/checklist/test_convert.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2662 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/checklist/test_general.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.508933 frictionless-5.8.3/tests/detector/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/detector/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7028 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/detector/test_general.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.508933 frictionless-5.8.3/tests/dialect/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/dialect/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.508933 frictionless-5.8.3/tests/dialect/control/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/dialect/control/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      155 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/dialect/control/test_general.py
+-rw-r--r--   0 runner    (1001) docker     (123)      680 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/dialect/test_convert.py
+-rw-r--r--   0 runner    (1001) docker     (123)      195 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/dialect/test_describe.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1171 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/dialect/test_general.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.508933 frictionless-5.8.3/tests/errors/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/errors/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.508933 frictionless-5.8.3/tests/formats/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/formats/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.508933 frictionless-5.8.3/tests/formats/csv/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/formats/csv/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11834 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/formats/csv/test_parser.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.508933 frictionless-5.8.3/tests/formats/erd/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/formats/erd/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1620 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/formats/erd/test_mapper.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.508933 frictionless-5.8.3/tests/formats/excel/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/formats/excel/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1174 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/formats/excel/test_adapter.py
+-rw-r--r--   0 runner    (1001) docker     (123)      220 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/formats/excel/test_control.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1844 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/formats/excel/test_mapper.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.508933 frictionless-5.8.3/tests/formats/gsheets/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/formats/gsheets/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2005 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/formats/gsheets/test_parser.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.508933 frictionless-5.8.3/tests/formats/html/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/formats/html/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1879 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/formats/html/test_parser.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.508933 frictionless-5.8.3/tests/formats/inline/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/formats/inline/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3692 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/formats/inline/test_parser.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.508933 frictionless-5.8.3/tests/formats/json/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/formats/json/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.508933 frictionless-5.8.3/tests/formats/json/parsers/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/formats/json/parsers/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4278 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/formats/json/parsers/test_json.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1341 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/formats/json/parsers/test_jsonl.py
+-rw-r--r--   0 runner    (1001) docker     (123)      238 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/formats/json/test_control.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.508933 frictionless-5.8.3/tests/formats/jsonschema/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/formats/jsonschema/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3175 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/formats/jsonschema/test_mapper.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.512933 frictionless-5.8.3/tests/formats/markdown/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/formats/markdown/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7045 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/formats/markdown/test_mapper.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.512933 frictionless-5.8.3/tests/formats/ods/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/formats/ods/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      543 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/formats/ods/test_adapter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3495 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/formats/ods/test_parser.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.512933 frictionless-5.8.3/tests/formats/pandas/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/formats/pandas/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11094 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/formats/pandas/test_parser.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.512933 frictionless-5.8.3/tests/formats/parquet/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/formats/parquet/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1649 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/formats/parquet/test_parser.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.512933 frictionless-5.8.3/tests/formats/spss/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/formats/spss/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4667 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/formats/spss/test_parser.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.512933 frictionless-5.8.3/tests/formats/sql/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/formats/sql/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      733 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/formats/sql/conftest.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.512933 frictionless-5.8.3/tests/formats/sql/databases/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/formats/sql/databases/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.512933 frictionless-5.8.3/tests/formats/sql/databases/mysql/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/formats/sql/databases/mysql/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8962 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/formats/sql/databases/mysql/test_adapter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1827 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/formats/sql/databases/mysql/test_parser.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.512933 frictionless-5.8.3/tests/formats/sql/databases/postgres/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/formats/sql/databases/postgres/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9373 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/formats/sql/databases/postgres/test_adapter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1789 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/formats/sql/databases/postgres/test_parser.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9998 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/formats/sql/test_adapter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1368 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/formats/sql/test_mapper.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4968 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/formats/sql/test_parser.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.512933 frictionless-5.8.3/tests/formats/yaml/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/formats/yaml/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1055 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/formats/yaml/test_parser.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.512933 frictionless-5.8.3/tests/formats/zip/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/formats/zip/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6347 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/formats/zip/test_adapter.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.512933 frictionless-5.8.3/tests/inquiry/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/inquiry/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.512933 frictionless-5.8.3/tests/inquiry/task/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/inquiry/task/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      734 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/inquiry/task/test_convert.py
+-rw-r--r--   0 runner    (1001) docker     (123)      468 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/inquiry/task/test_general.py
+-rw-r--r--   0 runner    (1001) docker     (123)      445 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/inquiry/task/test_validate.py
+-rw-r--r--   0 runner    (1001) docker     (123)      981 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/inquiry/test_convert.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1210 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/inquiry/test_general.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5005 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/inquiry/test_validate.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.516933 frictionless-5.8.3/tests/package/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/package/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7421 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/package/test_analyze.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1248 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/package/test_compression.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1964 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/package/test_convert.py
+-rw-r--r--   0 runner    (1001) docker     (123)      352 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/package/test_dereference.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5825 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/package/test_describe.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1403 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/package/test_extract.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9379 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/package/test_general.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3275 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/package/test_infer.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1912 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/package/test_onerror.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3348 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/package/test_profile.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3288 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/package/test_resources.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4357 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/package/test_schema.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2093 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/package/test_security.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1053 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/package/test_transform.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.516933 frictionless-5.8.3/tests/package/validate/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/package/validate/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11041 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/package/validate/test_general.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1158 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/package/validate/test_parallel.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5657 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/package/validate/test_schema.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2216 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/package/validate/test_stats.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.516933 frictionless-5.8.3/tests/pipeline/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/pipeline/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.516933 frictionless-5.8.3/tests/pipeline/step/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/pipeline/step/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      269 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/pipeline/step/test_convert.py
+-rw-r--r--   0 runner    (1001) docker     (123)      156 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/pipeline/step/test_general.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1123 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/pipeline/test_convert.py
+-rw-r--r--   0 runner    (1001) docker     (123)      878 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/pipeline/test_general.py
+-rw-r--r--   0 runner    (1001) docker     (123)      288 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/pipeline/test_validate.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.516933 frictionless-5.8.3/tests/portals/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/portals/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.516933 frictionless-5.8.3/tests/portals/ckan/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/portals/ckan/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      905 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/portals/ckan/conftest.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16583 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/portals/ckan/test_adapter.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.516933 frictionless-5.8.3/tests/portals/github/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/portals/github/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3423 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/portals/github/conftest.py
+-rw-r--r--   0 runner    (1001) docker     (123)    29355 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/portals/github/test_adapter.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.516933 frictionless-5.8.3/tests/portals/zenodo/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/portals/zenodo/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1604 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/portals/zenodo/conftest.py
+-rw-r--r--   0 runner    (1001) docker     (123)    29559 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/portals/zenodo/test_adapter.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.520933 frictionless-5.8.3/tests/project/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/project/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      740 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/project/test_bytes.py
+-rw-r--r--   0 runner    (1001) docker     (123)      767 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/project/test_data.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11427 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/project/test_file.py
+-rw-r--r--   0 runner    (1001) docker     (123)      864 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/project/test_folder.py
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/project/test_package.py
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/project/test_project.py
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/project/test_table.py
+-rw-r--r--   0 runner    (1001) docker     (123)      769 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/project/test_text.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.520933 frictionless-5.8.3/tests/report/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/report/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.520933 frictionless-5.8.3/tests/report/task/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/report/task/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2657 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/report/task/test_convert.py
+-rw-r--r--   0 runner    (1001) docker     (123)      521 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/report/task/test_general.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2446 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/report/test_convert.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1394 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/report/test_general.py
+-rw-r--r--   0 runner    (1001) docker     (123)      185 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/report/test_validate.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.520933 frictionless-5.8.3/tests/resource/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/resource/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8617 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/resource/test_analyze.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5099 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/resource/test_compression.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3468 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/resource/test_convert.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2876 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/resource/test_dereference.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8229 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/resource/test_describe.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6826 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/resource/test_detector.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10533 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/resource/test_dialect.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2288 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/resource/test_encoding.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3640 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/resource/test_extract.py
+-rw-r--r--   0 runner    (1001) docker     (123)      485 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/resource/test_extrapaths.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1040 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/resource/test_format.py
+-rw-r--r--   0 runner    (1001) docker     (123)    18365 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/resource/test_general.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2256 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/resource/test_index.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1688 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/resource/test_infer.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1523 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/resource/test_innerpath.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1583 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/resource/test_onerror.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8505 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/resource/test_open.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1544 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/resource/test_profile.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1518 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/resource/test_read.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6663 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/resource/test_schema.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2747 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/resource/test_scheme.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5597 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/resource/test_security.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3125 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/resource/test_stats.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1308 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/resource/test_write.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.524933 frictionless-5.8.3/tests/resource/transform/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/resource/transform/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5295 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/resource/transform/test_general.py
+-rw-r--r--   0 runner    (1001) docker     (123)      720 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/resource/transform/test_pipeline.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.524933 frictionless-5.8.3/tests/resource/validate/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/resource/validate/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      400 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/resource/validate/test_checklist.py
+-rw-r--r--   0 runner    (1001) docker     (123)      642 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/resource/validate/test_compression.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4244 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/resource/validate/test_detector.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2414 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/resource/validate/test_dialect.py
+-rw-r--r--   0 runner    (1001) docker     (123)      665 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/resource/validate/test_encoding.py
+-rw-r--r--   0 runner    (1001) docker     (123)      348 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/resource/validate/test_format.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14518 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/resource/validate/test_general.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9924 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/resource/validate/test_schema.py
+-rw-r--r--   0 runner    (1001) docker     (123)      441 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/resource/validate/test_scheme.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2588 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/resource/validate/test_stats.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.524933 frictionless-5.8.3/tests/schema/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/schema/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.524933 frictionless-5.8.3/tests/schema/field/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/schema/field/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8723 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/schema/field/test_constraints.py
+-rw-r--r--   0 runner    (1001) docker     (123)      614 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/schema/field/test_convert.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1490 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/schema/field/test_custom.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3498 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/schema/field/test_general.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1221 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/schema/field/test_read.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4154 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/schema/test_convert.py
+-rw-r--r--   0 runner    (1001) docker     (123)      309 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/schema/test_describe.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14453 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/schema/test_general.py
+-rw-r--r--   0 runner    (1001) docker     (123)      687 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/schema/test_validate.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.524933 frictionless-5.8.3/tests/schemes/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/schemes/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.524933 frictionless-5.8.3/tests/schemes/aws/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/schemes/aws/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.524933 frictionless-5.8.3/tests/schemes/aws/loaders/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/schemes/aws/loaders/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4178 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/schemes/aws/loaders/test_s3.py
+-rw-r--r--   0 runner    (1001) docker     (123)      101 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/schemes/aws/test_control.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.524933 frictionless-5.8.3/tests/schemes/buffer/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/schemes/buffer/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      994 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/schemes/buffer/test_loader.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.524933 frictionless-5.8.3/tests/schemes/local/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/schemes/local/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      669 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/schemes/local/test_loader.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.524933 frictionless-5.8.3/tests/schemes/multipart/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/schemes/multipart/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5279 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/schemes/multipart/test_loader.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.524933 frictionless-5.8.3/tests/schemes/remote/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/schemes/remote/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2552 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/schemes/remote/test_loader.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.524933 frictionless-5.8.3/tests/schemes/stream/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/schemes/stream/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1828 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/schemes/stream/test_loader.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.524933 frictionless-5.8.3/tests/server/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/server/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      494 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/server/conftest.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.528933 frictionless-5.8.3/tests/server/project/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/server/project/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      230 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/server/project/test_connect.py
+-rw-r--r--   0 runner    (1001) docker     (123)      393 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/server/project/test_create_directory.py
+-rw-r--r--   0 runner    (1001) docker     (123)      686 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/server/project/test_create_file.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1079 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/server/project/test_delete_file.py
+-rw-r--r--   0 runner    (1001) docker     (123)      685 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/server/project/test_list_files.py
+-rw-r--r--   0 runner    (1001) docker     (123)      492 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/server/project/test_list_folders.py
+-rw-r--r--   0 runner    (1001) docker     (123)      754 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/server/project/test_move_file.py
+-rw-r--r--   0 runner    (1001) docker     (123)      285 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/server/project/test_read_file.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.528933 frictionless-5.8.3/tests/server/resource/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/server/resource/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/server/test_server.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.528933 frictionless-5.8.3/tests/system/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/system/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/system/test_plugin.py
+-rw-r--r--   0 runner    (1001) docker     (123)      662 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/system/test_system.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:04.528933 frictionless-5.8.3/tests/table/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/table/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1239 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/table/test_header.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2135 2023-03-07 12:42:01.000000 frictionless-5.8.3/tests/table/test_row.py
```

### Comparing `frictionless-5.8.2/AUTHORS.md` & `frictionless-5.8.3/AUTHORS.md`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/LICENSE.md` & `frictionless-5.8.3/LICENSE.md`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/Makefile` & `frictionless-5.8.3/Makefile`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/PKG-INFO` & `frictionless-5.8.3/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: frictionless
-Version: 5.8.2
+Version: 5.8.3
 Summary: Data management framework for Python that provides functionality to describe, extract, validate, and transform tabular data
 Home-page: https://github.com/frictionlessdata/frictionless-py
 Author: Open Knowledge Foundation
 Author-email: info@okfn.org
 License: MIT
 Description: # Frictionless Framework
```

### Comparing `frictionless-5.8.2/README.md` & `frictionless-5.8.3/README.md`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/__init__.py` & `frictionless-5.8.3/frictionless/__init__.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/actions/describe.py` & `frictionless-5.8.3/frictionless/actions/describe.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/actions/extract.py` & `frictionless-5.8.3/frictionless/actions/extract.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/actions/transform.py` & `frictionless-5.8.3/frictionless/actions/transform.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/actions/validate.py` & `frictionless-5.8.3/frictionless/actions/validate.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/assets/profiles/geojson.json` & `frictionless-5.8.3/frictionless/assets/profiles/geojson.json`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/assets/profiles/topojson.json` & `frictionless-5.8.3/frictionless/assets/profiles/topojson.json`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/catalog/catalog.py` & `frictionless-5.8.3/frictionless/catalog/catalog.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/catalog/dataset.py` & `frictionless-5.8.3/frictionless/catalog/dataset.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/checklist/check.py` & `frictionless-5.8.3/frictionless/checklist/check.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/checklist/checklist.py` & `frictionless-5.8.3/frictionless/checklist/checklist.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/checks/baseline.py` & `frictionless-5.8.3/frictionless/checks/baseline.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/checks/cell/ascii_value.py` & `frictionless-5.8.3/frictionless/checks/cell/ascii_value.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/checks/cell/deviated_cell.py` & `frictionless-5.8.3/frictionless/checks/cell/deviated_cell.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/checks/cell/deviated_value.py` & `frictionless-5.8.3/frictionless/checks/cell/deviated_value.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/checks/cell/forbidden_value.py` & `frictionless-5.8.3/frictionless/checks/cell/forbidden_value.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/checks/cell/required_value.py` & `frictionless-5.8.3/frictionless/checks/cell/required_value.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/checks/cell/sequential_value.py` & `frictionless-5.8.3/frictionless/checks/cell/sequential_value.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/checks/cell/truncated_value.py` & `frictionless-5.8.3/frictionless/checks/cell/truncated_value.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/checks/row/duplicate_row.py` & `frictionless-5.8.3/frictionless/checks/row/duplicate_row.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/checks/row/row_constraint.py` & `frictionless-5.8.3/frictionless/checks/row/row_constraint.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/checks/table/table_dimensions.py` & `frictionless-5.8.3/frictionless/checks/table/table_dimensions.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/detector/detector.py` & `frictionless-5.8.3/frictionless/detector/detector.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/dialect/control.py` & `frictionless-5.8.3/frictionless/dialect/control.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/dialect/dialect.py` & `frictionless-5.8.3/frictionless/dialect/dialect.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/error/error.py` & `frictionless-5.8.3/frictionless/error/error.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/errors/cell.py` & `frictionless-5.8.3/frictionless/errors/cell.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/errors/file.py` & `frictionless-5.8.3/frictionless/errors/file.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/errors/header.py` & `frictionless-5.8.3/frictionless/errors/header.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/errors/label.py` & `frictionless-5.8.3/frictionless/errors/label.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/errors/metadata.py` & `frictionless-5.8.3/frictionless/errors/metadata.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/errors/resource.py` & `frictionless-5.8.3/frictionless/errors/resource.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/errors/row.py` & `frictionless-5.8.3/frictionless/errors/row.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/errors/table.py` & `frictionless-5.8.3/frictionless/errors/table.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/exception.py` & `frictionless-5.8.3/frictionless/exception.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/fields/array.py` & `frictionless-5.8.3/frictionless/fields/array.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/fields/boolean.py` & `frictionless-5.8.3/frictionless/fields/boolean.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/fields/date.py` & `frictionless-5.8.3/frictionless/fields/date.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/fields/datetime.py` & `frictionless-5.8.3/frictionless/fields/datetime.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/fields/duration.py` & `frictionless-5.8.3/frictionless/fields/duration.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/fields/geojson.py` & `frictionless-5.8.3/frictionless/fields/geojson.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/fields/geopoint.py` & `frictionless-5.8.3/frictionless/fields/geopoint.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/fields/integer.py` & `frictionless-5.8.3/frictionless/fields/integer.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/fields/number.py` & `frictionless-5.8.3/frictionless/fields/number.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/fields/object.py` & `frictionless-5.8.3/frictionless/fields/object.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/fields/string.py` & `frictionless-5.8.3/frictionless/fields/string.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/fields/time.py` & `frictionless-5.8.3/frictionless/fields/time.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/fields/year.py` & `frictionless-5.8.3/frictionless/fields/year.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/fields/yearmonth.py` & `frictionless-5.8.3/frictionless/fields/yearmonth.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/formats/csv/control.py` & `frictionless-5.8.3/frictionless/formats/csv/control.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/formats/csv/parser.py` & `frictionless-5.8.3/frictionless/formats/csv/parser.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/formats/csv/plugin.py` & `frictionless-5.8.3/frictionless/formats/csv/plugin.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/formats/erd/mapper.py` & `frictionless-5.8.3/frictionless/formats/erd/mapper.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/formats/excel/adapter.py` & `frictionless-5.8.3/frictionless/formats/excel/adapter.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/formats/excel/control.py` & `frictionless-5.8.3/frictionless/formats/excel/control.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/formats/excel/parsers/xls.py` & `frictionless-5.8.3/frictionless/formats/excel/parsers/xls.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/formats/excel/parsers/xlsx.py` & `frictionless-5.8.3/frictionless/formats/excel/parsers/xlsx.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/formats/excel/plugin.py` & `frictionless-5.8.3/frictionless/formats/excel/plugin.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/formats/excel/settings.py` & `frictionless-5.8.3/frictionless/formats/excel/settings.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/formats/gsheets/control.py` & `frictionless-5.8.3/frictionless/formats/gsheets/control.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/formats/gsheets/parser.py` & `frictionless-5.8.3/frictionless/formats/gsheets/parser.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/formats/gsheets/plugin.py` & `frictionless-5.8.3/frictionless/formats/gsheets/plugin.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/formats/html/control.py` & `frictionless-5.8.3/frictionless/formats/html/control.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/formats/html/parser.py` & `frictionless-5.8.3/frictionless/formats/html/parser.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/formats/html/plugin.py` & `frictionless-5.8.3/frictionless/formats/html/plugin.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/formats/inline/control.py` & `frictionless-5.8.3/frictionless/formats/inline/control.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/formats/inline/parser.py` & `frictionless-5.8.3/frictionless/formats/inline/parser.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/formats/inline/plugin.py` & `frictionless-5.8.3/frictionless/formats/inline/plugin.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/formats/json/control.py` & `frictionless-5.8.3/frictionless/formats/json/control.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/formats/json/parsers/json.py` & `frictionless-5.8.3/frictionless/formats/json/parsers/json.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/formats/json/parsers/jsonl.py` & `frictionless-5.8.3/frictionless/formats/json/parsers/jsonl.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/formats/json/plugin.py` & `frictionless-5.8.3/frictionless/formats/json/plugin.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/formats/jsonschema/mapper.py` & `frictionless-5.8.3/frictionless/formats/jsonschema/mapper.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/formats/markdown/mapper.py` & `frictionless-5.8.3/frictionless/formats/markdown/mapper.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/formats/ods/adapter.py` & `frictionless-5.8.3/frictionless/formats/ods/adapter.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/formats/ods/control.py` & `frictionless-5.8.3/frictionless/formats/ods/control.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/formats/ods/parser.py` & `frictionless-5.8.3/frictionless/formats/ods/parser.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/formats/ods/plugin.py` & `frictionless-5.8.3/frictionless/formats/ods/plugin.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/formats/pandas/parser.py` & `frictionless-5.8.3/frictionless/formats/pandas/parser.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/formats/pandas/plugin.py` & `frictionless-5.8.3/frictionless/formats/pandas/plugin.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/formats/parquet/control.py` & `frictionless-5.8.3/frictionless/formats/parquet/control.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/formats/parquet/parser.py` & `frictionless-5.8.3/frictionless/formats/parquet/parser.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/formats/parquet/plugin.py` & `frictionless-5.8.3/frictionless/formats/parquet/plugin.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/formats/qsv/adapter.py` & `frictionless-5.8.3/frictionless/formats/qsv/adapter.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/formats/qsv/mapper.py` & `frictionless-5.8.3/frictionless/formats/qsv/mapper.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/formats/spss/parser.py` & `frictionless-5.8.3/frictionless/formats/spss/parser.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/formats/spss/plugin.py` & `frictionless-5.8.3/frictionless/formats/spss/plugin.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/formats/sql/adapter.py` & `frictionless-5.8.3/frictionless/formats/sql/adapter.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/formats/sql/control.py` & `frictionless-5.8.3/frictionless/formats/sql/control.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/formats/sql/indexer.py` & `frictionless-5.8.3/frictionless/formats/sql/indexer.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/formats/sql/mapper.py` & `frictionless-5.8.3/frictionless/formats/sql/mapper.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/formats/sql/parser.py` & `frictionless-5.8.3/frictionless/formats/sql/parser.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/formats/sql/plugin.py` & `frictionless-5.8.3/frictionless/formats/sql/plugin.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/formats/yaml/control.py` & `frictionless-5.8.3/frictionless/formats/yaml/control.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/formats/yaml/parser.py` & `frictionless-5.8.3/frictionless/formats/yaml/parser.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/formats/yaml/plugin.py` & `frictionless-5.8.3/frictionless/formats/yaml/plugin.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/formats/zip/adapter.py` & `frictionless-5.8.3/frictionless/formats/zip/adapter.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/formats/zip/control.py` & `frictionless-5.8.3/frictionless/formats/zip/control.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/formats/zip/plugin.py` & `frictionless-5.8.3/frictionless/formats/zip/plugin.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/helpers.py` & `frictionless-5.8.3/frictionless/helpers.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/inquiry/inquiry.py` & `frictionless-5.8.3/frictionless/inquiry/inquiry.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/inquiry/task.py` & `frictionless-5.8.3/frictionless/inquiry/task.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/interfaces.py` & `frictionless-5.8.3/frictionless/interfaces.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/metadata.py` & `frictionless-5.8.3/frictionless/metadata.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/package/methods/transform.py` & `frictionless-5.8.3/frictionless/package/methods/transform.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/package/methods/validate.py` & `frictionless-5.8.3/frictionless/package/methods/validate.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/package/package.py` & `frictionless-5.8.3/frictionless/package/package.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/pipeline/pipeline.py` & `frictionless-5.8.3/frictionless/pipeline/pipeline.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/pipeline/step.py` & `frictionless-5.8.3/frictionless/pipeline/step.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/platform.py` & `frictionless-5.8.3/frictionless/platform.py`

 * *Files 4% similar despite different names*

```diff
@@ -9,14 +9,17 @@
     """Extra dependency decorator"""
 
     def outer(func):
         def inner(*args, **kwargs):
             try:
                 return func(*args, **kwargs)
             except Exception:
+                if name == "wkt" and sys.version_info >= (3, 10):
+                    note = "WKT is not supported in Python3.10+ (grako is unmaintained)"
+                    raise platform.frictionless.FrictionlessException(note)
                 module = import_module("frictionless.exception")
                 note = f'Please install "frictionless[{name}]"'
                 raise module.FrictionlessException(note)
 
         return inner
 
     return outer
```

### Comparing `frictionless-5.8.2/frictionless/portals/ckan/adapter.py` & `frictionless-5.8.3/frictionless/portals/ckan/adapter.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/portals/ckan/control.py` & `frictionless-5.8.3/frictionless/portals/ckan/control.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/portals/ckan/plugin.py` & `frictionless-5.8.3/frictionless/portals/ckan/plugin.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/portals/github/adapter.py` & `frictionless-5.8.3/frictionless/portals/github/adapter.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/portals/github/control.py` & `frictionless-5.8.3/frictionless/portals/github/control.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/portals/github/plugin.py` & `frictionless-5.8.3/frictionless/portals/github/plugin.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/portals/zenodo/adapter.py` & `frictionless-5.8.3/frictionless/portals/zenodo/adapter.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/portals/zenodo/control.py` & `frictionless-5.8.3/frictionless/portals/zenodo/control.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/portals/zenodo/plugin.py` & `frictionless-5.8.3/frictionless/portals/zenodo/plugin.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/program/api.py` & `frictionless-5.8.3/frictionless/program/api.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/program/common.py` & `frictionless-5.8.3/frictionless/program/common.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/program/convert.py` & `frictionless-5.8.3/frictionless/program/convert.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/program/describe.py` & `frictionless-5.8.3/frictionless/program/describe.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/program/extract.py` & `frictionless-5.8.3/frictionless/program/extract.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/program/index.py` & `frictionless-5.8.3/frictionless/program/index.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/program/program.py` & `frictionless-5.8.3/frictionless/program/program.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/program/summary.py` & `frictionless-5.8.3/frictionless/program/summary.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/program/transform.py` & `frictionless-5.8.3/frictionless/program/transform.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/program/validate.py` & `frictionless-5.8.3/frictionless/program/validate.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/project/database.py` & `frictionless-5.8.3/frictionless/project/database.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/project/filesystem.py` & `frictionless-5.8.3/frictionless/project/filesystem.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/project/interfaces.py` & `frictionless-5.8.3/frictionless/project/interfaces.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/project/project.py` & `frictionless-5.8.3/frictionless/project/project.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/report/report.py` & `frictionless-5.8.3/frictionless/report/report.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/report/task.py` & `frictionless-5.8.3/frictionless/report/task.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/resource/methods/analyze.py` & `frictionless-5.8.3/frictionless/resource/methods/analyze.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/resource/methods/transform.py` & `frictionless-5.8.3/frictionless/resource/methods/transform.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/resource/methods/validate.py` & `frictionless-5.8.3/frictionless/resource/methods/validate.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/resource/resource.py` & `frictionless-5.8.3/frictionless/resource/resource.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/resource/stats.py` & `frictionless-5.8.3/frictionless/resource/stats.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/resources/metadata.py` & `frictionless-5.8.3/frictionless/resources/metadata.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/schema/field.py` & `frictionless-5.8.3/frictionless/schema/field.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/schema/schema.py` & `frictionless-5.8.3/frictionless/schema/schema.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/schemes/aws/loaders/s3.py` & `frictionless-5.8.3/frictionless/schemes/aws/loaders/s3.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/schemes/buffer/plugin.py` & `frictionless-5.8.3/frictionless/schemes/buffer/plugin.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/schemes/local/loader.py` & `frictionless-5.8.3/frictionless/schemes/local/loader.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/schemes/local/plugin.py` & `frictionless-5.8.3/frictionless/schemes/local/plugin.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/schemes/multipart/loader.py` & `frictionless-5.8.3/frictionless/schemes/multipart/loader.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/schemes/multipart/plugin.py` & `frictionless-5.8.3/frictionless/schemes/multipart/plugin.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/schemes/remote/control.py` & `frictionless-5.8.3/frictionless/schemes/remote/control.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/schemes/remote/loader.py` & `frictionless-5.8.3/frictionless/schemes/remote/loader.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/schemes/remote/plugin.py` & `frictionless-5.8.3/frictionless/schemes/remote/plugin.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/schemes/stream/loader.py` & `frictionless-5.8.3/frictionless/schemes/stream/loader.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/schemes/stream/plugin.py` & `frictionless-5.8.3/frictionless/schemes/stream/plugin.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/server/bytes/read.py` & `frictionless-5.8.3/frictionless/server/bytes/read.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/server/config.py` & `frictionless-5.8.3/frictionless/server/config.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/server/file/copy.py` & `frictionless-5.8.3/frictionless/server/file/copy.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/server/file/create.py` & `frictionless-5.8.3/frictionless/server/file/create.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/server/file/move.py` & `frictionless-5.8.3/frictionless/server/file/move.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/server/file/rename.py` & `frictionless-5.8.3/frictionless/server/file/rename.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/server/file/upload.py` & `frictionless-5.8.3/frictionless/server/file/upload.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/server/folder/create.py` & `frictionless-5.8.3/frictionless/server/folder/create.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/server/package/publish.py` & `frictionless-5.8.3/frictionless/server/package/publish.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/server/project/connect.py` & `frictionless-5.8.3/frictionless/server/project/connect.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/server/project/query.py` & `frictionless-5.8.3/frictionless/server/project/query.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/server/server.py` & `frictionless-5.8.3/frictionless/server/server.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/server/table/read.py` & `frictionless-5.8.3/frictionless/server/table/read.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/settings.py` & `frictionless-5.8.3/frictionless/settings.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/standards/core/dialect.py` & `frictionless-5.8.3/frictionless/standards/core/dialect.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/standards/core/resource.py` & `frictionless-5.8.3/frictionless/standards/core/resource.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/standards/core/schema.py` & `frictionless-5.8.3/frictionless/standards/core/schema.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/steps/cell/cell_convert.py` & `frictionless-5.8.3/frictionless/steps/cell/cell_convert.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/steps/cell/cell_fill.py` & `frictionless-5.8.3/frictionless/steps/cell/cell_fill.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/steps/cell/cell_format.py` & `frictionless-5.8.3/frictionless/steps/cell/cell_format.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/steps/cell/cell_interpolate.py` & `frictionless-5.8.3/frictionless/steps/cell/cell_interpolate.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/steps/cell/cell_replace.py` & `frictionless-5.8.3/frictionless/steps/cell/cell_replace.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/steps/cell/cell_set.py` & `frictionless-5.8.3/frictionless/steps/cell/cell_set.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/steps/field/field_add.py` & `frictionless-5.8.3/frictionless/steps/field/field_add.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/steps/field/field_filter.py` & `frictionless-5.8.3/frictionless/steps/field/field_filter.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/steps/field/field_merge.py` & `frictionless-5.8.3/frictionless/steps/field/field_merge.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/steps/field/field_move.py` & `frictionless-5.8.3/frictionless/steps/field/field_move.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/steps/field/field_pack.py` & `frictionless-5.8.3/frictionless/steps/field/field_pack.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/steps/field/field_remove.py` & `frictionless-5.8.3/frictionless/steps/field/field_remove.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/steps/field/field_split.py` & `frictionless-5.8.3/frictionless/steps/field/field_split.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/steps/field/field_unpack.py` & `frictionless-5.8.3/frictionless/steps/field/field_unpack.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/steps/field/field_update.py` & `frictionless-5.8.3/frictionless/steps/field/field_update.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/steps/resource/resource_add.py` & `frictionless-5.8.3/frictionless/steps/resource/resource_add.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/steps/resource/resource_remove.py` & `frictionless-5.8.3/frictionless/steps/resource/resource_remove.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/steps/resource/resource_transform.py` & `frictionless-5.8.3/frictionless/steps/resource/resource_transform.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/steps/resource/resource_update.py` & `frictionless-5.8.3/frictionless/steps/resource/resource_update.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/steps/row/row_filter.py` & `frictionless-5.8.3/frictionless/steps/row/row_filter.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/steps/row/row_search.py` & `frictionless-5.8.3/frictionless/steps/row/row_search.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/steps/row/row_slice.py` & `frictionless-5.8.3/frictionless/steps/row/row_slice.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/steps/row/row_sort.py` & `frictionless-5.8.3/frictionless/steps/row/row_sort.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/steps/row/row_split.py` & `frictionless-5.8.3/frictionless/steps/row/row_split.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/steps/row/row_subset.py` & `frictionless-5.8.3/frictionless/steps/row/row_subset.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/steps/row/row_ungroup.py` & `frictionless-5.8.3/frictionless/steps/row/row_ungroup.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/steps/table/__init__.py` & `frictionless-5.8.3/frictionless/steps/table/__init__.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/steps/table/table_aggregate.py` & `frictionless-5.8.3/frictionless/steps/table/table_aggregate.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/steps/table/table_attach.py` & `frictionless-5.8.3/frictionless/steps/table/table_attach.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/steps/table/table_debug.py` & `frictionless-5.8.3/frictionless/steps/table/table_debug.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/steps/table/table_diff.py` & `frictionless-5.8.3/frictionless/steps/table/table_diff.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/steps/table/table_intersect.py` & `frictionless-5.8.3/frictionless/steps/table/table_intersect.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/steps/table/table_join.py` & `frictionless-5.8.3/frictionless/steps/table/table_join.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/steps/table/table_melt.py` & `frictionless-5.8.3/frictionless/steps/table/table_melt.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/steps/table/table_merge.py` & `frictionless-5.8.3/frictionless/steps/table/table_merge.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/steps/table/table_normalize.py` & `frictionless-5.8.3/frictionless/steps/table/table_normalize.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/steps/table/table_pivot.py` & `frictionless-5.8.3/frictionless/steps/table/table_pivot.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/steps/table/table_recast.py` & `frictionless-5.8.3/frictionless/steps/table/table_recast.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/steps/table/table_transpose.py` & `frictionless-5.8.3/frictionless/steps/table/table_transpose.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/steps/table/table_validate.py` & `frictionless-5.8.3/frictionless/steps/table/table_validate.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/steps/table/table_write.py` & `frictionless-5.8.3/frictionless/steps/table/table_write.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/system/adapter.py` & `frictionless-5.8.3/frictionless/system/adapter.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/system/loader.py` & `frictionless-5.8.3/frictionless/system/loader.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/system/parser.py` & `frictionless-5.8.3/frictionless/system/parser.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/system/plugin.py` & `frictionless-5.8.3/frictionless/system/plugin.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/system/system.py` & `frictionless-5.8.3/frictionless/system/system.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/table/header.py` & `frictionless-5.8.3/frictionless/table/header.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/table/row.py` & `frictionless-5.8.3/frictionless/table/row.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/vendor/wkt/grammar.txt` & `frictionless-5.8.3/frictionless/vendor/wkt/grammar.txt`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless/vendor/wkt/parser.py` & `frictionless-5.8.3/frictionless/vendor/wkt/parser.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless.egg-info/PKG-INFO` & `frictionless-5.8.3/frictionless.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: frictionless
-Version: 5.8.2
+Version: 5.8.3
 Summary: Data management framework for Python that provides functionality to describe, extract, validate, and transform tabular data
 Home-page: https://github.com/frictionlessdata/frictionless-py
 Author: Open Knowledge Foundation
 Author-email: info@okfn.org
 License: MIT
 Description: # Frictionless Framework
```

### Comparing `frictionless-5.8.2/frictionless.egg-info/SOURCES.txt` & `frictionless-5.8.3/frictionless.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/frictionless.egg-info/requires.txt` & `frictionless-5.8.3/frictionless.egg-info/requires.txt`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/setup.py` & `frictionless-5.8.3/setup.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/actions/test_describe.py` & `frictionless-5.8.3/tests/actions/test_describe.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/actions/test_extract.py` & `frictionless-5.8.3/tests/actions/test_extract.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/actions/test_transform.py` & `frictionless-5.8.3/tests/actions/test_transform.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/actions/test_validate.py` & `frictionless-5.8.3/tests/actions/test_validate.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/catalog/test_dereference.py` & `frictionless-5.8.3/tests/catalog/test_dereference.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/catalog/test_infer.py` & `frictionless-5.8.3/tests/catalog/test_infer.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/checklist/test_convert.py` & `frictionless-5.8.3/tests/checklist/test_convert.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/checklist/test_general.py` & `frictionless-5.8.3/tests/checklist/test_general.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/detector/test_general.py` & `frictionless-5.8.3/tests/detector/test_general.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/dialect/test_convert.py` & `frictionless-5.8.3/tests/dialect/test_convert.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/dialect/test_general.py` & `frictionless-5.8.3/tests/dialect/test_general.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/formats/csv/test_parser.py` & `frictionless-5.8.3/tests/formats/csv/test_parser.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/formats/erd/test_mapper.py` & `frictionless-5.8.3/tests/formats/erd/test_mapper.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/formats/excel/test_adapter.py` & `frictionless-5.8.3/tests/formats/excel/test_adapter.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/formats/excel/test_mapper.py` & `frictionless-5.8.3/tests/formats/excel/test_mapper.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/formats/gsheets/test_parser.py` & `frictionless-5.8.3/tests/formats/gsheets/test_parser.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/formats/html/test_parser.py` & `frictionless-5.8.3/tests/formats/html/test_parser.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/formats/inline/test_parser.py` & `frictionless-5.8.3/tests/formats/inline/test_parser.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/formats/json/parsers/test_json.py` & `frictionless-5.8.3/tests/formats/json/parsers/test_json.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/formats/json/parsers/test_jsonl.py` & `frictionless-5.8.3/tests/formats/json/parsers/test_jsonl.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/formats/jsonschema/test_mapper.py` & `frictionless-5.8.3/tests/formats/jsonschema/test_mapper.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/formats/markdown/test_mapper.py` & `frictionless-5.8.3/tests/formats/markdown/test_mapper.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/formats/ods/test_adapter.py` & `frictionless-5.8.3/tests/formats/ods/test_adapter.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/formats/ods/test_parser.py` & `frictionless-5.8.3/tests/formats/ods/test_parser.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/formats/pandas/test_parser.py` & `frictionless-5.8.3/tests/formats/pandas/test_parser.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/formats/parquet/test_parser.py` & `frictionless-5.8.3/tests/formats/parquet/test_parser.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/formats/spss/test_parser.py` & `frictionless-5.8.3/tests/formats/spss/test_parser.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/formats/sql/conftest.py` & `frictionless-5.8.3/tests/formats/sql/conftest.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/formats/sql/databases/mysql/test_adapter.py` & `frictionless-5.8.3/tests/formats/sql/databases/mysql/test_adapter.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/formats/sql/databases/mysql/test_parser.py` & `frictionless-5.8.3/tests/formats/sql/databases/mysql/test_parser.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/formats/sql/databases/postgres/test_adapter.py` & `frictionless-5.8.3/tests/formats/sql/databases/postgres/test_adapter.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/formats/sql/databases/postgres/test_parser.py` & `frictionless-5.8.3/tests/formats/sql/databases/postgres/test_parser.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/formats/sql/test_adapter.py` & `frictionless-5.8.3/tests/formats/sql/test_adapter.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/formats/sql/test_mapper.py` & `frictionless-5.8.3/tests/formats/sql/test_mapper.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/formats/sql/test_parser.py` & `frictionless-5.8.3/tests/formats/sql/test_parser.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/formats/yaml/test_parser.py` & `frictionless-5.8.3/tests/formats/yaml/test_parser.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/formats/zip/test_adapter.py` & `frictionless-5.8.3/tests/formats/zip/test_adapter.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/inquiry/task/test_convert.py` & `frictionless-5.8.3/tests/inquiry/task/test_convert.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/inquiry/test_convert.py` & `frictionless-5.8.3/tests/inquiry/test_convert.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/inquiry/test_general.py` & `frictionless-5.8.3/tests/inquiry/test_general.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/inquiry/test_validate.py` & `frictionless-5.8.3/tests/inquiry/test_validate.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/package/test_analyze.py` & `frictionless-5.8.3/tests/package/test_analyze.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/package/test_compression.py` & `frictionless-5.8.3/tests/package/test_compression.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/package/test_convert.py` & `frictionless-5.8.3/tests/package/test_convert.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/package/test_describe.py` & `frictionless-5.8.3/tests/package/test_describe.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/package/test_extract.py` & `frictionless-5.8.3/tests/package/test_extract.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/package/test_general.py` & `frictionless-5.8.3/tests/package/test_general.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/package/test_infer.py` & `frictionless-5.8.3/tests/package/test_infer.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/package/test_onerror.py` & `frictionless-5.8.3/tests/package/test_onerror.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/package/test_profile.py` & `frictionless-5.8.3/tests/package/test_profile.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/package/test_resources.py` & `frictionless-5.8.3/tests/package/test_resources.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/package/test_schema.py` & `frictionless-5.8.3/tests/package/test_schema.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/package/test_security.py` & `frictionless-5.8.3/tests/package/test_security.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/package/test_transform.py` & `frictionless-5.8.3/tests/package/test_transform.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/package/validate/test_general.py` & `frictionless-5.8.3/tests/package/validate/test_general.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/package/validate/test_parallel.py` & `frictionless-5.8.3/tests/package/validate/test_parallel.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/package/validate/test_schema.py` & `frictionless-5.8.3/tests/package/validate/test_schema.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/package/validate/test_stats.py` & `frictionless-5.8.3/tests/package/validate/test_stats.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/pipeline/test_convert.py` & `frictionless-5.8.3/tests/pipeline/test_convert.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/pipeline/test_general.py` & `frictionless-5.8.3/tests/pipeline/test_general.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/portals/ckan/conftest.py` & `frictionless-5.8.3/tests/portals/ckan/conftest.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/portals/ckan/test_adapter.py` & `frictionless-5.8.3/tests/portals/ckan/test_adapter.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/portals/github/conftest.py` & `frictionless-5.8.3/tests/portals/github/conftest.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/portals/github/test_adapter.py` & `frictionless-5.8.3/tests/portals/github/test_adapter.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/portals/zenodo/conftest.py` & `frictionless-5.8.3/tests/portals/zenodo/conftest.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/portals/zenodo/test_adapter.py` & `frictionless-5.8.3/tests/portals/zenodo/test_adapter.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/project/test_bytes.py` & `frictionless-5.8.3/tests/project/test_bytes.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/project/test_data.py` & `frictionless-5.8.3/tests/project/test_data.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/project/test_file.py` & `frictionless-5.8.3/tests/project/test_file.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/project/test_folder.py` & `frictionless-5.8.3/tests/project/test_folder.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/project/test_text.py` & `frictionless-5.8.3/tests/project/test_text.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/report/task/test_convert.py` & `frictionless-5.8.3/tests/report/task/test_convert.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/report/task/test_general.py` & `frictionless-5.8.3/tests/report/task/test_general.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/report/test_convert.py` & `frictionless-5.8.3/tests/report/test_convert.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/report/test_general.py` & `frictionless-5.8.3/tests/report/test_general.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/resource/test_analyze.py` & `frictionless-5.8.3/tests/resource/test_analyze.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/resource/test_compression.py` & `frictionless-5.8.3/tests/resource/test_compression.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/resource/test_convert.py` & `frictionless-5.8.3/tests/resource/test_convert.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/resource/test_dereference.py` & `frictionless-5.8.3/tests/resource/test_dereference.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/resource/test_describe.py` & `frictionless-5.8.3/tests/resource/test_describe.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/resource/test_detector.py` & `frictionless-5.8.3/tests/resource/test_detector.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/resource/test_dialect.py` & `frictionless-5.8.3/tests/resource/test_dialect.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/resource/test_encoding.py` & `frictionless-5.8.3/tests/resource/test_encoding.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/resource/test_extract.py` & `frictionless-5.8.3/tests/resource/test_extract.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/resource/test_format.py` & `frictionless-5.8.3/tests/resource/test_format.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/resource/test_general.py` & `frictionless-5.8.3/tests/resource/test_general.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/resource/test_index.py` & `frictionless-5.8.3/tests/resource/test_index.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/resource/test_infer.py` & `frictionless-5.8.3/tests/resource/test_infer.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/resource/test_innerpath.py` & `frictionless-5.8.3/tests/resource/test_innerpath.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/resource/test_onerror.py` & `frictionless-5.8.3/tests/resource/test_onerror.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/resource/test_open.py` & `frictionless-5.8.3/tests/resource/test_open.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/resource/test_profile.py` & `frictionless-5.8.3/tests/resource/test_profile.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/resource/test_read.py` & `frictionless-5.8.3/tests/resource/test_read.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/resource/test_schema.py` & `frictionless-5.8.3/tests/resource/test_schema.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/resource/test_scheme.py` & `frictionless-5.8.3/tests/resource/test_scheme.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/resource/test_security.py` & `frictionless-5.8.3/tests/resource/test_security.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/resource/test_stats.py` & `frictionless-5.8.3/tests/resource/test_stats.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/resource/test_write.py` & `frictionless-5.8.3/tests/resource/test_write.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/resource/transform/test_general.py` & `frictionless-5.8.3/tests/resource/transform/test_general.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/resource/transform/test_pipeline.py` & `frictionless-5.8.3/tests/resource/transform/test_pipeline.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/resource/validate/test_compression.py` & `frictionless-5.8.3/tests/resource/validate/test_compression.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/resource/validate/test_detector.py` & `frictionless-5.8.3/tests/resource/validate/test_detector.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/resource/validate/test_dialect.py` & `frictionless-5.8.3/tests/resource/validate/test_dialect.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/resource/validate/test_encoding.py` & `frictionless-5.8.3/tests/resource/validate/test_encoding.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/resource/validate/test_general.py` & `frictionless-5.8.3/tests/resource/validate/test_general.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/resource/validate/test_schema.py` & `frictionless-5.8.3/tests/resource/validate/test_schema.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/resource/validate/test_stats.py` & `frictionless-5.8.3/tests/resource/validate/test_stats.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/schema/field/test_constraints.py` & `frictionless-5.8.3/tests/schema/field/test_constraints.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/schema/field/test_convert.py` & `frictionless-5.8.3/tests/schema/field/test_convert.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/schema/field/test_custom.py` & `frictionless-5.8.3/tests/schema/field/test_custom.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/schema/field/test_general.py` & `frictionless-5.8.3/tests/schema/field/test_general.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/schema/field/test_read.py` & `frictionless-5.8.3/tests/schema/field/test_read.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/schema/test_convert.py` & `frictionless-5.8.3/tests/schema/test_convert.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/schema/test_general.py` & `frictionless-5.8.3/tests/schema/test_general.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/schema/test_validate.py` & `frictionless-5.8.3/tests/schema/test_validate.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/schemes/aws/loaders/test_s3.py` & `frictionless-5.8.3/tests/schemes/aws/loaders/test_s3.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/schemes/buffer/test_loader.py` & `frictionless-5.8.3/tests/schemes/buffer/test_loader.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/schemes/local/test_loader.py` & `frictionless-5.8.3/tests/schemes/local/test_loader.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/schemes/multipart/test_loader.py` & `frictionless-5.8.3/tests/schemes/multipart/test_loader.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/schemes/remote/test_loader.py` & `frictionless-5.8.3/tests/schemes/remote/test_loader.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/schemes/stream/test_loader.py` & `frictionless-5.8.3/tests/schemes/stream/test_loader.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/server/project/test_create_file.py` & `frictionless-5.8.3/tests/server/project/test_create_file.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/server/project/test_delete_file.py` & `frictionless-5.8.3/tests/server/project/test_delete_file.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/server/project/test_list_files.py` & `frictionless-5.8.3/tests/server/project/test_list_files.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/server/project/test_move_file.py` & `frictionless-5.8.3/tests/server/project/test_move_file.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/system/test_system.py` & `frictionless-5.8.3/tests/system/test_system.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/table/test_header.py` & `frictionless-5.8.3/tests/table/test_header.py`

 * *Files identical despite different names*

### Comparing `frictionless-5.8.2/tests/table/test_row.py` & `frictionless-5.8.3/tests/table/test_row.py`

 * *Files identical despite different names*

