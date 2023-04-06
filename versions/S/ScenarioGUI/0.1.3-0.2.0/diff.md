# Comparing `tmp/ScenarioGUI-0.1.3.tar.gz` & `tmp/ScenarioGUI-0.2.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "ScenarioGUI-0.1.3.tar", last modified: Mon Apr  3 13:33:34 2023, max compression
+gzip compressed data, was "ScenarioGUI-0.2.0.tar", last modified: Thu Apr  6 13:23:03 2023, max compression
```

## Comparing `ScenarioGUI-0.1.3.tar` & `ScenarioGUI-0.2.0.tar`

### file list

```diff
@@ -1,89 +1,89 @@
-drwxrwxrwx   0        0        0        0 2023-04-03 13:33:34.784408 ScenarioGUI-0.1.3/
--rw-rw-rw-   0        0        0     1550 2023-03-20 10:23:05.000000 ScenarioGUI-0.1.3/LICENSE
--rw-rw-rw-   0        0        0    13299 2023-04-03 13:33:34.784959 ScenarioGUI-0.1.3/PKG-INFO
--rw-rw-rw-   0        0        0    12614 2023-03-28 11:57:26.000000 ScenarioGUI-0.1.3/README.md
-drwxrwxrwx   0        0        0        0 2023-04-03 13:33:34.725844 ScenarioGUI-0.1.3/ScenarioGUI/
--rw-rw-rw-   0        0        0        0 2023-03-20 10:23:05.000000 ScenarioGUI-0.1.3/ScenarioGUI/__init__.py
--rw-rw-rw-   0        0        0     2714 2023-04-03 13:06:38.000000 ScenarioGUI-0.1.3/ScenarioGUI/global_settings.py
-drwxrwxrwx   0        0        0        0 2023-04-03 13:33:34.744505 ScenarioGUI-0.1.3/ScenarioGUI/gui_classes/
--rw-rw-rw-   0        0        0        0 2023-03-20 10:23:05.000000 ScenarioGUI-0.1.3/ScenarioGUI/gui_classes/__init__.py
--rw-rw-rw-   0        0        0    28668 2023-04-03 11:52:45.000000 ScenarioGUI-0.1.3/ScenarioGUI/gui_classes/gui_base_class.py
--rw-rw-rw-   0        0        0     2655 2023-04-03 11:52:45.000000 ScenarioGUI-0.1.3/ScenarioGUI/gui_classes/gui_calculation_thread.py
--rw-rw-rw-   0        0        0    57851 2023-04-03 11:52:45.000000 ScenarioGUI-0.1.3/ScenarioGUI/gui_classes/gui_combine_window.py
--rw-rw-rw-   0        0        0     4824 2023-03-28 09:31:05.000000 ScenarioGUI-0.1.3/ScenarioGUI/gui_classes/gui_data_storage.py
--rw-rw-rw-   0        0        0     6963 2023-04-03 11:52:45.000000 ScenarioGUI-0.1.3/ScenarioGUI/gui_classes/gui_structure.py
-drwxrwxrwx   0        0        0        0 2023-04-03 13:33:34.758129 ScenarioGUI-0.1.3/ScenarioGUI/gui_classes/gui_structure_classes/
--rw-rw-rw-   0        0        0     1002 2023-04-03 11:52:45.000000 ScenarioGUI-0.1.3/ScenarioGUI/gui_classes/gui_structure_classes/__init__.py
--rw-rw-rw-   0        0        0     5894 2023-04-03 11:52:45.000000 ScenarioGUI-0.1.3/ScenarioGUI/gui_classes/gui_structure_classes/aim.py
--rw-rw-rw-   0        0        0     9672 2023-03-28 09:31:05.000000 ScenarioGUI-0.1.3/ScenarioGUI/gui_classes/gui_structure_classes/button_box.py
--rw-rw-rw-   0        0        0     9951 2023-03-28 09:31:05.000000 ScenarioGUI-0.1.3/ScenarioGUI/gui_classes/gui_structure_classes/category.py
--rw-rw-rw-   0        0        0     3535 2023-03-28 09:31:05.000000 ScenarioGUI-0.1.3/ScenarioGUI/gui_classes/gui_structure_classes/figure_option.py
--rw-rw-rw-   0        0        0     7199 2023-04-03 11:52:45.000000 ScenarioGUI-0.1.3/ScenarioGUI/gui_classes/gui_structure_classes/filename_box.py
--rw-rw-rw-   0        0        0    14527 2023-03-29 14:36:03.000000 ScenarioGUI-0.1.3/ScenarioGUI/gui_classes/gui_structure_classes/flexible_amount_option.py
--rw-rw-rw-   0        0        0     9396 2023-03-28 09:31:05.000000 ScenarioGUI-0.1.3/ScenarioGUI/gui_classes/gui_structure_classes/float_box.py
--rw-rw-rw-   0        0        0     5335 2023-04-03 11:52:45.000000 ScenarioGUI-0.1.3/ScenarioGUI/gui_classes/gui_structure_classes/function_button.py
--rw-rw-rw-   0        0        0     5030 2023-03-28 09:15:55.000000 ScenarioGUI-0.1.3/ScenarioGUI/gui_classes/gui_structure_classes/functions.py
--rw-rw-rw-   0        0        0     4092 2023-03-27 14:48:43.000000 ScenarioGUI-0.1.3/ScenarioGUI/gui_classes/gui_structure_classes/hint.py
--rw-rw-rw-   0        0        0     8872 2023-03-28 09:31:05.000000 ScenarioGUI-0.1.3/ScenarioGUI/gui_classes/gui_structure_classes/int_box.py
--rw-rw-rw-   0        0        0     7816 2023-03-28 09:15:55.000000 ScenarioGUI-0.1.3/ScenarioGUI/gui_classes/gui_structure_classes/list_box.py
--rw-rw-rw-   0        0        0    10309 2023-03-28 09:31:05.000000 ScenarioGUI-0.1.3/ScenarioGUI/gui_classes/gui_structure_classes/option.py
--rw-rw-rw-   0        0        0    14251 2023-03-27 14:48:43.000000 ScenarioGUI-0.1.3/ScenarioGUI/gui_classes/gui_structure_classes/page.py
--rw-rw-rw-   0        0        0     3047 2023-04-03 11:52:45.000000 ScenarioGUI-0.1.3/ScenarioGUI/gui_classes/gui_structure_classes/result_export.py
--rw-rw-rw-   0        0        0    10412 2023-04-03 11:52:45.000000 ScenarioGUI-0.1.3/ScenarioGUI/gui_classes/gui_structure_classes/result_figure.py
--rw-rw-rw-   0        0        0     4670 2023-03-28 09:15:55.000000 ScenarioGUI-0.1.3/ScenarioGUI/gui_classes/gui_structure_classes/result_text.py
--rw-rw-rw-   0        0        0     5841 2023-03-28 09:31:05.000000 ScenarioGUI-0.1.3/ScenarioGUI/gui_classes/gui_structure_classes/text_box.py
--rw-rw-rw-   0        0        0     1451 2023-03-20 10:23:06.000000 ScenarioGUI-0.1.3/ScenarioGUI/gui_classes/status_bar_logger.py
--rw-rw-rw-   0        0        0     8448 2023-03-27 13:57:20.000000 ScenarioGUI-0.1.3/ScenarioGUI/gui_classes/translation_class.py
--rw-rw-rw-   0        0        0     1513 2023-03-28 09:31:05.000000 ScenarioGUI-0.1.3/ScenarioGUI/translation_csv_to_py.py
-drwxrwxrwx   0        0        0        0 2023-04-03 13:33:34.737985 ScenarioGUI-0.1.3/ScenarioGUI.egg-info/
--rw-rw-rw-   0        0        0    13299 2023-04-03 13:33:34.000000 ScenarioGUI-0.1.3/ScenarioGUI.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0     3760 2023-04-03 13:33:34.000000 ScenarioGUI-0.1.3/ScenarioGUI.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-03 13:33:34.000000 ScenarioGUI-0.1.3/ScenarioGUI.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       69 2023-04-03 13:33:34.000000 ScenarioGUI-0.1.3/ScenarioGUI.egg-info/requires.txt
--rw-rw-rw-   0        0        0       18 2023-04-03 13:33:34.000000 ScenarioGUI-0.1.3/ScenarioGUI.egg-info/top_level.txt
--rw-rw-rw-   0        0        0     1732 2023-03-28 09:31:05.000000 ScenarioGUI-0.1.3/pyproject.toml
--rw-rw-rw-   0        0        0      985 2023-04-03 13:33:34.785965 ScenarioGUI-0.1.3/setup.cfg
--rw-rw-rw-   0        0        0      113 2023-03-28 09:15:55.000000 ScenarioGUI-0.1.3/setup.py
-drwxrwxrwx   0        0        0        0 2023-04-03 13:33:34.760639 ScenarioGUI-0.1.3/tests/
--rw-rw-rw-   0        0        0        0 2023-03-20 10:23:08.000000 ScenarioGUI-0.1.3/tests/__init__.py
--rw-rw-rw-   0        0        0     7099 2023-04-03 11:52:45.000000 ScenarioGUI-0.1.3/tests/gui_structure_for_tests.py
--rw-rw-rw-   0        0        0     1618 2023-04-03 11:52:45.000000 ScenarioGUI-0.1.3/tests/result_creating_class_for_tests.py
-drwxrwxrwx   0        0        0        0 2023-04-03 13:33:34.770663 ScenarioGUI-0.1.3/tests/test_gui_structure_elements/
--rw-rw-rw-   0        0        0        0 2023-03-20 10:23:08.000000 ScenarioGUI-0.1.3/tests/test_gui_structure_elements/__init__.py
--rw-rw-rw-   0        0        0     1126 2023-03-28 09:31:05.000000 ScenarioGUI-0.1.3/tests/test_gui_structure_elements/test_aim.py
--rw-rw-rw-   0        0        0     1644 2023-03-28 09:31:05.000000 ScenarioGUI-0.1.3/tests/test_gui_structure_elements/test_button_box.py
--rw-rw-rw-   0        0        0     1360 2023-03-28 09:31:05.000000 ScenarioGUI-0.1.3/tests/test_gui_structure_elements/test_category.py
--rw-rw-rw-   0        0        0     1775 2023-04-03 11:52:45.000000 ScenarioGUI-0.1.3/tests/test_gui_structure_elements/test_filename.py
--rw-rw-rw-   0        0        0     5178 2023-03-28 09:31:05.000000 ScenarioGUI-0.1.3/tests/test_gui_structure_elements/test_flexible_amount_option.py
--rw-rw-rw-   0        0        0     2246 2023-03-28 09:31:05.000000 ScenarioGUI-0.1.3/tests/test_gui_structure_elements/test_float_box.py
--rw-rw-rw-   0        0        0     1424 2023-03-28 09:31:05.000000 ScenarioGUI-0.1.3/tests/test_gui_structure_elements/test_function_button.py
--rw-rw-rw-   0        0        0     2067 2023-03-28 09:31:05.000000 ScenarioGUI-0.1.3/tests/test_gui_structure_elements/test_int_box.py
--rw-rw-rw-   0        0        0     2047 2023-03-28 09:31:05.000000 ScenarioGUI-0.1.3/tests/test_gui_structure_elements/test_list_box.py
--rw-rw-rw-   0        0        0     1187 2023-03-28 09:31:05.000000 ScenarioGUI-0.1.3/tests/test_gui_structure_elements/test_page.py
--rw-rw-rw-   0        0        0     1311 2023-03-28 09:31:05.000000 ScenarioGUI-0.1.3/tests/test_gui_structure_elements/test_repr.py
--rw-rw-rw-   0        0        0     1921 2023-04-03 11:52:45.000000 ScenarioGUI-0.1.3/tests/test_gui_structure_elements/test_result_export.py
--rw-rw-rw-   0        0        0     1428 2023-03-28 09:31:05.000000 ScenarioGUI-0.1.3/tests/test_gui_structure_elements/test_results_figure.py
--rw-rw-rw-   0        0        0     1362 2023-03-28 09:31:05.000000 ScenarioGUI-0.1.3/tests/test_gui_structure_elements/test_results_text.py
--rw-rw-rw-   0        0        0     1366 2023-03-28 09:31:05.000000 ScenarioGUI-0.1.3/tests/test_gui_structure_elements/test_text_box.py
-drwxrwxrwx   0        0        0        0 2023-04-03 13:33:34.781047 ScenarioGUI-0.1.3/tests/test_main_window_functions/
--rw-rw-rw-   0        0        0        0 2023-03-20 10:23:08.000000 ScenarioGUI-0.1.3/tests/test_main_window_functions/__init__.py
--rw-rw-rw-   0        0        0     2414 2023-03-28 09:31:05.000000 ScenarioGUI-0.1.3/tests/test_main_window_functions/test_auto_save.py
--rw-rw-rw-   0        0        0     2354 2023-03-28 09:31:05.000000 ScenarioGUI-0.1.3/tests/test_main_window_functions/test_backup.py
--rw-rw-rw-   0        0        0     2796 2023-04-03 11:52:45.000000 ScenarioGUI-0.1.3/tests/test_main_window_functions/test_close.py
--rw-rw-rw-   0        0        0     1309 2023-03-28 09:31:05.000000 ScenarioGUI-0.1.3/tests/test_main_window_functions/test_datastorage.py
--rw-rw-rw-   0        0        0     2121 2023-03-28 09:31:05.000000 ScenarioGUI-0.1.3/tests/test_main_window_functions/test_double_naming.py
--rw-rw-rw-   0        0        0     2039 2023-04-03 13:05:50.000000 ScenarioGUI-0.1.3/tests/test_main_window_functions/test_global_settings.py
--rw-rw-rw-   0        0        0     2100 2023-03-28 09:31:05.000000 ScenarioGUI-0.1.3/tests/test_main_window_functions/test_move_scenario.py
--rw-rw-rw-   0        0        0     5607 2023-03-28 09:31:05.000000 ScenarioGUI-0.1.3/tests/test_main_window_functions/test_new_save_load.py
--rw-rw-rw-   0        0        0     1414 2023-03-28 09:31:05.000000 ScenarioGUI-0.1.3/tests/test_main_window_functions/test_no_file.py
--rw-rw-rw-   0        0        0     1908 2023-03-28 09:31:05.000000 ScenarioGUI-0.1.3/tests/test_main_window_functions/test_push_button_change.py
--rw-rw-rw-   0        0        0     4332 2023-03-28 09:31:05.000000 ScenarioGUI-0.1.3/tests/test_main_window_functions/test_rename_scenario.py
--rw-rw-rw-   0        0        0     5156 2023-03-28 09:31:05.000000 ScenarioGUI-0.1.3/tests/test_main_window_functions/test_run.py
--rw-rw-rw-   0        0        0     6402 2023-03-28 11:53:59.000000 ScenarioGUI-0.1.3/tests/test_main_window_functions/test_scenario_change.py
--rw-rw-rw-   0        0        0     1961 2023-03-28 09:31:05.000000 ScenarioGUI-0.1.3/tests/test_main_window_functions/test_scenario_properties.py
--rw-rw-rw-   0        0        0     2876 2023-03-28 09:31:05.000000 ScenarioGUI-0.1.3/tests/test_main_window_functions/test_toggle_buttons.py
-drwxrwxrwx   0        0        0        0 2023-04-03 13:33:34.783402 ScenarioGUI-0.1.3/tests/test_translations/
--rw-rw-rw-   0        0        0        0 2023-03-20 10:23:09.000000 ScenarioGUI-0.1.3/tests/test_translations/__init__.py
--rw-rw-rw-   0        0        0      913 2023-03-28 09:31:05.000000 ScenarioGUI-0.1.3/tests/test_translations/test_language_change.py
--rw-rw-rw-   0        0        0      612 2023-03-28 09:31:05.000000 ScenarioGUI-0.1.3/tests/test_translations/test_translation_csv_2_py.py
--rw-rw-rw-   0        0        0     8611 2023-04-03 13:07:07.000000 ScenarioGUI-0.1.3/tests/test_translations/translation_class.py
+drwxrwxrwx   0        0        0        0 2023-04-06 13:23:03.102604 ScenarioGUI-0.2.0/
+-rw-rw-rw-   0        0        0     1550 2023-03-17 13:39:19.000000 ScenarioGUI-0.2.0/LICENSE
+-rw-rw-rw-   0        0        0    13181 2023-04-06 13:23:03.103605 ScenarioGUI-0.2.0/PKG-INFO
+-rw-rw-rw-   0        0        0    12496 2023-04-06 10:21:47.000000 ScenarioGUI-0.2.0/README.md
+drwxrwxrwx   0        0        0        0 2023-04-06 13:23:02.983487 ScenarioGUI-0.2.0/ScenarioGUI/
+-rw-rw-rw-   0        0        0      283 2023-04-06 10:21:47.000000 ScenarioGUI-0.2.0/ScenarioGUI/__init__.py
+-rw-rw-rw-   0        0        0     3314 2023-04-06 10:21:47.000000 ScenarioGUI-0.2.0/ScenarioGUI/global_settings.py
+drwxrwxrwx   0        0        0        0 2023-04-06 13:23:03.004506 ScenarioGUI-0.2.0/ScenarioGUI/gui_classes/
+-rw-rw-rw-   0        0        0        0 2023-03-15 21:01:46.000000 ScenarioGUI-0.2.0/ScenarioGUI/gui_classes/__init__.py
+-rw-rw-rw-   0        0        0    28668 2023-03-31 17:17:03.000000 ScenarioGUI-0.2.0/ScenarioGUI/gui_classes/gui_base_class.py
+-rw-rw-rw-   0        0        0     2655 2023-03-31 17:17:03.000000 ScenarioGUI-0.2.0/ScenarioGUI/gui_classes/gui_calculation_thread.py
+-rw-rw-rw-   0        0        0    57851 2023-04-03 06:43:48.000000 ScenarioGUI-0.2.0/ScenarioGUI/gui_classes/gui_combine_window.py
+-rw-rw-rw-   0        0        0     4824 2023-03-29 05:42:57.000000 ScenarioGUI-0.2.0/ScenarioGUI/gui_classes/gui_data_storage.py
+-rw-rw-rw-   0        0        0     6963 2023-04-01 13:46:45.000000 ScenarioGUI-0.2.0/ScenarioGUI/gui_classes/gui_structure.py
+drwxrwxrwx   0        0        0        0 2023-04-06 13:23:03.038546 ScenarioGUI-0.2.0/ScenarioGUI/gui_classes/gui_structure_classes/
+-rw-rw-rw-   0        0        0     1002 2023-03-31 17:17:03.000000 ScenarioGUI-0.2.0/ScenarioGUI/gui_classes/gui_structure_classes/__init__.py
+-rw-rw-rw-   0        0        0     5894 2023-04-01 13:42:53.000000 ScenarioGUI-0.2.0/ScenarioGUI/gui_classes/gui_structure_classes/aim.py
+-rw-rw-rw-   0        0        0     9672 2023-03-29 05:42:57.000000 ScenarioGUI-0.2.0/ScenarioGUI/gui_classes/gui_structure_classes/button_box.py
+-rw-rw-rw-   0        0        0     9951 2023-03-29 05:42:57.000000 ScenarioGUI-0.2.0/ScenarioGUI/gui_classes/gui_structure_classes/category.py
+-rw-rw-rw-   0        0        0     3535 2023-03-29 05:42:57.000000 ScenarioGUI-0.2.0/ScenarioGUI/gui_classes/gui_structure_classes/figure_option.py
+-rw-rw-rw-   0        0        0     7199 2023-03-31 17:17:03.000000 ScenarioGUI-0.2.0/ScenarioGUI/gui_classes/gui_structure_classes/filename_box.py
+-rw-rw-rw-   0        0        0    14527 2023-03-30 05:40:29.000000 ScenarioGUI-0.2.0/ScenarioGUI/gui_classes/gui_structure_classes/flexible_amount_option.py
+-rw-rw-rw-   0        0        0     9396 2023-03-29 05:42:57.000000 ScenarioGUI-0.2.0/ScenarioGUI/gui_classes/gui_structure_classes/float_box.py
+-rw-rw-rw-   0        0        0     5335 2023-04-01 13:38:11.000000 ScenarioGUI-0.2.0/ScenarioGUI/gui_classes/gui_structure_classes/function_button.py
+-rw-rw-rw-   0        0        0     5030 2023-03-27 21:12:41.000000 ScenarioGUI-0.2.0/ScenarioGUI/gui_classes/gui_structure_classes/functions.py
+-rw-rw-rw-   0        0        0     4092 2023-03-28 05:52:35.000000 ScenarioGUI-0.2.0/ScenarioGUI/gui_classes/gui_structure_classes/hint.py
+-rw-rw-rw-   0        0        0     8872 2023-03-29 05:42:57.000000 ScenarioGUI-0.2.0/ScenarioGUI/gui_classes/gui_structure_classes/int_box.py
+-rw-rw-rw-   0        0        0     7816 2023-03-28 07:47:58.000000 ScenarioGUI-0.2.0/ScenarioGUI/gui_classes/gui_structure_classes/list_box.py
+-rw-rw-rw-   0        0        0    10309 2023-04-01 13:45:00.000000 ScenarioGUI-0.2.0/ScenarioGUI/gui_classes/gui_structure_classes/option.py
+-rw-rw-rw-   0        0        0    14296 2023-04-06 13:05:56.000000 ScenarioGUI-0.2.0/ScenarioGUI/gui_classes/gui_structure_classes/page.py
+-rw-rw-rw-   0        0        0     3047 2023-03-31 17:17:03.000000 ScenarioGUI-0.2.0/ScenarioGUI/gui_classes/gui_structure_classes/result_export.py
+-rw-rw-rw-   0        0        0    10412 2023-04-03 07:51:18.000000 ScenarioGUI-0.2.0/ScenarioGUI/gui_classes/gui_structure_classes/result_figure.py
+-rw-rw-rw-   0        0        0     4670 2023-03-28 07:47:58.000000 ScenarioGUI-0.2.0/ScenarioGUI/gui_classes/gui_structure_classes/result_text.py
+-rw-rw-rw-   0        0        0     5841 2023-03-29 05:42:57.000000 ScenarioGUI-0.2.0/ScenarioGUI/gui_classes/gui_structure_classes/text_box.py
+-rw-rw-rw-   0        0        0     1482 2023-04-06 10:21:47.000000 ScenarioGUI-0.2.0/ScenarioGUI/gui_classes/status_bar_logger.py
+-rw-rw-rw-   0        0        0     8448 2023-03-28 05:52:35.000000 ScenarioGUI-0.2.0/ScenarioGUI/gui_classes/translation_class.py
+-rw-rw-rw-   0        0        0     1513 2023-03-29 05:42:57.000000 ScenarioGUI-0.2.0/ScenarioGUI/translation_csv_to_py.py
+drwxrwxrwx   0        0        0        0 2023-04-06 13:23:02.990493 ScenarioGUI-0.2.0/ScenarioGUI.egg-info/
+-rw-rw-rw-   0        0        0    13181 2023-04-06 13:23:02.000000 ScenarioGUI-0.2.0/ScenarioGUI.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0     3760 2023-04-06 13:23:02.000000 ScenarioGUI-0.2.0/ScenarioGUI.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-06 13:23:02.000000 ScenarioGUI-0.2.0/ScenarioGUI.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       69 2023-04-06 13:23:02.000000 ScenarioGUI-0.2.0/ScenarioGUI.egg-info/requires.txt
+-rw-rw-rw-   0        0        0       18 2023-04-06 13:23:02.000000 ScenarioGUI-0.2.0/ScenarioGUI.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0     1732 2023-03-29 05:42:57.000000 ScenarioGUI-0.2.0/pyproject.toml
+-rw-rw-rw-   0        0        0      985 2023-04-06 13:23:03.104606 ScenarioGUI-0.2.0/setup.cfg
+-rw-rw-rw-   0        0        0      113 2023-03-28 07:47:58.000000 ScenarioGUI-0.2.0/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-06 13:23:03.042550 ScenarioGUI-0.2.0/tests/
+-rw-rw-rw-   0        0        0        0 2023-03-16 09:51:14.000000 ScenarioGUI-0.2.0/tests/__init__.py
+-rw-rw-rw-   0        0        0     7096 2023-04-06 11:50:27.000000 ScenarioGUI-0.2.0/tests/gui_structure_for_tests.py
+-rw-rw-rw-   0        0        0     1618 2023-03-31 17:17:03.000000 ScenarioGUI-0.2.0/tests/result_creating_class_for_tests.py
+drwxrwxrwx   0        0        0        0 2023-04-06 13:23:03.068565 ScenarioGUI-0.2.0/tests/test_gui_structure_elements/
+-rw-rw-rw-   0        0        0        0 2023-03-16 09:51:14.000000 ScenarioGUI-0.2.0/tests/test_gui_structure_elements/__init__.py
+-rw-rw-rw-   0        0        0      917 2023-04-06 10:21:47.000000 ScenarioGUI-0.2.0/tests/test_gui_structure_elements/test_aim.py
+-rw-rw-rw-   0        0        0     1644 2023-03-29 05:42:57.000000 ScenarioGUI-0.2.0/tests/test_gui_structure_elements/test_button_box.py
+-rw-rw-rw-   0        0        0     1360 2023-03-29 05:42:57.000000 ScenarioGUI-0.2.0/tests/test_gui_structure_elements/test_category.py
+-rw-rw-rw-   0        0        0     1873 2023-04-06 10:52:05.000000 ScenarioGUI-0.2.0/tests/test_gui_structure_elements/test_filename.py
+-rw-rw-rw-   0        0        0     5178 2023-03-29 05:42:57.000000 ScenarioGUI-0.2.0/tests/test_gui_structure_elements/test_flexible_amount_option.py
+-rw-rw-rw-   0        0        0     2246 2023-03-29 05:42:57.000000 ScenarioGUI-0.2.0/tests/test_gui_structure_elements/test_float_box.py
+-rw-rw-rw-   0        0        0     1424 2023-03-29 05:42:57.000000 ScenarioGUI-0.2.0/tests/test_gui_structure_elements/test_function_button.py
+-rw-rw-rw-   0        0        0     2067 2023-03-29 05:42:57.000000 ScenarioGUI-0.2.0/tests/test_gui_structure_elements/test_int_box.py
+-rw-rw-rw-   0        0        0     2047 2023-03-29 05:42:57.000000 ScenarioGUI-0.2.0/tests/test_gui_structure_elements/test_list_box.py
+-rw-rw-rw-   0        0        0     1187 2023-03-29 05:42:57.000000 ScenarioGUI-0.2.0/tests/test_gui_structure_elements/test_page.py
+-rw-rw-rw-   0        0        0     1311 2023-03-29 05:42:57.000000 ScenarioGUI-0.2.0/tests/test_gui_structure_elements/test_repr.py
+-rw-rw-rw-   0        0        0     2076 2023-04-06 12:27:05.000000 ScenarioGUI-0.2.0/tests/test_gui_structure_elements/test_result_export.py
+-rw-rw-rw-   0        0        0     1428 2023-03-29 05:42:57.000000 ScenarioGUI-0.2.0/tests/test_gui_structure_elements/test_results_figure.py
+-rw-rw-rw-   0        0        0     1362 2023-03-29 05:42:57.000000 ScenarioGUI-0.2.0/tests/test_gui_structure_elements/test_results_text.py
+-rw-rw-rw-   0        0        0     1366 2023-03-29 05:42:57.000000 ScenarioGUI-0.2.0/tests/test_gui_structure_elements/test_text_box.py
+drwxrwxrwx   0        0        0        0 2023-04-06 13:23:03.093588 ScenarioGUI-0.2.0/tests/test_main_window_functions/
+-rw-rw-rw-   0        0        0        0 2023-04-06 12:27:30.000000 ScenarioGUI-0.2.0/tests/test_main_window_functions/__init__.py
+-rw-rw-rw-   0        0        0     2414 2023-03-29 05:42:57.000000 ScenarioGUI-0.2.0/tests/test_main_window_functions/test_auto_save.py
+-rw-rw-rw-   0        0        0     2354 2023-03-29 05:42:57.000000 ScenarioGUI-0.2.0/tests/test_main_window_functions/test_backup.py
+-rw-rw-rw-   0        0        0     2946 2023-04-06 12:02:31.000000 ScenarioGUI-0.2.0/tests/test_main_window_functions/test_close.py
+-rw-rw-rw-   0        0        0     1309 2023-03-29 05:42:57.000000 ScenarioGUI-0.2.0/tests/test_main_window_functions/test_datastorage.py
+-rw-rw-rw-   0        0        0     2121 2023-03-29 05:42:57.000000 ScenarioGUI-0.2.0/tests/test_main_window_functions/test_double_naming.py
+-rw-rw-rw-   0        0        0     2769 2023-04-06 11:46:02.000000 ScenarioGUI-0.2.0/tests/test_main_window_functions/test_global_settings.py
+-rw-rw-rw-   0        0        0     2100 2023-03-29 05:42:57.000000 ScenarioGUI-0.2.0/tests/test_main_window_functions/test_move_scenario.py
+-rw-rw-rw-   0        0        0     6098 2023-04-06 10:51:01.000000 ScenarioGUI-0.2.0/tests/test_main_window_functions/test_new_save_load.py
+-rw-rw-rw-   0        0        0     1414 2023-03-29 05:42:57.000000 ScenarioGUI-0.2.0/tests/test_main_window_functions/test_no_file.py
+-rw-rw-rw-   0        0        0     1908 2023-03-29 05:42:57.000000 ScenarioGUI-0.2.0/tests/test_main_window_functions/test_push_button_change.py
+-rw-rw-rw-   0        0        0     4332 2023-03-29 05:42:57.000000 ScenarioGUI-0.2.0/tests/test_main_window_functions/test_rename_scenario.py
+-rw-rw-rw-   0        0        0     5156 2023-03-29 05:42:57.000000 ScenarioGUI-0.2.0/tests/test_main_window_functions/test_run.py
+-rw-rw-rw-   0        0        0     6402 2023-03-29 05:42:57.000000 ScenarioGUI-0.2.0/tests/test_main_window_functions/test_scenario_change.py
+-rw-rw-rw-   0        0        0     1961 2023-03-29 05:42:57.000000 ScenarioGUI-0.2.0/tests/test_main_window_functions/test_scenario_properties.py
+-rw-rw-rw-   0        0        0     2876 2023-03-29 05:42:57.000000 ScenarioGUI-0.2.0/tests/test_main_window_functions/test_toggle_buttons.py
+drwxrwxrwx   0        0        0        0 2023-04-06 13:23:03.101594 ScenarioGUI-0.2.0/tests/test_translations/
+-rw-rw-rw-   0        0        0        0 2023-03-16 13:35:34.000000 ScenarioGUI-0.2.0/tests/test_translations/__init__.py
+-rw-rw-rw-   0        0        0      913 2023-03-29 05:42:57.000000 ScenarioGUI-0.2.0/tests/test_translations/test_language_change.py
+-rw-rw-rw-   0        0        0      624 2023-04-06 12:28:47.000000 ScenarioGUI-0.2.0/tests/test_translations/test_translation_csv_2_py.py
+-rw-rw-rw-   0        0        0     8795 2023-04-06 12:28:41.000000 ScenarioGUI-0.2.0/tests/test_translations/translation_class.py
```

### Comparing `ScenarioGUI-0.1.3/LICENSE` & `ScenarioGUI-0.2.0/LICENSE`

 * *Files identical despite different names*

### Comparing `ScenarioGUI-0.1.3/PKG-INFO` & `ScenarioGUI-0.2.0/PKG-INFO`

 * *Files 6% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: ScenarioGUI
-Version: 0.1.3
+Version: 0.2.0
 Summary: Python package for a scenario based GUI
 Home-page: https://github.com/tblanke/ScenarioGUI
 Author: Tobias Blanke
 Author-email: blanke@fh-aachen.de
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
@@ -97,88 +97,74 @@
 FONT_SIZE_WINDOWS: 12
 FONT_SIZE_MAC: 14
 ```
 
 To create your own GUI part you can inherit from the GuiStructure provided by this lib and add more pages, categories and input field as you like.
 
 ```Python
-from ScenarioGUI.gui_classes.gui_structure import GuiStructure
-from ScenarioGUI.gui_classes.gui_structure_classes import (
-    Aim,
-    ButtonBox,
-    Category,
-    FigureOption,
-    FileNameBox,
-    FloatBox,
-    FunctionButton,
-    Hint,
-    IntBox,
-    ListBox,
-    Page,
-    ResultFigure,
-    ResultText,
-)
+from ScenarioGUI import GuiStructure
+from ScenarioGUI import elements as els
 from typing import TYPE_CHECKING
 
 if TYPE_CHECKING:
     import PySide6.QtWidgets as QtW
     from examples.translation_class import Translations
 
 class GUI(GuiStructure):
     """your own customized GUI"""
     def __init__(self, default_parent: QtW.QWidget, translations: Translations):
         # first init the parent clas
         super().__init__(default_parent, translations)
         # add a first page called "Inputs" and has a button name of "Input" and has an icon "Add.svg"
-        self.page_inputs = Page(name="Inputs", button_name="Input", icon="Add.svg")
+        self.page_inputs = els.Page(name="Inputs", button_name="Input", icon="Add.svg")
         # Then several aims can be added to the page with different names and icons
-        self.aim_add = Aim(label="Adding", icon="Add", page=self.page_inputs)
-        self.aim_sub = Aim(label="Substract", icon="Delete", page=self.page_inputs)
-        self.aim_plot = Aim(label="Plot", icon="Parameters", page=self.page_inputs)
+        self.aim_add = els.Aim(label="Adding", icon="Add", page=self.page_inputs)
+        self.aim_sub = els.Aim(label="Substract", icon="Delete", page=self.page_inputs)
+        self.aim_plot = els.Aim(label="Plot", icon="Parameters", page=self.page_inputs)
         # a category with the label "Inputs" can be added to the inputs page like:
-        self.category_inputs = Category(label="Inputs", page=self.page_inputs)
+        self.category_inputs = els.Category(label="Inputs", page=self.page_inputs)
         # an integer box can be added with different options like this (some of these options are optional):
-        self.int_a = IntBox(label="a",default_value=2,minimal_value=0,maximal_value=200,step=2,category=self.category_inputs)
+        self.int_a = els.IntBox(label="a",default_value=2,minimal_value=0,maximal_value=200,step=2,category=self.category_inputs)
         # a float box can be added with different options like this (some of these options are optional):
-        self.float_b = FloatBox(
+        self.float_b = els.FloatBox(
             label="b",
             default_value=100,
             minimal_value=0,
             maximal_value=1000,
             decimal_number=2,
             step=0.5,
             category=self.category_inputs,
         )
         # a button box can be added with different options like this
-        self.button_box = ButtonBox(label="a or b?", default_index=0, entries=["a", "b"], category=self.category_inputs)
+        self.button_box = els.ButtonBox(label="a or b?", default_index=0, entries=["a", "b"], category=self.category_inputs)
         # the button box can also be a list box for many options
-        self.list_box = ListBox(label="a or b?", default_index=0, entries=["a", "b"], category=self.category_inputs)
+        self.list_box = els.ListBox(label="a or b?", default_index=0, entries=["a", "b"], category=self.category_inputs)
         # a filename box can be added with different options like this
         file = "./example_data.csv"
-        self.filename = FileNameBox(label="Filename", default_value=file, dialog_text="Hello", error_text="no file found", category=self.category_inputs)
+        self.filename = els.FileNameBox(label="Filename", default_value=file, dialog_text="Hello", error_text="no file found", category=self.category_inputs)
         # a function button can be implemented like this:
-        self.function_button = FunctionButton(button_text="function", icon="Add", category=self.category_inputs)
+        self.function_button = els.FunctionButton(button_text="function", icon="Add", category=self.category_inputs)
         # the function ("func") which will be called every time the button is clicked can be defined as follows:
         self.page_inputs.add_function_called_if_button_clicked(func)
         # A Hint can be implemented (if warning is True the option is displayed in WARNING color) like:
-        self.hint = Hint(hint="Very important hint", category=self.category_inputs, warning=False)
+        self.hint = els.Hint(hint="Very important hint", category=self.category_inputs, warning=False)
         # The results page must be created like this:
         self.create_results_page()
         # then a category for numerical results can be added
-        self.numerical_results = Category(page=self.page_result, label="Numerical results")
+        self.numerical_results = els.Category(page=self.page_result, label="Numerical results")
         # A text result calling the get_results function from the ResultsClass and rounding it to 2 decimals can be set like this: 
-        self.result_text_add = ResultText("Result", category=self.numerical_results, prefix="Result: ", suffix="m")
+        self.result_text_add = els.ResultText("Result", category=self.numerical_results, prefix="Result: ", suffix="m")
         self.result_text_add.text_to_be_shown("ResultsClass", "get_result")
         self.result_text_add.function_to_convert_to_text(lambda x: round(x, 2))
         # a results figure calling the create_plot function from ResultsClass which is returning a tuple of a plt.Figure and plt.Axes can be implemented 
         # like this:
-        self.figure_results = ResultFigure(label="Plot", page=self.page_result)
+        self.figure_results = els.ResultFigure(label="Plot", page=self.page_result)
         self.figure_results.fig_to_be_shown(class_name="ResultsClass", function_name="create_plot")
         # this figure can then be linked to an option to display the legend like this:
-        self.legend_figure_results = FigureOption(
+        self.legend_figure_results = els.FigureOption(
             category=self.figure_results, label="Legend on", param="legend", default=0, entries=["No", "Yes"], entries_values=[False, True]
         )        
         # with this function the results options will be displayed if one of the aims is selected
         self.aim_add.add_link_2_show(self.result_text_add)
         self.aim_plot.add_link_2_show(self.figure_results)
         # The settings page must be created like this:
         self.create_settings_page()
@@ -246,15 +232,16 @@
 ```Python
 from sys import argv, exit as sys_exit
 
 def run(path_list=None):  # pragma: no cover
     import PySide6.QtWidgets as QtW
 
     from ScenarioGUI.global_settings import FILE_EXTENSION
-    from ScenarioGUI.gui_classes.gui_combine_window import MainWindow
+    from ScenarioGUI import MainWindow
+    # import your own Translation class a script to create one from a csv file is given as well
     from ScenarioGUI.gui_classes.translation_class import Translations
 
     # init application
     app = QtW.QApplication()
     # init window
     window = QtW.QMainWindow()
     # init gui window
```

### Comparing `ScenarioGUI-0.1.3/README.md` & `ScenarioGUI-0.2.0/README.md`

 * *Files 6% similar despite different names*

```diff
@@ -78,88 +78,74 @@
 FONT_SIZE_WINDOWS: 12
 FONT_SIZE_MAC: 14
 ```
 
 To create your own GUI part you can inherit from the GuiStructure provided by this lib and add more pages, categories and input field as you like.
 
 ```Python
-from ScenarioGUI.gui_classes.gui_structure import GuiStructure
-from ScenarioGUI.gui_classes.gui_structure_classes import (
-    Aim,
-    ButtonBox,
-    Category,
-    FigureOption,
-    FileNameBox,
-    FloatBox,
-    FunctionButton,
-    Hint,
-    IntBox,
-    ListBox,
-    Page,
-    ResultFigure,
-    ResultText,
-)
+from ScenarioGUI import GuiStructure
+from ScenarioGUI import elements as els
 from typing import TYPE_CHECKING
 
 if TYPE_CHECKING:
     import PySide6.QtWidgets as QtW
     from examples.translation_class import Translations
 
 class GUI(GuiStructure):
     """your own customized GUI"""
     def __init__(self, default_parent: QtW.QWidget, translations: Translations):
         # first init the parent clas
         super().__init__(default_parent, translations)
         # add a first page called "Inputs" and has a button name of "Input" and has an icon "Add.svg"
-        self.page_inputs = Page(name="Inputs", button_name="Input", icon="Add.svg")
+        self.page_inputs = els.Page(name="Inputs", button_name="Input", icon="Add.svg")
         # Then several aims can be added to the page with different names and icons
-        self.aim_add = Aim(label="Adding", icon="Add", page=self.page_inputs)
-        self.aim_sub = Aim(label="Substract", icon="Delete", page=self.page_inputs)
-        self.aim_plot = Aim(label="Plot", icon="Parameters", page=self.page_inputs)
+        self.aim_add = els.Aim(label="Adding", icon="Add", page=self.page_inputs)
+        self.aim_sub = els.Aim(label="Substract", icon="Delete", page=self.page_inputs)
+        self.aim_plot = els.Aim(label="Plot", icon="Parameters", page=self.page_inputs)
         # a category with the label "Inputs" can be added to the inputs page like:
-        self.category_inputs = Category(label="Inputs", page=self.page_inputs)
+        self.category_inputs = els.Category(label="Inputs", page=self.page_inputs)
         # an integer box can be added with different options like this (some of these options are optional):
-        self.int_a = IntBox(label="a",default_value=2,minimal_value=0,maximal_value=200,step=2,category=self.category_inputs)
+        self.int_a = els.IntBox(label="a",default_value=2,minimal_value=0,maximal_value=200,step=2,category=self.category_inputs)
         # a float box can be added with different options like this (some of these options are optional):
-        self.float_b = FloatBox(
+        self.float_b = els.FloatBox(
             label="b",
             default_value=100,
             minimal_value=0,
             maximal_value=1000,
             decimal_number=2,
             step=0.5,
             category=self.category_inputs,
         )
         # a button box can be added with different options like this
-        self.button_box = ButtonBox(label="a or b?", default_index=0, entries=["a", "b"], category=self.category_inputs)
+        self.button_box = els.ButtonBox(label="a or b?", default_index=0, entries=["a", "b"], category=self.category_inputs)
         # the button box can also be a list box for many options
-        self.list_box = ListBox(label="a or b?", default_index=0, entries=["a", "b"], category=self.category_inputs)
+        self.list_box = els.ListBox(label="a or b?", default_index=0, entries=["a", "b"], category=self.category_inputs)
         # a filename box can be added with different options like this
         file = "./example_data.csv"
-        self.filename = FileNameBox(label="Filename", default_value=file, dialog_text="Hello", error_text="no file found", category=self.category_inputs)
+        self.filename = els.FileNameBox(label="Filename", default_value=file, dialog_text="Hello", error_text="no file found", category=self.category_inputs)
         # a function button can be implemented like this:
-        self.function_button = FunctionButton(button_text="function", icon="Add", category=self.category_inputs)
+        self.function_button = els.FunctionButton(button_text="function", icon="Add", category=self.category_inputs)
         # the function ("func") which will be called every time the button is clicked can be defined as follows:
         self.page_inputs.add_function_called_if_button_clicked(func)
         # A Hint can be implemented (if warning is True the option is displayed in WARNING color) like:
-        self.hint = Hint(hint="Very important hint", category=self.category_inputs, warning=False)
+        self.hint = els.Hint(hint="Very important hint", category=self.category_inputs, warning=False)
         # The results page must be created like this:
         self.create_results_page()
         # then a category for numerical results can be added
-        self.numerical_results = Category(page=self.page_result, label="Numerical results")
+        self.numerical_results = els.Category(page=self.page_result, label="Numerical results")
         # A text result calling the get_results function from the ResultsClass and rounding it to 2 decimals can be set like this: 
-        self.result_text_add = ResultText("Result", category=self.numerical_results, prefix="Result: ", suffix="m")
+        self.result_text_add = els.ResultText("Result", category=self.numerical_results, prefix="Result: ", suffix="m")
         self.result_text_add.text_to_be_shown("ResultsClass", "get_result")
         self.result_text_add.function_to_convert_to_text(lambda x: round(x, 2))
         # a results figure calling the create_plot function from ResultsClass which is returning a tuple of a plt.Figure and plt.Axes can be implemented 
         # like this:
-        self.figure_results = ResultFigure(label="Plot", page=self.page_result)
+        self.figure_results = els.ResultFigure(label="Plot", page=self.page_result)
         self.figure_results.fig_to_be_shown(class_name="ResultsClass", function_name="create_plot")
         # this figure can then be linked to an option to display the legend like this:
-        self.legend_figure_results = FigureOption(
+        self.legend_figure_results = els.FigureOption(
             category=self.figure_results, label="Legend on", param="legend", default=0, entries=["No", "Yes"], entries_values=[False, True]
         )        
         # with this function the results options will be displayed if one of the aims is selected
         self.aim_add.add_link_2_show(self.result_text_add)
         self.aim_plot.add_link_2_show(self.figure_results)
         # The settings page must be created like this:
         self.create_settings_page()
@@ -227,15 +213,16 @@
 ```Python
 from sys import argv, exit as sys_exit
 
 def run(path_list=None):  # pragma: no cover
     import PySide6.QtWidgets as QtW
 
     from ScenarioGUI.global_settings import FILE_EXTENSION
-    from ScenarioGUI.gui_classes.gui_combine_window import MainWindow
+    from ScenarioGUI import MainWindow
+    # import your own Translation class a script to create one from a csv file is given as well
     from ScenarioGUI.gui_classes.translation_class import Translations
 
     # init application
     app = QtW.QApplication()
     # init window
     window = QtW.QMainWindow()
     # init gui window
```

### Comparing `ScenarioGUI-0.1.3/ScenarioGUI/global_settings.py` & `ScenarioGUI-0.2.0/ScenarioGUI/global_settings.py`

 * *Files 12% similar despite different names*

```diff
@@ -4,51 +4,85 @@
 from __future__ import annotations
 
 import logging
 from configparser import ConfigParser
 from pathlib import Path
 from platform import system
 
-path = Path(".").absolute()
+path = Path(__file__).parent.absolute()
 config = ConfigParser()
 
 
 def get_path_for_file(start_path: Path, filename: str) -> Path:
     path_i = start_path
-    for i in range(4):
+    for i in range(6):
         items = [item.parent for item in path_i.glob(f"**/{filename}")]
         if items:
             return items[0]
         path_i = path_i.parent
     raise FileNotFoundError
 
 
-config.read(get_path_for_file(path, "gui_config.ini").joinpath("gui_config.ini"))
+FOLDER: Path = Path("./icons")
 
-FOLDER: Path = get_path_for_file(get_path_for_file(path, config['DEFAULT']["PATH_2_ICONS"]).joinpath(config['DEFAULT']["PATH_2_ICONS"]), "icons")
-
-WHITE: str = config['COLORS']["WHITE"]
-LIGHT: str = config['COLORS']["LIGHT"]
-LIGHT_SELECT: str = config['COLORS']["LIGHT_SELECT"]
-DARK: str = config['COLORS']["DARK"]
-GREY: str = config['COLORS']["GREY"]
-WARNING: str = config['COLORS']["WARNING"]
-BLACK: str = config['COLORS']["BLACK"]
-
-FONT = config['DEFAULT']["FONT_WINDOWS"] if system() == "Windows" else config['DEFAULT']["FONT_MAC"]
-FONT_SIZE = int(config['DEFAULT']["FONT_SIZE_WINDOWS"] if system() == "Windows" else config['DEFAULT']["FONT_SIZE_MAC"])
-
-FILE_EXTENSION: str = config['DEFAULT']["FILE_EXTENSION"]
-GUI_NAME: str = config['DEFAULT']["GUI_NAME"]
-ICON_NAME: str = config['DEFAULT']["ICON_NAME"]
+WHITE: str = "rgb(0,0,0)"
+LIGHT: str = "rgb(0,0,0)"
+LIGHT_SELECT: str = "rgb(0,0,0)"
+DARK: str = "rgb(0,0,0)"
+GREY: str = "rgb(0,0,0)"
+WARNING: str = "rgb(0,0,0)"
+BLACK: str = "rgb(0,0,0)"
+
+FONT = "None"
+FONT_SIZE = 6
+
+FILE_EXTENSION: str = "nothing"
+GUI_NAME: str = "None"
+ICON_NAME: str = "icon"
 
 # get current version
 config.read(config.read(get_path_for_file(path, "setup.cfg").joinpath("setup.cfg")))
 VERSION = config.get("metadata", "version")
 
+
+def load(gui_file: str | Path):
+    config.read(gui_file)
+
+    global FOLDER
+    global WHITE
+    global LIGHT
+    global LIGHT_SELECT
+    global DARK
+    global GREY
+    global WARNING
+    global BLACK
+    global FONT
+    global FONT_SIZE
+    global FILE_EXTENSION
+    global GUI_NAME
+    global ICON_NAME
+
+    FOLDER = get_path_for_file(get_path_for_file(path, config['DEFAULT']["PATH_2_ICONS"]).joinpath(config['DEFAULT']["PATH_2_ICONS"]), "icons")
+
+    WHITE = config['COLORS']["WHITE"]
+    LIGHT = config['COLORS']["LIGHT"]
+    LIGHT_SELECT = config['COLORS']["LIGHT_SELECT"]
+    DARK = config['COLORS']["DARK"]
+    GREY = config['COLORS']["GREY"]
+    WARNING = config['COLORS']["WARNING"]
+    BLACK = config['COLORS']["BLACK"]
+
+    FONT = config['DEFAULT']["FONT_WINDOWS"] if system() == "Windows" else config['DEFAULT']["FONT_MAC"]
+    FONT_SIZE = int(config['DEFAULT']["FONT_SIZE_WINDOWS"] if system() == "Windows" else config['DEFAULT']["FONT_SIZE_MAC"])
+
+    FILE_EXTENSION = config['DEFAULT']["FILE_EXTENSION"]
+    GUI_NAME = config['DEFAULT']["GUI_NAME"]
+    ICON_NAME = config['DEFAULT']["ICON_NAME"]
+
+
 LOGGER = logging.getLogger()
 LOGGER.setLevel(logging.INFO)
 
 
 def set_graph_layout() -> None:
     """
     This function sets the graph layout to the correct format when the GUI is used.
```

### Comparing `ScenarioGUI-0.1.3/ScenarioGUI/gui_classes/gui_base_class.py` & `ScenarioGUI-0.2.0/ScenarioGUI/gui_classes/gui_base_class.py`

 * *Files identical despite different names*

### Comparing `ScenarioGUI-0.1.3/ScenarioGUI/gui_classes/gui_calculation_thread.py` & `ScenarioGUI-0.2.0/ScenarioGUI/gui_classes/gui_calculation_thread.py`

 * *Files identical despite different names*

### Comparing `ScenarioGUI-0.1.3/ScenarioGUI/gui_classes/gui_combine_window.py` & `ScenarioGUI-0.2.0/ScenarioGUI/gui_classes/gui_combine_window.py`

 * *Files identical despite different names*

### Comparing `ScenarioGUI-0.1.3/ScenarioGUI/gui_classes/gui_data_storage.py` & `ScenarioGUI-0.2.0/ScenarioGUI/gui_classes/gui_data_storage.py`

 * *Files identical despite different names*

### Comparing `ScenarioGUI-0.1.3/ScenarioGUI/gui_classes/gui_structure.py` & `ScenarioGUI-0.2.0/ScenarioGUI/gui_classes/gui_structure.py`

 * *Files identical despite different names*

### Comparing `ScenarioGUI-0.1.3/ScenarioGUI/gui_classes/gui_structure_classes/__init__.py` & `ScenarioGUI-0.2.0/ScenarioGUI/gui_classes/gui_structure_classes/__init__.py`

 * *Files identical despite different names*

### Comparing `ScenarioGUI-0.1.3/ScenarioGUI/gui_classes/gui_structure_classes/aim.py` & `ScenarioGUI-0.2.0/ScenarioGUI/gui_classes/gui_structure_classes/aim.py`

 * *Files identical despite different names*

### Comparing `ScenarioGUI-0.1.3/ScenarioGUI/gui_classes/gui_structure_classes/button_box.py` & `ScenarioGUI-0.2.0/ScenarioGUI/gui_classes/gui_structure_classes/button_box.py`

 * *Files identical despite different names*

### Comparing `ScenarioGUI-0.1.3/ScenarioGUI/gui_classes/gui_structure_classes/category.py` & `ScenarioGUI-0.2.0/ScenarioGUI/gui_classes/gui_structure_classes/category.py`

 * *Files identical despite different names*

### Comparing `ScenarioGUI-0.1.3/ScenarioGUI/gui_classes/gui_structure_classes/figure_option.py` & `ScenarioGUI-0.2.0/ScenarioGUI/gui_classes/gui_structure_classes/figure_option.py`

 * *Files identical despite different names*

### Comparing `ScenarioGUI-0.1.3/ScenarioGUI/gui_classes/gui_structure_classes/filename_box.py` & `ScenarioGUI-0.2.0/ScenarioGUI/gui_classes/gui_structure_classes/filename_box.py`

 * *Files identical despite different names*

### Comparing `ScenarioGUI-0.1.3/ScenarioGUI/gui_classes/gui_structure_classes/flexible_amount_option.py` & `ScenarioGUI-0.2.0/ScenarioGUI/gui_classes/gui_structure_classes/flexible_amount_option.py`

 * *Files identical despite different names*

### Comparing `ScenarioGUI-0.1.3/ScenarioGUI/gui_classes/gui_structure_classes/float_box.py` & `ScenarioGUI-0.2.0/ScenarioGUI/gui_classes/gui_structure_classes/float_box.py`

 * *Files identical despite different names*

### Comparing `ScenarioGUI-0.1.3/ScenarioGUI/gui_classes/gui_structure_classes/function_button.py` & `ScenarioGUI-0.2.0/ScenarioGUI/gui_classes/gui_structure_classes/function_button.py`

 * *Files identical despite different names*

### Comparing `ScenarioGUI-0.1.3/ScenarioGUI/gui_classes/gui_structure_classes/functions.py` & `ScenarioGUI-0.2.0/ScenarioGUI/gui_classes/gui_structure_classes/functions.py`

 * *Files identical despite different names*

### Comparing `ScenarioGUI-0.1.3/ScenarioGUI/gui_classes/gui_structure_classes/hint.py` & `ScenarioGUI-0.2.0/ScenarioGUI/gui_classes/gui_structure_classes/hint.py`

 * *Files identical despite different names*

### Comparing `ScenarioGUI-0.1.3/ScenarioGUI/gui_classes/gui_structure_classes/int_box.py` & `ScenarioGUI-0.2.0/ScenarioGUI/gui_classes/gui_structure_classes/int_box.py`

 * *Files identical despite different names*

### Comparing `ScenarioGUI-0.1.3/ScenarioGUI/gui_classes/gui_structure_classes/list_box.py` & `ScenarioGUI-0.2.0/ScenarioGUI/gui_classes/gui_structure_classes/list_box.py`

 * *Files identical despite different names*

### Comparing `ScenarioGUI-0.1.3/ScenarioGUI/gui_classes/gui_structure_classes/option.py` & `ScenarioGUI-0.2.0/ScenarioGUI/gui_classes/gui_structure_classes/option.py`

 * *Files identical despite different names*

### Comparing `ScenarioGUI-0.1.3/ScenarioGUI/gui_classes/gui_structure_classes/page.py` & `ScenarioGUI-0.2.0/ScenarioGUI/gui_classes/gui_structure_classes/page.py`

 * *Files 1% similar despite different names*

```diff
@@ -97,15 +97,16 @@
 
         Returns
         -------
         None
         """
         entry_name: list[str, str] = name.split(",")
         self.label.setText(entry_name[1])
-        self.button.setText(entry_name[0].replace("@", "\n"))
+        self.button_name = entry_name[0].replace("@", "\n")
+        self.button.setText(self.button_name)
         if self.push_button_previous is not None:
             self.push_button_previous.setText(self.previous_label)
         if self.push_button_next is not None:
             self.push_button_next.setText(self.next_label)
 
     def set_previous_page(self, previous_page: Page) -> None:
         """
```

### Comparing `ScenarioGUI-0.1.3/ScenarioGUI/gui_classes/gui_structure_classes/result_export.py` & `ScenarioGUI-0.2.0/ScenarioGUI/gui_classes/gui_structure_classes/result_export.py`

 * *Files identical despite different names*

### Comparing `ScenarioGUI-0.1.3/ScenarioGUI/gui_classes/gui_structure_classes/result_figure.py` & `ScenarioGUI-0.2.0/ScenarioGUI/gui_classes/gui_structure_classes/result_figure.py`

 * *Files identical despite different names*

### Comparing `ScenarioGUI-0.1.3/ScenarioGUI/gui_classes/gui_structure_classes/result_text.py` & `ScenarioGUI-0.2.0/ScenarioGUI/gui_classes/gui_structure_classes/result_text.py`

 * *Files identical despite different names*

### Comparing `ScenarioGUI-0.1.3/ScenarioGUI/gui_classes/gui_structure_classes/text_box.py` & `ScenarioGUI-0.2.0/ScenarioGUI/gui_classes/gui_structure_classes/text_box.py`

 * *Files identical despite different names*

### Comparing `ScenarioGUI-0.1.3/ScenarioGUI/gui_classes/status_bar_logger.py` & `ScenarioGUI-0.2.0/ScenarioGUI/gui_classes/status_bar_logger.py`

 * *Files 1% similar despite different names*

```diff
@@ -17,33 +17,32 @@
 
 
 class StatusBar(Handler):
     """
     Class to create a status bar logger. To display messages in the GUI Status Bar
     """
 
-    level_2_color: dict[str, str] = {
-        "DEBUG": f"{globs.WHITE}",
-        "INFO": f"{globs.WHITE}",
-        "ERROR": "rgb(255,0,0)",
-        "CRITICAL": "rgb(255,0,0)",
-        "WARNING": f"{globs.WARNING}",
-    }
-
     def __init__(self, parent: QWidget):
         """
         Init status bar.
 
         Parameters
         ----------
         parent: QtW.QWidget
             parent to create QStatusBar in
         """
         super().__init__()
         self.widget: QStatusBar = QStatusBar(parent)
+        self.level_2_color: dict[str, str] = {
+            "DEBUG": f"{globs.WHITE}",
+            "INFO": f"{globs.WHITE}",
+            "ERROR": "rgb(255,0,0)",
+            "CRITICAL": "rgb(255,0,0)",
+            "WARNING": f"{globs.WARNING}",
+        }
 
     def emit(self, record: LogRecord) -> None:
         """
         Display record in statusbar.
 
         Parameters
         ----------
```

### Comparing `ScenarioGUI-0.1.3/ScenarioGUI/gui_classes/translation_class.py` & `ScenarioGUI-0.2.0/ScenarioGUI/gui_classes/translation_class.py`

 * *Files identical despite different names*

### Comparing `ScenarioGUI-0.1.3/ScenarioGUI/translation_csv_to_py.py` & `ScenarioGUI-0.2.0/ScenarioGUI/translation_csv_to_py.py`

 * *Files identical despite different names*

### Comparing `ScenarioGUI-0.1.3/ScenarioGUI.egg-info/PKG-INFO` & `ScenarioGUI-0.2.0/ScenarioGUI.egg-info/PKG-INFO`

 * *Files 6% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: ScenarioGUI
-Version: 0.1.3
+Version: 0.2.0
 Summary: Python package for a scenario based GUI
 Home-page: https://github.com/tblanke/ScenarioGUI
 Author: Tobias Blanke
 Author-email: blanke@fh-aachen.de
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
@@ -97,88 +97,74 @@
 FONT_SIZE_WINDOWS: 12
 FONT_SIZE_MAC: 14
 ```
 
 To create your own GUI part you can inherit from the GuiStructure provided by this lib and add more pages, categories and input field as you like.
 
 ```Python
-from ScenarioGUI.gui_classes.gui_structure import GuiStructure
-from ScenarioGUI.gui_classes.gui_structure_classes import (
-    Aim,
-    ButtonBox,
-    Category,
-    FigureOption,
-    FileNameBox,
-    FloatBox,
-    FunctionButton,
-    Hint,
-    IntBox,
-    ListBox,
-    Page,
-    ResultFigure,
-    ResultText,
-)
+from ScenarioGUI import GuiStructure
+from ScenarioGUI import elements as els
 from typing import TYPE_CHECKING
 
 if TYPE_CHECKING:
     import PySide6.QtWidgets as QtW
     from examples.translation_class import Translations
 
 class GUI(GuiStructure):
     """your own customized GUI"""
     def __init__(self, default_parent: QtW.QWidget, translations: Translations):
         # first init the parent clas
         super().__init__(default_parent, translations)
         # add a first page called "Inputs" and has a button name of "Input" and has an icon "Add.svg"
-        self.page_inputs = Page(name="Inputs", button_name="Input", icon="Add.svg")
+        self.page_inputs = els.Page(name="Inputs", button_name="Input", icon="Add.svg")
         # Then several aims can be added to the page with different names and icons
-        self.aim_add = Aim(label="Adding", icon="Add", page=self.page_inputs)
-        self.aim_sub = Aim(label="Substract", icon="Delete", page=self.page_inputs)
-        self.aim_plot = Aim(label="Plot", icon="Parameters", page=self.page_inputs)
+        self.aim_add = els.Aim(label="Adding", icon="Add", page=self.page_inputs)
+        self.aim_sub = els.Aim(label="Substract", icon="Delete", page=self.page_inputs)
+        self.aim_plot = els.Aim(label="Plot", icon="Parameters", page=self.page_inputs)
         # a category with the label "Inputs" can be added to the inputs page like:
-        self.category_inputs = Category(label="Inputs", page=self.page_inputs)
+        self.category_inputs = els.Category(label="Inputs", page=self.page_inputs)
         # an integer box can be added with different options like this (some of these options are optional):
-        self.int_a = IntBox(label="a",default_value=2,minimal_value=0,maximal_value=200,step=2,category=self.category_inputs)
+        self.int_a = els.IntBox(label="a",default_value=2,minimal_value=0,maximal_value=200,step=2,category=self.category_inputs)
         # a float box can be added with different options like this (some of these options are optional):
-        self.float_b = FloatBox(
+        self.float_b = els.FloatBox(
             label="b",
             default_value=100,
             minimal_value=0,
             maximal_value=1000,
             decimal_number=2,
             step=0.5,
             category=self.category_inputs,
         )
         # a button box can be added with different options like this
-        self.button_box = ButtonBox(label="a or b?", default_index=0, entries=["a", "b"], category=self.category_inputs)
+        self.button_box = els.ButtonBox(label="a or b?", default_index=0, entries=["a", "b"], category=self.category_inputs)
         # the button box can also be a list box for many options
-        self.list_box = ListBox(label="a or b?", default_index=0, entries=["a", "b"], category=self.category_inputs)
+        self.list_box = els.ListBox(label="a or b?", default_index=0, entries=["a", "b"], category=self.category_inputs)
         # a filename box can be added with different options like this
         file = "./example_data.csv"
-        self.filename = FileNameBox(label="Filename", default_value=file, dialog_text="Hello", error_text="no file found", category=self.category_inputs)
+        self.filename = els.FileNameBox(label="Filename", default_value=file, dialog_text="Hello", error_text="no file found", category=self.category_inputs)
         # a function button can be implemented like this:
-        self.function_button = FunctionButton(button_text="function", icon="Add", category=self.category_inputs)
+        self.function_button = els.FunctionButton(button_text="function", icon="Add", category=self.category_inputs)
         # the function ("func") which will be called every time the button is clicked can be defined as follows:
         self.page_inputs.add_function_called_if_button_clicked(func)
         # A Hint can be implemented (if warning is True the option is displayed in WARNING color) like:
-        self.hint = Hint(hint="Very important hint", category=self.category_inputs, warning=False)
+        self.hint = els.Hint(hint="Very important hint", category=self.category_inputs, warning=False)
         # The results page must be created like this:
         self.create_results_page()
         # then a category for numerical results can be added
-        self.numerical_results = Category(page=self.page_result, label="Numerical results")
+        self.numerical_results = els.Category(page=self.page_result, label="Numerical results")
         # A text result calling the get_results function from the ResultsClass and rounding it to 2 decimals can be set like this: 
-        self.result_text_add = ResultText("Result", category=self.numerical_results, prefix="Result: ", suffix="m")
+        self.result_text_add = els.ResultText("Result", category=self.numerical_results, prefix="Result: ", suffix="m")
         self.result_text_add.text_to_be_shown("ResultsClass", "get_result")
         self.result_text_add.function_to_convert_to_text(lambda x: round(x, 2))
         # a results figure calling the create_plot function from ResultsClass which is returning a tuple of a plt.Figure and plt.Axes can be implemented 
         # like this:
-        self.figure_results = ResultFigure(label="Plot", page=self.page_result)
+        self.figure_results = els.ResultFigure(label="Plot", page=self.page_result)
         self.figure_results.fig_to_be_shown(class_name="ResultsClass", function_name="create_plot")
         # this figure can then be linked to an option to display the legend like this:
-        self.legend_figure_results = FigureOption(
+        self.legend_figure_results = els.FigureOption(
             category=self.figure_results, label="Legend on", param="legend", default=0, entries=["No", "Yes"], entries_values=[False, True]
         )        
         # with this function the results options will be displayed if one of the aims is selected
         self.aim_add.add_link_2_show(self.result_text_add)
         self.aim_plot.add_link_2_show(self.figure_results)
         # The settings page must be created like this:
         self.create_settings_page()
@@ -246,15 +232,16 @@
 ```Python
 from sys import argv, exit as sys_exit
 
 def run(path_list=None):  # pragma: no cover
     import PySide6.QtWidgets as QtW
 
     from ScenarioGUI.global_settings import FILE_EXTENSION
-    from ScenarioGUI.gui_classes.gui_combine_window import MainWindow
+    from ScenarioGUI import MainWindow
+    # import your own Translation class a script to create one from a csv file is given as well
     from ScenarioGUI.gui_classes.translation_class import Translations
 
     # init application
     app = QtW.QApplication()
     # init window
     window = QtW.QMainWindow()
     # init gui window
```

### Comparing `ScenarioGUI-0.1.3/ScenarioGUI.egg-info/SOURCES.txt` & `ScenarioGUI-0.2.0/ScenarioGUI.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `ScenarioGUI-0.1.3/pyproject.toml` & `ScenarioGUI-0.2.0/pyproject.toml`

 * *Files identical despite different names*

### Comparing `ScenarioGUI-0.1.3/setup.cfg` & `ScenarioGUI-0.2.0/setup.cfg`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 00000000: 5b6d 6574 6164 6174 615d 0d0a 6e61 6d65  [metadata]..name
 00000010: 203d 2053 6365 6e61 7269 6f47 5549 0d0a   = ScenarioGUI..
-00000020: 7665 7273 696f 6e20 3d20 302e 312e 330d  version = 0.1.3.
+00000020: 7665 7273 696f 6e20 3d20 302e 322e 300d  version = 0.2.0.
 00000030: 0a61 7574 686f 7220 3d20 546f 6269 6173  .author = Tobias
 00000040: 2042 6c61 6e6b 650d 0a61 7574 686f 725f   Blanke..author_
 00000050: 656d 6169 6c20 3d20 626c 616e 6b65 4066  email = blanke@f
 00000060: 682d 6161 6368 656e 2e64 650d 0a64 6573  h-aachen.de..des
 00000070: 6372 6970 7469 6f6e 203d 2050 7974 686f  cription = Pytho
 00000080: 6e20 7061 636b 6167 6520 666f 7220 6120  n package for a 
 00000090: 7363 656e 6172 696f 2062 6173 6564 2047  scenario based G
```

### Comparing `ScenarioGUI-0.1.3/tests/gui_structure_for_tests.py` & `ScenarioGUI-0.2.0/tests/gui_structure_for_tests.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,27 +1,28 @@
 from __future__ import annotations
 
 from pathlib import Path
 from typing import TYPE_CHECKING
 
-from ScenarioGUI.gui_classes.gui_structure import GuiStructure
+from ScenarioGUI import GuiStructure
 from ScenarioGUI.gui_classes.gui_structure_classes import (
     Aim,
     ButtonBox,
     Category,
     FigureOption,
     FileNameBox,
     FlexibleAmount,
     FloatBox,
     FunctionButton,
     Hint,
     IntBox,
     ListBox,
     Page,
-    ResultExport, ResultFigure,
+    ResultExport,
+    ResultFigure,
     ResultText,
     TextBox,
 )
 
 if TYPE_CHECKING:
     import PySide6.QtWidgets as QtW
 
@@ -52,15 +53,15 @@
             decimal_number=2,
             category=self.category_inputs,
         )
         folder: Path = Path(__file__).parent
         file = f'{folder.joinpath("./example_data.csv")}'
         self.filename = FileNameBox(label="Filename", default_value=file, category=self.category_inputs, dialog_text="Hello", error_text="no file found")
 
-        self.function_button = FunctionButton(button_text="function", icon="Add", category=self.category_inputs)
+        self.function_button = FunctionButton(button_text=translations.function_button, icon="Add", category=self.category_inputs)
 
         self.button_box = ButtonBox(label="a or b?", default_index=0, entries=["a", "b"], category=self.category_inputs)
 
         self.list_box = ListBox(
             label="List box",
             default_index=0,
             entries=["0", "1", "2", "3"],
```

### Comparing `ScenarioGUI-0.1.3/tests/result_creating_class_for_tests.py` & `ScenarioGUI-0.2.0/tests/result_creating_class_for_tests.py`

 * *Files identical despite different names*

### Comparing `ScenarioGUI-0.1.3/tests/test_gui_structure_elements/test_aim.py` & `ScenarioGUI-0.2.0/tests/test_gui_structure_elements/test_page.py`

 * *Files 14% similar despite different names*

```diff
@@ -1,31 +1,23 @@
 import PySide6.QtWidgets as QtW
 
 from ScenarioGUI.gui_classes.gui_combine_window import MainWindow
+from tests.gui_structure_for_tests import GUI
+from tests.result_creating_class_for_tests import ResultsClass, data_2_results
+from tests.test_translations.translation_class import Translations
 
-from ..gui_structure_for_tests import GUI
-from ..result_creating_class_for_tests import ResultsClass, data_2_results
-from ..test_translations.translation_class import Translations
 
-
-def test_aim(qtbot):
-    """
-    test float box functions
-
-    Parameters
-    ----------
-    qtbot: qtbot
-        bot for the GUI
-    """
+def test_page(qtbot):
     # init gui window
     main_window = MainWindow(QtW.QMainWindow(), qtbot, GUI, Translations, result_creating_class=ResultsClass, data_2_results_function=data_2_results)
     main_window.delete_backup()
     main_window = MainWindow(QtW.QMainWindow(), qtbot, GUI, Translations, result_creating_class=ResultsClass, data_2_results_function=data_2_results)
 
-    if not main_window.gui_structure.aim_plot.widget.isChecked():
-        main_window.gui_structure.aim_plot.widget.click()
-
-    assert main_window.gui_structure.aim_plot.widget.isChecked()
-
-    main_window.gui_structure.aim_plot.set_text("Hello")
-    assert main_window.gui_structure.aim_plot.widget.text() == "Hello"
-
+    main_window.gui_structure.page_result.set_text("button name,Name")
+    assert main_window.gui_structure.page_result.button.text() == "button name"
+    assert main_window.gui_structure.page_result.label.text() == "Name"
+
+    # test linked function which counts the counter every time button is clicked
+    assert main_window.gui_structure.counter == 1
+    main_window.gui_structure.page_inputs.button.click()
+    assert main_window.gui_structure.counter == 2
+    main_window.delete_backup()
```

### Comparing `ScenarioGUI-0.1.3/tests/test_gui_structure_elements/test_button_box.py` & `ScenarioGUI-0.2.0/tests/test_gui_structure_elements/test_button_box.py`

 * *Files identical despite different names*

### Comparing `ScenarioGUI-0.1.3/tests/test_gui_structure_elements/test_category.py` & `ScenarioGUI-0.2.0/tests/test_gui_structure_elements/test_category.py`

 * *Files identical despite different names*

### Comparing `ScenarioGUI-0.1.3/tests/test_gui_structure_elements/test_filename.py` & `ScenarioGUI-0.2.0/tests/test_gui_structure_elements/test_filename.py`

 * *Files 12% similar despite different names*

```diff
@@ -1,14 +1,11 @@
-import os
+from functools import partial
 from pathlib import Path
 
-import keyboard
-import PySide6.QtCore as QtC
 import PySide6.QtWidgets as QtW
-
 from ScenarioGUI.gui_classes.gui_combine_window import MainWindow
 
 from ..gui_structure_for_tests import GUI
 from ..result_creating_class_for_tests import ResultsClass, data_2_results
 from ..test_translations.translation_class import Translations
 
 
@@ -27,17 +24,21 @@
     main_window.gui_structure.filename._init_links()
 
     folder = Path(__file__).parent.parent
     file = f'{folder.joinpath("./example_data.csv")}'
     assert main_window.gui_structure.filename.get_value() == main_window.gui_structure.filename.default_value
     assert main_window.gui_structure.filename.default_value == file
     # check if no file is passed
-    QtC.QTimer.singleShot(1000, lambda: keyboard.press("Esc"))
+    def get_save_file_name(*args, **kwargs):
+        """getSaveFileName proxy"""
+        return kwargs["return_value"]
+
+    QtW.QFileDialog.getOpenFileName = partial(get_save_file_name, return_value=("", ""))
     main_window.gui_structure.filename.button.click()
     assert main_window.status_bar.widget.currentMessage() == main_window.gui_structure.filename.error_text
     # check file import and calculation
-    QtC.QTimer.singleShot(1000, lambda: keyboard.write(file))
-    QtC.QTimer.singleShot(1500, lambda: keyboard.press("enter"))
+
+    QtW.QFileDialog.getOpenFileName = partial(get_save_file_name, return_value=(f"{main_window.default_path.joinpath(file)}", "csv (*.csv"))
     main_window.gui_structure.filename.button.click()
-    assert main_window.gui_structure.filename.get_value() == file.replace("\\", "/")
-    assert main_window.gui_structure.filename.check_linked_value(file.replace("\\", "/"))
+    assert main_window.gui_structure.filename.get_value() == file
+    assert main_window.gui_structure.filename.check_linked_value(file)
     main_window.delete_backup()
```

### Comparing `ScenarioGUI-0.1.3/tests/test_gui_structure_elements/test_flexible_amount_option.py` & `ScenarioGUI-0.2.0/tests/test_gui_structure_elements/test_flexible_amount_option.py`

 * *Files identical despite different names*

### Comparing `ScenarioGUI-0.1.3/tests/test_gui_structure_elements/test_float_box.py` & `ScenarioGUI-0.2.0/tests/test_gui_structure_elements/test_float_box.py`

 * *Files identical despite different names*

### Comparing `ScenarioGUI-0.1.3/tests/test_gui_structure_elements/test_function_button.py` & `ScenarioGUI-0.2.0/tests/test_gui_structure_elements/test_function_button.py`

 * *Files identical despite different names*

### Comparing `ScenarioGUI-0.1.3/tests/test_gui_structure_elements/test_int_box.py` & `ScenarioGUI-0.2.0/tests/test_gui_structure_elements/test_int_box.py`

 * *Files identical despite different names*

### Comparing `ScenarioGUI-0.1.3/tests/test_gui_structure_elements/test_list_box.py` & `ScenarioGUI-0.2.0/tests/test_gui_structure_elements/test_list_box.py`

 * *Files identical despite different names*

### Comparing `ScenarioGUI-0.1.3/tests/test_gui_structure_elements/test_page.py` & `ScenarioGUI-0.2.0/tests/test_gui_structure_elements/test_results_figure.py`

 * *Files 20% similar despite different names*

```diff
@@ -2,22 +2,25 @@
 
 from ScenarioGUI.gui_classes.gui_combine_window import MainWindow
 from tests.gui_structure_for_tests import GUI
 from tests.result_creating_class_for_tests import ResultsClass, data_2_results
 from tests.test_translations.translation_class import Translations
 
 
-def test_page(qtbot):
+def test_results_figure(qtbot):
     # init gui window
     main_window = MainWindow(QtW.QMainWindow(), qtbot, GUI, Translations, result_creating_class=ResultsClass, data_2_results_function=data_2_results)
     main_window.delete_backup()
     main_window = MainWindow(QtW.QMainWindow(), qtbot, GUI, Translations, result_creating_class=ResultsClass, data_2_results_function=data_2_results)
-
-    main_window.gui_structure.page_result.set_text("button name,Name")
-    assert main_window.gui_structure.page_result.button.text() == "button name"
-    assert main_window.gui_structure.page_result.label.text() == "Name"
-
-    # test linked function which counts the counter every time button is clicked
-    assert main_window.gui_structure.counter == 1
-    main_window.gui_structure.page_inputs.button.click()
-    assert main_window.gui_structure.counter == 2
+    # get sum
+    main_window.gui_structure.figure_results.set_text("Hello,Y-Values,X-Values")
+    # calc sum from gui
+    main_window.save_scenario()
+    main_window.start_current_scenario_calculation(False)
+    with qtbot.waitSignal(main_window.threads[0].any_signal, raising=False):
+        QtW.QApplication.processEvents()
+    assert main_window.list_ds[main_window.list_widget_scenario.currentRow()].results is not None
+    # check text output
+    assert main_window.gui_structure.figure_results.label.text() == "Hello"
+    assert main_window.gui_structure.figure_results.a_x.get_ylabel() == "Y-Values"
+    assert main_window.gui_structure.figure_results.a_x.get_xlabel() == "X-Values"
     main_window.delete_backup()
```

### Comparing `ScenarioGUI-0.1.3/tests/test_gui_structure_elements/test_repr.py` & `ScenarioGUI-0.2.0/tests/test_gui_structure_elements/test_repr.py`

 * *Files identical despite different names*

### Comparing `ScenarioGUI-0.1.3/tests/test_gui_structure_elements/test_result_export.py` & `ScenarioGUI-0.2.0/tests/test_gui_structure_elements/test_result_export.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,41 +1,45 @@
 import os
+from functools import partial
 from pathlib import Path
-import PySide6.QtCore as QtC
 
 import PySide6.QtWidgets as QtW
-import keyboard
-
 from ScenarioGUI.gui_classes.gui_combine_window import MainWindow
+
 from tests.gui_structure_for_tests import GUI
 from tests.result_creating_class_for_tests import ResultsClass, data_2_results
 from tests.test_translations.translation_class import Translations
 
 
 def test_results_export(qtbot):
     # init gui window
     main_window = MainWindow(QtW.QMainWindow(), qtbot, GUI, Translations, result_creating_class=ResultsClass, data_2_results_function=data_2_results)
     main_window.delete_backup()
     main_window = MainWindow(QtW.QMainWindow(), qtbot, GUI, Translations, result_creating_class=ResultsClass, data_2_results_function=data_2_results)
-    # get sum
     main_window.save_scenario()
     main_window.start_current_scenario_calculation(False)
     with qtbot.waitSignal(main_window.threads[0].any_signal, raising=False):
         QtW.QApplication.processEvents()
     folder = Path(__file__).parent.parent
     file = f'{folder.joinpath("./test_export.txt")}'
     # delete files if they already exists
     if os.path.exists(main_window.default_path.joinpath(file)):  # pragma: no cover
         os.remove(main_window.default_path.joinpath(file))
-    QtC.QTimer.singleShot(1000, lambda: keyboard.write(file))
-    QtC.QTimer.singleShot(1500, lambda: keyboard.press("enter"))
+
+    def get_save_file_name(*args, **kwargs):
+        """getSaveFileName proxy"""
+        return kwargs["return_value"]
+
+    QtW.QFileDialog.getSaveFileName = partial(get_save_file_name, return_value=(f"{file}", f"{main_window.filename_default[1]}"))
     main_window.gui_structure.export_results.button.click()
     with open(file) as f:
         data = f.read()
 
     assert data == f"result: {main_window.list_ds[main_window.list_widget_scenario.currentRow()].results.result}"
 
     # test set text
     main_window.gui_structure.export_results.set_text("Hello,Set")
     assert main_window.gui_structure.export_results.button.text() == "Hello"
     assert main_window.gui_structure.export_results.caption == "Set"
+
+    os.remove(main_window.default_path.joinpath(file))
     main_window.delete_backup()
```

### Comparing `ScenarioGUI-0.1.3/tests/test_gui_structure_elements/test_results_figure.py` & `ScenarioGUI-0.2.0/tests/test_gui_structure_elements/test_results_text.py`

 * *Files 17% similar despite different names*

```diff
@@ -2,25 +2,24 @@
 
 from ScenarioGUI.gui_classes.gui_combine_window import MainWindow
 from tests.gui_structure_for_tests import GUI
 from tests.result_creating_class_for_tests import ResultsClass, data_2_results
 from tests.test_translations.translation_class import Translations
 
 
-def test_results_figure(qtbot):
+def test_results_text(qtbot):
     # init gui window
     main_window = MainWindow(QtW.QMainWindow(), qtbot, GUI, Translations, result_creating_class=ResultsClass, data_2_results_function=data_2_results)
     main_window.delete_backup()
     main_window = MainWindow(QtW.QMainWindow(), qtbot, GUI, Translations, result_creating_class=ResultsClass, data_2_results_function=data_2_results)
     # get sum
-    main_window.gui_structure.figure_results.set_text("Hello,Y-Values,X-Values")
+    sum_ab = main_window.gui_structure.int_a.get_value() + main_window.gui_structure.float_b.get_value()
+    main_window.gui_structure.result_text_add.set_text("Hello,kW")
     # calc sum from gui
     main_window.save_scenario()
     main_window.start_current_scenario_calculation(False)
     with qtbot.waitSignal(main_window.threads[0].any_signal, raising=False):
         QtW.QApplication.processEvents()
     assert main_window.list_ds[main_window.list_widget_scenario.currentRow()].results is not None
     # check text output
-    assert main_window.gui_structure.figure_results.label.text() == "Hello"
-    assert main_window.gui_structure.figure_results.a_x.get_ylabel() == "Y-Values"
-    assert main_window.gui_structure.figure_results.a_x.get_xlabel() == "X-Values"
+    assert main_window.gui_structure.result_text_add.label.text() == f"Hello{sum_ab}kW"
     main_window.delete_backup()
```

### Comparing `ScenarioGUI-0.1.3/tests/test_gui_structure_elements/test_results_text.py` & `ScenarioGUI-0.2.0/tests/test_main_window_functions/test_no_file.py`

 * *Files 22% similar despite different names*

```diff
@@ -1,25 +1,30 @@
 import PySide6.QtWidgets as QtW
 
 from ScenarioGUI.gui_classes.gui_combine_window import MainWindow
-from tests.gui_structure_for_tests import GUI
-from tests.result_creating_class_for_tests import ResultsClass, data_2_results
-from tests.test_translations.translation_class import Translations
 
+from ..gui_structure_for_tests import GUI
+from ..result_creating_class_for_tests import ResultsClass, data_2_results
+from ..test_translations.translation_class import Translations
+
+
+def test_no_load_save_file(qtbot):
+    """
+    test if the GUI handles wrong load and save inputs correctly
+
+    Parameters
+    ----------
+    qtbot: qtbot
+        bot for the GUI
+    """
 
-def test_results_text(qtbot):
     # init gui window
     main_window = MainWindow(QtW.QMainWindow(), qtbot, GUI, Translations, result_creating_class=ResultsClass, data_2_results_function=data_2_results)
     main_window.delete_backup()
     main_window = MainWindow(QtW.QMainWindow(), qtbot, GUI, Translations, result_creating_class=ResultsClass, data_2_results_function=data_2_results)
-    # get sum
-    sum_ab = main_window.gui_structure.int_a.get_value() + main_window.gui_structure.float_b.get_value()
-    main_window.gui_structure.result_text_add.set_text("Hello,kW")
-    # calc sum from gui
-    main_window.save_scenario()
-    main_window.start_current_scenario_calculation(False)
-    with qtbot.waitSignal(main_window.threads[0].any_signal, raising=False):
-        QtW.QApplication.processEvents()
-    assert main_window.list_ds[main_window.list_widget_scenario.currentRow()].results is not None
-    # check text output
-    assert main_window.gui_structure.result_text_add.label.text() == f"Hello{sum_ab}kW"
+    # check if an import error has been raises with a wrong load file
+    main_window._load_from_data("not_there.GHEtool")
+    assert main_window.status_bar.widget.currentMessage() == main_window.translations.no_file_selected[0]
+    # check if the current error message is shown with a wrong save file/folder
+    main_window._save_to_data("hello/not_there.GHEtool")
+    assert main_window.status_bar.widget.currentMessage() == main_window.translations.no_file_selected[main_window.gui_structure.option_language.get_value()[0]]
     main_window.delete_backup()
```

### Comparing `ScenarioGUI-0.1.3/tests/test_gui_structure_elements/test_text_box.py` & `ScenarioGUI-0.2.0/tests/test_gui_structure_elements/test_text_box.py`

 * *Files identical despite different names*

### Comparing `ScenarioGUI-0.1.3/tests/test_main_window_functions/test_auto_save.py` & `ScenarioGUI-0.2.0/tests/test_main_window_functions/test_auto_save.py`

 * *Files identical despite different names*

### Comparing `ScenarioGUI-0.1.3/tests/test_main_window_functions/test_backup.py` & `ScenarioGUI-0.2.0/tests/test_main_window_functions/test_backup.py`

 * *Files identical despite different names*

### Comparing `ScenarioGUI-0.1.3/tests/test_main_window_functions/test_close.py` & `ScenarioGUI-0.2.0/tests/test_main_window_functions/test_close.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,13 +1,12 @@
 import os
+from functools import partial
 
-import keyboard
 import PySide6.QtCore as QtC
 import PySide6.QtWidgets as QtW
-
 import ScenarioGUI.global_settings as globs
 from ScenarioGUI.gui_classes.gui_combine_window import MainWindow
 
 from ..gui_structure_for_tests import GUI
 from ..result_creating_class_for_tests import ResultsClass, data_2_results
 from ..test_translations.translation_class import Translations
 
@@ -65,14 +64,18 @@
     QtC.QTimer.singleShot(250, close)
     main_window.close()
 
     QtC.QTimer.singleShot(250, cancel)
     main_window.close()
 
     QtC.QTimer.singleShot(250, save)
-    QtC.QTimer.singleShot(300, lambda: keyboard.write(filename_1))
-    QtC.QTimer.singleShot(500, lambda: keyboard.press("enter"))
+    
+    def get_save_file_name(*args, **kwargs):
+        """getSaveFileName proxy"""
+        return kwargs["return_value"]
+    
+    QtW.QFileDialog.getSaveFileName = partial(get_save_file_name, return_value=(f"{filename_1}", f"{main_window.filename_default[1]}"))
     main_window.close()
 
     QtC.QTimer.singleShot(250, exit_window)
     main_window.close()
     main_window.delete_backup()
```

### Comparing `ScenarioGUI-0.1.3/tests/test_main_window_functions/test_datastorage.py` & `ScenarioGUI-0.2.0/tests/test_main_window_functions/test_datastorage.py`

 * *Files identical despite different names*

### Comparing `ScenarioGUI-0.1.3/tests/test_main_window_functions/test_double_naming.py` & `ScenarioGUI-0.2.0/tests/test_main_window_functions/test_double_naming.py`

 * *Files identical despite different names*

### Comparing `ScenarioGUI-0.1.3/tests/test_main_window_functions/test_global_settings.py` & `ScenarioGUI-0.2.0/tests/test_main_window_functions/test_global_settings.py`

 * *Files 26% similar despite different names*

```diff
@@ -1,49 +1,53 @@
 from pathlib import Path
+from platform import system
 
 import PySide6.QtWidgets as QtW
 from pytest import raises
-
+from ScenarioGUI import global_settings as globs
+from ScenarioGUI.global_settings import load
 from ScenarioGUI.gui_classes.gui_combine_window import MainWindow
 
 from ..gui_structure_for_tests import GUI
 from ..result_creating_class_for_tests import ResultsClass, data_2_results
 from ..test_translations.translation_class import Translations
-from ScenarioGUI import global_settings as globs
 
 
 def test_global_settings(qtbot):
     """
     test if two scenarios can have the same name.
 
     Parameters
     ----------
     qtbot: qtbot
         bot for the GUI
     """
     # init gui window
+    load(Path(".").absolute().joinpath("./tests/gui_config.ini") if Path(".").absolute().joinpath("./tests/gui_config.ini").exists() else Path(
+        "..").absolute().joinpath("./tests/gui_config.ini"))
     main_window = MainWindow(QtW.QMainWindow(), qtbot, GUI, Translations, result_creating_class=ResultsClass, data_2_results_function=data_2_results)
     main_window.delete_backup()
     main_window = MainWindow(QtW.QMainWindow(), qtbot, GUI, Translations, result_creating_class=ResultsClass, data_2_results_function=data_2_results)
-    assert main_window.dia.font().family() == globs.FONT == "Arial"
-    assert main_window.dia.font().pointSize() == 10 == globs.FONT_SIZE
+    assert main_window.dia.font().family() == globs.FONT == ("Arial" if system() == "Windows" else 'Helvetica')
+    assert main_window.dia.font().pointSize() == (10 if system() == "Windows" else 14) == globs.FONT_SIZE
 
     assert globs.WHITE == "rgb(255, 255, 255)"
     assert globs.LIGHT == "rgb(84, 188, 235)"
     assert globs.LIGHT_SELECT == "rgb(42, 126, 179)"
     assert globs.DARK == "rgb(0, 64, 122)"
     assert globs.GREY == "rgb(100, 100, 100)"
     assert globs.WARNING == "rgb(255, 200, 87)"
     assert globs.BLACK == "rgb(0, 0, 0)"
 
     assert globs.FILE_EXTENSION == "scenario"
     assert globs.GUI_NAME == "Scenario GUI"
     assert globs.ICON_NAME == "icon.svg"
-
-    assert globs.path.joinpath("./ScenarioGUI") == globs.FOLDER
+    print(globs.path.joinpath(".").parent if "tests" in f"{Path('.').absolute()}" else globs.path.joinpath("."), globs.FOLDER)
+    assert globs.path.joinpath(".").parent if "tests" in f"{Path('.').absolute()}" else globs.path.joinpath(".") == globs.FOLDER
     # test get_path_for_file function
-    assert globs.path == globs.get_path_for_file(globs.path.joinpath("./ScenarioGUI/gui_classes/gui_structure_classes"), "gui_config.ini")
+    assert globs.get_path_for_file(globs.path.joinpath("./ScenarioGUI/gui_classes/gui_structure_classes"), "gui_config.ini")  in [globs.path.parent.joinpath(
+        "." if "tests" in f"{Path('.').absolute()}" else "./examples"), globs.path.parent.joinpath("." if "tests" in f"{Path('.').absolute()}" else "./tests")]
     # test file not found error
     with raises(FileNotFoundError):
         assert globs.path == globs.get_path_for_file(globs.path.joinpath("./ScenarioGUI/gui_classes/gui_structure_classes"), "not_exists.ini")
 
     main_window.delete_backup()
```

### Comparing `ScenarioGUI-0.1.3/tests/test_main_window_functions/test_move_scenario.py` & `ScenarioGUI-0.2.0/tests/test_main_window_functions/test_move_scenario.py`

 * *Files identical despite different names*

### Comparing `ScenarioGUI-0.1.3/tests/test_main_window_functions/test_new_save_load.py` & `ScenarioGUI-0.2.0/tests/test_main_window_functions/test_new_save_load.py`

 * *Files 17% similar despite different names*

```diff
@@ -1,15 +1,13 @@
 import os
+from functools import partial
 from pathlib import Path
 
-import keyboard
 import numpy as np
-import PySide6.QtCore as QtC
 import PySide6.QtWidgets as QtW
-
 import ScenarioGUI.global_settings as global_vars
 from ScenarioGUI.gui_classes.gui_combine_window import MainWindow
 
 from ..gui_structure_for_tests import GUI
 from ..result_creating_class_for_tests import ResultsClass, data_2_results
 from ..test_translations.translation_class import Translations
 
@@ -45,20 +43,25 @@
     if os.path.exists(main_window.default_path.joinpath(filename_1)):  # pragma: no cover
         os.remove(main_window.default_path.joinpath(filename_1))
     if os.path.exists(main_window.default_path.joinpath(filename_2)):  # pragma: no cover
         os.remove(main_window.default_path.joinpath(filename_2))
     if os.path.exists(main_window.default_path.joinpath(filename_3)):  # pragma: no cover
         os.remove(main_window.default_path.joinpath(filename_3))
     # trigger save action and add filename
-    QtC.QTimer.singleShot(100, lambda: keyboard.press("Esc"))
+    
+    def get_save_file_name(*args, **kwargs):
+        """getSaveFileName proxy"""
+        return kwargs["return_value"]
+    
+    QtW.QFileDialog.getSaveFileName = partial(get_save_file_name, return_value=(f"{main_window.filename_default[0]}", f"{main_window.filename_default[1]}"))
     main_window.action_save.trigger()
     assert (Path(main_window.filename[0]), main_window.filename[1]) == (Path(main_window.filename_default[0]), main_window.filename_default[1])
     # trigger save action and add filename
-    QtC.QTimer.singleShot(1000, lambda: keyboard.write(filename_1))
-    QtC.QTimer.singleShot(1200, lambda: keyboard.press("enter"))
+
+    QtW.QFileDialog.getSaveFileName = partial(get_save_file_name, return_value=(f"{main_window.default_path.joinpath(filename_1)}", f"{global_vars.FILE_EXTENSION} (*.{global_vars.FILE_EXTENSION})"))
     main_window.action_save.trigger()
     # check if filename is set correctly
     assert (Path(main_window.filename[0]), main_window.filename[1]) == (
         main_window.default_path.joinpath(filename_1),
         f"{global_vars.FILE_EXTENSION} (*.{global_vars.FILE_EXTENSION})",
     )
     # check if filename is set correctly
@@ -68,25 +71,25 @@
     )
     # get old list and add a new scenario
     list_old = main_window.list_ds.copy()
     main_window.add_scenario()
     # check that they differ
     assert list_old != main_window.list_ds
     # set a different filename and test save as action
-    QtC.QTimer.singleShot(1000, lambda: keyboard.write(filename_2))
-    QtC.QTimer.singleShot(1200, lambda: keyboard.press("enter"))
+    QtW.QFileDialog.getSaveFileName = partial(get_save_file_name, return_value=(
+    f"{main_window.default_path.joinpath(filename_2)}", f"{global_vars.FILE_EXTENSION} (*.{global_vars.FILE_EXTENSION})"))
     main_window.action_save_as.trigger()
     # check if filename is set correctly
     assert (Path(main_window.filename[0]), main_window.filename[1]) == (
         main_window.default_path.joinpath(filename_2),
         f"{global_vars.FILE_EXTENSION} (*.{global_vars.FILE_EXTENSION})",
     )
     # trigger open function and set filename 1
-    QtC.QTimer.singleShot(1000, lambda: keyboard.write(filename_1))
-    QtC.QTimer.singleShot(1200, lambda: keyboard.press("enter"))
+    QtW.QFileDialog.getOpenFileName = partial(get_save_file_name, return_value=(
+    f"{main_window.default_path.joinpath(filename_1)}", f"{global_vars.FILE_EXTENSION} (*.{global_vars.FILE_EXTENSION})"))
     main_window.action_open.trigger()
     # check if filename is imported correctly and the data storages as well
     assert (Path(main_window.filename[0]), main_window.filename[1]) == (
         main_window.default_path.joinpath(filename_1),
         f"{global_vars.FILE_EXTENSION} (*.{global_vars.FILE_EXTENSION})",
     )
     # check if the imported values are the same
@@ -96,16 +99,16 @@
                 assert np.isclose(getattr(ds_old, option), getattr(ds_new, option))
                 continue
             if isinstance(getattr(ds_old, option), (str, bool)):
                 assert getattr(ds_old, option) == getattr(ds_new, option)
                 continue
 
     # set a different filename and test new action
-    QtC.QTimer.singleShot(1000, lambda: keyboard.write(filename_3))
-    QtC.QTimer.singleShot(1200, lambda: keyboard.press("enter"))
+    QtW.QFileDialog.getSaveFileName = partial(get_save_file_name, return_value=(
+    f"{main_window.default_path.joinpath(filename_3)}", f"{global_vars.FILE_EXTENSION} (*.{global_vars.FILE_EXTENSION})"))
     main_window.action_new.trigger()
     assert (Path(main_window.filename[0]), main_window.filename[1]) == (
         main_window.default_path.joinpath(filename_3),
         f"{global_vars.FILE_EXTENSION} (*.{global_vars.FILE_EXTENSION})",
     )
     assert len(main_window.list_ds) < 1
     main_window.filename = (filename_1, filename_1)
```

### Comparing `ScenarioGUI-0.1.3/tests/test_main_window_functions/test_no_file.py` & `ScenarioGUI-0.2.0/tests/test_gui_structure_elements/test_aim.py`

 * *Files 22% similar despite different names*

```diff
@@ -3,28 +3,25 @@
 from ScenarioGUI.gui_classes.gui_combine_window import MainWindow
 
 from ..gui_structure_for_tests import GUI
 from ..result_creating_class_for_tests import ResultsClass, data_2_results
 from ..test_translations.translation_class import Translations
 
 
-def test_no_load_save_file(qtbot):
+def test_aim(qtbot):
     """
-    test if the GUI handles wrong load and save inputs correctly
+    test float box functions
 
     Parameters
     ----------
     qtbot: qtbot
         bot for the GUI
     """
-
-    # init gui window
-    main_window = MainWindow(QtW.QMainWindow(), qtbot, GUI, Translations, result_creating_class=ResultsClass, data_2_results_function=data_2_results)
-    main_window.delete_backup()
     main_window = MainWindow(QtW.QMainWindow(), qtbot, GUI, Translations, result_creating_class=ResultsClass, data_2_results_function=data_2_results)
-    # check if an import error has been raises with a wrong load file
-    main_window._load_from_data("not_there.GHEtool")
-    assert main_window.status_bar.widget.currentMessage() == main_window.translations.no_file_selected[0]
-    # check if the current error message is shown with a wrong save file/folder
-    main_window._save_to_data("hello/not_there.GHEtool")
-    assert main_window.status_bar.widget.currentMessage() == main_window.translations.no_file_selected[main_window.gui_structure.option_language.get_value()[0]]
-    main_window.delete_backup()
+    if not main_window.gui_structure.aim_plot.widget.isChecked():
+        main_window.gui_structure.aim_plot.widget.click()
+
+    assert main_window.gui_structure.aim_plot.widget.isChecked()
+
+    main_window.gui_structure.aim_plot.set_text("Hello")
+    assert main_window.gui_structure.aim_plot.widget.text() == "Hello"
+
```

### Comparing `ScenarioGUI-0.1.3/tests/test_main_window_functions/test_push_button_change.py` & `ScenarioGUI-0.2.0/tests/test_main_window_functions/test_push_button_change.py`

 * *Files identical despite different names*

### Comparing `ScenarioGUI-0.1.3/tests/test_main_window_functions/test_rename_scenario.py` & `ScenarioGUI-0.2.0/tests/test_main_window_functions/test_rename_scenario.py`

 * *Files identical despite different names*

### Comparing `ScenarioGUI-0.1.3/tests/test_main_window_functions/test_run.py` & `ScenarioGUI-0.2.0/tests/test_main_window_functions/test_run.py`

 * *Files identical despite different names*

### Comparing `ScenarioGUI-0.1.3/tests/test_main_window_functions/test_scenario_change.py` & `ScenarioGUI-0.2.0/tests/test_main_window_functions/test_scenario_change.py`

 * *Files identical despite different names*

### Comparing `ScenarioGUI-0.1.3/tests/test_main_window_functions/test_scenario_properties.py` & `ScenarioGUI-0.2.0/tests/test_main_window_functions/test_scenario_properties.py`

 * *Files identical despite different names*

### Comparing `ScenarioGUI-0.1.3/tests/test_main_window_functions/test_toggle_buttons.py` & `ScenarioGUI-0.2.0/tests/test_main_window_functions/test_toggle_buttons.py`

 * *Files identical despite different names*

### Comparing `ScenarioGUI-0.1.3/tests/test_translations/test_language_change.py` & `ScenarioGUI-0.2.0/tests/test_translations/test_language_change.py`

 * *Files identical despite different names*

### Comparing `ScenarioGUI-0.1.3/tests/test_translations/test_translation_csv_2_py.py` & `ScenarioGUI-0.2.0/tests/test_translations/test_translation_csv_2_py.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,17 +1,17 @@
 from pathlib import Path
 
 import pandas as pd
-
 from ScenarioGUI.translation_csv_to_py import translate_csv_2_class
 
 
 def test_csv_2_py():
     folder: Path = Path(__file__).parent
     translate_csv_2_class(folder.joinpath("Translations.csv"), folder)
     d_f = pd.read_csv(folder.joinpath("Translations.csv"), sep=";")
     from .translation_class import Translations
 
     translation = Translations()
     for name, trans_1, trans_2 in zip(d_f["name"], d_f["English"], d_f["German"]):
         assert getattr(translation, name)[0] == trans_1
         assert getattr(translation, name)[1] == trans_2
+
```

### Comparing `ScenarioGUI-0.1.3/tests/test_translations/translation_class.py` & `ScenarioGUI-0.2.0/tests/test_translations/translation_class.py`

 * *Files 2% similar despite different names*

```diff
@@ -62,14 +62,16 @@
         "cat_no_results",
         "text_no_result",
         "category_save_scenario",
         "option_auto_saving",
         "hint_saving",
         "aim_add",
         "aim_sub",
+        "float_b",
+        "function_button",
         "languages",
     )
 
     def __init__(self):
         self.languages: list[str] = ["English", "German"]
         self.action_add_scenario: list[str] = ["Add scenario", "Szenario hinzufügen"]
         self.action_delete_scenario: list[str] = ["Delete scenario", "Szenario löschen"]
@@ -145,7 +147,9 @@
         self.option_auto_saving: list[str] = ["Use automatic saving?, no , yes ", "Automatisches speichern nutzen?, Nein, Ja"]
         self.hint_saving: list[str] = [
             "If Auto saving is selected the scenario will automatically saved if a scenario is changed. Otherwise the scenario has to be saved with the Update scenario button in the upper left corner if the changes should not be lost.",
             "Wenn Automatisch speichern ausgewählt ist, wird das Szenario automatisch gespeichert, wenn ein Szenario geändert wird. Andernfalls muss das Szenario mit der Schaltfläche Szenario aktualisieren in der oberen linken Ecke gespeichert werden, wenn die Änderungen nicht verloren gehen sollen.",
         ]
         self.aim_add: list[str] = ["Adding", "Addieren"]
         self.aim_sub: list[str] = ["Substract", "Subtrahieren"]
+        self.float_b: list[str] = ["nothing", "nothing"]
+        self.function_button: list[str] = ["call function", "Rufe Funktion"]
```

