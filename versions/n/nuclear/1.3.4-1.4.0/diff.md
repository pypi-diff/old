# Comparing `tmp/nuclear-1.3.4.tar.gz` & `tmp/nuclear-1.4.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "nuclear-1.3.4.tar", last modified: Tue Aug 16 13:24:24 2022, max compression
+gzip compressed data, was "nuclear-1.4.0.tar", last modified: Thu Apr  6 12:14:09 2023, max compression
```

## Comparing `nuclear-1.3.4.tar` & `nuclear-1.4.0.tar`

### file list

```diff
@@ -1,70 +1,73 @@
-drwxrwxr-x   0 ireneusz  (1001) ireneusz  (1001)        0 2022-08-16 13:24:24.240090 nuclear-1.3.4/
--rw-r--r--   0 ireneusz  (1001) ireneusz  (1001)     1063 2020-07-28 11:14:52.000000 nuclear-1.3.4/LICENSE
--rw-rw-r--   0 ireneusz  (1001) ireneusz  (1001)    18604 2022-08-16 13:24:24.240090 nuclear-1.3.4/PKG-INFO
--rw-rw-r--   0 ireneusz  (1001) ireneusz  (1001)    18152 2022-08-16 13:24:23.000000 nuclear-1.3.4/README.md
-drwxrwxr-x   0 ireneusz  (1001) ireneusz  (1001)        0 2022-08-16 13:24:24.232091 nuclear-1.3.4/nuclear/
--rw-r--r--   0 ireneusz  (1001) ireneusz  (1001)      505 2022-05-16 13:47:16.000000 nuclear-1.3.4/nuclear/__init__.py
-drwxrwxr-x   0 ireneusz  (1001) ireneusz  (1001)        0 2022-08-16 13:24:24.232091 nuclear-1.3.4/nuclear/args/
--rw-r--r--   0 ireneusz  (1001) ireneusz  (1001)        0 2020-07-28 11:14:52.000000 nuclear-1.3.4/nuclear/args/__init__.py
--rw-r--r--   0 ireneusz  (1001) ireneusz  (1001)     1399 2020-07-28 11:14:52.000000 nuclear-1.3.4/nuclear/args/args_que.py
--rw-r--r--   0 ireneusz  (1001) ireneusz  (1001)      504 2020-07-28 11:14:52.000000 nuclear-1.3.4/nuclear/args/container.py
-drwxrwxr-x   0 ireneusz  (1001) ireneusz  (1001)        0 2022-08-16 13:24:24.236091 nuclear-1.3.4/nuclear/autocomplete/
--rw-r--r--   0 ireneusz  (1001) ireneusz  (1001)        0 2020-07-28 11:14:52.000000 nuclear-1.3.4/nuclear/autocomplete/__init__.py
--rw-r--r--   0 ireneusz  (1001) ireneusz  (1001)     4445 2020-07-28 11:14:52.000000 nuclear-1.3.4/nuclear/autocomplete/autocomplete.py
--rw-r--r--   0 ireneusz  (1001) ireneusz  (1001)     2175 2022-04-12 16:38:36.000000 nuclear-1.3.4/nuclear/autocomplete/install.py
-drwxrwxr-x   0 ireneusz  (1001) ireneusz  (1001)        0 2022-08-16 13:24:24.236091 nuclear-1.3.4/nuclear/builder/
--rw-r--r--   0 ireneusz  (1001) ireneusz  (1001)        0 2020-07-28 11:14:52.000000 nuclear-1.3.4/nuclear/builder/__init__.py
--rw-rw-r--   0 ireneusz  (1001) ireneusz  (1001)     9263 2022-04-13 09:01:27.000000 nuclear-1.3.4/nuclear/builder/builder.py
--rw-rw-r--   0 ireneusz  (1001) ireneusz  (1001)     3752 2022-04-13 09:02:59.000000 nuclear-1.3.4/nuclear/builder/decorator_builder.py
--rw-rw-r--   0 ireneusz  (1001) ireneusz  (1001)     2974 2021-12-11 21:16:15.000000 nuclear-1.3.4/nuclear/builder/rule.py
--rw-r--r--   0 ireneusz  (1001) ireneusz  (1001)    11321 2022-04-13 09:13:28.000000 nuclear-1.3.4/nuclear/builder/rule_factory.py
--rw-r--r--   0 ireneusz  (1001) ireneusz  (1001)      227 2020-07-28 11:14:52.000000 nuclear-1.3.4/nuclear/builder/typedef.py
-drwxrwxr-x   0 ireneusz  (1001) ireneusz  (1001)        0 2022-08-16 13:24:24.236091 nuclear-1.3.4/nuclear/completers/
--rw-r--r--   0 ireneusz  (1001) ireneusz  (1001)       33 2020-07-28 11:14:52.000000 nuclear-1.3.4/nuclear/completers/__init__.py
--rw-r--r--   0 ireneusz  (1001) ireneusz  (1001)      739 2020-07-28 11:14:52.000000 nuclear-1.3.4/nuclear/completers/file.py
-drwxrwxr-x   0 ireneusz  (1001) ireneusz  (1001)        0 2022-08-16 13:24:24.236091 nuclear-1.3.4/nuclear/help/
--rw-r--r--   0 ireneusz  (1001) ireneusz  (1001)        0 2020-07-28 11:14:52.000000 nuclear-1.3.4/nuclear/help/__init__.py
--rw-r--r--   0 ireneusz  (1001) ireneusz  (1001)    11836 2022-04-13 09:11:11.000000 nuclear-1.3.4/nuclear/help/help.py
-drwxrwxr-x   0 ireneusz  (1001) ireneusz  (1001)        0 2022-08-16 13:24:24.236091 nuclear-1.3.4/nuclear/parser/
--rw-r--r--   0 ireneusz  (1001) ireneusz  (1001)        0 2020-07-28 11:14:52.000000 nuclear-1.3.4/nuclear/parser/__init__.py
--rw-r--r--   0 ireneusz  (1001) ireneusz  (1001)      442 2020-07-28 11:14:52.000000 nuclear-1.3.4/nuclear/parser/context.py
--rw-r--r--   0 ireneusz  (1001) ireneusz  (1001)      449 2020-07-28 11:14:52.000000 nuclear-1.3.4/nuclear/parser/error.py
--rw-rw-r--   0 ireneusz  (1001) ireneusz  (1001)     1843 2021-12-11 21:16:15.000000 nuclear-1.3.4/nuclear/parser/inject.py
--rw-r--r--   0 ireneusz  (1001) ireneusz  (1001)      326 2020-07-28 11:14:52.000000 nuclear-1.3.4/nuclear/parser/internal_vars.py
--rw-r--r--   0 ireneusz  (1001) ireneusz  (1001)      666 2020-07-28 11:14:52.000000 nuclear-1.3.4/nuclear/parser/keyword.py
--rw-r--r--   0 ireneusz  (1001) ireneusz  (1001)     1378 2020-07-28 11:14:52.000000 nuclear-1.3.4/nuclear/parser/matcher.py
--rw-r--r--   0 ireneusz  (1001) ireneusz  (1001)    12607 2022-05-12 13:06:55.000000 nuclear-1.3.4/nuclear/parser/parser.py
--rw-r--r--   0 ireneusz  (1001) ireneusz  (1001)      409 2020-07-28 11:14:52.000000 nuclear-1.3.4/nuclear/parser/transform.py
--rw-rw-r--   0 ireneusz  (1001) ireneusz  (1001)     3826 2021-12-11 21:16:15.000000 nuclear-1.3.4/nuclear/parser/validate.py
--rw-rw-r--   0 ireneusz  (1001) ireneusz  (1001)     1886 2022-05-13 09:22:45.000000 nuclear-1.3.4/nuclear/parser/value.py
-drwxrwxr-x   0 ireneusz  (1001) ireneusz  (1001)        0 2022-08-16 13:24:24.236091 nuclear-1.3.4/nuclear/shell/
--rw-rw-r--   0 ireneusz  (1001) ireneusz  (1001)      123 2022-05-16 13:47:34.000000 nuclear-1.3.4/nuclear/shell/__init__.py
--rw-rw-r--   0 ireneusz  (1001) ireneusz  (1001)     4734 2022-08-16 13:22:26.000000 nuclear-1.3.4/nuclear/shell/background_cmd.py
--rw-r--r--   0 ireneusz  (1001) ireneusz  (1001)     3676 2022-05-16 13:53:00.000000 nuclear-1.3.4/nuclear/shell/shell_utils.py
-drwxrwxr-x   0 ireneusz  (1001) ireneusz  (1001)        0 2022-08-16 13:24:24.236091 nuclear-1.3.4/nuclear/sublog/
--rw-r--r--   0 ireneusz  (1001) ireneusz  (1001)      309 2022-06-08 11:51:00.000000 nuclear-1.3.4/nuclear/sublog/__init__.py
--rw-rw-r--   0 ireneusz  (1001) ireneusz  (1001)     3546 2022-06-08 12:00:57.000000 nuclear-1.3.4/nuclear/sublog/catch.py
--rw-rw-r--   0 ireneusz  (1001) ireneusz  (1001)     4039 2022-04-13 09:02:02.000000 nuclear-1.3.4/nuclear/sublog/context_logger.py
--rw-rw-r--   0 ireneusz  (1001) ireneusz  (1001)      843 2022-06-08 12:04:08.000000 nuclear-1.3.4/nuclear/sublog/wrap_error.py
-drwxrwxr-x   0 ireneusz  (1001) ireneusz  (1001)        0 2022-08-16 13:24:24.236091 nuclear-1.3.4/nuclear/types/
--rw-r--r--   0 ireneusz  (1001) ireneusz  (1001)        0 2020-07-28 11:14:52.000000 nuclear-1.3.4/nuclear/types/__init__.py
--rw-r--r--   0 ireneusz  (1001) ireneusz  (1001)       94 2020-07-28 11:14:52.000000 nuclear-1.3.4/nuclear/types/boolean.py
--rw-r--r--   0 ireneusz  (1001) ireneusz  (1001)      358 2020-07-28 11:14:52.000000 nuclear-1.3.4/nuclear/types/filesystem.py
--rw-r--r--   0 ireneusz  (1001) ireneusz  (1001)     1189 2020-07-28 11:14:52.000000 nuclear-1.3.4/nuclear/types/time.py
-drwxrwxr-x   0 ireneusz  (1001) ireneusz  (1001)        0 2022-08-16 13:24:24.240090 nuclear-1.3.4/nuclear/utils/
--rw-r--r--   0 ireneusz  (1001) ireneusz  (1001)        0 2022-04-12 16:16:19.000000 nuclear-1.3.4/nuclear/utils/__init__.py
--rw-r--r--   0 ireneusz  (1001) ireneusz  (1001)      629 2020-07-28 11:14:52.000000 nuclear-1.3.4/nuclear/utils/files.py
--rw-r--r--   0 ireneusz  (1001) ireneusz  (1001)      138 2020-07-28 11:14:52.000000 nuclear-1.3.4/nuclear/utils/input.py
--rw-r--r--   0 ireneusz  (1001) ireneusz  (1001)     1298 2020-07-28 11:14:52.000000 nuclear-1.3.4/nuclear/utils/regex.py
--rw-rw-r--   0 ireneusz  (1001) ireneusz  (1001)      112 2022-04-12 16:39:09.000000 nuclear-1.3.4/nuclear/utils/shell.py
--rw-r--r--   0 ireneusz  (1001) ireneusz  (1001)      688 2020-07-28 11:14:52.000000 nuclear-1.3.4/nuclear/utils/strings.py
--rw-r--r--   0 ireneusz  (1001) ireneusz  (1001)      362 2020-07-28 11:14:52.000000 nuclear-1.3.4/nuclear/utils/time.py
--rw-rw-r--   0 ireneusz  (1001) ireneusz  (1001)       22 2022-08-16 13:23:04.000000 nuclear-1.3.4/nuclear/version.py
-drwxrwxr-x   0 ireneusz  (1001) ireneusz  (1001)        0 2022-08-16 13:24:24.232091 nuclear-1.3.4/nuclear.egg-info/
--rw-rw-r--   0 ireneusz  (1001) ireneusz  (1001)    18604 2022-08-16 13:24:23.000000 nuclear-1.3.4/nuclear.egg-info/PKG-INFO
--rw-rw-r--   0 ireneusz  (1001) ireneusz  (1001)     1432 2022-08-16 13:24:24.000000 nuclear-1.3.4/nuclear.egg-info/SOURCES.txt
--rw-rw-r--   0 ireneusz  (1001) ireneusz  (1001)        1 2022-08-16 13:24:23.000000 nuclear-1.3.4/nuclear.egg-info/dependency_links.txt
--rw-rw-r--   0 ireneusz  (1001) ireneusz  (1001)       48 2022-08-16 13:24:24.000000 nuclear-1.3.4/nuclear.egg-info/requires.txt
--rw-rw-r--   0 ireneusz  (1001) ireneusz  (1001)        8 2022-08-16 13:24:24.000000 nuclear-1.3.4/nuclear.egg-info/top_level.txt
--rw-rw-r--   0 ireneusz  (1001) ireneusz  (1001)       38 2022-08-16 13:24:24.240090 nuclear-1.3.4/setup.cfg
--rw-r--r--   0 ireneusz  (1001) ireneusz  (1001)      866 2022-04-13 08:25:38.000000 nuclear-1.3.4/setup.py
+drwxrwxr-x   0 ireneusz  (1001) ireneusz  (1001)        0 2023-04-06 12:14:09.963242 nuclear-1.4.0/
+-rw-r--r--   0 ireneusz  (1001) ireneusz  (1001)     1063 2020-07-28 11:14:52.000000 nuclear-1.4.0/LICENSE
+-rw-rw-r--   0 ireneusz  (1001) ireneusz  (1001)    18604 2023-04-06 12:14:09.963242 nuclear-1.4.0/PKG-INFO
+-rw-rw-r--   0 ireneusz  (1001) ireneusz  (1001)    18152 2023-04-06 12:14:09.000000 nuclear-1.4.0/README.md
+drwxrwxr-x   0 ireneusz  (1001) ireneusz  (1001)        0 2023-04-06 12:14:09.959242 nuclear-1.4.0/nuclear/
+-rw-r--r--   0 ireneusz  (1001) ireneusz  (1001)      571 2023-04-06 10:36:33.000000 nuclear-1.4.0/nuclear/__init__.py
+drwxrwxr-x   0 ireneusz  (1001) ireneusz  (1001)        0 2023-04-06 12:14:09.959242 nuclear-1.4.0/nuclear/args/
+-rw-r--r--   0 ireneusz  (1001) ireneusz  (1001)        0 2020-07-28 11:14:52.000000 nuclear-1.4.0/nuclear/args/__init__.py
+-rw-r--r--   0 ireneusz  (1001) ireneusz  (1001)     1399 2020-07-28 11:14:52.000000 nuclear-1.4.0/nuclear/args/args_que.py
+-rw-r--r--   0 ireneusz  (1001) ireneusz  (1001)      504 2020-07-28 11:14:52.000000 nuclear-1.4.0/nuclear/args/container.py
+drwxrwxr-x   0 ireneusz  (1001) ireneusz  (1001)        0 2023-04-06 12:14:09.959242 nuclear-1.4.0/nuclear/autocomplete/
+-rw-r--r--   0 ireneusz  (1001) ireneusz  (1001)        0 2020-07-28 11:14:52.000000 nuclear-1.4.0/nuclear/autocomplete/__init__.py
+-rw-r--r--   0 ireneusz  (1001) ireneusz  (1001)     4445 2020-07-28 11:14:52.000000 nuclear-1.4.0/nuclear/autocomplete/autocomplete.py
+-rw-r--r--   0 ireneusz  (1001) ireneusz  (1001)     2175 2022-04-12 16:38:36.000000 nuclear-1.4.0/nuclear/autocomplete/install.py
+drwxrwxr-x   0 ireneusz  (1001) ireneusz  (1001)        0 2023-04-06 12:14:09.959242 nuclear-1.4.0/nuclear/builder/
+-rw-r--r--   0 ireneusz  (1001) ireneusz  (1001)        0 2020-07-28 11:14:52.000000 nuclear-1.4.0/nuclear/builder/__init__.py
+-rw-rw-r--   0 ireneusz  (1001) ireneusz  (1001)     9263 2022-04-13 09:01:27.000000 nuclear-1.4.0/nuclear/builder/builder.py
+-rw-rw-r--   0 ireneusz  (1001) ireneusz  (1001)     3752 2022-04-13 09:02:59.000000 nuclear-1.4.0/nuclear/builder/decorator_builder.py
+-rw-rw-r--   0 ireneusz  (1001) ireneusz  (1001)     2974 2021-12-11 21:16:15.000000 nuclear-1.4.0/nuclear/builder/rule.py
+-rw-r--r--   0 ireneusz  (1001) ireneusz  (1001)    11321 2022-04-13 09:13:28.000000 nuclear-1.4.0/nuclear/builder/rule_factory.py
+-rw-r--r--   0 ireneusz  (1001) ireneusz  (1001)      227 2020-07-28 11:14:52.000000 nuclear-1.4.0/nuclear/builder/typedef.py
+drwxrwxr-x   0 ireneusz  (1001) ireneusz  (1001)        0 2023-04-06 12:14:09.959242 nuclear-1.4.0/nuclear/completers/
+-rw-r--r--   0 ireneusz  (1001) ireneusz  (1001)       33 2020-07-28 11:14:52.000000 nuclear-1.4.0/nuclear/completers/__init__.py
+-rw-r--r--   0 ireneusz  (1001) ireneusz  (1001)      739 2020-07-28 11:14:52.000000 nuclear-1.4.0/nuclear/completers/file.py
+drwxrwxr-x   0 ireneusz  (1001) ireneusz  (1001)        0 2023-04-06 12:14:09.959242 nuclear-1.4.0/nuclear/help/
+-rw-r--r--   0 ireneusz  (1001) ireneusz  (1001)        0 2020-07-28 11:14:52.000000 nuclear-1.4.0/nuclear/help/__init__.py
+-rw-r--r--   0 ireneusz  (1001) ireneusz  (1001)    11775 2023-03-13 13:40:47.000000 nuclear-1.4.0/nuclear/help/help.py
+drwxrwxr-x   0 ireneusz  (1001) ireneusz  (1001)        0 2023-04-06 12:14:09.959242 nuclear-1.4.0/nuclear/inspection/
+-rw-r--r--   0 ireneusz  (1001) ireneusz  (1001)        0 2023-04-03 14:03:48.000000 nuclear-1.4.0/nuclear/inspection/__init__.py
+-rw-rw-r--   0 ireneusz  (1001) ireneusz  (1001)    10314 2023-04-06 12:05:54.000000 nuclear-1.4.0/nuclear/inspection/inspection.py
+drwxrwxr-x   0 ireneusz  (1001) ireneusz  (1001)        0 2023-04-06 12:14:09.959242 nuclear-1.4.0/nuclear/parser/
+-rw-r--r--   0 ireneusz  (1001) ireneusz  (1001)        0 2020-07-28 11:14:52.000000 nuclear-1.4.0/nuclear/parser/__init__.py
+-rw-r--r--   0 ireneusz  (1001) ireneusz  (1001)      442 2020-07-28 11:14:52.000000 nuclear-1.4.0/nuclear/parser/context.py
+-rw-r--r--   0 ireneusz  (1001) ireneusz  (1001)      449 2020-07-28 11:14:52.000000 nuclear-1.4.0/nuclear/parser/error.py
+-rw-rw-r--   0 ireneusz  (1001) ireneusz  (1001)     1843 2021-12-11 21:16:15.000000 nuclear-1.4.0/nuclear/parser/inject.py
+-rw-r--r--   0 ireneusz  (1001) ireneusz  (1001)      326 2020-07-28 11:14:52.000000 nuclear-1.4.0/nuclear/parser/internal_vars.py
+-rw-r--r--   0 ireneusz  (1001) ireneusz  (1001)      666 2020-07-28 11:14:52.000000 nuclear-1.4.0/nuclear/parser/keyword.py
+-rw-r--r--   0 ireneusz  (1001) ireneusz  (1001)     1378 2020-07-28 11:14:52.000000 nuclear-1.4.0/nuclear/parser/matcher.py
+-rw-r--r--   0 ireneusz  (1001) ireneusz  (1001)    12607 2022-05-12 13:06:55.000000 nuclear-1.4.0/nuclear/parser/parser.py
+-rw-r--r--   0 ireneusz  (1001) ireneusz  (1001)      409 2020-07-28 11:14:52.000000 nuclear-1.4.0/nuclear/parser/transform.py
+-rw-rw-r--   0 ireneusz  (1001) ireneusz  (1001)     3826 2021-12-11 21:16:15.000000 nuclear-1.4.0/nuclear/parser/validate.py
+-rw-rw-r--   0 ireneusz  (1001) ireneusz  (1001)     1886 2022-05-13 09:22:45.000000 nuclear-1.4.0/nuclear/parser/value.py
+drwxrwxr-x   0 ireneusz  (1001) ireneusz  (1001)        0 2023-04-06 12:14:09.959242 nuclear-1.4.0/nuclear/shell/
+-rw-rw-r--   0 ireneusz  (1001) ireneusz  (1001)      123 2022-05-16 13:47:34.000000 nuclear-1.4.0/nuclear/shell/__init__.py
+-rw-rw-r--   0 ireneusz  (1001) ireneusz  (1001)     4734 2022-08-16 13:22:26.000000 nuclear-1.4.0/nuclear/shell/background_cmd.py
+-rw-r--r--   0 ireneusz  (1001) ireneusz  (1001)     3676 2022-05-16 13:53:00.000000 nuclear-1.4.0/nuclear/shell/shell_utils.py
+drwxrwxr-x   0 ireneusz  (1001) ireneusz  (1001)        0 2023-04-06 12:14:09.959242 nuclear-1.4.0/nuclear/sublog/
+-rw-r--r--   0 ireneusz  (1001) ireneusz  (1001)      309 2022-06-08 11:51:00.000000 nuclear-1.4.0/nuclear/sublog/__init__.py
+-rw-rw-r--   0 ireneusz  (1001) ireneusz  (1001)     3546 2022-06-08 12:00:57.000000 nuclear-1.4.0/nuclear/sublog/catch.py
+-rw-rw-r--   0 ireneusz  (1001) ireneusz  (1001)     4039 2022-04-13 09:02:02.000000 nuclear-1.4.0/nuclear/sublog/context_logger.py
+-rw-rw-r--   0 ireneusz  (1001) ireneusz  (1001)      843 2022-06-08 12:04:08.000000 nuclear-1.4.0/nuclear/sublog/wrap_error.py
+drwxrwxr-x   0 ireneusz  (1001) ireneusz  (1001)        0 2023-04-06 12:14:09.959242 nuclear-1.4.0/nuclear/types/
+-rw-r--r--   0 ireneusz  (1001) ireneusz  (1001)        0 2020-07-28 11:14:52.000000 nuclear-1.4.0/nuclear/types/__init__.py
+-rw-r--r--   0 ireneusz  (1001) ireneusz  (1001)       94 2020-07-28 11:14:52.000000 nuclear-1.4.0/nuclear/types/boolean.py
+-rw-r--r--   0 ireneusz  (1001) ireneusz  (1001)      358 2020-07-28 11:14:52.000000 nuclear-1.4.0/nuclear/types/filesystem.py
+-rw-r--r--   0 ireneusz  (1001) ireneusz  (1001)     1189 2020-07-28 11:14:52.000000 nuclear-1.4.0/nuclear/types/time.py
+drwxrwxr-x   0 ireneusz  (1001) ireneusz  (1001)        0 2023-04-06 12:14:09.963242 nuclear-1.4.0/nuclear/utils/
+-rw-r--r--   0 ireneusz  (1001) ireneusz  (1001)        0 2022-04-12 16:16:19.000000 nuclear-1.4.0/nuclear/utils/__init__.py
+-rw-r--r--   0 ireneusz  (1001) ireneusz  (1001)      116 2022-08-24 14:04:56.000000 nuclear-1.4.0/nuclear/utils/files.py
+-rw-r--r--   0 ireneusz  (1001) ireneusz  (1001)      138 2020-07-28 11:14:52.000000 nuclear-1.4.0/nuclear/utils/input.py
+-rw-r--r--   0 ireneusz  (1001) ireneusz  (1001)     1301 2022-08-24 13:59:25.000000 nuclear-1.4.0/nuclear/utils/regex.py
+-rw-rw-r--   0 ireneusz  (1001) ireneusz  (1001)      112 2022-04-12 16:39:09.000000 nuclear-1.4.0/nuclear/utils/shell.py
+-rw-r--r--   0 ireneusz  (1001) ireneusz  (1001)      688 2020-07-28 11:14:52.000000 nuclear-1.4.0/nuclear/utils/strings.py
+-rw-r--r--   0 ireneusz  (1001) ireneusz  (1001)      362 2020-07-28 11:14:52.000000 nuclear-1.4.0/nuclear/utils/time.py
+-rw-rw-r--   0 ireneusz  (1001) ireneusz  (1001)       22 2023-04-06 12:07:16.000000 nuclear-1.4.0/nuclear/version.py
+drwxrwxr-x   0 ireneusz  (1001) ireneusz  (1001)        0 2023-04-06 12:14:09.959242 nuclear-1.4.0/nuclear.egg-info/
+-rw-rw-r--   0 ireneusz  (1001) ireneusz  (1001)    18604 2023-04-06 12:14:09.000000 nuclear-1.4.0/nuclear.egg-info/PKG-INFO
+-rw-rw-r--   0 ireneusz  (1001) ireneusz  (1001)     1496 2023-04-06 12:14:09.000000 nuclear-1.4.0/nuclear.egg-info/SOURCES.txt
+-rw-rw-r--   0 ireneusz  (1001) ireneusz  (1001)        1 2023-04-06 12:14:09.000000 nuclear-1.4.0/nuclear.egg-info/dependency_links.txt
+-rw-rw-r--   0 ireneusz  (1001) ireneusz  (1001)       48 2023-04-06 12:14:09.000000 nuclear-1.4.0/nuclear.egg-info/requires.txt
+-rw-rw-r--   0 ireneusz  (1001) ireneusz  (1001)        8 2023-04-06 12:14:09.000000 nuclear-1.4.0/nuclear.egg-info/top_level.txt
+-rw-rw-r--   0 ireneusz  (1001) ireneusz  (1001)       38 2023-04-06 12:14:09.963242 nuclear-1.4.0/setup.cfg
+-rw-r--r--   0 ireneusz  (1001) ireneusz  (1001)      866 2022-04-13 08:25:38.000000 nuclear-1.4.0/setup.py
```

### Comparing `nuclear-1.3.4/LICENSE` & `nuclear-1.4.0/LICENSE`

 * *Files identical despite different names*

### Comparing `nuclear-1.3.4/PKG-INFO` & `nuclear-1.4.0/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: nuclear
-Version: 1.3.4
+Version: 1.4.0
 Summary: Declarative parser for command line interfaces
 Home-page: https://github.com/igrek51/nuclear
 Author: igrek51
 Author-email: igrek51.dev@gmail.com
 License: MIT
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
```

### Comparing `nuclear-1.3.4/README.md` & `nuclear-1.4.0/README.md`

 * *Files identical despite different names*

### Comparing `nuclear-1.3.4/nuclear/args/args_que.py` & `nuclear-1.4.0/nuclear/args/args_que.py`

 * *Files identical despite different names*

### Comparing `nuclear-1.3.4/nuclear/autocomplete/autocomplete.py` & `nuclear-1.4.0/nuclear/autocomplete/autocomplete.py`

 * *Files identical despite different names*

### Comparing `nuclear-1.3.4/nuclear/autocomplete/install.py` & `nuclear-1.4.0/nuclear/autocomplete/install.py`

 * *Files identical despite different names*

### Comparing `nuclear-1.3.4/nuclear/builder/builder.py` & `nuclear-1.4.0/nuclear/builder/builder.py`

 * *Files identical despite different names*

### Comparing `nuclear-1.3.4/nuclear/builder/decorator_builder.py` & `nuclear-1.4.0/nuclear/builder/decorator_builder.py`

 * *Files identical despite different names*

### Comparing `nuclear-1.3.4/nuclear/builder/rule.py` & `nuclear-1.4.0/nuclear/builder/rule.py`

 * *Files identical despite different names*

### Comparing `nuclear-1.3.4/nuclear/builder/rule_factory.py` & `nuclear-1.4.0/nuclear/builder/rule_factory.py`

 * *Files identical despite different names*

### Comparing `nuclear-1.3.4/nuclear/completers/file.py` & `nuclear-1.4.0/nuclear/completers/file.py`

 * *Files identical despite different names*

### Comparing `nuclear-1.3.4/nuclear/help/help.py` & `nuclear-1.4.0/nuclear/help/help.py`

 * *Files 0% similar despite different names*

```diff
@@ -115,16 +115,14 @@
 def app_name_version(app_name, version):
     infos = []
     if app_name:
         infos += [app_name]
     if version:
         version = _normalized_version(version)
         infos += [version]
-    if infos:
-        infos += [f'(nuclear v{__version__})']
     return ' '.join(infos)
 
 
 def generate_usage(app_bin_prefix, has_commands: bool, has_options: bool, many_args, pos_arguments) -> str:
     usage_syntax: str = app_bin_prefix
     if has_commands:
         usage_syntax += ' [COMMAND]'
```

### Comparing `nuclear-1.3.4/nuclear/parser/inject.py` & `nuclear-1.4.0/nuclear/parser/inject.py`

 * *Files identical despite different names*

### Comparing `nuclear-1.3.4/nuclear/parser/keyword.py` & `nuclear-1.4.0/nuclear/parser/keyword.py`

 * *Files identical despite different names*

### Comparing `nuclear-1.3.4/nuclear/parser/matcher.py` & `nuclear-1.4.0/nuclear/parser/matcher.py`

 * *Files identical despite different names*

### Comparing `nuclear-1.3.4/nuclear/parser/parser.py` & `nuclear-1.4.0/nuclear/parser/parser.py`

 * *Files identical despite different names*

### Comparing `nuclear-1.3.4/nuclear/parser/validate.py` & `nuclear-1.4.0/nuclear/parser/validate.py`

 * *Files identical despite different names*

### Comparing `nuclear-1.3.4/nuclear/parser/value.py` & `nuclear-1.4.0/nuclear/parser/value.py`

 * *Files identical despite different names*

### Comparing `nuclear-1.3.4/nuclear/shell/background_cmd.py` & `nuclear-1.4.0/nuclear/shell/background_cmd.py`

 * *Files identical despite different names*

### Comparing `nuclear-1.3.4/nuclear/shell/shell_utils.py` & `nuclear-1.4.0/nuclear/shell/shell_utils.py`

 * *Files identical despite different names*

### Comparing `nuclear-1.3.4/nuclear/sublog/catch.py` & `nuclear-1.4.0/nuclear/sublog/catch.py`

 * *Files identical despite different names*

### Comparing `nuclear-1.3.4/nuclear/sublog/context_logger.py` & `nuclear-1.4.0/nuclear/sublog/context_logger.py`

 * *Files identical despite different names*

### Comparing `nuclear-1.3.4/nuclear/sublog/wrap_error.py` & `nuclear-1.4.0/nuclear/sublog/wrap_error.py`

 * *Files identical despite different names*

### Comparing `nuclear-1.3.4/nuclear/types/time.py` & `nuclear-1.4.0/nuclear/types/time.py`

 * *Files identical despite different names*

### Comparing `nuclear-1.3.4/nuclear/utils/regex.py` & `nuclear-1.4.0/nuclear/utils/regex.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 import re
+from pathlib import Path
 
 from .strings import nonempty_lines
-from .files import read_file
 
 
 def regex_match(str_in, regex_match_pattern):
     return bool(re.compile(regex_match_pattern).match(str_in))
 
 
 def regex_replace(str_in, regex_match_pattern, regex_replace_pattern):
@@ -28,11 +28,11 @@
         for line in f:
             match = regex_matcher.match(line)
             if match:
                 return match.group(group_number)
 
 
 def regex_replace_file(file_path, regex_match_pattern, regex_replace_pattern):
-    file_content = read_file(file_path)
+    file_content = Path(file_path).read_text()
     lines = nonempty_lines(file_content)
     lines = regex_replace_list(lines, regex_match_pattern, regex_replace_pattern)
     return '\n'.join(lines)
```

### Comparing `nuclear-1.3.4/nuclear/utils/strings.py` & `nuclear-1.4.0/nuclear/utils/strings.py`

 * *Files identical despite different names*

### Comparing `nuclear-1.3.4/nuclear.egg-info/PKG-INFO` & `nuclear-1.4.0/nuclear.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: nuclear
-Version: 1.3.4
+Version: 1.4.0
 Summary: Declarative parser for command line interfaces
 Home-page: https://github.com/igrek51/nuclear
 Author: igrek51
 Author-email: igrek51.dev@gmail.com
 License: MIT
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
```

### Comparing `nuclear-1.3.4/nuclear.egg-info/SOURCES.txt` & `nuclear-1.4.0/nuclear.egg-info/SOURCES.txt`

 * *Files 8% similar despite different names*

```diff
@@ -20,14 +20,16 @@
 nuclear/builder/rule.py
 nuclear/builder/rule_factory.py
 nuclear/builder/typedef.py
 nuclear/completers/__init__.py
 nuclear/completers/file.py
 nuclear/help/__init__.py
 nuclear/help/help.py
+nuclear/inspection/__init__.py
+nuclear/inspection/inspection.py
 nuclear/parser/__init__.py
 nuclear/parser/context.py
 nuclear/parser/error.py
 nuclear/parser/inject.py
 nuclear/parser/internal_vars.py
 nuclear/parser/keyword.py
 nuclear/parser/matcher.py
```

### Comparing `nuclear-1.3.4/setup.py` & `nuclear-1.4.0/setup.py`

 * *Files identical despite different names*

