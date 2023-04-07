# Comparing `tmp/ooresults-0.2.1.tar.gz` & `tmp/ooresults-0.2.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "ooresults-0.2.1.tar", last modified: Thu Mar 23 18:08:04 2023, max compression
+gzip compressed data, was "ooresults-0.2.2.tar", last modified: Fri Apr  7 09:55:30 2023, max compression
```

## Comparing `ooresults-0.2.1.tar` & `ooresults-0.2.2.tar`

### file list

```diff
@@ -1,157 +1,159 @@
-drwxr-xr-x   0 rainer    (1000) users      (100)        0 2023-03-23 18:08:04.730076 ooresults-0.2.1/
--rw-r--r--   0 rainer    (1000) users      (100)    34523 2023-03-01 18:09:04.000000 ooresults-0.2.1/LICENSE
--rw-r--r--   0 rainer    (1000) users      (100)      260 2023-03-01 18:09:04.000000 ooresults-0.2.1/MANIFEST.in
--rw-r--r--   0 rainer    (1000) users      (100)    42907 2023-03-23 18:08:04.730076 ooresults-0.2.1/PKG-INFO
--rw-r--r--   0 rainer    (1000) users      (100)     2278 2023-03-01 18:09:04.000000 ooresults-0.2.1/README.rst
-drwxr-xr-x   0 rainer    (1000) users      (100)        0 2023-03-23 18:08:04.702077 ooresults-0.2.1/ooresults/
--rw-r--r--   0 rainer    (1000) users      (100)      803 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/__init__.py
--rw-r--r--   0 rainer    (1000) users      (100)    15992 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/_reader.py
--rw-r--r--   0 rainer    (1000) users      (100)    11645 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/_server.py
--rw-r--r--   0 rainer    (1000) users      (100)     4363 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/configuration.py
-drwxr-xr-x   0 rainer    (1000) users      (100)        0 2023-03-23 18:08:04.706077 ooresults-0.2.1/ooresults/handler/
--rw-r--r--   0 rainer    (1000) users      (100)      803 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/handler/__init__.py
--rw-r--r--   0 rainer    (1000) users      (100)     7830 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/handler/classes.py
--rw-r--r--   0 rainer    (1000) users      (100)     2554 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/handler/clubs.py
--rw-r--r--   0 rainer    (1000) users      (100)     4559 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/handler/competitors.py
--rw-r--r--   0 rainer    (1000) users      (100)     5797 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/handler/courses.py
--rw-r--r--   0 rainer    (1000) users      (100)     1066 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/handler/demo_reader.py
--rw-r--r--   0 rainer    (1000) users      (100)    12131 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/handler/entries.py
--rw-r--r--   0 rainer    (1000) users      (100)     3308 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/handler/events.py
--rw-r--r--   0 rainer    (1000) users      (100)     4504 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/handler/handicap.py
--rw-r--r--   0 rainer    (1000) users      (100)    30157 2023-03-23 18:03:14.000000 ooresults-0.2.1/ooresults/handler/model.py
--rw-r--r--   0 rainer    (1000) users      (100)     8221 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/handler/results.py
--rw-r--r--   0 rainer    (1000) users      (100)     9830 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/handler/series.py
-drwxr-xr-x   0 rainer    (1000) users      (100)        0 2023-03-23 18:08:04.706077 ooresults-0.2.1/ooresults/pdf/
-drwxr-xr-x   0 rainer    (1000) users      (100)        0 2023-03-23 18:08:04.710077 ooresults-0.2.1/ooresults/pdf/fonts/
--rw-r--r--   0 rainer    (1000) users      (100)   690516 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/pdf/fonts/Carlito-Bold.ttf
--rw-r--r--   0 rainer    (1000) users      (100)   816716 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/pdf/fonts/Carlito-BoldItalic.ttf
--rw-r--r--   0 rainer    (1000) users      (100)   623416 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/pdf/fonts/Carlito-Italic.ttf
--rw-r--r--   0 rainer    (1000) users      (100)   635996 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/pdf/fonts/Carlito-Regular.ttf
--rw-r--r--   0 rainer    (1000) users      (100)     2806 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/pdf/pdf.py
--rw-r--r--   0 rainer    (1000) users      (100)    11198 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/pdf/result.py
--rw-r--r--   0 rainer    (1000) users      (100)     5283 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/pdf/series.py
--rw-r--r--   0 rainer    (1000) users      (100)     9989 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/pdf/splittimes.py
-drwxr-xr-x   0 rainer    (1000) users      (100)        0 2023-03-23 18:08:04.710077 ooresults-0.2.1/ooresults/plugins/
--rw-r--r--   0 rainer    (1000) users      (100)      803 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/plugins/__init__.py
-drwxr-xr-x   0 rainer    (1000) users      (100)        0 2023-03-23 18:08:04.698077 ooresults-0.2.1/ooresults/plugins/imports/
-drwxr-xr-x   0 rainer    (1000) users      (100)        0 2023-03-23 18:08:04.710077 ooresults-0.2.1/ooresults/plugins/imports/entries/
--rw-r--r--   0 rainer    (1000) users      (100)      803 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/plugins/imports/entries/__init__.py
--rw-r--r--   0 rainer    (1000) users      (100)     2948 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/plugins/imports/entries/text.py
--rw-r--r--   0 rainer    (1000) users      (100)     2732 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/plugins/iof_class_list.py
--rw-r--r--   0 rainer    (1000) users      (100)     3987 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/plugins/iof_competitor_list.py
--rw-r--r--   0 rainer    (1000) users      (100)     5840 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/plugins/iof_course_data.py
--rw-r--r--   0 rainer    (1000) users      (100)     5103 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/plugins/iof_entry_list.py
--rw-r--r--   0 rainer    (1000) users      (100)     9993 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/plugins/iof_result_list.py
--rw-r--r--   0 rainer    (1000) users      (100)    13201 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/plugins/oe2003.py
--rw-r--r--   0 rainer    (1000) users      (100)      905 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/reader.py
-drwxr-xr-x   0 rainer    (1000) users      (100)        0 2023-03-23 18:08:04.714077 ooresults-0.2.1/ooresults/repo/
--rw-r--r--   0 rainer    (1000) users      (100)      803 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/repo/__init__.py
--rw-r--r--   0 rainer    (1000) users      (100)     2237 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/repo/class_params.py
--rw-r--r--   0 rainer    (1000) users      (100)     7358 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/repo/repo.py
--rw-r--r--   0 rainer    (1000) users      (100)    16171 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/repo/result_type.py
--rw-r--r--   0 rainer    (1000) users      (100)     1339 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/repo/series_type.py
--rw-r--r--   0 rainer    (1000) users      (100)    36349 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/repo/sqlite_repo.py
--rw-r--r--   0 rainer    (1000) users      (100)     1265 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/repo/start_type.py
-drwxr-xr-x   0 rainer    (1000) users      (100)        0 2023-03-23 18:08:04.714077 ooresults-0.2.1/ooresults/repo/update/
--rw-r--r--   0 rainer    (1000) users      (100)      803 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/repo/update/__init__.py
--rw-r--r--   0 rainer    (1000) users      (100)     4728 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/repo/update/update_008.py
--rw-r--r--   0 rainer    (1000) users      (100)     1890 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/repo/update/update_tables.py
-drwxr-xr-x   0 rainer    (1000) users      (100)        0 2023-03-23 18:08:04.714077 ooresults-0.2.1/ooresults/schema/
--rw-r--r--   0 rainer    (1000) users      (100)   177863 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/schema/IOF.xsd
--rwxr-xr-x   0 rainer    (1000) users      (100)     2117 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/schema/cardreader_log.json
--rw-r--r--   0 rainer    (1000) users      (100)      905 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/server.py
--rw-r--r--   0 rainer    (1000) users      (100)     2257 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/set_legacy_mode.py
-drwxr-xr-x   0 rainer    (1000) users      (100)        0 2023-03-23 18:08:04.714077 ooresults-0.2.1/ooresults/static/
--rw-r--r--   0 rainer    (1000) users      (100)      643 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/static/style-tab.css
--rw-r--r--   0 rainer    (1000) users      (100)     1267 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/static/style.css
--rw-r--r--   0 rainer    (1000) users      (100)    12106 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/static/w3.js
-drwxr-xr-x   0 rainer    (1000) users      (100)        0 2023-03-23 18:08:04.722077 ooresults-0.2.1/ooresults/templates/
--rw-r--r--   0 rainer    (1000) users      (100)     5982 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/templates/add_class.html
--rw-r--r--   0 rainer    (1000) users      (100)      883 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/templates/add_club.html
--rw-r--r--   0 rainer    (1000) users      (100)     3093 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/templates/add_competitor.html
--rw-r--r--   0 rainer    (1000) users      (100)     1758 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/templates/add_course.html
--rw-r--r--   0 rainer    (1000) users      (100)     6139 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/templates/add_entry.html
--rw-r--r--   0 rainer    (1000) users      (100)     1811 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/templates/add_entry_competitors.html
--rw-r--r--   0 rainer    (1000) users      (100)     7329 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/templates/add_entry_result.html
--rw-r--r--   0 rainer    (1000) users      (100)     2511 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/templates/add_event.html
--rw-r--r--   0 rainer    (1000) users      (100)      466 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/templates/base.html
--rw-r--r--   0 rainer    (1000) users      (100)    12647 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/templates/classes_tab_content.html
--rw-r--r--   0 rainer    (1000) users      (100)     2975 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/templates/classes_table.html
--rw-r--r--   0 rainer    (1000) users      (100)     7563 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/templates/clubs_tab_content.html
--rw-r--r--   0 rainer    (1000) users      (100)      453 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/templates/clubs_table.html
--rwxr-xr-x   0 rainer    (1000) users      (100)    12385 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/templates/competitors_tab_content.html
--rw-r--r--   0 rainer    (1000) users      (100)     1030 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/templates/competitors_table.html
--rw-r--r--   0 rainer    (1000) users      (100)    12662 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/templates/courses_tab_content.html
--rw-r--r--   0 rainer    (1000) users      (100)     1386 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/templates/courses_table.html
--rw-r--r--   0 rainer    (1000) users      (100)     6529 2023-03-23 18:03:14.000000 ooresults-0.2.1/ooresults/templates/demo_reader.html
--rwxr-xr-x   0 rainer    (1000) users      (100)    19512 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/templates/entries_tab_content.html
--rw-r--r--   0 rainer    (1000) users      (100)     3024 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/templates/entries_table.html
--rw-r--r--   0 rainer    (1000) users      (100)    10152 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/templates/events_tab_content.html
--rw-r--r--   0 rainer    (1000) users      (100)     1339 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/templates/events_table.html
--rw-r--r--   0 rainer    (1000) users      (100)     5937 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/templates/main.html
--rw-r--r--   0 rainer    (1000) users      (100)     6631 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/templates/results_tab_content.html
--rw-r--r--   0 rainer    (1000) users      (100)     5434 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/templates/results_table.html
--rw-r--r--   0 rainer    (1000) users      (100)      528 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/templates/root.html
--rw-r--r--   0 rainer    (1000) users      (100)     1084 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/templates/select_event.html
--rw-r--r--   0 rainer    (1000) users      (100)     2500 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/templates/series_settings.html
--rw-r--r--   0 rainer    (1000) users      (100)     9074 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/templates/series_tab_content.html
--rw-r--r--   0 rainer    (1000) users      (100)     1541 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/templates/series_table.html
-drwxr-xr-x   0 rainer    (1000) users      (100)        0 2023-03-23 18:08:04.722077 ooresults-0.2.1/ooresults/templates/si/
--rw-r--r--   0 rainer    (1000) users      (100)      914 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/templates/si/si1_data.html
--rw-r--r--   0 rainer    (1000) users      (100)      396 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/templates/si/si1_error.html
--rw-r--r--   0 rainer    (1000) users      (100)     6992 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/templates/si/si1_page.html
--rw-r--r--   0 rainer    (1000) users      (100)     4178 2023-03-23 18:03:14.000000 ooresults-0.2.1/ooresults/templates/si/si2_data.html
--rw-r--r--   0 rainer    (1000) users      (100)     3589 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/templates/si/si2_page.html
--rw-r--r--   0 rainer    (1000) users      (100)      383 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/templates/unauthorized.html
--rw-r--r--   0 rainer    (1000) users      (100)     2407 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/user.py
-drwxr-xr-x   0 rainer    (1000) users      (100)        0 2023-03-23 18:08:04.722077 ooresults-0.2.1/ooresults/utils/
--rw-r--r--   0 rainer    (1000) users      (100)      803 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/utils/__init__.py
--rw-r--r--   0 rainer    (1000) users      (100)     1318 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/utils/globals.py
-drwxr-xr-x   0 rainer    (1000) users      (100)        0 2023-03-23 18:08:04.722077 ooresults-0.2.1/ooresults/websocket_server/
--rw-r--r--   0 rainer    (1000) users      (100)      803 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/websocket_server/__init__.py
--rw-r--r--   0 rainer    (1000) users      (100)     1749 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/websocket_server/si.py
--rw-r--r--   0 rainer    (1000) users      (100)    14523 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/websocket_server/websocket_handler.py
--rw-r--r--   0 rainer    (1000) users      (100)     2143 2023-03-01 18:09:04.000000 ooresults-0.2.1/ooresults/websocket_server/websocket_server.py
-drwxr-xr-x   0 rainer    (1000) users      (100)        0 2023-03-23 18:08:04.702077 ooresults-0.2.1/ooresults.egg-info/
--rw-r--r--   0 rainer    (1000) users      (100)    42907 2023-03-23 18:08:04.000000 ooresults-0.2.1/ooresults.egg-info/PKG-INFO
--rw-r--r--   0 rainer    (1000) users      (100)     4400 2023-03-23 18:08:04.000000 ooresults-0.2.1/ooresults.egg-info/SOURCES.txt
--rw-r--r--   0 rainer    (1000) users      (100)        1 2023-03-23 18:08:04.000000 ooresults-0.2.1/ooresults.egg-info/dependency_links.txt
--rw-r--r--   0 rainer    (1000) users      (100)      102 2023-03-23 18:08:04.000000 ooresults-0.2.1/ooresults.egg-info/entry_points.txt
--rw-r--r--   0 rainer    (1000) users      (100)      152 2023-03-23 18:08:04.000000 ooresults-0.2.1/ooresults.egg-info/requires.txt
--rw-r--r--   0 rainer    (1000) users      (100)       10 2023-03-23 18:08:04.000000 ooresults-0.2.1/ooresults.egg-info/top_level.txt
--rwxr-xr-x   0 rainer    (1000) users      (100)      977 2023-03-23 18:03:14.000000 ooresults-0.2.1/pyproject.toml
--rwxr-xr-x   0 rainer    (1000) users      (100)      616 2023-03-23 18:08:04.730076 ooresults-0.2.1/setup.cfg
-drwxr-xr-x   0 rainer    (1000) users      (100)        0 2023-03-23 18:08:04.726076 ooresults-0.2.1/tests/
--rw-r--r--   0 rainer    (1000) users      (100)      803 2023-03-01 18:09:04.000000 ooresults-0.2.1/tests/__init__.py
--rw-r--r--   0 rainer    (1000) users      (100)     1414 2023-03-01 18:09:04.000000 ooresults-0.2.1/tests/competitor.py
--rw-r--r--   0 rainer    (1000) users      (100)     2061 2023-03-01 18:09:04.000000 ooresults-0.2.1/tests/entry.py
-drwxr-xr-x   0 rainer    (1000) users      (100)        0 2023-03-23 18:08:04.726076 ooresults-0.2.1/tests/model/
--rw-r--r--   0 rainer    (1000) users      (100)      803 2023-03-01 18:09:04.000000 ooresults-0.2.1/tests/model/__init__.py
--rw-r--r--   0 rainer    (1000) users      (100)    10750 2023-03-01 18:09:04.000000 ooresults-0.2.1/tests/model/test_courses.py
--rw-r--r--   0 rainer    (1000) users      (100)    16528 2023-03-01 18:09:04.000000 ooresults-0.2.1/tests/model/test_parse_cardreader_log.py
--rw-r--r--   0 rainer    (1000) users      (100)    27576 2023-03-23 18:03:14.000000 ooresults-0.2.1/tests/model/test_store_cardreader_result.py
-drwxr-xr-x   0 rainer    (1000) users      (100)        0 2023-03-23 18:08:04.726076 ooresults-0.2.1/tests/plugins/
--rw-r--r--   0 rainer    (1000) users      (100)    12933 2023-03-01 18:09:04.000000 ooresults-0.2.1/tests/plugins/test_export_competitors_oe2003.py
--rw-r--r--   0 rainer    (1000) users      (100)    27880 2023-03-01 18:09:04.000000 ooresults-0.2.1/tests/plugins/test_import_competitors_oe2003.py
--rw-r--r--   0 rainer    (1000) users      (100)     2709 2023-03-01 18:09:04.000000 ooresults-0.2.1/tests/plugins/test_plugin_iof_class_list.py
--rw-r--r--   0 rainer    (1000) users      (100)     3886 2023-03-01 18:09:04.000000 ooresults-0.2.1/tests/plugins/test_plugin_iof_competitor_list.py
--rw-r--r--   0 rainer    (1000) users      (100)    10115 2023-03-01 18:09:04.000000 ooresults-0.2.1/tests/plugins/test_plugin_iof_course_data.py
--rw-r--r--   0 rainer    (1000) users      (100)     8618 2023-03-01 18:09:04.000000 ooresults-0.2.1/tests/plugins/test_plugin_iof_entry_list.py
--rw-r--r--   0 rainer    (1000) users      (100)    27827 2023-03-01 18:09:04.000000 ooresults-0.2.1/tests/plugins/test_plugin_iof_result_list.py
-drwxr-xr-x   0 rainer    (1000) users      (100)        0 2023-03-23 18:08:04.726076 ooresults-0.2.1/tests/repo/
--rw-r--r--   0 rainer    (1000) users      (100)      803 2023-03-01 18:09:04.000000 ooresults-0.2.1/tests/repo/__init__.py
--rw-r--r--   0 rainer    (1000) users      (100)     9402 2023-03-01 18:09:04.000000 ooresults-0.2.1/tests/repo/test_classes.py
--rw-r--r--   0 rainer    (1000) users      (100)     5314 2023-03-01 18:09:04.000000 ooresults-0.2.1/tests/repo/test_clubs.py
--rw-r--r--   0 rainer    (1000) users      (100)    10687 2023-03-01 18:09:04.000000 ooresults-0.2.1/tests/repo/test_competitors.py
--rw-r--r--   0 rainer    (1000) users      (100)     7336 2023-03-01 18:09:04.000000 ooresults-0.2.1/tests/repo/test_courses.py
--rw-r--r--   0 rainer    (1000) users      (100)    39414 2023-03-01 18:09:04.000000 ooresults-0.2.1/tests/repo/test_entries.py
--rw-r--r--   0 rainer    (1000) users      (100)     7540 2023-03-01 18:09:04.000000 ooresults-0.2.1/tests/repo/test_events.py
--rw-r--r--   0 rainer    (1000) users      (100)     2353 2023-03-01 18:09:04.000000 ooresults-0.2.1/tests/repo/test_settings.py
--rw-r--r--   0 rainer    (1000) users      (100)     9467 2023-03-01 18:09:04.000000 ooresults-0.2.1/tests/test_compute_result_net.py
--rw-r--r--   0 rainer    (1000) users      (100)    15440 2023-03-01 18:09:04.000000 ooresults-0.2.1/tests/test_compute_result_score.py
--rw-r--r--   0 rainer    (1000) users      (100)    38250 2023-03-01 18:09:04.000000 ooresults-0.2.1/tests/test_compute_result_standard.py
--rw-r--r--   0 rainer    (1000) users      (100)     7257 2023-03-01 18:09:04.000000 ooresults-0.2.1/tests/test_configuration.py
--rw-r--r--   0 rainer    (1000) users      (100)     1758 2023-03-01 18:09:04.000000 ooresults-0.2.1/tests/test_handicap.py
--rw-r--r--   0 rainer    (1000) users      (100)    19384 2023-03-01 18:09:04.000000 ooresults-0.2.1/tests/test_ranking.py
--rw-r--r--   0 rainer    (1000) users      (100)    26017 2023-03-01 18:09:04.000000 ooresults-0.2.1/tests/test_series.py
--rw-r--r--   0 rainer    (1000) users      (100)     2326 2023-03-01 18:09:04.000000 ooresults-0.2.1/tests/test_user.py
+drwxr-xr-x   0 rainer    (1000) users      (100)        0 2023-04-07 09:55:30.567350 ooresults-0.2.2/
+-rw-r--r--   0 rainer    (1000) users      (100)    34523 2023-03-01 18:09:04.000000 ooresults-0.2.2/LICENSE
+-rw-r--r--   0 rainer    (1000) users      (100)      260 2023-03-01 18:09:04.000000 ooresults-0.2.2/MANIFEST.in
+-rw-r--r--   0 rainer    (1000) users      (100)    42907 2023-04-07 09:55:30.567350 ooresults-0.2.2/PKG-INFO
+-rw-r--r--   0 rainer    (1000) users      (100)     2278 2023-03-01 18:09:04.000000 ooresults-0.2.2/README.rst
+drwxr-xr-x   0 rainer    (1000) users      (100)        0 2023-04-07 09:55:30.535350 ooresults-0.2.2/ooresults/
+-rw-r--r--   0 rainer    (1000) users      (100)      803 2023-03-01 18:09:04.000000 ooresults-0.2.2/ooresults/__init__.py
+-rw-r--r--   0 rainer    (1000) users      (100)    15992 2023-03-01 18:09:04.000000 ooresults-0.2.2/ooresults/_reader.py
+-rw-r--r--   0 rainer    (1000) users      (100)    11645 2023-03-01 18:09:04.000000 ooresults-0.2.2/ooresults/_server.py
+-rw-r--r--   0 rainer    (1000) users      (100)     4363 2023-03-01 18:09:04.000000 ooresults-0.2.2/ooresults/configuration.py
+drwxr-xr-x   0 rainer    (1000) users      (100)        0 2023-04-07 09:55:30.539350 ooresults-0.2.2/ooresults/handler/
+-rw-r--r--   0 rainer    (1000) users      (100)      803 2023-03-01 18:09:04.000000 ooresults-0.2.2/ooresults/handler/__init__.py
+-rw-r--r--   0 rainer    (1000) users      (100)     7873 2023-04-03 19:51:02.000000 ooresults-0.2.2/ooresults/handler/classes.py
+-rw-r--r--   0 rainer    (1000) users      (100)     2597 2023-04-03 19:51:02.000000 ooresults-0.2.2/ooresults/handler/clubs.py
+-rw-r--r--   0 rainer    (1000) users      (100)     4559 2023-03-01 18:09:04.000000 ooresults-0.2.2/ooresults/handler/competitors.py
+-rw-r--r--   0 rainer    (1000) users      (100)     5824 2023-04-03 19:51:02.000000 ooresults-0.2.2/ooresults/handler/courses.py
+-rw-r--r--   0 rainer    (1000) users      (100)     1110 2023-04-03 19:51:02.000000 ooresults-0.2.2/ooresults/handler/demo_reader.py
+-rw-r--r--   0 rainer    (1000) users      (100)    12420 2023-03-31 20:12:46.000000 ooresults-0.2.2/ooresults/handler/entries.py
+-rw-r--r--   0 rainer    (1000) users      (100)     3351 2023-04-03 19:51:02.000000 ooresults-0.2.2/ooresults/handler/events.py
+-rw-r--r--   0 rainer    (1000) users      (100)     4504 2023-03-01 18:09:04.000000 ooresults-0.2.2/ooresults/handler/handicap.py
+-rw-r--r--   0 rainer    (1000) users      (100)    30157 2023-03-26 08:00:56.000000 ooresults-0.2.2/ooresults/handler/model.py
+-rw-r--r--   0 rainer    (1000) users      (100)     8221 2023-03-01 18:09:04.000000 ooresults-0.2.2/ooresults/handler/results.py
+-rw-r--r--   0 rainer    (1000) users      (100)     9873 2023-04-03 19:51:02.000000 ooresults-0.2.2/ooresults/handler/series.py
+drwxr-xr-x   0 rainer    (1000) users      (100)        0 2023-04-07 09:55:30.539350 ooresults-0.2.2/ooresults/pdf/
+drwxr-xr-x   0 rainer    (1000) users      (100)        0 2023-04-07 09:55:30.543350 ooresults-0.2.2/ooresults/pdf/fonts/
+-rw-r--r--   0 rainer    (1000) users      (100)   690516 2023-03-01 18:09:04.000000 ooresults-0.2.2/ooresults/pdf/fonts/Carlito-Bold.ttf
+-rw-r--r--   0 rainer    (1000) users      (100)   816716 2023-03-01 18:09:04.000000 ooresults-0.2.2/ooresults/pdf/fonts/Carlito-BoldItalic.ttf
+-rw-r--r--   0 rainer    (1000) users      (100)   623416 2023-03-01 18:09:04.000000 ooresults-0.2.2/ooresults/pdf/fonts/Carlito-Italic.ttf
+-rw-r--r--   0 rainer    (1000) users      (100)   635996 2023-03-01 18:09:04.000000 ooresults-0.2.2/ooresults/pdf/fonts/Carlito-Regular.ttf
+-rw-r--r--   0 rainer    (1000) users      (100)     2806 2023-03-01 18:09:04.000000 ooresults-0.2.2/ooresults/pdf/pdf.py
+-rw-r--r--   0 rainer    (1000) users      (100)    11206 2023-04-03 19:51:02.000000 ooresults-0.2.2/ooresults/pdf/result.py
+-rw-r--r--   0 rainer    (1000) users      (100)     5283 2023-03-01 18:09:04.000000 ooresults-0.2.2/ooresults/pdf/series.py
+-rw-r--r--   0 rainer    (1000) users      (100)    10007 2023-04-03 19:51:02.000000 ooresults-0.2.2/ooresults/pdf/splittimes.py
+drwxr-xr-x   0 rainer    (1000) users      (100)        0 2023-04-07 09:55:30.547350 ooresults-0.2.2/ooresults/plugins/
+-rw-r--r--   0 rainer    (1000) users      (100)      803 2023-03-01 18:09:04.000000 ooresults-0.2.2/ooresults/plugins/__init__.py
+drwxr-xr-x   0 rainer    (1000) users      (100)        0 2023-04-07 09:55:30.531350 ooresults-0.2.2/ooresults/plugins/imports/
+drwxr-xr-x   0 rainer    (1000) users      (100)        0 2023-04-07 09:55:30.547350 ooresults-0.2.2/ooresults/plugins/imports/entries/
+-rw-r--r--   0 rainer    (1000) users      (100)      803 2023-03-01 18:09:04.000000 ooresults-0.2.2/ooresults/plugins/imports/entries/__init__.py
+-rw-r--r--   0 rainer    (1000) users      (100)     2948 2023-03-01 18:09:04.000000 ooresults-0.2.2/ooresults/plugins/imports/entries/text.py
+-rw-r--r--   0 rainer    (1000) users      (100)     2813 2023-04-03 19:51:02.000000 ooresults-0.2.2/ooresults/plugins/iof_class_list.py
+-rw-r--r--   0 rainer    (1000) users      (100)     4068 2023-04-03 19:51:02.000000 ooresults-0.2.2/ooresults/plugins/iof_competitor_list.py
+-rw-r--r--   0 rainer    (1000) users      (100)     5935 2023-04-07 09:54:41.000000 ooresults-0.2.2/ooresults/plugins/iof_course_data.py
+-rw-r--r--   0 rainer    (1000) users      (100)     5184 2023-04-03 19:51:02.000000 ooresults-0.2.2/ooresults/plugins/iof_entry_list.py
+-rw-r--r--   0 rainer    (1000) users      (100)    10074 2023-04-03 19:51:02.000000 ooresults-0.2.2/ooresults/plugins/iof_result_list.py
+-rw-r--r--   0 rainer    (1000) users      (100)     7446 2023-03-31 20:12:46.000000 ooresults-0.2.2/ooresults/plugins/oe12.py
+-rw-r--r--   0 rainer    (1000) users      (100)    14580 2023-03-31 20:12:46.000000 ooresults-0.2.2/ooresults/plugins/oe2003.py
+-rw-r--r--   0 rainer    (1000) users      (100)      905 2023-03-01 18:09:04.000000 ooresults-0.2.2/ooresults/reader.py
+drwxr-xr-x   0 rainer    (1000) users      (100)        0 2023-04-07 09:55:30.547350 ooresults-0.2.2/ooresults/repo/
+-rw-r--r--   0 rainer    (1000) users      (100)      803 2023-03-01 18:09:04.000000 ooresults-0.2.2/ooresults/repo/__init__.py
+-rw-r--r--   0 rainer    (1000) users      (100)     2237 2023-03-01 18:09:04.000000 ooresults-0.2.2/ooresults/repo/class_params.py
+-rw-r--r--   0 rainer    (1000) users      (100)     7358 2023-03-01 18:09:04.000000 ooresults-0.2.2/ooresults/repo/repo.py
+-rw-r--r--   0 rainer    (1000) users      (100)    16171 2023-03-01 18:09:04.000000 ooresults-0.2.2/ooresults/repo/result_type.py
+-rw-r--r--   0 rainer    (1000) users      (100)     1339 2023-03-01 18:09:04.000000 ooresults-0.2.2/ooresults/repo/series_type.py
+-rw-r--r--   0 rainer    (1000) users      (100)    36349 2023-03-01 18:09:04.000000 ooresults-0.2.2/ooresults/repo/sqlite_repo.py
+-rw-r--r--   0 rainer    (1000) users      (100)     1265 2023-03-01 18:09:04.000000 ooresults-0.2.2/ooresults/repo/start_type.py
+drwxr-xr-x   0 rainer    (1000) users      (100)        0 2023-04-07 09:55:30.547350 ooresults-0.2.2/ooresults/repo/update/
+-rw-r--r--   0 rainer    (1000) users      (100)      803 2023-03-01 18:09:04.000000 ooresults-0.2.2/ooresults/repo/update/__init__.py
+-rw-r--r--   0 rainer    (1000) users      (100)     4728 2023-03-01 18:09:04.000000 ooresults-0.2.2/ooresults/repo/update/update_008.py
+-rw-r--r--   0 rainer    (1000) users      (100)     1890 2023-03-01 18:09:04.000000 ooresults-0.2.2/ooresults/repo/update/update_tables.py
+drwxr-xr-x   0 rainer    (1000) users      (100)        0 2023-04-07 09:55:30.547350 ooresults-0.2.2/ooresults/schema/
+-rw-r--r--   0 rainer    (1000) users      (100)   177863 2023-03-01 18:09:04.000000 ooresults-0.2.2/ooresults/schema/IOF.xsd
+-rwxr-xr-x   0 rainer    (1000) users      (100)     2117 2023-03-01 18:09:04.000000 ooresults-0.2.2/ooresults/schema/cardreader_log.json
+-rw-r--r--   0 rainer    (1000) users      (100)      905 2023-03-01 18:09:04.000000 ooresults-0.2.2/ooresults/server.py
+-rw-r--r--   0 rainer    (1000) users      (100)     2257 2023-03-01 18:09:04.000000 ooresults-0.2.2/ooresults/set_legacy_mode.py
+drwxr-xr-x   0 rainer    (1000) users      (100)        0 2023-04-07 09:55:30.551350 ooresults-0.2.2/ooresults/static/
+-rw-r--r--   0 rainer    (1000) users      (100)      643 2023-03-01 18:09:04.000000 ooresults-0.2.2/ooresults/static/style-tab.css
+-rw-r--r--   0 rainer    (1000) users      (100)     1267 2023-03-01 18:09:04.000000 ooresults-0.2.2/ooresults/static/style.css
+-rw-r--r--   0 rainer    (1000) users      (100)    12106 2023-03-01 18:09:04.000000 ooresults-0.2.2/ooresults/static/w3.js
+drwxr-xr-x   0 rainer    (1000) users      (100)        0 2023-04-07 09:55:30.555350 ooresults-0.2.2/ooresults/templates/
+-rw-r--r--   0 rainer    (1000) users      (100)     5964 2023-04-03 19:51:02.000000 ooresults-0.2.2/ooresults/templates/add_class.html
+-rw-r--r--   0 rainer    (1000) users      (100)      883 2023-03-01 18:09:04.000000 ooresults-0.2.2/ooresults/templates/add_club.html
+-rw-r--r--   0 rainer    (1000) users      (100)     3093 2023-03-01 18:09:04.000000 ooresults-0.2.2/ooresults/templates/add_competitor.html
+-rw-r--r--   0 rainer    (1000) users      (100)     1758 2023-03-01 18:09:04.000000 ooresults-0.2.2/ooresults/templates/add_course.html
+-rw-r--r--   0 rainer    (1000) users      (100)     6139 2023-03-01 18:09:04.000000 ooresults-0.2.2/ooresults/templates/add_entry.html
+-rw-r--r--   0 rainer    (1000) users      (100)     1811 2023-03-01 18:09:04.000000 ooresults-0.2.2/ooresults/templates/add_entry_competitors.html
+-rw-r--r--   0 rainer    (1000) users      (100)     7204 2023-04-03 19:51:02.000000 ooresults-0.2.2/ooresults/templates/add_entry_result.html
+-rw-r--r--   0 rainer    (1000) users      (100)     2511 2023-03-01 18:09:04.000000 ooresults-0.2.2/ooresults/templates/add_event.html
+-rw-r--r--   0 rainer    (1000) users      (100)      466 2023-03-01 18:09:04.000000 ooresults-0.2.2/ooresults/templates/base.html
+-rw-r--r--   0 rainer    (1000) users      (100)    11941 2023-04-07 09:54:41.000000 ooresults-0.2.2/ooresults/templates/classes_tab_content.html
+-rw-r--r--   0 rainer    (1000) users      (100)     2957 2023-04-03 19:51:02.000000 ooresults-0.2.2/ooresults/templates/classes_table.html
+-rw-r--r--   0 rainer    (1000) users      (100)     6858 2023-04-07 09:54:41.000000 ooresults-0.2.2/ooresults/templates/clubs_tab_content.html
+-rw-r--r--   0 rainer    (1000) users      (100)      453 2023-03-01 18:09:04.000000 ooresults-0.2.2/ooresults/templates/clubs_table.html
+-rwxr-xr-x   0 rainer    (1000) users      (100)    11673 2023-04-07 09:54:41.000000 ooresults-0.2.2/ooresults/templates/competitors_tab_content.html
+-rw-r--r--   0 rainer    (1000) users      (100)     1030 2023-03-01 18:09:04.000000 ooresults-0.2.2/ooresults/templates/competitors_table.html
+-rw-r--r--   0 rainer    (1000) users      (100)    11955 2023-04-07 09:54:41.000000 ooresults-0.2.2/ooresults/templates/courses_tab_content.html
+-rw-r--r--   0 rainer    (1000) users      (100)     1386 2023-03-01 18:09:04.000000 ooresults-0.2.2/ooresults/templates/courses_table.html
+-rw-r--r--   0 rainer    (1000) users      (100)     6529 2023-03-26 08:00:56.000000 ooresults-0.2.2/ooresults/templates/demo_reader.html
+-rwxr-xr-x   0 rainer    (1000) users      (100)    19221 2023-04-07 09:54:41.000000 ooresults-0.2.2/ooresults/templates/entries_tab_content.html
+-rw-r--r--   0 rainer    (1000) users      (100)     3006 2023-04-03 19:51:02.000000 ooresults-0.2.2/ooresults/templates/entries_table.html
+-rw-r--r--   0 rainer    (1000) users      (100)     9445 2023-04-07 09:54:41.000000 ooresults-0.2.2/ooresults/templates/events_tab_content.html
+-rw-r--r--   0 rainer    (1000) users      (100)     1339 2023-03-01 18:09:04.000000 ooresults-0.2.2/ooresults/templates/events_table.html
+-rw-r--r--   0 rainer    (1000) users      (100)     5937 2023-03-01 18:09:04.000000 ooresults-0.2.2/ooresults/templates/main.html
+-rw-r--r--   0 rainer    (1000) users      (100)     5924 2023-04-07 09:54:41.000000 ooresults-0.2.2/ooresults/templates/results_tab_content.html
+-rw-r--r--   0 rainer    (1000) users      (100)     5390 2023-04-03 19:51:02.000000 ooresults-0.2.2/ooresults/templates/results_table.html
+-rw-r--r--   0 rainer    (1000) users      (100)      528 2023-03-01 18:09:04.000000 ooresults-0.2.2/ooresults/templates/root.html
+-rw-r--r--   0 rainer    (1000) users      (100)     1084 2023-03-01 18:09:04.000000 ooresults-0.2.2/ooresults/templates/select_event.html
+-rw-r--r--   0 rainer    (1000) users      (100)     2500 2023-03-01 18:09:04.000000 ooresults-0.2.2/ooresults/templates/series_settings.html
+-rw-r--r--   0 rainer    (1000) users      (100)     8367 2023-04-07 09:54:41.000000 ooresults-0.2.2/ooresults/templates/series_tab_content.html
+-rw-r--r--   0 rainer    (1000) users      (100)     1541 2023-03-01 18:09:04.000000 ooresults-0.2.2/ooresults/templates/series_table.html
+drwxr-xr-x   0 rainer    (1000) users      (100)        0 2023-04-07 09:55:30.555350 ooresults-0.2.2/ooresults/templates/si/
+-rw-r--r--   0 rainer    (1000) users      (100)      902 2023-04-03 19:51:02.000000 ooresults-0.2.2/ooresults/templates/si/si1_data.html
+-rw-r--r--   0 rainer    (1000) users      (100)      396 2023-03-01 18:09:04.000000 ooresults-0.2.2/ooresults/templates/si/si1_error.html
+-rw-r--r--   0 rainer    (1000) users      (100)     6992 2023-03-01 18:09:04.000000 ooresults-0.2.2/ooresults/templates/si/si1_page.html
+-rw-r--r--   0 rainer    (1000) users      (100)     4161 2023-04-03 19:51:02.000000 ooresults-0.2.2/ooresults/templates/si/si2_data.html
+-rw-r--r--   0 rainer    (1000) users      (100)     3589 2023-03-01 18:09:04.000000 ooresults-0.2.2/ooresults/templates/si/si2_page.html
+-rw-r--r--   0 rainer    (1000) users      (100)      383 2023-03-01 18:09:04.000000 ooresults-0.2.2/ooresults/templates/unauthorized.html
+-rw-r--r--   0 rainer    (1000) users      (100)     2407 2023-03-01 18:09:04.000000 ooresults-0.2.2/ooresults/user.py
+drwxr-xr-x   0 rainer    (1000) users      (100)        0 2023-04-07 09:55:30.555350 ooresults-0.2.2/ooresults/utils/
+-rw-r--r--   0 rainer    (1000) users      (100)      803 2023-03-01 18:09:04.000000 ooresults-0.2.2/ooresults/utils/__init__.py
+-rw-r--r--   0 rainer    (1000) users      (100)     1666 2023-04-03 19:51:02.000000 ooresults-0.2.2/ooresults/utils/globals.py
+drwxr-xr-x   0 rainer    (1000) users      (100)        0 2023-04-07 09:55:30.559350 ooresults-0.2.2/ooresults/websocket_server/
+-rw-r--r--   0 rainer    (1000) users      (100)      803 2023-03-01 18:09:04.000000 ooresults-0.2.2/ooresults/websocket_server/__init__.py
+-rw-r--r--   0 rainer    (1000) users      (100)     1749 2023-03-01 18:09:04.000000 ooresults-0.2.2/ooresults/websocket_server/si.py
+-rw-r--r--   0 rainer    (1000) users      (100)    14523 2023-03-01 18:09:04.000000 ooresults-0.2.2/ooresults/websocket_server/websocket_handler.py
+-rw-r--r--   0 rainer    (1000) users      (100)     2143 2023-03-01 18:09:04.000000 ooresults-0.2.2/ooresults/websocket_server/websocket_server.py
+drwxr-xr-x   0 rainer    (1000) users      (100)        0 2023-04-07 09:55:30.535350 ooresults-0.2.2/ooresults.egg-info/
+-rw-r--r--   0 rainer    (1000) users      (100)    42907 2023-04-07 09:55:30.000000 ooresults-0.2.2/ooresults.egg-info/PKG-INFO
+-rw-r--r--   0 rainer    (1000) users      (100)     4448 2023-04-07 09:55:30.000000 ooresults-0.2.2/ooresults.egg-info/SOURCES.txt
+-rw-r--r--   0 rainer    (1000) users      (100)        1 2023-04-07 09:55:30.000000 ooresults-0.2.2/ooresults.egg-info/dependency_links.txt
+-rw-r--r--   0 rainer    (1000) users      (100)      102 2023-04-07 09:55:30.000000 ooresults-0.2.2/ooresults.egg-info/entry_points.txt
+-rw-r--r--   0 rainer    (1000) users      (100)      152 2023-04-07 09:55:30.000000 ooresults-0.2.2/ooresults.egg-info/requires.txt
+-rw-r--r--   0 rainer    (1000) users      (100)       10 2023-04-07 09:55:30.000000 ooresults-0.2.2/ooresults.egg-info/top_level.txt
+-rwxr-xr-x   0 rainer    (1000) users      (100)      977 2023-04-07 09:54:41.000000 ooresults-0.2.2/pyproject.toml
+-rwxr-xr-x   0 rainer    (1000) users      (100)      616 2023-04-07 09:55:30.567350 ooresults-0.2.2/setup.cfg
+drwxr-xr-x   0 rainer    (1000) users      (100)        0 2023-04-07 09:55:30.559350 ooresults-0.2.2/tests/
+-rw-r--r--   0 rainer    (1000) users      (100)      803 2023-03-01 18:09:04.000000 ooresults-0.2.2/tests/__init__.py
+-rw-r--r--   0 rainer    (1000) users      (100)     1414 2023-03-01 18:09:04.000000 ooresults-0.2.2/tests/competitor.py
+-rw-r--r--   0 rainer    (1000) users      (100)     2061 2023-03-01 18:09:04.000000 ooresults-0.2.2/tests/entry.py
+drwxr-xr-x   0 rainer    (1000) users      (100)        0 2023-04-07 09:55:30.559350 ooresults-0.2.2/tests/model/
+-rw-r--r--   0 rainer    (1000) users      (100)      803 2023-03-01 18:09:04.000000 ooresults-0.2.2/tests/model/__init__.py
+-rw-r--r--   0 rainer    (1000) users      (100)    10750 2023-03-01 18:09:04.000000 ooresults-0.2.2/tests/model/test_courses.py
+-rw-r--r--   0 rainer    (1000) users      (100)    16528 2023-03-01 18:09:04.000000 ooresults-0.2.2/tests/model/test_parse_cardreader_log.py
+-rw-r--r--   0 rainer    (1000) users      (100)    27576 2023-03-26 08:00:56.000000 ooresults-0.2.2/tests/model/test_store_cardreader_result.py
+drwxr-xr-x   0 rainer    (1000) users      (100)        0 2023-04-07 09:55:30.563350 ooresults-0.2.2/tests/plugins/
+-rw-r--r--   0 rainer    (1000) users      (100)    13070 2023-03-31 20:12:46.000000 ooresults-0.2.2/tests/plugins/test_export_competitors_oe2003.py
+-rw-r--r--   0 rainer    (1000) users      (100)    29297 2023-03-31 20:12:46.000000 ooresults-0.2.2/tests/plugins/test_import_competitors_oe2003.py
+-rw-r--r--   0 rainer    (1000) users      (100)     2766 2023-04-03 19:51:02.000000 ooresults-0.2.2/tests/plugins/test_plugin_iof_class_list.py
+-rw-r--r--   0 rainer    (1000) users      (100)     4000 2023-04-03 19:51:02.000000 ooresults-0.2.2/tests/plugins/test_plugin_iof_competitor_list.py
+-rw-r--r--   0 rainer    (1000) users      (100)    10229 2023-04-03 19:51:02.000000 ooresults-0.2.2/tests/plugins/test_plugin_iof_course_data.py
+-rw-r--r--   0 rainer    (1000) users      (100)     8789 2023-04-03 19:51:02.000000 ooresults-0.2.2/tests/plugins/test_plugin_iof_entry_list.py
+-rw-r--r--   0 rainer    (1000) users      (100)    28112 2023-04-03 19:51:02.000000 ooresults-0.2.2/tests/plugins/test_plugin_iof_result_list.py
+drwxr-xr-x   0 rainer    (1000) users      (100)        0 2023-04-07 09:55:30.567350 ooresults-0.2.2/tests/repo/
+-rw-r--r--   0 rainer    (1000) users      (100)      803 2023-03-01 18:09:04.000000 ooresults-0.2.2/tests/repo/__init__.py
+-rw-r--r--   0 rainer    (1000) users      (100)     9402 2023-03-01 18:09:04.000000 ooresults-0.2.2/tests/repo/test_classes.py
+-rw-r--r--   0 rainer    (1000) users      (100)     5314 2023-03-01 18:09:04.000000 ooresults-0.2.2/tests/repo/test_clubs.py
+-rw-r--r--   0 rainer    (1000) users      (100)    10687 2023-03-01 18:09:04.000000 ooresults-0.2.2/tests/repo/test_competitors.py
+-rw-r--r--   0 rainer    (1000) users      (100)     7336 2023-03-01 18:09:04.000000 ooresults-0.2.2/tests/repo/test_courses.py
+-rw-r--r--   0 rainer    (1000) users      (100)    39414 2023-03-01 18:09:04.000000 ooresults-0.2.2/tests/repo/test_entries.py
+-rw-r--r--   0 rainer    (1000) users      (100)     7540 2023-03-01 18:09:04.000000 ooresults-0.2.2/tests/repo/test_events.py
+-rw-r--r--   0 rainer    (1000) users      (100)     2353 2023-03-01 18:09:04.000000 ooresults-0.2.2/tests/repo/test_settings.py
+-rw-r--r--   0 rainer    (1000) users      (100)     9467 2023-03-01 18:09:04.000000 ooresults-0.2.2/tests/test_compute_result_net.py
+-rw-r--r--   0 rainer    (1000) users      (100)    15440 2023-03-01 18:09:04.000000 ooresults-0.2.2/tests/test_compute_result_score.py
+-rw-r--r--   0 rainer    (1000) users      (100)    38250 2023-03-01 18:09:04.000000 ooresults-0.2.2/tests/test_compute_result_standard.py
+-rw-r--r--   0 rainer    (1000) users      (100)     7257 2023-03-01 18:09:04.000000 ooresults-0.2.2/tests/test_configuration.py
+-rw-r--r--   0 rainer    (1000) users      (100)     1973 2023-04-03 19:51:02.000000 ooresults-0.2.2/tests/test_globals.py
+-rw-r--r--   0 rainer    (1000) users      (100)     1758 2023-03-01 18:09:04.000000 ooresults-0.2.2/tests/test_handicap.py
+-rw-r--r--   0 rainer    (1000) users      (100)    19384 2023-03-01 18:09:04.000000 ooresults-0.2.2/tests/test_ranking.py
+-rw-r--r--   0 rainer    (1000) users      (100)    26017 2023-03-01 18:09:04.000000 ooresults-0.2.2/tests/test_series.py
+-rw-r--r--   0 rainer    (1000) users      (100)     2326 2023-03-01 18:09:04.000000 ooresults-0.2.2/tests/test_user.py
```

### Comparing `ooresults-0.2.1/LICENSE` & `ooresults-0.2.2/LICENSE`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/PKG-INFO` & `ooresults-0.2.2/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: ooresults
-Version: 0.2.1
+Version: 0.2.2
 Summary: A software for the evaluation of the results of orienteering events
 Author: Rainer Garus
 License:                     GNU AFFERO GENERAL PUBLIC LICENSE
                                Version 3, 19 November 2007
         
          Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
          Everyone is permitted to copy and distribute verbatim copies
```

### Comparing `ooresults-0.2.1/README.rst` & `ooresults-0.2.2/README.rst`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/ooresults/__init__.py` & `ooresults-0.2.2/ooresults/__init__.py`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/ooresults/_reader.py` & `ooresults-0.2.2/ooresults/_reader.py`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/ooresults/_server.py` & `ooresults-0.2.2/ooresults/_server.py`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/ooresults/configuration.py` & `ooresults-0.2.2/ooresults/configuration.py`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/ooresults/handler/__init__.py` & `ooresults-0.2.2/ooresults/handler/__init__.py`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/ooresults/handler/classes.py` & `ooresults-0.2.2/ooresults/handler/classes.py`

 * *Files 8% similar despite different names*

```diff
@@ -28,18 +28,19 @@
 
 from ooresults.handler import model
 from ooresults.repo.repo import ClassUsedError
 from ooresults.repo.repo import EventNotFoundError
 from ooresults.repo.repo import ConstraintError
 from ooresults.repo.class_params import ClassParams
 from ooresults.plugins import iof_class_list
+from ooresults.utils.globals import t_globals
 
 
 templates = pathlib.Path(__file__).resolve().parent.parent / "templates"
-render = web.template.render(templates, globals={"str": str})
+render = web.template.render(templates, globals=t_globals)
 
 
 def update(event_id: int):
     classes_list = model.get_classes(event_id=event_id)
     event = list(model.get_event(event_id))
     if event == []:
         return render.classes_table({}, classes_list)
```

### Comparing `ooresults-0.2.1/ooresults/handler/clubs.py` & `ooresults-0.2.2/ooresults/handler/clubs.py`

 * *Files 3% similar despite different names*

```diff
@@ -22,18 +22,19 @@
 
 import web
 from web.utils import Storage
 
 from ooresults.handler import model
 from ooresults.repo.repo import ClubUsedError
 from ooresults.repo.repo import ConstraintError
+from ooresults.utils.globals import t_globals
 
 
 templates = pathlib.Path(__file__).resolve().parent.parent / "templates"
-render = web.template.render(templates, globals={"str": str})
+render = web.template.render(templates, globals=t_globals)
 
 
 class Update:
     def POST(self):
         """Update data"""
         return render.clubs_table(model.get_clubs())
```

### Comparing `ooresults-0.2.1/ooresults/handler/competitors.py` & `ooresults-0.2.2/ooresults/handler/competitors.py`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/ooresults/handler/courses.py` & `ooresults-0.2.2/ooresults/handler/courses.py`

 * *Files 1% similar despite different names*

```diff
@@ -24,18 +24,19 @@
 from web.utils import Storage
 
 from ooresults.handler import model
 from ooresults.repo.repo import CourseUsedError
 from ooresults.repo.repo import EventNotFoundError
 from ooresults.repo.repo import ConstraintError
 from ooresults.plugins import iof_course_data
+from ooresults.utils.globals import t_globals
 
 
 templates = pathlib.Path(__file__).resolve().parent.parent / "templates"
-render = web.template.render(templates, globals={"str": str, "round": round})
+render = web.template.render(templates, globals=t_globals)
 
 
 def update(event_id: int):
     courses_list = model.get_courses(event_id=event_id)
     event = list(model.get_event(event_id))
     if event == []:
         return render.courses_table({}, courses_list)
```

### Comparing `ooresults-0.2.1/ooresults/handler/demo_reader.py` & `ooresults-0.2.2/ooresults/handler/demo_reader.py`

 * *Files 20% similar despite different names*

```diff
@@ -17,16 +17,18 @@
 # along with this program.  If not, see <https://www.gnu.org/licenses/>.
 
 
 import pathlib
 
 import web
 
+from ooresults.utils.globals import t_globals
+
 
 templates = pathlib.Path(__file__).resolve().parent.parent / "templates"
-render = web.template.render(templates, globals={"str": str})
+render = web.template.render(templates, globals=t_globals)
 
 
 class Update:
     def GET(self):
         """Update data"""
         return render.demo_reader()
```

### Comparing `ooresults-0.2.1/ooresults/handler/entries.py` & `ooresults-0.2.2/ooresults/handler/entries.py`

 * *Files 2% similar despite different names*

```diff
@@ -26,14 +26,15 @@
 
 import tzlocal
 import web
 from web.utils import Storage
 
 from ooresults.handler import model
 from ooresults.plugins.imports.entries import text
+from ooresults.plugins import oe12
 from ooresults.plugins import oe2003
 from ooresults.plugins import iof_entry_list
 from ooresults.plugins import iof_result_list
 from ooresults.repo import result_type
 from ooresults.repo import start_type
 from ooresults.repo.result_type import ResultStatus
 from ooresults.repo.repo import EventNotFoundError
@@ -135,14 +136,18 @@
                 event = model.get_event(id=event_id)
                 entry_list = model.get_entries(event_id=event_id)
                 content = iof_result_list.create_result_list(event[0], entry_list)
             elif data.entr_export == "entr.export.3":
                 class_list = model.get_classes(event_id=event_id)
                 entry_list = model.get_entries(event_id=event_id)
                 content = oe2003.create(entry_list, list(class_list))
+            elif data.entr_export == "entr.export.4":
+                class_list = model.get_classes(event_id=event_id)
+                entry_list = model.get_entries(event_id=event_id)
+                content = oe12.create(entry_list, list(class_list))
 
         except KeyError:
             raise web.conflict("Entry deleted")
         except:
             logging.exception("Internal server error")
             raise
```

### Comparing `ooresults-0.2.1/ooresults/handler/events.py` & `ooresults-0.2.2/ooresults/handler/events.py`

 * *Files 6% similar despite different names*

```diff
@@ -22,18 +22,19 @@
 import pathlib
 
 import web
 from web.utils import Storage
 
 from ooresults.handler import model
 from ooresults.repo.repo import ConstraintError
+from ooresults.utils.globals import t_globals
 
 
 templates = pathlib.Path(__file__).resolve().parent.parent / "templates"
-render = web.template.render(templates, globals={"str": str})
+render = web.template.render(templates, globals=t_globals)
 
 
 def update():
     return render.events_table(model.get_events())
 
 
 class Update:
```

### Comparing `ooresults-0.2.1/ooresults/handler/handicap.py` & `ooresults-0.2.2/ooresults/handler/handicap.py`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/ooresults/handler/model.py` & `ooresults-0.2.2/ooresults/handler/model.py`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/ooresults/handler/results.py` & `ooresults-0.2.2/ooresults/handler/results.py`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/ooresults/handler/series.py` & `ooresults-0.2.2/ooresults/handler/series.py`

 * *Files 1% similar despite different names*

```diff
@@ -26,18 +26,19 @@
 import web
 import clevercsv as csv
 
 from ooresults.handler import model
 from ooresults.handler import results
 from ooresults.repo import series_type
 import ooresults.pdf.series
+from ooresults.utils.globals import t_globals
 
 
 templates = pathlib.Path(__file__).resolve().parent.parent / "templates"
-render = web.template.render(templates, globals={"str": str})
+render = web.template.render(templates, globals=t_globals)
 
 
 def build_total_results(settings: series_type.Settings, list_of_results, organizers=[]):
     q = Decimal(10) ** -settings.decimal_places
 
     r = {}
     for i, class_results in enumerate(list_of_results):
```

### Comparing `ooresults-0.2.1/ooresults/pdf/fonts/Carlito-Bold.ttf` & `ooresults-0.2.2/ooresults/pdf/fonts/Carlito-Bold.ttf`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/ooresults/pdf/fonts/Carlito-BoldItalic.ttf` & `ooresults-0.2.2/ooresults/pdf/fonts/Carlito-BoldItalic.ttf`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/ooresults/pdf/fonts/Carlito-Italic.ttf` & `ooresults-0.2.2/ooresults/pdf/fonts/Carlito-Italic.ttf`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/ooresults/pdf/fonts/Carlito-Regular.ttf` & `ooresults-0.2.2/ooresults/pdf/fonts/Carlito-Regular.ttf`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/ooresults/pdf/pdf.py` & `ooresults-0.2.2/ooresults/pdf/pdf.py`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/ooresults/pdf/result.py` & `ooresults-0.2.2/ooresults/pdf/result.py`

 * *Files 2% similar despite different names*

```diff
@@ -19,14 +19,15 @@
 
 from typing import Dict
 from typing import Optional
 from typing import Any
 
 from ooresults.repo.result_type import ResultStatus
 from ooresults.pdf.pdf import PDF
+from ooresults.utils import globals
 
 
 def create_pdf(
     event: Dict, results: Dict, include_dns: bool = False, landscape: bool = True
 ) -> bytes:
     W_SPACE = 4
     W_RANK = 9
@@ -52,21 +53,21 @@
         while pdf.get_string_width(txt) > w:
             txt = txt[:-1]
         pdf.cell(w=w, h=h, txt=txt, align=align)
 
     def print_time(width: int, time: int, status: ResultStatus) -> None:
         txt = ""
         if status == ResultStatus.OK:
-            txt = "{:d}:{:02d}".format(time // 60, time % 60)
+            txt = globals.minutes_seconds(time)
         cell(w=width, h=None, txt=txt, align="R")
 
     def print_time_or_status(width: int, time: int, status: ResultStatus) -> None:
         txt = pdf.MAP_STATUS[status]
         if status == ResultStatus.OK:
-            txt = "{:d}:{:02d}".format(time // 60, time % 60)
+            txt = globals.minutes_seconds(time)
         cell(w=width, h=None, txt=txt, align="R")
 
     def print_points(width: int, points: Optional[float], status: ResultStatus) -> None:
         txt = ""
         if points is not None and status == ResultStatus.OK:
             txt = "{:.2f}".format(points)
         cell(w=width, h=None, txt=txt, align="R")
```

### Comparing `ooresults-0.2.1/ooresults/pdf/series.py` & `ooresults-0.2.2/ooresults/pdf/series.py`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/ooresults/pdf/splittimes.py` & `ooresults-0.2.2/ooresults/pdf/splittimes.py`

 * *Files 2% similar despite different names*

```diff
@@ -21,14 +21,15 @@
 from typing import Dict
 from typing import List
 from typing import Optional
 
 from ooresults.repo.result_type import PersonRaceResult
 from ooresults.repo.result_type import ResultStatus
 from ooresults.pdf.pdf import PDF
+from ooresults.utils import globals
 
 
 def create_pdf(event: Dict, results: Dict, landscape: bool = False) -> bytes:
     # Instantiation of inherited class
     pdf = PDF(name=event.name, landscape=landscape)
     pdf.set_margin(margin=10)
     pdf.set_auto_page_break(auto=True, margin=15)
@@ -38,21 +39,21 @@
     def cell(w: int, h: Optional[int] = None, txt: str = "", align: str = "L") -> None:
         while pdf.get_string_width(txt) > w:
             txt = txt[:-1]
         pdf.cell(w=w, h=h, txt=txt, align=align)
 
     def format_time(time: int, status: ResultStatus) -> str:
         if status == ResultStatus.OK:
-            return "{:d}:{:02d}".format(time // 60, time % 60)
+            return globals.minutes_seconds(time=time)
         else:
             return pdf.MAP_STATUS[status]
 
     def format_splittime(time: Optional[int]) -> str:
         if time is not None:
-            return "{:d}:{:02d}".format(time // 60, time % 60)
+            return globals.minutes_seconds(time=time)
         else:
             return "-----"
 
     def pre(t1: str = "", t2: str = "", t3: str = "") -> None:
         pdf.set_font(style="B")
         cell(w=7, h=None, txt=t1, align="R")
         cell(w=2, h=None, txt="")
```

### Comparing `ooresults-0.2.1/ooresults/plugins/__init__.py` & `ooresults-0.2.2/ooresults/plugins/__init__.py`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/ooresults/plugins/imports/entries/__init__.py` & `ooresults-0.2.2/ooresults/plugins/imports/entries/__init__.py`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/ooresults/plugins/imports/entries/text.py` & `ooresults-0.2.2/ooresults/plugins/imports/entries/text.py`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/ooresults/plugins/iof_class_list.py` & `ooresults-0.2.2/ooresults/plugins/iof_class_list.py`

 * *Files 4% similar despite different names*

```diff
@@ -38,15 +38,18 @@
     E = ElementMaker(namespace=iof_namespace, nsmap=namespaces)
 
     CLASSLIST = E.ClassList
     CLASS = E.Class
     NAME = E.Name
     SHORTNAME = E.ShortName
 
-    root = CLASSLIST(iofVersion="3.0")
+    root = CLASSLIST(
+        iofVersion="3.0",
+        creator="ooresults (https://pypi.org/project/ooresults)",
+    )
 
     for c in classes:
         class_ = CLASS()
         class_.append(NAME(c["name"]))
 
         if c.get("short_name", None) is not None:
             class_.append(SHORTNAME(str(c["short_name"])))
```

### Comparing `ooresults-0.2.1/ooresults/plugins/iof_competitor_list.py` & `ooresults-0.2.2/ooresults/plugins/iof_competitor_list.py`

 * *Files 2% similar despite different names*

```diff
@@ -42,15 +42,18 @@
     NAME = E.Name
     FAMILY = E.Family
     GIVEN = E.Given
     BIRTHDATE = E.BirthDate
     ORGANISATION = E.Organisation
     CONTROLCARD = E.ControlCard
 
-    root = COMPETITORLIST(iofVersion="3.0")
+    root = COMPETITORLIST(
+        iofVersion="3.0",
+        creator="ooresults (https://pypi.org/project/ooresults)",
+    )
 
     for c in competitors:
         competitor = COMPETITOR()
         person = PERSON(
             NAME(
                 FAMILY(c.last_name),
                 GIVEN(c.first_name),
```

### Comparing `ooresults-0.2.1/ooresults/plugins/iof_course_data.py` & `ooresults-0.2.2/ooresults/plugins/iof_course_data.py`

 * *Files 2% similar despite different names*

```diff
@@ -49,31 +49,34 @@
     CLIMB = E.Climb
     COURSECONTROL = E.CourseControl
     CONTROL = E.Control
     CLASSCOURSEASSIGNMENT = E.ClassCourseAssignment
     CLASSNAME = E.ClassName
     COURSENAME = E.CourseName
 
-    root = COURSEDATA(iofVersion="3.0")
+    root = COURSEDATA(
+        iofVersion="3.0",
+        creator="ooresults (https://pypi.org/project/ooresults)",
+    )
 
     e_event = EVENT()
     e_event.append(NAME(event.get("name", "")))
     if event.get("date", None) is not None:
         e_event.append(STARTTIME(DATE(event["date"].isoformat())))
     root.append(e_event)
 
     race_course_data = RACECOURSEDATA()
     for c in courses:
         course = COURSE()
         course.append(NAME(c["name"]))
 
         if c.get("length", None) is not None:
-            course.append(LENGTH(str(c["length"])))
+            course.append(LENGTH(str(round(c["length"]))))
         if c.get("climb", None) is not None:
-            course.append(CLIMB(str(c["climb"])))
+            course.append(CLIMB(str(round(c["climb"]))))
 
         cc = COURSECONTROL(CONTROL("S1"))
         cc.set("type", "Start")
         course.append(cc)
 
         for control in c["controls"]:
             cc = COURSECONTROL(CONTROL(control))
```

### Comparing `ooresults-0.2.1/ooresults/plugins/iof_entry_list.py` & `ooresults-0.2.2/ooresults/plugins/iof_entry_list.py`

 * *Files 5% similar despite different names*

```diff
@@ -50,15 +50,18 @@
     FAMILY = E.Family
     GIVEN = E.Given
     BIRTHDATE = E.BirthDate
     ORGANISATION = E.Organisation
     CONTROLCARD = E.ControlCard
     CLASS = E.Class
 
-    root = ENTRYLIST(iofVersion="3.0")
+    root = ENTRYLIST(
+        iofVersion="3.0",
+        creator="ooresults (https://pypi.org/project/ooresults)",
+    )
 
     e_event = EVENT()
     e_event.append(NAME(event.get("name", "")))
     if event.get("date", None) is not None:
         e_event.append(STARTTIME(DATE(event["date"].isoformat())))
     root.append(e_event)
```

### Comparing `ooresults-0.2.1/ooresults/plugins/iof_result_list.py` & `ooresults-0.2.2/ooresults/plugins/iof_result_list.py`

 * *Files 1% similar despite different names*

```diff
@@ -60,15 +60,18 @@
     STATUS = E.Status
     STARTTIME = E.StartTime
     FINISHTIME = E.FinishTime
     TIME = E.Time
     SPLITTIME = E.SplitTime
     CONTROLCODE = E.ControlCode
 
-    root = RESULTLIST(iofVersion="3.0")
+    root = RESULTLIST(
+        iofVersion="3.0",
+        creator="ooresults (https://pypi.org/project/ooresults)",
+    )
 
     e_event = EVENT()
     e_event.append(NAME(event.get("name", "")))
     if event.get("date", None) is not None:
         e_event.append(STARTTIME(DATE(event["date"].isoformat())))
     root.append(e_event)
```

### Comparing `ooresults-0.2.1/ooresults/plugins/oe2003.py` & `ooresults-0.2.2/ooresults/plugins/oe2003.py`

 * *Files 6% similar despite different names*

```diff
@@ -78,58 +78,88 @@
         ResultStatus.DID_NOT_FINISH: "2",
         ResultStatus.OVER_TIME: "5",
         ResultStatus.DISQUALIFIED: "4",
     }
 
     # write entries
     for i, e in enumerate(entries):
-        class_no = None
-        class_short_name = None
+        class_no = ""
+        class_name = ""
+        class_short_name = ""
         for j, c in enumerate(class_list):
             if c.get("id") == e.get("class_id", None):
-                class_no = j + 1
-                class_short_name = c.get("short_name", None)
+                class_no = str(j + 1)
+                class_name = c.get("name", "")
+                if c.get("short_name", None):
+                    class_short_name = c.get("short_name", class_name)
+                else:
+                    class_short_name = class_name
                 break
 
         # export only items with defined name
-        if e.get("last_name", None) != None:
+        if e.get("last_name", None) is not None:
+            chip = e.get("chip", "")
+            last_name = e.get("last_name", "")
+            first_name = e.get("first_name", "")
+
+            year = ""
+            if e.get("year", None) is not None:
+                year = str(e.get("year", None))
+
+            gender = {"": "", "F": "W", "M": "M"}[e.get("gender", "")]
+            not_competing = "X" if e.get("not_competing", False) else "0"
+
+            start_time = ""
+            if e.result.start_time is not None:
+                start_time = e.result.start_time.strftime("%H:%M:%S")
+
+            finish_time = ""
+            if e.result.finish_time is not None:
+                finish_time = e.result.finish_time.strftime("%H:%M:%S")
+
+            result_time = ""
+            if e.result.time is not None:
+                result_time = "{:02d}:{:02d}:{:02d}".format(
+                    e.result.time // 3600,
+                    e.result.time % 3600 // 60,
+                    e.result.time % 60,
+                )
+
+            status = STATUS_MAP.get(e.result.status, "")
+
+            club_id = ""
+            if e.get("club_id", None) is not None:
+                club_id = str(e.get("club_id", None))
+
+            club_name = ""
+            if e.get("club_id", None) is not None:
+                club_name = e.get("club", "")
+
             writer.writerow(
                 [
-                    str(i + 1),
-                    e.get("chip", ""),
-                    "",
-                    cp1252(e.get("last_name", "")),
-                    cp1252(e.get("first_name", "")),
-                    str(e.get("year", None)) if e.get("year", None) is not None else "",
-                    {"": "", "F": "W", "M": "M"}[e.get("gender", "")],
-                    "",
-                    "X" if e.get("not_competing", False) else "0",
-                    e.result.start_time.strftime("%H:%M:%S")
-                    if e.result.start_time is not None
-                    else "",
-                    e.result.finish_time.strftime("%H:%M:%S")
-                    if e.result.finish_time is not None
-                    else "",
-                    "{:d}:{:02d}".format(e.result.time // 60, e.result.time % 60)
-                    if e.result.time is not None
-                    else "",
-                    STATUS_MAP.get(e.result.status, ""),
-                    str(e.get("club_id", None))
-                    if e.get("club_id", None) is not None
-                    else "",
-                    "",
-                    cp1252(e.get("club", ""))
-                    if e.get("club_id", None) is not None
-                    else "",
-                    "",
-                    str(class_no) if class_no is not None else "",
-                    class_short_name
-                    if class_short_name is not None
-                    else e.get("class_", ""),
-                    e.get("class_", ""),
+                    str(i + 1),  # Stnr
+                    chip,  # Chip
+                    "",  # Datenbank Id
+                    cp1252(last_name),  # Nachname
+                    cp1252(first_name),  # Vorname
+                    year,  # Jg
+                    gender,  # G
+                    "",  # Block
+                    not_competing,  # AK
+                    start_time,  # Start
+                    finish_time,  # Ziel
+                    result_time,  # Zeit
+                    status,  # Wertung
+                    club_id,  # Club-Nr.
+                    "",  # Abk
+                    cp1252(club_name),  # Ort
+                    "",  # Nat
+                    class_no,  # Katnr
+                    class_short_name,  # Kurz
+                    class_name,  # Lang
                 ]
             )
 
     content = output.getvalue()
     output.close()
     return content.encode(encoding="windows-1252")
 
@@ -143,15 +173,15 @@
     except:
         content = content.decode(encoding="windows-1252")
 
     dialect = csv.Sniffer().sniff(content, delimiters=",;\t")
     for values in csv.reader(io.StringIO(content), dialect=dialect):
         if column_nr == {}:
             for i, v in enumerate(values):
-                if v in ["Chip", "SI card1"]:
+                if v in ["Chip", "Chipno", "Chipnr", "SI card1"]:
                     column_nr["chip"] = i
                     break
             else:
                 raise RuntimeError("Chip column not found")
 
             for i, v in enumerate(values):
                 if v in ["First name", "Vorname"]:
@@ -206,19 +236,26 @@
                 if v in ["Class", "Lang", "Long"]:
                     column_nr["class_"] = i
                     break
             else:
                 raise RuntimeError("Class column not found")
 
             for i, v in enumerate(values):
-                if v in ["Club", "Ort", "City"]:
+                if v in ["City", "Ort"]:
                     column_nr["club"] = i
                     break
             else:
-                raise RuntimeError("Club column not found")
+                raise RuntimeError("City column not found")
+
+            for i, v in enumerate(values):
+                if v in ["Cl.name", "Abk"]:
+                    column_nr["club1"] = i
+                    break
+            else:
+                raise RuntimeError("Cl.name column not found")
 
             for i, v in enumerate(values):
                 if v in ["Start", "Start1"]:
                     column_nr["start_time"] = i
                     break
             else:
                 raise RuntimeError("Start column not found")
@@ -346,14 +383,21 @@
             if (
                 r["result"].time is None
                 and r["result"].finish_time is None
                 and r["result"].status == ResultStatus.OK
             ):
                 r["result"].status = ResultStatus.INACTIVE
 
+            # SportSoftware use column "club", but OOnet use column "club1"
+            # In contrast to SportSoftware, OOnet does not write any gender information
+            if r["gender"] == "" and r["club1"] != "":
+                r["club"] = r["club1"]
+            # we remove club1 key, it is not needed outside this function
+            del r["club1"]
+
             # store start time as start punch time only if finish time is defined
             # or status is missing punch, did not finished or over time
             if r["result"].finish_time is not None or r["result"].status in [
                 ResultStatus.MISSING_PUNCH,
                 ResultStatus.DID_NOT_FINISH,
                 ResultStatus.OVER_TIME,
             ]:
```

### Comparing `ooresults-0.2.1/ooresults/reader.py` & `ooresults-0.2.2/ooresults/reader.py`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/ooresults/repo/__init__.py` & `ooresults-0.2.2/ooresults/repo/__init__.py`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/ooresults/repo/class_params.py` & `ooresults-0.2.2/ooresults/repo/class_params.py`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/ooresults/repo/repo.py` & `ooresults-0.2.2/ooresults/repo/repo.py`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/ooresults/repo/result_type.py` & `ooresults-0.2.2/ooresults/repo/result_type.py`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/ooresults/repo/series_type.py` & `ooresults-0.2.2/ooresults/repo/series_type.py`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/ooresults/repo/sqlite_repo.py` & `ooresults-0.2.2/ooresults/repo/sqlite_repo.py`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/ooresults/repo/start_type.py` & `ooresults-0.2.2/ooresults/repo/start_type.py`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/ooresults/repo/update/__init__.py` & `ooresults-0.2.2/ooresults/repo/update/__init__.py`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/ooresults/repo/update/update_008.py` & `ooresults-0.2.2/ooresults/repo/update/update_008.py`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/ooresults/repo/update/update_tables.py` & `ooresults-0.2.2/ooresults/repo/update/update_tables.py`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/ooresults/schema/IOF.xsd` & `ooresults-0.2.2/ooresults/schema/IOF.xsd`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/ooresults/schema/cardreader_log.json` & `ooresults-0.2.2/ooresults/schema/cardreader_log.json`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/ooresults/server.py` & `ooresults-0.2.2/ooresults/server.py`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/ooresults/set_legacy_mode.py` & `ooresults-0.2.2/ooresults/set_legacy_mode.py`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/ooresults/static/style-tab.css` & `ooresults-0.2.2/ooresults/static/style-tab.css`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/ooresults/static/style.css` & `ooresults-0.2.2/ooresults/static/style.css`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/ooresults/static/w3.js` & `ooresults-0.2.2/ooresults/static/w3.js`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/ooresults/templates/add_class.html` & `ooresults-0.2.2/ooresults/templates/add_class.html`

 * *Files 4% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 $def with (class_, courses)
 
 
 $def format_time(time):
     $if time is not None:
-        $return '{:d}:{:02d}'.format(time//60, time%60)
+        $return minutes_seconds(time)
     $else:
         $return ''
 
 $def format_date(time):
     $if time is not None:
         $return time.strftime('%H:%M:%S')
     $else:
```

#### html2text {}

```diff
@@ -1,13 +1,13 @@
 $def with (class_, courses) $def format_time(time): $if time is not None:
-$return '{:d}:{:02d}'.format(time//60, time%60) $else: $return '' $def
-format_date(time): $if time is not None: $return time.strftime('%H:%M:%S')
-$else: $return '' $def format_int(value): $return str(value) if value is not
-None else '' $def format_voided_legs(legs): $ s = [] $for i in legs: $s.append
-(i[0] + '-' + i[1]) $return ', '.join(s)
+$return minutes_seconds(time) $else: $return '' $def format_date(time): $if
+time is not None: $return time.strftime('%H:%M:%S') $else: $return '' $def
+format_int(value): $return str(value) if value is not None else '' $def
+format_voided_legs(legs): $ s = [] $for i in legs: $s.append(i[0] + '-' + i[1])
+$return ', '.join(s)
 ×
 [$class_.id          ]
 Name *              [$class_.name        ]
 Short name          [$(class_.short_name if class_.short_name is not None else
                     '')]
                     $if class_.course_id is None:
                     $else:
```

### Comparing `ooresults-0.2.1/ooresults/templates/add_club.html` & `ooresults-0.2.2/ooresults/templates/add_club.html`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/ooresults/templates/add_competitor.html` & `ooresults-0.2.2/ooresults/templates/add_competitor.html`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/ooresults/templates/add_course.html` & `ooresults-0.2.2/ooresults/templates/add_course.html`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/ooresults/templates/add_entry.html` & `ooresults-0.2.2/ooresults/templates/add_entry.html`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/ooresults/templates/add_entry_competitors.html` & `ooresults-0.2.2/ooresults/templates/add_entry_competitors.html`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/ooresults/templates/add_entry_result.html` & `ooresults-0.2.2/ooresults/templates/add_entry_result.html`

 * *Files 5% similar despite different names*

```diff
@@ -1,25 +1,19 @@
 $def with (entry)
 
-$def format_time(time):
-    $if time is not None:
-        $return '{:d}:{:02d}'.format(time//60, time%60)
-    $else:
-        $return ''
-
 $def format_date(time):
     $if time is not None:
         $return time.strftime('%H:%M:%S')
     $else:
         $return ''
 
 $def format_diff_time(t):
     $if entry.result.start_time is not None:
         $ diff = t.replace(microsecond=0) - entry.result.start_time.replace(microsecond=0)
-        $return format_time(int(diff.total_seconds()))
+        $return minutes_seconds(int(diff.total_seconds()))
     $else:
         $return ''
 
 
 <!-- Modal content -->
 <div class="modal-content">
     <span class="close" onclick="document.getElementById('entr.resultDialog').style.display='none'">&times;</span>
@@ -56,15 +50,15 @@
             </tr>
             <tr>
                 <th class="input-header"><label>Status</label></th>
                 <td><label>$MAP_STATUS[entry.result.status]</label></td>
             </tr>
             <tr>
                 <th class="input-header"><label>Time</label></th>
-                <td><label>$(format_time(entry.result.extensions.get('running_time', entry.result.time)))</label></td>
+                <td><label>$(minutes_seconds(entry.result.extensions.get('running_time', entry.result.time)))</label></td>
             </tr>
         </table>
             
         <table style="border-collapse: collapse">
             $if entry.result.punched_clear_time is not None or entry.result.punched_check_time is not None or entry.result.punched_start_time is not None or entry.result.punched_finish_time is not None:
                 <thead>
                     <tr><th colspan="2" style="padding-top:2em"></th></tr>
@@ -129,15 +123,15 @@
                             $if punch.get('status', '') in ('OK', 'Missing'):
                                 $ i += 1
                                 <td class="dt" style="text-align:right">$str(i)</td>
                             $else:
                                 <td class="dt" style="text-align:right"></td>
                             <td class="dt" style="text-align:right">$punch.get('control_code', '')</td>
                             <td class="dt" style="text-align:right">$(format_date(punch.get('punch_time', None)))</td>
-                            <td class="dt" style="text-align:right">$(format_time(punch.get('time', None)))</td>
+                            <td class="dt" style="text-align:right">$(minutes_seconds(punch.get('time', None)))</td>
                             <td class="dt">$punch.get('status', '')</td>
                         </tr>
                 </tbody>
         </table>
         <p></p>
         <!--button type="submit" class="btn">Save</button-->
         <button type="button" class="btn cancel" onclick="document.getElementById('entr.resultDialog').style.display='none'">Cancel</button>
```

#### html2text {}

```diff
@@ -1,34 +1,32 @@
-$def with (entry) $def format_time(time): $if time is not None: $return '{:d}:
-{:02d}'.format(time//60, time%60) $else: $return '' $def format_date(time): $if
-time is not None: $return time.strftime('%H:%M:%S') $else: $return '' $def
-format_diff_time(t): $if entry.result.start_time is not None: $ diff =
-t.replace(microsecond=0) - entry.result.start_time.replace(microsecond=0)
-$return format_time(int(diff.total_seconds())) $else: $return ''
+$def with (entry) $def format_date(time): $if time is not None: $return
+time.strftime('%H:%M:%S') $else: $return '' $def format_diff_time(t): $if
+entry.result.start_time is not None: $ diff = t.replace(microsecond=0) -
+entry.result.start_time.replace(microsecond=0) $return minutes_seconds(int
+(diff.total_seconds())) $else: $return ''
 ×
 [$entry.id           ]
 First name  $entry.first_name
 Last name   $entry.last_name
 Year        $entry.year
 Class       $entry.class_
 Chip        $entry.chip
 Start time  $(format_date(entry.result.get('start_time', None)))
 Finish time $(format_date(entry.result.get('finish_time', None)))
 Status      $MAP_STATUS[entry.result.status]
-Time        $(format_time(entry.result.extensions.get('running_time',
+Time        $(minutes_seconds(entry.result.extensions.get('running_time',
             entry.result.time)))
 Number Control Punch time                         Time                               Status
        code
 Clear  Clear   $format_date                       $format_diff_time
                (entry.result.punched_clear_time)  (entry.result.punched_clear_time)
 Check  Check   $format_date                       $format_diff_time
                (entry.result.punched_check_time)  (entry.result.punched_check_time)
 Start  Start   $format_date                       $format_diff_time
                (entry.result.punched_start_time)  (entry.result.punched_start_time)
 Finish Finish  $format_date                       $format_diff_time
                (entry.result.punched_finish_time) (entry.result.punched_finish_time)
-                                                                                     $
-$str                                              $(format_date(punch.get            (format_time $punch.get
-(i)            $punch.get('control_code', '')     ('punch_time', None)))             (punch.get   ('status',
-                                                                                     ('time',     '')
-                                                                                     None)))
+                                                                                     $                $punch.get
+$str           $punch.get('control_code', '')     $(format_date(punch.get            (minutes_seconds ('status',
+(i)                                               ('punch_time', None)))             (punch.get       '')
+                                                                                     ('time', None)))
  Cancel
```

### Comparing `ooresults-0.2.1/ooresults/templates/add_event.html` & `ooresults-0.2.2/ooresults/templates/add_event.html`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/ooresults/templates/classes_tab_content.html` & `ooresults-0.2.2/ooresults/templates/classes_tab_content.html`

 * *Files 2% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 $def with (classes_table)
  
 <!-- Tab content -->
 <div id="Classes" class="tabcontent">
   <div class="actions">
     <!-- Trigger/Open The Modal -->
-    <button id="cls.myBtnReload" onclick="cls_myReload()">Reload</button>
+    <button id="cls.myBtnReload" onclick="cls_update()">Reload</button>
     <button id="cls.myBtnImport" onclick="cls_myImport()">Import ...</button>
     <button id="cls.myBtnExport" onclick="cls_myExport()">Export ...</button>
     <button id="cls.myBtnAdd" onclick="cls_myAdd()">Add class ...</button>
     <button id="cls.myBtnEdit" disabled onclick="cls_myEdit()">Edit class ...</button>
     <button id="cls.myBtnDelete" disabled onclick="cls_myDelete()">Delete class</button>
   </div>
 
@@ -100,34 +100,14 @@
             cls_selected = e.target.parentNode;
             cls_selected.className = 'selected';
             document.getElementById('cls.myBtnEdit').disabled = false;
             document.getElementById('cls.myBtnDelete').disabled = false;
         }
     }
 
-    function cls_myReload() {
-        var data = new FormData();
-        data.append('event_id', window.event_id);
-        var xhr = new XMLHttpRequest();
-        xhr.onreadystatechange = function() {
-            if (this.readyState == 4 && this.status == 200) {
-                entr_updateTable(this.responseText)
-            }
-            if (this.readyState == 4 && this.status == 409) {
-                window.alert(this.responseText);
-            }
-            if (this.readyState == 4 && this.status == 500) {
-                window.alert(this.responseText);
-            }
-        };
-        xhr.open("POST", "class/update", true);
-        xhr.responseType = "html";
-        xhr.send(data);
-    }
-
     function cls_myImport() {
         document.getElementById('cls.importDialog').style.display='block';
         updateDisplayedParams("cls_import");
     }
 
     function cls_myExport() {
         document.getElementById('cls.exportDialog').style.display='block';
```

### Comparing `ooresults-0.2.1/ooresults/templates/classes_table.html` & `ooresults-0.2.2/ooresults/templates/classes_table.html`

 * *Files 5% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 $def with (event, classes)
 
 $ date = event.get('date', '')
 
 $def format_time(time):
     $if time is not None:
-        $return '{:d}:{:02d}'.format(time//60, time%60)
+        $return minutes_seconds(time)
     $else:
         $return ''
 
 $def format_date(time):
     $if time is not None:
         $return time.strftime('%H:%M:%S')
     $else:
```

#### html2text {}

```diff
@@ -1,13 +1,13 @@
 $def with (event, classes) $ date = event.get('date', '') $def format_time
-(time): $if time is not None: $return '{:d}:{:02d}'.format(time//60, time%60)
-$else: $return '' $def format_date(time): $if time is not None: $return
-time.strftime('%H:%M:%S') $else: $return '' $def format_int(value): $return str
-(value) if value is not None else '' $def format_voided_legs(legs): $ s = []
-$for i in legs: $s.append(i[0] + '-' + i[1]) $return ', '.join(s)
+(time): $if time is not None: $return minutes_seconds(time) $else: $return ''
+$def format_date(time): $if time is not None: $return time.strftime('%H:%M:%S')
+$else: $return '' $def format_int(value): $return str(value) if value is not
+None else '' $def format_voided_legs(legs): $ s = [] $for i in legs: $s.append
+(i[0] + '-' + i[1]) $return ', '.join(s)
 Event name: $event.get('name', '')
 Event date: $(date.isoformat() if date != '' else '')
 [                    ]
 Name         Short name         Course         Voided legs                 Type                  Use start control                   Apply handicap                    Mass start         Time limit         Penalty controls     Penalty time limit
              $                  $                                          $({'standard':
              (class_.short_name (class_.course                             'Standard', 'net':    $({'if_punched': 'If punched',      $('Yes' if                        $format_date       $format_time       $format_int          $format_int
 $class_.name if                 if             $format_voided_legs         'Net', 'score':       'no': 'No', 'yes': 'Yes'}.get       class_.params.apply_handicap_rule (class_.params.get (class_.params.get (class_.params.get   (class_.params.get
```

### Comparing `ooresults-0.2.1/ooresults/templates/clubs_tab_content.html` & `ooresults-0.2.2/ooresults/templates/clubs_tab_content.html`

 * *Files 2% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 $def with (clubs_table)
  
 <!-- Tab content -->
 <div id="Clubs" class="tabcontent">
   <div class="actions">
     <!-- Trigger/Open The Modal -->
-    <button id="clb.myBtnReload" onclick="clb_myReload()">Reload</button>
+    <button id="clb.myBtnReload" onclick="clb_update()">Reload</button>
     <button id="clb.myBtnAdd" onclick="clb_myAdd()">Add club ...</button>
     <button id="clb.myBtnEdit" disabled onclick="clb_myEdit()">Edit club ...</button>
     <button id="clb.myBtnDelete" disabled onclick="clb_myDelete()">Delete club</button>
   </div>
 
   <div id=clb.data class="data">
     $:clubs_table
@@ -43,34 +43,14 @@
             clb_selected = e.target.parentNode;
             clb_selected.className = 'selected';
             document.getElementById('clb.myBtnEdit').disabled = false;
             document.getElementById('clb.myBtnDelete').disabled = false;
         }
     }
 
-    function clb_myReload() {
-        var data = new FormData();
-        data.append('event_id', window.event_id);
-        var xhr = new XMLHttpRequest();
-        xhr.onreadystatechange = function() {
-            if (this.readyState == 4 && this.status == 200) {
-                entr_updateTable(this.responseText)
-            }
-            if (this.readyState == 4 && this.status == 409) {
-                window.alert(this.responseText);
-            }
-            if (this.readyState == 4 && this.status == 500) {
-                window.alert(this.responseText);
-            }
-        };
-        xhr.open("POST", "club/update", true);
-        xhr.responseType = "html";
-        xhr.send(data);
-    }
-
     function clb_myAdd() {
         var xhr = new XMLHttpRequest();
         xhr.onreadystatechange = function() {
             if (this.readyState == 4 && this.status == 200) {
                 document.getElementById('clb.addDialog').innerHTML = this.responseText;
                 document.getElementById('clb.addDialog').style.display='block';
                 align_form_table('clb.addFormTable');
```

### Comparing `ooresults-0.2.1/ooresults/templates/competitors_tab_content.html` & `ooresults-0.2.2/ooresults/templates/competitors_tab_content.html`

 * *Files 1% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 $def with (competitors_table)
  
 <!-- Tab content -->
 <div id="Competitors" class="tabcontent">
   <div class="actions">
     <!-- Trigger/Open The Modal -->
-    <button id="comp.myBtnReload" onclick="comp_myReload()">Reload</button>
+    <button id="comp.myBtnReload" onclick="comp_update()">Reload</button>
     <button id="comp.myBtnImport" onclick="comp_myImport()">Import ...</button>
     <button id="comp.myBtnExport" onclick="comp_myExport()">Export ...</button>
     <button id="comp.myBtnAdd" onclick="comp_myAdd()">Add competitor ...</button>
     <button id="comp.myBtnEdit" disabled onclick="comp_myEdit()">Edit competitor ...</button>
     <button id="comp.myBtnDelete" disabled onclick="comp_myDelete()">Delete competitor</button>
   </div>
 
@@ -101,34 +101,14 @@
             comp_selected = e.target.parentNode;
             comp_selected.className = 'selected';
             document.getElementById('comp.myBtnEdit').disabled = false;
             document.getElementById('comp.myBtnDelete').disabled = false;
         }
     }
 
-    function comp_myReload() {
-        var data = new FormData();
-        data.append('event_id', window.event_id);
-        var xhr = new XMLHttpRequest();
-        xhr.onreadystatechange = function() {
-            if (this.readyState == 4 && this.status == 200) {
-                entr_updateTable(this.responseText)
-            }
-            if (this.readyState == 4 && this.status == 409) {
-                window.alert(this.responseText);
-            }
-            if (this.readyState == 4 && this.status == 500) {
-                window.alert(this.responseText);
-            }
-        };
-        xhr.open("POST", "competitor/update", true);
-        xhr.responseType = "html";
-        xhr.send(data);
-    }
-
     function comp_myAdd() {
         var xhr = new XMLHttpRequest();
         xhr.onreadystatechange = function() {
             if (this.readyState == 4 && this.status == 200) {
                 document.getElementById('comp.addDialog').innerHTML = this.responseText;
                 document.getElementById('comp.addDialog').style.display='block';
                 align_form_table('comp.addFormTable');
```

### Comparing `ooresults-0.2.1/ooresults/templates/competitors_table.html` & `ooresults-0.2.2/ooresults/templates/competitors_table.html`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/ooresults/templates/courses_tab_content.html` & `ooresults-0.2.2/ooresults/templates/courses_tab_content.html`

 * *Files 2% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 $def with (courses_table)
  
 <!-- Tab content -->
 <div id="Courses" class="tabcontent">
   <div class="actions">
     <!-- Trigger/Open The Modal -->
-    <button id="cou.myBtnReload" onclick="cou_myReload()">Reload</button>
+    <button id="cou.myBtnReload" onclick="cou_update()">Reload</button>
     <button id="cou.myBtnImport" onclick="cou_myImport()">Import ...</button>
     <button id="cou.myBtnExport" onclick="cou_myExport()">Export ...</button>
     <button id="cou.myBtnAdd" onclick="cou_myAdd()">Add course ...</button>
     <button id="cou.myBtnEdit" disabled onclick="cou_myEdit()">Edit course ...</button>
     <button id="cou.myBtnDelete" disabled onclick="cou_myDelete()">Delete course</button>
   </div>
 
@@ -100,34 +100,14 @@
             cou_selected = e.target.parentNode;
             cou_selected.className = 'selected';
             document.getElementById('cou.myBtnEdit').disabled = false;
             document.getElementById('cou.myBtnDelete').disabled = false;
         }
     }
 
-    function cou_myReload() {
-        var data = new FormData();
-        data.append('event_id', window.event_id);
-        var xhr = new XMLHttpRequest();
-        xhr.onreadystatechange = function() {
-            if (this.readyState == 4 && this.status == 200) {
-                entr_updateTable(this.responseText)
-            }
-            if (this.readyState == 4 && this.status == 409) {
-                window.alert(this.responseText);
-            }
-            if (this.readyState == 4 && this.status == 500) {
-                window.alert(this.responseText);
-            }
-        };
-        xhr.open("POST", "course/update", true);
-        xhr.responseType = "html";
-        xhr.send(data);
-    }
-
     function cou_myImport() {
         document.getElementById('cou.importDialog').style.display='block';
         updateDisplayedParams("cou_import");
     }
 
     function cou_myExport() {
         document.getElementById('cou.exportDialog').style.display='block';
```

### Comparing `ooresults-0.2.1/ooresults/templates/courses_table.html` & `ooresults-0.2.2/ooresults/templates/courses_table.html`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/ooresults/templates/demo_reader.html` & `ooresults-0.2.2/ooresults/templates/demo_reader.html`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/ooresults/templates/entries_tab_content.html` & `ooresults-0.2.2/ooresults/templates/entries_tab_content.html`

 * *Files 2% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 $def with (entries_table)
  
 <!-- Tab content -->
 <div id="Entries" class="tabcontent">
   <div class="actions">
     <!-- Trigger/Open The Modal -->
-    <button id="entr.myBtnReload" onclick="entr_myReload()">Reload</button>
+    <button id="entr.myBtnReload" onclick="entr_update()">Reload</button>
     <button id="entr.myBtnImport" onclick="entr_myImport()">Import ...</button>
     <button id="entr.myBtnExport" onclick="entr_myExport()">Export ...</button>
     <button id="entr.myBtnAdd" onclick="entr_myAdd()">Add entry ...</button>
     <button id="entr.myBtnEdit" disabled onclick="entr_myEdit()">Edit entry ...</button>
     <button id="entr.myBtnDelete" disabled onclick="entr_myDelete()">Delete entry</button>
     <button id="entr.myBtnResult" disabled onclick="entr_myResult()">Show result ...</button>
   </div>
@@ -33,15 +33,15 @@
           <input id="oo_2" name="entr_import" type="radio" value="entr.import.2"
                  onchange="updateDisplayedParams('entr_import')" required checked/>
           <label for="entr.import.2">IOF Interface Standard 3.0 Result List</label>
         </div>
         <div>
           <input id="oo_3" name="entr_import" type="radio" value="entr.import.3"
                  onchange="updateDisplayedParams('entr_import')" required checked/>
-          <label for="entr.import.3">OE2003 csv</label>
+          <label for="entr.import.3">OE2003 csv, OE12 csv</label>
         </div>
         $if EXPERIMENTAL:
           <div>
             <input id="oo_4" name="entr_import" type="radio" value="entr.import.4"
                    onchange="updateDisplayedParams('entr_import')" required/>
             <label for="entr.import.4">Text</label>
           </div>
@@ -106,22 +106,29 @@
           <label for="entr.export.2">IOF Interface Standard 3.0 Result List</label>
         </div>
         <div>
           <input id="oo_3" name="entr_export" type="radio" value="entr.export.3"
                  onchange="updateDisplayedParams('entr_export')" required checked/>
           <label for="entr.export.3">OE2003 csv</label>
         </div>
+        <div>
+          <input id="oo_4" name="entr_export" type="radio" value="entr.export.4"
+                 onchange="updateDisplayedParams('entr_export')" required checked/>
+          <label for="entr.export.4">OE12 csv</label>
+        </div>
         <p>Settings</p>
         <div id="entr_export">
           <div id="entr.export.1" class="params">
           </div>
           <div id="entr.export.2" class="params">
           </div>
           <div id="entr.export.3" class="params">
           </div>
+          <div id="entr.export.4" class="params">
+          </div>
         </div>
         <p></p>
         <p></p>
         <button type="submit" class="btn">Export</button>
         <button type="button" class="btn cancel" onclick="document.getElementById('entr.exportDialog').style.display='none'">Cancel</button>
       </form>
     </div>
@@ -189,34 +196,14 @@
             document.getElementById('entr.myBtnDelete').disabled = false;
             document.getElementById('entr.myBtnResult').disabled = false;
             ln = entr_selected.querySelector('[id="entr_table_lastname"]').innerHTML == '';
             document.getElementById('entr.myBtnEdit').disabled = ln;
         }
     }
 
-    function entr_myReload() {
-        var data = new FormData();
-        data.append('event_id', window.event_id);
-        var xhr = new XMLHttpRequest();
-        xhr.onreadystatechange = function() {
-            if (this.readyState == 4 && this.status == 200) {
-                entr_updateTable(this.responseText)
-            }
-            if (this.readyState == 4 && this.status == 409) {
-                window.alert(this.responseText);
-            }
-            if (this.readyState == 4 && this.status == 500) {
-                window.alert(this.responseText);
-            }
-        };
-        xhr.open("POST", "entry/update", true);
-        xhr.responseType = "html";
-        xhr.send(data);
-    }
-
     function entr_myImport() {
         document.getElementById('entr.importDialog').style.display='block';
         updateDisplayedParams("entr_import");
     }
 
     function entr_myExport() {
         document.getElementById('entr.exportDialog').style.display='block';
@@ -382,14 +369,17 @@
         }
         if (selected == "entr.export.2") {
             filename = "ResultList.xml";
         }
         if (selected == "entr.export.3") {
             filename = "entries.csv";
         }
+        if (selected == "entr.export.4") {
+            filename = "entries.csv";
+        }
         xhr.send(data);
     }
 
     function entr_submitAdd() {
         var form = document.getElementById('entr.formAdd');
         var data = new FormData(form);
         data.append('event_id', window.event_id);
```

#### html2text {}

```diff
@@ -2,28 +2,29 @@
  Reload Import ... Export ... Add entry ... Edit entry ... Delete entry Show
 result ...
 $:entries_table
 ×
 Format
 # IOF Interface Standard 3.0 Entry List
 # IOF Interface Standard 3.0 Result List
-# OE2003 csv
+# OE2003 csv, OE12 csv
 $if EXPERIMENTAL:
 o Text
 Settings
 File [File]
 File [File]
 File [File]
 File [File]
 Import Cancel
 ×
 Format
 # IOF Interface Standard 3.0 Entry List
 # IOF Interface Standard 3.0 Result List
 # OE2003 csv
+# OE12 csv
 Settings
 Export Cancel
 ×
 [id                  ]
 Confirm: Delete the selected entry?
 Delete Cancel
```

### Comparing `ooresults-0.2.1/ooresults/templates/entries_table.html` & `ooresults-0.2.2/ooresults/templates/entries_table.html`

 * *Files 2% similar despite different names*

```diff
@@ -7,15 +7,15 @@
     $if year is not None:
         $return str(year)
     $else:
         $return ''
 
 $def format_time(time):
     $if time is not None:
-        $return '{:d}:{:02d}'.format(time//60, time%60)
+        $return minutes_seconds(time)
     $else:
         $return ''
 
 $def format_date(time):
     $if time is not None:
         $return time.strftime('%H:%M:%S')
     $else:
@@ -47,18 +47,18 @@
                 <th class="dt">First name</th>
                 <th class="dt">Last name</th>
                 <th class="dt">Gender</th>
                 <th class="dt">Year</th>
                 <th class="dt">Chip</th>
                 <th class="dt">Club</th>
                 <th class="dt">Class</th>
+                <th class="dt">&nbsp;&nbsp;NC&nbsp;&nbsp;</th>
                 $if event:
                     $for i in range(len(event.fields)):
                         <th class="dt">$event.fields[i]</th>
-                <th class="dt">&nbsp;&nbsp;NC&nbsp;&nbsp;</th>
                 <th class="dt">Start</th>
                 <th class="dt">Time</th>
                 <th class="dt">Status</th>
             </tr>
         </thead>
         <tbody id="entries_tbody">
         $for competitor in competitors:
```

#### html2text {}

```diff
@@ -1,13 +1,13 @@
 $def with (event, competitors) $ date = event.get('date', '') $def format_year
 (year) -> str: $if year is not None: $return str(year) $else: $return '' $def
-format_time(time): $if time is not None: $return '{:d}:{:02d}'.format(time//60,
-time%60) $else: $return '' $def format_date(time): $if time is not None:
-$return time.strftime('%H:%M:%S') $else: $return ''
+format_time(time): $if time is not None: $return minutes_seconds(time) $else:
+$return '' $def format_date(time): $if time is not None: $return time.strftime
+('%H:%M:%S') $else: $return ''
 Event name: $event.get('name', '')
 Event date: $(date.isoformat() if date != '' else '')
 [                    ]
-First name      Last name       Gender          Year            Chip            Club            Class           $event.fields[i]    NC               Start                          Time                              Status
+First name      Last name       Gender          Year            Chip            Club            Class             NC          $event.fields[i]       Start                          Time                              Status
 $competitor.get $competitor.get                 $format_year                                                    $('X' if                                                                $(format_time
 ('first_name',  ('last_name',   $competitor.get (competitor.get $competitor.get $competitor.get $competitor.get competitor.get    $competitor.fields.get $(format_date                  (competitor.result.extensions.get $MAP_STATUS
 '')             '')             ('gender', '')  ('year', None)) ('chip', '')    ('club', '')    ('class_', '')  ('not_competing', (i, '')                (competitor.start.start_time)) ('running_time',                  [competitor.result.status]
                                                                                                                 False) else '')                                                         competitor.result.time)))
```

### Comparing `ooresults-0.2.1/ooresults/templates/events_tab_content.html` & `ooresults-0.2.2/ooresults/templates/events_tab_content.html`

 * *Files 2% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 $def with (events_table)
  
 <!-- Tab content -->
 <div id="Events" class="tabcontent">
   <div class="actions">
     <!-- Trigger/Open The Modal -->
-    <button id="evnt.myBtnReload" onclick="evnt_myReload()">Reload</button>
+    <button id="evnt.myBtnReload" onclick="evnt_update()">Reload</button>
     <button id="evnt.myBtnAdd" onclick="evnt_myAdd()">Add event ...</button>
     <button id="evnt.myBtnEdit" disabled onclick="evnt_myEdit()">Edit event ...</button>
     <button id="evnt.myBtnDelete" disabled onclick="evnt_myDelete()">Delete event</button>
   </div>
 
   <div id="evnt.results" class="data">
     $:events_table
@@ -57,34 +57,14 @@
             element = document.getElementById('evnt.event_name');
             element.innerHTML = evnt_selected.getElementsByTagName('TD')[0].innerHTML;
             element = document.getElementById('evnt.event_date');
             element.innerHTML = evnt_selected.getElementsByTagName('TD')[1].innerHTML;
         }
     }
 
-    function evnt_myReload() {
-        var data = new FormData();
-        data.append('event_id', window.event_id);
-        var xhr = new XMLHttpRequest();
-        xhr.onreadystatechange = function() {
-            if (this.readyState == 4 && this.status == 200) {
-                entr_updateTable(this.responseText)
-            }
-            if (this.readyState == 4 && this.status == 409) {
-                window.alert(this.responseText);
-            }
-            if (this.readyState == 4 && this.status == 500) {
-                window.alert(this.responseText);
-            }
-        };
-        xhr.open("POST", "event/update", true);
-        xhr.responseType = "html";
-        xhr.send(data);
-    }
-
     function evnt_myAdd() {
         var xhr = new XMLHttpRequest();
         xhr.onreadystatechange = function() {
             if (this.readyState == 4 && this.status == 200) {
                 document.getElementById('evnt.addDialog').innerHTML = this.responseText;
                 document.getElementById('evnt.addDialog').style.display='block';
                 align_form_table('evnt.addFormTable');
```

### Comparing `ooresults-0.2.1/ooresults/templates/events_table.html` & `ooresults-0.2.2/ooresults/templates/events_table.html`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/ooresults/templates/main.html` & `ooresults-0.2.2/ooresults/templates/main.html`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/ooresults/templates/results_tab_content.html` & `ooresults-0.2.2/ooresults/templates/results_tab_content.html`

 * *Files 7% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 $def with (results)
  
 <!-- Tab content -->
 <div id="Results" class="tabcontent">
   <div class="actions">
     <!-- Trigger/Open The Modal -->
-    <button id="res.myBtnReload" onclick="res_myReload()">Reload</button>
+    <button id="res.myBtnReload" onclick="res_update()">Reload</button>
     <button id="res.myBtnPdfResult" onclick="res_myPdfResult()">Print results ...</button>
     <button id="res.myBtnPdfSplittimes" onclick="res_myPdfSplittimes()">Print splittimes ...</button>
   </div>
 
   <div id="res.results" class="data">
     $:results
   </div>
@@ -46,34 +46,14 @@
       </form>
     </div>
   </div>
 
 </div>
 
 <script>
-    function res_myReload() {
-        var data = new FormData();
-        data.append('event_id', window.event_id);
-        var xhr = new XMLHttpRequest();
-        xhr.onreadystatechange = function() {
-            if (this.readyState == 4 && this.status == 200) {
-                entr_updateTable(this.responseText)
-            }
-            if (this.readyState == 4 && this.status == 409) {
-                window.alert(this.responseText);
-            }
-            if (this.readyState == 4 && this.status == 500) {
-                window.alert(this.responseText);
-            }
-        };
-        xhr.open("POST", "result/update", true);
-        xhr.responseType = "html";
-        xhr.send(data);
-    }
-
     function res_myPdfResult() {
         document.getElementById('res.pdfResultDialog').style.display='block';
     }
 
     function res_myPdfSplittimes() {
         document.getElementById('res.pdfSplittimesDialog').style.display='block';
     }
```

### Comparing `ooresults-0.2.1/ooresults/templates/results_table.html` & `ooresults-0.2.2/ooresults/templates/results_table.html`

 * *Files 5% similar despite different names*

```diff
@@ -10,29 +10,29 @@
         $return 'NC'
     $else:
         $return ''
 
 
 $def format_time(time: int, status: ResultStatus) -> str:
     $if status == ResultStatus.OK and time is not None:
-        $return '{:d}:{:02d}'.format(time // 60, time % 60)
+        $return minutes_seconds(time)
     $else:
         $return ''
 
 
 $def format_points(points: float, status: ResultStatus) -> str:
     $if status == ResultStatus.OK and points is not None:
         $return '{:.2f}'.format(points)
     $else:
         $return ''
 
 
 $def format_time_total(time: int, status: ResultStatus, start_time=None) -> str:
     $if status == ResultStatus.OK:
-        $return '{:d}:{:02d}'.format(time // 60, time % 60)
+        $return minutes_seconds(time)
     $elif status == ResultStatus.INACTIVE and start_time is not None:
         $return 'Start at ' + start_time.strftime('%H:%M:%S')
     $else:
         $return MAP_STATUS[status]
 
 
 $def format_points_total(points: float, status: ResultStatus, start_time=None) -> str:
```

#### html2text {}

```diff
@@ -1,27 +1,26 @@
 $def with (event, class_results, columns) $ date = event.get('date', '') $def
 format_rank(rank, not_competing: bool) -> str: $if rank is not None: $return
 str(rank) $elif not_competing: $return 'NC' $else: $return '' $def format_time
 (time: int, status: ResultStatus) -> str: $if status == ResultStatus.OK and
-time is not None: $return '{:d}:{:02d}'.format(time // 60, time % 60) $else:
-$return '' $def format_points(points: float, status: ResultStatus) -> str: $if
-status == ResultStatus.OK and points is not None: $return '{:.2f}'.format
-(points) $else: $return '' $def format_time_total(time: int, status:
-ResultStatus, start_time=None) -> str: $if status == ResultStatus.OK: $return '
-{:d}:{:02d}'.format(time // 60, time % 60) $elif status ==
-ResultStatus.INACTIVE and start_time is not None: $return 'Start at ' +
-start_time.strftime('%H:%M:%S') $else: $return MAP_STATUS[status] $def
-format_points_total(points: float, status: ResultStatus, start_time=None) -
-> str: $if status == ResultStatus.OK: $return '{:.2f}'.format(points) $elif
-status == ResultStatus.INACTIVE and start_time is not None: $return 'Start at '
-+ start_time.strftime('%H:%M:%S') $else: $return MAP_STATUS[status] $def
-voided_legs(ranked_results): $if ranked_results and ranked_results[0]['result']
-is not None: $ voided_legs = ranked_results[0]['result'].voided_legs() $if
-voided_legs: $return ' (Voided legs: ' + ', '.join(voided_legs) + ')' $else:
-$return ''
+time is not None: $return minutes_seconds(time) $else: $return '' $def
+format_points(points: float, status: ResultStatus) -> str: $if status ==
+ResultStatus.OK and points is not None: $return '{:.2f}'.format(points) $else:
+$return '' $def format_time_total(time: int, status: ResultStatus,
+start_time=None) -> str: $if status == ResultStatus.OK: $return minutes_seconds
+(time) $elif status == ResultStatus.INACTIVE and start_time is not None:
+$return 'Start at ' + start_time.strftime('%H:%M:%S') $else: $return MAP_STATUS
+[status] $def format_points_total(points: float, status: ResultStatus,
+start_time=None) -> str: $if status == ResultStatus.OK: $return '{:.2f}'.format
+(points) $elif status == ResultStatus.INACTIVE and start_time is not None:
+$return 'Start at ' + start_time.strftime('%H:%M:%S') $else: $return MAP_STATUS
+[status] $def voided_legs(ranked_results): $if ranked_results and
+ranked_results[0]['result'] is not None: $ voided_legs = ranked_results[0]
+['result'].voided_legs() $if voided_legs: $return ' (Voided legs: ' + ', '.join
+(voided_legs) + ')' $else: $return ''
 Event name: $event.get('name', '')
 Event date: $(date.isoformat() if date != '' else '')
 **** $class_.name$voided_legs(ranked_results) ****
 Rank               Name           Club        Time                  Handicap                      Run time           Score controls                Score overtime                Total score                   Run time                      Penalty controls              Penalty overtime              Total time
                    $result.get                $format_time_total                                                                                                                                                                                                                                         $format_time_total
 $format_rank       ('first_name',             (result                                             $format_time       $format_points                $format_points                $format_points_total          $format_time                  $format_time                  $format_time                  (result
 (result.get        '')            $result.get ['result'].time,      $'{:1.4f}'.format             (result            (result.result.extensions.get (result.result.extensions.get (result.result.extensions.get (result.result.extensions.get (result.result.extensions.get (result.result.extensions.get ['result'].time,
```

### Comparing `ooresults-0.2.1/ooresults/templates/root.html` & `ooresults-0.2.2/ooresults/templates/root.html`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/ooresults/templates/select_event.html` & `ooresults-0.2.2/ooresults/templates/select_event.html`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/ooresults/templates/series_settings.html` & `ooresults-0.2.2/ooresults/templates/series_settings.html`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/ooresults/templates/series_tab_content.html` & `ooresults-0.2.2/ooresults/templates/series_tab_content.html`

 * *Files 6% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 $def with (results)
 
 <!-- Tab content -->
 <div id="Series" class="tabcontent">
   <div class="actions">
     <!-- Trigger/Open The Modal -->
-    <button id="ser.myBtnReload" onclick="ser_myReload()">Reload</button>
+    <button id="ser.myBtnReload" onclick="ser_update()">Reload</button>
     <button id="ser.myBtnSettings" onclick="ser_mySettings()">Settings ...</button>
     <button id="ser.myBtnPdfResult" onclick="ser_myPdfResult()">Print results ...</button>
     <button id="ser.myBtnCsvResult" onclick="ser_myCsvResult()">CSV results ...</button>
   </div>
 
   <div id="ser.results" class="data">
     $:results
@@ -50,34 +50,14 @@
         <button type="button" class="btn cancel" onclick="document.getElementById('ser.csvResultDialog').style.display='none'">Cancel</button>
       </form>
     </div>
   </div>
 </div>
 
 <script>
-    function ser_myReload() {
-        var data = new FormData();
-        data.append('event_id', window.event_id);
-        var xhr = new XMLHttpRequest();
-        xhr.onreadystatechange = function() {
-            if (this.readyState == 4 && this.status == 200) {
-                entr_updateTable(this.responseText)
-            }
-            if (this.readyState == 4 && this.status == 409) {
-                window.alert(this.responseText);
-            }
-            if (this.readyState == 4 && this.status == 500) {
-                window.alert(this.responseText);
-            }
-        };
-        xhr.open("POST", "series/update", true);
-        xhr.responseType = "html";
-        xhr.send(data);
-    }
-
     function ser_mySettings() {
         var xhr = new XMLHttpRequest();
         xhr.onreadystatechange = function() {
             if (this.readyState == 4 && this.status == 200) {
                 document.getElementById('ser.settingsDialog').innerHTML = this.responseText;
                 document.getElementById('ser.settingsDialog').style.display='block';
                 align_form_table('ser.settingsFormTable');
```

### Comparing `ooresults-0.2.1/ooresults/templates/series_table.html` & `ooresults-0.2.2/ooresults/templates/series_table.html`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/ooresults/templates/si/si1_data.html` & `ooresults-0.2.2/ooresults/templates/si/si1_data.html`

 * *Files 12% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 $def with (message)
 
 $code
     def format(status: str, time: int) -> str:
         if status == ResultStatus.OK:
-            return MAP_STATUS[status] + ', {:d}:{:02d} min'.format(time // 60, time % 60)
+            return MAP_STATUS[status] + ', ' + minutes_seconds(time) + ' min'
         else:
             return MAP_STATUS[status]
     
     def background(status: str) -> str:
         if status == ResultStatus.OK:
             return "bgg"
         else:
```

### Comparing `ooresults-0.2.1/ooresults/templates/si/si1_page.html` & `ooresults-0.2.2/ooresults/templates/si/si1_page.html`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/ooresults/templates/si/si2_data.html` & `ooresults-0.2.2/ooresults/templates/si/si2_data.html`

 * *Files 5% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 $def with (status, event, messages)
 
 $ date = event.get('date', '') if event is not None else ''
 
 $code
     def format(time: int) -> str:
         if time is not None and time > 0:
-            return '{:d}:{:02d} min'.format(time // 60, time % 60)
+            return minutes_seconds(time) + ' min'
         else:
             return ''
     
     def color(status: ResultStatus) -> str:
         if status == ResultStatus.OK:
             return '#70ff70'  # green
         elif status in (ResultStatus.MISSING_PUNCH, ResultStatus.DID_NOT_FINISH, ResultStatus.OVER_TIME):
```

#### html2text {}

```diff
@@ -1,15 +1,15 @@
 $def with (status, event, messages) $ date = event.get('date', '') if event is
 not None else '' $code def format(time: int) -> str: if time is not None and
-time > 0: return '{:d}:{:02d} min'.format(time // 60, time % 60) else: return
-'' def color(status: ResultStatus) -> str: if status == ResultStatus.OK: return
-'#70ff70' # green elif status in (ResultStatus.MISSING_PUNCH,
-ResultStatus.DID_NOT_FINISH, ResultStatus.OVER_TIME): return '#ff7070' # red
-else: return '#ffff00' # yellow def format_cardreader_status(status: str) -
-> str: if status is None or status == 'offline': return '
+time > 0: return minutes_seconds(time) + ' min' else: return '' def color
+(status: ResultStatus) -> str: if status == ResultStatus.OK: return '#70ff70' #
+green elif status in (ResultStatus.MISSING_PUNCH, ResultStatus.DID_NOT_FINISH,
+ResultStatus.OVER_TIME): return '#ff7070' # red else: return '#ffff00' # yellow
+def format_cardreader_status(status: str) -> str: if status is None or status
+== 'offline': return '
 Card reader offline
 ' elif status in ['readerConnected', 'cardRead', 'cardRemoved']: return '
 Card reader connected
 ' elif status in ['online', 'readerDisconnected']: return '
 Card reader disconnected
 ' elif status == 'cardInserted': return '
 Reading card
```

### Comparing `ooresults-0.2.1/ooresults/templates/si/si2_page.html` & `ooresults-0.2.2/ooresults/templates/si/si2_page.html`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/ooresults/user.py` & `ooresults-0.2.2/ooresults/user.py`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/ooresults/utils/__init__.py` & `ooresults-0.2.2/ooresults/utils/__init__.py`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/ooresults/websocket_server/__init__.py` & `ooresults-0.2.2/ooresults/websocket_server/__init__.py`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/ooresults/websocket_server/si.py` & `ooresults-0.2.2/ooresults/websocket_server/si.py`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/ooresults/websocket_server/websocket_handler.py` & `ooresults-0.2.2/ooresults/websocket_server/websocket_handler.py`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/ooresults/websocket_server/websocket_server.py` & `ooresults-0.2.2/ooresults/websocket_server/websocket_server.py`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/ooresults.egg-info/PKG-INFO` & `ooresults-0.2.2/ooresults.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: ooresults
-Version: 0.2.1
+Version: 0.2.2
 Summary: A software for the evaluation of the results of orienteering events
 Author: Rainer Garus
 License:                     GNU AFFERO GENERAL PUBLIC LICENSE
                                Version 3, 19 November 2007
         
          Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
          Everyone is permitted to copy and distribute verbatim copies
```

### Comparing `ooresults-0.2.1/ooresults.egg-info/SOURCES.txt` & `ooresults-0.2.2/ooresults.egg-info/SOURCES.txt`

 * *Files 1% similar despite different names*

```diff
@@ -39,14 +39,15 @@
 ooresults/pdf/fonts/Carlito-Regular.ttf
 ooresults/plugins/__init__.py
 ooresults/plugins/iof_class_list.py
 ooresults/plugins/iof_competitor_list.py
 ooresults/plugins/iof_course_data.py
 ooresults/plugins/iof_entry_list.py
 ooresults/plugins/iof_result_list.py
+ooresults/plugins/oe12.py
 ooresults/plugins/oe2003.py
 ooresults/plugins/imports/entries/__init__.py
 ooresults/plugins/imports/entries/text.py
 ooresults/repo/__init__.py
 ooresults/repo/class_params.py
 ooresults/repo/repo.py
 ooresults/repo/result_type.py
@@ -106,14 +107,15 @@
 tests/__init__.py
 tests/competitor.py
 tests/entry.py
 tests/test_compute_result_net.py
 tests/test_compute_result_score.py
 tests/test_compute_result_standard.py
 tests/test_configuration.py
+tests/test_globals.py
 tests/test_handicap.py
 tests/test_ranking.py
 tests/test_series.py
 tests/test_user.py
 tests/model/__init__.py
 tests/model/test_courses.py
 tests/model/test_parse_cardreader_log.py
```

### Comparing `ooresults-0.2.1/pyproject.toml` & `ooresults-0.2.2/pyproject.toml`

 * *Files 0% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 [build-system]
 requires = ["setuptools"]
 build-backend = "setuptools.build_meta"
 
 [project]
 name = "ooresults"
-version = "0.2.1"
+version = "0.2.2"
 authors = [
   {name="Rainer Garus"},
 ]
 description = "A software for the evaluation of the results of orienteering events"
 readme = "README.rst"
 license = {file = "LICENSE"}
 requires-python = ">=3.8"
```

### Comparing `ooresults-0.2.1/setup.cfg` & `ooresults-0.2.2/setup.cfg`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/tests/__init__.py` & `ooresults-0.2.2/tests/__init__.py`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/tests/competitor.py` & `ooresults-0.2.2/tests/competitor.py`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/tests/entry.py` & `ooresults-0.2.2/tests/entry.py`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/tests/model/__init__.py` & `ooresults-0.2.2/tests/model/__init__.py`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/tests/model/test_courses.py` & `ooresults-0.2.2/tests/model/test_courses.py`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/tests/model/test_parse_cardreader_log.py` & `ooresults-0.2.2/tests/model/test_parse_cardreader_log.py`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/tests/model/test_store_cardreader_result.py` & `ooresults-0.2.2/tests/model/test_store_cardreader_result.py`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/tests/plugins/test_export_competitors_oe2003.py` & `ooresults-0.2.2/tests/plugins/test_export_competitors_oe2003.py`

 * *Files 1% similar despite different names*

```diff
@@ -167,20 +167,23 @@
 
 def test_class():
     content = oe2003.create(
         entries=[
             Entry(first_name="a", last_name="b", class_id=1, class_="Class_1"),
             Entry(first_name="c", last_name="d", class_id=2, class_="Class_2"),
         ],
-        class_list=[],
+        class_list=[
+            {"id": 1, "name": "Class_1", "short_name": ""},
+            {"id": 2, "name": "Class_2", "short_name": ""},
+        ],
     )
     v1 = (
-        "1;;;b;a;;;;0;;;;;;;;;;Class_1;Class_1"
+        "1;;;b;a;;;;0;;;;;;;;;1;Class_1;Class_1"
         + "\r\n"
-        + "2;;;d;c;;;;0;;;;;;;;;;Class_2;Class_2"
+        + "2;;;d;c;;;;0;;;;;;;;;2;Class_2;Class_2"
         + "\r\n"
     )
 
     assert content == bytes(header + "\r\n" + v1, encoding=encoding)
 
 
 def test_class_short_name():
@@ -265,17 +268,17 @@
         entries=[
             Entry(first_name="a", last_name="b", result=PersonRaceResult(time=301)),
             Entry(first_name="c", last_name="d", result=PersonRaceResult(time=8000)),
         ],
         class_list=[],
     )
     v1 = (
-        "1;;;b;a;;;;0;;;5:01;;;;;;;;"
+        "1;;;b;a;;;;0;;;00:05:01;;;;;;;;"
         + "\r\n"
-        + "2;;;d;c;;;;0;;;133:20;;;;;;;;"
+        + "2;;;d;c;;;;0;;;02:13:20;;;;;;;;"
         + "\r\n"
     )
 
     assert content == bytes(header + "\r\n" + v1, encoding=encoding)
 
 
 def test_status_ok():
```

### Comparing `ooresults-0.2.1/tests/plugins/test_import_competitors_oe2003.py` & `ooresults-0.2.2/tests/plugins/test_import_competitors_oe2003.py`

 * *Files 3% similar despite different names*

```diff
@@ -34,21 +34,22 @@
     "Ziel",
     "Zeit",
     "G",
     "Jg",
     "AK",
     "Wertung",
     "Lang",
+    "Abk",
     "Ort",
 ]
 tz = datetime.now(timezone.utc).astimezone().tzinfo
 
 
 def test_separator_comma():
-    value = "c,v,n,,,,,,,,,"
+    value = "c,v,n,,,,,,,,,,"
     content = bytes(",".join(header) + "\n" + value, encoding="utf-8")
     assert parse(content) == [
         {
             "first_name": "v",
             "last_name": "n",
             "class_": "",
             "club": "",
@@ -61,15 +62,15 @@
             ),
             "start": start_type.PersonRaceStart(),
         }
     ]
 
 
 def test_separator_semicolon():
-    value = "c;v;n;;;;;;;;;"
+    value = "c;v;n;;;;;;;;;;"
     content = bytes(";".join(header) + "\n" + value, encoding="utf-8")
     assert parse(content) == [
         {
             "first_name": "v",
             "last_name": "n",
             "class_": "",
             "club": "",
@@ -82,15 +83,15 @@
             ),
             "start": start_type.PersonRaceStart(),
         }
     ]
 
 
 def test_separator_tab():
-    value = "c\tv\tn\t\t\t\t\t\t\t\t\t"
+    value = "c\tv\tn\t\t\t\t\t\t\t\t\t\t"
     content = bytes("\t".join(header) + "\n" + value, encoding="utf-8")
     assert parse(content) == [
         {
             "first_name": "v",
             "last_name": "n",
             "class_": "",
             "club": "",
@@ -103,15 +104,15 @@
             ),
             "start": start_type.PersonRaceStart(),
         }
     ]
 
 
 def test_quoted_data():
-    value = '"c","v","n","","","","","","","","",""'
+    value = '"c","v","n","","","","","","","","","",""'
     content = bytes(",".join(header) + "\n" + value, encoding="utf-8")
     assert parse(content) == [
         {
             "first_name": "v",
             "last_name": "n",
             "class_": "",
             "club": "",
@@ -124,15 +125,15 @@
             ),
             "start": start_type.PersonRaceStart(),
         }
     ]
 
 
 def test_quote_within_quotes():
-    value = 'c,v,"n1""2",,,,,,,,,'
+    value = 'c,v,"n1""2",,,,,,,,,,'
     content = bytes(",".join(header) + "\n" + value, encoding="utf-8")
     assert parse(content) == [
         {
             "first_name": "v",
             "last_name": 'n1"2',
             "class_": "",
             "club": "",
@@ -145,15 +146,15 @@
             ),
             "start": start_type.PersonRaceStart(),
         }
     ]
 
 
 def test_separator_within_quotes():
-    value = 'c,v,"n1,2",,,,,,,,,'
+    value = 'c,v,"n1,2",,,,,,,,,,'
     content = bytes(",".join(header) + "\n" + value, encoding="utf-8")
     assert parse(content) == [
         {
             "first_name": "v",
             "last_name": "n1,2",
             "class_": "",
             "club": "",
@@ -166,15 +167,15 @@
             ),
             "start": start_type.PersonRaceStart(),
         }
     ]
 
 
 def test_newline_within_quotes():
-    value = 'c,v,"n1\n2",,,,,,,,,'
+    value = 'c,v,"n1\n2",,,,,,,,,,'
     content = bytes(",".join(header) + "\n" + value, encoding="utf-8")
     assert parse(content) == [
         {
             "first_name": "v",
             "last_name": "n1\n2",
             "class_": "",
             "club": "",
@@ -187,15 +188,15 @@
             ),
             "start": start_type.PersonRaceStart(),
         }
     ]
 
 
 def test_status_ok_and_defined_time():
-    value = "c,v,n,,,0:10,,,,0,,"
+    value = "c,v,n,,,0:10,,,,0,,,"
     content = bytes(",".join(header) + "\n" + value, encoding="utf-8")
     assert parse(content) == [
         {
             "first_name": "v",
             "last_name": "n",
             "class_": "",
             "club": "",
@@ -206,15 +207,15 @@
             "result": result_type.PersonRaceResult(status=ResultStatus.OK, time=10),
             "start": start_type.PersonRaceStart(),
         }
     ]
 
 
 def test_status_ok_but_no_time():
-    value = "c,v,n,,,,,,,0,,"
+    value = "c,v,n,,,,,,,0,,,"
     content = bytes(",".join(header) + "\n" + value, encoding="utf-8")
     assert parse(content) == [
         {
             "first_name": "v",
             "last_name": "n",
             "class_": "",
             "club": "",
@@ -227,15 +228,15 @@
             ),
             "start": start_type.PersonRaceStart(),
         }
     ]
 
 
 def test_status_dns():
-    value = "c,v,n,,,,,,,1,,"
+    value = "c,v,n,,,,,,,1,,,"
     content = bytes(",".join(header) + "\n" + value, encoding="utf-8")
     assert parse(content) == [
         {
             "first_name": "v",
             "last_name": "n",
             "class_": "",
             "club": "",
@@ -248,15 +249,15 @@
             ),
             "start": start_type.PersonRaceStart(),
         }
     ]
 
 
 def test_status_dnf():
-    value = "c,v,n,,,,,,,2,,"
+    value = "c,v,n,,,,,,,2,,,"
     content = bytes(",".join(header) + "\n" + value, encoding="utf-8")
     assert parse(content) == [
         {
             "first_name": "v",
             "last_name": "n",
             "class_": "",
             "club": "",
@@ -269,15 +270,15 @@
             ),
             "start": start_type.PersonRaceStart(),
         }
     ]
 
 
 def test_status_mp():
-    value = "c,v,n,,,,,,,3,,"
+    value = "c,v,n,,,,,,,3,,,"
     content = bytes(",".join(header) + "\n" + value, encoding="utf-8")
     assert parse(content) == [
         {
             "first_name": "v",
             "last_name": "n",
             "class_": "",
             "club": "",
@@ -290,15 +291,15 @@
             ),
             "start": start_type.PersonRaceStart(),
         }
     ]
 
 
 def test_status_disq():
-    value = "c,v,n,,,,,,,4,,"
+    value = "c,v,n,,,,,,,4,,,"
     content = bytes(",".join(header) + "\n" + value, encoding="utf-8")
     assert parse(content) == [
         {
             "first_name": "v",
             "last_name": "n",
             "class_": "",
             "club": "",
@@ -311,15 +312,15 @@
             ),
             "start": start_type.PersonRaceStart(),
         }
     ]
 
 
 def test_status_over_time():
-    value = "c,v,n,,,,,,,5,,"
+    value = "c,v,n,,,,,,,5,,,"
     content = bytes(",".join(header) + "\n" + value, encoding="utf-8")
     assert parse(content) == [
         {
             "first_name": "v",
             "last_name": "n",
             "class_": "",
             "club": "",
@@ -332,15 +333,15 @@
             ),
             "start": start_type.PersonRaceStart(),
         }
     ]
 
 
 def test_gender_male():
-    value = "c,v,n,,,,M,,,4,,"
+    value = "c,v,n,,,,M,,,4,,,"
     content = bytes(",".join(header) + "\n" + value, encoding="utf-8")
     assert parse(content) == [
         {
             "first_name": "v",
             "last_name": "n",
             "class_": "",
             "club": "",
@@ -353,15 +354,15 @@
             ),
             "start": start_type.PersonRaceStart(),
         }
     ]
 
 
 def test_gender_female():
-    value = "c,v,n,,,,F,,,4,,"
+    value = "c,v,n,,,,F,,,4,,,"
     content = bytes(",".join(header) + "\n" + value, encoding="utf-8")
     assert parse(content) == [
         {
             "first_name": "v",
             "last_name": "n",
             "class_": "",
             "club": "",
@@ -373,16 +374,60 @@
                 status=ResultStatus.DISQUALIFIED, time=None
             ),
             "start": start_type.PersonRaceStart(),
         }
     ]
 
 
+def test_club_name():
+    value = "c,v,n,,,,F,,,4,,OC Red,OC Green"
+    content = bytes(",".join(header) + "\n" + value, encoding="utf-8")
+    assert parse(content) == [
+        {
+            "first_name": "v",
+            "last_name": "n",
+            "class_": "",
+            "club": "OC Green",
+            "chip": "c",
+            "gender": "F",
+            "year": None,
+            "not_competing": False,
+            "result": result_type.PersonRaceResult(
+                status=ResultStatus.DISQUALIFIED, time=None
+            ),
+            "start": start_type.PersonRaceStart(),
+        }
+    ]
+
+
+# orienteeringonline.net uses another column for the club name,
+# but in opposite to oe2003 is does not write gender data
+def test_club_name_if_no_gender_is_defined():
+    value = "c,v,n,,,,,,,4,,OC Red,OC Green"
+    content = bytes(",".join(header) + "\n" + value, encoding="utf-8")
+    assert parse(content) == [
+        {
+            "first_name": "v",
+            "last_name": "n",
+            "class_": "",
+            "club": "OC Red",
+            "chip": "c",
+            "gender": "",
+            "year": None,
+            "not_competing": False,
+            "result": result_type.PersonRaceResult(
+                status=ResultStatus.DISQUALIFIED, time=None
+            ),
+            "start": start_type.PersonRaceStart(),
+        }
+    ]
+
+
 def test_year2():
-    value = "c,v,n,,,,,15,,4,,"
+    value = "c,v,n,,,,,15,,4,,,"
     content = bytes(",".join(header) + "\n" + value, encoding="utf-8")
     assert parse(content) == [
         {
             "first_name": "v",
             "last_name": "n",
             "class_": "",
             "club": "",
@@ -395,15 +440,15 @@
             ),
             "start": start_type.PersonRaceStart(),
         }
     ]
 
 
 def test_year4():
-    value = "c,v,n,,,,,1915,,4,,"
+    value = "c,v,n,,,,,1915,,4,,,"
     content = bytes(",".join(header) + "\n" + value, encoding="utf-8")
     assert parse(content) == [
         {
             "first_name": "v",
             "last_name": "n",
             "class_": "",
             "club": "",
@@ -416,15 +461,15 @@
             ),
             "start": start_type.PersonRaceStart(),
         }
     ]
 
 
 def test_not_competing_is_false():
-    value = "c,v,n,,,,,,0,4,,"
+    value = "c,v,n,,,,,,0,4,,,"
     content = bytes(",".join(header) + "\n" + value, encoding="utf-8")
     assert parse(content) == [
         {
             "first_name": "v",
             "last_name": "n",
             "class_": "",
             "club": "",
@@ -437,15 +482,15 @@
             ),
             "start": start_type.PersonRaceStart(),
         }
     ]
 
 
 def test_not_competing_is_true():
-    value = "c,v,n,,,,,,X,4,,"
+    value = "c,v,n,,,,,,X,4,,,"
     content = bytes(",".join(header) + "\n" + value, encoding="utf-8")
     assert parse(content) == [
         {
             "first_name": "v",
             "last_name": "n",
             "class_": "",
             "club": "",
@@ -458,15 +503,15 @@
             ),
             "start": start_type.PersonRaceStart(),
         }
     ]
 
 
 def test_start_time():
-    value = "c,v,n,14:05:00,,,,,,,,"
+    value = "c,v,n,14:05:00,,,,,,,,,"
     content = bytes(",".join(header) + "\n" + value, encoding="utf-8")
     assert parse(content) == [
         {
             "first_name": "v",
             "last_name": "n",
             "class_": "",
             "club": "",
@@ -481,15 +526,15 @@
                 start_time=datetime(1900, 1, 1, 14, 5, 0)
             ),
         }
     ]
 
 
 def test_relative_start_time_h_m_s():
-    value = "c,v,n,4:05:00,,,,,,,,"
+    value = "c,v,n,4:05:00,,,,,,,,,"
     content = bytes(",".join(header) + "\n" + value, encoding="utf-8")
     assert parse(content) == [
         {
             "first_name": "v",
             "last_name": "n",
             "class_": "",
             "club": "",
@@ -504,15 +549,15 @@
                 start_time=datetime(1900, 1, 1, 4, 5, 0)
             ),
         }
     ]
 
 
 def test_relative_start_time_m_s():
-    value = "c,v,n,245:02,,,,,,,,"
+    value = "c,v,n,245:02,,,,,,,,,"
     content = bytes(",".join(header) + "\n" + value, encoding="utf-8")
     assert parse(content) == [
         {
             "first_name": "v",
             "last_name": "n",
             "class_": "",
             "club": "",
@@ -527,15 +572,15 @@
                 start_time=datetime(1900, 1, 1, 4, 5, 2)
             ),
         }
     ]
 
 
 def test_finish_time():
-    value = "c,v,n,,18:59:12,,,,,,,"
+    value = "c,v,n,,18:59:12,,,,,,,,"
     content = bytes(",".join(header) + "\n" + value, encoding="utf-8")
     assert parse(content) == [
         {
             "first_name": "v",
             "last_name": "n",
             "class_": "",
             "club": "",
@@ -551,15 +596,15 @@
             ),
             "start": start_type.PersonRaceStart(),
         }
     ]
 
 
 def test_relative_finish_time_h_m_s():
-    value = "c,v,n,,1:59:12,,,,,,,"
+    value = "c,v,n,,1:59:12,,,,,,,,"
     content = bytes(",".join(header) + "\n" + value, encoding="utf-8")
     assert parse(content) == [
         {
             "first_name": "v",
             "last_name": "n",
             "class_": "",
             "club": "",
@@ -575,15 +620,15 @@
             ),
             "start": start_type.PersonRaceStart(),
         }
     ]
 
 
 def test_relative_finish_time_m_s():
-    value = "c,v,n,,299:12,,,,,,,"
+    value = "c,v,n,,299:12,,,,,,,,"
     content = bytes(",".join(header) + "\n" + value, encoding="utf-8")
     assert parse(content) == [
         {
             "first_name": "v",
             "last_name": "n",
             "class_": "",
             "club": "",
@@ -599,15 +644,15 @@
             ),
             "start": start_type.PersonRaceStart(),
         }
     ]
 
 
 def test_start_and_finish_time():
-    value = "c,v,n,14:05:00,14:36:11,,,,,,,"
+    value = "c,v,n,14:05:00,14:36:11,,,,,,,,"
     content = bytes(",".join(header) + "\n" + value, encoding="utf-8")
     assert parse(content) == [
         {
             "first_name": "v",
             "last_name": "n",
             "class_": "",
             "club": "",
@@ -627,15 +672,15 @@
                 start_time=datetime(1900, 1, 1, 14, 5, 0)
             ),
         }
     ]
 
 
 def test_start_time_and_status_mp():
-    value = "c,v,n,14:05:00,,,,,,3,,"
+    value = "c,v,n,14:05:00,,,,,,3,,,"
     content = bytes(",".join(header) + "\n" + value, encoding="utf-8")
     assert parse(content) == [
         {
             "first_name": "v",
             "last_name": "n",
             "class_": "",
             "club": "",
@@ -653,15 +698,15 @@
                 start_time=datetime(1900, 1, 1, 14, 5, 0)
             ),
         }
     ]
 
 
 def test_start_time_and_status_dnf():
-    value = "c,v,n,14:05:00,,,,,,2,,"
+    value = "c,v,n,14:05:00,,,,,,2,,,"
     content = bytes(",".join(header) + "\n" + value, encoding="utf-8")
     assert parse(content) == [
         {
             "first_name": "v",
             "last_name": "n",
             "class_": "",
             "club": "",
@@ -679,15 +724,15 @@
                 start_time=datetime(1900, 1, 1, 14, 5, 0)
             ),
         }
     ]
 
 
 def test_start_time_and_status_over_time():
-    value = "c,v,n,14:05:00,,,,,,5,,"
+    value = "c,v,n,14:05:00,,,,,,5,,,"
     content = bytes(",".join(header) + "\n" + value, encoding="utf-8")
     assert parse(content) == [
         {
             "first_name": "v",
             "last_name": "n",
             "class_": "",
             "club": "",
@@ -705,15 +750,15 @@
                 start_time=datetime(1900, 1, 1, 14, 5, 0)
             ),
         }
     ]
 
 
 def test_split_time():
-    value = "c,v,n,,,,,,,,,,123,4:16"
+    value = "c,v,n,,,,,,,,,,,123,4:16"
     content = bytes(
         ",".join(header + ["Posten1,Punch1"]) + "\n" + value, encoding="utf-8"
     )
     assert parse(content) == [
         {
             "first_name": "v",
             "last_name": "n",
@@ -731,15 +776,15 @@
             ),
             "start": start_type.PersonRaceStart(),
         }
     ]
 
 
 def test_split_time_without_punch():
-    value = "c,v,n,,,,,,,,,,123,-----"
+    value = "c,v,n,,,,,,,,,,,123,-----"
     content = bytes(
         ",".join(header + ["Posten1,Punch1"]) + "\n" + value, encoding="utf-8"
     )
     assert parse(content) == [
         {
             "first_name": "v",
             "last_name": "n",
@@ -759,15 +804,15 @@
             ),
             "start": start_type.PersonRaceStart(),
         }
     ]
 
 
 def test_two_split_times():
-    value = "c,v,n,,,,,,,,,,123,4:16,99,12:01"
+    value = "c,v,n,,,,,,,,,,,123,4:16,99,12:01"
     content = bytes(
         ",".join(header + ["Posten1,Punch1"]) + "\n" + value, encoding="utf-8"
     )
     assert parse(content) == [
         {
             "first_name": "v",
             "last_name": "n",
@@ -786,15 +831,15 @@
             ),
             "start": start_type.PersonRaceStart(),
         }
     ]
 
 
 def test_split_times_with_closing_separator():
-    value = "c,v,n,,,,,,,,,,123,4:16,99,12:01,"
+    value = "c,v,n,,,,,,,,,,,123,4:16,99,12:01,"
     content = bytes(
         ",".join(header + ["Posten1,Punch1"]) + "\n" + value, encoding="utf-8"
     )
     assert parse(content) == [
         {
             "first_name": "v",
             "last_name": "n",
@@ -813,17 +858,17 @@
             ),
             "start": start_type.PersonRaceStart(),
         }
     ]
 
 
 def test_import_several_lines():
-    value_1 = "c1,v1,n1,,,0:11,,,,0,,"
-    value_2 = "c2,v2,n2,,,0:12,,,,0,,"
-    value_3 = "c3,v3,n3,,,0:13,,,,0,,"
+    value_1 = "c1,v1,n1,,,0:11,,,,0,,,"
+    value_2 = "c2,v2,n2,,,0:12,,,,0,,,"
+    value_3 = "c3,v3,n3,,,0:13,,,,0,,,"
     content = bytes(
         ",".join(header) + "\n" + value_1 + "\n" + value_2 + "\n" + value_3,
         encoding="utf-8",
     )
     assert parse(content) == [
         {
             "first_name": "v1",
@@ -861,17 +906,17 @@
             "result": result_type.PersonRaceResult(status=ResultStatus.OK, time=13),
             "start": start_type.PersonRaceStart(),
         },
     ]
 
 
 def test_do_not_import_special_names():
-    value_1 = "c1,,Vacant,,,0:11,,,,0,,"
-    value_2 = "c2,v2,n2,,,0:12,,,,0,,"
-    value_3 = "c3,,Reserve,,,0:13,,,,0,,"
+    value_1 = "c1,,Vacant,,,0:11,,,,0,,,"
+    value_2 = "c2,v2,n2,,,0:12,,,,0,,,"
+    value_3 = "c3,,Reserve,,,0:13,,,,0,,,"
     content = bytes(
         ",".join(header) + "\n" + value_1 + "\n" + value_2 + "\n" + value_3,
         encoding="utf-8",
     )
     assert parse(content) == [
         {
             "first_name": "v2",
@@ -885,17 +930,17 @@
             "result": result_type.PersonRaceResult(status=ResultStatus.OK, time=12),
             "start": start_type.PersonRaceStart(),
         }
     ]
 
 
 def test_import_extra_fields():
-    value_1 = "c1,v1,n1,,,0:11,,,,0,,,A,B,C"
-    value_2 = "c2,v2,n2,,,0:12,,,,0,,,,X,"
-    value_3 = "c3,v3,n3,,,0:13,,,,0,,,,Y,Z"
+    value_1 = "c1,v1,n1,,,0:11,,,,0,,,,A,B,C"
+    value_2 = "c2,v2,n2,,,0:12,,,,0,,,,,X,"
+    value_3 = "c3,v3,n3,,,0:13,,,,0,,,,,Y,Z"
     content = bytes(
         ",".join(header + ["Text1", "Text2", "Text3"])
         + "\n"
         + value_1
         + "\n"
         + value_2
         + "\n"
```

### Comparing `ooresults-0.2.1/tests/plugins/test_plugin_iof_class_list.py` & `ooresults-0.2.2/tests/plugins/test_plugin_iof_class_list.py`

 * *Files 2% similar despite different names*

```diff
@@ -60,15 +60,15 @@
         },
     ]
 
 
 def test_export_class_list():
     content = """\
 <?xml version='1.0' encoding='UTF-8'?>
-<ClassList xmlns="http://www.orienteering.org/datastandard/3.0" iofVersion="3.0">
+<ClassList xmlns="http://www.orienteering.org/datastandard/3.0" iofVersion="3.0" creator="ooresults (https://pypi.org/project/ooresults)">
   <Class>
     <Name>D 14-15</Name>
   </Class>
   <Class>
     <Name>H 14-15</Name>
   </Class>
   <Class>
```

### Comparing `ooresults-0.2.1/tests/plugins/test_plugin_iof_competitor_list.py` & `ooresults-0.2.2/tests/plugins/test_plugin_iof_competitor_list.py`

 * *Files 3% similar despite different names*

```diff
@@ -48,15 +48,15 @@
         }
     ]
 
 
 def test_export_name():
     content = """\
 <?xml version='1.0' encoding='UTF-8'?>
-<CompetitorList xmlns="http://www.orienteering.org/datastandard/3.0" iofVersion="3.0">
+<CompetitorList xmlns="http://www.orienteering.org/datastandard/3.0" iofVersion="3.0" creator="ooresults (https://pypi.org/project/ooresults)">
   <Competitor>
     <Person>
       <Name>
         <Family>Merkel</Family>
         <Given>Angela</Given>
       </Name>
     </Person>
@@ -106,15 +106,15 @@
         }
     ]
 
 
 def test_export_full():
     content = """\
 <?xml version='1.0' encoding='UTF-8'?>
-<CompetitorList xmlns="http://www.orienteering.org/datastandard/3.0" iofVersion="3.0">
+<CompetitorList xmlns="http://www.orienteering.org/datastandard/3.0" iofVersion="3.0" creator="ooresults (https://pypi.org/project/ooresults)">
   <Competitor>
     <Person sex="F">
       <Name>
         <Family>Merkel</Family>
         <Given>Angela</Given>
       </Name>
       <BirthDate>1972-01-01</BirthDate>
```

### Comparing `ooresults-0.2.1/tests/plugins/test_plugin_iof_course_data.py` & `ooresults-0.2.2/tests/plugins/test_plugin_iof_course_data.py`

 * *Files 1% similar despite different names*

```diff
@@ -194,15 +194,15 @@
         },
     ]
 
 
 def test_export_course_data():
     content = """\
 <?xml version='1.0' encoding='UTF-8'?>
-<CourseData xmlns="http://www.orienteering.org/datastandard/3.0" iofVersion="3.0">
+<CourseData xmlns="http://www.orienteering.org/datastandard/3.0" iofVersion="3.0" creator="ooresults (https://pypi.org/project/ooresults)">
   <Event>
     <Name>1. O-Cup 2020</Name>
     <StartTime>
       <Date>2020-02-09</Date>
     </StartTime>
   </Event>
   <RaceCourseData>
@@ -276,15 +276,15 @@
     )
     assert document == bytes(content, encoding="utf-8")
 
 
 def test_export_course_data_with_class_assignment():
     content = """\
 <?xml version='1.0' encoding='UTF-8'?>
-<CourseData xmlns="http://www.orienteering.org/datastandard/3.0" iofVersion="3.0">
+<CourseData xmlns="http://www.orienteering.org/datastandard/3.0" iofVersion="3.0" creator="ooresults (https://pypi.org/project/ooresults)">
   <Event>
     <Name>1. O-Cup 2020</Name>
     <StartTime>
       <Date>2020-02-09</Date>
     </StartTime>
   </Event>
   <RaceCourseData>
```

### Comparing `ooresults-0.2.1/tests/plugins/test_plugin_iof_entry_list.py` & `ooresults-0.2.2/tests/plugins/test_plugin_iof_entry_list.py`

 * *Files 4% similar despite different names*

```diff
@@ -69,15 +69,15 @@
         },
     ]
 
 
 def test_export_entry_list_with_one_entry():
     content = """\
 <?xml version='1.0' encoding='UTF-8'?>
-<EntryList xmlns="http://www.orienteering.org/datastandard/3.0" iofVersion="3.0">
+<EntryList xmlns="http://www.orienteering.org/datastandard/3.0" iofVersion="3.0" creator="ooresults (https://pypi.org/project/ooresults)">
   <Event>
     <Name>1. O-Cup 2020</Name>
     <StartTime>
       <Date>2020-02-09</Date>
     </StartTime>
   </Event>
   <PersonEntry>
@@ -138,15 +138,15 @@
     }
     assert entries == []
 
 
 def test_export_entry_list_without_person_entries():
     content = """\
 <?xml version='1.0' encoding='UTF-8'?>
-<EntryList xmlns="http://www.orienteering.org/datastandard/3.0" iofVersion="3.0">
+<EntryList xmlns="http://www.orienteering.org/datastandard/3.0" iofVersion="3.0" creator="ooresults (https://pypi.org/project/ooresults)">
   <Event>
     <Name>1. O-Cup 2020</Name>
     <StartTime>
       <Date>2020-02-09</Date>
     </StartTime>
   </Event>
 </EntryList>
@@ -245,15 +245,15 @@
         },
     ]
 
 
 def test_export_entry_list_with_several_entries():
     content = """\
 <?xml version='1.0' encoding='UTF-8'?>
-<EntryList xmlns="http://www.orienteering.org/datastandard/3.0" iofVersion="3.0">
+<EntryList xmlns="http://www.orienteering.org/datastandard/3.0" iofVersion="3.0" creator="ooresults (https://pypi.org/project/ooresults)">
   <Event>
     <Name>1. O-Cup 2020</Name>
     <StartTime>
       <Date>2020-02-09</Date>
     </StartTime>
   </Event>
   <PersonEntry>
```

### Comparing `ooresults-0.2.1/tests/plugins/test_plugin_iof_result_list.py` & `ooresults-0.2.2/tests/plugins/test_plugin_iof_result_list.py`

 * *Files 2% similar despite different names*

```diff
@@ -194,15 +194,15 @@
         },
     ]
 
 
 def test_export_result_list():
     content = """\
 <?xml version='1.0' encoding='UTF-8'?>
-<ResultList xmlns="http://www.orienteering.org/datastandard/3.0" iofVersion="3.0">
+<ResultList xmlns="http://www.orienteering.org/datastandard/3.0" iofVersion="3.0" creator="ooresults (https://pypi.org/project/ooresults)">
   <Event>
     <Name>1. O-Cup 2020</Name>
     <StartTime>
       <Date>2020-02-09</Date>
     </StartTime>
   </Event>
   <ClassResult>
@@ -292,15 +292,15 @@
     )
     assert document == bytes(content, encoding="utf-8")
 
 
 def test_export_result_list_not_competing():
     content = """\
 <?xml version='1.0' encoding='UTF-8'?>
-<ResultList xmlns="http://www.orienteering.org/datastandard/3.0" iofVersion="3.0">
+<ResultList xmlns="http://www.orienteering.org/datastandard/3.0" iofVersion="3.0" creator="ooresults (https://pypi.org/project/ooresults)">
   <Event>
     <Name>1. O-Cup 2020</Name>
     <StartTime>
       <Date>2020-02-09</Date>
     </StartTime>
   </Event>
   <ClassResult>
@@ -359,15 +359,15 @@
     )
     assert document == bytes(content, encoding="utf-8")
 
 
 def test_export_result_list_not_competing():
     content = """\
 <?xml version='1.0' encoding='UTF-8'?>
-<ResultList xmlns="http://www.orienteering.org/datastandard/3.0" iofVersion="3.0">
+<ResultList xmlns="http://www.orienteering.org/datastandard/3.0" iofVersion="3.0" creator="ooresults (https://pypi.org/project/ooresults)">
   <Event>
     <Name>1. O-Cup 2020</Name>
     <StartTime>
       <Date>2020-02-09</Date>
     </StartTime>
   </Event>
   <ClassResult>
@@ -448,15 +448,15 @@
     }
     assert results == []
 
 
 def test_export_result_list_without_class_result():
     content = """\
 <?xml version='1.0' encoding='UTF-8'?>
-<ResultList xmlns="http://www.orienteering.org/datastandard/3.0" iofVersion="3.0">
+<ResultList xmlns="http://www.orienteering.org/datastandard/3.0" iofVersion="3.0" creator="ooresults (https://pypi.org/project/ooresults)">
   <Event>
     <Name>1. O-Cup 2020</Name>
     <StartTime>
       <Date>2020-02-09</Date>
     </StartTime>
   </Event>
 </ResultList>
@@ -671,15 +671,15 @@
         },
     ]
 
 
 def test_export_result_list_classes():
     content = """\
 <?xml version='1.0' encoding='UTF-8'?>
-<ResultList xmlns="http://www.orienteering.org/datastandard/3.0" iofVersion="3.0">
+<ResultList xmlns="http://www.orienteering.org/datastandard/3.0" iofVersion="3.0" creator="ooresults (https://pypi.org/project/ooresults)">
   <Event>
     <Name>1. O-Cup 2020</Name>
     <StartTime>
       <Date>2020-02-09</Date>
     </StartTime>
   </Event>
   <ClassResult>
```

### Comparing `ooresults-0.2.1/tests/repo/__init__.py` & `ooresults-0.2.2/tests/repo/__init__.py`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/tests/repo/test_classes.py` & `ooresults-0.2.2/tests/repo/test_classes.py`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/tests/repo/test_clubs.py` & `ooresults-0.2.2/tests/repo/test_clubs.py`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/tests/repo/test_competitors.py` & `ooresults-0.2.2/tests/repo/test_competitors.py`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/tests/repo/test_courses.py` & `ooresults-0.2.2/tests/repo/test_courses.py`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/tests/repo/test_entries.py` & `ooresults-0.2.2/tests/repo/test_entries.py`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/tests/repo/test_events.py` & `ooresults-0.2.2/tests/repo/test_events.py`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/tests/repo/test_settings.py` & `ooresults-0.2.2/tests/repo/test_settings.py`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/tests/test_compute_result_net.py` & `ooresults-0.2.2/tests/test_compute_result_net.py`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/tests/test_compute_result_score.py` & `ooresults-0.2.2/tests/test_compute_result_score.py`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/tests/test_compute_result_standard.py` & `ooresults-0.2.2/tests/test_compute_result_standard.py`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/tests/test_configuration.py` & `ooresults-0.2.2/tests/test_configuration.py`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/tests/test_handicap.py` & `ooresults-0.2.2/tests/test_handicap.py`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/tests/test_ranking.py` & `ooresults-0.2.2/tests/test_ranking.py`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/tests/test_series.py` & `ooresults-0.2.2/tests/test_series.py`

 * *Files identical despite different names*

### Comparing `ooresults-0.2.1/tests/test_user.py` & `ooresults-0.2.2/tests/test_user.py`

 * *Files identical despite different names*

