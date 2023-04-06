# Comparing `tmp/hspylib-0.9.22.tar.gz` & `tmp/hspylib-0.9.23.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/hspylib-0.9.22.tar", last modified: Wed Apr 28 14:32:13 2021, max compression
+gzip compressed data, was "hspylib-0.9.23.tar", last modified: Thu Apr 29 02:51:38 2021, max compression
```

## Comparing `hspylib-0.9.22.tar` & `hspylib-0.9.23.tar`

### file list

```diff
@@ -1,157 +1,167 @@
-drwxr-xr-x   0 hugo       (503) staff       (20)        0 2021-04-28 14:32:13.000000 hspylib-0.9.22/
--rw-r--r--   0 hugo       (503) staff       (20)      559 2021-04-28 14:32:13.000000 hspylib-0.9.22/PKG-INFO
--rw-r--r--   0 hugo       (503) staff       (20)        9 2021-04-28 14:28:31.000000 hspylib-0.9.22/README.md
-drwxr-xr-x   0 hugo       (503) staff       (20)        0 2021-04-28 14:32:13.000000 hspylib-0.9.22/hspylib/
--rw-r--r--   0 hugo       (503) staff       (20)      117 2021-04-28 14:28:31.000000 hspylib-0.9.22/hspylib/__init__.py
-drwxr-xr-x   0 hugo       (503) staff       (20)        0 2021-04-28 14:32:13.000000 hspylib-0.9.22/hspylib/core/
--rw-r--r--   0 hugo       (503) staff       (20)      174 2021-04-28 14:28:31.000000 hspylib-0.9.22/hspylib/core/__init__.py
-drwxr-xr-x   0 hugo       (503) staff       (20)        0 2021-04-28 14:32:13.000000 hspylib-0.9.22/hspylib/core/config/
--rw-r--r--   0 hugo       (503) staff       (20)      129 2021-04-28 14:28:31.000000 hspylib-0.9.22/hspylib/core/config/__init__.py
--rw-r--r--   0 hugo       (503) staff       (20)     3091 2021-04-27 13:38:11.000000 hspylib-0.9.22/hspylib/core/config/app_config.py
--rw-r--r--   0 hugo       (503) staff       (20)     2490 2021-01-07 04:31:12.000000 hspylib-0.9.22/hspylib/core/config/properties.py
-drwxr-xr-x   0 hugo       (503) staff       (20)        0 2021-04-28 14:32:13.000000 hspylib-0.9.22/hspylib/core/crud/
--rw-r--r--   0 hugo       (503) staff       (20)      154 2021-04-28 14:28:31.000000 hspylib-0.9.22/hspylib/core/crud/__init__.py
--rw-r--r--   0 hugo       (503) staff       (20)      620 2021-01-07 04:31:12.000000 hspylib-0.9.22/hspylib/core/crud/crud_repository.py
--rw-r--r--   0 hugo       (503) staff       (20)      967 2021-01-07 04:31:12.000000 hspylib-0.9.22/hspylib/core/crud/crud_service.py
-drwxr-xr-x   0 hugo       (503) staff       (20)        0 2021-04-28 14:32:13.000000 hspylib-0.9.22/hspylib/core/crud/db/
--rw-r--r--   0 hugo       (503) staff       (20)      186 2021-04-28 14:28:31.000000 hspylib-0.9.22/hspylib/core/crud/db/__init__.py
--rw-r--r--   0 hugo       (503) staff       (20)     1357 2021-04-23 11:07:57.000000 hspylib-0.9.22/hspylib/core/crud/db/db_repository.py
-drwxr-xr-x   0 hugo       (503) staff       (20)        0 2021-04-28 14:32:13.000000 hspylib-0.9.22/hspylib/core/crud/db/firebase/
--rw-r--r--   0 hugo       (503) staff       (20)      153 2021-04-28 14:28:31.000000 hspylib-0.9.22/hspylib/core/crud/db/firebase/__init__.py
--rw-r--r--   0 hugo       (503) staff       (20)     4014 2021-04-23 11:07:57.000000 hspylib-0.9.22/hspylib/core/crud/db/firebase/firebase_config.py
--rw-r--r--   0 hugo       (503) staff       (20)     3802 2021-04-27 10:32:32.000000 hspylib-0.9.22/hspylib/core/crud/db/firebase/firebase_repository.py
-drwxr-xr-x   0 hugo       (503) staff       (20)        0 2021-04-28 14:32:13.000000 hspylib-0.9.22/hspylib/core/crud/db/mysql/
--rw-r--r--   0 hugo       (503) staff       (20)      125 2021-04-28 14:28:31.000000 hspylib-0.9.22/hspylib/core/crud/db/mysql/__init__.py
--rw-r--r--   0 hugo       (503) staff       (20)     5688 2021-04-27 13:59:18.000000 hspylib-0.9.22/hspylib/core/crud/db/mysql/mysql_repository.py
-drwxr-xr-x   0 hugo       (503) staff       (20)        0 2021-04-28 14:32:13.000000 hspylib-0.9.22/hspylib/core/crud/db/postgres/
--rw-r--r--   0 hugo       (503) staff       (20)      110 2021-04-28 14:28:31.000000 hspylib-0.9.22/hspylib/core/crud/db/postgres/__init__.py
-drwxr-xr-x   0 hugo       (503) staff       (20)        0 2021-04-28 14:32:13.000000 hspylib-0.9.22/hspylib/core/crud/db/sql/
--rw-r--r--   0 hugo       (503) staff       (20)      105 2021-04-28 14:28:31.000000 hspylib-0.9.22/hspylib/core/crud/db/sql/__init__.py
--rw-r--r--   0 hugo       (503) staff       (20)     3044 2021-04-27 14:12:18.000000 hspylib-0.9.22/hspylib/core/crud/db/sql_factory.py
-drwxr-xr-x   0 hugo       (503) staff       (20)        0 2021-04-28 14:32:13.000000 hspylib-0.9.22/hspylib/core/crud/file/
--rw-r--r--   0 hugo       (503) staff       (20)      139 2021-04-28 14:28:31.000000 hspylib-0.9.22/hspylib/core/crud/file/__init__.py
--rw-r--r--   0 hugo       (503) staff       (20)     4051 2021-04-27 10:29:25.000000 hspylib-0.9.22/hspylib/core/crud/file/file_repository.py
--rw-r--r--   0 hugo       (503) staff       (20)      951 2021-04-27 10:29:25.000000 hspylib-0.9.22/hspylib/core/crud/file/file_storage.py
-drwxr-xr-x   0 hugo       (503) staff       (20)        0 2021-04-28 14:32:13.000000 hspylib-0.9.22/hspylib/core/enum/
--rw-r--r--   0 hugo       (503) staff       (20)      198 2021-04-28 14:28:31.000000 hspylib-0.9.22/hspylib/core/enum/__init__.py
--rw-r--r--   0 hugo       (503) staff       (20)     2289 2021-04-27 13:59:42.000000 hspylib-0.9.22/hspylib/core/enum/charset.py
--rw-r--r--   0 hugo       (503) staff       (20)     2346 2021-04-27 14:00:42.000000 hspylib-0.9.22/hspylib/core/enum/content_type.py
--rw-r--r--   0 hugo       (503) staff       (20)      199 2021-03-06 22:37:28.000000 hspylib-0.9.22/hspylib/core/enum/database_type.py
--rw-r--r--   0 hugo       (503) staff       (20)     1081 2021-03-06 22:37:28.000000 hspylib-0.9.22/hspylib/core/enum/enumeration.py
--rw-r--r--   0 hugo       (503) staff       (20)     2995 2021-04-27 10:29:25.000000 hspylib-0.9.22/hspylib/core/enum/http_code.py
--rw-r--r--   0 hugo       (503) staff       (20)      226 2021-03-06 22:37:28.000000 hspylib-0.9.22/hspylib/core/enum/http_method.py
-drwxr-xr-x   0 hugo       (503) staff       (20)        0 2021-04-28 14:32:13.000000 hspylib-0.9.22/hspylib/core/exception/
--rw-r--r--   0 hugo       (503) staff       (20)      146 2021-04-28 14:28:31.000000 hspylib-0.9.22/hspylib/core/exception/__init__.py
--rw-r--r--   0 hugo       (503) staff       (20)       45 2021-01-07 04:31:12.000000 hspylib-0.9.22/hspylib/core/exception/input_aborted_error.py
--rw-r--r--   0 hugo       (503) staff       (20)       41 2021-01-07 04:31:12.000000 hspylib-0.9.22/hspylib/core/exception/not_found_error.py
-drwxr-xr-x   0 hugo       (503) staff       (20)        0 2021-04-28 14:32:13.000000 hspylib-0.9.22/hspylib/core/meta/
--rw-r--r--   0 hugo       (503) staff       (20)      109 2021-04-28 14:28:31.000000 hspylib-0.9.22/hspylib/core/meta/__init__.py
--rw-r--r--   0 hugo       (503) staff       (20)      484 2021-01-07 04:31:12.000000 hspylib-0.9.22/hspylib/core/meta/singleton.py
-drwxr-xr-x   0 hugo       (503) staff       (20)        0 2021-04-28 14:32:13.000000 hspylib-0.9.22/hspylib/core/model/
--rw-r--r--   0 hugo       (503) staff       (20)      107 2021-04-28 14:28:31.000000 hspylib-0.9.22/hspylib/core/model/__init__.py
--rw-r--r--   0 hugo       (503) staff       (20)     1826 2021-04-27 10:29:25.000000 hspylib-0.9.22/hspylib/core/model/entity.py
-drwxr-xr-x   0 hugo       (503) staff       (20)        0 2021-04-28 14:32:13.000000 hspylib-0.9.22/hspylib/core/tools/
--rw-r--r--   0 hugo       (503) staff       (20)      177 2021-04-28 14:28:31.000000 hspylib-0.9.22/hspylib/core/tools/__init__.py
--rw-r--r--   0 hugo       (503) staff       (20)     6130 2021-04-27 09:04:40.000000 hspylib-0.9.22/hspylib/core/tools/commons.py
--rw-r--r--   0 hugo       (503) staff       (20)     3169 2021-04-28 14:26:44.000000 hspylib-0.9.22/hspylib/core/tools/keyboard.py
--rw-r--r--   0 hugo       (503) staff       (20)      402 2021-01-07 04:31:12.000000 hspylib-0.9.22/hspylib/core/tools/regex_commons.py
--rw-r--r--   0 hugo       (503) staff       (20)     1535 2021-04-27 14:20:26.000000 hspylib-0.9.22/hspylib/core/tools/text_helper.py
--rw-r--r--   0 hugo       (503) staff       (20)     1820 2021-04-27 14:20:04.000000 hspylib-0.9.22/hspylib/core/tools/validator.py
-drwxr-xr-x   0 hugo       (503) staff       (20)        0 2021-04-28 14:32:13.000000 hspylib-0.9.22/hspylib/modules/
--rw-r--r--   0 hugo       (503) staff       (20)      172 2021-04-28 14:28:31.000000 hspylib-0.9.22/hspylib/modules/__init__.py
-drwxr-xr-x   0 hugo       (503) staff       (20)        0 2021-04-28 14:32:13.000000 hspylib-0.9.22/hspylib/modules/eventbus/
--rw-r--r--   0 hugo       (503) staff       (20)      115 2021-04-28 14:28:31.000000 hspylib-0.9.22/hspylib/modules/eventbus/__init__.py
--rw-r--r--   0 hugo       (503) staff       (20)     1537 2021-04-27 10:03:37.000000 hspylib-0.9.22/hspylib/modules/eventbus/eventbus.py
-drwxr-xr-x   0 hugo       (503) staff       (20)        0 2021-04-28 14:32:13.000000 hspylib-0.9.22/hspylib/modules/fetch/
--rw-r--r--   0 hugo       (503) staff       (20)      129 2021-04-28 14:28:31.000000 hspylib-0.9.22/hspylib/modules/fetch/__init__.py
--rw-r--r--   0 hugo       (503) staff       (20)     2445 2021-04-27 10:29:25.000000 hspylib-0.9.22/hspylib/modules/fetch/fetch.py
--rw-r--r--   0 hugo       (503) staff       (20)     1275 2021-04-27 10:29:25.000000 hspylib-0.9.22/hspylib/modules/fetch/http_response.py
-drwxr-xr-x   0 hugo       (503) staff       (20)        0 2021-04-28 14:32:13.000000 hspylib-0.9.22/hspylib/modules/json_search/
--rw-r--r--   0 hugo       (503) staff       (20)      121 2021-04-28 14:28:31.000000 hspylib-0.9.22/hspylib/modules/json_search/__init__.py
--rwxr--r--   0 hugo       (503) staff       (20)     6311 2020-11-19 00:00:29.000000 hspylib-0.9.22/hspylib/modules/json_search/json_search.py
-drwxr-xr-x   0 hugo       (503) staff       (20)        0 2021-04-28 14:32:13.000000 hspylib-0.9.22/hspylib/modules/mock/
--rw-r--r--   0 hugo       (503) staff       (20)      159 2021-04-28 14:28:31.000000 hspylib-0.9.22/hspylib/modules/mock/__init__.py
--rw-r--r--   0 hugo       (503) staff       (20)     2221 2021-04-27 10:29:25.000000 hspylib-0.9.22/hspylib/modules/mock/mock_request.py
--rw-r--r--   0 hugo       (503) staff       (20)     1622 2021-04-27 14:14:39.000000 hspylib-0.9.22/hspylib/modules/mock/mock_server.py
--rw-r--r--   0 hugo       (503) staff       (20)     5032 2021-04-27 10:33:50.000000 hspylib-0.9.22/hspylib/modules/mock/mock_server_handler.py
-drwxr-xr-x   0 hugo       (503) staff       (20)        0 2021-04-28 14:32:13.000000 hspylib-0.9.22/hspylib/modules/security/
--rw-r--r--   0 hugo       (503) staff       (20)      115 2021-04-28 14:28:31.000000 hspylib-0.9.22/hspylib/modules/security/__init__.py
--rw-r--r--   0 hugo       (503) staff       (20)     3628 2021-04-27 10:29:25.000000 hspylib-0.9.22/hspylib/modules/security/security.py
-drwxr-xr-x   0 hugo       (503) staff       (20)        0 2021-04-28 14:32:13.000000 hspylib-0.9.22/hspylib/modules/web/
--rw-r--r--   0 hugo       (503) staff       (20)      129 2021-04-28 14:28:31.000000 hspylib-0.9.22/hspylib/modules/web/__init__.py
--rw-r--r--   0 hugo       (503) staff       (20)      839 2021-04-20 03:11:45.000000 hspylib-0.9.22/hspylib/modules/web/rest_utils.py
--rw-r--r--   0 hugo       (503) staff       (20)      914 2021-04-20 03:11:45.000000 hspylib-0.9.22/hspylib/modules/web/soap_utils.py
-drwxr-xr-x   0 hugo       (503) staff       (20)        0 2021-04-28 14:32:13.000000 hspylib-0.9.22/hspylib/ui/
--rw-r--r--   0 hugo       (503) staff       (20)      105 2021-04-28 14:28:31.000000 hspylib-0.9.22/hspylib/ui/__init__.py
-drwxr-xr-x   0 hugo       (503) staff       (20)        0 2021-04-28 14:32:13.000000 hspylib-0.9.22/hspylib/ui/cli/
--rw-r--r--   0 hugo       (503) staff       (20)      174 2021-04-28 14:28:31.000000 hspylib-0.9.22/hspylib/ui/cli/__init__.py
-drwxr-xr-x   0 hugo       (503) staff       (20)        0 2021-04-28 14:32:13.000000 hspylib-0.9.22/hspylib/ui/cli/app/
--rw-r--r--   0 hugo       (503) staff       (20)      125 2021-04-28 14:28:31.000000 hspylib-0.9.22/hspylib/ui/cli/app/__init__.py
--rw-r--r--   0 hugo       (503) staff       (20)     4773 2021-04-27 10:59:34.000000 hspylib-0.9.22/hspylib/ui/cli/app/application.py
--rw-r--r--   0 hugo       (503) staff       (20)     1171 2021-04-23 11:07:57.000000 hspylib-0.9.22/hspylib/ui/cli/app/option.py
-drwxr-xr-x   0 hugo       (503) staff       (20)        0 2021-04-28 14:32:13.000000 hspylib-0.9.22/hspylib/ui/cli/factory/
--rw-r--r--   0 hugo       (503) staff       (20)      152 2021-04-28 14:28:31.000000 hspylib-0.9.22/hspylib/ui/cli/factory/__init__.py
--rw-r--r--   0 hugo       (503) staff       (20)      963 2021-03-06 22:37:28.000000 hspylib-0.9.22/hspylib/ui/cli/factory/menu_entry.py
--rw-r--r--   0 hugo       (503) staff       (20)     1013 2021-04-27 13:38:11.000000 hspylib-0.9.22/hspylib/ui/cli/factory/menu_factory.py
--rw-r--r--   0 hugo       (503) staff       (20)      566 2021-03-06 22:37:28.000000 hspylib-0.9.22/hspylib/ui/cli/factory/menu_option.py
-drwxr-xr-x   0 hugo       (503) staff       (20)        0 2021-04-28 14:32:13.000000 hspylib-0.9.22/hspylib/ui/cli/icons/
--rw-r--r--   0 hugo       (503) staff       (20)      128 2021-04-28 14:28:31.000000 hspylib-0.9.22/hspylib/ui/cli/icons/__init__.py
-drwxr-xr-x   0 hugo       (503) staff       (20)        0 2021-04-28 14:32:13.000000 hspylib-0.9.22/hspylib/ui/cli/icons/emojis/
--rw-r--r--   0 hugo       (503) staff       (20)      128 2021-04-28 14:28:31.000000 hspylib-0.9.22/hspylib/ui/cli/icons/emojis/__init__.py
--rw-r--r--   0 hugo       (503) staff       (20)      471 2021-04-27 14:18:29.000000 hspylib-0.9.22/hspylib/ui/cli/icons/emojis/emojis.py
-drwxr-xr-x   0 hugo       (503) staff       (20)        0 2021-04-28 14:32:13.000000 hspylib-0.9.22/hspylib/ui/cli/icons/emojis/faces/
--rw-r--r--   0 hugo       (503) staff       (20)      128 2021-04-28 14:28:31.000000 hspylib-0.9.22/hspylib/ui/cli/icons/emojis/faces/__init__.py
--rw-r--r--   0 hugo       (503) staff       (20)      763 2021-04-01 03:09:41.000000 hspylib-0.9.22/hspylib/ui/cli/icons/emojis/faces/face_smiling.py
-drwxr-xr-x   0 hugo       (503) staff       (20)        0 2021-04-28 14:32:13.000000 hspylib-0.9.22/hspylib/ui/cli/icons/font_awesome/
--rw-r--r--   0 hugo       (503) staff       (20)      140 2021-04-28 14:28:31.000000 hspylib-0.9.22/hspylib/ui/cli/icons/font_awesome/__init__.py
--rw-r--r--   0 hugo       (503) staff       (20)     1002 2021-04-28 00:42:42.000000 hspylib-0.9.22/hspylib/ui/cli/icons/font_awesome/awesome.py
-drwxr-xr-x   0 hugo       (503) staff       (20)        0 2021-04-28 14:32:13.000000 hspylib-0.9.22/hspylib/ui/cli/icons/font_awesome/ui_compose/
--rw-r--r--   0 hugo       (503) staff       (20)      137 2021-04-28 14:28:31.000000 hspylib-0.9.22/hspylib/ui/cli/icons/font_awesome/ui_compose/__init__.py
--rw-r--r--   0 hugo       (503) staff       (20)     1072 2021-04-27 13:38:11.000000 hspylib-0.9.22/hspylib/ui/cli/icons/font_awesome/ui_compose/form_icons.py
-drwxr-xr-x   0 hugo       (503) staff       (20)        0 2021-04-28 14:32:13.000000 hspylib-0.9.22/hspylib/ui/cli/menu/
--rw-r--r--   0 hugo       (503) staff       (20)      165 2021-04-28 14:28:31.000000 hspylib-0.9.22/hspylib/ui/cli/menu/__init__.py
-drwxr-xr-x   0 hugo       (503) staff       (20)        0 2021-04-28 14:32:13.000000 hspylib-0.9.22/hspylib/ui/cli/menu/extra/
--rw-r--r--   0 hugo       (503) staff       (20)      159 2021-04-28 14:28:31.000000 hspylib-0.9.22/hspylib/ui/cli/menu/extra/__init__.py
--rwxr-xr-x   0 hugo       (503) staff       (20)     7623 2021-04-27 13:38:11.000000 hspylib-0.9.22/hspylib/ui/cli/menu/extra/mchoose.py
--rwxr-xr-x   0 hugo       (503) staff       (20)     6940 2021-04-28 14:27:28.000000 hspylib-0.9.22/hspylib/ui/cli/menu/extra/mdashboard.py
--rwxr-xr-x   0 hugo       (503) staff       (20)    14021 2021-04-28 13:54:49.000000 hspylib-0.9.22/hspylib/ui/cli/menu/extra/minput.py
--rwxr-xr-x   0 hugo       (503) staff       (20)     6606 2021-04-27 13:38:11.000000 hspylib-0.9.22/hspylib/ui/cli/menu/extra/mselect.py
--rw-r--r--   0 hugo       (503) staff       (20)      704 2021-03-06 22:37:28.000000 hspylib-0.9.22/hspylib/ui/cli/menu/menu.py
--rw-r--r--   0 hugo       (503) staff       (20)     1575 2021-03-06 22:37:28.000000 hspylib-0.9.22/hspylib/ui/cli/menu/menu_item.py
--rw-r--r--   0 hugo       (503) staff       (20)      811 2021-03-06 22:37:28.000000 hspylib-0.9.22/hspylib/ui/cli/menu/menu_ui.py
--rw-r--r--   0 hugo       (503) staff       (20)     3312 2021-03-13 02:38:43.000000 hspylib-0.9.22/hspylib/ui/cli/menu/menu_utils.py
-drwxr-xr-x   0 hugo       (503) staff       (20)        0 2021-04-28 14:32:13.000000 hspylib-0.9.22/hspylib/ui/cli/tables/
--rw-r--r--   0 hugo       (503) staff       (20)      118 2021-04-28 14:28:31.000000 hspylib-0.9.22/hspylib/ui/cli/tables/__init__.py
--rw-r--r--   0 hugo       (503) staff       (20)     5081 2021-03-06 22:37:28.000000 hspylib-0.9.22/hspylib/ui/cli/tables/table_renderer.py
-drwxr-xr-x   0 hugo       (503) staff       (20)        0 2021-04-28 14:32:13.000000 hspylib-0.9.22/hspylib/ui/cli/tools/
--rw-r--r--   0 hugo       (503) staff       (20)      112 2021-04-28 14:28:31.000000 hspylib-0.9.22/hspylib/ui/cli/tools/__init__.py
-drwxr-xr-x   0 hugo       (503) staff       (20)        0 2021-04-28 14:32:13.000000 hspylib-0.9.22/hspylib/ui/cli/tools/validator/
--rw-r--r--   0 hugo       (503) staff       (20)      131 2021-04-28 14:28:31.000000 hspylib-0.9.22/hspylib/ui/cli/tools/validator/__init__.py
--rw-r--r--   0 hugo       (503) staff       (20)      516 2021-04-23 11:07:57.000000 hspylib-0.9.22/hspylib/ui/cli/tools/validator/argument_validator.py
-drwxr-xr-x   0 hugo       (503) staff       (20)        0 2021-04-28 14:32:13.000000 hspylib-0.9.22/hspylib/ui/cli/vt100/
--rw-r--r--   0 hugo       (503) staff       (20)      140 2021-04-28 14:28:31.000000 hspylib-0.9.22/hspylib/ui/cli/vt100/__init__.py
--rw-r--r--   0 hugo       (503) staff       (20)     2775 2021-04-27 14:13:28.000000 hspylib-0.9.22/hspylib/ui/cli/vt100/vt_100.py
--rw-r--r--   0 hugo       (503) staff       (20)     3047 2021-04-27 14:11:44.000000 hspylib-0.9.22/hspylib/ui/cli/vt100/vt_codes.py
--rw-r--r--   0 hugo       (503) staff       (20)     1556 2021-04-27 14:11:28.000000 hspylib-0.9.22/hspylib/ui/cli/vt100/vt_colors.py
-drwxr-xr-x   0 hugo       (503) staff       (20)        0 2021-04-28 14:32:13.000000 hspylib-0.9.22/hspylib/ui/qt/
--rw-r--r--   0 hugo       (503) staff       (20)      146 2021-04-28 14:28:31.000000 hspylib-0.9.22/hspylib/ui/qt/__init__.py
-drwxr-xr-x   0 hugo       (503) staff       (20)        0 2021-04-28 14:32:13.000000 hspylib-0.9.22/hspylib/ui/qt/forms/
--rw-r--r--   0 hugo       (503) staff       (20)      100 2021-04-28 14:28:31.000000 hspylib-0.9.22/hspylib/ui/qt/forms/__init__.py
-drwxr-xr-x   0 hugo       (503) staff       (20)        0 2021-04-28 14:32:13.000000 hspylib-0.9.22/hspylib/ui/qt/promotions/
--rw-r--r--   0 hugo       (503) staff       (20)      156 2021-04-28 14:28:31.000000 hspylib-0.9.22/hspylib/ui/qt/promotions/__init__.py
--rw-r--r--   0 hugo       (503) staff       (20)      268 2021-04-27 13:38:11.000000 hspylib-0.9.22/hspylib/ui/qt/promotions/button_label.py
--rw-r--r--   0 hugo       (503) staff       (20)     2201 2021-04-27 14:10:35.000000 hspylib-0.9.22/hspylib/ui/qt/promotions/entity_table_model.py
--rw-r--r--   0 hugo       (503) staff       (20)      280 2021-04-27 13:38:11.000000 hspylib-0.9.22/hspylib/ui/qt/promotions/panel.py
--rw-r--r--   0 hugo       (503) staff       (20)     2015 2021-03-06 22:37:28.000000 hspylib-0.9.22/hspylib/ui/qt/qt_finder.py
-drwxr-xr-x   0 hugo       (503) staff       (20)        0 2021-04-28 14:32:13.000000 hspylib-0.9.22/hspylib/ui/qt/views/
--rw-r--r--   0 hugo       (503) staff       (20)      125 2021-04-28 14:28:31.000000 hspylib-0.9.22/hspylib/ui/qt/views/__init__.py
--rw-r--r--   0 hugo       (503) staff       (20)      466 2021-04-27 10:29:25.000000 hspylib-0.9.22/hspylib/ui/qt/views/main_view.py
--rw-r--r--   0 hugo       (503) staff       (20)      377 2021-04-27 10:29:07.000000 hspylib-0.9.22/hspylib/ui/qt/views/qt_view.py
-drwxr-xr-x   0 hugo       (503) staff       (20)        0 2021-04-28 14:32:13.000000 hspylib-0.9.22/hspylib.egg-info/
--rw-r--r--   0 hugo       (503) staff       (20)      559 2021-04-28 14:32:13.000000 hspylib-0.9.22/hspylib.egg-info/PKG-INFO
--rw-r--r--   0 hugo       (503) staff       (20)     3953 2021-04-28 14:32:13.000000 hspylib-0.9.22/hspylib.egg-info/SOURCES.txt
--rw-r--r--   0 hugo       (503) staff       (20)        1 2021-04-28 14:32:13.000000 hspylib-0.9.22/hspylib.egg-info/dependency_links.txt
--rw-r--r--   0 hugo       (503) staff       (20)      104 2021-04-28 14:32:13.000000 hspylib-0.9.22/hspylib.egg-info/requires.txt
--rw-r--r--   0 hugo       (503) staff       (20)        8 2021-04-28 14:32:13.000000 hspylib-0.9.22/hspylib.egg-info/top_level.txt
--rw-r--r--   0 hugo       (503) staff       (20)       38 2021-04-28 14:32:13.000000 hspylib-0.9.22/setup.cfg
--rw-r--r--   0 hugo       (503) staff       (20)     1220 2021-04-23 13:57:11.000000 hspylib-0.9.22/setup.py
+drwxr-xr-x   0 hjunior    (502) staff       (20)        0 2021-04-29 02:51:38.836424 hspylib-0.9.23/
+-rw-r--r--   0 hjunior    (502) staff       (20)      156 2021-04-28 18:19:41.000000 hspylib-0.9.23/MANIFEST.in
+-rw-r--r--   0 hjunior    (502) staff       (20)      559 2021-04-29 02:51:38.835215 hspylib-0.9.23/PKG-INFO
+-rw-r--r--   0 hjunior    (502) staff       (20)        9 2021-04-29 02:24:58.000000 hspylib-0.9.23/README.md
+drwxr-xr-x   0 hjunior    (502) staff       (20)        0 2021-04-29 02:51:38.712408 hspylib-0.9.23/hspylib/
+-rw-r--r--   0 hjunior    (502) staff       (20)        6 2021-04-29 02:51:38.000000 hspylib-0.9.23/hspylib/.version
+-rw-r--r--   0 hjunior    (502) staff       (20)      155 2021-04-29 02:24:58.000000 hspylib-0.9.23/hspylib/__init__.py
+-rwxr-xr-x   0 hjunior    (502) staff       (20)     7035 2021-04-29 01:46:06.000000 hspylib-0.9.23/hspylib/__main__.py
+drwxr-xr-x   0 hjunior    (502) staff       (20)        0 2021-04-29 02:51:38.722969 hspylib-0.9.23/hspylib/core/
+-rw-r--r--   0 hjunior    (502) staff       (20)      174 2021-04-29 02:24:58.000000 hspylib-0.9.23/hspylib/core/__init__.py
+drwxr-xr-x   0 hjunior    (502) staff       (20)        0 2021-04-29 02:51:38.723894 hspylib-0.9.23/hspylib/core/config/
+-rw-r--r--   0 hjunior    (502) staff       (20)      129 2021-04-29 02:24:58.000000 hspylib-0.9.23/hspylib/core/config/__init__.py
+-rw-r--r--   0 hjunior    (502) staff       (20)     3091 2021-04-27 19:50:29.000000 hspylib-0.9.23/hspylib/core/config/app_config.py
+-rw-r--r--   0 hjunior    (502) staff       (20)     2490 2021-04-15 21:52:40.000000 hspylib-0.9.23/hspylib/core/config/properties.py
+drwxr-xr-x   0 hjunior    (502) staff       (20)        0 2021-04-29 02:51:38.725038 hspylib-0.9.23/hspylib/core/crud/
+-rw-r--r--   0 hjunior    (502) staff       (20)      154 2021-04-29 02:24:58.000000 hspylib-0.9.23/hspylib/core/crud/__init__.py
+-rw-r--r--   0 hjunior    (502) staff       (20)      620 2021-04-15 21:52:40.000000 hspylib-0.9.23/hspylib/core/crud/crud_repository.py
+-rw-r--r--   0 hjunior    (502) staff       (20)      967 2021-04-15 21:52:40.000000 hspylib-0.9.23/hspylib/core/crud/crud_service.py
+drwxr-xr-x   0 hjunior    (502) staff       (20)        0 2021-04-29 02:51:38.727889 hspylib-0.9.23/hspylib/core/crud/db/
+-rw-r--r--   0 hjunior    (502) staff       (20)      176 2021-04-29 02:24:58.000000 hspylib-0.9.23/hspylib/core/crud/db/__init__.py
+-rw-r--r--   0 hjunior    (502) staff       (20)     1357 2021-04-23 04:12:28.000000 hspylib-0.9.23/hspylib/core/crud/db/db_repository.py
+drwxr-xr-x   0 hjunior    (502) staff       (20)        0 2021-04-29 02:51:38.730531 hspylib-0.9.23/hspylib/core/crud/db/firebase/
+-rw-r--r--   0 hjunior    (502) staff       (20)      153 2021-04-29 02:24:58.000000 hspylib-0.9.23/hspylib/core/crud/db/firebase/__init__.py
+-rw-r--r--   0 hjunior    (502) staff       (20)     4006 2021-04-29 02:30:51.000000 hspylib-0.9.23/hspylib/core/crud/db/firebase/firebase_config.py
+-rw-r--r--   0 hjunior    (502) staff       (20)     3802 2021-04-27 19:50:29.000000 hspylib-0.9.23/hspylib/core/crud/db/firebase/firebase_repository.py
+drwxr-xr-x   0 hjunior    (502) staff       (20)        0 2021-04-29 02:51:38.731695 hspylib-0.9.23/hspylib/core/crud/db/mysql/
+-rw-r--r--   0 hjunior    (502) staff       (20)      125 2021-04-29 02:24:58.000000 hspylib-0.9.23/hspylib/core/crud/db/mysql/__init__.py
+-rw-r--r--   0 hjunior    (502) staff       (20)     5688 2021-04-27 19:50:29.000000 hspylib-0.9.23/hspylib/core/crud/db/mysql/mysql_repository.py
+drwxr-xr-x   0 hjunior    (502) staff       (20)        0 2021-04-29 02:51:38.732650 hspylib-0.9.23/hspylib/core/crud/db/postgres/
+-rw-r--r--   0 hjunior    (502) staff       (20)      110 2021-04-29 02:24:58.000000 hspylib-0.9.23/hspylib/core/crud/db/postgres/__init__.py
+drwxr-xr-x   0 hjunior    (502) staff       (20)        0 2021-04-29 02:51:38.733520 hspylib-0.9.23/hspylib/core/crud/db/sql/
+-rw-r--r--   0 hjunior    (502) staff       (20)      268 2021-04-15 21:52:40.000000 hspylib-0.9.23/hspylib/core/crud/db/sql/sql_stubs.sql
+-rw-r--r--   0 hjunior    (502) staff       (20)     3044 2021-04-27 19:50:29.000000 hspylib-0.9.23/hspylib/core/crud/db/sql_factory.py
+drwxr-xr-x   0 hjunior    (502) staff       (20)        0 2021-04-29 02:51:38.735306 hspylib-0.9.23/hspylib/core/crud/file/
+-rw-r--r--   0 hjunior    (502) staff       (20)      139 2021-04-29 02:24:58.000000 hspylib-0.9.23/hspylib/core/crud/file/__init__.py
+-rw-r--r--   0 hjunior    (502) staff       (20)     4051 2021-04-27 19:50:29.000000 hspylib-0.9.23/hspylib/core/crud/file/file_repository.py
+-rw-r--r--   0 hjunior    (502) staff       (20)      951 2021-04-27 19:50:29.000000 hspylib-0.9.23/hspylib/core/crud/file/file_storage.py
+drwxr-xr-x   0 hjunior    (502) staff       (20)        0 2021-04-29 02:51:38.740346 hspylib-0.9.23/hspylib/core/enum/
+-rw-r--r--   0 hjunior    (502) staff       (20)      198 2021-04-29 02:24:58.000000 hspylib-0.9.23/hspylib/core/enum/__init__.py
+-rw-r--r--   0 hjunior    (502) staff       (20)     2289 2021-04-27 19:50:29.000000 hspylib-0.9.23/hspylib/core/enum/charset.py
+-rw-r--r--   0 hjunior    (502) staff       (20)     2346 2021-04-27 19:50:29.000000 hspylib-0.9.23/hspylib/core/enum/content_type.py
+-rw-r--r--   0 hjunior    (502) staff       (20)      199 2021-04-15 21:52:40.000000 hspylib-0.9.23/hspylib/core/enum/database_type.py
+-rw-r--r--   0 hjunior    (502) staff       (20)     1091 2021-04-28 22:51:58.000000 hspylib-0.9.23/hspylib/core/enum/enumeration.py
+-rw-r--r--   0 hjunior    (502) staff       (20)     2995 2021-04-27 19:50:29.000000 hspylib-0.9.23/hspylib/core/enum/http_code.py
+-rw-r--r--   0 hjunior    (502) staff       (20)      226 2021-04-15 21:52:40.000000 hspylib-0.9.23/hspylib/core/enum/http_method.py
+drwxr-xr-x   0 hjunior    (502) staff       (20)        0 2021-04-29 02:51:38.742183 hspylib-0.9.23/hspylib/core/exception/
+-rw-r--r--   0 hjunior    (502) staff       (20)      146 2021-04-29 02:24:58.000000 hspylib-0.9.23/hspylib/core/exception/__init__.py
+-rw-r--r--   0 hjunior    (502) staff       (20)       45 2021-04-15 21:52:40.000000 hspylib-0.9.23/hspylib/core/exception/input_aborted_error.py
+-rw-r--r--   0 hjunior    (502) staff       (20)       41 2021-04-15 21:52:40.000000 hspylib-0.9.23/hspylib/core/exception/not_found_error.py
+drwxr-xr-x   0 hjunior    (502) staff       (20)        0 2021-04-29 02:51:38.746513 hspylib-0.9.23/hspylib/core/meta/
+-rw-r--r--   0 hjunior    (502) staff       (20)      109 2021-04-29 02:24:58.000000 hspylib-0.9.23/hspylib/core/meta/__init__.py
+-rw-r--r--   0 hjunior    (502) staff       (20)      484 2021-04-15 21:52:40.000000 hspylib-0.9.23/hspylib/core/meta/singleton.py
+drwxr-xr-x   0 hjunior    (502) staff       (20)        0 2021-04-29 02:51:38.747629 hspylib-0.9.23/hspylib/core/model/
+-rw-r--r--   0 hjunior    (502) staff       (20)      107 2021-04-29 02:24:58.000000 hspylib-0.9.23/hspylib/core/model/__init__.py
+-rw-r--r--   0 hjunior    (502) staff       (20)     1826 2021-04-27 19:50:29.000000 hspylib-0.9.23/hspylib/core/model/entity.py
+drwxr-xr-x   0 hjunior    (502) staff       (20)        0 2021-04-29 02:51:38.753305 hspylib-0.9.23/hspylib/core/tools/
+-rw-r--r--   0 hjunior    (502) staff       (20)      177 2021-04-29 02:24:58.000000 hspylib-0.9.23/hspylib/core/tools/__init__.py
+-rw-r--r--   0 hjunior    (502) staff       (20)     6146 2021-04-28 18:16:46.000000 hspylib-0.9.23/hspylib/core/tools/commons.py
+-rw-r--r--   0 hjunior    (502) staff       (20)     3169 2021-04-28 15:08:18.000000 hspylib-0.9.23/hspylib/core/tools/keyboard.py
+-rw-r--r--   0 hjunior    (502) staff       (20)      402 2021-04-15 21:52:40.000000 hspylib-0.9.23/hspylib/core/tools/regex_commons.py
+-rw-r--r--   0 hjunior    (502) staff       (20)     1535 2021-04-27 19:50:29.000000 hspylib-0.9.23/hspylib/core/tools/text_helper.py
+-rw-r--r--   0 hjunior    (502) staff       (20)     1820 2021-04-27 19:50:29.000000 hspylib-0.9.23/hspylib/core/tools/validator.py
+drwxr-xr-x   0 hjunior    (502) staff       (20)        0 2021-04-29 02:51:38.753898 hspylib-0.9.23/hspylib/modules/
+-rw-r--r--   0 hjunior    (502) staff       (20)      172 2021-04-29 02:24:58.000000 hspylib-0.9.23/hspylib/modules/__init__.py
+drwxr-xr-x   0 hjunior    (502) staff       (20)        0 2021-04-29 02:51:38.754974 hspylib-0.9.23/hspylib/modules/eventbus/
+-rw-r--r--   0 hjunior    (502) staff       (20)      115 2021-04-29 02:24:58.000000 hspylib-0.9.23/hspylib/modules/eventbus/__init__.py
+-rw-r--r--   0 hjunior    (502) staff       (20)     1537 2021-04-15 21:52:40.000000 hspylib-0.9.23/hspylib/modules/eventbus/eventbus.py
+drwxr-xr-x   0 hjunior    (502) staff       (20)        0 2021-04-29 02:51:38.757854 hspylib-0.9.23/hspylib/modules/fetch/
+-rw-r--r--   0 hjunior    (502) staff       (20)      129 2021-04-29 02:24:58.000000 hspylib-0.9.23/hspylib/modules/fetch/__init__.py
+-rw-r--r--   0 hjunior    (502) staff       (20)     2445 2021-04-27 19:50:29.000000 hspylib-0.9.23/hspylib/modules/fetch/fetch.py
+-rw-r--r--   0 hjunior    (502) staff       (20)     1275 2021-04-27 19:50:29.000000 hspylib-0.9.23/hspylib/modules/fetch/http_response.py
+drwxr-xr-x   0 hjunior    (502) staff       (20)        0 2021-04-29 02:51:38.759124 hspylib-0.9.23/hspylib/modules/json_search/
+-rw-r--r--   0 hjunior    (502) staff       (20)      121 2021-04-29 02:24:58.000000 hspylib-0.9.23/hspylib/modules/json_search/__init__.py
+-rwxr-xr-x   0 hjunior    (502) staff       (20)     6311 2021-04-15 21:52:40.000000 hspylib-0.9.23/hspylib/modules/json_search/json_search.py
+drwxr-xr-x   0 hjunior    (502) staff       (20)        0 2021-04-29 02:51:38.765234 hspylib-0.9.23/hspylib/modules/mock/
+-rw-r--r--   0 hjunior    (502) staff       (20)      159 2021-04-29 02:24:58.000000 hspylib-0.9.23/hspylib/modules/mock/__init__.py
+-rw-r--r--   0 hjunior    (502) staff       (20)     2221 2021-04-27 19:50:29.000000 hspylib-0.9.23/hspylib/modules/mock/mock_request.py
+-rw-r--r--   0 hjunior    (502) staff       (20)     1622 2021-04-27 19:50:29.000000 hspylib-0.9.23/hspylib/modules/mock/mock_server.py
+-rw-r--r--   0 hjunior    (502) staff       (20)     5032 2021-04-27 19:50:29.000000 hspylib-0.9.23/hspylib/modules/mock/mock_server_handler.py
+drwxr-xr-x   0 hjunior    (502) staff       (20)        0 2021-04-29 02:51:38.766431 hspylib-0.9.23/hspylib/modules/security/
+-rw-r--r--   0 hjunior    (502) staff       (20)      115 2021-04-29 02:24:58.000000 hspylib-0.9.23/hspylib/modules/security/__init__.py
+-rw-r--r--   0 hjunior    (502) staff       (20)     3628 2021-04-27 19:50:29.000000 hspylib-0.9.23/hspylib/modules/security/security.py
+drwxr-xr-x   0 hjunior    (502) staff       (20)        0 2021-04-29 02:51:38.768126 hspylib-0.9.23/hspylib/modules/web/
+-rw-r--r--   0 hjunior    (502) staff       (20)      129 2021-04-29 02:24:58.000000 hspylib-0.9.23/hspylib/modules/web/__init__.py
+-rw-r--r--   0 hjunior    (502) staff       (20)      839 2021-04-19 23:13:06.000000 hspylib-0.9.23/hspylib/modules/web/rest_utils.py
+-rw-r--r--   0 hjunior    (502) staff       (20)      914 2021-04-19 23:12:19.000000 hspylib-0.9.23/hspylib/modules/web/soap_utils.py
+drwxr-xr-x   0 hjunior    (502) staff       (20)        0 2021-04-29 02:51:38.770575 hspylib-0.9.23/hspylib/templates/
+-rw-r--r--   0 hjunior    (502) staff       (20)      956 2021-04-29 01:33:50.000000 hspylib-0.9.23/hspylib/templates/tpl-build.gradle
+-rw-r--r--   0 hjunior    (502) staff       (20)      227 2021-04-29 01:40:36.000000 hspylib-0.9.23/hspylib/templates/tpl-dependencies.gradle
+-rw-r--r--   0 hjunior    (502) staff       (20)      760 2021-04-28 18:19:02.000000 hspylib-0.9.23/hspylib/templates/tpl-main.py
+-rw-r--r--   0 hjunior    (502) staff       (20)      221 2021-04-29 01:34:40.000000 hspylib-0.9.23/hspylib/templates/tpl-run-it.sh
+-rw-r--r--   0 hjunior    (502) staff       (20)      169 2021-04-29 01:20:22.000000 hspylib-0.9.23/hspylib/templates/tpl.gitignore
+drwxr-xr-x   0 hjunior    (502) staff       (20)        0 2021-04-29 02:51:38.771247 hspylib-0.9.23/hspylib/ui/
+-rw-r--r--   0 hjunior    (502) staff       (20)      105 2021-04-29 02:24:58.000000 hspylib-0.9.23/hspylib/ui/__init__.py
+drwxr-xr-x   0 hjunior    (502) staff       (20)        0 2021-04-29 02:51:38.772008 hspylib-0.9.23/hspylib/ui/cli/
+-rw-r--r--   0 hjunior    (502) staff       (20)      174 2021-04-29 02:24:58.000000 hspylib-0.9.23/hspylib/ui/cli/__init__.py
+drwxr-xr-x   0 hjunior    (502) staff       (20)        0 2021-04-29 02:51:38.773602 hspylib-0.9.23/hspylib/ui/cli/app/
+-rw-r--r--   0 hjunior    (502) staff       (20)      125 2021-04-29 02:24:58.000000 hspylib-0.9.23/hspylib/ui/cli/app/__init__.py
+-rw-r--r--   0 hjunior    (502) staff       (20)     4826 2021-04-29 02:08:25.000000 hspylib-0.9.23/hspylib/ui/cli/app/application.py
+-rw-r--r--   0 hjunior    (502) staff       (20)     1171 2021-04-23 00:59:09.000000 hspylib-0.9.23/hspylib/ui/cli/app/option.py
+drwxr-xr-x   0 hjunior    (502) staff       (20)        0 2021-04-29 02:51:38.775647 hspylib-0.9.23/hspylib/ui/cli/factory/
+-rw-r--r--   0 hjunior    (502) staff       (20)      152 2021-04-29 02:24:58.000000 hspylib-0.9.23/hspylib/ui/cli/factory/__init__.py
+-rw-r--r--   0 hjunior    (502) staff       (20)      963 2021-04-15 21:52:40.000000 hspylib-0.9.23/hspylib/ui/cli/factory/menu_entry.py
+-rw-r--r--   0 hjunior    (502) staff       (20)     1013 2021-04-15 21:52:40.000000 hspylib-0.9.23/hspylib/ui/cli/factory/menu_factory.py
+-rw-r--r--   0 hjunior    (502) staff       (20)      566 2021-04-15 21:52:40.000000 hspylib-0.9.23/hspylib/ui/cli/factory/menu_option.py
+drwxr-xr-x   0 hjunior    (502) staff       (20)        0 2021-04-29 02:51:38.776668 hspylib-0.9.23/hspylib/ui/cli/icons/
+-rw-r--r--   0 hjunior    (502) staff       (20)      128 2021-04-29 02:24:58.000000 hspylib-0.9.23/hspylib/ui/cli/icons/__init__.py
+drwxr-xr-x   0 hjunior    (502) staff       (20)        0 2021-04-29 02:51:38.781969 hspylib-0.9.23/hspylib/ui/cli/icons/emojis/
+-rw-r--r--   0 hjunior    (502) staff       (20)      128 2021-04-29 02:24:58.000000 hspylib-0.9.23/hspylib/ui/cli/icons/emojis/__init__.py
+-rw-r--r--   0 hjunior    (502) staff       (20)      471 2021-04-27 19:50:29.000000 hspylib-0.9.23/hspylib/ui/cli/icons/emojis/emojis.py
+drwxr-xr-x   0 hjunior    (502) staff       (20)        0 2021-04-29 02:51:38.783589 hspylib-0.9.23/hspylib/ui/cli/icons/emojis/faces/
+-rw-r--r--   0 hjunior    (502) staff       (20)      128 2021-04-29 02:24:58.000000 hspylib-0.9.23/hspylib/ui/cli/icons/emojis/faces/__init__.py
+-rw-r--r--   0 hjunior    (502) staff       (20)      763 2021-04-15 21:52:40.000000 hspylib-0.9.23/hspylib/ui/cli/icons/emojis/faces/face_smiling.py
+drwxr-xr-x   0 hjunior    (502) staff       (20)        0 2021-04-29 02:51:38.785681 hspylib-0.9.23/hspylib/ui/cli/icons/font_awesome/
+-rw-r--r--   0 hjunior    (502) staff       (20)      140 2021-04-29 02:24:58.000000 hspylib-0.9.23/hspylib/ui/cli/icons/font_awesome/__init__.py
+-rw-r--r--   0 hjunior    (502) staff       (20)     1002 2021-04-28 02:38:09.000000 hspylib-0.9.23/hspylib/ui/cli/icons/font_awesome/awesome.py
+drwxr-xr-x   0 hjunior    (502) staff       (20)        0 2021-04-29 02:51:38.787224 hspylib-0.9.23/hspylib/ui/cli/icons/font_awesome/ui_compose/
+-rw-r--r--   0 hjunior    (502) staff       (20)      137 2021-04-29 02:24:58.000000 hspylib-0.9.23/hspylib/ui/cli/icons/font_awesome/ui_compose/__init__.py
+-rw-r--r--   0 hjunior    (502) staff       (20)     1072 2021-04-27 19:50:29.000000 hspylib-0.9.23/hspylib/ui/cli/icons/font_awesome/ui_compose/form_icons.py
+drwxr-xr-x   0 hjunior    (502) staff       (20)        0 2021-04-29 02:51:38.792701 hspylib-0.9.23/hspylib/ui/cli/menu/
+-rw-r--r--   0 hjunior    (502) staff       (20)      165 2021-04-29 02:24:58.000000 hspylib-0.9.23/hspylib/ui/cli/menu/__init__.py
+drwxr-xr-x   0 hjunior    (502) staff       (20)        0 2021-04-29 02:51:38.806131 hspylib-0.9.23/hspylib/ui/cli/menu/extra/
+-rw-r--r--   0 hjunior    (502) staff       (20)      159 2021-04-29 02:24:58.000000 hspylib-0.9.23/hspylib/ui/cli/menu/extra/__init__.py
+-rwxr-xr-x   0 hjunior    (502) staff       (20)     7623 2021-04-27 19:50:29.000000 hspylib-0.9.23/hspylib/ui/cli/menu/extra/mchoose.py
+-rwxr-xr-x   0 hjunior    (502) staff       (20)     6940 2021-04-28 15:08:18.000000 hspylib-0.9.23/hspylib/ui/cli/menu/extra/mdashboard.py
+-rwxr-xr-x   0 hjunior    (502) staff       (20)    14021 2021-04-28 15:08:18.000000 hspylib-0.9.23/hspylib/ui/cli/menu/extra/minput.py
+-rwxr-xr-x   0 hjunior    (502) staff       (20)     6606 2021-04-20 01:03:01.000000 hspylib-0.9.23/hspylib/ui/cli/menu/extra/mselect.py
+-rw-r--r--   0 hjunior    (502) staff       (20)      704 2021-04-15 21:52:40.000000 hspylib-0.9.23/hspylib/ui/cli/menu/menu.py
+-rw-r--r--   0 hjunior    (502) staff       (20)     1575 2021-04-15 21:52:40.000000 hspylib-0.9.23/hspylib/ui/cli/menu/menu_item.py
+-rw-r--r--   0 hjunior    (502) staff       (20)      811 2021-04-15 21:52:40.000000 hspylib-0.9.23/hspylib/ui/cli/menu/menu_ui.py
+-rw-r--r--   0 hjunior    (502) staff       (20)     3312 2021-04-15 21:52:40.000000 hspylib-0.9.23/hspylib/ui/cli/menu/menu_utils.py
+drwxr-xr-x   0 hjunior    (502) staff       (20)        0 2021-04-29 02:51:38.807831 hspylib-0.9.23/hspylib/ui/cli/tables/
+-rw-r--r--   0 hjunior    (502) staff       (20)      118 2021-04-29 02:24:58.000000 hspylib-0.9.23/hspylib/ui/cli/tables/__init__.py
+-rw-r--r--   0 hjunior    (502) staff       (20)     5081 2021-04-15 21:52:40.000000 hspylib-0.9.23/hspylib/ui/cli/tables/table_renderer.py
+drwxr-xr-x   0 hjunior    (502) staff       (20)        0 2021-04-29 02:51:38.808897 hspylib-0.9.23/hspylib/ui/cli/tools/
+-rw-r--r--   0 hjunior    (502) staff       (20)      112 2021-04-29 02:24:58.000000 hspylib-0.9.23/hspylib/ui/cli/tools/__init__.py
+drwxr-xr-x   0 hjunior    (502) staff       (20)        0 2021-04-29 02:51:38.820039 hspylib-0.9.23/hspylib/ui/cli/tools/validator/
+-rw-r--r--   0 hjunior    (502) staff       (20)      131 2021-04-29 02:24:58.000000 hspylib-0.9.23/hspylib/ui/cli/tools/validator/__init__.py
+-rw-r--r--   0 hjunior    (502) staff       (20)      516 2021-04-23 03:34:04.000000 hspylib-0.9.23/hspylib/ui/cli/tools/validator/argument_validator.py
+drwxr-xr-x   0 hjunior    (502) staff       (20)        0 2021-04-29 02:51:38.824021 hspylib-0.9.23/hspylib/ui/cli/vt100/
+-rw-r--r--   0 hjunior    (502) staff       (20)      140 2021-04-29 02:24:58.000000 hspylib-0.9.23/hspylib/ui/cli/vt100/__init__.py
+-rw-r--r--   0 hjunior    (502) staff       (20)     2775 2021-04-27 19:50:29.000000 hspylib-0.9.23/hspylib/ui/cli/vt100/vt_100.py
+-rw-r--r--   0 hjunior    (502) staff       (20)     3047 2021-04-27 19:50:29.000000 hspylib-0.9.23/hspylib/ui/cli/vt100/vt_codes.py
+-rw-r--r--   0 hjunior    (502) staff       (20)     1556 2021-04-27 19:50:29.000000 hspylib-0.9.23/hspylib/ui/cli/vt100/vt_colors.py
+drwxr-xr-x   0 hjunior    (502) staff       (20)        0 2021-04-29 02:51:38.825998 hspylib-0.9.23/hspylib/ui/qt/
+-rw-r--r--   0 hjunior    (502) staff       (20)      146 2021-04-29 02:24:58.000000 hspylib-0.9.23/hspylib/ui/qt/__init__.py
+drwxr-xr-x   0 hjunior    (502) staff       (20)        0 2021-04-29 02:51:38.826992 hspylib-0.9.23/hspylib/ui/qt/forms/
+-rw-r--r--   0 hjunior    (502) staff       (20)      100 2021-04-29 02:24:58.000000 hspylib-0.9.23/hspylib/ui/qt/forms/__init__.py
+drwxr-xr-x   0 hjunior    (502) staff       (20)        0 2021-04-29 02:51:38.833069 hspylib-0.9.23/hspylib/ui/qt/promotions/
+-rw-r--r--   0 hjunior    (502) staff       (20)      156 2021-04-29 02:24:58.000000 hspylib-0.9.23/hspylib/ui/qt/promotions/__init__.py
+-rw-r--r--   0 hjunior    (502) staff       (20)      268 2021-04-15 21:52:40.000000 hspylib-0.9.23/hspylib/ui/qt/promotions/button_label.py
+-rw-r--r--   0 hjunior    (502) staff       (20)     2201 2021-04-27 19:50:29.000000 hspylib-0.9.23/hspylib/ui/qt/promotions/entity_table_model.py
+-rw-r--r--   0 hjunior    (502) staff       (20)      280 2021-04-15 21:52:40.000000 hspylib-0.9.23/hspylib/ui/qt/promotions/panel.py
+-rw-r--r--   0 hjunior    (502) staff       (20)     2015 2021-04-15 21:52:40.000000 hspylib-0.9.23/hspylib/ui/qt/qt_finder.py
+drwxr-xr-x   0 hjunior    (502) staff       (20)        0 2021-04-29 02:51:38.834559 hspylib-0.9.23/hspylib/ui/qt/views/
+-rw-r--r--   0 hjunior    (502) staff       (20)      125 2021-04-29 02:24:58.000000 hspylib-0.9.23/hspylib/ui/qt/views/__init__.py
+-rw-r--r--   0 hjunior    (502) staff       (20)      466 2021-04-27 19:50:29.000000 hspylib-0.9.23/hspylib/ui/qt/views/main_view.py
+-rw-r--r--   0 hjunior    (502) staff       (20)      377 2021-04-27 19:50:29.000000 hspylib-0.9.23/hspylib/ui/qt/views/qt_view.py
+-rw-r--r--   0 hjunior    (502) staff       (20)      214 2021-04-15 21:52:40.000000 hspylib-0.9.23/hspylib/welcome.txt
+drwxr-xr-x   0 hjunior    (502) staff       (20)        0 2021-04-29 02:51:38.722457 hspylib-0.9.23/hspylib.egg-info/
+-rw-r--r--   0 hjunior    (502) staff       (20)      559 2021-04-29 02:51:38.000000 hspylib-0.9.23/hspylib.egg-info/PKG-INFO
+-rw-r--r--   0 hjunior    (502) staff       (20)     4195 2021-04-29 02:51:38.000000 hspylib-0.9.23/hspylib.egg-info/SOURCES.txt
+-rw-r--r--   0 hjunior    (502) staff       (20)        1 2021-04-29 02:51:38.000000 hspylib-0.9.23/hspylib.egg-info/dependency_links.txt
+-rw-r--r--   0 hjunior    (502) staff       (20)      104 2021-04-29 02:51:38.000000 hspylib-0.9.23/hspylib.egg-info/requires.txt
+-rw-r--r--   0 hjunior    (502) staff       (20)        8 2021-04-29 02:51:38.000000 hspylib-0.9.23/hspylib.egg-info/top_level.txt
+-rw-r--r--   0 hjunior    (502) staff       (20)       38 2021-04-29 02:51:38.836646 hspylib-0.9.23/setup.cfg
+-rw-r--r--   0 hjunior    (502) staff       (20)     1148 2021-04-28 15:47:15.000000 hspylib-0.9.23/setup.py
```

### filetype from file(1)

```diff
@@ -1 +1 @@
-POSIX tar archive (GNU)
+POSIX tar archive
```

### Comparing `hspylib-0.9.22/PKG-INFO` & `hspylib-0.9.23/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,17 +1,17 @@
 Metadata-Version: 2.1
 Name: hspylib
-Version: 0.9.22
+Version: 0.9.23
 Summary: HomeSetup python library
 Home-page: https://github.com/yorevs/hspylib
 Author: Hugo Saporetti Junior
 Author-email: yorevs@hotmail.com
 License: MIT
 Description: # hspylib
 Platform: UNKNOWN
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Operating System :: OS Independent
-Requires-Python: >=3.6
+Requires-Python: >=3.7
 Description-Content-Type: text/markdown
```

### Comparing `hspylib-0.9.22/hspylib/core/config/app_config.py` & `hspylib-0.9.23/hspylib/core/config/app_config.py`

 * *Files identical despite different names*

### Comparing `hspylib-0.9.22/hspylib/core/config/properties.py` & `hspylib-0.9.23/hspylib/core/config/properties.py`

 * *Files identical despite different names*

### Comparing `hspylib-0.9.22/hspylib/core/crud/crud_repository.py` & `hspylib-0.9.23/hspylib/core/crud/crud_repository.py`

 * *Files identical despite different names*

### Comparing `hspylib-0.9.22/hspylib/core/crud/crud_service.py` & `hspylib-0.9.23/hspylib/core/crud/crud_service.py`

 * *Files identical despite different names*

### Comparing `hspylib-0.9.22/hspylib/core/crud/db/db_repository.py` & `hspylib-0.9.23/hspylib/core/crud/db/db_repository.py`

 * *Files identical despite different names*

### Comparing `hspylib-0.9.22/hspylib/core/crud/db/firebase/firebase_config.py` & `hspylib-0.9.23/hspylib/core/crud/db/firebase/firebase_config.py`

 * *Files 2% similar despite different names*

```diff
@@ -66,15 +66,15 @@
         self.passphrase = passphrase if passphrase else AppConfigs.INSTANCE['firebase.passphrase']
         assert self.project_id, "Project ID must be defined"
         assert self.database, "Database name must be defined"
         assert self.username, "Username must be defined"
         self.set_passphrase()
         self.project_uuid = str(self.project_uuid) if self.project_uuid else str(uuid.uuid4())
         assert self.validate_config(), "Your Firebase configuration is not valid"
-        log.debug('Successfully connected to Firebase: {}'.format(self.base_url()))
+        log.debug(f'Successfully connected to Firebase: {self.base_url()}')
 
     def __str__(self):
         return FB_CONFIG_FMT.format(
             self.project_id,
             self.username,
             self.database,
             str(base64.b64encode(self.passphrase.encode(self.encoding)), encoding=self.encoding),
```

### Comparing `hspylib-0.9.22/hspylib/core/crud/db/firebase/firebase_repository.py` & `hspylib-0.9.23/hspylib/core/crud/db/firebase/firebase_repository.py`

 * *Files identical despite different names*

### Comparing `hspylib-0.9.22/hspylib/core/crud/db/mysql/mysql_repository.py` & `hspylib-0.9.23/hspylib/core/crud/db/mysql/mysql_repository.py`

 * *Files identical despite different names*

### Comparing `hspylib-0.9.22/hspylib/core/crud/db/sql_factory.py` & `hspylib-0.9.23/hspylib/core/crud/db/sql_factory.py`

 * *Files identical despite different names*

### Comparing `hspylib-0.9.22/hspylib/core/crud/file/file_repository.py` & `hspylib-0.9.23/hspylib/core/crud/file/file_repository.py`

 * *Files identical despite different names*

### Comparing `hspylib-0.9.22/hspylib/core/crud/file/file_storage.py` & `hspylib-0.9.23/hspylib/core/crud/file/file_storage.py`

 * *Files identical despite different names*

### Comparing `hspylib-0.9.22/hspylib/core/enum/charset.py` & `hspylib-0.9.23/hspylib/core/enum/charset.py`

 * *Files identical despite different names*

### Comparing `hspylib-0.9.22/hspylib/core/enum/content_type.py` & `hspylib-0.9.23/hspylib/core/enum/content_type.py`

 * *Files identical despite different names*

### Comparing `hspylib-0.9.22/hspylib/core/enum/enumeration.py` & `hspylib-0.9.23/hspylib/core/enum/enumeration.py`

 * *Files 15% similar despite different names*

```diff
@@ -14,18 +14,18 @@
 
     @classmethod
     def value_of(cls, name: str, ignore_case: bool = False) -> Any:
         if ignore_case:
             found = next(filter(lambda en: en.name.upper() == name.upper(), list(cls)), None)
         else:
             found = next(filter(lambda en: en.name == name, list(cls)), None)
-        assert found, f"{name} is not a valid \"{cls.__name__}\" name"
+        assert found, f"{name} name is not a valid \"{cls.__name__}\""
         return found
 
     @classmethod
     def of_value(cls, value: Any, ignore_case: bool = False) -> Any:
         if ignore_case:
             found = next(filter(lambda en: str(en.value).upper() == str(value).upper(), list(cls)), None)
         else:
             found = next(filter(lambda en: en.value == value, list(cls)), None)
-        assert found, f"{value} does not correspond to a valid \"{cls.__name__}\""
+        assert found, f"\"{value}\" value does not correspond to a valid \"{cls.__name__}\""
         return found
```

### Comparing `hspylib-0.9.22/hspylib/core/enum/http_code.py` & `hspylib-0.9.23/hspylib/core/enum/http_code.py`

 * *Files identical despite different names*

### Comparing `hspylib-0.9.22/hspylib/core/model/entity.py` & `hspylib-0.9.23/hspylib/core/model/entity.py`

 * *Files identical despite different names*

### Comparing `hspylib-0.9.22/hspylib/core/tools/commons.py` & `hspylib-0.9.23/hspylib/core/tools/commons.py`

 * *Files 1% similar despite different names*

```diff
@@ -44,16 +44,16 @@
 
     return log
 
 
 def __version__(version_filepath: str = ".version") -> Optional[Tuple]:
     """Retrieve the version from the version file in the form: Tuple[major,minor,build]"""
     try:
-        with open(version_filepath) as fh:
-            return tuple(map(str.strip, fh.read().split('.')))
+        with open(version_filepath) as fh_version:
+            return tuple(map(str.strip, fh_version.read().split('.')))
     except FileNotFoundError:
         return None
 
 
 def __curdir__(filepath: str) -> str:
     """Retrieve the application directory"""
     return os.path.dirname(os.path.realpath(filepath))
```

### Comparing `hspylib-0.9.22/hspylib/core/tools/keyboard.py` & `hspylib-0.9.23/hspylib/core/tools/keyboard.py`

 * *Files identical despite different names*

### Comparing `hspylib-0.9.22/hspylib/core/tools/text_helper.py` & `hspylib-0.9.23/hspylib/core/tools/text_helper.py`

 * *Files identical despite different names*

### Comparing `hspylib-0.9.22/hspylib/core/tools/validator.py` & `hspylib-0.9.23/hspylib/core/tools/validator.py`

 * *Files identical despite different names*

### Comparing `hspylib-0.9.22/hspylib/modules/eventbus/eventbus.py` & `hspylib-0.9.23/hspylib/modules/eventbus/eventbus.py`

 * *Files identical despite different names*

### Comparing `hspylib-0.9.22/hspylib/modules/fetch/fetch.py` & `hspylib-0.9.23/hspylib/modules/fetch/fetch.py`

 * *Files identical despite different names*

### Comparing `hspylib-0.9.22/hspylib/modules/fetch/http_response.py` & `hspylib-0.9.23/hspylib/modules/fetch/http_response.py`

 * *Files identical despite different names*

### Comparing `hspylib-0.9.22/hspylib/modules/json_search/json_search.py` & `hspylib-0.9.23/hspylib/modules/json_search/json_search.py`

 * *Files identical despite different names*

### Comparing `hspylib-0.9.22/hspylib/modules/mock/mock_request.py` & `hspylib-0.9.23/hspylib/modules/mock/mock_request.py`

 * *Files identical despite different names*

### Comparing `hspylib-0.9.22/hspylib/modules/mock/mock_server.py` & `hspylib-0.9.23/hspylib/modules/mock/mock_server.py`

 * *Files identical despite different names*

### Comparing `hspylib-0.9.22/hspylib/modules/mock/mock_server_handler.py` & `hspylib-0.9.23/hspylib/modules/mock/mock_server_handler.py`

 * *Files identical despite different names*

### Comparing `hspylib-0.9.22/hspylib/modules/security/security.py` & `hspylib-0.9.23/hspylib/modules/security/security.py`

 * *Files identical despite different names*

### Comparing `hspylib-0.9.22/hspylib/modules/web/rest_utils.py` & `hspylib-0.9.23/hspylib/modules/web/rest_utils.py`

 * *Files identical despite different names*

### Comparing `hspylib-0.9.22/hspylib/modules/web/soap_utils.py` & `hspylib-0.9.23/hspylib/modules/web/soap_utils.py`

 * *Files identical despite different names*

### Comparing `hspylib-0.9.22/hspylib/ui/cli/app/application.py` & `hspylib-0.9.23/hspylib/ui/cli/app/application.py`

 * *Files 4% similar despite different names*

```diff
@@ -13,15 +13,15 @@
 class Application(metaclass=Singleton):
     """TODO"""
 
     def __init__(
             self,
             app_name: str,
             app_version: Tuple[int, int, int],
-            app_usage: str = "Usage: main.py <option> [arguments]",
+            app_usage: str = "Usage: __main__.py [options] <arguments>",
             source_dir: str = None,
             resource_dir: str = None,
             log_dir: str = None):
 
         signal.signal(signal.SIGINT, self.exit_handler)
         self.app_name = app_name
         self.app_version = app_version
@@ -63,23 +63,25 @@
             log.info('Exit handler called')
             exit_code = signum
         self.cleanup()
         if clear_screen:
             sysout('%ED2%%HOM%')
         sys.exit(exit_code)
 
-    def usage(self, exit_code: int = 0) -> None:
+    def usage(self, *args) -> None:
         """Display the usage message and exit with the specified code ( or zero as default )
-        :param exit_code: The application exit code
+        :param args: The application arguments
         """
         sysout(self.app_usage)
-        self.exit_handler(exit_code)
+        self.exit_handler(args[0] or 0)
 
-    def version(self) -> None:
-        """Display the current program version and exit"""
+    def version(self, *args) -> None:
+        """Display the current program version and exit
+        :param args: The application arguments
+        """
         sysout('{} v{}'.format(self.app_name, '.'.join(map(str, self.app_version))))
         self.exit_handler()
 
     def parse_arguments(self, arguments: List[str]) -> None:
         """ Handle program arguments and options. Short opts: -<C>, Long opts: --<Word>
         :param arguments: The list of unparsed program arguments passed by the command line
         """
```

### Comparing `hspylib-0.9.22/hspylib/ui/cli/app/option.py` & `hspylib-0.9.23/hspylib/ui/cli/app/option.py`

 * *Files identical despite different names*

### Comparing `hspylib-0.9.22/hspylib/ui/cli/factory/menu_entry.py` & `hspylib-0.9.23/hspylib/ui/cli/factory/menu_entry.py`

 * *Files identical despite different names*

### Comparing `hspylib-0.9.22/hspylib/ui/cli/factory/menu_factory.py` & `hspylib-0.9.23/hspylib/ui/cli/factory/menu_factory.py`

 * *Files identical despite different names*

### Comparing `hspylib-0.9.22/hspylib/ui/cli/factory/menu_option.py` & `hspylib-0.9.23/hspylib/ui/cli/factory/menu_option.py`

 * *Files identical despite different names*

### Comparing `hspylib-0.9.22/hspylib/ui/cli/icons/emojis/faces/face_smiling.py` & `hspylib-0.9.23/hspylib/ui/cli/icons/emojis/faces/face_smiling.py`

 * *Files identical despite different names*

### Comparing `hspylib-0.9.22/hspylib/ui/cli/icons/font_awesome/awesome.py` & `hspylib-0.9.23/hspylib/ui/cli/icons/font_awesome/awesome.py`

 * *Files identical despite different names*

### Comparing `hspylib-0.9.22/hspylib/ui/cli/icons/font_awesome/ui_compose/form_icons.py` & `hspylib-0.9.23/hspylib/ui/cli/icons/font_awesome/ui_compose/form_icons.py`

 * *Files identical despite different names*

### Comparing `hspylib-0.9.22/hspylib/ui/cli/menu/extra/mchoose.py` & `hspylib-0.9.23/hspylib/ui/cli/menu/extra/mchoose.py`

 * *Files identical despite different names*

### Comparing `hspylib-0.9.22/hspylib/ui/cli/menu/extra/mdashboard.py` & `hspylib-0.9.23/hspylib/ui/cli/menu/extra/mdashboard.py`

 * *Files identical despite different names*

### Comparing `hspylib-0.9.22/hspylib/ui/cli/menu/extra/minput.py` & `hspylib-0.9.23/hspylib/ui/cli/menu/extra/minput.py`

 * *Files identical despite different names*

### Comparing `hspylib-0.9.22/hspylib/ui/cli/menu/extra/mselect.py` & `hspylib-0.9.23/hspylib/ui/cli/menu/extra/mselect.py`

 * *Files identical despite different names*

### Comparing `hspylib-0.9.22/hspylib/ui/cli/menu/menu.py` & `hspylib-0.9.23/hspylib/ui/cli/menu/menu.py`

 * *Files identical despite different names*

### Comparing `hspylib-0.9.22/hspylib/ui/cli/menu/menu_item.py` & `hspylib-0.9.23/hspylib/ui/cli/menu/menu_item.py`

 * *Files identical despite different names*

### Comparing `hspylib-0.9.22/hspylib/ui/cli/menu/menu_ui.py` & `hspylib-0.9.23/hspylib/ui/cli/menu/menu_ui.py`

 * *Files identical despite different names*

### Comparing `hspylib-0.9.22/hspylib/ui/cli/menu/menu_utils.py` & `hspylib-0.9.23/hspylib/ui/cli/menu/menu_utils.py`

 * *Files identical despite different names*

### Comparing `hspylib-0.9.22/hspylib/ui/cli/tables/table_renderer.py` & `hspylib-0.9.23/hspylib/ui/cli/tables/table_renderer.py`

 * *Files identical despite different names*

### Comparing `hspylib-0.9.22/hspylib/ui/cli/tools/validator/argument_validator.py` & `hspylib-0.9.23/hspylib/ui/cli/tools/validator/argument_validator.py`

 * *Files identical despite different names*

### Comparing `hspylib-0.9.22/hspylib/ui/cli/vt100/vt_100.py` & `hspylib-0.9.23/hspylib/ui/cli/vt100/vt_100.py`

 * *Files identical despite different names*

### Comparing `hspylib-0.9.22/hspylib/ui/cli/vt100/vt_codes.py` & `hspylib-0.9.23/hspylib/ui/cli/vt100/vt_codes.py`

 * *Files identical despite different names*

### Comparing `hspylib-0.9.22/hspylib/ui/cli/vt100/vt_colors.py` & `hspylib-0.9.23/hspylib/ui/cli/vt100/vt_colors.py`

 * *Files identical despite different names*

### Comparing `hspylib-0.9.22/hspylib/ui/qt/promotions/entity_table_model.py` & `hspylib-0.9.23/hspylib/ui/qt/promotions/entity_table_model.py`

 * *Files identical despite different names*

### Comparing `hspylib-0.9.22/hspylib/ui/qt/qt_finder.py` & `hspylib-0.9.23/hspylib/ui/qt/qt_finder.py`

 * *Files identical despite different names*

### Comparing `hspylib-0.9.22/hspylib.egg-info/PKG-INFO` & `hspylib-0.9.23/hspylib.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,17 +1,17 @@
 Metadata-Version: 2.1
 Name: hspylib
-Version: 0.9.22
+Version: 0.9.23
 Summary: HomeSetup python library
 Home-page: https://github.com/yorevs/hspylib
 Author: Hugo Saporetti Junior
 Author-email: yorevs@hotmail.com
 License: MIT
 Description: # hspylib
 Platform: UNKNOWN
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Operating System :: OS Independent
-Requires-Python: >=3.6
+Requires-Python: >=3.7
 Description-Content-Type: text/markdown
```

### Comparing `hspylib-0.9.22/hspylib.egg-info/SOURCES.txt` & `hspylib-0.9.23/hspylib.egg-info/SOURCES.txt`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,14 @@
+MANIFEST.in
 README.md
 setup.py
+hspylib/.version
 hspylib/__init__.py
+hspylib/__main__.py
+hspylib/welcome.txt
 hspylib.egg-info/PKG-INFO
 hspylib.egg-info/SOURCES.txt
 hspylib.egg-info/dependency_links.txt
 hspylib.egg-info/requires.txt
 hspylib.egg-info/top_level.txt
 hspylib/core/__init__.py
 hspylib/core/config/__init__.py
@@ -18,15 +22,15 @@
 hspylib/core/crud/db/sql_factory.py
 hspylib/core/crud/db/firebase/__init__.py
 hspylib/core/crud/db/firebase/firebase_config.py
 hspylib/core/crud/db/firebase/firebase_repository.py
 hspylib/core/crud/db/mysql/__init__.py
 hspylib/core/crud/db/mysql/mysql_repository.py
 hspylib/core/crud/db/postgres/__init__.py
-hspylib/core/crud/db/sql/__init__.py
+hspylib/core/crud/db/sql/sql_stubs.sql
 hspylib/core/crud/file/__init__.py
 hspylib/core/crud/file/file_repository.py
 hspylib/core/crud/file/file_storage.py
 hspylib/core/enum/__init__.py
 hspylib/core/enum/charset.py
 hspylib/core/enum/content_type.py
 hspylib/core/enum/database_type.py
@@ -59,14 +63,19 @@
 hspylib/modules/mock/mock_server.py
 hspylib/modules/mock/mock_server_handler.py
 hspylib/modules/security/__init__.py
 hspylib/modules/security/security.py
 hspylib/modules/web/__init__.py
 hspylib/modules/web/rest_utils.py
 hspylib/modules/web/soap_utils.py
+hspylib/templates/tpl-build.gradle
+hspylib/templates/tpl-dependencies.gradle
+hspylib/templates/tpl-main.py
+hspylib/templates/tpl-run-it.sh
+hspylib/templates/tpl.gitignore
 hspylib/ui/__init__.py
 hspylib/ui/cli/__init__.py
 hspylib/ui/cli/app/__init__.py
 hspylib/ui/cli/app/application.py
 hspylib/ui/cli/app/option.py
 hspylib/ui/cli/factory/__init__.py
 hspylib/ui/cli/factory/menu_entry.py
```

### Comparing `hspylib-0.9.22/setup.py` & `hspylib-0.9.23/setup.py`

 * *Files 7% similar despite different names*

```diff
@@ -5,15 +5,15 @@
 # The directory containing this file
 HERE = pathlib.Path(__file__).parent
 
 # The text of the README file
 README = (HERE / "README.md").read_text()
 
 # The version of the package
-VERSION = (HERE / ".version").read_text()
+VERSION = (HERE / "hspylib/.version").read_text()
 
 # The package requirements
 REQUIREMENTS = list(filter(None, (HERE / "requirements.txt").read_text().splitlines()))
 
 # This call to setup() does all the work
 setuptools.setup(
     name='hspylib',
@@ -22,21 +22,18 @@
     author='Hugo Saporetti Junior',
     author_email='yorevs@hotmail.com',
     long_description=README,
     long_description_content_type="text/markdown",
     url="https://github.com/yorevs/hspylib",
     license='MIT',
     packages=setuptools.find_packages(),
-    package_data={
-        'hspylib.core.crud.db.sql': ['sql_stubs.sql']
-    },
     include_package_data=True,
     classifiers=[
         "License :: OSI Approved :: MIT License",
         "Programming Language :: Python :: 3.7",
         "Programming Language :: Python :: 3.8",
         "Programming Language :: Python :: 3.9",
         "Operating System :: OS Independent",
     ],
-    python_requires='>=3.6',
+    python_requires='>=3.7',
     install_requires=REQUIREMENTS,
 )
```

